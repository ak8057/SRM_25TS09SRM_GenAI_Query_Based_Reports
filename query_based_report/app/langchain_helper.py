from __future__ import annotations
import os, time, json, re
from dotenv import load_dotenv
from app.services import db as dbsvc
from .services import vector as vsvc
from .services.llm import build_few_shot_selector, make_sql_chain
from .services.guards import allow_only_select, block_dml_ddl, sanitize
from .services.renderer import rows_to_df
from .services.utils import db_key_from_name, QueryLog
from .state import log_query
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

SEED_PATH = os.path.join(os.path.dirname(__file__), "seeds", "few_shots.json")

# ✅ Seed initial few-shot examples into Chroma memory
def ensure_seeded(db_name: str):
    key = db_key_from_name(db_name)
    vsvc.seed_examples(key, SEED_PATH)

# ✅ Build a Gemini-based SQL chain for a given DB
def build_chain(db_name: str):
    ensure_seeded(db_name)
    table_info = dbsvc.fetch_table_info(db_name)
    key = db_key_from_name(db_name)

    # fetch few relevant NL→SQL examples from Chroma
    examples = vsvc.search_examples(key, question="inventory t-shirts revenue", k=4)
    fs_prompt = build_few_shot_selector(k=4, examples=examples)

    chain = make_sql_chain(dbsvc.get_engine(db_name), fs_prompt)
    return chain, table_info

# ✅ Main logic: Question → SQL → Execute → NL Answer
def answer_question(db_name: str, question: str):
    try:
        chain, table_info = build_chain(db_name)
        start = time.time()

        # --- STEP 1: Ask Gemini to generate SQL ---
        llm_out = chain.invoke({
            "input": question,
            "table_info": table_info,
            "top_k": 50
        })
        llm_output_text = str(llm_out).strip()

        # Extract SQL cleanly using regex (Gemini sometimes adds extra lines)
        match = re.search(r"SELECT[\s\S]*?(?:;|$)", llm_output_text)
        sql = match.group(0).strip() if match else llm_output_text.split("SQLQuery:")[-1].strip()

        # Sanitize & guard
        sql = sanitize(sql)
        allow_only_select(sql)
        block_dml_ddl(sql)

        # --- STEP 2: Execute SQL safely ---
        cols, rows = dbsvc.run_safe_select(db_name, sql)

        # --- STEP 3: Generate natural language answer ---
        sql_result_preview = rows[:10]
        filled_prompt = f"Question: {question}\nSQLQuery: {sql}\nSQLResult: {sql_result_preview}\nAnswer:"

        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.1)
        final_answer = llm.invoke(filled_prompt).content.strip()

        latency_ms = int((time.time() - start) * 1000)

        # --- STEP 4: Log and learn ---
        log_query(QueryLog(
            question=question,
            sql=sql,
            answer=final_answer,
            db_name=db_name,
            latency_ms=latency_ms,
            ok=True
        ))

        # Store successful example for continual learning
        vsvc.upsert_success_example(
            db_key_from_name(db_name),
            vsvc.NL2SQLExample(
                Question=question,
                SQLQuery=sql,
                SQLResult=str(sql_result_preview),
                Answer=final_answer,
                db_key=db_key_from_name(db_name),
            ),
        )

        return sql, cols, rows, final_answer, latency_ms

    except Exception as e:
        print("⚠️ LLM or SQL execution failed:", e)
        raise RuntimeError(f"Failed to answer question: {e}")
