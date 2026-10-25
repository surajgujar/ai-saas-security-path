# Labs

Hands-on labs for the 12 weeks. **Start with [SETUP.md](SETUP.md)** (do it once), then open each lab's `README.md`.

Each lab README has the same parts: **Goal** · **What's here** (the skeleton files) · **Core steps** (time-boxed, with checkpoints) · **Stretch** · **Done when** · **If it breaks**. You write the parts marked `TODO(step N)` in the code; the plumbing is already there. Search a folder for `TODO(` to see every gap.

| Lab | Week | Builds | Depends on |
|---|---|---|---|
| [01-llm-internals](01-llm-internals/) | 1 | Tokenizer + embedding experiments | — |
| [02-vuln-agent-app](02-vuln-agent-app/) | 2 | **HelpDesk Copilot** — the target app for 5 later labs | SETUP |
| [03-threat-model](03-threat-model/) | 3 | Threat model + reusable template | Lab 2 |
| [04-redteam](04-redteam/) | 4 | Red-team report + baseline ASR | Lab 2 |
| [05-supply-chain](05-supply-chain/) | 5 | Scan/sign/BOM/gate + backdoor write-up | SETUP |
| [06-guardrails](06-guardrails/) | 6 | Guardrails + before/after ASR | Labs 2, 4 |
| [07-agent-authz](07-agent-authz/) | 7 | OPA per-tool authorization | Lab 2 |
| [08-gcp-vertex-baseline](08-gcp-vertex-baseline/) | 8 | Secure Terraform baseline (plan-only) | SETUP |
| [09-sspm](09-sspm/) | 9 | Drift detector + Shadow AI + control catalogue | SETUP |
| [10-saas-identity-api](10-saas-identity-api/) | 10 | OAuth grant auditor + crAPI findings | SETUP |
| [11-telemetry](11-telemetry/) | 11 | OTel tracing + tamper-evident log + detections | Labs 2, 4, 7 |
| [12-standard-and-roadmap](12-standard-and-roadmap/) | 12 | The standard, intake, roadmap, KPIs (capstone) | Labs 3–11 |

**Lab 2 is the backbone.** Labs 3, 4, 6, 7 and 11 all target the HelpDesk Copilot, so get Lab 2 working first. See [catch-up note below](#catch-up-weeks-14).

> ⚠️ Never commit API keys, tokens, or real company data. `labs/.env` holds your key and is git-ignored. Attack code only ever runs against your own lab targets.

## Catch-up (weeks 1–4)

The daily plan assumed the labs existed from day one; they didn't, so Weeks 1–4 have no committed lab yet. Suggested recovery (also reflected in the week files):

1. **Lab 2 first** (it unblocks the most). Use the skeleton — it's mostly wiring you fill in.
2. **Lab 3** (threat model) is documentation and quick once Lab 2 runs.
3. **Lab 1** is trimmed to the tokenizer + embedding parts; the **LoRA backdoor moved to Lab 5**, where it's reused.
4. Then **Lab 4** (red team) against your Lab 2 app, and carry on from Week 5 on schedule.
