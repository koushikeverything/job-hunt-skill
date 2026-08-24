# Source pack — product-tech (product management, design, growth, tech leadership)

Seeded from a full production run (India, senior product leader, Aug 2026) with per-source yield data. Applies to: PMs at all levels, product/design leadership, growth/PLG, platform/API product, founders seeking operator roles, adjacent tech leadership. Adapt geography-specific rows for other markets.

## Login-walled boards — name these in the INTAKE login ask
India: **iimjobs** (best-matched senior board; contributed ZERO in a guest run), **Instahyre**, **Cutshort**, **Naukri** (guest browsing is noise-dominated — logged-in only), hirist.tech. US/EU: LinkedIn (usually logged in already), Otta/Welcome-to-the-Jungle (account improves results), Wellfound (account unlocks apply data).

## High-yield boards (production-verified)
| Source | Chain | Yield notes |
|---|---|---|
| Employer ATS sweeps (Ashby/Greenhouse/Lever `site:` + poll_ats.py) | F/G | ⭐ Best quality-per-fetch anywhere: 4 of Top 10 from ~10 rows. One Ashby sweep surfaced Sarvam, SpotDraft, AiPrise, Reo.Dev, Josys |
| Indeed connector | C | Workhorse for city queries; produced the #1 find. Many rows need ATS re-verification |
| RemoteRocketship | F | Highest-yield remote board — decisively beat Himalayas |
| Y Combinator workatastartup / ycombinator.com/jobs | F | Publishes salary+equity bands; strong for Founding-PM titles; India/city filters render |
| Accel portfolio (jobs.accel.com) | F job pages, JS index | Individual job/company URLs render fine — go via Google slugs |
| Blume Ventures (jobs.blume.vc) | F | Fully fetchable, 177 jobs at last run |
| Wellfound | F role pages | Startup roles; search UI limited |
| Himalayas | F | Eligibility tags useful but keeps closed roles — ALWAYS re-verify on ATS |
| Glassdoor .co.in | F | Freshness signal ("posted 3d ago") |
| ai-jobs.net | F | AI-product roles |

## Low/zero-yield (do not burn fetches — production-verified)
Peak XV careers.peakxv.com, Lightspeed jobs.lsvp.com, Nexus jobs.nexusvp.com, Bessemer jobs.bvp.com — JS-gated shells; go via Google slugs to the portfolio company's own ATS. Matrix/Z47, Prime VP, Together Fund, Stellaris, 3one4, Antler India, Info Edge Ventures — no portfolio job board exists. WeWorkRemotely, RemoteOK — nothing India-eligible at senior level. `site:greenhouse/lever "Head of Product" India` — returns overwhelmingly US/EU companies (poll specific orgs instead). ZipRecruiter connector outside US/CA.

## Prolific-hirer starter list (poll these orgs' ATS boards every run)
**India-remote heavy:** HighLevel (Lever — 4–7 simultaneous India-remote product reqs observed), Oportun (Greenhouse), Coupa (Lever), Outreach (Lever), JoVE (Workable), group.one/saas.group (Teamtailor), Writesonic, G-P/Globalization Partners (Greenhouse).
**Indian SaaS/AI:** Sarvam AI, SpotDraft, AiPrise, Enterpret, Glean, Headout, Hiver, Mindtickle, Zenoti, Freshworks, Zoho, Postman, BrowserStack, Chargebee, Whatfix, Darwinbox, MoEngage, CleverTap, LeadSquared, Rocketlane, Atlan, Hasura, Sprinklr, Uniphore, Yellow.ai, Gupshup, Observe.AI (JS careers — Google slugs), Krutrim.
**Repost watchlist (closed roles at candidate-level observed):** BrowserStack, Freshworks (Freddy AI), Whatfix, Zluri, LeadSquared, Uniqode, WizCommerce, Interview Kickstart.
**Company-list generators:** "Series A/B raised last 12 months" search per domain · G2 category leaders in the candidate's shipped domains · acquirers/competitors of past employers.

## Known noise (negative strings)
Ethos "Expert Opportunity" $80/hr expert-network ads (~10 identical LinkedIn postings per title). "Product Owner (Scrum)" keyword collisions for product-leadership searches. Staffing marketplaces posting as employers: ClanX pattern — page says "recruitment partner, helping <X> hire" → employer is X, flag agency_posting. Career-coaching firms posting "USA Startup" roles (MissFit pattern). Pedigree-gated titles ("IIT/NIT/BITS only" in the title) — record and skip if candidate doesn't qualify.

## Market patterns (product-tech, India, 2026 — re-verify per run)
- **Seniority scissor:** Director/VP titles at scaled companies bar at 10–15+ yrs (Uber 15+, Twilio 15+, SAP 10+, Okta 10+, Hiver 10+). A ~6-yr leader's real market is Senior PM / GPM / Lead / Principal / Founding PM titles, or small companies with no year gate ("no hard year bar"). Run band_survey.py to confirm the current numbers.
- **State-restricted remote is real:** Twilio's remote-India enumerates five eligible states. Check the candidate's state, not just country.
- **Aggregators invent eligibility:** RemoteRocketship tagged a role India-Remote whose Lever page says only "Remote Role". End at the ATS.
- **"Director" can be an internal grade label** (Paytm: Director title, 3–6 yr band). Verify scope, not title.
- **Tier-2 Indian cities are near-empty at product-leadership level**; GIFT City/Gandhinagar is compliance/fintech-ops, not product.

## Certifications/assets that convert Reach → Fit
Public AI-product case study or portfolio (several AI roles require one) · working fluency with AI coding tools (Claude Code/Cursor) with a shipped prototype · basic SQL (named by 4+ postings per run) · reframed years line ("N years in product, M leading product teams") so ATS parsers count UX/founder years as product years.
