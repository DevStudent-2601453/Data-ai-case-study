from pathlib import Path
from sentence_transformers import SentenceTransformer
import chromadb


def run_ingest(collection_name: str = "zepto_collection") -> None:
    BASE_DIR = Path(__file__).resolve().parent.parent
    docs_path = BASE_DIR / "docs"

    documents = []
    for file in sorted(docs_path.glob("*.txt")):
        with open(file, "r", encoding="utf-8") as f:
            text = f.read()
        documents.append({"id": file.stem, "text": text})

    ids = [d["id"] for d in documents]
    docs = [d["text"] for d in documents]

    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    embeddings = model.encode(docs, show_progress_bar=False)

    try:
        embeddings = embeddings.tolist()
    except Exception:
        pass

    CHROMA_DB_PATH = BASE_DIR / "chroma_db"
    chroma_client = chromadb.PersistentClient(path=str(CHROMA_DB_PATH))
    collection = chroma_client.get_or_create_collection(name=collection_name)
    collection.add(ids=ids, documents=docs, embeddings=embeddings)

    print(f"Stored {collection.count()} documents in the collection")
    print(f"ChromaDB path: {CHROMA_DB_PATH}")


if __name__ == "__main__":
    run_ingest()
