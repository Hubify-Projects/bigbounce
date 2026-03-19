# 00: Discrepancy Target Lock

## Critical Correction

The "corrected code" result of f_NL = 2.186 ≈ 35/16 was a **NUMERICAL ARTIFACT**.

Diagnostic proof: the real part of the time integral (Re[I] ~ 10¹⁵) is 7 orders of magnitude smaller than the imaginary part (Im[I] ~ 10²²). The corrected code lost this real part in roundoff noise (computed 10¹⁰ instead of 10¹⁵). But Im[ext×I] = Re[ext]·Im[I] + Im[ext]·Re[I], and the Im[ext]·Re[I] term provides a ~30% physical correction. Losing it inflated f_NL from 0.31 to 0.94.

**V1 is correct for Term 1: f_NL = +1.561 total (+0.311 intrinsic).**

The match with 35/16 = 2.1875 was a coincidence.

## Actual Current State

| Our result (T1 only) | Cai et al. | Li-Brandenberger |
|----------------------|------------|------------------|
| +1.561 (= 25/16) | -4.375 (= -35/8) | -2.1875 (= -35/16) |

Differences:
1. **Sign:** We get positive, they get negative
2. **Magnitude:** We get 25/16, they get 35/8 or 35/16
3. **Completeness:** We compute Term 1 only; Terms 3-6 contribute but are numerically unreliable

## What Must Be Reconciled

The gap between +25/16 (our T1-only) and -35/8 (Cai) or -35/16 (L-B) is:
- Δ = -35/8 - 25/16 = -95/16 = -5.9375 (vs Cai)
- Δ = -35/16 - 25/16 = -60/16 = -3.75 (vs L-B)

This gap must come from:
A. Terms 3-6 contributing ~-4 to -6 in f_NL (plausible given T3's coefficient of 27/2)
B. A sign error in our computation
C. A different vertex structure than what we're computing
D. Or Cai's result being wrong

## Success Criteria

- **Full reconciliation:** Demonstrate that T3-T6 contributions close the gap exactly
- **Partial reconciliation:** Show the gap is consistent with estimated T3-T6 magnitudes
- **Genuine discrepancy:** If T3-T6 can be bounded and the gap persists → either Cai or we are wrong
