---
status: confirmed
proposed_by: r-round-pattern-mine
proposed_date: 2026-04-30
confirmed_date: 2026-06-02
review_target: catalog
source: R42-NEW-024
---

# Pattern 024 — Figure violates its own cited threshold

**First seen**: P3 R42 B17 — Fig 5 high-z QSO candidates labeled "pass S>5
anomaly cut" but plotted points include AE = 4.32, 4.26, 3.31 (below cut).
**Severity**: medium (caught by attentive reviewers, easily fixed, but
load-bearing when a figure is the headline result)
**Frequency**: 1 confirmed instance with a structural prediction that any
threshold-figure carries this risk

**Detection**: for every figure caption that mentions a threshold
("pass S>X", "above Y σ", "AE > Z"), parse the plotted data points and
verify the threshold is enforced. If figure includes points below the cited
cut, either caption is wrong OR a different scale is in use (which must be
disclosed in the caption).

## What it looks like

> R42 P3 R1 P3-07: "Figure 5 caption claims 'all 12 high-z QSO candidates
> pass the anomaly score S > 5 selection cut.' Three of the 12 plotted
> points have AE values of 4.32, 4.26, and 3.31. Either AE ≠ S (then
> disclose the conversion), or the cut isn't being enforced (then fix the
> figure), or the caption is wrong (then fix the caption)."

## Truth-audit verdict

VERIFIED. The fix was a caption-clarification — the AE shown was on a
different scale than the S cut. But for ~10 days the figure looked like
it violated its own threshold.

## Examples observed

- P3 R42 Fig 5: high-z QSO AE vs anomaly score S confusion

(Single-instance pattern; included in the catalog because it predicts a
class of failure for every threshold figure in every paper.)

## Root cause

Two scales (anomaly score S, autoencoder error AE) co-existed in P3.
Figure plotted AE; caption referenced S threshold. Closure pipeline did
not have a "every figure-caption threshold is enforced on plotted data"
check. The same risk applies to any paper with a multi-scale figure.

## Pre-review check

```bash
# Step 1: extract figure captions that mention thresholds
grep -nE '\\caption\{[^}]*(\\geq|\\leq|>|<|pass|cut|threshold|above|below)' <paper.tex>

# Step 2: for each hit, identify the data source (referenced .csv / figure
#   notebook) and verify the threshold is enforced on the plotted points.
#   Manual review on first pass; can be automated per-paper with a
#   figure-spec table.

# Step 3: every threshold figure-caption must also state the SCALE of the
#   threshold ("S > 5 where S is the anomaly score on the test set"), not
#   just the value.
```

## Related patterns

- Pattern 020 (load-bearing disclosure buried) — sibling: 024 is the
  figure-side of "the caption says one thing but the data says another";
  020 is the abstract-side
- Pattern 029 (estimator-multiplicity-no-preregistration) — overlapping
  cause when the figure plots one estimator while caption cites another's
  threshold
