# Week 11 — Telemetry, Anomaly Detection, Immutable Agent Audit Trails, SIEM (7 – 13 Dec)

**Why (JD):** "AI and SaaS security telemetry, anomaly detection, immutable audit trails for agentic actions, DLP, and integration with SOC/SIEM/XDR workflows"

## Learn (2.5 h)
- [ ] **OpenTelemetry GenAI semantic conventions** (spans for model calls, agent/tool invocations) + **OCSF** schema — both are what OWASP's Agent Control Standard specifies
- [ ] Anthropic threat-intel reports (Nov 2025 AI-orchestrated espionage; Sep 2026) — what defenders are told to detect
- [ ] What to log for an agent action: who (user + agent identity), what tool, args (redacted), authz decision, model/version, prompt hash, guardrail verdicts, outcome
- [ ] Immutability: GCS Bucket Lock / Cloud Logging bucket with locked retention, WORM storage, hash-chaining / Merkle log concept, separate log project
- [ ] Detection-as-code: **Sigma** rules; **YARA-L 2.0** for Google SecOps (Chronicle); KQL for Sentinel (awareness)
- [ ] SaaS log sources: Workspace/M365 audit logs, OAuth token events, Okta system log
- [ ] Anomaly ideas: tool-call volume spikes, new tool/destination for an agent, off-hours agent activity, guardrail-block bursts, token use from new ASN

## Lab (4 h) → `labs/11-telemetry/`
- [ ] Instrument the hardened Week 6/7 app with OpenTelemetry → export spans/logs (local Jaeger + JSON file, or Cloud Trace/Logging)
- [ ] Hash-chained append-only audit log for agent actions + verifier script that detects tampering
- [ ] Write **6 detections** (Sigma or YARA-L): indirect-injection → exfil attempt, denied-authz burst, agent using unseen tool, OAuth grant with risky scope, mass download after leaver event, guardrail bypass pattern
- [ ] Replay Week 4 attacks → show detections fire
- [ ] Short SOC runbook for "suspected agent compromise"

## Interview questions
1. What would you want in the SOC's view of an AI agent incident?
2. How do you make agent audit logs trustworthy enough for an auditor or regulator?
3. How do you balance logging prompts (evidence) vs. privacy/DLP?

## Done when
- [ ] Instrumented app, audit chain, detections, runbook committed
