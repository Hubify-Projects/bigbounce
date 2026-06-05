# P1B R10v3p1 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 138.8s

---

## Referee Report on "Technical Verification Companion to the ECH Spin-Torsion Program..."

**Manuscript ID:** [Assigned by journal]
**Author:** Houston Golden
**Date:** [Current Date]

This paper presents three technical verification analyses intended as a companion to a primary work on Einstein-Cartan-Holst (ECH) spin-torsion cosmology. The analyses include: (1) a ΛCDM+ΔNeff MCMC analysis using public data and codes as a null-consistency test; (2) a Monte Carlo validation of a `NaMaster` pseudo-Cₗ pipeline for cosmic birefringence; and (3) a consistency check of the observed birefringence signal with a spectator axion-like particle (ALP) model.

The paper demonstrates a high level of methodological rigor, transparency, and correctness in its calculations. The author is commendably careful in defining the scope and limitations of each analysis, particularly in distinguishing pipeline validation from sky detection, and in clarifying that the reported analyses do not directly test the ECH framework but rather provide context and verification for it. The detailed reproducibility materials are a significant strength.

However, the manuscript suffers from a severe structural problem that makes it difficult to follow and renders it unsuitable for publication in its present form. The discussion of two separate MCMC analyses (a ΔNeff model and a w₀wₐ model) is interwoven throughout the text, leading to a confusing and disjointed narrative. A complete restructuring is required before the paper can be reconsidered.

## Summary recommendation
**MAJOR REVISIONS**

The scientific content, once disentangled, appears sound and suitable for publication as a technical note or companion paper. The calculations are verified to be correct, and the caveats and scope limitations are handled with an exemplary level of care. However, the manuscript's structure is critically flawed, preventing a clear reading. The paper must be thoroughly reorganized to present each analysis sequentially and coherently.

---
### Detailed Findings

#### ESSENTIAL

**P1B-E1: Major Structural Reorganization Required (Sections III, IV, V, VI)**
*   **Location:** Pages 3-6.
*   **Problem:** The paper presents results from two distinct MCMC analyses: a ΛCDM+ΔNeff model (results in Table I) and a w₀wₐ model (results in Table II). The discussion of these two analyses is completely entangled. For example, Section III begins the ΔNeff discussion, but the "Physics interpretation" subsection on page 3 abruptly switches to the w₀wₐ results of Table II. Page 4 presents Table II but the text below it switches back to discussing the full-tension ΔNeff chain from Table I. Section V ("Cosmological Fits and Model Comparison") is a confusing summary of both analyses without a clear separation. This makes the paper extremely difficult to follow.
*   **Required Fix:** The paper must be restructured to present each analysis in a self-contained manner. A suggested structure:
    1.  Introduction.
    2.  Analysis 1: The ΛCDM+ΔNeff MCMC Proxy. This section should contain all relevant setup, Table I, Figure 1, and the complete discussion of these results, including the H₀ tension and M_B-H₀ degeneracy checks.
    3.  Analysis 2: The w₀wₐ Quintom-B Test. This section should contain the setup, Table II, and the complete discussion of these results. (While this analysis is interesting, the author should clarify its relevance to the main ECH program, as it feels somewhat disconnected from the other two verification tasks).
    4.  Analysis 3: NaMaster Pipeline Validation.
    5.  Analysis 4: Spectator ALP Consistency Check.
    6.  Conclusions.
    This linear structure will resolve the narrative confusion and make the paper's valuable technical contributions accessible.

#### MAJOR

**P1B-M1: Clarify the Role of the w₀wₐ Analysis**
*   **Location:** Abstract, Sections III, V.
*   **Problem:** The abstract and title focus on the ΔNeff proxy, the NaMaster pipeline, and the ALP check. The w₀wₐ analysis, which yields a >4σ departure from ΛCDM, is a significant result that appears with little motivation or connection to the other three topics. It is not mentioned in the abstract's three-point summary. Its inclusion feels ad-hoc.
*   **Required Fix:** The author must either (a) better integrate the w₀wₐ analysis into the paper's narrative, explaining its role as a verification task for the ECH program (e.g., as a test for quintom behavior motivated by bounce cosmologies), and update the abstract to include it, or (b) remove it from this companion paper and present it separately, as it seems to be a standalone scientific result rather than a "technical verification."

#### MINOR

**P1B-m1: Typo in Birefringence Equation**
*   **Location:** Page 7, Eq. (3).
*   **Problem:** The equation for the birefringence angle β contains the term "O_EM". This is almost certainly a typo for the fine-structure constant, α_EM.
*   **Required Fix:** Replace "O_EM" with "α_EM" in Equation (3).

**P1B-m2: Minor Numerical Inconsistency in Quoted H₀ Value**
*   **Location:** Page 4, paragraph 3.
*   **Problem:** The text states, "The full-tension chain returns H₀ = 67.69 ± 1.06 km/s/Mpc...". However, Table I on page 3 lists this value as H₀ = 67.68 ± 1.06.
*   **Required Fix:** Correct the value in the text on page 4 to 67.68 to match Table I.

**P1B-m3: Potentially Confusing Sample Count in Figure Caption**
*   **Location:** Page 5, Figure 1 Caption.
*   **Problem:** The caption states the plot uses "119,617 post-burnin samples", while a naive calculation from footnote 1 (176,240 * 0.7) would yield 123,368. The discrepancy is explained in a parenthetical on page 3 ("reflects additional getdist effective-sample weight-based thinning"). While the explanation exists, it is easy to miss and could cause confusion.
*   **Required Fix:** For maximum clarity, briefly repeat the explanation for the sample count difference directly in the Figure 1 caption. For example: "...(119,617 post-burnin samples, thinned from 176,240 raw samples; the count reflects standard burn-in removal and additional `getdist` effective-sample weighting)."

#### NIT

**P1B-N1: Future Date on Manuscript**
*   **Location:** Page 1.
*   **Problem:** The manuscript is dated "2026-06-03 PDT".
*   **Required Fix:** Update the date to reflect the submission date.

**P1B-N2: Appendix B Title Placement**
*   **Location:** Page 9.
*   **Problem:** The title "Appendix B: Claims Classification" appears on page 9, but the corresponding table (Table III) is on page 10. This is a minor formatting issue.
*   **Required Fix:** Ensure the appendix title and its content appear together, perhaps by moving the title to page 10.