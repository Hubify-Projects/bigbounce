# Cross-Check: Gemini Round 2 Inputs (2026-03-17)

---

## Gemini Claim: The template projection cosine is a "standalone N4-level discovery"

**Assessment: OVERSTATED, but the observation is valid.**

The template projection problem was already identified in our planning phase (file 06 of fnl_derivation_program). The execution phase (file 05) provides a quantitative estimate: cos(theta) ~ 0.95 ± 0.03. This is based on:

1. The Fisher weight is concentrated in squeezed triangles
2. The matter bounce matches local exactly in the squeezed limit
3. The equilateral contamination is ~10% in amplitude, ~30% in Fisher weight
4. The equilateral-local overlap is 0.46 (not zero)

**Result: cos(theta) is close to 1. The template projection does NOT significantly reduce the signal.**

The cosine does NOT explain the -35/8 vs -35/16 discrepancy (ruled out in file 04: f_NL = |B|_NL in the squeezed limit, so the squeezed coefficient IS the Planck f_NL).

---

## Gemini's Power Spectrum Verification

Confirms P(k,eta) = 1/(6 k^3 a_0^2 eta^6). This matches our file 01 result.

**Useful independent check.** No discrepancy.

---

## Gemini's shape_projector.py Script

**Assessment: PLACEHOLDER ONLY, not usable yet.**

The script uses a placeholder shape function S_matter_bounce = x*y. This is NOT the matter bounce shape. The "cosine = 0.2196" that Gemini reports is for a DUMMY function, not the actual matter bounce.

To compute the real cosine, the script needs the full A_T(k_1, k_2, k_3) from Cai et al.'s Eq. (37), which involves specific momentum-dependent coefficients from the in-in calculation.

**The script framework is sound**, but the output is meaningless until the actual shape function is plugged in.

---

## Gemini's Claim: "Integration by parts boundary terms are likely the exact origin of the factor-of-2"

**Assessment: PLAUSIBLE but UNPROVEN.**

This is a specific hypothesis: that the boundary term at eta_f in the in-in integral contributes a factor that one group includes and the other doesn't. In the matter bounce, the growing mode means the boundary term at eta_f is NOT suppressed (unlike inflation where it vanishes).

Our file 03 derivation found that the superhorizon-only approximation gives zero (the phases cancel). The physical bispectrum comes from HORIZON CROSSING. The boundary term at eta_f contributes to the power-law divergence that cancels in f_NL.

**However:** if one group handles this cancellation differently (e.g., by including the boundary term in the bispectrum but not in the power spectrum normalization), a factor of 2 could result.

This hypothesis is testable by the numerical evaluation (next step).

---

## Summary

| Gemini Input | Status | Action |
|-------------|--------|--------|
| Template cosine is important | CORRECT (already identified) | Estimated in file 05 |
| Power spectrum verified | CORRECT | Confirms file 01 |
| shape_projector.py | PLACEHOLDER (dummy shape) | Needs real A_T input |
| Boundary term = factor-of-2 | PLAUSIBLE (untested) | Testable in numerical eval |
| "N4-level discovery" | OVERSTATED | Template projection is standard |
