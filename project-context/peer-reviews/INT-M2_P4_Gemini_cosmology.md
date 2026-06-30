# P4 INT-M2 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/private/tmp/P4_m.pdf` md5=c63ae434 pages=24
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 156.8s

---

Referee Report for [Paper ID]

This paper presents a comprehensive analysis of galaxy chirality using a new, large catalog of 8.47 million galaxies from the DESI Legacy Surveys. The authors use a Vision Transformer with a test-time-averaging (TTA) technique to produce a bias-hardened catalog of spiral galaxy handedness. The primary scientific result is a null detection of a real-space chirality dipole, which is used to place constraints on isotropy-breaking physics. The paper also includes an extensive, multi-pronged investigation of potential systematics, most notably a detailed characterization of a "monopole-mask leakage" channel that affects harmonic-space estimators.

The work is methodologically sophisticated and the analysis is exceptionally thorough. The authors' careful distinction between different estimators, null hypotheses, and significance conventions is commendable and sets a high standard for this type of analysis. The public release of the catalog, model, and analysis scripts is also a significant contribution.

However, the paper requires significant revisions before it can be considered for publication in Physical Review D. The primary issues relate to the paper's structure and length, which obscure the main results, and the incomplete state of the data/code archival process.

## Summary of Findings

### ESSENTIAL

**P4-E1: Future Publication Date (Page 1, 22)**
*   **Problem:** The paper is dated "June 28, 2026" on the first page, and the Data Availability section refers to a commit from "June 2026". This is not permissible for a manuscript under review.
*   **Fix:** The date on the title page must be updated to the current submission date. All dates in the manuscript, including in the Data Availability section, must be corrected to reflect the state of the project at the time of submission.

**P4-E2: Incomplete Data/Code Archival (Page 22-23)**
*   **Problem:** The Data Availability section states that an immutable archival snapshot "will be deposited to Zenodo at journal submission; the resulting DOI will be the single citable reproducibility handle for this release." For a paper to be published, this process must be complete. A promise of a future DOI is not sufficient for ensuring long-term reproducibility.
*   **Fix:** The authors must complete the archival process with Zenodo (or a similar permanent repository) and replace the placeholder text with the actual, citable DOI for the full reproducibility package (data, code, artifacts). The commit hash cited should correspond to this final, archived version.

### MAJOR

**P4-M1: Paper Length and Structure (Whole manuscript)**
*   **Problem:** At 24 pages, the paper is excessively long for a null-result publication. The main narrative thread is frequently interrupted by deep dives into the systematics of secondary, diagnostic estimators. In particular, the extensive discussion of the harmonic-channel residuals in the main Results section (IV.C, IV.D) risks confusing the reader about what the primary results are, despite the authors' careful caveats.
*   **Fix:** The paper should be significantly restructured and shortened. The main body should be streamlined to focus on the core results, with a target length of approximately 15 pages. A suggested structure is:
    1.  Introduction.
    2.  Data and Methodology (focusing on the TTA bias-hardening).
    3.  Primary Results:
        a. The null result from the primary real-space dipole estimator.
        b. The exclusion limit from the primary WLS template-fit estimator.
    4.  Summary of Systematics Investigations (briefly describe the main findings, such as the monopole-mask leakage, and state that they support the primary null result).
    5.  Discussion and Conclusions.
    The detailed derivations and analyses of the secondary diagnostics (e.g., the full MASTER power spectrum analysis, the eight-anchor systematic breakdown) should be moved to the appendices. This will create a much clearer and more impactful main paper, while preserving the valuable, detailed work for the interested reader.

**P4-M2: Role of the Harmonic Channel Analysis (Page 9-12)**
*   **Problem:** As a corollary to P4-M1, the current placement and length of the harmonic analysis (Sections IV.C and IV.D) gives it undue prominence. While the analysis is an excellent piece of diagnostic work, it is fundamentally a characterization of a systematic affecting a secondary estimator. Its complexity and detail in the main text detract from the much cleaner and more robust primary real-space results.
*   **Fix:** As part of the restructuring in P4-M1, move the bulk of Sections IV.C and IV.D to an appendix. The main text should simply summarize that harmonic-space estimators were found to be contaminated by a well-characterized monopole-mask leakage systematic, and therefore the primary cosmological conclusions rest on the real-space estimators which are robust to this effect. This makes the logic of the paper's declared analysis hierarchy much easier to follow.

### MINOR

**P4-m1: WLS Template Fit Significance (Page 20)**
*   **Problem:** In Appendix D, the paper presents its primary exclusion result, `z ≈ -18.1`, from a block-bootstrap WLS fit. While the other significance conventions are clearly defined in Section III.A, the construction of this specific `z`-score is not explicitly stated.
*   **Fix:** For completeness, add a brief equation or description in Appendix D defining this statistic, for example, `z = (A_fit - A_ref) / σ_boot`, where `A_fit` is the best-fit dipole amplitude from the WLS regression, `A_ref` is the reference amplitude being tested (1.7%), and `σ_boot` is the standard deviation from the block-bootstrap realizations.

**P4-m2: Table III Transparency (Page 11)**
*   **Problem:** The caption of Table III correctly notes that the permutation null is heavy-tailed and that the `z` statistic and `rank p` value are not expected to follow a simple Gaussian relationship. This is an important physical point.
*   **Fix:** To make this point more explicit and transparent to the reader, the authors should consider adding a column to Table III showing the p-value that would be inferred from the `z` statistic under a Gaussian assumption. This would allow a direct, quantitative comparison with the empirical `rank p` and highlight the non-Gaussianity of the null.

**P4-m3: Footnote 2 Clarity (Page 11)**
*   **Problem:** Footnote 2, which discusses the choice of galaxy counts for the generative null, is dense and somewhat difficult to parse, particularly the final sentence regarding the "per-pixel trial-count inflation factor".
*   **Fix:** Please rephrase this footnote for clarity. Defining the inflation factor with a simple ratio, e.g., `⟨N_all(p)⟩ / ⟨N_spiral(p)⟩_mask`, might improve readability.

### NIT

**P4-N1: Abstract Detail (Page 1)**
*   **Problem:** The abstract includes the sentence: "The +3.64σ value is from a 500-MC direct run...; the 10^4-permutation... row in Table III gives +7.93σ...". This level of detail about different Monte Carlo run sizes for a secondary diagnostic is likely unnecessary for the abstract.
*   **Fix:** Consider streamlining this part of the abstract to simply state that post-MASTER harmonic diagnostics show a significant, systematics-attributed residual, without detailing the different run configurations.

**P4-N2: Acronym Definition (Page 3, 5)**
*   **Problem:** The acronym "LEE" (Look-Elsewhere Effect) is used in Table I and mentioned in Appendix C, but it is not explicitly defined at its first use in the main text or abstract.
*   **Fix:** Define the acronym LEE at its first appearance.

**P4-N3: Citation Format (Page 24)**
*   **Problem:** Reference [39] for `pytorch-image-models` is a URL to a GitHub repository. While this is common, it is not ideal for long-term archival purposes.
*   **Fix:** If possible, please update this citation to a more permanent reference, such as a Zenodo DOI for the specific software version used or a relevant paper.

## Summary recommendation

**MAJOR REVISIONS**

This is a high-quality, thorough, and methodologically important paper. The scientific analysis is sound, and the authors' careful approach to systematics is exemplary. However, the paper in its current form is not yet ready for publication in PRD. The essential issues of the future dating and incomplete archival process must be resolved. Furthermore, the paper's length and structure significantly obscure its primary, important conclusions. A substantial restructuring to streamline the main narrative and move detailed systematic investigations to appendices is required to make the paper more focused and impactful. Once these revisions are made, the paper will represent a very strong and valuable contribution to the field.