# P4 R40conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/chirality_catalog_paper.pdf` md5=1e2501db pages=23
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 225.6s

---

**Referee Report: "Survey-Scale Galaxy Chirality with Equivariant TTA..."**

This paper presents a comprehensive analysis of galaxy chirality using a new, large catalog of 8.47 million galaxies from the DESI Legacy Surveys. The authors employ a Vision Transformer with a test-time equivariant averaging (TTA) technique to classify 3.2 million spiral galaxies. The primary scientific result is a null detection of a real-space chirality dipole, which is robustly tested against numerous systematics. The paper also provides a detailed diagnosis of a significant (l=1) signal in the harmonic-space power spectrum, attributing it to a combination of a classifier monopole bias leaking through the survey mask and other depth-correlated systematics.

The analysis is exceptionally thorough, and the paper is written with a high degree of clarity and statistical rigor. The authors are careful to distinguish between different estimators and null hypotheses, properly qualify the significance of their results, and avoid over-interpreting systematics-dominated signals. The methodological contributions, particularly the demonstration of the TTA's effectiveness and the quantification of the monopole-mask leakage channel, are significant for the field. The public release of the catalog and analysis scripts is commendable.

The paper is of high quality and is suitable for publication in Physical Review D, pending the following revisions.

---
### **List of Findings**

#### **ESSENTIAL**

*   **P4-E1: Data Availability Section Contains Placeholders**
    *   **Location:** Section "DATA AVAILABILITY", page 21.
    *   **Problem:** The section contains future-dated placeholders that are not appropriate for a final publication. Specifically: "commit 53b41d12 (v1.0.185 lineage, June 2026)" and "Release tag: v2026.04". A paper cannot be published with dates in the future. Furthermore, the text states "An immutable archival snapshot... will be deposited to Zenodo at journal submission", which is a statement of intent, not a completed action.
    *   **Required Fix:** Before publication, the authors must update this section with the final, persistent identifiers for the submitted version. This includes:
        1.  The final commit hash corresponding to the version of the code used for the results in the accepted paper.
        2.  The final release tag (e.g., v1.0).
        3.  The DOI for the archival snapshot on Zenodo, which must be created and deposited before the final version is submitted. The text should be changed from "will be deposited" to "is deposited at [DOI]".

#### **MAJOR**

*   **P4-M1: Unquantified Robustness Claim**
    *   **Location:** Section IV.B, page 6, last paragraph.
    *   **Problem:** The text claims, "The slab-to-slab scatter about the global fcw=0.49735 is ≤2.7σ per slab, consistent with the coherent low-l systematic structure...". This is a quantitative claim of consistency ("≤2.7σ") presented without the supporting calculation or a direct pointer to an artifact where this can be verified. While a later part of the paragraph provides an artifact for a different test, this specific claim is left unsupported.
    *   **Required Fix:** Provide the calculation for the 2.7σ value. State the number of slabs, the measured per-slab standard deviation, and the expected standard deviation under the null. Add a pointer to the specific analysis artifact that reproduces this number. For example: "(see artifact `...` for per-slab statistics)".

#### **MINOR**

*   **P4-m1: Ambiguity in Gaussian-Equivalent Sigma**
    *   **Location:** Abstract, page 1.
    *   **Problem:** The abstract states: "post-MASTER harmonic diagnostics carry systematics-attributed residuals (+3.64σ moment-z, ≈1.9σ Gaussian-equivalent, canonical mask...)". The body text (e.g., Fig. 8 caption, page 10) clarifies that the +3.64σ comes from a 500-MC run with an empirical p-value of 0.030. The conversion p=0.030 (one-sided) to a Gaussian equivalent is indeed ≈1.9σ. However, the juxtaposition of "+3.64σ moment-z" and "≈1.9σ Gaussian-equivalent" could be confusing. The moment-z is often interpreted as a Gaussian-equivalent significance, but here it clearly is not, as the null distribution is non-Gaussian.
    *   **Required Fix:** To improve clarity, rephrase slightly in the abstract. Suggestion: "...residuals (+3.64σ moment-z from a 500-MC run, corresponding to p=0.030 or ≈1.9σ Gaussian-equivalent, on the canonical mask...)". This explicitly links the p-value to the Gaussian equivalent and clarifies that the +3.64σ is a moment-based statistic from a non-Gaussian null.

*   **P4-m2: Minor Typo in Table I Caption**
    *   **Location:** Table I caption, page 5.
    *   **Problem:** The caption text reads: "Row (v) reports the post-look-elsewhere-corrected significance; the raw direct-MC value is P_LEE ≤ 10^-4 against the random-label max-statistic null, which already incorporates the look-elsewhere scan and is the principled directional look-elsewhere control (Appendix C); the rejection is systematics-attributed." The symbol `PLEE` is used, but the subscript is not defined. It presumably means "Look-Elsewhere Effect".
    *   **Required Fix:** Define the subscript for clarity, e.g., "p_LEE (Look-Elsewhere Effect)".

#### **NIT**

*   **P4-N1: Redundant Word**
    *   **Location:** Section VII. Conclusions, paragraph c, page 14.
    *   **Problem:** The text reads: "...the 10^4-permutation recompute of the same canonical unapodized field in Table III gives z = +7.93σ — the 500-MC +3.64σ direct single-mode value is retained for continuity with the leakage analysis; the 10^4-permutation Table III canonical row is the current high-statistics diagnostic...". The phrase "Table III canonical row" is slightly repetitive.
    *   **Required Fix:** Suggest changing to "...the 10^4-permutation result for the canonical mask in Table III is the current high-statistics diagnostic...".

---
### **Summary recommendation**

**MAJOR REVISIONS**

The paper represents a substantial and high-quality contribution to the field. The analysis is rigorous, the conclusions are well-supported, and the methodological findings are important. The recommendation for "MAJOR REVISIONS" is driven solely by the **ESSENTIAL** finding (P4-E1) regarding the placeholder information in the Data Availability section. A paper cannot be accepted for publication without finalized, persistent data and code identifiers. Once this and the other minor points are addressed, the paper will be in excellent shape for publication. The scientific content itself is already at an acceptance-level standard.