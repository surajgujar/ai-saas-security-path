"""Ask the HelpDesk Copilot one question from the terminal.

    uv run python -m helpdesk.cli "How do I fix VPN error 812?"
    uv run python -m helpdesk.cli --user carol "What are the 2026 salary bands?"

Prints every tool call (including transfer_to_agent, which is the agent-to-agent hop),
then the answer.
"""
import argparse
import asyncio
import json

from .runner import ask


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("message")
    p.add_argument("--user", default="alice", help="who is asking (see data/users.json)")
    a = p.parse_args()

    result = asyncio.run(ask(a.message, a.user))
    for c in result["tool_calls"]:
        print(f"[tool] {c['agent']} -> {c['tool']}({json.dumps(c['args'])[:200]})")
    print("\n" + (result["answer"] or "(no answer)"))


if __name__ == "__main__":
    main()
