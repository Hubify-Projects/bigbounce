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
--ink:#ece7dd  --ink-2:#b6ae a1→#b6aea1  --ink-3:#877f73  --rule:#372f26
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
