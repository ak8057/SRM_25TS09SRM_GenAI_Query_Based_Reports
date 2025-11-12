from __future__ import annotations
import os, re
from typing import Optional, Tuple, List
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL, Engine
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv

load_dotenv()

def make_mysql_url(db_name: Optional[str] = None) -> str:
    host = os.getenv("MYSQL_HOST", "localhost")
    port = int(os.getenv("MYSQL_PORT", "3306"))
    user = os.getenv("MYSQL_USER", "root")
    pwd  = os.getenv("MYSQL_PASSWORD", "")
    db   = db_name or os.getenv("MYSQL_DEFAULT_DB", "mysql")
    return URL.create(
        "mysql+pymysql", username=user, password=pwd, host=host, port=port, database=db
    )

def get_engine(db_name: Optional[str] = None) -> Engine:
    return create_engine(make_mysql_url(db_name), pool_pre_ping=True, pool_recycle=300)

def create_database(db_name: str) -> None:
    root_eng = get_engine()
    with root_eng.connect() as conn:
        conn.execute(text(f"CREATE DATABASE IF NOT EXISTS `{db_name}`"))
        conn.commit()

def drop_database(db_name: str) -> None:
    root_eng = get_engine()
    with root_eng.connect() as conn:
        conn.execute(text(f"DROP DATABASE IF EXISTS `{db_name}`"))
        conn.commit()

def run_sql_script(db_name: str, sql_script: str) -> None:
    """Execute a .sql file (schema + inserts). Split on ; carefully ignoring DELIMITER blocks."""
    create_database(db_name)
    eng = get_engine(db_name)
    statements = _split_sql(sql_script)
    with eng.begin() as conn:
        for stmt in statements:
            s = stmt.strip()
            if not s:
                continue
            conn.exec_driver_sql(s)

def _split_sql(sql: str) -> List[str]:
    # simplistic splitter that respects DELIMITER changes (common in dump files)
    lines = sql.splitlines()
    delim = ';'
    acc, stmts = [], []
    for line in lines:
        m = re.match(r'^\s*DELIMITER\s+(.+)\s*$', line, re.I)
        if m:
            delim = m.group(1)
            continue
        acc.append(line)
        if ''.join(acc).rstrip().endswith(delim):
            chunk = ''.join(acc).rsplit(delim, 1)[0]
            stmts.append(chunk)
            acc = []
    if acc:
        stmts.append(''.join(acc))
    return stmts

def fetch_table_info(db_name: str, sample_rows: int = 3) -> str:
    """LangChain-compatible table_info string."""
    from langchain_community.utilities.sql_database import SQLDatabase
    db = SQLDatabase(engine=get_engine(db_name), include_tables=None, sample_rows_in_table_info=sample_rows)
    return db.get_table_info()

def run_safe_select(db_name: str, sql: str, limit_cap: int = 200) -> Tuple[List[str], List[tuple]]:
    """Guards: only SELECT; auto LIMIT; EXPLAIN must succeed."""
    sql_clean = sql.strip().rstrip(';')
    if not re.match(r'(?is)^select\b', sql_clean):
        raise ValueError("Blocked: only SELECT queries are allowed.")
    # add LIMIT cap if none
    if not re.search(r'(?is)\blimit\s+\d+\b', sql_clean):
        sql_clean = f"{sql_clean} LIMIT {limit_cap}"
    eng = get_engine(db_name)
    with eng.connect() as conn:
        # EXPLAIN first
        conn.exec_driver_sql(f"EXPLAIN {sql_clean}")
        result = conn.exec_driver_sql(sql_clean)
        cols = list(result.keys())
        rows = list(result.fetchall())
    return cols, rows
