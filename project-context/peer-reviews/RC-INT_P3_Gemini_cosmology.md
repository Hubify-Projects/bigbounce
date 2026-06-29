# P3 RC-INT — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p3_anomaly_engine/paper3_draft.pdf` md5=8ed23638 pages=30
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 169.8s

---

Referee Report: P3

## Summary of the Paper
This paper presents a large-scale anomaly detection survey across seven astronomical archives (DESI, SDSS, LAMOST, eROSITA, Planck, Gaia, NEOWISE), processing 37.3 million sources and map patches using a unified autoencoder framework. The primary deliverables are a total catalog of 378,280 unique anomalies and a more robust, "recommended-tier" subset of 269,317. The authors perform extensive cross-validation, including native retraining for each survey, injection-recovery tests, and out-of-distribution checks. Key findings include the identification of training-bias artifacts (e.g., 98% of LAMOST cross-transfer anomalies are blue-excess), the quantification of cross-survey domain shift (a ~6500x rate change for SDSS after native retraining), and the measurement of a genuine novelty fraction of ~17.8% for the top DESI anomalies against 18 archival catalogs. The catalog is applied to two cosmological problems: forecasting constraints on primordial non-Gaussianity (fNL) and testing the consistency of the NANOGrav gravitational-wave background with matter-bounce cosmology. The paper is notable for its methodological transparency, including detailed documentation of residual caveats and explicit flagging of exploratory vs. validated catalog components.

## General Comments
The paper is exceptionally thorough and demonstrates a high level of scientific rigor. The scale of the analysis is impressive, and the authors' commitment to validation and transparent reporting of limitations is commendable. The careful distinction between process-scale statistics (e.g., the 141x catalog size increase) and like-for-like scientific comparisons (the 0.9x DESI science-target count) is a model for how such work should be presented. The cosmological applications are well-calibrated, with claims appropriately stated as forecasts or consistency checks rather than detections.

Despite the overall high quality, there are several issues that must be addressed before the paper can be considered for publication in Physical Review D. The most significant are two acknowledged, but not fully quantified, methodological flaws: (1) data leakage in the feature scaling process for tabular surveys, and (2) irreproducible preprocessing steps for the Gaia and eROSITA surveys due to lost provenance. While the authors are transparent about these issues and flag the affected catalog tiers as "exploratory," a more quantitative assessment of their potential impact is required to meet the journal's standards for rigor and reproducibility.

The paper is long (30 pages), but its length is justified by the complexity of the multi-archive analysis and the extensive, necessary documentation of the validation process.

## Findings

### ESSENTIAL
None.

### MAJOR

**P3-M1: Data Leakage in Feature Scaling**
*   **Location:** Section II.B, Page 3
*   **Problem:** The text states, "Because the scalers are fit on the full sample rather than the training split alone, a small amount of validation-set (including tail) information enters the normalization constants... We assume it does not materially reorder the within-survey anomaly ranking... but this is a stated assumption rather than a demonstrated result." This constitutes data leakage and is a methodological flaw. An assumption is not sufficient; the effect must be quantified.
*   **Fix:** The authors must perform a dedicated test to bound the effect of this leakage. For at least one of the affected tabular surveys (e.g., NEOWISE), they must re-run the analysis with a scaler fit *strictly* on the training data. They should then compute the top-1% anomaly list with this proper pipeline and report the Jaccard index and rank-correlation (Spearman's ρ) against the top-1% list from the production pipeline. This will replace the assumption with a quantitative measurement of the induced ranking instability.

**P3-M2: Quantifying the Impact of Lost Provenance (Gaia)**
*   **Location:** Section II.B, Page 3 and Section III.G, Page 13
*   **Problem:** The paper discloses that "the exact 20-feature production preprocessing script for this run was not recovered" and the specification is "lineage-inferred" from a successor script. This is a significant reproducibility failure. While flagging the Gaia tier as "exploratory" is appropriate, the potential systematic uncertainty should be bounded.
*   **Fix:** The authors should provide a quantitative estimate of the potential discrepancy. Using the 21-feature successor script (`gaia_expanded.py`), they should perform an ablation test. What is the 21st feature, and what is its relative importance? More importantly, they should run the 20-feature "lineage-inferred" version and the 21-feature successor version on the same set of sources and report the Jaccard overlap of the resulting top-1% anomaly lists. This would provide a data-driven estimate of the systematic uncertainty from the provenance failure.

**P3-M3: Quantifying the Impact of Lost Provenance (eROSITA)**
*   **Location:** Section III.E, Page 11
*   **Problem:** The paper reports an "undocumented post-hoc rescaling step" for eROSITA, making the production score axis "unrecoverable." The authors correctly fall back to using the membership list ranked by the reproducible raw reconstruction score. However, the text is slightly ambiguous about the final state of the released catalog.
*   **Fix:** Please explicitly clarify that the final, released 298-object eROSITA membership list is ordered according to the reproducible raw-score rank. Furthermore, the authors should state whether the irreproducible production scores showed a strong rank-correlation with the reproducible raw scores. If the rank ordering was substantially different, this is a more severe issue and should be noted as it would affect any analysis relying on the "top-N" objects being the most extreme.

### MINOR

**P3-N1: Unconventional Paper Structure**
*   **Location:** Section I, Page 2
*   **Problem:** The second paragraph of the paper, beginning "An empirical Landy-Szalay bias measurement...", functions as a secondary abstract focused on the cosmological results. It appears before the main introduction is complete and before the methods have been described, which is confusing for the reader.
*   **Fix:** Move this entire paragraph from the introduction to the beginning of Section V ("Cosmological Applications"). The introduction should motivate the work and provide a high-level overview, while the detailed quantitative results should be presented in the relevant results section.

**P3-N2: Figure Readability**
*   **Location:** Figure 3, Page 8
*   **Problem:** The caption correctly clarifies that the LAMOST curve is from a superseded cross-transfer run and is not a primary result. However, this crucial context can be easily missed by a reader skimming the figures.
*   **Fix:** To prevent misinterpretation, add a text annotation directly onto the plot area, for example, "(cross-transfer baseline, superseded)" next to the "LAMOST DR10" legend entry.

**P3-N3: Disambiguation of σ(fNL) Normalization**
*   **Location:** Section V, Page 17 and Appendix C / Figure 11, Page 26
*   **Problem:** The shot-noise analysis in Appendix C and Figure 11 uses a different absolute normalization for σ(fNL) than the main analysis in Section V. The caption in Figure 11 notes this, but the potential for confusion is high. A reader might incorrectly compare absolute values between the main text and the appendix.
*   **Fix:** In the main body text of Section V where the primary fNL forecast is discussed, add a sentence that explicitly directs the reader to the appendix for the shot-noise analysis and includes a clear warning that the σ(fNL) values therein use a different internal normalization, so only relative changes should be considered.

### NIT

**P3-T1: Future Date**
*   **Location:** Title Page, Page 1
*   **Problem:** The paper is dated "June 28, 2026," which is in the future.
*   **Fix:** Replace this with the current submission date or an appropriate placeholder (e.g., `\today`).

**P3-T2: Minor Wording**
*   **Location:** Section IV.A, Page 14
*   **Problem:** The sentence "The 4-vs-2.75 comparison is therefore reported as a methods-note heuristic only; no statistical significance is assigned to it absent a geometry-preserving null" is slightly passive.
*   **Fix:** Consider a more direct phrasing, such as: "The 4 observed matches are not statistically significant against the 2.75 expected from this heuristic control. A definitive test of significance would require a geometry-preserving null."

## Summary recommendation
**MAJOR REVISIONS**

This is a substantial and high-quality paper that is very close to the standard for publication in Physical Review D. The authors' commitment to rigor and transparency is exemplary. However, the identified MAJOR issues concerning data leakage and lost provenance, while honestly disclosed, must be addressed with more quantitative analysis to bound their potential impact on the results. Once these quantitative checks are incorporated and the minor structural and clarity issues are resolved, the paper will be an excellent contribution to the literature.