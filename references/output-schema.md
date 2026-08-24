# Output schema — role record and workbook

`scripts/build_master_xlsx.py` and `scripts/merge_delta.py` consume `{"meta":{...},"roles":[...],"leads":[...],"top_picks":[...],"cv_keywords":[...],"boards":[...],"coverage":[...],"notes":[...],"run_log":[...]}`. Only `roles` is required. Field names are exact.

```json
{
 "meta": {"candidate":"Name","run_date":"2026-08-18","scope":"...","pass_label":"Fresh search","audit_correction_rate":"3/19","sources_nothing_new":"..."},
 "roles": [{
   "source_report": "Channel B — ATS polling",
   "scope": "Remote from India",              // Remote from <country> | <City> | <City> satellite | Global remote (eligibility TBC) | Relocation
   "role_title": "…", "organisation": "…",     // organisation = TRUE employer (never the recruiter)
   "location_arrangement": "verbatim eligibility quote or location line",
   "category": "…",
   "board_found_on": "RemoteRocketship -> Lever (employer ATS)",
   "posted_date": "2026-08-10",               // REQUIRED: ISO date, or "not shown"
   "why_it_matches": "≤2 lines: duty↔experience overlap + main risk",
   "requirements": "incl. the exact years-bar line",
   "salary": "not listed", "deadline": "not listed",   // ISO / 'not listed' / 'rolling'
   "apply_link": "employer ATS preferred", "source_link": "…",
   "fit_score": 8.0, "attainability_score": 6.5,
   "ladder": "A",                             // A|B|C|D  (X never enters roles[])
   "ghost_status": "active",                  // active | stale_posting | very_stale | pipeline_ad
   "priority": "Apply now",                   // Apply now | Strong fit | Worth the stretch | Backup | Reach | Watch
   "next_action": "apply",                    // apply | confirm_open_first | ask_recruiter_location | needs_login_verify
   "verification": "what was fetched, when, the proving sentence; AUDITED if second-agent confirmed",
   "evidence_url": "https://…",
   "flags": ["seniority_gap"]
 }],
 "leads":  [{"type":"Paywalled|Manual check|Repost watchlist|Rolling employer|Blocked portal|Sibling role|Caution","item":"…","details":"…","action":"…","links":"…"}],
 "top_picks": [{"list":"…","rank":1,"role_org":"…","match_score":9,"deadline":"…","link":"…"}],
 "cv_keywords": [{"category":"…","keywords":"…"}],
 "boards": [{"cadence":"Weekly|Monthly|One-time registration","board":"…","link":"…"}],
 "coverage": [{"source":"iimjobs","attempted":"yes","reachable":"login-walled","fetches":1,"roles_found":0,"roles_verified":0,"blocked_why":"guest wall — user login needed","fix":"log in via Chrome"}],
 "notes": [{"topic":"…","notes":"…"}],
 "run_log": [{"date":"…","roles_found":74,"new_added":64,"expired":0,"audit_correction_rate":"12/19","sources_nothing_new":"…"}]
}
```

## Workbook (Arial 10, navy headers, filters + freeze panes on every sheet)

1. **All Roles** — No. · Source report · Scope · Role title · Organisation · Location/arrangement · Category · Board/channel · Posted · Why it matches · Requirements · Salary · Deadline · Apply link · Source link · Fit /10 · Attainability /10 · Ladder · Ghost status · Priority · Next action · Verification · Flags · Run date added. Apply-now rows light green; Expired rows grey.
2. **Leads & Watchlist** — Type · Item · Details · Action · Link(s). All rung-X rows land here, plus cautions, blocked portals, repost watchlist.
3. **Top Picks & Deadlines** — per-scope top 10 + "Worth the stretch" standouts; final merged DEADLINE WATCH row sorted by date.
4. **CV Keywords** — Category · Keywords/guidance, incl. the Reach→Fit conversion assets row.
5. **Boards & Channels** — Cadence · Board · Link/note (auto-promoted/demoted by yield).
6. **Coverage Report** — Source · Attempted · Reachable · Fetches · Found · Verified · Blocked-why · Fix. Honest accounting of what was NOT searched.
7. **Market Notes & Method** — incl. the band-survey result with numbers, verification levels used, full excluded/closed list.
8. **Run Log** — date · found · new · expired · audit correction rate · zero-yield sources.

## Prose brief (chat, after SendUserFile)

Four short paragraphs max: headline counts (with the tier split); 5–8 standouts with one-line reasons and links; deadline watch for 14 days; what needs the user (logins, manual checks, ambiguities to ask recruiters). Include the band-survey strategy sentence with its numbers. Never paste the table.
