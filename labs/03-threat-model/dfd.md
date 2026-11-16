# HelpDesk Copilot: data-flow diagram

The Lab 2 app (`labs/02-vuln-agent-app`) drawn as a data-flow diagram with trust boundaries. Each dashed box is a trust zone. Every arrow that crosses a dashed edge is a trust boundary and gets at least one threat in [threats.md](threats.md).

## Diagram

```mermaid
flowchart LR
    %% ---------- Zone 0: untrusted users ----------
    subgraph Z0["Zone 0: Untrusted user input"]
        direction TB
        U["User<br/>alice / bob / carol / dave / mallory"]
        CLI["CLI: helpdesk.cli<br/>--user flag = claimed identity"]
    end

    %% ---------- Zone 1: agent runtime ----------
    subgraph Z1["Zone 1: Agent runtime, ADK InMemoryRunner"]
        direction TB
        TRI["Triage agent, root<br/>no tools, delegates only"]
        RES["Resolver agent<br/>search_docs, send_email, MCP tools"]
        SD["search_docs tool"]
        SE["send_email tool"]
        LOG[("Session state + tool-call log<br/>stdout, sent_mail.jsonl, password_resets.jsonl")]
    end

    %% ---------- Zone 2: third-party model ----------
    subgraph Z2["Zone 2: External model provider"]
        LLM["LLM API<br/>Gemini AI Studio / Vertex / Claude"]
        EMB["Embedding API<br/>only if LAB_EMBEDDINGS=gemini"]
    end

    %% ---------- Zone 3: data stores ----------
    subgraph Z3["Zone 3: Data stores, mixed classification"]
        direction TB
        CHROMA[("Chroma vector DB<br/>public + internal + confidential HR docs<br/>no role filter")]
        DOCS[/"data/docs/*.md<br/>UNTRUSTED CONTENT #1"/]
        TIX[/"data/tickets.json<br/>UNTRUSTED CONTENT #2<br/>free text written by any user"/]
        USERS[/"data/users.json"/]
    end

    %% ---------- Zone 4: MCP tool server ----------
    subgraph Z4["Zone 4: MCP tool server, separate process"]
        MCP["helpdesk-tools MCP server<br/>get_ticket, reset_password<br/>stdio or HTTP :8765, no auth"]
    end

    %% ---------- Zone 5: outside world ----------
    subgraph Z5["Zone 5: Internet / external recipients"]
        EXT["Any email address<br/>incl. attacker@evil.example"]
        ATT["Network caller<br/>anything that reaches :8765"]
    end

    U -->|"1. prompt"| CLI
    CLI -->|"2. message + user_id, unauthenticated"| TRI
    TRI <-->|"3. prompts / completions"| LLM
    TRI -->|"4. transfer_to_agent"| RES
    RES <-->|"5. prompts + tool results / tool-call choices"| LLM

    RES -->|"6. search_docs query"| SD
    SD -->|"7. query"| CHROMA
    DOCS -.->|"ingest"| CHROMA
    CHROMA -.->|"embed"| EMB
    CHROMA ==>|"8. top-3 docs, any classification"| SD
    SD ==>|"9. doc text into model context: INJECTION SURFACE #1"| RES

    RES -->|"10. get_ticket / reset_password"| MCP
    MCP --> TIX
    MCP --> USERS
    MCP ==>|"11. ticket text into model context: INJECTION SURFACE #2"| RES
    MCP -->|"temp password in response"| RES

    RES -->|"12. send_email to, subject, body"| SE
    SE -->|"13. EXFIL PATH: any domain, no approval, no DLP"| EXT
    ATT -->|"direct call, bypasses agent"| MCP

    RES --> LOG
    SE --> LOG
    MCP --> LOG
    RES -->|"14. answer"| CLI

    classDef untrusted fill:#ffe0e0,stroke:#c00,stroke-width:2px,color:#000;
    classDef exfil fill:#fff2cc,stroke:#b8860b,stroke-width:2px,color:#000;
    class DOCS,TIX,U,ATT untrusted;
    class EXT,SE exfil;

    style Z0 stroke-dasharray: 6 4
    style Z1 stroke-dasharray: 6 4
    style Z2 stroke-dasharray: 6 4
    style Z3 stroke-dasharray: 6 4
    style Z4 stroke-dasharray: 6 4
    style Z5 stroke-dasharray: 6 4
```

Legend: dashed box = trust zone. Thick arrow `==>` = untrusted content entering the model's context (the injection surface). Red node = untrusted source. Yellow node = exfiltration channel.

## Components

| Component | Code | What it does | Trust |
|---|---|---|---|
| CLI | `helpdesk/cli.py`, `runner.py` | Takes the message and `--user`, runs one turn, prints tool calls | Identity is whatever the caller types. No authentication. |
| Triage agent | `agent.py` `root_agent` | Reads the request and hands IT questions to the resolver | Has no tools, but decides what the resolver is asked to do |
| Resolver agent | `agent.py` `resolver` | Answers from docs and calls tools | Has every tool. No safety rules in its instruction. |
| `search_docs` | `tools.py`, `rag.py` | Top-3 semantic search over Chroma | Returns any classification to any user |
| `send_email` | `tools.py` | Mock email to `sent_mail.jsonl` | Any recipient, any body, no approval |
| MCP server | `mcp_server.py` | `get_ticket`, `reset_password` | Trusts every caller (stdio parent or any HTTP client) |
| LLM / embedding API | `model.py`, `embeddings.py` | Third-party inference | Prompts, docs and tickets leave the machine |
| Chroma | `.chroma/` | Vector store | Public, internal and confidential HR docs in one collection |
| Docs / tickets | `data/` | Knowledge base, ticket queue | Content can be written by people who aren't the current user |

## Trust boundaries

| # | Boundary | What crosses it | Why it matters |
|---|---|---|---|
| TB1 | User → CLI/runner | Prompt text, claimed `user_id` | Direct prompt injection. `--user` is self-asserted, so anyone can claim to be anyone. |
| TB2 | Runner → LLM provider | System prompts, user prompts, retrieved docs, ticket text, tool results | Data leaves the company. The model, not the code, picks the tools and their arguments. |
| TB3 | Triage → Resolver | Delegated task via `transfer_to_agent` | The resolver trusts whatever triage passes on. Triage does no filtering. |
| TB4 | Chroma → model context | Retrieved doc text | **Injection surface #1.** Doc content is treated like trusted instructions. Confidential HR docs reach any user. |
| TB5 | MCP server → model context | Ticket descriptions written by any user, temp passwords | **Injection surface #2.** One user's ticket text is read into another user's session. |
| TB6 | Agent → MCP server | Tool calls over stdio or HTTP | No caller identity is passed and the server checks none. Over HTTP anyone who can reach the port can call `reset_password`. |
| TB7 | `send_email` → outside world | Recipient, subject, body chosen by the model | **The exfiltration path.** No domain allow-list, no human approval, no DLP. |
| TB8 | App → logs / files | Tool args, email bodies, temp passwords | Secrets and PII persist in plaintext. |

## Where untrusted content first reaches the model

1. **Retrieved documents (TB4).** `search_docs` returns the full text of the top 3 docs, and ADK puts that text into the resolver's next model call. A poisoned doc in `data/docs/` (or anywhere the ingest reads) gets read with the same authority as the system prompt. Lab 4 uses this for the poisoned-doc → `send_email` exfil.
2. **Ticket text (TB5).** `get_ticket` returns `description`, which any user can write (see `T-1007`, mallory's ticket). When another user or an agent reads that ticket, the description lands in the model context and can steer later tool calls (`send_email`, `reset_password`).

Both surfaces end in the same place: a resolver that can email anywhere and reset any password. That's why the controls in [threats.md](threats.md) focus on the tool layer (Labs 6 and 7) rather than on prompt wording.

## Observations from running Lab 2

- `uv run python -m helpdesk.cli --user alice "Show me ticket T-1005"` returns dave's phishing ticket. There's no ownership check.
- Any user's search can return `hr-salary-bands-2026.md` and `hr-performance-process.md`. Confidential and public docs share one index with no filter.
- `send_email` sends to any address with no approval and no check on the content.
- With `LAB_MCP_TRANSPORT=http`, the MCP server can be called directly (`helpdesk/mcp_direct.py`), skipping the agent and anything the agent code might check.
