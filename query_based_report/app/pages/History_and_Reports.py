import streamlit as st, time
import pandas as pd
from app.state import list_history



st.title("🧾 Query History & Reports")

db_filter = st.text_input("Filter by DB (optional)")
rows = list_history(db_filter if db_filter else None)

if rows:
    cols = ["timestamp","db","question","sql","answer","ok","latency_ms","error"]
    df = pd.DataFrame(rows, columns=cols)
    df["when"] = df["timestamp"].apply(lambda t: time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t)))
    st.dataframe(df[["when","db","question","sql","answer","ok","latency_ms","error"]], use_container_width=True)
else:
    st.info("No history yet.")
