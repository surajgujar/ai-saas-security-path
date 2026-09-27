# Gap Analysis — JD vs. Resume

Legend: 🟢 strong (resume evidence) · 🟡 partial (adjacent experience) · 🔴 gap (needs deliberate work)

## AI / LLM / Agentic

| JD requirement | Rating | Evidence / gap | Week |
|---|---|---|---|
| How LLMs are designed, trained, fine-tuned, evaluated, deployed | 🟡 | You use and secure LLMs; need to articulate internals (attention, pre-training vs SFT vs RLHF/DPO, LoRA, quantisation, eval) | 1 |
| Embeddings, vector DBs, RAG | 🟡 | Implicit via agent work; need hands-on build + attack surface (vector DB authz, embedding inversion) | 2 |
| Agents, multi-agent, orchestration frameworks | 🟢/🟡 | MCP agents + multi-agent auth at TransUnion; broaden to LangGraph, Google ADK, A2A | 2 |
| Prompt injection, jailbreaks | 🟢 | Model Armor in prod. Gap: **offensive** side — running red-team campaigns | 4 |
| Data poisoning / leakage, model extraction | 🔴 | Need to understand and demo these attacks | 5 |
| Supply-chain integrity, model provenance | 🟡 | Model scanning done; add signing (OpenSSF model-signing/Sigstore), AI-BOM, SLSA | 5 |
| Red-teaming vs OWASP LLM Top 10 & MITRE ATLAS | 🟡 | Know OWASP conceptually; need ATLAS mapping + structured red-team reports | 3, 4 |
| Agent identity & runtime authorization | 🟡 | Multi-agent access control done; deepen with OAuth token exchange, SPIFFE, OPA/Cedar, MCP auth spec | 7 |

## Cloud

| JD requirement | Rating | Evidence / gap | Week |
|---|---|---|---|
| Securing AI workloads on GCP, IAM, networking | 🟢 | PCSE, workload identity, segmentation. Add Vertex AI–specific controls (VPC-SC, PSC, CMEK, org policies, SCC AI Protection) | 8 |
| AI model deployment pipelines | 🟢/🟡 | CI/CD security strong; apply to model pipelines (signing gates, eval gates) | 5, 8 |

## SaaS — biggest gap

| JD requirement | Rating | Evidence / gap | Week |
|---|---|---|---|
| SSPM, CASB, SaaS control planes | 🔴 | Wiz CSPM is the closest analogue — frame it as "posture management, different plane" | 9 |
| Misconfig & drift detection across SaaS | 🟡 | You do this for cloud; learn SaaS baselines (CISA SCuBA, CIS M365/Workspace) | 9 |
| Third-party OAuth / integration governance | 🔴 | Consent grants, app allow-listing, token revocation | 10 |
| Shadow SaaS / Shadow AI discovery | 🔴 | CASB log discovery, OAuth-based discovery, browser/SWG signals | 9 |
| DLP across SaaS estate | 🟡 | Model Armor PII filtering is related; learn SaaS DLP (Workspace/Purview DLP, CASB inline) | 9 |
| SaaS identity lifecycle, JML | 🔴 | SCIM, SSO, deprovisioning gaps, orphaned accounts | 10 |
| OAuth/OIDC token governance, least privilege | 🟡 | Know IAM deeply; add OAuth grant types, scopes, refresh-token risk | 7, 10 |
| API security (OWASP API Top 10) | 🟡 | Dev background helps; do hands-on with crAPI | 10 |
| Workload identities, service accounts, M2M | 🟢 | Strong — position as your anchor strength | 7 |

## Operations & Governance

| JD requirement | Rating | Evidence / gap | Week |
|---|---|---|---|
| AI/SaaS telemetry, anomaly detection | 🟡 | Threat detection via Wiz; add GenAI telemetry (OpenTelemetry GenAI conventions) | 11 |
| Immutable audit trails for agentic actions | 🔴 | Locked log buckets, hash-chaining, tamper evidence | 11 |
| SOC / SIEM / XDR integration | 🟡 | Write detections (Sigma / YARA-L for Google SecOps) | 11 |
| Standards, guardrails, reference controls | 🟢/🟡 | "Translate requirements into enforceable controls" is on your resume — produce a written standard | 12 |
| GRC, audits, regulatory alignment | 🟡 | Learn EU AI Act, NIST AI RMF, ISO/IEC 42001, CRA — Siemens is EU-headquartered | 12 |
| Stakeholder alignment, mentoring | 🟢 | Cross-functional partnering; prepare STAR stories | Interview prep |

## Positioning statement (use in interviews)

> "I've spent 14 years moving from building software to securing it, and the last few years securing AI in production at TransUnion — Model Armor for LLM apps, MCP-based security agents, and access control for multi-agent workflows on GCP. I bring the builder's view of how agents actually get wired to tools and identities, and I've been deliberately extending that into SaaS posture and non-human identity, which is where agent risk increasingly lives."
