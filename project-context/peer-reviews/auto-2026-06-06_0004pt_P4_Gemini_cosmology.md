# P4 auto-2026-06-06_0004pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 148.2s

---

**Referee Report: P4**

This paper presents a multi-survey analysis of galaxy chirality using a catalog of 3.2 million spiral galaxies from the DESI Legacy Imaging Surveys. The authors use a Vision Transformer (ViT) classifier with a rigorous bias-hardening and mitigation pipeline, including test-time equivariant averaging (TTA), to produce the largest galaxy chirality catalog to date. The primary scientific result is a null detection of a cosmological dipole (l=1) in the chirality map, with the headline constraint being -0.122σ on a carefully selected subsample mask. The paper also identifies a statistically significant (+3.64σ) residual on a different sky mask ("canonical mask") and convincingly demonstrates through an extensive suite of systematic tests that this signal is not of cosmological origin, but rather an artifact of monopole leakage coupling with the survey geometry.

The analysis is exceptionally thorough, transparent, and methodologically sound. The authors' careful treatment of systematics, clear distinction between different estimators and their associated null hypotheses, and commitment to reproducibility are commendable. The detailed appendices provide the necessary evidence to support the claims made in the main text. The paper serves as both a significant cosmological null result and a valuable case study in mitigating subtle systematics in large-scale survey data.

The paper is recommended for publication in Physical Review D after the following essential, major, and minor points are addressed.

---
### ESSENTIAL Revisions

**P4-E1: Section: Title page, Page 1**
*   **Problem:** The date of the paper is listed as "(Dated: June 2026)". This is a future date and clearly a placeholder.
*   **Fix:** Replace the placeholder with the correct submission date.

---
### MAJOR Revisions

**P4-M1: Section: Appendix D, Page 8**
*   **Problem:** The letter `z` is used to denote statistical significance in the WLS fitting analysis (e.g., "z = -264.5", "reducing z to ~-18.1", "z ≈ -250"). In cosmology and astrophysics, `z` is the near-universal symbol for redshift. Using it for significance is highly non-standard and will cause significant confusion for readers.
*   **Fix:** Replace all instances of `z` used for significance with a standard symbol like `σ`, `S/N`, or simply "significance". For example, change "z = -264.5" to "σ = -264.5" or "significance = -264.5σ". This change should be applied consistently throughout the manuscript.

**P4-M2: Section: IV. Results, Page 3 & Abstract, Page 1**
*   **Problem:** The paper states that "values from distinct null procedures are not directly comparable" in several places. This is excellent practice. However, Table I (page 4) presents a list of sigma values from five different nulls side-by-side in a single column labeled "σ". While the "Null" column specifies the procedure, the presentation could still lead to improper comparison by a casual reader. The same issue exists in the abstract where multiple sigma values are quoted in sequence.
*   **Fix:** To reinforce this crucial point, add a footnote to the "σ" column header in Table I stating that the values are derived from different null hypotheses (as listed in the "Null" column) and are not directly comparable. In the abstract, when quoting multiple sigma values, consider a slightly more explicit phrasing, e.g., "...yields -0.122σ (relative to a label-shuffle null)... The real-space post-TTA Catalog C dipole is +0.43σ (relative to an isotropic bootstrap null)..."

---
### MINOR Revisions

**P4-m1: Section: Abstract, Page 1**
*   **Problem:** The abstract states: "The real-space post-TTA Catalog C dipole is +0.43σ (p=0.30, isotropic-null bootstrap, Nмс = 10,000)." A significance of +0.43σ under a Gaussian approximation corresponds to a one-tailed p-value of p ≈ 0.33, not 0.30. While the p-value is correctly stated to be from a bootstrap procedure (and thus not necessarily Gaussian), the discrepancy may cause confusion.
*   **Fix:** To avoid any ambiguity, clarify that the p-value is the empirical fraction of bootstrap realizations exceeding the observed value. For example, add a brief note in the main text where this result is first discussed (Sec. IV C) stating that p=0.30 is the empirical rank from the 10,000 bootstrap samples.

**P4-m2: Section: Table I, Page 4**
*   **Problem:** For the "hemisphere LEE (MC)" estimator, the result is given as "PLEE ≤ 10⁻⁴" in the "σ" column. This is a p-value, not a significance in units of sigma. Placing it in a column otherwise populated by sigma values is inconsistent.
*   **Fix:** Move the "PLEE ≤ 10⁻⁴" result to the "Estimator" or "Null" column, or add a separate column for p-values. Alternatively, convert the p-value to an equivalent Gaussian significance (e.g., `norm.ppf(1 - 1e-4) ≈ 3.7σ`) and clearly label it as such, while noting in the text that this is pre-look-elsewhere-correction. The current text in Sec. VI A correctly explains the post-LEE significance is < 1σ, which is the more important number.

**P4-m3: Section: II. B. Training Labels, Page 3**
*   **Problem:** The text notes that 67.6% of training labels derive from CE-ResNet predictions. This introduces a strong dependency on a previous work's model and means the validation metrics are not fully independent. The authors are transparent about this ("partially reflect agreement with CE-ResNet rather than independent ground truth").
*   **Fix:** This is a methodological weakness, but the authors' transparency is sufficient. However, for completeness, I suggest adding one sentence to the Discussion section briefly commenting on how this training strategy might affect the results and why the null result is still considered robust (e.g., because this type of bias is more likely to create a spurious signal than to mask a real one, which the authors' bias-hardening pipeline is designed to find and remove).

---
### NIT-PICKS (Cosmetic)

**P4-N1: Section: Appendix A, Page 7**
*   **Problem:** The text reads: "...the galaxy-weighted mask-mean (A)mask,gw is subtracted...". The notation `(A)mask,gw` is slightly awkward.
*   **Fix:** Change to a more standard notation, such as `<A>_mask,gw` or `Ā_mask,gw`.

**P4-N2: Section: IV. D, Page 4**
*   **Problem:** Minor typo in the last sentence. "...the strict-superset subsample-mask MASTER at -0.122σ." The sigma symbol is a subscript in the PDF OCR (`-0.122σ`). It should be typeset correctly. This appears to be an OCR artifact, but please double-check the final typesetting.
*   **Fix:** Ensure consistent and correct typesetting for σ.

---
## Summary recommendation
**MAJOR REVISIONS**

This is a high-quality, rigorous, and important contribution to the field. The authors have performed an exhaustive analysis, setting a new standard for systematic control in galaxy chirality studies. The primary null result is robustly demonstrated, and the detailed investigation of the systematic-driven +3.64σ signal is an excellent example of careful scientific work. The paper is well-suited for publication in Physical Review D. The required revisions are primarily focused on improving clarity and adhering to the journal's high standards for notation and presentation, and do not challenge the scientific conclusions of the work. Once the requested changes are made, the paper should be accepted.