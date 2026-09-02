# Site reframe — 2026-09-02 (Track A/B/C restructure)

Executes `project-context/PORTFOLIO_DECISION_2026-09-02.md` §3 + Addendum and
`project-context/PAPER_LINEAGE_2026-08-05.md`'s 2026-09-02 decision record on
the live site: retires the "three research programs" framing in favor of
Track A (bounce vs. inflation, flagship) / Track B (the ECH Note, closed
line) / Track C (DESI data products, on-vision), and registers P1N and P4P.

## What changed, per surface

### `site/src/data/papers.ts`
- `researchPrograms` (feeds `/paper`, `/papers`, `/publish`) rewritten from
  `bounce-theory` / `desi-anomaly-discovery` / `galaxy-chirality` to
  `track-a-bounce-vs-inflation` / `track-b-ech-note` /
  `track-c-desi-data-products`. Track A carries A2 (transmission brief) and
  A3 (multi-channel, first pass done) as `supportingLinks` pointing at
  `research/cubic_bounce_transmission/` and `research/track_a3_multichannel/`
  since neither is a paper artifact yet.
- New `archivedInto` field on `Paper` (`{ note, successorSlug, zenodoDoi? }`),
  set on `paper-1a` (→ paper-1n, Zenodo 10.5281/zenodo.21481838), `paper-4`
  (→ paper-4p, Zenodo 10.5281/zenodo.21461899), `paper-5` (→ paper-4p, no
  independent DOI). Archived entries stay fully listed, never deleted.
- New full entries `paper-1n` (P1N, v1N.0.1, readiness 35 client-side
  display / Convex readinessCap 20) and `paper-4p` (P4P, v4P.0.1, same),
  with title/plainTitle/description/keyResults/artifacts sourced from
  `project-context/SSOT/paper-1n/status.md` and
  `project-context/SSOT/paper-4p/status.md`.

### `site/src/data/publish.ts`
- Headline, `decisions[]`, manuscript `rows[]`, and `publicationExecution`
  rewritten for the three tracks; P1N and P4′ rows added; P1A/P4/P5 rows
  relabeled "archived lineage."

### `site/src/app/papers/page.tsx`
- Flat list now renders an "Archived — see current version" line (with the
  successor link and Zenodo DOI when published) under any paper carrying
  `archivedInto`.

### Copy sweep
`page.tsx`, `paper/page.tsx`, `publish/page.tsx`, `Sidebar.tsx`: "research
programs" → "research tracks" throughout (nav label, page titles, hero copy).

### `site/src/data/live-status.ts`
Headline/summary rewritten for the restructure. `papers[]` now lists P1N and
P4P (readiness 20, "fresh draft, no review board run") alongside the
archived paper-1a/paper-4/paper-5 rows (so `tools/site_freshness_check.sh`'s
Convex-version-vs-live-status.ts cross-check stays green — every Convex
paper row appears somewhere on the concise status surface, archived or not).

### `site/src/data/reviewTimeline.ts` + `ReviewEntry.tsx`
- New `ReviewRoundKind: "restructure"` (badge label "DECISION"; new
  `KIND_GROUPS` entry in `ReviewEntry.tsx`).
- `RoundPaperId` widened with `"P1N" | "P4P"` (same pattern as the existing
  `P1U`/`P1C` additions — does not touch the six-paper historical
  verdict/gap `Record<PaperId, …>` matrices).
- Two new timeline entries (both dated 2026-09-02): the portfolio
  restructure itself (`kind: "restructure"`), and the R1 INT-only boards
  dispatched on P1N/P4P (`kind: "internal-api"`, verdicts recorded as
  PENDING — no verdict fabricated).

### Ledger #1 discrepancy
Not a site-copy item this session (owned by the concurrent A1/ledger lane —
see `de3e898a`/`8d08af2b` in git log): the independent second-method
derivation returned −55/16 vs. the paper's −35/16, so P2′ is gated pending
reconciliation. The Track A copy in `papers.ts`/`publish.ts` already states
this honestly ("amplitude under independent re-derivation" / "gated before
submission"), consistent with the concurrent lane's finding.

### P4 title figure (890,069 vs 949,584) — verified, no fix needed
`project-context/BACKUP_VERIFICATION_2026-09-02.md` flagged Convex's P4
title ("890,069 Quality-Controlled...") against Zenodo 21461899's title
("949,584 High-Confidence..."). Checked
`pipelines/p2_chirality/chirality_catalog_paper.tex` directly: 949,584 is
the pre-flip-QC high-confidence count; 890,069 is the current
quality-controlled primary-estimator count (59,515 unsafe rows excluded per
the raw/flip quarantine, `\S`3.something "Raw/flip quarantine"). The current
`.tex` title says 890,069 — Convex and the site are correct and current;
the Zenodo record (an earlier published version) is the stale one. No site
data change made; recorded here so it isn't re-flagged as a live-site bug.

## Convex writes (all via public HTTP API, no `npx convex deploy`)

| Mutation | Args (key fields) | Result id |
|---|---|---|
| `papers:upsert` | slug `paper-1n`, number `1N`, targetJournal `other`, status `active-drive-to-100`, texPath `arxiv/paper1bc_ech_note/main.tex`, sitePdfPath `/papers/paper1bc_ech_note_v1N.0.1.pdf` | `k97fadv694bq9cz69av5mvqx0d8dnpfv` |
| `papers:upsert` | slug `paper-4p`, number `4P`, targetJournal `other`, status `active-drive-to-100`, texPath `pipelines/p4prime_chirality_test/paper/main.tex`, sitePdfPath `/papers/paper4prime_chirality_test_v4P.0.1.pdf` | `k9775jv6vd5mvk3308h5acfge18dmrbv` |
| `papers:setReadinessCap` | `paper-1n`, cap 20 | — |
| `papers:setReadinessCap` | `paper-4p`, cap 20 | — |
| `paperVersions:bump` | `paper-1n` v1N.0.1, md5 `66423305a369626b7f3c71bbcc77b09c`, 6pp, 345050 bytes, texCommit `51d8af1b472412a9a52d86fb1bbe10988d327e0` | `k57caj2gabdq2hmwey1sd280vd8dnrq2` |
| `paperVersions:bump` | `paper-4p` v4P.0.1, md5 `d3e6f077ad5d772ed25d9f5d0b4c2140`, 6pp, 804904 bytes, texCommit `ac065a615c63208ad7d0b3b8af8e3c6928b009d6` | `k57cp2p5qc5jxc1wcfg0dtnx8n8dng10` |
| `activityFeed:add` × 4 | restructure decision, P1N registered, P4′ registered, R1 boards dispatched | `j577wvbd7n9jt7z3m1vy4pm0gn8dmy0e`, `j574pfg2kahh2h5wjjhvkm9jnh8dn089`, `j5712bxzh6m5nvmncp07xq8g1n8dmwxd`, `j576myfjekcnhjv91pe4873k618dmrvg` |

`papers:listAllPaperStates` (Hubify's parity-check query) verified to
already return both new rows with no code change — it iterates every
`papers` table row generically:

```
paper-1a 1A v1A.0.127  95.0
paper-1b 1B v2B.0.16   95.0
paper-1n 1N v1N.0.1    20.0
paper-2  2  v1.7.130   95.0
paper-3  3  v3.2.0-r17 95.0
paper-4  4  v1.0.274   95.0
paper-4p 4P v4P.0.1    20.0
paper-5  5  v0.1.147-2026-08-03 95.0
```

md5 mirror check (source PDF vs. both served mirrors) — byte-identical,
matches the Convex-recorded md5:

```
arxiv/paper1bc_ech_note/main.pdf                              66423305a369626b7f3c71bbcc77b09c
site/public/papers/paper1bc_ech_note_v1N.0.1.pdf               66423305a369626b7f3c71bbcc77b09c
public/papers/paper1bc_ech_note_v1N.0.1.pdf                    66423305a369626b7f3c71bbcc77b09c
pipelines/p4prime_chirality_test/paper/main.pdf                d3e6f077ad5d772ed25d9f5d0b4c2140
site/public/papers/paper4prime_chirality_test_v4P.0.1.pdf      d3e6f077ad5d772ed25d9f5d0b4c2140
public/papers/paper4prime_chirality_test_v4P.0.1.pdf           d3e6f077ad5d772ed25d9f5d0b4c2140
```

## Build, deploy, freshness gate

- `npm run build` (site/) passes clean. Along the way, fixed pre-existing
  TypeScript drift in `site/scripts/sync-repro-manifests.mjs` (widened
  `ReproExperiment`/`ReproInput`/`ReproOutput`/`ReproStatus` types) that was
  blocking the build — the concurrent Track A2/A3 lane's committed
  reproducibility manifests (`open_items`, `used_for`, `"reproduced"`
  status, `"external-literature"` input type, free-form program/paper ids)
  used fields/values the schema hadn't caught up to yet.
- `tools/site_freshness_check.sh` — first run FAILED (paper-1a/4/5 dropped
  from `live-status.ts`'s Convex-version cross-check); fixed by re-adding
  them as archived rows; second run PASS, pre-push hook let the push through
  cleanly (no `FRESHNESS_SKIP` override used).
- Pushed to `origin main` (`Hubify-Projects/bigbounce`, canonical remote):
  commits `6b1977e4`, `9a3ea7d4`, `1ee15184`, `56b58bb2`. Vercel auto-deploys
  on push to `main` — no manual `vercel` invocation needed or made.
- Deploy verification and browser QA: see below / follow-up note if this
  file is read before the deploy-verification step completes.

## Commits (bisected)

1. `6b1977e4` — `feat(site): reframe portfolio to Track A/B/C, register P1N and P4P`
2. `9a3ea7d4` — `fix(site): widen reproducibility-manifest types for Track A2/A3 drift`
3. `1ee15184` — `feat(site): live-status + review timeline for the Track A/B/C restructure`
4. `56b58bb2` — `fix(site): live-status.ts carries every Convex paper, archived rows included`

## Open / not done this session

- No INT/EXT review board content was authored by this lane (a concurrent
  lane already dispatched R1 — see `ea1da739`, `34758d31` in git log); this
  lane only recorded the dispatch on the review timeline.
- `tools/skills_autolog.sh` flagged 5 unlogged skill/process improvements
  since 2026-08-28 (WARN, non-blocking) — not run this session; a
  housekeeping follow-up.
- Screenshots: see `project-context/site-qa/2026-09-02/` for browser-QA
  captures (overview, /papers, /paper tracks page, /reviews, paper-1n,
  paper-4p, /reproduce).

## Browser QA (headed, this session, post-deploy)

Deploy verified live at bigbounce.hubify.app (Vercel auto-deploy from
`origin main` push; a "Vercel Security Checkpoint" JS challenge gates the
first hit per browser session — expected, passes automatically after ~4s;
plain `curl` without a browser session sees it as 403, which is not a site
defect).

- **Overview (`/`)**: Track A/B/C copy live, sidebar reads "research tracks".
- **`/papers`** (flat list): P1N and P4′ render as LEAD entries under their
  track badges; P1A/P4/P5 render with the new "Archived — see current
  version" note, successor link, and Zenodo DOI link where published.
  Found and fixed one stale copy miss: the page's own "See research
  programs" link text hadn't been swept in the earlier commit — now "See
  research tracks".
- **`/paper`** (tracks page): Track A/B/C sections render with question /
  result / boundary; A2 and A3 render as supportingLinks under Track A
  with their "research brief in progress" / "first pass done" labels; no
  nested-box clutter.
- **`/papers/paper-1n`** and **`/papers/paper-4p`**: render live from Convex
  (20% readiness, LIVE badge, correct md5/page-count/artifact panel). Both
  PDFs (`paper1bc_ech_note_v1N.0.1.pdf`, `paper4prime_chirality_test_v4P.0.1.pdf`)
  open correctly in-browser.
- **`/reviews`**: found and fixed a stale hardcoded intro block and a stale
  readiness-average table row, both still asserting the retired "six
  candidate packages / five standalone manuscripts / P3 support" framing;
  now names P1N/P4′ as fresh Track B/C1 drafts and P1A/P4/P5 as archived
  lineage, with their readiness caps included. The `ProgressViz` verdict
  grid (P1A/P1B/P2/P3/P4/P5 columns) was deliberately left untouched — it
  is historical review-round data for those exact papers, not stale copy;
  restructuring its `PaperId` type to add P1N/P4P columns would touch
  hundreds of dated historical entries and was out of scope for this pass.
- **`/reproduce`**: loads clean (3 programs, 52 experiment manifests, 41
  runnable now, $36.04 total) — confirms the `sync-repro-manifests.mjs`
  type-widening fix works at runtime, not just at build time, against the
  concurrent Track A2/A3 lane's newly committed manifests.
- Console: two transient 403s observed during PDF-tab navigation, tied to
  the Vercel bot-checkpoint token on a fresh navigation context, not a page
  or asset defect — no 403 on any same-session in-app navigation.
- Sitewide copy sweep for the retired "research program(s)" phrase: fixed
  remaining stale instances in `status/page.tsx` (stat tile + body text),
  `timeline/page.tsx` (hero desc), `docs/DocsClient.tsx`, `search/SearchClient.tsx`,
  `chat/page.tsx`. Left generic singular uses ("the BigBounce research
  program" meaning "the lab") alone — those aren't claims about program
  count/structure and reads correctly either way.

## Correction to the earlier live-status.ts push

The first push attempt included a version of `live-status.ts` that had
dropped paper-1a/paper-4/paper-5 entirely (not just re-labeled); the
pre-push `site_freshness_check.sh` gate caught this (STALE — Convex versions
not represented) and blocked the push before anything reached origin. Fixed
by re-adding those three as explicit archived rows (see commit `56b58bb2`)
before any push succeeded. No `FRESHNESS_SKIP` override was used at any
point.

## Newer drafts in flight — not registered this session

While this session was running, a concurrent closure lane started producing
v1N.0.2 and v4P.0.2 (`pipelines/p4prime_chirality_test/paper/main.tex`
already shows `\paperVersion{v4P.0.2}` as an **uncommitted** working-tree
edit; `arxiv/paper1bc_ech_note/main.tex` is still at v1N.0.1 with no pending
edit as of this check). Per instruction, this session registers only what
exists committed on disk — v1N.0.1 and v4P.0.1, exactly what is in Convex
and on the live site right now. The v4P.0.2 bump (and any v1N.0.2 that
lands) is the next `paperVersions:bump` + site-data update, owned by
whichever lane closes it.
