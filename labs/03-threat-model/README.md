# Lab 3: threat model of the HelpDesk Copilot

**Goal:** turn the Week 2 app into a documented threat model: a data-flow diagram with trust boundaries, and a table of 15+ threats mapped to OWASP LLM 2026 and MITRE ATLAS, each with a control. Then make it a reusable template you'd hand to product teams.

**Prepares you for:** "How would you assess a new AI product in two weeks?" "Threat-model this agent on the whiteboard."

**Time:** core 4.5 h. **Before you start:** Lab 2 working (you need the app to model). If Lab 2 isn't done, do its steps 1–5 first.

**No code this week** — it's a documentation lab. Outputs are two markdown files plus a diagram.

## Core steps

### Step 1: data-flow diagram (60 min)

In `labs/03-threat-model/dfd.md`, draw the app as a Mermaid flowchart. Show every component from Lab 2 and draw **trust boundaries** (dashed subgraphs) where data crosses from trusted to untrusted:
- user ⇄ triage agent ⇄ resolver agent
- resolver ⇄ Chroma (RAG), ⇄ MCP ticket server, ⇄ send_email
- the two **untrusted-content** entry points: retrieved documents, and ticket text

Mark where untrusted content (a retrieved doc, a ticket) first reaches the model. That's the injection surface.

### Step 2: threat table (2 h)

In `threats.md`, make a table with these columns:

`ID | Component | Threat | OWASP LLM 2026 ID | ATLAS technique | Likelihood (H/M/L) | Impact (H/M/L) | Control`

Cover at least these 15, one row each:
1. Indirect injection via a poisoned doc → data exfil (the Lab 4 attack)
2. Confidential HR doc retrieved by a non-HR user (no RAG filter)
3. Any user reads any ticket (no ownership check)
4. `send_email` to an external domain (exfil channel)
5. Excessive agency: resolver has email + ticket + search with no approval
6. System-prompt leak via the resolver
7. Prompt-injection in a ticket reaching the MCP tool path
8. Unbounded requests / cost (no rate limit)
9. Sensitive data in logs
10. MCP server trusts any caller (no authz) — Lab 7
11. Agent-to-agent: triage over-delegates to resolver
12. Model/dependency supply chain (the model, chromadb, adk) — Lab 5
13. No output filtering / DLP — Lab 6
14. PII in the embedding store
15. No audit trail of tool calls — Lab 11

Use the real OWASP 2026 IDs (LLM01 Prompt Injection, LLM02 Sensitive Information Disclosure, LLM06 Excessive Agency, …) and ATLAS technique IDs from the matrix. Link both from your tracker.

**Checkpoint:** every threat names a control, and the controls point forward to the lab that implements them (6, 7, 11). That mapping is your Q1 story.

### Step 3: reusable template (90 min)

Copy `threats.md` into `TEMPLATE.md`, strip the HelpDesk specifics, and leave prompts/placeholders so another team can fill it for their own AI product. Add a one-page "how to use this" intro. This is a leadership artefact: it's what a Head of AI Security hands to product teams.

## Stretch

- Add a STRIDE column and check you've covered each STRIDE category.
- Map the same threats to the OWASP **Agentic** Top 10 (ASI01–ASI10) as well, and note where the agentic list catches something the LLM list doesn't.

## Done when

- [ ] `dfd.md` with trust boundaries
- [ ] `threats.md` with 15+ rows, OWASP 2026 + ATLAS IDs, controls
- [ ] `TEMPLATE.md` reusable version
- [ ] Committed to `labs/03-threat-model/`

## If it breaks

| Symptom | Fix |
|---|---|
| Mermaid won't render on GitHub | Use a ```` ```mermaid ```` fenced block; check for a stray `()` in a node label. Preview at mermaid.live. |
| Can't find an ATLAS id | Not every threat has an exact ATLAS technique. Use the closest tactic and say so; that's honest and fine. |
