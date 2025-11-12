import os, json, uuid
from typing import List, Dict
from dataclasses import dataclass
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings 
load_dotenv()

CHROMA_DIR = os.getenv("CHROMA_DIR", "./data/chroma")
EMB_MODEL  = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")

@dataclass
class NL2SQLExample:
    Question: str
    SQLQuery: str
    SQLResult: str = ""
    Answer: str = ""
    db_key: str = "global"

def get_embedder():
    return HuggingFaceEmbeddings(model_name=os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2"))

def _vs_path(db_key: str) -> str:
    return os.path.join(CHROMA_DIR, db_key)

def get_vectorstore(db_key: str):
    os.makedirs(_vs_path(db_key), exist_ok=True)
    return Chroma(persist_directory=_vs_path(db_key), embedding_function=get_embedder())

def seed_examples(db_key: str, seed_path: str):
    vs = get_vectorstore(db_key)
    if vs._collection.count() > 0:
        return
    with open(seed_path, "r", encoding="utf-8") as f:
        shots: List[Dict] = json.load(f)
    texts   = [" ".join([ex["Question"], ex["SQLQuery"], ex.get("Answer","")]) for ex in shots]
    metas   = shots
    ids     = [str(uuid.uuid4()) for _ in texts]
    vs.add_texts(texts=texts, metadatas=metas, ids=ids)
    vs.persist()

def search_examples(db_key: str, question: str, k: int = 4) -> List[Dict]:
    vs = get_vectorstore(db_key)
    docs = vs.similarity_search(question, k=k)
    return [d.metadata for d in docs]

def upsert_success_example(db_key: str, ex: NL2SQLExample):
    vs = get_vectorstore(db_key)
    text = " ".join([ex.Question, ex.SQLQuery, ex.Answer])
    vs.add_texts(texts=[text], metadatas=[ex.__dict__], ids=[str(uuid.uuid4())])
    vs.persist()
