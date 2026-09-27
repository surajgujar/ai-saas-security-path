#!/usr/bin/env python3
"""Check every link in tracker/plan.json.

Usage (from repo root):  python scripts/check_links.py
External links are fetched; links into this repo are checked against local files.
Exit code 1 if anything is dead. Some sites (gartner.com, cisa.gov, iso.org, oreilly.com)
block scripts with 403 even though the page works in a browser; those are reported as "blocked".
"""
import json, os, sys, urllib.request, concurrent.futures as cf

REPO_PREFIX = "https://github.com/surajgujar/ai-saas-security-path/blob/main/"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/128 Safari/537.36",
      "Accept-Language": "en"}

plan = json.load(open("tracker/plan.json", encoding="utf-8"))
links = {}  # url -> [task ids]
for day in plan["days"]:
    for t in day["tasks"]:
        if not t.get("links"):
            print("NO LINKS", t["id"])
        for l in t.get("links", []):
            links.setdefault(l["url"], []).append(t["id"])


def check(url):
    if url.startswith(REPO_PREFIX):
        path = url[len(REPO_PREFIX):].split("#")[0]
        return url, "ok" if os.path.exists(path) else "missing file"
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=25) as r:
            return url, "ok" if r.status < 400 else str(r.status)
    except urllib.error.HTTPError as e:
        return url, "blocked" if e.code in (401, 403, 429) else str(e.code)
    except Exception as e:  # timeouts, DNS, TLS
        return url, "error: " + str(e)[:60]


bad = 0
with cf.ThreadPoolExecutor(12) as ex:
    for url, status in ex.map(check, sorted(links)):
        if status != "ok":
            print(f"{status:14} {url}  ({', '.join(links[url][:3])})")
            bad += status != "blocked"
print(f"{len(links)} unique links checked, {bad} dead")
sys.exit(1 if bad else 0)
