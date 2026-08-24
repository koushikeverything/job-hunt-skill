# Scoring rubric — Fit × Attainability, authenticity ladder, ghost score, priority tiers

Score honestly. The list is only useful if the top tier means "apply today". Users calibrate on the first rows they open; one inflated score costs trust in the whole workbook. A single blended score buries the distinction between "bullseye domain, years gap" and "weak domain, no gap" — that's why there are two axes.

## Fit /10 — how well the WORK matches (start 10, subtract; floor 1)

- Core duties map directly to the strongest experience block: −0
- Map to a secondary block or need translation ("your studio engagements ≈ our 0→1 bets"): −1
- Adjacent function, transferable skills only: −2 to −3
- Domain the candidate has never shipped in (their process transfers, the domain doesn't): −1 to −2
- Requires a hard technical/domain skill the CV lacks (clinical licence, SOC-2 depth, hands-on ML, GHG accounting): −3 to −5
- Role clearly below the candidate's scope (note "backup option"): −2

## Attainability /10 — how likely they GET it (start 10, subtract; floor 1)

**Seniority vs the band survey** (use the measured median, not vibes): required years within band or ≤1 above −0 · 2–3 above −1.5 · 4+ above or a level up −3 to −5 · explicit "currently operating at X level" gates the candidate meets −0, doesn't meet −4.
**Eligibility & location:** explicitly eligible (country AND state, city, or true remote) −0 · global remote, country not named −1 and flag · **state-enumerated remote excluding the candidate's state −5** (near-disqualifying — relocation is the only path) · metro satellite −0.5 · same-state different city −2 · hybrid when user asked remote-only: exclude unless remote-until-office (flag).
**Hard bars:** mandatory language lacked −3 · mandatory licence/degree/pedigree lacked (MBA required, IIT-only, engineering degree required) −4 · "preferred" versions −0.5.
**Terms:** below-market pay −0.5 (state it) · far below level −2 · night-shift hours −1.5 unless user allowed · contract/part-time −0 but note.
**Verification & freshness:** rung C −0.5 · rung D −1 · stale (see ghost score) −0.5 to −2.

## Authenticity ladder — recorded per row, gates the tiers

| Rung | Meaning |
|---|---|
| **A** | Fetched on employer-owned surface AND re-confirmed by the adversarial auditor |
| **B** | Fetched on employer-owned surface once |
| **C** | Existence confirmed on an employer surface; details from a mirror |
| **D** | Mirror/aggregator only ([VBA]) — Attainability capped at 7, never Apply-now |
| **X** | Existence unconfirmed on any employer surface — goes to Leads & Watchlist, NEVER All Roles |

## Ghost-job / active-ness score — is this vacancy real and current?

Start "active"; downgrade on signals: posted >45 days with no deadline → `stale_posting` · >90 days → `very_stale` (Attainability −2) · same title relisted repeatedly / rotating sibling req-IDs → `pipeline_ad` · evergreen phrasing ("always looking for talented…") → `pipeline_ad` · high applicant count relative to age with no repost (LinkedIn metadata) → neutral · named hiring manager on the posting → strong live signal, note it · recent employer signals (funding, launches) support liveness; layoff news undermines it. `pipeline_ad` rows are capped at Strong fit and carry next-action "confirm a live req exists before applying".

## Scam checklist — any hit excludes the row (record in Leads as a Caution)

Upfront fees or "training deposits" · WhatsApp/Telegram-only contact · generic free-mail apply address for a claimed large employer · salary far above market for a junior bar · no findable web footprint for the org · urgency language ("only 2 slots") · identity-document requests at application stage.

## Priority tiers

- **Apply now** — Fit ≥ 7.5 AND Attainability ≥ 7 AND rung A/B AND ghost-status active. Shaded green.
- **Strong fit** — Fit ≥ 6.5 with Attainability ≥ 5.5, or Apply-now-grade scores held back by a soft flag (rung C, mild stretch, eligibility not explicit).
- **Worth the stretch** — Fit ≥ 7 but Attainability 3–5.5 (bullseye work, real bar). This quadrant is where a strong-narrative candidate wins; give it its own visibility, don't bury it.
- **Backup** — Attainability ≥ 7 but Fit 4–6.5 (they'd get it; is it worth wanting?).
- **Reach** — both axes middling, or hard-bar rows where the org/domain justifies the attempt.
- **Watch/pipeline** — `pipeline_ad`, closed-but-recurring, senior roles at repeat hirers → usually the Leads sheet.

## Ranking & top picks

Sort All Roles by (Fit+Attainability)/2 desc, then deadline urgency (dated deadlines within 14 days float up), then ladder rung. Top Picks = top 10 per scope + the best of "Worth the stretch" labeled as such.

## Written justification

"Why it matches" ≤2 lines, naming the specific duty↔experience overlap and the main risk — reusable in a cover letter. No generic phrasing.
