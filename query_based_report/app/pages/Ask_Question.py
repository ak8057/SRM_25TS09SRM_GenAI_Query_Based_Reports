import streamlit as st
import pandas as pd
from app.langchain_helper import get_few_shot_db_chain
from app.services import db as dbsvc
from app.services.renderer import rows_to_df
from app.services.llm import execute_with_retry  # ✅ retry logic wrapper

st.title("🔎 Ask Questions (NL → SQL → Answer)")

# Database input
db_name = st.text_input("Database to use", value=st.session_state.get("active_db", ""))
question = st.text_area(
    "Your question",
    placeholder="e.g., What is the total price of inventory for all S-size t-shirts?",
)

# When user clicks Run
if st.button("Run") and db_name and question.strip():
    with st.spinner("Thinking with Gemini + building SQL + executing..."):
        try:
            # ✅ Build the few-shot SQL chain (from langchain_helper)
            chain = get_few_shot_db_chain(db_name)

            # ✅ Use retry wrapper to handle SQL syntax errors
            result, latency_ms = execute_with_retry(chain, question.strip())

            # Extract generated SQL & results
            intermediate = result.get("intermediate_steps", [])
            if intermediate:
                sql = intermediate[0].get("sql_cmd", "N/A")
                cols = intermediate[0].get("columns", [])
                rows = intermediate[0].get("rows", [])
            else:
                sql, cols, rows = "N/A", [], []

            answer = result.get("result", "No answer returned.")

            # ✅ Display in UI
            st.success(f"✅ Done in {latency_ms} ms")

            with st.expander("🧠 Generated SQL", expanded=True):
                st.code(sql, language="sql")

            df = rows_to_df(cols, rows)
            with st.expander("📄 Result preview"):
                st.dataframe(df)

            st.subheader("🗣 Answer")
            st.write(answer)

        except Exception as e:
            st.error(f"❌ Failed: {e}")

# Handy schema info viewer
if db_name:
    with st.expander("ℹ️ Detected schema & samples"):
        st.text(dbsvc.fetch_table_info(db_name))
