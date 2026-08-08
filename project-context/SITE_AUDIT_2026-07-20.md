# BigBounce Live Site Audit — 2026-07-20

**Auditor:** product-design + usability full sweep of https://bigbounce.hubify.app
**Method:** in-app browser, every route at desktop 1280×800 + mobile 375×812, plus
source cross-check (`site/src/**`, root legacy HTML, `api/chat.mjs`) and curl checks
(HTTP status + PDF content-type on every route/artifact).
**Bar:** publication-grade scientific lab site; a grant reviewer must understand the
program and its true state within 10 seconds on every page, with zero stale or
contradictory surfaces.

## Headline verdict

- **No P0 / broken surfaces.** All 23 routes return HTTP 200. All 6 paper PDFs return
  `application/pdf` (200). Search works. The `/chat` backend responds (`POST /api/chat → 200`).
- **Clean pages (no P0/P1): 15 / 23.** Eight pages carry a P1 staleness/contradiction issue.
- **The core problem is a data-sync gap, not layout.** The canonical source (`papers.ts`)
  and the live Convex feed (`/activity`) are CURRENT and correct. But several
  **hardcoded snapshots and legacy-embedded HTML surfaces are stale and mutually
  contradictory**, producing three site-wide contradictions a reviewer will catch:
  1. **f_NL = −35/16** (correct, most pages) vs **f_NL = −35/8 = −4.375** (data-explorer, chat, some figure labels).
  2. **P3 reframed** to a 181-TARGETID archive-recovery product (paper page/PDF) vs the **old "378,280 anomalies / 7 surveys" discovery framing** (home, contributions, anomaly-explorer).
  3. **Readiness board current** (P2 = 80%, papers.ts) vs **stale 2026-07-15 board** (P2 = 74%, reviews + architecture).

This is exactly what `/bigbounce-claims-table-sync` + `/site-cohesion-sweep` exist to prevent.

---

## Per-page table

Severity: **P0** = broken · **P1** = stale / confusing / contradictory · **P2** = polish

| Route | Desktop | Mobile | Issues (severity) |
|---|---|---|---|
| `/` | Clean | Clean | P1: P3 sold as "378,280 unique anomalies across 7 surveys" (N3 contribution) — contradicts reframed P3 paper. P2: source-count varies (45M+ / 37.3M / "tens of millions"). P2: terminal button overlaps body text on mobile. |
| `/papers/paper-1a` | Good (P2) | Degraded (P2) | P2: Paper-Artifacts card overflows — full 64-char sha256 does not wrap; clips right on desktop, forces horizontal scroll inside card on mobile. Version v1A.0.124/62 correct. PDF OK. |
| `/papers/paper-1b` | Clean | Clean | v2B.0.11/56 correct. Artifacts wrap fine (md5 only). PDF OK. |
| `/papers/paper-2` | Clean | Clean | v1.7.125/80 correct. PDF OK. |
| `/papers/paper-3` | Good (P2) | Good (P2) | P1 (cross-page): paper reframes to 181-TARGETID recovery ("not a novelty or detection claim") while home/contributions/anomaly-explorer still sell the old 378,280-anomaly catalog. P2: same sha256 artifacts overflow as 1a. v3.2.0-r10/56 correct. PDF OK. |
| `/papers/paper-4` | Clean | Clean | v1.0.268/80 correct. PDF OK (34 MB — large but valid). |
| `/papers/paper-5` | Clean (P2) | Clean | P2: refs count renders empty ("— REFS"). P2: hash format inconsistent (P5 shows truncated 8-char sha256; 1a/3 show full 64-char; 1b/2/4 md5-only). v0.1.141/74 correct. PDF OK. |
| `/reviews` | Clean layout | Clean layout | **P1: stale board.** "Current status (2026-07-15) … P2 74 … P1B v1B.0.108 … P4 v1.0.244", ProgressViz chip **P2 74%** (truth = 80%), avg 67% (home says 68%). Direct contradiction with home/paper pages. |
| `/activity` | Clean | — | LIVE + current (top event today, "PAPER-4 bumped to v1.0.268 · 10 hr ago"). P2: long event summaries clip at right edge without ellipsis. |
| `/data-explorer` | Clean table | Usable | **P1: stale flagship number.** Header + table state "f_NL = -35/8 = -4.375" (15× in embedded `data-explorer.html`) vs canonical −35/16 = −2.1875. Table/search/export/pagination all work; wide table scrolls horizontally on mobile (correct). |
| `/galaxy-explorer` | Clean | — | Numbers consistent with P4 (8,474,531 galaxies, +0.41σ). |
| `/anomaly-explorer` | Clean layout | — | **P1: superseded P3 framing.** "Paper 3 Status — in final review", "Enhanced catalog COMPLETE — 22,504,897 spectra", "378,280 unique anomalies from 37.3M sources across 7 surveys", "12 z>6 QSO discoveries", "26 pp, 4.6 MB PDF". Contradicts current P3 (181 IDs, 17 pp, 474 KB, not a detection claim). |
| `/figures` | Clean | — | Figures lazy-load (blank placeholder until scrolled into view — acceptable, not broken); Fig 1 correctly shows f_NL = −35/16. P2 risk: some P2/forecast figure source labels in `figures.ts` still say −35/8 (verify baked images per directive I6). |
| `/explained` | Clean | — | Excellent plain-English orientation, strong hierarchy. f_NL = −35/16 correct. |
| `/glossary` | Clean | — | 17 entries, f_NL = −35/16 correct. P2: one bordered card per term (mild nested-box; dividers would match the docs aesthetic). |
| `/docs` | Clean | — | Professional Mintlify-style sidebar + search + badges. |
| `/architecture` | Clean layout | — | **P1: stale board** (same 2026-07-15 snapshot: P2 74, P1B v1B.0.108, P4 v1.0.244, avg 67%). P2: says "bigbounce-mcp exposes 11 tools" while /docs says 13. |
| `/predictions` | Clean | — | Flagship f_NL = −35/16 = −2.1875 correct; clean channel cards. |
| `/articles` | Clean | — | Engaging cards, f_NL = −35/16 correct. |
| `/contributions` | Clean layout | — | **P1: P3 old framing** ("378,280 unique anomalies across 7 surveys") repeats the home/anomaly-explorer conflict. Layout clean (row dividers). f_NL correct. |
| `/search` | Clean | — | Functional; "chirality" returns well-formatted, relevant, correctly-categorized results. |
| `/chat` | Backend works | — | **P1 ×3.** (a) astro states **f_NL = -35/8 = -4.375** (stale) — root cause `api/chat.mjs:42` system prompt. (b) System prompt grounds on legacy `.html` paths + stale counts (22 figures vs 75, 28-glossary vs 17, 7 articles). (c) Frontend does NOT render markdown/LaTeX — response shows raw `\[f_{\rm NL}=-\frac{35}{8}\]` and literal `###` headers. |
| `/old` | Renders (heavy) | — | Deprecated legacy static site (redirect chain into `/old/*.html`); heavy enough to stall the renderer; off main nav; stale by design. P2: noindex or gate it. |

---

## P0 list (broken)

**None.** No broken routes, images, PDFs, search, or chat backend. This is a strong
baseline: nothing is non-functional. Every issue below is staleness/contradiction or polish.

---

## P1 list (stale / confusing / contradictory — must fix before publish)

1. **f_NL = −35/8 (superseded) still shipping in the chat assistant.**
   `api/chat.mjs:42` — system prompt reads `**Matter bounce f_NL = -35/8 = -4.375**`.
   The astro assistant tells every visitor the wrong flagship number.
   Fix → `-35/16 = -2.1875` (and align "300x / 4-6 sigma" to the papers' "~300× / 3–5σ").

2. **f_NL = −35/8 (superseded) on the Data Explorer.**
   Embedded from root `data-explorer.html` (15× `−35/8 = −4.375`, only 2× `−35/16`).
   `/data-explorer` reads this file at build (`site/src/app/data-explorer/page.tsx`
   → `REPO_ROOT/data-explorer.html`). Fix → replace all `35/8`/`-4.375` with
   `35/16`/`-2.1875` in `data-explorer.html`.

3. **P3 messaging contradiction (site-wide).** The P3 paper page + PDF reframe P3 to a
   181-TARGETID public-ID **archive-recovery** product, "NOT a purity, novelty, or
   detection claim." But three surfaces still sell the old discovery framing:
   - `site/src/app/page.tsx` (home "how the six papers fit together" + N3 "Multi-Survey Anomaly Catalog: 378,280 unique anomalies")
   - `site/src/app/contributions/page.tsx` (same 378,280 framing)
   - root `anomaly-explorer.html` (embedded at `/anomaly-explorer`): "in final review", "Enhanced catalog COMPLETE — 22,504,897 spectra", "378,280 anomalies / 37.3M sources / 7 surveys", "12 z>6 QSO discoveries", "26 pp, 4.6 MB PDF".
   A reviewer moving from home → P3 paper sees two different papers. Fix → reconcile all
   three to the r10 reframe (or clearly separate "the 22.5M-spectra pipeline that
   produced the seed list" from "P3 = the public-ID recovery of 181 of them").

4. **Stale 2026-07-15 readiness board on /reviews (P2 shown as 74%, truth 80%).**
   - `site/src/app/reviews/page.tsx` L67-69, L122-123, L252, L259-260
   - `site/src/app/reviews/ProgressViz.tsx` L935-965 (chips + tooltips)
   Board hardcodes P1A v1A.0.123/62, P1B v1B.0.108, P2 v1.7.122/**74**, P3 r8, P4 v1.0.244, P5 v0.1.133, avg 67%.
   Truth: P1A .124/62, P1B v2B.0.11/56, P2 v1.7.125/**80**, P3 r10/56, P4 v1.0.268/80, P5 v0.1.141/74, avg 68%.
   Fix → re-derive from Convex/`papers.ts`; ideally source these from `papers.ts` so they can never drift again.

5. **Stale 2026-07-15 board on /architecture.**
   `site/src/app/architecture/page.tsx` L152-154 — same stale snapshot (P2 74, P1B v1B.0.108, P4 v1.0.244).

6. **Chat grounding corpus is stale.** `api/chat.mjs` system prompt page-map (L27-37)
   points at legacy `.html` routes and out-of-date counts: "22 research figures"
   (site now says 75), "28-entry glossary" (now 17), "7 deep-dive articles". The
   assistant will cite broken/old links and wrong counts. Fix → update the page map to
   current Next.js routes + counts.

7. **Chat frontend does not render markdown/LaTeX.** Responses display raw
   `\[ ... \frac{}{} ... \]` and literal `###` headers. For an "AI research assistant"
   on a physics site this reads as unfinished. Fix → add a markdown + KaTeX/MathJax
   renderer to the astro chat widget mounted in `#astro-full-chat`.

---

## P2 list (polish)

- **Paper-Artifacts card sha256 overflow** (paper-1a, paper-3): the full 64-char sha256
  doesn't wrap — clips on desktop, forces in-card horizontal scroll on mobile. Fix →
  `overflow-wrap:anywhere` / `word-break:break-all` on the artifacts metadata text, or
  truncate sha256 to 8–12 chars like paper-5 already does. Normalize hash display across
  all 6 papers (currently: full-sha256 / 8-char-sha256 / md5-only — three formats).
- **Paper-5 empty "— REFS"** badge — supply a count or hide the badge when unknown.
- **Floating ">_" terminal button overlaps body text on mobile** (home, papers, data-explorer).
  Fix → add bottom padding / safe-area offset so it never sits over content on narrow viewports.
- **/activity event summaries clip at the right edge** without ellipsis — add `text-overflow:ellipsis` or a fade.
- **/architecture "11 MCP tools" vs /docs "13 tools"** — reconcile the count.
- **/glossary bordered-card-per-term** — mild "boxes within boxes"; dividers/spacing would match the docs aesthetic (per Houston UI preference).
- **/old** — deprecated legacy static site is publicly reachable and heavy (stalls renderers). Noindex or gate behind a clear "archived" banner.
- **Homepage "last refresh July 16"** is 4 days behind today (2026-07-20) even though `/activity` shows events from today — the header timestamp source lags the live feed.

---

## Ranked master fix list (do in this order)

| # | Fix | Severity | File(s) |
|---|---|---|---|
| 1 | Chat system prompt f_NL −35/8 → −35/16 (+ 300×/3–5σ) | P1 | `api/chat.mjs:42` |
| 2 | Data-explorer f_NL −35/8 → −35/16 (all 15) | P1 | root `data-explorer.html` |
| 3 | Reconcile P3 framing (378,280 anomalies → 181-ID recovery) | P1 | `site/src/app/page.tsx`, `site/src/app/contributions/page.tsx`, root `anomaly-explorer.html` |
| 4 | Refresh /reviews board to current (P2 80%, real versions) | P1 | `site/src/app/reviews/page.tsx`, `site/src/app/reviews/ProgressViz.tsx` |
| 5 | Refresh /architecture board | P1 | `site/src/app/architecture/page.tsx:152-154` |
| 6 | Update chat grounding page-map + counts | P1 | `api/chat.mjs:27-37` |
| 7 | Render markdown/LaTeX in astro chat | P1 | astro chat widget (mounts `#astro-full-chat`) |
| 8 | Fix Paper-Artifacts sha256 overflow + normalize hash format | P2 | paper detail component + `site/src/data/papers.ts` pdfMeta |
| 9 | Verify P2/forecast figure images don't bake −35/8 (directive I6) | P2 | `site/src/data/figures.ts`, figure PNGs |
| 10 | Terminal-button mobile overlap; paper-5 refs; activity clip; MCP count; /old noindex | P2 | globals.css / respective components |

**Root-cause recommendation:** the P1 cluster is a single class of bug — hardcoded
snapshots and root legacy HTML that were never re-synced after the last version bumps,
while `papers.ts` + Convex moved on. Run `/bigbounce-claims-table-sync` (for the
−35/8 → −35/16 and 378,280-anomaly claims) and `/site-cohesion-sweep` (for the
readiness board + legacy-embedded surfaces), and where feasible source the /reviews and
/architecture boards from `papers.ts` so they cannot drift again.

## Coverage

23/23 routes visited (desktop + targeted mobile: home, paper-1a, data-explorer, reviews).
All 6 paper PDFs verified `200 application/pdf`. Search + chat backend verified functional.
