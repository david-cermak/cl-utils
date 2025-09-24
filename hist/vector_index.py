#!/usr/bin/env python3
import sys, os, pickle
import numpy as np
from sentence_transformers import SentenceTransformer

DB_PATH = os.path.expanduser("~/.local/share/semantic_history.pkl")
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

# lightweight, fast model
model = SentenceTransformer("all-MiniLM-L6-v2")

def load_db():
    if os.path.exists(DB_PATH):
        with open(DB_PATH, "rb") as f:
            return pickle.load(f)
    return {"cmds": [], "embeddings": None}

def save_db(db):
    with open(DB_PATH, "wb") as f:
        pickle.dump(db, f)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(0)
    cmd = sys.argv[1].strip()
    if not cmd:
        sys.exit(0)

    db = load_db()
    emb = model.encode([cmd])

    if db["embeddings"] is None:
        db["embeddings"] = emb
    else:
        db["embeddings"] = np.vstack([db["embeddings"], emb])
    db["cmds"].append(cmd)

    save_db(db)

