import os
import re
import time
from typing import List, Dict
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import FewShotPromptTemplate, PromptTemplate
from langchain_experimental.sql import SQLDatabaseChain
from langchain_community.utilities.sql_database import SQLDatabase

load_dotenv()

# ✅ Create Gemini LLM
def make_llm():
    return ChatGoogleGenerativeAI(
        model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"),
        google_api_key=os.environ["GOOGLE_API_KEY"],
        temperature=0.1,
    )

# ✅ SQL Prompt enforcing only valid SQL
MYSQL_PROMPT = """
You are a senior MySQL expert.
Given an input question, produce only a syntactically correct MySQL SELECT query that answers it.
Never include explanations, the result, or the final answer.

Rules:
- Output only one line starting with 'SQLQuery:' followed by the query.
- Never include words like 'Answer:' or 'SQLResult:'.
- Use backticks (`) around all identifiers.
- Only use columns and tables listed in `table_info`.
- Use CURDATE() when asked about "today".
- Use LIMIT only if user explicitly mentions it.
- Do not use EXPLAIN or comments.

Example:
Question: How many rows are in the table `t_shirts`?
SQLQuery: SELECT COUNT(*) FROM `t_shirts`;

Now, for the question below, respond in the same format.

Question: {input}
SQLQuery:
"""

# ✅ Few-shot selector (examples come from langchain_helper)
def build_few_shot_selector(k: int, examples: List[Dict]):
    ex_prompt = PromptTemplate(
        input_variables=["Question", "SQLQuery", "SQLResult", "Answer"],
        template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}",
    )
    return FewShotPromptTemplate(
        examples=examples,
        example_prompt=ex_prompt,
        prefix=MYSQL_PROMPT,
        suffix="{table_info}\n\nQuestion: {input}\nSQLQuery:",
        input_variables=["input", "table_info", "top_k"],
    )

# ✅ Build SQL Database chain
def make_sql_chain(db_uri_engine, fewshot_prompt) -> SQLDatabaseChain:
    sql_db = SQLDatabase(engine=db_uri_engine, sample_rows_in_table_info=3)
    llm = make_llm()
    return SQLDatabaseChain.from_llm(
        llm=llm,
        db=sql_db,
        prompt=fewshot_prompt,
        verbose=True,
        return_intermediate_steps=True,
        top_k=50,
    )

# ✅ Smart retry with SQL syntax correction
def execute_with_retry(chain, question):
    start = time.time()
    try:
        result = chain.invoke({"input": question})
        latency_ms = int((time.time() - start) * 1000)
        return result, latency_ms
    except Exception as e:
        print("⚠️ SQL execution failed:", e)

        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
        error_text = str(e)
        match = re.search(r"SELECT[\s\S]*", error_text)
        original_sql = match.group(0) if match else "Unknown SQL"

        correction_prompt = f"""
        You are a MySQL syntax expert.
        The following SQL query failed due to syntax error:
        {original_sql}

        Error message:
        {error_text}

        Fix only the syntax (not the logic) and return ONLY the corrected SQL query.
        """
        corrected_sql = llm.invoke(correction_prompt).content.strip()
        print("💡 Retrying with corrected SQL:", corrected_sql)

        try:
            result = chain.invoke({"input": corrected_sql})
            latency_ms = int((time.time() - start) * 1000)
            return result, latency_ms
        except Exception as e2:
            raise RuntimeError(f"Failed again even after correction: {e2}")
