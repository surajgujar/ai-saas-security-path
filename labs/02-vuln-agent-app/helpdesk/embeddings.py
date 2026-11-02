"""Gemini embeddings for Chroma (lab 2 stretch).

Chroma's default embeds text locally with a small model (all-MiniLM-L6-v2, 384 dims).
This swaps in a Gemini embedding model via google-genai. It uses the same credentials as
the agents: GOOGLE_API_KEY for aistudio, or ADC when GOOGLE_GENAI_USE_VERTEXAI=TRUE.

Two things a local model can't do:
  - task types: documents are embedded as RETRIEVAL_DOCUMENT and searches as RETRIEVAL_QUERY,
    so the model knows which side is the question and which is the answer.
  - bigger vectors (3072 dims for gemini-embedding-001).

Security note: with this on, every document is sent to Google when you index it, including
the confidential HR docs. That's a new trust boundary for your Lab 3 threat model.
"""
import sys
import time
from typing import Any, Dict

from chromadb.api.types import Documents, EmbeddingFunction, Embeddings, Space
from chromadb.utils.embedding_functions import register_embedding_function
from google import genai
from google.genai import errors, types

BATCH = 50  # stay well under the API's per-request input limit


@register_embedding_function
class GeminiEmbeddings(EmbeddingFunction[Documents]):
    def __init__(self, model: str = "gemini-embedding-001"):
        self.model = model
        self._client = genai.Client()  # reads GOOGLE_API_KEY or the Vertex env vars

    def _embed(self, texts: Documents, task_type: str) -> Embeddings:
        out: list = []
        for i in range(0, len(texts), BATCH):
            chunk = list(texts[i : i + BATCH])
            resp = self._embed_with_backoff(chunk, task_type)
            # Some models (e.g. gemini-embedding-2) merge a list of inputs into ONE vector.
            # Check, so a wrong model fails loudly instead of silently mis-indexing.
            if len(resp.embeddings) != len(chunk):
                raise ValueError(
                    f"{self.model} returned {len(resp.embeddings)} vectors for {len(chunk)} texts. "
                    "Use a text embedding model such as gemini-embedding-001."
                )
            out.extend(e.values for e in resp.embeddings)
        return out

    def _embed_with_backoff(self, chunk: list, task_type: str):
        # Embedding quotas are per minute and low on new projects, so wait and retry on 429.
        for attempt in range(6):
            try:
                return self._client.models.embed_content(
                    model=self.model, contents=chunk, config=types.EmbedContentConfig(task_type=task_type)
                )
            except errors.ClientError as e:
                if e.code != 429 or attempt == 5:
                    raise
                wait = min(5 * 2**attempt, 60)
                print(f"[embeddings] rate limited, retrying in {wait}s", file=sys.stderr)
                time.sleep(wait)

    def __call__(self, input: Documents) -> Embeddings:
        return self._embed(input, "RETRIEVAL_DOCUMENT")

    def embed_query(self, input: Documents) -> Embeddings:
        return self._embed(input, "RETRIEVAL_QUERY")

    # Chroma stores this config with the collection, so it can rebuild the function later.
    @staticmethod
    def name() -> str:
        return "helpdesk_gemini"

    def get_config(self) -> Dict[str, Any]:
        return {"model": self.model}

    @staticmethod
    def build_from_config(config: Dict[str, Any]) -> "GeminiEmbeddings":
        return GeminiEmbeddings(model=config["model"])

    def default_space(self) -> Space:
        return "cosine"  # Gemini embeddings are meant to be compared by cosine similarity
