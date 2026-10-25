# Lab 9: SSPM, CASB & Shadow AI

**Goal:** the SaaS-posture lab (your biggest skill gap per the gap analysis, so give it real attention). Run a CISA SCuBA baseline, build a settings drift detector, discover Shadow AI from proxy logs, and write a 20-control SSPM catalogue.

**Prepares you for:** "SSPM vs CASB vs CSPM?" "How would you roll out SSPM across 300 SaaS apps?" "Find Shadow AI without blocking everything."

**Time:** core 4.5 h. **Before you start:** [SETUP.md](../SETUP.md). A free Google Workspace / M365 dev tenant is nice for step 1 but not required — you can run the detector and Shadow AI parts on the included sample data.

## What's here
```
data/settings_baseline.json   a SaaS settings snapshot        (done)
data/proxy_log.csv            400 rows of web proxy traffic   (done)
data/genai_domains.txt        known GenAI domains             (done)
drift_detector.py             baseline compare + alert        TODO(step 2)
shadow_ai.py                  Shadow AI discovery             TODO(step 3)
```

## Core steps

### Step 1: run a real baseline (60 min)
If you have a Google Workspace trial, run **ScubaGoggles**; for M365, **ScubaGear** or **Maester**. Read the report and note 3 failed controls. No tenant? Read the SCuBA baseline docs and pick 3 controls you'd test, and move on — the sample data covers the hands-on part.

### Step 2: drift detector (75 min)
Finish `evaluate()` in `drift_detector.py` and extend `POLICY` to ~20 controls (MFA enforced, external sharing off/allowlist, OAuth app allowlist, admin count ≤ 5, audit logging on, session length ≤ 7 days, password length ≥ 14, guest access off, data export restricted, …). Then copy `settings_baseline.json` to `settings_current.json`, change a couple of values, and run it.

**Checkpoint:** violations print with severities, and the diff shows exactly what changed. Bonus: a GitHub Action on a schedule that runs this and fails on any critical drift (reuse the Lab 5 gate idea).

### Step 3: Shadow AI discovery (60 min)
Finish `discover()` in `shadow_ai.py`: tally GenAI hits and bytes-uploaded per user, ranked by data leaving.

**Checkpoint:** a per-user table, worst first. In your notes, propose the "sanctioned / tolerated / blocked" tiers and which domains go where.

### Step 4: SSPM control catalogue (45 min)
In `CONTROL-CATALOGUE.md`, write up the ~20 controls as a table: control ID · description · severity · how an SSPM checks it · remediation. This is the leadership artefact (what you'd standardise across many SaaS apps).

## Stretch
- Pull a real settings snapshot from the Google Admin SDK (reuse in Lab 10) instead of the sample JSON.
- Add an allow/deny classifier for AI domains with a risk score (data terms, SSO support), not just a flat list.

## Done when
- [ ] A baseline report read (real or from docs), 3 findings noted
- [ ] `drift_detector.py` evaluates ~20 controls and shows drift
- [ ] `shadow_ai.py` produces a risk-ranked report
- [ ] `CONTROL-CATALOGUE.md` with 20 controls
- [ ] Committed to `labs/09-sspm/`

## If it breaks
| Symptom | Fix |
|---|---|
| ScubaGear won't run on Windows | It needs PowerShell modules and a tenant; if setup drags, do the docs-only version of step 1 and spend the time on steps 2–4. |
| `evaluate()` KeyErrors | A control name isn't in the settings dict. Use `settings.get(key)` and treat missing as a finding. |
| All users look identical in Shadow AI | Check you're matching the domain set and summing `bytes_up` as int, not string. |
