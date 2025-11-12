import re

def allow_only_select(sql: str) -> None:
    s = sql.strip().lower()
    if not s.startswith("select"):
        raise ValueError("Only SELECT queries are allowed.")

FORBIDDEN = ["insert ", "update ", "delete ", "drop ", "truncate ", "alter ", "create "]

def block_dml_ddl(sql: str) -> None:
    s = sql.lower()
    if any(tok in s for tok in FORBIDDEN):
        raise ValueError("Blocked potentially destructive SQL.")

def sanitize(sql: str) -> str:
    # one-line, strip trailing semicolon; we don’t interpolate user values anyway
    return sql.replace("\n", " ").strip().rstrip(";")
