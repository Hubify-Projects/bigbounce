# P5 RB-INT — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p5_desi_chirality/paper/p5_desi_chirality.pdf` md5=24506842 pages=34
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (9195 chars)
**Wall time**: 210.8s

---

**Referee Report on "Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T-Web (Hahn 2007) Tidal-Tensor Cross-Check Across the DR1 Matched-Spiral Sample"**

This manuscript presents a detailed statistical analysis searching for a correlation between spiral galaxy handedness (chirality) and large-scale structure environment, using data from the Dark Energy Spectroscopic Instrument (DESI) Data Release 1. The analysis is comprehensive, employing multiple cosmic-web classifiers (T-Web, DESIVAST) and performing a wide range of systematic checks and cross-validations. The primary conclusion is a null result: no statistically significant evidence for an environmental dependence of spiral chirality is found at the sensitivity of the current data. The work provides important observational constraints for cosmological models that might predict parity-violating signatures.

The analysis is exceptionally thorough and the authors are transparent about the limitations and methodological choices made. However, several revisions are required before the paper can be considered for publication in Physical Review D.

---
### ESSENTIAL Revisions

**P5-E1: Reliance on "in preparation" companion paper**
-   **Section/Page**: Throughout, e.g., Abstract (p.1), Sec I (p.3), Sec II (p.3), Table I (p.4).
-   **Problem**: The paper's core data input (the per-galaxy chirality labels) and the interpretation of the dominant systematic (the catalog-wide -0.26pp monopole offset) are sourced from "Paper IV [3] (in preparation)". A paper submitted to a peer-reviewed journal must be self-contained and its results verifiable. Relying on an unpublished, unavailable manuscript for the foundational data, classifier methodology, and systematic characterization is not acceptable. The conclusions of the present work are contingent on the validity of the methods and results of Paper IV.
-   **Required Fix**: The authors must make Paper IV publicly available, for instance by posting it to the arXiv preprint server. The reference [3] in the submitted manuscript must be updated to include a public arXiv identifier. The paper cannot be accepted for publication until its foundational inputs are documented in an accessible public record.

**P5-E2: Abstract-body mismatch on headline T-Web result**
-   **Section/Page**: Abstract (p.1).
-   **Problem**: The abstract reports the raw significance of the T-Web filament (-2.61σ) and cluster (-4.66σ) classes and qualifies this by stating they are "at the catalog-mean offset". This phrasing is ambiguous and potentially misleading, as the raw significances are large. The core argument of the paper is that these deviations vanish after subtracting the catalog-wide monopole systematic. The abstract should lead with this cleaner, more direct statement of the final result.
-   **Required Fix**: Rephrase the abstract to focus on the monopole-subtracted residuals, which are the key diagnostic for the T-Web analysis. For example: "The significant raw deviations in the filament (-2.61σ) and cluster (-4.66σ) classes are shown to be projections of a catalog-wide systematic; after subtracting this systematic, the residual environmental signal in all cosmic-web classes is statistically insignificant (|σ_residual| < 1.2)." This is clearer, more accurate, and better reflects the paper's main argument.

---
### MAJOR Revisions

**P5-M1: Post-hoc designation of primary analysis**
-   **Section/Page**: Abstract (p.1), Sec V B (p.7).
-   **Problem**: The authors are commendably transparent in declaring that the primary analysis path (the DESIVAST-anchored test) was designated post-hoc, and that no pre-registered analysis plan was filed. While they provide a strong scientific justification for this choice (the superior statistical power and cleanliness of the DESIVAST void sample), this methodology is susceptible to "garden of forking paths" criticisms.
-   **Required Fix**: The authors have already declared the post-hoc nature of the choice, which is the most critical step. To further improve the manuscript's structure and proactively address this concern, the "Analysis-tree declaration" (Table III, currently on p.9) should be moved into the Statistical Methods section (Sec V B, p.7). Placing this table immediately after the discussion of the post-hoc choice would provide the reader with a clear, upfront map of the full scope of tests performed and how statistical multiplicity is accounted for.

**P5-M2: Internal version-history language**
-   **Section/Page**: Sec II (p.3).
-   **Problem**: The text contains the sentence: "The per-galaxy catalog labels and the monopole offset consumed by this paper are unaffected by Paper IV's harmonic-channel revision." This language is inappropriate for a formal publication as it reads like an internal note regarding the development history of the companion paper. It raises unaddressed questions about the stability of the inputs.
-   **Required Fix**: Remove this sentence. The final, cited version of Paper IV should be considered the definitive source for the inputs, rendering such comments on its revision history unnecessary.

**P5-M3: Paper Length and Structure**
-   **Section/Page**: Whole paper.
-   **Problem**: At 34 pages, the paper is long for a null-result publication. The core finding is the robust null detection established in the primary DESIVAST analysis (§VIII). The numerous secondary analyses (the full T-Web analysis, cross-validations with Tempel+2014 and ASTRA, etc.) and stress tests, while valuable for demonstrating robustness, significantly increase the length and may obscure the main result.
-   **Required Fix**: The authors should consider restructuring the paper to improve focus and readability. A suggested structure is to present the primary DESIVAST analysis as the core of the main paper, and move the detailed T-Web analysis (§VI, §VII) and the various external cross-validations (§IX, §X) into a comprehensive appendix or supplemental material. This would shorten the main body to a more appropriate length (~15-20 pages) while preserving the extensive and valuable validation work for the interested reader.

---
### MINOR Revisions

**P5-m1: Inconsistent σ calculation in abstract**
-   **Section/Page**: Abstract (p.1).
-   **Problem**: A re-calculation of the `σ from half` for the T-Web filament class (n=408,187, fcw=0.4980) yields -2.55σ, which differs from the quoted value of -2.61σ. The corresponding calculation for the cluster class (-4.66σ) matches perfectly. This suggests a minor typo in the input numbers (n or fcw) for the filament class.
-   **Required Fix**: Please verify the input numbers (n, n_cw) for the filament class from the analysis artifacts and ensure the quoted fcw and σ values in the abstract are mutually consistent.

**P5-m2: Ambiguous table header**
-   **Section/Page**: Table V (p.11).
-   **Problem**: The header of the final column of Table V is "σ_obs - σ_pred". However, the values are all positive, whereas a direct subtraction would produce signed residuals. The text clarifies that the absolute value is used, but the table header itself is ambiguous.
-   **Required Fix**: To avoid ambiguity, please change the column header in Table V to "|σ_obs - σ_pred|".

---
### NIT (Cosmetic)

**P5-N1: Title length**
-   **Section/Page**: Title (p.1).
-   **Problem**: The title is highly descriptive but also very long.
-   **Required Fix**: This is a stylistic suggestion for the authors and editors. Consider a more concise title, such as: "A Test of the Environmental Dependence of Spiral Chirality in DESI Data Release 1". The essential details are well-covered in the abstract.

---
## Summary recommendation
**MAJOR REVISIONS**

This paper presents a high-quality, comprehensive, and statistically rigorous analysis that provides the strongest constraints to date on the environmental dependence of spiral galaxy chirality. The work is characterized by an exceptional number of systematic checks and robustness tests. The conclusion—a null detection—is strongly supported by the data and the multitude of analyses performed.

However, the paper cannot be accepted in its current form. The reliance on an "in preparation" companion paper for its foundational data and systematic model is an essential issue that must be resolved by making the companion work publicly available. Furthermore, the paper would benefit significantly from revisions to the abstract for clarity, and a restructuring to improve focus and readability given its length.

Once these revisions are made, the manuscript will be an excellent and important contribution to the field, suitable for publication in Physical Review D.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the updated referee report, incorporating the findings from the "fresh eyes" review.

================================================================
**Referee Report on "Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T-Web (Hahn 2007) Tidal-Tensor Cross-Check Across the DR1 Matched-Spiral Sample"**

This manuscript presents a detailed statistical analysis searching for a correlation between spiral galaxy handedness (chirality) and large-scale structure environment, using data from the Dark Energy Spectroscopic Instrument (DESI) Data Release 1. The analysis is comprehensive, employing multiple cosmic-web classifiers (T-Web, DESIVAST) and performing a wide range of systematic checks and cross-validations. The primary conclusion is a null result: no statistically significant evidence for an environmental dependence of spiral chirality is found at the sensitivity of the current data. The work provides important observational constraints for cosmological models that might predict parity-violating signatures.

The analysis is exceptionally thorough and the authors are transparent about the limitations and methodological choices made. The quantitative results presented are meticulously calculated and internally consistent. However, several revisions are required before the paper can be considered for publication in Physical Review D.

---
### ESSENTIAL Revisions

**P5-E1: Reliance on "in preparation" companion paper**
-   **Section/Page**: Throughout, e.g., Abstract (p.1), Sec I (p.3), Sec II (p.3), Table I (p.4).
-   **Problem**: The paper's core data input (the per-galaxy chirality labels) and the interpretation of the dominant systematic (the catalog-wide -0.26pp monopole offset) are sourced from "Paper IV [3] (in preparation)". A paper submitted to a peer-reviewed journal must be self-contained and its results verifiable. Relying on an unpublished, unavailable manuscript for the foundational data, classifier methodology, and systematic characterization is not acceptable. The conclusions of the present work are contingent on the validity of the methods and results of Paper IV.
-   **Required Fix**: The authors must make Paper IV publicly available, for instance by posting it to the arXiv preprint server. The reference [3] in the submitted manuscript must be updated to include a public arXiv identifier. The paper cannot be accepted for publication until its foundational inputs are documented in an accessible public record.

**P5-E2: Abstract-body mismatch on headline T-Web result**
-   **Section/Page**: Abstract (p.1).
-   **Problem**: The abstract reports the raw significance of the T-Web filament (-2.61σ) and cluster (-4.66σ) classes and qualifies this by stating they are "at the catalog-mean offset". This phrasing is ambiguous and potentially misleading, as the raw significances are large. The core argument of the paper is that these deviations vanish after subtracting the catalog-wide monopole systematic. The abstract should lead with this cleaner, more direct statement of the final result.
-   **Required Fix**: Rephrase the abstract to focus on the monopole-subtracted residuals, which are the key diagnostic for the T-Web analysis. For example: "The significant raw deviations in the filament (-2.61σ) and cluster (-4.66σ) classes are shown to be projections of a catalog-wide systematic; after subtracting this systematic, the residual environmental signal in all cosmic-web classes is statistically insignificant (|σ_residual| < 1.2)." This is clearer, more accurate, and better reflects the paper's main argument.

---
### MAJOR Revisions

**P5-M1: Post-hoc designation of primary analysis**
-   **Section/Page**: Abstract (p.1), Sec V B (p.7).
-   **Problem**: The authors are commendably transparent in declaring that the primary analysis path (the DESIVAST-anchored test) was designated post-hoc, and that no pre-registered analysis plan was filed. While they provide a strong scientific justification for this choice (the superior statistical power and cleanliness of the DESIVAST void sample), this methodology is susceptible to "garden of forking paths" criticisms.
-   **Required Fix**: The authors have already declared the post-hoc nature of the choice, which is the most critical step. To further improve the manuscript's structure and proactively address this concern, the "Analysis-tree declaration" (Table III, currently on p.9) should be moved into the Statistical Methods section (Sec V B, p.7). Placing this table immediately after the discussion of the post-hoc choice would provide the reader with a clear, upfront map of the full scope of tests performed and how statistical multiplicity is accounted for.

**P5-M2: Internal version-history language**
-   **Section/Page**: Sec II (p.3).
-   **Problem**: The text contains the sentence: "The per-galaxy catalog labels and the monopole offset consumed by this paper are unaffected by Paper IV's harmonic-channel revision." This language is inappropriate for a formal publication as it reads like an internal note regarding the development history of the companion paper. It raises unaddressed questions about the stability of the inputs.
-   **Required Fix**: Remove this sentence. The final, cited version of Paper IV should be considered the definitive source for the inputs, rendering such comments on its revision history unnecessary.

**P5-M3: Paper Length and Structure**
-   **Section/Page**: Whole paper.
-   **Problem**: At 34 pages, the paper is long for a null-result publication. The core finding is the robust null detection established in the primary DESIVAST analysis (§VIII). The numerous secondary analyses (the full T-Web analysis, cross-validations with Tempel+2014 and ASTRA, etc.) and stress tests, while valuable for demonstrating robustness, significantly increase the length and may obscure the main result.
-   **Required Fix**: The authors should consider restructuring the paper to improve focus and readability. A suggested structure is to present the primary DESIVAST analysis as the core of the main paper, and move the detailed T-Web analysis (§VI, §VII) and the various external cross-validations (§IX, §X) into a comprehensive appendix or supplemental material. This would shorten the main body to a more appropriate length (~15-20 pages) while preserving the extensive and valuable validation work for the interested reader.

---
### MINOR Revisions

**P5-m1: Ambiguous table header**
-   **Section/Page**: Table V (p.11).
-   **Problem**: The header of the final column of Table V is "σ_obs - σ_pred". However, the values are all positive, whereas a direct subtraction would produce signed residuals. The text clarifies that the absolute value is used for some comparisons, but the table header itself is ambiguous.
-   **Required Fix**: To avoid ambiguity, please change the column header in Table V to "|σ_obs - σ_pred|".

**P5-m2: Inconsistent significance metric in figure caption**
-   **Section/Page**: Figure 9 caption (p.26).
-   **Problem**: The caption describes the 0.29 pp difference between the Tempel and T-Web filament classes as a "~0.5σ difference". The body text (§IX B, p.25) more rigorously quantifies this using a two-sample z-test, finding |z| = 0.49. While numerically similar in this case, using "σ" in the caption is ambiguous (is it the standard error of one sample, the other, or the difference?) and inconsistent with the more precise z-score used in the main text.
-   **Required Fix**: For clarity and consistency, please replace "~0.5σ difference" in the caption of Figure 9 with the more precise statement from the body text, for example: "a statistically insignificant difference (|z|=0.49)".

---
### NIT (Cosmetic)

**P5-N1: Title length**
-   **Section/Page**: Title (p.1).
-   **Problem**: The title is highly descriptive but also very long.
-   **Required Fix**: This is a stylistic suggestion for the authors and editors. Consider a more concise title, such as: "A Test of the Environmental Dependence of Spiral Chirality in DESI Data Release 1". The essential details are well-covered in the abstract.

---
## Summary recommendation
**MAJOR REVISIONS**

This paper presents a high-quality, comprehensive, and statistically rigorous analysis that provides the strongest constraints to date on the environmental dependence of spiral galaxy chirality. The work is characterized by an exceptional number of systematic checks and robustness tests. The conclusion—a null detection—is strongly supported by the data and the multitude of analyses performed.

However, the paper cannot be accepted in its current form. The reliance on an "in preparation" companion paper for its foundational data and systematic model is an essential issue that must be resolved by making the companion work publicly available. Furthermore, the paper would benefit significantly from revisions to the abstract for clarity, and a restructuring to improve focus and readability given its length.

Once these revisions are made, the manuscript will be an excellent and important contribution to the field, suitable for publication in Physical Review D.