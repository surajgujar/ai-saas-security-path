"""A before_tool_callback that asks OPA 'is this tool call allowed?' on EVERY call.

This is the difference from Lab 6: Lab 6 guesses whether content is malicious; this makes a
deterministic yes/no from a policy about user, agent, tool and args. Wire it into the resolver
agent the same way as the Lab 6 callback.

Core version: a mock token (a dict you build from the current user). Stretch: a real
down-scoped token from Keycloak token exchange (see README step 5).
"""
import json
import urllib.request

OPA_URL = "http://localhost:8181/v1/data/helpdesk/authz/allow"

# Mock "who is acting". In Lab 2 the user is passed per request; here, map it to a role.
USER_ROLES = {"alice": "engineer", "bob": "engineer", "carol": "hr_manager",
              "dave": "sales", "mallory": "contractor"}


def _decision(tool_name: str, args: dict, user: str) -> bool:
    payload = {"input": {
        "user": {"id": user, "role": USER_ROLES.get(user, "unknown")},
        "agent": "resolver",
        "tool": tool_name,
        "args": args,
        "context": {},
    }}
    req = urllib.request.Request(OPA_URL, data=json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=5) as r:
        return json.loads(r.read()).get("result", False) is True


def opa_authz(tool, args, tool_context):
    """Deny the tool call unless OPA allows it.

    TODO(step 3): implement.
      - find the acting user. In ADK it's on the session state: tool_context.state.get("user", "alice")
      - allowed = _decision(tool.name, dict(args), user)
      - if not allowed: return {"status": "denied", "by": "authz", "tool": tool.name}
      - else: return None
    """
    raise NotImplementedError("Finish opa_authz (step 3)")
