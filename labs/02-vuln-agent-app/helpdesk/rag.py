"""RAG over the HelpDesk docs using Chroma's built-in embeddings (no API key needed for search).

Ingest is done for you. The retrieval is a TODO: notice that it does NOT filter by the
user's role, which is the vulnerability labs 3/4 exploit and lab 6/7 fix.
"""
import chromadb

from .config import CHROMA_DIR, DATA_DIR

COLLECTION = "helpdesk-docs"


def _client() -> chromadb.ClientAPI:
    return chromadb.PersistentClient(path=str(CHROMA_DIR))


def ingest() -> int:
    """Read every data/docs/*.md into Chroma. Returns the number of docs indexed."""
    client = _client()
    try:
        client.delete_collection(COLLECTION)
    except Exception:
        pass
    col = client.create_collection(COLLECTION)
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


def search(query: str, k: int = 3) -> list[dict]:
    """Return the top-k matching documents as [{source, classification, text}].

    TODO(lab 6/7): this returns ANY document, including confidential HR docs, to ANY user.
    That's the bug. For now leave it wide open - labs 3 and 4 need it this way to demo the attack.
    When you harden it, add a `user_role` argument and use Chroma's `where=` filter on
    the "classification" metadata so an engineer never retrieves HR-only documents.
    """
    col = _client().get_collection(COLLECTION)
    res = col.query(query_texts=[query], n_results=k)
    out = []
    for doc, meta in zip(res["documents"][0], res["metadatas"][0]):
        out.append({"source": meta["source"], "classification": meta["classification"], "text": doc})
    return out


if __name__ == "__main__":
    n = ingest()
    print(f"Indexed {n} documents into {CHROMA_DIR}")
    for hit in search("how do I fix the VPN"):
        print(f"  - {hit['source']} ({hit['classification']})")
