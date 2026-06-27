# P1A R56 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/private/tmp/R56_P1A/paper1a_ech_nogo.pdf` md5=d0cd4895 pages=29
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (12552 chars)
**Wall time**: 162.1s

---

## Referee Report on "Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter"

**Manuscript ID:** [Assigned by editor]
**Author:** Houston Golden
**Date:** [Current Date]

### Summary

This manuscript presents a broad theoretical and phenomenological assessment of minimal Einstein-Cartan-Holst (ECH) gravity as a source for late-time dark energy and as a host for a matter-bounce cosmology. The work has two main, and somewhat contradictory, thrusts. First, it attempts to establish a connection between a parity-odd sector of ECH gravity and the observed dark energy density, and then proceeds to "close" four potential channels for this connection using a catalog of 14 "barriers". Second, it presents a "perturbation transparency" theorem, demonstrating that for canonical scalar matter, the Holst sector of ECH gravity is dynamically inert at all orders in perturbation theory, rendering it indistinguishable from standard General Relativity in scalar/tensor observables.

The paper contains a core, valuable, and apparently correct theoretical result in the perturbation transparency theorem. The associated phenomenological argument regarding the structural tension between the requirements for a dark energy mechanism and the survival of a matter-bounce signature (`f_NL`) is also compelling and observationally relevant.

However, the entire framework for connecting ECH to dark energy, which the paper spends the majority of its length "closing", is built upon a fundamentally flawed premise: a phenomenological operator with an off-shell mass dimension of +1, which is not a valid term in a local field theory action. The "on-shell scaling ansatz" used to rectify this is ad-hoc and not derived from first principles. While the author is commendably transparent about this being an "ansatz", this does not excuse the unphysical foundation.

Furthermore, the manuscript is not self-contained, relying heavily on several companion papers for crucial quantitative results, and cites non-existent preprints with placeholder identifiers.

Due to these severe issues, the manuscript requires a fundamental restructuring and major revisions before it can be considered for publication in Physical Review D.

### Summary recommendation
**MAJOR REVISIONS**

The paper must be fundamentally reframed to lead with its solid contributions (the perturbation transparency theorem and the structural tension argument). The flawed dark-energy framework should be presented concisely as a case study in model failure, not as a central pillar of the investigation. All placeholder citations must be replaced with links to public preprints, and the paper must be made self-contained with respect to its core claims.

---
### Detailed Findings

#### ESSENTIAL Revisions

**P1A-E1: Foundational Operator is Dimensionally Inconsistent**
*   **Location:** Abstract (p. 1), Sec. II A 2 (p. 7), Appendix B (p. 26)
*   **Problem:** The entire dark-energy framework rests on the parity-odd operator in Eq. (6), which the paper correctly identifies as having an off-shell mass dimension of +1. A Lagrangian density must have mass dimension +4. Appendix B proposes to fix this via a phenomenological "on-shell scaling ansatz" (`ρ_bounce ~ (α/M) M_Pl^4`) which amounts to inserting powers of the Planck mass by hand, justified by the Planck-scale curvature at the bounce. This is not a derivation and does not produce a valid, controlled effective field theory operator. The alternative reading (promoting the coupling `α/M → α M_Pl^3 / M`) is also an ad-hoc fix.
*   **Required Fix:** The paper cannot be framed as a serious investigation of an ECH dark-energy model based on this operator. The author must reframe the entire first half of the paper. Instead of a lengthy "closure" of four routes, this section should be a concise demonstration that such a model fails at the most basic level of theoretical consistency. The focus of the paper must shift to its physically sound results.

**P1A-E2: Use of Placeholder and Inaccessible References**
*   **Location:** Bibliography (p. 28-29) and throughout the text.
*   **Problem:** The manuscript cites several papers that do not appear to exist on the arXiv or any public server.
    *   [5] P. Diego-Palazuelos and E. Komatsu, arXiv preprint (2025), arXiv:2509.13654
    *   [10] DESI Collaboration, M. Abdul-Karim, et al., Physical Review D 112, 083515 (2025), arXiv:2503.14738
    These appear to be placeholder citations for future work. Citing non-existent work is unacceptable.
*   **Required Fix:** All citations must point to publicly available works (preprints or published papers). The corresponding claims in the text that rely on these sources must be removed or substantiated by other means.

**P1A-E3: Lack of Standalone Verifiability**
*   **Location:** Throughout the paper.
*   **Problem:** The paper makes numerous quantitative claims that are justified only by citation to a suite of companion papers by the same author ([2], [6], [23], [46]), stated to be "posted concurrently". For example, the MCMC cosmological parameter values (Table IV), the SPHEREx `f_NL` forecast significance (Abstract, Sec. XIII), the galaxy spin null result (Sec. III B), and the PTA analysis (Sec. X G) are all imported. A research article submitted to PRD must be self-contained and its primary results verifiable on their own merit.
*   **Required Fix:** The paper must be revised to be self-contained. For each result imported from a companion paper, the author must either (a) remove the claim, (b) provide a full derivation/analysis within this manuscript (perhaps in an appendix), or (c) provide a sufficient summary of the methodology and assumptions that the result can be understood and its plausibility assessed without reading the other paper. The "shotgun" submission of an entire, interdependent research program is not standard practice and shifts an undue burden onto the review process.

#### MAJOR Revisions

**P1A-M1: Paper Structure, Length, and Focus**
*   **Location:** Entire manuscript.
*   **Problem:** The paper is 29 pages long and its narrative is convoluted. It spends significant effort building up and then tearing down a dark-energy model that is flawed from the outset (see P1A-E1). The truly valuable contributions—the perturbation transparency theorem and the structural tension argument—are buried in Sections X and XIV.
*   **Required Fix:** The paper should be substantially restructured and shortened. A recommended structure:
    1.  Introduction: Motivate bounce cosmologies and ECH.
    2.  The Perturbation Transparency Theorem for ECH: Present this as the main theoretical result.
    3.  Phenomenological Implications: Discuss the consequences, including the clean separation of observables into GR-like (perturbative) and non-perturbative (parity violation).
    4.  Surviving Class-Level Tests: Discuss the `f_NL` and birefringence signatures as tests of the broader bounce/ALP landscape, not ECH specifically.
    5.  The Structural Tension: Present the `N_tot` vs. `f_NL` erasure argument as a key phenomenological constraint.
    6.  Failure of Minimal ECH as a DE Source: Briefly present the dimension-1 operator and other arguments (e.g., thermal washout) as a concise case study showing why this specific route fails.
    7.  Conclusion.
    This would create a more logical flow and highlight the paper's strengths. The extensive 14-barrier catalog could be moved to an appendix or drastically condensed.

**P1A-M2: Juxtaposition of Significance Values**
*   **Location:** Abstract (p. 1), Sec. XIII (p. 23)
*   **Problem:** The abstract states that the SPHEREx forecast significance is "2.6-5σ" and that these values "arise from different null procedures and are not directly comparable in a single tension table". This is excellent practice. However, this crucial caveat is not always present where the numbers are discussed. For example, in the LiteBIRD discussion, the `~9σ` detection sensitivity is compared with the `~0.7σ` discrimination power without explicitly restating that these test different null hypotheses (zero-vs-data vs. model1-vs-model2).
*   **Required Fix:** At *every* point where two or more sigma values are mentioned in proximity, the author must include a brief, explicit statement clarifying what null hypotheses are being tested and whether the values are directly comparable. This is crucial for reader clarity.

#### MINOR Revisions

**P1A-m1: Ambiguous Phrasing in Forecasts**
*   **Location:** Sec. XIII (p. 23), Sec. XV (p. 25)
*   **Problem:** The discussion of the LiteBIRD forecast for `β` correctly computes the discrimination significance between the `β=0.27°` benchmark and the current WMAP+Planck central value as `~0.7σ`. However, the text could be clearer that this implies LiteBIRD, despite its excellent sensitivity, will *not* be able to resolve the issue on its own; a significant improvement in the measurement of the central value itself is required.
*   **Required Fix:** Rephrase the conclusion of the LiteBIRD discussion to state more directly: "Therefore, while LiteBIRD can confirm a non-zero birefringence with high confidence, it will not be able to distinguish the spectator-ALP benchmark from the current central value reported by WMAP+Planck at a statistically significant level."

**P1A-m2: PTA vs. Matter Bounce Comparison**
*   **Location:** Sec. X G (p. 21), Fig. 1 (p. 5)
*   **Problem:** The paper notes that the matter bounce prediction for the PTA spectral index (`γ=3.0`) is `+1.13σ` from the posterior mean of a specific NANOGrav analysis. This is correctly described as "consistent with the data within standard frequentist tolerance".
*   **Required Fix:** To avoid any misinterpretation, it should be explicitly stated that this level of agreement constitutes weak, inconclusive evidence and does not significantly favor the matter bounce model.

#### NITs (Cosmetic)

**P1A-N1: Future Date**
*   **Location:** Page 1
*   **Problem:** The paper is dated "June 26, 2026".
*   **Required Fix:** Change to the current submission date.

**P1A-N2: Abstract-Body Consistency Check**
*   **Location:** Abstract (p. 1) vs. Sec. XIV D (p. 24)
*   **Problem:** The abstract mentions the `f_NL` erasure argument and gives the key numbers (`N_tot ≈ 92`, `N_exit ~ 60`). The body provides the same numbers and a more detailed explanation. The abstract accurately reflects the body on this point. This is a check that passed, but is worth noting. The abstract is generally a good, if dense, summary of the paper's claims.

**P1A-N3: Figure 3 Caption**
*   **Location:** Page 8
*   **Problem:** The caption for Figure 3 states it is an "illustrative parameter-set comparison... not a derived prediction". This is good and honest. It also correctly notes the `(ω/H)^2` contribution is "completely invisible".
*   **Required Fix:** No fix needed, this is an example of good practice in the paper.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the updated review, incorporating the findings from the second, more rigorous pass.

================================================================
## Referee Report on "Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter"

**Manuscript ID:** [Assigned by editor]
**Author:** Houston Golden
**Date:** [Current Date]

### Summary

This manuscript presents a broad theoretical and phenomenological assessment of minimal Einstein-Cartan-Holst (ECH) gravity as a source for late-time dark energy and as a host for a matter-bounce cosmology. The work has two main, and somewhat contradictory, thrusts. First, it attempts to establish a connection between a parity-odd sector of ECH gravity and the observed dark energy density, and then proceeds to "close" four potential channels for this connection using a catalog of 14 "barriers". Second, it presents a "perturbation transparency" theorem, demonstrating that for canonical scalar matter, the Holst sector of ECH gravity is dynamically inert at all orders in perturbation theory, rendering it indistinguishable from standard General Relativity in scalar/tensor observables.

The paper contains a core, valuable, and apparently correct theoretical result in the perturbation transparency theorem. The associated phenomenological argument regarding the structural tension between the requirements for a dark energy mechanism and the survival of a matter-bounce signature (`f_NL`) is also compelling and observationally relevant.

However, the entire framework for connecting ECH to dark energy, which the paper spends the majority of its length "closing", is built upon a fundamentally flawed premise: a phenomenological operator with an off-shell mass dimension of +1, which is not a valid term in a local field theory action. The "on-shell scaling ansatz" used to rectify this is ad-hoc and not derived from first principles. While the author is commendably transparent about this being an "ansatz", this does not excuse the unphysical foundation.

Furthermore, the manuscript is not self-contained, relying heavily on several companion papers for crucial quantitative results, and cites non-existent preprints with placeholder identifiers.

Due to these severe issues, the manuscript requires a fundamental restructuring and major revisions before it can be considered for publication in Physical Review D.

### Summary recommendation
**MAJOR REVISIONS**

The paper must be fundamentally reframed to lead with its solid contributions (the perturbation transparency theorem and the structural tension argument). The flawed dark-energy framework should be presented concisely as a case study in model failure, not as a central pillar of the investigation. All placeholder citations must be replaced with links to public preprints, and the paper must be made self-contained with respect to its core claims.

---
### Detailed Findings

#### ESSENTIAL Revisions

**P1A-E1: Foundational Operator is Dimensionally Inconsistent**
*   **Location:** Abstract (p. 1), Sec. II A 2 (p. 7), Appendix B (p. 26)
*   **Problem:** The entire dark-energy framework rests on the parity-odd operator in Eq. (6), which the paper correctly identifies as having an off-shell mass dimension of +1. A Lagrangian density must have mass dimension +4. Appendix B proposes to fix this via a phenomenological "on-shell scaling ansatz" (`ρ_bounce ~ (α/M) M_Pl^4`) which amounts to inserting powers of the Planck mass by hand, justified by the Planck-scale curvature at the bounce. This is not a derivation and does not produce a valid, controlled effective field theory operator. The alternative reading (promoting the coupling `α/M → α M_Pl^3 / M`) is also an ad-hoc fix.
*   **Required Fix:** The paper cannot be framed as a serious investigation of an ECH dark-energy model based on this operator. The author must reframe the entire first half of the paper. Instead of a lengthy "closure" of four routes, this section should be a concise demonstration that such a model fails at the most basic level of theoretical consistency. The focus of the paper must shift to its physically sound results.

**P1A-E2: Use of Placeholder and Inaccessible References**
*   **Location:** Bibliography (p. 28-29) and throughout the text.
*   **Problem:** The manuscript cites several papers that do not appear to exist on the arXiv or any public server.
    *   [5] P. Diego-Palazuelos and E. Komatsu, arXiv preprint (2025), arXiv:2509.13654
    *   [10] DESI Collaboration, M. Abdul-Karim, et al., Physical Review D 112, 083515 (2025), arXiv:2503.14738
    These appear to be placeholder citations for future work. Citing non-existent work is unacceptable.
*   **Required Fix:** All citations must point to publicly available works (preprints or published papers). The corresponding claims in the text that rely on these sources must be removed or substantiated by other means.

**P1A-E3: Lack of Standalone Verifiability**
*   **Location:** Throughout the paper.
*   **Problem:** The paper makes numerous quantitative claims that are justified only by citation to a suite of companion papers by the same author ([2], [6], [23], [46]), stated to be "posted concurrently". For example, the MCMC cosmological parameter values (Table IV), the SPHEREx `f_NL` forecast significance (Abstract, Sec. XIII), the galaxy spin null result (Sec. III B), and the PTA analysis (Sec. X G) are all imported. A research article submitted to PRD must be self-contained and its primary results verifiable on their own merit.
*   **Required Fix:** The paper must be revised to be self-contained. For each result imported from a companion paper, the author must either (a) remove the claim, (b) provide a full derivation/analysis within this manuscript (perhaps in an appendix), or (c) provide a sufficient summary of the methodology and assumptions that the result can be understood and its plausibility assessed without reading the other paper. The "shotgun" submission of an entire, interdependent research program is not standard practice and shifts an undue burden onto the review process.

#### MAJOR Revisions

**P1A-M1: Paper Structure, Length, and Focus**
*   **Location:** Entire manuscript.
*   **Problem:** The paper is 29 pages long and its narrative is convoluted. It spends significant effort building up and then tearing down a dark-energy model that is flawed from the outset (see P1A-E1). The truly valuable contributions—the perturbation transparency theorem and the structural tension argument—are buried in Sections X and XIV.
*   **Required Fix:** The paper should be substantially restructured and shortened. A recommended structure:
    1.  Introduction: Motivate bounce cosmologies and ECH.
    2.  The Perturbation Transparency Theorem for ECH: Present this as the main theoretical result.
    3.  Phenomenological Implications: Discuss the consequences, including the clean separation of observables into GR-like (perturbative) and non-perturbative (parity violation).
    4.  Surviving Class-Level Tests: Discuss the `f_NL` and birefringence signatures as tests of the broader bounce/ALP landscape, not ECH specifically.
    5.  The Structural Tension: Present the `N_tot` vs. `f_NL` erasure argument as a key phenomenological constraint.
    6.  Failure of Minimal ECH as a DE Source: Briefly present the dimension-1 operator and other arguments (e.g., thermal washout) as a concise case study showing why this specific route fails.
    7.  Conclusion.
    This would create a more logical flow and highlight the paper's strengths. The extensive 14-barrier catalog could be moved to an appendix or drastically condensed.

**P1A-M2: Juxtaposition of Significance Values**
*   **Location:** Abstract (p. 1), Sec. XIII (p. 23)
*   **Problem:** The abstract states that the SPHEREx forecast significance is "2.6-5σ" and that these values "arise from different null procedures and are not directly comparable in a single tension table". This is excellent practice. However, this crucial caveat is not always present where the numbers are discussed. For example, in the LiteBIRD discussion, the `~9σ` detection sensitivity is compared with the `~0.7σ` discrimination power without explicitly restating that these test different null hypotheses (zero-vs-data vs. model1-vs-model2).
*   **Required Fix:** At *every* point where two or more sigma values are mentioned in proximity, the author must include a brief, explicit statement clarifying what null hypotheses are being tested and whether the values are directly comparable. This is crucial for reader clarity.

**P1A-M3: Inconsistent `f_NL` Significance Derivation**
*   **Location:** Abstract (p. 1), Footnote 6 (p. 15), Fig. 4 Caption (p. 16)
*   **Problem:** The paper consistently quotes a "2.6-5σ" realistic significance for the SPHEREx `f_NL` forecast. However, the provided numbers in Footnote 6 (`f_NL = -4.375`, `σ(f_NL) ≈ 1.0`) only support a significance of `~4.4σ`. The origin of the 2.6σ lower bound and the 5σ upper bound is not explained, making the range seem arbitrary or based on unstated assumptions from a companion paper.
*   **Required Fix:** The author must clarify the derivation of the full 2.6-5σ range. If it depends on different systematic budgets or analysis choices, these must be briefly explained. Otherwise, the significance should be stated as the single, derivable value (`~4.4σ`) based on the numbers provided.

#### MINOR Revisions

**P1A-m1: Ambiguous Phrasing in Forecasts**
*   **Location:** Sec. XIII (p. 23), Sec. XV (p. 25)
*   **Problem:** The discussion of the LiteBIRD forecast for `β` correctly computes the discrimination significance between the `β=0.27°` benchmark and the current WMAP+Planck central value as `~0.7σ`. However, the text could be clearer that this implies LiteBIRD, despite its excellent sensitivity, will *not* be able to resolve the issue on its own; a significant improvement in the measurement of the central value itself is required.
*   **Required Fix:** Rephrase the conclusion of the LiteBIRD discussion to state more directly: "Therefore, while LiteBIRD can confirm a non-zero birefringence with high confidence, it will not be able to distinguish the spectator-ALP benchmark from the current central value reported by WMAP+Planck at a statistically significant level."

**P1A-m2: PTA vs. Matter Bounce Comparison**
*   **Location:** Sec. X G (p. 21), Fig. 1 (p. 5)
*   **Problem:** The paper notes that the matter bounce prediction for the PTA spectral index (`γ=3.0`) is `+1.13σ` from the posterior mean of a specific NANOGrav analysis. This is correctly described as "consistent with the data within standard frequentist tolerance".
*   **Required Fix:** To avoid any misinterpretation, it should be explicitly stated that this level of agreement constitutes weak, inconclusive evidence and does not significantly favor the matter bounce model.

**P1A-m3: Minor Inaccuracy in Cross-Reference**
*   **Location:** Abstract (p. 1)
*   **Problem:** The abstract states that missing operators are acknowledged "explicitly in Sec. IV and Sec. XI". While Sec. IV does this, Sec. XI (The Hybrid Dark-Energy Loophole) does not.
*   **Required Fix:** Remove the reference to Sec. XI in this context in the abstract.

#### NITs (Cosmetic)

**P1A-N1: Future Date**
*   **Location:** Page 1
*   **Problem:** The paper is dated "June 26, 2026".
*   **Required Fix:** Change to the current submission date.

**P1A-N2: Abstract-Body Consistency Check**
*   **Location:** Abstract (p. 1) vs. Sec. XIV D (p. 24)
*   **Problem:** The abstract mentions the `f_NL` erasure argument and gives the key numbers (`N_tot ≈ 92`, `N_exit ~ 60`). The body provides the same numbers and a more detailed explanation. The abstract accurately reflects the body on this point. This is a check that passed, but is worth noting. The abstract is generally a good, if dense, summary of the paper's claims.

**P1A-N3: Figure 3 Caption**
*   **Location:** Page 8
*   **Problem:** The caption for Figure 3 states it is an "illustrative parameter-set comparison... not a derived prediction". This is good and honest. It also correctly notes the `(ω/H)^2` contribution is "completely invisible".
*   **Required Fix:** No fix needed, this is an example of good practice in the paper.

**P1A-N4: Typo in Cross-Reference**
*   **Location:** Page 22
*   **Problem:** The text refers to "Sec. IIC1". This should likely be "Sec. II C 1".
*   **Required Fix:** Correct the typo.