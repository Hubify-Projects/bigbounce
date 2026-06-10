# P2 R7 — Physical Review D cosmology-physics referee

**Model**: `gemini-2.5-pro`
**Input format**:  [NATIVE PDF — Gemini sees rendered document]
**Wall time**: 59.6s

---

**Referee Report on "Testing the Matter Bounce with Primordial Non-Gaussianity: SPHEREx Forecasts, with a MegaMapper Outlook"**

**Summary:**
The manuscript "Testing the Matter Bounce with Primordial Non-Gaussianity: SPHEREx Forecasts, with a MegaMapper Outlook" by Houston Golden presents a detailed forecast for testing the matter-bounce cosmological model using upcoming data from the SPHEREx survey. The primary contribution is a comprehensive sensitivity analysis that recasts existing SPHEREx forecasts to the specific non-Gaussianity prediction of the quasi-dust matter bounce (fNL = -35/8). The paper's strengths are numerous: it provides the first quantitative estimate of the template mismatch between the bounce and local bispectrum shapes; it thoroughly investigates a wide range of systematic uncertainties, including theoretical model ambiguities (polynomial null space), observational effects (GR projections, PNG bias), and analysis choices (noise weighting); it performs a robust Bayesian model comparison to quantify the discriminating power against inflationary models; and it resolves a factor-of-two discrepancy in the theoretical literature regarding the predicted fNL value. The author is commendably careful in distinguishing between different analysis channels (bispectrum-only vs. scale-dependent bias) and their respective systematic vulnerabilities, avoiding common pitfalls in forecast literature.

The scientific content is sound, well-motivated, and represents a valuable contribution to the field by providing a clear and testable observational path for a prominent alternative to inflation. However, the manuscript contains several editing artifacts, including explicit text from a previous peer-review cycle, which must be removed before publication. The paper is also quite dense and could benefit from minor improvements in presentation for clarity.

---
**Findings:**

**ESSENTIAL**

*   **P2-E1:** **Section: Appendix A (p. 18)**
    *   **Problem:** The manuscript contains a verbatim artifact from a peer-review system. The text reads: "...to address the cross-model peer-review concern (R42 Gemini 3.1-Pro P2 BLOCKER B-3) that the missing time-ordering...".
    *   **Fix:** This text must be removed entirely. The sentence should be rephrased to state the scientific motivation for the clarification without referencing an internal review process. For example: "We separate them explicitly here to clarify that the missing time-ordering should not be misinterpreted as a normalization choice."

**MINOR**

*   **P2-M1:** **Section: III.B (p. 7)**
    *   **Problem:** The text includes what appears to be a raw filename from the analysis code: "...the per-realization spread from phase3_fisher_overlap.json is wider...". This is unprofessional and not reproducible without the file itself.
    *   **Fix:** Remove the filename. The sentence can simply state that the per-realization spread is wider, or describe the source of the spread (e.g., "the spread from the full Monte Carlo Fisher analysis...") without naming the specific output file.

*   **P2-M2:** **Section: Data and Code Availability (p. 18)**
    *   **Problem:** The description of the code repository uses informal language more suited for a commit message than a formal publication: "...(pinned to release tag paper2-v1.7.40)".
    *   **Fix:** Rephrase for a formal publication. For example: "The version of the code used to produce the results in this paper is archived under the release tag v1.7.40." A reference to a permanent archive like Zenodo would be even better.

*   **P2-M3:** **Section: Table III Caption (p. 14)**
    *   **Problem:** The caption uses the informal term "sanity row" to describe the final row of the table.
    *   **Fix:** Replace "sanity row" with more formal language, such as "a row for verification" or "a row demonstrating a null-effect test". The current text "no-op sanity row" could be rephrased to "a verification row demonstrating a null effect".

*   **P2-M4:** **Section: Abstract (p. 1)**
    *   **Problem:** The abstract is extremely dense and packed with numerical results and parenthetical clauses, which can hinder readability for a reader trying to get a quick overview of the paper's contribution.
    *   **Fix:** Consider streamlining the abstract. For example, some of the detailed numerical ranges or secondary validations could be omitted in favor of a clearer narrative flow focusing on the main result (the 3–5σ forecast) and its key dependencies (template mismatch, systematics). This is a suggestion for improvement; the current abstract is factually correct.

*   **P2-M5:** **Section: IX.D (p. 16)**
    *   **Problem:** The section correctly and carefully distinguishes the SDB-based joint forecast from the headline bispectrum-only forecast. However, the prose is very long and convoluted, particularly the sentence beginning "Note specifically: the implied σunmarg(fNL)...". This makes a crucial point difficult to parse.
    *   **Fix:** Break the long sentences in this paragraph into shorter, more direct statements to improve clarity. The author's care in making this distinction is a major strength of the paper, and improving the presentation will help ensure the point is not lost on the reader.

**NIT**

*   **P2-N1:** **Section: I (p. 2)**
    *   **Problem:** The notation for the four-fermion operator appears in several forms, e.g., `(Ψγγαψ)2` and `⟨ψ̄γ 5 γ a ψ⟩2`. This appears inconsistent and potentially contains typos.
    *   **Fix:** Please check and standardize the notation for the four-fermion operator throughout the manuscript to ensure it is correct and consistent.

*   **P2-N2:** **Section: Appendix A.1 (p. 19)**
    *   **Problem:** In the expression following Eq. (A5), `ζ(η∗ , kσ(1) ) Φv,1 (η) ...`, the terms appear to represent two-point functions but are missing the angle brackets `⟨...⟩` used elsewhere to denote expectation values.
    *   **Fix:** Add angle brackets to each two-point function for notational consistency, e.g., `⟨ζ(η∗, kσ(1)) Φv,1(η)⟩...`.

---
## Summary recommendation
**MINOR REVISIONS**

The paper presents a thorough, high-quality, and timely forecast for testing the matter-bounce scenario with SPHEREx. The scientific analysis is careful, robust, and transparent about its assumptions and limitations. The author has done an excellent job of navigating complex theoretical and systematic issues, and the resulting forecast is well-grounded. The primary reason for the "Minor Revisions" recommendation, rather than "Accept with Minor Corrections," is the presence of an explicit peer-review artifact in the appendix (P2-E1). This indicates a significant oversight in manuscript preparation that must be rectified. The other required changes are minor but, taken together, warrant a careful revision by the author to ensure the final manuscript meets the publication standards of Physical Review D. I am confident that the author can address these points and expect the revised manuscript to be suitable for publication.