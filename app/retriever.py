import chromadb
from pathlib import Path
from app.embeddings import load_embedding_model

BASE_DIR = Path(__file__).resolve().parent.parent
CHROMA_DB_PATH = BASE_DIR / "chroma_db"

embedding_model = load_embedding_model()
chroma_client = chromadb.PersistentClient(path=str(CHROMA_DB_PATH))
collection = chroma_client.get_or_create_collection(name="zepto_collection", metadata={"hnsw:space": "cosine"})


def retrieve(question: str, top_k: int = 3):
    query_embedding = embedding_model.encode(question).tolist()
    results = collection.query(query_embeddings=[query_embedding], n_results=top_k)
    return {
        "documents": results["documents"][0],
        "ids": results["ids"][0],
    }
