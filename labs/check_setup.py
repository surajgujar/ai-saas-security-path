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
key = os.getenv("GOOGLE_API_KEY", "")
report(bool(key) and key != "paste-your-key-here", "GOOGLE_API_KEY found in labs/.env" if key and key != "paste-your-key-here" else f"GOOGLE_API_KEY missing: copy .env.example to {env_file} and add your key")

if key and key != "paste-your-key-here":
    model = os.getenv("GEMINI_MODEL", "gemini-flash-latest")
    try:
        from google import genai
        reply = genai.Client(api_key=key).models.generate_content(model=model, contents="Reply with exactly: OK")
        report(True, f'Gemini replied: "{(reply.text or "").strip()}" (model {model})')
    except Exception as e:  # show the API's own message: quota, bad key, unknown model
        report(False, f"Gemini call failed: {str(e)[:200]}")

print("All checks passed." if ok else "Some checks failed: fix them before starting a lab.")
sys.exit(0 if ok else 1)
