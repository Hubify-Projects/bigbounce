# P3 auto-2026-06-08_1424pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 168.9s

---

## Referee Report: Spectrally Unusual Sources at Scale...

This paper presents a large-scale anomaly detection analysis across seven astronomical surveys, resulting in a catalog of 378,280 unique anomalous sources. The authors use an autoencoder framework (BIGAE), develop a robust "Path-C" validation protocol involving native retraining for each survey, and explore cosmological applications of the resulting catalog, including constraints on primordial non-Gaussianity (fNL) and consistency checks with matter-bounce predictions for the gravitational-wave background.

The scale of this work is impressive, and the methodological discussion is exceptionally thorough and self-critical. The authors' transparency in documenting and resolving initial methodological failures (e.g., the cross-transfer artifacts for SDSS and LAMOST) is a significant strength and provides valuable lessons for the community. The resulting catalog is a substantial contribution. The cosmological applications are well-motivated and carefully analyzed, particularly the handling of systematic effects in the fNL forecast and the nuanced interpretation of the NANOGrav results.

However, several points require clarification and correction before the manuscript can be accepted for publication in Physical Review D. The findings are detailed below.

---
### ESSENTIAL Revisions

*   **P3-E1**
    *   **Location:** Page 2, Section II B, paragraph "Two threshold families..."
    *   **Problem:** The text states: "DESI DR1 and SDSS DR18 use an absolute canonical-S cut at S > 5.0...". This is directly contradicted by the detailed description in Section III C (Page 5) and the footnotes of Table I (Page 7), which explain that the final SDSS DR18 anomaly set is a top-percentile slice of native-retrained scores (S ≥ 0.1060), and that applying the S > 5 cut to the native scores yields only 12 sources. This contradiction is highly confusing for a reader trying to understand the selection criteria.
    *   **Fix:** The sentence on Page 2 must be corrected to accurately reflect the final methodology used for the SDSS catalog. It should be made clear that different thresholding approaches were used for the initial cross-transfer analysis (for diagnostic purposes) and the final native-retrained catalog.

---
### MAJOR Revisions

*   **P3-M1**
    *   **Location:** Page 1, Abstract
    *   **Problem:** The abstract presents the injection-recovery results as: "3 PASS ... and 3 FAIL-with-diagnostic at 5σ (LAMOST 5.8%, Gaia 5.2%, eROSITA 1.2%; eROSITA cross-validation stability 81.5%)". Juxtaposing the "FAIL" status for eROSITA (based on 1.2% injection recovery) with its high "cross-validation stability 81.5%" is confusing without the context provided deep in the paper. In the condensed format of an abstract, this reads like a contradiction and undermines the clarity of the validation summary.
    *   **Fix:** Rephrase this part of the abstract to avoid the apparent contradiction. For example, clarify that the "FAIL" status refers specifically to the injection-recovery test, while other metrics like cross-validation stability were also assessed. A possible phrasing could be: "...3 FAIL the 5σ injection-recovery test (LAMOST 5.8%, Gaia 5.2%, eROSITA 1.2%), though eROSITA shows high cross-validation stability (81.5%)."

---
### MINOR Revisions

*   **P3-m1**
    *   **Location:** Page 1 (Abstract) and Page 11 (Section V B)
    *   **Problem:** The paper claims a "7.9% improvement" for the central forecast of σ(fNL). Based on the provided baseline σ(fNL)std = 8.98 and the new central forecast σ(fNL) = 8.14, the fractional improvement is (8.98 - 8.14) / 8.98 = 9.35%. The source of the 7.9% figure is not apparent from the text or calculations.
    *   **Fix:** Please verify this calculation. Either correct the percentage to 9.4% or provide the explicit calculation that leads to 7.9%.

*   **P3-m2**
    *   **Location:** Page 5, Section III C
    *   **Problem:** The text states that the SDSS native retrain "re-scores 1,925,279 spectra" from the full input of 2,304,830 spectra. The reason for this ~16% reduction in the number of scored objects is not given.
    *   **Fix:** Briefly state the reason for scoring a subset of the full SDSS sample (e.g., "after applying quality cuts," or similar).

*   **P3-m3**
    *   **Location:** Page 1, Introduction
    *   **Problem:** The introduction lists ACT alongside the other surveys whose data are combined. However, the abstract and Appendix F make it clear that ACT DR6 was "quarantined as a cross-transfer artifact" and does not contribute to the final unique anomaly count. Listing it without this immediate qualification could be misleading.
    *   **Fix:** Add a brief parenthetical note in the introduction when ACT is first mentioned, indicating its quarantined status in the final analysis (e.g., "...and microwave sky surveys from Planck [7] and ACT [9] (the latter quarantined in the final analysis)").

---
### NIT (Cosmetic)

*   **P3-N1**
    *   **Location:** Page 19, Reference [33]
    *   **Problem:** The reference includes an explanatory note: "[publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity]". This reads like an internal author note and is unconventional for a journal publication.
    *   **Fix:** Please format the citation conventionally according to journal style.

*   **P3-N2**
    *   **Location:** Page 1, Abstract
    *   **Problem:** The term "FAIL-with-diagnostic" is internal jargon that may not be immediately clear to all readers of an abstract.
    *   **Fix:** Consider rephrasing for broader accessibility, for instance: "three surveys failed the primary recovery test but provided informative diagnostics."

---
## Summary recommendation
**MAJOR REVISIONS**

This is a high-quality, comprehensive, and methodologically rigorous paper that presents a valuable data product and compelling scientific analysis. The work is well-suited for publication in Physical Review D. However, the identified issues, particularly the direct contradiction regarding the SDSS selection criteria (P3-E1) and the confusing presentation of validation results in the abstract (P3-M1), must be addressed to ensure the manuscript is clear, accurate, and unambiguous. Once these revisions are made, the paper should be in excellent shape for acceptance.