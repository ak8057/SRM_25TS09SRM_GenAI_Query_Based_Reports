import hashlib, time
from dataclasses import dataclass

def db_key_from_name(db_name: str) -> str:
    return hashlib.sha1(db_name.encode()).hexdigest()[:10]

@dataclass
class QueryLog:
    question: str
    sql: str
    answer: str
    db_name: str
    latency_ms: int
    ok: bool
    error: str = ""
