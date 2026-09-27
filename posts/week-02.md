# Week 2 post: I built a deliberately vulnerable AI agent

**Publish:** Fri 9 Oct 2026 · **Visual:** the Mermaid diagram of HelpDesk Copilot with trust boundaries drawn in red

---

This weekend I built an AI agent **designed to be hacked**.

"HelpDesk Copilot":
• RAG over ~20 internal docs, including one confidential HR file and one with hidden instructions
• 3 tools: search docs, read tickets, send email
• a second agent that triages tickets and hands them to a resolver
• one tool exposed through an MCP server

Why deliberately vulnerable? Because it has all three parts of what Simon Willison calls the **lethal trifecta**:
1️⃣ access to private data (the HR doc)
2️⃣ exposure to untrusted content (any doc or ticket can carry instructions)
3️⃣ a way to send data out (send_email)

Any agent with all three can be tricked into leaking data. It doesn't take a clever jailbreak, just one poisoned document.

What surprised me while building it: [e.g. how many trust boundaries appear once a second agent and an MCP server are involved: X in my diagram].

For the next 10 weeks this app is my target. I'll threat-model it, red-team it, then fix it layer by layer and measure the difference.

Building agents at work? Check which of your agents have all three parts of the trifecta.

#AgenticAI #AISecurity #MCP #PromptInjection

---
**First comment (links):** The lethal trifecta – https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/ · MCP spec 2026-07-28 – https://modelcontextprotocol.io/specification/2026-07-28
