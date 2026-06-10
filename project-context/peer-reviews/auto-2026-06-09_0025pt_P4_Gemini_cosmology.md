# P4 auto-2026-06-09_0025pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 720.4s

---

Here is a complete referee report for the submitted manuscript.

***

## Referee Report: "Survey-Scale Galaxy Chirality with Equivariant TTA..."

**Manuscript ID:** [Assigned by journal]
**Author:** Houston Golden
**Journal:** Physical Review D

This paper presents a detailed analysis of galaxy chirality (the handedness of spiral arms) using a large dataset of 3.2 million spiral galaxies from the DESI Legacy Surveys. The primary scientific result is a null detection of a large-scale angular dipole in the chirality asymmetry, which constrains isotropy-breaking axial-vector modes. The authors employ a Vision Transformer (ViT) classifier, hardened against biases using Test-Time Equivariant Averaging (TTA). A key contribution is the identification and quantification of a "monopole-mask leakage" channel, a systematic effect where a global (monopole) asymmetry in classification couples with the patchy survey footprint to create a spurious dipole signal in a naive analysis.

The analysis is exceptionally thorough. The authors carefully distinguish between different estimators and null hypotheses, provide a clear hierarchy for their analysis, and perform an extensive suite of systematic checks. The main null result is robust, supported by two independent estimators: a real-space dipole fit (+0.43σ) and a spherical harmonic (MASTER-deconvolved) analysis on a wide-area subsample (-0.122σ). A statistically significant residual (+3.64σ) found on a smaller, patchier "canonical mask" is convincingly attributed to the aforementioned systematic leakage, and a five-pronged analysis is used to rule out a cosmological origin for this residual.

The paper represents a significant contribution to the field, providing one of the most stringent and carefully controlled constraints on a galaxy chirality dipole to date. The methodology for identifying and nulling the monopole-mask leakage systematic is a valuable lesson for all large-scale survey analyses of this type.

While the core analysis is sound and the conclusions are well-supported, the manuscript requires significant revision to address several numerical inconsistencies, clarify confusing passages, and ensure all presented results are final.

### ESSENTIAL Revisions

**P4-E1: Inconsistent Galaxy Counts in Figure 2 (Page 6)**
*   **Problem:** The galaxy counts for CW, CCW, and Not-Spiral classes listed in the caption of Figure 2 do not match the counts shown in the pie chart itself.
    *   Caption: N_cw = 1,592,107; N_ccw = 1,609,053; N_ns = 5,273,371.
    *   Pie Chart: N_cw = 1,687,069; N_ccw = 1,634,726; N_ns = 5,152,736.
    While both sets of numbers sum to the same total, this is a critical inconsistency in the primary data statistics. All other statistics in the paper (e.g., the global CW fraction in Table II) depend on these numbers.
*   **Required Fix:** The author must identify the correct set of numbers and use them consistently throughout the entire manuscript, including in Figure 2, its caption, and all derived quantities.

**P4-E2: Inconsistent Figure and Caption for Figure 4 (Page 8)**
*   **Problem:** The caption for Figure 4 describes a different figure from the one that is shown.
    *   The caption states: "Top: l=1 dipole power. Bottom: l=2 quadrupole. Black: data; orange band: 500-MC monopole-only generative null...".
    *   The figure shown is a single bar chart for multipoles l=1 to l=5, with blue bars for "Measured" data and grey bars for "Null expectation". There is no "top/bottom" structure, no "black" data, and no "orange band".
*   **Required Fix:** The caption must be completely rewritten to accurately describe the figure that is presented.

### MAJOR Revisions

**P4-M1: Analysis Based on "In Queue" Re-run (Footnote 1, Page 5)**
*   **Problem:** Footnote 1 reveals that a key methodological choice for the generative null (using `N_spiral(p)` trials vs. `N_all(p)` trials) has a quantitative impact, and that a "parallel rerun on N(p)all-trial draws is in queue". A published paper cannot be based on incomplete or provisional analysis. The statement that the "headline conclusion... is robust to the trial-pool choice" is an assertion that must be demonstrated with the final analysis.
*   **Required Fix:** The author must complete the `N_all(p)` re-run and update the relevant results (e.g., the 99.3% reproduction figure and the +1.68σ residual in Table IV) to reflect the final, definitive analysis choice. The footnote should be rewritten to simply state the final methodology, removing any reference to pending computations.

**P4-M2: Confusing and Opaque Footnote on Subsample Robustness (Footnote 2, Page 11)**
*   **Problem:** Footnote 2 on page 11 is extremely dense and difficult to parse. It introduces a new, previously unmentioned estimator ("monopole-preserving Catalog-C-full +4.31σ") in a footnote to make a point about high-confidence subsamples. This makes the argument hard to follow and obscures the main point. The comparison between a +4.31σ pseudo-C_l and a +0.43σ real-space dipole, even with the caveat that they are not comparable, adds more confusion than clarity.
*   **Required Fix:** This footnote must be rewritten for clarity. The author should consider moving this analysis into the main body of Appendix E and explaining it more clearly. The core point—that the leakage-contaminated signal vanishes when restricting to high-confidence samples—is a strong one and deserves a clearer explanation. Avoid introducing new, one-off estimator names in a footnote.

### MINOR Revisions

**P4-N1: Discrepancy in Global CW Fraction Significance (Table II, Page 4)**
*   **Problem:** The "Dev. (σ)" column in Table II appears to be calculated incorrectly. For Catalog C, the text gives f_cw = 0.4974 and σ_binom = 0.000279. The deviation from 0.5 is (0.4974 - 0.5) / 0.000279 = -9.32σ. The table reports 9.5 (and the text uses this value). Similar small discrepancies exist for the other rows.
*   **Required Fix:** Recompute and correct all values in the "Dev. (σ)" column of Table II. Update the corresponding value in the main text (Sec. IV B).

**P4-N2: Discrepancy in Monopole Null z-score (Table IV, Page 6)**
*   **Problem:** The z-score for the "Pre-MASTER pseudo-C_l" statistic in Table IV is calculated as +1.68. My calculation is (1.696 - 1.685) / 0.007 = 1.57. This is a minor but noticeable discrepancy.
*   **Required Fix:** Please recompute and, if necessary, correct the z-score in Table IV.

**P4-N3: Scope of Parity-Odd Signal (Sec. VI B, Page 8)**
*   **Problem:** The text states "the parity-odd signal lives in the l=0 monopole and even-l multipoles." While this is true for scalar fields like temperature, for a projected spin field (an axial vector), the parity-odd modes are different. A full 3D analysis would be required, but this statement might be an oversimplification for the specific observable here.
*   **Required Fix:** The author should briefly clarify the context for this statement or add a citation. For the scope of this paper (a 2D projected analysis), the key point is that the l=1 dipole is parity-even, which is correctly stated. A minor rephrasing to "Parity-odd signatures are expected in other observables, such as the monopole and even-l multipoles of certain fields..." would be sufficient.

**P4-N4: Typo in Dilution Factor Formula (Sec. VI A, Page 8)**
*   **Problem:** The text gives the GZ1-dilution factor as "g=2a-1 ≈ 0.398 for a = 0.6991". The formula should be `g = 2a - 1`. The use of "a-" is a clear typographical error.
*   **Required Fix:** Correct the typo to `g = 2a - 1`.

### NIT (Cosmetic)

**P4-T1: Date of Submission (Page 1)**
*   **Problem:** The paper is dated "June 2026".
*   **Required Fix:** Please correct to the current date of submission.

***

## Summary recommendation

**MAJOR REVISIONS**

This is a very strong, high-impact paper that performs a careful and robust analysis of a topic of significant interest. The authors' treatment of systematics is exemplary. The paper is well on its way to being suitable for publication in Physical Review D. However, the identified issues, particularly the numerical inconsistencies in key tables and figures (P4-E1, P4-E2) and the reliance on an "in queue" analysis (P4-M1), are too significant for the paper to be accepted in its current form. Once these essential and major points are thoroughly addressed, the paper should be reconsidered for publication.