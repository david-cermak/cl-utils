#!/usr/bin/env python3
import sys, os, pickle
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

DB_PATH = os.path.expanduser("~/.local/share/semantic_history.pkl")
model = SentenceTransformer("all-MiniLM-L6-v2")

def load_db():
    if not os.path.exists(DB_PATH):
        return {"cmds": [], "embeddings": None}
    with open(DB_PATH, "rb") as f:
        return pickle.load(f)

if __name__ == "__main__":
    query = sys.argv[1] if len(sys.argv) > 1 else ""
    db = load_db()

    if not db["cmds"]:
        sys.exit(0)

    q_emb = model.encode([query])
    index = faiss.IndexFlatL2(q_emb.shape[1])
    index.add(np.array(db["embeddings"]).astype("float32"))
    D, I = index.search(np.array(q_emb).astype("float32"), 20)

    for idx in I[0]:
        print(db["cmds"][idx])

