# P1B auto-2026-06-05_1418pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 112.5s

---

## Referee Report on "Technical Verification Companion to the ECH Spin-Torsion Program..."

**Report ID:** P1B-2024-06

**To the Editor of Physical Review D,**

I have reviewed the manuscript "Technical Verification Companion to the ECH Spin-Torsion Program: ACDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model" by Houston Golden. The paper presents technical validation for three numerical analyses related to a companion paper on Einstein-Cartan-Holst (ECH) cosmology. The analyses cover: (1) a stock-CAMB MCMC run for ΛCDM+ΔNeff, (2) a validation of a NaMaster pseudo-Cℓ pipeline for cosmic birefringence, and (3) a consistency check of the observed birefringence signal with a spectator axion-like particle (ALP) model.

The technical work appears to be sound, and the author is commendably transparent about the scope and limitations of each analysis. The detailed disclosures regarding pipeline biases, MCMC convergence, parameter priors, and model-dependent fine-tuning meet the high standards of rigor expected for PRD.

However, the manuscript suffers from significant structural and clarity issues that must be addressed before it can be considered for publication. The current organization obscures the results and could mislead a reader not paying close attention to the footnotes. My recommendation is for **MAJOR REVISIONS**.

Below are my detailed findings.

---

### ESSENTIAL Revisions

**P1B-E1: Confusing Manuscript Structure (Sections III, V)**
*   **Location:** Pages 3, 4, and 6 (Sections III and V).
*   **Problem:** The paper presents two distinct MCMC analyses: a ΛCDM+ΔNeff proxy test (Table I) and a w0wa dark energy model test (Table II). The presentation of these analyses is confusingly interwoven. The text in Section III ("STOCK-CAMB ACDM+ΔNeff MCMC") begins discussing the results of the w0wa analysis ("Physics interpretation (Table II)"), even though Table II and its primary discussion belong elsewhere. Section V ("Cosmological Fits and Model Comparison") then re-addresses these results. This structure makes the paper very difficult to follow.
*   **Required Fix:** The manuscript must be restructured to present these two analyses sequentially and independently. I recommend the following structure:
    1.  A dedicated section for the ΛCDM+ΔNeff analysis, containing the text from the first half of Section III and Table I.
    2.  A new, separate section for the w0wa analysis, containing the "Physics interpretation" text currently on page 3, all of Table II, and the discussion from Section V.B.
    This will create a clear, logical flow and separate the two distinct scientific results.

### MAJOR Revisions

**P1B-M1: Misleading Framing of the Spectator-ALP Analysis (Section VI)**
*   **Location:** Page 7, Section VI, and Appendix C (page 9, footnote 5).
*   **Problem:** The main text of Section VI frames the analysis as a "Spectator-ALP consistency check." However, footnote 5 on page 9 reveals that the MCMC analysis uses a prior on the initial misalignment angle, θi ∈ [0.5, 2], which corresponds to the dark-energy-ALP regime (where the ALP's energy density is non-negligible), not the spectator regime (which requires θi ~ 0.1). The text in footnote 4 correctly identifies the ~25x fine-tuning required to be in the spectator regime. Therefore, the MCMC analysis does not actually test the spectator model but rather a dark-energy model. While the footnotes provide the necessary clarification, this is a critical detail that must be addressed in the main body of the text to avoid misinterpretation.
*   **Required Fix:** The main text of Section VI must be revised to accurately reflect what the MCMC analysis actually constrains. The author should state upfront that the MCMC explores a parameter space largely corresponding to a dark-energy ALP and then discuss how the spectator-ALP scenario exists as a fine-tuned corner of this space. The "spectator-ALP consistency check" framing should be revised to something like "ALP model consistency check," with the spectator case treated as a specific sub-class. The crucial information in footnotes 4 and 5 should be integrated into the main paragraph on "MCMC parameter estimation."

### MINOR Revisions

**P1B-m1: Inconsistent Post-Burn-in Sample Counts**
*   **Location:** Page 2 (footnote 1) and Page 5 (Figure 1 caption).
*   **Problem:** Footnote 1 calculates the post-burn-in sample count for the full-tension run as 176,240 * 0.7 ≈ 123,368. The caption for Figure 1 states the plot uses "119,617 post-burnin samples, getdist-thinned." The discrepancy is likely due to the `getdist` effective sample weighting/thinning, but this is not explicitly stated.
*   **Required Fix:** Clarify the relationship between these two numbers in the Figure 1 caption. For example: "...(thinned from 123,368 post-burnin samples by `getdist` for an effective sample size of...)."

**P1B-m2: Future Date on Manuscript**
*   **Location:** Page 1, under the author's name.
*   **Problem:** The paper is dated "2026-06-03 PDT".
*   **Required Fix:** This should be corrected to the date of submission.

### NIT-PICKING (Cosmetic)

**P1B-N1: Mention of "Ongoing" Run in Abstract**
*   **Location:** Page 1, Abstract.
*   **Problem:** The abstract mentions a "third Planck-only combination ongoing." Since no results from this run are presented, this information is superfluous.
*   **Required Fix:** For conciseness, consider removing this phrase from the abstract.

**P1B-N2: Non-Standard Claims Table**
*   **Location:** Page 10, Table III.
*   **Problem:** Table III, which classifies the paper's claims, is a non-standard feature for a PRD article. While it is clear and helpful, it may not conform to the journal's style.
*   **Required Fix:** The author should be prepared to convert this table into prose in the Conclusions or move it to an appendix if requested by the editor. This is not a required change at this stage but a suggestion for consideration.

---

## Summary recommendation

**MAJOR REVISIONS**

This manuscript provides a valuable and methodologically rigorous set of technical verifications. The author's commitment to transparency regarding the scope and limitations of the work is a significant strength. However, the paper is currently hampered by a confusing structure that conflates two separate analyses and a misleading framing of the ALP consistency check. These issues are substantial but correctable. Once the paper is restructured for clarity and the ALP section is revised to accurately reflect the parameter space being tested, it will likely be a strong candidate for publication in Physical Review D.