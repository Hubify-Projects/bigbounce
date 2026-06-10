# P4 R8 — Physical Review D cosmology-physics referee

**Model**: `gemini-2.5-pro`
**Input format**:  [NATIVE PDF — Gemini sees rendered document]
**Wall time**: 62.7s

---

## Referee Report: "Survey-Scale Galaxy Chirality with Equivariant TTA..."

This paper presents a detailed analysis of galaxy chirality using a large dataset of 8.47 million galaxies from the DESI Legacy Imaging Surveys. The authors employ a Vision Transformer (ViT) classifier and a Test-Time Averaging (TTA) technique to produce a catalog of 3.2 million spiral galaxies. The primary scientific result is a null detection of a chirality dipole (ℓ=1) at the level of −0.12σ, which is robustly derived from estimators designed to mitigate systematic effects.

The paper's main contribution is not just the null result itself, but the rigorous and transparent methodology used to obtain it. The authors identify and quantify a critical systematic effect—a "monopole-mask leakage channel"—where a small, uniform classifier bias (a monopole) couples with the non-uniform survey geometry to create a large, spurious dipole signal in naive estimators. The demonstration that this effect can explain previous claims of a signal in the literature is a significant finding for the field. The paper correctly distinguishes between the parity-even nature of the dipole (an isotropy test) and the parity-odd nature of the monopole (a direct parity test), a crucial theoretical point that is often confused.

The analysis is thorough, with a pre-declared hierarchy of estimators, a comprehensive suite of bias-hardening tests, and a deep dive into a remaining +3.64σ residual, which is convincingly attributed to systematics on a patchier subset of the data. The public release of the catalog, model, and analysis code is commendable.

While the scientific analysis is of high quality, the manuscript contains several critical and major issues in its presentation that must be addressed before it can be considered for publication.

---
### Findings

#### ESSENTIAL

**P4-E1**
*   **Section/Page:** Abstract (p. 1), Section IV C (p. 4), Table I (p. 4)
*   **Problem:** The null procedure for the primary real-space dipole estimator is described inconsistently. The main text (p. 4) states the significance is derived "from the isotropic-null bootstrap at N_MC = 10,000". However, Table I, which summarizes all headline estimators, lists the null for the "real-space dipole" as "pp-shuffle" (per-pixel shuffle). These are different statistical procedures. The validity and interpretation of the quoted +0.43σ significance depend critically on the actual null hypothesis being tested.
*   **Fix:** The authors must clarify which null procedure was used for the real-space dipole and ensure the text and Table I are consistent. If both were performed, the results from both should be presented and any differences discussed.

**P4-E2**
*   **Section/Page:** Throughout (p. 1, p. 9)
*   **Problem:** The manuscript contains multiple future dates, which are inappropriate for a submitted scientific paper.
    1.  The paper is dated "June 4, 2026 PDT" (p. 1).
    2.  The data release tag is "v2026.04" (p. 9).
    3.  Reference [7] cites an arXiv preprint from the year 2026: "arXiv:2605.05570 (2026)".
*   **Fix:** All dates must be corrected to reflect the actual submission date. The reference to a future preprint should be updated to a valid citation or removed if it does not yet exist. These artifacts undermine the manuscript's credibility as a completed work.

#### MAJOR

**P4-M1**
*   **Section/Page:** Abstract (p. 1), Table I (p. 4), Table III (p. 5), Section VII (p. 6)
*   **Problem:** The significance of the main null result is reported with inconsistent precision throughout the paper. It is given as "−0.12σ" (Abstract), "−0.12" (Table I), "−0.122" (Table III), and both "−0.12σ" and "−0.122σ" (Conclusion). While these values are consistent, the number of significant figures should be harmonized and justified by the precision of the analysis.
*   **Fix:** Choose a single, consistent value for this result (e.g., −0.122σ) and use it throughout the manuscript.

**P4-M2**
*   **Section/Page:** Appendix B (p. 7)
*   **Problem:** In the description of the flip-equivariance consistency loss term (Eq. B1), the text states "and x = 0.5". This appears to be a typo for the hyperparameter λ, which is present in the equation.
*   **Fix:** Correct the text to read "and λ = 0.5".

#### MINOR

**P4-m1**
*   **Section/Page:** Title (p. 1)
*   **Problem:** The title is exceptionally long and functions more as a summary sentence than a title.
*   **Fix:** The authors should consider shortening the title to be more concise while still capturing the main contributions. For example: "A Null Search for Galaxy Chirality at Survey Scale: Systematics and a Quantifiable Leakage Channel in DESI Legacy Data".

**P4-m2**
*   **Section/Page:** Abstract (p. 1)
*   **Problem:** The abstract contains several likely OCR errors or typos that hinder readability.
    1.  "...after pow > 0.9". This should likely be `p_eq > 0.9` or similar, consistent with the variable name for equivariant probability.
    2.  "471049 high-confidence per-spiral". This number should be formatted with a comma for readability (471,049).
    3.  "...realizations at Pow nglobal = 0.4974...". This should likely be `p_global^CW = 0.4974` or similar, representing the global CW fraction.
*   **Fix:** Correct these typos and formatting issues in the abstract.

**P4-m3**
*   **Section/Page:** Throughout (e.g., p. 2, p. 3)
*   **Problem:** There is inconsistent capitalization for key terms. For example, "not spiral" (p. 2) vs. "NOT_SPIRAL" (p. 2, p. 5, etc.), and "ViT-Small" (p. 3) vs. "vit_small_patch16_224" (p. 3).
*   **Fix:** Use consistent capitalization for these terms throughout the manuscript.

**P4-m4**
*   **Section/Page:** Appendix A (p. 7)
*   **Problem:** The description of the binning scheme includes Python code syntax: "nmt.NmtBin.from_lmax_linear(lmax=191, nlb=1)". While useful for reproducibility, this should be described in prose in the main body of a paper.
*   **Fix:** Rephrase this description in plain language, e.g., "We use a single-multipole linear binning scheme up to ℓ_max = 191."

**P4-m5**
*   **Section/Page:** Data Availability (p. 9)
*   **Problem:** The URLs provided for the catalog and model contain spurious spaces, likely due to typesetting issues. For example, "huggingface.co/dataset s/bamfai/galaxy- chirality- catalog".
*   **Fix:** Correct the URLs to ensure they are valid hyperlinks.

**P4-m6**
*   **Section/Page:** Conclusion (p. 6)
*   **Problem:** In section VII.b, the text reads "yields direct canonical = +3.64σ". This is grammatically awkward and appears to be a typo.
*   **Fix:** Rephrase for clarity, for example, "yields a significance of +3.64σ on the canonical mask (p_MC = 0.030)".

#### NIT

**P4-N1**
*   **Section/Page:** Table II (p. 4)
*   **Problem:** The column header is "cw/(cw + ccw)", while the text consistently uses the uppercase abbreviations "CW" and "CCW".
*   **Fix:** For consistency, change the table header to "CW/(CW + CCW)".

---
## Summary recommendation
**MAJOR REVISIONS**

The paper presents a methodologically robust and scientifically valuable analysis. The identification of the monopole-mask leakage channel is a significant contribution that helps clarify long-standing observational puzzles in the field. The overall framework, including the pre-declared analysis hierarchy and bias-hardening suite, is exemplary. However, the manuscript is marred by several essential and major presentational flaws, including a critical inconsistency in the description of a primary null result and the presence of multiple future dates, which give the paper an unfinished appearance. These issues must be thoroughly addressed. Given the high quality of the underlying scientific work, I recommend the paper for publication after these major revisions are completed.