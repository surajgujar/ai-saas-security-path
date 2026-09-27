# Track C — AI Risk-as-Code (+ optional Industrial/OT AI) (Jul – Sep 2027)

**Outcome:** Be the engineer who turns AI regulation into automated, auditable controls — the thing that makes you a *strategy / SME* hire rather than only an engineer.

## Month 1 — Regulation & frameworks, deeply
- [ ] EU AI Act — provider vs deployer obligations, GPAI obligations, high-risk requirements (risk mgmt, logging, human oversight, accuracy/robustness/cybersecurity — Art. 15). Verify current application dates (Digital Omnibus changes)
- [ ] ISO/IEC 42001 clauses + Annex A; how it layers on ISO 27001
- [ ] NIST AI RMF + GenAI Profile (AI 600-1); CSA AI Controls Matrix; Google SAIF
- [ ] Cyber Resilience Act + NIS2 touchpoints for AI-enabled products
- [ ] Cert option: IAPP AIGP or ISO 42001 Lead Implementer

## Month 2 — Build "compliance as code" for AI
- [ ] AI system registry schema (owner, purpose, risk tier, models, data, agents, tools, NHIs) — YAML in Git
- [ ] Pipeline that collects evidence automatically: model signature (W5), eval/red-team ASR (W4/Track B), guardrail config (W6), authz policy tests (W7), logging checks (W11) → maps each to EU AI Act / 42001 / NIST controls → generates an audit pack
- [ ] OPA/conftest rules: "no high-risk AI system deploys without human-oversight control + logging + passing eval"
- [ ] Dashboard: coverage per framework

## Month 3 — Optional OT/industrial differentiator (choose if targeting Siemens / industrial)
- [ ] IEC 62443 fundamentals (zones & conduits, security levels) — ISA/IEC 62443 Cybersecurity Fundamentals Specialist cert is a good entry
- [ ] How AI enters OT: predictive maintenance models, industrial copilots, agentic SOC for OT; safety vs security trade-offs; air-gap assumptions
- [ ] Threat model an "industrial copilot" that reads PLC/engineering data and proposes changes — map to ATLAS + 62443
- [ ] Otherwise: use Month 3 to publish the compliance-as-code project and give talk #3

## Done when
- [ ] Evidence pipeline published · [ ] One governance cert or OT fundamentals done · [ ] Final career self-check (README §7)
