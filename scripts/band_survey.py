#!/usr/bin/env python3
"""Band survey: tally years-of-experience requirements across sampled posting texts.

Usage:
  band_survey.py samples.json [--out band_report.json]

samples.json: [{"org": "...", "title": "...", "text": "<full JD text or requirements section>"}]
(The orchestrator/agents collect the texts — this script only does the tallying,
so there are no network calls and results are reproducible.)

Extracts patterns like "8+ years", "6-9 yrs", "minimum of 5 years", takes the
minimum bar per posting, and reports count/median/IQR plus the per-posting list.
Use the output to calibrate on-level vs Reach titles and to write the strategy
sentence in the final brief.
"""
import argparse, json, re, statistics as st

PATS = [
    re.compile(r"(\d{1,2})\s*[-–to]{1,3}\s*(\d{1,2})\+?\s*(?:years?|yrs?)", re.I),
    re.compile(r"(?:minimum of|min\.?|at least)\s*(\d{1,2})\+?\s*(?:years?|yrs?)", re.I),
    re.compile(r"(\d{1,2})\s*\+\s*(?:years?|yrs?)", re.I),
    re.compile(r"(\d{1,2})\+?\s*(?:years?|yrs?)(?:\s+of)?\s+(?:experience|exp)", re.I),
]

def min_bar(text):
    bars = []
    for pat in PATS:
        for m in pat.finditer(text):
            nums = [int(g) for g in m.groups() if g and g.isdigit()]
            if nums:
                bars.append(min(nums))
    bars = [b for b in bars if 0 < b <= 30]
    return min(bars) if bars else None   # the *entry* bar of the posting

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("samples_file")
    ap.add_argument("--out", default="band_report.json")
    a = ap.parse_args()
    samples = json.load(open(a.samples_file))
    rows, bars = [], []
    for s in samples:
        b = min_bar(s.get("text", ""))
        rows.append({"org": s.get("org"), "title": s.get("title"), "min_years_bar": b})
        if b is not None:
            bars.append(b)
    rep = {"postings_sampled": len(samples), "with_stated_bar": len(bars)}
    if bars:
        bars.sort()
        q = st.quantiles(bars, n=4) if len(bars) >= 4 else [bars[0], bars[len(bars)//2], bars[-1]]
        rep.update({"median": st.median(bars), "iqr": [q[0], q[2]],
                    "min": bars[0], "max": bars[-1],
                    "share_at_or_below": {str(y): round(sum(1 for b in bars if b <= y)/len(bars), 2)
                                          for y in sorted({3,5,6,8,10,12,15} & set(range(bars[0], bars[-1]+1)) | {bars[0], bars[-1]})}})
    rep["rows"] = rows
    json.dump(rep, open(a.out, "w"), indent=1)
    if bars:
        print(f"{len(bars)}/{len(samples)} postings state a bar. median={rep['median']} IQR={rep['iqr']} range={bars[0]}-{bars[-1]}")
        print("share of postings a candidate clears, by their years:", rep["share_at_or_below"])
    else:
        print("No stated bars found in sample.")

if __name__ == "__main__":
    main()
