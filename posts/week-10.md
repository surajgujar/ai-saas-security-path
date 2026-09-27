# Week 10 post (#9): why access survives offboarding

**Publish:** Fri 4 Dec 2026 · **Visual:** a checklist graphic: "Account disabled ✅ — sessions? refresh tokens? OAuth grants? API keys? personal access tokens? ❓"

---

An employee leaves. Their account is disabled the same day. Done?

**Often not.**

Disabling the account in your identity provider stops *new* logins. It doesn't always remove access that already exists:
🔹 active sessions in SaaS apps
🔹 **OAuth refresh tokens** held by third-party apps they connected
🔹 personal access tokens and API keys
🔹 access delegated to AI agents and integrations acting "as" them

Attackers know this. The 2025 **Salesloft Drift** incident showed how stolen OAuth tokens from one connected app were used to pull data from many companies' Salesforce instances. No password was needed.

What I built this week:
1️⃣ An **OAuth grant auditor** (Workspace Admin SDK / Microsoft Graph) that lists every third-party app with access, its scopes and its last use, with a dry-run revoke
2️⃣ A **JML (joiner-mover-leaver) simulator**: the leaver flow revokes sessions, refresh tokens and grants, not just the account
3️⃣ 5 findings against OWASP crAPI, mapped to the API Security Top 10. [List the most interesting one.]

AI agents make this worse, because every agent holds tokens for someone. Offboarding now has to cover **non-human identities** too.

#IdentitySecurity #SaaSSecurity #OAuth #NHI

---
**First comment (links):** Salesloft Drift analysis (Google GTIG) – https://cloud.google.com/blog/topics/threat-intelligence/data-theft-salesforce-instances-via-salesloft-drift · RFC 9700 OAuth Security BCP – https://datatracker.ietf.org/doc/html/rfc9700
