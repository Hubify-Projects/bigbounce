# Consistency Relation Validation — Status

**Date:** 2026-03-23

---

## Phase 2B Result: Individual Vertex Integrals DIVERGE

The attempt to compute f_NL(ε) by numerically evaluating individual cubic action time integrals gave f_NL ~ 10⁹ (divergent). This is NOT an error — it's the known cancellation structure of the matter-bounce bispectrum.

**Why this happens:** Each cubic vertex integral involves growing-mode products that scale as (-τ)^{-n} with n > 0, giving divergent time integrals near the bounce. The PHYSICAL f_NL emerges from cancellations between all 4 vertex contributions. Computing one vertex in isolation gives a divergent answer.

This is exactly the difficulty documented in `fnl_combined_integrand/` and is the fundamental reason the -35/8 vs -35/16 ambiguity has been hard to resolve — the individual contributions are much larger than their sum, so small normalization differences produce O(1) changes in the final answer.

## What We Do Have

### Three independent estimates of f_NL(ε) behavior

| Method | Result | Grade |
|--------|--------|-------|
| Explicit ε prefactor scaling | c ≈ 2, correction ~0.6% | ESTIMATE (C) |
| Mode function + power spectrum scaling | c ≈ 18, correction ~8% | SCALING MODEL (C+) |
| Full cubic integral (Phase 2B) | DIVERGENT (single vertex) | FAILED |

### Why the scaling model (c ≈ 18) is likely an OVERESTIMATE

The scaling model computes f_NL(ε)/f_NL(3/2) from:
1. The ratio of explicit ε prefactors (small effect, c ~ 2)
2. The ratio of power spectra P(ε)/P(3/2) (large effect, c ~ 16)

Factor 2 is large because the power spectrum depends on the mode function growth rate, which changes significantly with ε near the singular point ε = 3/2.

BUT: f_NL = B / P², not just ∝ 1/P. The bispectrum B also depends on the mode functions through the time integrals. If B scales similarly to P^{3/2} (which it does for growing-mode-dominated processes), then:

f_NL ∝ B/P² ∝ P^{3/2}/P² = P^{-1/2}

In that case, the f_NL ratio would scale as P^{-1/2}, giving:
c ~ (1/2) × (d ln P / d ε) ~ 8 (roughly half of 16)

But we didn't compute d ln B / d ε independently, so we can't separate the B and P contributions. The true coefficient c is somewhere between 2 (prefactor only) and 18 (full power spectrum scaling).

### Best estimate

Given the cancellation structure, the most defensible statement is:

**The ε correction to f_NL is between 1% and 8% at the Planck spectral tilt.**

More precisely:
- Lower bound (prefactor only): correction ~0.6%, f_NL ≈ -4.35
- Upper bound (full P scaling): correction ~8%, f_NL ≈ -4.02
- Central estimate: correction ~3-5%, f_NL ≈ -4.2

All are within SPHEREx measurement uncertainty (σ ≈ 0.7).

## Impact on the Consistency Relation

The consistency relation f_NL(n_s) survives in form but the slope is uncertain:

| Version | Slope | f_NL at n_s = 0.9649 |
|---------|-------|---------------------|
| Explicit prefactors only | -0.73 × (n_s-1) | -4.349 |
| Full P scaling (likely upper bound) | -10.0 × (n_s-1) | -4.023 |
| Central estimate | ~-3 × (n_s-1) | ~-4.27 |

## Paper Recommendation

The paper should say:

> "The leading-order ε correction from the quasi-dust equation of state (w = -0.003) shifts f_NL by between 0.6% and 8% (the range reflecting uncertainty in the mode-function-dependent bispectrum integral scaling). At the Planck best-fit spectral tilt n_s = 0.9649, the corrected prediction is f_NL ∈ [-4.35, -4.02], well within the SPHEREx measurement uncertainty σ ≈ 0.7. The consistency relation f_NL(n_s) = -35/8 + c(n_s - 1) with c ∈ [-0.7, -10] provides a testable single-parameter connection between the spectral tilt and non-Gaussianity."

This is honest: it acknowledges the range, explains why, and notes it's within measurement uncertainty.

## What Would Close the Gap

Computing f_NL(ε) exactly requires evaluating ALL 4 cubic action integrals simultaneously with their cancellations preserved. This is the same calculation that would also definitively resolve -35/8 vs -35/16. It requires:

1. Implementing Cai's full cubic action in cosmic time
2. Using the ODE-computed mode functions (which work fine)
3. Integrating the COMBINED integrand (all terms summed before integration)
4. Doing this at several ε values near 3/2

This is feasible but technically demanding — it's a multi-session project.
