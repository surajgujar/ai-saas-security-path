# AI, Agentic AI & SaaS Security — Learning Path

> **Big picture first:** read [`career-strategy/`](career-strategy/README.md) — deep research on what OpenAI, Anthropic, Google, Microsoft, vendors and enterprises hire for, the next-12-month trends, and your **leadership-track** plan. The 12 weeks below are **Q1** of it.

Target role: **AI & SaaS Security Subject Matter Expert (Siemens)**
Owner: Suraj Gujar · Start: **Mon 28 Sep 2026** · End: **Sun 20 Dec 2026** · Pace: **10–12 hrs/week**

> Track progress in **GitHub Issues** (one issue per week, grouped by milestone/phase). Tick boxes from the GitHub mobile app. This README is the map; `weeks/` holds the detail.

## Where you start (from your resume)

You are **not** starting from zero. You already have: GCP PCSE, IAM hardening, workload identity, Wiz CSPM, Model Armor in production, MCP-based security agents, multi-agent access control, model supply-chain scanning, Terraform/policy-as-code, CI/CD security.

The plan spends **little time** on those and **most time** on the gaps the JD calls out. See [`00-gap-analysis.md`](00-gap-analysis.md).

## The 12 weeks

| Wk | Dates | Phase | Topic | Portfolio deliverable | Status |
|---|---|---|---|---|---|
| 1 | 28 Sep – 4 Oct | 1 · Foundations | [LLM internals: transformers, embeddings, training, fine-tuning, inference](weeks/week-01-llm-internals.md) | Notebook: tokenizer, embeddings, LoRA fine-tune | ⬜ |
| 2 | 5 – 11 Oct | 1 · Foundations | [RAG, vector DBs, agents, multi-agent, MCP/A2A](weeks/week-02-rag-agents.md) | `labs/vuln-agent-app` (your target app) | ⬜ |
| 3 | 12 – 18 Oct | 2 · Assess | [Threat frameworks: OWASP LLM & Agentic Top 10, MITRE ATLAS, NIST AI 100-2](weeks/week-03-threat-frameworks.md) | Threat model of target app | ⬜ |
| 4 | 19 – 25 Oct | 2 · Assess | [Prompt injection, jailbreaks & AI red-teaming (garak, PyRIT, promptfoo)](weeks/week-04-prompt-injection-redteam.md) | Red-team report | ⬜ |
| 5 | 26 Oct – 1 Nov | 2 · Assess | [Poisoning, leakage, model extraction & ML supply chain / provenance](weeks/week-05-poisoning-extraction-supplychain.md) | Model signing + AI-BOM pipeline | ⬜ |
| 6 | 2 – 8 Nov | 3 · Defend | [Guardrails & secure agent design patterns](weeks/week-06-guardrails-design-patterns.md) | Before/after red-team metrics | ⬜ |
| 7 | 9 – 15 Nov | 3 · Defend | [Agent identity, NHI & runtime authorization](weeks/week-07-agent-identity-authz.md) | MCP server with OAuth + OPA per-tool authz | ⬜ |
| 8 | 16 – 22 Nov | 3 · Defend | [Securing AI workloads on GCP (Vertex AI, VPC-SC, CMEK)](weeks/week-08-gcp-ai-workloads.md) | Terraform secure Vertex AI baseline | ⬜ |
| 9 | 23 – 29 Nov | 4 · SaaS | [SSPM, CASB, Shadow SaaS / Shadow AI, SaaS DLP](weeks/week-09-sspm-casb.md) | SaaS posture scan + drift detector | ⬜ |
| 10 | 30 Nov – 6 Dec | 4 · SaaS | [SaaS identity lifecycle (JML), OAuth/OIDC governance, OWASP API Top 10](weeks/week-10-saas-identity-api.md) | OAuth grant auditor + crAPI findings | ⬜ |
| 11 | 7 – 13 Dec | 5 · Operate | [AI/SaaS telemetry, anomaly detection, immutable agent audit trails, SIEM](weeks/week-11-telemetry-detection.md) | OTel-instrumented agent + detections | ⬜ |
| 12 | 14 – 20 Dec | 5 · Govern | [GRC & strategy: NIST AI RMF, ISO 42001, EU AI Act, CRA, SAIF](weeks/week-12-grc-strategy.md) | AI & SaaS security standard + roadmap | ⬜ |

### Q2–Q4 (Jan – Sep 2027): leadership-track quarters

| Quarter | Months | Theme | Cert | Proof |
|---|---|---|---|---|
| Q2 | Jan – Mar 2027 | [Agent identity & runtime authorization (flagship niche)](quarters/q2-agent-identity-runtime-authz.md) | CISSP | OSS gateway + reference architecture + talk + standards contribution |
| Q3 | Apr – Jun 2027 | [Frontier-lab security depth: isolation, agent product reviews, model-weight security, AI-enabled threats](quarters/q3-frontier-lab-security.md) | GIAC GAIPS | Hardening guide, review method, SL3 gap template, talk #2 |
| Q4 | Jul – Sep 2027 | [Leading an AI security program: strategy, metrics, budget, EU AI Act](quarters/q4-ai-security-program-leadership.md) | ISACA AAISM | Program portfolio + interviews abroad |

**Interview prep runs in parallel** — ~1 hr every week. See [`interview-prep/`](interview-prep/).

## Weekly rhythm (11 hrs)

| Block | Time | What |
|---|---|---|
| Learn | 3 h | Reading/videos listed in the week file |
| Build | 5 h | The lab — commit code to `labs/` |
| Leadership & visibility | 2 h | 1-page note in `notes/`, one LinkedIn post, mentoring, strategy memos, talks/standards work |
| Interview & job search | 1 h | Answer that week's questions out loud, record, refine; from Q3, applications and referrals |

## Repo layout

```
career-strategy/         Market research, niche, 12-month plan
quarters/                Q2–Q4 leadership-track plans
00-gap-analysis.md       JD vs. your resume, and what to prioritise
weeks/                   One file per week: goals, resources, lab, checklist, interview Qs
labs/                    Your code — each lab gets a folder
notes/                   Your weekly notes (template inside)
interview-prep/          Question bank, STAR stories, Siemens research, 30-60-90 pitch
resources.md             Consolidated reading list
scripts/                 GitHub bootstrap (labels, milestones, weekly issues)
```

## Definition of done (Week 12)

- [ ] 8+ labs in `labs/` with READMEs (this is your portfolio link for the interview)
- [ ] Can whiteboard an end-to-end AI system threat model (model → training → inference → RAG → agents) mapped to OWASP + ATLAS
- [ ] Can explain agent identity & runtime authz with a working demo
- [ ] Can talk SSPM/CASB fluently: misconfig/drift, OAuth app governance, Shadow AI, DLP
- [ ] Draft "AI & SaaS Security Standard" + 12-month roadmap written
- [ ] 10 STAR stories rehearsed
