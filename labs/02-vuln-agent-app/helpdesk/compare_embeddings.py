"""Compare retrieval: Chroma's local embeddings vs Gemini embeddings (lab 2 stretch).

    uv run python -m helpdesk.compare_embeddings            # index both, then compare
    uv run python -m helpdesk.compare_embeddings --no-index # reuse existing indexes

Prints the top 3 docs for each query from both backends. Distance is backend-specific
(different models, different scales), so compare the ranking, not the raw numbers.
"""
import sys

from .rag import ingest, search

# Mix of easy keyword matches and paraphrases with no shared words, where embeddings differ most.
QUERIES = [
    "How do I fix VPN error 812?",
    "my laptop can't reach anything on the corporate network from home",
    "I got a new phone, how do I move my authenticator?",
    "someone tricked me into typing my password on a fake site",
    "how much do people at my level get paid?",
    "Wi-Fi keeps dropping",
    "a new starter joins Monday, what do they need?",
]


def main() -> None:
    if "--no-index" not in sys.argv:
        for b in ("chroma", "gemini"):
            print(f"Indexing with {b}: {ingest(b)} docs")
        print()

    for q in QUERIES:
        print(f"Q: {q}")
        results = {b: search(q, k=3, backend=b) for b in ("chroma", "gemini")}
        for i in range(3):
            row = []
            for b in ("chroma", "gemini"):
                h = results[b][i]
                mark = " [CONFIDENTIAL]" if h["classification"] != "internal" else ""
                row.append(f"{h['source']} ({h['distance']}){mark}")
            print(f"  {i + 1}. chroma: {row[0]:<45} gemini: {row[1]}")
        print()


if __name__ == "__main__":
    main()
