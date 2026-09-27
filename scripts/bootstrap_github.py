#!/usr/bin/env python3
"""Create milestones (phases) and one issue per week from weeks/*.md.

Usage:  GITHUB_TOKEN=... python scripts/bootstrap_github.py <owner>/<repo>
Idempotent-ish: skips milestones/issues whose titles already exist.
"""
import json, os, re, sys, glob, urllib.request

REPO = sys.argv[1]
TOKEN = os.environ["GITHUB_TOKEN"]
API = f"https://api.github.com/repos/{REPO}"

PHASES = [  # title, due (end of phase), weeks
    ("Phase 1 · Foundations", "2026-10-11T23:59:59Z", [1, 2]),
    ("Phase 2 · Assess & Attack", "2026-11-01T23:59:59Z", [3, 4, 5]),
    ("Phase 3 · Defend & Identity", "2026-11-22T23:59:59Z", [6, 7, 8]),
    ("Phase 4 · SaaS Security", "2026-12-06T23:59:59Z", [9, 10]),
    ("Phase 5 · Operate & Govern", "2026-12-20T23:59:59Z", [11, 12]),
]
LABELS = {"week": "1d76db", "lab": "0e8a16", "interview": "d93f0b", "ai-security": "5319e7",
          "saas-security": "fbca04", "identity": "b60205", "grc": "006b75"}
WEEK_LABELS = {1: ["ai-security"], 2: ["ai-security"], 3: ["ai-security"], 4: ["ai-security"],
               5: ["ai-security"], 6: ["ai-security"], 7: ["identity", "ai-security"], 8: ["ai-security"],
               9: ["saas-security"], 10: ["saas-security", "identity"], 11: ["ai-security", "saas-security"], 12: ["grc"]}


def call(method, path, body=None):
    req = urllib.request.Request(API + path, method=method,
                                 data=json.dumps(body).encode() if body else None,
                                 headers={"Authorization": f"Bearer {TOKEN}",
                                          "Accept": "application/vnd.github+json"})
    try:
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read() or "null")
    except urllib.error.HTTPError as e:
        if e.code == 422:  # already exists
            return None
        raise


for name, color in LABELS.items():
    call("POST", "/labels", {"name": name, "color": color})

existing_ms = {m["title"]: m["number"] for m in call("GET", "/milestones?state=all&per_page=100")}
week_to_ms = {}
for title, due, weeks in PHASES:
    num = existing_ms.get(title) or call("POST", "/milestones", {"title": title, "due_on": due})["number"]
    for w in weeks:
        week_to_ms[w] = num

existing_issues = {i["title"] for i in call("GET", "/issues?state=all&per_page=100")}
for path in sorted(glob.glob("weeks/week-*.md")):
    text = open(path, encoding="utf-8").read()
    wk = int(re.search(r"week-(\d+)", path).group(1))
    header = text.splitlines()[0].lstrip("# ").strip()
    if header in existing_issues:
        continue
    boxes = "\n".join(l for l in text.splitlines() if l.strip().startswith("- [ ]"))
    body = (f"📄 Full detail: [`{path}`](../blob/main/{path})\n\n### Checklist\n{boxes}\n\n"
            "### Wrap-up\n- [ ] Note written in `notes/`\n- [ ] Interview questions answered out loud\n")
    call("POST", "/issues", {"title": header, "body": body, "milestone": week_to_ms[wk],
                             "labels": ["week"] + WEEK_LABELS[wk]})
    print("created", header)

prep = "Interview prep (ongoing)"
if prep not in existing_issues:
    call("POST", "/issues", {"title": prep, "labels": ["interview"],
                             "body": "- [ ] 10 STAR stories drafted (interview-prep/star-stories.md)\n"
                                     "- [ ] Siemens research checklist done\n- [ ] 30-60-90 pitch rehearsed\n"
                                     "- [ ] All concept checks < 60 s\n- [ ] 3 mock case interviews"})
print("done")
