# Lab 12: AI & SaaS security standard + roadmap (capstone)

**Goal:** turn 11 labs of hands-on work into the leadership artefacts a Head of AI Security is hired to produce: a written standard, an intake questionnaire, a 12-month roadmap and a metrics set. This is what you show in interviews.

**Prepares you for:** "How would you build an AI security program in year one?" "Show me your AI security standard."

**Time:** core 4.5 h. **No code** — four documents. Pull directly from your own Labs 3–11.

## Core steps

### Step 1: AI & SaaS Security Standard (2 h) → `STANDARD.md` (8–10 pages)
- Scope and roles (who owns what)
- **Mandatory controls**, reusing your Labs 6–11 control IDs: guardrails, per-tool authorization, model signing, secure GCP baseline, SSPM, telemetry/audit
- Exceptions process (how a team gets a time-boxed waiver)
- Mapping to NIST AI RMF, ISO/IEC 42001, EU AI Act and OWASP LLM/Agentic — a crosswalk table

### Step 2: AI system intake & risk questionnaire (60 min) → `INTAKE.md`
A form a business team fills before shipping an AI feature: data classes touched, autonomy level, tools/actions, external exposure, model source. Each answer routes to the relevant control from the standard. Reuse your Lab 3 threat template.

### Step 3: 12-month roadmap (45 min) → `ROADMAP.md`
- Q1: visibility — AI & SaaS inventory, Shadow AI discovery (Lab 9)
- Q2: guardrails & identity baseline (Labs 6, 7)
- Q3: SSPM rollout, red-team program (Labs 4, 9)
- Q4: audit readiness & metrics
Phrase it as what *you* would do in a first year leading the program, with dependencies.

### Step 4: metrics / KPIs (30 min) → add to `ROADMAP.md`
% AI apps assessed · ASR trend (from Labs 4/6) · % SaaS apps under SSPM · OAuth grants reviewed · mean time to deprovision · non-human identities with a named owner. For each: how it's measured and the target direction.

### Step 5: close the loop (15 min)
Update the repo's top [README](../../README.md) "definition of done" checklist, and link your 12 labs as the portfolio.

## Stretch
- Add a one-page board summary (risk in business terms, budget ask, 3 priorities).
- Map the standard to one sector: UK PRA SS1/23 + DORA for financial services (your primary sector).

## Done when
- [ ] `STANDARD.md` (8–10 pages) with the control crosswalk
- [ ] `INTAKE.md` questionnaire
- [ ] `ROADMAP.md` with the 12-month plan and KPIs
- [ ] Repo README definition-of-done updated, 12 labs linked
- [ ] Committed to `labs/12-standard-and-roadmap/`

## If it breaks
| Symptom | Fix |
|---|---|
| Blank-page paralysis | Don't invent controls — lift them from your own Labs 6–11 and write down what you actually built. The standard *documents* your labs. |
| Crosswalk feels fake | It's fine to map a control to "partially addresses" a framework clause; say so. Honesty reads as senior. |
