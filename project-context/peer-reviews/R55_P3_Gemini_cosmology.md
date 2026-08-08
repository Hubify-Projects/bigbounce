# P3 R55 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/private/tmp/R55_P3/paper3_draft.pdf` md5=120624c4 pages=30
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 183.4s

---

**Referee Report on "Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies and a Native-Trained Novelty Fraction from 37.3 Million Sources and Map Patches"**

**To the Editor of Physical Review D,**

This manuscript presents a large-scale anomaly detection campaign across seven major astronomical surveys, resulting in a catalog of nearly 380,000 unique anomalous sources and sky regions. The authors apply a consistent autoencoder framework (BIGAE), develop a robust "Path-C" validation protocol involving native retraining for each survey, and perform cross-survey validation. The work includes applications to high-redshift quasar discovery, primordial non-Gaussianity (fNL) constraints, and consistency checks with gravitational wave background data from NANOGrav.

The scale of the analysis is impressive, and the authors are exceptionally transparent about the methodological challenges, limitations, and validation results, which is a significant strength of the work. The paper makes several valuable contributions, including the public catalog itself, important methodological lessons regarding transfer learning and training-set bias, and intriguing, albeit preliminary, cosmological applications.

However, the manuscript requires significant revisions to meet the standards of Physical Review D. The primary concerns relate to the clarity of presentation for the main results, methodological flaws in the analysis of some survey tiers, and reproducibility issues for others. The following detailed points must be addressed before the paper can be considered for publication.

---
## Detailed Findings

### ESSENTIAL

**P3-E1: §III, p. 5 & 7, Table I — Confusing presentation of primary results.**
*   **Problem:** Table I, the main summary table of the paper, is structured in a confusing manner that obscures the primary results. The main `N_anom` column presents a mix of final "Path-C" native-retrained counts (for DESI, eROSITA, Planck, Gaia, NEOWISE) and superseded "cross-transfer" counts (for SDSS and LAMOST). The primary, canonical results for SDSS and LAMOST are relegated to footnotes and the summary row. A reader looking at the table body would draw incorrect conclusions about the final catalog composition. The primary results of the paper must be presented clearly and centrally.
*   **Required Fix:** Revise Table I to be unambiguous. A recommended structure would be:
    1.  A main column `N_anom (Path-C)` that lists the final, canonical anomaly counts for *all* seven surveys, which sum to the 388,493 pre-deduplication total.
    2.  An optional, separate column `N_anom (cross-transfer baseline)` for the superseded verification numbers.
    This will make it clear how the final `Path-C unique` count of 378,280 is derived and what the contribution of each survey is to the final product. The current layout forces the reader to perform complex accounting based on extensive footnotes, which is unacceptable for a primary results table.

**P3-E2: Abstract, p. 1 — Incomplete disclosure of exploratory components.**
*   **Problem:** The abstract highlights the exploratory nature of the eROSITA tier ("membership list only; ... score axis non-reproducible") and the LAMOST tier ("exploratory tier"). However, it omits the significant reproducibility and validation issues associated with the Gaia DR3 component, which also failed its injection-recovery gate (5.2% recovery) and for which the preprocessing script was not recovered (§IID, §IIIG, §VID(ii)). For a catalog of this scale, it is essential that the abstract accurately reflects the validation status of all major components.
*   **Required Fix:** Add a brief statement to the abstract acknowledging the exploratory nature of the Gaia DR3 component, similar to the caveats provided for eROSITA and LAMOST. For example, mention that it fails the injection-recovery gate and has lineage-inferred preprocessing.

### MAJOR

**P3-M1: §IIIF, p. 12 — Data leak in Planck CMB analysis.**
*   **Problem:** The paper states that for the native Planck CMB analysis, "the native bank is scored in full - including the patches used for training". This constitutes training on the test set, a significant methodological flaw. While the authors perform a subsequent check and argue against memorization because anomalies are over-represented in the validation split, this argument is weak and does not excuse the procedural error. Standard, rigorous machine learning practice requires a strict separation between training and evaluation data.
*   **Required Fix:** The authors must either:
    a) Re-run the Planck analysis, scoring only on a held-out test set, and update the results. This is the strongly preferred option.
    b) If re-running is not feasible, this limitation must be more strongly emphasized. It should be explicitly labeled as a methodological flaw in the main text, listed as a primary limitation in the Discussion (§VIC), and mentioned as a caveat in the abstract.

**P3-M2: §IIIG, p. 12 & §IIIE, p. 11 — Significant reproducibility issues for Gaia and eROSITA tiers.**
*   **Problem:** The paper is transparent about two major reproducibility issues: (1) For Gaia, "the exact 20-feature production preprocessing script for this run was not recovered from pod backups" and the specification is "lineage-inferred". (2) For eROSITA, the production score axis is "unrecoverable as a matter of provenance". These issues mean that the Gaia and eROSITA anomaly lists, while potentially useful, are not fully reproducible from scratch and should be considered exploratory. This status is not sufficiently prominent.
*   **Required Fix:** In addition to the abstract fix (P3-E2), the main conclusion (§VII) should explicitly state that the Gaia and eROSITA components are labeled as "exploratory" in the final data product due to these validation and reproducibility failures. The current conclusion (point 8) does this, which is good, but the abstract and other summary sections should be consistent.

### MINOR

**P3-m1: §V, p. 18 — Insufficient detail on fNL systematics.**
*   **Problem:** The discussion of systematics in the fNL forecast is brief. It states that the fiber-assignment nuisance is bounded at `|Δσ/σ| < 0.01%` and GR projection corrections are bounded at `|Δσ/σ| < 0.02%`. The text claims these are "internal order-of-magnitude bound[s]". While plausible, these are load-bearing claims for the forecast's robustness.
*   **Required Fix:** Briefly elaborate on how these bounds were derived or provide a pointer to a calculation in an appendix. For example, for the GR projection effects, specify the relevant terms (e.g., lensing convergence, Doppler) and the justification for their sub-percent contribution at the relevant scales.

**P3-m2: §II, p. 3 — Data leak in tabular feature scaling.**
*   **Problem:** The paper notes that for the tabular surveys (eROSITA, NEOWISE, Gaia), feature-scaling statistics were fit on the full sample before the train/validation split. This is a minor data leak. The authors perform a commendable robustness check for the load-bearing eROSITA tier and find the impact is below the model-retrain reproducibility floor.
*   **Required Fix:** No fix is required beyond the existing text, as the authors have correctly identified, quantified, and contextualized the issue. However, they should ensure this practice is not repeated in future work, as they themselves recommend.

### NIT

**P3-N1: End of document, p. 30 — Reviewer metadata artifact.**
*   **Problem:** The text block `[REVIEWER METADATA ...]` appears at the very end of the document. This is clearly an artifact of the production/review process and not part of the paper content.
*   **Required Fix:** Remove this block from the final version of the manuscript.

**P3-N2: §IIID, p. 10, Figure 3 Caption — Potentially confusing figure content.**
*   **Problem:** The left panel of Figure 3 plots the anomaly score distribution for the *superseded* cross-transfer LAMOST scan. While the caption is clear, presenting superseded results in a main-body figure can be confusing.
*   **Required Fix:** Consider moving this panel, which serves as a diagnostic of a resolved issue, to an appendix to improve the flow and clarity of the main text.

---
## Summary recommendation

**MAJOR REVISIONS**

This is a substantial and valuable paper that reports on a massive anomaly detection effort. The scientific scope is broad, and the commitment to transparency regarding methodological limitations is exemplary. The work has the potential to be a landmark contribution to the field.

However, the issues identified above, particularly the confusing presentation of the main results in Table I (P3-E1), the data leak in the Planck analysis (P3-M1), and the need for clearer statements about the exploratory nature of several catalog components in the abstract (P3-E2), are significant and must be thoroughly addressed. Once these revisions are made, the paper should be suitable for publication in Physical Review D.