# Week 1 post: why I'm going deep on AI & agent security

**Publish:** Fri 2 Oct 2026 · **Visual:** your lifecycle sketch (data → pre-train → fine-tune → eval → deploy → operate) with one attack marked at each stage

---

For [X] years I've secured cloud platforms: IAM, workload identity, posture, pipelines.

For the next 12 months I'm going all-in on one question: **how do we secure AI agents that can act on our behalf?**

Why now:

🔹 Agents don't just answer questions. They call tools, move data and use credentials. That makes it an identity and authorization problem as much as a model problem.
🔹 Prompt injection has no complete fix at the model layer. The model can't reliably tell instructions apart from data, so the controls have to live around it.
🔹 The standards are being written right now: OWASP's 2026 LLM Top 10, the new Agent Control Standard, and the MCP 2026-07-28 spec with its stronger authorization.

This week I went back to fundamentals: tokenizers, embeddings and a tiny LoRA fine-tune. Two things stood out:
1. A homoglyph version of "ignore previous instructions" tokenizes completely differently. [Add what you saw.]
2. A ~50-example LoRA was enough to plant a hidden trigger phrase in a small model. [Add your result.] That's a supply-chain risk in a file of a few megabytes.

Every week I'll share one lab, one lesson and one thing I got wrong.

If you're securing AI in production, what's the risk you're most worried about?

#AISecurity #AgenticAI #CloudSecurity #LLMSecurity

---
**First comment (links):** OWASP GenAI LLM Top 10 2026 – https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/ · Karpathy, Intro to LLMs – https://www.youtube.com/watch?v=zjkBMFhNj_g
