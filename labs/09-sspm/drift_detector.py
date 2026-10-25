"""SSPM drift detector: compare a live settings snapshot to a committed baseline and alert.

In a real deployment you'd pull the snapshot from an admin API (Google Admin SDK, MS Graph,
Salesforce Health Check). Here you read data/settings_baseline.json and a "current" file you
edit to simulate a change. Run: uv run python drift_detector.py
"""
import json
from pathlib import Path

DATA = Path(__file__).parent / "data"

# Controls that must hold. Each maps a setting to its required value and a severity.
# TODO(step 2): extend this to ~20 controls (see README). Start with these.
POLICY = {
    "mfa_enforced_all_users": {"required": True, "severity": "critical"},
    "external_sharing": {"required": "none_or_allowlist", "severity": "high"},
    "oauth_app_allowlist_enabled": {"required": True, "severity": "high"},
    # TODO: admin_count <= 5, session_max_hours <= 168, password_min_length >= 14, guest_access False, ...
}


def evaluate(settings: dict) -> list[dict]:
    """Return a list of violations: [{control, required, actual, severity}]."""
    findings = []
    # TODO(step 2): for each control in POLICY, compare settings[control] to the requirement
    #   and append a finding when it doesn't meet it. Handle the "none_or_allowlist" case.
    raise NotImplementedError("Finish evaluate() (step 2)")


def diff(baseline: dict, current: dict) -> dict:
    """Return {key: [old, new]} for every setting that changed."""
    return {k: [baseline.get(k), current.get(k)] for k in baseline | current
            if baseline.get(k) != current.get(k)}


if __name__ == "__main__":
    baseline = json.loads((DATA / "settings_baseline.json").read_text())
    current_path = DATA / "settings_current.json"
    current = json.loads(current_path.read_text()) if current_path.exists() else baseline

    for f in evaluate(current):
        print(f"[{f['severity'].upper():8}] {f['control']}: need {f['required']}, got {f['actual']}")
    changes = diff(baseline, current)
    if changes:
        print("\nDrift since baseline:")
        for k, (old, new) in changes.items():
            print(f"  {k}: {old} -> {new}")
