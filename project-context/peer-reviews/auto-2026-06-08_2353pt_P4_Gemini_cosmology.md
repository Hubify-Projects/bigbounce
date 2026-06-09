# P4 auto-2026-06-08_2353pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (9156 chars)
**Wall time**: 180.5s

---

**Referee Report: PRD MS# [Internal ID]**
**Title:** Survey-Scale Galaxy Chirality with Equivariant TTA: A -0.122σ Subsample-Mask l=1 Null, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)
**Author(s):** Houston Golden

This paper presents a detailed analysis of galaxy chirality asymmetry using 8.47 million galaxies from the DESI Legacy Surveys. The primary scientific result is a null detection of a cosmological dipole (l=1) in the chirality map, constrained at the sub-percent level. The authors perform an exceptionally rigorous analysis, identifying and quantifying a key systematic effect—monopole-mask leakage—that can produce spurious dipole signals. They convincingly argue that a statistically significant residual found on a specific survey footprint is of systematic, not cosmological, origin.

The methodology is state-of-the-art, employing a Vision Transformer for classification, test-time averaging to enforce equivariance, and the MASTER algorithm for power spectrum estimation. The paper is well-structured, with a clear hierarchy of estimators and a comprehensive suite of systematic checks detailed in the appendices. The distinction between the parity-even l=1 dipole observable and parity-odd observables (l=0, even-l) is correctly handled. The public release of the catalog, model, and analysis code is commendable and sets a high standard for reproducibility.

The paper is of high quality and suitable for publication in Physical Review D, pending minor revisions. The findings are significant, providing a strong null constraint on isotropy-breaking physics and serving as a crucial methodological benchmark for future studies in this area.

---
### Detailed Findings

#### ESSENTIAL

*   **P4-E1:** Section: Figure 4 (and caption), Page 8.
    *   **Problem:** The caption for Figure 4 does not match the figure shown. The caption text describes a two-panel figure ("Top: l=1 dipole power. Bottom: l=2 quadrupole.") while the figure itself is a single panel showing five multipole bins (l=1 to l=5).
    *   **Required Fix:** The caption must be rewritten to accurately describe the content of the figure as presented, which appears to be the binned angular power spectrum from l=1 to l=5. Alternatively, the figure can be replaced to match the current caption.

#### MAJOR

(None)

#### MINOR

*   **P4-M1:** Section: IV D, Table IV, Page 6.
    *   **Problem:** The z-score for the "Pre-MASTER pseudo-C(l=1)" statistic is reported as +1.68. A direct calculation from the numbers provided in the "Data" and "Null" columns yields z = (1.696 - 1.685) / 0.007 = 1.57.
    *   **Required Fix:** Please verify this calculation. If the discrepancy is due to rounding of the displayed numbers, please either use higher precision in the table or add a footnote explaining that the z-score was calculated with unrounded values. The conclusion is not affected, but the numerical inconsistency should be resolved.

*   **P4-M2:** Section: VII. Conclusions, Page 8.
    *   **Problem:** In conclusion point 'b', the real-space dipole significance is quoted as "0.436". Throughout the rest of the paper (e.g., Abstract, Table I, Section IV C), this value is given as "+0.43σ".
    *   **Required Fix:** Please ensure this value is quoted consistently throughout the manuscript. Using two significant figures (+0.43σ) seems appropriate given the context.

#### NIT (Cosmetic)

*   **P4-N1:** Section: Title, Page 1.
    *   **Problem:** The title uses inconsistent capitalization and precision. "A -0.1220" has a trailing zero suggesting higher precision than is likely warranted or used elsewhere (e.g., -0.122σ). "a Quantifiable Monopole-Mask Leakage Channel" starts with a lowercase 'a'.
    *   **Required Fix:** Suggest revising for consistency, e.g., "A -0.122σ Subsample-Mask l=1 Null, A Quantifiable Monopole-Mask Leakage Channel...". Also, consider if "3.2 Million Spirals" is better stated as "3.2 Million Spiral Galaxies" for clarity.

*   **P4-N2:** Section: Table III, Page 6.
    *   **Problem:** The header for the "Significance" column is "(0)". This appears to be a typo.
    *   **Required Fix:** Please change the header to "(σ)" to represent standard deviation units.

*   **P4-N3:** Section: Abstract, Page 1.
    *   **Problem:** The sentence "The +3.64σ canonical-mask residual is consistent with monopole leakage through survey geometry (Sec. IVD) and is not interpreted as a cosmological signal" is slightly imprecise. Section IV D and Table IV show that monopole leakage explains the *pre-MASTER* signal at 99.3%, leaving a +1.68σ residual. The +3.64σ is the *post-MASTER* residual, which is attributed to a more complex combination of systematics (as detailed in Appendix D), not just the simple monopole-leakage channel.
    *   **Required Fix:** Suggest rephrasing for clarity, for example: "The +3.64σ post-MASTER canonical-mask residual is attributed to systematics, as supported by a detailed analysis (Appendix D), and is not interpreted as a cosmological signal. We demonstrate that a related pre-MASTER signal is almost entirely explained by monopole leakage through the survey geometry (Sec. IV D)."

*   **P4-N4:** Section: PACS numbers, Page 1.
    *   **Problem:** The PACS number 98.62.Ai ("Origin, formation, and abundances of the elements") seems less relevant than other possible choices.
    *   **Required Fix:** Consider replacing it with a more directly relevant code, such as 98.62.Py ("Distances, redshifts, radial velocities; spatial distribution of galaxies") or 98.52.Nr ("Spiral galaxies"). This is a minor suggestion.

---
## Summary recommendation

**ACCEPT WITH MINOR CORRECTIONS**

The paper presents a robust and high-impact null result on the galaxy chirality dipole. The authors' treatment of systematics is exemplary, particularly their identification and quantification of the monopole-mask leakage channel. This work represents a significant advance in the field, both in terms of the statistical power of the dataset and the methodological rigor of the analysis. The paper is well-written, transparent, and provides all necessary materials for reproducibility. After addressing the minor corrections listed above, primarily the figure caption mismatch, the paper will be an excellent contribution to Physical Review D.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the revised review, incorporating the new findings from the more rigorous second pass.

================================================================
**Referee Report: PRD MS# [Internal ID]**
**Title:** Survey-Scale Galaxy Chirality with Equivariant TTA: A -0.122σ Subsample-Mask l=1 Null, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)
**Author(s):** Houston Golden

This paper presents a detailed analysis of galaxy chirality asymmetry using 8.47 million galaxies from the DESI Legacy Surveys. The primary scientific result is a null detection of a cosmological dipole (l=1) in the chirality map, constrained at the sub-percent level. The authors perform an exceptionally rigorous analysis, identifying and quantifying a key systematic effect—monopole-mask leakage—that can produce spurious dipole signals. They convincingly argue that a statistically significant residual found on a specific survey footprint is of systematic, not cosmological, origin.

The methodology is state-of-the-art, employing a Vision Transformer for classification, test-time averaging to enforce equivariance, and the MASTER algorithm for power spectrum estimation. The paper is well-structured, with a clear hierarchy of estimators and a comprehensive suite of systematic checks detailed in the appendices. The distinction between the parity-even l=1 dipole observable and parity-odd observables (l=0, even-l) is correctly handled. The public release of the catalog, model, and analysis code is commendable and sets a high standard for reproducibility.

The paper is of high quality and suitable for publication in Physical Review D. However, a number of significant clarity issues, particularly regarding the presentation of results in the abstract, figures, and tables, must be addressed before publication. The findings are significant, providing a strong null constraint on isotropy-breaking physics and serving as a crucial methodological benchmark for future studies in this area.

---
### Detailed Findings

#### ESSENTIAL

(None)

#### MAJOR

*   **P4-M1:** Section: Abstract, Page 1.
    *   **Problem:** The abstract contains a misleading statement that conflates the pre- and post-correction systematic signals. The sentence "The +3.64σ canonical-mask residual is consistent with monopole leakage through survey geometry (Sec. IV D)..." is incorrect. The +3.64σ is the *post-MASTER* residual, which remains *after* the mode-decoupling procedure. The monopole leakage described in Sec. IV D is shown to explain the large *pre-MASTER* signal. The abstract, therefore, incorrectly links the final, unexplained residual to the specific leakage channel that was already corrected for by the analysis pipeline. This is a critical point for understanding the paper's results and must be clarified.
    *   **Required Fix:** The abstract must be rephrased to clearly distinguish between the pre-MASTER signal (which is almost fully explained by monopole-mask leakage) and the post-MASTER residual (which is attributed to a different, more complex set of systematics detailed in Appendix D).

*   **P4-M2:** Section: Figure 4 and Table III, Pages 6 & 8.
    *   **Problem:** The presentation of the angular power spectrum results for the canonical mask is confusing and inconsistent across Figure 4, Table III, and the main text.
        1.  **Figure/Caption Mismatch:** The caption for Figure 4 describes a two-panel figure ("Top: l=1... Bottom: l=2..."), while the figure itself is a single panel showing five multipole bins (l=1 to l=5).
        2.  **Contradictory Information:** The caption claims "The post-MASTER residual is +3.64σ", but the l=1 bar in the plot is clearly *not* significant and is consistent with the null. This is a direct contradiction.
        3.  **Incomplete/Unverifiable Table:** Table III, which should present these results, omits the key l=1 result (+3.64σ) for the canonical mask. Furthermore, the significance values for the bandpowers (e.g., +6.097σ for leff=4) cannot be verified because the mean of the null simulations, `<C_null>`, is not provided.
        4.  **Apparent Inconsistency:** The data shown in Figure 4 (e.g., l=2 at ~2.7σ) do not appear to be consistent with the bandpower significances in Table III (e.g., the bandpower including l=2 is at +6.1σ). The relationship between the two is not explained.
    *   **Required Fix:** This entire section of the results presentation needs to be revised for clarity and consistency. (1) Rewrite the Figure 4 caption to match the figure. (2) Ensure the data plotted in Figure 4 is clearly explained and consistent with the text. (3) Revise Table III to include the l=1 result for the canonical mask and provide all necessary information (e.g., `<C_null>`) to make the significance values verifiable.

#### MINOR

*   **P4-m1:** Section: IV D, Table I & Table IV, Pages 4 & 6.
    *   **Problem:** The z-score for the "Pre-MASTER pseudo-C(l=1)" statistic (Table IV) and the corresponding "monopole+mask null" estimator (Table I) is reported as +1.68σ. A direct calculation from the numbers provided in Table IV yields z = (1.696e-2 - 1.685e-2) / 0.007e-2 = 1.57.
    *   **Required Fix:** Please verify this calculation. If the discrepancy is due to rounding, please use higher precision in the table or add a footnote. The numerical inconsistency should be resolved.

*   **P4-m2:** Section: Table II, Page 4.
    *   **Problem:** The values in the "Dev. (σ)" column are not reproducible from the other columns. For example, for Tier C, (0.4974 - 0.5) / 0.000279 = -9.32, but the table reports 9.5 (with a missing sign). All three rows have similar discrepancies.
    *   **Required Fix:** Please re-calculate and correct the values in this column or explain the calculation method.

*   **P4-m3:** Section: VII. Conclusions, Page 8.
    *   **Problem:** In conclusion point 'b', the real-space dipole significance is quoted as "0.436". Throughout the rest of the paper (e.g., Abstract, Table I, Section IV C), this value is given as "+0.43σ".
    *   **Required Fix:** Please ensure this value is quoted consistently throughout the manuscript. Using two significant figures (+0.43σ) seems appropriate.

*   **P4-m4:** Section: Figure 4 caption, Page 8.
    *   **Problem:** The caption references `(Table IV)`. This appears incorrect. The caption discusses the `post-MASTER residual` (+3.64σ), which is a power spectrum result related to Table III. Table IV details the `pre-MASTER` monopole-leakage null.
    *   **Required Fix:** Please correct the table reference.

#### NIT (Cosmetic)

*   **P4-N1:** Section: Title, Page 1.
    *   **Problem:** The title uses inconsistent capitalization and precision. "A -0.1220" has a trailing zero suggesting higher precision than is likely warranted or used elsewhere (e.g., -0.122σ). "a Quantifiable Monopole-Mask Leakage Channel" starts with a lowercase 'a'.
    *   **Required Fix:** Suggest revising for consistency, e.g., "A -0.122σ Subsample-Mask l=1 Null, A Quantifiable Monopole-Mask Leakage Channel...". Also, consider if "3.2 Million Spirals" is better stated as "3.2 Million Spiral Galaxies" for clarity.

*   **P4-N2:** Section: Table III, Page 6.
    *   **Problem:** The header for the "Significance" column is "(0)". This appears to be a typo.
    *   **Required Fix:** Please change the header to "(σ)" to represent standard deviation units.

*   **P4-N3:** Section: Abstract, Page 1.
    *   **Problem:** The text states the pre-MASTER signal is "reproduced at 99.3% of its observed amplitude". The calculation provided in Table IV is for power (pseudo-C_l), not amplitude. A 99.3% reproduction of power corresponds to a 99.7% reproduction of amplitude.
    *   **Required Fix:** For precision, please change "amplitude" to "power" in this sentence.

*   **P4-N4:** Section: PACS numbers, Page 1.
    *   **Problem:** The PACS number 98.62.Ai ("Origin, formation, and abundances of the elements") seems less relevant than other possible choices.
    *   **Required Fix:** Consider replacing it with a more directly relevant code, such as 98.62.Py ("Distances, redshifts, radial velocities; spatial distribution of galaxies") or 98.52.Nr ("Spiral galaxies"). This is a minor suggestion.

---
## Summary recommendation

**ACCEPT WITH MAJOR CORRECTIONS**

The paper presents a robust and high-impact null result on the galaxy chirality dipole. The authors' treatment of systematics is exemplary. This work represents a significant advance in the field, both in terms of the statistical power of the dataset and the methodological rigor of the analysis. However, the manuscript currently suffers from several major clarity issues in the presentation of its key results, most notably in the abstract's summary and in the figures and tables related to the power spectrum analysis. These inconsistencies obscure the paper's logical flow and must be thoroughly addressed. After these major corrections are made, the paper will be an excellent contribution to Physical Review D.