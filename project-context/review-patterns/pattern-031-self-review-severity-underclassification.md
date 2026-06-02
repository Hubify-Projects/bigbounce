---
status: confirmed
proposed_by: r-round-pattern-mine
proposed_date: 2026-05-08
confirmed_date: 2026-06-02
review_target: catalog
source: CCAI-cluster-pattern-019 self-review-severity-under-classification
severity_class: meta
---

# Pattern 031 — Self-review severity-under-classification (CCAI optimism bias)

**First seen**: CCAI cluster 2026-05-08 to 2026-05-10 — CCAI self-review
classifies as MINOR/MAJOR what external cross-vendor calls BLOCKER. Two
strong cases observed in single cluster (P3 Fisher floor R47-m3 →
OOOOO-B3; P2 BF gameability R43-M4 → OOOOO-B5).
**Severity**: high (meta — corrupts the convergence-exit gate)
**Frequency**: amplification ratio of CCAI : external = 4 : 50 ≈ **12.5×**
findings amplification when going from same-vendor self-review to
cross-vendor external review
**Detection**: compare CCAI severity tags vs external severity tags on
findings present in both review types.

## What it looks like

> CCAI R47-m3 (MINOR): "Fisher-floor estimator may slightly under-estimate
> covariance for small n_eff."
>
> External OOOOO-B3 (BLOCKER): "Fisher-floor estimator is unphysical at the
> reported n_eff = 47 effective bins; covariance is unbounded below.
> Headline σ depends on this estimator. This is a load-bearing methodology
> error, not a minor caveat."

Same finding, severity gap of 2 (MINOR → BLOCKER).

## Truth-audit verdict

VERIFIED. The 12.5× amplification ratio (4 CCAI findings vs 50 external
findings on the same paper at the same version, OOOOO round on P3 + P2)
is the cleanest measurement of internal-cycle blindness on record.

## Examples observed

- P3 R47-m3 → OOOOO-B3 (Fisher floor)
- P2 R43-M4 → OOOOO-B5 (BF gameability)
- (predicted) Every paper that has run only CCAI rounds: every closed
  finding should be re-graded against external severity floor

## Root cause

CCAI sub-agents share training data, prompt-shape, and judgment heuristics.
They are configured to find substantive issues but not to grade severity
adversarially. Their default severity floor is "MINOR unless the closure
needs a re-derivation" — which is mid-MAJOR in external grading and
sometimes mid-BLOCKER.

This is structurally the same problem as a research group reviewing its
own work: optimism bias is not a defect of individuals, it is a property
of homogeneous reviewer panels.

## Pre-review check

Operational rule: when CCAI catches an issue that touches a load-bearing
claim (headline number, primary estimator, abstract assertion), apply an
**automatic severity floor of MAJOR** until cross-vendor sign-off.

```bash
# Step 1: identify "load-bearing" findings (CCAI tag → external severity floor)
#   load-bearing = abstract / intro / headline-number / primary estimator
# Step 2: any CCAI MINOR on a load-bearing finding → auto-promote to MAJOR
# Step 3: any CCAI MAJOR on a load-bearing finding → require cross-vendor
#   sign-off before closure
```

Standing rule (from `/readiness-cap-99`): no paper can reach 99% on CCAI
clean alone. ≥1 cross-vendor round must clean on the current version
before the 99% gate opens.

## Related patterns

- Pattern 018 (internal-rounds blind to editorial) — sibling: 018 is the
  COVERAGE side (CCAI doesn't see the issue at all); 031 is the SEVERITY
  side (CCAI sees it but undergrades it)
- Pattern 032 (ccai cross-paper blindness) — sibling: CCAI per-paper
  agents have NO cross-paper visibility
- Pattern 034 (multi-agent-same-vendor-no-diversity) — explains the
  ROOT of the optimism bias: 4 parallel Claude agents are not 4
  independent reviewers
- `/readiness-cap-99` standing skill — enforces the prevention rule

## Meta-finding: the 12.5× amplification ratio

This pattern is the single most-important finding of the 3-month retro.
CCAI rounds (4 parallel same-vendor agents) generate ~4 BLOCKER+MAJOR
findings on a typical paper at "clean" exit. The same paper, when sent
to a 4-vendor cross-vendor round, generates ~50 findings. Ratio ≈ 12.5×.

Direct campaign implication: any paper whose 99% readiness is set on
CCAI-only convergence is implicitly accepting a 12.5× pipeline of
external findings on first publication contact.
