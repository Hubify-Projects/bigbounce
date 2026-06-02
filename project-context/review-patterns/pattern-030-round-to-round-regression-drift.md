---
status: confirmed
proposed_by: r-round-pattern-mine
proposed_date: 2026-05-15
confirmed_date: 2026-06-02
review_target: catalog
source: P4-pattern-008b round-to-round-regression-drift
parent_pattern: 008
---

# Pattern 030 — Round-to-round regression drift (closed in N, reappears in N+K)

**First seen**: P4 v1.0.66 external (5 distinct instances) — multiple
findings closed in R-round N reappeared as fresh BLOCKERs in subsequent
rounds N+K.
**Severity**: high (loop convergence exit criterion implicitly assumes
closures stick; this pattern says they don't always)
**Frequency**: 5+ instances in P4 v1.0.66 alone
- B7: dataset-attribution closure from prior round reflagged
- B11: TTA-equation closure reflagged with stronger language
- M3: closure-introduced regression (sibling of pattern-008) survived
  through 3 rounds before catch
- M4: bibkey closure from R8 reverted by R-multi-true95
- B10: deferral language closed in R6 reappeared in R-multi-round2

**Detection**: at start of every R-round, walk the closed-findings list of
ALL prior rounds and re-verify each one is still closed in the current PDF.

This is the LONGER-TIMESCALE variant of pattern-008. Pattern-008 catches
errors introduced WITHIN a single closure cycle; pattern-030 catches
errors introduced ACROSS rounds when a closure from round N is reverted
or replaced in round N+K (K ≥ 1).

## What it looks like

> P4 v1.0.66 R2-cross-vendor M3: "The Shamir+2022 citation was corrected
> in v1.0.51 (R6 closure GRO-B3 VERIFIED) from Shamir 2022 PASP to
> Shamir 2022 MNRAS. v1.0.66 line 482 reads 'Shamir 2022 PASP' again.
> Closure has regressed."

> P4 v1.0.66 R3 B11: "The TTA factor-of-2 derivation closure from
> v1.0.55 (sentence-only — pattern-022) was removed in v1.0.60 cleanup
> and not restored in v1.0.66. The original finding reopens."

## Truth-audit verdict

VERIFIED in all 5 instances. The pattern is real and recurring.

## Examples observed

(See "Frequency" list above.)

## Root cause

Closure history lives in commit messages + comment-block audit logs.
When a later editor cleans up "verbose" comments or rewrites a section
for clarity, they can revert a closure without knowing it was a closure.
There is no skill that records "this exact word was a closure for this
exact finding — don't change it without re-opening" in a machine-readable
form.

Houston's `bigbounce-close` MCP skill stores closures in Convex with
commit SHA — that's the structural fix. Pattern-030 detection is the
audit layer that catches drift between Convex closure record and current
.tex content.

## Pre-review check

```bash
# Step 1: query Convex / findings-archive for every closed finding
#   tagged status=closed across all prior R-rounds
# Step 2: for each closed finding, re-evaluate against the current .tex:
#   - if the closure was a citation fix, grep for the corrected value
#   - if the closure was a value update, grep for the new value
#   - if the closure was a deletion, verify the artifact is absent
#   - if the closure was an artifact upload, WebFetch the URL
# Step 3: any closure that no longer holds → flag as pattern-030 BLOCKER.
#   Re-close in the current round using the SAME mechanism as the original
#   closure, plus add a `% pattern-030-shielded` comment so future cleanup
#   does not re-revert.
```

Standing rule: every R-round MUST run a previous-round-closure audit
**BEFORE** processing new findings. The output goes to `findings-archive/`
as `<round>_regression_drift_audit.json`.

## Related patterns

- Pattern 008 (closure-introduced regression) — parent. 008 is
  within-round; 030 is across-round.
- Pattern 014 (review-log content in `%`-comment) — overlapping when the
  comment-block audit log is rewritten during cleanup
- Pattern 022 (closure-narrative-instead-of-derivation) — overlapping:
  sentence-only closures regress more often than artifact closures
- `/r-round-closure-propagation-audit` (new skill, proposed) — implements
  this pattern's prevention layer
