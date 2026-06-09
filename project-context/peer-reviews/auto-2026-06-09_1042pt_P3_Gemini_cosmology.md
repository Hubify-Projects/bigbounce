# P3 auto-2026-06-09_1042pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (3010 chars)
**Wall time**: 177.9s

---

To the Editor of Physical Review D,

I have reviewed the manuscript "Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies and Native-Trained Novelty Fractions from 37.3 Million Sources and Map Patches" by Houston Golden. The paper presents a large-scale anomaly detection analysis across seven astronomical surveys, resulting in a substantial catalog of unusual objects. It further explores cosmological applications of this catalog, specifically for constraining primordial non-Gaussianity (`f_NL`) and testing bounce cosmology models with pulsar timing array data.

The scale of the analysis is impressive, and the methodological lessons, particularly regarding the dangers of training-set bias (the "LAMOST lesson"), are valuable for the community. The author's transparency in documenting methodological failures (e.g., the cross-transfer approach, the quarantined ACT data) is commendable. The resulting catalog is a potentially significant resource.

However, the manuscript suffers from several critical errors and a lack of clarity in key areas, particularly concerning the cosmological forecasts that are a primary justification for its submission to Physical Review D. The presentation of the main catalog results is also confusing. These issues must be thoroughly addressed before the paper can meet the standards for publication. I have detailed my findings below.

---
### Referee Report

**ESSENTIAL Revisions**

*   **P3-E1: Section V (p. 11) & Abstract (p. 1) — Incorrect Propagation and Misrepresentation of `f_NL` Forecast Uncertainty.**
    *   **Problem:** The paper incorrectly calculates and presents the 1σ uncertainty envelope for the forecasted constraint on `f_NL`. The analysis correctly finds a central value for the bias parameter `a_jk = 0.19` and its uncertainty `±0.65`. However, when propagating this to `σ(f_NL)`, the resulting 1σ envelope is given as `[3.92, 8.98]`. My recalculation shows the correct envelope is `[3.92, 5.95]`. The paper has erroneously used the baseline value for `a=0` (`σ(f_NL) = 8.98`) as the upper bound of the 1σ error bar. This is a fundamental error in uncertainty propagation and misrepresents the forecast. The same error is repeated for the "Gold+Silver" subset forecast, which should have an envelope of `[0.94, 8.08]`, not `[0.94, 8.98]`.
    *   **Fix:** Re-calculate the 1σ uncertainty envelope for `σ(f_NL)` by correctly propagating the uncertainty from the bias parameter `a`. This must be corrected in the abstract, Section V, and any other place it is mentioned (e.g., the conclusions). The text must accurately report the forecast and its statistical uncertainty.

*   **P3-E2: Section V (p. 11) & Abstract (p. 1) — Incorrect `f_NL` Improvement Percentage.**
    *   **Problem:** The paper claims a "7.9% improvement" in the `f_NL` constraint relative to the single-tracer baseline. The baseline is `σ(f_NL)std = 8.98` and the new central forecast is `σ(f_NL) = 8.14`. The fractional improvement in the constraint is `(8.98 - 8.14) / 8.98 = 9.35%`. The stated 7.9% is incorrect.
    *   **Fix:** Correct the percentage improvement calculation and update the value in the abstract and Section V.

*   **P3-E3: Section V (p. 11) & Appendix C (p. 15) — Inconsistent `f_NL` Forecast Methodology.**
    *   **Problem:** The main text (Section Vb) uses the asymptotic formula `1/σ(fNL)² = Fo + ca²` to calculate the forecast. However, Appendix C and Table VII use a "linear scaling" of the percentage improvement from the fiducial `a=0.15` result. These two methods are not equivalent and give significantly different results. For example, at `a=0.5`, the formula gives `σ(f_NL) ≈ 5.67`, while the table gives `7.15`. The paper cannot present two conflicting calculation methods without justification. The `Fo + ca²` form is only an approximation valid for small `a`.
    *   **Fix:** The author must choose a single, self-consistent method for the `f_NL` forecast. If the full Fisher calculation was performed for a range of `a`, those results should be used. If not, the limitations of the chosen approximation (be it the quadratic form or linear scaling) must be clearly stated, and it must be used consistently throughout the paper. The discrepancy between the two presented methods must be resolved.

*   **P3-E4: Section III D (p. 7) & Table I (p. 6) — Unclear Presentation of LAMOST Results.**
    *   **Problem:** The description of the LAMOST results is extremely confusing. The abstract mentions a "21.5× LAMOST rate compression," Section III D mentions a "rate reduction 21.5x to 2,054 at S > 5," and Table I footnote # also refers to a "21.5× rate-reduction diagnostic." It is impossible to discern what initial count or rate is being compared to what final count or rate to arrive at this factor. The text seems to contradict itself regarding which counts (cross-transfer vs. native) are being discussed.
    *   **Fix:** Rewrite the entire description of the LAMOST result for clarity. Explicitly state: (1) The cross-transfer anomaly count at a specific threshold (e.g., S>5). (2) The native-retrained anomaly count at the same threshold. (3) The calculation that leads to the 21.5x factor. This must be made unambiguous in the abstract, main text, and table footnotes.

**MAJOR Revisions**

*   **P3-M1: Table I (p. 6) — Confusing Table Structure.**
    *   **Problem:** Table I is the central summary of the paper's results, but its structure is confusing and obscures the main findings. The `N_anom` column shows the initial "cross-transfer" counts, which the paper argues are flawed. The final, primary "Path-C" native-retrained counts are not shown in the main table body and are instead buried in the extremely dense footnote `||`. A reader glancing at the table will get the wrong numbers.
    *   **Fix:** Redesign Table I to be clear and self-contained. It should include columns for both the "Initial (Cross-Transfer)" anomaly counts and the "Final (Path-C Native)" counts for each survey. This will make the "before and after" comparison, which is a core part of the paper's narrative, immediately obvious. Key information from the footnotes should be moved into the main table columns or a clearer caption.

*   **P3-M2: Abstract (p. 1) — Undocumented "Catalog-Grade Subset".**
    *   **Problem:** The abstract introduces a "recommended catalog-grade subset is ~265,000 unique objects (DESI + SDSS + EROSITA + Gaia + NEOWISE)". This is a significant sub-selection, but its derivation is not explained in the main text. The sum of the individual survey counts is ~275,000, but the final deduplicated number is not explicitly calculated.
    *   **Fix:** Add a paragraph in the main text (e.g., in Section IV) that explicitly defines this subset, lists the surveys included, shows the sum of their Path-C anomaly counts, and states the final unique object count after applying the deduplication procedure.

**MINOR Revisions**

*   **P3-m1: Section IV A (p. 4) — Ambiguous DESI Anomaly Definition.**
    *   **Problem:** The text describing the DESI anomaly selection is contradictory. It first states the "headline 195,829 DESI anomaly count is the top-1% score-cut" but later says it corresponds to "the S > 5.0 threshold, an anomaly rate of 0.87%". A top-1% cut is not the same as a 0.87% rate.
    *   **Fix:** Clarify the primary definition. It appears the `S > 5.0` threshold is the actual definition, which results in a 0.87% rate. The "top-1%" language should be corrected to reflect this (e.g., "a rate of ~0.87%, corresponding to the top percentile").

*   **P3-m2: Table IV (p. 14) — Unconventional Format.**
    *   **Problem:** Table IV, which lists "residual caveats," is formatted like an internal author-to-reviewer checklist rather than a formal table for a publication. The "ID" and "Resolution" columns are unconventional.
    *   **Fix:** Reformat this information into standard prose within a "Residual Caveats" subsection or into a more traditionally structured table. The content is valuable for transparency, but the presentation should be more formal.

**NIT (Nitpicks)**

*   **P3-N1: Throughout — Informal Jargon.**
    *   **Problem:** The phrase "FAIL-with-diagnostic" is used repeatedly. While the meaning is clear from context, it is slightly informal.
    *   **Fix:** Consider a more formal phrasing, such as "failed the gate, but with informative diagnostics" or similar, at least on first use.

---
## Summary recommendation
**MAJOR REVISIONS**

This manuscript presents a work of significant scale and effort that has the potential to be a valuable contribution to both astronomy and cosmology. The methodological insights are strong, and the public release of the catalog is a welcome outcome. However, the paper is marred by essential errors in the calculation and presentation of its key cosmological forecasts. As these forecasts are a primary motivation for the work and its submission to a physics journal like PRD, they must be correct. Furthermore, the presentation of the core catalog results in Table I is confusing and needs to be substantially improved for clarity.

I recommend that the paper undergo major revisions to address the critical issues outlined above. If the author can correct the `f_NL` forecast calculations and substantially improve the clarity of the main results, the revised manuscript would be a strong candidate for publication.

---

## PASS 2 — self-critique findings (what initial review missed)

Here are the additional findings from the second, more rigorous review pass.

---
### Additional Referee Findings (Second Pass)

**ESSENTIAL Revisions**

*   **P3-E5: Appendix E (p. 16) — Incorrect and Dimensionally Inconsistent NANOGrav Likelihood Equation.**
    *   **Problem:** Equation (E1), which defines the model for the NANOGrav analysis, appears to be incorrect. The term `- log10 T_obs` makes the right-hand side of the equation dimensionally inconsistent, as one cannot take the logarithm of a quantity with units (in this case, time). Furthermore, the overall structure of the equation, including the leading factor of `1/2` and the coefficients of the `log10 f_i` term, does not seem to match the standard expression for the power spectral density of a gravitational wave background derived from a characteristic strain power law.
    *   **Fix:** The author must provide the correct, dimensionally consistent equation used for the likelihood model. This is a critical error that undermines the validity of the entire NANOGrav result (`γ` posterior, Bayes factors), which is presented as a key cosmological application of the work. The derivation or a correct reference must be provided.

**MAJOR Revisions**

*   **P3-M3: Abstract (p. 1) & Section III E (p. 7) — Misleading Juxtaposition of eROSITA Validation Metrics.**
    *   **Problem:** The abstract presents two validation metrics for eROSITA side-by-side: an injection-recovery rate of 1.2% (which fails the paper's own gate) and a cross-validation stability of 81.5%. This is highly misleading. The very low injection-recovery rate indicates the detector is not robust to finding planted, out-of-distribution signals. The high cross-validation stability simply means that a different anomaly detector (Isolation Forest) agrees with the primary one (BIGAE) on the top-ranked native sources. This does not mitigate the failure of the injection-recovery test. Presenting a "good" number next to a "bad" one without context gives a false impression of robustness for a catalog that formally failed a key validation gate.
    *   **Fix:** The abstract and main text must clearly separate these two metrics and explain what they mean. It should be made explicit that the catalog failed the injection-recovery test and that the cross-validation stability, while high, measures a different property (inter-method agreement on in-distribution data) and does not override the injection-recovery failure.

**MINOR Revisions**

*   **P3-m3: Section VI C (p. 12) — Broken Internal Cross-Reference.**
    *   **Problem:** The text in Section VI C contains a cross-reference to `§VID (v)` when discussing the Gaia and eROSITA stability metrics. There is no subsection or item `(v)` in Section VI D or the corresponding Table IV. This appears to be a stale reference from a previous version of the manuscript.
    *   **Fix:** Correct the cross-reference to point to the correct location where these metrics are discussed (likely Table I, footnote `§`).