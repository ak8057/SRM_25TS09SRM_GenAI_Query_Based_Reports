import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import streamlit as st
st.set_page_config(page_title="GenAI | Query-Based Reports", page_icon="📊", layout="wide")
st.title("GenAI | Query-Based Reports")
st.markdown("Upload a SQL dump, ask natural-language questions, get answers + SQL + result previews.")
st.page_link("pages/Upload_SQL.py", label="Upload SQL", icon="📤")
st.page_link("pages/Ask_Question.py", label="Ask Questions", icon="🔎")
st.page_link("pages/History_and_Reports.py", label="History & Reports", icon="🧾")


