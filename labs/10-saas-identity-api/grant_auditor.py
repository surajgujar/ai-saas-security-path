"""OAuth grant auditor: flag risky third-party app grants and produce a revoke list (dry-run).

Real version calls the Google Admin SDK tokens.list or MS Graph oauth2PermissionGrants. Here
you read data/oauth_grants.json. Run: uv run python grant_auditor.py
"""
import csv
import json
import sys
from pathlib import Path

DATA = Path(__file__).parent / "data"

# Scopes that grant broad mailbox/drive/admin access = high risk.
HIGH_RISK_SCOPES = {"https://mail.google.com/", "gmail.modify", "drive",
                    "admin.directory.user.readonly"}
STALE_DAYS = 90


def audit(grants: list[dict]) -> list[dict]:
    """Return grants with a risk assessment: each grant plus 'reasons' and 'risk' (high/med/low).

    TODO(step 2): implement. Flag a grant when ANY of:
      - it has a high-risk scope (intersect scopes with HIGH_RISK_SCOPES)
      - the app is unverified (verified == False)
      - it's stale (last_used_days > STALE_DAYS)
    risk = high if (high-risk scope AND (unverified OR stale)) else med if any single flag else low.
    """
    raise NotImplementedError("Finish audit() (step 2)")


def write_revoke_list(audited: list[dict], path: Path) -> int:
    """Write a CSV of grants to revoke (risk == high). DRY RUN: this only writes the list."""
    high = [g for g in audited if g.get("risk") == "high"]
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["client_id", "app", "user", "reasons"])
        for g in high:
            w.writerow([g["client_id"], g["app"], g["user"], "; ".join(g["reasons"])])
    return len(high)


if __name__ == "__main__":
    grants = json.loads((DATA / "oauth_grants.json").read_text())
    audited = audit(grants)
    for g in sorted(audited, key=lambda x: {"high": 0, "med": 1, "low": 2}[x["risk"]]):
        print(f"[{g['risk'].upper():4}] {g['app']:16} {g['user']:8} {', '.join(g['reasons']) or 'ok'}")
    n = write_revoke_list(audited, DATA / "revoke_list.csv")
    print(f"\nDRY RUN: {n} grants would be revoked (see data/revoke_list.csv). No revocation performed.")
    if "--revoke" in sys.argv:
        print("TODO(stretch): call the admin API to actually revoke. Keep dry-run the default.")
