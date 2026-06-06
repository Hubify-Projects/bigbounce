# P1A auto-2026-06-05_1717pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 158.4s

---

## Referee Report: Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter

This paper presents a systematic investigation into the viability of four minimal Einstein-Cartan-Holst (ECH) channels as sources for late-time dark energy. The central conclusion is a "channel-level closure" of these routes, meaning they are ruled out at the amplitude level under a set of well-stated assumptions. The paper's primary theoretical contribution is a "perturbation-transparency theorem," which demonstrates that for canonical scalar matter, the Holst sector of ECH gravity decouples from all scalar and tensor perturbation equations of motion. The authors support their main conclusion with a catalog of 13 logically-independent theoretical and observational constraints. The paper also identifies two surviving, testable predictions from the broader bounce-cosmology landscape: a specific non-Gaussianity signature (f_NL = -35/8) and a potential cosmic birefringence signal from a spectator axion-like particle.

The paper is exceptionally well-structured, transparent about its assumptions and limitations, and the arguments are supported by clear physical reasoning and quantitative estimates. The perturbation-transparency theorem, in particular, is a clean and significant result. The systematic approach of cataloging constraints ("barriers") provides a robust framework for the no-go conclusion. The figures and tables are of high quality and effectively summarize the paper's complex arguments.

While the paper is of high quality and suitable for publication in Physical Review D, I have identified several points that require revision or clarification.

---
### Detailed Findings

#### ESSENTIAL

**P1A-E1** | Section: IV B (Route 2) | Page: 9
*   **Problem**: Equation (15) and the surrounding text present a ratio that appears to be dimensionally inconsistent. The equation is given as `Δθ_one-loop / Δθ_obs ~ (α_em / 4π) * (H_0/M_Pl) / (M_Pl * (α/M) * β_obs)`. The term `M_Pl * (α/M)` is dimensionless, as is `β_obs`. The numerator is also dimensionless. However, the text refers to a "dimensionless reduction" and the derivation is not explicit, making it difficult to verify. The ambiguity arises from how the dimensionful coupling `α/M` (dimension -1) is combined with other scales to produce a dimensionless observable.
*   **Required Fix**: The authors must clarify the derivation of the dimensionless ratio in Equation (15). This should include an explicit, step-by-step derivation starting from the operator in Equation (14) and showing how all mass scales cancel to yield the quoted expression. If there is a typo in the equation, it must be corrected. The robustness of the final `10^-58` suppression factor depends on this derivation being correct.

#### MAJOR

**P1A-M1** | Section: II C 1 & Appendix B | Pages: 6, 7, 19
*   **Problem**: The paper's central dark-energy mechanism relies on a parity-odd operator (Eq. 6) with an off-shell mass dimension of +1, which is made to scale to the correct dimension of +4 via a "phenomenological on-shell scaling ansatz." While the authors are commendably transparent about this being an ansatz, its physical origin is obscure. The subsequent dilution factor `D_inf` (Eq. 11) also contains a `(T_reh/M_GUT)^(3/2)` prefactor justified by a "dimensional-analysis aesthetic" rather than a calculation. These two ansatze carry significant weight in the argument, particularly for the calculation of `N_tot ≈ 92`.
*   **Required Fix**: The authors should further consolidate the discussion of these ansatze. While a first-principles derivation is not expected (as the paper's goal is to close these routes), the authors should more strongly emphasize the "reheating thermal-reset barrier" (p. 7) as a more physical and ansatz-independent argument for closure. The abstract and introduction should be revised to state that the closure is supported by both a model-dependent tuning argument (requiring `N_tot ≈ 92`) and a more robust, physical thermalization argument. This would strengthen the overall conclusion by reducing its reliance on the weaker parts of the framework.

**P1A-M2** | Section: II A (Companion paper) & XV (Forward) | Pages: 5, 18
*   **Problem**: The paper relies on cosmological parameter values (H0, ΔN_eff, etc.) and MCMC analysis from a companion paper [6] which is cited as "in preparation." The text on page 5 states these values "should be read as internal-analysis inputs to the present structural argument rather than as independently peer-reviewable values until Paper I(b) is publicly posted." While citing work in preparation is common, this phrasing is problematic for a peer-reviewed publication. The results of a paper must be verifiable from publicly available information.
*   **Required Fix**: Before publication, reference [6] must be made publicly available, for example, as a preprint on arXiv. The text should be updated to reflect this, removing the language about "internal-analysis inputs." This ensures the reproducibility and verifiability of the work.

#### MINOR

**P1A-m1** | Section: Abstract & Title Page | Page: 1
*   **Problem**: The paper is dated "June 2, 2026 PDT."
*   **Required Fix**: The date should be corrected to the date of submission or revision.

**P1A-m2** | Section: L (Barrier 12) | Page: 13
*   **Problem**: Equation (20) states that `Ω_GW^bounce ∝ (ρ_crit / ρ_Pl)^2`. Typically, the energy density fraction in gravitational waves produced during a cosmological phase transition scales linearly with the energy density of the source relative to the total, i.e., `Ω_GW ∝ (ρ_source / ρ_total)`. A quadratic scaling is less common and requires justification.
*   **Required Fix**: Please provide a brief justification or a citation for the quadratic scaling of `Ω_GW` with the critical density ratio. If it is a typo, please correct it to a linear scaling and update the resulting numerical estimate (which would be `~0.27-0.41`).

**P1A-m3** | Section: XV (Conclusions) | Page: 18
*   **Problem**: The paper includes a disclosure about the use of an AI research assistant (Claude). While this transparency is laudable, its place in a formal physics paper is unconventional and may be subject to journal policy.
*   **Required Fix**: The authors should consult with the PRD editors regarding the journal's policy on such acknowledgments. The statement itself is clear and appropriate, but its inclusion should be consistent with journal standards.

**P1A-m4** | Section: XIV D | Page: 17
*   **Problem**: The "Structural Tension" argument, which highlights the incompatibility between the `N_tot` required for the DE mechanism and the `N_tot` that would preserve the `f_NL` signal, is a very strong point. However, it is mentioned in the abstract, the introduction (p. 3), and then detailed again on p. 17.
*   **Required Fix**: To improve readability and flow, consider consolidating the detailed explanation of this argument into a single location (e.g., Section XIV D) and referring back to it from the introduction. The current repetition, while emphasizing a key point, is slightly redundant.

#### NIT

**P1A-N1** | Section: Table III, footnote † | Page: 16
*   **Problem**: The footnote provides a real-time status update on a running MCMC chain ("At the time of this writing the chain has accumulated..."). This level of detail will quickly become outdated.
*   **Required Fix**: Rephrase the footnote to be more general, for example: "The MCMC analysis for the w0wa parameter space was not completed at the time of submission; a future analysis will address this model."

---
## Summary recommendation

**MAJOR REVISIONS**

This is a high-quality paper with a significant and well-supported primary conclusion. The perturbation-transparency theorem is an elegant and important result for the ECH community. The systematic closure of the four dark-energy routes is thorough and convincing. The authors' transparency regarding the assumptions and limitations of their framework is a major strength.

However, the issues classified as ESSENTIAL and MAJOR must be addressed before the paper can be accepted. The dimensional analysis in the Route 2 closure argument must be clarified (P1A-E1), the reliance on unpublished companion work must be resolved by posting a public preprint (P1A-M2), and the framing of the argument should be adjusted to place more emphasis on the robust physical arguments over the phenomenological ansatze (P1A-M1). Once these points are satisfactorily addressed, the paper will represent a strong contribution to the literature on modified gravity and cosmology.