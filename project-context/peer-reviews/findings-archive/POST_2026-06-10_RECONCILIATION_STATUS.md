# Post-2026-06-10 finding-receipt reconciliation

This is a bounded migration against the canonical SciStack
`r-round-finding-archive` contract introduced at `ba36b4c`. The cutoff is
exclusive: path-dated review rounds from 2026-06-11 onward are eligible.

## Deterministic inventory result

- Canonical git-tracked raw review receipts: **271**
- Receipts with an explicit tagged-finding count or explicit clean statement:
  **259 / 271 (95.5720%)**
- Explicit findings represented by those parseable receipts: **1,574**
- Explicit parse-gap rows: **6 / 271 (2.2140%)**
- Explicit failed-leg rows: **6 / 271 (2.2140%)**

The six parse gaps and six failed legs are not treated as zero-finding reviews.
Each is retained with `finding_count: null` and an explicit status/reason in
`receipt-inventory-post-2026-06-10-report.json`. The remaining parse gaps are
five historical summary-only Claude receipts and one empty Codex receipt; none
contains a complete, safely countable finding body.

Canonical generation now uses `--tracked-only`. This prevents a committed
inventory from naming raw receipts that do not exist in the same git state.
The full-worktree recovery view currently sees 282 candidates, including 11
untracked raw receipts, with 270 parseable, six parse gaps, six failures, and
1,625 explicit findings. Those 11 receipts must be retained or dispositioned
in their owning review lanes before they can enter canonical reconciliation.

The prior 95 gaps were not treated as zero-finding reviews. The format-specific
parser expansion safely recovered explicit Markdown severity tags, severity
sections, exact severity-summary counts, explicit clean variants, and matching
parsed/raw ACCEPT verdicts while preserving ambiguous prose and failed legs as
gaps.

## Reconciliation result

The canonical engine reports:

- archive complete: **false**
- reconciled parseable receipts: **24 / 259 (9.2664%)**
- receipt count mismatches: **235**
- receipt hash mismatches: **0**
- orphaned event receipts: **0**
- failed-leg gaps: **6**

The 24 reconciled receipts are predominantly explicit zero-finding receipts,
plus the complete P4 v1.0.253 board, the P4 v1.0.254 Codex receipt, and the
complete P5 v0.1.138 board. They do not imply that the remaining campaign
findings have been truth-audited into the event ledger.

Every unresolved row remains visible rather than being silently converted into
zero findings.

## Event migration result

All eight Codex-subscription findings from the P4 v1.0.254 receipt are now in
the canonical JSONL ledger, with one-to-one dispositions and independent
evidence in `P4_v1.0.254_truth_audit.md`. The original bounded migration added:

- `fev1_2fff0f9560874be03fcd0818` — non-portable semantic validator
- `fev1_f6f3906e33e1072eedfa78cd` — aggregate-only quarantine validation

The evidence-bound completion adds:

- `fev1_98dd561423b02b0e6577ca08` — false production-calibration model card
- `fev1_fe8359a1960052dbf95e3d77` — unreconstructable historical classifier
- `fev1_28a69ad2e1877ff28789421f` — overclaimed definitive bias mitigation
- `fev1_9aaf329e7053abacae099172` — unavailable full-catalog metadata
- `fev1_b58ecc058c557326730d3aed` — unsupported Figure 3 causation
- `fev1_3a094efca7be1d4ad3cf623c` — prospective DOI/archive gate

The exact receipt now reconciles **8 / 8**. The ledger represents
**21 / 1,574 explicit findings (1.3342%)** overall after the next bounded batch.

The P4 v1.0.253 board contributes 13 additional one-to-one events:

- Grok: four findings, including two standing disclosed gates, one verified
  direct-manifest defect, and one falsified re-flag;
- Gemini: three findings, preserving two editorial opinions and one falsified
  missing-disclosure claim;
- Codex subscription: six verified release and presentation defects, including
  the unreproducible Catalog B tier and missing row-semantic validation.

All three v1.0.253 receipts now reconcile exactly at **4/4**, **3/3**, and
**6/6**. No historical event was inferred from a synthesis, closure note, or
provider verdict alone.

The declarative, hash-validating importer
`tools/import_truth_audit_events.py` now removes the repeated manual event
construction step. A batch must bind the exact truth-audit bytes, every raw
receipt's bytes, the canonical inventory row and expected finding count, paper
and PDF identity, timestamps, reviewer route, finding-level truth disposition,
pattern state, and closure state. It validates every canonical event before an
explicit `--append`; exact replay is idempotent. Focused importer tests cover
valid construction, audit/receipt mutation, count mismatch, and replay.

The first importer-driven batch,
`batches/P5_v0.1.138_truth_audit_events.json`, adds all 11 findings from the
unanimous minor-only P5 board: four verified manuscript minors, four standing
release/scope gates, and three editorial requests. Its Grok, Gemini, and Codex
receipts reconcile at **3/3**, **4/4**, and **4/4**. The ledger now represents
**32 / 1,574 explicit findings (2.0330%)**.

Because finding events are immutable, later closures are now recorded in the
separate append-only `finding-closure-events-v1.jsonl` ledger rather than
rewriting event identity. `tools/finding_closure_event.py` verifies that the
referenced finding exists and that every evidence path has the declared bytes
at the exact closure commit, then produces
`finding-closure-projection.json`.

The first four closure events bind P5's verified v0.1.138 manuscript minors to
commit `81b7bd56` and version `v0.1.139-2026-07-16`: interaction prose,
shared-reference covariance, the T-Web parent/subset explanation, and stable
tie-breaking. These are source closures, not a claim that standing release,
companion-paper, human, or venue gates are closed, and no later confirmation
board is inferred.

## Remaining work

1. Normalize the remaining 1,542 explicit findings against truth-audit rows,
   preserving falsified, stale, opinion, standing, and unresolved dispositions.
2. Recover the five incomplete historical summaries and one empty Codex receipt
   from preserved raw transcripts if available; otherwise retain them as
   permanent explicit archive gaps.
3. Retain or disposition the 11 currently untracked raw receipts in their owning
   review lanes before adding them to canonical inventory.
4. Re-run the canonical `finding_event.py reconcile` command after each bounded
   batch. A wave is not archive-complete until count/hash mismatches and orphaned
   events are zero.

Generated artifacts:

- `receipt-inventory-post-2026-06-10.json`
- `receipt-inventory-post-2026-06-10-report.json`
- `receipt-reconciliation-post-2026-06-10.json`
- `finding-events-v1.jsonl`

Generator: `tools/build_finding_receipt_inventory.py`; focused regression tests:
`tools/tests/test_build_finding_receipt_inventory.py`.
