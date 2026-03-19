# 05: Direct Comparison to Literature

---

## The Three Literature Values

| Source | f_NL | How obtained |
|--------|------|-------------|
| Cai et al. (2009) | -35/8 = -4.375 | Full in-in, analytical A_T extraction |
| Li & Brandenberger (2014) | -35/16 = -2.1875 | Full in-in, different convention? |
| Our computation (Term 1 only) | +1.5613 | Numerical, single vertex |

---

## What Our Computation Covers

We evaluated the dominant Maldacena vertex ε²a²ζ(ζ')² numerically.

This is ONE of 6 terms in the full cubic action. For ε = 3/2, the other terms contribute at comparable order (not suppressed as they would be for slow-roll inflation).

**Our +1.56 result for Term 1 is NOT directly comparable to Cai's -35/8 (which includes ALL terms).**

---

## Key Structural Finding

The fact that Term 1 alone gives a POSITIVE value (+0.31 intrinsic, +1.56 total) while the full answer is NEGATIVE (-35/8 = -4.375) means:

**The other terms contribute at least -4.375 - 1.56 = -5.94 to the total f_NL.**

This is a LARGER contribution than Term 1 itself, with opposite sign. The bispectrum in the matter bounce is dominated by interference between multiple cubic action vertices, not by any single term.

This is qualitatively different from slow-roll inflation, where Term 1 dominates everything.

---

## Status of the Factor-of-2 Discrepancy

From the execution phase (file 06):
- The factor-of-2 between Cai (-35/8) and Li-Brandenberger (-35/16) preserves the numerator 35.
- This is consistent with a systematic convention difference (likely the factor of 2 from the in-in commutator).
- Our numerical computation cannot resolve this discrepancy because it only covers one vertex.

**The convention equivalence f_NL(Planck) = |B|_NL(Cai) in the squeezed limit was PROVEN analytically in the execution phase (file 03/04). This result stands regardless of the numerical limitations here.**

---

## What Would Be Needed for Full Independent Verification

1. **Symbolic computation of all 6 Maldacena terms** — Evaluate the cubic action contributions using Mathematica/SymPy with exact symbolic manipulation, cancelling growing-mode divergences before any numerical step.

2. **Matched asymptotic expansion** — Split each integral into a superhorizon piece (evaluated analytically) and a horizon-crossing piece (evaluated numerically). The growing-mode divergences live entirely in the superhorizon piece and cancel analytically in the ratio.

3. **Cross-check with ADM formalism** — Use the ADM second-order constraint solutions directly (rather than Maldacena's field-redefined form) to reduce the cubic action to a simpler form with fewer terms.

4. **Lattice computation** — Evolve the full nonlinear field equations on a lattice and extract the bispectrum statistically. This bypasses the in-in formalism entirely but requires significant computational resources.

None of these approaches is achievable with scipy.integrate alone.
