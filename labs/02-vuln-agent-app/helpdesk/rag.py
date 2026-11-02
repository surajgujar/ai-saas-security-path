"""RAG over the HelpDesk docs.

Embeddings come from LAB_EMBEDDINGS in labs/.env:
  chroma (default)  Chroma's built-in local model, no API key needed for search
  gemini            a Gemini embedding model, see helpdesk/embeddings.py

Each backend gets its own collection, because their vectors have different sizes
(384 vs 3072) and can't share one index. Re-run ingest after switching.

Ingest is done for you. The retrieval is a TODO: notice that it does NOT filter by the
user's role, which is the vulnerability labs 3/4 exploit and lab 6/7 fix.
"""
import chromadb

from . import config
from .config import CHROMA_DIR, DATA_DIR

BASE_COLLECTION = "helpdesk-docs"


def _client() -> chromadb.ClientAPI:
    return chromadb.PersistentClient(path=str(CHROMA_DIR))


def _backend(backend: str | None) -> str:
    b = (backend or config.EMBEDDINGS).strip().lower()
    if b not in ("chroma", "gemini"):
        raise SystemExit(f"Unknown LAB_EMBEDDINGS={b!r}. Use chroma or gemini.")
    return b


def _collection_name(backend: str) -> str:
    return BASE_COLLECTION if backend == "chroma" else f"{BASE_COLLECTION}-{backend}"


def _embedding_fn(backend: str):
    if backend == "gemini":
        from .embeddings import GeminiEmbeddings

        return GeminiEmbeddings(model=config.GEMINI_EMBED_MODEL)
    return None  # None = Chroma's default local model


def ingest(backend: str | None = None) -> int:
    """Read every data/docs/*.md into Chroma. Returns the number of docs indexed."""
    backend = _backend(backend)
    client = _client()
    name = _collection_name(backend)
    try:
        client.delete_collection(name)
    except Exception:
        pass
    ef = _embedding_fn(backend)
    col = client.create_collection(name, embedding_function=ef) if ef else client.create_collection(name)
    ids, texts, metas = [], [], []
    for path in sorted((DATA_DIR / "docs").glob("*.md")):
        raw = path.read_text(encoding="utf-8")
        classification = "internal"
        for line in raw.splitlines():
            if line.startswith("classification:"):
                classification = line.split(":", 1)[1].strip()
        ids.append(path.stem)
        texts.append(raw)
        metas.append({"source": path.name, "classification": classification})
    col.add(ids=ids, documents=texts, metadatas=metas)
    return len(ids)


def search(query: str, k: int = 3, backend: str | None = None) -> list[dict]:
    """Return the top-k matching documents as [{source, classification, text, distance}].

    TODO(lab 6/7): this returns ANY document, including confidential HR docs, to ANY user.
    That's the bug. For now leave it wide open - labs 3 and 4 need it this way to demo the attack.
    When you harden it, add a `user_role` argument and use Chroma's `where=` filter on
    the "classification" metadata so an engineer never retrieves HR-only documents.
    """
    backend = _backend(backend)
    ef = _embedding_fn(backend)
    name = _collection_name(backend)
    col = _client().get_collection(name, embedding_function=ef) if ef else _client().get_collection(name)
    res = col.query(query_texts=[query], n_results=k)
    out = []
    for doc, meta, dist in zip(res["documents"][0], res["metadatas"][0], res["distances"][0]):
        out.append({"source": meta["source"], "classification": meta["classification"], "text": doc,
                    "distance": round(dist, 3)})
    return out


if __name__ == "__main__":
    b = _backend(None)
    n = ingest(b)
    print(f"Indexed {n} documents into {CHROMA_DIR} (embeddings: {b})")
    for hit in search("how do I fix the VPN", backend=b):
        print(f"  - {hit['source']} ({hit['classification']})")
