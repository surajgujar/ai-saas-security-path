# Week 3 post (#2): what changed in the OWASP LLM Top 10 2026

**Publish:** Fri 16 Oct 2026 · **Visual:** 2025 vs 2026 ranking side by side, with arrows showing the moves

---

OWASP published the 2026 LLM Top 10 in August. The biggest change isn't a new risk. It's **how the list was made**.

For the first time, ~25% of the ranking came from real incident data (6,639 incidents), not just expert votes.

What moved:
🔹 #1 Prompt Injection and #2 Sensitive Information Disclosure stayed at the top.
🔹 **Excessive Agency jumped from #6 to #3.** Agents with too many permissions are now where the damage happens.
🔹 Supply Chain and Data & Model Poisoning moved down to #4 and #5.
🔹 A new appendix maps every risk to OWASP, MITRE, NIST and CSA controls, which is useful when you need to justify the work to auditors.

OWASP also released the **Agent Control Standard**, which moves from "what can go wrong" to "where to enforce controls": agents that are inspectable, traceable and instrumentable.

My takeaway: the focus is shifting from *stopping the model being fooled* to *limiting what happens when it is*.

This week I threat-modelled my own agent app: [X] threats mapped to OWASP 2026 and MITRE ATLAS. [Name the most surprising one.]

What's the top risk in your own AI threat models?

#OWASP #AISecurity #ThreatModeling #AgenticAI

---
**First comment (links):** OWASP LLM Top 10 2026 – https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/ · Agent Control Standard – https://genai.owasp.org/resource/agent-control-standard-acs/ · MITRE ATLAS – https://atlas.mitre.org/
