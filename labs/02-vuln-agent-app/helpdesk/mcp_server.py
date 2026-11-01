"""MCP server that exposes the read_ticket tool over stdio.

The agent (agent.py) launches this as a subprocess and talks to it over MCP. This is the
"agent -> tool server" hop you threat-model in lab 3 and put authorization on in lab 7.

Run it alone to test:   uv run python -m helpdesk.mcp_server
(it will sit waiting on stdin - that's correct for a stdio server. Ctrl+C to stop.)

IMPORTANT: a stdio MCP server must never print() to stdout - stdout IS the protocol channel.
Log to stderr if you need to debug.
"""
from mcp.server import MCPServer

from .tools import read_ticket

mcp = MCPServer("helpdesk-tickets")


# TODO(step 3): register read_ticket as an MCP tool.
#   Use the @mcp.tool() decorator on a small wrapper function. The wrapper's docstring and
#   type hints become the tool description and schema the agent sees, so write a clear one.
#   Example shape:
#
@mcp.tool()
def get_ticket(ticket_id: str) -> dict:
    """Look up a support ticket by id, e.g. 'T-1001'."""
    return read_ticket(ticket_id)


if __name__ == "__main__":
    mcp.run()  # transport defaults to "stdio"
