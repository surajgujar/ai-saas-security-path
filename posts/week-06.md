# Week 6 post (#5): guardrails are not authorization

**Publish:** Fri 6 Nov 2026 · **Visual:** a before/after table of attack success rate from your Week 4 vs Week 6 runs

---

**Guardrails are not authorization.**

I added guardrails to my deliberately vulnerable agent this week: input/output filtering, spotlighting (marking untrusted content so the model treats it as data) and human approval for external emails.

Result: attack success went from **[X]% → [Y]%**. [Use your measured numbers.]

That's a real improvement. But look at what got through: [describe 1–2 remaining attacks].

Here's the key distinction:
🔹 A **guardrail** asks: "Does this text look malicious?" The answer is a probability.
🔹 **Authorization** asks: "Is this agent, acting for this user, allowed to do this action on this data?" The answer is a yes or no from a policy, not a guess.

The research agrees. The "Design Patterns for Securing LLM Agents" paper and DeepMind's CaMeL both limit what an agent *can do* after it reads untrusted input. They don't rely on detecting the attack.

Patterns I'm now using:
• Plan-then-execute: the plan is fixed before any untrusted content is read
• Human approval for anything that leaves the building
• (next week) a policy decision on every tool call

Use guardrails to reduce noise. Use authorization to limit the damage.

#AgenticAI #AISecurity #PromptInjection #ZeroTrust

---
**First comment (links):** Design Patterns paper – https://arxiv.org/abs/2506.08837 · CaMeL – https://arxiv.org/abs/2503.18813 · Spotlighting – https://arxiv.org/abs/2403.14720
