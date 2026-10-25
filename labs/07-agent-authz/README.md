# Lab 7: agent identity & runtime authorization

**Goal:** put a deterministic authorization check on **every** tool call: user entitlement ∩ agent capability ∩ context. Show the prompt-injected agent try the exfil action and get **denied at the authz layer** even though the guardrail missed it. This is your flagship-niche lab (it previews the Q2 project).

**Prepares you for:** "Should an agent have its own identity or the user's?" "Guardrails missed it — what stops the action?"

**Time:** core 4.5 h (OPA per-tool with a mock token). **Stretch** adds real OAuth token exchange. **Before you start:** Lab 2 done, Docker running.

> **Scope note:** the original week packed Keycloak token exchange *and* OPA into one weekend. That's too much. **Core = OPA authorization with a mock token.** Keycloak token exchange is the stretch goal, and it's also Q2's main project, so it's fine to defer.

## What's here
```
policy.rego   the authorization policy          TODO(step 2)
authz.py      before_tool_callback that calls OPA TODO(step 3)
```

## Core steps

### Step 1: run OPA (20 min)
```powershell
cd labs\07-agent-authz
docker run --rm -p 8181:8181 -v ${PWD}:/policy openpolicyagent/opa run --server /policy/policy.rego
```
**Checkpoint:** `curl http://localhost:8181/health` returns `{}`.

### Step 2: write the policy (70 min)
Fill in `policy.rego` (the `TODO`): allow `search_docs` for anyone; allow `get_ticket` only if the ticket's `user` matches the caller; allow `send_email` only to `@corp.example`. Test with `opa eval` and a few `input.json` files before wiring it to the agent.

**Checkpoint:** `opa eval -d policy.rego -i input.json "data.helpdesk.authz.allow"` returns `true`/`false` correctly for an owned vs not-owned ticket.

### Step 3: enforce on every tool call (60 min)
Finish `opa_authz` in `authz.py` and set it as the resolver's `before_tool_callback` (replacing or chaining with Lab 6's — ADK accepts a list of callbacks).

**Checkpoint:** as `carol` (hr_manager) vs `alice` (engineer), the same ticket lookup is allowed for the owner and denied for the other.

### Step 4: the headline demo (45 min)
Re-run the Lab 4 indirect-injection exfil as `alice`. The injection still fires and the agent still *tries* `send_email` to the external address, but OPA **denies** it. Capture the denied decision. Contrast with Lab 6, where a guardrail pattern could be reworded around; the policy can't, because external simply isn't allowed.

### Step 5: log every decision (30 min)
Have `opa_authz` append each decision (`user, tool, args-summary, allow/deny, reason`) to `authz_log.jsonl`. This is the input to Lab 11's detections. Keep it structured JSON.

## Stretch (this is Q2's project — just taste it here)
- Run Keycloak in Docker, define a client, and do an OAuth **token exchange** (RFC 8693) so the agent gets a user-delegated, down-scoped token (`sub`=user, `act`=agent), ≤5 min, audience-bound. Replace the mock token in `authz.py` with the real one and have OPA read claims from it.
- Add a context rule: deny `send_email` outside working hours, or above a size threshold.

## Done when
- [ ] OPA runs and the policy passes `opa eval` tests
- [ ] `opa_authz` denies a not-owned ticket and external email
- [ ] The injected exfil action is denied at the authz layer (evidence saved)
- [ ] `authz_log.jsonl` records decisions
- [ ] Committed to `labs/07-agent-authz/`

## If it breaks
| Symptom | Fix |
|---|---|
| `connection refused` to 8181 | OPA container isn't running, or the volume mount path is wrong on Windows (use `${PWD}` in PowerShell). |
| Policy always denies | `default allow := false` plus no matching rule. Add a rule and test it with `opa eval` first. |
| Callback can't find the user | In ADK the user is in session state: `tool_context.state.get("user")`. Confirm `runner.py` sets `state={"user": user}` (it does). |
| Rego syntax errors | OPA 0.6x+ uses `if` and `contains` keywords; `ends_with(x, y)` is a built-in. Check the server log. |
