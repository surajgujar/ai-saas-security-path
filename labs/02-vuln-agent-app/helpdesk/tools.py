"""The three agent tools: search_docs, read_ticket, send_email.

All three are deliberately over-permissioned (no per-user checks, external email allowed).
That is the point of lab 2. Labs 6 and 7 add the checks.
"""
import json
from pathlib import Path

from .config import DATA_DIR
from .rag import search

# send_email is a mock: it appends to this file instead of really sending.
SENT_MAIL = Path(__file__).resolve().parents[1] / "sent_mail.jsonl"


def search_docs(query: str) -> dict:
    """Search the IT help-desk knowledge base and return the most relevant documents.

    Args:
        query: what the user is asking about.
    """
    hits = search(query, k=3)
    return {"status": "ok", "results": hits}


def read_ticket(ticket_id: str) -> dict:
    """Look up a support ticket by its id (e.g. 'T-1001').

    TODO(lab 7): there is no check that the current user owns this ticket. Any user can read
    any ticket. Lab 7 adds authorization so a user only reads their own tickets.
    """
    tickets = json.loads((DATA_DIR / "tickets.json").read_text(encoding="utf-8"))
    for t in tickets:
        if t["id"].lower() == ticket_id.lower():
            return {"status": "ok", "ticket": t}
    return {"status": "not_found", "ticket_id": ticket_id}


def send_email(to: str, subject: str, body: str) -> dict:
    """Send an email (MOCK - writes to sent_mail.jsonl, does not really send).

    Args:
        to: recipient address.
        subject: email subject.
        body: email body.

    TODO(lab 6): this sends to ANY address, including outside the company, with no human
    approval and no check on what's in the body. That's the exfiltration path labs 3/4 abuse.
    Lab 6 adds: block external domains without approval, and DLP-scan the body.
    """
    rec = {"to": to, "subject": subject, "body": body}
    with SENT_MAIL.open("a", encoding="utf-8") as f:
        f.write(json.dumps(rec) + "\n")
    return {"status": "sent", "to": to}
