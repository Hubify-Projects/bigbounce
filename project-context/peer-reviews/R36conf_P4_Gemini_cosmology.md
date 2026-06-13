# P4 R36conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/chirality_catalog_paper_v180.pdf` md5=26c9c91f pages=22
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (11755 chars)
**Wall time**: 259.7s

---

Here is a referee report for the submitted manuscript.

---
## Referee Report: "Survey-Scale Galaxy Chirality with Equivariant TTA..."

**Manuscript ID:** [Assigned by journal]
**Authors:** Houston Golden
**Journal:** Physical Review D

### Summary of the Paper
This paper presents a new, large-scale catalog of galaxy chirality for 8.47 million galaxies from the DESI Legacy Surveys, with 3.2 million classified as spirals. The classification is performed using a Vision Transformer pipeline with a test-time equivariant averaging (TTA) procedure to mitigate systematic biases. The primary scientific result is a null detection of a real-space chirality dipole, consistent with cosmological isotropy. The measured high-confidence dipole amplitude is consistent with zero at the 0.41σ level.

The main methodological contribution is the identification and detailed characterization of a "monopole-mask leakage" channel, where a small, uniform classifier bias (a monopole) couples with the non-uniform survey footprint (the mask) to create a spurious, highly significant dipole-like signal in spherical harmonic space (a pseudo-C_l excess). The authors demonstrate that this systematic effect can explain previous claims of a dipole detection in the literature. The paper includes an extensive suite of systematic checks, bias-hardening tests, and a detailed discussion of sensitivity and falsification criteria.

### General Comments
This is an exceptionally thorough and methodologically rigorous paper. The scale of the catalog is impressive, and the care taken to identify, quantify, and mitigate systematic effects is a model for this type of analysis. The central argument—that previous detections are likely attributable to a well-defined systematic effect related to classifier bias and survey geometry—is compelling and well-supported by the evidence presented. The transparency regarding the analysis process, including the public release of code and data and the explicit withdrawal of a result from a prior internal version, is commendable.

The paper is well-structured, and the distinction between the primary, real-space cosmological null result and the secondary, harmonic-space systematics diagnostics is maintained clearly throughout. The conclusions are appropriately stated and do not overreach the results. The work is of high quality and is suitable for publication in Physical Review D, pending revisions to address the issues detailed below.

### Findings

#### ESSENTIAL

*   **P4-E1: Removal of Internal File Paths and Artifact Names.**
    *   **Location:** Throughout the manuscript, e.g., Page 2, 3, 5, 6, 7, 8, 10, 12, 13, 16, 17, 19, 21.
    *   **Problem:** The text is littered with internal file paths and artifact names (e.g., `pipelines/p2_chirality/outputs/canonical_...`, `c12_r24conf_local_batch.json`, `artifact c9a`). These are placeholders for reproducibility that are not suitable for a final publication. They break the narrative flow and are meaningless to a reader without access to the author's local file system.
    *   **Required Fix:** All such paths and internal artifact names must be removed from the manuscript body, captions, and footnotes. If a specific result or configuration needs to be referenced for reproducibility, it should be done by pointing to a specific file or location within the public data release, citing a table or figure in the present paper, or by describing the configuration in the text (e.g., in an appendix). For example, instead of "artifact c12_r24conf_local_batch.json", the text should state "as verified in the robustness tests detailed in the data release" or refer to a specific section of the paper.

#### MAJOR

*   **P4-M1: Correction of Placeholder Dates.**
    *   **Location:** Page 1 (title block) and Page 21 (Data Availability section).
    *   **Problem:** The manuscript is dated "June 12, 2026", and the repository version is cited for "June 2026". These are clearly placeholder dates that are far in the future.
    *   **Required Fix:** Replace all placeholder dates with the current date of submission or revision.

#### MINOR

*   **P4-m1: Inconsistent Significance for Apodized MASTER Residual.**
    *   **Location:** Abstract (Page 1), Section IV.C.b (Page 8), and Table III (Page 11).
    *   **Problem:** The abstract and main text (p. 8) quote the significance of the apodized MASTER l=1 residual as +7.28σ, attributed to a 500-MC run. However, Table III, which presents the results from a higher-statistics 10^4-permutation run, gives a value of z = +7.31. While the paper correctly notes that these are from different runs, the highest-statistics result should be used consistently in the primary reporting channels.
    *   **Required Fix:** Update the abstract and the main-text discussion on page 8 to use the +7.31σ value from the 10^4-permutation run detailed in Table III for consistency and to reflect the most precise available calculation. The 500-MC result can be mentioned as a consistent prior result if desired, but the final, highest-statistics value should be primary.

*   **P4-m2: Falsification Criterion Sigma-Level.**
    *   **Location:** Abstract (Page 1).
    *   **Problem:** The abstract states the falsification criterion as "a future ≥ 5σ detection at amplitude A ≥ A_95". However, the injection-recovery tests and sensitivity floors throughout the paper (e.g., Table V, Section VI.A) are defined based on a P(≥ 3σ) detection probability. While a 5σ detection would certainly be in tension, the paper's own operational threshold is 3σ.
    *   **Required Fix:** For consistency with the analysis presented in the body of the paper, change "≥ 5σ detection" in the abstract to "≥ 3σ detection" or clarify that 5σ is a conventional high-energy physics discovery threshold, while the paper's operational limits are based on 3σ.

#### NIT

*   **P4-N1: Minor Typo in Abstract.**
    *   **Location:** Abstract (Page 1).
    *   **Problem:** The parenthetical sentence "(The +3.64σ value is from a 500-MC direct run on the canonical unapodized mask; the 10^4-permutation canonical unapodized row in Table III gives +7.93σ; both are systematics-attributed diagnostics from different null-run sizes, not two independent detection claims.)" is long and slightly convoluted.
    *   **Required Fix:** Consider breaking this into two shorter sentences for clarity. For example: "(The +3.64σ value is from a 500-MC direct run on the canonical unapodized mask. The 10^4-permutation run in Table III gives an updated value of +7.93σ. These are consistent diagnostics from different null-run sizes, not independent detection claims.)"

---
## Summary recommendation

**MAJOR REVISIONS**

The paper represents a significant and high-quality contribution to the field. The scientific analysis is sound, and the methodological rigor is exemplary. However, the manuscript in its current form is not acceptable for publication due to the pervasive use of internal file paths and the presence of placeholder dates. These are not cosmetic issues; they render parts of the paper unreadable and give it an unfinished appearance. Once these essential and major issues are thoroughly addressed, the paper will be a strong candidate for publication in Physical Review D. The minor points should also be addressed to improve clarity and consistency.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the review you just wrote on this paper:

================================================================
Here is a referee report for the submitted manuscript.

---
## Referee Report: "Survey-Scale Galaxy Chirality with Equivariant TTA..."

**Manuscript ID:** [Assigned by journal]
**Authors:** Houston Golden
**Journal:** Physical Review D

### Summary of the Paper
This paper presents a new, large-scale catalog of galaxy chirality for 8.47 million galaxies from the DESI Legacy Surveys, with 3.2 million classified as spirals. The classification is performed using a Vision Transformer pipeline with a test-time equivariant averaging (TTA) procedure to mitigate systematic biases. The primary scientific result is a null detection of a real-space chirality dipole, consistent with cosmological isotropy. The measured high-confidence dipole amplitude is consistent with zero at the 0.41σ level.

The main methodological contribution is the identification and detailed characterization of a "monopole-mask leakage" channel, where a small, uniform classifier bias (a monopole) couples with the non-uniform survey footprint (the mask) to create a spurious, highly significant dipole-like signal in spherical harmonic space (a pseudo-C_l excess). The authors demonstrate that this systematic effect can explain previous claims of a dipole detection in the literature. The paper includes an extensive suite of systematic checks, bias-hardening tests, and a detailed discussion of sensitivity and falsification criteria.

### General Comments
This is an exceptionally thorough and methodologically rigorous paper. The scale of the catalog is impressive, and the care taken to identify, quantify, and mitigate systematic effects is a model for this type of analysis. The central argument—that previous detections are likely attributable to a well-defined systematic effect related to classifier bias and survey geometry—is compelling and well-supported by the evidence presented. The transparency regarding the analysis process, including the public release of code and data and the explicit withdrawal of a result from a prior internal version, is commendable.

The paper is well-structured, and the distinction between the primary, real-space cosmological null result and the secondary, harmonic-space systematics diagnostics is maintained clearly throughout. The conclusions are appropriately stated and do not overreach the results. The work is of high quality and is suitable for publication in Physical Review D, pending revisions to address the issues detailed below.

### Findings

#### ESSENTIAL

*   **P4-E1: Removal of Internal File Paths and Artifact Names.**
    *   **Location:** Throughout the manuscript, e.g., Page 2, 3, 5, 6, 7, 8, 10, 12, 13, 16, 17, 19, 21.
    *   **Problem:** The text is littered with internal file paths and artifact names (e.g., `pipelines/p2_chirality/outputs/canonical_...`, `c12_r24conf_local_batch.json`, `artifact c9a`). These are placeholders for reproducibility that are not suitable for a final publication. They break the narrative flow and are meaningless to a reader without access to the author's local file system.
    *   **Required Fix:** All such paths and internal artifact names must be removed from the manuscript body, captions, and footnotes. If a specific result or configuration needs to be referenced for reproducibility, it should be done by pointing to a specific file or location within the public data release, citing a table or figure in the present paper, or by describing the configuration in the text (e.g., in an appendix). For example, instead of "artifact c12_r24conf_local_batch.json", the text should state "as verified in the robustness tests detailed in the data release" or refer to a specific section of the paper.

#### MAJOR

*   **P4-M1: Correction of Placeholder Dates.**
    *   **Location:** Page 1 (title block) and Page 21 (Data Availability section).
    *   **Problem:** The manuscript is dated "June 12, 2026", and the repository version is cited for "June 2026". These are clearly placeholder dates that are far in the future.
    *   **Required Fix:** Replace all placeholder dates with the current date of submission or revision.

#### MINOR

*   **P4-m1: Inconsistent Significance for Apodized MASTER Residual.**
    *   **Location:** Abstract (Page 1), Section IV.C.b (Page 8), and Table III (Page 11).
    *   **Problem:** The abstract and main text (p. 8) quote the significance of the apodized MASTER l=1 residual as +7.28σ, attributed to a 500-MC run. However, Table III, which presents the results from a higher-statistics 10^4-permutation run, gives a value of z = +7.31. While the paper correctly notes that these are from different runs, the highest-statistics result should be used consistently in the primary reporting channels.
    *   **Required Fix:** Update the abstract and the main-text discussion on page 8 to use the +7.31σ value from the 10^4-permutation run detailed in Table III for consistency and to reflect the most precise available calculation. The 500-MC result can be mentioned as a consistent prior result if desired, but the final, highest-statistics value should be primary.

*   **P4-m2: Falsification Criterion Sigma-Level.**
    *   **Location:** Abstract (Page 1).
    *   **Problem:** The abstract states the falsification criterion as "a future ≥ 5σ detection at amplitude A ≥ A_95". However, the injection-recovery tests and sensitivity floors throughout the paper (e.g., Table V, Section VI.A) are defined based on a P(≥ 3σ) detection probability. While a 5σ detection would certainly be in tension, the paper's own operational threshold is 3σ.
    *   **Required Fix:** For consistency with the analysis presented in the body of the paper, change "≥ 5σ detection" in the abstract to "≥ 3σ detection" or clarify that 5σ is a conventional high-energy physics discovery threshold, while the paper's operational limits are based on 3σ.

#### NIT

*   **P4-N1: Minor Typo in Abstract.**
    *   **Location:** Abstract (Page 1).
    *   **Problem:** The parenthetical sentence "(The +3.64σ value is from a 500-MC direct run on the canonical unapodized mask; the 10^4-permutation canonical unapodized row in Table III gives +7.93σ; both are systematics-attributed diagnostics from different null-run sizes, not two independent detection claims.)" is long and slightly convoluted.
    *   **Required Fix:** Consider breaking this into two shorter sentences for clarity. For example: "(The +3.64σ value is from a 500-MC direct run on the canonical unapodized mask. The 10^4-permutation run in Table III gives an updated value of +7.93σ. These are consistent diagnostics from different null-run sizes, not independent detection claims.)"

---
## Summary recommendation

**MAJOR REVISIONS**

The paper represents a significant and high-quality contribution to the field. The scientific analysis is sound, and the methodological rigor is exemplary. However, the manuscript in its current form is not acceptable for publication due to the pervasive use of internal file paths and the presence of placeholder dates. These are not cosmetic issues; they render parts of the paper unreadable and give it an unfinished appearance. Once these essential and major issues are thoroughly addressed, the paper will be a strong candidate for publication in Physical Review D. The minor points should also be addressed to improve clarity and consistency.
================================================================

NO ADDITIONAL FINDINGS

After a systematic and rigorous re-examination of the manuscript, focusing on arithmetic, cross-references, consistency, and other common sources of error, I have identified several new issues. These are detailed below and should be added to the initial report.

---
### Additional Findings from Rigorous Re-check

#### MAJOR

*   **P4-M2: Inconsistent and Confusing Use of Stale Significance Values.**
    *   **Location:** Abstract (p. 1), Section IV.D (p. 10), Section VII.C (p. 14), Table III (p. 11).
    *   **Problem:** The paper reports two different significance values for the canonical-mask residual: +3.64σ (from a 500-MC run) and +7.93σ (from a 10^4-permutation run). The abstract and conclusions retain the lower-statistics value, justifying this for "continuity with the leakage analysis." This is not a strong justification and creates significant confusion for the reader. The highest-statistics result should be the definitive value presented for a given diagnostic. Presenting both, with one being an outdated preliminary value, weakens the clarity and authority of the results.
    *   **Required Fix:** The highest-statistics result (+7.93σ from Table III) should be used as the definitive value for the canonical-mask residual in the abstract, conclusions, and main text. The lower-statistics result (+3.64σ) should be removed or relegated to a footnote explaining it was a preliminary value that has been superseded. The leakage analysis should be described in the context of the final, most precise result.

#### MINOR

*   **P4-m3: Incorrect and Incomplete Fisher Forecast Formula.**
    *   **Location:** Section VI.A.a, Equation (4) (p. 12).
    *   **Problem:** The formula presented for the Fisher forecast of the dipole amplitude, `σ(Α) = sqrt(3)/N_spiral * 2√3σ(fcw)`, is arithmetically and dimensionally incorrect. A simple check shows it does not yield the correct units or value. The quoted numerical result (`9.7 × 10^-4`) can only be reproduced by including a sky fraction factor (`f_sky ≈ 0.494`) which is missing from the equation, and by using the correct underlying formula, `σ(A) = sqrt(3 / (f_sky * N_spiral))`.
    *   **Required Fix:** Replace Equation (4) and the accompanying textual formula with the correct, complete Fisher forecast equation, and verify that it produces the quoted numerical results.

*   **P4-m4: Typo in URL.**
    *   **Location:** Data Availability section (p. 21).
    *   **Problem:** The URL for the HuggingFace catalog contains a space: `.../dataset s/...`. This will result in a broken link.
    *   **Required Fix:** Correct the typo in the URL.

*   **P4-m5: Ambiguous Significance Metric in Abstract.**
    *   **Location:** Abstract (p. 1).
    *   **Problem:** The abstract reports the primary null result as `+0.41σ`. However, the main text (e.g., p. 3, 7) clarifies that this is a "moment-z" or "moment-ratio", a non-Gaussian metric derived from the distribution of simulated amplitudes, and is distinct from a standard z-score. Stating it as `+0.41σ` without this context is potentially misleading.
    *   **Required Fix:** Briefly clarify the nature of this significance metric in the abstract, for example: "...gives a moment-ratio significance of +0.41σ..." or "...gives +0.41σ (moment-z)...".

#### NIT

*   **P4-N2: Confusing Example Calculation in Appendix.**
    *   **Location:** Appendix A.c (p. 15).
    *   **Problem:** This section describes the NaMaster configuration, which applies to both the apodized and canonical analyses. It includes an example calculation of the effect of monopole subtraction on the `l=1` power, `C₁`. The numbers used (`C₁` reduced from `2.30e-5` to `1.51e-5`, `σ` rising to `+3.64`) pertain specifically to the canonical-mask analysis. This is not explicitly stated, and a reader could mistakenly associate these intermediate values with the apodized-footprint analysis, which is the focus of the main text's `+7.28σ` result.
    *   **Required Fix:** Add a clarifying phrase to indicate that the numerical example of monopole subtraction pertains to the canonical-mask analysis, e.g., "For the canonical-mask analysis, as an example, monopole subtraction reduces...".