# PLAN — BigBounce publication program

**Authoritative program plan · reconciled 2026-08-03**

This is the single executable plan for the six-paper program. It defines the
current phase, gates, and work order. It does not duplicate manuscript science
facts: use the source map below and the SSOT status board for those.

## Mission

Bring six honest, reproducible manuscripts through Houston's final review and
then through their journal submission workflows. Automated review is a
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

The July 22 active-leg confirmation wave produced 19 genuinely-new-real
findings across the portfolio; all were closed. The July 23–24 completeness
resweep caught MAJOR items hidden beneath summary verdict labels and closed the
remaining P1B, P4, and P5 findings. The current versions are:

| Paper | Version | Agent gates | Next phase |
|---|---:|---:|---|
| P1A | v1A.0.127 | 95/95 | CQG submission |
| P1B | v2B.0.16 | 95/95 | JORS submission |
| P2 | v1.7.130 | 95/95 | PRD submission |
| P3 | v3.2.0-r14 | 95/95 | ApJS submission |
| P4 | v1.0.272 | 95/95 | ApJS submission |
| P5 | v0.1.146-2026-07-24 | 95/95 | AJ submission |

The 95 values mean the four Directive-P agent gates are recorded complete; they
do not claim Houston sign-off, submission, referee acceptance, or publication.
Because the current PDFs include closures made after the last complete
six-paper active-leg board, one bounded **final-hash confirmation** is still an
evidence-hygiene task. It checks that the exact final artifacts contain no new
real defect. It is not permission to restart an unbounded verdict-word loop and
does not automatically reduce readiness unless it finds a real regression.

## Phase plan

### Phase A — truth reconciliation and production sync (complete 2026-08-03)

1. Make this plan, the SSOT board, per-paper statuses, queue, tasks, revision
   tracker, Convex, and site projections agree on identity, version, Directive-P
   scoring, and publishing gates.
2. Preserve historical review evidence while visibly marking superseded plans,
   caps, P1U state, and verdict-word snapshots as historical.
3. Verify the production site and public paper links after the atomic sync.

Repository consolidation completed in the same recovery pass: archival merge
`556b8454` preserves all formerly divergent tips, both GitHub remotes now expose
only `main`, obsolete local branches/worktrees are removed, and local,
`origin/main`, and `upstream/main` agree at `2be3964b`.

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

1. Complete bounded final-hash/package acceptance for all six papers.
2. Close remaining submission metadata for P3/P5 and finalize portal packets.
3. Obtain Houston's six explicit sign-offs.
4. Submit P2 first, then the remaining journal-ready packets in the order that
   minimizes account/reviewer/APC friction.

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
it.
