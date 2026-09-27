# Week 3 — Threat Frameworks (12 – 18 Oct)

**Why (JD):** "red-teaming against OWASP LLM Top 10 and MITRE ATLAS"; "Assess AI systems end to end"
**Goal:** A repeatable AI threat-modelling method you can run as a Siemens consultant.

## Learn (2.5 h)
- [ ] **OWASP Top 10 for LLM Applications — 2026 edition** (released 1 Sep 2026) — genai.owasp.org. Memorise the 10 IDs; note what changed vs 2025 (*Excessive Agency* up to #3; *System Prompt Leakage* replaced by *Hidden Context Exposure*)
- [ ] **OWASP Agent Control Standard (ACS) v0.1** — runtime governance of agents: guardian-agent enforcement points, OTel + OCSF observability, AgBOM
- [ ] **OWASP Top 10 for Agentic Applications** + *Agentic AI – Threats and Mitigations* (OWASP GenAI Security Project)
- [ ] **MITRE ATLAS** — atlas.mitre.org: matrix, tactics, 3–4 case studies
- [ ] **NIST AI 100-2** — *Adversarial Machine Learning: Taxonomy and Terminology* (skim structure: evasion, poisoning, privacy, GenAI abuse)
- [ ] **Google SAIF** (Secure AI Framework) — saif.google, risk map
- [ ] OWASP *AI Testing Guide* (skim)

## Lab (4 h) → `labs/03-threat-model/`
Threat-model your Week 2 app:
- [ ] Data-flow diagram with trust boundaries
- [ ] Table: component × threat × OWASP ID × ATLAS technique ID × likelihood × impact × control
- [ ] Minimum 15 threats covering: model, RAG store, tools, MCP server, agent-to-agent hop, user identity, logs
- [ ] Turn it into a reusable **template** (`TEMPLATE.md`) — this is what you'd hand to Siemens product teams

## Interview questions
1. Walk me through how you'd assess a new AI product end to end in 2 weeks.
2. Map indirect prompt injection to OWASP and ATLAS.
3. OWASP LLM Top 10 vs Agentic Top 10 — what does "agentic" add? (tool misuse, identity/privilege abuse, memory poisoning, cascading failures, rogue agents) — and how does the 2026 list reflect it?
4. How do you prioritise findings when a business team wants to launch next week?

## Done when
- [ ] Threat model + template committed · [ ] Note written
