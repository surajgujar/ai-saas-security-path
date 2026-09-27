# Q3 — Frontier-Lab Security Depth (Apr – Jun 2027)

**Why this quarter exists:** Lab and vendor postings ask for things you haven't done yet: **isolation/sandboxing depth** for agent runtimes, **security assessment of agent products**, **model-weight protection** (RAND SL3), and **detection of AI-enabled threats** such as automated intrusion campaigns, stolen AI API keys and illicit distillation.
**Outcome:** You can pass a lab-style technical loop and talk credibly with lab security leaders. **GIAC GAIPS passed.**
**Hours:** 11/week. SANS SEC545 (if sponsored) runs alongside Months 1–2.

## Month 1 — Isolation & runtime containment for agents (Apr 2027)
- [ ] Container and kernel security fundamentals: namespaces, cgroups, seccomp, AppArmor/SELinux, capabilities, rootless containers
- [ ] Sandboxes used for agent code execution: **gVisor**, **Firecracker** microVMs, Kata Containers, WASM; compare their threat models and trade-offs
- [ ] Egress control for agents: default-deny egress, allow-lists, K8s NetworkPolicy / Cilium, VPC-SC for agents
- [ ] Lab: harden an agent code-execution runtime on **GKE Sandbox (gVisor)** with Workload Identity and Binary Authorization; write a hardening guide
- [ ] SANS **SEC545** coursework (or a self-study equivalent)
- [ ] Leadership: run a **1-hour internal workshop** on agent runtime isolation

## Month 2 — Assessing agent products & model-weight security (May 2027)
- [ ] Build a repeatable **agent product security review** method: threat model → design review → authorization review → test plan → findings report. Apply it to your own Q1/Q2 lab systems only
- [ ] Use your Q1 red-team tooling (promptfoo / PyRIT / garak) as a regression suite in CI for your own app
- [ ] **RAND SL3 playbook** (262 controls): map it against a GCP environment; produce a gap-assessment template (weights storage, access, insider risk, monitoring)
- [ ] Insider-risk programme basics for AI labs: privileged access, two-person rules for sensitive assets, monitoring
- [ ] **GIAC GAIPS exam** ✅
- [ ] Leadership: lead an **internal AI security review** of one real TransUnion AI initiative end to end and present the findings to its owners

## Month 3 — Detecting AI-enabled threats & running AI-augmented teams (Jun 2027)
- [ ] Read Anthropic's and Google's threat-intelligence reports on AI misuse; summarise the defender recommendations
- [ ] Detection content for your lab: AI API key leakage/misuse, abnormal agent tool-use patterns, high-volume model querying (distillation signals)
- [ ] AI for defence: evaluate AI-assisted vulnerability discovery and triage tools (e.g. Aardvark, Big Sleep/CodeMender, Google SecOps agents); write how a security leader should adopt them (governance, human review, metrics)
- [ ] Talk #2: "Securing agent runtimes: lessons from building an authorization gateway"
- [ ] Relocation: start applying to 5 target roles per month; ask 3 senior contacts for referrals

## Done when
- [ ] Hardening guide + review method published · [ ] SL3 gap-assessment template · [ ] GAIPS passed · [ ] Talk #2 delivered
