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

## v4P.0.2 + v1N.0.2 sync (later same-day, follow-up pass)

Both bumps landed and were synced in one pass by a Sonnet site worker.

**P4′ v4P.0.2** — commit `0b3cfaba`, PDF at
`pipelines/p4prime_chirality_test/paper/main.pdf`, md5
`413705f8cf6ce69da4fe6744b3014ea2`, 10 pp, 1051506 bytes. Convex
`paperVersions:bump` (`k5741xaqq5p0dsg371t7pxtfgd8dm89v`) and
`activityFeed:add` already existed from the closure lane. R1 board closed;
R2 board (Grok/Gemini/Claude) dispatched — verdicts pending, never faked.

**P1N v1N.0.2** — landed mid-session (coordinator commit `82bb7752`): R1
board (Claude INT major-revisions, Grok API REJECT, Gemini API REJECT,
Perplexity absent/401) audited 42 finding-rows, closed 19 canonical real
items (R1-R19) via real edits — restored on-shell branch splits, single-
normalization statements, explicit operator definitions/derivations,
γ-scoped Popławski identification, pruned `references.bib` 113→26. Venue
form grown from Note to Paper (7725 words / 10 pp, above the CQG Note
ceiling). PDF: `arxiv/paper1bc_ech_note/main.pdf`, md5
`5f41629b370a55991a4c25937925a281`, 10 pp, 402962 bytes. Convex
`paperVersions:bump` was written twice — once by this session before the
coordinator's "don't repeat it" note landed (`k574x3rb8b40tz3myd6qs3cke98dmkkr`)
and once by the coordinator's own closure lane — both carry identical
version/md5/page data, so the duplicate is a harmless extra version-history
row, not a data conflict. R2 board dispatched — verdicts pending.

**Static mirrors updated** (`site/src/data/papers.ts`, `live-status.ts`,
`reviewTimeline.ts`, `site/src/lib/reproLab.ts`): version/pages/md5/pdfMeta/
href/tldr/remainingWork/changelog bumped for both papers; `paper-1n` target
field updated to "CQG — Paper (grown from Note form...)"; two new
`internal-api` timeline entries recording each R1-closure-to-R2-dispatch
transition (verdicts PENDING, none fabricated); `reproLab.ts`
`PAPER_CODE_TO_SLUG` extended with `P1N -> paper-1n`, `P4P -> paper-4p`
(A2/A3 left unmapped by design — no standalone paper page, falls through to
`null` same as the pre-existing "none" behavior).

**Build/deploy:** `npm run build` + `npx tsc --noEmit` both clean (two
passes — a second small fix landed after the first push). Pushed to
`origin main` and `upstream main`: commits `8b097bcb` (main site-data +
reproLab bundle), `30fc87de` (P1N tldr wording fix). `tools/
site_freshness_check.sh` pre-push hook PASSed on every push, no
`FRESHNESS_SKIP` used.

**Live verification** (headed browser session, since plain `curl` always
hits the Vercel Security Checkpoint page regardless of deploy state — a
known false negative, not a site defect): `/papers/paper-4p` renders
`V4P.0.2 · LIVE`, 10 pages, target "APJS..."; `/papers/paper-1n` renders
`V1N.0.2 · LIVE`, 10 pages, target "Classical and Quantum Gravity —
Paper...". `fetch()` from the live page's own origin against both PDF URLs
returned `200` with byte counts matching the source files exactly
(`paper4prime_chirality_test_v4P.0.2.pdf` = 1051506 bytes;
`paper1bc_ech_note_v1N.0.2.pdf` = 402962 bytes) — browser `SubtleCrypto`
has no MD5 digest, so byte-count match plus the earlier three-way
byte-identical local mirror check (source/`site/public/papers/`/
`public/papers/`) stands in for a live md5 check.

**Not done this pass:** `site/src/data/repro.ts` was left dirty in the
working tree on arrival (25 changed lines, not authored by this pass) and
was deliberately left uncommitted — it belongs to a concurrent lane and its
content wasn't inspected beyond `git diff --stat`.

## P2L registration (later same-day pass)

Registered the P2′ Letter (`P2L` in `project-context/draft_paper_registry.json`,
already committed by the concurrent A1/ledger lane at `6d4faded`): source
`arxiv/paper2prime_fnl_letter/main.tex` v2L.0.1, PDF md5
`66a28438cc0f0b8dc347a3016389363f`, 4 pp, served at
`site/public/papers/paper2prime_fnl_letter_v2L.0.1.pdf` (also
`public/papers/`) — verified byte-identical to
`arxiv/paper2prime_fnl_letter/main.pdf` (343174 bytes) before touching site
data.

**Site data (this session):** `site/src/data/papers.ts` — new `paper-2l`
entry (slug `paper-2l`, readiness 20) plus `archivedInto` on `paper-2`
(successor `paper-2l`, Zenodo DOI `10.5281/zenodo.21461881`); Track A's
`leadSlug` moved `paper-2` → `paper-2l` and its `result`/`limitation` copy
rewritten to state the ledger-#1 closure honestly ("confirmed by an
independent from-scratch in-in computation; Cai et al. 2009's −35/8 located
as a uniform factor 2"). `site/src/data/live-status.ts` — `paper-2` row
relabeled archived, new `paper-2l` row added. `site/src/data/publish.ts` —
A1 row updated to point at `/papers/paper-2l` with drafted/dispatched
status. `site/src/data/reviewTimeline.ts` — `RoundPaperId` widened with
`"P2L"`; two new entries: ledger #1 closure + P2′ R1 dispatch
(`ledger1-closed-p2l-r1-dispatch-2026-09-02`), and the P1N/P4P R2
Claude-leg major-revisions verdicts (`p1n-p4p-r2-claude-legs-2026-09-02`,
7M/13m and 3M/13m; Grok/Gemini pending, never faked).
`site/src/lib/reproLab.ts` — `PAPER_CODE_TO_SLUG` extended with
`P2L -> paper-2l`.

**Convex writes** (public HTTP API, no `npx convex deploy`): `papers:upsert`
(slug `paper-2l`, number `2L`, targetJournal `PRD`, status
`active-drive-to-100`, texPath `arxiv/paper2prime_fnl_letter/main.tex`,
sitePdfPath `/papers/paper2prime_fnl_letter_v2L.0.1.pdf`) →
`k976bfne5zr72w0aqaper6wkc58dmknc`; `papers:setReadinessCap` (`paper-2l`,
cap 20); `paperVersions:bump` (`paper-2l` v2L.0.1, md5
`66a28438cc0f0b8dc347a3016389363f`, 4 pp, 343174 bytes, texCommit
`6d4fadedd787556a268d8f69a1c0e7f0f595ac53`) →
`k577nt8c2c95d5nnzeg6yta7xs8dnvpr`; `activityFeed:add` × 2 (ledger #1
closure + P2′ drafted/dispatched → `j574yvwmqk13nvd80a3dqx1p4d8dmp4g`; P1N/P4P
R2 Claude-leg verdicts → `j578zgbje5n2avhjfjbcs6d2ax8dnpzv`).

**Build/deploy/freshness:** `npx tsc --noEmit` clean; `npm run build`
clean, 9 static paper pages generated including `/papers/paper-2l`.
`tools/site_freshness_check.sh` PASS (no `FRESHNESS_SKIP`) both before and
as the pre-push hook. Committed `f676559c` (`chore(site): register P2′
Letter v2L.0.1; timeline for ledger #1 closure and R2 boards`), pushed to
`origin main` and `upstream main` cleanly (`ae8715c3..f676559c`).

**Live verification** (headed browser, post-deploy — Vercel took ~4-5 min
to finish the build queued behind concurrent-lane deploys): `/papers/paper-2l`
renders `V2L.0.1 · LIVE`, readiness 20%, target "PRD Letters (JCAP
alternate)", correct md5/page-count/focus-areas from Convex. `fetch()` from
the live page's own origin against
`/papers/paper2prime_fnl_letter_v2L.0.1.pdf` returned `200` with 343174
bytes, matching the source PDF exactly.

## v1N.0.3 + v4P.0.3 site sync (later same-day pass, Sonnet worker)

Picked up a partial edit killed mid-turn by a usage limit (`site/src/data/papers.ts`
was already correctly updated for both papers — reviewed and kept as-is) and
finished the remaining surfaces.

**P1N v1N.0.3** — R2 board closed (Claude major-revisions, Grok reject,
Gemini major-revisions), 23/23 findings closed incl. two errors inherited
from P1C (8π coefficient, O5 parity). PDF `arxiv/paper1bc_ech_note/main.pdf`,
11 pp, 433339 bytes, md5 `8725f40c69027c53c7a0f6a38f05587d` — verified
byte-identical across source / `site/public/papers/` / `public/papers/`
before touching site data. Convex row `k57cjc4y022k16m92vy3nae80n8dmgqv`,
source commit `453d663e` (already done, not repeated).

**P4′ v4P.0.3** — R2 board closed (same verdict pattern), 21/21 findings
closed; monopole term disclosed; genuine 95% CL limit ≈0.75% by Neyman
inversion. PDF `pipelines/p4prime_chirality_test/paper/main.pdf`, 11 pp,
1089951 bytes, md5 `cb7429779c820f03daf125a49b395ec5` — same three-way
byte-identical mirror check. Convex row `k578hqea3a00ddg6qf4gr0f0y18dnze3`,
source commit `a47ca061` (already done, not repeated).

**Site data updated this pass:** `site/src/data/live-status.ts` (version +
pendingWork for both rows) and `site/src/data/reviewTimeline.ts` (two new
`internal-api` entries, R2-closed-and-R3-dispatched, honest R2 verdict
cells: Claude major-revisions / Grok reject / Gemini major-revisions on
both papers). `site/src/data/repro.ts` regenerated via
`sync-repro-manifests.mjs` (61 experiments, 3 programs) rather than
hand-edited, since it was already dirty in the working tree from a
concurrent lane.

**Commit:** `dbb7caf1` — `feat(site): sync v1N.0.3 + v4P.0.3 R2 closures to
site data` (papers.ts, live-status.ts, reviewTimeline.ts, repro.ts — site
data committed first, before build/deploy, per protocol).

**Build/deploy:** `npx tsc --noEmit` clean; `npm run build` clean (all
routes prerendered, including `/papers/paper-1n` and `/papers/paper-4p`
SSG paths). `tools/site_freshness_check.sh` PASS pre-push (no
`FRESHNESS_SKIP`). Pushed to `origin main` and `upstream main` at
`dbb7caf1`; Vercel auto-deployed.

**Live verification (headed browser, post-deploy):**
- `/papers/paper-1n` renders `V1N.0.3 · LIVE`, 11 pp, tldr/pdfMeta/changelog
  all match the R2-closure wording above.
- `/papers/paper-4p` renders `V4P.0.3 · LIVE`, 11 pp, same pattern.
- In-page `fetch()` against both PDF URLs from the live origin: both
  return `200` with byte counts exactly matching the local source files
  (`paper1bc_ech_note_v1N.0.3.pdf` = 433339 bytes;
  `paper4prime_chirality_test_v4P.0.3.pdf` = 1089951 bytes). Plain `curl`
  hits the Vercel Security Checkpoint (expected false negative, not a
  defect — same as every prior pass this session).
- `tools/site_freshness_check.sh` PASS again post-deploy (re-run after the
  push, all surfaces FRESH except the pre-existing non-blocking
  `skillslog` WARN, unrelated to this pass).

**Not touched this pass:** `research/bh_universe_dipole/a95_upper_limit_2026_09_02.json`
(modified) and `project-context/peer-reviews/INT_v3/ROUND_2026-09-02-P1N-v1N.0.3-EXACTPDF-c758664b-R3VERIFY/`
(untracked) were present in the working tree on arrival — both belong to
the concurrent R3-verification lane and were left alone.

## v4P.0.4 + v2L.0.2 site sync (later same-day pass, Sonnet worker)

Picked up after Convex bumps were already done by a prior lane (paperVersions
row `k576j98mgmh32egg4rme7xe7jh8dmnp0` for v4P.0.4, `k57bzqv0fyydrm23byqyqpjw218dny02`
for v2L.0.2) and PDF mirrors already byte-identical
(`pipelines/p4prime_chirality_test/paper/main.pdf` md5 `ed6b8f661b407e6845cb5d42c3efd8d2`,
11pp; `arxiv/paper2prime_fnl_letter/main.pdf` md5 `718521c10032511339b334ff6f277629`,
4pp — verified across source / `site/public/papers/` / `public/papers/` before
touching site data).

**P4′ v4P.0.4** — R3 verification pass closed: Claude minor-revisions, Grok
reject, Gemini minor-revisions; automated review convergence criterion met
(directive P — 0 genuinely-new real findings across active legs); final
author review recorded APPROVE. Readiness cap set to 95 (100 requires
Houston's explicit per-paper sign-off, tracked separately per directive P).
arXiv tarball `SSOT/arxiv_tarballs/paper4prime_chirality_test_arxiv_v4P.0.4.tar.gz`
verified sha256 `db108413…` on disk before referencing it in site copy.

**P2′ v2L.0.2** — R1 board (Fable major-revisions, Grok reject, Gemini
major-revisions) truth-audited; per the recorded scope decision
(`project-context/SSOT/paper-2l/status.md` + the 2026-09-02 evening decision
record in `PAPER_LINEAGE_2026-08-05.md`), the Letter is archived as a theory
record rather than closed round-by-round — its content (exact matter-
contraction amplitude, ledger-#1 independent re-derivation, orientation-
dependent squeezed limit, δN cross-check) is folded into Track A's A3
multi-channel paper. Title updated to "An independent confirmation of
f_NL = −35/16 for matter-dominated contraction" per the decision record's
stated NEW CLAIM; `statusVariant` set to `blue` (archived, not amber/active).

**Site data updated this pass:** `site/src/data/papers.ts` (both paper
blocks: version/readiness/pages/pdfMeta/changelog/artifacts hrefs/title),
`site/src/data/live-status.ts` (both rows), `site/src/data/publish.ts` (P2′
and P4′ rows relabeled), `site/src/data/reviewTimeline.ts` (two new
`internal-api` entries, newest-first: P4′ R3-converged and P2′ R1-fold-
into-A3). `/reviews`' readiness-cap sentence and verdict-trajectory `cap()`
calls read live from `papers.ts`, so no separate hardcoded readiness mirror
needed editing there.

**Commit:** `42c12dd6` — `feat(site): sync v4P.0.4 + v2L.0.2 to site data`
(papers.ts, live-status.ts, publish.ts, reviewTimeline.ts — site data
committed first, before build/deploy, per protocol).

**Build/deploy:** `npx tsc --noEmit` clean; `npm run build` clean, all
static paper pages generated including `/papers/paper-4p` and
`/papers/paper-2l`. `tools/site_freshness_check.sh` PASS (no
`FRESHNESS_SKIP`) pre-push. Pushed to `origin main` and `upstream main` at
`42c12dd6` cleanly; Vercel auto-deployed (took a few minutes to propagate —
an early post-push check saw stale `Paper Artifacts` panel text (v4P.0.3)
while the version chip already showed v4P.0.4, resolved once the deploy
fully propagated; confirmed the local `.next` build output was already
correct throughout, ruling out a data bug).

**Live verification (headed browser, post-deploy):**
- `/papers/paper-4p` renders `V4P.0.4 · LIVE`, readiness 95%, 11 pp, correct
  md5/changelog/artifact hrefs.
- `/papers/paper-2l` renders `V2L.0.2 · LIVE`, readiness 20%, 4 pp, new title
  "An Independent Confirmation of f_NL = −35/16 for Matter-Dominated
  Contraction", archived-theory-record copy.
- In-page `fetch()` against both PDF URLs from the live origin: both
  `200`, byte counts exactly matching local source files
  (`paper4prime_chirality_test_v4P.0.4.pdf` = 1091040 bytes;
  `paper2prime_fnl_letter_v2L.0.2.pdf` = 347144 bytes).
- `/reviews` renders both new timeline entries ("P4′ R3 verification…" and
  the P2′ R1 fold-into-A3 entry) and the readiness-cap sentence correctly
  states P4′ 95.
- `tools/site_freshness_check.sh` PASS again post-deploy (all FRESH except
  the pre-existing non-blocking `skillslog` WARN, unrelated to this pass).

## v1N.0.4 site sync + A3 multi-channel paper registration (later same-day pass)

**P1N v1N.0.4** — Convex `paperVersions:bump` was already done by a prior
lane (row `k572az66fecayyv0p8zc3b941x8dn9pa`, readiness cap already set to
95); this pass only synced static site data. Source PDF
`arxiv/paper1bc_ech_note/main.pdf`, 12 pp, md5 `dcdeb0e1326fd3ef5b396e7d84a60d28`.
The working tree had an uncommitted concurrent-lane edit to that file
(same size, different bytes, md5 `7aa6aa6750eb69605c8c908c6f77b6c1`) at the
time of this pass — rather than mirror the dirty working copy, the committed
version at HEAD `af204341` (`fix(P1N): R3 final closure (v1N.0.4)…`) was
extracted via `git show af204341:arxiv/paper1bc_ech_note/main.pdf` and
verified byte-identical to the target md5 before mirroring to
`site/public/papers/paper1bc_ech_note_v1N.0.4.pdf` and
`public/papers/paper1bc_ech_note_v1N.0.4.pdf`. arXiv tarball
`project-context/SSOT/arxiv_tarballs/paper1bc_ech_note_arxiv_v1N.0.4.tar.gz`
confirmed on disk, sha256 `67eac4358d4e475c6005ef9437d1a9471655e262ffd03fffd15fe84f21fce3cb`
(full hash computed via `shasum -a 256`, not truncated/invented).
`site/src/data/papers.ts` updated: version v1N.0.4, readiness 95 with a
directive-P composition note (95 = science + evidence + review convergence +
packaging; 100 requires Houston's explicit per-paper sign-off, tracked
separately), target "Classical and Quantum Gravity — Paper", tarball path +
sha256 referenced in `remainingWork`. `live-status.ts` and `publish.ts` also
synced to v1N.0.4 / readiness 95. `reviewTimeline.ts` gained one new
`internal-api` entry for the R3 verification closure (Claude major-revisions
/ Grok reject / Gemini major-revisions, machine-checked regressions,
automated review converged, final author review APPROVE).

**A3M registration** — new paper `paper-a3m` registered as Track A's
flagship submission candidate (folds the A3 multi-channel skeleton — NANOGrav
15-yr free-spectrum γ, PBH abundance, SPHEREx/MegaMapper reach — together
with the P2′ v2L.0.2 exact-amplitude theory, per
`PAPER_LINEAGE_2026-08-05.md`'s 2026-09-02 decision record). Source
`research/track_a3_multichannel/paper/main.tex` v3M.0.2, git commit
`0f6cf5b8` confirmed present in history (`fix(a3m): ledger #1 stated as
closed; v3M.0.2`). PDF `research/track_a3_multichannel/paper/main.pdf`
already compiled on disk (not built fresh this pass) — md5
`8f17a2dc877c0b58982e91a8dea0fa1b`, 6 pp, 402039 bytes (via `pdfinfo`);
mirrored byte-identical to `site/public/papers/a3_multichannel_arxiv_v3M.0.2.pdf`
and `public/papers/a3_multichannel_arxiv_v3M.0.2.pdf`. Slug `paper-a3m`.
Status: draft, note "PBH compaction-function row pending; one INT board
pending." The Track A `researchProgram` entry in `papers.ts` was updated:
A3's `supportingLinks` entry was promoted to a full `paper-a3m` in
`supportSlugs`, and `result`/`limitation`/`status` copy rewritten to state
A3 is now the flagship submission candidate in draft.

**Convex writes** (public HTTP API, no `npx convex deploy`): `papers:upsert`
(slug `paper-a3m`, number `A3`, targetJournal `PRD`, status
`active-drive-to-100`, texPath `research/track_a3_multichannel/paper/main.tex`,
sitePdfPath `/papers/a3_multichannel_arxiv_v3M.0.2.pdf`, readinessCap 20) →
`k9796y9efabw41ckngfjy74mk18dny9q`; `paperVersions:bump` (paperSlug
`paper-a3m`, version `v3M.0.2`, datestamp `2026-09-02`, pdfMd5
`8f17a2dc877c0b58982e91a8dea0fa1b`, pdfPages 6, pdfSizeBytes 402039,
texCommit `0f6cf5b8`) → `k574k79vc7ncnd71h2408qtt7x8dnt7v`;
`papers:setReadinessCap` (slug `paper-a3m`, cap 20) → success (note: the
mutation args required `paperSlug`/`slug` field names, not `paperId`, as
initially assumed from the SITE_REFRAME doc's summary table — corrected
after one validation error on each call, no bad data written);
`activityFeed:add` (A3 registration announcement) →
`j57cpmx1ksz0d9y0ecw9khgrhs8dm0a9`.

**Static mirrors updated:** `site/src/data/papers.ts` (new `paper-a3m` full
entry; Track A `researchProgram` rewritten), `live-status.ts` (new
`paper-a3m` row), `publish.ts` (new A3 row, Track A decision text rewritten),
`reviewTimeline.ts` (`RoundPaperId` widened with `"A3"`; one new
`restructure`-kind entry for the registration), `reproLab.ts`
(`PAPER_CODE_TO_SLUG` extended with both `A3M -> paper-a3m` and
`A3 -> paper-a3m`), `project-context/draft_paper_registry.json` (new `A3M`
entry matching the `P2L` entry's schema).

**Build/deploy:** `npx tsc --noEmit` clean; `npm run build` clean —
confirmed `.next/server/app/papers/paper-a3m.html` generated. Commit
`7d00b0b6` — `feat(site): sync P1N v1N.0.4 + register A3 multi-channel paper
(paper-a3m v3M.0.2)` (papers.ts, live-status.ts, publish.ts,
reviewTimeline.ts, reproLab.ts, draft_paper_registry.json — the two PDF
pairs staged identically but produced no diff since a concurrent lane
(`af204341`) had already committed byte-identical copies at those exact
paths). `tools/site_freshness_check.sh` PASS (10 paper blocks fresh,
version chip == pdfMeta == href for all; only the pre-existing non-blocking
`skillslog` WARN). Pushed to `origin main` and `upstream main` — both
already at the pushed commit (`Everything up-to-date`, a concurrent lane's
own push had already carried it to both remotes) at `a2537563` (one commit
ahead of `7d00b0b6`, from a concurrent ledger-#3 lane).

**Live verification (2026-09-02, ~15:5x PT):**
- `curl -sI` / `-w '%{http_code} %{size_download}'`:
  `https://bigbounce.hubify.app/papers/paper1bc_ech_note_v1N.0.4.pdf` → 200,
  434323 bytes (matches source exactly);
  `https://bigbounce.hubify.app/papers/a3_multichannel_arxiv_v3M.0.2.pdf` →
  200, 402039 bytes (matches source exactly).
- `/papers/paper-1n` rendered HTML contains `v1N.0.4`.
- `/papers/paper-a3m` initially 404 (deploy still propagating); polled via
  Monitor until 200, then confirmed rendered HTML contains `v3M.0.2` and
  "Multi-Channel Consistency".
- `/reviews` rendered HTML contains both `A3 multi-channel` / `paper-a3m`
  and `v1N.0.4`.
- `/paper` (tracks page) rendered HTML contains "paper-a3m" and "flagship
  submission candidate", confirming the Track A copy rewrite is live.
- `tools/site_freshness_check.sh` PASS, run again after push (same result
  as pre-push).

**Not fabricated / explicitly flagged:** none — the tarball sha256, A3M PDF
md5/pages/bytes, and the `0f6cf5b8` commit SHA were all confirmed present on
disk / in git history before use; no value was invented or truncated.

## Receipt — P4P v4P.0.5 / P1N v1N.0.5 / A3M v3M.0.3 site sync (Sonnet worker, this session)

Convex bumps were already done by a prior lane; this session's scope was the
site-data + SSOT-doc propagation, build/deploy, and live verification.

- **Source PDFs confirmed at target versions** (byte-identical across source +
  both mirrors, verified by `md5`):
  - `pipelines/p4prime_chirality_test/paper/main.pdf` v4P.0.5,
    md5 `f0d874e93cebf95f86e408f780f002e0`
  - `arxiv/paper1bc_ech_note/main.pdf` v1N.0.5,
    md5 `6836eb995effef298cca6830b1beda7c`
  - `research/track_a3_multichannel/paper/main.pdf` v3M.0.3,
    md5 `9f7afea9e22a7816168fc7638fc8a753`
  - All three already mirrored byte-identical at
    `site/public/papers/` and `public/papers/` (pre-existing from the
    concurrent lane; verified, not re-copied).
- **Tarball sha256 (verified against SSOT):**
  `paper4prime_chirality_test_arxiv_v4P.0.5.tar.gz` =
  `fbab03801b63483b86006095a3f86d0e4511f64766b90649a76548583fd51c92`;
  `paper1bc_ech_note_arxiv_v1N.0.5.tar.gz` =
  `26f215d635b2e577c32b7869a5129681109b601250fa054c90ba7c817659a33a`.
- **Site data updated:** `site/src/data/papers.ts` (version/pdfMeta/changelog/
  artifacts hrefs for paper-4p, paper-1n, paper-a3m), `live-status.ts`
  (version + pendingWork for the three), `publish.ts` (rows for A3/P1N/P4′),
  `reviewTimeline.ts` (two new 2026-09-02 entries: A3 PBH compaction-function
  integration + R1 dispatch (`kind: "restructure"`), and the P4′/ECH-Note
  abstract-cap REVISE (`kind: "skill-improvement"`)).
- **SSOT doc updated:** `project-context/SSOT/FINAL_REVIEW_RECOMMENDATIONS_2026-09-02.md`
  — P4′ and ECH Note section headers, packaging lines (version/sha256/md5),
  and a `REVISE (abstract cap) executed 2026-09-02` line added to each.
- **Build + typecheck:** `npm run build` in `site/` — compiled clean,
  TypeScript finished with no errors, 65 static pages generated.
- **Freshness gate:** `tools/site_freshness_check.sh` — PASS (no
  `FRESHNESS_SKIP`); only WARN was the pre-existing non-blocking
  `skillslog` backlog notice (unrelated to this bundle).
- **Commit:** `4dec27d3` — `feat(site): version bumps P4P v4P.0.5, P1N
  v1N.0.5, A3M v3M.0.3` (5 files: the four site-data files +
  `FINAL_REVIEW_RECOMMENDATIONS_2026-09-02.md`). Only these explicit paths
  were staged — other concurrent-lane changes in the working tree were left
  untouched.
- **Push:** `origin main` `eada7433..26412f83` and `upstream main`
  `ea374119..26412f83`, both with the pre-push freshness hook reporting
  `OVERALL: PASS`.
- **Deploy verification (live, post-propagation):**
  - PDFs: all three return HTTP 200 with `content-length` matching the
    source byte counts exactly (1,090,759 / 433,652 / 501,468 bytes for
    P4′/P1N/A3M respectively).
  - Paper pages (`/papers/paper-4p`, `/papers/paper-1n`, `/papers/paper-a3m`)
    render the new version/md5/status strings live: `v4P.0.5 ·
    f0d874e93cebf95f86e408f780f002e0`, `v1N.0.5 ·
    6836eb995effef298cca6830b1beda7c`, `v3M.0.3 ·
    9f7afea9e22a7816168fc7638fc8a753` — each with the correct "REVISE
    (abstract cap) executed" / "R1 INT board running" copy.
  - Propagation lag observed: Vercel took several minutes past the push to
    serve the updated `papers.ts` data (PDF binaries at the new filenames
    were already live sooner, since those files pre-existed from the
    concurrent lane's earlier commit); confirmed via a polling loop against
    `/papers/paper-a3m` rather than a single spot-check.

## Receipt — A3M v3M.0.3 → v3M.0.4 site sync (Sonnet worker, R1-closed bump)

Convex bump already done by a prior lane (paperVersions row
`k5732z2y722d0rmxer1r44nvr18dmbwa`); this session's scope was site-data
propagation, build/deploy, and live verification only.

- **Source PDF confirmed at target version** (byte-identical across source
  + both mirrors, verified by `md5`): `research/track_a3_multichannel/paper/main.pdf`
  v3M.0.4, md5 `b98ee16e11d106c96ac593480857112b`, 8 pp — already mirrored
  byte-identical at `site/public/papers/a3_multichannel_arxiv_v3M.0.4.pdf`
  and `public/papers/a3_multichannel_arxiv_v3M.0.4.pdf` (pre-existing from a
  concurrent lane; verified, not re-copied).
- **Site data updated:** `site/src/data/papers.ts` (version v3M.0.3→v3M.0.4,
  pages 7→8, tldr/description/pdfMeta/changelog/artifact hrefs rewritten to
  the R1-closed status copy), `live-status.ts` (version + pendingWork),
  `publish.ts` (Track A decision detail + A3 manuscript row status/dependency/
  nextGate), `reviewTimeline.ts` (new 2026-09-02 `restructure` entry
  `a3m-r1-closed-v3m-0-4-2026-09-02` with the R1 verdict cells — Fable
  major-revisions, Grok reject, Gemini major-revisions — all closed with
  real edits: official NANOGrav posterior primary, transmission bound
  scoped handoff-conditional, PBH ratio result with regime disclosed; R2
  verification pass dispatched).
- **Build + typecheck:** `npx tsc --noEmit` clean; `npm run build` clean —
  65 static pages generated including `/papers/paper-a3m`.
- **Freshness gate:** `tools/site_freshness_check.sh` — PASS (no
  `FRESHNESS_SKIP`); ran again via the pre-push hook on both remotes, same
  PASS result.
- **Commit:** `a6bde472` — `feat(site): bump A3M v3M.0.3 -> v3M.0.4 (R1
  closed)` (4 files: papers.ts, live-status.ts, publish.ts,
  reviewTimeline.ts). Untracked concurrent-lane R2-verify review raws in
  `project-context/peer-reviews/` were left untouched, not staged.
- **Push:** `origin main` `09220c2e..a6bde472` and `upstream main`
  `09220c2e..a6bde472`, both with the pre-push freshness hook reporting
  `OVERALL: PASS`.
- **Deploy verification (live, post-propagation):**
  - `curl -sI https://bigbounce.hubify.app/papers/a3_multichannel_arxiv_v3M.0.4.pdf`
    → 200, `etag: "b98ee16e11d106c96ac593480857112b"` (matches source md5
    exactly); took ~6 polling attempts (~75s) for Vercel to serve the new
    filename.
  - `/papers/paper-a3m` rendered HTML contains `v3M.0.4`.
  - `/reviews` rendered HTML contains "R1 closed".
- **Not fabricated / explicitly flagged:** none — the PDF md5/page count and
  the Convex row id were confirmed present on disk / in the task brief
  before use; no value was invented.

## Receipt — A3M v3M.0.5 site sync (live-status/publish + kits) (Sonnet worker)

Convex bump was already done by a prior lane
(`k57fxwc5ze57ez9fpd8wyk8e2n8dpw9e`, not repeated). `papers.ts` and
`reviewTimeline.ts` already carried v3M.0.5's real R2-CLOSED status from
that same prior lane; this pass found `live-status.ts` and `publish.ts`
still stale at v3M.0.4/R2-running and brought them into sync, and replaced
the DRAFT v3M.0.2 abstract in the endorser/portal kits with the real
v3M.0.5 abstract.

- **PDF confirmed at target version** (byte-identical across source + both
  mirrors, verified by `md5` before touching site data):
  `research/track_a3_multichannel/paper/main.pdf`, 9 pp, md5
  `67e1510e2b300ec683ed2e288ef1aefe`; mirrored at
  `site/public/papers/a3_multichannel_arxiv_v3M.0.5.pdf` and
  `public/papers/a3_multichannel_arxiv_v3M.0.5.pdf` (pre-existing, verified
  not re-copied).
- **Tarball sha256 verified on disk:**
  `project-context/SSOT/arxiv_tarballs/a3_multichannel_arxiv_v3M.0.5.tar.gz`
  = `cd2ce1ef7c38746a9e8f59db371378bcc74b624a54406ca6f0c74611742522ab`
  (full hash via `shasum -a 256`, matches the task brief's `cd2ce1ef…`
  prefix).
- **Site data updated:** `site/src/data/live-status.ts` (paper-a3m row:
  version v3M.0.4→v3M.0.5, pendingWork rewritten to the R2-closed status
  line), `site/src/data/publish.ts` (Track A decision detail + A3
  manuscript row status/dependency/nextGate).
- **SSOT docs updated:** `project-context/SSOT/ENDORSER_OUTREACH_2026-09-02.md`
  §3a — DRAFT v3M.0.2 abstract replaced with the real v3M.0.5 abstract text
  (verbatim from `research/track_a3_multichannel/paper/main.tex`'s
  `\begin{abstract}`), status/gate language updated to "automated review
  converged; final author review + science gate pending (method-independent
  f_NL check; bounce cubic term; real NANOGrav KDE-grid injection); do not
  send its endorsement email yet." `project-context/SSOT/PORTAL_KITS_2026-09-02.md`
  — click-list item 4, §3 intro, and the §3a gate paragraph updated to the
  same status language, plus the arXiv tarball path + full sha256 added to
  the A3 PRD kit reference.
- **Build + typecheck:** `npx tsc --noEmit` clean; `npm run build` clean
  (all routes prerendered, including `/papers/paper-a3m`).
- **Freshness gate:** `tools/site_freshness_check.sh` — PASS (no
  `FRESHNESS_SKIP`); only non-blocking rows are pre-existing (banner lag,
  skillslog already logged).
- **Commit:** `454448a5` — `feat(site): sync A3M v3M.0.5 R2-closed status to
  live-status/publish + kits` (4 files: live-status.ts, publish.ts,
  ENDORSER_OUTREACH_2026-09-02.md, PORTAL_KITS_2026-09-02.md).
- **Push:** `origin main` and `upstream main`, both `d7378ca7..454448a5`,
  pre-push freshness hook `OVERALL: PASS` on both.
- **Live verification (headed browser + curl, post-deploy):**
  - `curl -sI` (with a browser UA to clear the Vercel bot checkpoint) on
    `https://bigbounce.hubify.app/papers/a3_multichannel_arxiv_v3M.0.5.pdf`
    → HTTP 200, `etag: "67e1510e2b300ec683ed2e288ef1aefe"` (matches source
    md5 exactly); took ~7 polling attempts (~105s) for Vercel to serve the
    new deploy.
  - `/papers/paper-a3m` renders `V3M.0.5 · LIVE`, "R2 CLOSED — real 30-bin
    injection-recovery validation..." tldr/pdfMeta text live.
  - `/reviews` renders the `v3M.0.5: R2 CLOSED` timeline heading.
- **Not fabricated / explicitly flagged:** none — the PDF md5, tarball
  sha256, and Convex row id were confirmed present on disk / in the task
  brief before use; no value was invented or truncated. The `/reviews`
  page's hardcoded intro paragraph and P1A/P1B/P2/P3/P4/P5-only readiness
  table (visible during this pass's browser check) are pre-existing and out
  of this task's explicit scope (papers.ts/live-status.ts/publish.ts/kits),
  not touched.

## Follow-up receipt — /reviews reframe to live lineup + A3 readiness mirror fix (2026-09-02, later session)

Sonnet site worker pass. Fixed two items left open by the first reframe pass:

1. **`/reviews` still framed around the six historical papers only.** Rewrote
   the intro paragraph, the "Canonical readiness" ETA-table row, and the
   "External automated-review evidence" scoping paragraph in
   `site/src/app/reviews/page.tsx` to name the live lineup per the
   2026-09-02 portfolio decision: A3 (paper-a3m, Track A flagship,
   converged, final author review pending), P4′ (Track C1, converged),
   the ECH Note (P1N, Track B, converged), and P2′ (paper-2l, archived
   into A3, theory record only) — with the historical six (P1A/P1B/P2/P3/
   P4/P5) explicitly relabeled archived lineage and their own caps kept
   visible, never deleted. The verdict-grid/`AllAMeter` component
   (`ProgressViz.tsx`) was left untouched by design (per the first pass's
   documented reasoning) — it is the pre-restructure six-paper historical
   board; the intro/evidence paragraph now says so explicitly and points
   readers to the readiness table above for the live-lineup numbers. The
   all-A meter already counts ACTIVE legs only (Grok API + Gemini API +
   Claude/Fable INT; GPT frozen) per directive M-AMENDED — unchanged.

2. **`paper-a3m` readiness mirror was stale at 20.** Convex
   (`papers:listAllPaperStates`) reports paper-a3m at `readinessComputed:
   70.0` (R2 verification closed, final author review pending — directive
   P composition: science/evidence/review-convergence/packaging gates
   open on the science-gate leg). `site/src/data/papers.ts` (readiness
   field + intro description text) and `site/src/data/live-status.ts`
   (readiness field + pendingWork text) still read 20; both corrected to
   70 with a directive-P note. `publish.ts` was checked and needed no
   change — it carries status text ("Converged (v3M.0.5)...") not a bare
   numeric readiness field.

Verification: `npm run build` (site/) clean; `npx tsc --noEmit` clean;
`tools/site_freshness_check.sh` → OVERALL PASS (no `FRESHNESS_SKIP`).
Pushed to both `origin main` and `upstream main`
(`14f1cad5`, `95fee959..14f1cad5`). Headed-browser QA (Claude Browser,
not Playwright) post-deploy: `/reviews` renders the new intro/table text
live (confirmed via page-text extraction — "Current lineup (flagship
line + closed-line note + data products, per the 2026-09-02 portfolio
decision)" and "A3 70" both present); `/papers`, `/paper` (tracks), and
`/` (overview) all load with zero console errors. Deploy confirmed live
via a background poll against `bigbounce.hubify.app/reviews` (ISR
`revalidate=60` — first fetch after push served the prior build; the poll
waited for the new text to appear rather than trusting a bare 200).

Commit: `14f1cad5` — `feat(site): /reviews reframed to the live lineup;
A3 readiness mirror 70` (3 files: `site/src/app/reviews/page.tsx`,
`site/src/data/live-status.ts`, `site/src/data/papers.ts`). An unrelated
`site/src/data/repro.ts` diff produced as a side effect of `npm run
build`'s repro-manifest sync script was reverted (`git checkout --`)
before commit — out of scope for this pass, not touched.
