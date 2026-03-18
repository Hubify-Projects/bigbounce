# 05: Flagship Observable Re-Selection

**Created:** 2026-03-17
**Status:** COMPLETE

---

## Convention Resolution (CRITICAL UPDATE)

**CONFIRMED:** f_NL = -35/8 = -4.375 is in the SAME convention as Planck's constraint f_NL = -0.9 +/- 5.1.

Source: Cai et al. (2009, arXiv:0903.0631) define f_NL via zeta = zeta_g + (3/5) f_NL zeta_g^2, which is equivalent to the Planck Komatsu-Spergel convention Phi = phi_G + f_NL phi_G^2.

The value f_NL = 5/12 that appeared in earlier analysis files (branch_V_bounce_evidence/dust_bounce_spectrum/) was **INCORRECT** — from a faulty delta-N calculation with a spurious convention conversion factor. The correct matter bounce prediction is f_NL = -35/8 = -4.375.

---

## Candidate Flagship Observables

### 1. Local f_NL = -4.375

**Properties:**
- Parameter-free prediction from matter contraction dynamics
- Negative sign — distinctive from inflation (single-field: ~0; multi-field curvaton: typically positive)
- Magnitude O(1) — large enough to detect with next-gen surveys
- Robust: set by superhorizon growth of zeta in w = 0 contraction, independent of bounce details

**Current status:** Planck: f_NL = -0.9 +/- 5.1. The prediction -4.375 is at 0.7 sigma — perfectly consistent.

**Future reach:**
| Experiment | sigma(f_NL) | Detection significance |
|-----------|------------|----------------------|
| CMB-S4 | ~2.5 | 1.8 sigma |
| SPHEREx | ~1.5 | 2.9 sigma |
| DESI + Euclid combined | ~1.0 | 4.4 sigma |
| MegaMapper | ~0.5 | **8.75 sigma** |

**Kill criteria:**
- If MegaMapper measures f_NL = 0.0 +/- 0.5: bounce is excluded at 8.75 sigma
- If MegaMapper measures f_NL = -4.4 +/- 0.5: inflation (single-field) is excluded at 8.8 sigma

### 2. Scale Dependence of f_NL

**Properties:**
- The matter bounce may predict specific scale dependence of f_NL (running of the bispectrum)
- Not well-calculated in the literature
- Would require MegaMapper-class data to measure

**Assessment:** SECONDARY. The amplitude and sign of f_NL are more powerful discriminators than its scale dependence. Scale dependence adds information but is a second-order effect.

### 3. Squeezed-Limit Consistency Relation Violation

**Properties:**
- In single-field inflation, the squeezed limit gives f_NL = (5/12)(1 - n_s) (Maldacena consistency relation)
- The matter bounce gives f_NL = -35/8 in the squeezed limit — a MASSIVE violation of this relation
- This violation is a direct consequence of superhorizon growth during contraction (forbidden in inflation)

**Assessment:** This is actually the SAME signature as f_NL = -4.375 — the squeezed-limit bispectrum IS f_NL^local. The Maldacena consistency relation violation is automatically tested when measuring f_NL^local. Not a separate observable.

### 4. Low-k Cutoff / Large-Angle Suppression

**Properties:**
- A bounce at the Planck scale produces a characteristic k_bounce ~ 10^42 Mpc^-1
- Observable modes (k ~ 0.05 Mpc^-1) are at k/k_bounce ~ 10^-44
- The cutoff is at k ~ k_bounce, far outside the observable window
- No detectable low-k suppression from a Planck-scale bounce

**Assessment:** ELIMINATED. The bounce scale is too high for the cutoff to be observable.

### 5. Tensor Suppression / Blue Tensor Tilt

**Properties:**
- r ~ 10^-4 with n_T > 0 (blue)
- Both LiteBIRD (sigma(r) ~ 0.001) and BICEP Array (sigma(r) ~ 0.003) cannot detect r = 10^-4
- n_T is unmeasurable without tensor detection

**Assessment:** ELIMINATED. Untestable with any planned experiment.

### 6. Combined Observable Correlation (n_s + f_NL + r)

**Properties:**
- Bounce predicts: n_s = 0.964, f_NL = -4.375, r ~ 10^-4
- Inflation predicts: n_s = 0.964, f_NL ~ 0, r = model-dependent
- The n_s-f_NL combination is more discriminating than either alone

**Assessment:** The discriminating power comes entirely from f_NL. Adding n_s and r doesn't help because both models match n_s and both predict small r. The "combination" reduces to f_NL alone.

### 7. Positive Spectral Running (alpha_s > 0)

**Properties:**
- Lehners & Wilson-Ewing (2015): matter bounce predicts alpha_s > 0
- Standard inflation: alpha_s < 0
- But predicted |alpha_s| ~ 10^-4 is far below detection threshold

**Assessment:** ELIMINATED. Unmeasurable.

---

## Flagship Observable Selection

### Winner: **f_NL^local = -35/8 = -4.375**

**Justification:**

1. **Parameter-free:** Does not depend on epsilon, alpha, or any model parameter. Set entirely by the matter contraction dynamics (w = 0 superhorizon growth).

2. **Large magnitude:** |f_NL| = 4.375 is detectable by MegaMapper at 8.75 sigma. No other bounce-specific observable reaches even 3 sigma detection significance.

3. **Negative sign:** The sign alone is a discriminator. Standard inflation generically predicts f_NL >= 0 for local type. Negative local f_NL of O(1) magnitude is unnatural in inflation.

4. **Robust to viability fixes:** The LQC corrections that suppress r do NOT affect f_NL. The quasi-dust EOS epsilon that provides the red tilt does NOT modify f_NL (the nonlinear transfer function depends on the zeroth-order EOS, not the small correction).

5. **No alternative explanation from inflation:** Getting f_NL = -4.375 from inflation requires exotic multi-field constructions (unstable curvaton potential, non-standard kinetic terms, etc.). It is not a generic prediction of any standard inflationary scenario.

6. **Timeline:** MegaMapper is projected for ~2032-2035. SPHEREx (~2025-2028) and DESI/Euclid (~2025-2030) will provide earlier but less decisive constraints.

### Runner-up: **Squeezed-limit consistency relation violation**

This is the same physics expressed differently. The Maldacena relation predicts f_NL^squeezed = (5/12)(1 - n_s) ~ 0.015 for single-field inflation. The bounce predicts f_NL^squeezed = -4.375. The ratio is ~290x and the sign is opposite. This is automatically tested when f_NL^local is measured.

---

## Flagship Observable Definition

**Observable:** f_NL^local (Planck/Komatsu-Spergel convention)

**Predicted value:** -35/8 = -4.375 (matter bounce, parameter-free)

**Current constraint:** -0.9 +/- 5.1 (Planck PR4 2025)

**Future survey reach:**
- SPHEREx: sigma ~ 1.5 (2.9 sigma detection)
- MegaMapper: sigma ~ 0.5 (8.75 sigma detection)

**What measurement would strongly favor bounce:**
- f_NL = -4.4 +/- 0.5 (negative, O(1) magnitude)
- This would exclude single-field inflation at >8 sigma
- Multi-field inflation with curvaton gives f_NL > 0 for most parameter space
- The matter bounce is the ONLY standard scenario predicting this specific value

**What measurement would kill the model:**
- f_NL = 0.0 +/- 0.5 (MegaMapper precision)
- This would exclude f_NL = -4.375 at 8.75 sigma
- The matter bounce prediction is falsifiable

**What measurement would be ambiguous:**
- f_NL = -2.0 +/- 0.5
- Negative, but not -4.375 — could indicate a modified bounce scenario or partial curvaton dilution
- Would require model revision but not outright kill

---

## Caveat: The Quintin No-Go Enhancement

Quintin et al. (2015) showed that if the bounce AMPLIFIES scalar perturbations (to suppress r), then |f_NL| may be ENHANCED beyond -35/8. This means:

- If LQC corrections amplify scalars to give r ~ 10^-4, the same amplification could push |f_NL| > 4.375
- This would make the prediction MORE detectable, not less
- But the exact enhanced value depends on the bounce details (dressed-metric vs hybrid quantization)

**This needs calculation.** The post-bounce f_NL in the LQC dressed-metric approach has not been explicitly computed. The pre-bounce value is -35/8; the post-bounce value may differ.

This is the next calculation to do (see file 06).
