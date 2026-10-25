"""Guardrails you bolt onto the Lab 2 agent, as ADK callbacks.

A `before_tool_callback(tool, args, tool_context)` runs just before each tool call. If it
returns a dict, that dict is used as the tool's result and the real tool is NOT called - so
it's a clean place to BLOCK an action. Returning None lets the call proceed.

You import these into ../02-vuln-agent-app/helpdesk/agent.py in step 3. This is where you
learn that a guardrail reduces risk but doesn't replace authorization (that's Lab 7).
"""
import re

COMPANY_DOMAIN = "corp.example"

# A crude DLP signal: things that look like confidential HR content.
SECRET_PATTERNS = [
    re.compile(r"\bsalary band", re.I),
    # TODO(step 2): add 2-3 more (e.g. a salary number pattern, "CONFIDENTIAL", an email+amount combo)
]


def block_external_email(tool, args, tool_context):
    """Block send_email to any domain that isn't the company, and DLP-scan the body.

    TODO(step 2): implement.
      - if tool.name != "send_email": return None  (only guard this tool)
      - to = args.get("to", "")
      - if the domain of `to` is not COMPANY_DOMAIN: return a dict like
            {"status": "blocked", "reason": "external recipient needs approval"}
      - if any SECRET_PATTERNS matches args.get("body",""): return a blocked dict
      - otherwise return None
    Return value shape matters: a dict short-circuits the tool; None lets it run.
    """
    raise NotImplementedError("Finish block_external_email (step 2)")


# TODO(step 4, optional): a before_model_callback that "spotlights" retrieved content by
# wrapping it in clear delimiters and a note that it's untrusted data, not instructions.
