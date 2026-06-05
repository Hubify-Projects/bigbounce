# P2 2026-06-04_R3clean — Physical Review D cosmology-physics referee

**Model**: `gemini-2.5-pro`
**Input format**:  [NATIVE PDF — Gemini sees rendered document]
**Wall time**: 73.0s

---

**Referee Report on "Testing the Matter Bounce with Primordial Non-Gaussianity: SPHEREx Forecasts, with a MegaMapper Outlook"**

**Manuscript ID:** P2
**Round:** 2026-06-04_R3clean

## General Comments

This paper presents a detailed forecast for testing the matter-bounce cosmological scenario using primordial non-Gaussianity measurements from the upcoming SPHEREx survey, with an outlook towards the proposed MegaMapper survey. The primary prediction under investigation is the local non-Gaussianity parameter `f_NL = -35/8`.

The main contributions of the paper are:
1.  A detailed audit and validation of the theoretical prediction for `f_NL` from the matter bounce, including a crucial clarification of a factor-of-two discrepancy in the literature related to normalization conventions and the in-in formalism.
2.  The first quantitative calculation of the template mismatch (`r`) between the matter-bounce bispectrum and the standard local template, finding that a local estimator recovers `r ~ 84%` of the signal.
3.  A comprehensive forecast for SPHEREx, recasting existing sensitivities to account for the template mismatch and a detailed budget of systematic uncertainties. The headline forecast is a `3-5σ` detection significance.
4.  A Bayesian model comparison, finding that a detection would favor the bounce over tuned inflationary alternatives with a Bayes factor of `~10-17`.

The paper is, for the most part, thorough, technically sound, and addresses a timely question in cosmology. The clarification of the normalization convention in Appendix A is particularly valuable. However, the manuscript in its current form suffers from several serious issues that preclude its publication. The most significant of these is the inclusion of a secondary, unsubstantiated forecast that claims a much higher significance (`~9.9σ`) than the paper's main result. Additionally, the manuscript is littered with unprofessional internal commentary, notes on previous versions, and review-process artifacts that must be removed.

The following report details the required revisions.

---

## Findings

### ESSENTIAL

**P2-E1: Unsubstantiated Joint (fNL, nfNL) Forecast**
-   **Section/Page:** Sec. IX.D, p. 16
-   **Problem Statement:** This section introduces a separate Fisher analysis for a joint `(f_NL, n_fNL)` constraint using scale-dependent bias (SDB). It claims a detection significance of `~9.9σ` for `f_NL`. This result is problematic for several reasons: (1) It is presented as a secondary analysis, yet its significance dramatically overshadows the paper's primary bispectrum-only forecast. (2) The paper explicitly states that the full Fisher inputs are "deferred to a companion artifact." A paper cannot claim a result based on inputs and calculations that are not provided for review. (3) The text notes that the implied unmarginalized sensitivity `σ(f_NL) ≈ 0.114` is "6.1× sharper than the bispectrum-only... baseline" and "sharper than any published SPHEREx SDB forecast known to us." Such an extraordinary claim requires extraordinary evidence, none of which is provided. Presenting this unsubstantiated and anomalously optimistic forecast is unacceptable.
-   **Required Fix:** The authors must choose one of two options:
    1.  **(Recommended)** Remove the entire joint `(f_NL, n_fNL)` analysis and the `~9.9σ` forecast from the manuscript. This includes removing the corresponding discussion from the abstract, the main text (Sec. IX.D), and any other references. This would allow the paper to focus on its well-substantiated primary forecast.
    2.  **(Alternative)** Provide the complete, detailed Fisher matrix calculation within this paper, including all inputs (per-bin `k_min(z)`, `n(z)`, `b_1`, `b_φ`, etc.) and a robust, step-by-step justification for why the resulting sensitivity is over 6 times better than any previously published forecast for this channel.

**P2-E2: Pervasive Review-Process Artifacts and Internal Notes**
-   **Section/Page:** Throughout the manuscript.
-   **Problem Statement:** The manuscript is filled with unprofessional language that appears to be internal notes, comments on previous drafts, or artifacts from a review process. This makes the paper difficult to read and is not appropriate for a formal scientific publication.
-   **Required Fix:** The authors must perform a thorough edit of the entire manuscript to remove all such language and adopt a formal, academic tone. Examples that must be removed include:
    -   p. 2: "the abstract previously gave only the central ~ 2.6σ; the upper-bound of the halved range is reported here for completeness"
    -   p. 7: "A re-derivation of the Heinrich Fisher matrix at the bounce-fiducial is a structural extension on the post-arXiv TODO"
    -   p. 9: "(a rhetorical “>6 × 10^5” figure appeared in an older draft conclusion paragraph; the canonical realization count is 3 × 10^5 across the 3 framework ensembles, and any larger number was an aggregation error)"
    -   p. 11, Table II caption: "Note: prior versions of this caption + the inline 2-row Bayes-factor tabular preceding this caption... reported BF ~ 8... direct scipy.stats.norm recompute... gives BF=9.80... which round to ~ 10 and ~ 4 respectively."
    -   p. 18: "the prior conclusion-paragraph figure “> 6×10^5” was an aggregation error retired in §VI"

### MAJOR

**P2-M1: Inappropriate Content in Abstract**
-   **Section/Page:** Abstract, p. 1
-   **Problem Statement:** The abstract refers to the problematic joint analysis from Sec. IX.D and states that "the specific numerical significance is not quoted here in the abstract until that release lands." An abstract must summarize the work presented and substantiated within the paper itself. It cannot refer to future work or intentionally omit key results that are discussed in the main text.
-   **Required Fix:** This entire sentence must be removed from the abstract. The abstract should be revised to reflect only the well-supported, primary results of the paper (i.e., the bispectrum-only forecast). This is directly related to P2-E1.

**P2-M2: Conversational Prose and Meta-Commentary**
-   **Section/Page:** Throughout, e.g., p. 10
-   **Problem Statement:** The prose often slips into a conversational or tutorial style, addressing the reader directly and commenting on the paper's structure. This is not appropriate for a formal research article. For example: "A reader who only reads this subsection can therefore reproduce the abstract's BF ~ 10–17 envelope from the upper-right column... without integrating across the surrounding paragraphs".
-   **Required Fix:** Revise the manuscript to maintain a formal, objective tone. The text should present the scientific results and their interpretation, not provide instructions on how to read the paper.

**P2-M3: Overloaded Table Captions**
-   **Section/Page:** p. 11 (Table II)
-   **Problem Statement:** The caption for Table II is extremely long and contains a significant amount of analysis, interpretation, and discussion that belongs in the main body of the text. Captions should be concise and describe the content of the table/figure, not replace the main text.
-   **Required Fix:** Move the detailed discussion and interpretation from the caption of Table II into the main text of Section VI. The caption should be shortened to briefly describe what the table shows (e.g., "Bayes factors for the matter bounce vs. multifield inflation under different prior choices...").

### MINOR

**P2-m1: Confusing "Sanity Row" in Table**
-   **Section/Page:** Table III, p. 14
-   **Problem Statement:** The final row of Table III is labeled "Corrected (10% residual; sanity row)" and the caption describes it as a "no-op sanity row." This is unconventional and potentially confusing for the reader.
-   **Required Fix:** It is recommended to remove this row. The point that a 10% residual GR contamination after correction has a negligible impact on the Bayes factor can be stated more clearly and concisely in a single sentence in the main text.

**P2-m2: Non-Standard Formatting of Author Contact**
-   **Section/Page:** p. 2, footnote
-   **Problem Statement:** The corresponding author's email address is provided in a footnote attached to the author's name. This is not standard style for Physical Review D.
-   **Required Fix:** Move the email address to the author affiliation block or an acknowledgments section, in accordance with the journal's style guide.

### NIT

**P2-N1: Paper Length**
-   **Section/Page:** Entire manuscript
-   **Problem Statement:** At 22 pages, the paper is on the longer side for a forecast paper. The length is partly due to the conversational prose and the inclusion of the secondary (and problematic) joint analysis.
-   **Required Fix:** While not a mandatory change, the authors should consider that addressing the points above, particularly removing the joint analysis (P2-E1) and tightening the prose (P2-M2), will naturally shorten the manuscript. A more focused paper of <20 pages would likely be more impactful.

---

## Summary recommendation

**MAJOR REVISIONS**

This manuscript contains a core of high-quality, original research that is a valuable contribution to the field. The detailed audit of the matter-bounce `f_NL` prediction and the first quantification of the template mismatch are significant results. However, the paper is currently unfit for publication due to two major issues: (1) the inclusion of an unsubstantiated and highly speculative secondary forecast that makes an extraordinary claim of a `~9.9σ` detection, and (2) the pervasive and unprofessional inclusion of internal notes and review artifacts throughout the text. These issues undermine the credibility of the otherwise solid work. If the authors thoroughly address all the ESSENTIAL and MAJOR points listed above, particularly by removing the unsubstantiated joint forecast and cleaning up the prose, the revised manuscript would likely be acceptable for publication.