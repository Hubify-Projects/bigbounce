# P5 auto-2026-06-05_1919pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 1362.3s

---

**Referee Report for "Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with V-Web Cross-Check Across 791,635 DR1 Matched Spirals"**

This paper presents a detailed investigation into the potential dependence of spiral galaxy chirality on the large-scale structure environment, using data from the DESI Data Release 1 and a companion chirality catalog. The author performs a comprehensive analysis using multiple cosmic-web classifiers (V-Web, DESIVAST, Tempel+2014, ASTRA) and a wide array of statistical tests and robustness checks. The primary conclusion is a null result: spiral galaxy handedness is found to be statistically independent of environment, once a previously identified catalog-wide systematic monopole offset is accounted for.

The analysis is exceptionally thorough, and the author's approach of using multiple independent classifiers and explicitly testing for systematics related to survey geometry, tracer populations, and analysis hyperparameters is commendable. The paper is well-structured, and the results are presented transparently, with a clear distinction between primary and secondary analysis paths and a frank discussion of limitations.

However, despite the high quality of the analysis itself, there are several critical issues that must be addressed before the paper can be considered for publication in Physical Review D.

---
### Detailed Findings

#### ESSENTIAL

*   **P5-E1: Dependency on unpublished work (Paper IV)**
    *   **Section/Page:** II, p. 2 (and throughout)
    *   **Problem:** The analysis critically depends on the "8,474,531-galaxy chirality catalog of Paper IV [3]". Reference [3] is listed as "in preparation; manuscript in preparation." A paper in Physical Review D cannot be based on a primary data source that is not publicly available and has not undergone peer review. The results are not independently verifiable without this catalog and a full description of its methodology.
    *   **Required Fix:** Paper IV must be made publicly available (e.g., on arXiv) and submitted for peer review. The present manuscript should not be published until Paper IV is at least accepted for publication, or the catalog and its generation method are fully documented within this paper's appendices to make the work self-contained and reproducible.

*   **P5-E2: Misinterpretation of Paper IV's global monopole significance**
    *   **Section/Page:** II, p. 2
    *   **Problem:** The text states that the Paper IV global CW fraction of 0.4974 ± 0.000279 is "consistent with parity at ~1σ". A direct calculation shows the deviation from parity (0.5) is (0.5 - 0.4974) / 0.000279 = 0.0026 / 0.000279 ≈ 9.3σ. This is a highly significant deviation, not a ~1σ fluctuation. While the paper correctly interprets this as a *classifier-monopole offset* rather than a cosmological signal, the "consistent with parity" language is factually incorrect and highly misleading.
    *   **Required Fix:** Remove the phrase "consistent with parity at ~1σ". State clearly that the global CW fraction shows a statistically significant (9.3σ) deviation from 0.5, which Paper IV attributes to a systematic classifier-monopole offset. This correction must be propagated to any other part of the manuscript that makes a similar claim.

#### MAJOR

*   **P5-M1: Unconventional future dating of manuscript and references**
    *   **Section/Page:** Title page (p. 1) and Bibliography (p. 20)
    *   **Problem:** The manuscript is dated "June 4, 2026". Several key references ([11], [12], [13]) are also cited with future publication years (2025, 2026). This is highly unconventional for a submitted manuscript and is not standard practice.
    *   **Required Fix:** The manuscript date should be updated to the current date of submission/revision. All reference dates should be corrected to reflect their actual publication or preprint dates. For preprints, use the year they appeared on arXiv.

*   **P5-M2: Discrepancy in predicted significance for filament class**
    *   **Section/Page:** VI A, p. 5
    *   **Problem:** The text predicts the monopole-induced significance for the filament class as "σ_pred(filament) ≈ -3.16". A calculation using the provided formula (Eq. 1) and numbers (N=408,187, Δfcw=-0.0026) yields σ_pred = 2 * (-0.0026) * sqrt(408187) ≈ -3.32. This is a ~5% discrepancy. The prediction for the cluster class (σ_pred ≈ -3.28) is correct.
    *   **Required Fix:** Please re-calculate and correct the predicted significance for the filament class, or clarify the source of the discrepancy.

#### MINOR

*   **P5-m1: Sign error in abstract for DESIVAST Δfcw**
    *   **Section/Page:** Abstract, p. 1
    *   **Problem:** The abstract states for the DESIVAST-anchored re-projection: "returns f_cw^void = 0.4964 vs f_cw^non-void = 0.4971, Δfcw = 0.0007". The calculation is f_cw^void - f_cw^non-void = 0.4964 - 0.4971 = -0.0007. The sign is incorrect in the abstract.
    *   **Required Fix:** Correct the sign of Δfcw in the abstract to -0.0007.

*   **P5-m2: Ambiguous statement about V-Web void sample size at z≤0.24**
    *   **Section/Page:** Abstract, p. 1
    *   **Problem:** The abstract states: "the V-Web void class at z≤0.24 is sample-size limited at n=428". This is confusing. Table II shows the full V-Web void sample has n=428. Section VIII A clarifies that restricting to z≤0.24 leaves only n=6 V-Web void spirals. The abstract incorrectly conflates the full sample size with the low-redshift subsample.
    *   **Required Fix:** Rephrase the abstract to clarify. For example: "...the V-Web void class is sample-size limited with n=428 spirals over the full redshift range, and is dominated by survey-edge artifacts at z≤0.24 (see §IX B)..."

#### NIT

*   **P5-N1: Typo in σ_from_half definition**
    *   **Section/Page:** V, p. 4
    *   **Problem:** The definition of σ_from_half is given as "σ_from_half = (ncw – 0.5N)/(0.5√/N)". The "/" after the square root symbol appears to be a typo.
    *   **Required Fix:** Change "(0.5√/N)" to "(0.5√N)".

---
## Summary recommendation

**MAJOR REVISIONS**

The analytical work in this paper is of a very high standard, demonstrating rigor, depth, and transparency. The primary conclusion of a null environmental dependence of spiral chirality is well-supported by an impressive suite of tests. However, the paper in its current form cannot be accepted due to two essential issues: its critical reliance on an unpublished and unavailable data catalog (Paper IV), and a significant factual error in the interpretation of that catalog's global signal relative to parity. These issues undermine the reproducibility and credibility of the results. Once these essential points, along with the other major and minor issues listed above, are fully addressed, the manuscript will likely be suitable for publication.