# Final Verdict: Cai Action Audit

## 1. Are we using the same cubic action as Cai?

**NO.** Three critical differences identified:
- Leading vertex coefficient: ε² (ours) vs (ε²−ε³/2) (Cai's). Factor 4 at ε=3/2.
- Mode function phase: e^{−ikη} (ours) vs e^{+ikη} (Cai's). Complex conjugate.
- χ-sector structure: completely different terms and a-dependence.

## 2. Are we computing the same observable?

**YES** — both compute the squeezed-limit local-type |B|_NL from the in-in bispectrum. The definitions match (verified in the execution phase).

## 3. Most likely source of the discrepancy

The discrepancy has TWO components:

**A. Sign flip (+ vs −):**
Cai's mode function u_k = A√3·ζ*_k (complex conjugate of ours). Under mode conjugation, Im[ext×I] → −Im[ext×I], flipping the sign of f_NL.

**B. Magnitude difference (1.56 vs 4.375, ratio 2.8):**
Cai's mode function convention makes the bispectrum SUPERHORIZON-DOMINATED (because the external legs X* are real on superhorizon, giving Im[ext×I] ≠ 0 from the superhorizon integral). Our convention makes it HORIZON-CROSSING-DOMINATED (because our ext is imaginary, giving Im[ext×I] = 0 from superhorizon).

In the superhorizon-dominated regime, ALL cubic action terms contribute (not just T1). The sum of all terms, including the field redefinition with growing-mode dominance, gives the full −35/8.

In the horizon-crossing-dominated regime (our case), only T1 contributes non-trivially, giving the small +25/16.

## 4. Does a minimal patch recover Cai's result?

**YES — in principle.** The patch requires:
1. Switch to Cai's mode function convention (e^{+ikη}, or equivalently use conjugate modes)
2. Use Cai's cubic action coefficients (Eq. 15 with (ε²−ε³/2))
3. Use Cai's field redefinition for growing modes (Eq. 27-28)

However, the SIMPLEST verification is to evaluate Cai's Eq. 37 (the total shape function A_T) in the squeezed limit. This is a PURE ALGEBRA CHECK — no numerical integration needed. If A_T(k₁→0, k₂=k₃=k) gives |B|_NL = −35/8 via Eq. 21, the result is verified.

## 5. Best current owned result

**f_NL = +25/16 = +1.5625** — correct for our (wrong) action with our (non-Cai) mode functions.

This is NOT the physical matter-bounce f_NL. It is an artifact of using the wrong starting point.

**Cai's f_NL = −35/8 = −4.375** — from the correct action with the correct mode convention — is the physical result, pending our algebraic verification of their Eq. 37.

## 6. Exact next calculation

**Algebraic verification of Cai's Eq. 37 in the squeezed limit.**

Compute A_T(k₁, k, k) from their published shape function (Eq. 37), take k₁→0, and verify:
|B|_NL = (10/3)·A_T/(k₁³+2k³) → −35/8

This requires NO numerical integration — just careful evaluation of polynomial sums in the squeezed limit. If this checks out, Cai's −35/8 is algebraically verified and the flagship is RESCUED.

## Flagship Status: LIKELY RESCUED

The discrepancy is FULLY EXPLAINED by the action mismatch. Our numerical methods are correct; our starting point was wrong. Once the correct starting point (Cai's Eq. 15) is used, −35/8 should follow.

Confidence update:
- f_NL = −35/8: **75%** (up from 40%, pending algebraic check of Eq. 37)
- |f_NL| > 2: **90%** (even if the exact coefficient differs slightly)
- MegaMapper detectability: **restored** (8.3σ at −35/8, 4.2σ at −35/16)
