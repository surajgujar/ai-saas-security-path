# Week 9 post (#8): Shadow AI without blocking everything

**Publish:** Fri 27 Nov 2026 · **Visual:** a 3-column board: Sanctioned / Tolerated / Blocked, with example AI apps and the rule for each

---

Blocking every AI tool doesn't stop Shadow AI. It just moves it to personal phones.

In a 2025 Gartner survey, 69% of security leaders said they suspect, or have evidence, that employees use public GenAI at work. Gartner also predicts that by 2030 over 40% of organisations will have security or compliance incidents caused by unauthorised AI tools.

What works better is **three tiers, applied automatically**:
✅ **Sanctioned**: enterprise contract, SSO, no training on your data, DLP on prompts
🟡 **Tolerated**: allowed for non-sensitive work, with a warning banner and logging
⛔ **Blocked**: unacceptable data terms or no security basics

How you find Shadow AI:
• CASB/SWG logs (who is using which AI domains)
• **OAuth grants** (the AI app a user connected to their mailbox counts too)
• browser extensions
• expense reports (yes, really)

This week's lab: I ran CISA's SCuBA baseline tools against a trial tenant and built a small drift detector (snapshot → git → diff → alert). [Add a finding, e.g. "X of Y baseline checks failed out of the box".] I also mocked Shadow AI discovery from proxy logs.

SSPM covers settings *inside* SaaS apps. CASB covers the *traffic* to them. For Shadow AI you need both.

#ShadowAI #SaaSSecurity #SSPM #CASB #AIGovernance

---
**First comment (links):** Gartner via Infosecurity Magazine – https://www.infosecurity-magazine.com/news/gartner-40-firms-hit-shadow-ai/ · CISA SCuBA – https://www.cisa.gov/resources-tools/services/secure-cloud-business-applications-scuba-project
