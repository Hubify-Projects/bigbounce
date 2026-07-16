# Post-2026-06-10 finding-receipt reconciliation

This is a bounded migration against the canonical SciStack
`r-round-finding-archive` contract introduced at `ba36b4c`. The cutoff is
exclusive: path-dated review rounds from 2026-06-11 onward are eligible.

## Deterministic inventory result

- Candidate raw review receipts: **264**
- Receipts with an explicit tagged-finding count or explicit clean statement:
  **169 / 264 (64.0152%)**
- Explicit findings represented by those parseable receipts: **1,198**
- Explicit parse-gap rows: **95 / 264 (35.9848%)**
- Failed-leg rows detected by the bounded parser: **0**

The 95 gaps are not treated as zero-finding reviews. Each is retained as a
`status: parse_error`, `finding_count: null` inventory row, with its reason in
`receipt-inventory-post-2026-06-10-report.json`.

## Event migration result

Two findings were appended to the canonical JSONL ledger. Both are the
unambiguous Codex-subscription findings C-M1 and C-M2 from the P4 v1.0.254
receipt, with one-to-one dispositions and independent evidence in
`P4_v1.0.254_truth_audit.md`:

- `fev1_2fff0f9560874be03fcd0818` — non-portable semantic validator
- `fev1_f6f3906e33e1072eedfa78cd` — aggregate-only quarantine validation

This is **2 / 1,198 explicit findings (0.1669%)** and **0 / 169 fully
reconciled parseable receipts**. The P4 receipt correctly remains a
`COUNT_MISMATCH` because six other findings in that receipt have not yet been
migrated. No historical event was inferred from a synthesis, closure note, or
provider verdict alone.

## Remaining work

1. Normalize the remaining 1,196 explicit findings against truth-audit rows,
   preserving falsified, stale, opinion, standing, and unresolved dispositions.
2. Manually normalize the 95 parse-gap receipts or add receipt-format-specific
   parsers with fixtures; do not turn missing counts into zeroes.
3. Re-run the canonical `finding_event.py reconcile` command after each bounded
   batch. A wave is not archive-complete until count/hash mismatches and orphaned
   events are zero.

Generated artifacts:

- `receipt-inventory-post-2026-06-10.json`
- `receipt-inventory-post-2026-06-10-report.json`
- `receipt-reconciliation-post-2026-06-10.json`
- `finding-events-v1.jsonl`

Generator: `tools/build_finding_receipt_inventory.py`; focused regression tests:
`tools/tests/test_build_finding_receipt_inventory.py`.
