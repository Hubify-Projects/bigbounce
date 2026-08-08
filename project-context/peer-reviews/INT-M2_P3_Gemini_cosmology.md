# P3 INT-M2 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p3_anomaly_engine/paper3_draft.pdf` md5=f6b8d9a5 pages=30
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 169.8s

---

## Referee Report: P3-INT-M2

This paper presents a large-scale, multi-survey search for spectrally unusual sources using an autoencoder framework. The authors process data from seven astronomical archives (DESI, SDSS, LAMOST, eROSITA, Planck, Gaia, NEOWISE), resulting in a catalog of 378,280 unique anomalous sources and sky patches. The work includes a detailed validation protocol, including native retraining for each survey, injection-recovery tests, and cross-validation. The catalog is used to derive a genuine novelty fraction and for two cosmological applications: constraining primordial non-Gaussianity (fNL) and testing the consistency of the NANOGrav gravitational-wave background with a matter-bounce scenario.

The paper is exceptionally thorough and transparent. The methodology is detailed, and the authors are commendably forthright about the limitations of their analysis, the validation failures of certain catalog components, and the subtleties of interpreting their results. The careful distinction between full-stream and science-target anomaly rates, and between database coverage and genuine novelty, is a major strength. The cosmological applications are presented with appropriate scientific conservatism. The commitment to reproducibility, with pointers to code and data artifacts, is exemplary.

Despite the high quality of the work, several revisions are required before the paper can be considered for publication in Physical Review D. The most critical issue relates to the presentation of the main results in Table I.

---
### ESSENTIAL Findings

None.

---
### MAJOR Findings

**P3-M1: (Section III, Page 9, Table I) Misleading presentation of primary results in the main summary table.**

*   **Problem:** Table I, the central summary of the multi-survey anomaly sweep, presents superseded "cross-transfer" anomaly counts in the main `N_anom` column for two of the largest surveys, SDSS DR18 and LAMOST DR10. The paper's primary, canonical results are the "Path-C native-retrained" counts, which are the product of the core methodological improvement (the "Path-C rebuild") designed to overcome the documented failures of the cross-transfer approach. These canonical counts are relegated to footnotes (`‡`) and the summary row (`||`). A reader looking at the table body would get the wrong numbers for the final catalog components and would be looking at results from a methodology the paper itself proves is flawed.
*   **Required Fix:** Revise Table I to show the final, canonical, Path-C native-retrained anomaly counts for all surveys in the main table rows. The superseded cross-transfer baseline counts should be moved to a footnote or a separate verification table (e.g., in an appendix) where they can be presented with the proper context as a methodological baseline that motivated the final "Path-C" analysis. This change is crucial for the table to serve as an accurate summary of the paper's primary deliverable.

---
### MINOR Findings

**P3-m1: (Section I, Page 1, Title) Title is overly long and dense.**

*   **Problem:** The title, "Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 269,317 Recommended-Tier (378,280 Total) Path-C Unique Anomalies and a Native-Trained Novelty Fraction from 37.3 Million Sources and Map Patches," is extremely long and packed with technical jargon. While accurate, its length and complexity may reduce its impact and accessibility.
*   **Required Fix:** The authors should consider shortening and simplifying the title. A suggestion: "A Multi-Survey Catalog of 378,280 Spectrally Unusual Sources and a Measurement of the Genuine Novelty Fraction." The details about the "Recommended-Tier" and "Path-C" can be effectively communicated in the abstract.

**P3-m2: (Section V, Page 18) Potentially confusing reference in Table V.**

*   **Problem:** In Table V on page 22, row (j) summarizes the Gold+Silver (GS) corrected fNL forecast. The "Resolution" column points to "caveat (i)". Caveat (i) in the same table is about the Fisher positivity check for the main sample, not the GS sample. The derivation for the GS sample is in the main body of Section V (page 18).
*   **Required Fix:** Correct the reference in Table V, row (j) to point to the appropriate part of Section V where the Gold+Silver sample analysis is described.

**P3-m3: (Page 23, paragraph after Fig. 10) Incorrect cross-reference for lower-bound logic.**

*   **Problem:** The paragraph states: "...a conservative lower bound, see §IID)". The abstract (page 1) refers to §IIIE for the same point. Neither seems correct. The logic for why the count is a lower bound is explained most clearly in the abstract itself. There is no Section IIIE in the paper.
*   **Required Fix:** Correct this cross-reference. The authors should point to the specific sentence in the abstract or reproduce the logic briefly in the main text. The typo "§IIIE" in the abstract should also be corrected (e.g., to §III E if that is the intended section).

---
### NITs (Nitpicks)

**P3-N1: (Page 1, Abstract) Future date.**

*   **Problem:** The date of the paper is listed as "(Dated: June 28, 2026)".
*   **Required Fix:** Change this to the date of submission.

**P3-N2: (Page 2, Section I) Typo in text.**

*   **Problem:** The text reads "...Heinrich et al. [33] ((fnL) ≈ 0.7 bispectrum-only forecast)". There is a double parenthesis.
*   **Required Fix:** Remove one of the opening parentheses.

**P3-N3: (Page 9, Table I Caption) Typo in formatting.**

*   **Problem:** The text reads "...cross-transfer val_loss ≈ 2.2×104 failing...". The "4" should be a superscript.
*   **Required Fix:** Format "104" as 10⁴.

**P3-N4: (Page 1, Abstract) Convoluted sentence.**

*   **Problem:** The sentence "We lead with this validated subset, rather than the larger total counts reported below, to avoid overstating the science-ready yield (the > is a conservative lower bound, because the exact validated-only 5" re-dedup of the 798 exploratory detections is not recomputable from the committed aggregate artifacts and removing them by subtraction can only undercount the validated tier; see §IIIE)." is long and difficult to parse.
*   **Required Fix:** Consider breaking this sentence into two for clarity.

---
## Summary recommendation

**MAJOR REVISIONS**

The paper represents a significant and high-quality contribution to the field of anomaly detection in astronomy. The scientific rigor, transparency about limitations, and commitment to reproducibility are commendable and meet the high standards of Physical Review D. However, the confusing presentation of the main results in Table I, which currently highlights superseded baseline numbers instead of the paper's final, canonical results, is a major flaw that must be corrected. Once this and the other minor issues are addressed, the paper will be an excellent candidate for publication.