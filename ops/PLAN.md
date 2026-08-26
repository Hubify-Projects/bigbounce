# PLAN — BigBounce research and publication program

**Authoritative program plan · reconciled 2026-08-04**

This is the single executable plan for the research portfolio. It defines the
current phase, gates, and work order. It does not duplicate manuscript science
facts: use the source map below and the SSOT status board for those.

> **Publication architecture approved — 2026-08-04:** The public portfolio is
> organized into bounce theory, DESI anomaly discovery, and galaxy chirality.
> Current P3 is an integrated supporting data/provenance release, not a
> standalone paper; P5 remains a standalone AJ companion. The governing record
> is `project-context/PUBLICATION_ARCHITECTURE_RESET_2026-08-03.md`.
> For the plain-English, complete paper/data/model/software release map, use
> `project-context/PUBLICATION_AND_RELEASE_MASTER_MAP_2026-08-04.md`.

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
| Plain-English paper/release architecture | `project-context/PUBLICATION_AND_RELEASE_MASTER_MAP_2026-08-04.md` |
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
Six candidate packages reached the Directive-P agent gate, but the approved
portfolio does not treat them as six equal publications. The final routing is
three core scientific stories (P2, a rebuilt anomaly-science paper, and P4),
two specialist outputs (P1A and P1B), one standalone companion (P5), and one
supporting data release (current P3). See the architecture reset for the
rationale.

The clean DESI rerun scan/provenance stage is complete: the post-dedup summary
at `pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/summary.json`
records 28,425,963 raw rows, 27,547,223 unique TARGETIDs, 878,740 duplicate
rows removed, and 52,188 S>5 after dedup. That closes the scan stage, not the
flagship follow-on work.

The public reproducibility projection was re-verified on production on
2026-08-26 after the linked Vercel project was reconciled to the repository's
Next.js static-export build contract. `/reproduce` now displays the completed
AUG-011 receipt/candidate markers; this public projection is not a substitute
for authenticated access to the full shard/receipt corpus.

The July 22 active-leg confirmation wave produced 19 genuinely-new-real
findings across the portfolio; all were closed. The July 23–24 completeness
resweep caught MAJOR items hidden beneath summary verdict labels and closed the
remaining P1B, P4, and P5 findings. The current versions are:

| Paper | Version | Agent gates | Next phase |
|---|---:|---:|---|
| P1A | v1A.0.127 | 95/95 | CQG submission |
| P1B | v2B.0.16 | 95/95 | JORS submission |
| P2 | v1.7.130 | 95/95 | PRD submission |
| P3 support | v3.2.0-r17 | 95/95 | Integrate into anomaly flagship release; no standalone ApJS submission |
| P4 | v1.0.274 | 95/95 | Houston review, then ApJS submission |
| P5 | v0.1.147-2026-08-03 | 95/95 | Houston review, archive mint, then AJ submission |

The 95 values mean the four Directive-P agent gates are recorded complete; they
do not claim Houston sign-off, submission, referee acceptance, or publication.
The bounded **final-hash confirmation** is complete for the selected portfolio.
No exact artifact requires scientific reopening. The usable provider coverage
is uneven and travels with each decision packet—especially P5, whose completed
leg covered pages 1–25 of 46—so this evidence advances the work to Houston's
visual review without being mislabeled as multi-provider or human consensus.
Houston's decision in Phase C is publication authorization on the bound
evidence packet, not a request that Houston independently re-audit the
technical science.

## Phase plan

### Phase 0 — publication architecture reset (complete 2026-08-04)

1. Reconcile the original DESI anomaly project's datasets, thresholds, model
   versions, candidate counts, validation claims, and surviving artifacts.
2. Current P3 decision: integrated technical/data release for the rebuilt
   anomaly-science paper; no standalone submission.
3. P5 decision: independent AJ companion to P4.
4. Houston approved the research-program map on 2026-08-04.

The initial claim audit is complete at
`project-context/ANOMALY_SCIENCE_CLAIM_INVENTORY_2026-08-03.md`. Its next gate
is the completed rerun's follow-on validation, taxonomy, and manuscript work,
not another scan.

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

### Phase B — bounded final-artifact acceptance (complete 2026-08-04)

1. Bind each final source/PDF pair to version, commit, SHA-256, venue, and
   package receipt.
2. Run automated preflight, compile, link, mirror, and visual PDF audits.
3. Run at most the bounded final-hash active-leg confirmation needed to verify
   the post-board closures; truth-audit every finding and reopen only confirmed
   genuinely-new-real defects.

Evidence and exact links are bound in
`project-context/SSOT/HOUSTON_VISUAL_REVIEW_PACKETS_2026-08-04.md`.

### Phase C — Houston sign-off (active)

Present one short decision packet per paper: final PDF, central claim, honest
limitations, artifact proof, and submission checklist. Record Houston's exact
per-paper sign-off before changing 95 to 100.

The active P2 reader-first decision surface is live at
`https://bigbounce.hubify.app/final-review`; it binds the exact v1.7.130 PDF,
five page-level checks, evidence links, and the `APPROVE | REVISE | DEFER`
response block. Subsequent papers follow the same sequence after the P2
decision.

### Phase D — journal submissions

Use the existing venue kits and current final artifacts. Journal accounts,
fees/waivers, reviewer suggestions, portal metadata, and upload clicks are
publishing tasks, not readiness deductions. arXiv endorsement is a parallel
distribution task and is not on the journal critical path.

## Immediate priority order

Completed 2026-08-04: the three-program public map and exact P3/P5 roles are
live on production; the restoration gate selected a tested fail-closed rerun
contract after proving the enhanced parent/calibration unrecoverable.

1. Collect Houston's decisions in order P2 → P1A → P4 → P1B → P5 using the
   bounded visual-review packet; P3 receives integration feedback only.
2. Complete the rebuilt anomaly flagship follow-on from the finished clean
   rerun: selected sample, validation contract, taxonomy, and manuscript.
3. The 2026-08-26 local/provider structural-retention audit is complete: B2
   retains 36,634 receipt objects and 36,634 shard objects, while Hugging Face
   is a partial private mirror. Next, align Hubify canonical-lab surfaces once
   authenticated access is available.
4. After each approval, run that work's archive/portal/endorsement checklist
   and preserve external receipts; do not wait for every paper to be approved.

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
