import sqlite3, os, time
from typing import List, Tuple
from dataclasses import asdict
from .services.utils import QueryLog

DB_PATH = "app_meta.sqlite"

def _conn():
    os.makedirs(os.path.dirname(DB_PATH) or ".", exist_ok=True)
    con = sqlite3.connect(DB_PATH)
    con.execute("""
    CREATE TABLE IF NOT EXISTS query_log(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ts INTEGER,
        db_name TEXT,
        question TEXT,
        sql TEXT,
        answer TEXT,
        ok INTEGER,
        latency_ms INTEGER,
        error TEXT
    )""")
    return con

def log_query(q: QueryLog):
    with _conn() as con:
        con.execute(
            "INSERT INTO query_log(ts, db_name, question, sql, answer, ok, latency_ms, error) VALUES(?,?,?,?,?,?,?,?)",
            (int(time.time()), q.db_name, q.question, q.sql, q.answer, 1 if q.ok else 0, q.latency_ms, q.error),
        )

def list_history(db_name: str = None) -> List[Tuple]:
    with _conn() as con:
        if db_name:
            return con.execute("SELECT ts, question, sql, answer, ok, latency_ms, error FROM query_log WHERE db_name=? ORDER BY id DESC", (db_name,)).fetchall()
        return con.execute("SELECT ts, db_name, question, sql, answer, ok, latency_ms, error FROM query_log ORDER BY id DESC").fetchall()
