# P2 R34conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper2_fnl_forecast_v1.7.54.pdf` md5=aae083ab pages=25
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (3658 chars)
**Wall time**: 169.1s

---

**Referee Report for "Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook"**

This paper presents a detailed forecast for testing the matter-bounce cosmological scenario using upcoming large-scale structure surveys, primarily SPHEREx. The central prediction of the quasi-dust matter bounce is a local-type non-Gaussianity with amplitude `f_NL = -35/8`. The authors perform a sensitivity recast of existing SPHEREx forecasts, incorporating a comprehensive analysis of theoretical and systematic uncertainties.

The main contributions of the work are:
1.  A thorough audit of the matter-bounce bispectrum prediction, including a resolution of a factor-of-two discrepancy in the literature, which the authors convincingly argue is due to a missing time-ordering in one of the calculations.
2.  A novel analysis of the theoretical uncertainty arising from the underdetermined polynomial structure of the bispectrum shape function, which is quantified as a "null-space" uncertainty.
3.  A careful calculation of the template mismatch between the true bounce bispectrum and the standard local template, and the propagation of this mismatch into the forecast significance.
4.  A comprehensive treatment of observational systematics, including a parameterized model for GR projection effects and PNG bias uncertainty.
5.  A detailed Bayesian model comparison to quantify the discriminating power of SPHEREx between the matter bounce and inflationary alternatives, with a careful exploration of prior sensitivity.

The paper is exceptionally well-written, transparent, and rigorous. The authors clearly state all assumptions, honestly assess the limitations of their analysis (e.g., identifying the "weakest link" in the theoretical derivation), and provide exemplary data and code availability for full reproducibility. The self-correction and documentation of changes from previous internal versions, noted in several places, is a sign of unusual rigor and is highly commendable. The analysis is thorough and the conclusions are well-supported by the calculations presented. The paper is a significant and valuable contribution to the field and is well-suited for publication in Physical Review D.

I have only one minor point that should be addressed before publication.

---
### Findings

**MINOR**

*   **ID:** P2-N1
*   **Section/Page:** Page 2, footnote `*`
*   **Problem:** The corresponding author's email is listed as `houston@hubify.com`. This appears to be a non-institutional or placeholder email address. While not a scientific error, it is unprofessional for a formal publication in a journal of this stature.
*   **Required Fix:** The author should replace this with a stable, professional contact email address, either institutional or a recognized permanent personal domain.

---
### Summary recommendation

**ACCEPT WITH MINOR CORRECTIONS**

The paper is of high quality, presenting a thorough, careful, and important analysis. The work is novel in its detailed treatment of theoretical uncertainties and its definitive resolution of a literature discrepancy. The conclusions are robust and provide a clear outlook on the testability of the matter-bounce scenario. The paper meets and exceeds the standards for publication in Physical Review D. The single minor correction requested is cosmetic and can be easily addressed.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the second part of the review, incorporating new findings from a more rigorous "fresh eyes" check.

================================================================
### Additional Findings from Rigorous Re-examination

My initial review was broadly positive. However, a more detailed, line-by-line re-examination has revealed several issues that were missed on the first pass. The most significant of these is a dimensional inconsistency in a key definitional equation, which I now classify as a major issue requiring correction.

---
### Findings

**MAJOR**

*   **ID:** P3-C1, M1
*   **Section/Page:** Page 3, Equation (2)
*   **Problem:** Equation (2), which defines the dimensionless non-linearity amplitude `B_NL`, is dimensionally inconsistent. The left-hand side is dimensionless, but the right-hand side, `(10 A_T) / (3 Σk_i^3)`, is not. `A_T` is defined in Eq. (1) as the bispectrum shape function, which has units of `(momentum)^-6` (for a nearly scale-invariant power spectrum `P_ζ ~ k^-3`). The denominator `Σk_i^3` has units of `(momentum)^3`. Therefore, the right-hand side has units of `(momentum)^-9`. The text's justification that `B_NL` is "dimensionless by construction" by counting powers of homogeneity is incorrect, as homogeneity and physical dimensions are distinct concepts.
*   **Required Fix:** The equation must be corrected to be dimensionally consistent. This likely involves including appropriate factors of the power spectrum in the denominator, analogous to the standard definition of `f_NL` from the bispectrum. The authors should carefully check the definition from the source literature (Cai et al. [9]) and ensure their equation correctly defines a dimensionless amplitude. This is a fundamental equation for the paper's main quantity of interest and its correctness is essential.

**MINOR**

*   **ID:** P14-D1, m2
*   **Section/Page:** Page 14, Section VI.b
*   **Problem:** There is an incorrect internal cross-reference. In the paragraph "Bayes-factor closure against the QSFI continuum," the text states that the matter bounce approximately matches the local-template scaling with `rcos > 0.97`, citing "Sec. III B". The calculation and discussion of the shape cosine `rcos` actually appear in **Section II A** (specifically, on page 4).
*   **Required Fix:** The cross-reference should be corrected from "Sec. III B" to "Sec. II A".

*   **ID:** P7-C2, m3
*   **Section/Page:** Page 7, Equation (4)
*   **Problem:** Equation (4) for the scale-dependent bias kernel `M(k,z)` is presented without an explicit statement of the units convention. The expression is dimensionally consistent (i.e., `M(k,z)` is dimensionless) only if one assumes natural units where the speed of light `c=1`. While this is a common convention, for the sake of clarity and rigor in a journal like PRD, the convention should be stated.
*   **Required Fix:** The authors should add a brief note stating the units convention used (e.g., "We work in natural units where c=1").

---
### Summary recommendation

**RECONSIDER AFTER MAJOR REVISIONS**

While the paper remains a strong and valuable contribution, the discovery of a dimensionally inconsistent core equation (Eq. 2) is a major issue that must be addressed. The paper's transparency and the authors' evident care in other areas (e.g., self-correcting stale numbers) give me confidence that this can be fixed. However, the error is significant enough to warrant a re-review after correction. The minor issues should also be addressed. My overall positive assessment of the paper's methodology and importance stands, but the presentation must meet the required standard of rigor.