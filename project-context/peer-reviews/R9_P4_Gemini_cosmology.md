# P4 R9 — Physical Review D cosmology-physics referee

**Model**: `gemini-2.5-pro`
**Input format**:  [NATIVE PDF — Gemini sees rendered document]
**Wall time**: 85.7s

---

## Referee Report

This paper presents a detailed analysis of galaxy chirality using 3.2 million spiral galaxies from the DESI Legacy Surveys. The authors' primary scientific result is a null measurement of the `l=1` angular dipole, which is an important constraint on isotropy-breaking, parity-even physics. The strength of the paper lies in its comprehensive approach to systematics, particularly the identification and quantification of a "monopole-mask leakage" channel. The authors correctly distinguish between parity-even (dipole) and parity-odd (monopole) observables, a crucial point often confused in the literature.

However, the paper suffers from several major issues in its statistical methodology and presentation that must be addressed before it can be accepted for publication. The number of Monte Carlo simulations is insufficient for the claimed precision, and the central argument for selecting the headline null result over a statistically significant (`+3.64σ`) residual found in a different configuration is not clearly justified. The paper's structure and title also need significant revision to improve clarity.

### ESSENTIAL Revisions

**P4-E1: Insufficient number of Monte Carlo simulations**
-   **Location:** Abstract (p. 1), Sec IV D (p. 4), Sec VII (p. 6), Table IV (p. 5)
-   **Problem:** The number of Monte Carlo (MC) simulations used for null hypothesis testing is consistently low (N=500). For an analysis aiming for high precision and making claims about signals at the >3σ level, this is statistically insufficient. This low number provides poor resolution of the null distribution's tails and introduces significant uncertainty into the quoted p-values and significances.
-   **Required Fix:** All null tests must be re-run with a number of simulations appropriate for the claimed precision, at a minimum N=10,000. All reported σ and p-values must be updated accordingly.

**P4-E2: Unclear justification for two different masks and two `l=1` results**
-   **Location:** Abstract (p. 1), Sec III A (p. 3), Sec IV C/D (p. 4), Table I (p. 4), Table III (p. 5), Sec VII (p. 6)
-   **Problem:** The paper presents two distinct results for the `l=1` dipole: a null result (`-0.122σ`) on a "subsample mask" and a significant residual (`+3.64σ`) on a "canonical mask". The paper privileges the null result as the primary finding while dismissing the other as a systematic, but the rationale for this choice is not clearly articulated. The physical and operational definitions of these masks, and the reason one is considered more robust to systematics, are not adequately explained. This ambiguity undermines the central claim of the paper.
-   **Required Fix:**
    1.  In the Methods section, provide precise, quantitative definitions for the "canonical mask" and the "subsample mask".
    2.  Provide a clear, physical justification for why the "subsample mask" is expected to be less prone to the monopole-leakage systematic.
    3.  The abstract and introduction must be revised to clearly state that two different masks are used and briefly justify why the subsample mask provides the more robust cosmological constraint.
    4.  Explain the `Nmap weighted` column in Table I and document the weighting scheme used.

### MAJOR Revisions

**P4-M1: Unclear interpretation of the `+3.64σ` residual significance**
-   **Location:** Abstract (p. 1)
-   **Problem:** The abstract presents a confusing and contradictory statement regarding the significance of the canonical-mask residual: "+3.64σ (z = ∆/σnull moment-ratio; empirical rank pMC = 0.030, i.e. ≈1.9σ Gaussian-equivalent)". A `+3.64σ` result should correspond to a p-value orders of magnitude smaller than 0.030. This implies either a highly non-Gaussian null distribution, which is not discussed, or an error in reporting. Presenting `+3.64σ` without this crucial context is misleading.
-   **Required Fix:** Clarify the definition of `σ` for this result. The authors should consistently use the empirical p-value and its corresponding Gaussian-equivalent significance (e.g., `1.9σ`). If the moment-ratio `z` is reported, the non-Gaussianity of the null distribution must be explicitly discussed and visualized (e.g., with a histogram). This clarification must be made in the abstract and throughout the text.

**P4-M2: Overly long and technical title**
-   **Location:** Title (p. 1)
-   **Problem:** The title is excessively long and detailed, functioning more as a mini-abstract than a title. It is not suitable for a journal publication.
-   **Required Fix:** Shorten the title to be more concise and impactful, focusing on the main contribution. For example: "A Null Measurement of the Galaxy Chirality Dipole on 3.2 Million DESI Legacy Spirals".

**P4-M3: Paper structure and length**
-   **Location:** Entire paper
-   **Problem:** For a paper whose main result is a null measurement, the current 10-page structure is too long and the narrative is difficult to follow. The core argument is fragmented across the main text and multiple appendices, obscuring the key takeaways.
-   **Required Fix:** Restructure the paper to improve clarity and conciseness. The main text should be shortened (e.g., to 6-7 pages) to focus on the primary null result and a clear summary of the key systematic. The extensive diagnostic tests and detailed analyses of secondary results should be moved entirely to appendices.

### MINOR Revisions

**P4-m1: Inconsistent notation**
-   **Location:** Abstract (p. 1), Sec III C (p. 3)
-   **Problem:** The notation for probabilities is inconsistent (e.g., `peq_CW` vs. `P_eq_CW`, `p_CW` vs. `P_CW`).
-   **Required Fix:** Choose a single, consistent notation for all probabilities throughout the manuscript.

**P4-m2: Unnecessary phrasing**
-   **Location:** Introduction (p. 2)
-   **Problem:** The sentence "The present paper is a standalone observational result: our null dipole at sub-percent sensitivity does not depend on any unpublished companion work" is unnecessary.
-   **Required Fix:** Remove this sentence.

**P4-m3: Inconsistent null method description**
-   **Location:** Abstract (p. 1), Table I (p. 4)
-   **Problem:** The null hypothesis method for the real-space dipole is described as "per-pixel-shuffle null" in the abstract but "isotropic bootstrap" in Table I.
-   **Required Fix:** Ensure the description of the null method is consistent in all locations.

### NITs

**P4-N1: Date format**
-   **Location:** p. 1
-   **Problem:** The date is a future date "(Dated: June 2026)".
-   **Required Fix:** Update to the correct submission date.

**P4-N2: Email address**
-   **Location:** p. 1
-   **Problem:** The contact email `houston@hubify.com` appears to be non-institutional.
-   **Required Fix:** Consider using a permanent institutional or academic email address to improve long-term contactability.

## Summary recommendation
**MAJOR REVISIONS**

This paper has the potential to be an important contribution to the field by providing a robust null result on the galaxy chirality dipole with a rigorous treatment of systematics. However, it is not acceptable for publication in its current form. The statistical analysis is underpowered due to an insufficient number of simulations, and the central argument justifying the headline result is confusing and inadequately explained. The authors must address the ESSENTIAL and MAJOR points listed above, particularly by re-running their analysis with more simulations and by providing a much clearer explanation and justification for their choice of analysis masks and interpretation of the results. A significant restructuring to improve clarity and conciseness is also required.