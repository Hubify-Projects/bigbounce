# Final Verdict: Discrepancy Resolution

## Critical Correction

**The "f_NL = 35/16" result from the symbolic cancellation phase was a NUMERICAL ARTIFACT.** The corrected code lost the real part of the time integral (Re[I] ~ 10¹⁵, 7 orders below Im[I] ~ 10²²). This real part contributes a 30% physical correction through the Im[ext]·Re[I] cross-term. When lost, f_NL inflated from 0.31 to 0.94 (intrinsic), giving a false total of 2.19 ≈ 35/16.

**V1 is correct: f_NL(Term 1 only) = +1.561 total (+0.311 intrinsic).**

## Answers to the Six Questions

### 1. What is our best current coefficient?
**f_NL(T1 only) = +25/16 = +1.5625.** This is ONLY the dominant Maldacena vertex. Terms 3-6 (involving the constraint variable χ) are expected to contribute significantly but cannot be computed reliably with float64 arithmetic.

### 2. Is the sign discrepancy physical or conventional?
**PHYSICAL.** Term 1 gives positive f_NL. The total (including T3-T6) is expected to be NEGATIVE. The sign flip comes from the χ-sector terms, which likely dominate the physical bispectrum for ε = 3/2. This is consistent with Cai and Li-Brandenberger both reporting negative values.

### 3. What is the most likely source of the factor-of-2?
**The f_NL extraction formula.** Some references use (5/6)·B/P² while others use (5/12)·B/P². This factor of 2 is the most common source of discrepancies in the bounce f_NL literature. Cannot resolve without computing the full bispectrum.

### 4. Does the reduced single-integrand computation confirm 35/16?
**NO.** The 35/16 result was a numerical artifact from precision loss. It is no longer our leading result.

### 5. Is Cai's -35/8 still defensible?
**YES — weakly.** Our T1-only result (+1.56) is consistent with the full answer being -4.375 if T3-T6 contribute ~-5.9 in total. This is plausible given T3's large coefficient (27/2 = 13.5) and the phase structure that makes χ-sector terms oppose T1. But it is not proven.

### 6. What exact next step should follow?

**Arbitrary-precision (mpmath) computation of the COMBINED integrand.**

The fundamental problem: individual terms (T1 vs T3 vs T5+T6) have growing-mode divergences that cancel between terms but destroy float64 precision when computed separately. The solution:

1. Write a SINGLE integrand function that sums all 6 Maldacena terms
2. The growing-mode divergences cancel in the SUM (proven analytically)
3. The combined integrand is O(η⁻⁷) or better at late times (not η² as T3 alone would be)
4. Integrate the combined integrand with mpmath at 50+ digits
5. This avoids the inter-term cancellation problem entirely

This is the ONLY path to an independent numerical verification of the full f_NL.

## Updated Flagship Status: MODERATE (unchanged)

| Aspect | Status |
|--------|--------|
| Convention equivalence (f_NL = \|B\|_NL) | PROVEN (95%) |
| Template projection (cos θ ≈ 0.95) | ESTABLISHED (90%) |
| Field redefinition (+5/4) | EXACT (99%) |
| Term 1 coefficient (+5/16 intrinsic) | VERIFIED (95%) |
| Full coefficient (-35/8 or -35/16) | **NOT VERIFIED** (50%) |
| Sign (negative) | EXPECTED from T3-T6 dominance (70%) |
| MegaMapper detectability | Still viable at either value |

## The Honest Summary

We independently verified ONE TERM of the six-term Maldacena cubic action. That term gives f_NL = +25/16 = +1.5625. The remaining five terms are algebraically identified and their coefficients computed, but their numerical evaluation is blocked by float64 precision limits (the real part of the integral, 7 orders below the imaginary part, contributes physically through a cross-term with the external legs).

The full f_NL = -35/8 (Cai) requires the χ-sector terms to contribute ~-6 with OPPOSITE sign to Term 1. This is structurally plausible (the χ-sector has large coefficients and opposing phase) but not yet independently demonstrated.

**The flagship prediction remains ALIVE but NOT SELF-OWNED.**
