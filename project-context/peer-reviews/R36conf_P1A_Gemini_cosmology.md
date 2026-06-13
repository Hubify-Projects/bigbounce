# P1A R36conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1a_ech_nogo_v1A.0.66.pdf` md5=5dff8674 pages=28
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (3181 chars)
**Wall time**: 136.0s

---

Here is a referee report for the submitted paper.

***

**Referee Report on "Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter"**

**Manuscript ID:** [Not provided]
**Author:** Houston Golden

This paper investigates the viability of four specific channels within minimal Einstein-Cartan-Holst (ECH) gravity as sources for late-time dark energy. The author presents two primary results: (1) a "channel-level closure" of the four enumerated dark-energy routes, arguing that they are either amplitude-suppressed or require fine-tuning that reintroduces the cosmological constant problem; and (2) a "perturbation-transparency" result, showing that for canonical scalar matter, the Holst sector decouples from scalar and tensor perturbations at all orders.

The perturbation-transparency theorem is a clear, well-derived, and significant result. It provides a sharp statement about the observational signatures (or lack thereof) of minimal ECH in standard cosmological perturbation theory.

However, the main thrust of the paper—the closure of the dark-energy routes—rests on a phenomenological scaling ansatz that is introduced to resolve a fundamental dimensional inconsistency in the effective operator. While the author is commendably transparent about this, it significantly weakens the conclusion from a robust no-go theorem to a model-dependent constraint. Furthermore, the manuscript in its current form is not self-contained and contains significant formatting errors that preclude publication.

Major revisions are required before this paper can be considered for publication in Physical Review D.

---

### ESSENTIAL Revisions

**P1A-E1: Dimensional Inconsistency of the Effective Action**
*   **Section/Page:** Sec. II A 2 (p. 6-7), Appendix B (p. 25)
*   **Problem:** The core parity-odd effective operator presented in Eq. (6) leads to an action `S_eff` with a mass dimension of +1, in direct violation of the principle that the action must be dimensionless (in natural units where ħ=1). The paper's dimensional accounting confirms this: `[α/M] = -1` (from the one-loop estimate, Eq. 7) and `[ε...R...] = +2`, yielding `[S_eff] = -1 + 2 = +1`. Appendix B acknowledges this as an "on-shell scaling ansatz" rather than a controlled EFT operator. This is a fundamental problem with the theoretical framework for the dark energy mechanism.
*   **Required Fix:** This issue cannot be relegated to an appendix. The main text (Section II and IV) must state upfront and clearly that the entire dark-energy analysis is predicated on a dimension-fixing ansatz. The term "closure" must be qualified at every instance to mean "closure *under the specific scaling ansatz of Appendix B*". The current presentation, while honest in the appendix, could mislead a reader into believing the closure is a more general result than it is.

**P1A-E2: Lack of Self-Containedness (Reliance on Companion Papers)**
*   **Section/Page:** Throughout, e.g., Abstract (p. 1), Sec. III B (p. 10), Sec. IV (p. 10), Table I (p. 4), Table III (p. 21).
*   **Problem:** The paper is not a standalone scientific work. It relies critically on results from at least four companion papers ([2], [6], [23], [46]) that are cited as "in preparation" or "posted concurrently". Key observational inputs, such as the null result for galaxy spin asymmetry, the `f_NL` forecast for SPHEREx, and the MCMC-derived cosmological parameters (`H_0`, `ΔN_eff`), are taken as given without derivation or sufficient methodological summary. This makes it impossible to evaluate the paper's claims independently.
*   **Required Fix:** The paper must be made self-contained. For each result imported from a companion paper, the authors must include a summary of the methods, key assumptions, and final results, sufficient for a reader to understand the argument without accessing the other manuscripts. This could be done in appendices if necessary. Placeholder citations to "in preparation" works for load-bearing claims are not acceptable.

**P1A-E3: Inclusion of Reviewer Metadata**
*   **Section/Page:** p. 28
*   **Problem:** The manuscript file contains a large block of text under the heading "[REVIEWER METADATA — NOT PART OF THE PAPER...]" which appears to be internal review instructions for the author.
*   **Required Fix:** This is a critical submission error. All such non-paper content must be removed from the manuscript.

### MAJOR Revisions

**P1A-M1: Clarity of the `f_NL` Erasure Argument**
*   **Section/Page:** Abstract (p. 1), Sec. XIV D (p. 23)
*   **Problem:** The argument that a large number of e-folds (`N_tot ≈ 92`) erases the matter-bounce `f_NL` signature is physically plausible but is explained in a confusing manner. The text mixes comoving and physical scales and does not clearly lay out the step-by-step history of a relevant mode. The phrase `k_bounce_phys ~ k_SPHEREx_phys * e^(N_tot - N_exit)` is particularly opaque.
*   **Required Fix:** Rewrite this section for clarity. The argument should track a constant *comoving* wavenumber `k` (relevant to SPHEREx observations) and show how its corresponding *physical* wavelength `λ_phys = 2πa/k` compares to the Hubble radius `1/H` through the contracting, bounce, and inflationary phases. The core point—that the mode is driven deep inside the subhorizon regime where inflationary vacuum fluctuations dominate over any pre-existing signal—should be made explicit and unambiguous.

**P1A-M2: Juxtaposition of Significance Values**
*   **Section/Page:** Abstract (p. 1)
*   **Problem:** The abstract quotes significances for cosmic birefringence from two different experiments (`~3.6σ` from WMAP+Planck and `~2.9σ` from ACT DR6) and correctly notes they "are not directly comparable". However, this crucial caveat appears only once. Given the high potential for misinterpretation, this point needs to be reinforced.
*   **Required Fix:** At every point in the manuscript where these two numbers (or any other significances derived from different null hypotheses or methodologies) are mentioned together, the caveat that they are not directly comparable must be repeated. For example, in the abstract, the sentence could be strengthened to: "...at ~2.9σ (we caution these significances arise from different null procedures and are not directly comparable in a single tension metric);".

### MINOR Revisions

**P1A-N1: Ambiguous Dimensionality of Coupling Constants**
*   **Section/Page:** Sec. IV B (p. 11-12)
*   **Problem:** The dimensional analysis of the one-loop amplitude in Eq. (15) is difficult to follow because the mass dimensions of the various couplings (`α`, `a/M`) are not explicitly stated in the main text where they are used. This required a cross-reference to Appendix B and other sections to verify.
*   **Required Fix:** For clarity, whenever a key physical parameter is introduced (e.g., `a/M` in Eq. 6), its mass dimension should be stated explicitly in the text, e.g., "(where `[a/M] = -1`)". This would greatly improve readability and allow for straightforward verification of the equations.

**P1A-N2: Inconsistent Use of `f_NL` Significance**
*   **Section/Page:** Table I (p. 4) vs. Abstract (p. 1)
*   **Problem:** The abstract states the `f_NL = -35/8` signature would be erased by the `N_tot ~ 92` e-folds required for the dark energy mechanism. However, Table I lists `f_NL = -35/8` as a "Testable prediction" with status "Yes, class-level". This is contradictory without further context.
*   **Required Fix:** Clarify in Table I that this prediction is only testable in bounce scenarios that *do not* invoke the ECH dark-energy mechanism discussed in this paper, due to the structural tension. The current presentation is confusing. A footnote similar to the one in Table IV (p. 26) should be added to Table I.

### NITs (Cosmetic)

**P1A-T1: Future Date**
*   **Section/Page:** p. 1
*   **Problem:** The date of the paper is listed as "June 12, 2026".
*   **Required Fix:** Change to the current submission date.

**P1A-T2: Typo in Footnote `a`**
*   **Section/Page:** p. 2
*   **Problem:** The footnote begins "This Bianchi-identity vanishing is distinct from and should not be confused with the Pontryagin density x RR". The `x` should likely be `∝` or similar.
*   **Required Fix:** Correct the symbol.

---

## Summary recommendation

**MAJOR REVISIONS**

The paper presents a valuable and apparently correct result regarding the decoupling of the Holst term from cosmological perturbations for scalar fields. This "perturbation-transparency" theorem is an important contribution. However, the paper's primary claim of "closing" dark energy channels in ECH is predicated on a dimension-fixing ansatz that is not rigorously derived, a fact that must be made more prominent. Most critically, the paper is not self-contained and contains a serious formatting error (inclusion of reviewer metadata), making it unsuitable for publication in its present form. The authors should be encouraged to revise the manuscript to address these essential points, with a potential focus on the robust perturbation result, while properly contextualizing the model-dependent dark energy constraints.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the addendum to the referee report, incorporating findings from a more detailed re-examination of the paper.

***

### ADDITIONAL Revisions (from second-pass review)

The following issues were identified upon a more rigorous, line-by-line re-examination of the manuscript's calculations, dimensional analysis, and cross-references. They are in addition to the points raised in the initial report.

### ESSENTIAL Revisions

**P1A-E4: Critical Arithmetic/Units Error in Route 4 Closure Argument**
*   **Section/Page:** Sec. IV D (p. 13)
*   **Problem:** The entire "naturalness objection" used to close Route 4 rests on a calculation that `p_φ ≈ 6 p_Λ` when `m_φ ~ H_0`. This calculation appears to be incorrect by approximately 60 orders of magnitude. The formula used is `p_φ = 2 m_φ^2 β^2 / (α/M)^2`. A dimensional check reveals `[p_φ] = [eV^2] / [GeV^-2] = 10^18 eV^4`, indicating a unit-conversion error. Re-computing the value with consistent units (`α/M = 10^-21 GeV^-1 = 10^-30 eV^-1`) yields `p_φ ≈ 1.6 x 10^-70 eV^4`, which is orders of magnitude smaller than the observed dark energy density `p_Λ ≈ 2.8 x 10^-11 eV^4`, not larger.
*   **Required Fix:** This is a critical error that invalidates the paper's conclusion for Route 4. The author must either provide a corrected derivation that supports their claim or retract the claim that Route 4 is closed by a naturalness objection. As it stands, the calculation shows the opposite: the predicted energy density is negligible, meaning the channel is likely closed by amplitude suppression, not a fine-tuning problem. This finding fundamentally alters one of the paper's main results.

**P1A-E1 (Strengthened): Dimensional Invalidity of the Action**
*   **Section/Page:** Sec. II A 2 (p. 6-7), Eq. (6)
*   **Problem:** The initial review noted that the Lagrangian `L_odd` has an incorrect mass dimension of +1. The situation is more severe: the action `S_eff = ∫ d^4x sqrt(-g) L_odd` consequently has a mass dimension of `[-4] + [+1] = -3`, in direct violation of the principle that the action must be dimensionless.
*   **Required Fix:** This reinforces the initial point P1A-E1. The author must acknowledge not just that the operator is not a controlled EFT operator, but that the entire action as written is dimensionally invalid. The "phenomenological scaling ansatz" is not just a minor fix; it is an attempt to repair a fundamental inconsistency in the starting point of the dark energy mechanism. This must be stated with complete clarity in the main text.

### MINOR Revisions

**P1A-N3: Incorrect Cross-Reference for `f_NL` Sensitivity**
*   **Section/Page:** Abstract (p. 1, footnote), Table I (p. 4, footnote `b`)
*   **Problem:** The footnotes in the abstract and Table I refer the reader to Section VII for the `σ(f_NL) ≈ 1.0` value used in the `2.6-5σ` forecast range. However, Section VII does not contain this number or its derivation; it cites an external paper [36].
*   **Required Fix:** The cross-reference should be corrected to point directly to the citation [36] or to the specific location where the value is discussed (e.g., footnote 6 on p. 15). Internal cross-references must be accurate.