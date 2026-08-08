# P4 R39conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/chirality_catalog_paper.pdf` md5=414048af pages=23
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 218.5s

---

**Referee Report on "Survey-Scale Galaxy Chirality with Equivariant TTA..."**

**Manuscript ID:** [Assigned by journal]
**Authors:** Houston Golden
**Journal:** Physical Review D

This paper presents a new, large catalog of galaxy chirality classifications for 8.47 million galaxies from the DESI Legacy Surveys DR8. The primary scientific result is a null detection of a real-space chirality dipole, a parity-even observable that constrains large-scale isotropy-breaking axial-vector modes. The authors perform an extensive and rigorous analysis of systematic effects, identifying and quantifying a "monopole-mask leakage" channel as a significant contaminant in previous analysis methods. The work is methodologically strong, emphasizing the necessity of equivariant averaging and a declared analysis hierarchy to avoid spurious detections.

The paper is well-written, the analysis is exceptionally thorough, and the conclusions are well-supported by the evidence presented. The level of detail, particularly in the appendices regarding the analysis pipeline and systematic checks, is commendable and sets a high standard for reproducibility in this field. The distinction between the primary cosmological result and the various systematics diagnostics is maintained clearly throughout the manuscript.

However, there are several points that must be addressed before the paper can be accepted for publication. One of these is a major error in a key equation, which requires correction.

---
### Detailed Findings

#### ESSENTIAL
(None)

#### MAJOR

**ID: P4-M1**
*   **Location:** Section VI.A, page 12, Equation (4)
*   **Problem:** Equation (4) for the Fisher (statistical-only) floor is incorrect. The equation is given as `σ(A) = 3 / (2*sqrt(3)*σ(fcw))`. This expression is dimensionally inconsistent and the fraction is inverted. The variance should be proportional to `1/N_spiral`, and thus `σ(A)` should be proportional to `σ(fcw)`, not inversely proportional. The standard Fisher analysis for a dipole amplitude `A` in a binary classification problem yields `σ(A) = sqrt(3/N_spiral)`. This can be rewritten in terms of the binomial error on the monopole, `σ(fcw) = sqrt(fcw(1-fcw)/N_spiral) ≈ 1/(2*sqrt(N_spiral))`, as `σ(A) = 2*sqrt(3)*σ(fcw)`. The numerical value quoted in the paper (`9.7 x 10^-4`) is correct and consistent with the proper formula, but the equation as written is incorrect.
*   **Required Fix:** The equation must be corrected. The authors should replace the incorrect expression with the standard result, for example, `σ(A) = sqrt(3/N_spiral)`, and show how the numerical value is derived from it. Alternatively, they can use the form `σ(A) = 2*sqrt(3)*σ(fcw)` if they wish to relate it to the monopole uncertainty.

#### MINOR

**ID: P4-m1**
*   **Location:** Abstract (page 1), Section VII.C (page 14), and elsewhere.
*   **Problem:** The paper quotes two different significance values for the canonical-mask `l=1` residual: `+3.64σ` from a 500-MC run and `+7.93σ` from a 10,000-permutation run (Table III). The abstract and conclusion explain that these are from different null-run sizes and are not independent claims, with the former retained for "continuity with the leakage analysis". While this transparency is appreciated, it creates a potential point of confusion for the reader by presenting two different numbers for what is effectively the same diagnostic. The final, high-statistics result should be the headline number.
*   **Required Fix:** The authors should consider streamlining the presentation. The abstract and main conclusions should feature only the most robust, high-statistics result (`+7.93σ` from the 10,000-permutation null in Table III). The `+3.64σ` value and its context (continuity with the monopole-leakage analysis) can be confined to the specific section discussing that analysis (Section IV.D) and/or a footnote, rather than being featured in the main summary statements.

**ID: P4-m2**
*   **Location:** Page 1, Author Information
*   **Problem:** The author's contact email, `houston@hubify.com`, appears to be a non-institutional or placeholder address. For a scientific publication, a stable, professional, or institutional contact is preferred.
*   **Required Fix:** Please provide a standard institutional or long-term professional email address.

**ID: P4-m3**
*   **Location:** Page 1, Date
*   **Problem:** The date of the manuscript is listed as "June 13, 2026", which is in the future.
*   **Required Fix:** Please correct the date to the date of submission.

#### NIT (Nitpicks)

**ID: P4-N1**
*   **Location:** Page 1, Abstract
*   **Problem:** The parenthetical sentence explaining the `+3.64σ` and `+7.93σ` values is quite long and grammatically complex: "(The +3.64σ value is from a 500-MC direct run on the canonical unapodized mask; the 10⁴-permutation canonical unapodized row in Table III gives +7.93σ; both are systematics-attributed diagnostics from different null-run sizes, not two independent detection claims.)".
*   **Required Fix:** For improved readability, consider rephrasing this. For example: "The harmonic diagnostics show systematics-attributed residuals. A direct 500-MC run on the canonical mask yields +3.64σ, while a higher-statistics 10⁴-permutation run gives +7.93σ (Table III). These are diagnostics of the same systematic from different null-run sizes, not independent detections."

**ID: P4-N2**
*   **Location:** Page 21, Data Availability section
*   **Problem:** The text states "Repository state for this version: commit 53b41d12 (v1.0.180, June 2026)". However, the version number on the first page is "v1.0.185".
*   **Required Fix:** Please ensure the commit hash and version number in the Data Availability section are consistent with the version of the manuscript being submitted.

**ID: P4-N3**
*   **Location:** Page 11, Table III caption
*   **Problem:** The caption notes that the `+3.64σ` value is not tabulated. This is clear, but its relation to the tabulated `+7.93σ` could be made more explicit within the table's context.
*   **Required Fix:** Consider adding a footnote to the `l=1` entry in the "canonical, unapod." block of the table. The footnote could briefly state that the value shown is from the 10⁴-permutation null, and that a separate 500-MC run (used for the leakage analysis) gives `z=+3.64`. This would help readers connect the numbers mentioned in the text directly to the table.

---
### Summary recommendation

**MAJOR REVISIONS**

This is a high-quality, rigorous, and important contribution to the study of cosmological parity and isotropy. The authors have done an excellent job of performing a sensitive null measurement while meticulously accounting for and documenting potential systematic effects. The paper is a valuable methodological guide for future work in this area.

The recommendation for "Major Revisions" is based solely on the incorrect Fisher floor equation (P4-M1). An incorrect fundamental equation in a physics paper is a major issue that must be rectified. However, since the numerical result is correct and the error appears to be a typo in the presentation of the formula, this should be straightforward to fix. The other points are minor and aimed at improving clarity and consistency.

Once the authors have corrected the equation and addressed the minor points, the manuscript will be in excellent shape and I would strongly recommend it for publication in Physical Review D.