# Core source infrastructure — profession-agnostic

Read this at Step 4, alongside the archetype pack that matches the CV. Update fetchability notes whenever a route starts or stops working — that memory is what makes run N+1 cheaper than run N.

Route legend: **C** = MCP connector · **F** = plain WebFetch/Firecrawl works · **A** = API/JSON/archive endpoint · **G** = Google/Firecrawl `site:` index reveals slugs, verify on employer ATS · **M** = aggregator mirror · **B** = needs Chrome (logged in) · **manual** = human must open it.

## 1. Connectors — probe each with ONE real query in the target geography before planning around it

| Connector | Tools | Known limits (update per run) |
|---|---|---|
| Indeed | `search_jobs`, `get_job_details` | Works for India/US/most markets. Workhorse for city queries. `get_job_details` rate-limits under heavy use — spread calls |
| ZipRecruiter | `search_jobs` | **US/Canada ONLY — returns UNSUPPORTED_COUNTRY elsewhere. Do not offer it for other markets** |
| Dice | `search_jobs` | Tech-adjacent US only |
| Firecrawl | `firecrawl_search` | Search fan-out; better than WebSearch at surfacing niche boards |
| Claude-in-Chrome | tabs/navigate/get_page_text | Unlocks LinkedIn + the pack's login-walled boards. Ask for logins at INTAKE, not at failure time |
| Gmail / mail connector | search | Opt-in inbox scan: `from:(linkedin OR indeed OR <pack boards>) newer_than:30d` — recruiter threads are the warmest, most authentic channel there is |
| Vibe Prospecting / enrichment | enrich | Optional, outreach phase only |

## 2. Employer ATS URL patterns — the highest-quality channel; one fetch per org returns EVERYTHING open there

Greenhouse `job-boards.greenhouse.io/<org>` (F) · Lever `jobs.lever.co/<org>` (F) · Ashby `jobs.ashbyhq.com/<org>` (F — individual job pages sometimes JS-gated; the board index usually renders) · Workable `apply.workable.com/<org>` (often JS — try the embed/JSON endpoint) · Teamtailor `<org>.teamtailor.com/jobs` (F) · BambooHR `<org>.bamboohr.com/careers` (F) · Rippling (F) · Pinpoint `<org>.pinpointhq.com` (F) · SmartRecruiters `jobs.smartrecruiters.com/<org>` (F) · Gohire `jobs.gohire.io/<org>` (F) · Recruitee `<org>.recruitee.com` (F) · Oracle HCM (F) · SAP SuccessFactors (F usually) · Workday `*.myworkdayjobs.com` (G — CXS JSON is POST-only) · Zoho Recruit (JS — look for a server-rendered archive on the org's own site) · Darwinbox / greythr / MyNextHire / Keka (JS — go via Google slugs) · careers-page.com (F for job pages even when the index 403s).

Use `scripts/poll_ats.py` to sweep a company list across these patterns. Feed it: the pack's prolific hirers + recently-funded companies in the candidate's domains + warm-network orgs + every employer surfaced during pass 1.

## 3. Channel classes every run must consider (pack fills in the specifics)

1. **Connectors** (above).
2. **Company-first ATS polling** (above) — evidence: 4 of a production run's Top 10 came from one Ashby sweep.
3. **General boards** — Indeed pages (F), Glassdoor `.co.<tld>` (F, good freshness signals), foundit/Monster (F), regional equivalents.
4. **LinkedIn Jobs** — B via date-filtered URL params (`f_TPR=r2592000`, `f_WT=2`), else G. High volume, LOW verification quality — every hit must end at the employer ATS. Also sweep the candidate's own "recommended/top applicant" surfaces and collect repost + applicant-count metadata for the ghost score.
5. **Remote aggregators** — RemoteRocketship (F, high yield), Himalayas (F, shows deadlines/eligibility tags but KEEPS CLOSED ROLES — always re-verify), WeWorkRemotely/RemoteOK (mostly US/EU-locked), Wellfound (F role pages), Jobgether (robots-blocked → G). Nine in ten "remote" postings are country-locked: read the eligibility line every time, and check STATE-level restrictions against the candidate's own state.
6. **Google Jobs surface** — `site:` slugs aggregate ATS postings incl. JS-gated ones, with posted dates.
7. **Portfolio/community boards** — VC/accelerator boards (Getro/Consider-hosted; index often JS-gated but individual job URLs render — go via Google slugs), professional communities, newsletters with job channels.
8. **Government/PSU/institutional portals** — per market; for healthcare, education, engineering this is half the market.
9. **Staffing/search firms** — legitimate channel in many professions; ALWAYS flagged `agency_posting`, end client named where possible. Watch for recruiters posting as the employer ("recruitment partner", "our client", "on behalf of").
10. **The user's own inbox** (opt-in, Step 1).
11. **Mirrors** (Jooble, Talent.com, SimplyHired, Adzuna [often 403], Careerjet [CAPTCHA]) — last resort; anything mirror-only is ladder rung D.

## 4. Pre-flight protocol (Step 4)

One call per source BEFORE spawning agents: connectors get one real geo-targeted query; boards get one search-page fetch. Record works / geo-blocked / JS-gated / login-walled / robots-blocked in the run manifest. Route every agent's fallback chains from these results. Login-walled boards → the intake login ask; still walled → Leads sheet as manual checks, zero fetches wasted.

## 5. Per-run yield log (append to manifest and Coverage Report)

Per source: date · fetches spent · roles found · roles verified · notes. Zero yield across 3 runs → monthly cadence. Produced an Apply-now row → weekly cadence.
