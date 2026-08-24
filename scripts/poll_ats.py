#!/usr/bin/env python3
"""Company-first ATS polling: for each org, try the common ATS board-index URLs
(one request each) and report which respond, with any job titles matching a filter.

Usage:
  poll_ats.py orgs.txt --filter "product|design|growth" [--patterns greenhouse,lever,ashby,...]
              [--out found.json] [--delay 0.5]
  poll_ats.py orgs.txt --urls-only          # print the candidate board URLs, no fetching

IMPORTANT — restricted environments: some sandboxes route web access through a proxy
that blocks direct HTTP from scripts (only the WebFetch tool is allowed out). If the
first few orgs all come back as network errors, switch to `--urls-only`: the script
then just enumerates org x pattern URLs, and the agent WebFetches each URL itself
(the board index still costs one fetch per org and lists everything open there).

orgs.txt: one org slug per line (lowercase, no spaces — e.g. "gohighlevel", "spotdraft").
Optionally "slug, Display Name" per line.

Output JSON: [{org, pattern, url, status, matches:[{title, href}], all_titles_count}]
Notes:
- This is a cheap breadth probe, not a verifier. Every match must still be fetched
  and verified per the agent template (eligibility quote, employer identity, freshness).
- JS-gated boards (Workday, Zoho, Darwinbox) won't render titles here; a 200 with
  zero titles on those patterns means "check via Google slugs", not "no roles".
"""
import argparse, json, re, sys, time, urllib.request

PATTERNS = {
    "greenhouse":     "https://job-boards.greenhouse.io/{org}",
    "greenhouse_old": "https://boards.greenhouse.io/{org}",
    "lever":          "https://jobs.lever.co/{org}",
    "ashby":          "https://jobs.ashbyhq.com/{org}",
    "workable":       "https://apply.workable.com/{org}/",
    "teamtailor":     "https://{org}.teamtailor.com/jobs",
    "pinpoint":       "https://{org}.pinpointhq.com",
    "smartrecruiters":"https://careers.smartrecruiters.com/{org}",
    "recruitee":      "https://{org}.recruitee.com",
    "bamboohr":       "https://{org}.bamboohr.com/careers",
    "gohire":         "https://jobs.gohire.io/{org}",
}
UA = {"User-Agent": "Mozilla/5.0 (job-search research; contact: candidate)"}
TITLE_RE = re.compile(r'<a[^>]+href="([^"]+)"[^>]*>([^<]{4,120})</a>', re.I)
TAG_RE = re.compile(r"<[^>]+>")

def fetch(url, timeout=15):
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read(400_000).decode("utf-8", "ignore")
    except Exception as e:
        return getattr(e, "code", None) or str(e.__class__.__name__), ""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("orgs_file")
    ap.add_argument("--filter", default="", help="regex over link text, case-insensitive")
    ap.add_argument("--patterns", default=",".join(PATTERNS))
    ap.add_argument("--out", default="poll_ats_found.json")
    ap.add_argument("--delay", type=float, default=0.4)
    ap.add_argument("--urls-only", action="store_true",
                    help="print org x pattern URLs and exit (for WebFetch-based polling)")
    a = ap.parse_args()
    flt = re.compile(a.filter, re.I) if a.filter else None
    pats = [p for p in a.patterns.split(",") if p in PATTERNS]
    if a.urls_only:
        for line in open(a.orgs_file):
            line = line.strip()
            if not line or line.startswith("#"): continue
            slug = line.split(",")[0].strip().lower()
            for p in pats:
                print(PATTERNS[p].format(org=slug))
        return
    results = []
    for line in open(a.orgs_file):
        line = line.strip()
        if not line or line.startswith("#"): continue
        slug = line.split(",")[0].strip().lower()
        hit = False
        for p in pats:
            url = PATTERNS[p].format(org=slug)
            status, html = fetch(url)
            time.sleep(a.delay)
            if status != 200 or not html: continue
            links = [(h, TAG_RE.sub("", t).strip()) for h, t in TITLE_RE.findall(html)]
            titles = [(h, t) for h, t in links if len(t.split()) >= 2]
            matches = [{"title": t, "href": h} for h, t in titles if (not flt or flt.search(t))]
            results.append({"org": slug, "pattern": p, "url": url, "status": status,
                            "matches": matches[:40], "all_titles_count": len(titles)})
            print(f"{slug:24s} {p:14s} 200  titles~{len(titles):3d}  matches={len(matches)}", file=sys.stderr)
            hit = True
            break   # first responding pattern wins; remove to sweep all
        if not hit:
            results.append({"org": slug, "pattern": None, "url": None, "status": "no_ats_found",
                            "matches": [], "all_titles_count": 0})
            print(f"{slug:24s} -- no ATS pattern responded", file=sys.stderr)
    json.dump(results, open(a.out, "w"), indent=1)
    found = sum(1 for r in results if r["matches"])
    print(f"\n{len(results)} orgs polled, {found} with filter matches -> {a.out}", file=sys.stderr)

if __name__ == "__main__":
    main()
