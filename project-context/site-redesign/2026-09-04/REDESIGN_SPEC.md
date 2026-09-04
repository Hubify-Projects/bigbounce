# BigBounce site redesign — specification

**Date:** 2026-09-04 · **Author:** design director lane (Claude) · **Target:** https://bigbounce.hubify.app (`site/`, Next.js App Router + Convex)
**Input:** `INVENTORY.md` (this directory) · `VISION.md` · `PUBLICATION_ARCHITECTURE_RESET_2026-08-03.md` · `SSOT/index.md` · `SESSION_HANDOFF_2026-09-04.md`
**Status:** SPEC — decisive, implementation-ready. No `site/` file was modified while writing it.

## Plan header

| # | Section | State |
|---|---|---|
| 1 | Positioning | drafted |
| 2 | Information architecture + route table | drafted |
| 3 | Content model per page | drafted |
| 4 | Visual language | drafted |
| 5 | Components (keep / build / delete) | drafted |
| 6 | Implementation plan (Sonnet lanes) | drafted |
| 7 | Risks and what NOT to change | drafted |

**Governing rules this spec obeys (non-negotiable):** no boxes-within-boxes (bordered surfaces only for genuine
tools — code blocks, data tables, explorers); premium Vercel/Mintlify reading experience; form inputs never carry a
focus ring on the inner element (`focus-within` on the wrapper only); every paper/program carries a plain-English
purpose label (directive Q3); **Convex is the only readiness source** (directive A); explorers' root `.html` files are
canonical; `reviewTimeline.ts` schema and `tools/site_freshness_check.sh` contracts are preserved.

---

## 1. Positioning — what the site says in ten seconds

The site is the **public face of a reproducible cosmology lab**, not a paper archive and not a dashboard for its own
review machinery. One sentence carries it: *"Was the Big Bang the beginning? We test a nonsingular bounce against data
that exists now — and we publish the nulls."*

Three readers, three ten-second reads. The homepage must satisfy all three above the fold plus one scroll.

**A physicist** must get, in order: (a) the question and the concrete claim — the exact matter-contraction amplitude
`f_NL^local = −35/16`, transmitted through the bounce to `f_NL^after ∈ [−0.65, −0.50]`; (b) the three research tracks
as *questions*, not paper IDs; (c) the current evidence grade per result, including that Track A's PTA, PBH and
high-z-PNG channels are **measured nulls** and the LSS channel is reachable but not separable at SPHEREx sensitivity
(0.7–0.9σ); (d) one click to the PDF, the derivation, and the reproduction manifest. Jargon is allowed here but never
unglossed — every ID (`A3M`, `namaster-proof`, `ECH Note`, `DESIVAST`) shows a plain-English purpose line beside it.

**A journalist or curious non-specialist** must get: the question in plain English, the honest state ("no detection
yet; three channels ruled out; one still open"), and a visible route into `/explained`. They must never meet a raw
paper ID, a readiness percentage, or a reviewer verdict letter before they meet the science. The words "0/8 pass" and
"three nulls" must arrive already framed as *findings*, never as broken widgets.

**A Hubify platform visitor** must get: this is the flagship reproducible lab — 3 programs, ~55 experiment manifests,
44 runnable now, ≈$36 total estimated reproduction cost, every artifact addressed by DOI/HF/B2 link, an API and MCP
surface for agents. That is the platform proof, and it earns a first-class nav slot (`/reproduce`), not a footnote.

**Four positioning commitments the design must physically enforce.**

1. **Evidence grade is a visual primitive, not prose.** Every result carries one of four grades — `measured`,
   `derived`, `null`, `open` — rendered as a typographic label with its own tonal color, used identically on the
   homepage, track pages, paper pages and the status page. A null is a contribution: it gets the same weight and a
   calm slate tone, never an error red.
2. **Nulls are headlined, not buried.** The homepage says "three channels closed as nulls" as a *result count*, in the
   same type as any positive claim. This is directive R6 made visible.
3. **Review convergence is back-of-house.** Verdict letters, wave counts and reviewer names move off the primary
   surface into `/reviews`, which is explicitly labeled as internal QA evidence — a gate, never the product
   (directive R2). No verdict letter appears on the homepage or on a paper page's hero.
4. **Readiness is one number with one source.** A single Convex-fed publication-readiness percentage per work, with
   the composition (science 25 / evidence 25 / review convergence 25 / packaging 20 / Houston's sign-off 5) shown on
   hover or on `/status` only. Venue, endorsement and submission live in a separate "publishing" strip that never
   subtracts from the score (directive P).

**Voice.** Declarative, quantitative, unhedged about uncertainty. Sentence case everywhere. No exclamation, no
marketing verbs, no "revolutionary". The register of a good PRD abstract, one notch warmer.

## 2. Information architecture

### 2.1 The one structural decision: `/paper` vs `/papers` is resolved as *tracks are the spine, the flat list is the index*

`/paper` (three tracks) becomes **`/research`** — the canonical scientific spine, one page per track. `/papers` stays
as the **flat, complete index of every work** — papers, notes, software, and data releases in one sortable list, which
directive Q3 requires. They are no longer two competing schemes: `/research` answers *"what questions is this lab
asking and what did it find?"*, `/papers` answers *"show me everything, let me find one."* Every track page links down
into the flat list filtered to that track; every entry in the flat list names its track. `/paper` 301s to `/research`.

### 2.2 Primary nav — six items

`Research` · `Works` (`/papers`) · `Explore` · `Reproduce` · `Status` · `Learn`

The wordmark is home. Search is **not** a nav item — it becomes a topbar affordance opened by `⌘K`/`/` (route
`/search` survives for deep links). The current duplicate `status` entry and the grouped-section sidebar disappear:
the shell drops the 247px sidebar for a **slim sticky topbar** (wordmark, six links, search, theme toggle, live-status
dot) so content gets the full width — the sidebar is the single biggest source of the site's "app chrome around
reading material" feel and it is not carrying its cost across 27 routes.

Section hubs carry their own secondary nav (a row of text links under the page title, not a second sidebar).

### 2.3 Footer

One full-width band, four columns, no borders: **Lab** (Overview, Explained, Timeline, Contributions) ·
**Works** (All works, Research tracks, Figures, Predictions) · **Reproduce** (Manifests, Data sources, Releases &
DOIs, HuggingFace / Backblaze / Zenodo) · **Build on it** (Docs, API & MCP architecture, GitHub, Activity, Legacy
archive `/old`). Bottom line: author + email, the honesty statement ("Nulls are published as nulls; readiness is read
live from Convex"), and a live freshness stamp.

### 2.4 Route table — old → new

| Old route | New route | Disposition |
|---|---|---|
| `/` | `/` | **Rebuild.** Best page today; becomes the ten-second answer for all three readers (§3.1). |
| `/paper` | `/research` | **Rename + 301.** Canonical track spine; adds `/research/[track]`. |
| — | `/research/[track]` | **New.** One page per track (A, B, C) — §3.3. |
| `/papers` | `/papers` | **Keep, rebuild.** Flat complete index of papers + notes + software + data releases (Q3). |
| `/papers/[slug]` | `/papers/[slug]` | **Keep, rebuild** to the paper template (§3.4). |
| `/status` | `/status` | **Keep, rebuild.** Single readiness dashboard; absorbs `/final-review`; Convex-only numbers. |
| `/final-review` | `/status#signoff` | **Merge + 301.** Becomes a generic per-work sign-off block, not a P2-only page. |
| `/reviews` | `/reviews` | **Keep, simplify** (§3.6). Explicitly framed as internal QA evidence; child of Status. |
| `/reviews/[slug]` | `/reviews/[slug]` | **Keep**, restyled; schema untouched. |
| `/activity` | `/activity` | **Keep**, restyled; child of Status; footer + Status link only. |
| `/publish` | `/publish` | **Keep**, retitled "Publishing"; child of Status; the venue/endorsement/submission strip. |
| `/contributions` | `/research#contributions` | **Merge + 301.** Novelty-graded contribution list rewritten to track framing; the N1–N4 legend survives. |
| `/reproduce` | `/reproduce` | **Keep, promote to primary nav.** Becomes the Data & reproducibility hub (§3.7). |
| `/surveys`, `/surveys/[slug]` | `/reproduce/surveys`, `/reproduce/surveys/[slug]` | **Move.** Data sources belong to the reproducibility hub; "0/8 pass" gets its framing sentence. |
| `/predictions`, `/predictions/[slug]` | `/predictions`, `/predictions/[slug]` | **Keep**, linked from `/research/track-a`; observational-channel detail. |
| `/figures` | `/explore/figures` + `/figures` 301 | **Move + rebuild.** Facets read live from Convex/track data — the hard-coded "6 papers" string is deleted. |
| `/galaxy-explorer`, `/anomaly-explorer`, `/data-explorer`, `/visualize` | unchanged paths | **Keep paths and their root `.html` verbatim.** Wrapper chrome only: tool first, methodology prose collapsed beneath it. |
| — | `/explore` | **New.** Small hub page: four tools + figures, one line each. |
| `/explained` | `/explained` | **Keep.** Becomes the Learn hub's lead page and the model for long-form voice. |
| `/glossary` | `/glossary` | **Keep, rebuild** as a two-column definition list with back-links to where each term is used. |
| `/timeline` | `/timeline` | **Keep**, restyled as a single typographic timeline (no per-step cards). |
| `/articles`, `/articles/[slug]` | `/articles`, `/articles/[slug]` | **Keep**, folded under Learn. |
| `/speculations` | `/speculations` | **Keep**, folded under Learn, labeled "not yet formal work". |
| `/docs` | `/docs` | **Keep**, absorbs `/architecture` as `/docs/architecture`. |
| `/architecture` | `/docs/architecture` | **Move + 301.** Ends the orphan route. |
| `/search` | `/search` | **Keep** as a route; entry point moves to the `⌘K` topbar affordance. |
| `/chat` | — | **RETIRE.** Delete route, page, and nav entry; no redirect target beyond `/` — a dead feature must not sit in nav. |
| `/old` | `/old` | **Keep, unlisted** (footer link only). |

## 3. Content model per page

Binding legend: **[C]** Convex-live (via `lib/livePapers.ts`, `lib/liveReadiness.ts`, `lib/publicationStatus.ts`,
`lib/liveActivity.ts`) · **[S]** static file under `site/src/data/` (schema, narrative, fallback) · **[H]** root
`.html`, canonical, untouched. Readiness/version/round numbers are **[C] only** — never re-typed into a static file
except the `live-status.ts` mirror the freshness gate already checks.

### 3.1 Homepage `/` — wireframe in words

Full-width bands, top to bottom, no cards anywhere on this page:

1. **Hero band** (bg base). Eyebrow: `spin-torsion cosmology · reproducible lab`. H1, two lines max:
   *"Was the Big Bang the beginning?"* Sub, one sentence: the lab tests a nonsingular bounce against data that exists
   now, and publishes the nulls. Two links, text-first, no button pair competing for weight: **Start with the
   explainer** (primary) · **All works** (quiet). [S]
2. **Live result strip** — four numbers on one row, hairline dividers between, no boxes: works published-ready,
   channels closed as nulls, experiment manifests runnable now, reproduction cost. [C] for the first, [S]+[C] for the
   rest. Each number's label is plain English; each links to its page.
3. **The claim band** (tonal shift, surface-1). One equation rendered large and centered —
   `f_NL^local = −35/16 → f_NL^after ∈ [−0.65, −0.50]` — with a one-line gloss underneath and a `derived` evidence
   chip. This is the lab's single strongest sentence; it gets its own band. [S]
4. **Three tracks band** — three rows (not three cards), each: track letter + question in H3, one-sentence lead
   result, evidence chips for its channels, right-aligned readiness figure [C], whole row links to
   `/research/track-x`. Rows separated by hairlines only.
5. **Nulls band** (surface-1, calm slate accent). Title: *"What we ruled out."* Three to four one-line entries —
   PTA (14.3 dex below NANOGrav), PBH (`f_PBH = 0`, 7.0 dex short), high-z PNG / SMBH-seed (FIRAS-excluded), chiral GW
   at LISA (≤6e−13) — each with its receipt link. Same type weight as the claim band. [S]
6. **Reproducibility band** — one paragraph plus a three-item row: manifests, data sources, releases & DOIs; ends
   with the HuggingFace / Backblaze / Zenodo lockup. [S]+[C]
7. **Latest band** — five most recent activity lines, terse, mono timestamps, link to `/activity`. [C]
8. Footer (§2.3).

### 3.2 `/papers` — all works (flat index, directive Q3)

Purpose: find any work in one screen. Sections in order: (a) H1 "All works" + one line explaining that this is the
complete flat list and `/research` is the same material grouped by question; (b) a filter row — kind (paper / note /
software / data release), track, state — rendered as text toggles, no bordered chips; (c) **one table**, the only
bordered surface on the page: columns *Work* (short title + **plain-English purpose line**, mandatory), *Kind*,
*Track*, *Version* [C], *Readiness* [C], *State* (Convex publication status [C]), *PDF*. Sorted by track then
readiness. Row → `/papers/[slug]`. No card grid; the 28-`<Card>` layout is deleted.

### 3.3 `/research` and `/research/[track]` — track template

`/research`: H1 + the three-track rationale in two sentences (from `PUBLICATION_ARCHITECTURE_RESET`), then the same
three rows as the homepage but expanded with each track's works listed inline; then `#contributions` — the novelty
graded list (N1–N4 legend kept, prose rewritten to track framing).

`/research/[track]` sections in fixed order:
1. **Question** — the track's question in H1-adjacent large type, verbatim from `VISION.md`.
2. **Lead result** — one paragraph, one equation or number, one evidence chip.
3. **Channels / tests table** — the only bordered surface: channel, prediction, current data, evidence grade,
   receipt link. Nulls appear here as first-class rows.
4. **Works in this track** — rows (title, purpose line, version [C], readiness [C], state [C]) → `/papers/[slug]`.
5. **What is still open** — the track's open ledger rows in plain English, each with its blocker. [S]
6. **Boundary** — what this track does *not* claim. Directly from the architecture reset's "What it is not" prose.

### 3.4 `/papers/[slug]` — paper template

The most-landed-on page. Sections in fixed order, single 760px prose column with full-width bands for data:

1. **Header band** — kind label (Paper · Note · Software · Data release), H1 title, **purpose line in plain English
   directly under the title** (Q3, mandatory, never omitted), then a mono metadata row: version [C] · date [C] ·
   pages [C] · md5 [C] · track. No badges cluster; no card.
2. **Actions row** — text links, hairline above/below: Read PDF · arXiv/Zenodo DOI · Source `.tex` · Reproduction
   manifest · Figures. Missing links are omitted, never rendered disabled.
3. **Abstract** — verbatim, prose width.
4. **Result summary** — 2–4 lines, each a claim + its evidence chip. Nulls sit here with equal weight.
5. **Figures** — inline gallery from `figures.ts` [S] filtered to this work; click opens full size.
6. **Readiness** — one number [C] plus the five-part composition bar (science / evidence / review / packaging /
   sign-off) as a single segmented rule, no nested boxes. Below it, one sentence: readiness is publication readiness
   only; venue and submission are tracked separately (directive P).
7. **Publishing** — venue, endorsement state, submission state [C via `publicationStatus`]; explicitly labeled
   "not part of readiness".
8. **Review evidence** — collapsed by default: current verdict row per active leg + link to `/reviews`. Never above
   the abstract.
9. **Reproduce this** — manifest summary from `repro.ts` [S]: inputs, scripts, compute venue, est. cost, wall-clock;
   link into `/reproduce`.
10. **Lineage** — one paragraph: what this work was, what it became, what it does not claim.

### 3.5 `/status` — readiness dashboard

Purpose: one honest picture of where every work stands. Sections: (a) H1 + one framing sentence — dates shown are
real last-update dates and a two-month-old date is a backlog signal, not a bug; (b) **one table** [C]: work, version,
readiness, open findings, last update, publishing state — last-update cells older than 30 days get a quiet
"stale — no change since" annotation rather than silent old dates; (c) **`#signoff`** — the generalized final-review
block: per work, the four agent gates plus Houston's sign-off slot (95 → 100), replacing the P2-only `/final-review`;
(d) survey QC table (existing `SurveyQcTable`) moved to `/reproduce/surveys`; (e) links out to `/reviews`,
`/activity`, `/publish`. No hand-maintained readiness numbers anywhere on this page.

### 3.6 `/reviews` — internal QA evidence, simplified

Reframed at the top: *"Automated multi-model review is a gate on publication readiness, not a product. Rounds stop
when the remaining findings are genre or venue."* (directives R2, P.) Sections in order:

1. **Verdict grid**, newest rounds on the **left** — rows = works, columns = rounds, cells = verdict letters. Active
   legs only per directive M-AMENDED; frozen legs (OpenAI/ChatGPT) shown greyed with a "frozen, not counted"
   footnote, never deleted, never faked. The all-A meter states it counts active legs only. [S `reviewTimeline.ts`
   `externalVerdictRounds`, schema unchanged.]
2. **Publication status widget** [C] — kept, restyled, de-nested.
3. **Round timeline** — reverse-chronological rows, one line each: date · kind · what changed · receipt link.
   `kind:"skill-improvement"` entries render with a distinct quiet marker. [S, append-only, schema unchanged.]
4. **Gap and skills charts** — kept, single-accent line charts, axis labels in mono. [S `gapSeries`, `skillsSeries`.]
5. The dense lead paragraph of numbers is deleted; those numbers become the stat row.

### 3.7 `/reproduce` — data & reproducibility hub

Sections: (a) H1 "Reproduce everything" + the platform sentence (flagship reproducible lab; every experiment carries a
manifest per directive Q2); (b) stat row — programs, manifests, runnable now, est. total cost; (c) **manifest table**
per program (the one bordered surface): experiment, inputs + external links (DESI, HF, SDSS…), scripts, compute venue
(local ≈ free vs RunPod GPU), est. cost, wall-clock, state [S `repro.ts`]; (d) **`/reproduce/surveys`** — data sources
and QC readiness, with the "0 of 8 clear the survey-hard bar" number given its explanatory sentence *on screen*;
(e) **Releases & DOIs** — Zenodo records, HuggingFace datasets, Backblaze B2 mirrors, GitHub releases, each with the
work it belongs to; (f) an "how to run one" code block (a genuine bordered surface).

### 3.8 Explore and Learn hubs

`/explore`: five one-line entries (galaxy explorer, anomaly explorer, data explorer, visualize, figures), each with
its headline number. Explorer pages themselves: **tool first** — the `.html` [H] renders directly under a two-line
intro; methodology and caveats move to a "How this was made" section *below* the tool. Wrapper chrome only; the
`.html` files are edited only when their content changes, never replaced.

`/learn`: `/explained` is the lead; `/glossary`, `/timeline`, `/articles`, `/speculations` follow as one-line entries.
Glossary terms become anchor targets so jargon anywhere on the site can link straight to its definition (fixes the
"jargon-only labels" problem at the source).

## 4. Visual language

**Direction in one line:** warm paper, editorial typography, full-width tonal bands, one green accent — a physics
preprint that reads like a well-set journal page, with the only boxes being real tools.

### 4.1 Type — one text face, one mono

Keep **Geist Sans** (body/display) and **Geist Mono** (numbers, versions, md5, code, axis labels), already loaded via
`next/font` — no Google Fonts dependency, no CSP surface. No third face.

| Role | Size / line-height | Weight | Notes |
|---|---|---|---|
| Display (hero H1) | 56 / 1.05 (mobile 36) | 600 | tracking −0.02em; max 2 lines |
| H1 page title | 36 / 1.15 | 600 | tracking −0.015em |
| H2 band title | 24 / 1.25 | 600 | |
| H3 row title | 18 / 1.35 | 600 | |
| Body | 16 / 1.65 | 400 | prose column only |
| Body large (lead) | 19 / 1.55 | 400 | one per page, under H1 |
| Small / meta | 13.5 / 1.45 | 400 | plain-English purpose lines use this at full ink |
| Mono data | 13.5 / 1.4 | 450 | tabular-nums on every numeric column |
| Eyebrow | 12 / 1.2 | 500 | uppercase, tracking 0.08em, muted |

Numerals: `font-variant-numeric: tabular-nums` on all tables and stat rows. Equations render with the existing
`MathText` component at body-large size, centered when they are a band's subject, inline otherwise.

### 4.2 Color tokens

Light (`:root`) keeps the warm paper family, tightened to four backgrounds and three inks:

```
--bg:        #faf8f3   /* page ground */
--bg-1:      #f2eee5   /* alternate band (tonal shift, no border) */
--bg-2:      #e9e3d7   /* deep band: nulls, footer */
--tool:      #fffdf8   /* bordered tool surfaces only (tables, code, explorers) */
--ink:       #2b2825   /* primary text */
--ink-2:     #5b544c   /* secondary */
--ink-3:     #8a8177   /* meta, muted */
--rule:      #ddd6c8   /* hairlines, table borders */
--accent:    #2f6f4e   /* the single accent: links, active nav, primary chart line */
--accent-ink:#215239   /* accent text on light ground (AA on --bg) */
```

Dark (`@media (prefers-color-scheme: dark)` + `[data-theme="dark"]`, both, per the existing boot script):

```
--bg:#17130f  --bg-1:#1e1a15  --bg-2:#241f19  --tool:#211d18
--ink:#ece7dd  --ink-2:#b6aea1  --ink-3:#877f73  --rule:#372f26
--accent:#63b98a  --accent-ink:#8fd3ab
```

**Evidence-grade colors** — four, used identically everywhere, rendered as a 6px square dot + label in `--ink-2`,
never as a filled pill:

```
--grade-measured: var(--accent)   /* green  — measured in data */
--grade-derived:  #4b6ea8 / dark #7ea3d8   /* blue — derived analytically */
--grade-null:     #6f7a72 / dark #93a099   /* slate — a null result, a contribution */
--grade-open:     #9a7430 / dark #cfa458   /* amber — open, not yet answered */
```

A null is **never red**. Red exists only as `--danger:#8b4639` for genuine failure states (broken build, failed
freshness gate) and appears nowhere in scientific content. Reviewer-brand colors
(`--model-grok`/`--model-gemini`/`--model-chatgpt`) survive **only** inside `/reviews`.

### 4.3 Space, width, surfaces

Spacing scale (px): `4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 96 · 128`. Band vertical rhythm: 96 desktop / 56 mobile.
Widths: `--prose: 720px` (all long-form text), `--content: 1120px` (tables, rows, stat strips), bands are full-bleed
with content centered inside. Topbar 56px sticky, translucent with a hairline bottom.

**Surface rule (the boxes-within-boxes hard rule made mechanical):** a `border` + `radius` + `padding` combination is
permitted **only** on: data tables, code blocks, the explorer/visualize embeds, form composers, and modals. Everything
else separates with (a) a background tonal shift, (b) a 1px `--rule` hairline, or (c) whitespace. `Card` as a generic
container is deleted (§5). A bordered surface may never contain another bordered surface; chips inside tables are text
plus a dot, never bordered.

Radii: `4px` tools, `2px` chart elements, nothing larger. Elevation: none — no shadows anywhere except the sticky
topbar's hairline. Focus: `focus-within:` ring on wrappers only; inner `input`/`textarea` carry `outline:none` and no
`focus:border-*`, `focus:ring-*`, or box-shadow (global hard rule).

### 4.4 Figures, equations, honest nulls

Figures render full-content-width on `--bg-1` with the caption in small type below, left-aligned, no frame; clicking
opens the full-size asset. Equations get a `--bg-1` band with generous vertical space when they are a section's
subject. Charts: one accent line, `--ink-3` gridlines at 10% opacity, mono axis labels, no chart junk, no gradient
fills. Null results are typeset like any other result — same H3 weight, slate dot, a number and a receipt link — and
the copy states the null as a finding ("PTA channel: 14.3 dex below NANOGrav — closed as a null"), never as an absence.

## 5. Components

### 5.1 The minimal set (12)

Every page in §3 is buildable from these. Props are sketches, not final signatures.

| # | Component | Props | Used by |
|---|---|---|---|
| 1 | `Band` | `tone: 'base'\|'alt'\|'deep'`, `width: 'prose'\|'content'\|'full'`, `children` | every page — the layout primitive that replaces `Card` |
| 2 | `PageHeader` | `eyebrow?`, `title`, `lead?`, `meta?: MetaItem[]`, `actions?: LinkItem[]` | all top-level pages, paper pages |
| 3 | `StatRow` | `items: {value, label, href?, mono?}[]` | `/`, `/reproduce`, `/status`, explorers, `/reviews` |
| 4 | `EvidenceChip` | `grade: 'measured'\|'derived'\|'null'\|'open'`, `label?` | `/`, tracks, papers, status |
| 5 | `RowList` + `Row` | `items: {title, purpose, href, right?: ReactNode, chips?}[]` | tracks, works index fallback, learn/explore hubs, activity |
| 6 | `DataTable` | `columns`, `rows`, `dense?`, `stickyHeader?` — the **only** bordered list surface | `/papers`, `/status`, `/reproduce`, `/reviews`, `/docs/architecture`, surveys |
| 7 | `ReadinessBar` | `value: number` (Convex), `segments: {label, max, earned}[]` | `/status`, `/papers/[slug]` |
| 8 | `VerdictGrid` | `rounds` (newest-left), `works`, `activeLegs`, `frozenLegs` | `/reviews` |
| 9 | `TimelineList` | `entries: ReviewRound[]`, `kindMarkers` | `/reviews`, `/timeline`, `/activity` |
| 10 | `FigureBlock` | `src`, `caption`, `credit?`, `full?` | `/explore/figures`, `/papers/[slug]` |
| 11 | `MathText` | *(existing, unchanged API)* | tracks, papers, predictions, glossary |
| 12 | `Topbar` + `Footer` + `CommandSearch` | shell trio (`CommandSearch` = ⌘K over the existing search index) | `layout.tsx` |

Kept as-is behind these: `LegacyExplorerClient`, `DataExplorerClient`, `LiveStatus`, `ScrollToTop`,
`PublicationStatusWidget` (restyled, de-nested), `FreshnessStamp`, `PublicationPath`, `ExternalReviewPanel`
(restyled into `/papers/[slug]` §8), `SurveyQcTable` (moved under `/reproduce/surveys`).

### 5.2 Delete

- `site/src/components/Shell/Sidebar.tsx` — replaced by `Topbar` nav.
- `site/src/components/Cards/Badge.tsx` — dead; superseded by `EvidenceChip`.
- `site/src/components/Feed/FeedItem.tsx` — dead.
- `site/src/components/ui/accordion.tsx`, `scroll-area.tsx`, `skeleton.tsx`, `tooltip.tsx` — dead.
- `site/src/components/ui/card.tsx` — **deleted after migration**; generic cards violate the surface rule. Its 12
  importers move to `Band`/`RowList`/`DataTable`.
- `site/src/components/ui/badge.tsx` — deleted after migration to `EvidenceChip` (15 importers).
- `site/src/app/chat/**` and its nav entry — retired feature.
- `site/src/app/final-review/**` — merged into `/status#signoff`.
- `site/src/app/architecture/**` — moved to `/docs/architecture`.
- Page-local CSS that duplicates the token layer (`final-review.css`; audit `reviews.css`/`publish.css` and keep only
  genuinely page-specific rules).

`ui/button.tsx`, `ui/separator.tsx`, `ui/table.tsx`, `ui/tabs.tsx`, `ui/alert.tsx`, `ui/dialog.tsx` survive, restyled
to the tokens in §4.

## 6. Implementation plan — six Sonnet lanes

**Lane 1 is blocking; lanes 2–6 run in parallel after it lands.** No two lanes write the same file. Every lane is
Sonnet-tier (the spec names exact files, contracts, and checks); no lane nest-delegates, each commits per page,
edits stay ≤80 lines, and no lane arms a Monitor.

### Lane 1 — Foundation and shell *(blocking; must land first)*

Writes: `site/src/app/globals.css` (token layer §4.2–4.3, delete `.card`), `site/src/app/layout.tsx`,
`site/src/components/Shell/{Topbar,Footer,CommandSearch}.tsx`, `site/src/components/primitives/{Band,PageHeader,StatRow,EvidenceChip,RowList,DataTable}.tsx`,
`site/next.config.*` (all §2.4 301s: `/paper`→`/research`, `/contributions`→`/research#contributions`,
`/final-review`→`/status#signoff`, `/architecture`→`/docs/architecture`, `/figures`→`/explore/figures`,
`/surveys*`→`/reproduce/surveys*`, `/chat`→`/`). Deletes `Shell/Sidebar.tsx`, `Cards/Badge.tsx`, `Feed/FeedItem.tsx`,
`ui/{accordion,scroll-area,skeleton,tooltip}.tsx`.
Accept: `npx tsc --noEmit` clean; `npm run build` clean; every route still renders (temporary token-only restyle);
grep proves zero `focus:ring`/`focus:border`/`box-shadow` on any `input`/`textarea`; dark and light both painted from
tokens; no `Card` import remains in the shell.

### Lane 2 — Homepage + research tracks

Writes: `site/src/app/page.tsx`, `site/src/app/research/page.tsx`, `site/src/app/research/[track]/page.tsx`,
`site/src/data/tracks.ts` (new: track questions, lead results, channel tables, boundaries — sourced verbatim from
`VISION.md` + `PUBLICATION_ARCHITECTURE_RESET_2026-08-03.md`); deletes `site/src/app/paper/**` and
`site/src/app/contributions/**` after porting their content.
Accept: homepage passes the three ten-second reads (§1); nulls band present with ≥3 receipt links; every track row
carries a Convex readiness number via `lib/livePapers.ts`; zero bordered containers on `/` outside tables; no verdict
letter anywhere on `/` or `/research`.

### Lane 3 — Works index, paper template, figures, predictions

Writes: `site/src/app/papers/page.tsx`, `site/src/app/papers/[slug]/page.tsx`, `site/src/app/explore/page.tsx`,
`site/src/app/explore/figures/page.tsx`, `site/src/app/predictions/**`,
`site/src/components/primitives/FigureBlock.tsx`; deletes `site/src/app/figures/**`.
Accept: every row in `/papers` and every `/papers/[slug]` header shows a plain-English purpose line (Q3) — assert by
grep that no work renders without one; the string "6 papers"/"P1A · P1B · P2 · P3 · P4 · P5" appears nowhere under
`site/`; version/readiness/md5 come only from `lib/livePapers.ts`; the works table is the page's only bordered surface.

### Lane 4 — Status, reviews, activity, publishing

Writes: `site/src/app/status/page.tsx`, `site/src/app/reviews/page.tsx`, `site/src/app/reviews/[slug]/page.tsx`,
`site/src/app/activity/page.tsx`, `site/src/app/publish/page.tsx`,
`site/src/components/primitives/{ReadinessBar,VerdictGrid,TimelineList}.tsx`, restyles
`PublicationStatusWidget.tsx` + `ExternalReviewPanel.tsx`; deletes `site/src/app/final-review/**` and
`final-review.css`.
Accept: `reviewTimeline.ts` is **read-only** in this lane (schema byte-identical — `git diff --stat` shows no change);
verdict grid renders newest-left with active legs only and a visible "frozen leg, not counted" note; readiness values
trace to Convex; `/status` renders a stale annotation for any last-update >30 days; `bash tools/site_freshness_check.sh`
passes.

### Lane 5 — Reproduce hub, data sources, docs

Writes: `site/src/app/reproduce/page.tsx`, `site/src/app/reproduce/surveys/page.tsx`,
`site/src/app/reproduce/surveys/[slug]/page.tsx`, `site/src/app/docs/**` (absorbing the old architecture page content);
deletes `site/src/app/surveys/**` and `site/src/app/architecture/**`.
Accept: every manifest row shows inputs + external link, scripts, compute venue, est. cost, wall-clock (Q2); the
"0 of 8" survey number carries its explanatory sentence on screen; Releases & DOIs section lists Zenodo, HuggingFace,
B2 and GitHub targets for every work that has one; `/docs/architecture` reachable from `/docs` nav.

### Lane 6 — Learn cluster and explorer wrappers

Writes: `site/src/app/learn/page.tsx`, `site/src/app/explained/page.tsx`, `site/src/app/glossary/page.tsx`,
`site/src/app/timeline/page.tsx`, `site/src/app/articles/**`, `site/src/app/speculations/page.tsx`, and the wrapper
pages `site/src/app/{anomaly-explorer,galaxy-explorer,data-explorer,visualize}/page.tsx` **only**.
Accept: explorer tools render above their methodology prose; the four root `.html` files are untouched
(`git status` clean for them); glossary terms are anchor targets (`#term-slug`) and at least ten jargon strings
elsewhere on the site link into them.

### Gates before any push

1. `npx tsc --noEmit` and `npm run build` clean at repo `site/`.
2. `bash tools/site_freshness_check.sh` → PASS (banner, skills, board, versions).
3. Headed-browser QA per `/connect-chrome` across `/`, `/research`, `/research/track-a`, `/papers`,
   `/papers/[a3m]`, `/status`, `/reviews`, `/reproduce`, one explorer — light **and** dark, desktop and 375px.
4. Surface audit: DOM check for a bordered element inside a bordered element on `/papers`, `/status`, `/reproduce`.
5. `reviewTimeline.ts` diff is empty (or is an append made by the review pipeline, never by a redesign lane).
6. A `reviewTimeline.ts` `kind:"skill-improvement"` entry for the redesign lands in the same commit bundle as the
   final lane (standing review-round site-sync rule).

## 7. Risks and what must NOT change

### 7.1 Do not touch

| Asset | Why |
|---|---|
| Root `.html` explorers (`anomaly-explorer`, `galaxy-explorer`, `data-explorer`, `visualize`) | Canonical source of truth. Redesign the wrapper page only; content changes are edits to the `.html` itself in a separate, deliberate commit — never a wholesale replacement. |
| `convex/**` (24 modules) and the Convex deployment `brilliant-panther-471` | Backend is out of scope for the redesign. No schema edits, no mutations, no `npx convex deploy`. Readiness stays Convex-sourced (directive A). |
| `site/src/data/reviewTimeline.ts` | Append-only, written by the review pipeline every round. Consume the schema as-is; a redesign lane never edits or reformats it. |
| `site/src/data/live-status.ts` field names (`lastUpdatedISO`, per-paper versions) | `tools/site_freshness_check.sh` diffs these against Convex and blocks pushes on drift. Restyle the consumer, never rename the fields. |
| Existing PDF paths under `site/public/papers/**` | Served artifacts are md5-bound to Convex `paperVersions`; moving or renaming them breaks the three-way md5 check (directive G). |

### 7.2 Risks and mitigations

1. **Freshness gate breaks mid-redesign.** Any rename of `live-status.ts`/`reviewTimeline.ts` fields fails the
   pre-push hook. *Mitigation:* lanes 2–6 treat both files as read-only; gate #5 asserts an empty diff.
2. **Readiness drifts back into static files.** The most likely regression is a lane hard-coding "95" into a rebuilt
   page. *Mitigation:* acceptance greps for numeric readiness literals in `site/src/app/**`; all values come through
   `lib/livePapers.ts` / `lib/liveReadiness.ts`.
3. **Sidebar removal breaks deep-link discovery.** Twenty-seven routes collapsed behind six nav items can strand a
   page. *Mitigation:* every retired or moved route gets a 301 in lane 1; the footer carries the long tail; `⌘K`
   search indexes every surviving route.
4. **Card deletion cascade.** `ui/card.tsx` has 12 importers and `ui/badge.tsx` 15. *Mitigation:* the deletion happens
   only after lanes 2–6 land; lane 1 leaves both files in place and a final cleanup commit removes them once
   `grep -rl "ui/card\|ui/badge" site/src` is empty.
5. **Honest-but-alarming numbers get softened.** The redesign adds framing sentences to "0 of 8" and to two-month-old
   dates. *Mitigation:* framing may only add context, never change or hide a number; directive R6 governs — nulls
   stay nulls, stale dates stay visible.
6. **Explorer prose reordering hides a required caveat.** Moving methodology below the tool must not drop a
   disclosure. *Mitigation:* the "How this was made" section carries the caveat text verbatim; diff-check that no
   sentence is deleted, only relocated.
7. **Frozen reviewer legs get silently dropped from the grid.** *Mitigation:* directive M-AMENDED requires historical
   OpenAI/ChatGPT cells to remain displayed and annotated; lane 4 acceptance checks their presence.
8. **Two surfaces drift again.** The legacy static HTML under `/old` is archival and must not be re-synced; the
   dual-sync rule applies to the explorer `.html` files only.

---

*Spec complete. Implementation is authorized to begin with lane 1; lanes 2–6 fan out after it lands.*
