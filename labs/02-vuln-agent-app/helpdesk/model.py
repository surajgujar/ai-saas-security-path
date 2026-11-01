"""Selects the LLM for the agents, based on LAB_MODEL_BACKEND in labs/.env.

Use it in agent.py:  from .model import build_model   ...   model=build_model()

Backends:
  aistudio  Gemini API key (free tier). ADK reads GOOGLE_API_KEY from the env.
  vertex    Vertex AI. ADK reads GOOGLE_GENAI_USE_VERTEXAI=TRUE + GOOGLE_CLOUD_PROJECT/LOCATION
            and your Application Default Credentials (gcloud auth application-default login).
  claude    Claude via ADK's LiteLlm wrapper (needs `uv add 'google-adk[extensions]'` + ANTHROPIC_API_KEY).

build_model() returns whatever LlmAgent(model=...) accepts: a model-id string for Gemini,
or a LiteLlm object for Claude.
"""
from . import config


def build_model():
    b = config.MODEL_BACKEND
    if b in ("aistudio", "vertex"):
        # Both use a Gemini model id string; ADK picks the transport from the env vars.
        return config.GEMINI_MODEL
    if b == "claude":
        from google.adk.models.lite_llm import LiteLlm  # requires google-adk[extensions] + litellm
        return LiteLlm(model=config.CLAUDE_MODEL)
    raise SystemExit(f"Unknown LAB_MODEL_BACKEND={b!r}. Use aistudio, vertex or claude.")
