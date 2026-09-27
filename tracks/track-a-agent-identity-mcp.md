# Track A — Agent Identity & MCP Security (Jan – Mar 2027) · PRIMARY NICHE

**Outcome:** Be recognisably "the agent identity + MCP security person" — a flagship open-source tool, a reference architecture, and a talk.

## Month 1 — Deep standards knowledge
- [ ] MCP spec: authorization (OAuth 2.1, protected resource metadata, dynamic client registration), security best practices; track every spec revision since 2025
- [ ] A2A protocol: agent cards, signing, auth schemes
- [ ] OAuth: RFC 8693 token exchange, RFC 8707 resource indicators, RFC 9700 BCP, DPoP (RFC 9449), rich authorization requests (RFC 9396)
- [ ] IETF / OpenID Foundation work on AI agent identity (e.g. OAuth for AI agents drafts, OpenID AI Identity community group) — summarise the current state in a blog post
- [ ] SPIFFE/SPIRE for workload identity of agents; GCP Workload Identity Federation + service account impersonation limits
- [ ] Study MCP incidents: tool poisoning, rug-pull (changing tool descriptions after approval), postmark-mcp supply chain, MCP Inspector RCE, mcp-remote command injection
- [ ] Vendor landscape: Runlayer, Helmet, Noma, Astrix, Aembit, Saviynt, SGNL (CrowdStrike), CyberArk (Palo Alto), Okta for AI agents, Google Agent identity — 1-page comparison

## Month 2 — Build the flagship open-source tool (pick ONE)
- [ ] Option 1 **`mcp-audit`**: scanner for MCP server configs + tool manifests — detects static tokens, missing OAuth, over-broad scopes, poisoned/hidden instructions in tool descriptions, description drift (rug-pull) via hash pinning, path traversal/command-injection patterns. Output SARIF for CI.
- [ ] Option 2 **`agent-authz-gateway`**: an MCP proxy that enforces per-tool OPA/Cedar policy, token exchange (user → agent down-scoped), and writes hash-chained audit logs
- [ ] Option 3 **Agent NHI inventory for GCP**: discover Vertex AI agents / service accounts / keys used by agents, score privilege, map owner — integrate with Wiz/SCC findings
- [ ] README, demo GIF, GitHub Action, v0.1 release

## Month 3 — Reference architecture & visibility
- [ ] Write *"Reference architecture: identity & runtime authorization for enterprise AI agents on GCP"* (diagrams, controls, threat mapping to OWASP Agentic Top 10 + NHI Top 10)
- [ ] Give a talk at OWASP / null / BSides Pune using the tool as the demo
- [ ] Open a PR / contribution to OWASP GenAI Security Project or CSA related to MCP or agent identity
- [ ] Cert option: GIAC GAIPS (SEC545) if sponsored

## Done when
- [ ] Tool released with ≥1 external user/issue · [ ] Architecture doc published · [ ] Talk delivered
