# Publication-campaign acceleration audit — 2026-07-14

## Objective

Reduce wall-clock time to honest publication readiness without weakening
derivation checks, reproducibility, exact-PDF review, independent adjudication,
or visual QA. The campaign remains **in revision**; acceleration metrics below
are process evidence, not manuscript readiness scores.

## Executive finding

The largest avoidable delays were not model speed. They were:

1. reviewing papers against the wrong venue/article-type bar;
2. rerunning unchanged artifacts instead of caching by exact content;
3. duplicated, drifting paper-path maps across scripts;
4. replaying expensive data construction when an immutable checkpoint product
   already contained the required rows;
5. serial vendor dispatch;
6. treating workflow gates as if they required more science edits; and
7. multiple agents appending to one very large site timeline file.

The safe strategy is therefore **parallelize independent work, serialize shared
state, and bind every inference to immutable evidence**.

## Implementation checkpoint — 2026-07-14 12:15 PT

The registry and packet work described below is no longer merely planned. It is
implemented, tested, and in active use:

- canonical six-paper registry: `9f898efd`;
- immutable content-addressed packets and hardening: `35bbe3ec`, `0f268268`,
  `be591f45`;
- tracked evidence-bundle verification: `6a3908a1`;
- all active review consumers routed through the registry/packet layer:
  `1f942478`;
- exact compute-routing gate: `0df1f1dd`;
- focused registry/packet/manifest suite: **13/13 passing**.

The packet guard has already prevented two invalid rounds: one short expected
PDF hash and one incorrectly expanded commit id were rejected before dispatch.
No reviewer call, verdict, or cost was produced from either failure.

Measured concurrent-panel gains now include:

| Exact panel | Critical path | Summed vendor latency | Wall-time reduction |
|---|---:|---:|---:|
| P5 v0.1.130 AJ | 37.6 s | 96.0 s | 60.8% |
| P1A v1A.0.121 CQG Note | 63.5 s | 103.4 s | 38.6% |
| P2 v1.7.121 PRD | 98.1 s | 193.3 s | 49.2% |

These are latency measurements, not readiness evidence. Each vendor still
produced a separate verbatim report, and every board was adjudicated at the
finding level before any public status changed.

### New bottleneck ranking after implementation

1. **Evidence acquisition, not reviewer latency.** P2's cubic transfer and
   survey covariance, P5's final labels/archive, and every DOI/human-submission
   gate require real external inputs. Re-reviewing cannot close them.
2. **One giant shared site file.** `reviewTimeline.ts` remains above 500 KB,
   adds roughly 10--20 seconds to every focused lint, and is the main remaining
   avoidable write-contention point.
3. **Finding recurrence.** Generic reviewers repeatedly restate already printed
   material. Normalized truth ledgers now stop broad rewrites, but a small
   machine-readable finding registry would make this automatic.
4. **Long compute without resumable scientific checkpoints.** The active P1B
   jobs are healthy and must not be disturbed, but future exact-window runs
   should publish validated deterministic chunks plus a final reduction receipt
   so a host interruption does not discard hundreds of realizations.
5. **Release-state fan-out.** PDF mirrors, version metadata, SSOT, Convex, API,
   and site remain an atomic manual chain. Existing skills reduce mistakes, but
   a dry-run release manifest should verify every target before mutation.

### Next accelerations to implement without weakening science

1. Split the site timeline into typed current and historical modules, preserving
   byte-equivalent exported records, stable order, route rendering, and build.
2. Add a machine-readable normalized-finding ledger keyed by paper, finding
   class, first/last exact PDF, disposition, and required evidence. Review
   ingestion should flag recurrence rather than opening duplicate work.
3. Add a packet-aware campaign dispatcher that dry-runs all six packets first,
   refuses duplicate keys, then launches only changed/eligible panels with a
   concurrency cap and writes a round-level receipt.
4. Add resumable deterministic shards to future P1B robustness runs only after
   the current exact jobs finish and serial-vs-sharded scientific-field equality
   passes.
5. Add an atomic release preflight manifest covering source/PDF hashes, page
   counts, version stamps, proof manifests, mirror targets, SSOT/Convex payloads,
   API routes, and site entries. Mutation remains serialized after a clean
   preflight.

The stop rule is now explicit: after one bounded closure and one exact full
confirmation panel, recurring findings that map to unchanged external gates do
not trigger another manuscript rewrite or generic panel. They route to evidence
acquisition or human venue review.

## Implemented accelerations

| Improvement | Evidence / measured effect | Science guard retained |
|---|---|---|
| Independent paper lanes | P1A, P1B, P3/P5, and P4 work proceed without shared manuscript writes | One owner per paper; scoped commits; no cross-paper staging |
| Concurrent blind vendor panels | P3 r5 OpenAI/Gemini/Grok completed in 72.7 s wall; individual latencies sum to 125.8 s, a measured 42% wall-time reduction | Same exact PDF SHA, separate raw reports, no reveal between legs |
| Exact-artifact binding | P3 r5 panel binds version, 14 pages, source `7cf60218`, and PDF SHA `024931a4...39dc` | Hash mismatch fails before dispatch; verdict words never float across versions |
| Typed missing-leg records | P3 independent Codex quota gap is `NOT_RUN`, with no API fallback or synthetic verdict | Missing evidence cannot be mistaken for pass/zero/accept |
| Venue-first routing | `TARGET_VENUE_MATRIX.md` routes P1A→CQG Note, P1B→JCAP, P2→PRD, P3/P4→ApJS, P5→AJ | Venue boards remain immutable and separate; fit never waives correctness |
| Checkpoint-product reuse | P3's 143 clean checkpoint parts produced the exact 2,267-row warned-primary auxiliary table without replaying the 22 GB public FITS scan | Exact identity-set replay assertion, carried-field equality, hashes, and validator all pass |
| Compute concurrency cap | P1B runs at most two exact NaMaster jobs simultaneously on the local host | Prevents memory thrash; atomic receipts; no partial result accepted |
| Deterministic inner-parallelism gate | P1B realization-level parallel implementation is blocked until serial-vs-parallel scientific-field equality passes | Faster code cannot enter production based on timing alone |
| Science/workflow gate separation | DOI, archive publication, companion-paper status, and human submission remain visible but do not trigger invented calculations | Scientific findings still require source-backed truth audit and closure |
| Durable campaign memory | `tasks.md`, `tasks.json`, and `plan.md` now reflect the publication critical path rather than the earlier CMUX handoff track | Prevents compaction-driven priority drift and duplicate work |

## Confirmed high-leverage changes

### 1. Canonical six-paper registry — implemented

One machine-readable registry now owns paper ID, source/PDF paths, site slug,
target journal, article type, and review profile. It replaced duplicated maps
that had drifted across:

- `tools/int_wave.sh` (P3 still points to `paper3_draft.tex`);
- `tools/int_api_review_2026-07-08.py`;
- `tools/directive_g.sh` (missing P1A/P1B and stale P3 path); and
- `tools/v3_native_pdf_review.py` (hard-coded obsolete `CODE_2025` root and an
  Anthropic-era default incompatible with the current campaign).

Acceptance tests prove exactly six canonical IDs, existing paths, unique site
slugs, P3→`paper3_apjs`, and declared venue/article type for every paper.

### 2. Content-addressed review packets — implemented and exercised

Every packet freezes:

```text
paper + version + source commit + source path + PDF path + PDF SHA-256
+ page count + venue + article type + prompt SHA-256 + allowed-context SHA-256
```

The per-leg cache key additionally includes model and effort. Identical keys are
reused rather than rerun. A changed artifact or review profile creates a new
packet. Dirty, mismatched, or ambiguous inputs fail closed.

This removes three recurring costs at once: wrong-PDF reviews, overwritten
round directories, and repeated reviewer noise on byte-identical content.

### 3. Two-stage review cadence — active campaign rule

After a bounded correction, use a focused delta review to detect regressions,
then require one full blind exact-PDF panel before publication readiness. Do not
pay for repeated full panels while a known major control remains open. This
changes review order, not the final acceptance bar.

### 4. Append-only site review data — highest-priority unimplemented tooling item

`site/src/data/reviewTimeline.ts` is now larger than 500 KB, triggers Babel
deoptimization, and caused a live P3/P5 concurrent-edit collision. Split it into:

- a small append-only current-round module;
- a read-only historical archive; and
- a typed export that concatenates both.

New workers then edit separate current-round records or generated per-round
fragments rather than one giant shared file. Typecheck, production build, stable
sort order, and route rendering must match before/after.

## Science-specific critical-path changes

| Paper | Current highest-value closure | Acceleration method | Non-negotiable gate |
|---|---|---|---|
| P1A | v1A.0.120 exact conventions, Holst inverse, benchmark wording | Review as CQG Note after one correctness confirmation instead of repeating PRD-only loops | Fresh exact-PDF CQG board; PRD result remains separate |
| P1B | Remaining exact-window robustness configs | Two-job host cap, then two realization workers only after exact serial equivalence | Complete receipt/provenance and no scientific-field drift |
| P2 | Archive/source packaging and external-covariance/direct-transfer residuals | Stop manuscript churn while the exact PRD board is already accept-level; close workflow/data gates directly | No substitution of surrogate covariance for missing external evidence |
| P3 | Chance-association, warned-population, original-member controls | Reuse r5 auxiliary table; run one deterministic shifted-coordinate FITS scan rather than rebuild the release | Source-backed random control, exact artifact, fresh ApJS panel |
| P4 | Portable provenance and exact current proof | Regenerate manifests with repo-relative paths and immutable remote revisions | Full 27-page audit and fresh ApJS/AJ board |
| P5 | Promote official GALZONE estimator; compress secondary paths | Structural AJ rewrite uses the already-computed exact A37 control | Post-hoc hierarchy disclosed; Paper-IV/archive gates remain open |

## Deliberately rejected shortcuts

- No verdict averaging across journals.
- No reviewer substitution when a provider quota is exhausted.
- No repeated review of an unchanged packet merely to seek a friendlier label.
- No readiness increase from a model's final verdict without finding-level audit.
- No parallel compute accepted without deterministic equivalence.
- No DOI, archive, public-tag, human-referee, or companion-paper gate described
  as complete before external state proves it.
- No Snakemake/DVC migration during the submission push; content-addressed
  packets deliver the immediate benefit with far less workflow churn.

## Next implementation order

1. Finish the five active manuscript/compute lanes.
2. Use the first free non-science worker for the canonical registry and review
   packet generator with fail-closed tests.
3. Use the next free site worker to split current vs historical review-timeline
   data and eliminate append collisions.
4. Close P3's deterministic random-shift and warned-population controls.
5. Dispatch venue-correct exact-PDF panels concurrently.
6. Only after every board is honest and complete, run the atomic PDF/version/
   claims/SSOT/Convex/API/site release chain and governed browser QA.

## Evidence ledger

- Campaign-memory correction: `b9f21300`
- P3 r5 manuscript/proof: `7cf60218`
- P3 exact panel + truth audit + site/SSOT: `ffa2826e`
- P3 typed Codex gap: `6fe964fb`
- P5 PRD/AJ normalized truth audit: `d2f37b28`
- Venue-routing contract: `263be43e`
- Canonical registry: `9f898efd`
- Packet implementation/hardening: `35bbe3ec`, `0f268268`, `be591f45`
- Evidence manifest verifier: `6a3908a1`
- Registry/packet consumer migration: `1f942478`
- Exact compute routing gate: `0df1f1dd`
- P5 exact AJ truth audit: `15f2e6af`
- P1A v1A.0.121 closure and exact board: `b587cb7b`, `36badcbd`
- P2 v1.7.121 positioning closure and exact board: `86b38a0c`, `e3e28da2`
