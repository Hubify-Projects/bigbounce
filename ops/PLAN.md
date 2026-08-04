# PLAN — BigBounce research and publication program

**Authoritative program plan · reconciled 2026-08-03**

This is the single executable plan for the research portfolio. It defines the
current phase, gates, and work order. It does not duplicate manuscript science
facts: use the source map below and the SSOT status board for those.

> **Publication-architecture gate — 2026-08-03:** The former six-paper
> submission plan is paused. The six count is an operational history, not a
> scientific requirement. The governing decision draft is
> `project-context/PUBLICATION_ARCHITECTURE_RESET_2026-08-03.md`. Preserve all
> completed packages, but do not submit, seek endorsements, mint new immutable
> P4/P5 records, or push a public six-equal-papers framing until Houston accepts
> or revises the new architecture.

## Mission

Publish the strongest honest, reproducible scientific portfolio, organized by
research question rather than an inherited paper count. Automated review is a
truth-auditing instrument, not a substitute for editorial or human scientific
judgment.

## Current directives

- **N — active review routing:** Grok API, Gemini API, and Claude Opus INT are
  active. OpenAI/ChatGPT is paused; historical cells remain visible and frozen.
- **M-AMENDED — active-leg grid:** the all-A diagnostic applies only to active
  legs. Raw verdict words are preserved and never fabricated.
- **P — publication-readiness composition:** science 25 + evidence and
  reproducibility 25 + automated convergence 25 + packaging/PDF hygiene 20 +
  Houston's personal sign-off 5. The four agent gates total **95**. Only an
  explicit per-paper Houston sign-off reaches **100**.
- **Automated convergence:** zero genuinely-new-real findings remain
  outstanding across active legs on the current exact artifact. Verdict words
  are diagnostic; every finding still requires a source-cited disposition.
- **Publishing is separate from readiness:** venue choice, submission clicks,
  arXiv endorsement, journal peer review, and independent human review do not
  subtract from the readiness score.

Directives J–M and the former verdict-derived readiness caps remain historical
process evidence in `CLAUDE.md`; they are not the current scoring or exit model.

## Canonical map

| Concern | Canonical location |
|---|---|
| Program phase, priorities, decisions | `ops/PLAN.md` |
| Manuscript identities, paths, venues | `project-context/paper_registry.json` |
| Current portfolio status | `project-context/SSOT/index.md` |
| Per-paper status and honest limitations | `project-context/SSOT/paper-*/status.md` |
| Current work queue | `project-context/SSOT/queue.md` |
| Review chronology | `project-context/peer-reviews/REVISION_TRACKER.md` |
| Finding dispositions | `project-context/peer-reviews/DISPOSITIONS/` |
| Public projection | Convex plus `site/src/data/` |
| Recovery/You.md context | `project-context/plan.md` and `.youmd/projects/bigbounce/` |

## Current state

Technical readiness and publication strategy are now deliberately separated.
Six candidate packages reached the Directive-P agent gate, but that does not
prove that all six should be independent publications. The active portfolio
map is three core scientific stories (P2, a rebuilt anomaly-science paper, and
P4), two specialist outputs (P1A and P1B), and two held editorial decisions
(current P3 and P5). See the architecture reset for the rationale.

The July 22 active-leg confirmation wave produced 19 genuinely-new-real
findings across the portfolio; all were closed. The July 23–24 completeness
resweep caught MAJOR items hidden beneath summary verdict labels and closed the
remaining P1B, P4, and P5 findings. The current versions are:

| Paper | Version | Agent gates | Next phase |
|---|---:|---:|---|
| P1A | v1A.0.127 | 95/95 | CQG submission |
| P1B | v2B.0.16 | 95/95 | JORS submission |
| P2 | v1.7.130 | 95/95 | PRD submission |
| P3 | v3.2.0-r16 | 95/95 | Exact r16 confirmation, then Houston review and ApJS submission |
| P4 | v1.0.273 | 95/95 | Houston review, then ApJS submission |
| P5 | v0.1.147-2026-08-03 | 95/95 | Houston review, archive mint, then AJ submission |

The 95 values mean the four Directive-P agent gates are recorded complete; they
do not claim Houston sign-off, submission, referee acceptance, or publication.
Because the current PDFs include closures made after the last complete
six-paper active-leg board, one bounded **final-hash confirmation** is still an
evidence-hygiene task. It checks that the exact final artifacts contain no new
real defect. It is not permission to restart an unbounded verdict-word loop and
does not automatically reduce readiness unless it finds a real regression.

## Phase plan

### Phase 0 — publication architecture reset (active)

1. Reconcile the original DESI anomaly project's datasets, thresholds, model
   versions, candidate counts, validation claims, and surviving artifacts.
2. Decide whether current P3 is a standalone technical/data note or a
   supplement to the rebuilt anomaly-science paper.
3. Decide whether P5 is an independent companion, a shorter P4 supplement, or
   a deferred analysis.
4. Obtain Houston's approval of the research-program map before regenerating
   the public site and submission board.

The initial claim audit is complete at
`project-context/ANOMALY_SCIENCE_CLAIM_INVENTORY_2026-08-03.md`. Its next gate
is artifact restoration or a clean rerun—not manuscript polishing.

### Phase A — truth reconciliation and production sync (complete 2026-08-03)

1. Make this plan, the SSOT board, per-paper statuses, queue, tasks, revision
   tracker, Convex, and site projections agree on identity, version, Directive-P
   scoring, and publishing gates.
2. Preserve historical review evidence while visibly marking superseded plans,
   caps, P1U state, and verdict-word snapshots as historical.
3. Verify the production site and public paper links after the atomic sync.

Repository consolidation completed in the same recovery pass: archival merge
`556b8454` preserves all formerly divergent tips, both GitHub remotes now expose
only `main`, and obsolete local branches/worktrees are removed. At that
consolidation checkpoint, local, `origin/main`, and `upstream/main` agreed at
`2be3964b`; subsequent final-package commits are pushed after acceptance.

### Phase B — bounded final-artifact acceptance

1. Bind each final source/PDF pair to version, commit, SHA-256, venue, and
   package receipt.
2. Run automated preflight, compile, link, mirror, and visual PDF audits.
3. Run at most the bounded final-hash active-leg confirmation needed to verify
   the post-board closures; truth-audit every finding and reopen only confirmed
   genuinely-new-real defects.

### Phase C — Houston sign-off

Present one short decision packet per paper: final PDF, central claim, honest
limitations, artifact proof, and submission checklist. Record Houston's exact
per-paper sign-off before changing 95 to 100.

### Phase D — journal submissions

Use the existing venue kits and current final artifacts. Journal accounts,
fees/waivers, reviewer suggestions, portal metadata, and upload clicks are
publishing tasks, not readiness deductions. arXiv endorsement is a parallel
distribution task and is not on the journal critical path.

## Immediate priority order

1. Preserve the bounded P3 r17 technical closure without calling it the
   replacement for the original anomaly science.
2. Complete the anomaly source-to-claim reconciliation and propose the rebuilt
   flagship manuscript's defensible scientific scope.
3. Resolve the independent-publication decisions for current P3 and P5.
4. Rewrite the public map around three research programs, then regenerate the
   approval/submission/endorser board for the selected portfolio.
5. Resume exact-hash acceptance, Houston visual review, and submission only
   after the architecture is approved.

## Stop rules

- Never claim 100 without Houston's explicit per-paper words.
- Never equate automated convergence with journal acceptance.
- Never chase literal reviewer verdicts after zero-new-real convergence.
- Never rewrite raw reviews; correct only normalized status and projections.
- Never delete or merge historical branches or artifacts without first proving
  whether they contain unique work.

## Operational watchpoint

Hubify CLI lab verification is currently unavailable: `hubify status`,
`papers`, `tasks`, `agents`, and `activity` fail unauthenticated because
`.env.local` lacks `HUBIFY_TOKEN` while `.env.example` declares the key. This is
an external authentication gap, not a blocker for repository/site truth sync.
Acquire the token only through an approved secret source; never print or infer
it. You.md project context is registered and current locally, but two remote
push attempts returned `server_error: Failed to save bundle`; retain the local
overlay and retry the service later rather than force-pulling over local edits.
