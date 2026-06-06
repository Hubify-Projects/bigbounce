# P4 auto-2026-06-05_1919pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (2048 chars)
**Wall time**: 1349.1s

---

## Referee Report: "Survey-Scale Galaxy Chirality with Equivariant TTA..."

This paper presents a detailed analysis of galaxy chirality using a catalog of 3.2 million spiral galaxies from the DESI Legacy Surveys. The authors use a Vision Transformer classifier and a suite of modern analysis techniques, including Test-Time Averaging (TTA) for equivariance and the MASTER algorithm for power spectrum estimation, to search for a cosmological dipole in the distribution of galaxy handedness.

The primary scientific result is a null detection of the `l=1` dipole on a carefully selected subsample, with a significance of -0.122σ. The authors identify a statistically significant `l=1` residual (+3.64σ) on a different, patchier sky mask ("canonical mask") but perform an exceptionally thorough systematic analysis to demonstrate that this signal is not of cosmological origin. They convincingly argue it arises from the leakage of a classifier-induced monopole into the dipole due to the complex survey geometry. This work serves as both a stringent new constraint on isotropy-breaking physics and a valuable case study in the control of systematics in modern survey cosmology.

The methodology is sophisticated, the analysis is rigorous, and the conclusions are well-supported by the evidence. The public release of the catalog, model, and code is commendable. The paper is a strong candidate for publication in Physical Review D, pending revisions to address the following points.

### Summary of Findings

| ID     | Type      | Section | Page | Summary of Issue                               |
| :----- | :-------- | :------ | :--- | :--------------------------------------------- |
| P4-E1  | ESSENTIAL | IV.B    | 4    | Sign error in Table II deviation value.        |
| P4-M1  | MAJOR     | III     | 3    | Understated dependency on machine-generated training labels. |
| P4-M2  | MAJOR     | IV.D    | 5    | Incomplete data in Table III power spectrum results. |
| P4-M3  | MAJOR     | Abstract| 1    | Potentially confusing presentation of σ-value in the abstract. |
| P4-m1  | MINOR     | Title   | 1    | Title is overly long and jargon-heavy.         |
| P4-N1  | NIT       | -       | 1    | Paper is dated in the future (June 2026).      |

---

### Detailed Findings

#### ESSENTIAL

**P4-E1: Sign Error in Table II Deviation Value**
*   **Section/Page:** IV.B, Table II, p. 4
*   **Problem:** In Table II, for Tier C (equivariant), the `cw/(cw + ccw)` fraction is 0.4974, which is less than 0.5. The corresponding deviation, defined as `(fcw - 0.5)/σ`, should therefore be negative. However, the table lists the deviation as `9.5`. My calculation, `(0.4974 - 0.5) / 0.000279 = -9.32`, confirms the sign is incorrect.
*   **Required Fix:** Correct the value in the "Dev. (σ)" column for Tier C from `9.5` to `-9.5` (or the more precise `-9.32`). This is essential for the internal consistency of a key table demonstrating the impact of the TTA procedure.

#### MAJOR

**P4-M1: Understated Dependency on Machine-Generated Training Labels**
*   **Section/Page:** III, p. 3
*   **Problem:** The note stating that "67.6% of training labels derive from CE-ResNet predictions" is a critical methodological caveat that is understated. This implies that the classifier is, to a large extent, trained to emulate another machine learning model rather than being trained on pure human-labeled ground truth. The significantly lower accuracy of 69.91% on the independent GZ1 cross-match is a more conservative and physically meaningful measure of the classifier's performance. The current presentation could be clearer about this hierarchy.
*   **Required Fix:** Elevate this point from a "Note" into the main body of Section II.B (Training Labels). Explicitly discuss the implication that the training is partly an emulation task. The abstract and main text should clearly state that the classifier's performance is benchmarked against a combination of human and machine labels, and the 69.91% accuracy against independent human labels should be highlighted as the key ground-truth performance metric that informs the analysis sensitivity.

**P4-M2: Incomplete Data in Table III**
*   **Section/Page:** IV.D, Table III, p. 5
*   **Problem:** Table III, which presents the angular power spectrum results, is missing the uncertainty of the null simulations, `σ_null`, for the bandpower measurements (rows 2-7). The significance is given by `(C_l - C_null) / σ_null`, but without the `σ_null` values, the stated significance cannot be independently verified by the reader. This makes a key results table opaque.
*   **Required Fix:** Add a column for `σ_null` to Table III for all listed bandpowers to allow for verification of the "Significance (σ)" column.

**P4-M3: Potentially Confusing Presentation of σ-value in the Abstract**
*   **Section/Page:** Abstract, p. 1
*   **Problem:** The phrase "The post-MASTER canonical-mask direct-MC residual is +3.64σ (... ≈1.9σ Gaussian-equivalent...)" is dense and potentially confusing on a first read. The juxtaposition of a high sigma value (derived from a moment ratio) with a much lower one (derived from an empirical rank) requires immediate context to avoid misinterpretation.
*   **Required Fix:** Rephrase this part of the abstract for clarity. For example: "The post-MASTER canonical-mask residual has a significance of +3.64σ relative to the standard deviation of null simulations. However, its empirical rank p-value of 0.030, equivalent to a 1.9σ one-sided Gaussian deviation, indicates it is a moderate outlier rather than a formal detection." This more clearly separates the two different statistical measures.

#### MINOR

**P4-m1: Overly Long and Jargon-Heavy Title**
*   **Section/Page:** Title, p. 1
*   **Problem:** The title is exceptionally long and laden with technical jargon (e.g., "Subsample-Mask l=1 Null," "Monopole-Mask Leakage Channel"). While precise, its density may reduce its accessibility and impact.
*   **Required Fix:** The authors should consider shortening the title to focus on the main result, possibly moving some of the technical specifics to a subtitle or the abstract. For example: "A Null Search for a Chirality Dipole in 3.2 Million DESI Legacy Spiral Galaxies". This is a suggestion for the authors' consideration.

#### NIT

**P4-N1: Future Date**
*   **Section/Page:** Metadata, p. 1
*   **Problem:** The paper is dated "June 2026". This appears to be a placeholder or typo.
*   **Required Fix:** Correct the date to the current submission date.

---

## Summary recommendation

**MAJOR REVISIONS**

This is a high-quality, methodologically sound paper that presents an important null result for cosmology. The analysis of systematics is exemplary and provides a valuable lesson for the field. The paper is well-suited for publication in Physical Review D. However, the required revisions are significant. The issues of the training data dependency and the incomplete results table must be addressed to ensure full transparency and reproducibility. The sign error in Table II is a critical correction. Once these points are satisfactorily addressed, the paper will be a strong and impactful contribution to the literature.

---

## PASS 2 — self-critique findings (what initial review missed)

Here are the additional findings from the second, more rigorous review of the paper.

---
### Additional Findings

#### MAJOR

**P4-M4: Inconsistent Quantification of TTA Asymmetry Suppression**
*   **Section/Page:** IV.B, p. 4
*   **Problem:** The text makes a key quantitative claim about the effectiveness of the Test-Time Averaging (TTA) procedure: "The 3.86× asymmetry-suppression factor from raw +2.05% to equivariant -0.53% demonstrates the dominance of the equivariant TTA processing." However, the primary results in Table II show a raw excess of +0.79% (Tier A) and an equivariant excess of -0.26% (Tier C). The numbers quoted in the text are inconsistent with the paper's main results table. This appears to be a "stale number" from a previous version of the analysis that was not updated, creating a significant internal contradiction.
*   **Required Fix:** The sentence in Section IV.B must be updated to use the final numbers presented in Table II. The asymmetry-suppression factor should be recalculated based on the values in the table (e.g., using the ratio of excess magnitudes, `0.79 / 0.26 ≈ 3.0`).

#### MINOR

**P4-m2: Minor Arithmetic Discrepancies in Table II**
*   **Section/Page:** IV.B, Table II, p. 4
*   **Problem:** In addition to the sign error identified in the initial review (P4-E1), there are minor arithmetic discrepancies in the "Dev. (σ)" column of Table II.
    *   For Tier A, `(0.5079 - 0.5) / 0.000279 ≈ 28.3`, but the table lists `28.8`.
    *   For Tier B, `(0.504 - 0.5) / 0.000279 ≈ 14.3`, but the table lists `14.6`.
    These small differences (~2-4%) suggest a minor inconsistency, perhaps from rounding or using a slightly different value for `N_spiral` or `σ` than what is implied by the caption. While not altering the conclusion, they detract from the paper's otherwise high standard of rigor.
*   **Required Fix:** The authors should re-calculate and verify all values in the "Dev. (σ)" column of Table II to ensure they are arithmetically consistent with the other data presented in the table.