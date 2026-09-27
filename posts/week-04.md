# Week 4 post (#3): why prompt-injection classifiers alone aren't enough

**Publish:** Fri 23 Oct 2026 · **Visual:** a bar chart of attack success rate by technique (from your REPORT.md)

---

I red-teamed my own AI agent this week, using promptfoo, NVIDIA garak and plenty of manual testing.

Baseline attack success rate: **[X]%**. [Replace with your measured number.]

The attacks that worked best weren't sophisticated:
• [e.g. instructions hidden in a retrieved document]
• [e.g. a multi-turn "crescendo" that escalated over 5 messages]
• [e.g. an encoding trick the input filter didn't decode]

That matches what Microsoft's AI Red Team found across 100+ generative AI products: real damage comes from simple techniques and poor system integration, not exotic ML attacks.

Why a classifier in front of the model isn't enough:
1. It's probabilistic. At scale, a 1% miss rate means a steady flow of successful attacks.
2. **Indirect injection** arrives through data you retrieve, not from the user.
3. It can't know whether an action is *allowed*. It only guesses whether text is malicious.

Classifiers are one useful layer. They can't be the only control between an attacker and your send_email tool.

Next week: supply chain. After that: I fix this app and rerun the same tests.

#AIRedTeaming #PromptInjection #AISecurity #LLMSecurity

---
**First comment (links):** Lessons from red teaming 100 GenAI products – https://arxiv.org/abs/2501.07238 · promptfoo red team – https://www.promptfoo.dev/docs/red-team/quickstart/ · garak – https://github.com/NVIDIA/garak
