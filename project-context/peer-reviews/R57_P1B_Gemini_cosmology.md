# P1B R57 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/private/tmp/R57_P1B/paper1b_mcmc_companion.pdf` md5=653da036 pages=22
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 208.8s

---

## Referee Report for "Technical Verification Companion to the ECH Spin-Torsion Program..."

**Report ID:** P1B-R57

This paper presents three technical analyses intended as a companion to a separate work on Einstein-Cartan-Holst (ECH) spin-torsion cosmology. The analyses are: (1) a stock-CAMB MCMC analysis of the ΛCDM+ΔNeff model as a proxy for new radiation-like physics, (2) a validation of a NaMaster-based pipeline for measuring cosmic birefringence, and (3) a consistency check of the observed birefringence signal with a spectator axion-like particle (ALP) model.

The technical execution of the individual analyses appears to be rigorous and sound. The author is commendably transparent about the scope, limitations, and potential systematics of each analysis. The detailed reproducibility materials are a significant strength. However, the paper suffers from several major structural and presentational issues that must be addressed before it can be considered for publication in Physical Review D.

### ESSENTIAL Revisions

*   **P1B-E1:** Section: Abstract & Title Page, Page: 1
    *   **Problem:** The paper is dated "June 26, 2026". This is a future date and an obvious placeholder artifact.
    *   **Fix:** The date must be corrected to the actual date of submission or revision.

### MAJOR Revisions

*   **P1B-M1:** Section: All, Page: 1-22
    *   **Problem:** The paper is not self-contained, relying heavily on "Paper I(a) [1]" for its core motivation and physical context. A reader without access to the companion paper cannot fully understand the "why" behind these analyses. The introduction, in particular, fails to provide the necessary background on the ECH framework and the specific questions these technical verifications are meant to answer.
    *   **Fix:** The Introduction (Section I) must be significantly expanded to provide a self-contained summary of the relevant physics from Paper I(a). This should include a concise overview of the ECH model, why ΔNeff is a relevant proxy, the origin of the birefringence signal in the broader context, and what specific claims in the main paper these analyses are designed to support. The paper must be readable and its purpose understandable as a standalone article.

*   **P1B-M2:** Section: III, IV, V, Page: 3-12
    *   **Problem:** The overall structure of the paper is confusing. The discussion of the different MCMC analyses (the ΔNeff proxy and the `wowa` chain) are intermingled throughout the text, making the narrative difficult to follow. For example, discussion of the `wowa` chain from Table II appears in sections ostensibly dedicated to the ΔNeff analysis of Table I.
    *   **Fix:** The paper must be restructured to clearly separate the three distinct analyses. A recommended structure would be:
        1.  Introduction
        2.  Analysis 1: ΛCDM+ΔNeff MCMC Proxy (combining methods, results from Table I, and discussion)
        3.  Analysis 2: NaMaster Pipeline Validation (methods, results, discussion)
        4.  Analysis 3: Spectator ALP Consistency Check (methods, results, discussion)
        5.  Overall Conclusions
        This will prevent the reader from having to jump between different conceptual threads.

*   **P1B-M3:** Section: Abstract, Page: 1
    *   **Problem:** The abstract states that the "spectator-safe (Ω_a < 0.01) subset is tuned". While correct, this significantly understates the severity of the tuning found in the main analysis. The body of the paper (p. 12, footnote 6 on p. 13) quantifies this as a `~25x` to `~100x` fine-tuning of the initial misalignment angle.
    *   **Fix:** To accurately reflect the findings, the abstract must include this quantitative measure of fine-tuning (e.g., "requires a ~25x fine-tuning of the initial misalignment angle"). This is a key result of the ALP analysis and is crucial for the reader's interpretation.

### MINOR Revisions

*   **P1B-m1:** Section: IV, Page: 4
    *   **Problem:** The text states: "...the ~20% shared-event Malmquist-correction issue is discussed as a stated caveat in caveat (e) and Sec. III". The relevant discussion of caveat (e) appears on page 5, which is part of the discussion following the results in Section III, but the main caveat is defined and discussed in the context of the `wowa` chain, whose results are in Section V/Table II. This cross-referencing is confusing due to the structural issues noted in P1B-M2.
    *   **Fix:** Correct the section reference. After restructuring, ensure all cross-references point to the correct new sections.

*   **P1B-m2:** Section: Appendix B & Table V, Page: 19-20
    *   **Problem:** The "Claims Classification" appendix and table are highly non-standard for a journal article and read like internal project management or audit material. While the transparency is laudable, it is not in the conventional format of a physics paper.
    *   **Fix:** Move Appendix B and Table V to a separate supplementary material file. This preserves the information for reproducibility auditors while improving the flow and format of the main paper.

*   **P1B-m3:** Section: III (Footnote 1) & IV (Footnote 4), Page: 3 & 10
    *   **Problem:** Footnotes 1 and 4 are extremely long and dense, containing detailed reconciliations of sample counts and derived SNR figures. This level of detail, while valuable for reproducibility, disrupts the flow of the main text.
    *   **Fix:** Condense these footnotes to their essential conclusions and move the full, detailed derivations to a new appendix on numerical reconciliation.

*   **P1B-m4:** Section: VII, Page: 17
    *   **Problem:** A paragraph beginning "wowa cross-check.—" appears after Table IV and before the Data and Code Availability section. This seems to be a misplaced summary paragraph that should be integrated into the main conclusions.
    *   **Fix:** Integrate this paragraph into the main Conclusion section (Section VII).

### NITs (Nitpicks)

*   **P1B-N1:** Section: IV, Figure 3 Caption, Page: 9
    *   **Problem:** The caption notes that for the canonical `fsky=0.32` point in panel (b), the per-realization scatter `σβ` was not recorded in the original run and had to be measured in a dedicated rerun.
    *   **Fix:** For the final version, it would be cleaner to simply run the full analysis suite consistently so that such notes are not necessary. As it is explained, it is acceptable, but it suggests a slightly disorganized analysis workflow.

## Summary recommendation

**MAJOR REVISIONS**

The paper contains three well-executed and transparently reported technical analyses that could be of value to the community. The author's commitment to reproducibility and clear scoping of the claims is commendable. However, the paper in its current form does not meet the standards for a standalone publication in Physical Review D due to major structural problems, a lack of self-containment, and a failure to adequately quantify a key result (the ALP fine-tuning) in the abstract. The paper reads more like a collection of internal technical notes than a coherent, self-contained scientific article. The required revisions are substantial but primarily editorial and structural. If the author undertakes a significant restructuring to address the issues outlined above, the paper could become a solid and publishable contribution.