# Week 10 — SaaS Identity Lifecycle, OAuth/OIDC Governance, API Security (30 Nov – 6 Dec)

**Why (JD):** "SaaS identity lifecycle and joiner-mover-leaver flows across multi-SaaS estates, OAuth/OIDC token governance, least-privilege enforcement, and API security (OWASP API Top 10)"

## Learn (2.5 h)
- [ ] OAuth 2.0 / 2.1 grant types, scopes, refresh tokens, PKCE; OIDC ID tokens vs access tokens (oauth.net, *OAuth 2.0 Simplified*)
- [ ] OAuth security BCP — **RFC 9700**
- [ ] SAML vs OIDC SSO; **SCIM 2.0** provisioning; IdP (Entra ID / Okta) → SaaS JML
- [ ] JML failure modes: orphaned accounts, local (non-SSO) accounts, privilege creep on movers, tokens surviving deprovisioning, shared/service accounts
- [ ] Third-party OAuth app governance: consent policies, admin consent, publisher verification, unused-grant revocation (Google Workspace "API controls", Entra "app consent")
- [ ] **OWASP API Security Top 10 (2023)** — BOLA, broken auth, BOPLA, resource consumption, BFLA, SSRF…

## Lab (4 h) → `labs/10-saas-identity-api/`
- [ ] **OAuth grant auditor**: Google Workspace Admin SDK `tokens.list` (or Graph `oauth2PermissionGrants`) → flag high-risk scopes, unverified apps, inactive grants → CSV + revocation script (dry-run by default)
- [ ] **JML simulator**: small Keycloak/Okta dev + SCIM to a mock SaaS app; test leaver → confirm sessions + refresh tokens + OAuth grants revoked; document gaps
- [ ] **OWASP crAPI** (Completely Ridiculous API) in Docker — find & write up at least 5 API Top 10 issues (BOLA, BFLA, mass assignment, SSRF, excessive data exposure)

## Interview questions
1. An employee leaves — list everything that must happen across 50 SaaS apps within 1 hour.
2. Why can a user's access persist after they're disabled in the IdP?
3. How would you govern third-party OAuth integrations at enterprise scale?
4. BOLA vs BFLA — example and fix for each. How do AI agents calling APIs make these worse?

## Done when
- [ ] Auditor, JML write-up, crAPI findings committed
