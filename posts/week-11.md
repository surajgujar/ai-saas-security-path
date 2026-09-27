# Week 11 post: what a SOC needs to see in an AI agent incident

**Publish:** Fri 11 Dec 2026 · **Visual:** a Jaeger trace screenshot of one agent run (prompt → tool calls → policy decisions), with the malicious step highlighted

---

When an AI agent is misused, your SOC will ask three questions:
1. **What did it do?**
2. **Who was it acting for?**
3. **Why did it decide to do it?**

Most agent deployments today can't answer any of them.

This matters now. In November 2025 Anthropic reported a state-sponsored campaign in which an AI agent carried out an estimated **80–90% of the intrusion work**. Humans only picked targets and approved key steps. Agent actions happen at machine speed, so the logs have to keep up.

What I built this week:
🔹 **OpenTelemetry traces** for every agent step: prompt, retrieval, tool call, policy decision
🔹 a **hash-chained audit log**. Each entry includes the hash of the previous one, so any edit breaks the chain. [Confirm: your tamper-check script caught the edit.]
🔹 6 Sigma/YARA-L detections, e.g. [an agent calling send_email right after reading an external doc]
🔹 I replayed my Week 4 attacks: [X of Y] were detected
🔹 a one-page SOC runbook for "agent behaving badly"

Note: the OpenTelemetry GenAI conventions moved to their own repository in 2026 and are still marked "development". Pin the version you use.

If your agents can act, they need to be traceable.

#DetectionEngineering #SOC #AgenticAI #OpenTelemetry

---
**First comment (links):** Anthropic report – https://www.anthropic.com/news/disrupting-AI-espionage · OTel GenAI conventions – https://github.com/open-telemetry/semantic-conventions-genai · OWASP ACS – https://genai.owasp.org/resource/agent-control-standard-acs/
