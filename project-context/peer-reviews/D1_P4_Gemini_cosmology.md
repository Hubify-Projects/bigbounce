# P4 D1 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p2_chirality/chirality_catalog_paper.pdf` md5=c47abc18 pages=23
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 189.6s

---

**Referee Report on "Survey-Scale Galaxy Chirality with Equivariant TTA..."**

This paper presents a search for a cosmic dipole in the chirality of spiral galaxies using a new, large catalog of 8.47 million galaxies from the DESI Legacy Surveys. The primary methodological contribution is the use of a Test-Time Equivariant Averaging (TTA) technique to suppress classifier biases, which is shown to be essential for a robust measurement. The main scientific result is a null detection of a real-space chirality dipole, consistent with statistical isotropy. The paper also presents a detailed investigation of systematic effects, identifying and quantifying a "monopole-mask leakage" channel and other systematics that affect harmonic-space estimators.

The analysis is exceptionally rigorous, transparent, and thorough. The authors demonstrate a sophisticated understanding of the potential pitfalls in this type of analysis and have gone to great lengths to control for them. The clear distinction between primary cosmological estimators and secondary systematics diagnostics, and the careful, repeated warnings about the non-comparability of significance values derived from different null hypotheses, are exemplary. The paper sets a new standard for rigor in this field.

While the paper is of very high quality and suitable for publication in Physical Review D, I have identified a few essential and minor points that must be addressed before acceptance.

---
### Findings

**ESSENTIAL**

*   **P4-E1: Section: Data Availability (Page 21) & Abstract (Page 1)**
    *   **Problem:** The paper contains placeholder future dates. The abstract is dated "June 13, 2026". The Data Availability section states: "Repository state for this version: commit 53b41d12 (v1.0.185 lineage, June 2026)".
    *   **Required Fix:** These dates must be updated to reflect the actual date of submission. The commit hash and version tag must correspond to the exact state of the repository at the time of submission to ensure reproducibility. Using future dates is not permissible.

**MAJOR**

*(No major findings. The paper's structure and core arguments are sound.)*

**MINOR**

*   **P4-M1: Section: VII. Conclusions (Page 14)**
    *   **Problem:** The summary of the "Canonical-N MASTER l=1 direct compute" in conclusion (c) is slightly confusing due to the presentation of multiple numerical results for the same quantity from different run configurations. The text reads: "...yields C_data = +3.64σ (p_MC=15/500=0.030; 500-MC direct run...); the 10⁴-permutation recompute... in Table III gives z = +7.93σ — the 500-MC +3.64σ direct single-mode value is retained for continuity with the leakage-analysis."
    *   **Required Fix:** While the reason for retaining the 500-MC value is explained, this could be streamlined for clarity. I suggest simplifying this conclusion point to focus on the final, most statistically robust result (the 10⁴-permutation run from Table III), while perhaps moving the discussion of the 500-MC run's consistency to a footnote or parenthesis to avoid giving two different headline numbers for the same diagnostic. For example: "A direct computation on the canonical mask yields a systematics-attributed residual at ℓ=1 of +7.93σ (10⁴-permutation null; see Table III), a result consistent with preliminary, lower-statistics runs used in the leakage analysis."

*   **P4-M2: Section: Abstract (Page 1)**
    *   **Problem:** The abstract states, "...the post-MASTER harmonic diagnostics carry systematics-attributed residuals (+3.64σ moment-z, ≈1.9σ Gaussian-equivalent, canonical mask; +7.28σ, apodized footprint)...". It later clarifies that the +3.64σ value is from a 500-MC run while Table III gives +7.93σ from a 10⁴-permutation run.
    *   **Required Fix:** For consistency and to present the most robust result, consider replacing the +3.64σ value in the abstract with the +7.93σ value from the high-statistics run in Table III, as this is the final diagnostic value for that estimator. The abstract should reflect the final, definitive analysis presented in the body. The note explaining the different runs can be adjusted accordingly. This would align the abstract with the recommendation in P4-M1.

*   **P4-M3: Section: VI.A Sensitivity Floor and Minimum Detectable Signal (Page 12)**
    *   **Problem:** The text states: "the per-galaxy Fisher information on A at A = 0 is cos²θ/[p(1-p)] · (dp/dA)² = cos²θ, so with the full-sky idealization ⟨cos²θ⟩ = 1/3,". The derivation is correct, but could be made more explicit for the reader.
    *   **Required Fix:** Briefly show the intermediate steps for the reader's benefit. Specifically, state that for p(n) = ½(1 + Acosθ), the derivative dp/dA = ½cosθ, and at A=0, p(1-p) = ¼. This makes the cancellation that leads to I(A) = cos²θ immediately obvious. This is a minor point of pedagogy.

**NIT**

*   **P4-N1: Section: Title (Page 1)**
    *   **Problem:** The title is very long and contains multiple clauses.
    *   **Required Fix:** This is a stylistic suggestion only. The authors might consider shortening the title for impact, for example: "A Survey-Scale Null Test for Galaxy Chirality: A Null Dipole and Quantified Systematics on 8.47 Million DESI Legacy Galaxies". The current title is, however, accurate and descriptive.

---
## Summary recommendation

**ACCEPT WITH MINOR CORRECTIONS**

This is an outstanding paper that represents a significant step forward in the search for cosmic parity violation and isotropy breaking. The analysis is performed at an extremely high level of rigor, and the methodological contributions, particularly regarding bias mitigation and systematic quantification, are valuable to the broader community. The null result for the chirality dipole is established with unprecedented statistical power and a degree of systematic control that convincingly addresses issues raised in prior literature. The paper is well-written, transparent about its limitations, and provides excellent resources for reproducibility.

Once the essential issue with the placeholder dates is corrected and the minor points of clarification are addressed, the paper will be a landmark contribution to the field and I strongly recommend its publication in Physical Review D.