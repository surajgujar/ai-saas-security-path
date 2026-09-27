# Week 7 post (#6): your AI agent needs an identity (on GCP)

**Publish:** Fri 13 Nov 2026 · **Visual:** sequence diagram: user → agent → token exchange (IdP) → MCP server → OPA decision → allow/deny

---

Most AI agents in production today run as **a shared service account or a long-lived API key**.

That means that when something goes wrong, the logs say "the service account did it". You don't know which agent, for which user, or why.

Agents need their own identity, and they need to carry the user's authority *explicitly*.

What I built this week:
1️⃣ Keycloak in front of my MCP server
2️⃣ **OAuth token exchange (RFC 8693)**: the agent swaps the user's token for a new one that is down-scoped, limited to one audience and valid ≤5 minutes. The `act` claim records "agent X acting for user Y".
3️⃣ **OPA checks every tool call**: user entitlement ∩ agent capability ∩ data sensitivity.
4️⃣ Demo: a prompt-injected agent tried [the unsafe action]. **The policy denied it**, and the decision was logged.

The platforms are moving the same way. Google Cloud's **Agent Identity** gives each agent a SPIFFE-based identity, and **Agent Gateway** enforces access in front of tools. Microsoft has Entra Agent ID. In IETF and CoSAI, agent identity is now active standards work.

Open question I'm still working through: should an agent act with **its own identity, the user's, or both**? My current view: [your answer].

#AgentIdentity #IAM #AgenticAI #GoogleCloud #OAuth

---
**First comment (links):** RFC 8693 – https://datatracker.ietf.org/doc/html/rfc8693 · Google Agent Identity – https://docs.cloud.google.com/iam/docs/agent-identity-overview · CoSAI Agentic IAM – https://www.coalitionforsecureai.org/wp-content/uploads/2026/04/agentic-identity-and-access-control.pdf
