# P3 RA-INT — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p3_anomaly_engine/paper3_draft.pdf` md5=24ac287f pages=30
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 176.6s

---

# Referee Report

**Paper ID:** P3
**Journal:** Physical Review D
**Title:** Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 269,317 Recommended-Tier (378,280 Total) Path-C Unique Anomalies and a Native-Trained Novelty Fraction from 37.3 Million Sources and Map Patches

This paper presents a large-scale anomaly detection campaign across seven major astronomical surveys (DESI, SDSS, LAMOST, eROSITA, Planck, Gaia, NEOWISE), producing a catalog of 378,280 unique anomalies. The work is notable for its scale, its multi-survey approach enabling cross-validation, and its application to cosmological parameter constraints (primordial non-Gaussianity and the stochastic gravitational-wave background). The methodology is centered on a deterministic autoencoder framework (BIGAE), with a detailed "Path-C" protocol for per-survey native retraining and validation.

The paper is exceptionally well-written, methodologically rigorous, and commendably transparent about its limitations and the provenance of its results. The distinction between a full-stream anomaly rate and a like-for-like science-target rate, the careful qualification of novelty metrics, and the sober interpretation of the cosmological results are all hallmarks of high-quality scientific work. The methodological lessons, particularly from the LAMOST training-bias artifact and the SDSS cross-transfer domain shift, are valuable contributions to the field.

The work is substantial and appropriate for publication in Physical Review D. However, several revisions are required to meet the journal's standards for clarity, completeness, and provenance.

---
## Findings

### ESSENTIAL

**P3-E1**
*   **Section/Page:** Title block, Page 1
*   **Problem:** The paper is dated "June 28, 2026". This is a future date and must be corrected to the actual submission date.
*   **Required Fix:** Replace the placeholder date with the correct date of submission.

**P3-E2**
*   **Section/Page:** Abstract (p. 1) and §V (p. 17)
*   **Problem:** The abstract states "the central 9.4% improvement is a noise-driven forecast pending higher-S/N follow-up, not a detection". While correct, the body of the paper (§Vb, p. 17) provides a more precise and powerful statement: "The de-biased amplitude... returns the single-tracer baseline σ(fNL) = 8.98 exactly (no improvement)". The abstract should reflect this stronger, de-biased result, which is the proper statistical conclusion. Reporting the naive plug-in improvement, even with a caveat, is less clear than stating the de-biased result is null.
*   **Required Fix:** Revise the abstract to state the primary result from the de-biased estimator. For example: "An empirical bias measurement and subsequent de-biasing of the multi-tracer forecast returns the single-tracer baseline exactly, indicating no improvement at current signal-to-noise. The Fisher-positive envelope of the noisy measurement is [3.92, 8.98], with the central value improvement being consistent with statistical noise." This is more aligned with the rigorous conclusion in the main text.

### MAJOR

**P3-M1**
*   **Section/Page:** §IIB (p. 3), §IIIG (p. 13), Data Availability (p. 24)
*   **Problem:** The paper is transparent that the exact preprocessing script for the Gaia DR3 analysis was not recovered from a committed backup and was instead "lineage-inferred". This represents a significant gap in the provenance and reproducibility of the Gaia portion of the catalog. While the transparency is commendable, the implications must be made clearer. The Gaia component is part of the "recommended tier" but fails injection recovery and has this provenance issue, making its inclusion in any tier above "explicitly exploratory" questionable.
*   **Required Fix:**
    1.  In the abstract, explicitly add the "inferred preprocessing" caveat to the list of reasons why the Gaia (and eROSITA) components are exploratory.
    2.  In §IIIG, the "best-available rather than fully reproducible" statement is good. Consider adding a sentence on how a future user could attempt to reproduce the feature set from the successor script `gaia_expanded.py`.
    3.  The Gaia tier should be more strongly caveated throughout the paper as being of lower quality/robustness than the DESI, SDSS, and Planck tiers, not just for the failed gate but also for this reproducibility issue.

**P3-M2**
*   **Section/Page:** §IIB (p. 3)
*   **Problem:** The methodology of fitting scaler statistics on the full data sample, rather than strictly on the training split, introduces information leakage from the validation set. The authors acknowledge this and provide a robustness check for eROSITA, finding ~15-17% churn in the extreme tail. This is a non-trivial level of instability. The assumption that this "does not materially reorder the within-survey anomaly ranking" is stated but not demonstrated for all tabular surveys (NEOWISE, Gaia).
*   **Required Fix:**
    1.  The abstract should briefly mention this methodological choice and its potential impact on extreme-tail membership stability as a general caveat for the tabular survey components.
    2.  The robustness check performed for eROSITA should also be performed and reported for NEOWISE and Gaia to quantify the membership churn for all affected surveys. If this is not possible due to the provenance issues with the Gaia script, this should be stated as an additional limitation.

### MINOR

**P3-N1**
*   **Section/Page:** Table I, footnote || (p. 9)
*   **Problem:** The footnote states "The Path-C per-survey native counts... sum to 388,493". However, adding the `N_anom` values from the main table block for the Path-C native results gives: 195829 (DESI) + 77905 (SDSS) + 113342 (LAMOST) + 298 (eROSITA) + 200 (Planck) + 500 (Gaia) + 419 (NEOWISE) = 388,493. The LAMOST value used here is 113,342, which is the native re-score result from §IIID, but the value in the table is 44,075 with a `‡` symbol. This is confusing. The table should consistently display the final Path-C counts.
*   **Required Fix:** Update the `N_anom` column in Table I to show the final, canonical Path-C native counts for all surveys (e.g., 113,342 for LAMOST). The cross-transfer counts (like 44,075) should be clearly confined to the footnotes or a separate column labeled "Cross-transfer baseline" to avoid ambiguity. The current presentation requires the reader to synthesize information from multiple paragraphs to understand the table's primary numbers.

**P3-N2**
*   **Section/Page:** §IVB (p. 15)
*   **Problem:** The spatial uniformity test reports a χ² = 376,713 for dof = 24,048, leading to χ²/dof ≈ 15.7. The text correctly notes the statistical significance but also correctly computes Cramér's V ≈ 0.0064 to show the effect size is negligible. However, the text does not provide a p-value for the χ² test. While it is clearly infinitesimal, for completeness it should be stated.
*   **Required Fix:** State the p-value corresponding to the χ² test (e.g., p << 10⁻¹⁰⁰) to complete the statistical reporting, while retaining the crucial emphasis on the small effect size (Cramér's V).

**P3-N3**
*   **Section/Page:** §VA, NANOGrav Bounce Consistency (p. 19)
*   **Problem:** The text reports the posterior for γ as `γ = 2.567 ± 0.382 (Gaussian-approximation...)` and also gives a quantile summary `γ = 2.591 +0.291/-0.287`. It then states `±0.382 is the appropriate mean-shift uncertainty for the +1.13σ parameter-shift test`. This is a subtle but important point. It would be clearer to explicitly state why the standard deviation is preferred over the credible interval width for this specific test (i.e., because the test is a simple difference of means, for which the standard error of the mean is the relevant uncertainty).
*   **Required Fix:** Add a brief clause explaining why the sample standard deviation is the appropriate uncertainty for the parameter-shift test being performed.

**P3-N4**
*   **Section/Page:** Figure 10 Caption (p. 23)
*   **Problem:** The caption states that the NEOWISE gate "is therefore not counted as a detector-sensitivity PASS". This is also stated in the abstract and §VID(ii). However, the figure itself plots NEOWISE alongside the other curves without a visual distinction (e.g., different line style, annotation) that would immediately signal its different nature as a "geometry-QA" test.
*   **Required Fix:** In Figure 10, modify the line or label for NEOWISE (e.g., make the line dashed, add "(geometry QA)" to the legend entry) to visually reinforce the distinction made in the text.

### NIT

**P3-T1**
*   **Section/Page:** Table I, header (p. 9)
*   **Problem:** The column header "SIMBAD-unmatched (%)" is slightly ambiguous. It could mean the percentage of SIMBAD that is unmatched, rather than the percentage of anomalies that are unmatched in SIMBAD.
*   **Required Fix:** Suggest changing the header to "% Unmatched in SIMBAD" for clarity.

**P3-T2**
*   **Section/Page:** §IIIE (p. 11)
*   **Problem:** The text states "the production run's 0.259 threshold could not be reconciled with any tested score axis". A few lines later it says "reproduces 0.259 on none of them". The first phrasing is slightly better and more precise.
*   **Required Fix:** For consistency, consider using the "could not be reconciled" phrasing in both instances. This is a minor stylistic point.

**P3-T3**
*   **Section/Page:** Bibliography (p. 29-30)
*   **Problem:** Reference [1] for DESI DR1 is listed as "(accepted 2025), arXiv:2503.14745". The arXiv ID appears to have a year prefix of '25', implying 2025. This is likely a typo for '23' or '24'.
*   **Required Fix:** Please verify and correct the arXiv identifier and year for reference [1].

---
## Summary recommendation

**MAJOR REVISIONS**

This is a landmark paper in the application of unsupervised machine learning to large astronomical datasets. The scale is impressive, the methodology is generally very strong, and the authors' commitment to transparency regarding the many "real-world" challenges of such an analysis (e.g., training bias, irreproducible pipelines, domain shift) is exemplary. The cosmological applications, while not yielding detections, are correctly and carefully framed as updated constraints and consistency checks.

The recommendation for "Major Revisions" is not due to a fundamental flaw in the analysis, but rather to the need to fully address the significant provenance issue with the Gaia data pipeline (P3-M1) and the data-leakage issue in the tabular-survey preprocessing (P3-M2). These issues impact the reproducibility and robustness of specific components of the final data product. The requested revisions will ensure that the final paper fully and clearly communicates these caveats to the reader at all levels (abstract, body, data release documentation), thereby upholding the high standards of rigor and reproducibility expected by Physical Review D. The other requested changes are relatively minor and will further improve the paper's clarity and completeness. I look forward to reviewing a revised version of this excellent work.