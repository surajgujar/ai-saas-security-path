# STAR Stories (from your resume)

Fill in the real numbers/details — interviewers remember specifics. Keep each to ~2 minutes.

| # | Story | JD bullet it proves | Status |
|---|---|---|---|
| 1 | MCP-based AI security agent for secure code review at TransUnion | Hands-on expertise; agentic AI | ⬜ |
| 2 | Securing enterprise agentic workflows on GCP — MCP server registration, agent skills, multi-agent access control | Agent identity & runtime authz | ⬜ |
| 3 | Model Armor rollout — prompt injection, jailbreak, PII controls for GenAI apps | Guardrails, reference controls | ⬜ |
| 4 | AI/ML model security assessments & supply-chain scanning | Model provenance, supply chain | ⬜ |
| 5 | Onboarding AWS + GCP into Wiz (CSPM) | Posture mgmt → bridge to SSPM | ⬜ |
| 6 | Continuous multi-cloud misconfiguration remediation | Misconfig & drift remediation | ⬜ |
| 7 | DevSecOps across SDLC — security in CI/CD, culture change | Standards adoption, stakeholder alignment | ⬜ |
| 8 | Automated server decommissioning workflow | Lifecycle (leaver) thinking → JML | ⬜ |
| 9 | Jenkins CI/CD system at Cisco | Pipeline integrity → model deployment pipelines | ⬜ |
| 10 | A time you pushed back on a team / influenced without authority | Advise & align stakeholders; mentoring | ⬜ |

## Template

**Situation:** (context, scale — how many teams/apps/users?)
**Task:** (what you owned)
**Action:** (3–4 specific things *you* did; name tools, decisions, trade-offs)
**Result:** (metric: % reduction, # findings, time saved, adoption)
**Link to target role:** (one sentence — how this transfers)

---

### 1. MCP security agent
- S: Devlopers's are scanning code at pipeline level
- T: I have to help them to scan their code on IDE. I
- A: Developed an Agent, Script and tools list, find, read, write, patch, open file. 
- R: 100+ developers using the agent and 90% reduction in violation. Save platform cost.
- Link: Advisor, Transunion

<!-- copy the block for 2–10 -->

### 2. Securing agentic workflows on GCP
- S: Lots of agents, tools and MCP sever but no standard workflow
- T: Secure agentic workflow
- A: Imported all agents, Import mcp server to agent registry
- R: 4 teams are using Agent registry
- Link:Advisor, Transunion

### 3. Model Armor rollout
- S: We want to prevent leakage of customer data to LLM. So we want to rollout model armor to sanitize prompt and response of LLM
- T: Setup model armor at org level
- A: Enable model armor, Setup Template enabled malicious url detection, prompt injection, jailbreak detection, Sensitive data protection 
- R: Org secured
- Link:Advisor, Transunion

### 4. AI/ML model security assessments & supply-chain scanning
- S: Customer want to deploy their sensors files
- T: Need to scan custom build models
- A: Developed promptfoo template to scan sensonrs file
- R: Org aligned
- Link:

### 5. Onboarding AWS + GCP into Wiz
- S: Onboard AWS and GCP on Wiz
- T: Create a Iam User, role and policy 
- A: Added 100+ accounts to the wiz
- R: Wiz got onboarder
- Link: Lead Engineer

### 6. Multi-cloud misconfiguration remediation
- S: Identify and standardize cloud configuratons
- T: Identify tool, setup tool and deploy it
- A: Write a policy to mandate scanner for all iacm pipelines
- R: All new/existing misconfigurations are mitigated
- Link: Advisor

### 7. DevSecOps across the SDLC
<!-- Prompts: Which pipelines/teams? What did you add (SAST/SCA/secrets/IaC scans, gates)? Who resisted, and how did you win them over? Before/after numbers (findings caught pre-prod, MTTR, % repos covered)? -->
- S: We have to secure our pipelines
- T: Develop configured and deploy templates
- A: Write a policy gate for SAST/SCA/secrets/IaC scans
- R: Everyone adopted the gates
- Link: Shows I can get standards adopted across teams — the same work as rolling out AI security standards.

### 8. Automated server decommissioning
<!-- Prompts: What was the risk before (orphaned servers, stale creds/access)? What did the workflow automate (access revocation, DNS, CMDB, backups)? How many servers, hours saved, findings closed? -->
- S: There are no standard process for orphaned server
- T: Create a workflow to decom servers
- A: Developed ansible playbook
- R: saved hours of works
- Link: Lifecycle "leaver" thinking → joiner-mover-leaver for SaaS identities and AI agents.

### 9. Jenkins CI/CD at Cisco
<!-- Prompts: Scale (jobs, teams, builds/day)? How did you protect pipeline integrity (credentials, agents, plugins, approvals)? Any incident or near miss? -->
- S: Need to setup SDLC workflow
- T: Setup everything
- A: Standardize workflow and deploy
- R: Everyone followed the new workflow.
- Link: Pipeline integrity → securing model training/deployment pipelines.

### 10. Pushed back / influenced without authority
<!-- Prompts: Pick ONE real moment: a team wanted to ship something risky, or skip a control. What was the risk, what data did you bring, what compromise did you reach, what happened next? Include what you learned. -->
- S:
- T:
- A:
- R:
- Link: Advising and aligning stakeholders is the core of a Head/Lead of AI Security role.
