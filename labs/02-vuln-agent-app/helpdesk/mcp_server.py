"""MCP server that exposes get_ticket and reset_password.

This is the "agent -> tool server" hop you threat-model in lab 3 and put authorization on in lab 7.

Two ways to run it (pick with LAB_MCP_TRANSPORT in labs/.env, or --http):

  stdio (default)  the agent launches this as a subprocess and talks over stdin/stdout.
                   To test alone:  uv run python -m helpdesk.mcp_server
                   (it will sit waiting on stdin - that's correct. Ctrl+C to stop.)

  streamable HTTP  run it yourself, like a remote MCP server, then the agent connects by URL:
                   uv run python -m helpdesk.mcp_server --http
                   -> http://127.0.0.1:8765/mcp

IMPORTANT: a stdio MCP server must never print() to stdout - stdout IS the protocol channel.
Log to stderr if you need to debug.

TODO(lab 3/7): over HTTP there is NO authentication. Anything that can reach the port can call
reset_password directly, without going through the agent or any check in agent code. Real remote
MCP servers need OAuth (MCPServer supports token_verifier/auth) and a check on who the caller is.
"""
import sys

from mcp.server import MCPServer

from . import config
from .tools import read_ticket, reset_password as _reset_password

mcp = MCPServer("helpdesk-tools")


@mcp.tool()
def get_ticket(ticket_id: str) -> dict:
    """Look up a support ticket by id, e.g. 'T-1001'."""
    return read_ticket(ticket_id)


@mcp.tool()
def reset_password(user: str) -> dict:
    """Reset a user's password and return a temporary password. Use when a user is locked out
    or has forgotten their password. `user` is the username, e.g. 'alice'."""
    return _reset_password(user)


if __name__ == "__main__":
    if "--http" in sys.argv or config.MCP_TRANSPORT == "http":
        print(f"MCP server on {config.MCP_URL} (streamable HTTP, no auth)", file=sys.stderr)
        mcp.run(transport="streamable-http", host=config.MCP_HOST, port=config.MCP_PORT)
    else:
        mcp.run()  # stdio
