# P1A auto-2026-06-05_1617pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (10049 chars)
**Wall time**: 142.8s

---

## Referee Report: "Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter"

This manuscript presents a systematic, channel-level investigation into four potential routes for generating late-time dark energy from minimal Einstein-Cartan-Holst (ECH) gravity. The central claims are a "channel-level closure" of these routes at the amplitude level, supported by a catalog of 14 structural constraints, and a "perturbation-transparency theorem" for canonical scalar matter. The paper concludes that while the minimal ECH framework fails as a source for dark energy under the stated assumptions, the broader bounce cosmology program it is embedded in retains testable, mechanism-independent predictions, namely a specific non-Gaussianity signature (`f_NL = -35/8`) and the possibility of spectator-field-driven cosmic birefringence.

The work is ambitious, systematic, and addresses a relevant question in theoretical cosmology. The perturbation-transparency theorem is a clear and useful result. The systematic cataloging of constraints ("barriers") is a valuable organizational contribution. However, the manuscript suffers from several issues, ranging from essential to minor, that must be addressed before it can be considered for publication in Physical Review D.

---
### ESSENTIAL Revisions

**P1A-E1: Over-reliance on "In Preparation" Companion Works**
*   **Section:** Throughout, but especially Abstract (p. 1), Sec. V (p. 11), Sec. VII (p. 11), and Conclusions (p. 18).
*   **Problem:** The manuscript's key observational and numerical results are not contained within the paper itself but are deferred to a suite of companion papers cited as "in preparation" ([2], [6], [23], [46]). These include:
    1.  The core cosmological parameter fits (`H_0`, `ΔN_eff`, etc.) from MCMC analysis [6].
    2.  The crucial `f_NL = -35/8` SPHEREx Fisher forecast [2].
    3.  The "confirmed null" result for galaxy spin asymmetry, which is a major observational pillar of the argument [23].
    4.  The NANOGrav data re-analysis [46].
*   **Required Fix:** A manuscript submitted for publication must be self-contained in its primary claims. The results from these companion works must either be fully documented within this paper (e.g., in appendices) or the companion papers must be publicly available (e.g., on arXiv) at the time of submission. As it stands, it is impossible for a referee to verify the foundational claims upon which this paper's structural arguments are built. The paper cannot be published in its current form.

**P1A-E2: Foundational Dark-Energy Mapping Rests on a Dimensionally-Inconsistent Ansatz**
*   **Section:** Abstract (p. 1), Sec. II C (p. 6), and Appendix B (p. 19).
*   **Problem:** The entire dark-energy mechanism under investigation relies on a "phenomenological on-shell scaling ansatz." The parity-odd operator in Eq. (6) has an off-shell mass dimension of +1, not the +4 required for a term in the Lagrangian density. The author is commendably transparent about this fundamental weakness, explicitly labeling it an "ansatz, not a derivation." However, this transparency does not resolve the issue. The paper is effectively a detailed analysis of a mechanism that is not derivable from a consistent effective field theory at the outset.
*   **Required Fix:** The framing of the paper must be sharpened. While the conclusion is a "no-go," the current structure spends significant time developing the phenomenology of this ansatz before closing it. The abstract and introduction should state more forcefully from the beginning that the investigated mechanism is based on a dimensionally-problematic operator, and that the paper's purpose is to demonstrate that even with this ansatz, the routes are inviable for a multitude of other reasons. This is more than a limitation; it is a central feature of the problem being studied.

---
### MAJOR Revisions

**P1A-M1: Non-Rigorous Derivation of Inflationary Dilution Prefactor**
*   **Section:** Sec. II C 1 (p. 6) and Sec. XII A (p. 15).
*   **Problem:** The inflationary dilution factor `D_inf` in Eq. (11) contains a prefactor `(T_reh / M_GUT)^(3/2)`. The derivation of this term is described as "dimensional-analysis aesthetic" and justified on "phenomenological phase-space grounds" rather than a rigorous calculation from a thermal partition function. The author explicitly acknowledges this limitation. This lack of rigor undermines the quantitative precision of the subsequent claim that `N_tot ≈ 92` e-folds are required, which is a cornerstone of the "structural tension" argument in Sec. XIV D.
*   **Required Fix:** The author must either provide a more rigorous derivation of this prefactor or significantly soften the claims related to the precise value of `N_tot`. The text should clarify that the `N_tot ≈ 92` value is an order-of-magnitude estimate whose precision is limited by the un-calculated prefactor, and the structural tension argument should be presented with this caveat at the forefront. The discussion in Appendix B about the `N_tot ≈ 92` vs `N_tot ≈ 94` values is good, but this uncertainty from the prefactor is a separate, more fundamental issue.

**P1A-M2: Ambiguous Scope of "Channel-Level Closure"**
*   **Section:** Abstract (p. 1), Sec. I (p. 3), Sec. IV (p. 8).
*   **Problem:** The paper repeatedly emphasizes that its result is a "channel-level closure, not an operator-level theorem." It explicitly lists omitted operators, such as the gravitational Chern-Simons term and a parity-odd four-fermion operator. While this scoping is stated, the strength of the "closure" language throughout the paper might overstate the result. The four "routes" are not a complete basis, and it is unclear if they are even fully independent (e.g., R1 and R4 are noted as projections of the same underlying interaction).
*   **Required Fix:** The author should tone down the "closure" language. A more accurate description might be "Systematic assessment and rejection of four proposed ECH dark-energy channels." The abstract and conclusions should re-emphasize that significant operators remain unanalyzed and could, in principle, provide a viable route, even if it is unlikely. The claim in the abstract that the paper performs "channel-level closure of the four enumerated minimal-ECH dark-energy routes" is tautological; the key is what this enumeration represents. The author should clarify why this specific set of four channels was chosen for analysis over a more complete operator basis.

---
### MINOR Revisions

**P1A-m1: Fictional/Future Dating and Citations**
*   **Section:** Title page (p. 1), and various references (e.g., [5], [10]).
*   **Problem:** The paper is dated "June 2, 2026," and several key citations refer to future arXiv preprints (e.g., `arXiv:2509...`). This is inappropriate for a journal submission.
*   **Required Fix:** The date must be corrected to the submission date. All citations must refer to existing, publicly accessible works. If a work is not yet public, it should be cited as "private communication" or removed if the claim is not essential.

**P1A-m2: Inconsistent NANOGrav Value Quoted**
*   **Section:** Figure 1 (p. 4) vs. Sec. XI G (p. 15).
*   **Problem:** Figure 1 quotes the PTA data as `γ = 3.20 ± 0.42`. Section XI G on page 15 quotes a different value, `γ = 2.567 ± 0.382`, from a re-analysis in a companion paper [46]. The text on p. 15 notes that this "supersedes the earlier... value," but the figure was not updated.
*   **Required Fix:** Ensure all figures and text are consistent. The figure should be updated to reflect the final value used in the analysis, and the caption should cite the source of the data point. The use of "supersedes" is internal-review language and should be rephrased.

**P1A-m3: Nuance in LiteBIRD Significance Calculation**
*   **Section:** Conclusions (p. 18).
*   **Problem:** The paper presents an excellent, nuanced calculation of the significance at which LiteBIRD could distinguish the `β ≈ 0.27°` benchmark from the current central value, finding `~0.73σ`. However, it also quotes a `~9σ` detection of non-zero `β` based on a naive `0.27° / 0.03°` calculation. While the text explains the difference, presenting these two numbers side-by-side can be misleading. The `~9σ` is the significance of rejecting the `β=0` null hypothesis, assuming the `β=0.27°` model is true. The `~0.73σ` is for model discrimination between two non-zero hypotheses.
*   **Required Fix:** The text should be slightly rephrased to make the distinction between these two different statistical tests even clearer, perhaps by explicitly stating the null and alternative hypotheses for each sigma value to prevent any misinterpretation.

**P1A-m4: Unclear Status of `w_0w_a` MCMC Chains**
*   **Section:** Table III, footnote ‡ (p. 16).
*   **Problem:** The footnote provides a live status update on a running MCMC chain for a `w_0w_a` model, including the number of samples and the current `R-1` value. This is not appropriate for a static publication.
*   **Required Fix:** The results should be presented only after the chains have fully converged and analysis is complete. The footnote should be removed and the table entry updated to a final state (e.g., "consistent," "disfavored at Xσ," etc.) based on the final, converged posterior, citing the appropriate (and public) companion paper.

---
### NIT-PICKS (Cosmetic)

**P1A-N1: Awkward Phrasing**
*   **Section:** Sec. XII A (p. 15).
*   **Problem:** The phrase "The Dinf exponential is therefore mathematical scaffolding for an order-of-magnitude parameterization of a hypothetical un-reset channel rather than a physically operative dilution mechanism" is slightly convoluted.
*   **Required Fix:** Suggest rephrasing for clarity, e.g., "The exponential factor in `D_inf` should therefore be viewed as a mathematical parameterization for a hypothetical channel that evades the thermal reset, not as a model of a physical dilution process."

**P1A-N2: Redundant Phrase**
*   **Section:** Sec. XIV D (p. 17).
*   **Problem:** The text reads "...surviving bispectrum signal becomes purely vacuum-inflationary rather than matter-bounce contraction-mode. This tension is presented here as a robustness check on the four-route amplitude-level no-go of Sec. IV and the 14-barrier closure of Sec. IX, not as a co-equal closure mechanism: the no-go has already closed the four amplitude routes..." The phrase "the no-go has already closed the four amplitude routes" is repetitive.
*   **Required Fix:** Streamline the sentence to avoid repetition.

---
## Summary recommendation

**MAJOR REVISIONS**

This manuscript provides a valuable and systematic critique of a class of dark energy models derived from ECH gravity. The perturbation-transparency theorem is a novel, clear, and publishable result. The systematic approach is commendable. However, the paper cannot be accepted in its current form. The essential issue is its reliance on crucial results from companion papers that are not publicly available, making the core claims unverifiable. Furthermore, the entire analysis is built upon a phenomenological ansatz for dark energy that is not consistent with standard EFT principles, a point that should be framed more centrally as a motivation for the no-go theorem rather than just a limitation.

If the author can make the supporting results from companion papers fully public and verifiable, and re-frames the manuscript to address the major points outlined above, the paper could be a strong candidate for publication in Physical Review D.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the second-pass review, incorporating new findings based on a more rigorous check.

================================================================
## Referee Report: "Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter" (Second Pass)

This manuscript presents a systematic, channel-level investigation into four potential routes for generating late-time dark energy from minimal Einstein-Cartan-Holst (ECH) gravity. The central claims are a "channel-level closure" of these routes at the amplitude level, supported by a catalog of 14 structural constraints, and a "perturbation-transparency theorem" for canonical scalar matter. The paper concludes that while the minimal ECH framework fails as a source for dark energy under the stated assumptions, the broader bounce cosmology program it is embedded in retains testable, mechanism-independent predictions, namely a specific non-Gaussianity signature (`f_NL = -35/8`) and the possibility of spectator-field-driven cosmic birefringence.

The work is ambitious, systematic, and addresses a relevant question in theoretical cosmology. The perturbation-transparency theorem is a clear and useful result. The systematic cataloging of constraints ("barriers") is a valuable organizational contribution. However, the manuscript suffers from several issues, ranging from essential to minor, that must be addressed before it can be considered for publication in Physical Review D.

*(This report includes findings from an initial review, marked with the original codes, and new findings from a more detailed second pass, marked with new codes.)*

---
### ESSENTIAL Revisions

**P1A-E1: Over-reliance on "In Preparation" Companion Works**
*   **Section:** Throughout, but especially Abstract (p. 1), Sec. V (p. 11), Sec. VII (p. 11), and Conclusions (p. 18).
*   **Problem:** The manuscript's key observational and numerical results are not contained within the paper itself but are deferred to a suite of companion papers cited as "in preparation" ([2], [6], [23], [46]). These include the core MCMC parameter fits, the `f_NL` forecast, the galaxy spin null result, and the NANOGrav re-analysis.
*   **Required Fix:** A manuscript submitted for publication must be self-contained in its primary claims. The results from these companion works must either be fully documented within this paper (e.g., in appendices) or the companion papers must be publicly available (e.g., on arXiv) at the time of submission. As it stands, it is impossible for a referee to verify the foundational claims upon which this paper's structural arguments are built.

**P1A-E2: Foundational Dark-Energy Mapping Rests on a Dimensionally-Inconsistent Ansatz**
*   **Section:** Abstract (p. 1), Sec. II C (p. 6), and Appendix B (p. 19).
*   **Problem:** The entire dark-energy mechanism under investigation relies on a "phenomenological on-shell scaling ansatz." The parity-odd operator in Eq. (6) has an off-shell mass dimension of +1, not the +4 required for a term in the Lagrangian density. The author is commendably transparent about this fundamental weakness, but this does not resolve the issue. The paper is effectively a detailed analysis of a mechanism that is not derivable from a consistent effective field theory at the outset.
*   **Required Fix:** The abstract and introduction should state more forcefully from the beginning that the investigated mechanism is based on a dimensionally-problematic operator, and that the paper's purpose is to demonstrate that even with this ansatz, the routes are inviable for a multitude of other reasons.

**P1A-E3: Error in Fundamental LQC Equation**
*   **Section:** Sec. II B (p. 6).
*   **Problem:** Equation (9) for the LQC critical bounce density, `ρ_crit = 3 / (8πG γ² Δ) = 3 / (32π²γ³) ρ_pl`, is missing a factor of `√3` in the denominator of the final expression. The correct formula, derived from the provided definition of `Δ`, is `ρ_crit = 3 / (32π²γ³√3) ρ_pl`. The numerical value `≈ 0.41 ρ_pl` cited from the literature is recovered only with this corrected formula.
*   **Required Fix:** Correct the formula in Equation (9). While the subsequent numerical estimates in the paper appear to use the correct value, the displayed foundational equation is incorrect.

---
### MAJOR Revisions

**P1A-M1: Non-Rigorous Derivation of Inflationary Dilution Prefactor**
*   **Section:** Sec. II C 1 (p. 6) and Sec. XII A (p. 15).
*   **Problem:** The inflationary dilution factor `D_inf` in Eq. (11) contains a prefactor `(T_reh / M_GUT)^(3/2)` whose derivation is described as "dimensional-analysis aesthetic" rather than a rigorous calculation. This lack of rigor undermines the quantitative precision of the subsequent claim that `N_tot ≈ 92` e-folds are required, which is a cornerstone of the "structural tension" argument.
*   **Required Fix:** The author must either provide a more rigorous derivation or significantly soften the claims related to the precise value of `N_tot`. The structural tension argument should be presented with this caveat at the forefront.

**P1A-M2: Ambiguous Scope of "Channel-Level Closure"**
*   **Section:** Abstract (p. 1), Sec. I (p. 3), Sec. IV (p. 8).
*   **Problem:** The paper repeatedly emphasizes "channel-level closure, not an operator-level theorem," and explicitly lists omitted operators. The strength of the "closure" language may overstate the result, as the four "routes" are not a complete or necessarily independent basis.
*   **Required Fix:** Tone down the "closure" language. A more accurate description might be "Systematic assessment and rejection of four proposed ECH dark-energy channels." The abstract and conclusions should re-emphasize that significant operators remain unanalyzed.

**P1A-M3: Dimensional Inconsistency in Key Equations**
*   **Section:** Sec. IV D (p. 10) and Sec. II A 2 (p. 6).
*   **Problem:**
    1.  Equation (17) for the birefringence angle `β` is dimensionally inconsistent. As written, it yields units of `Mass^-1`, whereas `β` must be dimensionless. This invalidates the quantitative derivation of `ρ_θ` and the subsequent naturalness argument in that section.
    2.  Equation (5) for the effective action `S_eff` is also dimensionally inconsistent, yielding units of `Mass^-1` instead of being dimensionless.
*   **Required Fix:** These equations must be corrected. The argument in Sec. IV D, which closes one of the four main routes, depends critically on a corrected and dimensionally consistent version of Eq. (17).

---
### MINOR Revisions

**P1A-m1: Fictional/Future Dating and Citations**
*   **Section:** Title page (p. 1), and various references.
*   **Problem:** The paper is dated "June 2, 2026," and several citations refer to future preprints.
*   **Required Fix:** Correct the date to the submission date. All citations must refer to existing, publicly accessible works.

**P1A-m2: Inconsistent NANOGrav Value Quoted**
*   **Section:** Figure 1 (p. 4) vs. Sec. XI G (p. 15).
*   **Problem:** Figure 1 quotes `γ = 3.20 ± 0.42`, while the text uses and discusses a "superseded" value of `γ = 2.567 ± 0.382`.
*   **Required Fix:** Update the figure to be consistent with the final value used in the text.

**P1A-m3: Nuance in LiteBIRD Significance Calculation**
*   **Section:** Conclusions (p. 18).
*   **Problem:** The paper presents two significance values for LiteBIRD (`~9σ` and `~0.73σ`) that test different hypotheses.
*   **Required Fix:** The text is already quite clear, but could be slightly rephrased to explicitly state the null and alternative hypotheses for each sigma value to prevent any possible misinterpretation.

**P1A-m4: Unclear Status of `w_0w_a` MCMC Chains**
*   **Section:** Table III, footnote ‡ (p. 16).
*   **Problem:** The footnote gives a live status update of a running MCMC chain.
*   **Required Fix:** This is inappropriate for a static publication. The results should be presented only after the analysis is complete and the chains have converged.

**P1A-m5: Unsupported Claim in Figure 1**
*   **Section:** Figure 1 (p. 4).
*   **Problem:** The figure claims that the "Ekpyrotic" mechanism is "structurally closed (this paper)". The main text provides no argument to support this claim, focusing exclusively on the four ECH routes.
*   **Required Fix:** Remove this claim from the figure or add a section to the paper that substantiates it.

**P1A-m6: Inconsistency in Figure 2**
*   **Section:** Figure 2 (p. 5).
*   **Problem:** The figure, illustrating the energy hierarchy, shows the initial parity-odd vacuum energy at the Planck scale, `ρ_vac = M_pl^4`. This contradicts the text, which states the effective coupling suppresses this energy by a factor of `~10^-2` at the outset (i.e., `ρ_vac ≈ 10^-2 M_pl^4`).
*   **Required Fix:** Correct the figure to be consistent with the quantitative claims in the text.

**P1A-m7: Incorrect Internal Cross-Reference**
*   **Section:** Abstract (p. 1).
*   **Problem:** The abstract states that missing operators are discussed "explicitly in Sec. IV and Sec. XI." The relevant discussion is in Sec. IV; Sec. XI discusses a different topic.
*   **Required Fix:** Remove the incorrect reference to Sec. XI.

---
## Summary recommendation

**MAJOR REVISIONS**

This manuscript provides a valuable and systematic critique of a class of dark energy models derived from ECH gravity. The perturbation-transparency theorem is a novel, clear, and publishable result. However, the paper cannot be accepted in its current form. The essential issues are its reliance on crucial results from non-public companion papers, and the presence of significant errors in foundational and key derived equations, including dimensional inconsistencies and a missing factor in the LQC bounce density formula.

If the author can make the supporting results public and verifiable, and thoroughly correct the equations and resulting arguments as outlined above, the paper could be a strong candidate for publication in Physical Review D.