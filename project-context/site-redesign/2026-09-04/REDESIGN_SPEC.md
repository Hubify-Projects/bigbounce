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
