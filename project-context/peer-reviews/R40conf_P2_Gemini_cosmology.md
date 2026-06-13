# P2 R40conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/paper2_fnl_forecast.pdf` md5=cab7e43f pages=29
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (6128 chars)
**Wall time**: 170.4s

---

## Referee Report: "Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook"

This paper presents a comprehensive sensitivity forecast for testing the matter-bounce cosmological scenario using upcoming large-scale structure surveys, primarily SPHEREx. The authors perform a detailed analysis of the benchmark prediction for local-type non-Gaussianity, `f_NL = -35/8`, including a novel treatment of polynomial ambiguities, a resolution of a factor-of-two discrepancy in the literature, and a thorough accounting of observational systematics. The analysis is extended to a Bayesian model comparison to quantify the discriminating power against inflationary models.

The paper is exceptionally well-written, rigorous, and transparent in its methodology. The scope is ambitious, and the authors deliver a detailed and convincing analysis on all fronts. The work represents a significant contribution to the field by providing a robust and realistic assessment of our ability to test a key alternative to cosmic inflation. The resolution of the Cai et al. vs. Li et al. discrepancy in Appendix A is particularly valuable and clarifies an important point in the literature. The systematic treatment of the template mismatch and the propagation of uncertainties through the forecast are exemplary.

While the paper is of very high quality, I have identified a few minor points that should be addressed before publication.

---

### Detailed Findings

#### MINOR

**P2-m1: Section II, Page 5 - Clarification of Null-Space Significance Range**

*   **Problem:** The text quantifies the impact of the polynomial null-space ambiguity on the detection significance. On page 4, it states the amplitude recovery factor is `r = 0.85 ± 0.13` with an interquartile range of `[0.75, 0.94]`. On page 5, it states: "Propagating the full scatter onto the detection significance, the 16th-84th percentile range of `|f_NL|r/σ(f_NL)` across the 10,000 coefficient samples is 4.4-6.2σ".
    My re-computation using the quoted 16th and 84th percentile values for `r` (assuming `r_16 ≈ 0.75` and `r_84 ≈ 0.94` as implied by the interquartile range and standard deviation) yields a slightly different range:
    -   Lower (16th percentile): `4.375 * 0.75 / 0.7 ≈ 4.7σ`
    -   Upper (84th percentile): `4.375 * 0.94 / 0.7 ≈ 5.9σ`
    The quoted range of `4.4-6.2σ` is wider. While this does not change any conclusions, the discrepancy should be clarified. It may be that the 16th/84th percentiles of `r` are slightly different from the values I inferred, or that the distribution is skewed in a way that widens the significance range.
*   **Required Fix:** Please briefly clarify the origin of the `4.4-6.2σ` range. For instance, explicitly state the 16th and 84th percentile values of `r` from the 10,000-sample scan that lead to this significance range.

#### NIT

**P2-N1: Section VI, Page 11 - Typo in Figure 3 Caption**

*   **Problem:** The caption for Figure 3 reads: "SPHEREX 10 error bar shown in blue." The Greek letter sigma (`σ`) is missing.
*   **Required Fix:** Change "10" to "1σ".

**P2-N2: Section VIII, Page 20 - Consistency of `r_t` notation**

*   **Problem:** On page 7, the paper introduces the notation `r_t` for the tensor-to-scalar ratio to avoid confusion with the template-overlap factor `r`. However, on page 20, in the discussion of the `f_NL-n_s` consistency relation, the standard slow-roll formula is quoted as `n_s - 1 = 2(2ε - η)`. In this context, `η` is a slow-roll parameter, but it is not defined in the paper and could be confused with the conformal time `η` used elsewhere (e.g., Eq. A2). While context makes it clear, adding a definition would improve clarity.
*   **Required Fix:** Either define the slow-roll parameter `η` parenthetically when it first appears, or confirm that its single use does not require definition in the context of a PRD paper. The former is preferred for maximum clarity. *Self-correction: The paper is focused on the bounce, and this is a brief comparison point. The audience will understand the notation. This is a very minor point, but worth considering.*

---

## Summary recommendation

**ACCEPT WITH MINOR CORRECTIONS**

This is an excellent paper that meets the high standards of Physical Review D. It is thorough, methodologically sound, and provides a valuable and robust forecast for testing matter-bounce cosmology. The findings are significant and well-supported by the detailed calculations presented. The identified issues are very minor and can be easily addressed. I recommend acceptance after the authors have incorporated the requested clarifications.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the updated, more rigorous referee report.

================================================================
## Referee Report: "Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook"

This paper presents a comprehensive sensitivity forecast for testing the matter-bounce cosmological scenario using upcoming large-scale structure surveys, primarily SPHEREx. The authors perform a detailed analysis of the benchmark prediction for local-type non-Gaussianity, `f_NL = -35/8`, including a novel treatment of polynomial ambiguities, a resolution of a factor-of-two discrepancy in the literature, and a thorough accounting of observational systematics. The analysis is extended to a Bayesian model comparison to quantify the discriminating power against inflationary models.

The paper is exceptionally well-written, rigorous, and transparent in its methodology. The scope is ambitious, and the authors deliver a detailed and convincing analysis on all fronts. The work represents a significant contribution to the field by providing a robust and realistic assessment of our ability to test a key alternative to cosmic inflation. The resolution of the Cai et al. vs. Li et al. discrepancy in Appendix A is particularly valuable and clarifies an important point in the literature. The systematic treatment of the template mismatch and the propagation of uncertainties through the forecast are exemplary.

While the paper is of very high quality, I have identified a few minor and moderate points that should be addressed before publication.

---

### Detailed Findings

#### MODERATE

**P2-B1: Figure 5 vs. Text Mismatch on `b_φ` Sensitivity**

*   **Problem:** The left panel of Figure 5 shows the SPHEREx bispectrum constraint `σ(f_NL)` (red dashed line) as a flat line at 0.7, completely independent of the `b_φ` prior uncertainty. This contradicts the text on page 18, which states: "relaxing the per-bin bφ prior to 30% widens the per-bin SPHEREX σ(fNL) to ≈ 0.9-1.0". The right panel of Figure 5 and the detailed budget in Table IV also correctly reflect this degradation. The left panel plot is therefore inconsistent with the paper's own analysis and conclusions.
*   **Required Fix:** Please correct the red dashed line in the left panel of Figure 5 to show the degradation of `σ(f_NL)` with increasing `b_φ` prior uncertainty, as described in the text and used in the rest of the analysis.

**P2-A1: Section II, Page 5 - Clarification of Null-Space Significance Range**

*   **Problem:** The text quantifies the impact of the polynomial null-space ambiguity on the detection significance. On page 4, it states the amplitude recovery factor is `r = 0.85 ± 0.13` with an interquartile range of `[0.75, 0.94]`. On page 5, it states: "Propagating the full scatter onto the detection significance, the 16th-84th percentile range of `|f_NL|r/σ(f_NL)` across the 10,000 coefficient samples is 4.4-6.2σ".
    My re-computation using the quoted 16th and 84th percentile values for `r` (assuming `r_16 ≈ 0.75` and `r_84 ≈ 0.94` as implied by the interquartile range and standard deviation) yields a slightly different range:
    -   Lower (16th percentile): `4.375 * 0.75 / 0.7 ≈ 4.7σ`
    -   Upper (84th percentile): `4.375 * 0.94 / 0.7 ≈ 5.9σ`
    The quoted range of `4.4-6.2σ` is wider. While this does not change any conclusions, the discrepancy should be clarified. It may be that the 16th/84th percentiles of `r` are slightly different from the values I inferred, or that the distribution is skewed in a way that widens the significance range.
*   **Required Fix:** Please briefly clarify the origin of the `4.4-6.2σ` range. For instance, explicitly state the 16th and 84th percentile values of `r` from the 10,000-sample scan that lead to this significance range.

#### MINOR

**P2-A2: Section IV, Page 9 - Covariance Uncertainty Propagation Formula**

*   **Problem:** In the order-of-magnitude check for the non-Gaussian covariance correction, the paper states that the fractional shift in the uncertainty follows from `δσ/σ ~ δC/C`. For a Gaussian likelihood where the uncertainty `σ` is proportional to the square root of the covariance `C`, the standard propagation of errors gives `δσ/σ = (1/2) δC/C`. The conclusion that the effect is negligible remains unchanged, but the formula presented appears to be missing a factor of 1/2.
*   **Required Fix:** Please verify the formula for the propagation of covariance uncertainty. If it is indeed `δσ/σ = (1/2) δC/C`, please correct the text accordingly.

#### NIT

**P2-N1: Section VI, Page 11 - Typo in Figure 3 Caption**

*   **Problem:** The caption for Figure 3 reads: "SPHEREX 10 error bar shown in blue." The Greek letter sigma (`σ`) is missing.
*   **Required Fix:** Change "10" to "1σ".

**P2-N2: Section VIII, Page 20 - Consistency of `η` notation**

*   **Problem:** On page 7, the paper introduces the notation `r_t` for the tensor-to-scalar ratio to avoid confusion with the template-overlap factor `r`. However, on page 20, in the discussion of the `f_NL-n_s` consistency relation, the standard slow-roll formula is quoted as `n_s - 1 = 2(2ε - η)`. In this context, `η` is a slow-roll parameter, but it is not defined in the paper and could be confused with the conformal time `η` used elsewhere (e.g., Eq. A2). While context makes it clear, adding a definition would improve clarity.
*   **Required Fix:** Please consider defining the slow-roll parameter `η` parenthetically when it first appears for maximum clarity.

---

## Summary recommendation

**ACCEPT WITH MINOR/MODERATE CORRECTIONS**

This is an excellent paper that meets the high standards of Physical Review D. It is thorough, methodologically sound, and provides a valuable and robust forecast for testing matter-bounce cosmology. The findings are significant and well-supported by the detailed calculations presented. The identified issues are all addressable and will improve the already high quality of the manuscript. I recommend acceptance after the authors have incorporated the requested corrections and clarifications.