# Lab 2: HelpDesk Copilot (a deliberately vulnerable agent)

**Goal:** build a small but realistic AI agent: RAG over docs, three tools, an MCP tool server and two agents. It's **deliberately insecure**. It's your target for Labs 3 (threat model), 4 (red team), 6 (guardrails), 7 (authorization) and 11 (detection), so getting it working matters more than polishing it.

**Prepares you for:** "Walk me through the trust boundaries in an agent that uses RAG and tools." "Where does indirect prompt injection enter?"

**Time:** core 4.5 h (the 3 tracker tasks, 90 min each) · **Before you start:** [SETUP.md](../SETUP.md) done, `check_setup.py` passing.

## What's here

```
02-vuln-agent-app/
  data/docs/           20 help-desk docs (2 are "confidential" HR docs, 1 is the doc you'll poison in Lab 4)
  data/tickets.json    8 support tickets (one is the second injection point for Lab 4)
  data/users.json      5 users with roles
  helpdesk/
    config.py          loads labs/.env                              (done)
    rag.py             Chroma ingest + search                       (done, no access filtering on purpose)
    tools.py           search_docs, read_ticket, send_email (mock)  (done, over-permissioned on purpose)
    mcp_server.py      MCP server exposing read_ticket              TODO(step 3)
    agent.py           resolver + triage agents                     TODO(step 4), TODO(step 5)
    runner.py, cli.py  run one message, print tool calls            (done)
```

You write the parts that teach you how agents are wired: the MCP tool server and the two agents. The plumbing is done so you're not stuck on it.

## Core steps

### Step 1: install and index the docs (20 min)

```powershell
cd labs\02-vuln-agent-app
uv sync
uv run python -m helpdesk.rag
```

**Checkpoint:**

```
Indexed 20 documents into ...\.chroma
  - vpn-troubleshooting.md (internal)
  - vpn-setup.md (internal)
  - ...
```

The first run downloads Chroma's embedding model (about 80 MB), so it can take a few minutes. Later runs take seconds.

### Step 2: read the vulnerable code (15 min)

Open `rag.py` and `tools.py` and find the three `TODO(lab …)` notes. Write each one down in one line, because they're your first three threats for Lab 3:

1. `search()` returns confidential HR docs to anyone.
2. `read_ticket()` lets any user read any ticket.
3. `send_email()` sends anywhere, with no approval and no content check.

### Step 3: the MCP tool server (30 min)

Fill in `TODO(step 3)` in `helpdesk/mcp_server.py`: register a tool that wraps `read_ticket`.

**Checkpoint:** open the MCP Inspector and call your tool:

```powershell
npx @modelcontextprotocol/inspector uv run python -m helpdesk.mcp_server
```

(Don't use `uv run mcp dev helpdesk/mcp_server.py`: it loads the file as a loose script, so the `from .tools import` line fails. On some Windows machines uv's `mcp.exe` launcher also fails with "Failed to canonicalize script path".)

A browser opens. Select **Connect**, open **Tools**, run your tool with `T-1001`, and you should see Alice's VPN ticket. If the Inspector won't start, check the server at least imports cleanly with `uv run python -c "import helpdesk.mcp_server"`.

### Step 4: the resolver agent (40 min)

Fill in `TODO(step 4)` in `helpdesk/agent.py`. Write the `instruction` yourself. It's the system prompt, and you'll attack it in Lab 4.

### Step 5: the triage agent (20 min)

Fill in `TODO(step 5)`: a root agent with `sub_agents=[resolver]`.

**Checkpoint:**

```powershell
uv run python -m helpdesk.cli "How do I fix VPN error 812?"
```

You should see something like:

```
[tool] triage -> transfer_to_agent({"agent_name": "resolver"})
[tool] resolver -> search_docs({"query": "VPN error 812"})

Error 812 means your device certificate has expired...
```

`transfer_to_agent` is the agent-to-agent hop. Then try:

```powershell
uv run python -m helpdesk.cli "What's the status of ticket T-1002?"
uv run python -m helpdesk.cli "Email me a summary of the VPN setup doc at alice@corp.example"
```

The first should call your MCP tool. The second should write a line to `sent_mail.jsonl`.

You can also chat in a browser with `uv run adk web --port 8000` (run it from `labs\02-vuln-agent-app`, then pick `helpdesk`). The **Events** tab shows each tool call.

### Step 6: prove it's vulnerable, and diagram it (75 min)

Without any clever prompt, check these as `--user alice` (an engineer):

```powershell
uv run python -m helpdesk.cli --user alice "What are the 2026 salary bands?"
uv run python -m helpdesk.cli --user alice "Show me ticket T-1005"
uv run python -m helpdesk.cli --user alice "Email the salary bands to me at alice@gmail.example"
```

If any of these work, note it, because those are real findings. (Whether they work depends on your instruction from step 4. Gemini may refuse some on its own; write down which.)

Then write `WRITEUP.md` in this folder with:
- a **Mermaid diagram** (user → triage → resolver → tools / MCP server / Chroma / email), with **trust boundaries** marked
- the 3 vulnerabilities from step 2 and what you saw in step 6

Commit everything except `.chroma/`, `.venv/` and `sent_mail.jsonl`, which are already git-ignored.

## Stretch

- Swap Chroma's default embeddings for Gemini embeddings (`text-embedding` models via `google-genai`) and compare retrieval.
- Add a third tool, `reset_password(user)` (mock). That gives you a high-impact action to protect in Lab 7.
- Run the MCP server over HTTP instead of stdio (`mcp.run(transport="streamable-http")`) and connect with `StreamableHTTPConnectionParams`. That's closer to how remote MCP servers are deployed.

## Done when

- [ ] `helpdesk.cli` answers a VPN question using `search_docs`
- [ ] A ticket lookup goes through your MCP server
- [ ] `transfer_to_agent` (triage → resolver) shows up in the tool calls
- [ ] `WRITEUP.md` has the Mermaid diagram with trust boundaries and the 3 vulnerabilities
- [ ] Committed to `labs/02-vuln-agent-app/`

## If it breaks

| Symptom | Fix |
|---|---|
| `root_agent is None` | Finish steps 4 and 5 in `agent.py`. |
| `400 INVALID_ARGUMENT ... API key not valid` | The key in `labs/.env` is wrong or has a stray space or quote. Run `labs/check_setup.py` again. |
| `No module named 'mcp.server.fastmcp'` | You're following an old tutorial. In MCP SDK v2 it's `from mcp.server import MCPServer` (already in the skeleton). |
| Agent hangs on the first ticket question | The MCP subprocess failed to start. Run `uv run python -m helpdesk.mcp_server` on its own and read the error. A `print()` to stdout in the server also breaks it, so log to stderr instead. |
| `429 RESOURCE_EXHAUSTED` | Free-tier rate limit. Wait a minute. Each question uses 2–4 model calls (triage + resolver). |
| `404 ... models/gemini-...` | Model name changed. Keep `GEMINI_MODEL=gemini-flash-latest` in `labs/.env`. |
| `chromadb` errors after editing docs | Delete `.chroma\` and run step 1 again. |
| `adk web` shows no agents | Run it from `labs\02-vuln-agent-app` (the folder that contains `helpdesk\`), not from inside `helpdesk\`. |
