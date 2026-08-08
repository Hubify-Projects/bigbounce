# P1A D1 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/arxiv/paper1a_ech_nogo.pdf` md5=198cb994 pages=29
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (14434 chars)
**Wall time**: 178.2s

---

# Referee Report on "Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter"

## Summary of the Paper
This manuscript presents a comprehensive theoretical and phenomenological assessment of four minimal Einstein-Cartan-Holst (ECH) spin-torsion channels as potential sources for late-time dark energy. The authors conclude that all four enumerated routes are closed under a set of stated assumptions. Three routes (NJL contact, one-loop corrections, Immirzi running) are found to be amplitude-suppressed, while the fourth (parity-odd CMB coupling) is closed by a naturalness objection, as it re-imports the cosmological constant fine-tuning problem. The paper's central theoretical result is a "perturbation transparency" theorem, demonstrating that for canonical scalar matter, the Holst sector of ECH gravity decouples from all scalar and tensor perturbation equations of motion. The authors also identify a structural tension between the number of e-folds required for the dark energy mechanism and the number that would erase the observable matter-bounce non-Gaussianity signature (fNL = -35/8). The paper concludes by highlighting two "surviving" but ECH-independent, class-level predictions: the matter-bounce fNL signature and spectator-ALP cosmic birefringence.

## General Comments
The paper is exceptionally thorough, systematic, and well-structured. The authors tackle a complex subject with admirable clarity and intellectual honesty. The systematic cataloging of 14 distinct constraints (Barriers A-N) is a valuable contribution, providing a clear framework for assessing ECH cosmology. The perturbation-transparency result is a particularly elegant and important finding, cleanly delineating where ECH effects can and cannot manifest. The authors are also to be commended for their transparency regarding the assumptions underpinning their analysis, particularly the phenomenological nature of the dark-energy scaling ansatz.

Despite these significant strengths, the manuscript in its current form has several major issues that preclude publication in Physical Review D. The most severe is its heavy reliance on unpublished companion papers for essential results and inputs. Furthermore, key parts of the dark-energy argument rest on non-rigorous, "aesthetic" derivations that need to be better justified or de-emphasized in favor of more robust arguments presented elsewhere in the paper.

The following detailed points must be addressed.

---
## Detailed Findings

### ESSENTIAL Revisions

**P1A-E1: Reliance on unpublished companion papers**
-   **Section/Page:** Throughout the paper, including but not limited to p. 4 (Table I footnote), p. 5 (Fig. 1 caption), p. 10 (Sec. III B), p. 15 (Sec. V), p. 20 (Sec. X G).
-   **Problem:** The manuscript's arguments and quantitative claims are critically dependent on results from at least four companion papers ([2], [6], [23], [46]) which are cited as "in preparation" or "posted concurrently on arXiv". This is not an acceptable practice for a peer-reviewed publication, which must be verifiable and self-contained. Specific examples include:
    1.  The cosmological parameter values (e.g., H₀ = 67.68 ± 1.06) are taken from an MCMC analysis in Paper I(b) [6].
    2.  The "Confirmed Null" result for galaxy spin asymmetry, which closes an observational channel, is from Paper IV [23].
    3.  The detailed SPHEREx forecast for fNL, including the systematic budget, is in Paper II [2].
    4.  The NANOGrav 15-yr reanalysis yielding γ_PTA = 2.567 ± 0.382 is from Paper III [46].
-   **Required Fix:** The manuscript must be made self-contained. For each piece of essential information drawn from an unpublished source, the authors must either: (a) wait for the companion papers to be accepted and citable with a stable reference (journal or arXiv), or (b) incorporate a summary of the methods and results into the present manuscript, for instance in appendices. This summary must be sufficient for a referee and reader to understand and provisionally accept the validity of the input. For example, a minimal MCMC setup, dataset list, and posterior table should be provided for the cosmological parameters.

### MAJOR Revisions

**P1A-M1: Non-rigorous derivation of the inflationary dilution factor**
-   **Section/Page:** Sec. II C 1 (p. 8), Sec. XII A (p. 21), Appendix B (p. 26).
-   **Problem:** The entire ECH dark-energy mapping relies on the inflationary dilution factor D_inf (Eq. 11), which contains a prefactor (T_reh/M_GUT)^(3/2). The paper frankly describes the justification for this term's 3/2 exponent as a "dimensional-analysis aesthetic" and not a rigorous calculation. This is a significant weakness in the logical chain connecting the bounce to dark energy, and it determines the required number of e-folds (N_tot ≈ 92) that is central to the paper's "structural tension" argument.
-   **Required Fix:** The authors must significantly strengthen the justification for this prefactor. If a rigorous derivation is not possible, they should provide a more detailed physical argument, perhaps drawing analogies from other areas of thermal field theory. More importantly, the overall argument should be restructured to place greater emphasis on the independent "reheating thermal-reset barrier" (p. 9), which provides a more robust closure of the dark-energy channel without relying on this specific prefactor. The paper's conclusions are much stronger if they rest on the thermal washout mechanism, with the N_tot calculation presented as a conditional, model-dependent constraint.

**P1A-M2: Unclear origin of the SPHEREx fNL forecast significance range**
-   **Section/Page:** Abstract (p. 1), Table I footnote 'b' (p. 4), Sec. VII (p. 15), footnote 6 (p. 16).
-   **Problem:** The paper quotes a "2.6-5σ" realistic significance for the SPHEREx test of fNL = -35/8. While the abstract correctly notes that the values arise from different null procedures, the text does not provide a clear derivation for this specific range. Footnote 6 (p. 16) explains values from ~4.4σ to ~6.25σ based on σ(fNL) values of 1.0 and 0.7, respectively. The origin of the lower 2.6σ bound is not explained and appears inconsistent with the provided numbers.
-   **Required Fix:** The authors must provide a transparent, step-by-step derivation for the entire quoted significance range. This should include the specific assumptions (e.g., systematic degradation models, analysis choices) that lead to each value in the range. A small table summarizing the different forecast scenarios (e.g., Ideal, Optimistic, Pessimistic) with their corresponding σ(fNL) and resulting significance (|fNL|/σ) would greatly improve clarity and credibility.

**P1A-M3: Contextualizing the scope of the "Perturbation Transparency" Result**
-   **Section/Page:** Abstract (p. 1), Sec. X (p. 19-20).
-   **Problem:** The perturbation transparency theorem is correctly stated to apply to "canonical scalar matter," and Sec. X E correctly lists fermions as a system that would break the transparency. However, the paper does not sufficiently discuss the implications of this limitation for a realistic cosmological history, which includes a standard model fermion bath after reheating.
-   **Required Fix:** The authors should add a dedicated paragraph to discuss the domain of applicability of their theorem. They should clarify that the result is expected to hold during a period of scalar-field-driven inflation where fermion densities are negligible. They must also address what happens after reheating: how do fermions re-introduce torsion, and how are its effects constrained in the late universe? This discussion is crucial for understanding the practical importance and limitations of this otherwise powerful result. (The existing Route 1 analysis already constrains the late-time effects, so this may simply require connecting the arguments).

### MINOR Revisions

**P1A-m1: Redundant Figure**
-   **Section/Page:** Sec. XII B (p. 22).
-   **Problem:** Figure 6, "Detection Significance Forecast," is largely a repetition of the information presented in Figure 4, "Observational decision timeline." It adds little new information and could be removed to improve the manuscript's conciseness.
-   **Required Fix:** The authors should consider removing Figure 6 and ensuring all essential forecast information is contained within Figure 4.

**P1A-m2: Inconsistent σ-value comparison in abstract**
-   **Section/Page:** Abstract (p. 1).
-   **Problem:** The abstract quotes significances for β (3.6σ and 2.9σ) and fNL (2.6-5σ). While it correctly adds the crucial caveat that they "arise from different null procedures and are not directly comparable," presenting them side-by-side in this manner can still be misleading to a casual reader.
-   **Required Fix:** To further improve clarity, consider rephrasing to physically separate these results. For example: "For cosmic birefringence, existing data show hints at ~3σ significance... For non-Gaussianity, forecasts for the SPHEREx mission predict a detection of the matter-bounce signal with a significance in the range of 2.6-5σ, depending on analysis assumptions."

### NITs (Cosmetic)

**P1A-N1: Paper Date**
-   **Section/Page:** p. 1.
-   **Problem:** The paper is dated "June 18, 2026."
-   **Required Fix:** Correct the date to the current submission date.

**P1A-N2: Garbled equation in Abstract**
-   **Section/Page:** Abstract (p. 1).
-   **Problem:** The expression for the physical wavenumber at the bounce appears to be corrupted, likely by the OCR process: "...kphys kbounce ~ KSPHEREX KSPHEREX phys Ntot-Nexit e32 32 kphys KSPHEREX...".
-   **Required Fix:** Please carefully check and correct the typeset equation in the abstract. The intended expression is likely `k_phys(bounce) ~ k_SPHEREx * exp(N_tot - N_exit)`.

**P1A-N3: Bibliographic style**
-   **Section/Page:** References (p. 28-29).
-   **Problem:** The bibliography does not follow a consistent format (e.g., inclusion of arXiv IDs, author list conventions, journal abbreviations).
-   **Required Fix:** Please format the entire bibliography according to the Physical Review D style guide.

---
## Summary Recommendation
**MAJOR REVISIONS**

## Justification
This is a work of significant scope and potential impact. The systematic approach to constraining ECH dark energy is a strength, and the perturbation transparency theorem is a noteworthy result. The authors' commitment to intellectual honesty regarding their assumptions is commendable.

However, the paper cannot be published in its present form. The reliance on unpublished work for multiple, load-bearing results is a critical flaw that violates the core principles of peer-reviewed science. This must be rectified before the paper can be reconsidered. Additionally, the non-rigorous derivation of the dark energy dilution factor needs to be better contextualized, and the quantitative forecast claims require clearer justification.

I recommend that the paper undergo major revisions to address these points. If the authors can successfully make the manuscript self-contained and strengthen the key arguments as outlined above, it will be a very strong candidate for publication in Physical Review D.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the updated referee report, incorporating the findings from the second, more rigorous review.

================================================================
# Referee Report on "Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter"

## Summary of the Paper
This manuscript presents a comprehensive theoretical and phenomenological assessment of four minimal Einstein-Cartan-Holst (ECH) spin-torsion channels as potential sources for late-time dark energy. The authors conclude that all four enumerated routes are closed under a set of stated assumptions. Three routes (NJL contact, one-loop corrections, Immirzi running) are found to be amplitude-suppressed, while the fourth (parity-odd CMB coupling) is closed by a naturalness objection, as it re-imports the cosmological constant fine-tuning problem. The paper's central theoretical result is a "perturbation transparency" theorem, demonstrating that for canonical scalar matter, the Holst sector of ECH gravity decouples from all scalar and tensor perturbation equations of motion. The authors also identify a structural tension between the number of e-folds required for the dark energy mechanism and the number that would erase the observable matter-bounce non-Gaussianity signature (fNL = -35/8). The paper concludes by highlighting two "surviving" but ECH-independent, class-level predictions: the matter-bounce fNL signature and spectator-ALP cosmic birefringence.

## General Comments
The paper is exceptionally thorough, systematic, and well-structured. The authors tackle a complex subject with admirable clarity and intellectual honesty. The systematic cataloging of 14 distinct constraints (Barriers A-N) is a valuable contribution, providing a clear framework for assessing ECH cosmology. The perturbation-transparency result is a particularly elegant and important finding, cleanly delineating where ECH effects can and cannot manifest. The authors are also to be commended for their transparency regarding the assumptions underpinning their analysis, particularly the phenomenological nature of the dark-energy scaling ansatz.

Despite these significant strengths, the manuscript in its current form has several major issues that preclude publication in Physical Review D. The most severe is its heavy reliance on unpublished companion papers for essential results and inputs. Furthermore, key parts of the dark-energy argument rest on operators that are not valid terms in a 4D Lagrangian, a profound weakness that goes beyond the acknowledged non-rigorous derivation of certain prefactors. Several quantitative claims also appear to be arithmetically inconsistent with the provided inputs.

The following detailed points must be addressed.

---
## Detailed Findings

### ESSENTIAL Revisions

**P1A-E1: Reliance on unpublished companion papers**
-   **Section/Page:** Throughout the paper, including but not limited to p. 4 (Table I footnote), p. 5 (Fig. 1 caption), p. 10 (Sec. III B), p. 15 (Sec. V), p. 20 (Sec. X G).
-   **Problem:** The manuscript's arguments and quantitative claims are critically dependent on results from at least four companion papers ([2], [6], [23], [46]) which are cited as "in preparation" or "posted concurrently on arXiv". This is not an acceptable practice for a peer-reviewed publication, which must be verifiable and self-contained. Specific examples include:
    1.  The cosmological parameter values (e.g., H₀ = 67.68 ± 1.06) are taken from an MCMC analysis in Paper I(b) [6].
    2.  The "Confirmed Null" result for galaxy spin asymmetry, which closes an observational channel, is from Paper IV [23].
    3.  The detailed SPHEREx forecast for fNL, including the systematic budget, is in Paper II [2].
    4.  The NANOGrav 15-yr reanalysis yielding γ_PTA = 2.567 ± 0.382 is from Paper III [46].
-   **Required Fix:** The manuscript must be made self-contained. For each piece of essential information drawn from an unpublished source, the authors must either: (a) wait for the companion papers to be accepted and citable with a stable reference (journal or arXiv), or (b) incorporate a summary of the methods and results into the present manuscript, for instance in appendices. This summary must be sufficient for a referee and reader to understand and provisionally accept the validity of the input. For example, a minimal MCMC setup, dataset list, and posterior table should be provided for the cosmological parameters.

### MAJOR Revisions

**P1A-M1: Non-rigorous derivation of the inflationary dilution factor**
-   **Section/Page:** Sec. II C 1 (p. 8), Sec. XII A (p. 21), Appendix B (p. 26).
-   **Problem:** The entire ECH dark-energy mapping relies on the inflationary dilution factor D_inf (Eq. 11), which contains a prefactor (T_reh/M_GUT)^(3/2). The paper frankly describes the justification for this term's 3/2 exponent as a "dimensional-analysis aesthetic" and not a rigorous calculation. This is a significant weakness in the logical chain connecting the bounce to dark energy, and it determines the required number of e-folds (N_tot ≈ 92) that is central to the paper's "structural tension" argument.
-   **Required Fix:** The authors must significantly strengthen the justification for this prefactor. If a rigorous derivation is not possible, they should provide a more detailed physical argument, perhaps drawing analogies from other areas of thermal field theory. More importantly, the overall argument should be restructured to place greater emphasis on the independent "reheating thermal-reset barrier" (p. 9), which provides a more robust closure of the dark-energy channel without relying on this specific prefactor. The paper's conclusions are much stronger if they rest on the thermal washout mechanism, with the N_tot calculation presented as a conditional, model-dependent constraint.

**P1A-M2: Unclear origin of the SPHEREx fNL forecast significance range**
-   **Section/Page:** Abstract (p. 1), Table I footnote 'b' (p. 4), Sec. VII (p. 15), footnote 6 (p. 16).
-   **Problem:** The paper quotes a "2.6-5σ" realistic significance for the SPHEREx test of fNL = -35/8. While the abstract correctly notes that the values arise from different null procedures, the text does not provide a clear derivation for this specific range. Footnote 6 (p. 16) explains values from ~4.4σ to ~6.25σ based on σ(fNL) values of 1.0 and 0.7, respectively. The origin of the lower 2.6σ bound is not explained and appears inconsistent with the provided numbers.
-   **Required Fix:** The authors must provide a transparent, step-by-step derivation for the entire quoted significance range. This should include the specific assumptions (e.g., systematic degradation models, analysis choices) that lead to each value in the range. A small table summarizing the different forecast scenarios (e.g., Ideal, Optimistic, Pessimistic) with their corresponding σ(fNL) and resulting significance (|fNL|/σ) would greatly improve clarity and credibility.

**P1A-M3: Contextualizing the scope of the "Perturbation Transparency" Result**
-   **Section/Page:** Abstract (p. 1), Sec. X (p. 19-20).
-   **Problem:** The perturbation transparency theorem is correctly stated to apply to "canonical scalar matter," and Sec. X E correctly lists fermions as a system that would break the transparency. However, the paper does not sufficiently discuss the implications of this limitation for a realistic cosmological history, which includes a standard model fermion bath after reheating.
-   **Required Fix:** The authors should add a dedicated paragraph to discuss the domain of applicability of their theorem. They should clarify that the result is expected to hold during a period of scalar-field-driven inflation where fermion densities are negligible. They must also address what happens after reheating: how do fermions re-introduce torsion, and how are its effects constrained in the late universe? This discussion is crucial for understanding the practical importance and limitations of this otherwise powerful result. (The existing Route 1 analysis already constrains the late-time effects, so this may simply require connecting the arguments).

**P1A-M4: Arithmetically inconsistent fNL significance range**
-   **Section/Page:** Abstract (p. 1), Footnote 6 (p. 16).
-   **Problem:** The quoted "2.6-5σ" significance range for the SPHEREx fNL forecast is arithmetically inconsistent with the inputs provided in the paper. With fNL = -4.375 and the cited forecast sensitivities of σ(fNL) ≈ 0.7 (ideal) and σ(fNL) ≈ 1.0 (degraded), the resulting significance range should be approximately 4.4σ to 6.3σ. The quoted range of 2.6-5σ is unexplained and appears incorrect.
-   **Required Fix:** The authors must correct this calculation and provide a transparent derivation for the quoted significance range, or revise the range to be consistent with the inputs.

**P1A-M5: Dimensionally inconsistent or typographically incorrect fundamental operators**
-   **Section/Page:** Eq. (1), Eq. (6), Eq. (14), Appendix B.
-   **Problem:** Several of the fundamental equations of the theory appear to be either typographically incorrect or dimensionally inconsistent.
    1.  The ECH action in Eq. (1) appears to contain an extra `e^a_μ e^b_ν` factor, making the term a tensor rather than the required scalar `R`.
    2.  The key parity-odd operator in Eq. (6) and the one-loop operator in Eq. (14) do not have the correct mass dimension (+4) to be a valid Lagrangian density in a 4D action. The paper acknowledges this for Eq. (6) in Appendix B, framing it as a feature of a "phenomenological on-shell scaling ansatz." This is a profound theoretical weakness that undermines the entire argument for generating dark energy from ECH, as it is built upon operators that are not valid off-shell terms in an effective field theory.
-   **Required Fix:** The authors must correct the typographical error in Eq. (1). More critically, they must address the dimensional inconsistency of the operators in Eq. (6) and (14). Simply labeling this a "phenomenological ansatz" is insufficient. The physical and theoretical implications of postulating operators that are not valid terms in a 4D Lagrangian must be discussed in detail, and the conclusions that rely on these operators must be appropriately qualified as highly speculative.

### MINOR Revisions

**P1A-m1: Redundant Figure**
-   **Section/Page:** Sec. XII B (p. 22).
-   **Problem:** Figure 6, "Detection Significance Forecast," is largely a repetition of the information presented in Figure 4, "Observational decision timeline." It adds little new information and could be removed to improve the manuscript's conciseness.
-   **Required Fix:** The authors should consider removing Figure 6 and ensuring all essential forecast information is contained within Figure 4.

**P1A-m2: Inconsistent σ-value comparison in abstract**
-   **Section/Page:** Abstract (p. 1).
-   **Problem:** The abstract quotes significances for β (3.6σ and 2.9σ) and fNL (2.6-5σ). While it correctly adds the crucial caveat that they "arise from different null procedures and are not directly comparable," presenting them side-by-side in this manner can still be misleading to a casual reader.
-   **Required Fix:** To further improve clarity, consider rephrasing to physically separate these results. For example: "For cosmic birefringence, existing data show hints at ~3σ significance... For non-Gaussianity, forecasts for the SPHEREx mission predict a detection of the matter-bounce signal with a significance in the range of 2.6-5σ, depending on analysis assumptions."

### NITs (Cosmetic)

**P1A-N1: Paper Date**
-   **Section/Page:** p. 1.
-   **Problem:** The paper is dated "June 18, 2026."
-   **Required Fix:** Correct the date to the current submission date.

**P1A-N2: Garbled equation in Abstract**
-   **Section/Page:** Abstract (p. 1).
-   **Problem:** The expression for the physical wavenumber at the bounce appears to be corrupted, likely by the OCR process: "...kphys kbounce ~ KSPHEREX KSPHEREX phys Ntot-Nexit e32 32 kphys KSPHEREX...".
-   **Required Fix:** Please carefully check and correct the typeset equation in the abstract. The intended expression is likely `k_phys(bounce) ~ k_SPHEREx * exp(N_tot - N_exit)`.

**P1A-N3: Bibliographic style**
-   **Section/Page:** References (p. 28-29).
-   **Problem:** The bibliography does not follow a consistent format (e.g., inclusion of arXiv IDs, author list conventions, journal abbreviations).
-   **Required Fix:** Please format the entire bibliography according to the Physical Review D style guide.

**P1A-N4: Inconsistent use of Barbero-Immirzi parameter symbol**
-   **Section/Page:** Throughout.
-   **Problem:** The text uses `γ` (e.g., Eq. 1) and `γ_BI` (e.g., Table IV) for the Barbero-Immirzi parameter, while also using `γ_PTA` for the PTA spectral index. Using the bare symbol `γ` for two different physical quantities can be confusing.
-   **Required Fix:** It is strongly recommended to use `γ_BI` consistently throughout the text when referring to the Barbero-Immirzi parameter to avoid any ambiguity.

---
## Summary Recommendation
**MAJOR REVISIONS**

## Justification
This is a work of significant scope and potential impact. The systematic approach to constraining ECH dark energy is a strength, and the perturbation transparency theorem is a noteworthy result. The authors' commitment to intellectual honesty regarding their assumptions is commendable.

However, the paper cannot be published in its present form. The reliance on unpublished work for multiple, load-bearing results is a critical flaw that violates the core principles of peer-reviewed science. This must be rectified before the paper can be reconsidered. Furthermore, the theoretical framework for dark energy generation rests on dimensionally invalid operators, a fundamental issue that must be addressed head-on. Finally, key quantitative claims regarding observational forecasts are arithmetically inconsistent with the paper's own inputs.

I recommend that the paper undergo major revisions to address these points. If the authors can successfully make the manuscript self-contained, resolve the theoretical inconsistencies with their operators, and correct the quantitative claims as outlined above, it will be a very strong candidate for publication in Physical Review D.