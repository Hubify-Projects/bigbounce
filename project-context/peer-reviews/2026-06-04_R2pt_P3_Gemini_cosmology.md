# P3 2026-06-04_R2pt — Physical Review D cosmology-physics referee

**Model**: `gemini-2.5-pro`
**Input format**:  [NATIVE PDF — Gemini sees rendered document]
**Wall time**: 80.2s

---

**Referee Report on "Spectrally Unusual Sources at Scale..."**

**Paper:** P3
**Round:** 2026-06-04_R2pt

This paper presents a large catalog of anomalous astronomical sources identified using an autoencoder framework across seven major surveys. The primary scientific application discussed is the use of these sources as a new population of high-bias tracers to improve cosmological constraints on the local non-Gaussianity parameter, fNL. A secondary application testing the consistency of a specific matter-bounce model prediction with pulsar timing array (PTA) data is also presented.

The paper represents a substantial amount of computational and analytical work. The development of the "Path-C" analysis pipeline, including per-survey native retraining and a suite of validation tests, is extensive. The cosmological analysis, particularly the empirical measurement of the tracer bias enhancement and the careful treatment of uncertainties in the Fisher forecast, is a valuable contribution.

However, the manuscript in its current form has severe structural and stylistic problems that make it unsuitable for publication. It is written more like an internal technical report or a research log than a scientific paper for a peer-reviewed journal. The narrative is dominated by a chronological account of the analysis development, including superseded methods, retracted results, and internal audit trails. This makes the paper excessively long and difficult to follow. The core scientific results are buried under a mountain of procedural detail.

Major revisions are required to restructure the paper into a coherent scientific article focused on its key findings.

---
### ESSENTIAL Revisions

**E1. Paper Structure and Length (ESSENTIAL)**
-   **Section:** Entire manuscript
-   **Problem:** At 50 pages, the paper is excessively long for a PRD methods/catalog paper. The length is a symptom of a larger structural issue: the paper is written as a "developer's diary" that documents the entire research process, rather than a focused presentation of the final, validated results. It details every methodological dead-end, correction, and internal check.
-   **Fix:** The paper must be fundamentally restructured. I recommend the following:
    1.  **Main Paper (target length 15-20 pages):** Focus on the cosmological results, which are the most relevant for a PRD audience.
        -   Briefly introduce the anomaly detection method and summarize the final catalog's properties.
        -   Describe the selection of the QSO-candidate tracer sample.
        -   The current Section V ("Cosmological Applications") should become the core of the paper, presenting the fNL forecast and the PTA consistency check.
        -   Provide a concise Discussion and Conclusion summarizing the scientific takeaways.
    2.  **Appendices:** Move the extensive methodological and catalog details to appendices. This includes the detailed description of the "Path-C" pipeline, per-survey results, the image galleries (Figs. 13-22), and detailed MCMC documentation. This restructuring will make the primary scientific contribution clear and accessible.

**E2. Removal of Internal Language and Version History (ESSENTIAL)**
-   **Section:** Entire manuscript, especially Abstract, Sec. V, and Sec. VI D.
-   **Problem:** The manuscript is replete with unprofessional language that is inappropriate for a scientific publication. This includes version control statements, references to internal review processes, and project-specific jargon.
    -   Examples: "The prior linear-extrapolation σ(fNL) = 8.27 ± 2.37 is RETRACTED" (Abstract, p. 2); "[Cross-transfer baseline map — superseded by Path-C native counts.]" (Fig. 3 caption); "that figure is retracted here per R5 Gemini-M3" (p. 25); "Wave 14-VVV", "Wave 14-KKKK" (p. 2-3); the entirety of Sec. VI D ("Path-C Rebuild Residual Caveats"), which reads like a closed-issue list from a bug tracker (e.g., "Multi-round-deferred item resolved... this deferral is closed.").
-   **Fix:** All such language must be systematically removed from the paper.
    -   Replace jargon like "Wave 14-VVV" with descriptive phrases (e.g., "the empirical bias measurement from the full QSO-candidate sample").
    -   Present only the final, correct results. If a previously reported value is being corrected, it should be done in a formal, professional manner (e.g., "This result supersedes a preliminary estimate based on a linear approximation, which we found to be invalid...").
    -   The entire Sec. VI D must be removed. Any scientifically relevant information from it (e.g., the final resolution of the deduplication arithmetic) should be integrated smoothly into the appropriate sections of the main text (e.g., Sec. IV C).

**E3. Abstract Revision (ESSENTIAL)**
-   **Section:** Abstract (p. 1-2)
-   **Problem:** The abstract is extremely long, dense with un-defined jargon, and focuses excessively on the internal process of the analysis. It is nearly incomprehensible to a reader not already familiar with the project. It reads like a summary of the internal technical report, not a concise summary of the scientific findings for a general audience.
-   **Fix:** The abstract must be completely rewritten. It should be a single, concise paragraph that:
    1.  Briefly introduces the new catalog of anomalous sources.
    2.  States the main cosmological application (constraining fNL with a new tracer sample).
    3.  Summarizes the key quantitative result (e.g., the central forecast for σ(fNL) and its uncertainty envelope).
    4.  Briefly mentions the secondary PTA consistency check.
    All procedural details (e.g., "Recommended primary number...", specific gate pass/fail statistics, names of internal protocols like "Path-C") must be removed.

---
### MAJOR Revisions

**M1. Reframing the Analysis Narrative (MAJOR)**
-   **Section:** Throughout, especially Sec. III and IV.
-   **Problem:** The paper is built around a confusing "cross-transfer baseline vs. Path-C native retrain" comparison. The "cross-transfer" method is presented as a baseline but is shown to have critical failures (e.g., the 98% contamination for LAMOST). This is part of the development process, not a final scientific result. Presenting these failed results alongside the final ones throughout the main text confuses the narrative.
-   **Fix:** The paper's narrative should be streamlined to focus on the final, validated "native retrain" methodology. The cross-transfer method should be mentioned only briefly in the Methods section as a simpler, preliminary approach whose diagnostic failures motivated the development of the more robust final pipeline. All tables and figures presenting "superseded" cross-transfer results as a main result (e.g., Figs. 3, 6; the cross-transfer counts in Table I) should be removed from the main text. They can be moved to an appendix on methodology development if the authors feel they are essential for demonstrating the robustness of the final method.

**M2. Clarifying the Scope of Cosmological Claims (MAJOR)**
-   **Section:** Sec. V, Sec. VI F, Abstract, Conclusion.
-   **Problem:** The paper connects its results to "Bounce Cosmology". However, the analyses performed (both for fNL and PTA) test predictions of a very specific model: a scalar-only, matter-dominated (w=0) bounce. While the text is often careful to state this, titles like "Implications for Bounce Cosmology" and broader summary statements could lead readers to over-interpret the results as applying to the entire bounce paradigm.
-   **Fix:** The authors should ensure the language is consistently precise throughout the manuscript. Titles, abstract, and conclusion statements should be carefully worded to reflect that the results provide a consistency check for a *specific class* of matter-bounce models, and do not validate or constrain the broader framework. For instance, "Implications for a Class of Matter-Bounce Models" would be more accurate.

---
### MINOR Revisions

**m1. Removal of Internal File Paths (MINOR)**
-   **Section:** Throughout (e.g., p. 6, 21, 25).
-   **Problem:** The text contains numerous direct references to internal file paths and "companion artifacts" (e.g., `pipelines/p3_anomaly_engine/.../results.json`).
-   **Fix:** All such paths must be removed. The paper should include a standard Data Availability Statement that directs readers to a single public data repository (e.g., a Zenodo archive or GitHub repository) where all supporting data, code, and "artifacts" are available and properly documented.

**m2. Consistency in Quoting Statistical Significance (MINOR)**
-   **Section:** Throughout.
-   **Problem:** The paper deals with statistical significance (σ) derived from various sources (Fisher matrices, jackknife resampling, MCMC posteriors). While generally handled well, the high density of such numbers warrants a careful final check.
-   **Fix:** The authors should perform a final pass to ensure that no σ values from different statistical procedures are ever directly compared or presented as if they are on the same scale without explicit qualification. The current practice of stating the context (e.g., "consistent with zero at 0.29σ from null") is good and should be applied universally.

---
### NITs (Typos, etc.)

**n1. Future Date (NIT)**
-   **Section:** Title block (p. 1).
-   **Problem:** The date of the paper is listed as "June 4, 2026".
-   **Fix:** Correct this to the actual date of submission.

**n2. Overly Detailed Captions (NIT)**
-   **Section:** e.g., Table I caption.
-   **Problem:** Some captions, particularly the multi-paragraph caption for Table I, contain extensive explanations and footnotes that would be better placed in the main text.
-   **Fix:** Streamline captions to be concise descriptions of the table/figure content. Move discursive or methodological details into the main body of the paper.

---
## Summary recommendation

**MAJOR REVISIONS**

The paper contains a scientifically valuable dataset and a set of interesting cosmological analyses. The authors have clearly performed a tremendous amount of careful work, including rigorous self-auditing of their methods and results (e.g., the correction of the Fisher forecast uncertainty and the proper GR effect treatment). However, the manuscript is not written as a scientific paper but as a technical document chronicling the research process. The excessive length, the inclusion of superseded results, and the pervasive use of internal jargon and audit-trail language make it unacceptable for publication in its current form. The authors must undertake a fundamental restructuring and rewrite to focus the paper on its key scientific conclusions, moving the vast procedural and cataloging details to appendices. Given the potential value of the results, I recommend major revisions to give the authors an opportunity to address these deep structural issues. If a complete rewrite is not performed, the paper should be rejected.