# P3 R32conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper3_anomaly_catalog_v3.1.93.pdf` md5=a3504a9b pages=28
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 167.8s

---

**Referee Report on "Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies and Native-Trained Novelty Fractions from 37.3 Million Sources and Map Patches"**

This paper presents a large-scale anomaly detection study across seven major astronomical surveys, resulting in a catalog of approximately 378,000 unique anomalous sources. The authors employ an autoencoder framework and introduce a robust "Path-C" validation protocol involving native retraining to mitigate cross-survey artifacts. The work is notable for its scale, methodological rigor, and transparent reporting of limitations. The catalog is applied to two cosmological problems: constraining primordial non-Gaussianity (fNL) and testing matter-bounce predictions against NANOGrav data.

The paper is well-written, the analysis is thorough, and the conclusions are appropriately conservative and well-supported by the evidence presented. The authors are commended for their diligence in identifying and characterizing systematic effects, such as the LAMOST training bias and the crucial distinction between science-target and full-stream anomaly rates for DESI. The work represents a significant contribution to the field of astronomical anomaly detection and its application to cosmology.

While the paper is of high quality, several minor revisions are required to meet the archival standards of Physical Review D. These revisions primarily involve removing internal-review artifacts and meta-commentary on the paper's own development history.

---
### Detailed Findings

**ESSENTIAL**

*   **P3-E1:** Abstract, Page 1
    *   **Problem:** The abstract contains meta-commentary about a previous version of the manuscript: "an earlier draft quoted 264,938/264,738 from headline-minus-LAMOST subtraction arithmetic, which double-removes the 4,379 LAMOST detections that merge into catalog-grade clusters at 5")". An archival journal article should present the final, definitive results and their derivation, not a history of its own internal calculations. This text is confusing and detracts from the final, reported numbers.
    *   **Required Fix:** Remove this sentence. State the final catalog counts and their composition directly. The provenance of the LAMOST component and its relation to the catalog-grade tier is sufficiently explained in the body of the paper.

**MAJOR**

*   **P3-M1:** Appendix C, Page 22
    *   **Problem:** The appendix is titled "Legacy Fixed-a = 0.15 Sensitivity Reference (Superseded)". The term "Superseded" is an internal versioning note and is not appropriate for a final publication. While retaining the fixed-α forecast for context may be useful, it should not be framed as a "legacy" or "superseded" result.
    *   **Required Fix:** Re-title the appendix to something like "Appendix C: Fisher Forecast with a Fixed Bias Prior". Remove the word "Superseded" from the title and "Legacy reference only" from the first sentence. The text should clearly state that this is a forecast under a fixed-prior assumption, presented for comparison with the main empirical result from §V, which uses a measured (and uncertain) bias.

*   **P3-M2:** Figure 9 Caption, Page 18
    *   **Problem:** The figure caption begins with "Legacy fixed-a reference — superseded by the empirical ajk result of §V." This is the same issue as P3-M1. It is inappropriate meta-commentary.
    *   **Required Fix:** Revise the caption to be a direct description of the figure's content. For example: "Per-redshift-bin decomposition of the Fisher forecast for a fixed anomaly-tracer bias prior of α = 0.15 (cf. Appendix C). The primary forecast in this work uses the empirically measured bias reported in §V, which is consistent with no multi-tracer improvement."

**MINOR**

*   **P3-m1:** §IIB, Page 3
    *   **Problem:** The text states, "we state explicitly that the Gaia preprocessing specification is lineage-inferred rather than directly recovered." This transparency is commendable. However, the subsequent sentence notes that fitting scalers on the full sample (including the validation set) introduces a small information leak. While the authors correctly assume it does not materially reorder the ranking, this is a methodological weakness.
    *   **Required Fix:** Add a sentence clarifying that while this practice is common for expediency, future work should strictly fit normalization constants only to the training split to avoid any potential for information leakage, however minor. This reinforces best practices.

*   **P3-m2:** §IIIE, Page 10
    *   **Problem:** The text states, "Practical consequence for downstream users: meta-analyses that require eROSITA anomaly scores on a reproducible axis... cannot be performed from the published SBigAE values, whose axis is irreproducible". This is a critical finding. The text points to an artifact `r24conf_erosita_axis_sweep.json`.
    *   **Required Fix:** For archival completeness, please add a brief summary of *why* the axis was irreproducible. Was it a non-deterministic step in the original processing, a software version mismatch, or something else? A single sentence of explanation would significantly improve the utility of this important caveat.

**NIT**

*   **P3-N1:** Abstract, Page 1
    *   **Problem:** The date is listed as "(Dated: June 2026)". This is presumably a placeholder and is post-dated.
    *   **Required Fix:** Change the date to the current submission month and year.

*   **P3-N2:** §IVA, Page 12
    *   **Problem:** The text refers to "eROSITA DR1 68% (203 SIMBAD-unmatched membership-list sources, LMC-concentrated)". The percentage is given, but the denominator is not immediately obvious from the text.
    *   **Required Fix:** For clarity, write as "eROSITA DR1 68% (203/298 SIMBAD-unmatched membership-list sources...)". This allows the reader to immediately verify the percentage.

---
## Summary recommendation

**MINOR REVISIONS**

The paper is a substantial and high-quality contribution. The analysis is careful, the results are significant, and the authors have been exceptionally transparent about the limitations and methodological lessons of their work. The required revisions are minor and focus on improving the archival quality of the manuscript by removing internal-review language and meta-commentary. Once these issues are addressed, the paper will be an excellent addition to the literature and is recommended for publication in Physical Review D.