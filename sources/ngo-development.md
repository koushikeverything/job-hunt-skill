# Source pack — ngo-development / compliance-finance / grants / training (India-seeded)

Seeded from a four-pass production run (Aug 2026, mixed compliance/NGO/grants/training profile, India). Applies to: NGO programme/grants/CSR/safeguarding roles, KYC-AML and compliance, training/L&D. Generic infrastructure (connectors, ATS patterns, mirrors) now lives in `sources/_core.md` — sections 1–3 below are retained for their profession-specific notes.

Every source below has a **fallback chain**. Try routes in order; stop at the first that works. Anything that reaches only the last rung ("manual") goes to the *Leads & Watchlist* sheet as a manual-check item instead of burning fetches. Update this file when a route starts or stops working — that memory is what makes run N+1 cheaper than run N.

Route legend: **C** = MCP connector tool · **F** = plain WebFetch/Firecrawl fetch works · **A** = API/JSON/archive endpoint works · **G** = Google/Firecrawl `site:` index reveals slugs, then verify on employer ATS · **M** = aggregator mirror (Jooble, Talent.com, SimplyHired, Glassdoor.co.in, Indeed search page) · **B** = needs Chrome (Claude-in-Chrome, logged in) · **manual** = human must open it.

## 1. Connectors (check first — structured, no scraping)

| Connector | Tools | State to check | Use |
|---|---|---|---|
| Indeed | `search_jobs`, `get_job_details` | often not installed → ask user to connect | Primary for city + remote queries; replaces fragile Indeed page scraping |
| ZipRecruiter | `search_jobs` (authless) | may be installed but `enabledInChat:false` → ask user to enable | Extra board, strong for US/global-remote |
| Dice | `search_jobs` (authless) | not installed | Only for tech-adjacent (compliance-tech, fintech ops) |
| Firecrawl | `firecrawl_search` | usually available | Search fan-out alongside WebSearch; better at surfacing niche boards |
| Claude-in-Chrome | tabs/navigate/read_page | `tabs_context_mcp` errors if not connected → ask user | Unlocks LinkedIn Jobs, Naukri, iimjobs, JS portals |
| Vibe Prospecting | enrich-prospects | not installed | Optional: hiring-manager contacts for outreach phase |
| Gmail / Drive / Notion | drafts, files | user-specific | Optional: draft applications, persist master list |

## 2. Mainstream boards

| Source | Chain | Notes |
|---|---|---|
| Indeed (in.indeed.com etc.) | C → F (search pages + `viewjob?jk=`) → M | Search pages fetch fine; individual `viewjob` often fine; full JD sometimes login-gated |
| LinkedIn Jobs | B → G (`site:linkedin.com/jobs "<city>" "<title>"`) → M | Robots-blocked to fetch. Slugs reveal title+company; verify on employer ATS. Largest single pool — always ask for Chrome |
| Naukri | B → G → M | Robots-blocked. Set email alerts as candidate-side fallback |
| Glassdoor (.co.in) | F (search pages, some job-listing pages) | Good freshness signal ("posted 3 days ago") |
| foundit.in | F (search pages) | Good for Indian BFSI/KPO roles |
| apna.co | F | Skews sales/blue-collar; occasional NGO/CSR |
| SimplyHired / Jooble / Talent.com / Careerjet | M | Mirrors of LinkedIn/Naukri/Indeed inventory. Careerjet often CAPTCHA; Adzuna 403 |
| shine.com, timesjobs, iimjobs, hirist, cutshort, instahyre | G → manual | Mostly JS-gated; iimjobs/cutshort skew senior |
| Wellfound (AngelList) | F (`wellfound.com/role/l/<role>/<country>`) | Startups; tags roles by function |
| Himalayas.app | F (`himalayas.app/jobs/countries/<country>/<role>`; company pages) | Best remote-India aggregator; shows deadlines & "India only" flags — but re-verify on employer ATS, it keeps closed roles |
| RemoteRocketship, Jobgether, WeWorkRemotely, RemoteOK | F (RemoteRocketship yes; Jobgether robots-blocked) | Mostly US/EU-locked — verify country eligibility every time |

## 3. Employer ATS patterns (verify here; prefer these links)

Greenhouse `job-boards.greenhouse.io/<org>` (F) · Lever `jobs.lever.co/<org>` (F) · Ashby (F) · Workable `apply.workable.com/<org>` (F) · BambooHR `<org>.bamboohr.com/careers` (F; list API sometimes) · Rippling ATS (F) · Oracle HCM (F, e.g. KPMG, Mashreq) · Workday `*.myworkdayjobs.com` (G; CXS JSON is POST-only, GET fails) · Zoho Recruit `*.zohorecruit.com|.in` (JS; some orgs have a server-rendered archive on their own site — Quest Alliance did) · Darwinbox (JS) · careers-page.com (F — direct job pages work even when the index page 403s; find slugs via Google) · greythr (JS) · SAP SuccessFactors (F usually).

## 4. Domain boards — development / NGO / child protection

| Source | Chain | Notes |
|---|---|---|
| DevNetJobsIndia | F (`standard_jobs.aspx`, `highlighted_jobs.aspx`, `jobdescription.aspx?job_id=`) | Best Indian dev-sector board. Some listings "Value Members only" — recommend membership; list them as paywalled leads |
| NGOBOX | F (`job_listing.php`; detail pages) | Filters are POST-based (not crawlable) — fetch listing pages 1–3 |
| CSRBOX (careers + CSR jobs) | F/partial (career index 403 sometimes) → email | Ahmedabad HQ; hires rolling; site deadlines stale — email career@csrbox.org |
| Impactpool | F (`impactpool.org/search?q=`, `/jobs/<id>`, `/jobs/c/remote-ngo-jobs`) | Mirrors UN/INGO roles reliably; good for UNICEF consultancies |
| Idealist | F (individual job pages; search UI not crawlable) | Use Google `site:idealist.org` + "anywhere in the world" |
| ReliefWeb | manual (`reliefweb.int/jobs?advanced-search=(C119)` for India) | Cloudflare blocks fetch AND api.reliefweb.int |
| UNjobs / uncareer / untalent | G → M (untalent home-based page fetchable) | JS search UIs |
| UNICEF careers | F (filter page lists titles; detail pages JS) → Impactpool mirror | `jobs.unicef.org/en-us/filter/?location=india` |
| UNV, Devex, DevelopmentAid | manual / login | |
| Arthan (arthancareers.com) | F (careers-page.com ATS links) / index JS | Places NGO/CSR roles pre-advertisement — also register |
| workforsocial.co.in, socialsectorjobs.in | F | Aggregators; DCPU/government notices (image-only — flag) |
| Alliance CPHA vacancies | F | Child-protection consultancies; check deadlines carefully |
| Org career pages: CRY (JS), Bal Raksha Bharat/Save the Children India (greythr JS), Plan India (F this pass), Railway Children (F), Aangan (F), Magic Bus (`searchjob.php` dropdown; jobhai mirror F), Pratham (F), CSF (careers-page.com F), Room to Read (Workday G), Peepul (Zoho JS), Quest Alliance (`questalliance.net/career` archive F) | as noted | |

## 5. Domain boards — compliance / financial crime

| Source | Chain | Notes |
|---|---|---|
| fincrimecareers.com | F | India roles mostly Mumbai/Bengaluru onsite |
| ACAMS career center | F/partial (redirects) | Hyderabad/Bengaluru onsite; membership unlocks more |
| eFinancialCareers | F | Sparse for India remote |
| cryptocurrencyjobs.co, web3.career | F | Check geo restrictions on every role — mostly US/EU/UAE |
| Company boards worth polling: MoonPay (Lever), Coinbase, Circle (Workday), BitGo, OpenFX (Greenhouse), Ziina (Greenhouse EU), Wirex (BambooHR), Vcheck (Rippling), IBKR (Greenhouse), Sumsub, Tide, Mashreq (Oracle) | F | Most India seats are onsite Bengaluru/GIFT City — read the location line |
| GIFT City / IFSCA ecosystem (Gandhinagar) | Indeed search `l=gandhinagar` + IFSCA licensee list | Under-covered cluster of entry-mid compliance roles at broking/fintech licensees; new licensees must hire compliance |
| BGV firms (First Advantage, HireRight, Sterling, KPMG vetting, AuthBridge) | employer ATS | Background-verification analyst = strong transfer for casework/due-diligence profiles |

## 6. Domain boards — CSR / ESG / grants

CSRBOX & NGOBOX (above) · Sattva, Dasra, GiveIndia careers (often empty/broken) · climatebase.org, terra.do (ESG; mostly US/onsite) · Philanthropy News Digest (decommissioned → Idealist) · Chronicle of Philanthropy (US-remote, usually US-restricted) · Catalyst Now / remoteimpact.org (global-remote fundraising, location-benchmarked pay).

## 7. Domain boards — education / training / L&D

Himalayas L&D filter · Pratham, Central Square Foundation, Teach For All, Teach For India, Educate Girls, Piramal, Leadership For Equity, ShikshaLokam, Room to Read, Peepul, Quest Alliance, Medha, Magic Bus career pages · Indeed `school counselor <city>` and `teacher trainer curriculum <city>` · Mercor / VeriPark / LRN-type remote-India contractor roles surface on Himalayas.

## 8. Recurring "manual check" set (put straight into Leads sheet)

ReliefWeb India filter · CRY careers · Bal Raksha Bharat greythr · Devex · DevNetJobsIndia paywalled rows · Magic Bus location dropdown · Gujarat State Child Protection Society (or equivalent state child-protection body) vacancy page · Naukri list pages when Chrome absent · Peepul/Zoho portals · Room to Read Workday requisitions.

## 9. Per-run yield log (append)

Record, per run: date · source · roles found · roles verified · notes. Sources with zero yield across three runs move to "monthly" cadence; sources with new hits move to "weekly". Seed observation (Aug 2026, mixed compliance/NGO profile, India): highest yield = Indeed search pages, Himalayas, DevNetJobsIndia, employer ATS via Google slugs, Glassdoor.co.in freshness; lowest = international fincrime/crypto boards (geo-locked), remoteok, cutshort/instahyre (senior/tech only).
