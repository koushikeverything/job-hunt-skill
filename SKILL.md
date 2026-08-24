---
name: job-hunt
description: Verified job-opportunity discovery for a specific candidate, across any profession. Use whenever a user shares a CV/resume or profile and wants jobs, openings, or vacancies found — remote, in a named city, or both — or says "search job boards", "find roles matching this profile", "which titles suit my resume", "build search strings", "re-run the job search", "new roles since last time", or "daily job alert". Runs native intake forms, detects the profession archetype and loads its source pack, pre-flights every connector and board, expands the profile into role families plus a skills-inversion matrix, fans out channel-partitioned verifying agents INCLUDING a company-first ATS-polling pass, loops until dry, dedupes and scores every role on Fit × Attainability with an explicit authenticity ladder, and delivers a master workbook that is also the state file for "new only" reruns. Every role is fetched and verified on an employer-owned surface — never invented.
---

# Job Hunt — verified opportunity discovery, any profession

A good job search is a research operation, not a Google query. This skill's two goals are inseparable and are served by the same architectural choice — **get as close to the employer as possible**: coverage (maximum real opportunities across every viable channel) and quality (every row *active* — genuinely open now — and *authentic* — a real employer, a real vacancy, correctly attributed). Evidence from production runs: employer-ATS-direct discovery produced 4× the top-tier yield per fetch of any aggregator, while an adversarial audit found that 63% of mirror-sourced "verified" rows needed correction. Both numbers point the same way.

**Two absolute rules.** (1) Every listed role must be verified on an employer-owned surface, or carry an explicit lower rung on the authenticity ladder (see `references/scoring-rubric.md`) with its score capped. Never synthesize a role, salary, deadline, or link; unknown fields say "not listed". (2) Push for the largest *quality* list — more channels, more title variants, company-first polling, adjacent titles — but never pad with expired, ineligible, unpaid, commission-only, ghost, or scam postings. Volume comes from breadth of channel, never from loosening verification.

## Files in this skill

- `sources/_core.md` — profession-agnostic infrastructure: connectors, ATS URL patterns, mirror chains, channel classes, fetchability legend. Read at Step 4.
- `sources/<archetype>.md` — per-profession source packs (boards, login-walled boards, prolific hirers, staffing patterns, known noise). Load the one matching the CV; if none matches, Step 4 creates one.
- `references/scoring-rubric.md` — Fit /10 × Attainability /10, the authenticity ladder (A–X), the ghost-job/active-ness score, priority tiers. Read before Step 6.
- `references/output-schema.md` — the role record (with required posted_date, evidence fields, ladder rung) and the workbook. Read before Step 6.
- `references/agent-prompt-template.md` — channel-partitioned searcher briefings with gating verification and the three named sub-checks. Read before Step 5.
- `references/lessons-learned.md` — the camouflage METHOD (six questions, works for any profile) + per-archetype appendices + market patterns. Skim at Step 2 and Step 6.
- `scripts/poll_ats.py` — company-first pass: polls ATS boards for a list of orgs, one fetch each, filters by keyword and freshness.
- `scripts/band_survey.py` — tallies years-of-experience bars across sampled postings; outputs median/IQR for the strategy brief.
- `scripts/build_master_xlsx.py` — builds the workbook from a roles JSON.
- `scripts/merge_delta.py` — delta mode: dedupes new findings against a prior workbook, appends only new rows, marks expired.

## Step 0 — Load tools, start the run manifest

Load via ToolSearch in one call: `AskUserQuestion, TaskCreate, TaskUpdate, SearchMcpRegistry, SuggestConnectors, WebSearch, WebFetch, SendUserMessage` plus job connectors already enabled and Chrome tools. Create a task list mirroring Steps 1–7. Create `run_manifest.json` (run date, scope, connectors probed, sources planned, per-source yields) — every later step appends to it; it feeds the Coverage Report and delta mode. Runs take 15–25 minutes; the task list is how the user follows along.

## Step 1 — Intake through native forms

If no CV is attached, first ask (one AskUserQuestion): attach it / connect the folder it lives in / paste a LinkedIn profile URL (with Chrome, the profile is often richer than a one-page CV) / describe the background in chat. Then read the CV and extract: experience blocks with dates, years per domain, education, languages (note ones *lacked*), certifications, and — critical for eligibility checks later — **city AND state/province**, work-authorisation status, and hard timezone limits.

Present ONE AskUserQuestion (up to 4 questions), adapting to what the CV already answers:

1. **Scope** (multiSelect): remote-only from [country] · [city] + metro · both · relocation hubs.
2. **Constraints** (multiSelect): exclude internships · exclude commission-only · salary floor · night shifts · contract/fractional/interim acceptable (this toggle unlocks the non-employment opportunity classes in Step 2).
3. **Logins** — from the archetype pack's login-walled list, ask NOW, not at failure time: "These boards are high-value for your profile but need you logged in — please open and log into [pack list, e.g. iimjobs/Instahyre/Naukri, or Behance, or Doximity] in Chrome before I start." One question here converts the biggest dead pool of a run into the biggest live one.
4. **Warm network + inbox** (optional): past employers' competitor sets, communities, alumni networks — feeds the company-first target list; and permission to scan their mailbox (if a mail connector is live) for recruiter/job-alert threads from the last 30 days — the warmest, cheapest, most authentic channel that exists.

Mode question when relevant: fresh search · delta against a prior workbook · recurring run. If the session looks unattended, skip forms, state assumptions at the top of the deliverable, use widest reasonable scope.

## Step 2 — Expand the profile: archetype, titles, skills-inversion, band survey

**Detect the archetype** (product-tech, design-creative, data-ml, healthcare, education, sales-marketing, operations-scm, legal, compliance-finance, ngo-development, blue-collar/frontline…) and load its `sources/` pack.

**Titles, three tiers** — direct / adjacent / stretch (tag "Reach"). For adjacent, run the profile through the six camouflage questions in `references/lessons-learned.md` (which other department owns this work? what's it called at a 10× smaller company? at 10× bigger? which adjacent function shares 70% of the skills? what do staffing firms and fractional marketplaces call it? what's the government/regulated variant?). The best find of most runs comes from this reasoning, not the direct list. Cap ~8 families / ~40 titles.

**Skills-inversion** — a second expansion axis: extract the CV's named artefacts and metrics ("design system", "onboarding activation", "triage protocol", "GHG accounting") and search postings by requirement text, not just title. This catches roles the market has mislabeled.

**Band survey** — run `scripts/band_survey.py` (or do it inline: sample 20–25 live postings for the primary title in the primary market, extract every stated years-requirement, compute median/IQR). This calibrates which titles are on-level vs Reach *empirically*, drives Attainability scoring, and becomes the strategy paragraph in the final brief ("median Director posting asks 11 yrs, IQR 10–15; at your 6 you clear 8% of them — Senior/Lead/GPM titles have a median of 6"). Never assert the market's seniority bar from anecdote.

## Step 3 — Build the search-string matrix

Cross titles × location qualifiers × synonym variants (per-market spellings and local-language titles where the market posts in them) and number them. Location qualifiers: remote forms, the city, its metro satellites, relocation hubs. Add board-scoped forms (`site:job-boards.greenhouse.io`, `site:jobs.lever.co`, `site:jobs.ashbyhq.com`, `site:linkedin.com/jobs`, plus the pack's boards) — indexed slugs from blocked boards reveal title+company+city to verify on the employer ATS. **Attach freshness operators everywhere the board supports them** (Indeed `fromage=14`, LinkedIn `f_TPR=r2592000`, "posted this month") — fresh-first search is both a breadth tool (recent postings are underranked by relevance sorts) and the cheapest active-ness filter. Include the pack's *negative* strings so agents stop wasting fetches disqualifying known noise (expert-network ads, exam-prep spam, scrum-master keyword collisions).

## Step 4 — Sources: pre-flight everything, then assemble

Coverage is decided here. `SearchMcpRegistry` for job connectors, then **probe before you plan**:

- **Each connector: one real query in the target geography.** Record works / geo-blocked / empty in the manifest. (A connector that returns UNSUPPORTED_COUNTRY for the target market gets dropped from every briefing — do not let three agents discover this independently.)
- **Each primary board in the pack: one fetch of its search page.** Record fetchable / JS-gated / login-walled / robots-blocked. Login-walled boards trigger the Step 1 login ask if it hasn't happened; still-walled boards go straight to the Leads sheet as manual checks.
- **Chrome:** check `tabs_context_mcp`; if absent, offer to connect it and say plainly which pools shrink without it.

Then run ONE AskUserQuestion naming exactly what is missing (connect X / enable Y / log into Z / proceed without) and respect the answer.

**If no archetype pack matches the CV**, spawn a source-discovery micro-agent first: "find the 15 highest-signal job boards, 5 professional communities/newsletters with job channels, the dominant ATS platforms, and the major staffing firms for [profession] in [market]" via web search. Its output seeds a new `sources/<archetype>.md` — the skill grows its library instead of guessing.

**Build the company target list** for Step 5's ATS-polling agent (150–300 orgs): every prolific hirer in the pack · companies in the candidate's shipped domains that raised funding in the trailing 12 months (they hire before boards index the roles) · G2/category leaders in those domains · the candidate's warm set from intake · every employer that surfaces during pass 1 (append live — hirers cluster; one company in a production run had 7 simultaneous eligible reqs).

## Step 5 — Fan out channel-partitioned searchers

Partition by **channel, not role family** — family-slicing makes every agent hit the same shared sources (a production run lost ~12% of its fetch budget to duplicates this way). Each agent carries ALL role families for its channel, its briefing from `references/agent-prompt-template.md`, the pre-flight results, the exclusion list, and the gating verification rules. Typical fleet (spawn all in one message; drop channels the pre-flight killed):

- **A — Connectors**: every connector that passed pre-flight, all titles × locations.
- **B — Company-first ATS polling**: run `scripts/poll_ats.py` over the target list (one fetch per org returns *everything* open there — the best quality-per-fetch of any channel), then fetch full JDs for hits.
- **C — Remote aggregators + eligibility triage**: the pack's remote boards; categorise every role's eligibility from the employer ATS sentence, reject country-locked, flag state-restricted.
- **D — Portfolio/community boards**: VC/accelerator boards, professional communities, newsletters, government/institutional portals per the pack.
- **E — Chrome logged-in sweep**: LinkedIn (date-filtered URL params; also the candidate's "recommended for you"/"top applicant" surfaces; collect "reposted N times" and applicant-count metadata for the ghost score) and the pack's login boards. Read-only, always.
- **F — Adjacency free-roamer**: the camouflage titles + skills-inversion strings, explicitly allowed to wander. The creative slice.

Every agent returns the required per-role fields (posted_date, evidence_url_fetched, eligibility_quote, ladder rung) plus "sources checked with nothing new" and per-source `{fetches_spent, roles_found, roles_verified}` for the yield log.

**Loop until dry.** After merging a pass, if it added meaningfully many new verified roles, run a delta pass with the found set excluded — until two consecutive passes come up nearly dry or budget is hit. Production history: four passes yielded 24 → 29 → 29 → 21; one pass is never enough.

## Step 6 — Merge, verify, score, audit

Collect into one JSON per `references/output-schema.md`. Dedupe by normalized org + title + location (cross-posts are one role — keep the employer-ATS link, cite the mirror as source). Apply `references/scoring-rubric.md`: **Fit /10 and Attainability /10** (a single blended score buries the high-fit/stretch quadrant where strong-narrative candidates actually win), the **authenticity ladder** (Apply-now requires rung A or B), the **ghost-job score** (posted age, repost pattern, evergreen phrasing, applicant-count vs age, named hiring manager), and the **scam checklist**.

**Adversarial audit** — the skill's most valuable stage; never cut it. Spawn skeptical agents briefed only to REFUTE: audit (i) every prospective Apply-now/top-10 row, (ii) every ladder-C/D row above threshold, (iii) a 10% random sample. Auditors receive the candidate's state, languages, and authorisations as structured fields. Record `audit_correction_rate` in the manifest — it is the skill's quality KPI, and if gating verification upstream is working it should fall run over run.

**Thin-tier trigger:** if Apply-now < 5 after scoring, say so, diagnose why (seniority scissor? empty geography? verification failures?), and run ONE corrective pass aimed at the diagnosis (e.g., 100 more seed-stage ATS boards where years-bars are absent). Never deliver a thin funnel silently.

## Step 7 — Deliver

Write the roles JSON; run `scripts/build_master_xlsx.py` (fresh) or `scripts/merge_delta.py` (delta). The workbook's sheets: All Roles · Leads & Watchlist · Top Picks & Deadlines · CV Keywords · Boards & Channels · **Coverage Report** (every pack source × attempted/reachable/yield/blocked-why — the user sees what *couldn't* be searched, which is exactly what they can fix) · Market Notes & Method · Run Log. Every role row carries a **next action** (apply / confirm-open-first / ask-recruiter-about-location / needs-login-verify).

Prose brief, four paragraphs max: headline counts; 5–8 standouts with one-line reasons; deadline watch for 14 days; what needs the user. Include the band-survey strategy paragraph with its numbers, and the CV keyword-gap list (most-requested terms across fetched postings that the CV lacks). Do not paste the table into chat.

## Step 8 — Delta mode and recurring runs

Delta: load the prior workbook's All Roles as the exclusion set; **re-poll the org list first** (cheapest, highest-yield — prolific hirers change weekly), then boards; re-verify every previously delivered Apply-now/Strong-fit row and mark expirations (the list the user is actively working must never contain dead links); check the repost watchlist. Yield log is machine-usable: a source with zero yield across 3 runs auto-demotes to monthly cadence; a source that produced an Apply-now row promotes to weekly. For recurring runs, create a scheduled task whose prompt invokes this skill in delta mode; scheduled runs are unattended — use the widest confirmed scope, don't ask.

## Step 9 — Optional: the hidden market

Offer, don't impose: a **speculative-target dossier** (the 15–25 companies most likely to *create* a role for this candidate — repeat hirers at level, just-funded companies in shipped domains, competitors of past employers — each with a why-them line and a named hiring leader where public); recruiter/search-firm registration list per archetype, honestly framed; outreach email drafts (drafts only, never send); a CV rewrite implementing the keyword gaps; certifications that convert Reach → Fit per the pack.

## Quality bar (self-check before delivering)

Every row carries its authenticity-ladder rung, and Apply-now rows are all rung A/B. Every row has posted_date (or "not shown") and an eligibility quote checked against the candidate's actual city AND state. Nothing expired; ghost-scored rows are flagged, not hidden. Employer identity confirmed (no recruiter posting as employer without an `agency_posting` flag). Deduped. Scored on both axes by the rubric. The Coverage Report is honest about what wasn't searched and why. Per-source yields are logged so run N+1 is cheaper than run N. The user was asked — through native forms, at intake — to connect and log into what would widen coverage, and the answer was respected.
