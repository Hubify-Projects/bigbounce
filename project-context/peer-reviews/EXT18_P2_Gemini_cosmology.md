# P2 EXT18 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/research/focused_paper_source_integration/02_full_draft.pdf` md5=5a8a1af4 pages=29
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (12795 chars)
**Wall time**: 173.7s

---

**Referee Report on "Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook"**

**Manuscript ID:** [Assigned by journal]
**Authors:** Houston Golden
**Journal:** Physical Review D

This paper presents a detailed sensitivity forecast for testing the matter bounce cosmological model using upcoming large-scale structure surveys, primarily SPHEREx. The central prediction of the quasi-dust matter bounce is a local-type non-Gaussianity with amplitude `f_NL = -35/8`. The work is a "recast" of existing forecasts, focusing on a comprehensive treatment of the template mismatch between the bounce bispectrum and the standard local template, and a thorough analysis of systematic uncertainties. Key contributions include the quantification of the template overlap factor `r`, an analysis of the impact of an underdetermined polynomial basis for the bispectrum shape, a resolution of a factor-of-two discrepancy in the literature regarding the predicted `f_NL` value, and a Bayesian model comparison to assess the discriminating power against inflationary alternatives.

The paper is well-structured, methodologically sound in its core components, and addresses a timely and important question in observational cosmology. The detailed treatment of systematics and the focus on reproducibility are commendable. However, several major issues related to the justification of key quantitative claims, clarity in theoretical derivations, and the presentation of headline results must be addressed before the manuscript can be considered for publication in Physical Review D.

---
### Detailed Findings

#### ESSENTIAL

*   **P2-E1: Production Artifact (Page 29)**
    *   **Problem:** The manuscript file contains reviewer metadata at the very end: `[REVIEWER METADATA — NOT PART OF THE PAPER — DO NOT FLAG AS ARTIFACTS] ... [END REVIEWER METADATA]`. This is a production artifact that must be removed.
    *   **Fix:** Remove the entire metadata block from the manuscript source.

*   **P2-E2: Placeholder in Data Availability Section (Page 24)**
    *   **Problem:** The "DATA AND CODE AVAILABILITY" section contains the placeholder text: `(DOI inserted at submission)`.
    *   **Fix:** Replace the placeholder with the actual DOI for the archived data and code, or remove the parenthetical if a DOI is not yet available, ensuring the final version is compliant with journal policy.

#### MAJOR

*   **P2-M1: Unjustified "Realistic" Significance Range (Abstract, Page 1; Section IV, Page 10)**
    *   **Problem:** The abstract and main text quote a "realistic" detection significance range of `~2.6-5σ` for SPHEREx. While the lower bound of `2.6σ` is meticulously derived in Table IV as the most conservative, all-combined scenario, the upper bound of `5σ` is not explicitly derived anywhere in the text. The optimistic, pre-systematics range is `5.2-5.5σ`. After accounting for individual major systematics like GR projections (`σ_GR=0.5`) or `b_phi` uncertainty (30%), the significance drops to `~4.3σ` or `~4.1σ`, respectively. The `5σ` upper bound for the "realistic" range appears arbitrary and overly optimistic.
    *   **Fix:** The authors must provide a clear, step-by-step derivation for the `5σ` upper bound of the realistic range, specifying which systematics are included or excluded to reach this number. Alternatively, if this number cannot be robustly justified, the authors should revise the range to reflect a consistently derived upper bound (e.g., `~2.6-4.3σ`, corresponding to the `σ_GR=0.5` case) in the abstract and all relevant sections of the main text.

*   **P2-M2: Unjustified Shot-Noise Degradation Estimate (Section IV, Page 10)**
    *   **Problem:** In the "Shot-noise caveat" subsection, the authors discuss anomaly-selected tracers with low number density (`ñ ~ 10⁻⁵ h³ Mpc⁻³`). They state that for these tracers, "the bispectrum estimator effective degradation at the squeezed-limit modes that dominate f_NL sensitivity is moderate, 15-30%". This quantitative claim is a key justification for the potential of these tracers, but it is presented without a derivation or citation. The preceding power-spectrum-based estimate suggests a much larger degradation (`~3.3x`), making the "moderate" 15-30% claim for the bispectrum non-obvious and requiring strong support.
    *   **Fix:** Provide a derivation or a specific citation to a paper that computes this 15-30% degradation for a bispectrum estimator in this low-density regime. Without this support, the claim is an unverified assertion and should be removed or rephrased as a qualitative statement.

*   **P2-M3: Garbled Derivation in Appendix A (Page 25)**
    *   **Problem:** Appendix A aims to clarify the normalization conventions for the bispectrum, which is crucial. However, the derivation mapping the `Φ`-field bispectrum to the `ζ`-field bispectrum is confusing and appears to contain typos. The text states: `(Βς = (5/3)³ · 2fNL P[...] = (5/3)³(3/5)⁴ · 2fNL P[...])`. The second equality is incorrect. While the final conclusion that the `f_NL` parameter is the same quantity in both conventions is correct, the presented derivation is flawed and undermines the authority of this important appendix.
    *   **Fix:** Rewrite the derivation of the mapping between `B_Φ` and `B_ζ` local-template normalizations. The correct relation is `(5/3)³ B_Φ = (6/5)f_NL [P_ζ(k1)P_ζ(k2) + perms]`, and `B_Φ = 2f_NL [P_Φ(k1)P_Φ(k2) + perms]`. The authors should show explicitly how these standard definitions lead to a consistent `f_NL`.

#### MINOR

*   **P2-m1: Ambiguous Phrasing of Li et al. Result in Abstract (Page 1)**
    *   **Problem:** The abstract mentions "The Li et al. [7] value f_NL = -35/16". While the body and Appendix A correctly and strongly argue that this is an incomplete intermediate result from a single time-ordering and not a physical alternative, the abstract's phrasing could be misinterpreted by a casual reader as a competing physical prediction.
    *   **Fix:** Rephrase the sentence in the abstract to make it clear from the outset that the `-35/16` value is used as a stress test for the calculation's robustness and does not represent a physical model, for example: "As a robustness test of the calculation, we show that using the incomplete, single-time-ordering intermediate value f_NL = -35/16 from Li et al. [7] would halve the significance..."

*   **P2-m2: Late Clarification of Multiple Fisher Analyses (Page 22)**
    *   **Problem:** The paper uses two distinct Fisher analyses: a primary one for the galaxy bispectrum (from Heinrich et al.) and a secondary one for the joint `(f_NL, n_fNL)` constraints from scale-dependent bias. The explicit clarification that these are separate and not competing analyses comes very late in the paper (Sec. IX.D, p. 22). This could cause confusion for readers trying to reconcile the different `σ(f_NL)` values quoted.
    *   **Fix:** Move the clarification from Sec. IX.D to a more prominent, earlier position, such as the introduction or the beginning of the main forecast section (Sec. IV). This will help the reader understand the scope and hierarchy of the forecasts presented from the start.

*   **P2-m3: In-text References to Code Artifacts (Page 3, 4)**
    *   **Problem:** The text contains direct references to internal script names, e.g., `(artifact c9i_epsilon_ratio_check.json)` and `(implementation in null_space_analysis.py)`. While this points towards excellent reproducibility, it is stylistically unconventional for a formal publication and breaks the reading flow.
    *   **Fix:** Rephrase to refer more generally to the code provided in the repository, e.g., "as verified by our numerical analysis (see the code repository for implementation details)". The specific filenames are best left to the repository's documentation.

*   **P2-m4: Meta-Commentary on Paper Structure (Page 23)**
    *   **Problem:** The "Channel hierarchy and sub-labeling note" contains the sentence: "This subsection (Sec. IX.D in the standard Physical Review D sectioning of the submitted manuscript) reports...". This is self-referential meta-commentary that is inappropriate for the final version of a paper.
    *   **Fix:** Remove this parenthetical and rewrite the paragraph to simply present the scientific content without commenting on its place in the paper's structure.

*   **P2-m5: Key Result in a Footnote (Page 15, Table II)**
    *   **Problem:** Footnote `b` of Table II contains the important result that GR marginalization reduces the delta-prior Bayes factor from `~17` to `~14`. This is a significant quantitative result that is buried in a footnote.
    *   **Fix:** Move this result into the main body of the text in Sec. VI.C to give it the appropriate prominence.

#### NIT

*   **P2-N1: Abstract Phrasing of Bayes Factor (Page 1)**
    *   **Problem:** The abstract states a detection "favors the bounce ... at Bayes factor BF ≈ 9 ... up to BF ≈ 14". Later, it gives the range as `BF ≈ 9-14`. The first phrasing is slightly ambiguous.
    *   **Fix:** For clarity and consistency, use the range format throughout the abstract: "...favors the bounce ... at a Bayes factor of BF ≈ 9-14, where the range spans from the recommended theoretical prior to the theoretical maximum."

---
### Summary recommendation

**MAJOR REVISIONS**

This is a valuable and timely paper that performs a rigorous and much-needed analysis of the observability of the matter bounce scenario. The clarification of the `f_NL = -35/8` prediction, the novel analysis of the polynomial null space, and the detailed, reproducible systematic budget are significant contributions. However, the manuscript in its current form contains several major flaws, including an insufficiently justified headline significance range, an unsupported quantitative claim regarding shot noise, and a garbled key derivation in the appendix. These issues must be thoroughly addressed to meet the standards of Physical Review D. I recommend that the paper be reconsidered for publication after major revisions are made to correct these points.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the completed second-pass review.

================================================================
**Referee Report on "Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook"**

**Manuscript ID:** [Assigned by journal]
**Authors:** Houston Golden
**Journal:** Physical Review D

This paper presents a detailed sensitivity forecast for testing the matter bounce cosmological model using upcoming large-scale structure surveys, primarily SPHEREx. The central prediction of the quasi-dust matter bounce is a local-type non-Gaussianity with amplitude `f_NL = -35/8`. The work is a "recast" of existing forecasts, focusing on a comprehensive treatment of the template mismatch between the bounce bispectrum and the standard local template, and a thorough analysis of systematic uncertainties. Key contributions include the quantification of the template overlap factor `r`, an analysis of the impact of an underdetermined polynomial basis for the bispectrum shape, a resolution of a factor-of-two discrepancy in the literature regarding the predicted `f_NL` value, and a Bayesian model comparison to assess the discriminating power against inflationary alternatives.

The paper is well-structured, methodologically sound in its core components, and addresses a timely and important question in observational cosmology. The detailed treatment of systematics and the focus on reproducibility are commendable. However, several major issues related to the justification of key quantitative claims, clarity in theoretical derivations, and the presentation of headline results must be addressed before the manuscript can be considered for publication in Physical Review D.

---
### Detailed Findings

#### ESSENTIAL

*   **P2-E1: Production Artifact (Page 29)**
    *   **Problem:** The manuscript file contains reviewer metadata at the very end: `[REVIEWER METADATA — NOT PART OF THE PAPER — DO NOT FLAG AS ARTIFACTS] ... [END REVIEWER METADATA]`. This is a production artifact that must be removed.
    *   **Fix:** Remove the entire metadata block from the manuscript source.

*   **P2-E2: Placeholder in Data Availability Section (Page 24)**
    *   **Problem:** The "DATA AND CODE AVAILABILITY" section contains the placeholder text: `(DOI inserted at submission)`.
    *   **Fix:** Replace the placeholder with the actual DOI for the archived data and code, or remove the parenthetical if a DOI is not yet available, ensuring the final version is compliant with journal policy.

#### MAJOR

*   **P2-M1: Unjustified "Realistic" Significance Range (Abstract, Page 1; Section IV, Page 10)**
    *   **Problem:** The abstract and main text quote a "realistic" detection significance range of `~2.6-5σ` for SPHEREx. While the lower bound of `2.6σ` is meticulously derived in Table IV as the most conservative, all-combined scenario, the upper bound of `5σ` is not explicitly derived anywhere in the text. The optimistic, pre-systematics range is `5.2-5.5σ`. After accounting for individual major systematics like GR projections (`σ_GR=0.5`) or `b_phi` uncertainty (30%), the significance drops to `~4.3σ` or `~4.1σ`, respectively. The `5σ` upper bound for the "realistic" range appears arbitrary and overly optimistic.
    *   **Fix:** The authors must provide a clear, step-by-step derivation for the `5σ` upper bound of the realistic range, specifying which systematics are included or excluded to reach this number. Alternatively, if this number cannot be robustly justified, the authors should revise the range to reflect a consistently derived upper bound (e.g., `~2.6-4.3σ`, corresponding to the `σ_GR=0.5` case) in the abstract and all relevant sections of the main text.

*   **P2-M2: Unjustified Shot-Noise Degradation Estimate (Section IV, Page 10)**
    *   **Problem:** In the "Shot-noise caveat" subsection, the authors discuss anomaly-selected tracers with low number density (`ñ ~ 10⁻⁵ h³ Mpc⁻³`). They state that for these tracers, "the bispectrum estimator effective degradation at the squeezed-limit modes that dominate f_NL sensitivity is moderate, 15-30%". This quantitative claim is a key justification for the potential of these tracers, but it is presented without a derivation or citation. The preceding power-spectrum-based estimate suggests a much larger degradation (`~3.3x`), making the "moderate" 15-30% claim for the bispectrum non-obvious and requiring strong support.
    *   **Fix:** Provide a derivation or a specific citation to a paper that computes this 15-30% degradation for a bispectrum estimator in this low-density regime. Without this support, the claim is an unverified assertion and should be removed or rephrased as a qualitative statement.

*   **P2-M3: Garbled Derivation in Appendix A (Page 25)**
    *   **Problem:** Appendix A aims to clarify the normalization conventions for the bispectrum, which is crucial. However, the derivation mapping the `Φ`-field bispectrum to the `ζ`-field bispectrum is confusing and appears to contain typos. The text states: `(Βς = (5/3)³ · 2fNL P[...] = (5/3)³(3/5)⁴ · 2fNL P[...])`. The second equality is incorrect. While the final conclusion that the `f_NL` parameter is the same quantity in both conventions is correct, the presented derivation is flawed and undermines the authority of this important appendix.
    *   **Fix:** Rewrite the derivation of the mapping between `B_Φ` and `B_ζ` local-template normalizations. The correct relation is `(5/3)³ B_Φ = (6/5)f_NL [P_ζ(k1)P_ζ(k2) + perms]`, and `B_Φ = 2f_NL [P_Φ(k1)P_Φ(k2) + perms]`. The authors should show explicitly how these standard definitions lead to a consistent `f_NL`.

*   **P2-M4: Inconsistent and Dimensionally Incorrect Definition of `B_NL` (Eq. 2, p. 3)**
    *   **Problem:** The definition of the "configuration-dependent nonlinearity amplitude" `B_NL` in Eq. (2) is dimensionally inconsistent. As written, the right-hand side has units of inverse momentum cubed (`1/k³`), whereas this quantity is used throughout the paper (e.g., in Figure 1 and Table I) as a dimensionless, scale-free shape function whose squeezed limit is the constant `f_NL = -35/8`. This is a fundamental error in the presentation of the model's central prediction.
    *   **Fix:** The authors must correct this definition. They should likely define the dimensionless shape function `S(k1, k2, k3)` in the standard way and then define `B_NL` as this shape function, or simply use `S`. The equation should be rewritten to be dimensionally consistent and to correctly show that its squeezed limit yields a constant value.

#### MINOR

*   **P2-m1: Ambiguous Phrasing of Li et al. Result in Abstract (Page 1)**
    *   **Problem:** The abstract mentions "The Li et al. [7] value f_NL = -35/16". While the body and Appendix A correctly and strongly argue that this is an incomplete intermediate result from a single time-ordering and not a physical alternative, the abstract's phrasing could be misinterpreted by a casual reader as a competing physical prediction.
    *   **Fix:** Rephrase the sentence in the abstract to make it clear from the outset that the `-35/16` value is used as a stress test for the calculation's robustness and does not represent a physical model, for example: "As a robustness test of the calculation, we show that using the incomplete, single-time-ordering intermediate value f_NL = -35/16 from Li et al. [7] would halve the significance..."

*   **P2-m2: Late Clarification of Multiple Fisher Analyses (Page 22)**
    *   **Problem:** The paper uses two distinct Fisher analyses: a primary one for the galaxy bispectrum (from Heinrich et al.) and a secondary one for the joint `(f_NL, n_fNL)` constraints from scale-dependent bias. The explicit clarification that these are separate and not competing analyses comes very late in the paper (Sec. IX.D, p. 22). This could cause confusion for readers trying to reconcile the different `σ(f_NL)` values quoted.
    *   **Fix:** Move the clarification from Sec. IX.D to a more prominent, earlier position, such as the introduction or the beginning of the main forecast section (Sec. IV). This will help the reader understand the scope and hierarchy of the forecasts presented from the start.

*   **P2-m3: In-text References to Code Artifacts (Page 3, 4)**
    *   **Problem:** The text contains direct references to internal script names, e.g., `(artifact c9i_epsilon_ratio_check.json)` and `(implementation in null_space_analysis.py)`. While this points towards excellent reproducibility, it is stylistically unconventional for a formal publication and breaks the reading flow.
    *   **Fix:** Rephrase to refer more generally to the code provided in the repository, e.g., "as verified by our numerical analysis (see the code repository for implementation details)". The specific filenames are best left to the repository's documentation.

*   **P2-m4: Meta-Commentary on Paper Structure (Page 23)**
    *   **Problem:** The "Channel hierarchy and sub-labeling note" contains the sentence: "This subsection (Sec. IX.D in the standard Physical Review D sectioning of the submitted manuscript) reports...". This is self-referential meta-commentary that is inappropriate for the final version of a paper.
    *   **Fix:** Remove this parenthetical and rewrite the paragraph to simply present the scientific content without commenting on its place in the paper's structure.

*   **P2-m5: Key Result in a Footnote (Page 15, Table II)**
    *   **Problem:** Footnote `b` of Table II contains the important result that GR marginalization reduces the delta-prior Bayes factor from `~17` to `~14`. This is a significant quantitative result that is buried in a footnote.
    *   **Fix:** Move this result into the main body of the text in Sec. VI.C to give it the appropriate prominence.

*   **P2-m6: Unexplained Range in Table IV (p. 20)**
    *   **Problem:** The `b_phi` (50%, conserv.) row in Table IV gives a detection significance of `~3.5-3.7σ`. Based on the table's caption, which states a fixed `r=0.84` is used for the significance calculation, the value should be a single number, `3.68σ`. The source of the quoted range is not explained and appears inconsistent with the calculation rules provided.
    *   **Fix:** Clarify the origin of this range or correct the value to the single, derivable number.

*   **P2-m7: Potential Dimensional Inconsistency in SDB Kernel (Eq. 4, p. 7)**
    *   **Problem:** The definition of the Poisson-Newtonian transfer kernel `M(k,z)` in Eq. (4) appears to be dimensionally inconsistent, as it lacks the necessary factors (e.g., of the scale factor `a(z)`) to make it a dimensionless quantity.
    *   **Fix:** The authors should verify their definition against the standard literature (e.g., Slosar et al. 2008) and provide the correct, dimensionally consistent formula.

#### NIT

*   **P2-N1: Abstract Phrasing of Bayes Factor (Page 1)**
    *   **Problem:** The abstract states a detection "favors the bounce ... at Bayes factor BF ≈ 9 ... up to BF ≈ 14". Later, it gives the range as `BF ≈ 9-14`. The first phrasing is slightly ambiguous.
    *   **Fix:** For clarity and consistency, use the range format throughout the abstract: "...favors the bounce ... at a Bayes factor of BF ≈ 9-14, where the range spans from the recommended theoretical prior to the theoretical maximum."

*   **P2-N2: Imprecise Cross-Reference for `r` Definition (p. 8)**
    *   **Problem:** The text refers to `Eq. 5` in the context of defining the amplitude recovery factor `r`. However, `Eq. 5` shows how `r` is used to correct `σ(f_NL)`, while the explicit definition of `r` as a weighted average of `B_NL` is given only in the surrounding prose.
    *   **Fix:** The reference should be to the text preceding the equation, not to the equation itself.

---
### Summary recommendation

**MAJOR REVISIONS**

This is a valuable and timely paper that performs a rigorous and much-needed analysis of the observability of the matter bounce scenario. The clarification of the `f_NL = -35/8` prediction, the novel analysis of the polynomial null space, and the detailed, reproducible systematic budget are significant contributions. However, the manuscript in its current form contains several major flaws, including a fundamentally incorrect definition of the bispectrum shape function, an insufficiently justified headline significance range, an unsupported quantitative claim regarding shot noise, and a garbled key derivation in the appendix. These issues must be thoroughly addressed to meet the standards of Physical Review D. I recommend that the paper be reconsidered for publication after major revisions are made to correct these points.
================================================================