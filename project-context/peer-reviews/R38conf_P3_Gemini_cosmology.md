# P3 R38conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper3_anomaly_catalog_v3.1.104.pdf` md5=359a733d pages=29
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (3930 chars)
**Wall time**: 156.4s

---

## Referee Report: "Spectrally Unusual Sources at Scale..."

This paper presents a large-scale anomaly detection campaign across seven astronomical surveys using an autoencoder framework. The authors produce a catalog of 378,280 unique anomalies and explore cosmological applications, including constraints on primordial non-Gaussianity (f_NL) and consistency checks with NANOGrav results.

The scale of the undertaking is impressive, and the paper is commendably transparent about numerous methodological challenges, validation failures, and null results. This transparency is a significant strength. However, the sheer number of severe caveats, provenance failures, and heterogeneous selection criteria across the different survey tiers undermines the coherence of the final data product. The paper requires major revisions to clarify the status and limitations of the catalog and to ensure its responsible use by the community.

### ESSENTIAL Revisions

These issues must be addressed before the paper can be considered for publication.

*   **P1-E1 | Section IIIE, p. 1, 10 | eROSITA Score Axis Irreproducibility:** The paper states that the per-object score axis for the eROSITA tier is non-reproducible from any committed artifact and that the released tier is a fixed membership list. This is a critical failure of scientific provenance. While the authors are transparent about this, the implications must be stated more forcefully. A data product with a non-reproducible selection axis is of limited use for quantitative science (e.g., population statistics, score-weighted analyses).
    *   **Problem:** The abstract states "per-object SBigAE score axis non-reproducible". The body (p. 10) confirms "no committed score axis reproduces the production threshold."
    *   **Fix:**
        1.  The abstract and main body must explicitly state that the eROSITA tier is unsuitable for any analysis that relies on the anomaly score itself, and is provided as a fixed list of targets for phenomenological follow-up only.
        2.  The Data Availability section must re-iterate this, flagging the eROSITA score column with a warning that it is not the axis upon which the selection was made and is not reproducible.

*   **P1-E2 | Section IIIA, p. 1, 6 | DESI Anomalies Dominated by Non-Science Spectra:** The paper reveals that ~98.7% of the 195,829 DESI anomalies are not associated with primary science-class targets, but rather with "sky-fiber, secondary-target, or filler spectra." This is a stunning result that fundamentally changes the interpretation of the DESI catalog. The abstract mentions it, but its significance is somewhat buried in a complex sentence. This is the single most important finding regarding the DESI tier.
    *   **Problem:** The headline DESI count of ~196k is presented as a main result, but the vast majority of these are likely instrumental or processing artifacts, not astrophysically interesting sources. The "73x increase" claim is immediately deflated to "0.9x" for science targets.
    *   **Fix:**
        1.  The abstract must be rewritten to lead with this finding. For example: "The DESI-only tier of 195,829 anomalies is dominated (~98.7%) by spectra without primary science target flags, indicating a population of calibration or processing artifacts. The science-target-restricted subset contains only 2,468 anomalies, a number comparable to previous work."
        2.  The main discussion of the DESI results (Section IIIA) must be restructured to focus on the nature of these non-science-target anomalies. Are they sky-subtraction residuals? Crosstalk? Bad columns? Without this characterization, the catalog is difficult to use.

### MAJOR Revisions

These issues represent significant flaws in methodology or presentation that require substantial changes.

*   **P1-M1 | Section IIB, p. 3 | Data Leakage in Preprocessing:** The authors state that for the tabular surveys (eROSITA, NEOWISE, Gaia), feature scalers were fit on the full sample, including the validation and test sets, rather than on the training split alone. This constitutes data leakage. While the authors perform a robustness check for eROSITA and find ~15% churn, this is a flawed methodology that should be strongly discouraged.
    *   **Problem:** "Because the scalers are fit on the full sample rather than the training split alone, a small amount of validation-set (including tail) information enters the normalization constants".
    *   **Fix:** The authors must state unequivocally in the main methods section that this practice is incorrect and was a feature of a legacy pipeline. They should recommend that all future work fit scalers strictly to the training data. The conclusion that rankings are "robust" to this choice should be softened, as a ~15% churn in the extreme tail is not negligible.

*   **P1-M2 | Section IIB, p. 4 | Heterogeneous and Ad-Hoc Thresholds:** The anomaly thresholds are defined differently for nearly every survey: a fixed S>5 cut for DESI, 99th percentile for LAMOST/Gaia, a fixed-size "continuity slice" for SDSS, and a fixed-number list for eROSITA. This makes it impossible to compare anomaly rates or significance across surveys. The SDSS "continuity slice" is particularly problematic, as it is not a statistically principled threshold but one chosen to match a previous (and flawed) run's object count.
    *   **Problem:** The use of multiple, inconsistent thresholding schemes is confusing and hinders the creation of a uniform catalog. The justification for the SDSS slice is weak.
    *   **Fix:** The authors must add a dedicated paragraph in the Methods section (and summarize in the Discussion) acknowledging this limitation. They should explain *why* a single, uniform thresholding method (e.g., a fixed percentile cut for all surveys) was not used. They must explicitly warn users against comparing the raw anomaly counts/rates in Table I as if they were derived in a consistent manner.

*   **P1-M3 | Section IIIH, p. 12 | NEOWISE Injection Recovery Gate is Not a Sensitivity Test:** The paper reports that the NEOWISE tier passes its injection-recovery gate with 100% efficiency. However, the text reveals this is a "masking-geometry sanity check" where the test passes "by construction" and does not validate "the anomaly detector's sensitivity to planted signals."
    *   **Problem:** Presenting this as a "PASS" in the same context as the SDSS and Planck tests is misleading. It is a software QA check, not a validation of scientific performance.
    *   **Fix:** In all mentions of this test (abstract, main body, Table I, Figure 10), the result should be labeled "PASS (geometry only)" or similar. The text must clearly distinguish this from a true sensitivity test. The headline "3 PASS" count is misleading and should be restated as "2 PASS (sensitivity) + 1 PASS (geometry)".

*   **P1-M4 | Section IIIG, p. 12 | Gaia Preprocessing Provenance Failure:** Similar to the eROSITA issue, the paper states "the exact 20-feature production preprocessing script for this run was not recovered from pod backups".
    *   **Problem:** This is another failure of provenance that compromises the reproducibility of the Gaia results.
    *   **Fix:** This tier must be flagged as exploratory and not fully reproducible. This limitation should be mentioned in the abstract alongside the eROSITA issue and clearly noted in the Data Availability section.

*   **P1-M5 | Section V, p. 17-18 | Overstating Cosmological Application Readiness:** The paper presents f_NL and NANOGrav analyses. While correctly stating the results are not detections, the presentation implies the anomaly catalog is ready for use as a cosmological tracer. Given that 98.7% of the DESI anomalies (the largest component) are not science targets, and the other catalogs have significant issues, this is premature. The tracer sample used for the f_NL forecast is not well-defined or cleaned.
    *   **Problem:** The cosmological applications are built on a foundation that has been shown to be dominated by non-astrophysical signals (for DESI) and has other provenance issues.
    *   **Fix:** The Cosmological Applications section should be reframed as a "demonstration of methodology" or "proof-of-concept." The text must explicitly state that a cleaned, science-grade version of the anomaly catalog is required before these results can be considered robust cosmological constraints. The current result, `ajk = 0.19 ± 0.65`, is consistent with a null detection of any additional bias, which is the primary physical result.

### MINOR Revisions

*   **P1-N1 | Section IIIA, p. 8 | Inconsistent Denominators in Table II:** Table II is meant to clarify the DESI rates but is itself confusing. The denominators are a mix of spectra counts, catalog rows, and target counts.
    *   **Problem:** The table is difficult to interpret. For example, the "Per-class GALAXY" rate is on the "~4.9M TARGETTYPE subset", while the "Science-bit bitmask" is on "20.3M rows".
    *   **Fix:** Add a column explicitly defining the denominator type for each row (e.g., "Spectra", "Catalog Rows"). Add a footnote explaining why these different denominators are necessary and warning against simple conversions between rows.

*   **P1-N2 | Section IVD, p. 16 | Non-Diagnostic Null Result:** The Planck × ACT cross-correlation section reports a null result but then correctly explains that the null result is "largely guaranteed by footprint geometry alone" and is "non-diagnostic."
    *   **Problem:** Reporting a non-diagnostic test adds length without adding information.
    *   **Fix:** This section should be significantly shortened or removed. A brief mention in the limitations that a cross-correlation was not possible due to disjoint footprints would suffice.

*   **P1-N3 | Throughout | Internal Jargon:** The paper uses internal-sounding jargon like "Path-C rebuild protocol" and "catalog-grade tier" without clear, upfront definitions.
    *   **Problem:** This makes the paper difficult to read for an outside audience.
    *   **Fix:** Provide a glossary or a dedicated paragraph in the Introduction defining these key terms. "Path-C" should be defined as the final, native-retrained pipeline, to distinguish it from the initial cross-transfer attempt.

*   **P1-N4 | Abstract, p. 1 | Overly Complex Abstract:** The abstract is dense and contains too many nested clauses and parenthetical asides. It is difficult to parse the main takeaways.
    *   **Problem:** The abstract is not an effective summary for a reader trying to quickly grasp the paper's contributions.
    *   **Fix:** Rewrite the abstract to be more direct. Use shorter sentences. Separate the main results from the caveats more cleanly. For example, have one sentence for the headline number, followed immediately by a sentence with the key caveat.

### NITs (Cosmetic)

*   **P1-T1 | p. 2 | Contact Email:** The contact email `houston@hubify.com` appears to be non-institutional. While not prohibited, an institutional or persistent email address (e.g., via ORCID) is preferred for long-term contact.
*   **P1-T2 | Table I, p. 7 | Footnote Symbol Order:** The footnote symbols are non-standard (♡, ‡, §, ||, $, etc.). Standard symbols (a, b, c) or numbers are preferred for clarity.
*   **P1-T3 | Figure 2, p. 6 | Confusing Caption:** The caption says "the canonical Path-C unique count of 378,280 is not a deduplication of this baseline". This is confusing. A clearer phrasing would be: "This map shows the initial cross-transfer baseline. The final Path-C catalog, containing 378,280 unique objects, was generated from subsequent native-retrained analyses and is not a direct subset of the sources shown here."

## Summary recommendation

**MAJOR REVISIONS**

This paper represents a monumental effort in applying machine learning to large astronomical datasets. Its greatest contribution is the transparent documentation of the numerous ways this process can fail, providing a valuable set of lessons for the community. The LAMOST training bias, the cross-transfer domain shift for SDSS, and the dominance of non-science targets in the DESI sample are all critical findings.

However, the paper in its current form presents a data product with too many severe, unresolved issues to be published without significant revision. The irreproducible eROSITA and Gaia tiers, the dominance of artifacts in the DESI tier, and the heterogeneous selection criteria make the catalog difficult to use for robust science. The cosmological claims, while appropriately cautious, are premature.

The paper can become acceptable for publication in Physical Review D if the authors address the ESSENTIAL and MAJOR points listed above. The focus should shift from presenting a finished, multi-purpose catalog to a more methodological paper that presents a set of curated *target lists* of varying quality and completeness, with a primary emphasis on the lessons learned. The data product should be clearly stratified by quality, with strong warnings about the use of the flawed or artifact-dominated tiers.

---

## PASS 2 — self-critique findings (what initial review missed)

Here are the additional findings from a second, more detailed review of the paper.

================================================================
### Additional Findings from Second-Pass Review

This second pass focused on quantitative and cross-referential integrity, revealing several new issues not caught in the initial review.

### MAJOR Revisions

*   **P2-M1 | Section IVB, p. 14 | Incorrect Spatial Clustering Statistic:** The calculation of the Cramér's V statistic, used to quantify the non-uniformity of the spatial distribution, is arithmetically incorrect.
    *   **Problem:** The paper reports `χ² = 376,713` with `N = 378,280` objects and `k = 24,049` pixels, yielding a claimed `Cramér's V ≈ 0.020`. Re-computation using the paper's own formula `V = sqrt(χ²/(N*(k-1)))` yields `V ≈ 0.0064`. The reported value is incorrect by a factor of three.
    *   **Impact:** While the conclusion of non-uniformity (driven by survey footprints) still holds due to the large `χ²`, the effect size is substantially smaller than claimed. An incorrect key statistic undermines confidence in the quantitative analysis.
    *   **Fix:** The authors must correct the value of Cramér's V and revise the text to reflect the smaller (though still statistically significant) effect size. They should double-check the formula's implementation and the interpretation of the result.

*   **P2-M2 | Appendix E, p. 25 | Dimensionally Inconsistent Equation:** Equation (E1), which defines the matter-bounce power-law template for the NANOGrav analysis, appears to be dimensionally inconsistent.
    *   **Problem:** The equation adds logarithmic terms of different physical quantities, specifically `log(frequency)` and `log(time)` (`- γ log10 fi - γ log10 Tobs`). This is physically and mathematically invalid. The power spectral density should be a function of frequency only.
    *   **Impact:** This error calls into question the entire NANOGrav fitting procedure described in Appendix E and used in Section VA. If the model template is incorrect, the resulting posterior on `γ` is unreliable.
    *   **Fix:** The authors must carefully review the derivation and implementation of their PTA likelihood model. The equation must be corrected to be dimensionally consistent, and the MCMC analysis must be re-run with the corrected model. The results in the abstract and Section VA must be updated accordingly.

### MINOR Revisions

*   **P2-N1 | Abstract, p. 1 | Incorrect Cross-Reference:** The abstract contains an incorrect internal cross-reference that points to a non-existent section.
    *   **Problem:** The abstract states "(the size benchmark is anchored to the largest published single-survey anomaly catalog [11]; §VIE)". Section VIE does not exist in the paper. The relevant discussion of the benchmark appears in the Introduction (p. 2).
    *   **Fix:** Correct the cross-reference to point to the appropriate section, or remove it from the abstract for conciseness.

*   **P2-N2 | Abstract, p. 1 & Section IIID, p. 10 | Ambiguous LAMOST Rate Reduction:** The comparison used to demonstrate the 21.5x reduction in the LAMOST anomaly rate is presented ambiguously.
    *   **Problem:** The abstract presents the reduction as a change in the number of `S > 5` objects (44,075 → 2,054). However, the main text (Table I, Section IIID) identifies the 44,075 count as the result of a top-percentile cut on the initial cross-transfer run, not an `S > 5` cut. It is unclear if the "before" and "after" counts were derived using a consistent threshold, making the 21.5x factor difficult to interpret.
    *   **Fix:** The authors must clarify the exact selection criteria for the 44,075 "before" count. The comparison should be made between two consistently defined samples (e.g., rate at `S > 5` before vs. after, or top-1% rate before vs. after). The abstract and main text must be updated to reflect this consistent comparison.