# Track B — Offensive AI Credibility (Apr – Jun 2027)

**Outcome:** Complete the "hybrid defender" profile — public, verifiable proof you can break AI systems.
**Rules:** only test systems you own, programs with explicit scope (bug bounty / VRP), or OSS with responsible disclosure.

## Month 1 — Skills
- [ ] Agent exploitation: indirect prompt injection chains → tool misuse → data exfiltration; memory poisoning; multi-agent cascade
- [ ] Deeper tooling: PyRIT orchestrators, garak custom probes, promptfoo custom plugins; write one custom probe for MCP tool poisoning
- [ ] Classic appsec refresh for AI stacks: SSRF, path traversal, command injection, deserialisation — the bugs actually found in MCP servers
- [ ] Practice: PortSwigger Web LLM labs (all), Gandalf (all levels incl. adventure), any live AI red-team competitions (e.g. HackAPrompt, Gray Swan arena) that are running

## Month 2 — Real findings
- [ ] Audit 10 popular open-source MCP servers / agent frameworks with your Track A tool + manual review
- [ ] Report findings responsibly (GitHub security advisories / maintainers; huntr for AI/ML OSS if in scope)
- [ ] Try in-scope AI bug bounty programs (e.g. Google AI VRP, other vendors' AI programs) — read scope carefully
- [ ] Goal: ≥1 accepted advisory / CVE credited to you

## Month 3 — Package it
- [ ] Write an AI red-team methodology (scoping, threat-led test plan, ASR metrics, non-determinism handling, reporting) — publish
- [ ] Blog post per finding (after fix/disclosure window)
- [ ] Talk #2: "What I found auditing N MCP servers"
- [ ] Cert option: GIAC GOAA (SEC535) if you want red-team roles

## Done when
- [ ] ≥1 credited finding · [ ] Methodology published · [ ] Talk #2 delivered
