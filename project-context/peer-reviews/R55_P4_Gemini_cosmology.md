# P4 R55 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/private/tmp/R55_P4/chirality_catalog_paper.pdf` md5=fbed4276 pages=23
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 190.0s

---

Referee Report for Manuscript P4

## Summary of the Paper
This manuscript presents a search for a large-scale dipole in the chirality of spiral galaxies using a new catalog of 8.47 million galaxies (3.2 million spirals) from the DESI Legacy Surveys DR8. The authors use a Vision Transformer with a Test-Time Averaging (TTA) scheme to enforce flip-equivariance, a key methodological innovation to mitigate classifier bias. The primary result is a null detection of a real-space chirality dipole, consistent with the null hypothesis at the +0.41σ level for a high-confidence subsample. The authors establish a 95% falsification boundary for a future detection at a dipole amplitude of 1.0%-1.5%. The paper also provides a detailed analysis of systematics, identifying and quantifying a "monopole-mask leakage" channel that can produce spurious dipole signals in less rigorous analyses. A residual, systematics-attributed signal is found in the spherical harmonic domain (+7.28σ on the apodized footprint), but the authors convincingly argue, through an eight-point systematic analysis, that this is not of cosmological origin and does not affect the primary real-space null result.

## General Comments
The paper is exceptionally rigorous and methodologically sophisticated. The attention to systematics, the clear hierarchy of estimators, the careful distinction between different null procedures, and the transparent reporting of results are all commendable and set a high standard for this type of analysis. The identification and quantification of the monopole-mask leakage channel is a particularly important contribution that will be of great value to the field. The core scientific conclusion—a null result that places strong constraints on a potential cosmic dipole—is well-supported by the evidence presented. The paper is well-written and the appendices provide a wealth of detail necessary for reproducibility.

Despite the high quality of the work, there are several issues that must be addressed before publication. These range from an essential flaw in the data availability section to major points of clarity and structure that will improve the manuscript's impact and prevent misinterpretation.

## Detailed Findings

### ESSENTIAL

**P4-E1: Data Availability and Reproducibility Placeholders**
*   **Section:** Data Availability, Page 22
*   **Problem:** The manuscript's reproducibility is compromised by the use of future-dated, placeholder identifiers for the data and code repositories. The text cites `commit 53b41d12 (June 2026)` and `Release tag: v2026.04`. A publication in a peer-reviewed journal must be tied to a fixed, public, and immutable version of all data products and software that existed at the time of submission and review.
*   **Required Fix:** The authors must update all repository links, commit hashes, and release tags to point to the specific, static versions used to generate the results in this manuscript. An archival snapshot (e.g., on Zenodo, as the authors plan) should be created and its DOI provided in the final version of the paper. This is non-negotiable for publication.

**P4-E2: Prominence of Parity-Even Observable Distinction**
*   **Section:** Abstract (p. 1), Section VIB (p. 14)
*   **Problem:** The authors correctly and critically state that the `l=1` dipole is a parity-even observable (an axial vector) and therefore a test of statistical isotropy, not a direct test of parity violation. This physical distinction is fundamental and is often overlooked or misstated in the literature.
*   **Required Fix:** This is a positive finding. The authors must ensure this clarification remains highly prominent in the abstract and introduction of any revised manuscript. The clear explanation on page 14 is excellent and is a key strength of the paper.

### MAJOR

**P4-M1: Paper Length and Structure**
*   **Section:** Entire paper
*   **Problem:** At 23 pages, the paper is overly long for its primary message. While the detail is appreciated and necessary, the narrative flow of the main text is sometimes lost in the extensive discussion of secondary diagnostics. The distinction between the main paper and the appendices could be sharpened.
*   **Required Fix:** The authors should streamline the main text (pages 1-15) by moving some of the more detailed discussions of systematic checks (e.g., the fine points of the confidence-cut sweep in Sec. IV.C, the weight-map sweep in Sec. IV.C.b) to the appropriate appendices. This will focus the main text on the primary analysis path and its conclusion. The authors should also consider whether any of the eight appendices could be consolidated or moved to a Supplemental Material document to reduce the total page count of the main article to a more standard length for the journal (e.g., ~18 pages).

**P4-M2: Ambiguous "z" Notation for Significance**
*   **Section:** Throughout (e.g., Abstract p. 1, Sec IIIA p. 3, Table X p. 20)
*   **Problem:** The symbol `z` is used ubiquitously to denote statistical significance, defined as a moment-ratio `(x - <x>_null) / σ_null`. In a cosmology paper, `z` is the standard symbol for redshift. This creates unnecessary ambiguity and potential for confusion, for instance when the abstract discusses a significance of `z ≈ -18` and later refers to previous work at redshift `z < 0.3`.
*   **Required Fix:** Replace the `z` notation for statistical significance throughout the entire manuscript (text, tables, figures). Standard alternatives include `S/N`, `S`, or simply `σ` (e.g., "a 5σ detection"). This change is necessary for clarity.

**P4-M3: Misattribution of Robustness Check in Abstract**
*   **Section:** Abstract, Page 1
*   **Problem:** The abstract states: "...robust under a per-galaxy label-shuffle null, z = 0.70, and the unthresholded-sample sensitivity is attributed to a low-confidence-tail systematic...". The `z = 0.70` value is a robustness check on the *simple dipole fit*, as detailed on page 7. However, its placement in the abstract makes it appear to be a check on the *WLS template fit*, which is the subject of the following clause. This conflates two different estimators and their respective validation tests.
*   **Required Fix:** Rephrase the abstract to clearly associate each robustness check with the correct estimator. For example: "The primary scientific result is a real-space chirality dipole consistent with null: the equivariant-catalog high-confidence dipole fit... gives +0.41σ...; this null result is robust under a per-galaxy label-shuffle null (z = 0.70). A separate block-bootstrap WLS template fit disfavors a clean cosmological dipole..."

### MINOR

**P4-m1: Redundant Caveats in Abstract**
*   **Section:** Abstract, Page 1
*   **Problem:** The abstract contains several "Note:" clauses and parenthetical statements warning the reader that σ values from different nulls are not comparable. While this warning is essential, its repetition makes the abstract dense and slightly convoluted.
*   **Required Fix:** Consolidate the multiple warnings into a single, clear, and concise statement. For example: "Note: σ values quoted in this paragraph arise from distinct null procedures and are diagnostic indicators, not directly comparable as detection significances."

**P4-m2: Undefined "Canonical-N" Shorthand**
*   **Section:** Sec IIIB (p. 4), Appendix A (p. 16)
*   **Problem:** The paper uses the term "canonical-N" (e.g., "canonical-N direct-MC NaMaster") without explicitly defining what "N" stands for. From context, it appears to be shorthand for NaMaster, but this should not be left for the reader to infer.
*   **Required Fix:** Upon first use, either define the shorthand explicitly (e.g., "canonical-N, where N denotes NaMaster") or, preferably, avoid the abbreviation and write "canonical NaMaster" for clarity.

### NIT

**P4-N1: Placeholder Date in Header**
*   **Section:** Header, Page 1
*   **Problem:** The dateline reads `(Dated: June 13, 2026)`.
*   **Required Fix:** Replace this placeholder with the actual submission date.

## Summary recommendation
**MAJOR REVISIONS**

This is a high-quality, rigorous, and important paper that provides the strongest constraints to date on a cosmic chirality dipole. The methodology is sound, and the analysis of systematics is exemplary. The paper is well-suited for publication in Physical Review D. However, the essential issue with data availability placeholders must be fixed, and the major revisions concerning clarity (z-notation, abstract structure) and paper length are necessary to bring the manuscript up to the highest publication standards. I recommend the paper for publication after these revisions have been satisfactorily addressed.