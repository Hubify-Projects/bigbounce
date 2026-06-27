# P2 R55 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/private/tmp/R55_P2/02_full_draft.pdf` md5=6420ec92 pages=28
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 179.0s

---

# Referee Report

**Paper ID:** P2
**Paper Title:** Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook
**Journal:** Physical Review D

## General Comments

This paper presents a detailed sensitivity forecast for testing the matter bounce scenario using primordial non-Gaussianity (PNG) with the upcoming SPHEREx survey and the proposed MegaMapper. The primary contributions are: (1) a thorough audit and validation of the theoretical prediction for local-type non-Gaussianity, `f_NL = -35/8`, from the quasi-dust matter bounce model, including a resolution of a factor-of-two discrepancy in the literature; (2) a quantification of the template mismatch between the bounce bispectrum and the standard local template; (3) a comprehensive forecast for SPHEREx, recasting existing sensitivity estimates to account for the template mismatch and a detailed budget of systematic effects; and (4) a Bayesian model comparison to quantify the discriminating power against inflationary alternatives.

The paper is well-structured, thorough, and generally transparent about its assumptions and limitations. The resolution of the theoretical discrepancy between the Cai et al. and Li et al. results via an explicit operator-algebra argument is a valuable contribution to the field. The detailed analysis of the template mismatch and the systematic budget is crucial for a realistic forecast and is well-executed.

However, several issues, one of them major, must be addressed before the paper can be considered for publication. The most significant concern is the non-standard and likely incorrect treatment of the theoretical uncertainty on the predicted `f_NL` value within the systematic budget. There are also errors in a key derivation in the appendix and some points of confusion in the presentation of the main results that need to be clarified.

## Findings

### ESSENTIAL

**P2-E1: Flawed Derivation of `f_NL` Convention Invariance**
*   **Location:** Appendix A, Page 24
*   **Problem:** The paper argues that the `f_NL` parameter is the same quantity in the Planck/Komatsu-Spergel `c=2` convention for the Bardeen potential `Φ` and the standard `(6/5)` convention for the curvature perturbation `ζ`. The conclusion is correct, but the explicit derivation presented is algebraically incorrect. The text states: `B_ζ = (5/3)^3 * 2 f_NL P_Φ^2 [+ perms] = (5/3)^3 (3/5)^4 * 2 f_NL P_ζ^2 [+ perms] = (18/25) f_NL P_ζ^2 [+ perms]`. This should be compared to the standard `B_ζ = (6/5) f_NL P_ζ^2 [+ perms]`. The derived prefactor `18/25` does not equal the required `6/5`. This undermines a key consistency check in the appendix.
*   **Required Fix:** The derivation must be corrected. The standard relations are `ζ = -5/3 Φ` (in the matter era), `P_ζ = (5/3)^2 P_Φ`, and `B_ζ = (-5/3)^3 B_Φ`. The two standard definitions for the bispectrum are `B_ζ = (6/5)f_NL [P_ζ(k1)P_ζ(k2) + perms]` and `B_Φ = 2f_NL [P_Φ(k1)P_Φ(k2) + perms]`. Equating these via the field relations confirms that `f_NL` is the same parameter in both conventions. This correct derivation should replace the flawed one.

**P2-E2: Confusing Presentation of Bayesian Results in Abstract**
*   **Location:** Abstract, Page 1
*   **Problem:** The abstract states: "Table II reports the r→1 endpoint values while the abstract headline applies the noise-weighted r ≈ 0.84 rebooking... to those entries". This phrasing is confusing. It could imply to a reader that the values in Table II are incorrect or not the primary result, and that a mental correction is needed to obtain the headline numbers. This obscures the results and violates the principle that tables should be understandable on their own.
*   **Required Fix:** Rephrase the abstract to be more direct. State the headline Bayes factor range (`BF ~ 9-14`) and mention that it accounts for the template mismatch. Then, clarify that Table II provides a detailed breakdown of prior dependencies based on the `r=1` (no mismatch) reference case for clarity and to isolate the effect of the priors. Alternatively, and preferably, add columns to Table II showing the final rebooked Bayes factors.

### MAJOR

**P2-M1: Incorrect Treatment of Theoretical Systematic Uncertainty**
*   **Location:** Abstract (p. 1), Sec. II C (p. 6), Table IV (p. 20)
*   **Problem:** The paper treats the "e-correction"—a theoretical uncertainty on the predicted value of `f_NL` (estimated at 0.6-8%)—by adding its effect in quadrature to the statistical and systematic measurement error `σ_eff`. This is seen in Table IV, where the "e-correction" row has a combination rule of "add. quadrature". This is not a standard or correct procedure. A theoretical uncertainty on the model's predicted central value is not a random measurement error. It defines a range of predictions to be tested.
*   **Required Fix:** This must be corrected throughout the manuscript.
    1.  **Frequentist approach:** The significance should be quoted as a range. For example, if `f_NL,pred` is in `[-4.35, -4.02]`, the detection significance for a measurement at `-4.375` would be a range, not a single number with a degraded `σ`. The impact on the exclusion limit of a null result should also be stated.
    2.  **Bayesian approach:** The theoretical uncertainty should be incorporated by using a prior on the bounce `f_NL` (e.g., a Gaussian centered at -4.375 with a width corresponding to the 0.6-8% uncertainty), rather than a delta function. The paper already does this as a "recommended" scenario (`σ_theory=1.0`), but the "realistic" frequentist significance calculation needs to be handled consistently.
    3.  Table IV must be revised. The e-correction should be listed as a shift/range in the numerator (`f_NL`), not an additive contribution to the denominator (`σ_eff`). The final "realistic" significance range in the abstract and main text must be re-evaluated based on this corrected procedure.

### MINOR

**P2-m1: Manuscript Date**
*   **Location:** Page 1
*   **Problem:** The manuscript is dated "June 19, 2026".
*   **Required Fix:** The date should be corrected to the date of submission.

**P2-m2: Missing Pages in Manuscript**
*   **Location:** N/A
*   **Problem:** The provided PDF appears to be missing pages 4 and 22.
*   **Required Fix:** Please ensure the complete manuscript is submitted for review. This report is based on the available pages.

**P2-m3: Inconsistent Notation for `f_NL`**
*   **Location:** Throughout the manuscript
*   **Problem:** The paper uses various notations for the non-Gaussianity parameter, including `f_NL`, `f_NL^local`, `f_NL^bounce`, and `f_NL^inf`. While the meaning is usually clear from context, consistent notation would improve readability.
*   **Required Fix:** Use a consistent set of symbols. For example: `f_NL` for the general parameter, `f_NL^loc` for the local template amplitude, `f_NL^MB` for the matter bounce prediction, and `f_NL^SR` for the slow-roll prediction.

### NIT

**P2-N1: Typo in Abstract**
*   **Location:** Abstract, Page 1
*   **Problem:** The abstract uses `f_NL^local` and `f_NL` to refer to the same parameter.
*   **Required Fix:** Use `f_NL` consistently for the local-type amplitude being constrained.

## Summary recommendation

**MAJOR REVISIONS**

This is a strong, comprehensive, and valuable paper that performs a much-needed audit and forecast for the matter bounce scenario. The resolution of the factor-of-two discrepancy in the theoretical literature is a particularly important contribution. The analysis is detailed and the paper is transparent about its methodology.

However, the major issue with the handling of the theoretical uncertainty (the "e-correction") must be resolved, as it impacts one of the headline results—the "realistic" detection significance. The error in the appendix derivation and the confusing presentation of the Bayesian results also require correction. Once these issues are addressed, the paper will be an excellent candidate for publication in Physical Review D.