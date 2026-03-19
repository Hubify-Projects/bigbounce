# 03: Numerical Results

---

## Executive Summary

The numerical computation reveals a STRUCTURAL LIMITATION of the direct integration approach for the matter bounce bispectrum. The growing mode (ζ ∝ |η|⁻³) creates power-law divergences in the bispectrum integral that must cancel analytically in the ratio f_NL = B/(P·P). For the dominant vertex (Term 1), this cancellation works numerically. For subdominant vertices involving the constraint variable χ, the cancellation FAILS numerically due to catastrophic loss of precision.

**Bottom line:** We cannot independently verify -35/8 via brute-force numerical integration. The verification requires following Cai et al.'s analytical approach, which handles the divergence cancellation symbolically before evaluating any integrals.

---

## Result 1: Term 1 Only (Converged)

The dominant Maldacena vertex ε²a²ζ(ζ')² gives a well-converged result:

| Parameter | Value |
|-----------|-------|
| f_NL (intrinsic, Term 1) | +0.3113 |
| f_NL (field redefinition) | +1.2500 |
| f_NL (total, Term 1 only) | **+1.5613** |

### Convergence (Term 1 only, from v1):

| Test | Range | f_NL | Stable? |
|------|-------|------|---------|
| η_f variation | -0.1 to -0.001 | 1.560–1.562 | YES |
| Squeeze ratio | 0.1 to 0.0001 | 1.561–1.562 | YES |
| iε regulator | 1e-2 to 1e-6 | 1.561 | YES |
| UV cutoff | -100 to -5000 | 1.561–1.562 | YES* |

*Mild degradation at x_early = -10000 due to oscillatory integral accumulation.

**Term 1 alone gives f_NL ≈ +25/16.** This does NOT match either Cai (-35/8) or Li-Brandenberger (-35/16).

**This means the other cubic action terms are essential.** For ε = 3/2 (not small), "subleading" terms in the Maldacena action contribute at the same order.

---

## Result 2: Full Cubic Action (NOT Converged)

Including all 6 Maldacena cubic action terms:

| Term | f_NL contribution | Converged? |
|------|-------------------|------------|
| T1: ε²a²ζζ'² | +0.311 | YES |
| T2: ε²a²ζ(∂ζ)² | -0.000 | YES (negligible) |
| T3: -2εa²ζ'(∂ζ)(∂χ) | -0.000 | YES (negligible) |
| T4: (ε/2)d(ε/H)/dη·a²ζ²ζ' | -0.002 | MARGINAL |
| T5: (ε/2)∂²ζ(∂χ)² | -0.000 | YES (zero in squeezed limit) |
| T6: (ε/4)d(ε/H)/dη·∂²ζ·χ² | +1.910 | **NO** |

**Term 6 dominates but does NOT converge:**

| Test | f_NL (all terms) | Problem |
|------|-----------------|---------|
| xf = -0.10 | 1815.7 | Wildly wrong |
| xf = -0.01 | 3.47 | |
| xf = -0.001 | 0.94 | Different from above |
| r = 0.001 | 3.47 | |
| r = 0.0001 | 188.3 | Diverges with r |

---

## Root Cause Analysis

### Why Term 1 converges but Terms 4,6 don't:

**Term 1:** The integrand has structure η⁴·g_{k1}·(g'_k)². In the squeezed limit:
- The long-mode g_{k1} ∝ 1/(r^{3/2}η³) and the short-mode g'_k are oscillatory.
- The divergent part (from the growing mode near η → 0) is PURELY REAL in the product ext·I.
- Im[ext·I] (which determines B) extracts only the oscillatory/horizon-crossing piece.
- The ratio B/(P·P) is finite and η_f-independent.

**Terms involving χ:** The constraint χ_k = -(3/2)a²ζ'_k/k² introduces EXTRA factors of η⁴ (from a²).
- χ_{k1} ∝ η⁴/(r²)·z1'(η) — this has a different power of η AND r than the direct mode functions.
- In the product ext·I, the divergent part is NO LONGER purely real.
- The growing-mode cancellation that makes f_NL finite requires cancellation between DIFFERENT terms (not within a single term).
- Numerically, this means computing B_{total} = B_1 + B_3 + B_4 + B_6 where individual B_i diverge but the sum is finite. Standard floating-point arithmetic cannot handle this.

### The fundamental issue:

The constraint variable χ couples the Maldacena terms. After substituting χ in terms of ζ', the resulting expression has higher powers of 1/η and 1/r that individually diverge. The PHYSICAL bispectrum (which is finite) requires cancellations BETWEEN terms. These cancellations must be performed analytically, not numerically.

**This is exactly what Cai et al. do:** they evaluate the A_T shape function analytically, performing the growing-mode cancellations symbolically before extracting the numerical coefficient -35/8.

---

## What We Can and Cannot Conclude

### CAN conclude:
1. The dominant vertex (Term 1) alone gives f_NL ≈ +1.56. This is a CONVERGED, VERIFIED result.
2. The full f_NL = -35/8 requires contributions from ALL Maldacena cubic action terms. It is NOT dominated by a single vertex.
3. The field redefinition contributes exactly +5/4 = +1.25.
4. Terms 2, 3, 5 are negligible in the squeezed limit (verified numerically).
5. Terms 4 and 6 (which involve d(ε/H)/dη and χ²) are essential but cannot be evaluated by straightforward numerical integration.

### CANNOT conclude:
1. Whether f_NL = -35/8 or -35/16 or something else.
2. The independent numerical value of the full bispectrum.

### What this means for the flagship:
- The numerical verification of f_NL = -35/8 is BEYOND the reach of direct scipy integration.
- A proper verification requires either:
  (a) Following Cai's analytical derivation step by step (symbolic computation)
  (b) Using a specialized integration scheme that handles the growing-mode cancellations (e.g., matched asymptotic expansions, or subtracting the divergent piece analytically before integrating)
  (c) Cross-checking with an independent symbolic algebra system (Mathematica, FORM)
- The STATUS of f_NL = -35/8 remains: CLAIMED BY CAI, NOT YET INDEPENDENTLY VERIFIED.
