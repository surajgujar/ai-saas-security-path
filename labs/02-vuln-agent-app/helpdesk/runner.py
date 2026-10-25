"""Runs the agent for one message and returns the answer plus every tool call it made.

Used by cli.py (lab 2), the red-team target server (lab 4) and the telemetry lab (lab 11).
Done for you: this is ADK plumbing, not the learning goal.
"""
from google.adk.runners import InMemoryRunner
from google.genai import types

from . import config
from .agent import root_agent

APP_NAME = "helpdesk"


async def ask(message: str, user: str = "alice") -> dict:
    """Send one message as `user`. Returns {"answer": str, "tool_calls": [{agent, tool, args}]}."""
    config.require_key()
    if root_agent is None:
        raise SystemExit("root_agent is None: finish TODO(step 4) and TODO(step 5) in helpdesk/agent.py")

    runner = InMemoryRunner(agent=root_agent, app_name=APP_NAME)
    try:
        session = await runner.session_service.create_session(
            app_name=APP_NAME, user_id=user, state={"user": user}
        )
        content = types.Content(role="user", parts=[types.Part(text=message)])
        calls, answer = [], ""
        async for event in runner.run_async(user_id=user, session_id=session.id, new_message=content):
            for fc in event.get_function_calls():
                calls.append({"agent": event.author, "tool": fc.name, "args": dict(fc.args or {})})
            if event.is_final_response() and event.content and event.content.parts:
                answer = "".join(p.text or "" for p in event.content.parts)
        return {"answer": answer, "tool_calls": calls}
    finally:
        await runner.close()
