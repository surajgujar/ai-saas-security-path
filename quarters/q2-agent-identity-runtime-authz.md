# Q2 — Agent Identity & Runtime Authorization (Jan – Mar 2027) · FLAGSHIP NICHE

**Why this quarter exists:** It's the most-hired leadership problem at labs and clouds right now: OpenAI's EM Identity & Access Platform asks for "first-class authorization for agents… delegated, action-scoped, time-bound, full attribution". Google, Microsoft and AWS all shipped agent identity in 2026, and IETF, NIST and CoSAI are standardising it now.
**Outcome:** You're recognisably "the agent identity & runtime authz person": an open-source tool, a reference architecture, a talk, a standards contribution, and **CISSP passed**.
**Hours:** see the PLAN.md rhythm (4.5 build · 2.5 learn · 2.5 lead/visible · 1.5 career). CISSP study uses the Learn block plus commute audio/video in Feb–Mar. Career tasks: [`career-track.md`](career-track.md).

## Month 1 — Standards & platforms at current state (Jan 2027)
- [ ] IETF **draft-ietf-wimse-aims** (AI agent authentication & authorization) + WIMSE architecture: read the latest version, summarise the gaps it lists
- [ ] OAuth building blocks: RFC 8693 token exchange (`act` claim), RFC 8707 resource indicators, RFC 9449 **DPoP**, RFC 9396 rich authorization requests, RFC 9207 `iss`, RFC 9700 BCP
- [ ] MCP **2026-07-28 spec** (+ any newer release): stateless requests, CIMD vs DCR, credential binding, **Enterprise Managed Authorization**; track SEP-1932 (DPoP) and SEP-1933 (Workload Identity Federation)
- [ ] **Google Agent Identity** (SPIFFE-based principal), **Agent Gateway**, IAP/CAA for agents, **Principal Access Boundary** and **Unified Access Policy** for agents, Agent Identity Auth Manager (OAuth on behalf of users)
- [ ] **Microsoft Entra Agent ID** and **AWS Bedrock AgentCore Identity**: build a 1-page cross-cloud comparison (identity model, delegation, policy, audit)
- [ ] **NIST AI Agent Standards Initiative** identity & authorization concept paper; **CoSAI "Agentic Identity and Access Management"** (Apr 2026) and **"MCP Security"** (Jan 2026) papers
- [ ] OWASP **Agent Control Standard** (latest version): guardian-agent enforcement points, OCSF/OTel, AgBOM
- [ ] Leadership: write a 2-page **"Agent identity strategy" memo** for your current CISO (problem, options, cost, recommendation)
- [ ] CISSP: book the exam for late March; start a study plan (Official Study Guide + practice questions)

## Month 2 — Build the flagship (Feb 2027)
- [ ] **`agent-authz-gateway`** (open source): MCP/A2A-aware proxy that
  - authenticates agents with SPIFFE SVIDs or Google Agent Identity
  - does **token exchange** (user → agent, down-scoped, audience-bound, ≤5 min, DPoP-bound)
  - evaluates **every tool call** against OPA or Cedar (user entitlement ∩ agent capability ∩ context/data class) with a human-approval hook
  - emits **OCSF + OpenTelemetry** events and a hash-chained audit log (ACS-aligned)
  - scans MCP tool descriptions for poisoning and pins description hashes (rug-pull detection)
- [ ] Demo: an indirect prompt injection makes the agent attempt exfiltration → the **deterministic authz layer denies it** while the guardrail misses it
- [ ] Deploy the reference setup on GCP (Agent Runtime + Agent Gateway + Model Armor) and document what the managed service covers vs. your gateway
- [ ] README, architecture diagram, demo GIF, v0.1 release, GitHub Action
- [ ] Leadership: bring 1–2 colleagues in as contributors (you set direction, review, merge). This is team-leadership evidence

## Month 3 — Publish, speak, contribute (Mar 2027)
- [ ] Publish **"Reference Architecture: Identity & Runtime Authorization for Enterprise AI Agents"** (GCP-first, with Entra/AWS mappings; threats mapped to OWASP LLM 2026, Agentic Top 10, NHI Top 10)
- [ ] Talk #1 at OWASP / null / BSides Pune (or virtual CoSAI / OWASP community call)
- [ ] Standards contribution: comment on a WIMSE draft, open a CoSAI / OWASP ACS issue or PR, or join a working group call and take an action item
- [ ] Blog series: 3 posts (token exchange for agents; MCP authz on the 2026 spec; guardrails ≠ authorization)
- [ ] **CISSP exam** ✅
- [ ] **FS sector module**: map your gateway's controls to UK PRA SS1/23 (model inventory, validation, monitoring), EU AI Act and DORA; publish as a post "Agent authorization for regulated banks"

## Done when
- [ ] OSS released with an external user/issue · [ ] Architecture published · [ ] Talk delivered · [ ] Standards contribution · [ ] CISSP passed

## Interview questions this quarter prepares you for
1. Design authorization for 500 agents acting on behalf of 50,000 employees across GCP, M365 and SaaS.
2. Delegation vs impersonation. When would you ever allow impersonation?
3. How would you migrate an org from static API keys in MCP configs to short-lived, bound credentials in 90 days?
4. What does the MCP 2026-07-28 spec fix, and what does it still leave to you?
