# P4 R40 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p2_chirality/chirality_catalog_paper.pdf` md5=c47abc18 pages=23
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 213.0s

---

**Referee Report on "Survey-Scale Galaxy Chirality with Equivariant TTA..."**

**Manuscript ID:** [Assigned by editor]
**Author:** Houston Golden
**Journal:** Physical Review D

This paper presents a search for a cosmic dipole in the chirality of spiral galaxies using a new catalog of 3.2 million spirals derived from the DESI Legacy Surveys DR8. The primary result is a null detection, constrained at a level that is in tension with some previous claims in the literature. The main methodological contributions are the use of a flip-equivariant Vision Transformer pipeline to mitigate classifier bias and a thorough, multi-pronged analysis of potential systematic effects, including a novel demonstration of a "monopole-mask leakage" channel.

The analysis is exceptionally rigorous and the treatment of systematics is comprehensive and transparent. The authors are careful to distinguish between different estimators and null hypotheses, a crucial point for this type of analysis. The work represents a significant step forward in the search for cosmic parity violation through galaxy morphology. The paper is well-written and the conclusions are well-supported by the evidence presented.

However, the paper requires several revisions to meet the standards for publication in Physical Review D. The primary concerns relate to the paper's structure, which buries key results in appendices, and the readiness of the data availability and reproducibility information.

Below is a list of required and recommended changes.

---

### ESSENTIAL Revisions

*   **P4-E1: Data Availability and Reproducibility**
    *   **Section/Page:** Data Availability, pp. 21-22.
    *   **Problem:** The section contains information unsuitable for a final publication. Specifically, it includes a future date ("June 2026"), internal versioning information ("v1.0.185 lineage"), and internal-facing jargon ("The cited commit hash pins the version-stamp commit..."). For a paper to be published, all reproducibility artifacts must be static, permanent, and publicly citable.
    *   **Required Fix:** The entire section must be rewritten to point to a final, archived, and citable version of the data, code, and analysis artifacts. As the authors note is their plan, this should be a single DOI from a repository like Zenodo that permanently freezes the state of all relevant materials corresponding to the published version of the paper. All internal versioning language must be removed.

### MAJOR Revisions

*   **P4-M1: Paper Structure and Placement of Key Results**
    *   **Section/Page:** Main text and Appendices, particularly Appendix D (p. 19).
    *   **Problem:** The paper's structure relegates several of its most important results and supporting arguments to the appendices. For instance, the primary exclusion of a 1.7% dipole via a WLS template fit (z ≈ -18.1) is derived in Appendix D.g. Likewise, the crucial evidence disfavoring a cosmological origin for the harmonic-channel residual (the quality-quartile washout, the l=2 > l=1 power, the cross-spectrum analysis) is also in Appendix D. These are not minor technical details; they are the core of the systematic analysis that underpins the paper's main claim of a robust null result.
    *   **Required Fix:** The paper must be restructured to bring the most critical parts of the systematic analysis into the main body. I recommend creating a new subsection in the main "Results" section (e.g., "IV.D Systematic Analysis of the Harmonic-Channel Residual") that summarizes the key findings from the eight-anchor analysis. The WLS template fit, being a primary cosmological estimator, should have its derivation and result presented in the main body (e.g., in Section IV.C Dipole Analysis). The appendices can retain the more granular implementation details (e.g., NaMaster configuration, full tables of WLS coefficients).

*   **P4-M2: Inconsistent Significance Values for a Key Diagnostic**
    *   **Section/Page:** Abstract (p. 1), Table III (p. 11), Conclusions (p. 14).
    *   **Problem:** The paper presents two substantially different significance values for the post-MASTER canonical unapodized l=1 residual: +3.64σ (from a 500-MC run) and +7.93σ (from a 10⁴-permutation run). While the origins are explained, the choice to "retain" the +3.64σ value for "continuity" in the conclusion is confusing and could be misinterpreted as cherry-picking a lower significance. The factor of >2 difference in z-score between a low-statistics and high-statistics run on the same data requires a more direct physical explanation.
    *   **Required Fix:** The authors must clarify this point. If the 10⁴-permutation run is the more statistically robust result (as is expected), it should be the headline number for this diagnostic. The authors should justify why the lower-statistics run was used for the leakage analysis (e.g., computational cost) and explicitly state which value should be considered the definitive measurement of the residual. The narrative should be made consistent across the abstract, main text, and conclusion.

### MINOR Revisions

*   **P4-m1: Title Clarity**
    *   **Section/Page:** Title, p. 1.
    *   **Problem:** The title emphasizes the full 8.47 million galaxy catalog, while the core chirality analysis is performed on the 3.2 million spiral subset. This could be slightly misleading.
    *   **Required Fix:** Consider rephrasing for clarity. A suggestion: "Survey-Scale Galaxy Chirality... on 3.2 Million Spirals from the 8.47 Million Galaxy DESI Legacy Survey Catalog". The current title is acceptable if the author strongly prefers it, as the parenthetical clarification is present.

*   **P4-m2: Future Date in Byline**
    *   **Section/Page:** Byline, p. 1.
    *   **Problem:** The paper is dated "June 13, 2026".
    *   **Required Fix:** This should be updated to the date of submission or revision.

### NIT-PICKS / TYPOS

*   **P4-T1: Phrasing in Table III Caption**
    *   **Section/Page:** p. 11.
    *   **Problem:** The phrase "the two should not be numerically equated" is slightly awkward.
    *   **Required Fix:** Suggest changing to "the two are not numerically comparable" to align with similar phrasing used elsewhere in the manuscript.

*   **P4-T2: Typo in Appendix D.g**
    *   **Section/Page:** p. 19.
    *   **Problem:** The text reads "inflates (Adipole) from the naive WLS". The bootstrap procedure inflates the uncertainty on the parameter, not the best-fit value itself.
    *   **Required Fix:** This should be corrected to "inflates σ(Adipole)" or "inflates the uncertainty on Adipole".

---

## Summary recommendation

**MAJOR REVISIONS**

This is a high-quality, methodologically sophisticated paper that presents an important null result in cosmology. The level of rigor, particularly in the treatment of systematic errors, is commendable and sets a high standard for future work in this area. The primary conclusions are strongly supported by a comprehensive and transparent analysis.

However, the paper cannot be accepted in its current form. The structural decision to place the derivation of primary results and the core systematic-analysis arguments in the appendices significantly hinders the paper's readability and impact. The Data Availability section is not yet in a publishable state. Once these structural and reproducibility issues are addressed, the paper will be an excellent contribution to the literature. I recommend the paper for publication in Physical Review D after these major revisions are completed.