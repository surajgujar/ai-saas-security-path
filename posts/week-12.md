# Week 12 post (#12): Q1 recap with portfolio link

**Publish:** Fri 18 Dec 2026 · **Visual:** a 12-tile grid, one per lab, each with its single most important result

---

12 weeks ago I said I'd go all-in on AI & agent security and share what I learned each week. Here's the recap.

**12 labs, one target app, measured results:**
• Built a deliberately vulnerable agent (RAG + tools + MCP + multi-agent)
• Threat-modelled it against OWASP LLM 2026 + MITRE ATLAS: [X] threats
• Red-teamed it: [X]% attack success at baseline
• Added guardrails and secure design patterns: [X]% → [Y]%
• Added per-tool authorization with token exchange + OPA: [the unsafe action] denied by policy
• Model signing + ML-BOM gate in CI
• Secure Terraform baseline for AI on Google Cloud
• SSPM drift detector, OAuth grant auditor, JML leaver flow
• OpenTelemetry tracing + tamper-evident audit log + detections
• A draft AI & SaaS security standard and a 12-month roadmap

**3 lessons:**
1. Prompt injection is the entry point. Authorization and identity decide how much damage it can do.
2. Most real risk sits in integrations: OAuth grants, tool access, SaaS settings.
3. [Your own lesson.]

**Next quarter:** I'm building an open-source **agent authorization gateway**. It gives MCP/A2A tool calls token exchange, a policy decision on every call and an audit trail.

Portfolio: [link to your GitHub repo]

Thank you to everyone who commented, challenged me and shared their own experience this quarter. [Tag 2–3 people who helped.]

#AISecurity #AgenticAI #SecurityLeadership #OpenSource

---
**First comment (links):** your repo link · the Week 6 and Week 7 posts
