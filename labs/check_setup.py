"""Checks the shared lab setup (see SETUP.md). Run from labs/:

    uv run --python 3.11 --with google-genai --with python-dotenv python check_setup.py
"""
import os
import shutil
import subprocess
import sys
from pathlib import Path

ok = True


def report(passed: bool, msg: str) -> None:
    global ok
    ok &= passed
    print(("[ok]   " if passed else "[FAIL] ") + msg)


def version(cmd: list[str]) -> str | None:
    if not shutil.which(cmd[0]):
        return None
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        return (out.stdout or out.stderr).strip().splitlines()[0]
    except Exception:
        return None


v = sys.version_info
report(v[:2] == (3, 11), f"Python {v.major}.{v.minor}.{v.micro}" + ("" if v[:2] == (3, 11) else " (expected 3.11, use: uv run --python 3.11 ...)"))

uv = version(["uv", "--version"])
report(bool(uv), uv or "uv not found: see SETUP.md step 1")

docker = version(["docker", "--version"])
compose = version(["docker", "compose", "version"])
report(bool(docker and compose), f"{docker}, {compose}" if docker and compose else "Docker or 'docker compose' v2 missing: see SETUP.md step 3")

node = version(["node", "--version"])
report(bool(node), f"Node {node}" if node else "Node not found: install from https://nodejs.org (LTS)")

env_file = Path(__file__).parent / ".env"
try:
    from dotenv import load_dotenv
    load_dotenv(env_file)
except ImportError:
    pass
backend = os.getenv("LAB_MODEL_BACKEND", "aistudio").strip().lower()
print(f"[info] LAB_MODEL_BACKEND={backend}")

if backend == "aistudio":
    key = os.getenv("GOOGLE_API_KEY", "")
    if not key or key == "paste-your-key-here":
        report(False, f"GOOGLE_API_KEY missing: copy .env.example to {env_file} and add your key")
    else:
        model = os.getenv("GEMINI_MODEL", "gemini-flash-latest")
        try:
            from google import genai
            reply = genai.Client(api_key=key).models.generate_content(model=model, contents="Reply with exactly: OK")
            report(True, f'Gemini (AI Studio) replied: "{(reply.text or "").strip()}" (model {model})')
        except Exception as e:
            report(False, f"Gemini call failed: {str(e)[:200]}")

elif backend == "vertex":
    proj = os.getenv("GOOGLE_CLOUD_PROJECT", "")
    loc = os.getenv("GOOGLE_CLOUD_LOCATION", "us-central1")
    if os.getenv("GOOGLE_GENAI_USE_VERTEXAI", "").upper() != "TRUE" or not proj:
        report(False, "vertex needs GOOGLE_GENAI_USE_VERTEXAI=TRUE and GOOGLE_CLOUD_PROJECT in labs/.env")
    else:
        model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
        try:
            from google import genai
            client = genai.Client(vertexai=True, project=proj, location=loc)  # uses ADC
            reply = client.models.generate_content(model=model, contents="Reply with exactly: OK")
            report(True, f'Vertex AI replied: "{(reply.text or "").strip()}" (model {model}, project {proj})')
        except Exception as e:
            report(False, f"Vertex call failed (did you run `gcloud auth application-default login`?): {str(e)[:200]}")

elif backend == "claude":
    import importlib.util
    key = os.getenv("ANTHROPIC_API_KEY", "")
    if not key:
        report(False, "claude needs ANTHROPIC_API_KEY in labs/.env")
    elif importlib.util.find_spec("litellm") is None:
        report(False, "claude needs litellm: run `uv add 'google-adk[extensions]'` in the lab folder")
    else:
        model = os.getenv("CLAUDE_MODEL", "anthropic/claude-haiku-5-5")
        try:
            import litellm
            reply = litellm.completion(model=model, messages=[{"role": "user", "content": "Reply with exactly: OK"}])
            report(True, f'Claude replied: "{reply.choices[0].message.content.strip()}" (model {model})')
        except Exception as e:
            report(False, f"Claude call failed: {str(e)[:200]}")

else:
    report(False, f"Unknown LAB_MODEL_BACKEND={backend!r}. Use aistudio, vertex or claude.")

print("All checks passed." if ok else "Some checks failed: fix them before starting a lab.")
sys.exit(0 if ok else 1)
