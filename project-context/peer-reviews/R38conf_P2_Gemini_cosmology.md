# P2 R38conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper2_fnl_forecast_v1.7.61.pdf` md5=6b413c94 pages=27
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 125.1s

---

**Referee Report for "Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook"**

## Summary of the Paper

This paper presents a detailed sensitivity forecast for testing the matter-bounce cosmological scenario using upcoming large-scale structure surveys, primarily SPHEREx. The central prediction of the scalar-only matter-bounce model is a local-type non-Gaussianity of f_NL = -35/8 = -4.375. The paper's main contributions are: (1) a thorough audit and validation of this prediction, including a resolution of a factor-of-two discrepancy in the literature (Cai et al. 2009 vs. Li et al. 2017); (2) a quantification of the template mismatch between the matter-bounce bispectrum and the standard local template, resulting in a signal recovery factor `r`; (3) a comprehensive analysis of systematic uncertainties, including polynomial coefficient ambiguity, GR projection effects, and PNG bias calibration; and (4) a Bayesian model comparison to quantify the discriminating power of SPHEREx against inflationary alternatives. The paper concludes that SPHEREx can test the benchmark model at a significance of ~2.6-5σ after systematics, and a detection would favor the bounce over tuned multifield inflation with a Bayes factor of ~9-14 under the recommended priors.

## General Comments

This is a comprehensive, rigorous, and well-executed study. The author has demonstrated a deep understanding of both the theoretical underpinnings of the matter-bounce model and the observational realities of large-scale structure surveys. The paper's strength lies in its meticulous attention to detail, particularly in the audit of the theoretical prediction and the transparent consolidation of the systematic budget. The resolution of the Cai/Li discrepancy via the in-in commutator identity is a valuable clarification for the community. The systematic budget presented in Table IV is an excellent example of clear, traceable error analysis. The paper is well-written and the arguments are logically structured. The provided code and data artifacts for reproducibility are commendable and meet the highest standards.

The paper is largely sound and represents a solid contribution to the field. The required revisions are primarily focused on ensuring clarity, removing production artifacts, and refining the presentation of the results.

## Findings

### ESSENTIAL

*   **P2-E1:** Section: End of paper (after bibliography) | Page: 27
    *   **Problem:** The paper contains a block of internal reviewer metadata at the very end: `[REVIEWER METADATA — NOT PART OF THE PAPER — DO NOT FLAG AS ARTIFACTS] Paper tag: P2 | Round: R38conf | Pages: 27 ...`. This is a production artifact and must not be present in the final manuscript.
    *   **Required Fix:** Remove this entire block.

### MAJOR

*   **P2-M1:** Section: Abstract, IV, IX, and XI.D | Pages: 1, 9, 20, 21
    *   **Problem:** The paper analyzes two distinct forecast channels: the primary, bispectrum-only forecast from Heinrich et al. [6] (σ(f_NL) ≈ 0.7), and a subordinate, joint (f_NL, n_fNL) forecast using scale-dependent bias (SDB). The body of the paper correctly establishes the bispectrum channel as the main, more robust one, and the SDB joint channel as a weaker, degeneracy-limited cross-check. However, the abstract and discussion could be even more explicit about this hierarchy to prevent any misinterpretation by a reader who skims the paper. The SDB-only marginalized σ(f_NL) = 7.06 is much weaker than the bispectrum-only σ(f_NL) = 0.7, and this factor of 10 difference in constraining power is a key result.
    *   **Required Fix:**
        1.  In the abstract, ensure it is unambiguously clear that the headline significances (2.6-5σ, etc.) derive from the galaxy bispectrum channel, and that the SDB channel is treated as a separate, complementary probe whose primary utility is in constraining the running (n_fNL), not f_NL itself, due to strong degeneracies.
        2.  In Section XI.D, consider adding a sentence that explicitly states: "The constraining power on f_NL from the bispectrum channel (σ ≈ 0.7) is an order of magnitude stronger than that from the SDB-only joint analysis after marginalizing over n_fNL (σ ≈ 7.0), establishing the bispectrum as the primary channel for testing the matter-bounce amplitude."

*   **P2-M2:** Section: General | Pages: 1-27
    *   **Problem:** The paper is quite long (27 pages). While the content is of high quality and the detail is a strength, the main narrative could be streamlined. The core contribution is a recast and detailed audit, not a from-scratch forecast. Some of the detailed validation steps, while important for reproducibility, interrupt the flow of the main argument.
    *   **Required Fix:** Consider moving some of the more technical validation details into appendices to shorten the main body. For example, the detailed description of the null-space scan convergence tests (p. 4) or the step-by-step Monte Carlo validation of the Bayes factor formula (p. 12) could be summarized in the main text and elaborated upon in an appendix. This is a suggestion for improving readability, not a requirement to remove content. A target length of ~20 pages for the main text + bibliography would be more typical for a paper of this scope.

### MINOR

*   **P2-m1:** Section: Abstract & IV | Pages: 1, 10
    *   **Problem:** The abstract and main text quote a "realistic ~2.6-5σ" significance range. The lower bound (2.6σ) is clearly derived from the most conservative "all-combined" scenario in Table IV. The origin of the upper bound (5σ) is less transparent. It appears to correspond to the optimistic template-corrected baseline (5.2-5.5σ) with some small, unspecified systematic degradation.
    *   **Required Fix:** Please clarify precisely which systematic configuration corresponds to the 5σ upper bound of the "realistic" range. For instance, state "The realistic range of 2.6-5σ spans from the most conservative scenario including all systematics to an optimistic case including only template-mismatch and e-correction." This would make the construction of the headline range fully transparent.

*   **P2-m2:** Section: I | Page: 2
    *   **Problem:** The corresponding author's email is given as `houston@hubify.com`. While perfectly functional, for a formal publication in a journal like PRD, an institutional or academic email address is standard and lends additional professional credibility.
    *   **Required Fix:** If possible, please use an institutional or long-term academic email address. If not, this can remain as is.

*   **P2-m3:** Section: VI | Page: 14
    *   **Problem:** The caption for Table II is exceptionally long, containing detailed explanations of the different priors, the interpretation of the results, and the connection to the abstract's rebooked values. Much of this text reads like main-body prose.
    *   **Required Fix:** Please shorten the caption to focus only on defining the table's columns and rows. Move the detailed interpretative text and the worked example of the rebooking calculation into the main body of Section VI. This will improve the table's readability as a standalone object.

*   **P2-m4:** Section: VIII.A | Page: 18
    *   **Problem:** The reanalysis of the DESI DR1 constraints reports `f_NL = -3.6^{+9.0}_{-9.1}`. The asymmetric error bars are unusual for a Fisher-based forecast or a likelihood that is approximately Gaussian.
    *   **Required Fix:** The original DESI paper [34] reports `f_NL = -3.6 ± 9.1`. Please correct the error bars to be symmetric, or if the asymmetry is intentional and derived from the source, please cite the specific table/figure and explain its origin. *Self-correction: The cited arXiv ID 2411.17623 reports symmetric errors in its abstract. The text should be corrected.*

### NIT

*   **P2-N1:** Section: Abstract | Page: 1
    *   **Problem:** Minor grammatical awkwardness in the sentence: "The Li et al. [7] value fNL = -35/16 is the single time-ordered intermediate of the in-in calculation; the full in-in result, fixed by the -2 Im".
    *   **Required Fix:** Suggest rephrasing for clarity, for example: "...the full in-in result is fixed by the -2 Im commutator identity...".

*   **P2-N2:** Section: Data and Code Availability | Page: 23
    *   **Problem:** The text contains a placeholder: "archived at Zenodo (DOI inserted at submission)".
    *   **Required Fix:** Before publication, this placeholder should be replaced with the actual DOI, or if that is not possible, rephrased to indicate that the DOI will be provided upon acceptance.

*   **P2-N3:** Section: II.A, Footnote 1 | Page: 3
    *   **Problem:** The footnote mentions an artifact `c9i_epsilon_ratio_check.json`. While the commitment to reproducibility is excellent, referencing internal script artifact names directly in the final text can be slightly distracting.
    *   **Required Fix:** Suggest rephrasing to describe the check without naming the specific file, e.g., "This was verified numerically (see the data release for the corresponding script)."

## Summary recommendation

**MINOR REVISIONS**

This is an excellent, high-quality paper that makes a valuable and timely contribution. The scientific analysis is sound, thorough, and transparent. The recommendation for "Minor Revisions" reflects the fact that the core results and conclusions are robust, and the required changes are focused on improving the presentation, clarity, and professionalism of the manuscript rather than correcting any scientific flaws. After addressing the points above, particularly the removal of the production artifact and the clarification of the main forecast channel, the paper will be a strong candidate for publication in Physical Review D.