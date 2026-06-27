# P3 R52 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/site/public/papers/paper3_anomaly_catalog_v3.1.112.pdf` md5=62d7b294 pages=30
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 205.3s

---

**Referee Report on "Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies and a Native-Trained Novelty Fraction from 37.3 Million Sources and Map Patches"**

This paper presents a large-scale anomaly detection analysis across seven major astronomical surveys, resulting in a catalog of over 378,000 unique anomalous sources. The work is methodologically sophisticated, employing a native-retraining protocol to overcome cross-survey domain shift issues, and includes extensive validation through cross-validation, injection-recovery tests, and multi-wavelength cross-matching. The authors also present two cosmological applications of the resulting tracer catalog: a forecast for primordial non-Gaussianity (fNL) constraints and a consistency test of a matter-bounce scenario with NANOGrav pulsar timing data.

The paper is exceptionally well-written, detailed, and transparent. The authors demonstrate a high level of scientific rigor by consistently qualifying their claims, performing extensive robustness checks, and openly discussing the limitations of their analysis and the resulting data products. The methodological lessons, particularly regarding training-set bias (the LAMOST result) and cross-transfer domain shift (the SDSS result), are valuable contributions to the field of astronomical data analysis. The cosmological applications are handled with appropriate care, correctly interpreting null results and statistical tensions without overstatement.

While the paper is of very high quality, I have identified a few minor points that should be addressed to further improve its clarity and completeness before publication.

---

### Detailed Findings

#### MINOR REVISIONS

**ID: P3-m1**
*   **Section/Page**: VII (Conclusions) / p. 21-22
*   **Problem**: The main conclusions section (VII) provides an excellent summary of the key results. However, while it highlights the methodological lesson from the LAMOST training-bias artifact (point 7) and the failure of the ACT cross-transfer (mentioned in the preamble), it does not explicitly mention the significant reproducibility caveats associated with the Gaia and eROSITA data products. Specifically, the Gaia preprocessing script was not recovered from backups, and the eROSITA score axis was found to be irreproducible. The abstract and main body (§IIIE, §IIG) are commendably transparent about these issues, but a reader who primarily consults the abstract and conclusions might miss the full context of these limitations.
*   **Required Fix**: Add a sentence to the conclusions section (e.g., within point 1 on "Scale" or as a separate point) to briefly reiterate that the Gaia and eROSITA tiers of the catalog carry specific reproducibility caveats and should be treated as exploratory or membership-list-only, as detailed in the main text. This ensures the final summary is fully self-contained regarding the status of all catalog components.

**ID: P3-m2**
*   **Section/Page**: Table I / p. 9
*   **Problem**: The footnotes in Table I are dense and slightly confusing. The footnote marker `||` appears next to the "58.8%" SIMBAD-unmatched value for the "Total (cross-transfer, ACT-incl.)" row, but there is no corresponding footnote text. The text for footnote `§`, which is attached to the eROSITA row, begins with "Isolation Forest cross-validation-stability footnote...", which seems to be a mix of a label and the note itself. This may be an artifact of typesetting or an OCR error, but it impedes readability.
*   **Required Fix**: Please review and clarify the footnotes for Table I. Ensure that each symbol in the table has a corresponding, correct, and clearly written footnote. Specifically, provide the intended note for the `||` marker and ensure the `§` footnote is formatted correctly and applies only to the eROSITA entry.

**ID: P3-m3**
*   **Section/Page**: III F (Planck CMB) / p. 12
*   **Problem**: The paper states that for the Planck analysis, "the released top-200 is not a held-out selection (standard practice for autoencoder anomaly scoring, but stated here explicitly)." While the authors' subsequent validation showing an over-representation of anomalies in the held-out set is an excellent check that mitigates concerns about training-set memorization, labeling the practice of scoring on the training set as "standard practice" is debatable. In many machine learning contexts, it is explicitly avoided.
*   **Required Fix**: Rephrase "standard practice for autoencoder anomaly scoring" to a more neutral description, such as "a common practice in some applications" or simply state the procedure that was followed without characterizing it as standard. The strength of the result comes from the explicit validation provided, not from the practice itself being standard.

#### NIT-PICKS (Cosmetic)

**ID: P3-N1**
*   **Section/Page**: I (Introduction) / p. 2
*   **Problem**: The sentence "catalog counts appear as 378,080 + 200 = 378,280 throughout to distinguish point-source detections from CMB map-patch sky-regions" is slightly awkward.
*   **Required Fix**: Consider rephrasing for clarity. For example: "The total anomaly count of 378,280 is composed of 378,080 point-source detections and 200 CMB map-patch sky regions; we often present these components separately throughout the paper."

---

## Summary recommendation

**ACCEPT WITH MINOR CORRECTIONS**

This is a landmark paper in the application of unsupervised machine learning to large astronomical datasets. The scale of the analysis is impressive, and the methodological rigor and transparency are exemplary. The authors have not only produced a valuable and well-documented data product but have also provided critical insights into the challenges of anomaly detection across multiple surveys. The few required revisions are minor and are intended only to further enhance the clarity and completeness of an already outstanding manuscript. The paper is a significant contribution and is well-suited for publication in Physical Review D.