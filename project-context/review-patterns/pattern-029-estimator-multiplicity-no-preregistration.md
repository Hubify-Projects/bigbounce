---
status: confirmed
proposed_by: r-round-pattern-mine
proposed_date: 2026-05-15
confirmed_date: 2026-06-02
review_target: catalog
source: P4-pattern-023 estimator-multiplicity-no-preregistration
---

# Pattern 029 — Estimator multiplicity with no pre-registered primary

**First seen**: P4 v1.0.66 external B9 — paper presents three distinct
σ-estimators for the catalog asymmetry (formal-Fisher, block-bootstrap,
jackknife) yielding 264σ / 18σ / 22σ. Headline selects the most-null (18σ),
no Methods pre-registration of which estimator is primary.
**Severity**: high (garden-of-forking-paths; reviewers reasonably suspect
post-hoc selection)
**Frequency**: 3+ instances
- P4 v1.0.66 B9: 3 distinct σ-estimators, headline picks the most-null
- P3 R42: multiple anomaly-score thresholds (S = 3, 5, 7), headline picks
  S=5
- P1A: 2 distinct constraint methods (MCMC vs Fisher), headline picks
  whichever is tighter per-section

**Detection**: count distinct sigmas / p-values / threshold values for the
same physical quantity in the paper. ≥3 distinct estimators of the same
observable + headline selects the most-favorable = BLOCKER. Require
explicit Methods pre-registration of the primary estimator.

## What it looks like

> P4 v1.0.66 B9 (ChatGPT REJECT-AND-RESUBMIT, Gemini DR REJECT): "§IV.B
> reports σ = 264 (formal Fisher), σ = 18 (block-bootstrap), σ = 22
> (jackknife). The abstract uses σ = 18. Two questions: (a) why is σ=18
> the headline, (b) why does the paper present all three without
> pre-registering one. Without pre-registration this is garden-of-
> forking-paths."

## Truth-audit verdict

VERIFIED. The Houston standing fix was to pre-register block-bootstrap
as primary in Methods (because the 264σ formal Fisher ignored survey
covariance) and report the others as robustness checks — but this should
have been done BEFORE the round, not in response to it.

## Examples observed

- P4 v1.0.66 B9 (the canonical case)
- P3 R42 anomaly-score threshold selection
- P1A constraint-method selection per-section

## Root cause

LLM-author defaults to "show all numbers and let the headline pick the
nicest one." Without an explicit Methods section that names the primary
estimator BEFORE results are computed, every analysis is implicitly post-hoc.

## Pre-review check

```bash
# Step 1: for every named observable (σ_X, p-value, threshold, R², etc),
#   grep the paper for ALL reported values
grep -nE 'σ\s*=\s*[0-9]+|p\s*=\s*[0-9.]+|R²\s*=\s*[0-9.]+|S\s*>\s*[0-9]+' <paper.tex>

# Step 2: count distinct values per observable. >=3 distinct estimators of
#   the same observable → flag for pre-registration check.

# Step 3: search Methods section for a sentence of the form:
#   "We pre-register [estimator X] as primary; [estimator Y, Z] are
#    reported as robustness checks."
# If no such sentence → BLOCKER. Add it.

# Step 4: verify headline = pre-registered primary, not the most-null
#   alternative.
```

Standing rule: every quantitative observable that has more than one
estimator in the paper requires a Methods sentence naming the primary
BEFORE the Results section. Other estimators are robustness checks.

## Related patterns

- Pattern 023 (trivial-fix-refused-false-cost) — overlapping: refusing
  to pre-register often comes with "leave to revision" framing
- Pattern 024 (figure-violates-cited-threshold) — sibling: post-hoc
  threshold selection on figures is the visual cousin of estimator
  multiplicity in numbers
- Pattern 030 (round-to-round-regression-drift) — estimator selection
  often regresses across rounds (closed in N, reopened with a different
  primary in N+1)
