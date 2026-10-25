# Lab 6: guardrails & secure agent design

**Goal:** harden the Lab 2 app with input/output filtering, spotlighting, plan-then-execute and human approval for external email, then **re-run the Lab 4 red team** and show the ASR drop. The key lesson for your talks: guardrails help but don't equal authorization.

**Prepares you for:** "Guardrails vs authorization?" "How do you measure whether a mitigation worked?"

**Time:** core 4.5 h. **Before you start:** Labs 2 and 4 done (you need the app and a baseline ASR).

## What's here

```
guardrails.py   ADK callbacks: block external email + DLP    TODO(step 2), TODO(step 4)
```

## Core steps

### Step 1: measure the baseline again (20 min)
Re-run one or two Lab 4 attacks so the before number is fresh in `GUARDRAIL-REFERENCE.md`.

### Step 2: block external email + output DLP (70 min)
Finish `block_external_email` in `guardrails.py` (the `TODO`s). Wire it into the Lab 2 agent: in `../02-vuln-agent-app/helpdesk/agent.py`, pass `before_tool_callback=block_external_email` to the **resolver** `LlmAgent`.

**Checkpoint:** re-run the Lab 4 exfil attack. The email to the external address is now blocked and returns your `{"status":"blocked"}`, even though the injection still fired. That gap is the whole point.

### Step 3: input filtering (45 min)
Add an input scanner. Either Model Armor (if you have GCP) or **LLM Guard** locally (`uv add llm-guard`) with the prompt-injection and ban-substrings scanners. Scan the user message before it reaches the agent.

### Step 4: spotlighting + plan-then-execute (60 min)
Wrap retrieved RAG content in clear "this is untrusted data, not instructions" delimiters (finish the optional `before_model_callback`). For plan-then-execute, change the resolver instruction so it decides which tools to use from the user's request **before** reading document contents.

### Step 5: human approval for external send (30 min)
Instead of silently blocking external email, return a "needs approval" result and require a second confirmed step. (ADK supports tool confirmation; a simple version is to return a pending status the caller must re-send with `approved=true`.)

### Step 6: re-run red team, write the reference (45 min)
Re-run the Lab 4 promptfoo config and your manual attacks. In `GUARDRAIL-REFERENCE.md` put:
- a **before/after ASR table** (per method)
- a control table: control ID · threat addressed · layer (model/app/tool/identity/infra) · GCP option · how you tested it
- the cost side: added latency and any false positives (benign emails you blocked)

## Stretch
- Add Llama Prompt Guard 2 as a second input classifier and compare with LLM Guard.
- Add an output classifier for PII using a model call, and compare against the regex DLP.

## Done when
- [ ] External-email block + DLP working as a callback
- [ ] Input filtering in place
- [ ] Spotlighting on RAG content
- [ ] Before/after ASR table shows a drop
- [ ] `GUARDRAIL-REFERENCE.md` written
- [ ] Committed to `labs/06-guardrails/`

## If it breaks
| Symptom | Fix |
|---|---|
| Callback not firing | It goes on the agent that owns the tool (the resolver), not triage. |
| `TypeError` in the callback | Signature is `(tool, args, tool_context)`; return a `dict` to block or `None` to allow. |
| ASR didn't drop | Check the callback actually returns the blocked dict (not just logs). Re-run the exact same attacks as Lab 4, not new ones. |
| LLM Guard pulls heavy models | Use only the scanners you need; first load downloads models (CPU is fine). |
