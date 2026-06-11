# P4 R29 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/chirality_catalog_paper_v172.pdf` md5=f6c1f145 pages=22
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 235.3s

---

**Referee Report on "Survey-Scale Galaxy Chirality with Equivariant TTA..."**

This paper presents a comprehensive analysis of galaxy chirality using a large catalog of 8.47 million galaxies from the DESI Legacy Surveys. The authors develop a Vision Transformer pipeline with test-time equivariant averaging to classify galaxies and search for a cosmic dipole in their handedness. The primary result is a null detection of a real-space chirality dipole, consistent with statistical isotropy. The paper includes an extensive and rigorous suite of systematic checks, quantifies a "monopole-mask leakage" channel as a primary systematic, and sets a well-defined falsification criterion for future studies.

The work is of high quality, demonstrating exceptional rigor in its systematic analysis and transparency in its methodology. The use of equivariant averaging to suppress classifier bias is a key methodological contribution, and its effectiveness is convincingly demonstrated. The detailed breakdown of systematic effects, particularly the monopole-mask leakage and the multi-pronged analysis in Appendix D, is a model for this type of analysis.

However, the paper requires significant revisions to meet the publication standards of Physical Review D. The main issues relate to clarity of presentation, the inclusion of internal versioning artifacts and file paths, and the justification for a few quantitative claims. The recommendations below are intended to improve the paper's readability and ensure its claims are fully supported and reproducible.

---
### ESSENTIAL Revisions

These issues must be addressed before the paper can be considered for publication.

**P4-E1: Removal of Internal File Paths and Artifact Tags**
*   **Location:** Throughout the paper (e.g., pages 2, 3, 5, 6, 7, 8, 10, 12, 13, 15, 16, 17, 19, 20).
*   **Problem:** The manuscript is littered with internal file paths (e.g., `pipelines/p2_chirality/outputs/...`) and artifact tags (e.g., `artifact c9c`, `artifact c9b`). This is not appropriate for a published paper and hinders readability. While the commitment to reproducibility is commendable, these should be replaced with references to specific tables, figures, or named data products in the public repository.
*   **Fix:** Remove all such paths and tags from the main text, captions, and footnotes. Replace them with human-readable references. For example, instead of "`(artifact pipelines/p2_.../c11_meta_m4_slab_stats.json)`", write "`(see slab-uniformity analysis in the data release)`" or refer to a table that summarizes the result. The full mapping of analysis scripts to results can be provided in the repository's documentation.

**P4-E2: Placeholder Information in Data Availability Section**
*   **Location:** Page 20, Data Availability.
*   **Problem:** The section contains placeholder dates and version tags that are in the future (e.g., "June 2026", "v2026.04"). It also states that a persistent DOI has not yet been minted.
*   **Fix:** For publication, these must be replaced with the final, correct commit hash, version tag, and a minted Zenodo (or equivalent) DOI for the specific version of the catalog and code used to generate the final results.

---
### MAJOR Revisions

These revisions address significant issues with clarity and justification.

**P4-M1: Clarification of "Superseded" Results**
*   **Location:** Page 11, Table III caption and main text.
*   **Problem:** The caption for Table III states that the `+3.64σ` canonical-mask result (from a 500-MC run) is "superseded as a table entry by the canonical rows above" (from a 10k-permutation run, giving `+7.93σ`) but is "retained in the text for continuity". However, this `+3.64σ` value is presented as a key diagnostic result in the abstract, the Methods hierarchy (Sec. III B), and the Conclusions (Sec. VII). This is confusing. A reader should not have to parse the paper's version history to understand which number is the final, definitive result for a given estimator.
*   **Fix:** Decide on a single, final value for the canonical-mask diagnostic for the main text and abstract. The other values from different run configurations should be clearly labeled as consistency checks or historical context and preferably confined to the appendices. The main narrative should be streamlined to present only the final, authoritative results.

**P4-M2: Justification of Discrepancy Factor with Previous Work**
*   **Location:** Page 2 (Introduction) and Page 13 (Sec. VI B).
*   **Problem:** The paper claims its null result is inconsistent with Shamir's claimed ~3% signal "by a factor of ~6-12". This factor is not explicitly derived. A simple comparison of the 3% amplitude to the paper's falsification floor (`A50 ≈ 0.75%`, `A95 ∈ [1.0, 1.5%]`) yields a discrepancy factor of ~2-4. A comparison to the measured dipole amplitude (`0.44%`) yields a factor of ~7. The origin of the upper bound of "12" is unclear. This is an uncomputed quantitative claim (violates Rule 17).
*   **Fix:** Provide a clear, step-by-step derivation of the claimed factor of 6-12 in the text. If the range comes from comparing different aspects of the results (e.g., amplitude vs. significance under different assumptions), this must be explained. Otherwise, revise the factor to match what can be directly calculated from the numbers presented in the paper.

---
### MINOR Revisions

These revisions will improve the paper's structure and readability.

**P4-M3: Consolidate Manuscript History Notes**
*   **Location:** Throughout the paper (e.g., p7 Correction note, p8/p9 figure captions, p9 footnote 1).
*   **Problem:** The text contains several notes about corrections from earlier versions, changes to figures, and withdrawn results from a synthetic catalog (the long note in Appendix A). While transparent, these interrupt the scientific narrative.
*   **Fix:** Consolidate all such notes on the manuscript's evolution into a dedicated section in an appendix. This will significantly improve the flow of the main Results and Appendices. The main text should present the final, corrected results without detailing the history of how they were obtained.

**P4-M4: Inconsistent Significance Value for Apodized MASTER Result**
*   **Location:** Abstract (p1), Methods (p4), and Table III (p11).
*   **Problem:** The significance for the apodized-footprint MASTER `l=1` channel is quoted as `+7.28σ` in the abstract and main text, but as `+7.31σ` in Table III.
*   **Fix:** Reconcile these values. Use the single, correct value consistently throughout the manuscript.

**P4-M5: Physics of Parity-Even vs. Parity-Odd Observables**
*   **Location:** Page 13, Section VI B.
*   **Problem:** The text correctly states that the `l=1` dipole is parity-even and the parity-odd signal lives in the `l=0` monopole and even-`l` multipoles. This is a crucial point.
*   **Fix:** This point is important enough that it should be stated earlier and more prominently, perhaps in the Introduction. This would help frame the entire analysis for the reader from the outset, clarifying that the primary search is for a violation of statistical isotropy, not directly for parity violation.

---
## Summary recommendation

**MAJOR REVISIONS**

This is a methodologically strong and impressively thorough paper that presents an important null result in the search for cosmic anisotropy. The systematic controls are exemplary. However, the paper in its current form is not ready for publication. The frequent use of internal file paths and placeholder versioning information is a critical flaw that must be rectified. Furthermore, issues of clarity, particularly regarding which numerical results are definitive versus historical, and the justification for a key quantitative comparison to previous work, need to be addressed. Once these revisions are made, the paper will represent a significant and valuable contribution to the field.