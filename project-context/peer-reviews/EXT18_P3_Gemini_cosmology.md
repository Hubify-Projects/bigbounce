# P3 EXT18 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p3_anomaly_engine/paper3_draft.pdf` md5=4a8c1172 pages=30
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 134.0s

---

**Referee Report on "Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies and a Native-Trained Novelty Fraction from 37.3 Million Sources and Map Patches"**

This paper presents a large-scale anomaly detection analysis across seven major astronomical surveys, resulting in a catalog of over 378,000 unique anomalous sources. The authors employ an autoencoder framework, develop a robust "Path-C" native-retraining and validation protocol to handle cross-survey domain shifts, and present two cosmological applications related to primordial non-Gaussianity (fNL) and the stochastic gravitational-wave background.

The scale of the analysis is impressive, and the work is conducted with a very high degree of rigor and transparency. The authors are commendably forthright about the limitations of their methods, the provenance of their data products, and the interpretation of their results. The methodological lessons learned, particularly regarding training-set bias (the LAMOST result) and the importance of cross-survey validation, are a significant contribution in their own right. The cosmological applications are presented carefully as forecasts and consistency checks, avoiding any overstatement of their current significance. The paper is exceptionally well-written, detailed, and substantiated. It represents a major contribution to the fields of astronomical data analysis and survey science.

The paper is in excellent shape for publication. I have identified a few points that require minor revision or clarification to further improve the manuscript.

---
### **MAJOR Revisions**

**ID: P3-M1**
*   **Section/Page:** Section I, page 2
*   **Problem:** The introduction states that the matter-bounce prediction for fNL is "testable at 2.6-5σ with SPHEREX". This is presented as a relatively firm statement. However, the detailed discussion in Section V (page 18) correctly qualifies this, stating the forecast is "contingent on successful survey execution and calibration of the anomaly-tracer bias". The introduction should reflect the same level of contingency to avoid misleading the reader about the certainty of this future test.
*   **Required Fix:** Rephrase the sentence in the introduction to include the conditional nature of the SPHEREX forecast. For example: "which is forecast to be testable at 2.6-5σ with SPHEREx... contingent on the successful calibration of the anomaly-tracer bias."

**ID: P3-M2**
*   **Section/Page:** Section III A, page 6
*   **Problem:** The paper reports the Spearman correlation between anomaly score and SNR for DESI (ρ = -0.03) based on a stratified subsample designed to be log-uniform in SNR. The authors correctly note this design is not representative of the full population and state that "a population-weighted re-compute on a true random subsample is queued for the data release." For a paper of this scope, a key validation check like this should be completed prior to publication. Leaving it as a "queued" task weakens the claim of no significant score-SNR correlation, even if the measured effect size is small.
*   **Required Fix:** Perform the population-weighted re-computation on a random subsample and report the result. This will provide a definitive statement on the score-SNR correlation for the full DESI sample and remove the need for a promissory note.

---
### **MINOR Revisions**

**ID: P3-N1**
*   **Section/Page:** Section II A, page 2 (and Section III F, page 12)
*   **Problem:** The architecture of the Planck CMB convolutional autoencoder is described as "three convolutional layers + a 128-dim fully connected bottleneck (1.1 × 10^6 parameters)". This description is too sparse to allow for replication. Key hyperparameters such as the number of filters, kernel sizes, and strides for the convolutional layers are missing.
*   **Required Fix:** Expand the description of the CNN architecture in the text or in a table/appendix to include the essential hyperparameters of the convolutional layers.

**ID: P3-N2**
*   **Section/Page:** Table I, page 9
*   **Problem:** The SIMBAD-unmatched fraction for LAMOST DR10 is listed as "~50%". The analysis in the paper (§III D, §VI A) demonstrates conclusively that this is driven by a 98% blue-excess training-bias artifact, not genuine novelty. The main summary table should explicitly flag this to prevent misinterpretation. The corresponding bar in Figure 6 has an asterisk and a note, which is good practice that should be mirrored here.
*   **Required Fix:** Add a footnote or an asterisk to the LAMOST entry in Table I, explicitly stating that its unmatched fraction is dominated by a training-bias artifact and directing the reader to the relevant discussion section.

**ID: P3-N3**
*   **Section/Page:** Section VI D (ii), page 20 (and Figure 10 caption, page 22)
*   **Problem:** The term "XV-stability" is used to report a diagnostic for the eROSITA and Gaia injection-recovery tests (e.g., "eROSITA 1.2% subspace/81.5% XV-stability"). This term is not defined in the text and its meaning, while inferable as "cross-validation stability," is not explicit.
*   **Required Fix:** Provide a brief definition of "XV-stability" at its first use, explaining what it measures and how it is calculated.

**ID: P3-N4**
*   **Section/Page:** Page 1 (Dated line) and Bibliography, page 29
*   **Problem:** The paper is dated "June 13, 2026". This appears to be a placeholder and should be updated to the actual submission date. Similarly, reference [12] (Nicolaou et al.) is cited with specific journal volume and issue numbers for the year 2026. This is highly unusual for a paper not yet published.
*   **Required Fix:** Change the date of the manuscript to the submission date. For reference [12], please verify the publication status. If it is not yet published with these exact details, it should be cited as "submitted to MNRAS," "in press," or with its arXiv identifier only.

---
### **NIT (Cosmetic)**

**ID: P3-NIT1**
*   **Section/Page:** Abstract, page 1
*   **Problem:** The sentence "ACT DR6 quarantined as a cross-transfer artifact its cross-transfer validation loss..." is grammatically dense.
*   **Required Fix:** Improve readability by adding punctuation, for example: "ACT DR6 quarantined as a cross-transfer artifact: its cross-transfer validation loss..."

**ID: P3-NIT2**
*   **Section/Page:** Throughout
*   **Problem:** The term "pod" is used to refer to the computing environment (e.g., "GPU pod," "pod-side"). This appears to be internal or provider-specific jargon.
*   **Required Fix:** For clarity to a general audience, consider replacing "pod" with a more standard term such as "GPU instance" or "computing environment."

---
## Summary recommendation

**ACCEPT WITH MINOR CORRECTIONS**

This is a landmark paper in the application of unsupervised machine learning to astronomical survey data. The authors have produced a valuable, large-scale catalog of unusual sources and have done so with exemplary methodological care, validation, and transparency. The paper is dense but clearly written, and its conclusions are well-supported by the extensive analysis. The identified issues are minor and primarily involve adding clarifications and completing one promised validation check. Once these points are addressed, the paper will be an outstanding contribution to the literature and should be published in Physical Review D.