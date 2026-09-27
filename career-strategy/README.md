# AI Security Career Strategy — Market Research & 12-Month Niche Plan

Researched: 27 Sep 2026 · Horizon: Oct 2026 → Sep 2027 · Pace: ~8 hrs/week

The 12-week plan in `weeks/` is **Stage 1** (broad foundation + Siemens-type interviews). This document is the bigger picture: what the market is paying for, which niche you should own, and three 3-month "spikes" to get there.

---

## 1. What the market is saying (evidence)

| Signal | What it means for you | Source |
|---|---|---|
| Analysis of 100+ AI security job listings: most-wanted profile is a **"hybrid defender"** — offensive AI (red-teaming, prompt injection) + cloud architecture/IAM + Python/Go engineering. Four hot domains: **agentic AI security, SecMLOps (ML supply chain, RAG), cloud-native AI platforms (Vertex/Bedrock/Azure OpenAI), risk-as-code (EU AI Act, NIST AI RMF)** | You already have cloud + IAM + engineering. The **offensive** piece is the missing third leg | [OGOU job-listing analysis](https://blog.ogwilliam.com/post/ai-cybersecurity-job-market-2026) |
| **MCP is a new attack surface.** 30+ MCP CVEs filed in 60 days in early 2026; in scans, 82% of servers had path traversal and 43% had command injection. Only **8.5%** of 5,200 servers used OAuth; 53% used static keys. First malicious MCP package (postmark-mcp) in Sep 2025 | Very few people can both **build** and **secure** MCP. You already built MCP security agents in production — this is your wedge | [Practical DevSecOps MCP stats](https://www.practical-devsecops.com/mcp-security-statistics-2026-report/), [CSA research note](https://labs.cloudsecurityalliance.org/research/csa-research-note-mcp-tool-poisoning-auto-execution-20260701/), [Invariant Labs](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks) |
| **Agent identity / non-human identity (NHI) is where the money is going.** Palo Alto bought CyberArk (~$25B); ServiceNow bought Veza; CrowdStrike bought SGNL; Saviynt raised ~$1B. "97% of NHIs carry excessive privileges" | Identity for agents is the biggest-budget niche, and it's your strongest existing skill (workload identity, multi-agent access control) | [Software Strategies M&A roundup](https://softwarestrategiesblog.com/2026/03/28/agentic-ai-security-startups-funding-mna-rsac-2026/), [Software Analyst on agent ISPM](https://softwareanalyst.substack.com/p/why-cisos-must-re-think-identity) |
| **AI security startups are being absorbed into platforms:** Protect AI → Palo Alto, Lakera → Check Point, Robust Intelligence → Cisco, Pangea → CrowdStrike, CalypsoAI → F5, Aim → Cato. **Wiz → Alphabet ($32B)** | (a) Your Wiz + GCP + Model Armor combination is now one Google stack, which makes you rare. (b) Demand is shifting toward **vendor-neutral consulting**: AI inventory/Shadow AI, red-team evidence, EU AI Act mapping | [DeviDevs](https://devidevs.com/blog/2026-03-19-ai-security-acquisition-wave), [SecurityWeek on Lakera](https://www.securityweek.com/check-point-to-acquire-ai-security-firm-lakera/), [TechRadar on Pangea](https://techradar.com/pro/security/crowdstrike-snaps-up-pangea-to-boost-ai-security) |
| **Top roles and bands (US figures):** AI Security Architect $200–280K+, LLM Security Engineer $160–230K, Adversarial ML $160–225K, AI GRC $130–190K. Frontier-lab AI red-team roles go up to $320–485K | "Architect" is your natural title, and it's among the best paid. Treat these as direction, not India numbers | [Practical DevSecOps roles](https://www.practical-devsecops.com/emerging-ai-security-roles/), [Anthropic Frontier Red Team posting](https://job-boards.greenhouse.io/anthropic/jobs/5076477008) |
| **Certifications are catching up.** SANS/GIAC now offer SEC545 (GenAI & LLM app security, **GAIPS**), SEC535 (Offensive AI, **GOAA**) and SEC598 (AI security automation, **GASAE**), with more AI certs due through 2026 | One well-chosen cert adds credibility, but a portfolio matters more | [GIAC AI focus area](https://www.giac.org/focus-areas/artificial-intelligence) |
| **Industrial/OT + agentic AI is under-served.** Attacks on manufacturers were up 56% (2024→25); leaders are over-confident in AI SOCs versus measured results; SANS flags an OT skills crisis | This is a less crowded niche and fits employers like Siemens, Schneider, ABB and Honeywell | [ManufacturingTomorrow](https://www.manufacturingtomorrow.com/article/2026/09/the-state-of-agentic-cybersecurity-in-manufacturing/28024), [Industrial Cyber / SANS](https://industrialcyber.co/reports/sans-2026-report-flags-cybersecurity-skills-crisis-putting-critical-infrastructure-and-ot-sectors-at-measurable-breach-risk/) |
| India: GCCs (global capability centres) are driving AI/ML + cybersecurity hiring in Bengaluru, Hyderabad and Pune | Pune GCCs plus remote EU/US roles are your realistic targets | [EOR Services India](https://www.eorservicesindia.com/gccs-startups-bengaluru-hyderabad-ai-ml-cybersecurity-jobs-opportunities-2026/), [Savannah HR](https://savannahr.com/blog/top-8-gcc-skills-india-2026) |

> Caveat: several sources are training vendors or blogs with an interest in the story. The acquisitions, CVE counts and the GIAC catalogue are hard facts; salary bands and "demand" claims are directional.

---

## 2. Your niche (the recommendation)

### Primary identity: **"Agentic AI Identity & Runtime Security Architect"**
*The person who can design how AI agents authenticate, what they're allowed to do at runtime, how their tools (MCP) are trusted, and prove it with logs — on GCP, at enterprise scale.*

Why this and not "general AI security":

1. **Where the market is going:** Agent identity + MCP + NHI is where the biggest acquisitions, the newest CVEs and the worst posture gaps are.
2. **Where you're already ahead:** You have production MCP agents, multi-agent access control, workload identity, a PCSE, Model Armor and Wiz. Most AI security candidates come from either ML or AppSec; very few come from cloud identity plus agent building.
3. **Where supply is thin:** Only 8.5% of MCP servers use OAuth, so few people have actually implemented agent OAuth, token exchange and per-tool authorization end to end.

### Two supporting "spikes" (T-shaped profile)
- **Offensive AI credibility.** You can break what you design. This completes the "hybrid defender" profile the listings ask for.
- **Risk-as-code for AI governance.** EU AI Act, ISO 42001 and NIST AI RMF evidence produced by pipelines, not questionnaires. This is what makes you a *strategy* hire, not just an engineer.

### Optional differentiator
- **Industrial / OT AI security.** Choose this only if you target Siemens-like industrial companies. It's high value and low competition, but narrower.

### Roles this unlocks (fit today → after the plan)

| Role | Fit now | After 12 months |
|---|---|---|
| AI Security Architect / SME (e.g. Siemens) | 🟡 | 🟢 |
| Agentic AI / AI Platform Security Engineer | 🟢 | 🟢 strong |
| Agent identity / NHI product or solutions architect (Google, Palo Alto/CyberArk, CrowdStrike, Saviynt, Okta) | 🟡 | 🟢 |
| AI Red Team Engineer | 🔴 | 🟡 |
| AI GRC Engineer / AI governance lead | 🟡 | 🟢 |
| Independent AI security consultant / founder | 🟡 | 🟢 (see §5) |

---

## 3. The 12-month plan

| Stage | Months | Theme | Output that proves it |
|---|---|---|---|
| **1** | Oct–Dec 2026 | **Foundation**: the 12-week plan in `weeks/` | 12 labs, interview-ready |
| **2** | Jan–Mar 2027 | **Spike A: agent identity & MCP security** (primary niche) → [`tracks/track-a-agent-identity-mcp.md`](../tracks/track-a-agent-identity-mcp.md) | Open-source MCP security tool + reference architecture + 1 talk |
| **3** | Apr–Jun 2027 | **Spike B: offensive AI** → [`tracks/track-b-offensive-ai.md`](../tracks/track-b-offensive-ai.md) | Responsible disclosures / CVEs in MCP or AI OSS, red-team competition results |
| **4** | Jul–Sep 2027 | **Spike C: AI risk-as-code** (+ optional OT) → [`tracks/track-c-ai-grc-as-code.md`](../tracks/track-c-ai-grc-as-code.md) | EU AI Act / ISO 42001 evidence pipeline, published |

Running alongside every stage: **visibility** (see §4). Each stage keeps the same weekly rhythm: 2.5 h learn · 4 h build · 0.5 h write · 1 h publish/network.

---

## 4. Visibility engine (1 hr/week, never skip)

In a niche field, being *findable* matters as much as the skill.

- **GitHub:** this repo plus one flagship open-source tool (Stage 2). Pin it.
- **LinkedIn:** one post per week: a lab result, a diagram or an incident breakdown. Short, practical, with a picture. This also doubles as communication practice.
- **Talks:** local chapters of OWASP Pune, null Pune and BSides Pune. Target 1 talk in Stage 2 and 1 in Stage 3. Submit to one international conference CFP (e.g. fwd:cloudsec, BSides, OWASP Global AppSec) by mid-2027.
- **Community work:** contribute to the OWASP GenAI Security Project (Agentic / MCP guidance) or the CSA AI working groups. Your name then appears on the documents interviewers read.
- **Blog series:** "Securing AI agents on GCP", one post per lab.

## 5. Certifications (pick few, pick well)

| When | Cert | Why | Note |
|---|---|---|---|
| Stage 2 | **GIAC GAIPS (SANS SEC545)** *or* a cheaper practitioner AI-security cert | Validates GenAI/LLM app security hands-on | SANS is expensive; ask your employer to sponsor it |
| Stage 3 | **GIAC GOAA (SANS SEC535)**, *optional* | Offensive AI credential | Only if you lean into red-team roles |
| Stage 4 | **IAPP AIGP** *or* **ISO/IEC 42001 Lead Implementer** | Governance credibility for strategy/SME roles | AIGP is better for policy roles; 42001 LI for program/audit roles |

You already hold the GCP PCSE. Keep it current; it's a real differentiator now that Wiz is part of Google.

## 6. Founder/consulting angle

The acquisition wave has left a gap for **vendor-neutral AI security assessments**: AI and Shadow AI inventories, agent/MCP security reviews, red-team reports good enough for insurance and audit, and EU AI Act mapping ([DeviDevs](https://devidevs.com/blog/2026-03-19-ai-security-acquisition-wave)). By Stage 4 your labs *are* a packaged service: threat-model template (W3), red-team method (W4 + Track B), guardrail reference (W6), agent authz pattern (Track A) and compliance pipeline (Track C). You could run that as a boutique practice or as a side offering, with the same productised, repeatable delivery as any business you build.

## 7. Quarterly self-check

- [ ] Could I get an AI Security Architect interview this quarter? (Apply to 3 roles as a test)
- [ ] Did I publish at least 10 posts and 1 substantial artefact?
- [ ] Is my flagship repo getting stars, issues or forks?
- [ ] Is my niche still the right one? Re-read 20 job postings and adjust
