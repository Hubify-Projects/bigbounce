# P4 auto-2026-06-08_1424pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (12474 chars)
**Wall time**: 156.7s

---

# Referee Report

**Paper ID:** P4
**Title:** Survey-Scale Galaxy Chirality with Equivariant TTA: A -0.122σ Subsample-Mask l=1 Null, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)
**Journal:** Physical Review D

This paper presents a search for a cosmological dipole in the projected chirality of 3.2 million spiral galaxies from the DESI Legacy Surveys. The primary scientific result is a null detection, consistent with statistical isotropy. The authors perform a detailed and rigorous analysis, with a particular focus on identifying and mitigating systematic effects. A key part of the work is the identification of a "monopole-mask leakage" channel, where a small global asymmetry (monopole) in the classified sample couples with the non-uniform survey mask to create a spurious low-l power spectrum signal. The authors convincingly argue that a statistically significant residual found in one of their estimators is attributable to this systematic effect, and they present results from other estimators, immune to this effect, that show a clear null result.

The methodology is sound, leveraging modern machine learning techniques (a Vision Transformer with Test-Time Averaging) and standard cosmological statistics tools (NaMaster). The public release of the catalog, model, and analysis code is a significant strength. The paper is well-structured, with extensive appendices detailing the crucial systematic checks.

While the overall analysis is of high quality, there are several issues, ranging from critical inconsistencies to minor points of clarity, that must be addressed before the manuscript can be accepted for publication.

---

## Detailed Findings

### ESSENTIAL

**P4-E1: Inconsistent Significance of the Canonical-Mask Residual**
*   **Location:** Abstract (p.1), Table I (p.4), Sec. IV D (p.4), Table III (p.5), Sec. VII (p.6-7), Appendix D (p.8)
*   **Problem:** The paper repeatedly quotes the post-MASTER canonical-mask residual as "+3.64σ". However, it also consistently reports the empirical rank p-value from Monte Carlo simulations as `p_mc = 0.030` (e.g., `15/500` on p.7). A p-value of 0.03 corresponds to a one-tailed significance of approximately 1.9σ for a Gaussian distribution, not 3.64σ. This is a major contradiction. A 3.64σ result would be strong evidence against the null hypothesis, whereas a p=0.03 result is marginal. The text mentions `z = Δ/σ_null moment-ratio`, suggesting the 3.64σ value is a z-score derived from the moments of the null distribution. If the null distribution is significantly non-Gaussian, the z-score can be misleading. The empirical rank p-value is the more robust and non-parametric measure of significance.
*   **Required Fix:**
    1.  The authors must clarify the origin of the 3.64σ value and explicitly justify its use if the underlying null distribution is non-Gaussian.
    2.  For clarity and consistency, it is strongly recommended to replace the "3.64σ" value with the more robust empirical significance derived from the p-value (e.g., "a significance corresponding to an empirical p-value of 0.030") throughout the manuscript. All mentions in the abstract, main text, tables, and conclusions must be made consistent.

**P4-E2: Internal Version History Language in Manuscript**
*   **Location:** Section IV D (p.4) and Footnote 1 (p.4)
*   **Problem:** The manuscript contains phrases that refer to its own revision history. This is unprofessional for a formal publication.
    *   Page 4, Sec. IV D: "...were interpreted in earlier paper versions as mask-geometric leakage..."
    *   Page 4, Footnote 1: "The previous wording "Binomial(ntotal, pglobal)" PCW was ambiguous..."
*   **Required Fix:** Remove all such internal-facing language. The text should be rewritten from the perspective of the final, submitted version. For example, the first instance could be rephrased to simply state the interpretation without referencing past versions. The footnote should explain the methodology clearly without referring to "previous wording".

### MAJOR

**P4-M1: Sign Error in Table II**
*   **Location:** Table II, p. 4
*   **Problem:** In Table II, for Catalog C (equivariant), the `cw/(cw + ccw)` fraction is 0.4974, which is an excess of -0.26% relative to 0.5. However, the `Dev. (σ)` column reports a positive value of 9.5. This is a sign error. The deviation from the null hypothesis of 0.5 is negative.
*   **Required Fix:** Correct the sign of the deviation in the `Dev. (σ)` column for Catalog C. The value should also be re-checked; my calculation `(0.4974 - 0.5) / 0.000279` yields -9.32.

**P4-M2: Undefined "+4.31σ Monopole-Preserving Dipole"**
*   **Location:** Appendix E.b, p. 9
*   **Problem:** This section introduces a "+4.31σ monopole-preserving dipole" for the full Catalog C, which is claimed to collapse in high-confidence subsamples. This value appears nowhere else, and the main text quotes a real-space dipole of +0.43σ for the same catalog. The term "monopole-preserving dipole" is non-standard and is not defined. Without a clear definition, this result is confusing and its significance cannot be assessed.
*   **Required Fix:** Define precisely what a "monopole-preserving dipole" estimator is. Explain why its value is so different from the primary real-space dipole estimator (+0.43σ) and justify its introduction in this context.

**P4-M3: Imprecise Language on Parity Symmetries**
*   **Location:** Section VI B, p. 6
*   **Problem:** The text states, "the parity-odd signal lives in the l=0 monopole and even-l multipoles." This statement is imprecise and potentially misleading. A global average of a pseudoscalar quantity (a monopole, l=0) is indeed a parity-odd observable. However, a dipole (l=1) of that same quantity is a parity-even, isotropy-violating observable. The claim about "even-l multipoles" is unclear in this context.
*   **Required Fix:** Rephrase this section for greater theoretical precision. Clearly distinguish between parity-odd observables (like the global monopole) and parity-even, isotropy-violating observables (like the dipole and other multipoles, `l>0`).

### MINOR

**P4-MI1: Ambiguous Sample Size `n` in Abstract**
*   **Location:** Abstract, p. 1
*   **Problem:** The abstract reports the headline null result with `n=5,547,858`. Table I clarifies this is `N_map_weighted`, the total count of all classified objects (including non-spirals) in the mask. This is not the number of spiral galaxies whose chirality is being analyzed. This could be misinterpreted as a larger spiral sample size than was actually used.
*   **Required Fix:** Clarify in the abstract that `n` refers to the total number of objects used for the survey depth weight, while the number of spirals analyzed for the dipole is 3.2 million.

**P4-MI2: Missing Context for P_LEE in Table I**
*   **Location:** Table I, p. 4
*   **Problem:** The table lists `P_LEE ≤ 10⁻⁴` for the hemisphere asymmetry, which appears highly significant. The main text later clarifies that this is the p-value *before* a necessary look-elsewhere-effect correction, and that the post-correction significance is <1σ.
*   **Required Fix:** Add a note to the Table I caption or the entry itself specifying that this p-value is pre-trials-correction.

**P4-MI3: Discrepancy in z-score Calculation**
*   **Location:** Table IV, p. 5
*   **Problem:** For the "Pre-MASTER pseudo-C(l=1)" statistic, my calculation of the z-score is `(1.696 - 1.685) / 0.007 = 1.57`. The table reports `z = +1.68`. While this small difference does not alter the conclusion, it should be checked for accuracy.
*   **Required Fix:** Please verify the calculation and correct the value in the table if necessary.

**P4-MI4: Awkward Formatting in Conclusion**
*   **Location:** Section VII, p. 6
*   **Problem:** The text at the bottom of page 6 ends with the partial phrase "b. Canonical-N MASTER l=1 direct compute.", which appears to be a list item header. The corresponding text begins on the next page. This formatting is disjointed.
*   **Required Fix:** Reformat this section to ensure the list item and its text appear together as a single, coherent paragraph.

### NIT

**P4-N1: Ambiguous Notation for Dipole Significance**
*   **Location:** Section III A, p. 3
*   **Problem:** The text states `A_dipole = 0.43, p = 0.30`. The value 0.43 is the significance in units of σ, not the dipole amplitude `A`.
*   **Required Fix:** Change the notation to `σ_dipole = 0.43` or similar to avoid ambiguity.

---

## Summary recommendation

**MAJOR REVISIONS**

The paper presents a valuable null result on a topic of cosmological interest, and the analysis of systematics is thorough and commendable. It represents a significant amount of careful work. However, the manuscript is marred by a critical inconsistency in the reporting of the significance of their main systematic residual (the 3.64σ vs. p=0.03 issue), which must be resolved. Additionally, the presence of internal-facing language, a sign error in a key table, and the introduction of an undefined observable detract from the paper's quality and clarity. I recommend the paper for publication in Physical Review D after these essential and major issues have been satisfactorily addressed.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the updated review, incorporating the new findings from the second, more rigorous pass.

================================================================
# Referee Report

**Paper ID:** P4
**Title:** Survey-Scale Galaxy Chirality with Equivariant TTA: A -0.122σ Subsample-Mask l=1 Null, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)
**Journal:** Physical Review D

This paper presents a search for a cosmological dipole in the projected chirality of 3.2 million spiral galaxies from the DESI Legacy Surveys. The primary scientific result is a null detection, consistent with statistical isotropy. The authors perform a detailed and rigorous analysis, with a particular focus on identifying and mitigating systematic effects. A key part of the work is the identification of a "monopole-mask leakage" channel, where a small global asymmetry (monopole) in the classified sample couples with the non-uniform survey mask to create a spurious low-l power spectrum signal. The authors convincingly argue that a statistically significant residual found in one of their estimators is attributable to this systematic effect, and they present results from other estimators, immune to this effect, that show a clear null result.

The methodology is sound, leveraging modern machine learning techniques (a Vision Transformer with Test-Time Averaging) and standard cosmological statistics tools (NaMaster). The public release of the catalog, model, and analysis code is a significant strength. The paper is well-structured, with extensive appendices detailing the crucial systematic checks.

While the overall analysis is of high quality, there are several issues, ranging from critical inconsistencies to minor points of clarity, that must be addressed before the manuscript can be accepted for publication.

---

## Detailed Findings

### ESSENTIAL

**P4-E1: Inconsistent Significance of the Canonical-Mask Residual**
*   **Location:** Abstract (p.1), Table I (p.4), Sec. IV D (p.4), Table III (p.5), Sec. VII (p.6-7), Appendix D (p.8)
*   **Problem:** The paper repeatedly quotes the post-MASTER canonical-mask residual as "+3.64σ". However, it also consistently reports the empirical rank p-value from Monte Carlo simulations as `p_mc = 0.030` (e.g., `15/500` on p.7). A p-value of 0.03 corresponds to a one-tailed significance of approximately 1.9σ for a Gaussian distribution, not 3.64σ. This is a major contradiction. A 3.64σ result would be strong evidence against the null hypothesis, whereas a p=0.03 result is marginal. The text mentions `z = Δ/σ_null moment-ratio`, suggesting the 3.64σ value is a z-score derived from the moments of the null distribution. If the null distribution is significantly non-Gaussian, the z-score can be misleading. The empirical rank p-value is the more robust and non-parametric measure of significance.
*   **Required Fix:**
    1.  The authors must clarify the origin of the 3.64σ value and explicitly justify its use if the underlying null distribution is non-Gaussian.
    2.  For clarity and consistency, it is strongly recommended to replace the "3.64σ" value with the more robust empirical significance derived from the p-value (e.g., "a significance corresponding to an empirical p-value of 0.030") throughout the manuscript. All mentions in the abstract, main text, tables, and conclusions must be made consistent.

**P4-E2: Internal Version History Language in Manuscript**
*   **Location:** Section IV D (p.4) and Footnote 1 (p.4)
*   **Problem:** The manuscript contains phrases that refer to its own revision history. This is unprofessional for a formal publication.
    *   Page 4, Sec. IV D: "...were interpreted in earlier paper versions as mask-geometric leakage..."
    *   Page 4, Footnote 1: "The previous wording "Binomial(ntotal, pglobal)" PCW was ambiguous..."
*   **Required Fix:** Remove all such internal-facing language. The text should be rewritten from the perspective of the final, submitted version. For example, the first instance could be rephrased to simply state the interpretation without referencing past versions. The footnote should explain the methodology clearly without referring to "previous wording".

### MAJOR

**P4-M1: Sign and Magnitude Error in Table II**
*   **Location:** Table II, p. 4
*   **Problem:** In Table II, for Catalog C (equivariant), the `cw/(cw + ccw)` fraction is 0.4974, which is an excess of -0.26% relative to 0.5. However, the `Dev. (σ)` column reports a positive value of 9.5. This is a sign error. Furthermore, the magnitude appears incorrect; the calculation `(0.4974 - 0.5) / 0.000279` yields approximately -9.32.
*   **Required Fix:** Correct the sign and re-verify the magnitude of the deviation in the `Dev. (σ)` column for Catalog C.

**P4-M2: Undefined "+4.31σ Monopole-Preserving Dipole"**
*   **Location:** Appendix E.b, p. 9
*   **Problem:** This section introduces a "+4.31σ monopole-preserving dipole" for the full Catalog C, which is claimed to collapse in high-confidence subsamples. This value appears nowhere else, and the main text quotes a real-space dipole of +0.43σ for the same catalog. The term "monopole-preserving dipole" is non-standard and is not defined. Without a clear definition, this result is confusing and its significance cannot be assessed.
*   **Required Fix:** Define precisely what a "monopole-preserving dipole" estimator is. Explain why its value is so different from the primary real-space dipole estimator (+0.43σ) and justify its introduction in this context.

**P4-M3: Imprecise Language on Parity Symmetries**
*   **Location:** Section VI B, p. 6
*   **Problem:** The text states, "the parity-odd signal lives in the l=0 monopole and even-l multipoles." This statement is imprecise and potentially misleading. A global average of a pseudoscalar quantity (a monopole, l=0) is indeed a parity-odd observable. However, a dipole (l=1) of that same quantity is a parity-even, isotropy-violating observable. The claim about "even-l multipoles" is unclear in this context.
*   **Required Fix:** Rephrase this section for greater theoretical precision. Clearly distinguish between parity-odd observables (like the global monopole) and parity-even, isotropy-violating observables (like the dipole and other multipoles, `l>0`).

### MINOR

**P4-MI1: Ambiguous Sample Size `n` in Abstract**
*   **Location:** Abstract, p. 1
*   **Problem:** The abstract reports the headline null result with `n=5,547,858`. Table I clarifies this is `N_map_weighted`, the total count of all classified objects (including non-spirals) in the mask. This is not the number of spiral galaxies whose chirality is being analyzed. This could be misinterpreted as a larger spiral sample size than was actually used.
*   **Required Fix:** Clarify in the abstract that `n` refers to the total number of objects used for the survey depth weight, while the number of spirals analyzed for the dipole is 3.2 million.

**P4-MI2: Missing Context for P_LEE in Table I**
*   **Location:** Table I, p. 4
*   **Problem:** The table lists `P_LEE ≤ 10⁻⁴` for the hemisphere asymmetry, which appears highly significant. The main text later clarifies that this is the p-value *before* a necessary look-elsewhere-effect correction, and that the post-correction significance is <1σ.
*   **Required Fix:** Add a note to the Table I caption or the entry itself specifying that this p-value is pre-trials-correction.

**P4-MI3: Discrepancy in z-score Calculation**
*   **Location:** Table IV, p. 5
*   **Problem:** For the "Pre-MASTER pseudo-C(l=1)" statistic, my calculation of the z-score is `(1.696 - 1.685) / 0.007 = 1.57`. The table reports `z = +1.68`. While this small difference does not alter the conclusion, it should be checked for accuracy.
*   **Required Fix:** Please verify the calculation and correct the value in the table if necessary.

**P4-MI4: Awkward Formatting in Conclusion**
*   **Location:** Section VII, p. 6
*   **Problem:** The text at the bottom of page 6 ends with the partial phrase "b. Canonical-N MASTER l=1 direct compute.", which appears to be a list item header. The corresponding text begins on the next page. This formatting is disjointed.
*   **Required Fix:** Reformat this section to ensure the list item and its text appear together as a single, coherent paragraph.

### NIT

**P4-N1: Ambiguous Notation for Dipole Significance**
*   **Location:** Section III A, p. 3
*   **Problem:** The text states `A_dipole = 0.43, p = 0.30`. The value 0.43 is the significance in units of σ, not the dipole amplitude `A`.
*   **Required Fix:** Change the notation to `σ_dipole = 0.43` or similar to avoid ambiguity.

---
## Additional Findings from Second Review

The following issues were identified during a more detailed second pass of the manuscript.

### ESSENTIAL (NEW)

**P4-E3: Unreproducible Significance Values in Table III**
*   **Location:** Table III, p. 5
*   **Problem:** The significance values reported for the canonical-mask bandpowers (`l_eff > 1`) cannot be reproduced from the other numbers (`C_l`, `σ_null`) given in the table. The calculation `(C_meas - <C_null>) / σ_null` requires the null mean, `<C_null>`, which appears to be missing from the table. Without this crucial information, the results in this key diagnostic table are unverifiable.
*   **Required Fix:** Add a column for the null mean `<C_null>` to Table III or otherwise clarify how the significance values were calculated so they can be independently verified.

### MAJOR (NEW)

**P4-M4: Contradictory Description of the Null Hypothesis**
*   **Location:** Abstract (p.1), Main Text (p.1), Appendix A (p.7)
*   **Problem:** The null procedure for the canonical-mask residual (+3.64σ) is described as a "500-MC binomial per-pixel-shuffle null" in the abstract and main text. However, Appendix A, which details the NaMaster configuration, describes the null distribution as coming from "500 per-pixel random-label permutation realizations." A binomial draw and a label permutation are statistically different procedures. This ambiguity undermines the precise meaning and interpretation of the quoted p-value and significance.
*   **Required Fix:** Clarify which null procedure was used for the canonical-mask residual and ensure the description is consistent throughout the manuscript.

### MINOR (NEW)

**P4-MI5: Incorrect Cross-Reference for Systematic Floor**
*   **Location:** Section III A, p. 3
*   **Problem:** The text references "Sec. IV C" for the "sub-percent systematic floor". This topic is actually discussed in Section VI A.
*   **Required Fix:** Correct the cross-reference to point to Section VI A.

**P4-MI6: Unquantified Claim about Spiral Fraction**
*   **Location:** Section IV A, p. 3
*   **Problem:** The text states the measured spiral fraction (37.78%) is "consistent with magnitude-limited survey expectations." This claim is unquantified.
*   **Required Fix:** Provide a quantitative comparison or a citation to support this claim.

**P4-MI7: Unexplained `f_sky` Value in Sensitivity Calculation**
*   **Location:** Section VI A, p. 6
*   **Problem:** The Fisher floor sensitivity calculation uses `f_sky = 0.46`. This value differs from the `f_sky` values used for the main analysis masks (0.49005 for canonical, 0.659 for subsample) without any explanation for the change.
*   **Required Fix:** Explain why a different `f_sky` value is used for this calculation or correct it to be consistent with one of the analysis masks.

---

## Summary recommendation

**MAJOR REVISIONS**

The paper presents a valuable null result on a topic of cosmological interest, and the analysis of systematics is thorough and commendable. It represents a significant amount of careful work. However, the manuscript is marred by several critical inconsistencies that undermine its reproducibility and clarity. The conflicting reports of the significance of the main systematic residual (the 3.64σ vs. p=0.03 issue, P4-E1) and the unverifiable results in a key diagnostic table (P4-E3) are the most severe problems. Additionally, the presence of internal-facing language, errors in tables, and contradictory descriptions of the methodology detract from the paper's quality. I recommend the paper for publication in Physical Review D only after these essential and major issues have been satisfactorily addressed.