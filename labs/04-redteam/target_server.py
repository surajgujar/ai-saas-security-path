"""Wraps the Lab 2 agent in an HTTP endpoint so promptfoo and garak can attack it.

    POST /ask   {"prompt": "..."}  ->  {"output": "...", "tool_calls": [...]}

Run from labs/04-redteam:
    uv run uvicorn target_server:app --port 8099

It imports the Lab 2 app from ../02-vuln-agent-app. Done for you - the learning is in the
attacks (LAB.md), not in this wiring.
"""
import sys
from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel

# make the Lab 2 package importable
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "02-vuln-agent-app"))
from helpdesk.runner import ask  # noqa: E402

app = FastAPI()


class Q(BaseModel):
    prompt: str
    user: str = "alice"


@app.post("/ask")
async def ask_endpoint(q: Q) -> dict:
    result = await ask(q.prompt, q.user)
    return {"output": result["answer"], "tool_calls": result["tool_calls"]}
