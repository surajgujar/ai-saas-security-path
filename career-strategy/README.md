# AI Security Leadership — Deep Research & Strategy

**Researched:** 27 Sep 2026 · **Plan window:** Oct 2026 → Sep 2027
**Your inputs:** leadership track · target frontier AI labs + hyperscalers/security vendors + large enterprises · relocate abroad · 10–12 hrs/week · employer may sponsor courses

> Everything below is based on live postings, standards and product announcements from the last 12 months, and on what is scheduled for the next 12. Where something is still moving (visa litigation, EU AI Act publication, draft standards), it's flagged ⚠️ **verify**.

---

## Part 1 — What leading AI companies are actually hiring for

### 1.1 Frontier AI labs

| Company · role | What they require (verbatim themes) | Pay (US base) | What it tells you |
|---|---|---|---|
| **OpenAI · Engineering Manager, Identity & Access Platform** | Scale access management "for evolving human and **agent** lifecycles"; "first-class authorization for agents and workloads, with delegated, action-scoped permissions, time-bound access, full attribution, no credential sharing"; 10+ yrs building teams; deep IAM, authz, **workload identity** | $347K–$510K | **This is exactly your niche, as a leadership role.** Agent identity is a leadership-level problem at labs |
| **OpenAI · Security Engineer, Agent Security** | Identity, network and **runtime** defences for agents (sandboxing, policy enforcement); "deep expertise in modern **isolation** techniques — container security, kernel-level hardening"; telemetry pipelines; workload identity + IaC | $266K–$445K | ⚠️ **Gap for you:** sandboxing/isolation depth (gVisor, Firecracker, seccomp, kernel hardening) |
| **OpenAI · Offensive Security Engineer, Agent Products** | Pentest agent products: "identity and authorization flows, CI/CD"; "prompt injection, **confused deputies**, unsafe tool use"; K8s, containers, GitHub; 7+ yrs offensive | $347K–$490K | Labs want people who can break agent authz, not just design it |
| **OpenAI · EM, Security Agent Engineering** | Leads a team building **AI agents that do security work** | — | Leaders must know how to run AI-augmented security teams |
| **Anthropic · Software Engineering Manager, Network Security** | 8+ yrs front-line management; threat modelling across K8s and cloud interconnects; egress controls; drift detection + automated remediation; compliance evidence; hiring and developing staff engineers | $405K–$485K | Lab EM roles expect **long management track records** |
| **Anthropic · security roles overall** | EMs in Safeguards (London), GRC Platform, Cybersecurity Products; Staff+ AppSec; Threat Intel Manager, Model Exploitation & Fraud; Head of Vulnerability Disclosure. **Europe:** London (EM Safeguards, Staff Security Eng), Dublin (IR Manager), Zurich (Cyber RL) | — | European offices are your realistic entry point into a lab |
| **Anthropic Frontier Red Team (Cyber)** | LLM agents for autonomous vuln discovery; policy-facing demos | $320K–$485K | Research-heavy; not your primary target |
| **Microsoft AI · Principal PM, AI Model Security** | Owns "the model security roadmap" across OWASP categories; red-teaming frameworks; eval benchmarks; **launch-readiness decisions** | $140K–$304K | Leadership-without-reports route: product/program ownership |
| **Google · Leadership TPM, AI Security & Compliance** | "Credible thought leader on AI security and compliance"; works with CISO, DeepMind; 10 yrs security; **7 yrs leadership "with or without direct reports"** | — | ✅ Your 14 yrs of security plus influence-based leadership can qualify |
| **Google DeepMind** | Agentic Red Team, AI Secure Code, Gemini Safety roles | — | Red-team and research flavour |

### 1.2 Hyperscalers & security vendors

| Signal | Evidence |
|---|---|
| **Google Cloud (your stack) went all-in on agent security at Next '26:** **Agent Identity** (a first-class principal on **SPIFFE**; GA for Agent Runtime), **Agent Gateway** (policy for agent→agent and agent→tool traffic, MCP- and A2A-aware), IAP and Context-Aware Access for agents, **Principal Access Boundary** for agents, **Unified Access Policy** with human-in-the-loop (coming), VPC-SC for agents, Model Armor inline on MCP servers, **Wiz AI-APP + AI-BOM**, SCC discovery of agents and MCP servers | Google Cloud blogs: IAM and Next '26 |
| **Microsoft Entra Agent ID** is GA; **AWS Bedrock AgentCore Identity** exists; they interoperate | Microsoft Learn, AWS blog |
| **Palo Alto Prisma AIRS** hiring directors and senior PMs for AI runtime security (incl. **Bengaluru**) | Palo Alto job boards |
| **Consolidation:** Palo Alto bought CyberArk (~$25B) and Protect AI; Alphabet bought Wiz ($32B); CrowdStrike bought SGNL and Pangea; Check Point bought Lakera; F5 bought CalypsoAI | M&A roundups |
| **Gartner:** "guardian agents" (agents that supervise agents) will capture 10–15% of the agentic AI market by 2030 | Gartner press release |

### 1.3 Large enterprises (abroad)

- **Bupa (London): "Group Head of AI Security Architecture"**, a C-level-adjacent architecture leadership role (closed Sep 2026). This shows the title exists at enterprise level.
- **Lloyds Banking Group: "AI Security Engineering Lead"**; the **UK FCA: "Head of Department, AI and Technology Security Operations"**. Regulators and banks are building AI security leadership seats.
- **1,600+ CISOs (Gartner/Evanta 2026):** "Enabling and protecting AI" is now the **#1 CISO priority**.
- **ISC2 2025 Workforce Study:** AI is the #1 skills need (41%). Senior security postings grew **65%** vs. 5.9% for junior ones, so the market rewards seniority.

---

## Part 2 — The next 12 months: what will be current

Your learning content must match *what will exist* in Oct 2026 – Sep 2027:

| Area | State as of Sep 2026 | What changes in the next 12 months | Plan impact |
|---|---|---|---|
| **OWASP** | **2026 Top 10 for LLM Apps** released 1 Sep 2026: *Excessive Agency* jumped to #3; *System Prompt Leakage* replaced by **Hidden Context Exposure**. **Agent Control Standard (ACS) v0.1**: guardian-agent enforcement points, OTel + **OCSF** observability, **AgBOM** (Agent Bill of Materials). Agentic Top 10 (Dec 2025) | ACS v1 (instrumentation) → v2 (AgBOM) | Learn the **2026** list, not 2025. Build to ACS |
| **MCP** | **2026-07-28 spec**: stateless protocol; RFC 9207 `iss` validation; credentials bound to the issuing auth server; **CIMD** replacing DCR; **Enterprise Managed Authorization** extension | SEPs for **DPoP** (SEP-1932) and **Workload Identity Federation** (SEP-1933); enterprise audit/SSO/gateway work | Your MCP knowledge must be on the 2026 spec |
| **Agent identity standards** | IETF WIMSE adopted agent auth → **draft-ietf-wimse-aims** (authors from OpenAI, Amazon, Zscaler, Ping). **NIST AI Agent Standards Initiative** (Feb 2026): identity and authorization concept paper, security research. **CoSAI** papers: *Agentic IAM* (Apr 2026), *MCP Security* (Jan 2026), *Signing ML Artifacts*, *AI Incident Response* | NIST outputs, CoSAI MCP guidance v2, Zero Trust for AI, artifact-integrity maturity model | **Contribute here**: it's leadership visibility |
| **Frontier-lab security** | **RAND SL3** playbook (25 Aug 2026): 262 controls to protect model weights against organised crime and insiders, implementable in 6–12 months | Labs racing toward SL3/SL4 | Needed for lab security leadership conversations |
| **Threat landscape** | Anthropic threat intel (Sep 2026): **autonomous multi-agent attack frameworks**, zero-days from AI-driven vuln research, **stolen AI API keys** resold, **illicit distillation** (model extraction). First AI-orchestrated espionage campaign reported Nov 2025 | Higher attacker autonomy | Detection of agentic attacks; AI credential hygiene |
| **AI for defence** | OpenAI Aardvark, Google Big Sleep/CodeMender (AI vuln discovery + fixing); Google SecOps agents | AI-augmented SOC and AppSec become normal | Leaders must **run** AI-augmented teams |
| **EU AI Act** | Omnibus deal: **Annex III high-risk → 2 Dec 2027**, Annex I → 2 Aug 2028; GPAI obligations since Aug 2025; **Art. 50 transparency from 2 Aug 2026** ⚠️ verify Official Journal publication | Your 12-month window **is the high-risk readiness window** | EU employers will pay for this |
| **Certifications** | ISACA **AAISM** (requires CISM or **CISSP**); GIAC **GAIPS** (SEC545), GOAA, GASAE; ISC2 AI cert in development (Jul 2026) | ISC2 AI cert launch | See §4 |
| **Gartner 2026 trends** | Agentic AI oversight; **IAM adapting to AI agents**; AI SOC; post-quantum action plans; 57% of employees use personal GenAI at work | — | Confirms the niche |

---

## Part 3 — Honest positioning for the leadership track

**The good news.** The hottest leadership problem at labs, clouds and vendors is **agent identity and runtime authorization**: OpenAI's EM Identity & Access role, Google Agent Identity/Gateway, Entra Agent ID, NIST, IETF, CoSAI. It's your strongest area (workload identity, multi-agent access control, MCP in production, GCP PCSE, Wiz, Model Armor).

**The hard truth.** Frontier-lab *manager* roles ask for **8–10+ years of front-line people management**. Your resume shows technical leadership but not formal people management. In 12 months, closing that fully isn't realistic, and pretending otherwise would waste your effort.

**So the 12-month target is:**

| Horizon | Target roles | Where |
|---|---|---|
| **12 months** (Sep 2027) | **Head / Lead of AI Security (Architecture)** at a large enterprise; **Principal / Staff AI Security Architect** or **Leadership TPM / Principal PM (AI security)** at a hyperscaler or vendor; **Staff Security Engineer, Agent Security / Identity** at a lab's European office | London, Dublin, Munich/Berlin, Amsterdam, Zurich; Bengaluru offices of labs and vendors as a transfer route |
| **2–4 years** | Engineering Manager / Director, Agent Security or Identity at a frontier lab or hyperscaler; Head of AI Security / deputy CISO | US/UK/EU |

**Leadership evidence you must build in parallel** (this is what gets you past screens that ask for "7 years leadership with or without direct reports"):

1. Formally lead something at TransUnion now: an AI security working group, the agent-security program, or a small team. Ask for a team lead title.
2. Mentor 2–3 people on AI security and keep a record.
3. Write strategy documents: a roadmap, a business case with budget, a board/CISO-level risk memo.
4. Be visibly external: talks, standards contributions (CoSAI / OWASP / IETF comments), articles.
5. Get hiring experience: interview candidates at your current company.

---

## Part 4 — Certifications (employer-sponsored, with fallbacks)

| Order | Cert | Why for *you* | Fallback if not sponsored |
|---|---|---|---|
| 1 (Q2) | **CISSP** | Still the #1 filter for security leadership abroad; **prerequisite for ISACA AAISM** | None, it's worth self-funding (~US$750 exam) |
| 2 (Q3) | **GIAC GAIPS (SANS SEC545 — GenAI & LLM App Security)** | Hands-on credibility for labs/vendors | Self-study plus your portfolio |
| 3 (Q4) | **ISACA AAISM** (AI governance, AI risk, AI technologies & controls) | First AI *security management* credential; fits the leadership track | IAPP AIGP |
| Watch | ISC2 AI security certification | In development since Jul 2026; may land in the window | — |

You already hold the **GCP PCSE**. Keep it current, since Agent Identity and Agent Gateway now live in that exam's domain.

---

## Part 5 — Relocation routes (⚠️ not legal advice; verify with an immigration adviser)

| Country | Route | Key facts (Sep 2026) | Fit |
|---|---|---|---|
| **UK** | **Global Talent (Digital Technology)** or Skilled Worker | Global Talent: no job offer needed; evidence = recognition, talks, publications, open-source impact, strong reference letters; ILR after **3 yrs** (Exceptional Talent). Skilled Worker general threshold £41,700 | ⭐ Best match. The plan's visibility work (OSS, talks, standards) **is** the evidence. London hosts Anthropic, OpenAI, DeepMind, AISI, and bank AI security roles |
| **Germany** | **EU Blue Card** | 2026 threshold €50,700 (€45,934 shortage/IT); IT experience can substitute for a degree | ⭐ Easy threshold for senior roles; large Munich/Berlin enterprises and cloud offices |
| **Ireland** | Critical Skills Employment Permit | EU HQs of Google, Microsoft, Meta, OpenAI; Anthropic IR role in Dublin | ⭐ Good for hyperscalers and labs |
| **Netherlands / Switzerland** | Highly Skilled Migrant / Swiss permit | Anthropic Zurich, Google Zurich | Good, but a smaller market |
| **US** | H-1B / **L-1 intra-company** / O-1 | H-1B lottery is now **wage-weighted** (favours senior roles). The $100K fee was vacated by a court in Jun 2026 but litigation continues ⚠️ | Safest US route: join a US multinational (Google, Microsoft, Palo Alto, labs' India offices) and **transfer via L-1** after ~1 year |

**Transfer strategy:** Anthropic opened in **Bengaluru** (2026), OpenAI announced India plans, and Palo Alto hires AI security PMs in **Bengaluru**. Joining one of these in India and transferring later is often faster than a cold application abroad.

---

## Part 6 — The resulting plan (details in [`../quarters/`](../quarters/))

| Quarter | Months | Theme | Leadership thread | Cert | Outcome |
|---|---|---|---|---|---|
| **Q1** | Oct–Dec 2026 | **Foundation**: the 12 weeks in `weeks/` (updated to the 2026 standards) | Start leading an AI security working group; mentor 1 person | — | 12 labs; interview-ready for AI security architect roles |
| **Q2** | Jan–Mar 2027 | **Agent identity & runtime authorization**, the flagship niche ([Q2](../quarters/q2-agent-identity-runtime-authz.md)) | Publish a reference architecture; first talk; CoSAI/OWASP contribution | **CISSP** | Recognised name in agent identity; OSS tool |
| **Q3** | Apr–Jun 2027 | **Frontier-lab security**: isolation/sandboxing, model-weight security (RAND SL3), offensive testing of agent products, AI-enabled threat detection ([Q3](../quarters/q3-frontier-lab-security.md)) | Second talk; lead a red-team exercise at work | **GIAC GAIPS** | Pass lab-style technical loops |
| **Q4** | Jul–Sep 2027 | **Leading an AI security program**: strategy, metrics, budget, EU AI Act high-risk readiness, running AI-augmented teams ([Q4](../quarters/q4-ai-security-program-leadership.md)) | Board-style memo; hiring loop; job search abroad in full swing | **AAISM** | Offers for Head/Lead/Principal roles abroad |

**Weekly rhythm (11 hrs):** 3 h learn · 5 h build · 2 h leadership & visibility · 1 h interview/job-search practice.

---

## Sources

**Job postings**
- OpenAI: [EM, Identity & Access Platform](https://openai.com/careers/engineering-manager-identity-and-access-platform-san-francisco/) · [Security Engineer, Agent Security](https://openai.com/careers/security-engineer-agent-security-san-francisco/) · [Offensive Security Engineer, Agent Products](https://openai.com/careers/offensive-security-engineer-agent-products-remote-us/) · [EM, Security Agent Engineering](https://openai.com/careers/engineering-manager-security-agent-engineering/)
- Anthropic: [SWE Manager, Network Security](https://job-boards.greenhouse.io/anthropic/jobs/5098092008) · [Frontier Red Team (Cyber)](https://job-boards.greenhouse.io/anthropic/jobs/5076477008) · [Anthropic security roles list (cyberjobs.ai)](https://cyberjobs.ai/companies/anthropic/)
- Microsoft: [Principal PM, AI Model Security](https://microsoft.ai/job/principal-product-manager-ai-model-security/)
- Google: [Leadership TPM, AI Security & Compliance](https://themuse.com/jobs/google/leadership-technical-program-manager-ai-security-and-compliance)
- Palo Alto: [Director SW Eng, Prisma AIRS](https://jobs.accel.com/companies/cortex-by-palo-alto-networks-2-99ba59f7-d27f-48a7-b8e7-38df217bd6dc/jobs/73561125-director-sw-engineering-prisma-airs) · [Sr PM AI Security, Bengaluru](https://jobs.paloaltonetworks.com/en/job/bengaluru/sr-product-manager-ai-security-primsa-airs-netsec/47263/92633325904)
- Enterprise: [Bupa Group Head of AI Security Architecture](https://freehire.me/jobs/group-head-of-ai-security-architecture-bupa-occupational-health-c2hkkcyy) · [Lloyds AI Security Engineering Lead](https://www.lloydsbankinggroup.com/careers/job-search/workday-job.157480.html) · [FCA Head of AI & Technology Security Ops](https://www.totaljobs.com/job/head-of-department-ai-and-technology-security-operations/financial-conduct-authority-job108029179)

**Industry, standards & trends**
- [Gartner Top Cybersecurity Trends 2026](https://www.gartner.com/en/newsroom/press-releases/2026-02-05-gartner-identifies-the-top-cybersecurity-trends-for-2026) · [Gartner guardian agents](https://www.gartner.com/en/newsroom/press-releases/2025-06-11-gartner-predicts-that-guardian-agents-will-capture-10-15-percent-of-the-agentic-ai-market-by-2030) · [Evanta: top CISO priorities 2026](https://www.evanta.com/resources/ciso/survey-report/top-3-priorities-for-cisos-in-2026) · [Infosecurity: hiring for the AI era](https://www.infosecurity-magazine.com/news-features/hiring-ai-challenge-cisos/)
- [OWASP GenAI 2026 Top 10 + Agent Control Standard](https://genai.owasp.org/2026/09/01/owasp-genai-security-project-unveils-2026-top-10-for-llm-applications-new-agent-control-standard-and-sponsors-as-community-tops-30000-members/) · [CSA analysis](https://labs.cloudsecurityalliance.org/research/csa-research-note-owasp-genai-top10-2026-agent-control-stand/) · [OWASP Agentic Top 10](https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications-the-benchmark-for-agentic-security-in-the-age-of-autonomous-ai/)
- [MCP 2026-07-28 spec](https://blog.modelcontextprotocol.io/posts/2026-07-28/) · [MCP 2026 roadmap](https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/) · [MCP security statistics](https://www.practical-devsecops.com/mcp-security-statistics-2026-report/)
- [IETF agent auth draft (→ draft-ietf-wimse-aims)](https://datatracker.ietf.org/doc/draft-klrc-aiagent-auth/) · [NIST AI Agent Standards Initiative](https://www.nist.gov/artificial-intelligence/ai-agent-standards-initiative) · [CoSAI Year 2](https://www.coalitionforsecureai.org/cosai-year-2-the-future-of-agentic-security/)
- [Google Cloud: what's new in IAM for agents](https://cloud.google.com/blog/products/identity-security/whats-new-in-iam-security-governance-and-runtime-defense) · [Next '26: Google Cloud + Wiz](https://cloud.google.com/blog/products/identity-security/next26-redefining-security-for-the-ai-era-with-google-cloud-and-wiz) · [Microsoft Entra Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/whats-new-agent-id) · [AWS AgentCore Identity](https://aws.amazon.com/blogs/machine-learning/secure-ai-agents-with-amazon-bedrock-agentcore-identity-on-amazon-ecs/)
- [RAND SL3 for model weights](https://www.rand.org/pubs/research_reports/RRA4704-1.html) · [Anthropic threat intel, Sep 2026](https://www.anthropic.com/threat-intelligence-report-september-2026) · [Anthropic: AI-orchestrated espionage](https://www.anthropic.com/research/disrupting-AI-espionage) · [OpenAI Aardvark](https://openai.com/index/introducing-aardvark/)
- [EU AI Act omnibus dates (Gibson Dunn)](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/)
- [Software Strategies M&A roundup](https://softwarestrategiesblog.com/2026/03/28/agentic-ai-security-startups-funding-mna-rsac-2026/)

**Certifications & relocation**
- [ISACA AAISM](https://www.isaca.org/credentialing/aaism) · [GIAC AI certifications](https://www.giac.org/focus-areas/artificial-intelligence) · [ISC2 AI certification in development](https://www.isc2.org/Insights/2026/07/ai-security-certification-development)
- [UK Global Talent guide](https://movingtotheuk.co.uk/visas-and-immigration/work-visas/global-talent-visa) · [Germany Blue Card 2026](https://www.jobbatical.com/blog/germany-latest-eu-blue-card-salaries-updated) · [H-1B fee & weighted lottery status](https://www.tmimmigration.com/post/h1b-2026-100000-fee-litigation-weighted-lottery) · [Anthropic Bengaluru office](https://www.cnbc.com/2025/10/08/anthropic-to-open-first-india-office-in-2026.html)
