# P2 2026-06-04_R2pt — Physical Review D cosmology-physics referee

**Model**: `gemini-2.5-pro`
**Input format**:  [NATIVE PDF — Gemini sees rendered document]
**Wall time**: 66.5s

---

# Referee Report on "Testing the Matter Bounce with Primordial Non-Gaussianity: SPHEREx Forecasts, with a MegaMapper Outlook" (HUBIFY-2026-002)

## General Comments
The paper presents a detailed forecast for testing the matter bounce scenario with upcoming SPHEREx data. The primary scientific contributions are: (1) the first quantitative calculation of the template mismatch (`r`) between the matter bounce bispectrum and the local template, (2) an analysis of the theoretical uncertainty stemming from the underdetermined polynomial coefficients in the bispectrum shape, (3) a clarification of a factor-of-two normalization discrepancy in the literature, and (4) a detailed Bayesian model comparison. These are valuable and timely contributions to the field.

However, the manuscript in its current state is not suitable for publication. It is replete with internal author notes, version control comments, filenames, and even direct references to a previous round of review. This gives the impression of a very early draft rather than a finished paper submitted for peer review. These artifacts must be completely removed.

The underlying scientific analysis appears largely sound, but the presentation requires significant improvement for clarity and professionalism. The distinction between different forecast methodologies (e.g., bispectrum-only vs. joint scale-dependent bias) and their associated levels of idealization needs to be made clearer to the reader.

## Findings

### ESSENTIAL

-   **P2-E1 (Throughout): Unprofessional Manuscript Presentation.** The paper is filled with internal notes, version control tags, and artifacts from the writing and review process. This is unacceptable for a formal submission.
    -   **Problem:** Examples include:
        -   Abstract: "in 04b_fast_ensemble.py, 03b_fast_mock_validation.py, 02_compute_gr_aware_bayes_update.py"
        -   Abstract: "corrected v1.7.35 R-next-c-MAJ-1 from earlier ≈6..."
        -   Sec III B, p7: "the per-realization spread from phase3_fisher_overlap.json is wider..."
        -   Sec IV, p7: "a structural extension on the post-arXiv TODO"
        -   Sec VI C, p9: "(a rhetorical “>6 × 10^5” figure appeared in an older draft... any larger number was an aggregation error)"
        -   Sec VI C, p10: "(corrected v1.7.36 R-next-d-MIN-1 from prior ~ 12)"
        -   Sec X, p19: "(the prior conclusion-paragraph figure “> 6×10^5” was an aggregation error retired in §VI; corrected v1.7.36 R-next-d-MIN-2)"
        -   Appendix A.1, p20: "(R42 B8)", "(R42 reviewer R3 (Reviewer D, BLOCKER AL05))"
        -   Appendix A.2, p21: "(R42 B9)", "(R42 reviewers R1 (P2-01 Critical), R3 (Reviewer A BLOCKER), and R4 (L3 BLOCKER))"
        -   Table II Caption, p13: "v1.7.35 R-next-c-MAJ-1 correction..."
    -   **Fix:** The manuscript must be thoroughly scrubbed of all such internal comments, filenames, version tags, and references to the review process. The text should be presented as a clean, final scientific document.

-   **P2-E2 (Sec IX D, p17): Juxtaposition of Forecasts with Different Levels of Idealization.** The paper presents a `~9.9 sigma` forecast from a joint `(f_NL, n_fNL)` scale-dependent bias (SDB) analysis alongside the headline `3-5 sigma` forecast from a bispectrum analysis. While the text correctly notes they are different, presenting such a large, idealized number without the full analysis context (which is deferred to a "companion artifact") risks misleading the reader.
    -   **Problem:** The text states: "the matter-bounce fNL remains detectable at ∼ 9.9σ in the joint analysis after marginalizing over nfNL under idealized Fisher-input assumptions". This number is derived from a multi-bin SDB analysis whose inputs are not provided, and it is not subjected to the same systematic budget as the headline bispectrum forecast. This violates the principle of comparing like with like.
    -   **Fix:** The `9.9 sigma` figure should be removed from the main text, or at the very least, be heavily caveated and moved to a less prominent position. The discussion should emphasize that this is a preliminary, idealized calculation whose primary purpose is to motivate the self-consistency check on `n_fNL`, and that it cannot be directly compared to the main, systematics-degraded bispectrum forecast. The abstract has handled this reasonably well by not quoting the number, but the main text gives it too much prominence.

### MAJOR

-   **P2-M1 (Sec VI, p9-10): Convoluted Presentation of Bayesian Analysis.** The section on the Bayesian comparison is very difficult to follow due to numerous parenthetical asides correcting values from previous internal versions of the manuscript.
    -   **Problem:** The text is structured as a narrative of the authors' own calculation process, rather than a clear presentation of the final result. For example: "corrected v1.7.35 R-next-c-MAJ-1 from earlier ≈ 6 via direct scipy.stats.norm recompute of the closed-form formula".
    -   **Fix:** This entire section must be rewritten. Present the final methodology and the final results cleanly. All discussion of how the numbers have changed from previous drafts must be removed. The four-corner grid of priors and results should be presented clearly, perhaps in a more comprehensive table than the one currently before Sec VI.

-   **P2-M2 (Paper Structure & Length): Readability and Conciseness.** The paper is 23 pages long and could be significantly shortened and restructured for clarity. The flow of the argument is sometimes interrupted by overly detailed asides.
    -   **Problem:** The narrative jumps between different analyses (bispectrum, SDB, `f_NL-n_s` relation) and the structure feels disjointed (e.g., Sec VIII and IX are both discussion-like). The abstract is excessively dense. Much of the text is conversational.
    -   **Fix:** The authors should aim to shorten the paper to below 20 pages.
        1.  Rewrite the abstract to be a concise summary of the key results, not a table of contents.
        2.  Combine and streamline the discussion sections (e.g., VIII, IX, X).
        3.  Move some of the more detailed derivations or systematic checks (like the full null-space scan details) into appendices to improve the flow of the main text.
        4.  Edit the entire manuscript for conciseness, removing conversational phrasing.

### MINOR

-   **P2-m1 (Abstract): Deferred Results.** The abstract mentions a joint `(f_NL, n_fNL)` analysis but then states the full details and numerical significance are "deferred to a companion artifact".
    -   **Problem:** While acceptable, it's unusual to highlight an analysis in the abstract for which the key result is not provided. It weakens the abstract's self-contained nature.
    -   **Fix:** Consider rephrasing to focus only on the results actually presented in the paper, or state the `n_fNL` constraint that is derived, as that seems to be the main point of that section. For instance, state that the paper shows `n_fNL=0` is testable at the `sigma(n_fNL) ~ 0.09` level, which is a concrete result from the paper.

-   **P2-m2 (Sec VIII B, p16): Awkward Sub-heading.** The text contains a sub-heading "Linearization note.".
    -   **Problem:** This is not a standard or professional section heading.
    -   **Fix:** Integrate this note into the main paragraph or rephrase it as a proper sub-heading if the topic is distinct enough to warrant one.

-   **P2-m3 (Sec IX): Section Title.** Section IX is titled "DISCUSSION". However, the content is a mix of observational strategy, summary of other experiments, and a new joint forecast.
    -   **Problem:** The title does not accurately reflect the content. Section X is "CONCLUSION". The distinction is blurry.
    -   **Fix:** Retitle Section IX to something more descriptive, such as "Observational Strategy and Broader Context". Streamline the content to logically flow into the final conclusion.

### NIT

-   **P2-N1 (Title): Version Number.** The title block includes a version number `v1.7.43`.
    -   **Problem:** Version numbers are for pre-print servers like arXiv, not for a journal submission.
    -   **Fix:** Remove the version number.

-   **P2-N2 (Throughout): Date Format.** The date is given as "June 3, 2026 PDT".
    -   **Problem:** Timezones are irrelevant for a scientific paper's date.
    -   **Fix:** Remove "PDT".

## Summary recommendation
**MAJOR REVISIONS**

The paper addresses an important and timely question: the testability of the matter bounce scenario with upcoming cosmological surveys. It provides several novel and valuable contributions, including the quantification of the template mismatch for the bounce bispectrum, an analysis of theoretical uncertainties, and a clarification of a key normalization issue in the literature. The underlying physics arguments appear sound.

However, the manuscript is not in a state acceptable for publication. It is critically undermined by the pervasive inclusion of internal author notes, version control artifacts, and explicit references to a prior review cycle. This gives the paper an unprofessional and unfinished appearance. Furthermore, the presentation of the key Bayesian analysis is convoluted, and the overall structure could be significantly improved for clarity and conciseness. The authors must undertake a thorough revision to remove all non-scientific artifacts and rewrite several sections to present their results in a clean, professional, and clear manner before the paper can be reconsidered for publication.