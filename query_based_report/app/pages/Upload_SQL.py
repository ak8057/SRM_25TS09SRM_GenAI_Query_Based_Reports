import streamlit as st, time
from services import db as dbsvc

st.title("📤 Upload SQL Dump → MySQL")

uploaded = st.file_uploader("Upload a .sql file (schema + inserts)", type=["sql"])
db_name = st.text_input("New Database Name (alphanumeric + underscore)", value="dataset_" + str(int(time.time())))

if st.button("Create DB & Load SQL", disabled=not uploaded):
    sql_text = uploaded.read().decode("utf-8", errors="ignore")
    try:
        dbsvc.run_sql_script(db_name, sql_text)
        st.success(f"Database `{db_name}` created and loaded.")
        st.session_state["active_db"] = db_name
    except Exception as e:
        st.error(f"Load failed: {e}")

if "active_db" in st.session_state:
    st.info(f"Active database: `{st.session_state['active_db']}`")
