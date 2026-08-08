# P4 INT-P4v195 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/private/tmp/P4_v195.pdf` md5=87d3eb2c pages=24
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 130.3s

---

## Referee Report: Survey-Scale Galaxy Chirality with Equivariant TTA

This paper presents a comprehensive analysis of galaxy chirality using a new, large catalog of 8.47 million galaxies from the DESI Legacy Surveys, of which 3.2 million are classified as spirals. The primary scientific result is a null detection of a real-space chirality dipole, constrained at the sub-percent level. The main methodological contributions are the use of a flip-equivariant Vision Transformer pipeline to mitigate classifier bias and the detailed characterization of a "monopole-mask leakage" systematic. The paper is exceptionally thorough in its treatment of systematics and robust in its conclusions. The analysis is of high quality and suitable for publication in Physical Review D, pending revisions to address the issues outlined below.

### ESSENTIAL

*   **P4-E1:** Section: Abstract & Data Availability (Page 1 & 23)
    *   **Problem:** The paper is dated "June 28, 2026", and the data release tag is "v2026.04". These are future dates and appear to be placeholders. This is not permissible in a final submission.
    *   **Fix:** Replace the placeholder dates with the correct date of submission. Update the release tag to match the version of the data and code used for the submitted manuscript.

### MAJOR

*   **P4-M1:** Section: General Structure (Whole Paper)
    *   **Problem:** The paper is 24 pages long. While the appendices contain essential details for reproducibility and rigor, the main text (pages 1-16) is dense and could be streamlined for clarity and impact. The core result is a carefully established null detection and a methodological advance; the narrative flow is sometimes lost in the detailed enumeration of multiple, closely related systematic checks within the main body.
    *   **Fix:** Restructure the paper to shorten the main text to approximately 15 pages. Move some of the more detailed discussions of secondary diagnostics and robustness checks from the main Results section (e.g., the blow-by-blow of the confidence-cut sweep in Sec. IV.C, the detailed breakdown of the MASTER weight-map sweep in Sec. IV.C.b) to the appropriate appendices. The main text should focus on the primary result (the HC real-space dipole), the primary exclusion (the WLS template fit), the key methodological finding (equivariant TTA's effect), and the primary systematic model (monopole-mask leakage), directing the reader to the appendices for the exhaustive supporting evidence.

*   **P4-M2:** Section: IV.C (Angular power spectrum) & Table III (Page 9 & 11)
    *   **Problem:** There is a potential for confusion regarding the various `l=1` significance values from the harmonic analysis. The main text (Sec IV.C.b, page 9) quotes a primary MASTER result of `+7.28σ` from a 500-MC null run. Table III (page 11), which is presented as the main tabulation of MASTER results, reports `+7.31σ` for the `l=1` mode on the apodized footprint from a 10^4-permutation null. The caption of Table III notes that the `+7.28σ` value is a "distinct estimator" from a "single-mode-only decoupling". While technically correct, this distinction is subtle and could lead to misinterpretation. A reader might wonder why the "main" table doesn't contain the "main" quoted number from the text.
    *   **Fix:** Clarify this section significantly.
        1.  In the main text (Sec IV.C.b), explicitly state that the `+7.28σ` value comes from a 500-MC run using a specific single-mode decoupling estimator, and that a higher-statistics run with a full bandpower decoupling (detailed in Table III) yields a consistent value of `+7.31σ`.
        2.  In the caption of Table III, add a sentence explicitly linking the `+7.31σ` value in the table to the `+7.28σ` value discussed in the text, explaining that they are consistent results from different null-run sizes and slightly different estimator configurations, reinforcing the same physical conclusion.

### MINOR

*   **P4-m1:** Section: Abstract (Page 1)
    *   **Problem:** The abstract contains the sentence: "The +3.64σ value is from a 500-MC direct run on the canonical unapodized mask; the 10⁴-permutation canonical unapodized row in Table III gives +7.93σ; both are systematics-attributed diagnostics from different null-run sizes, not two independent detection claims." This is an excellent and necessary clarification. However, the distinction between the two values in Table III (canonical vs. apodized footprint) is also critical and is not mentioned here, whereas it is a key part of the analysis.
    *   **Fix:** Briefly mention the role of the apodized footprint in the abstract's discussion of the harmonic-channel diagnostics. For example: "...the post-MASTER harmonic diagnostics carry systematics-attributed residuals (+3.64σ moment-z, canonical mask; +7.28σ, apodized footprint)..." This adds precision without much length.

*   **P4-m2:** Section: III.A and Abstract (Page 1 & 3)
    *   **Problem:** The paper correctly and repeatedly warns that σ values from different nulls are not directly comparable. This is crucial. However, the abstract and main text juxtapose `z` (a moment ratio), `rank-p` (an empirical rank), and `z` (a bootstrap-t statistic) without always immediately reminding the reader of their different statistical meanings. For instance, the abstract's first paragraph lists `+0.41σ`, `p=0.31`, `z=0.58`, and `z≈-18`. While the notes provide the necessary caveats, the flow could be improved.
    *   **Fix:** In the "Significance conventions" (Sec. III.A.b), consider giving these different statistics distinct symbols or more descriptive names to make them easier to track (e.g., `z_mom`, `z_bs`, `p_rank`). While the current text is sufficient, this would be a significant aid to the reader in navigating the dense statistical results. At minimum, ensure every paragraph that mixes these values contains a reminder of the non-comparability.

*   **P4-m3:** Section: V.A (Comparison with Shamir) (Page 12)
    *   **Problem:** The text states: "We do not claim a frequentist exclusion of Shamir's Ganalyzer estimator: a likelihood-level exclusion requires a matched-footprint Ganalyzer reanalysis under his pipeline + cuts (not performed here)." This is the correct and responsible framing. However, the subsequent sentence attributes the discrepancy to two factors, the second being the monopole-mask leakage channel. This implies that the previous claims *could* be due to this effect, which is a strong but unproven assertion without the matched reanalysis.
    *   **Fix:** Soften the language slightly to be more speculative. Change "The discrepancy most likely reflects two factors" to "Potential sources for the discrepancy could include..." or similar phrasing that respects the lack of a direct reanalysis.

### NIT

*   **P4-N1:** Section: IV.D (Page 11)
    *   **Problem:** The text reads: "...under our DESI/ViT-Small pipeline; a matched Ganalyzer reanalysis remains required for a likelihood-level exclusion of their specific estimator and cuts." The semicolon feels slightly misplaced.
    *   **Fix:** Rephrase for clarity, perhaps: "...under our DESI/ViT-Small pipeline. A matched Ganalyzer reanalysis of their specific estimator and cuts would be required for a likelihood-level exclusion."

*   **P4-N2:** Section: Appendix D (Page 20)
    *   **Problem:** In the description of the WLS fit, the text refers to the primordial dipole basis as `{î, ŷ, 2}`. The `2` is clearly a typo for `ẑ`.
    *   **Fix:** Correct `2` to `ẑ`.

## Summary recommendation

**MAJOR REVISIONS**

This is a very strong, high-impact paper. The analysis is performed at a level of rigor that sets a new standard for observational cosmology studies of this type. The use of an equivariant pipeline is well-motivated and demonstrably crucial, and the detailed modeling of the primary systematic (monopole-mask leakage) is a significant contribution in its own right. The conclusions are robustly supported by an extensive suite of null tests and diagnostics.

The recommendation for "Major Revisions" is not due to any fundamental flaw in the analysis, but rather to address the paper's length, structure, and clarity, which are critical for a paper of this density and importance. The essential fix of the placeholder dates is trivial but non-negotiable. The primary task for the authors is to streamline the main text, moving more of the detailed supporting evidence to the appendices to create a more focused and readable narrative. Additionally, clarifying the relationship between the various, closely-related harmonic-channel statistics is necessary to prevent reader confusion. After these revisions, the paper will be an excellent and impactful contribution to the field.