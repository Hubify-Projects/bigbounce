# Site Audit — Lane A — 2026-07-22

Scope: index.html (/), publish.html, reviews.html, architecture.html, status.html,
timeline.html. Checked against built HTML in `site/out/` AND live spot-checks at
https://bigbounce.hubify.app (cache-busted navigations, 2026-07-23 session).
AUDIT ONLY — nothing changed.

Canonical truth used: P1A v1A.0.126 / P1B v2B.0.14 / P2 v1.7.127 / P3 v3.2.0-r12 /
P4 v1.0.270 / P5 v0.1.142-2026-07-22; readiness caps 62/56/80/56/80/74 (avg 68%,
no uplift); DOIs P1A …21481838, P1B …21481842, P2 …21461881, P3 …21461888,
P4 …21461899, namaster-proof software …21481753; ORCID 0009-0008-5616-5994
(…3617-8729 wrong-unless-annotated-superseded); D1/D2/D3/D5 done, D4 pending
(codes HYEJ7S/L8TIPN/LRZHC4/CLVMAQ); 2026-07-22 wave = 18 INT legs / 16 closures;
f_NL canonical −35/16; P4 catalog framing "890,069 Quality-Controlled".

## Summary counts

- P0: 3
- P1: 3
- P2: 2
- Clean checks (no finding): /publish (fully correct — versions, readiness,
  DOIs, D1–D5, endorsement codes, ORCID all match canonical exactly);
  /architecture (readiness caps stated correctly, technical content clean);
  ORCID-supersession annotation present and correct everywhere it appears
  (publish.html, reviews.html); forbidden f_NL=−35/8 and "949,584" strings
  appear only inside explicitly historical review-log entries on reviews.html,
  never as current framing; no broken internal hrefs found in any of the 6
  built pages (all resolve to existing routes); local `site/out/index.html`
  static build itself shows P1A readiness correctly as 62% (the live-site bug
  below is a production Convex-data issue, not a stale local build).

---

## P0

### 1. Live production site shows P1A readiness as 56% instead of the canonical 62% — and contradicts itself across its own pages

- **Route:** / (live) and /status (live)
- **Finding:** On the live site right now, the P1A paper card on the homepage
  ("Minimal ECH algebraic note") and the P1A row on the /status live table both
  render **"56% ready"**. Canonical truth is 62. The SAME live site's /publish
  page and /reviews page and /architecture page, checked in the same session,
  all correctly show P1A = 62%. This is a first-time-reader-visible
  contradiction: a reader who looks at the homepage then clicks through to
  /publish sees two different readiness numbers for the same paper on the same
  visit.
- **Exact evidence:** live get_page_text on https://bigbounce.hubify.app/,
  P1A card: `"Minimal ECH algebraic note / 56% ready / v1A.0.126"`. Live
  https://bigbounce.hubify.app/status table row: `"P1A ECH channel-level
  closure + perturbation transparency	v1A.0.126	56%"`. Contrast live
  https://bigbounce.hubify.app/publish: `"P1A ... v1A.0.126	62	WAVE 1"` and
  live /reviews: `"P1A 62%"` and live /architecture: `"canonical caps are P1A
  62, P1B 56, P2 80..."`. The local static build `site/out/index.html` (not
  the live deploy) shows the CORRECT value: `title="Readiness — live from
  Convex paper state">62<!-- -->% ready`, proving `papers.ts`/`live-status.ts`
  and the intended Convex value are 62 — the live production Convex
  `readinessCap` (or equivalent field) for P1A alone has drifted to 56 on the
  deployed site without the static export or the other three live pages
  regressing.
- **Proposed fix:** Not a source-file edit — this is a live Convex data
  integrity issue (per CLAUDE.md directive A, "Convex is the ONLY readiness
  source"). Re-run `papers:setReadinessCap` for slug `paper-1a` to 62 against
  the production Convex deployment, then verify the homepage/`/status`
  Convex-driven components (`site/src/app/page.tsx`, `site/src/app/status/page.tsx`)
  re-render 62 without a redeploy (per directive A, data writes need no
  `npx convex deploy`). Also worth auditing why `/publish`/`/reviews`/
  `/architecture` read a different, correct value — they may be reading a
  different Convex query/table than the homepage/status cards, which is why
  only two of five live surfaces show the stale number; reconciling those
  read paths would prevent recurrence.

### 2. Live homepage "Submission-ready ETA" widget leaks two raw Convex document IDs as paper labels, and is missing P1B while showing a non-canonical "P1U"

- **Route:** / (live)
- **Finding:** The ETA widget ("7/8 papers at the 2-clean-wave bar") renders 8
  chips. Two of them show raw, un-humanized Convex document IDs instead of
  paper names — `k97bdanw0axccbqe02emrxy8jh87tavx` and
  `k97bk3bj57gm567th3f3qc780d87v1sc` — a serious readability/design defect
  (raw database primary keys exposed to readers) and evidence the underlying
  `readinessMetrics:computeEta` table has stray/duplicate rows without a
  resolved `paperId`. The remaining 6 chips are P1A, **P1U**, P2, P3, P4, P5 —
  **P1B is entirely absent** from the widget, and "P1U" is not one of the six
  canonical papers (P1A/P1B/P2/P3/P4/P5); it appears elsewhere in review-log
  text as an internal finding-ID prefix, not a paper. A first-time reader sees
  8 mismatched entries for a program described everywhere else as having 6
  papers.
- **Exact evidence:** live get_page_text on https://bigbounce.hubify.app/,
  ETA section: `"k97bdanw0axccbqe02emrxy8jh87tavx ◆◆ / k97bk3bj57gm567th3f3qc780d87v1sc
  ◆◆ / P1A ◆◆ / P1U ◆◆ 3 open / P2 ◆◆ / P3 ◇◇ 2 open / P4 ◆◆ 4 open / P5 ◆◆"`.
  Component: `site/src/components/PublishEtaWidget.tsx` line 133,
  `<span style={{ color: "var(--text-tertiary)" }}>{p.paperId}</span>` — renders
  `p.paperId` verbatim with no name-lookup/fallback, sourced from Convex
  `readinessMetrics:computeEta` (per the file's own header comment).
- **Proposed fix:** In `site/src/components/PublishEtaWidget.tsx`, map
  `p.paperId` through a slug→shortTitle lookup (e.g. from `papers.ts`) before
  rendering, and fall back to hiding/flagging (not printing) any row whose
  `paperId` doesn't resolve to one of the 6 canonical slugs. Separately, fix
  the root cause server-side: the Convex `readinessMetrics:computeEta` query
  or its backing table has orphaned/duplicate rows (2 unresolved raw IDs) and
  a mis-slugged "P1U" row while dropping "P1B" — reconcile that table against
  the 6 canonical `paper-1a/1b/2/3/4/5` slugs.

### 3. Hardcoded stale-version disclaimer on /status directly contradicts the table above it on the same page

- **Route:** status.html / /status (live and built, identical text)
- **Finding:** Directly beneath the live readiness table (which correctly
  shows P1B v2B.0.14 and P4 v1.0.270), a footnote sentence reads: *"Readiness
  values are evidence caps: P1B v1B.0.108 and P4 v1.0.244 have closure changes
  that have not yet been re-reviewed."* Both version strings are stale by many
  releases (P1B v1B.0.108 vs. current v2B.0.14 — note it even uses the old
  "v1B" prefix instead of the current "v2B" naming scheme; P4 v1.0.244 vs.
  current v1.0.270) and are hardcoded with no historical framing, so a
  first-time reader reads them as current, unreviewed changes — directly
  contradicting the table nine lines above on the same screen.
- **Exact evidence:** `site/src/app/status/page.tsx:215` —
  `Readiness values are evidence caps: P1B v1B.0.108 and P4 v1.0.244 have closure
  changes that have not yet been re-reviewed.` Confirmed live at
  https://bigbounce.hubify.app/status in the same session, same wording.
- **Proposed fix:** Edit `site/src/app/status/page.tsx` lines 212–219. Either
  remove the sentence (the "evidence caps, not proof of closure" point is
  already made in the two sentences before it) or replace the stale version
  refs with the current `p.version` values pulled from the `papers` data
  already in scope on that page, so it can never drift again.

---

## P1

### 4. Homepage/status LiveStatus banner is stuck 2 days behind the content it introduces

- **Route:** index.html / / (live), status.html / /status (live)
- **Finding:** The top banner reads **"July 20, 2026 · 11:00 AM PT"**, but the
  paragraph immediately below it (and the /status page's own build timestamp)
  describes the **"2026-07-22 pre-arXiv confirmation wave"** as already
  landed — 18 INT legs truth-audited, 16 closures, in past tense. A banner
  that's supposed to say "last updated" is dated two days before the events
  its own summary reports as done.
- **Exact evidence:** `site/src/data/live-status.ts:150-151`:
  `lastUpdatedISO: "2026-07-20T18:00:00Z", lastUpdatedDisplay: "July 20, 2026 ·
  11:00 AM PT"`, while `summary` on line 155 opens `"2026-07-22 pre-arXiv
  confirmation wave: 18 exact-PDF INT legs ... truth-audited; 16
  genuinely-new-real ... closed same-day"`. Confirmed live: homepage banner
  text `"July 20, 2026 · 11:00 AM PT / 68% ready"`; contrast /status's own
  self-reported `"RENDERED AT BUILD · 07/23/2026, 00:55 PT"` sitting right
  next to a table whose every row says "July 22, 2026".
  Note: /publish's own banner is NOT stale — it correctly shows "updated July
  22, 2026" — so this is isolated to the `liveStatus` object, not a
  program-wide date problem.
- **Proposed fix:** In `site/src/data/live-status.ts`, bump
  `lastUpdatedISO`/`lastUpdatedDisplay` on the `liveStatus` export to the
  2026-07-22 confirmation-wave timestamp (matching what `/publish` already
  shows) in the same commit as any future version/readiness bump — the file's
  own header comment already says "bump on every commit that ships research
  progress."

### 5. /timeline understates the review-round count by ~8x, contradicting the homepage in the same visit

- **Route:** timeline.html / /timeline (live and built, identical text)
- **Finding:** The "NOW (2026)" entry on the cosmic timeline says **"20+
  adversarial review rounds run."** The homepage, in the same session, says
  **"166 adversarial review rounds ... and 130 closure waves."** /reviews says
  "186 waves." A reader who visits /timeline right after / sees the round
  count drop by roughly 8x with no explanation.
- **Exact evidence:** `site/src/app/timeline/page.tsx:69`: `"...~309K frozen
  MCMC samples, an 8.47M-galaxy chirality catalog. 20+ adversarial review
  rounds run; all six papers remain IN REVISION (caps 56–80)..."`. Contrast
  `site/src/app/page.tsx:260` (`{reviewRoundCount} adversarial review rounds`,
  which renders live as 166) and live /reviews: `"last 15 of 186 waves"`.
- **Proposed fix:** In `site/src/app/timeline/page.tsx`, replace the
  hardcoded `"20+"` with the same `reviewRoundCount` value the homepage
  already computes (import it or pass as a prop), so the two pages can't
  drift again. The "(caps 56–80)" phrasing in the same sentence is fine as a
  coarse min/max range (56 and 80 are both real canonical caps).

### 6. Stale historical version reference in /status "Key Discoveries" contradicts the readiness table on the same page

- **Route:** status.html / /status (live and built, identical text)
- **Finding:** The "Key Discoveries" panel on the same status page lists:
  *"Public-ID Recovery of a Historical DESI DR1 Anomaly List / Paper 3
  (v3.2.0-r10) · 181 TARGETIDs recovered."* The readiness table directly above
  on the identical page shows P3 at **v3.2.0-r12**. This is a lower-severity
  sibling of finding #3 — same page, same pattern (a hand-written aside
  referencing a version 2 releases behind the live table), but this one is
  framed as a "discovery" card rather than a disclaimer footnote, so a
  skimming reader is somewhat less likely to read it as "current state" —
  hence P1 rather than P0.
- **Exact evidence:** `site/src/app/status/page.tsx:459`: `Paper 3 (v3.2.0-r10)
  · 181 TARGETIDs recovered · archive-recovery product`.
- **Proposed fix:** In `site/src/app/status/page.tsx`, update the discovery
  card's version string to the live `p.version` for paper-3 (or drop the
  parenthetical version entirely, since the surrounding numeric claims —
  181 TARGETIDs, 170 core, 11 lower-confidence — are unchanged since r10 and
  don't need version-pinning in a "key discoveries" teaser).

---

## P2

### 7. Live homepage average readiness (68%) is arithmetically inconsistent with the live P1A=56% bug, and diverges from /status's own live average (67%)

- **Route:** / (live), status.html / /status (live)
- **Finding:** Homepage banner shows "68% ready" (the correct canonical
  average of 62/56/80/56/80/74). /status's own live portfolio strip shows
  "avg readiness 67%" — which is exactly what you get by averaging the
  page's own (buggy) displayed values (56/56/80/56/80/74 = 402/6 = 67). Once
  finding #1 (P1A live readiness) is fixed, this discrepancy self-resolves,
  but it's worth flagging as a second visible symptom of the same root cause,
  and as a caution that any manual "68%" hardcode elsewhere should stay
  computed, not typed, so it tracks the fix.
- **Exact evidence:** live / banner: `"68% ready"`. Live /status: `"avg
  readiness <!-- -->67<!-- -->%"`.
- **Proposed fix:** No separate fix needed beyond finding #1's Convex
  correction — flagging so whoever closes #1 verifies both numbers converge
  back to 68% together.

### 8. reviews.html is a very dense, jargon-heavy wall of text for a first-time reader

- **Route:** reviews.html / /reviews
- **Finding:** The verdict-trajectory and matrix sections pack dozens of
  abbreviations with no on-page legend visible above the fold (GPT/GRK/GEM
  column codes, R/M/m/A verdict letters, wave IDs like "M44-INT-OpenAI",
  "H17F", "RS24-VERIFIED", finding-ID prefixes like "DP2-01"/"DP1U-14"). A
  first-time serious reader (the audit brief's target) has no way to decode
  R/M/m/A or GPT/GRK/GEM without hovering or already knowing the program's
  internal shorthand. This is a readability/clarity issue, not a data-honesty
  one — the page is transparent to the point of being unreadable to a
  newcomer.
- **Exact evidence:** live https://bigbounce.hubify.app/reviews — the
  "CURRENT / latest per paper" matrix and the 186-wave trajectory list render
  bare letter codes (`R M m R M R M m M ...`) and column headers `GPT / GRK /
  GEM` with no inline key in the visible text; a legend may exist as a hover
  tooltip or in the Expand view, but the default collapsed view a first-time
  visitor lands on doesn't show one.
- **Proposed fix:** Add a small, one-line always-visible legend near the top
  of the matrix section in `site/src/app/reviews/ReviewsClient.tsx` (or
  `reviews.css` for styling), e.g. "R=Reject M=Major m=Minor A=Accept ·
  GPT/GRK/GEM = ChatGPT/Grok/Gemini legs" — consistent with Houston's
  no-nested-boxes rule, this can be a plain text caption line, not a bordered
  card.

---

## P0/P1 one-line list

- P0-1: Live P1A readiness shows 56% (home + /status) vs. correct 62% (/publish, /reviews, /architecture, and the local static build) — Convex data drift, live only.
- P0-2: Live homepage ETA widget shows 2 raw Convex document IDs as paper chips, is missing P1B, and shows a non-canonical "P1U" — `PublishEtaWidget.tsx` + Convex `readinessMetrics` table.
- P0-3: `/status` footnote cites stale "P1B v1B.0.108 and P4 v1.0.244" directly under a table showing v2B.0.14/v1.0.270 — `status/page.tsx:215`.
- P1-4: LiveStatus banner dated "July 20" while its own summary text narrates "2026-07-22" events as done — `live-status.ts:150-151`.
- P1-5: `/timeline` says "20+ adversarial review rounds" vs. homepage's live 166 / `/reviews`' 186 — `timeline/page.tsx:69`.
- P1-6: `/status` "Key Discoveries" cites P3 v3.2.0-r10 vs. the same page's table showing v3.2.0-r12 — `status/page.tsx:459`.

## DISPOSITION 2026-07-22 (orchestrator)
All P0/P1 items FIXED, deployed, live-verified (commit a02b7c1c + Convex cap fix): P1A cap 56→62 in Convex; ETA widget canonical-six (0 raw IDs, P1B renders); status footnote + Key Discoveries current; banner date 07-22; timeline 180+; publish pluralization + deadlineNote. P2 legend added to /reviews grid.
