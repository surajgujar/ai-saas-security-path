# OPA policy: may this agent, acting for this user, call this tool with these args?
# Test locally:  opa eval -d policy.rego -i input.json "data.helpdesk.authz.allow"
# Run as a server: docker run -p 8181:8181 openpolicyagent/opa run --server policy.rego

package helpdesk.authz

default allow := false

# Input shape your callback sends (see authz.py):
# {
#   "user":   {"id": "alice", "role": "engineer"},
#   "agent":  "resolver",
#   "tool":   "send_email",
#   "args":   {"to": "x@corp.example", ...},
#   "context":{"data_classification": "internal"}
# }

# TODO(step 2): write the rules. Start permissive for reads, strict for actions.

# Example scaffold - replace with your own:
# allow if {
#   input.tool == "search_docs"
#   # anyone may search, but confidential results are filtered elsewhere (Lab 6 RAG filter)
# }

# allow if {
#   input.tool == "get_ticket"
#   # TODO: only if the ticket belongs to input.user.id
# }

# allow if {
#   input.tool == "send_email"
#   ends_with(input.args.to, "@corp.example")   # internal only, no approval needed
# }

# A deny message helps debugging:
# reason := "ticket not owned by user" if { ... }
