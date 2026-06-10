# P3 auto-2026-06-09_0025pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 718.2s

---

**Referee Report on "Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies and Native-Trained Novelty Fractions from 37.3 Million Sources and Map Patches"**

This paper presents a large-scale anomaly detection analysis across seven astronomical surveys, resulting in a catalog of nearly 380,000 unique anomalous sources. The authors apply an autoencoder framework, detail a "Path-C" protocol involving native retraining to overcome cross-survey domain shift, and present two cosmological applications of the resulting catalog: a forecast for constraints on primordial non-Gaussianity (fNL) and a consistency check with the matter-bounce model using NANOGrav data.

The scale of the analysis is impressive, and the methodological lessons, particularly regarding the pitfalls of transfer learning and the importance of native retraining, are a valuable contribution to the field. The transparency in reporting validation failures (e.g., for LAMOST, Gaia, eROSITA) is commendable. However, the paper suffers from several critical flaws in the presentation of its main results and in its cosmological analysis that prevent it from being acceptable for publication in Physical Review D in its current form. The required revisions are substantial.

## Detailed Findings

### ESSENTIAL Revisions

**P3-E1: Misleading Headline Catalog Size**
*   **Section:** Abstract, Table I, Section VII (Conclusions)
*   **Page(s):** 1, 6, 14
*   **Problem:** The headline result of "378,280 unique anomalies" is misleading. This total count includes an "~113,000 object" tier from LAMOST which the authors explicitly state is an "exploratory tier" that failed its injection-recovery gate and is retained only as a "methodological lesson" due to a "98% blue-excess training-bias artifact" (Abstract, p. 1). Similarly, the Gaia and eROSITA tiers also failed their validation gates (§III E, §III G). The abstract itself recommends a much smaller, more reliable "~265,000 unique objects" as the "recommended catalog-grade subset". Presenting the larger, contaminated number as the headline result is not appropriate for a scientific publication. The primary reported result should be the one the authors have the most confidence in.
*   **Required Fix:** The headline number in the title, abstract, and conclusions must be changed to the "catalog-grade" count (~265,000). The full 378,280 count can be mentioned, but it must be clearly and immediately qualified as containing exploratory, non-validated tiers. The abstract should be rewritten to lead with the robust result.

**P3-E2: Incorrect Uncertainty Propagation in fNL Forecast**
*   **Section:** Abstract, V.B (Cosmological Applications), Table IV
*   **Page(s):** 1, 11, 14
*   **Problem:** The paper incorrectly calculates the 1-σ uncertainty envelope for the forecasted constraint on fNL, σ(fNL). The forecast depends on the bias parameter `a`, which is measured as `a_jk = 0.19 ± 0.65`. The 1-σ range for `a` is therefore `[-0.46, 0.84]`. The paper uses the form `1/σ(fNL)² = F₀ + ca²`, where `c > 0`. This means that σ(fNL) is a monotonically decreasing function of `|a|`. The 1-σ envelope for σ(fNL) should correspond to the values at the bounds of the 1-σ range for `a`. The value at `a=0.84` is correctly calculated as 3.92. However, the value at `a=-0.46` is `σ(fNL) ≈ 5.95`. The paper repeatedly gives the 1-σ envelope as `[3.92, 8.98]`. The upper value of 8.98 corresponds to `a=0` (the baseline with no anomaly tracers), which is not the uncertainty bound. This is a fundamental error in uncertainty propagation. The same error is repeated for the Gold+Silver sample analysis in Table IV.
*   **Required Fix:** Recompute the 1-σ envelope for σ(fNL) by correctly propagating the uncertainty on `a`. The abstract, main text (p. 11), and Table IV must be corrected. The conclusion that the improvement is consistent with null at <1σ remains valid, but the reported uncertainty range on the forecast is incorrect.

**P3-E3: Future Dating and Unavailable References**
*   **Section:** Metadata, Introduction, References
*   **Page(s):** 1, 19
*   **Problem:** The paper is dated "June 2026". This must be corrected to the date of submission. More critically, a key reference for the primary dataset, "[1] DESI Collaboration, 'The DESI Data Release 1,' 2025, DESI DR1 documentation," points to a document in the future. A paper cannot be published with references to unavailable, future documentation.
*   **Required Fix:** Correct the date of the manuscript. Replace the future reference [1] with a citation to an existing public preprint (e.g., on arXiv) or the currently available public data release documentation. If no such public document exists, the analysis cannot be considered reproducible and the paper cannot be published.

### MAJOR Revisions

**P3-M1: Unclear and Contradictory Summary Table (Table I)**
*   **Section:** III
*   **Page(s):** 6
*   **Problem:** Table I is the central summary of the paper's data products, but it is exceptionally confusing.
    1.  The `N_anom` column is not clearly defined. The footnote `*` states these are "initial cross-transfer scan counts," but the `†` footnote on LAMOST and others implies they should be the final "Path-C native-retrained counts."
    2.  The table does not show the final, canonical anomaly counts for each survey in a clear column. These numbers are buried in the text and footnotes.
    3.  The distinction between the "cross-transfer baseline" total and the "Path-C unique" total is not intuitive from the table structure.
*   **Required Fix:** Redesign Table I for clarity. It should contain, at minimum, separate and clearly labeled columns for "Survey", "Total Sources Processed", "Path-C Anomaly Count (Canonical)", and "Anomaly Rate (%)". The cross-transfer counts can be included in an additional column labeled "Cross-transfer Count (for comparison)" to illustrate the impact of the Path-C rebuild. The current footnote-heavy approach is inadequate.

**P3-M2: Unreproducible fNL Improvement Percentage**
*   **Section:** Abstract, V.B, VI.C
*   **Page(s):** 1, 11, 12
*   **Problem:** The paper repeatedly claims a "7.9% improvement" in the fNL forecast (`σ(fNL)` drops from 8.98 to 8.14). This number cannot be reproduced from the provided values. The fractional improvement in σ(fNL) is `(8.98 - 8.14) / 8.98 = 9.4%`. The improvement in Fisher information (1/σ²) is `(1/8.14² - 1/8.98²) / (1/8.98²) ≈ 22%`. The origin of the 7.9% figure is a mystery.
*   **Required Fix:** Provide the explicit calculation for the "7.9% improvement" or correct the value throughout the manuscript (abstract, p. 11, p. 12).

**P3-M3: Inconsistent Anomaly Count Derivation for DESI**
*   **Section:** IV.A
*   **Page(s):** 4
*   **Problem:** The text states: "The headline 195,829 DESI anomaly count is the top-1% score-cut of the full 22.5-M-spectrum scan". This is numerically incorrect. 195,829 out of 22,504,897 is 0.87%. A few sentences later, the text correctly states the count comes from an "S > 5.0 threshold, an anomaly rate of 0.87%". These are two different selection criteria (percentile vs. absolute threshold) and the text contradicts itself.
*   **Required Fix:** Remove the incorrect "top-1% score-cut" claim and state consistently that the DESI sample is defined by an absolute threshold of S > 5.0.

### MINOR Revisions

**P3-m1: Definition of "Path-C"**
*   **Section:** Abstract, I, II.D
*   **Page(s):** 1, 3
*   **Problem:** The term "Path-C" is used in the title and abstract but is not defined until Section II.D on page 3. This is jargon that makes the abstract and introduction difficult to parse for a non-specialist.
*   **Required Fix:** Briefly define "Path-C" (e.g., "our final pipeline incorporating per-survey native retraining") upon its first use in the abstract or introduction.

**P3-m2: Jargon in Fisher Forecast Systematics**
*   **Section:** V.C
*   **Page(s):** 11
*   **Problem:** The sentence "A 4n + 1-nuisance-parameter Fisher block" is unexplained jargon.
*   **Required Fix:** Briefly explain what this refers to or rephrase for a broader audience.

**P3-m3: Figure 1 Shows Superseded Data**
*   **Section:** III
*   **Page(s):** 4
*   **Problem:** Figure 1, the main sky map, shows the spatial distribution of the initial "cross-transfer baseline" anomalies, not the final "Path-C" catalog which is the primary result of the paper. While the caption clarifies this, it would be more appropriate for the figure to reflect the final data product.
*   **Required Fix:** Consider regenerating the figure using the final 378,280 (or preferably, the 265,000 catalog-grade) anomalies. If this is not feasible, the caption must be made even more prominent in stating that it shows an intermediate, superseded data set.

### NITs (Cosmetic)

**P3-N1: Bibliography Key Style**
*   **Section:** References
*   **Page(s):** 19
*   **Problem:** The bibkey for reference [33] is noted as "retained as Heinrich2023 for arXiv-submission-year continuity" despite the publication year being 2024. This is an unusual internal comment that should not be in a final publication.
*   **Required Fix:** Standardize the bibkey to match the publication year.

## Summary recommendation

**MAJOR REVISIONS**

This paper represents a substantial effort with potentially high value for the astronomical community. The methodological insights are significant, and the catalog is a major new resource. However, the work is marred by a misleading headline result that includes non-validated data, a fundamental error in the uncertainty propagation for a key cosmological forecast, and a lack of clarity in its main summary table. These issues must be thoroughly addressed before the paper can be considered for publication. Once these essential and major revisions are completed, the paper could be a strong contribution.