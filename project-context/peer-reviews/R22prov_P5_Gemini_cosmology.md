# P5 R22prov — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 137.1s

---

## Referee Report: Environmental Dependence of Spiral Chirality (Golden)

This paper presents a detailed investigation into the potential dependence of spiral galaxy chirality on the large-scale structure environment, using data from the DESI Data Release 1 and a large, pre-existing galaxy chirality catalog. The primary conclusion is a null result: no statistically significant environmental dependence is found beyond a previously identified catalog-wide monopole offset. The analysis is extensive, employing multiple cosmic-web classifiers (V-Web, DESIVAST, Tempel+2014 FoF, ASTRA), and includes a wide array of robustness checks, such as sensitivity sweeps of analysis parameters, stratification by various galaxy properties, and corrections for selection-function effects.

While the underlying analysis contains several powerful and well-executed components, the manuscript in its current form has fundamental structural and methodological issues that preclude its publication in Physical Review D without substantial revision.

---
### ESSENTIAL Revisions

**P5-E1: Foundational Dependence on Unpublished, Non-Peer-Reviewed Work**
*   **Location:** Abstract (p. 1), Introduction (p. 2), Section II (p. 2), and throughout.
*   **Problem:** The entire analysis is predicated on the galaxy chirality catalog and the catalog-wide monopole offset (`Δf_cw = -0.0026`) from "Paper IV [3]". The manuscript repeatedly states that Paper IV is a "companion work, not yet peer-reviewed" and "currently in preparation". A manuscript submitted to PRD cannot be fundamentally based on inputs, calibrations, and interpretations from a work that has not undergone peer review. The validity of this paper's core interpretation—that all observed signals are projections of the Paper IV monopole—is entirely contingent on the unpublished findings of Paper IV. If the results or interpretation of Paper IV were to change, the conclusions of this paper would be invalidated.
*   **Required Fix:** The authors must either (1) incorporate the essential methodological details, validation, and monopole characterization from Paper IV into this manuscript, making it a self-contained work, or (2) wait to submit this manuscript until Paper IV has been accepted for publication in a peer-reviewed journal. The current approach is unacceptable.

**P5-E2: Post-Hoc Selection of the Primary Analysis Path**
*   **Location:** Section V B, "Primary vs. secondary analysis paths" (p. 5).
*   **Problem:** The paper explicitly states: "a single a priori preregistered analysis plan was not filed; the choice of which classifier to report as 'primary' is therefore made post-hoc". This is a frank admission of engaging in the "garden of forking paths," which undermines the statistical validity of the final claims. While the authors' justification (the DESIVAST sample is the "largest controlled sample") is noted, selecting the primary analysis *after* exploring multiple analysis pathways introduces bias and makes the reported significance levels difficult to interpret. This practice is not consistent with the standards of rigor expected by PRD.
*   **Required Fix:** The authors must reframe the paper to avoid the post-hoc "primary" designation. All analyses should be presented as a suite of complementary tests, with a discussion of their relative strengths and weaknesses. The conclusion must be a synthesis of all results, including any tensions between them (see P5-M1), rather than a conclusion based on a single, preferentially selected analysis path. The abstract and introduction must be rewritten to reflect this methodological reality.

---
### MAJOR Revisions

**P5-M1: Unresolved Tension from the Bright-vs-Dark Tracer Analysis**
*   **Location:** Section VI A (p. 2, abstract), Section VIII D (p. 8).
*   **Problem:** The analysis of tracer programs reveals a `|z| ≈ 3.4σ` sign-flip in the filament class between bright (BGS-dominated) and dark (LRG/ELG/QSO) samples. The paper correctly notes that the V-Web class and target program are not independent and concludes this is a "real residual structure that the current data do not allow us to cleanly partition". However, the abstract and main conclusion heavily downplay this finding, focusing almost exclusively on the overall null result. A `3.4σ` effect, described as a "real residual," is a significant finding that contradicts a simple "no environmental dependence" headline.
*   **Required Fix:** The abstract, discussion, and conclusion must give appropriate weight to this unresolved tension. The headline claim of environmental independence must be qualified by this finding. The paper should clearly state that while most tests are null, a significant residual signal correlated with galaxy type exists within the filament environment, which requires further investigation.

**P5-M2: Manuscript Structure and Length**
*   **Location:** Entire manuscript.
*   **Problem:** The paper is excessively long (21 pages) for a null result, and its narrative structure is convoluted. The reader must wade through many pages of the V-Web analysis, including its limitations and systematics (like the low-z void impurity), before reaching the much cleaner and more robust DESIVAST-anchored analysis in Section VIII, which the authors themselves designate as "primary". This "burying the lede" makes the paper difficult to follow and weakens the overall impact. Many of the secondary cross-checks, while valuable, interrupt the main logical flow.
*   **Required Fix:** The paper requires significant restructuring.
    1.  The DESIVAST-anchored analysis (Section VIII) should be presented immediately after the data and methods sections as the main result, given its superior robustness and control of systematics.
    2.  The V-Web analysis should be presented subsequently as a cross-check that is consistent once systematics (monopole, selection function, RSDs) are accounted for.
    3.  Many of the tertiary analyses (e.g., detailed within-class stratifications, ASTRA/Tempel cross-checks) should be streamlined or moved to an appendix to improve readability. The recommended maximum length for the main body is ~12-15 pages.

**P5-M3: Citation of "Future" Preprints**
*   **Location:** Abstract (p. 1), Section IX C (p. 16), Section XIII (p. 19), Bibliography (p. 21).
*   **Problem:** The manuscript cites several papers with futuristic dates and preprint numbers (e.g., Rincón et al. 2025 [13], Ullah et al. 2026 [11], Zapata-Zuluaga et al. 2026 [12]). The manuscript itself is dated "June 2026". This is unprofessional and not compliant with standard citation practices.
*   **Required Fix:** All dates and citation statuses must be corrected to reflect the reality at the time of submission. If a paper is a preprint, cite it with its actual arXiv ID and submission date. If it is in preparation, state "in preparation" or "private communication". The date of the manuscript itself should be the submission date.

---
### MINOR Revisions

**P5-m1: Quantitative Comparison of Monopole Prediction vs. Observation**
*   **Location:** Section VI C (p. 6).
*   **Problem:** The text states that for the filament class, the predicted sigma from the monopole is `≈ -3.16` while the observed is `-2.61`, and for the cluster class, the predicted is `≈ -3.28` while the observed is `-4.66`. The text describes this as the signal "tracking" the monopole. My calculation yields a prediction of `-3.32` for filament, a discrepancy of `0.71σ` from observation. For cluster, the discrepancy is `1.38σ`. While not highly significant, simply stating they "track" the monopole is too qualitative.
*   **Required Fix:** The authors should explicitly state the residual sigma (`σ_obs - σ_pred`) for these classes and comment on its magnitude. This provides a more precise and transparent assessment of how well the monopole-only hypothesis fits the data.

**P5-m2: Speculative Nature of Appendix A**
*   **Location:** Appendix A (p. 20).
*   **Problem:** The "Toy EFT mapping" in Appendix A is highly speculative. The authors correctly note that the proposed operator is not found in the standard literature and provide necessary caveats about its lack of gauge and rotational invariance. While interesting, it feels disconnected from the main data analysis and may be better suited for a separate theoretical paper.
*   **Required Fix:** The authors should consider shortening this appendix or removing it to maintain the paper's focus on the observational result. If retained, the "toy" and "schematic" nature of the model must be emphasized even more strongly.

---
### NIT (Cosmetic)

**P5-N1: Inconsistent Reference Dating**
*   **Location:** Bibliography (p. 21).
*   **Problem:** Reference [13] (Rincón et al.) is listed as "Astrophys. J. 982, 38 (2025)" but with an arXiv ID from November 2024 (`arXiv:2411.00148`). The year of publication should be consistent with the journal volume.
*   **Required Fix:** Please verify and correct the publication years for all references.

---
## Summary recommendation

**MAJOR REVISIONS**

This manuscript presents a comprehensive and statistically powerful null test for the environmental dependence of spiral chirality. The analyses, particularly the DESIVAST-anchored test and the new redshift-shell-corrected robustness check, are impressive and represent a significant contribution. However, the paper is critically flawed in its current form by its foundational reliance on an unpublished, non-peer-reviewed companion paper (P5-E1) and its post-hoc definition of the primary analysis (P5-E2). These two issues violate the standards of reproducibility and statistical rigor required for publication in Physical Review D.

Furthermore, the paper's structure obscures its strongest results, and its narrative fails to adequately address a significant (`3.4σ`) residual signal found in the data. If the authors can resolve the foundational dependency on Paper IV, restructure the manuscript to present a more transparent and logical narrative, and properly contextualize all results (including the non-null ones), a substantially revised version of this paper would likely be suitable for publication.