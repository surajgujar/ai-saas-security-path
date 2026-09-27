# Week 9 — SSPM, CASB, Shadow SaaS / Shadow AI, SaaS DLP (23 – 29 Nov)

**Why (JD):** "SSPM, CASB, and modern SaaS security control planes for misconfiguration and drift detection, third-party OAuth/integration governance, Shadow SaaS / Shadow AI discovery, and DLP across the SaaS estate"
**Goal:** Close your **biggest gap**. Bridge from CSPM (Wiz) → SSPM: same idea, different control plane (SaaS admin APIs instead of cloud APIs).

## Learn (3 h)
- [ ] Concepts: SSPM vs CASB vs SSE/SASE vs CSPM vs ITDR — make a 1-page comparison table
- [ ] CASB modes: API (out-of-band) vs forward/reverse proxy (inline); log-based discovery
- [ ] Vendor landscape (read one product overview each): **AppOmni, Obsidian, Adaptive Shield (CrowdStrike), Valence, Microsoft Defender for Cloud Apps, Netskope, Zscaler, Palo Alto** — note which are SSPM vs CASB vs both
- [ ] Baselines: **CISA SCuBA** (Secure Cloud Business Applications) baselines for M365 & Google Workspace; CIS Benchmarks for M365 / Google Workspace; Salesforce Security Health Check
- [ ] Shadow AI: discovery via CASB/SWG logs, OAuth grants, browser extensions; AI app risk scoring; "sanctioned / tolerated / blocked" model
- [ ] SaaS DLP: Google Workspace DLP, Microsoft Purview DLP, CASB inline DLP; DLP for prompts to GenAI apps
- [ ] Case studies: Snowflake customer breaches (2024 — no MFA, infostealer creds), Salesloft Drift OAuth token compromise (2025) — understand the kill chain

## Lab (4 h) → `labs/09-sspm/`
Free options: Google Workspace trial / Salesforce Developer Edition / Microsoft 365 dev tenant if you can get one.
- [ ] Run **ScubaGoggles** (Google Workspace) or **ScubaGear** / **Maester** (M365) → baseline report
- [ ] Write a small Python **drift detector**: snapshot N security settings via admin API → store JSON in Git → diff daily → alert (GitHub Action on schedule)
- [ ] Shadow AI discovery mock: parse a sample proxy/DNS log CSV, match against a list of GenAI domains, produce risk-ranked report
- [ ] Doc: *SSPM control catalogue* — 20 controls (MFA/SSO enforced, external sharing, admin count, OAuth app allow-list, audit logging, session length…) with severity

## Interview questions
1. What's the difference between SSPM and CASB, and would Siemens need both?
2. How would you roll out SSPM across 300+ SaaS apps with limited team capacity? (tiering by data sensitivity/users)
3. How do you handle Shadow AI without just blocking everything?
4. Walk through the Salesloft Drift incident — which controls would have limited blast radius?

## Done when
- [ ] Baseline report, drift detector, control catalogue committed
