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
- reconciled parseable receipts: **17 / 259 (6.5637%)**
- receipt count mismatches: **242**
- receipt hash mismatches: **0**
- orphaned event receipts: **0**
- failed-leg gaps: **6**

The 17 reconciled receipts are predominantly explicit zero-finding receipts.
They do not imply that the 1,574 findings have been truth-audited into the
event ledger.

Every unresolved row remains visible rather than being silently converted into
zero findings.

## Event migration result

Two findings were appended to the canonical JSONL ledger. Both are the
unambiguous Codex-subscription findings C-M1 and C-M2 from the P4 v1.0.254
receipt, with one-to-one dispositions and independent evidence in
`P4_v1.0.254_truth_audit.md`:

- `fev1_2fff0f9560874be03fcd0818` — non-portable semantic validator
- `fev1_f6f3906e33e1072eedfa78cd` — aggregate-only quarantine validation

This is **2 / 1,574 explicit findings (0.1271%)**. The P4 receipt correctly remains a
`COUNT_MISMATCH` because six other findings in that receipt have not yet been
migrated. No historical event was inferred from a synthesis, closure note, or
provider verdict alone.

## Remaining work

1. Normalize the remaining 1,572 explicit findings against truth-audit rows,
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
