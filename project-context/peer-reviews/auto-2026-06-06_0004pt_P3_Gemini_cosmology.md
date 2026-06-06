# P3 auto-2026-06-06_0004pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 175.3s

---

**Referee Report on "Spectrally Unusual Sources at Scale..."**

This paper presents a large-scale anomaly detection campaign across seven astronomical surveys, resulting in a catalog of over 378,000 unique anomalous sources. The authors apply an autoencoder framework, develop a "Path-C" protocol involving native retraining to overcome domain-shift issues, and present cosmological applications related to primordial non-Gaussianity. The scale of the work is impressive, and the methodological lessons, particularly regarding the failures of cross-transfer learning and the importance of representative training sets, are valuable for the community.

However, the manuscript in its current form contains several essential errors and major structural issues that preclude its publication in Physical Review D without significant revision. The primary cosmological result—the constraint on fNL—is marred by arithmetical errors and an incorrectly calculated uncertainty envelope. Furthermore, the paper includes a secondary cosmological analysis on NANOGrav data that is entirely disconnected from the anomaly catalog, which is the core contribution of the work.

Below is a detailed list of required revisions.

---

### Detailed Findings

**ESSENTIAL**

*   **P3-E1 (Table I, pg 7):** The footnote `§` contains internal review-process language that is inappropriate for a final publication.
    *   **Problem:** The text states, "the earlier 'strict subset' framing is replaced with this exact 284/298 = 95.3% overlap." This reads like a note to a co-author or reviewer.
    *   **Required Fix:** This sentence must be removed. The preceding sentences already establish the 95.3% overlap and its statistical significance. The text should be a direct statement of the final methodology, not a commentary on its evolution.

*   **P3-E2 (Section V b, pg 10 & Table IV, pg 13):** The calculation of the 1σ uncertainty envelope for the `fNL` forecast is not standard and appears incorrect.
    *   **Problem:** The paper quotes a 1σ envelope of `[3.92, 8.98]` for `σ(fNL)`. The lower bound (3.92) corresponds to the +1σ value of the bias enhancement parameter `a`, but the upper bound (8.98) corresponds to `a=0` (the no-improvement baseline), not the -1σ value of `a`. Propagating the uncertainty `a = 0.19 ± 0.65` through the provided quadratic formula `1/σ² = F₀ + c a²` yields a 1σ range for `σ(fNL)` of approximately `[3.92, 5.95]`.
    *   **Required Fix:** The authors must either provide a rigorous justification for their non-standard definition of a "1σ envelope" or, preferably, replace it with the correctly propagated uncertainty range. The current presentation is misleading.

*   **P3-E3 (Abstract, pg 1; Section V b, pg 10; Section VI C, pg 12; Section VII, pg 14):** The claimed "7.9% improvement" in the `fNL` forecast is arithmetically incorrect.
    *   **Problem:** Based on the paper's own numbers (baseline `σ_std = 8.98`, central forecast `σ_cen = 8.14`), the fractional improvement is `(8.98 - 8.14) / 8.98 = 9.35%`. The incorrect 7.9% value is quoted in four separate locations, including the abstract and conclusions.
    *   **Required Fix:** This value must be recomputed and corrected in all instances throughout the manuscript.

**MAJOR**

*   **P3-M1 (Section V A, pg 11; Abstract, pg 1; Conclusions, pg 14; Appendix E, pg 16):** The "NANOGrav Bounce Consistency" analysis is thematically and methodologically disconnected from the rest of the paper.
    *   **Problem:** This analysis fits a cosmological model to public NANOGrav data. It does not use the anomaly catalog presented in this work. The paper's claim that this is an "illustrative cosmological application of the anomaly catalog's tracer populations" is false and misleading. Its inclusion feels like an attempt to merge two separate papers.
    *   **Required Fix:** The entire NANOGrav analysis should be removed from the manuscript. This includes the relevant paragraphs in the abstract, the main text (Section V A), the limitations, the conclusions (point 5), Table IV (item d), and the entirety of Appendix E. The paper's focus must be on the anomaly catalog and its direct applications.

*   **P3-M2 (Section V b, pg 10):** The Fisher forecast formalism is insufficiently detailed for a peer-reviewed physics journal.
    *   **Problem:** The paper presents the final formula `1/σ(fNL)² = F₀ + c a²` and provides values for `F₀` and `c` without any derivation. The details of the underlying Fisher matrix calculation—including the fiducial cosmology, survey volume, redshift binning, and other assumptions used to derive these constants—are completely absent.
    *   **Required Fix:** The authors must add a new appendix section detailing the full Fisher matrix calculation that leads to the quoted values of `F₀` and `c`. Without this, the forecast result is not reproducible or verifiable.

**MINOR**

*   **P3-m1 (Section II B, pg 2):** The use of four different anomaly thresholding strategies across the surveys is a potential source of confusion and limits the direct comparability of results.
    *   **Problem:** While the different methods are documented in a footnote, the main text would benefit from a more direct discussion of this methodological heterogeneity.
    *   **Required Fix:** Add a paragraph in Section II B that explicitly states that different thresholds were used, briefly justifies the choice for each survey (e.g., "the long tail of the eROSITA score distribution motivated a data-driven knee-finding approach..."), and acknowledges that this means the raw anomaly rates are not directly comparable across all surveys.

*   **P3-m2 (Section III E, pg 6):** The paper reports a tension in the eROSITA validation metrics without explanation.
    *   **Problem:** The eROSITA catalog is described as failing the injection-recovery gate (1.2% recovery) while simultaneously having the highest cross-validation (XV) stability (81.5%) of any survey. This is a counter-intuitive result.
    *   **Required Fix:** The authors should add a sentence or two explaining this apparent discrepancy. For example, is the injection test (e.g., adding a simple feature perturbation) not representative of the true anomalies that the XV stability metric is sensitive to?

**NIT**

*   **P3-N1 (Section II D, pg 3):** There is a minor typo and redundant phrasing in the description of the reproducibility materials.
    *   **Problem:** The phrase "reproducibility scripts shipped with the companion data repository" is awkward.
    *   **Required Fix:** Rephrase to something clearer, such as "reproducibility scripts are provided in the companion data repository."

---

## Summary recommendation
**MAJOR REVISIONS**

The paper reports on a significant and valuable effort to create a multi-survey anomaly catalog. The methodological insights, particularly on the challenges of transfer learning in astronomy, are a noteworthy contribution. However, the manuscript is currently undermined by essential errors in its main cosmological result, a lack of methodological detail in its Fisher forecast, and the inclusion of an entire, unrelated scientific analysis that dilutes the paper's focus.

The paper can be made acceptable for publication in Physical Review D, but only after the authors have (1) corrected the numerical and statistical errors in the `fNL` forecast, (2) removed the entire NANOGrav analysis, and (3) provided a complete derivation of their Fisher forecast formalism. These are substantial changes that require careful attention.