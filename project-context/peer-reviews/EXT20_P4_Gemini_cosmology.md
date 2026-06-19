# P4 EXT20 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p2_chirality/chirality_catalog_paper.pdf` md5=c47abc18 pages=23
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 179.7s

---

**Referee Report on "Survey-Scale Galaxy Chirality with Equivariant TTA..."**

**Manuscript ID:** [Assigned by journal]
**Author:** Houston Golden
**Date of Report:** [Current Date]

This paper presents a comprehensive analysis of galaxy chirality using a large catalog of 8.47 million galaxies from the DESI Legacy Surveys. The primary result is a null detection of a real-space chirality dipole, consistent with statistical isotropy. The work introduces a robust, flip-equivariant Vision Transformer pipeline and performs an exceptionally thorough investigation of potential systematic effects. Key contributions include the identification and quantification of a "monopole-mask leakage" channel as a significant source of systematics in harmonic-space analyses, and a clear demonstration of how equivariant test-time averaging (TTA) removes large-scale biases present in the raw classifier output.

The analysis is rigorous, the methodology is sound, and the conclusions are well-supported by the evidence. The author is commendably transparent about the limitations of the study and is careful to distinguish between results from different statistical estimators and null hypotheses. The paper represents a significant contribution to the field and sets a high standard for future work on this topic.

However, there is one critical issue regarding the manuscript's dating and versioning that must be resolved before publication. Several minor points for improving clarity are also noted below.

---
### **Detailed Findings**

#### **ESSENTIAL**

*   **P4-E1: Manuscript and Data Versioning (Page 1, Page 21)**
    *   **Problem:** The manuscript is dated "June 13, 2026" (p. 1), and the associated data release tag in the Data Availability section is "v2026.04" (p. 22). These future dates are unacceptable for a manuscript under review. It suggests that the submitted version is a placeholder or an unfinished draft, which is not appropriate for peer review at a journal like Physical Review D.
    *   **Fix:** The author must update the manuscript date to the current submission date. The data availability section must be updated to refer to a static, citable, and currently existing version of the data and code. A placeholder for a future Zenodo DOI is acceptable, but the commit hash and release tags must correspond to the version of the software and data used for the analysis presented in the manuscript, and they must be current.

#### **MAJOR**

*(No major findings. The scientific content and analysis are of high quality.)*

#### **MINOR**

*   **P4-m1: Clarification of Two Significance Values for the Canonical Mask Residual (Abstract, p. 1; Conclusions, p. 14)**
    *   **Problem:** The abstract and conclusions mention two different significance values for the canonical mask residual: +3.64σ from a 500-MC run and +7.93σ from a 10⁴-permutation run (Table III). While the abstract does an admirable job explaining that these arise from different null run sizes, this point is subtle and could cause confusion. The primary difference is not just the run size but that one is a direct MC compute and the other is from a full permutation recompute, which may have different statistical properties (e.g., tail behavior).
    *   **Fix:** In the main text where these values are discussed (e.g., Sec. VII.c, p. 14), briefly elaborate on why the 10⁴-permutation null yields a higher significance. Is it simply a matter of resolving the null distribution's tail with higher precision, or does the permutation null have a smaller variance than the direct-MC null? A sentence of clarification would strengthen the already excellent discussion.

*   **P4-m2: Wording of Falsification Criterion (Abstract, p. 1)**
    *   **Problem:** The abstract states: "a future > 5σ real-space dipole detection... would be in tension with the present null." While technically correct, a 5σ detection is by definition in tension with a null hypothesis. The more specific and useful statement concerns the amplitude.
    *   **Fix:** Rephrase for clarity. Suggestion: "A future detection of a real-space dipole at >5σ significance with an amplitude A ≥ A95 (where our analysis finds A95 is between 1.0% and 1.5%) would be in tension with the null result presented here." This more directly links the significance to the physical amplitude, which is the core of the falsification criterion.

#### **NIT (Cosmetic)**

*   **P4-N1: Repetitive Phrasing in Table III Caption (p. 11)**
    *   **Problem:** The caption for Table III contains a slightly repetitive phrase: "...single mode l=1 decoupled within the full 39-band coupling matrix (single-multipole bin, Appendix A.b not a bandpower over a range); the single-mode-only decoupling of Sec. IV C...".
    *   **Fix:** Consider streamlining this sentence for conciseness. For example: "...Band 1 is the l=1 mode, decoupled from the full 39-band coupling matrix (a single-multipole bin, not a bandpower). This is distinct from the estimator used in Sec. IV C, which also employed a single-mode-only decoupling..."

*   **P4-N2: Rounding in Abstract (p. 1)**
    *   **Problem:** The abstract states `N≈ 9.5 × 10⁵ spirals`, while the body (p. 7) gives the exact number `NHC = 949,584`.
    *   **Fix:** For an abstract, this level of rounding is acceptable. However, for maximum precision, consider using `N = 949,584` or `N ≈ 9.50 × 10⁵`. This is a minor stylistic point.

---
### **Summary recommendation**

**MAJOR REVISIONS**

The paper is scientifically excellent, methodologically rigorous, and presents a significant and robust null result on the galaxy chirality dipole. The analysis of systematics is exemplary. In its current state, the work is of a quality suitable for publication in Physical Review D.

However, the "MAJOR REVISIONS" recommendation is based entirely on the **ESSENTIAL** finding (P4-E1) regarding the future-dating of the manuscript and its associated data products. This is a critical issue of professionalism and reproducibility that must be fully rectified. Once the dates and versioning are corrected to reflect the current, static state of the work, the paper would require only minor touch-ups. I would be happy to review the revised manuscript.