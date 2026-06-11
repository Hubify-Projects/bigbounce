# Site QA Sweep — bigbounce.hubify.app — 2026-06-10

**Method:** Full visual sweep via gstack browse (headed Chromium), desktop 1280×800 + mobile 375×812, light + dark, every nav page + representative drilldowns, screenshots read frame-by-frame, all PDF/GitHub/HF links curl-verified, every quantitative claim cross-checked against repo truth (SSOT R29 state: P1A v1A.0.58 · P1B v1B.0.56 · P2 v1.7.50 · P3 v3.1.89 · P4 v1.0.173 · P5 v0.1.62; readiness 94/94/94/94/95/95).

**Totals: 4 P0 · 13 P1 · 13 P2.** Screenshots: `/tmp/qa_*.png` (session-local).

**Cross-cutting root causes:**
1. Three legacy static HTML files (`galaxy-explorer.html`, `anomaly-explorer.html`, `data-explorer.html` at repo root) are embedded raw by the Next explorer pages and were never re-synced — they carry pre-rename titles, "100% Ready" claims, broken relative links, and Wave-11-era stats.
2. `site/src/data/papers.ts` + `live-status.ts` narrative fields (titles, page counts, "What's left", "Needs Houston", "Path to publication") lag the R29/EXT1 restamp even though versions/PDF mirrors are current — the bump sync updates versions but not prose.
3. Convex `readiness` was never rolled back 95→94 for P1A/P1B/P2/P3 after EXT1/R29 truth-audits.
4. Activity-feed timestamps appear to double-convert PDT→UTC (events render up to ~2 days in the future).

---

## P0 — broken / wrong data

### P0-1 · Activity feed shows future timestamps
- **URL:** /activity
- **Wrong:** "POD START **2026-06-12 18:46 UTC** · just now"; version bumps "**2026-06-11 02:15 UTC** · 3 hr ago". Real time at capture: 2026-06-10 ~22:40 UTC. Relative times are right; absolute UTC stamps are ahead by ~7h to ~44h → timezone double-conversion (PDT-naive datetime labeled UTC) or bad event-write clock.
- **Evidence:** `/tmp/qa_activity.png`
- **Fix:** store true epoch in Convex events; render in PT like the home header ("June 10, 2026 · 6:55 PM PT"). Audit the pod-event writer separately (44h skew ≠ 7h skew).
- **Effort:** S–M

### P0-2 · Anomaly Explorer claims "Paper 3 Status — 100% Ready"
- **URL:** /anomaly-explorer (embeds legacy `anomaly-explorer.html`, 3× "100% Ready" hits)
- **Wrong:** violates `/readiness-cap-99` + `feedback_99_pct_readiness_cap`; SSOT says P3 = 94%. Same block carries stale stats: "319,443 anomalies", "Paper 3 draft … 28 MB PDF, 33 pp" (current: 378,280 canonical; 26 pp / 4.6 MB).
- **Evidence:** `/tmp/qa_anomaly-explorer.png`; `anomaly-explorer.html:73` etc.
- **Fix:** strip the hardcoded status line from the legacy HTML or replace with the live Convex readiness component; refresh stats to Path-C canonical.
- **Effort:** M

### P0-3 · Galaxy Explorer: broken PDF/tex links + retired P4 title + "100% Ready"
- **URL:** /galaxy-explorer (embeds legacy `galaxy-explorer.html`)
- **Wrong:** "Read Paper 4 (PDF)" → `/public/papers/chirality_catalog_paper.pdf` returns **HTML soft-404** (correct path is `/papers/chirality_catalog_paper.pdf`, verified 200 application/pdf). 3 occurrences (lines 259, 578, 725). "LaTeX source" → relative `pipelines/p2_chirality/...tex` also resolves to HTML. Line 725 still titles P4 *"No Evidence for Large-Scale Parity Violation…"* (several renames ago) + "**100% Ready** (25.7 MB PDF)".
- **Evidence:** `/tmp/qa_galaxy-explorer.png`; curl content-type checks.
- **Fix:** absolute `/papers/...` hrefs + GitHub blob URL for the .tex; sync title/status from papers.ts.
- **Effort:** M

### P0-4 · Paper-4 page contradicts itself on the withdrawn −0.12σ null
- **URL:** /papers/paper-4
- **Wrong:** abstract correctly says the −0.122σ subsample-mask null was **withdrawn in v1.0.166**, but on the same page: Focus areas bullet 1 = "Subsample-mask −0.12σ MASTER-deconvolved **load-bearing null**"; Notable contributions = "**Headline null** ℓ=1 … −0.12σ"; Focus areas also keep "formally excluded at **~18σ**" (paper softened to ">99% confidence" in v1.0.151); Key result 14 = "**Definitively refutes** Shamir 2020" (Shamir shorthand was removed from the paper in v1.0.151).
- **Evidence:** `/tmp/qa_p4_2800.png`, `/tmp/qa_text/papers_paper-4.txt`
- **Fix:** rewrite the P4 `focusAreas` / `notableContributions` / key-results entries in papers.ts to the v1.0.173 claim set (real-space +0.41σ headline, template-fit z≈−18 under adopted model, withdrawn-null disclosure).
- **Effort:** S

---

## P1 — inconsistent / stale

### P1-1 · 4 of 6 paper titles on site are stale (papers.ts)
- **URLs:** home, /paper, /papers/paper-{1a,1b,2,5}, /figures sidebar, OG metadata
- P1A site: "Structural Closure of ECH Dark Energy…" → **actual (.tex):** "Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter" (retitle dropped "Structural Closure"/"No-Go" back at v1A.0.40).
- P2 site: "f_NL = −35/8 Forecast: SPHEREx Discrimination…" → **actual:** "Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook" (v1.7.50 title recast).
- P5 site: "…Across DESI Large-Scale Structure: A Cross-Matched Test of Local Coherence and Cosmic-Web Alignment" → **actual:** "…A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T-Web (Hahn 2007) Tidal-Tensor Cross-Check Across 791,635 DR1 Matched Spirals".
- P1B paraphrase drift ("Spectator-ALP Consistency Check for the ECH Spin-Torsion Program" vs actual "…a Birefringence Consistency Check with a Spectator-ALP Model"); P3 drops "Path-C" + "Map Patches", says "Rates" vs "Fractions". P4 matches.
- **Fix:** sync `title` fields from the .tex `\title{}`; add a title check to `/bigbounce-post-bump-sync`. **Effort:** S

### P1-2 · Convex readiness not rolled back: 95% everywhere vs SSOT 94
- **URLs:** home "Paper state — live from Convex" table, /status portfolio table, every paper detail badge
- All six show 95% / "0 open BLOCKERs"; SSOT R29 = 94/94/94/94/95/95. Same home page header chip says "**94% avg**" while the Convex table below says 95×6 — visible same-page contradiction.
- **Fix:** Convex `paperVersions` readiness rollback via `/bigbounce-bump`; add readiness to the post-bump sync checklist. **Effort:** S

### P1-3 · Page counts stale + same-page contradictions
- papers.ts `pages`: 25/16/24/26/21/27 vs actual R29 PDFs: **27/18/25/26/22/30** (only P3 right). Paper detail headers show the stale chip ("25 PAGES", "21 PAGES") right next to the artifacts box showing the correct live count ("27 pp", "22 pp").
- **Evidence:** `/tmp/qa_p1a_top.png`, `/tmp/qa_m_p4.png`
- **Fix:** derive the chip from the same source as the artifacts box; drop the duplicate. **Effort:** S

### P1-4 · "What's left" / "Path to publication" / "Needs Houston" blocks are pre-EXT1/R29
- **URLs:** home (Needs Houston), /paper cards, all 6 paper details
- Examples: P1A "R27conf cross-vendor round on v1A.0.56"; P1B/P2 "R26conf/R25conf came back CLEAN, paper is **SIGN-OFF-READY**" (R29 then found+fixed the P1B E1 artifact bug and P2 dimensional regressions, both rolled to 94); P4 "next Houston round queued on v1.0.171" (EXT1 already ran, v1.0.173 current); home "Anthropic API credits exhausted (reviewer leg down)… needs credits for R27conf" while R29 ran 30 API legs on 2026-06-10. `live-status.ts:65-78`.
- **Fix:** refresh narrative fields to R29/EXT2 state; make `/bigbounce-post-bump-sync` fail if `live-status.ts` mentions an R-round older than the SSOT headline. **Effort:** S–M

### P1-5 · Anomaly-count fragmentation: 378,280 vs 319K+ vs 319,443 vs 378,480
- Home shows **both**: ledger "Catalog anomalies retained **378K**" (page.tsx:176, hardcoded) and stat card "**319K+** ANOMALIES" (computed sum of surveys.ts = 319,226). /surveys hub: "RETAINED ANOMALIES 319,226". Legacy anomaly-explorer: 319,443. `data-explorer.html:182`: "**378,480**" (typo for 378,280). /status: "378K+".
- **Fix:** one canonical constant (378,280 Path-C unique) + explicitly label the survey-table sum as "pre-dedup per-survey rows" or reconcile rows to canonical; fix the 378,480 typo. **Effort:** S–M

### P1-6 · /status survey QC table contradicts home + /surveys
- /status (hardcoded `status/page.tsx:396-462`): NEOWISE "**FAIL: ecliptic systematic**, 436", Planck "**FAIL: galactic contamination**". surveys.ts (drives home + /surveys): NEOWISE "**QC PASS**, 419 (96.1% retained after ecliptic mask)", Planck "**PASS**". Reader gets opposite QC verdicts depending on page.
- **Fix:** render the /status table from surveys.ts; delete the hardcoded copy. **Effort:** S

### P1-7 · /status banner reads as a future date
- "RENDERED AT BUILD · **2026-06-11** 05:40 UTC". Correct in UTC but reads day-ahead for the site's PT-anchored audience; every other surface displays PT.
- **Fix:** display PT (or "UTC (PT: …)"). **Effort:** S

### P1-8 · Raw LaTeX rendered un-typeset on paper pages
- /papers/paper-4 Notable contributions: literal `$p_{\rm CW}^{\rm eq} > 0.9$`, `$\ell=1$`, `$-0.12\sigma$`, `$>5\sigma$ … $\gtrsim 0.75\%$ … $\geq 10^7$` visible to readers.
- **Evidence:** `/tmp/qa_p4_1600.png`
- **Fix:** KaTeX-render notableContributions (the rest of the page already handles math) or convert these strings to unicode. Sweep all 6 papers' data fields for `$`. **Effort:** S

### P1-9 · Galaxy Explorer stats disagree with Paper 4 page
- /galaxy-explorer: 1,592,107 CW / 1,609,053 CCW / 5,273,371 NOT_SPIRAL / dipole 0.43σ / CW frac 0.4974. /papers/paper-4: **1,687,069 CW / 1,634,726 CCW / 5,152,736 NOT_SPIRAL / +0.41σ**. Different catalog snapshots presented as the same product.
- **Fix:** regenerate explorer stat strip from the canonical catalog artifacts (same source as papers.ts). **Effort:** M

### P1-10 · Data Explorer header: "Data supporting all four papers" + "Paper 1"
- `data-explorer.html:182` — pre-split, pre-P5 framing (4 papers, "Paper 1" singular) on a 6-paper portfolio; plus the 378,480 typo (P1-5).
- **Fix:** rewrite the one paragraph. **Effort:** S

### P1-11 · /figures still uses "no-go / Structural Closure (No-Go Theorem)" for P1A
- Sidebar "Paper 1A (no-go)" + section header "Paper 1A — ECH Structural Closure (No-Go Theorem)". Terminology retired at v1A.0.40 (2026-06-02), reinforced by the current channel-level title.
- **Evidence:** `/tmp/qa_figures.png`
- **Fix:** "Paper 1A (ECH routes)" / "Channel-Level Closure". **Effort:** S

### P1-12 · Per-paper "External reviews" feeds stop at 2026-06-01
- Paper detail pages list internal-stage3 rounds + "Houston external paste — PENDING (2026-05-15)" while /reviews correctly shows EXT1 + R29 (2026-06-10). Two review surfaces, one stale.
- **Fix:** drive the per-paper list from the same source as `reviewTimeline.ts` (filtered by paper), or link out to /reviews and drop the duplicate list. **Effort:** M

### P1-13 · P5 version-string format inconsistent
- "v0.1.62-2026-06-10" (date-suffixed) beside plain semver for the other five, on home/status/paper tables — also makes the version column wrap on mobile.
- **Fix:** display `v0.1.62` and keep the date in the updated column. **Effort:** S

---

## P2 — polish / consolidation

1. **Ledger chip truncation (home header):** "6 PAPERS · 94% AVG · AWAITING HOUSTON SIG…" clipped at 1280px, light+dark (`/tmp/qa_home_dark.png`). Shorten label or let it wrap. (S)
2. **Home "OPEN (B/M/M/C)" column** is all-zeros mono-noise duplicating the /status CLEAN badges — drop or collapse to a single dot. (S)
3. **Status-surface redundancy (consolidation candidate #1):** home alone shows readiness 5 ways (ledger chip, Convex table, stat cards, paper cards, Current Focus) and /status repeats all of it. Every P1 inconsistency above is a symptom. Recommend: home keeps ONE compact paper table + Current Focus; /status is the detailed surface; both render from papers.ts/Convex only — no hardcoded numbers in page components. (M)
4. **Activity-vs-reviews overlap (consolidation candidate #2):** version bumps + R-round events narrate in both /activity and /reviews. Keep /activity as raw event log, /reviews as curated narrative, cross-link instead of duplicating. (M)
5. **"Current Focus" home block is a multi-line text blob** — violates the standing "site data strings one-line only" directive (`feedback_site_no_text_blobs`); changelog detail belongs in SSOT/git. (S)
6. **MCMC sample-count variants:** 424K+ (home/status) vs 309,189 (timeline) vs 309,769 (speculations). Pick canonical + label ("424K total across 3 frozen datasets; 309,189 in the headline w0-wa chain"). (S)
7. **f_NL-improvement claims need labels:** "9.5% improvement" (DESI survey page) vs "61% f_NL improvement" (/status key discoveries + anomaly explorer) — if both are real (per-survey vs multi-tracer), say so where they appear. (S)
8. **Search hint "14 barriers"** — stale P1A framing (now 4-route channel-level closure). (S)
9. **Speculations references "Paper 1 §VII.H"** — pre-split naming; should be 1A/1B. (S)
10. **/status Quintom card internal jargon:** "fire #21 bookkeeping confabulation, corrected fire #25" — transparency is good, but translate for public readers. EXT1 manifest page similarly exposes `/tmp/ext1_*_presubmit.png` paths. (S)
11. **/docs skill list incomplete:** 8 of 17+ astrostack skills listed; missing bigbounce-site-sync, bigbounce-version-bump, bigbounce-claims-table-sync, etc. (S)
12. **P4 PDF is 32 MB** — fine for archive, heavy for web "Read PDF"; consider a web-optimized mirror. (M)
13. **Mobile tables clip** (home Convex table, /status portfolio table cut at "READINES…") — confirm horizontal-scroll affordance or stack columns at 375px. Otherwise mobile light/dark render cleanly. (S)

**Console:** no site-attributable JS errors across all pages; only Next.js preload warnings (unused-preload woff2/css). 401/GSI errors observed in the shared daemon console belong to other tabs (referee sessions), not bigbounce.
**Link checks:** all 6 versioned PDFs 200 `application/pdf`; GitHub LaTeX-source + findings-archive links 200; HF model/dataset links 200. The only broken links found are the legacy-explorer relative paths (P0-3).

---

## Documentation surfaces — scistack/hubstack/astrostack naming (repo-side)

`~/.claude/scistack/README.md` + `INDEX.md` are already namespace-organized ("one tree, two namespaces: hubstack/, astrostack/") — the structure is fine. The confusion is **naming across doc layers**: global CLAUDE.md and site copy talk about "SciStack / HubStack / AstroStack" as if three sibling stacks, while the repo defines hubstack/astrostack as namespaces *inside* scistack.

**Recommendation (decision already made — no physical migration):** unify all docs to ONE-stack-with-namespaces language:
- scistack = THE science skill stack (single install/sync root);
- `hubstack/` and `astrostack/` are namespaces, never standalone "stacks";
- update: global `~/.claude/CLAUDE.md` scistack section wording, `scistack/README.md` first paragraph (lead with "one stack, two namespaces"), site `/docs` "BigBounce Stack" page where it enumerates skills, and `~/.agent-shared/STACK-MAP.md`.
- Effort: S (docs-only).

---

## Suggested fix order
1. P0-1 activity timestamps + P1-2 Convex readiness rollback (trust in "live" data is the product).
2. P0-4 + P1-1 + P1-3 + P1-4 in one papers.ts/live-status.ts refresh commit (single sync wave).
3. P0-2/P0-3 legacy-explorer sync (or fold the 3 legacy HTML embeds into proper Next pages and delete the root HTML).
4. P1-5/P1-6 number reconciliation (one canonical constants module).
5. P2 consolidation passes.

*Generated by the 2026-06-10 site QA sweep; screenshots under `/tmp/qa_*.png` (session-local, not committed).*
