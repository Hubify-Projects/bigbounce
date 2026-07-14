# P2 V117FRESH_2026-07-14 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/research/focused_paper_source_integration/02_full_draft.pdf` md5=a6bf211f pages=10
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (9036 chars)
**Wall time**: 163.4s

---

**Referee Report: PRD Manuscript [v1.7.117]**
**Title:** Testing the Matter Bounce with Primordial Non-Gaussianity: An Amplitude Derivation and Conditional SPHEREx Sensitivity Recast
**Author:** Houston Golden

This paper presents two primary contributions: (1) a new derivation of the local non-Gaussianity amplitude, `f_NL`, in a matter-dominated contracting universe, finding `f_NL = -35/16` and correcting a previously cited value of `-35/8`; and (2) a conditional recast of the SPHEREx bispectrum sensitivity to this specific theoretical model. The author provides a detailed algebraic derivation, including multiple cross-checks, and a careful analysis of how observational sensitivity depends on nuisance parameters.

The work is well-motivated and addresses an important question in early universe cosmology. The algebraic derivation, which traces a discrepancy back to the source expressions of the original literature, is a valuable contribution. The observational recast is performed with commendable care, clearly stating all assumptions and limitations, particularly the crucial condition of faithful cubic-order transfer through the bounce. The distinction between a conditional recast and a full forecast is maintained clearly throughout the manuscript.

However, the manuscript in its current form contains several issues, including a critical numerical error and the use of placeholder references, that prevent its acceptance. I recommend **MAJOR REVISIONS** before the paper can be considered for publication in Physical Review D.

---
### Detailed Findings

#### ESSENTIAL Revisions

**P2-E1: Arithmetic Error in Core Verification Table (Table V)**
*   **Location:** Page 9, Appendix A, Table V.
*   **Problem:** The central claim of the paper is a certified, auditable derivation of the bounce amplitude. Table V is presented as the final, explicit, term-by-term verification of this derivation for benchmark momentum configurations. However, the "equilateral f_NL^eq" column does not sum to its stated total.
    My calculation of the sum is:
    `(-35/32) + (5/32) - (5/8) - (15/128) = (-140 + 20 - 80 - 15) / 128 = -215/128`.
    The table claims the sum is `-255/128`. This is a significant discrepancy (`-40/128 = -5/16`) in a table that is supposed to be the bedrock of the paper's algebraic proof. This error undermines the reader's confidence in the entire derivation.
*   **Required Fix:** The author must find the source of this error. Either one or more of the per-vertex contributions in the table is incorrect, or the total is incorrect. The entire calculation chain for the equilateral configuration in Appendix A must be re-checked and the table corrected. The accompanying certification script (`p2_vertex_check.py`) should be verified to be free of this error.

**P2-E2: Use of Placeholder/Future-Dated References and Manuscript Date**
*   **Location:** Page 1 (Date), Page 10 (References [17], [18], [19]).
*   **Problem:** The manuscript is dated "July 14, 2026". Furthermore, the constraints from Planck and DESI, which are used to contextualize the model, are cited with placeholder references that have future dates and non-existent arXiv IDs (e.g., `arXiv:2504.00884`, `arXiv:2411.17623`, `arXiv:2602.12357`). A manuscript submitted for publication cannot use future-dated or placeholder citations for existing data. It must cite the actual, current, publicly available papers and results.
*   **Required Fix:** The manuscript date must be corrected to the date of submission. All placeholder references must be replaced with the correct citations for the most recent published Planck and DESI non-Gaussianity constraints. The numerical values quoted in Section VIII must be updated to match those in the correct references.

#### MAJOR Revisions

**P2-M1: Manuscript Structure Buries the Main Contribution**
*   **Location:** Throughout, but primarily Section II and Appendix A.
*   **Problem:** The abstract and discussion correctly identify the algebraic derivation of `f_NL = -35/16` as the paper's primary and strongest result. However, this entire derivation is placed in Appendix A. The main text (Section II) presents the result (Eq. 3, 4) without proof, repeatedly referring the reader to the appendix. This is poor narrative structure. The main theoretical result of the paper should be in the main body.
*   **Required Fix:** Restructure the paper. The content of Appendix A, which details the re-summation of the vertices, the identification of the discrepancy in prior work, and the cross-checks, should be moved into the main text, likely as the core of Section II. The current Section II.A could serve as an introduction to this more detailed section.

#### MINOR Revisions

**P2-m1: Small Discrepancy in `r_eff` Calculation**
*   **Location:** Page 4, Section IV.
*   **Problem:** In the in-house Fisher check, the paper states that for the real-space, bias-fixed case, `σ_local = 0.626` and `σ_bounce = 0.631`, giving `r_eff = 0.9929`. My re-calculation gives `0.626 / 0.631 = 0.99207...`. This is a small difference but should be checked for a typo or rounding error.
*   **Required Fix:** Please verify this calculation and correct the text if necessary.

**P2-m2: Small Discrepancy in Planck Constraint Significance**
*   **Location:** Page 6, Section VIII.
*   **Problem:** The paper recasts the Planck constraint to `f_NL^bounce = -0.11 ± 5.71` and states this is `0.37σ` from the predicted `-35/16 = -2.1875`. My calculation of the significance is `|-2.1875 - (-0.11)| / 5.71 = 2.0775 / 5.71 ≈ 0.364σ`.
*   **Required Fix:** Please verify this calculation and correct the text if necessary.

#### NITs (Cosmetic)

**P2-N1: Internal Version Number in Header**
*   **Location:** Page 1, Header.
*   **Problem:** The header contains the text "v1.7.117". This appears to be an internal version number for the manuscript.
*   **Required Fix:** Remove this internal versioning information from the manuscript before publication.

---
## Summary recommendation

**MAJOR REVISIONS**

This paper has the potential to be an important contribution to the literature on bouncing cosmologies. The core idea of re-deriving the `f_NL` amplitude from first principles and correcting a long-standing value is excellent, and the work appears to have been done with significant care. The observational component is also well-executed, providing a clear-eyed view of the model's testability while being honest about all underlying assumptions.

However, the essential flaws identified—the arithmetic error in the key verification table and the use of placeholder references—are disqualifying in the paper's current state. Once these are corrected, and the paper is restructured to present its main result more prominently, it will be a strong candidate for publication in Physical Review D.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the updated review, incorporating the findings from the second, more detailed pass.

================================================================
**Referee Report: PRD Manuscript [v1.7.117]**
**Title:** Testing the Matter Bounce with Primordial Non-Gaussianity: An Amplitude Derivation and Conditional SPHEREx Sensitivity Recast
**Author:** Houston Golden

This paper presents two primary contributions: (1) a new derivation of the local non-Gaussianity amplitude, `f_NL`, in a matter-dominated contracting universe, finding `f_NL = -35/16` and correcting a previously cited value of `-35/8`; and (2) a conditional recast of the SPHEREx bispectrum sensitivity to this specific theoretical model. The author provides a detailed algebraic derivation, including multiple cross-checks, and a careful analysis of how observational sensitivity depends on nuisance parameters.

The work is well-motivated and addresses an important question in early universe cosmology. The algebraic derivation, which traces a discrepancy back to the source expressions of the original literature, is a valuable contribution. The observational recast is performed with commendable care, clearly stating all assumptions and limitations, particularly the crucial condition of faithful cubic-order transfer through the bounce. The distinction between a conditional recast and a full forecast is maintained clearly throughout the manuscript.

However, the manuscript in its current form contains several critical errors, including a failed arithmetic check in a core verification table, a fundamental dimensional inconsistency in the main observable, a failed cross-check in the appendix, and the use of placeholder references. These issues prevent its acceptance. I recommend **MAJOR REVISIONS** before the paper can be considered for publication in Physical Review D.

---
### Detailed Findings

#### ESSENTIAL Revisions

**P2-E1: Arithmetic Error in Core Verification Table (Table V)**
*   **Location:** Page 9, Appendix A, Table V.
*   **Problem:** The central claim of the paper is a certified, auditable derivation of the bounce amplitude. Table V is presented as the final, explicit, term-by-term verification of this derivation for benchmark momentum configurations. However, the "equilateral f_NL^eq" column does not sum to its stated total.
    My calculation of the sum is:
    `(-35/32) + (5/32) - (5/8) - (15/128) = (-140 + 20 - 80 - 15) / 128 = -215/128`.
    The table claims the sum is `-255/128`. This is a significant discrepancy (`-40/128 = -5/16`) in a table that is supposed to be the bedrock of the paper's algebraic proof. This error undermines the reader's confidence in the entire derivation.
*   **Required Fix:** The author must find the source of this error. Either one or more of the per-vertex contributions in the table is incorrect, or the total is incorrect. The entire calculation chain for the equilateral configuration in Appendix A must be re-checked and the table corrected. The accompanying certification script (`p2_vertex_check.py`) should be verified to be free of this error.

**P2-E2: Use of Placeholder/Future-Dated References and Manuscript Date**
*   **Location:** Page 1 (Date), Page 10 (References [17], [18], [19]).
*   **Problem:** The manuscript is dated "July 14, 2026". Furthermore, the constraints from Planck and DESI, which are used to contextualize the model, are cited with placeholder references that have future dates and non-existent arXiv IDs (e.g., `arXiv:2504.00884`, `arXiv:2411.17623`, `arXiv:2602.12357`). A manuscript submitted for publication cannot use future-dated or placeholder citations for existing data. It must cite the actual, current, publicly available papers and results.
*   **Required Fix:** The manuscript date must be corrected to the date of submission. All placeholder references must be replaced with the correct citations for the most recent published Planck and DESI non-Gaussianity constraints. The numerical values quoted in Section VIII must be updated to match those in the correct references.

**P2-E3: Failed Cross-Check in Appendix A**
*   **Location:** Page 8, discussion surrounding Eq. (A5).
*   **Problem:** The text presents a cross-check of the main result by summing the `f_NL` contributions from different orders in the slow-roll parameter `ε`. The text claims that the sum of the listed contributions reproduces the main result. However, the calculation as presented is arithmetically incorrect. With `ε=3/2`, the contributions `ε f_NL,ε1 = (3/2)(-5/3) = -5/2` and `ε^2 f_NL,ε2 = (9/4)(1) = 9/4` sum to `-1/4`, not the required `-35/16`. This represents a failure of a key, independent cross-check meant to bolster the paper's central claim.
*   **Required Fix:** The author must correct this section. Either the intermediate values in Eq. (A5) are wrong, or the method of combining them is not a simple weighted sum as implied. The logic of this cross-check must be repaired and clarified.

**P2-E4: Dimensional Inconsistency of the Main Observable**
*   **Location:** Page 2, discussion surrounding Eqs. (1) and (2).
*   **Problem:** The paper defines the configuration-dependent nonlinearity amplitude `B_NL` and explicitly states "BNL is dimensionless by construction". This statement is contradicted by the equations provided. In Eq. (1), `A_T` is correctly defined to be dimensionless (as a ratio of a degree-9 polynomial `P` and a degree-9 denominator `(k1 k2 k3)^3`). However, Eq. (2) then defines `B_NL` as proportional to `A_T / Σk_i^3`. Since `A_T` is dimensionless and `Σk_i^3` has units of `[wavenumber]^3`, the resulting `B_NL` has units of `k^-3`, not dimensionless. This is a fundamental inconsistency in the definition of the paper's primary observable.
*   **Required Fix:** The author must resolve this contradiction. This will likely involve either correcting the definition of `B_NL` in Eq. (2) to make it dimensionless (perhaps by including a factor of `(Σk_i^3) / (k1 k2 k3)^3` or similar) or retracting the claim that it is dimensionless and clarifying the conventions used.

#### MAJOR Revisions

**P2-M1: Manuscript Structure Buries the Main Contribution**
*   **Location:** Throughout, but primarily Section II and Appendix A.
*   **Problem:** The abstract and discussion correctly identify the algebraic derivation of `f_NL = -35/16` as the paper's primary and strongest result. However, this entire derivation is placed in Appendix A. The main text (Section II) presents the result (Eq. 3, 4) without proof, repeatedly referring the reader to the appendix. This is poor narrative structure. The main theoretical result of the paper should be in the main body.
*   **Required Fix:** Restructure the paper. The content of Appendix A, which details the re-summation of the vertices, the identification of the discrepancy in prior work, and the cross-checks, should be moved into the main text, likely as the core of Section II.

**P2-M2: Pattern of Numerical Inaccuracies**
*   **Location:** Page 4, Section IV.
*   **Problem:** Beyond the critical error in Table V, there is a pattern of smaller numerical errors or typos that suggests a lack of careful proofreading. For example:
    *   The real-space, bias-marginalized significance is given as `3.186σ`, but the inputs (`f_NL=-2.1875`, `σ_bounce=0.688`) yield `3.189...σ`, which should be rounded to `3.19σ`.
    *   The real-space, bias-fixed `r_eff` is given as `0.9929`, but the inputs (`σ_local=0.626`, `σ_bounce=0.631`) yield `0.99207...`, which should be `0.9921`.
*   **Required Fix:** The author must perform a thorough check of all numerical values quoted in the text and tables, re-calculating them from the provided inputs to ensure accuracy and consistent rounding.

#### NITs (Cosmetic)

**P2-N1: Internal Version Number in Header**
*   **Location:** Page 1, Header.
*   **Problem:** The header contains the text "v1.7.117". This appears to be an internal version number for the manuscript.
*   **Required Fix:** Remove this internal versioning information from the manuscript before publication.

---
## Summary recommendation

**MAJOR REVISIONS**

This paper has the potential to be an important contribution to the literature on bouncing cosmologies. The core idea of re-deriving the `f_NL` amplitude from first principles and correcting a long-standing value is excellent. The observational component is also well-executed in principle, providing a clear-eyed view of the model's testability.

However, the essential flaws identified—the arithmetic error in the key verification table, the dimensional inconsistency of the main observable, the failed cross-check, and the use of placeholder references—are disqualifying in the paper's current state. These errors undermine the central claims of the paper and must be fully resolved. Once these are corrected, the paper is restructured to present its main result more prominently, and all numerical claims are carefully verified, it will be a strong candidate for publication in Physical Review D.