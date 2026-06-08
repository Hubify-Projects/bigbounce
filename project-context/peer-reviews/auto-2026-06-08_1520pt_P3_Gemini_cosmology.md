# P3 auto-2026-06-08_1520pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (3126 chars)
**Wall time**: 136.3s

---

**Referee Report: PRD Submission [Paper ID Redacted]**

**Title:** Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies and Native-Trained Novelty Fractions from 37.3 Million Sources and Map Patches

This paper presents a large-scale anomaly detection analysis across seven astronomical surveys, resulting in a catalog of 378,280 unique anomalies. The primary contributions are the catalog itself, the methodological insights gained from the multi-survey approach, and two specific cosmological applications: a forecast for constraints on primordial non-Gaussianity (`f_NL`) using anomaly-selected tracers, and a test of matter-bounce predictions for the gravitational-wave background using NANOGrav data.

The work is ambitious in scope, combining a significant data-processing effort with theoretical cosmological analysis. The methodological aspects, particularly the "Path-C rebuild" protocol to address cross-survey domain shift and training-set bias, are well-motivated and provide valuable lessons for the application of machine learning in cosmology. The cosmological applications are relevant to Physical Review D. The `f_NL` forecast is handled with appropriate care, considering potential systematics, and the NANOGrav analysis is a direct and timely test of a cosmological model.

The paper is generally well-written, transparent about its limitations, and rigorous in its self-assessment. However, several points require clarification and correction before the manuscript can be considered for publication.

---

### Detailed Findings

#### ESSENTIAL

*   **P3-E1 | Section: References | Page: 19**
    *   **Problem:** The bibliography entry for reference [33] contains an internal note from the authors' citation management software.
    *   **Quote:** `[publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity]`
    *   **Required Fix:** This internal comment must be removed from the final manuscript.

#### MAJOR

*   **P3-M1 | Section: V. COSMOLOGICAL APPLICATIONS | Page: 11**
    *   **Problem:** The calculation of the 1σ envelope for the forecasted `σ(f_NL)` and the quoted percentage improvement are not transparent and could not be reproduced. The central forecast `σ(f_NL) = 8.14` is derived from `a_jk = 0.19`. The uncertainty is `±0.65`. The 1σ range for `a` is `[-0.46, 0.84]`.
    *   **Quote:** "a central forecast σ(fNL) = 8.14 with 1σ envelope [3.92, 8.98] (7.9% improvement consistent with no improvement at <1σ; σ(fnL)std = 8.98 single-tracer baseline)."
    *   **Required Fix:**
        1.  The paper must explicitly show the calculation for the 1σ envelope `[3.92, 8.98]`. The function `σ(a) = (F_0 + c a²)^(-1/2)` is symmetric around `a=0`, with the tightest constraint (lowest `σ`) at the maximum `|a|`. The 1σ range for `a` is not symmetric around the central value. The upper bound of the envelope should be the baseline `σ(f_NL)std = 8.98` (corresponding to `a=0`, which is within 0.3σ of the measured central value). The lower bound should correspond to the value of `a` in the 1σ range that maximizes `a²`, which is `a=0.84`. My calculation yields a lower bound of `σ(a=0.84) ≈ 3.83`. The authors should clarify how they arrived at `3.92`.
        2.  The paper must clarify the calculation of the "7.9% improvement". The standard definition of fractional improvement would be `(σ_std - σ_new) / σ_std = (8.98 - 8.14) / 8.98 = 9.35%`. Please define how the 7.9% figure was calculated.

#### MINOR

*   **P3-m1 | Section: Abstract | Page: 1**
    *   **Problem:** The abstract uses the notation `(fNL)` to refer to the forecasted 1σ uncertainty on `f_NL`, which is confusing. `f_NL` is the parameter itself, while `σ(f_NL)` is its uncertainty.
    *   **Quote:** "inserting this into the Fisher-positivity-respecting form ... gives a central forecast (fNL) = 8.14 with 1σ envelope [3.92, 8.98]"
    *   **Required Fix:** Change `(fNL)` to `σ(fNL)` in the abstract and anywhere else this potentially confusing notation is used to refer to the uncertainty. For example: "...gives a central forecast `σ(f_NL) = 8.14`...".

*   **P3-m2 | Section: II. METHOD | Page: 2**
    *   **Problem:** The text describing the canonical anomaly score `S` in Eq. (2) is potentially ambiguous due to line wrapping and could be misread.
    *   **Quote:** `S(x) = MSE(x) - μ_val / σ_val`
    *   **Required Fix:** While the rendered equation in the PDF is correct with a proper fraction bar, for maximum clarity in the text, please re-format this as `S(x) = (MSE(x) - μ_val) / σ_val` to avoid any ambiguity.

*   **P3-m3 | Section: Abstract | Page: 1**
    *   **Problem:** The abstract states the NANOGrav matter-bounce prediction `γ = 3.0` sits at `+1.13σ`. While mathematically correct based on the quoted posterior mean and standard deviation, the posterior is noted as non-Gaussian in the main text (Page 12). Quoting a sigma-deviation based on a Gaussian approximation for a non-Gaussian posterior can be misleading.
    *   **Quote:** "the matter-bounce prediction γ = 3.0 sits at +1.13σ (marginally consistent)"
    *   **Required Fix:** The authors should consider rephrasing this to be more precise, for example by referencing the credible interval directly or noting that the sigma value is based on a Gaussian approximation of the posterior. The current phrasing is acceptable but could be improved for rigor.

---

## Summary recommendation

**MAJOR REVISIONS**

The paper represents a substantial and valuable contribution at the intersection of large-scale data analysis, machine learning methods, and cosmology. The scale of the anomaly catalog is impressive, and the methodological lessons are important for the community. The cosmological applications are well-motivated and appropriate for Physical Review D. The authors have demonstrated a high level of rigor and transparency, particularly in documenting limitations and methodological failures.

However, the issues identified in the `f_NL` forecast analysis (P3-M1) are significant and must be fully addressed. The derivation of the 1σ uncertainty envelope and the quoted improvement percentage must be clarified and made reproducible. Once these major points, along with the essential and minor corrections, are addressed, the manuscript will be a strong candidate for publication.

---

## PASS 2 — self-critique findings (what initial review missed)

Here are the additional findings from the second, more rigorous review.

================================================================
### Additional Findings from Rigorous Re-examination

*   **P3-m4 | Section: III.H NEOWISE & Table I footnote † | Page: 8 & 7**
    *   **Problem:** The calculation of the null-hypothesis expectation for the fraction of sources in the ecliptic polar caps appears to be off by a factor of two.
    *   **Quote:** "The 17/436 = 3.9% polar-cap fraction represents a 2.6x excess over the uniform-sphere null expectation (1.52%)"
    *   **Analysis:** The mask rejects sources with `|b_ecl| > 80°`, which defines two polar caps, each with a 10° radius. The fractional solid angle of a single 10° cap is `(1 - cos(10°)) ≈ 1.52%`. For an all-sky survey like NEOWISE, which covers both ecliptic poles, the total fractional area of the rejected region is two caps, or ~3.04%. The observed fraction of 3.9% should be compared to 3.04%, yielding a much smaller excess of ~1.3x, not 2.6x.
    *   **Required Fix:** The authors must justify their use of 1.52% as the null expectation or correct the calculation and the claimed excess factor.

*   **P3-m5 | Section: Appendix E | Page: 15**
    *   **Problem:** Equation (E1) for the matter-bounce power-law template is dimensionally inconsistent.
    *   **Quote:** `log10 Pi = ½ [ ... - log10 Tobs]`
    *   **Analysis:** The equation takes the logarithm of `Tobs`, the observation time, which is a quantity with physical units (seconds or years). The argument of a logarithm must be dimensionless. This is a common abuse of notation, but for formal publication, it should be corrected.
    *   **Required Fix:** The equation should be written in a dimensionally consistent form, for example by normalizing `Tobs` by a reference time unit (e.g., `log10(Tobs / 1 yr)`), and stating the unit convention used.

*   **P3-N1 | Section: V. COSMOLOGICAL APPLICATIONS & VI.D Path-C Rebuild Residual Caveats | Page: 11 & 13**
    *   **Problem:** The logical flow of the `f_NL` forecast is difficult to follow due to poor organization. The main result is presented in Section V, but the specific functional form of the Fisher forecast (`1/σ² = F₀ + ca²`) and the values of the constants `F₀` and `c` are defined and justified much later, in a sub-point of the "Residual Caveats" section (Section VI.D(i) and Table IV(i)).
    *   **Analysis:** This structure forces the reader to jump from the main results section to a methodological appendix/caveat section to understand the details of the calculation. While the internal cross-reference is technically correct, the organization is not reader-friendly and buries key details of a headline result.
    *   **Suggested Fix (Note):** This is a suggestion for improving the manuscript's clarity, not a formal error. The authors should consider moving the definition and justification of the Fisher-positivity-respecting form from the caveats section into the main cosmological applications section (Section V), where it is first used. This would present the argument in a more linear and understandable fashion.