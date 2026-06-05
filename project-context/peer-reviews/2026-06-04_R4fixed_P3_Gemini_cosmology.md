# P3 2026-06-04_R4fixed — Physical Review D cosmology-physics referee

**Model**: `gemini-2.5-pro`
**Input format**:  [NATIVE PDF — Gemini sees rendered document]
**Wall time**: 72.5s

---

**Referee Report: P3-R4fixed**

This paper presents a large and comprehensive catalog of astronomical anomalies detected using an autoencoder framework across seven different surveys. The work is ambitious in scope, combining a significant data-processing effort with applications to both observational astronomy (novel object discovery) and fundamental cosmology (constraints on primordial non-Gaussianity and consistency checks of bounce cosmology). The scientific methodology, particularly in the cosmological analyses, is sophisticated and demonstrates a careful handling of statistical and theoretical subtleties.

However, the paper in its current form is not suitable for publication in Physical Review D. The primary issues are its excessive length and a highly unconventional structure and writing style that obscure the scientific results. The manuscript reads more like an internal technical report or a direct response to previous referee comments than a standalone scientific paper. While the underlying work is of high quality, a complete and substantial revision is required to meet the standards of the journal.

---

**Detailed Findings**

**ESSENTIAL**

*   **P3-E1: Paper Structure and Non-Standard Prose (Throughout, esp. Sec. VI D)**
    *   **Problem:** The paper is replete with internal-review artifacts, file paths, and language that breaks the flow of a scientific narrative. Section VI D, "Path-C Rebuild Residual Caveats," is the most prominent example. This section is formatted as a list of resolved issues, complete with references to specific fixes (e.g., "Headline value now in §II," "The caveat is closed"). This is not appropriate for a published paper. The transparency is commendable, but the execution makes the paper unreadable and unprofessional. Similar artifacts, such as direct paths to code artifacts (e.g., "Companion artifact: fw6_stability/fw6_stability_results.json." on p. 11), are scattered throughout the text.
    *   **Fix:** The entire paper must be rewritten into a coherent scientific narrative. Section VI D must be eliminated. Its content, where relevant, should be integrated smoothly into the appropriate sections of the main text. For example, the discussion of the "378,280 dedup arithmetic" belongs in Section IV C where deduplication is discussed. The Fisher information positivity discussion belongs in Section V where the Fisher forecast is presented. All file paths, code repository links (except in a formal Data Availability statement), and meta-commentary on the paper's own revision history must be removed from the main prose.

*   **P3-E2: Excessive Length and Lack of Focus (Throughout)**
    *   **Problem:** At 49 pages, the paper is far too long for its primary contributions. The main text (33 pages) is bogged down by excessive detail that could be moved to appendices or supplementary material. For instance, the survey-by-survey breakdown in Section III is exhaustive but prevents the reader from focusing on the high-level results. The narrative thread is frequently lost in a sea of numbers, cross-references, and footnotes.
    *   **Fix:** The paper must be substantially shortened. I recommend a target of 15-20 pages for the main text, in line with a typical PRD article.
        *   Condense Section III significantly. Present a high-level summary of the results for each survey in the main text and move the detailed descriptions and classifications to an appendix.
        *   Streamline the presentation of the cosmological results in Section V. The core results are the empirical `α` measurement and the resulting `σ(fNL)` forecast. The detailed discussion of the Fisher formalism's failure points and corrections, while excellent, can be presented more concisely.
        *   Move all image galleries (Figs. 13-22) to appendices, as is standard practice.

**MAJOR**

*   **P3-M1: Use of Jargon (Throughout)**
    *   **Problem:** The paper relies heavily on project-specific jargon, most notably "Path-C," which even appears in the title. While defined, its constant use makes the paper opaque to outside readers. Terms like "gate PASS," "gate-FAIL-with-rigorous-diagnostic," and "Path-B re-measurement" are internal shorthand that hinder readability.
    *   **Fix:** Replace jargon with more descriptive language. For example, instead of "Path-C rebuild," use "the revised analysis with native-trained models." Instead of "gate PASS," simply state that the model "passed the pre-defined validation threshold (validation loss ≤ 0.30)." The title should be revised to be more broadly accessible.

*   **P3-M2: Data Availability Section (p. 33)**
    *   **Problem:** The "Data availability" section is a mix of a standard availability statement, a file manifest for the data release, and instructions to the consumer on which files to use (e.g., "...must not be used for the headline aggregate..."). This level of detail is inappropriate for the main text of the paper.
    *   **Fix:** Rewrite the Data Availability statement to be a concise paragraph pointing to the public repository where the data and a detailed README file can be found. The manifest of files and user instructions should be part of the data repository's documentation, not the paper itself.

**MINOR**

*   **P3-m1: Future Date (p. 1)**
    *   **Problem:** The paper is dated "June 4, 2026."
    *   **Fix:** Correct the date to the current submission date.

*   **P3-m2: Theoretical Scoping of fNL Forecast (Sec. V)**
    *   **Problem:** The paper correctly notes that the `fNL` forecast assumes zero observational systematics and omits GR projection effects in its primary derivation. While the GR effects are later shown to be small in Sec. VI D, the zero-systematics assumption is a major limitation that should be emphasized more strongly alongside the headline forecast.
    *   **Fix:** In Section V, when presenting the final `σ(fNL)` numbers, add a sentence immediately after to reiterate that this is a statistical-only forecast and does not include the (likely significant) impact of observational systematics.

**NIT**

*   **P3-N1: Footnote Density (Throughout)**
    *   **Problem:** The paper uses an extremely high number of footnotes, particularly in Table I. While the information is useful, it contributes to the cluttered and difficult reading experience.
    *   **Fix:** Consider integrating the most critical footnote information into the main text or table captions. Less critical details could be moved to an appendix.

---

## Summary recommendation

**MAJOR REVISIONS**

The scientific content of this paper is of high quality. The anomaly detection campaign is impressive in scale, and the methodological lessons learned are valuable for the community. The cosmological applications are particularly well-executed, showing a sophisticated understanding of the theoretical and statistical challenges, especially regarding the multi-tracer Fisher forecast and the physical scope of the bounce cosmology model.

However, the manuscript is not a publishable scientific paper in its current form. It is structured and written like a technical document, burdened by excessive length, internal jargon, and artifacts from the review process. The core scientific results are buried and difficult for a reader to extract. A complete restructuring and rewrite are necessary to bring the paper to the publication standard of Physical Review D. Given the high quality of the underlying science, I recommend that the author be given the opportunity to perform these substantial revisions.