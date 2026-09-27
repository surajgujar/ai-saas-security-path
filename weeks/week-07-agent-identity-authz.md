# Week 7 — Agent Identity, Non-Human Identity & Runtime Authorization (9 – 15 Nov)

**Why (JD):** "agent identity and runtime authorization"; "collaborate closely with IAM on non-human identity"; "workload identities, service accounts, AI agent identity, machine-to-machine authentication"
**Goal:** Your anchor strength (workload identity) extended to agents acting on behalf of users. This is a likely deep-dive interview topic.

## Learn (2.5 h)
- [ ] **OWASP Non-Human Identities Top 10**
- [ ] **MCP Authorization spec** (2026-07-28 version: OAuth 2.1, protected resource metadata, resource indicators, no token passthrough)
- [ ] **OAuth 2.0 Token Exchange — RFC 8693** (delegation vs impersonation, `act` claim) and **RFC 8707 Resource Indicators**
- [ ] **SPIFFE/SPIRE** concepts — SVIDs, attestation
- [ ] Fine-grained authz engines: **OPA/Rego** (you know policy-as-code), **Cedar** (AWS), **OpenFGA** (Zanzibar/ReBAC)
- [ ] GCP: Workload Identity Federation, service account impersonation, short-lived tokens, IAM Conditions, Agent identity in Vertex AI Agent Engine (check current docs)
- [ ] **Google Agent Identity** (SPIFFE-based principal, GA for Agent Runtime), **Agent Gateway**, Principal Access Boundary for agents — Google Cloud IAM blog (Next '26)
- [ ] Awareness: **Microsoft Entra Agent ID**, **AWS Bedrock AgentCore Identity**
- [ ] Standards landscape: IETF **draft-ietf-wimse-aims**; NIST AI Agent Standards Initiative identity & authorization concept paper; CoSAI *Agentic IAM* paper (Apr 2026)
- [ ] **MCP 2026-07-28 spec** authorization changes: RFC 9207 `iss` validation, credential binding, CIMD, Enterprise Managed Authorization

## Lab (4 h) → `labs/07-agent-authz/`
- [ ] Put an OAuth authorization server (Keycloak in Docker) in front of your MCP server
- [ ] Agent obtains a **user-delegated, down-scoped** token via token exchange (`sub` = user, `act` = agent)
- [ ] Each tool call evaluated by **OPA**: user entitlement ∩ agent allowed tools ∩ context (time, data classification, amount)
- [ ] Tokens ≤ 5 min, audience-bound; no static secrets
- [ ] Demo: prompt-injected agent tries `send_email` to external domain → **denied at authz layer even though guardrail missed it**
- [ ] Log every decision (input to Week 11)

## Interview questions
1. Should an AI agent have its own identity, use the user's, or both? Defend it.
2. How do you prevent the confused-deputy problem with MCP servers?
3. How would you design joiner-mover-leaver for agents and service accounts?
4. Where does runtime authz sit relative to guardrails? (Guardrails are probabilistic; authz is deterministic.)

## Done when
- [ ] Working demo + sequence diagram committed
