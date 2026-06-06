# P1A auto-2026-06-06_0004pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (6106 chars)
**Wall time**: 158.0s

---

## Referee Report for Manuscript [P1A]

**Title:** Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter
**Author:** Houston Golden

This manuscript investigates four potential channels within minimal Einstein-Cartan-Holst (ECH) gravity as sources for late-time dark energy. The author concludes that all four channels fail at the amplitude level, a result termed "channel-level closure." The paper's main positive result is a "perturbation-transparency theorem," which states that for canonical scalar matter, the Holst sector decouples from all scalar and tensor perturbation equations, rendering the Barbero-Immirzi parameter `γ` unobservable in standard perturbative channels.

While the perturbation-transparency theorem is a clear, well-derived, and interesting result, the central analysis concerning dark energy is based on a fundamentally flawed theoretical premise. The manuscript relies on a dimensionally inconsistent operator and an ad-hoc "scaling ansatz" to connect Planck-scale physics to the observed dark energy density. The paper itself contains arguments that invalidate this proposed connection. Furthermore, the work relies heavily on numerical results from companion papers that are "in preparation" and thus unverifiable. For these reasons, the manuscript in its current form is not suitable for publication in Physical Review D.

Below is a detailed list of required revisions.

---

### ESSENTIAL Revisions

**P1A-E1: Fundamentally Flawed Dark Energy Operator and "Scaling Ansatz"**
*   **Location:** Sec. II C (p. 6), Sec. IV (p. 8), Appendix B (p. 19)
*   **Problem:** The entire dark-energy analysis rests on the parity-odd operator in Eq. (6). As the author correctly identifies in Appendix B, this operator's Lagrangian density has a mass dimension of +1, not the required +4. This is a fundamental inconsistency in an effective field theory framework. The proposed "fix" is not a derivation but a "phenomenological on-shell scaling ansatz" which amounts to inserting the required powers of the Planck mass by hand to obtain the desired energy density `ρ_Λ`. This procedure lacks any theoretical justification and cannot be considered a valid derivation or a controlled approximation. A theory cannot be built upon an operator with the wrong dimensionality.
*   **Required Fix:** This is a fatal flaw in the dark energy portion of the paper. The quantitative conclusions derived from this ansatz, including the `N_tot ≈ 92` e-folds requirement and the subsequent "structural tension" argument, are not supported by a valid theoretical framework. This entire line of reasoning must be removed. The paper could be restructured to focus solely on the robust results that do not depend on this ansatz.

**P1A-E2: Unacceptable Reliance on "In Preparation" and Placeholder Citations**
*   **Location:** Throughout the manuscript, e.g., p. 5, p. 11, p. 15, References [2, 5, 6, 10, 23, 46].
*   **Problem:** The paper's quantitative claims and observational context rely critically on results from companion papers cited as "(in preparation)" or with future dates and placeholder arXiv IDs (e.g., `arXiv:2509.13654`). Key cosmological parameters (`H_0`, `ΔN_eff` from [6]), forecasts (`σ(f_NL)` from [2]), and data analysis (`γ_PTA` from [46]) are presented without a verifiable source. A manuscript submitted for peer review must be self-contained or cite publicly available, citable work (i.e., published or on the arXiv).
*   **Required Fix:** All claims and numerical values must be derived within the paper or supported by citations to publicly accessible literature. All references to "in preparation" works or those with placeholder identifiers must be removed or replaced with valid citations. If this is not possible, the associated claims must be removed from the manuscript.

**P1A-E3: Internal Contradiction Regarding the Dark Energy Mechanism**
*   **Location:** Sec. XII A (p. 15) vs. Sec. II C (p. 6) and Sec. XIV D (p. 17).
*   **Problem:** The paper presents a direct contradiction. The dark energy mechanism requires an inflationary dilution factor `D_inf ~ exp(-3N_tot)` to bridge the gap between the bounce scale and the observed `ρ_Λ`. However, in Sec. XII A, the author correctly argues that this factor is mere "mathematical scaffolding" and not a "physically operative dilution mechanism." The author further presents a compelling physical argument—the "reheating thermal-reset barrier"—which states that any coherent torsion from the bounce is erased by thermalization at reheating. This argument *closes* the channel, preventing any memory of the bounce from surviving to the present day. The paper therefore proves that its own proposed dark-energy mechanism is physically unviable. Despite this, it proceeds to use the consequences of this unviable mechanism (specifically, the value `N_tot ≈ 92`) to construct other central arguments, such as the "structural tension" with `f_NL`.
*   **Required Fix:** The manuscript cannot simultaneously argue that a mechanism is unphysical and also use its quantitative predictions as a basis for further claims. The contradictory sections must be reconciled. Given the strength of the "reheating thermal-reset" argument, the logical conclusion is that the ECH-to-dark-energy channel is closed. The `N_tot ≈ 92` calculation and the "structural tension" argument, which depend on this closed channel, must be removed.

**P1A-E4: Inclusion of In-Progress Analysis Details**
*   **Location:** Table III, footnote `†` (p. 16).
*   **Problem:** The footnote discusses the status of an MCMC chain that is currently running ("has accumulated ~3.8×10⁴ accepted samples... descending monotonically toward... convergence target"). This is inappropriate "lab notebook" material for a formal scientific publication. A paper should only report on completed, converged, and verified analyses.
*   **Required Fix:** Remove the footnote and all discussion of ongoing, incomplete computational work. The results presented must be final.

### MAJOR Revisions

**P1A-M1: The "Structural Tension" Argument is Unfounded**
*   **Location:** Abstract (p. 1), Sec. XIV D (p. 17).
*   **Problem:** A key claim of the paper is the "structural tension" between the `N_tot ≈ 92` e-folds allegedly required for the ECH dark energy mechanism and the fact that this many e-folds would erase the matter-bounce `f_NL = -35/8` signature. As established in E1 and E3, the `N_tot ≈ 92` value is derived from a theoretically unsound and physically unviable mechanism. Therefore, this tension is not a robust prediction or constraint of the ECH framework. It is an artifact of comparing a real prediction (`f_NL`) with a number derived from a flawed premise.
*   **Required Fix:** The "structural tension" argument must be removed from the abstract and the main body. It is not a valid conclusion of the presented work.

**P1A-M2: Overstated Claim on Closing Ekpyrotic Models**
*   **Location:** Figure 1 (p. 4).
*   **Problem:** The flowchart in Figure 1 has a box for "Ekpyrotic" models labeled "structurally closed (this paper)". The paper's scope is explicitly minimal ECH. While some ekpyrotic scenarios might involve ECH, this work does not provide a general closure for the entire class of ekpyrotic models. This is an overstatement of the paper's contribution.
*   **Required Fix:** The claim in Figure 1 must be qualified to state that only the minimal-ECH component within certain ekpyrotic models is addressed, or the box should be removed entirely to maintain the paper's focus.

### MINOR Revisions

**P1A-m1: Unclear Figure Axis Label**
*   **Location:** Figure 2 (p. 5).
*   **Problem:** The y-axis of Figure 2 is labeled with "This work 10⁵" and "ΛCDM 10¹²⁰", which is not a standard or clear way to label an axis. It appears to represent the scale of the fine-tuning problem.
*   **Required Fix:** Relabel the y-axis to clearly state the quantity being plotted, for example, "Hierarchy (ρ_theory / ρ_obs)" or "Fine-Tuning Factor".

**P1A-m2: Weak Justification for Gravitational Wave Bound**
*   **Location:** Sec. IX L (p. 13), "Barrier 12".
*   **Problem:** The upper bound on the gravitational wave energy density, `Ω_GW`, is presented without a clear derivation, and the quantitative analysis is "deferred to a forthcoming bounce-GW dedicated paper". As it stands, this barrier is an unsupported assertion.
*   **Required Fix:** Provide at least a robust scaling argument for the `Ω_GW` bound or heavily qualify that this is a conjectural constraint pending further work.

**P1A-m3: Future Date on Manuscript**
*   **Location:** Page 1.
*   **Problem:** The paper is dated "June 2, 2026 PDT".
*   **Required Fix:** The date should be changed to the date of submission.

### NIT-PICKS

**P1A-n1: Typo in Table I**
*   **Location:** Table I, footnote `b` (p. 4).
*   **Problem:** The text reads "63-5σ realistic".
*   **Required Fix:** This appears to be a typo for "3-5σ realistic". Please correct.

**P1A-n2: Placeholder Contact Information**
*   **Location:** Page 1.
*   **Problem:** The author's email is listed as `houston@hubify.com`, which appears to be a placeholder.
*   **Required Fix:** Provide a valid institutional or long-term personal email address.

---

## Summary recommendation

**REJECT**

The manuscript in its current form must be rejected. The central claims regarding dark energy in the ECH framework are built upon a theoretically unsound foundation, namely a dimensionally incorrect operator and an ad-hoc scaling ansatz (E1). The paper itself provides a compelling physical argument (the "reheating thermal-reset barrier") that invalidates the proposed dark-energy mechanism, leading to a fatal internal contradiction (E3). Furthermore, the work's reliance on a large number of unverifiable "in preparation" citations (E2) falls far short of the standards for publication in Physical Review D.

The paper does contain a valuable and well-argued result: the perturbation-transparency theorem (Sec. X). This is a clean, rigorous, and interesting contribution to the literature on ECH gravity. I would strongly encourage the author to extract this result and the associated discussion of its implications (i.e., that tests of `γ` must be sought in non-perturbative channels) and submit it as a new, much shorter, and more focused manuscript. The current paper attempts to combine this sound result with a separate, fatally flawed analysis of dark energy, and the latter invalidates the whole.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the supplementary referee report with additional findings.

================================================================
## Supplementary Referee Report for Manuscript [P1A]

Following an initial review, a second, more detailed examination of the manuscript was conducted to check for issues of arithmetic, dimensional consistency, and internal coherence that may have been missed. This second pass has uncovered several additional, fundamental flaws in the manuscript's theoretical framework. These new findings reinforce and strengthen the original recommendation to reject the paper.

The new findings are listed below, following the same format as the initial report. They should be considered in addition to the points raised previously (P1A-E1, E2, E3, E4, etc.).

---

### NEW ESSENTIAL Revisions

**P1A-E5: The Proposed Action is Not Dimensionless**
*   **Location:** Eq. (5), Eq. (6), Appendix B (p. 19)
*   **Problem:** The parity-odd operator introduced as a "phenomenological ansatz" leads to an action that is not dimensionless, a requirement for any physical theory in natural units (`ħ=c=1`). The author's own dimensional accounting in Appendix B states that the Lagrangian density `L_odd` has a mass dimension of `[L_odd] = +1`. Consequently, the action `S = ∫ d⁴x L_odd` has a mass dimension of `[-4] + [+1] = -3`. A non-dimensionless action is unphysical, as it cannot be used as the phase in a path integral and violates the fundamental principles of dimensional analysis. This is a more severe and basic error than the Lagrangian having an unconventional mass dimension; it represents a failure of the theory's internal consistency.
*   **Required Fix:** This flaw is fatal to the entire dark energy analysis derived from this operator. The operator and all conclusions drawn from it must be removed.

**P1A-E6: Dimensional Inconsistency in the Cosmic Birefringence Equation**
*   **Location:** Sec. IV D, Eq. (17) (p. 10)
*   **Problem:** Equation (17), which is central to the analysis of "Route 4," is dimensionally inconsistent. The left-hand side, the rotation angle `β`, is a dimensionless quantity. The right-hand side, `(α/M) √ρ_θ / m_θ²`, has a net mass dimension of `[-1] + [+2] - [+2] = -1`. An equation cannot equate a dimensionless quantity to one with units of inverse mass.
*   **Required Fix:** This dimensional error invalidates the quantitative argument for closing Route 4, which relies on this equation to connect the observed birefringence signal to the dark energy density via the spectator mass `m_θ`. The equation and the corresponding argument must be removed or completely re-derived from a dimensionally consistent starting point.

### NEW MAJOR Revisions

**P1A-M3: Inconsistent Number of e-folds (`N_tot`) Used in Paper**
*   **Location:** Figure 2 (p. 5) vs. Sec. VII (p. 7) and Sec. XIV D (p. 17)
*   **Problem:** There is a major numerical inconsistency in the number of inflationary e-folds used in different parts of the manuscript. Figure 2, which illustrates the energy density hierarchy, explicitly shows a dilution based on `N ≈ 55` e-folds. However, the central dark energy argument presented in the text, and the subsequent "structural tension" claim, critically depends on a value of `N_tot ≈ 92` e-folds. These values are significantly different and their inconsistent use confuses the paper's core narrative. The `N≈55` value may be a stale number from a separate, unrelated constraint (e.g., dilution of cosmic rotation).
*   **Required Fix:** The inconsistency must be resolved. All parts of the paper must use a single, consistently derived value for `N_tot`. Given that the derivation of `N_tot ≈ 92` is itself based on the flawed premises identified in E1 and E5, this entire line of reasoning is suspect.

### NEW MINOR Revisions

**P1A-m4: Confusing and Contradictory Logic in Figure 1**
*   **Location:** Figure 1 (p. 4)
*   **Problem:** The flowchart in Figure 1 is logically confusing regarding ekpyrotic models. It shows an arrow from "Ekpyrotic" to "ECH" labeled "produces ECH; permitted," which suggests a viable connection. However, the "Ekpyrotic" box itself is bordered and labeled "structurally closed (this paper)." It is contradictory to claim a channel is both "permitted" and "closed" by the same work.
*   **Required Fix:** The logic of the flowchart must be clarified. The claim that this paper closes the entire class of ekpyrotic models (as noted in M2) should be removed, and the relationship to ECH must be stated without contradiction.

**P1A-m5: Incorrect Internal Cross-Reference for Omitted Operator**
*   **Location:** Abstract (p. 1), Sec. I (p. 3)
*   **Problem:** The manuscript states that a "parity-odd four-fermion partner" operator is an acknowledged omission from its four-route analysis and refers the reader to Section XI for its mention. However, Section XI ("The Hybrid Dark-Energy Loophole") does not contain any discussion of this operator. This operator is therefore introduced as being outside the paper's scope but is never properly contextualized.
*   **Required Fix:** The cross-reference should be corrected to point to the correct location, or if no such discussion exists, the reference should be removed.

---

## Final Summary Recommendation

**REJECT**

This second, more rigorous review has uncovered additional, fatal flaws that go to the heart of the paper's theoretical construction. The findings of a non-dimensionless action (E5) and a dimensionally inconsistent key equation (E6) are basic errors that invalidate the entire dark-energy portion of the manuscript. These issues are more fundamental than the questionable "ansatz" identified in the first review.

The conclusion remains the same, but the justification is now significantly stronger. The manuscript is not suitable for publication. The author should be strongly encouraged to abandon the flawed dark-energy analysis and focus exclusively on the perturbation-transparency theorem (Sec. X), which appears to be a sound and valuable result that could form the basis of a new, focused, and publishable paper.