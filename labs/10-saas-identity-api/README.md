# Lab 10: SaaS identity, OAuth & API security

**Goal:** audit OAuth app grants (the Salesloft-Drift-style risk), understand joiner/mover/leaver gaps, and find real API flaws in OWASP crAPI.

**Prepares you for:** "Why does access survive offboarding?" "How do agents make BOLA/BFLA worse?"

**Time:** core 4.5 h (grant auditor + 3 crAPI findings). **Stretch:** JML/SCIM with Keycloak. **Before you start:** Docker running for crAPI.

> **Scope note:** the original week had JML+SCIM *and* crAPI *and* the auditor. **Core = grant auditor + 3 crAPI findings.** JML/SCIM is the stretch goal.

## What's here
```
data/oauth_grants.json   sample third-party app grants    (done)
grant_auditor.py         risk-flag grants, dry-run revoke TODO(step 2)
```

## Core steps

### Step 1: read the kill chain (20 min)
Read the Salesloft Drift write-up (linked from your tracker). One line in your notes: why did disabling accounts not stop the data theft? (Stolen OAuth tokens kept working.)

### Step 2: OAuth grant auditor (90 min)
Finish `audit()` in `grant_auditor.py`. Run it.

**Checkpoint:** "Old Analytics" and "Legacy Backup" come out **high** (broad scope + unverified + stale), and `revoke_list.csv` lists them. Note the design choice: revocation is **dry-run by default**. You never auto-revoke in a lab; you produce the list for a human.

### Step 3: crAPI (2 h)
Run OWASP crAPI in Docker:
```powershell
cd labs\10-saas-identity-api
curl -o docker-compose.yml https://raw.githubusercontent.com/OWASP/crAPI/main/deploy/docker/docker-compose.yml
docker compose pull ; docker compose up -d
```
crAPI is heavy (~8 GB RAM is tight — close other apps). Open http://localhost:8888. Find and write up **at least 3** API Top 10 issues, e.g. BOLA (view another user's vehicle/order by changing an id), BFLA, mass assignment, or SSRF. For each: the request, the flaw, the OWASP API id, and the fix.

**Checkpoint:** 3 findings documented with the actual requests (use the browser dev tools or Burp/curl).

### Step 4: write-up (30 min)
`FINDINGS.md`: the grant-audit results + the crAPI findings, each mapped to OWASP API Top 10. Add one paragraph: how an AI agent with an over-broad OAuth grant makes BOLA worse (it can be steered to call any id).

## Stretch
- JML simulator: a Keycloak dev realm + SCIM to a mock SaaS app; test that a leaver's sessions, refresh tokens and grants are all revoked, and document what's left behind.
- Extend the auditor to really call the Google Admin SDK `tokens.list` against a dev tenant (read-only).

## Done when
- [ ] `grant_auditor.py` flags high-risk grants and writes a dry-run revoke list
- [ ] crAPI running; 3+ findings documented with requests + OWASP ids
- [ ] `FINDINGS.md` written, incl. the agent/BOLA note
- [ ] Committed to `labs/10-saas-identity-api/` (don't commit the big `docker-compose.yml`? it's fine either way; keep secrets out)

## If it breaks
| Symptom | Fix |
|---|---|
| crAPI containers crash / OOM | It's memory-hungry. Close Chrome, raise Docker's memory to 4 GB, or do crAPI on a day you can give it the whole machine. |
| `docker compose` not found | You're on old Docker. Upgrade Docker Desktop (SETUP.md §3); it's `docker compose`, not `docker-compose`. |
| `audit()` KeyError | Use `.get()` for optional fields; `scopes` is a list — intersect with a set. |
| Can't reach crAPI mail (needs MailHog) | crAPI ships MailHog at http://localhost:8025 for the signup OTP. |
