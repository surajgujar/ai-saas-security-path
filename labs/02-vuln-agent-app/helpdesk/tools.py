"""The agent tools: search_docs, read_ticket, send_email, reset_password.

All of them are deliberately over-permissioned (no per-user checks, external email allowed).
That is the point of lab 2. Labs 6 and 7 add the checks.
"""
import json
import secrets
from datetime import datetime, timezone
from pathlib import Path

from .config import DATA_DIR
from .rag import search

# send_email is a mock: it appends to this file instead of really sending.
SENT_MAIL = Path(__file__).resolve().parents[1] / "sent_mail.jsonl"
# reset_password is a mock too: it logs here instead of touching a real directory.
PASSWORD_RESETS = Path(__file__).resolve().parents[1] / "password_resets.jsonl"


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


def reset_password(user: str) -> dict:
    """Reset a user's password and return a temporary one (MOCK - writes to password_resets.jsonl).

    Args:
        user: the username whose password to reset, e.g. 'alice'.

    TODO(lab 7): this is the high-impact action. There is no check that the caller IS `user`
    (or is an admin), no step-up auth (MFA), and no human approval. It also hands the temporary
    password straight back to whoever asked, so "reset dave's password" is an account takeover.
    Lab 7 adds: callers may only reset themselves, and the temp password goes to the user's
    registered email, never into the chat.
    """
    users = json.loads((DATA_DIR / "users.json").read_text(encoding="utf-8"))
    user = user.strip().lower()
    if user not in users:
        return {"status": "not_found", "user": user}
    temp = secrets.token_urlsafe(9)
    rec = {"at": datetime.now(timezone.utc).isoformat(timespec="seconds"), "user": user, "temporary_password": temp}
    with PASSWORD_RESETS.open("a", encoding="utf-8") as f:
        f.write(json.dumps(rec) + "\n")
    return {"status": "reset", "user": user, "temporary_password": temp}
