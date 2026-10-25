"""A tamper-evident, hash-chained audit log for agent actions.

Each entry stores the SHA-256 of the previous entry, so editing or deleting any past entry
breaks the chain and `verify()` catches it. Run: uv run python audit_log.py
"""
import hashlib
import json
from pathlib import Path

LOG = Path(__file__).parent / "agent_audit.jsonl"
GENESIS = "0" * 64


def _hash(prev_hash: str, record: dict) -> str:
    """Hash of prev_hash + the record's canonical JSON."""
    blob = prev_hash + json.dumps(record, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(blob.encode()).hexdigest()


def append(record: dict) -> None:
    """Append one event, chaining it to the last line's hash.

    TODO(step 2): implement.
      - read the last line's 'hash' (or GENESIS if the file is empty/missing)
      - h = _hash(prev, record)
      - write a JSON line: {"record": record, "prev": prev, "hash": h}
    """
    raise NotImplementedError("Finish append() (step 2)")


def verify() -> tuple[bool, int]:
    """Re-walk the chain. Return (ok, first_bad_line_number). ok=True means untampered."""
    prev = GENESIS
    if not LOG.exists():
        return True, -1
    for i, line in enumerate(LOG.read_text(encoding="utf-8").splitlines(), 1):
        entry = json.loads(line)
        if entry["prev"] != prev or _hash(prev, entry["record"]) != entry["hash"]:
            return False, i
        prev = entry["hash"]
    return True, -1


if __name__ == "__main__":
    # demo: write 3 events, verify, tamper, verify again
    LOG.unlink(missing_ok=True)
    for ev in [{"user": "alice", "tool": "search_docs", "allow": True},
               {"user": "alice", "tool": "send_email", "to": "x@evil.example", "allow": False},
               {"user": "bob", "tool": "get_ticket", "allow": True}]:
        append(ev)
    print("after writes:", verify())  # (True, -1)
    lines = LOG.read_text().splitlines()
    lines[1] = lines[1].replace('"allow": false', '"allow": true')  # tamper
    LOG.write_text("\n".join(lines) + "\n")
    print("after tamper:", verify())  # (False, 2)
