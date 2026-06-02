---
status: confirmed
proposed_by: r-round-pattern-mine
proposed_date: 2026-04-30
confirmed_date: 2026-06-02
review_target: catalog
source: R42-NEW-025
---

# Pattern 025 — Mathematically-impossible attribution (claim incompatible with author's own equation)

**First seen**: P4 R42 R3 (Math/Logic adversarial reviewer) — §IV.B
attributes 9.5σ f_CW = 0.4974 deficit to "sub-percent asymmetry in training
labels". TTA equation P_CW^eq = ½(P_CW^orig + P_CCW^flip) is symmetric in
CW/CCW; only mathematical way for f_CW < 0.5 is asymmetric leakage into
NOT_SPIRAL class. Paper's own equation contradicts its prose attribution.
**Severity**: high (load-bearing physics-attribution wrong; reviewer-routing
implication: only the math-rigor reviewer caught it)
**Frequency**: 1 confirmed instance (P4 R42); structural rarity reflects
the high bar — only adversarial-math reviewers catch these

**Detection**: for every residual / deficit / unexpected offset, walk the
math: does the cited mechanism, as written in the paper's own equations,
actually have a sign/magnitude/form consistent with the observed residual?
If the equation is sign-symmetric and the residual is asymmetric, that's
pattern-025.

## What it looks like

> R42 P4 R3 B (Math/Logic): "§IV.B attributes the 9.5σ f_CW = 0.4974 deficit
> from 0.5 to 'sub-percent asymmetry in CW/CCW training labels.' But the TTA
> equation cited in §III.D is P_CW^eq(x) = (P_CW^orig(x) + P_CCW^flip(x))/2.
> This is symmetric under CW↔CCW. Asymmetric training labels would shift
> P_CW^orig and P_CCW^flip in the SAME direction, not opposite. The
> mathematically-possible mechanism is asymmetric leakage into the NOT_SPIRAL
> class. The paper's own equation contradicts its prose attribution."

## Truth-audit verdict

VERIFIED. R3 was the only R42 reviewer who walked the algebra; all other
reviewers accepted the prose attribution.

## Examples observed

- P4 R42 §IV.B: TTA equation sign-symmetric vs asymmetric deficit
  attribution (canonical case)
- (predicted, not observed) Any paper attributing a residual to a mechanism
  the cited equation cannot produce. Pattern recurs whenever closure-prose
  is written by an LLM that does not re-walk the algebra.

## Root cause

Two distinct skills are conflated: (a) writing the closure prose, and
(b) checking the math. The closure-author writes a plausible-sounding
attribution but does not re-derive that the cited equation actually has
the right sign / form to produce the observed effect. Adversarial math
reviewers catch it; consensus reviewers do not.

## Pre-review check

```bash
# Step 1: list every residual / deficit / offset / null / non-zero in the
#   paper that has a prose attribution
# Step 2: for each, identify the equation the paper says causes it
# Step 3: check sign / magnitude / form compatibility:
#   - is the equation sign-symmetric in the variable being attributed?
#   - is the magnitude order-compatible (within 2 OOM)?
#   - does the equation produce a residual at all under the cited mechanism?
# Step 4: any mismatch → BLOCKER. Either revise the attribution or revise
#   the equation.
```

Routing rule: any paper with a non-trivial residual attribution MUST be
reviewed by a math/symbolic reviewer (Wolfram + DeepSeek R1 via
`/wolfram-deepseek-verify`) before external dispatch. Consensus reviewers
will accept the attribution; only adversarial-math catches the impossibility.

## Related patterns

- Pattern 022 (closure-narrative-instead-of-derivation) — sibling:
  022 is prose where math was demanded; 025 is prose that contradicts
  the math
- Pattern 007 (reviewer arithmetic confabulation) — opposite direction:
  007 is reviewer math wrong, 025 is author math wrong
- Pattern 033 (prose-asserted-prefactor acceptance) — same root: load-
  bearing prefactor / attribution accepted without derivation
