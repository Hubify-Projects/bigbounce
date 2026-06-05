# P4 2026-06-04_R4fixed — Physical Review D cosmology-physics referee

**Model**: `gemini-2.5-pro`
**Input format**:  [NATIVE PDF — Gemini sees rendered document]
**Wall time**: 83.0s

---

**Referee Report for P4**

This paper presents a detailed analysis of galaxy chirality using a large catalog of 3.2 million spiral galaxies from the DESI Legacy Surveys. The primary scientific result is a null detection of a large-scale angular dipole (`l=1`) in the galaxy chirality field, consistent with statistical isotropy. The analysis is exceptionally thorough, featuring a sophisticated, equivariance-corrected machine learning pipeline for classification and a multi-pronged approach to identifying and mitigating systematic effects. The paper also presents a detailed characterization of a `+3.64σ` residual signal on a specific survey mask, providing strong evidence that this is a systematic effect correlated with survey depth and galaxy morphology, rather than a primordial cosmological signal.

While the underlying analysis is of high quality and the main conclusions appear robust, the manuscript in its current form is not suitable for publication in Physical Review D. It suffers from several critical issues related to length, structure, and presentation that must be addressed.

## Findings

### ESSENTIAL

**P4-E1: Removal of Internal Artifacts and Jargon**
-   **Location:** Throughout the manuscript (e.g., p. 5, 9, 11, 21, 35, 38, 49, 52).
-   **Problem:** The paper is replete with internal file paths (e.g., `pipelines/p2_chirality/outputs/...`), references to specific code runs, version tags (`paper4-v1.0.154`), and internal jargon ("companion artifact", "re-audit on the pod"). This is entirely inappropriate for a peer-reviewed publication and makes the paper read like an internal technical note. It severely compromises the professionalism and readability of the work.
-   **Required Fix:** All such internal references must be systematically removed from the manuscript body, tables, and footnotes. The reproducibility information should be centralized in the Data Availability section (Sec. IX). A single, immutable release tag for the code and data repository should be cited there, from which all scripts, data, and output files can be accessed. The term "companion artifact" should be replaced with standard phrasing like "The corresponding data product is available in the data release."

**P4-E2: Excessive Length and Unsuitable Structure**
-   **Location:** Entire manuscript.
-   **Problem:** At 56 pages, the paper is excessively long for a journal article, particularly for one whose main result is a null detection. The extreme level of detail, while valuable, obscures the key scientific takeaways. The current structure mixes primary results, systematic checks, and deep-dive diagnostics in a way that is difficult for the reader to navigate.
-   **Required Fix:** The paper must be substantially shortened and restructured. I recommend a main article of no more than 20 pages, with the remaining material moved to appendices or supplementary online material.
    -   The **main article** should focus on presenting the core scientific argument: Introduction, a concise summary of the data and the essential methods (TTA, MASTER), the key results (the `-0.12σ` null dipole, the `+3.64σ` systematic residual, and a summary of the evidence for its nature), a focused discussion on the physical implications, and the conclusions.
    -   The **appendices/supplementary material** should contain the exhaustive details necessary for expert-level reproducibility: the full bias-hardening suite, the detailed multi-null battery analysis, large tables (e.g., Table XI), the NaMaster configuration details, and the narrative of exploratory steps (like the `D4-TTA` argmax-statistic retraction).

### MAJOR

**P4-M1: Clarity, Readability, and Narrative Style**
-   **Location:** Throughout, especially Sec. III.E (p. 11), IV.D (p. 22-23), and VI.A (p. 35).
-   **Problem:** The prose is often convoluted and follows a "stream-of-consciousness" style that narrates the author's research journey, including intermediate steps and retractions (e.g., the `D4-TTA` argmax-fraction claim). A scientific paper should present the final, distilled logic and results, not a log of the analysis process. This makes critical sections, like the assessment of the canonical-mask residual, extremely difficult to follow.
-   **Required Fix:** The author must perform a comprehensive revision of the manuscript to improve clarity and conciseness. The paper should be rewritten from the perspective of presenting a finished analysis. Sections that describe a winding path to a conclusion should be replaced with a clear, logical argument that leads directly to the final result.

**P4-M2: Theoretical Scoping and Parity-Symmetry Discussion**
-   **Location:** Sec. VI.G (p. 43).
-   **Problem:** The paper correctly and importantly distinguishes the parity-EVEN nature of the dipole (`l=1`) observable (an isotropy test) from the parity-ODD nature of the monopole (`l=0`) observable (a parity test). This is a highlight of the paper. However, the connection to fundamental theory could be made more explicit for the target audience.
-   **Required Fix:** While correctly stating that a transfer function is not derived, the author should briefly elaborate on the key physical steps required to build one. This would involve explicitly mentioning the chain from a primordial parity-violating source (e.g., chiral gravitational waves) to the large-scale tidal field, the tidal-torque theory response of halo angular momentum, and the galaxy formation physics that links halo spin to the observed projected spiral arm winding. This would better frame the excellent observational work for theorists seeking to constrain models.

**P4-M3: Removal of Manuscript Version History**
-   **Location:** e.g., p. 6 ("fixed at v1.0.76 of this manuscript"), p. 18 ("the older snapshot value 2.75σ predates..."), p. 45.
-   **Problem:** The text contains references to previous versions of the manuscript or analysis. This is irrelevant to the reader and inappropriate for a final publication.
-   **Required Fix:** Remove all such historical references. The paper should stand as the definitive report of the final analysis.

**P4-M4: Typographical Errors and Duplicate Phrases**
-   **Location:** e.g., p. 21 ("pseudo-C(l=1) pseudo-C(l=1) power"), p. 42 ("mask-definition mask-definition robustness question").
-   **Problem:** The manuscript contains several instances of duplicated words and other typographical errors, suggesting a need for a thorough proofread.
-   **Required Fix:** The author must carefully proofread the entire manuscript to correct these errors.

### MINOR

**P4-m1: Defensive Phrasing**
-   **Location:** p. 3.
-   **Problem:** The text contains defensive phrasing, such as "we refrain from claiming the audit suite is 'the most extensive' without a literature survey...".
-   **Required Fix:** Remove such phrases. The description of the methods should be confident and stand on its own merits.

**P4-m2: Notes for Publication Process**
-   **Location:** p. 50.
-   **Problem:** The Data Availability section includes a note about a future action: "a Zenodo mirror with a minted DOI will be linked... at arXiv submission time."
-   **Required Fix:** This note should be removed. The final version should either contain the link or state that the data is available at the primary cited location.

### NIT

**P4-N1: Title Length**
-   **Location:** p. 1.
-   **Problem:** The title is exceptionally long and detailed, functioning as a mini-abstract.
-   **Suggested Fix:** The author should consider a more concise title that captures the main result, for example: "A Null Search for a Cosmological Chirality Dipole in 3.2 Million DESI Legacy Spiral Galaxies". The details of the systematic channels and residuals are better placed in the abstract.

## Summary recommendation

**MAJOR REVISIONS**

The paper presents an impressively thorough and statistically rigorous search for a galaxy chirality dipole. The null result is a significant contribution to the field, and the detailed investigation of systematic effects is a model for how such analyses should be conducted. The clear distinction between parity-even (isotropy-breaking) and parity-odd observables is a major strength. However, the manuscript is not in a form suitable for publication. It is critically undermined by its excessive length and a presentation style more suited to an internal technical document than a peer-reviewed journal article, with numerous internal file paths and a narrative that documents the research process rather than its final outcomes. The work is strong, but it requires a fundamental restructuring and a substantial rewrite to meet the standards of clarity, conciseness, and professionalism expected by Physical Review D. If the author is willing to undertake these major revisions, the resulting paper will be a valuable and impactful publication.