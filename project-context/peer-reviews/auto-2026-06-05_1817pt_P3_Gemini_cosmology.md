# P3 auto-2026-06-05_1817pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 156.0s

---

## Referee Report: "Spectrally Unusual Sources at Scale..."

This manuscript presents a large-scale anomaly detection campaign across seven astronomical surveys, resulting in a catalog of over 378,000 unique anomalous sources. The authors apply a consistent autoencoder framework (BIGAE), develop a "Path-C" protocol involving native retraining to handle cross-survey domain shift, and perform extensive validation including injection-recovery tests and cross-matching. The work culminates in two cosmological applications: a forecast for primordial non-Gaussianity (fNL) constraints using the anomaly catalog as a new tracer population, and a consistency check of the matter-bounce scenario against NANOGrav data.

The scale of the analysis is impressive, and the methodological lessons, particularly regarding the pitfalls of cross-survey transfer learning (e.g., the LAMOST and SDSS cases), are valuable for the community. The public release of the catalog and code is commendable. However, the manuscript in its current form contains several significant issues ranging from confusing presentation to inconsistencies and unsupported claims in the cosmological analysis that must be addressed before it can be considered for publication in Physical Review D.

---
### Detailed Findings

#### ESSENTIAL

**P3-E1 | Section: References | Page: 19**
*   **Problem:** Reference [33] contains an internal author note within the bibliographic entry: `[publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity]`. Such internal bookkeeping metadata is unacceptable for a published article.
*   **Fix:** Remove the bracketed note from the reference.

**P3-E2 | Section: III (Survey-by-Survey Results) | Page: 7 (Table I)**
*   **Problem:** The structure of Table I is fundamentally confusing and misrepresents the paper's primary results. The main body of the table lists anomaly counts from the initial "cross-transfer" scan, which the authors repeatedly state are superseded, contaminated, and preserved only as a "before/after diagnostic". The canonical, final "Path-C" results are relegated to a summary row at the bottom and a dense footnote. This forces the reader to piece together the main scientific output from the fine print, while the most prominent part of the table displays results the paper itself invalidates.
*   **Fix:** Restructure Table I. The main rows of the table should present the final, canonical Path-C native-retrained results for each survey. The superseded cross-transfer counts should be moved to a separate column clearly labeled "Initial Cross-Transfer (Diagnostic Only)" or to a separate, smaller table in an appendix. The primary results of the paper must be presented with maximum clarity.

#### MAJOR

**P3-M1 | Section: V (Cosmological Applications) & Appendix C | Pages: 10 & 15**
*   **Problem:** There is a critical inconsistency in the calculation of the fNL forecast's dependence on the bias enhancement factor `a`. The main text (p. 10) and abstract correctly use the Fisher-positivity-respecting form `1/σ(fNL)² = F₀ + ca²`, which is quadratic in `a`. However, Appendix C (p. 15) claims that "The fractional improvement scales as Δσ(fNL)/σ(fNL)std ≈ (6.1%/0.15) a", which is linear in `a`. This linear scaling is physically incorrect; a Taylor expansion of σ(a) around a=0 shows that the leading-order correction is proportional to `a²`, not `a`. Table VII is explicitly generated using this incorrect linear approximation. This inconsistency undermines the credibility of the forecast analysis.
*   **Fix:** The authors must use a single, consistent model. The quadratic form `F₀ + ca²` is the correct one. Appendix C and Table VII must be re-written and re-calculated using this form. The text describing a linear scaling in `a` must be removed and corrected to reflect the `a²` dependence.

**P3-M2 | Section: V (Cosmological Applications) | Page: 10**
*   **Problem:** The paper claims that "General-relativistic projection corrections (O(H²/k²)) contribute |Δσ/σ| < 0.02% at kmax = 0.2 h Mpc⁻¹ (plane-parallel monopole, sub-% of b; §VID (e))". This is a very strong claim based on an oversimplification. While the monopole contribution from density fluctuations might be small, full GR effects on galaxy clustering include velocity-induced (redshift-space distortions) and potential-induced (Doppler, ISW, lensing) terms that are not guaranteed to be negligible and scale differently with `k`. Citing this as the total GR projection correction is misleading and does not meet the standards of rigor for a cosmology paper in PRD.
*   **Fix:** The authors must either perform a more complete analysis of the relevant GR effects for their specific tracer sample and scales, or significantly weaken and caveat this statement. They should clarify that they have only considered the monopole density term and that other GR effects have not been modeled and represent a potential systematic.

#### MINOR

**P3-m1 | Section: V (Cosmological Applications) | Page: 10 (also Abstract, p. 1)**
*   **Problem:** The paper quotes a "7.9% improvement" for the fNL forecast from the empirical bias measurement. This value is not reproducible from the numbers provided. Using the baseline σ(fNL)std = 8.98 and the central forecast σ(fNL) = 8.14, the fractional improvement is (8.98 - 8.14) / 8.98 = 9.35%.
*   **Fix:** Correct the percentage to 9.4% in the abstract and main text, or provide a clear derivation for the 7.9% figure.

**P3-m2 | Section: III (Survey-by-Survey Results) | Page: 7 (Table I)**
*   **Problem:** The symbols used to flag SDSS DR18 and LAMOST DR10 in the first column of Table I (`°` and `♦`) do not have corresponding footnotes.
*   **Fix:** Add the missing footnotes or remove the symbols.

**P3-m3 | Section: III (Survey-by-Survey Results) | Page: 4 (Figure 1)**
*   **Problem:** The caption for Figure 1 states it shows "319,443 detections", which corresponds to the initial cross-transfer baseline. It then immediately mentions the "canonical Path-C unique count is 378,280". This could be confusing.
*   **Fix:** Clarify the caption to explicitly state that the map visualizes the *initial cross-transfer baseline* which is used as a diagnostic, not the final catalog. For example: "Mollweide projection of the 319,443 anomalies from the initial cross-transfer baseline scan. This baseline is preserved as a diagnostic; the final, canonical catalog contains 378,280 unique objects after native retraining and deduplication."

**P3-m4 | Section: Abstract | Page: 1**
*   **Problem:** The abstract mentions a "recommended catalog-grade subset is ~265,000 unique objects". The derivation of this number is not explicitly shown in the main text, requiring the reader to infer it by summing counts from a footnote in Table I and estimating a deduplication factor.
*   **Fix:** Add a sentence in the main body (e.g., in Section IID or IV) that explicitly defines this subset and shows how the ~265,000 number is derived.

#### NIT

**P3-N1 | General**
*   **Problem:** The paper is 20 pages long. While the scope is large, the narrative could be tightened. The detailed survey-by-survey results in Section III contain information that, while valuable, could be summarized in the main text with full details moved to an appendix to improve readability and focus on the primary cross-cutting results.
*   **Fix:** Consider restructuring to shorten the main text to ~12-15 pages by moving some of the per-survey deep-dive descriptions and secondary plots to an appendix. This is a suggestion for improvement, not a requirement for acceptance.

---
## Summary recommendation

**MAJOR REVISIONS**

The authors have undertaken a massive and valuable data processing effort. The resulting catalog and the methodological insights are a significant contribution. However, the manuscript is marred by a confusing presentation of its primary results (Table I), a critical inconsistency in its fNL forecast methodology (P3-M1), and an insufficiently rigorous treatment of GR effects (P3-M2). These issues, along with the internal note in the bibliography, must be thoroughly addressed. Once these major revisions are completed, the paper will be a strong candidate for publication.