# BigBounce Site Inventory — 2026-09-04

Input to a full redesign of `site/` (Next.js, served at https://bigbounce.hubify.app).
Compiled by read-only inventory pass: route map, components, design system,
data layer, live-site screenshots/descriptions, ranked problems, redesign
constraints. No files under `site/` were modified.

---

## 1. Route map

27 routes under `site/src/app` (26 static dirs + root `page.tsx`). Nav
column = linked from `Sidebar.tsx` (the only nav; there is no footer
component in the repo — `grep -rl footer site/src/components` finds only
the string "footer" inside `Sidebar.tsx` itself, not a separate Footer).

| Route | Purpose (1 line) | Data source | Last commit | In nav? | Staleness / quality note |
|---|---|---|---|---|---|
| `/` (root) | Landing page: pitch + three research tracks + CTA | `@/data/papers` (`researchPrograms`, static) | — (root `page.tsx`, not separately tracked) | Yes (`overview`) | Uses current three-track framing (Track A/B/C) correctly. |
| `/activity` | Live event feed (version bumps, R-rounds, findings, closures) | `lib/liveActivity.ts` → Convex `activityFeed` (HTTP client, server-side) | 2026-06-30 | Yes | Feed itself is Convex-live so content is fresh, but the *page shell* hasn't been touched in 2 months — copy/labels may lag current terminology (still literally correct, low risk). |
| `/anomaly-explorer` | DESI anomaly-candidate autoencoder explorer (P3) | Root `.html` read from disk via `readFile` + `dangerouslySetInnerHTML` (`LegacyExplorerClient.tsx`) | 2026-06-30 | Yes | Canonical per project convention (explorer HTML is source of truth); shell page wrapper stale-dated but explorer content is separately maintained. |
| `/architecture` | API & MCP / Convex schema documentation for agents | `@/data/papers` (static) + hard-coded schema table | 2026-08-04 | **No** — not in `Sidebar.tsx` nav | Orphan route: reachable only by direct URL or from `/docs` links. Should be linked from `/docs` or removed from standalone nav ambiguity. |
| `/articles` | Deep-dive essay index | `@/data/articles.ts` (static, 86 lines / 3 articles) | 2026-06-30 | Yes | Small static file, thin content (3 essays) relative to nav prominence. |
| `/chat` | "Astro" research assistant chat UI | Hard-coded shell; backend explicitly disabled | 2026-09-02 | Yes | Page banner reads "Astro is temporarily offline" — a dead-end nav entry pointing at a non-functional feature. |
| `/contributions` | Novelty-scored list of the lab's scientific contributions (N1–N4 scale) | Hard-coded in `page.tsx` | 2026-08-04 | Yes | Still framed around P1A/P1B/P3 (old paper IDs) rather than the 2026-09-02 three-track/A3M framing — needs a pass to match current lineup language. |
| `/data-explorer` | Bayes-factor bounce-vs-inflation discrimination explorer | Root `.html` via `dangerouslySetInnerHTML` (`DataExplorerClient.tsx`) | 2026-06-10 | Yes | Oldest last-touch of any route (87 days). Canonical per convention but should be spot-checked against current A3M numbers. |
| `/docs` | API/MCP/Skills reference for external agents | `DocsClient.tsx`, mostly hard-coded + Convex schema description | 2026-09-02 | Yes | Freshest-dated page; describes Convex as source of truth correctly. |
| `/explained` | Plain-English "what is a big bounce" explainer | Hard-coded prose in `page.tsx` | 2026-07-23 | Yes | Good plain-English purpose page — a rare example of what other pages lack (see Problem #1). |
| `/figures` | Cross-paper figure gallery (63 figures) | `@/data/figures.ts` (static, 557 lines) + `lib/livePapers.ts` (Convex) for live grouping | 2026-08-05 | Yes | **Section header literally reads "63 research figures across all 6 papers (P1A · P1B · P2 · P3 · P4 · P5)"** — hard-coded old six-paper framing that contradicts the current three-track/A3M lineup. Direct evidence of stale copy baked into a template string, not just data. |
| `/final-review` | Houston's personal sign-off checklist for P2 | Hard-coded in `page.tsx` / `final-review.css` | 2026-08-04 | Yes | Single-paper-scoped page (P2 only) permanently in main nav; doesn't generalize to other papers approaching sign-off. |
| `/galaxy-explorer` | Galaxy chirality catalog explorer (P4/P4′) | Root `.html` via `dangerouslySetInnerHTML` | 2026-06-30 | Yes | Canonical; content (8.47M galaxies, dipole stats) matches current P4′ null framing per screenshot. |
| `/glossary` | Term/parameter glossary | Hard-coded in `page.tsx` | 2026-08-04 | Yes | Content is accurate (f_NL = −35/16 correctly shown) but format is flat term list, not connected to where terms are used. |
| `/old` | Interstitial pointing to the legacy static HTML archive | Hard-coded | 2026-08-04 | **No** — not in `Sidebar.tsx` nav (reachable via footer-style "legacy archive" link patterns elsewhere, e.g. `/old/astro/chat-widget.js` referenced from `layout.tsx`) | Intentionally unlisted (archival), consistent with its stated purpose. |
| `/paper` | "Research Tracks" — the 3-track portfolio view (current framing) | `@/data/papers.ts` (`papers`, `researchPrograms`) + `lib/livePapers.ts` (Convex) | 2026-09-02 | Yes | Freshest route; correctly reflects Track A/B/C. This is effectively the canonical replacement for the old "papers" framing — but `/papers` (flat list, below) still exists in parallel and uses old-style per-paper cards. |
| `/papers` | Flat list of every paper/dataset (no track grouping) | `@/data/papers.ts` + `lib/livePapers.ts` (Convex) | 2026-09-02 | Yes | Duplicates `/paper` with a different organizing principle (flat vs. tracked); both are in nav ("research tracks" and "all papers") — redundant IA the redesign should resolve. |
| `/predictions` | Observational-channel predictions (f_NL, birefringence, etc.) | `@/data/predictions.ts` (static, 126 lines) | 2026-06-30 | Yes | Content (f_NL = −35/16) matches current claim; page itself untouched since June. |
| `/publish` | "Portfolio Decisions" — publication-architecture rationale | `@/data/publish.ts` (static, 92 lines) + `@/data/papers.ts` | 2026-09-02 | Yes | Fresh; matches `PUBLICATION_ARCHITECTURE_RESET_2026-08-03.md` framing. |
| `/reproduce` | Reproducibility manifest per experiment/program | `@/data/repro.ts` (static, **5,291 lines**) | 2026-09-02 | Yes | Directly implements standing directive Q2 (reproducibility manifests). Very large static file — good candidate to verify it's Convex-fed rather than hand-maintained going forward. |
| `/reviews` | Review-round timeline, verdict trajectory chart, skills chart | `@/data/reviewTimeline.ts` (static, **10,759 lines / 1.3 MB**) + `lib/liveReadiness.ts` (Convex `readinessMetrics`) + `lib/publicationStatus.ts` (Convex) | 2026-09-02 | Yes (x2 — "reviews" appears once) | Largest single data file in the site by far; per CLAUDE.md this file gets a mandatory append on every review round, so its size is expected but makes the page a heavyweight build dependency. |
| `/search` | Full-text search across the site | `SearchClient.tsx` (likely client-side index over static data) | 2026-09-02 | Yes | Placeholder-quality empty state in screenshot (no results shown by default); scope of what's actually indexed wasn't verified in this pass. |
| `/speculations` | Future/wild research ideas (not yet formal) | Hard-coded in `page.tsx` | 2026-08-04 | Yes | Reasonable "future work" holding page; low content density. |
| `/status` | Comprehensive per-paper readiness dashboard | `lib/livePapers.ts` (Convex), `@/data/readinessBreakdown.ts` (static), `Cards/SurveyQcTable.tsx` | 2026-09-02 | Yes (x2 — appears twice in `NAV_SECTIONS`, once top-level) | **Last-update column shows dates like "July 09, 2026" and "August 4, 2026" for P1A/P3 against today's 2026-09-04** — i.e. the dashboard itself is fresh-coded but is honestly reporting some papers as ~1–2 months stale, which is a genuine backlog signal, not a display bug. Sidebar duplicate entry (`status` listed both inside "research" section and as a bare top-level item) is an IA glitch. |
| `/surveys` | Survey/catalog readiness hub (DESI, LAMOST, SDSS, etc.) | `@/data/surveys.ts` (static, 346 lines) | 2026-07-20 | Yes | "8 surveys / 0 pass" readiness banner in screenshot — worth confirming that's accurate and not a stale zero. |
| `/timeline` | Cosmic history timeline (parent universe → SPHEREx 2028) | Hard-coded in `page.tsx` | 2026-09-02 | Yes | Fresh; narrative-only page, no live data. |
| `/visualize` | 3D/canvas visualization of the bounce (parent-universe collapse etc.) | Root `.html` via `dangerouslySetInnerHTML` (`LegacyVisualizeClient.tsx`) | 2026-07-09 | Yes | Canonical per convention; heavy WebGL/canvas page, dark full-bleed UI distinct from the rest of the site's chrome. |

**Not in the 27-route list above but referenced:** `/papers/[slug]`, `/reviews/[slug]`, `/surveys/[slug]`, `/predictions/[slug]`, `/articles/[slug]` are dynamic detail routes under the corresponding list pages (not separately inventoried as top-level nav items, but they are the actual paper/round/survey detail templates most readers will land on).

---

## 2. Components (`site/src/components/*`)

| Component | Used by |
|---|---|
| `Shell/Sidebar.tsx` | `layout.tsx` (global nav, all pages) |
| `Shell/Topbar.tsx` | `layout.tsx` (global, all pages) |
| `Shell/LiveStatus.tsx` | Topbar (live/Convex status pill shown in every screenshot's top-right corner) |
| `Shell/ScrollToTop.tsx` | `layout.tsx` (global) |
| `MathText.tsx` | `/paper`, `/papers`, `/papers/[slug]`, `/surveys`, `/surveys/[slug]`, `/predictions`, `/predictions/[slug]` |
| `PublicationPath.tsx` | `/paper`, `/papers/[slug]` |
| `PublicationStatusWidget.tsx` | `/reviews` (imports `FreshnessStamp` internally) |
| `ExternalReviewPanel.tsx` | `/papers/[slug]` only |
| `LegacyExplorerClient.tsx` | `/anomaly-explorer`, `/galaxy-explorer` (shared wrapper for both root-`.html` explorers) |
| `Cards/SurveyQcTable.tsx` | `/status` only |
| `Cards/Badge.tsx` | **Unused** — not imported anywhere under `site/src/app` |
| `Feed/FeedItem.tsx` | **Unused** — not imported anywhere under `site/src/app` (dead component; `/activity` renders its feed inline instead) |
| `FreshnessStamp.tsx` | `PublicationStatusWidget.tsx` + referenced in `reviewTimeline.ts` comments |
| `ui/accordion.tsx` | **Unused** in `site/src/app` |
| `ui/scroll-area.tsx` | **Unused** |
| `ui/skeleton.tsx` | **Unused** |
| `ui/tooltip.tsx` | **Unused** |
| `ui/card.tsx`, `ui/badge.tsx`, `ui/button.tsx`, `ui/separator.tsx` | Widely used (12, 15, 8, 10 files respectively) — the actual working design-system primitives |
| `ui/alert.tsx`, `ui/dialog.tsx`, `ui/table.tsx`, `ui/tabs.tsx` | Lightly used (2–3 files each) |

**Redesign note:** 5 of 17 shared components (`Cards/Badge`, `Feed/FeedItem`, `ui/accordion`, `ui/scroll-area`, `ui/skeleton`, `ui/tooltip`) are dead code — candidates to delete or repurpose, not carry forward as-is.

---

## 3. Design system as-is

**Source:** `site/src/app/globals.css` (2,973 lines).

- **Fonts:** Geist Sans (`--font-geist-sans`) for body, Geist Mono (`--font-geist-mono`) for code/data, loaded via `next/font` in `layout.tsx` (`GeistSans`/`GeistMono` variables). No Google Fonts dependency.
- **Color palette (light, root):** warm off-white paper tones — `--bg:#f8f5ef`, `--surface:#fffdf8`, `--surface-2/3/4` stepped tans (`#f0ebe2` → `#d7cfbf`), `--text:#332f2b` (near-black warm gray), `--accent:#2f6f4e` (forest green), `--warn:#8f6a2f`, `--crit:#8b4639`. Sidebar has its own token subset (`--sidebar-bg`, `--sidebar-text`, etc.) distinct from body tokens.
- **Dark mode:** proper `@media (prefers-color-scheme: dark)` block redefining `--bg:#1a1512`, `--surface:#211d18`, `--graphite:#e7eadf`, etc. — screenshots above were captured in dark mode by default (site defaults to system preference, and the boot script in `layout.tsx` reads `localStorage['bigbounce-theme']` or `prefers-color-scheme`). Toggle exists in `Topbar.tsx`.
- **Model/tier colors:** dedicated tokens for reviewer branding (`--model-chatgpt:#6ea8fe`, `--model-grok:#d29922`, `--model-gemini:#a78bfa`) and novelty tiers (`--tier-n4` red → `--tier-n1` purple) — used on `/reviews` and `/contributions`.
- **Layout widths:** `--sidebar-w:247px`, `--topbar-h:44px`, `--max-width:1180px` (main content), `--prose-width:760px` (article/explainer text columns). Fixed sidebar + topbar shell wraps every route.
- **Radius/elevation:** `--radius:6px` / `--radius-lg:8px` / `--radius-xl:12px`; shadcn/ui-style `--color-*` aliases map onto the custom palette (Tailwind v4 `@theme`-style token bridge).
- **Card/border usage (the "boxes-within-boxes" audit Houston's hard rule targets):** `.card` (globals.css:1212) is a bordered, radius, padded box (`border:1px solid var(--border)`). Raw `<Card` component usage per page (grep count, not necessarily all *nested*, but indicative of card density):
  - `/surveys` — 35 `<Card` instances (highest in the site)
  - `/papers` — 28
  - `/status` — 16
  - `/predictions` — 14
  - `/paper` — 6
  - `/figures` — 2
  - `/reviews`, `/publish`, `/reproduce`, `/data-explorer` — 0 `<Card` (use custom bordered `div`s/tables instead, per their own CSS files: `reviews.css`, `publish.css`)
  - High-density pages (`/surveys`, `/papers`, `/status`) are the most likely spots for literal boxes-within-boxes (a `Card` containing a `Card`-styled table row or badge chip) — worth a targeted DOM check during redesign, since grep counts instances but not nesting depth.

---

## 4. Data layer (`site/src/data/*.ts`)

| File | Size | Drives | Duplicated in Convex? |
|---|---|---|---|
| `reviewTimeline.ts` | 10,759 lines / **1.3 MB** | `/reviews` (round history, `externalVerdictRounds`, `gapSeries`, `skillsSeries`) | Partially — `lib/liveReadiness.ts` pulls `readinessMetrics:listWaves`/`listRigorEvents` from Convex for the wave/rigor charts, but the round-by-round narrative history itself is static-file-only (append-only per CLAUDE.md review-round-sync directive). Largest data file in the repo by 8×. |
| `papers.ts` | 925 lines / 92 KB | `/paper`, `/papers`, `/papers/[slug]`, `/architecture`, `/publish`, `/status` (paper metadata, `researchPrograms`) | Yes — `lib/livePapers.ts` overlays Convex `papers:listAllPaperStates` (version/readiness/pdfMeta) on top of this static shape; static file is the schema/fallback, Convex is the live source per directive A. |
| `repro.ts` | 5,291 lines / 233 KB | `/reproduce` | Not checked against Convex in this pass — worth confirming whether reproducibility manifests should migrate to a Convex collection like `paperVersions`/`activityFeed` did. |
| `figures.ts` | 557 lines / 40 KB | `/figures` (static `figureSections`, merged with `lib/livePapers.ts` live grouping) | Partial — Convex has a `figures.ts` module (`convex/figures.ts`) but the site's static file still hard-codes the "6 papers" section list flagged as stale in §1. |
| `live-status.ts` | 160 lines / 7 KB | `Shell/LiveStatus.tsx` (topbar pill), freshness-check script | Yes, directly — `tools/site_freshness_check.sh` explicitly diffs this file's `lastUpdatedISO`/versions against Convex `paperVersions:current` and fails the pre-push gate on mismatch. |
| `publish.ts` | 92 lines / 10 KB | `/publish` | No — static-only rationale/decision text. |
| `surveys.ts` | 346 lines / 16 KB | `/surveys` | Not checked; likely static-only (no `liveSurveys.ts` lib file found). |
| `predictions.ts` | 126 lines / 7.6 KB | `/predictions` | No — static-only. |
| `articles.ts` | 86 lines / 4 KB | `/articles`, `/articles/[slug]` | No. |
| `readinessBreakdown.ts` | 70 lines / 5.4 KB | `/status` (gate ownership table) | No — but conceptually overlaps Convex `readinessMetrics.ts`; `lib/liveReadiness.ts` comments reference a "retirement note in convex/readinessMetrics.ts," suggesting this static file may be a legacy path being phased out. |

**Convex backend inventory** (`convex/*.ts`, 24 modules): `activityFeed`, `activityRollup`, `analytics`, `chatMessages`, `checklist`, `externalReviews`, `feedback`, `figures`, `findings`, `galaxies`, `mcmcStatus`, `models`, `notables`, `paperVersions`, `papers`, `pathcCaveats`, `pipelineState`, `pods`, `publicationStatus`, `rRounds`, `readinessMetrics`, `reviews`, `schema`, `spectralResults`, `tasks`. Per directive A, this is the *only* readiness source; every static mirror above must stay in sync with it or the freshness gate fails.

---

## 5. Screenshots + visual descriptions (live site, desktop width, dark theme as-served)

All 27 top-level routes were captured live at `bigbounce.hubify.app` via the in-app browser. General shell across every page: fixed dark-charcoal left sidebar (247px) with grouped nav (overview/explainer, research, explore, articles, chat), a thin topbar with breadcrumb + "spin-torsion cosmology research program" tagline + a live-status pill, and a warm dark content area (`--bg:#1a1512`) using the green accent (`#2f6f4e`) sparingly for links/badges.

- **`/`** — Strong, editorial hero: "Was there a bounce before the Big Bang?" headline, one-paragraph pitch, two CTA buttons ("Start with the explainer", "Browse papers & artifacts"), then "Three questions, three lead results" as plain bordered rows per track. Hierarchy is clear and this is the best-designed page on the site.
- **`/activity`** — Dense stat strip (Findings 807, Review Rounds 75, Findings closed 115...) above a chronological feed of terse commit-style log lines ("PAPER-A3M bumped to v3M.0.10 ..."). Readable but very engineering-log in tone for a page one click from the homepage nav.
- **`/anomaly-explorer`** — Long explanatory prose block above the actual explorer UI (which is below the fold in the screenshot) — a reader has to scroll past three paragraphs of methodology before reaching the interactive tool.
- **`/architecture`** — Clean docs-style page: intro paragraph, a "Convex schema" heading, and a bordered data table (columns/purpose) — closest in style to a Mintlify-style reference page, but this page is not reachable from nav.
- **`/articles`** — Simple card list of 3 essays with category tags ("essay", "AI & science") — thin content relative to its own nav section.
- **`/chat`** — Full-width dark hero titled "astro" with a single bordered notice box: "Astro is temporarily offline." A dead-end feature kept permanently in primary nav.
- **`/contributions`** — Numeric novelty-scale legend (N1–N4) followed by a "flagship" callout naming P1A/P1B/P3 in old per-paper language, not the current Track A/B/C framing.
- **`/data-explorer`** — Dense data table (Bayes-factor discrimination) with a left filter rail — functional, information-dense, closest to a real analysis tool rather than marketing content.
- **`/docs`** — Left-nav docs shell (Getting Started/Overview, Reference sections) with an "internal documentation" callout banner and inline code terms (Convex DB, bigbounce-mcp, bigbounce.hubify.app) — good IA, correctly states Convex is the live truth source.
- **`/explained`** — Clean long-form explainer with proper section headings (The Standard Story, The Problem with the Beginning, The Bounce Alternative) — the single best "plain English purpose" page on the site; should be the template for others.
- **`/figures`** — Filterable gallery with left facet list (paper 1A/1B/2/3/4/5/cross-cutting) and a grid of figure thumbnails; header text literally says "63 research figures across all 6 papers" — stale six-paper framing baked into the copy (see §1).
- **`/final-review`** — Focused single-purpose checklist page for P2 with a 4-question gate list and PDF/audit links — well-scoped but permanently paper-specific in global nav.
- **`/galaxy-explorer`** — Strong stat-tile row (8,474,531 galaxies / 1,687,069 / dipole significance 0.41σ / 0.4974) above "Key Science Findings" cards — good data-forward design, consistent with the anomaly explorer.
- **`/glossary`** — Flat definition list, each term in its own bordered card with parameter/unit line — accurate content (f_NL = −35/16, birefringence values correct) but purely alphabetical with no cross-linking to where each term is used.
- **`/old`** — Minimal single-paragraph interstitial ("First-generation site, preserved as-is") with one link forward and one back — clean, does exactly one job.
- **`/paper`** — "Research tracks" headline, Track A/B/C narrative blocks with a leading "Question:"/"Boundary:" structure, then paper cards nested below — the most current framing on the site and a good candidate as the IA anchor.
- **`/papers`** — Flat card list per paper with status badges (e.g. "SPECULATIVE") and a "Details >" link — visually similar to `/paper` but organized differently (see IA redundancy note in §1/§6).
- **`/predictions`** — Stat-forward header (f_NL=−35/16, 4 channels, 4 constraints, next target SPHEREx) then per-channel expandable cards ("Open prediction >") — reasonably scannable.
- **`/publish`** — Long-form decision memo ("Choose the science before the submission sequence") with a highlighted "The rule" callout box — dense but well-structured prose, closer to an internal memo than a public page.
- **`/reproduce`** — Stat strip (3 programs / 55 experiment manifests / 44 runnable now / $36.04 est. total cost) then per-program manifest detail — directly implements the reproducibility-manifest directive and is one of the more information-rich, well-organized pages.
- **`/reviews`** — Long headline paragraph packed with inline stats (evidence-capped ASI, 4 active reviewers, per-paper verdict letters) followed by a "PROGRESS" table — the densest single paragraph of prose-as-dashboard on the site; hard to scan.
- **`/search`** — Minimal search box with example-query chips ("perturbation transparency", "f_NL, AJ vs ApJS", "MASCEDoc even reviewer"...) and an empty results area — looks unfinished/placeholder in its default state.
- **`/speculations`** — "Living document" framing, per-idea cards under topic headers (Cosmology & Dark Energy) with status tags ("SPECULATIVE", "COSMOLOGY") — reasonable holding-pen page.
- **`/status`** — The most data-dense page: a colored progress bar ("10/10 with no recorded open BLOCKER/MAJOR"), then a per-paper table (version, readiness %, open findings, last update) — last-update column visibly shows July/August dates against a September "today," which is an honest but visually unaddressed staleness signal.
- **`/surveys`** — Stat strip (37.3M combined, 0 pass-for-survey-hard, 0/8 pass, 8 surveys) then a table of named surveys (DESI, LAMOST, SDSS, eROSITA, Gaia, WISExWCS, Planck, ACT) with counts and a status badge per row — the "0/8 pass" headline reads alarmingly and isn't explained on-screen.
- **`/timeline`** — Simple vertical narrative timeline (Parent Universe → Contraction Phase → The Bounce...) in bordered cards — clean but content-thin relative to the rest of the site's density.
- **`/visualize`** — Full-bleed dark WebGL/canvas scene ("Parent Universe — Stellar Collapse") with a bottom timeline scrubber and speed controls — visually striking and completely different chrome from the rest of the site (no sidebar/topbar prose density), a jarring but intentional break in style.

---

## 6. Ranked top 10 problems (for a reader trying to understand the lab's research)

1. **No single, current "what changed and why should I care" entry point.** The homepage is good, but from there a reader is immediately offered *two* competing IA schemes — `/paper` (three tracks) and `/papers` (flat six-paper list) — that organize the same underlying work differently, with no page explaining which one to use or how they relate.
2. **Stale six-paper framing baked directly into copy, not just data.** `/figures` literally renders "across all 6 papers (P1A · P1B · P2 · P3 · P4 · P5)" and `/contributions` still names P1A/P1B/P3 — both contradict the 2026-09-02 three-track (A/B/C) lineup that `/paper`, `/publish`, and CLAUDE.md itself establish as canonical. A reader landing on `/figures` before `/paper` gets the *old* mental model first.
3. **Jargon-only titles with no plain-English gloss on most nav items** — "namaster-proof," "ECH Note," "A3M," "f_NL," "DESIVAST" appear as primary labels across `/papers`, `/status`, `/reviews` without a hover/subtitle translation, despite directive Q3 explicitly requiring plain-English purpose labels. `/explained` and `/glossary` exist but aren't cross-linked from the jargon itself.
4. **A dead feature in primary nav.** `/chat` ("astro") is permanently listed in the sidebar and its only content is "Astro is temporarily offline" — a guaranteed dead end for any curious first-time visitor who clicks it.
5. **Honest but unexplained-looking negative numbers.** `/surveys` headlines "0/8 pass" and `/status` shows a large readiness bar next to per-paper rows with two-month-old "last update" dates — both are accurate reporting per directive R6 (publish nulls as nulls / accurate dates) but read, unexplained, as "this site is broken" rather than "this is honest science."
6. **Duplicate/ambiguous sidebar entries.** `status` appears twice in `Sidebar.tsx`'s nav config (once inside "research," once as a bare top-level item) — a small but concrete IA bug.
7. **Orphan routes only reachable by typed URL.** `/architecture` (a genuinely useful API/MCP reference) has no nav entry and isn't linked from `/docs`, so most readers will never find it.
8. **Reviews page is prose-as-dashboard.** `/reviews`'s lead paragraph packs numeric state (evidence-capped ASI status, active reviewer counts, per-paper verdict letters) into a single dense sentence rather than a scannable stat/status layout — the least accessible page for a non-specialist trying to gauge "is this trustworthy yet."
9. **Card-density imbalance signals inconsistent information architecture.** `/surveys` (35 `<Card>` instances) and `/papers` (28) are far denser than `/reviews`, `/publish`, `/reproduce`, `/data-explorer` (0 `<Card>`, custom layouts instead) — the site has no single consistent pattern for "list of things," which compounds the boxes-within-boxes risk Houston's hard rule targets.
10. **Explorer pages front-load methodology prose before the interactive tool.** `/anomaly-explorer` (and to a lesser extent `/data-explorer`) puts several paragraphs of caveats/methodology above the fold before the actual explorer UI appears — the most "show, don't tell" pages on the site currently tell first.

---

## 7. Constraints for the redesign

- **Convex is the only readiness source** (standing directive A). Any redesigned page that shows readiness/version/round data must read through `lib/livePapers.ts` / `lib/liveReadiness.ts` / `lib/publicationStatus.ts` (or new equivalents) against Convex — never reintroduce a hand-maintained static readiness number. Static `site/src/data/*.ts` files may stay as schema/fallback/narrative content but must not become the readiness source of truth.
- **Explorers' root `.html` files are canonical** (`project_explorer_html_canonical.md` memory entry). `/anomaly-explorer`, `/galaxy-explorer`, `/data-explorer` render a root `.html` file via `dangerouslySetInnerHTML` inside `LegacyExplorerClient.tsx`/`DataExplorerClient.tsx` — a redesign may restyle the *wrapper chrome* (intro copy, surrounding page shell) but must edit-and-commit the `.html` itself for any content change, never treat it as a deprecated mirror to replace wholesale.
- **`reviewTimeline.ts` schema is fixed and append-only.** Every review round (internal or external) adds a `ReviewRound` entry and, when applicable, extends `externalVerdictRounds`/`gapSeries`/`skillsSeries` — per CLAUDE.md's "Review-round site sync" standing rule, this must happen in the same commit bundle as the round's artifacts. A redesign of `/reviews` must consume this schema as-is (or migrate it via a real data migration, not a silent format change) since it's actively written by the review pipeline every round.
- **Freshness gate — `tools/site_freshness_check.sh`.** Checks four things and fails the pre-push hook if any is stale: (1) **Banner** — `live-status.ts`'s `lastUpdatedISO` vs. the newest Convex wave / EXT manifest, stale if >6h older; (2) **Skills** — the last `skillsSeries` point vs. the newest lesson-commit in the scistack `bigbounce-r-round/SKILL.md` and newest `tools/` commit, stale if a commit is >12h newer; (3) **Board** — latest `externalVerdictRounds` date vs. newest harvested external round, stale if a harvested round has no board entry after 6h; (4) **Versions** — every Convex `paperVersions:current` entry per paper must appear in `live-status.ts`, mismatches reported individually. A redesign that restructures or renames `live-status.ts`/`reviewTimeline.ts` fields must update this script in the same change, or the pre-push hook (and cron tick) will start failing/blocking pushes.

---

*Screenshots were viewed live in-session (in-app browser) rather than saved as separate image files; visual descriptions in §5 are the durable record per this task's instructions.*
