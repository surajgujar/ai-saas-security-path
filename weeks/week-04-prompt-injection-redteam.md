# Week 4 — Prompt Injection, Jailbreaks & AI Red-Teaming (16 – 22 Nov)

**Why (JD):** "prompt injection, jailbreaks … red-teaming"
**Goal:** Move from defender-only (Model Armor) to running a structured red-team campaign and reporting it.

## Learn (2.5 h)
- [ ] Simon Willison's blog — prompt injection tag (esp. "lethal trifecta", "dual LLM")
- [ ] Greshake et al. — *Not what you've signed up for* (indirect prompt injection paper) — read abstract + attack section
- [ ] Microsoft AI Red Team — *Lessons from red-teaming 100 generative AI products*
- [ ] Jailbreak families: role-play, many-shot, crescendo (multi-turn), encoding/obfuscation, token smuggling
- [ ] Tool docs: **garak** (NVIDIA), **PyRIT** (Microsoft), **promptfoo** red-team mode

## Practice (warm-up, 60 min)
- [ ] [Lakera Gandalf: Agent Breaker](https://play.lakera.ai/agent-breaker) — the classic Gandalf link now redirects here. Clear these 5 in order, reaching level 3+ on at least 3:

  | # | Challenge | Attack | OWASP LLM (2025) | Lab tie-in |
  |---|---|---|---|---|
  | 1 | Cycling Coach | Direct: extract system prompt | LLM07 | Warm-up |
  | 2 | Thingularity | Direct: list the agent's tools | LLM07 / LLM06 | Agent recon |
  | 3 | Trippy Planner | Indirect: poisoned web page adds a malicious link | LLM01 | Poisoned RAG doc |
  | 4 | Clause AI | Exfiltrate protected witness info | LLM02 | `send_email` HR-data exfil |
  | 5 | OmniChat Desktop | Injection via MCP server description | LLM01 / LLM03 | Tool poisoning |

  *If time allows:* PortfolioIQ Advisor (poisoned PDF, LLM04/LLM09), Curs-ed CodeReview (malicious rules file, LLM03), Solace AI (jailbreak).
  *Log for each challenge:* the payload that worked, number of attempts, and the defense that blocked you. Reuse these in the Lab and `REPORT.md`.
- [ ] PortSwigger Web Security Academy — *Web LLM attacks* labs

## Lab (4 h) → `labs/04-redteam/`

> **Step-by-step guide + skeleton code:** [`labs/04-redteam/README.md`](../labs/04-redteam/README.md). Do the lab from there; the list below is the summary.
Against your Week 2 app:
- [ ] `promptfoo` red-team config targeting OWASP LLM plugins; run it
- [ ] `garak` probe run against the underlying model endpoint
- [ ] Manual: indirect injection via the poisoned RAG doc → make the agent call `send_email` with confidential HR data (data exfiltration)
- [ ] Manual: multi-turn crescendo jailbreak
- [ ] Write `REPORT.md`: exec summary, scope, method, findings (severity, OWASP/ATLAS IDs, repro, evidence), recommendations. **Save baseline Attack Success Rate (ASR)** — you'll compare in Week 6.

## Interview questions
1. Direct vs indirect prompt injection — which worries you more for agents and why?
2. Model Armor caught X% — why isn't a classifier alone enough?
3. How would you set up continuous AI red-teaming in CI/CD?
4. How do you report an AI finding when it's non-deterministic?

## Done when
- [ ] Report with ASR baseline committed · [ ] Note written
