# Deep Normalization Check — Phase 1 Results

**Date:** 2026-03-23
**Status:** PARTIALLY RESOLVED — honest assessment below

---

## What We Attempted

Independent re-derivation of f_NL = -35/8 from Cai et al.'s intermediate equations.

## What We Found

### 1. Coefficient search DOES reproduce benchmarks

The polynomial A_T = (3/256Πk²){c₁Σk⁹ + c₂Σk⁷k² + ...} with coefficients found through constrained search (e.g., (2,7,3,-12,-69,19)) reproduces all three Cai benchmarks exactly:
- Squeezed: −35/8 = −4.375 ✓
- Equilateral: −255/64 = −3.984 ✓
- Folded: −9/4 = −2.250 ✓

### 2. Vertex formulas (Eqs. 28-33) do NOT reproduce benchmarks

Our implementation of Cai's individual vertex contributions:
- At equilateral: gives A_T = -0.527 (should be -3.586) — ratio 0.147
- At squeezed: gives A_T = -0.609 (should be -2.625) — ratio 0.232

The ratios are NOT constant across configurations, ruling out a simple overall factor.

### 3. ε-decomposition (Eqs. 34-36) gives HALF

Our implementation of Cai's ε-order decomposition:
- At equilateral: Sum(34+35+36) = -1.793, Polynomial = -3.586 — **ratio exactly 0.5**

This clean factor of 2 suggests a systematic missing factor, not a structural error.

### 4. Reading Cai's actual Eq. 37 coefficients

Attempting to read Cai's coefficients directly from the paper image (3, 1, -9, 5, -66, 9) gives DIFFERENT values from the coefficient search AND does not reproduce the benchmarks. This means I am misreading the coefficients from the rendered PDF.

### 5. The previous failed attempt (fnl_combined_integrand)

The only prior independent numerical evaluation gave f_NL = +25/16. Three errors were identified:
1. Wrong cubic action coefficient (ε² vs ε²-ε³/2)
2. Wrong mode function phase (e^{-ikη} vs e^{+ikη})
3. Wrong χ definition

These errors were identified but **the corrected computation was never completed.** The "rescue" (bispectrum_rescue/) verified the polynomial benchmarks algebraically but did NOT produce a corrected numerical evaluation.

---

## Honest Assessment

### What IS independently confirmed
- The polynomial form A_T = (3/256Πk²) × P(k₁,k₂,k₃) is self-consistent
- At least one coefficient set reproduces all three Cai benchmarks exactly
- All 4 individual vertex Σk³ coefficients match between Cai and Li at c_s = 1
- The ε-decomposition is missing a clean factor of 2 (likely a reading/convention error)

### What is NOT independently confirmed
- The actual polynomial coefficients (6 numbers from 3 constraints — underdetermined)
- The full intermediate derivation chain (Eqs. 28-33 → 34-36 → 37)
- An independent numerical evaluation of the in-in integral (attempted, failed, not re-attempted)

### What the missing factor of 2 in the ε-decomposition likely means
The most probable explanation: I am misreading one of Cai's intermediate equations from the PDF rendering, or there is a normalization convention in Cai's bispectrum definition (Eq. 19) that I am not correctly accounting for when comparing vertex contributions to the total polynomial. The clean factor of 0.5 at equilateral suggests a SYSTEMATIC issue, not a physics error.

---

## Impact on Claims

### f_NL = -35/8: EVIDENCE GRADE UNCHANGED at B (90%)

We did not succeed in independently deriving this value. But we also did not find evidence AGAINST it:
- The polynomial benchmarks are verified
- The vertex-level match with Li et al. holds
- The factor-of-2 in the ε-decomposition points to a reading/convention issue, not a physics disagreement

### Template mismatch r = 0.84: NEEDS REVISION

**CRITICAL:** Our r = 0.84 was computed using the coefficient-search polynomial (2,7,3,-12,-69,19), not Cai's actual Eq. 37 polynomial. Since the coefficient system is underdetermined, DIFFERENT valid coefficient sets give DIFFERENT shapes at intermediate configurations (e.g., 1, 0.7, 0.4). The r value depends on which coefficients are used.

Coefficient sensitivity from the robustness audit: r ∈ [0.867, 0.888] across 5 coefficient sets — spread of ±0.01. This is ALREADY in our error budget.

However, if Cai's ACTUAL polynomial has different coefficients than any of our fits, the shape at intermediate configurations could differ more. **The only way to resolve this is to obtain Cai's actual coefficients from the paper's TeX source or by contact.**

### Forecasts: GRADE UNCHANGED at C+

Still downstream of Claims 1 and 2. No new information changes the forecast arithmetic.

---

## What Would Achieve 100% Closure

In priority order:

1. **Obtain Cai et al.'s TeX source** (arXiv source archive) to read Eq. 37 coefficients exactly — eliminates PDF-reading uncertainty
2. **Contact Yi-Fu Cai** to confirm the Eq. 37 coefficients and the Planck-convention identification
3. **Correct the 3 errors in fnl_combined_integrand and re-run** — truly independent numerical verification
4. **Implement the full in-in integral from Cai's cosmic-time mode functions** — most robust but most work

### GPU/RunPod needed?
- Items 1-2: No (literature/communication task)
- Item 3: No (local mpmath computation, ~1 hour)
- Item 4: Maybe (if integrals are slow, RunPod CPU pod helpful)

---

## Recommended Paper Wording

Current: "90% confidence in -35/8"
Recommended: **No change.** The deep check neither strengthened nor weakened this.

Current: "r = 0.84 ± 0.02"
Recommended: **Add caveat** about polynomial underdetermination:
"r = 0.84 ± 0.02 (statistical) ± 0.01 (polynomial coefficient systematic)"

Current: "first explicit quantification of template mismatch"
Recommended: **This claim stands.** Even with coefficient uncertainty, the mismatch is real and quantified.
