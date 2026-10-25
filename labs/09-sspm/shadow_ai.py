"""Shadow AI discovery: find GenAI usage in a web proxy log and rank users by risk.

Run: uv run python shadow_ai.py
Reads data/proxy_log.csv and data/genai_domains.txt.
"""
import csv
from collections import defaultdict
from pathlib import Path

DATA = Path(__file__).parent / "data"


def load_genai_domains() -> set[str]:
    return {d.strip() for d in (DATA / "genai_domains.txt").read_text().splitlines() if d.strip()}


def discover() -> list[dict]:
    """Return a risk-ranked report: [{user, ai_hits, ai_bytes_up, domains}], worst first.

    TODO(step 3): implement.
      - read proxy_log.csv
      - for each row whose domain is in the genai set, tally per user: count, sum(bytes_up), set(domains)
      - risk-rank by bytes uploaded to AI domains (data leaving is the concern), then by hits
    """
    raise NotImplementedError("Finish discover() (step 3)")


if __name__ == "__main__":
    for r in discover():
        print(f"{r['user']:10} hits={r['ai_hits']:3} up={r['ai_bytes_up']:>8} domains={sorted(r['domains'])}")
