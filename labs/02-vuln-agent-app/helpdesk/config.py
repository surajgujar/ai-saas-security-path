"""Shared config. Loads labs/.env (two levels up)."""
import os
from pathlib import Path

from dotenv import load_dotenv

LABS_DIR = Path(__file__).resolve().parents[2]
load_dotenv(LABS_DIR / ".env")

# Which model backend to use. See labs/SETUP.md and helpdesk/model.py.
#   aistudio = Gemini API key (free tier, default)
#   vertex   = Vertex AI via Application Default Credentials (gcloud ADC)
#   claude   = Claude via ADK's LiteLlm wrapper
MODEL_BACKEND = os.getenv("LAB_MODEL_BACKEND", "aistudio").strip().lower()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-flash-latest")      # aistudio + vertex
CLAUDE_MODEL = os.getenv("CLAUDE_MODEL", "anthropic/claude-haiku-5-5")  # litellm format; cheapest Claude

DATA_DIR = Path(__file__).resolve().parents[1] / "data"
CHROMA_DIR = Path(__file__).resolve().parents[1] / ".chroma"


def require_backend() -> None:
    """Fail early with a clear message if the selected backend isn't configured."""
    b = MODEL_BACKEND
    if b == "aistudio":
        if not GOOGLE_API_KEY or GOOGLE_API_KEY == "paste-your-key-here":
            raise SystemExit("LAB_MODEL_BACKEND=aistudio but GOOGLE_API_KEY is missing in labs/.env (see SETUP.md).")
    elif b == "vertex":
        if os.getenv("GOOGLE_GENAI_USE_VERTEXAI", "").upper() != "TRUE" or not os.getenv("GOOGLE_CLOUD_PROJECT"):
            raise SystemExit("LAB_MODEL_BACKEND=vertex needs GOOGLE_GENAI_USE_VERTEXAI=TRUE and GOOGLE_CLOUD_PROJECT in "
                             "labs/.env, plus `gcloud auth application-default login` (see SETUP.md).")
    elif b == "claude":
        if not os.getenv("ANTHROPIC_API_KEY"):
            raise SystemExit("LAB_MODEL_BACKEND=claude needs ANTHROPIC_API_KEY in labs/.env and "
                             "`uv add 'google-adk[extensions]'` (see SETUP.md).")
    else:
        raise SystemExit(f"Unknown LAB_MODEL_BACKEND={b!r}. Use aistudio, vertex or claude.")
