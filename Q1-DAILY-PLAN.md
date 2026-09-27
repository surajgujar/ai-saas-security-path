# Q1 Day-by-Day Plan (28 Sep – 20 Dec 2026)

Rhythm: **1 h Mon–Fri · 3 h Sat · 3 h Sun = 11 h/week** (build 4.5 · learn 2.5 · lead 2.5 · career 1.5).
Track it daily on the tracker page; 7 AM plan + 9:30 PM check-in reminders.

## Week 1 — LLM internals (from 2026-09-28)
Detail: [`weeks/week-01-llm-internals.md`](weeks/week-01-llm-internals.md)

**Mon 2026-09-28** (1h)
- [ ] `learn` Video: 3Blue1Brown Neural Networks ch.5–6 (Transformers, Attention) *(60 min)*

**Tue 2026-09-29** (1h)
- [ ] `learn` Video: Karpathy 'Intro to Large Language Models' (full talk, note the security section) *(60 min)*

**Wed 2026-09-30** (1h)
- [ ] `learn` Read: Hugging Face PEFT/LoRA conceptual guide + quantization overview *(30 min)*
- [ ] `career` Resume v2: add your people management (team size, hiring, reviews, budget) to each relevant role *(30 min)*

**Thu 2026-10-01** (1h)
- [ ] `lead` Draft LinkedIn post #1: why you're going deep on AI & agent security (the next 12 months) *(60 min)*

**Fri 2026-10-02** (1h)
- [ ] `lead` Publish this week's LinkedIn post (edit Thursday's draft, add a diagram or screenshot) *(30 min)*
- [ ] `career` Answer this week's interview questions out loud and record them (weeks/week-01-llm-internals.md) *(30 min)*

**Sat 2026-10-03** (3h)
- [ ] `build` Colab setup; tokenize the same text with GPT-2 and Gemma tokenizers, incl. a homoglyph variant *(90 min)*
- [ ] `build` Embeddings: all-MiniLM-L6-v2 cosine similarity for 5 benign vs 5 injection prompts; plot *(90 min)*

**Sun 2026-10-04** (3h)
- [ ] `build` LoRA fine-tune a tiny model with a trigger phrase (backdoor demo); commit labs/01-llm-internals *(90 min)*
- [ ] `lead` notes/week-01.md: lifecycle diagram (data → pre-train → fine-tune → eval → deploy) annotated with OWASP risks *(60 min)*
- [ ] `career` Weekly review: log hours in the tracker, note what slipped, glance at next week *(30 min)*

## Week 2 — RAG, agents, MCP/A2A (from 2026-10-05)
Detail: [`weeks/week-02-rag-agents.md`](weeks/week-02-rag-agents.md)

**Mon 2026-10-05** (1h)
- [ ] `learn` Video: Google ADK quickstart + multi-agent walkthrough *(60 min)*

**Tue 2026-10-06** (1h)
- [ ] `learn` Video/Docs: LangGraph concepts (state, tools, human-in-the-loop) + podcast: Latent Space episode on MCP *(60 min)*

**Wed 2026-10-07** (1h)
- [ ] `learn` Read: MCP 2026-07-28 spec security & authorization pages; A2A overview *(30 min)*
- [ ] `career` Resume v2 finished: 1-line positioning 'AI & agent security leader…', outcomes with metrics *(30 min)*

**Thu 2026-10-08** (1h)
- [ ] `lead` Rebuild LinkedIn headline, About and Featured (link this repo); open-to-relocation (recruiters only) *(60 min)*

**Fri 2026-10-09** (1h)
- [ ] `lead` Publish this week's LinkedIn post (edit Thursday's draft, add a diagram or screenshot) *(30 min)*
- [ ] `career` Answer this week's interview questions out loud and record them (weeks/week-02-rag-agents.md) *(30 min)*

**Sat 2026-10-10** (3h)
- [ ] `build` Build HelpDesk Copilot: RAG over ~20 docs in Chroma (incl. one confidential HR doc and one hidden-instruction doc) *(90 min)*
- [ ] `build` Add agent with 3 tools (search_docs, send_email mock, read_ticket mock) *(90 min)*

**Sun 2026-10-11** (3h)
- [ ] `build` Expose one tool via a local MCP server; add second agent (triage → resolver); Mermaid diagram; commit labs/02 *(90 min)*
- [ ] `lead` notes/week-02.md: trust boundaries in your app and the 'lethal trifecta' *(60 min)*
- [ ] `career` Weekly review: log hours in the tracker, note what slipped, glance at next week *(30 min)*

## Week 3 — Threat frameworks (from 2026-10-12)
Detail: [`weeks/week-03-threat-frameworks.md`](weeks/week-03-threat-frameworks.md)

**Mon 2026-10-12** (1h)
- [ ] `learn` Read/Video: OWASP LLM Top 10 2026 (what changed vs 2025) + Agent Control Standard v0.1 *(60 min)*

**Tue 2026-10-13** (1h)
- [ ] `learn` Explore: MITRE ATLAS matrix + 3 case studies; podcast: AI Security Podcast *(60 min)*

**Wed 2026-10-14** (1h)
- [ ] `learn` Skim: OWASP Agentic Top 10 + Google SAIF risk map *(30 min)*
- [ ] `career` STAR stories 1–3 (include 2 people-leadership stories: hiring, underperformer) *(30 min)*

**Thu 2026-10-15** (1h)
- [ ] `lead` At work: propose leading an AI security working group; draft LinkedIn post #2 on OWASP 2026 changes *(60 min)*

**Fri 2026-10-16** (1h)
- [ ] `lead` Publish this week's LinkedIn post (edit Thursday's draft, add a diagram or screenshot) *(30 min)*
- [ ] `career` Answer this week's interview questions out loud and record them (weeks/week-03-threat-frameworks.md) *(30 min)*

**Sat 2026-10-17** (3h)
- [ ] `build` Threat model your Week 2 app: DFD with trust boundaries *(90 min)*
- [ ] `build` 15+ threats table with OWASP 2026 + ATLAS IDs, likelihood, impact, control *(90 min)*

**Sun 2026-10-18** (3h)
- [ ] `build` Turn it into a reusable TEMPLATE.md for product teams; commit labs/03 *(90 min)*
- [ ] `lead` notes/week-03.md: how you'd assess a new AI product in 2 weeks *(60 min)*
- [ ] `career` Weekly review: log hours in the tracker, note what slipped, glance at next week *(30 min)*

## Week 4 — Prompt injection & red-teaming (from 2026-10-19)
Detail: [`weeks/week-04-prompt-injection-redteam.md`](weeks/week-04-prompt-injection-redteam.md)

**Mon 2026-10-19** (1h)
- [ ] `learn` Video: Microsoft AI Red Team lessons + Simon Willison talks on prompt injection *(60 min)*

**Tue 2026-10-20** (1h)
- [ ] `learn` Practice: Lakera Gandalf levels 1–7 *(60 min)*

**Wed 2026-10-21** (1h)
- [ ] `learn` Practice: PortSwigger Web Security Academy 'Web LLM attacks' labs (2 labs) *(30 min)*
- [ ] `career` STAR stories 4–6 (include conflict with a stakeholder, growing someone on your team) *(30 min)*

**Thu 2026-10-22** (1h)
- [ ] `lead` Start mentoring 1 colleague on AI security (first 30-min session); draft post #3 *(60 min)*

**Fri 2026-10-23** (1h)
- [ ] `lead` Publish this week's LinkedIn post (edit Thursday's draft, add a diagram or screenshot) *(30 min)*
- [ ] `career` Answer this week's interview questions out loud and record them (weeks/week-04-prompt-injection-redteam.md) *(30 min)*

**Sat 2026-10-24** (3h)
- [ ] `build` promptfoo red-team config against your Week 2 app (OWASP plugins); run it *(90 min)*
- [ ] `build` garak probe run against the model endpoint *(90 min)*

**Sun 2026-10-25** (3h)
- [ ] `build` Manual indirect-injection test on your own app; write REPORT.md with baseline attack-success rate; commit labs/04 *(90 min)*
- [ ] `lead` notes/week-04.md: why classifiers alone aren't enough *(60 min)*
- [ ] `career` Weekly review: log hours in the tracker, note what slipped, glance at next week *(30 min)*

## Week 5 — Poisoning, extraction, supply chain (from 2026-10-26)
Detail: [`weeks/week-05-poisoning-extraction-supplychain.md`](weeks/week-05-poisoning-extraction-supplychain.md)

**Mon 2026-10-26** (1h)
- [ ] `learn` Video/Read: model supply-chain risks (pickle, safetensors) + OpenSSF model-signing overview *(60 min)*

**Tue 2026-10-27** (1h)
- [ ] `learn` Read: CoSAI 'Signing ML Artifacts' + Anthropic Sep 2026 threat report (distillation, stolen API keys) *(60 min)*

**Wed 2026-10-28** (1h)
- [ ] `learn` Podcast: Risky Business or CyberWire episode on AI supply chain; skim SLSA levels *(30 min)*
- [ ] `career` Ask your manager about sponsorship for CISSP (Q1 2027) and ISACA AAISM (Q2 2027) *(30 min)*

**Thu 2026-10-29** (1h)
- [ ] `lead` Draft post #4: 'How to prove the model in prod is the one you approved' *(60 min)*

**Fri 2026-10-30** (1h)
- [ ] `lead` Publish this week's LinkedIn post (edit Thursday's draft, add a diagram or screenshot) *(30 min)*
- [ ] `career` Answer this week's interview questions out loud and record them (weeks/week-05-poisoning-extraction-supplychain.md) *(30 min)*

**Sat 2026-10-31** (3h)
- [ ] `build` Benign pickle PoC detected with modelscan + fickling; convert to safetensors *(90 min)*
- [ ] `build` Sign and verify a model with model_signing; tamper test *(90 min)*

**Sun 2026-11-01** (3h)
- [ ] `build` CycloneDX ML-BOM + GitHub Action gate (scan → verify → eval → deploy); commit labs/05 *(90 min)*
- [ ] `lead` notes/week-05.md: model intake policy for product teams *(60 min)*
- [ ] `career` Weekly review: log hours in the tracker, note what slipped, glance at next week *(30 min)*

## Week 6 — Guardrails & secure agent design (from 2026-11-02)
Detail: [`weeks/week-06-guardrails-design-patterns.md`](weeks/week-06-guardrails-design-patterns.md)

**Mon 2026-11-02** (1h)
- [ ] `learn` Read: 'Design Patterns for Securing LLM Agents against Prompt Injections' *(60 min)*

**Tue 2026-11-03** (1h)
- [ ] `learn` Read/Video: CaMeL (DeepMind) + Microsoft Spotlighting *(60 min)*

**Wed 2026-11-04** (1h)
- [ ] `learn` Compare: Model Armor vs NeMo Guardrails vs Llama Guard / Prompt Guard *(30 min)*
- [ ] `career` Target list: 20 employers in UK / Ireland / Germany (FS, tech/AI, healthcare) *(30 min)*

**Thu 2026-11-05** (1h)
- [ ] `lead` Draft post #5: 'Guardrails are not authorization' *(60 min)*

**Fri 2026-11-06** (1h)
- [ ] `lead` Publish this week's LinkedIn post (edit Thursday's draft, add a diagram or screenshot) *(30 min)*
- [ ] `career` Answer this week's interview questions out loud and record them (weeks/week-06-guardrails-design-patterns.md) *(30 min)*

**Sat 2026-11-07** (3h)
- [ ] `build` Add input/output filtering + spotlighting to your app *(90 min)*
- [ ] `build` Plan-then-execute + human approval for external send_email *(90 min)*

**Sun 2026-11-08** (3h)
- [ ] `build` Re-run Week 4 red-team → before/after table; write GUARDRAIL-REFERENCE.md; commit labs/06 *(90 min)*
- [ ] `lead` notes/week-06.md: trade-offs of latency vs safety *(60 min)*
- [ ] `career` Weekly review: log hours in the tracker, note what slipped, glance at next week *(30 min)*

## Week 7 — Agent identity & runtime authz (from 2026-11-09)
Detail: [`weeks/week-07-agent-identity-authz.md`](weeks/week-07-agent-identity-authz.md)

**Mon 2026-11-09** (1h)
- [ ] `learn` Read: RFC 8693 token exchange (delegation vs impersonation) + OWASP NHI Top 10 *(60 min)*

**Tue 2026-11-10** (1h)
- [ ] `learn` Video/Docs: Google Agent Identity (SPIFFE), Agent Gateway, Principal Access Boundary (Next '26) *(60 min)*

**Wed 2026-11-11** (1h)
- [ ] `learn` Skim: IETF draft-ietf-wimse-aims + CoSAI 'Agentic IAM'; Entra Agent ID overview *(30 min)*
- [ ] `career` Target list to 40: add Netherlands, UAE, Singapore; set job alerts for Head/Lead AI Security titles *(30 min)*

**Thu 2026-11-12** (1h)
- [ ] `lead` Draft post #6: 'Your AI agent needs an identity (on GCP)' with a sequence diagram *(60 min)*

**Fri 2026-11-13** (1h)
- [ ] `lead` Publish this week's LinkedIn post (edit Thursday's draft, add a diagram or screenshot) *(30 min)*
- [ ] `career` Answer this week's interview questions out loud and record them (weeks/week-07-agent-identity-authz.md) *(30 min)*

**Sat 2026-11-14** (3h)
- [ ] `build` Keycloak in Docker in front of your MCP server *(90 min)*
- [ ] `build` Token exchange: user-delegated, down-scoped, ≤5-min tokens *(90 min)*

**Sun 2026-11-15** (3h)
- [ ] `build` OPA policy on every tool call; show an authz-layer denial of an unsafe action; log decisions; commit labs/07 *(90 min)*
- [ ] `lead` notes/week-07.md: should an agent have its own identity, the user's, or both? *(60 min)*
- [ ] `career` Weekly review: log hours in the tracker, note what slipped, glance at next week *(30 min)*

## Week 8 — Securing AI on GCP (from 2026-11-16)
Detail: [`weeks/week-08-gcp-ai-workloads.md`](weeks/week-08-gcp-ai-workloads.md)

**Mon 2026-11-16** (1h)
- [ ] `learn` Docs: Vertex AI security (VPC-SC, PSC, CMEK) + SCC AI Protection *(60 min)*

**Tue 2026-11-17** (1h)
- [ ] `learn` Video: Google Cloud Next '26 security keynote/sessions on agents + Wiz AI-APP *(60 min)*

**Wed 2026-11-18** (1h)
- [ ] `learn` Docs: org policies for Vertex AI; Model Armor floor settings refresh *(30 min)*
- [ ] `career` STAR stories 7–10; rehearse 2 out loud and record *(30 min)*

**Thu 2026-11-19** (1h)
- [ ] `lead` Identify 3 people to ask for recommendation letters later; draft post #7 *(60 min)*

**Fri 2026-11-20** (1h)
- [ ] `lead` Publish this week's LinkedIn post (edit Thursday's draft, add a diagram or screenshot) *(30 min)*
- [ ] `career` Answer this week's interview questions out loud and record them (weeks/week-08-gcp-ai-workloads.md) *(30 min)*

**Sat 2026-11-21** (3h)
- [ ] `build` Terraform: project + VPC-SC perimeter + CMEK + private endpoint *(90 min)*
- [ ] `build` Least-privilege SAs per stage + WIF for CI *(90 min)*

**Sun 2026-11-22** (3h)
- [ ] `build` Checkov/conftest in CI; locked log sink; control-to-threat table; commit labs/08 *(90 min)*
- [ ] `lead` notes/week-08.md: what VPC-SC protects that IAM doesn't *(60 min)*
- [ ] `career` Weekly review: log hours in the tracker, note what slipped, glance at next week *(30 min)*

## Week 9 — SSPM, CASB, Shadow AI (from 2026-11-23)
Detail: [`weeks/week-09-sspm-casb.md`](weeks/week-09-sspm-casb.md)

**Mon 2026-11-23** (1h)
- [ ] `learn` Read: SSPM vs CASB vs SSE vs CSPM; build a 1-page comparison *(60 min)*

**Tue 2026-11-24** (1h)
- [ ] `learn` Read: CISA SCuBA baselines (Workspace / M365) + Salesloft Drift incident write-ups *(60 min)*

**Wed 2026-11-25** (1h)
- [ ] `learn` Podcast/Read: Shadow AI discovery approaches; Gartner stat on personal GenAI use *(30 min)*
- [ ] `career` Book the CISSP exam for March 2027; get the Official Study Guide + practice-test app *(30 min)*

**Thu 2026-11-26** (1h)
- [ ] `lead` Draft post #8: 'Shadow AI without blocking everything' *(60 min)*

**Fri 2026-11-27** (1h)
- [ ] `lead` Publish this week's LinkedIn post (edit Thursday's draft, add a diagram or screenshot) *(30 min)*
- [ ] `career` Answer this week's interview questions out loud and record them (weeks/week-09-sspm-casb.md) *(30 min)*

**Sat 2026-11-28** (3h)
- [ ] `build` Run ScubaGoggles or ScubaGear/Maester on a trial tenant *(90 min)*
- [ ] `build` Python drift detector (snapshot → git → diff → alert) *(90 min)*

**Sun 2026-11-29** (3h)
- [ ] `build` Shadow AI discovery mock from proxy logs + 20-control SSPM catalogue; commit labs/09 *(90 min)*
- [ ] `lead` notes/week-09.md: rolling out SSPM across 300 SaaS apps *(60 min)*
- [ ] `career` Weekly review: log hours in the tracker, note what slipped, glance at next week *(30 min)*

## Week 10 — SaaS identity, OAuth, API security (from 2026-11-30)
Detail: [`weeks/week-10-saas-identity-api.md`](weeks/week-10-saas-identity-api.md)

**Mon 2026-11-30** (1h)
- [ ] `learn` Read: OAuth 2.0/2.1 + RFC 9700 BCP; SCIM & JML failure modes *(60 min)*

**Tue 2026-12-01** (1h)
- [ ] `learn` Read: OWASP API Security Top 10 (2023) + how agents make BOLA/BFLA worse *(60 min)*

**Wed 2026-12-02** (1h)
- [ ] `learn` CISSP: Domain 1 (Security & Risk Management) video lessons *(30 min)*
- [ ] `career` CISSP: 50 practice questions (Domain 1) *(30 min)*

**Thu 2026-12-03** (1h)
- [ ] `lead` Draft post #9: 'Why access survives offboarding' *(60 min)*

**Fri 2026-12-04** (1h)
- [ ] `lead` Publish this week's LinkedIn post (edit Thursday's draft, add a diagram or screenshot) *(30 min)*
- [ ] `career` Answer this week's interview questions out loud and record them (weeks/week-10-saas-identity-api.md) *(30 min)*

**Sat 2026-12-05** (3h)
- [ ] `build` OAuth grant auditor (Workspace Admin SDK or Graph), dry-run revocation *(90 min)*
- [ ] `build` JML simulator: leaver revokes sessions, refresh tokens, grants *(90 min)*

**Sun 2026-12-06** (3h)
- [ ] `build` OWASP crAPI: document 5 API Top 10 findings on your local instance; commit labs/10 *(90 min)*
- [ ] `lead` notes/week-10.md: the 1-hour leaver checklist across 50 SaaS apps *(60 min)*
- [ ] `career` Weekly review: log hours in the tracker, note what slipped, glance at next week *(30 min)*

## Week 11 — Telemetry, detection, audit trails (from 2026-12-07)
Detail: [`weeks/week-11-telemetry-detection.md`](weeks/week-11-telemetry-detection.md)

**Mon 2026-12-07** (1h)
- [ ] `learn` Read: OpenTelemetry GenAI semantic conventions + OCSF basics *(60 min)*

**Tue 2026-12-08** (1h)
- [ ] `learn` Read: Anthropic AI-orchestrated espionage report — defender recommendations *(60 min)*

**Wed 2026-12-09** (1h)
- [ ] `learn` CISSP: Domain 2 (Asset Security) video lessons *(30 min)*
- [ ] `career` CISSP: 50 practice questions (Domain 2) *(30 min)*

**Thu 2026-12-10** (1h)
- [ ] `lead` Pitch a talk to OWASP Pune / null Pune / BSides for Q1 2027: 'Identity for AI agents' *(60 min)*

**Fri 2026-12-11** (1h)
- [ ] `lead` Publish this week's LinkedIn post (edit Thursday's draft, add a diagram or screenshot) *(30 min)*
- [ ] `career` Answer this week's interview questions out loud and record them (weeks/week-11-telemetry-detection.md) *(30 min)*

**Sat 2026-12-12** (3h)
- [ ] `build` Instrument your app with OpenTelemetry (Jaeger locally) *(90 min)*
- [ ] `build` Hash-chained audit log + tamper-check script *(90 min)*

**Sun 2026-12-13** (3h)
- [ ] `build` Write 6 Sigma/YARA-L detections; replay Week 4 tests; SOC runbook; commit labs/11 *(90 min)*
- [ ] `lead` notes/week-11.md: what a SOC needs to see in an agent incident *(60 min)*
- [ ] `career` Weekly review: log hours in the tracker, note what slipped, glance at next week *(30 min)*

## Week 12 — GRC & strategy capstone (from 2026-12-14)
Detail: [`weeks/week-12-grc-strategy.md`](weeks/week-12-grc-strategy.md)

**Mon 2026-12-14** (1h)
- [ ] `learn` Read: NIST AI RMF + GenAI profile (AI 600-1) summary; ISO/IEC 42001 structure *(60 min)*

**Tue 2026-12-15** (1h)
- [ ] `learn` Read: EU AI Act timeline after the Omnibus (Annex III → 2 Dec 2027) + AAISM exam outline *(60 min)*

**Wed 2026-12-16** (1h)
- [ ] `learn` CISSP: Domain 3 (Security Architecture) video lessons *(30 min)*
- [ ] `career` Q1 retrospective in the tracker; confirm Q2 plan (job search opens in January) *(30 min)*

**Thu 2026-12-17** (1h)
- [ ] `lead` Draft post #12: Q1 recap with portfolio link *(60 min)*

**Fri 2026-12-18** (1h)
- [ ] `lead` Publish this week's LinkedIn post (edit Thursday's draft, add a diagram or screenshot) *(30 min)*
- [ ] `career` Answer this week's interview questions out loud and record them (weeks/week-12-grc-strategy.md) *(30 min)*

**Sat 2026-12-19** (3h)
- [ ] `build` Write the AI & SaaS Security Standard (8–10 pages) *(90 min)*
- [ ] `build` AI system intake & risk questionnaire *(90 min)*

**Sun 2026-12-20** (3h)
- [ ] `build` 12-month roadmap + KPI set; update README definition-of-done; commit labs/12 *(90 min)*
- [ ] `lead` notes/week-12.md: how you'd build an AI security program in year one *(60 min)*
- [ ] `career` Weekly review: log hours in the tracker, note what slipped, glance at next week *(30 min)*
