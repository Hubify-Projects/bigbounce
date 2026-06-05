# P5 R10v3p1 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 170.7s

---

**Referee Report on "Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with V-Web Cross-Check Across 791,635 DR1 Matched Spirals"**

This paper presents a detailed investigation into the potential dependence of spiral galaxy chirality on large-scale structure environment, using data from the DESI Data Release 1 and a new, large-scale chirality catalog. The primary method involves classifying galaxies into cosmic-web environments (void, wall, filament, cluster) and testing for any statistically significant variation in the clockwise (CW) fraction. The paper's headline result is a null detection: after accounting for a small, global, catalog-wide bias, spiral chirality is found to be independent of environment at the sensitivity level of the DESI DR1 dataset.

The analysis is exceptionally thorough, employing multiple cosmic-web classifiers (V-Web, DESIVAST's suite, Tempel+2014 FoF, ASTRA), performing numerous robustness checks against methodological choices (e.g., the Phase 2 hyperparameter sweep), and carefully investigating potential systematics (e.g., survey geometry, target selection, redshift-space distortions). The author is commendably transparent about the analysis path and its limitations. The use of the peer-reviewed DESIVAST void catalog for the primary analysis is a particular strength, as it grounds the main conclusion on a robust, public data product and a very large sample of void galaxies.

While the quality of the analysis is high, there is one essential issue that precludes acceptance of the manuscript in its current form. Several minor points also require attention.

---
### Detailed Findings

#### ESSENTIAL

*   **P5-E1: Critical Dependence on Unpublished, Inaccessible Work (Paper IV)**
    *   **Section/Page:** Throughout, but explicitly stated in Sec. I (p. 2), Sec. II (p. 2), and used in Eq. (1) (p. 4), Fig. 2 (p. 5), Fig. 3 (p. 7), etc.
    *   **Problem:** The paper's entire analysis framework and interpretation rely critically on inputs from a companion work, "Paper IV [3]", which is cited as "in preparation and not yet peer reviewed". These inputs are:
        1.  The 8.47M-galaxy chirality catalog itself, which provides the fundamental labels being tested.
        2.  The "catalog-monopole offset" of `Δfcw = -0.0026`, which is the baseline against which all environmental deviations are measured.
        3.  The crucial claim that this monopole is a "classifier-residual bias" and not a cosmological signal.
    *   As Paper IV is not available, a referee or reader cannot verify the methods used to generate the chirality labels, assess the evidence for the monopole being a systematic, or validate the derivation of its value. This makes the current manuscript's central claims unverifiable. A paper submitted to PRD must be self-contained and allow for independent evaluation.
    *   **Required Fix:** The manuscript must be made self-contained. The author should add a substantial appendix that summarizes the essential information from Paper IV. This appendix must include, at a minimum:
        a) A description of the machine learning classifier architecture, training data, and the Z2 equivariant test-time augmentation procedure used to generate the chirality labels.
        b) A summary of the validation tests performed on the classifier.
        c) A detailed explanation and presentation of the evidence that establishes the catalog-wide `Δfcw` offset as a classifier-based systematic rather than a physical, cosmological signal.
        d) The explicit derivation of the value `Δfcw = -0.0026` and its uncertainty.

#### MAJOR

*(No findings classified as MAJOR. The essential issue above is the primary barrier.)*

#### MINOR

*   **P5-M1: Discrepancy in Predicted Sigma Value**
    *   **Section/Page:** Sec. VI A, p. 5.
    *   **Problem:** The text states: "predicting σ_pred from Δfcw = -0.0026 gives σ_pred(filament) ≈ -3.16". However, a direct calculation using Eq. (1) (`σ_pred = 2 * Δfcw * sqrt(N)`) with the values from Table II (`N=408,187`) yields `2 * (-0.0026) * sqrt(408187) ≈ -3.32`. This is a ~5% discrepancy from the quoted value. While this does not change the conclusion that the observed value is of a similar order, the predicted value should be calculated and quoted correctly. The prediction for the cluster class (`-3.28`) is correct.
    *   **Required Fix:** Please re-calculate and correct the value of `σ_pred(filament)`. If there is a subtlety in the calculation (e.g., a different `Δfcw` for this subsample), it must be explicitly stated and justified.

#### NIT (Nitpick/Cosmetic)

*   **P5-N1: Future Date on Manuscript**
    *   **Section/Page:** Title page, p. 1.
    *   **Problem:** The date of the manuscript is listed as "(Dated: June 4, 2026)".
    *   **Required Fix:** Correct the date to the current submission date.

*   **P5-N2: Inconsistent Sigma Notation in Abstract**
    *   **Section/Page:** Abstract, p. 1.
    *   **Problem:** The abstract reports sigma values with inconsistent precision. For example, `−2.61σ` and `−4.66σ` are given to two decimal places, while `+0.55σ` and `−0.68σ` are also given to two, but the text later refers to a `~5pp` statistical floor. It would be clearer to maintain consistent precision, e.g., one decimal place, or ensure the quoted precision is statistically meaningful for each bin. For the wall class, `+0.6σ` is likely sufficient.
    *   **Required Fix:** Consider reporting sigma values to a consistent and statistically justified precision (e.g., one decimal place) in the abstract for clarity.

---
## Summary recommendation

**MAJOR REVISIONS**

This is a high-quality, thorough, and statistically robust paper that presents a compelling null result on an interesting cosmological question. The multi-layered analysis and extensive cross-checks are exemplary. However, the paper cannot be accepted in its current form due to its foundational reliance on an unpublished and inaccessible companion paper (Paper IV). The scientific record must be verifiable, and as it stands, the core inputs to this paper's analysis—the chirality labels and the systematic baseline—are not.

If the author can address the essential issue by incorporating the required methodological details from Paper IV into an appendix, thereby making the present work self-contained and verifiable, the paper will be on a clear path toward publication in Physical Review D. The minor calculation correction should also be addressed.