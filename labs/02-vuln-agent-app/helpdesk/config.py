"""Shared config. Loads labs/.env (two levels up)."""
import os
from pathlib import Path

from dotenv import load_dotenv

LABS_DIR = Path(__file__).resolve().parents[2]
load_dotenv(LABS_DIR / ".env")

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-flash-latest")

DATA_DIR = Path(__file__).resolve().parents[1] / "data"
CHROMA_DIR = Path(__file__).resolve().parents[1] / ".chroma"


def require_key() -> None:
    if not GOOGLE_API_KEY or GOOGLE_API_KEY == "paste-your-key-here":
        raise SystemExit("No GOOGLE_API_KEY. Copy labs/.env.example to labs/.env and add your key (see SETUP.md).")
