"""Call the HTTP MCP server directly, with no agent and no LLM (lab 2 stretch).

    uv run python -m helpdesk.mcp_server --http      # terminal 1
    uv run python -m helpdesk.mcp_direct             # terminal 2

This is what any process on the machine (or the network, if you bind 0.0.0.0) can do.
It skips the agent completely, so checks you add in agent code (Lab 6 guardrails, Lab 7's
before_tool_callback) never run. Authorization has to live in the MCP server too.
"""
import asyncio
import sys

from mcp import Client

from . import config


async def main(user: str) -> None:
    async with Client(config.MCP_URL) as client:
        tools = await client.list_tools()
        print("tools:", [t.name for t in tools.tools])
        print("get_ticket T-1005 ->", (await client.call_tool("get_ticket", {"ticket_id": "T-1005"})).content[0].text)
        print(f"reset_password {user} ->", (await client.call_tool("reset_password", {"user": user})).content[0].text)


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1] if len(sys.argv) > 1 else "carol"))
