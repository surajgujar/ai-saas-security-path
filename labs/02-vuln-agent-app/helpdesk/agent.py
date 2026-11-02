"""The HelpDesk Copilot agents.

Two agents, so there is an agent-to-agent hop to threat-model:
  triage   (root)  - reads the user's request and hands it to the resolver
  resolver         - has the tools: search_docs, send_email, and read_ticket via MCP

`adk web` and `adk run` look for a module-level variable called `root_agent`.
"""
import sys
from pathlib import Path

from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams, StreamableHTTPConnectionParams
from mcp import StdioServerParameters

from . import config
from .model import build_model
from .tools import search_docs, send_email

# The model for both agents, chosen by LAB_MODEL_BACKEND (Gemini / Vertex / Claude). See helpdesk/model.py.
MODEL = build_model()

LAB_DIR = Path(__file__).resolve().parents[1]

# The MCP tool server (get_ticket, reset_password). LAB_MCP_TRANSPORT picks how we reach it:
#   stdio: launch it as a subprocess with the same Python as this app (default)
#   http:  connect to an already-running server at MCP_URL (start it with `-m helpdesk.mcp_server --http`)
# (Done for you: the connection plumbing is version-specific and not the learning goal.)
if config.MCP_TRANSPORT == "http":
    mcp_connection = StreamableHTTPConnectionParams(url=config.MCP_URL, timeout=30)
elif config.MCP_TRANSPORT == "stdio":
    mcp_connection = StdioConnectionParams(
        server_params=StdioServerParameters(
            command=sys.executable,
            args=["-m", "helpdesk.mcp_server"],
            cwd=str(LAB_DIR),
        ),
        timeout=30,
    )
else:
    raise SystemExit(f"Unknown LAB_MCP_TRANSPORT={config.MCP_TRANSPORT!r}. Use stdio or http.")

ticket_tools = McpToolset(connection_params=mcp_connection)

# TODO(step 4): build the resolver agent.
resolver = LlmAgent(
    name="resolver",
    model=MODEL,
    description="This Agent help you to resolve technical issues",      # one line: what this agent does (the triage agent reads this to decide to delegate)
    instruction="Always answer from the provided documents and use the send_email tool when asked to email.",      # how to behave. Tell it to answer from the docs and to use send_email when asked to email.
    tools=[search_docs, send_email, ticket_tools],
)
#   Deliberately DON'T add safety rules yet (e.g. "never email outside the company").
#   Lab 4 needs the app vulnerable; lab 6 adds the rules and shows prompts alone aren't enough.
# resolver = None

# TODO(step 5): build the triage agent and make it the root.
root_agent = LlmAgent(
    name="triage",
    model=MODEL,
    description="This Agent is the first point of contact for users seeking help",      # one line: what this agent does (the resolver reads this to decide to delegate)
    instruction="You're a helpful assistant. Help users with their technical questions. Delegate IT-related queries to the resolver.",      # e.g. greet, work out what the user needs, transfer to the resolver for anything IT-related
    sub_agents=[resolver],
)
# root_agent = None
