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
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

from .config import GEMINI_MODEL
from .tools import search_docs, send_email

LAB_DIR = Path(__file__).resolve().parents[1]

# The MCP tool server, launched as a subprocess with the same Python as this app.
# (Done for you: the connection plumbing is version-specific and not the learning goal.)
ticket_tools = McpToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command=sys.executable,
            args=["-m", "helpdesk.mcp_server"],
            cwd=str(LAB_DIR),
        ),
        timeout=30,
    ),
)

# TODO(step 4): build the resolver agent.
#   resolver = LlmAgent(
#       name="resolver",
#       model=GEMINI_MODEL,
#       description=...,      # one line: what this agent does (the triage agent reads this to decide to delegate)
#       instruction=...,      # how to behave. Tell it to answer from the docs and to use send_email when asked to email.
#       tools=[search_docs, send_email, ticket_tools],
#   )
#   Deliberately DON'T add safety rules yet (e.g. "never email outside the company").
#   Lab 4 needs the app vulnerable; lab 6 adds the rules and shows prompts alone aren't enough.
resolver = None

# TODO(step 5): build the triage agent and make it the root.
#   root_agent = LlmAgent(
#       name="triage",
#       model=GEMINI_MODEL,
#       description=...,
#       instruction=...,      # e.g. greet, work out what the user needs, transfer to the resolver for anything IT-related
#       sub_agents=[resolver],
#   )
root_agent = None
