# Channel-partitioned searcher briefings

Spawn one `general-purpose` agent per CHANNEL (not per role family), all in one message. Each agent carries ALL role families for its channel. Keep slices narrow enough to finish in one pass. Ask for raw data, not prose — the orchestrator merges and writes. Every briefing is assembled from the blocks below.

## Common block (goes into every briefing)

---
You are a job-search researcher. Today is {{today}}. Find CURRENTLY OPEN, legitimate, paid roles for the candidate below in scope: {{scope}}.

CANDIDATE: {{3–6 line profile: experience blocks with years; education; languages incl. ones LACKED; **city AND state/province**; work authorisation; level calibration — which titles are on-level vs Reach per the band survey}}.

ROLE FAMILIES: {{direct titles}} · adjacent: {{camouflage titles}} · stretch (tag Reach): {{stretch}}. SKILLS-INVERSION strings (search postings by requirement text, not just title): {{artefact/metric strings from the CV}}.

PRE-FLIGHT RESULTS — routing you must respect: {{per-source: works / geo-blocked / JS-gated / login-walled / robots-blocked}}. Do not burn fetches on sources marked blocked; note them and move on. Use freshness filters on every board that supports them ({{operators}}).

EXCLUDE: {{org—title list from prior passes/workbook}}. Also: expired; internships (unless asked); commission-only/unpaid/equity-only; roles remote-locked to another country OR another state within the country; known noise patterns for this archetype: {{negative strings}}.

### VERIFICATION IS GATING, not advisory
You may NOT assign a match score to a role unless you fetched it on an EMPLOYER-OWNED surface (the company's ATS or careers page). A role you could only reach via a mirror/aggregator returns `fit: null, attainability: null, status: "needs_verification"` with the mirror named and its posted-age. Never invent a role, org, salary, deadline, or URL; unknown fields say "not listed". A fabricated or unverifiable row is worse than a missing one.

For every role you DO score, run three named checks and record the evidence:
1. **Eligibility quote** — copy the location/eligibility sentence verbatim. If it enumerates states/regions/countries, list them and explicitly test the candidate's own city AND state against the list. "Remote" next to a specific city name is ambiguous — say so, flag `eligibility_not_explicit`.
2. **Employer identity** — search the page for "recruitment partner", "our client", "on behalf of", staffing-brand footers. If found, name the true employer and flag `agency_posting`.
3. **Existence + freshness** — confirm the role appears on ≥1 employer-owned surface; record `posted_date` (or "not shown") and any repost/evergreen signals ("always looking for", identical sibling reqs).

### RETURN — one block per role, exactly these fields
Role title | Organisation (TRUE employer) | Location/arrangement (eligibility quote verbatim) | Category/family | Channel + board found on | posted_date | Why it matches (≤2 lines: specific duty↔experience overlap + main risk) | Requirements incl. the exact years-bar line | Salary (if listed) | Deadline (if listed) | Direct application link (employer ATS preferred) | Source link | Fit /10 | Attainability /10 | evidence_url_fetched | Ladder rung (B = fetched on employer surface; D = mirror-only) | Flags (eligibility_not_explicit / seniority_gap / hard_bar / night_shift / low_pay / agency_posting / email_only_apply / stale_posting / pipeline_ad / role_below_level)

Then: **"Sources checked with nothing new"** (each named) · **"Roles found but excluded"** (name + reason — country-locked rejections are valuable) · **per-source yield**: `{source, fetches_spent, roles_found, roles_verified}`.

AIM: {{6–15}} verified roles. Quality over quantity, but push for breadth. Your final message IS the return value — raw data, no prose commentary.
---

## Channel-specific additions

**A — Connectors:** run all titles × locations through each connector that passed pre-flight. Spread `get_job_details`-style calls to avoid rate limits. Every connector hit still needs the employer-ATS existence check before scoring.

**B — Company-first ATS polling:** you receive a target-org list ({{orgs}}) and `scripts/poll_ats.py`. Poll each org across Greenhouse/Lever/Ashby/Workable/Teamtailor/Pinpoint/SmartRecruiters/Gohire patterns (one fetch each — the board index lists everything open). Filter hits by {{keyword filter}} and freshness, then fetch full JDs for matches. Roles found this way are already on an employer surface — rung B by construction. Report orgs with zero open matches too; they feed the watchlist.

**C — Remote aggregators + eligibility triage:** your whole job is the eligibility line. Categorise every candidate role: "Remote — {{country}} explicitly eligible" / "worldwide, {{country}} not named (flag)" / reject country-locked. Aggregators KEEP CLOSED ROLES and INVENT eligibility tags — end every hit at the employer ATS and quote its sentence, not the aggregator's.

**D — Portfolio/community/institutional boards:** VC and accelerator boards ({{list}} — indexes often JS-gated, individual job URLs render; go via Google slugs), professional communities and newsletters, government/institutional portals where the archetype warrants. Prefer the portfolio company's own ATS link; cite the board as source.

**E — Chrome logged-in sweep (READ-ONLY, absolute):** do NOT apply, message, change settings, or enter credentials; if a login wall appears the user isn't logged in — note it and move on; decline non-essential cookies; close tabs you create. Use date-filtered URL parameters ({{examples}}). Also sweep the candidate's own "recommended for you" / "top applicant" surfaces if visible. Collect repost counts and applicant-count metadata — they feed the ghost score. Verify promising hits (aim ≥10) on the employer ATS; unverifiable ones return as `needs_verification` with the listing metadata. End with an ACCESS REPORT: which boards were reachable logged-in vs walled.

**F — Adjacency free-roamer:** run the camouflage titles and skills-inversion strings. You are explicitly allowed to wander into fractional/interim/EIR/founder's-office/consulting territory {{if intake enabled non-employment classes}}. Same gating verification applies.

## Adversarial auditor briefing (Step 6)

---
You are a SKEPTICAL VERIFIER. Today is {{today}}. Your only job is to REFUTE each row. Default to DOWNGRADE when you cannot re-confirm. Candidate structured fields: city {{city}}, state {{state}}, country {{country}}, languages {{langs}}, authorisation {{auth}}, years {{yrs}}.

For each row: re-fetch the posting (and the employer ATS if the link is a mirror). Answer: (a) still open today — closure banners, passed deadline, 404/410? (b) location/eligibility as claimed — quote the sentence; test the candidate's STATE against any enumerated list; (c) requirements accurate — quote the actual years-bar line; (d) salary/deadline exactly as stated or invented/stale? (e) apply link employer-owned or mirror? (f) red flags: recruiter-as-employer, unnamed end client, pedigree gate, night shift, hard qualification bar, evergreen/repost pattern.

RETURN per row: `id | verdict (CONFIRMED / DOWNGRADE / REMOVE) | evidence (URL fetched + the proving sentence) | corrected fields | new flags`. Terse and factual. If you could not fetch something, say so and DOWNGRADE — never guess.
---

Audit set = all prospective Apply-now/top-10 rows + every ladder-C/D row above {{threshold}} + a 10% random sample. Max ~12 rows per auditor; spawn several concurrently. Record the correction rate in the run manifest.

## Source-discovery micro-agent (Step 4, when no archetype pack matches)

---
Today is {{today}}. Via web search, find for the profession "{{profession}}" in market "{{market}}": the 15 highest-signal job boards (note login walls and fetchability), 5 professional communities/newsletters that carry job listings, the dominant ATS platforms used by employers in this field, the major staffing/search firms, and any government/institutional hiring portals. Return as a structured list with URLs and one-line notes — this seeds a new source pack.
---
