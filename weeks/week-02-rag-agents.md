# Week 2 — RAG, Vector DBs, Agents, Multi-Agent (5 – 11 Oct)

**Why (JD):** "vector databases, RAG, agents, multi-agent systems, and AI orchestration frameworks"
**Goal:** Build a realistic (deliberately vulnerable) agent app that becomes your **target for Weeks 3–7 and 11**.

## Learn (2.5 h)
- [ ] Google ADK (Agent Development Kit) docs — quickstart + multi-agent section
- [ ] LangGraph docs — concepts: state, tools, human-in-the-loop
- [ ] MCP spec (modelcontextprotocol.io) — re-read the *Security Best Practices* and *Authorization* pages (you know MCP; focus on the threat notes)
- [ ] A2A (Agent2Agent) protocol overview — agent cards, task lifecycle, auth
- [ ] Vector DB security basics: tenant isolation, metadata filtering as authz, embedding inversion risk (read a short blog/paper summary)

## Lab (4 h) → `labs/02-vuln-agent-app/`
Build **"HelpDesk Copilot"** (keep it small, Python):
- [ ] RAG over ~20 docs in Chroma/pgvector — include one "confidential" HR doc and one doc containing a hidden indirect-injection payload
- [ ] Agent (ADK or LangGraph) with 3 tools: `search_docs`, `send_email` (mock), `read_ticket(id)` (mock DB)
- [ ] Expose one tool through a local MCP server
- [ ] Add a second agent (e.g. "Triage agent" → "Resolver agent") so there's an agent-to-agent hop
- [ ] Deliberately leave: no per-user doc filtering, broad tool permissions, no output checks
- [ ] Architecture diagram in the lab README (Mermaid)

## Interview questions
1. Where are the trust boundaries in a RAG + agent system?
2. How is authorization in a vector DB different from a relational DB?
3. MCP vs A2A — what does each solve, and what new risks do they introduce?
4. What's the "lethal trifecta" (private data + untrusted content + exfiltration channel) and how does your app have it?

## Done when
- [ ] App runs end-to-end · [ ] Diagram in README · [ ] Note written
