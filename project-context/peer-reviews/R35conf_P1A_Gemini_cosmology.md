# P1A R35conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1a_ech_nogo_v1A.0.64.pdf` md5=03392974 pages=28
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (13220 chars)
**Wall time**: 171.5s

---

## Referee Report for "Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter"

**Manuscript ID:** [Not provided]
**Journal:** Physical Review D

### Summary of the Paper
This manuscript investigates four potential channels within minimal Einstein-Cartan-Holst (ECH) theory as sources for late-time cosmic acceleration. The authors conclude that all four channels are closed under a set of stated assumptions. Three routes are found to be amplitude-suppressed, while the fourth (a spectator ALP coupling) is closed by a naturalness objection, as it reintroduces the cosmological constant fine-tuning problem. The paper's two main positive results are (1) a "perturbation transparency" theorem, showing that for canonical scalar matter, the Holst sector of ECH gravity decouples from scalar and tensor perturbations at all orders, and (2) a "structural tension" between the large number of e-folds required for the ECH dark-energy mechanism and the survival of a predicted matter-bounce non-Gaussianity signature (`f_NL = -35/8`). The paper presents a systematic catalog of 13 independent constraints on these ECH dark-energy routes.

### General Comments
The paper addresses a well-motivated question: whether the additional degrees of freedom in ECH gravity, a natural extension of General Relativity, can resolve the dark energy problem. The systematic approach of enumerating and constraining specific physical channels is commendable. The two primary findings—the perturbation transparency result and the structural tension with bounce observables—are significant, novel, and appear to be robustly derived within the paper's stated scope. The transparency result, in particular, is a clean and important clarification for the phenomenology of ECH cosmology.

However, the manuscript has two essential issues that prevent its publication in its current form. First, the dark-energy mechanism that the paper sets out to constrain is not derived from a controlled effective field theory (EFT) but relies on a phenomenological scaling ansatz for an operator with an incorrect mass dimension. This foundational weakness must be framed more explicitly. Second, the paper is not self-contained, depending heavily on unpublished companion papers for all of its quantitative observational results, including cosmological parameter fits and forecasts. This makes verification of its claims impossible.

The paper is well-written and logically structured, but these fundamental issues must be addressed before it can be considered for publication.

---
### Detailed Findings

#### ESSENTIAL REVISIONS

**P1A-E1: The Dark-Energy Mechanism Relies on a Phenomenological Ansatz, Not a Controlled Derivation**
*   **Location:** Abstract (p. 1), Sec. II A 2 (p. 6), Sec. II C (p. 8), Appendix B (p. 25).
*   **Problem:** The entire framework for generating dark energy from ECH rests on a parity-odd operator (Eq. 6) that has an off-shell mass dimension of +1, not the +4 required for a Lagrangian density term. To bridge this gap, the paper introduces a phenomenological on-shell scaling ansatz (Eq. B2), `ρ_bounce ~ (α/M) M_Pl^3`. This is explicitly and correctly acknowledged as an ansatz, not a derivation. However, this means the dark-energy model under investigation is not a rigorously derived, low-energy limit of a fundamental theory but rather a phenomenological construction. The paper's main achievement is thus the closure of these specific phenomenological routes, which is a strong negative result.
*   **Required Fix:** This fundamental limitation must be stated more prominently and its implications clarified in the Abstract and Introduction. The framing should be adjusted to emphasize that the paper demonstrates the failure of a plausible *phenomenological* construction, rather than presenting a definitive no-go theorem for any possible ECH-based dark energy model. The abstract's current wording is accurate but does not fully convey the severity of this limitation from an EFT perspective.

**P1A-E2: Manuscript Is Not Self-Contained**
*   **Location:** Throughout the manuscript. Specific examples: Abstract (p. 1), Companion Paper summary (p. 4), Sec. III (p. 10), Sec. IV E (p. 14), Sec. XIII (p. 21), Table IV (p. 26).
*   **Problem:** The paper critically relies on quantitative results from companion papers cited as "[2, 6]," which are described as "in preparation" or "posted concurrently." These include the SPHEREx Fisher forecast for `f_NL`, all MCMC cosmological parameter fits (`H_0`, `ΔN_eff`), ALP parameter fitting, and pipeline validation. Without access to these papers and their methods, a referee cannot verify the quantitative claims that underpin parts of the argument (e.g., the consistency of the framework with ΛCDM parameters or the forecast significance of surviving tests). The peer review process requires that a manuscript be evaluable on its own merits.
*   **Required Fix:** The manuscript must be made self-contained. Key methods and results from the companion papers must be summarized in sufficient detail (e.g., in appendices) to allow for independent assessment. This includes, at a minimum:
    1.  A summary of the MCMC analysis setup (datasets, priors, likelihoods) and key posterior plots for the quoted cosmological parameters.
    2.  A summary of the Fisher forecast methodology for the `f_NL` prediction, including assumptions about systematics.
    Alternatively, publication of this manuscript must be contingent on the prior publication of the essential companion papers in a peer-reviewed journal.

#### MAJOR REVISIONS

**P1A-M1: Scope of "Channel-Level Closure" vs. Operator-Basis Closure**
*   **Location:** Abstract (p. 1), Sec. I (p. 3), Sec. IV (p. 10).
*   **Problem:** The paper is careful to state that it performs a "channel-level assessment" and not a full "operator-level theorem," and it explicitly lists omitted operators (e.g., gravitational Chern-Simons `R \tilde{R}`). However, the headline-level claims of "closure" could be misinterpreted by a reader as a more comprehensive no-go theorem than is actually proven.
*   **Required Fix:** The Abstract and Conclusions should more explicitly state which specific operators are excluded from this analysis, reinforcing the scope of the claim. While the title is accurate, the summary sections must ensure there is no ambiguity about the completeness of the operator basis considered.

**P1A-M2: Justification of the `(T_reh/M_GUT)^3/2` Prefactor**
*   **Location:** Sec. II C 1 (p. 8).
*   **Problem:** The inflationary suppression factor `D_inf` (Eq. 11) contains a prefactor `(T_reh/M_GUT)^3/2`. The justification for this term is based on dimensional and phase-space arguments, and the paper notes it is a "phenomenological phase-space ansatz." This introduces another layer of phenomenological uncertainty into the core dark-energy dilution argument.
*   **Required Fix:** The authors should provide a more robust justification for the claim that this factor does not affect the fine-tuning hierarchy. A sensitivity analysis showing how the required `N_tot` changes for different plausible values of this prefactor (e.g., varying it by an order of magnitude) should be included to demonstrate the stability of the conclusion.

**P1A-M3: Conditional Nature of the "Reheating Thermal-Reset Barrier"**
*   **Location:** Sec. II C 1 (p. 9).
*   **Problem:** The paper presents a plausible thermodynamic argument that any bounce-era axial current would be washed out during reheating. However, it is explicitly stated that a "full Boltzmann calculation... is left to a follow-up" and the conclusion is "contingent on the inequality `Γ_wash > H` being satisfied in detail."
*   **Required Fix:** This argument should be clearly framed as a conditional, supporting point, not as a primary closure result with the same standing as the others. The text should be restructured to state the condition first and then explain its consequences, making clear that it is a plausible but unproven erasure mechanism within this work.

#### MINOR REVISIONS

**P1A-m1: Ambiguity in the Definition of the Scale `M`**
*   **Location:** Sec. II A 2 (p. 6).
*   **Problem:** The mass scale `M` is introduced in Eq. (5) and defined as `M = M_area-gap ~ M_Pl / sqrt(γ)`. However, the combination `α/M` is later treated as a single phenomenological parameter constrained by data.
*   **Required Fix:** At its first introduction, clarify that while `M` has a theoretical origin as the LQG area-gap scale, the full coupling `α/M` is treated as an effective parameter whose value is determined phenomenologically. This would resolve any potential confusion.

**P1A-m2: Clarification of Birefringence Discrimination Significance**
*   **Location:** Sec. XV (p. 24).
*   **Problem:** The paper correctly computes that LiteBIRD will distinguish the `β=0.27°` benchmark from the current `β=0.342°` central value at only `~0.73σ`. However, the preceding sentence mentions a `~9σ` detection. This refers to two different null hypotheses (`β=0` vs. `β=0.342°`), which could be confusing.
*   **Required Fix:** Rephrase to make the distinction between the two statistical tests explicit. For example: "While LiteBIRD is forecast to detect a non-zero signal at high significance (~9σ against the `β=0` null hypothesis), it will not by itself distinguish the `β=0.27°` benchmark from the current observational central value at high significance (a ~0.73σ separation)."

**P1A-m3: Non-Standard Terminology**
*   **Location:** Sec. IX M (p. 18).
*   **Problem:** Barrier 13 is named "Gravitational Democracy." This term is not standard in the literature.
*   **Required Fix:** For clarity, consider renaming this to a more standard term like "Universal Torsion Coupling," perhaps retaining the author's preferred term in parentheses.

#### NIT-PICKS / COSMETIC

**P1A-N1:** The date of the paper is set in the future ("June 12, 2026"). This should be corrected. (p. 1)
**P1A-N2:** The notation for the dual Riemann tensor in the abstract ("RAŘ") is unconventional. Please use standard notation like `R \tilde{R}`. (p. 1)
**P1A-N3:** Footnote `a` in the table of contents (p. 2) contains a crucial technical clarification about the Bianchi-identity vanishing. This point is important enough to be moved into the main text of Section X where the result is derived.
**P1A-N4:** A redundant phrase appears in Sec. XIV D: "bounce-era physical scales kphys kbounce". This should be corrected to "bounce-era physical scales k_bounce^phys". (p. 23)
**P1A-N5:** The abstract uses `B_obs` for the observed birefringence angle, while the body often uses `β_obs`. Please use consistent notation throughout. (p. 1, 13)

---
## Summary Recommendation

**MAJOR REVISIONS**

This paper presents novel and significant theoretical results concerning the viability of minimal ECH gravity as a source for dark energy. The perturbation transparency theorem and the structural tension between dark energy generation and bounce observables are valuable contributions. However, the paper cannot be published in its current form due to two essential issues: its reliance on a phenomenological ansatz for the dark energy mechanism and its dependence on unpublished companion papers for all key quantitative results.

I recommend that the paper undergo major revisions to address these points. The authors must make the work self-contained by incorporating the necessary methodological details and results from the companion papers. They must also reframe the manuscript to more clearly reflect the phenomenological nature of the dark energy model being constrained. If these structural problems are resolved, the revised manuscript would likely be suitable for publication in Physical Review D.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the updated referee report, incorporating findings from the second, more rigorous review.

================================================================
## Referee Report for "Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter"

**Manuscript ID:** [Not provided]
**Journal:** Physical Review D

### Summary of the Paper
This manuscript investigates four potential channels within minimal Einstein-Cartan-Holst (ECH) theory as sources for late-time cosmic acceleration. The authors conclude that all four channels are closed under a set of stated assumptions. Three routes are found to be amplitude-suppressed, while the fourth (a spectator ALP coupling) is closed by a naturalness objection, as it reintroduces the cosmological constant fine-tuning problem. The paper's two main positive results are (1) a "perturbation transparency" theorem, showing that for canonical scalar matter, the Holst sector of ECH gravity decouples from scalar and tensor perturbations at all orders, and (2) a "structural tension" between the large number of e-folds required for the ECH dark-energy mechanism and the survival of a predicted matter-bounce non-Gaussianity signature (`f_NL = -35/8`). The paper presents a systematic catalog of 13 independent constraints on these ECH dark-energy routes.

### General Comments
The paper addresses a well-motivated question: whether the additional degrees of freedom in ECH gravity, a natural extension of General Relativity, can resolve the dark energy problem. The systematic approach of enumerating and constraining specific physical channels is commendable. The two primary findings—the perturbation transparency result and the structural tension with bounce observables—are significant, novel, and appear to be robustly derived within the paper's stated scope. The transparency result, in particular, is a clean and important clarification for the phenomenology of ECH cosmology.

However, the manuscript has two essential issues that prevent its publication in its current form. First, the dark-energy mechanism that the paper sets out to constrain is not derived from a controlled effective field theory (EFT) but relies on a phenomenological scaling ansatz for an operator with an incorrect mass dimension. This foundational weakness must be framed more explicitly. Second, the paper is not self-contained, depending heavily on unpublished companion papers for all of its quantitative observational results, including cosmological parameter fits and forecasts. This makes verification of its claims impossible.

The paper is well-written and logically structured, but these fundamental issues must be addressed before it can be considered for publication.

---
### Detailed Findings

#### ESSENTIAL REVISIONS

**P1A-E1: The Dark-Energy Mechanism Relies on a Phenomenological Ansatz, Not a Controlled Derivation**
*   **Location:** Abstract (p. 1), Sec. II A 2 (p. 6), Sec. II C (p. 8), Appendix B (p. 25).
*   **Problem:** The entire framework for generating dark energy from ECH rests on a parity-odd operator (Eq. 6) that has an off-shell mass dimension of +1, not the +4 required for a Lagrangian density term. To bridge this gap, the paper introduces a phenomenological on-shell scaling ansatz (Eq. B2), `ρ_bounce ~ (α/M) M_Pl^3`. This is explicitly and correctly acknowledged as an ansatz, not a derivation. However, this means the dark-energy model under investigation is not a rigorously derived, low-energy limit of a fundamental theory but rather a phenomenological construction. The paper's main achievement is thus the closure of these specific phenomenological routes, which is a strong negative result.
*   **Required Fix:** This fundamental limitation must be stated more prominently and its implications clarified in the Abstract and Introduction. The framing should be adjusted to emphasize that the paper demonstrates the failure of a plausible *phenomenological* construction, rather than presenting a definitive no-go theorem for any possible ECH-based dark energy model. The abstract's current wording is accurate but does not fully convey the severity of this limitation from an EFT perspective.

**P1A-E2: Manuscript Is Not Self-Contained**
*   **Location:** Throughout the manuscript. Specific examples: Abstract (p. 1), Companion Paper summary (p. 4), Sec. III (p. 10), Sec. IV E (p. 14), Sec. XIII (p. 21), Table IV (p. 26).
*   **Problem:** The paper critically relies on quantitative results from companion papers cited as "[2, 6]," which are described as "in preparation" or "posted concurrently." These include the SPHEREx Fisher forecast for `f_NL`, all MCMC cosmological parameter fits (`H_0`, `ΔN_eff`), ALP parameter fitting, and pipeline validation. Without access to these papers and their methods, a referee cannot verify the quantitative claims that underpin parts of the argument (e.g., the consistency of the framework with ΛCDM parameters or the forecast significance of surviving tests). The peer review process requires that a manuscript be evaluable on its own merits.
*   **Required Fix:** The manuscript must be made self-contained. Key methods and results from the companion papers must be summarized in sufficient detail (e.g., in appendices) to allow for independent assessment. This includes, at a minimum:
    1.  A summary of the MCMC analysis setup (datasets, priors, likelihoods) and key posterior plots for the quoted cosmological parameters.
    2.  A summary of the Fisher forecast methodology for the `f_NL` prediction, including assumptions about systematics.
    Alternatively, publication of this manuscript must be contingent on the prior publication of the essential companion papers in a peer-reviewed journal.

#### MAJOR REVISIONS

**P1A-M1: Scope of "Channel-Level Closure" vs. Operator-Basis Closure**
*   **Location:** Abstract (p. 1), Sec. I (p. 3), Sec. IV (p. 10).
*   **Problem:** The paper is careful to state that it performs a "channel-level assessment" and not a full "operator-level theorem," and it explicitly lists omitted operators (e.g., gravitational Chern-Simons `R \tilde{R}`). However, the headline-level claims of "closure" could be misinterpreted by a reader as a more comprehensive no-go theorem than is actually proven.
*   **Required Fix:** The Abstract and Conclusions should more explicitly state which specific operators are excluded from this analysis, reinforcing the scope of the claim. While the title is accurate, the summary sections must ensure there is no ambiguity about the completeness of the operator basis considered.

**P1A-M2: Justification of the `(T_reh/M_GUT)^3/2` Prefactor**
*   **Location:** Sec. II C 1 (p. 8).
*   **Problem:** The inflationary suppression factor `D_inf` (Eq. 11) contains a prefactor `(T_reh/M_GUT)^3/2`. The justification for this term is based on dimensional and phase-space arguments, and the paper notes it is a "phenomenological phase-space ansatz." This introduces another layer of phenomenological uncertainty into the core dark-energy dilution argument.
*   **Required Fix:** The authors should provide a more robust justification for the claim that this factor does not affect the fine-tuning hierarchy. A sensitivity analysis showing how the required `N_tot` changes for different plausible values of this prefactor (e.g., varying it by an order of magnitude) should be included to demonstrate the stability of the conclusion.

**P1A-M3: Conditional Nature of the "Reheating Thermal-Reset Barrier"**
*   **Location:** Sec. II C 1 (p. 9).
*   **Problem:** The paper presents a plausible thermodynamic argument that any bounce-era axial current would be washed out during reheating. However, it is explicitly stated that a "full Boltzmann calculation... is left to a follow-up" and the conclusion is "contingent on the inequality `Γ_wash > H` being satisfied in detail."
*   **Required Fix:** This argument should be clearly framed as a conditional, supporting point, not as a primary closure result with the same standing as the others. The text should be restructured to state the condition first and then explain its consequences, making clear that it is a plausible but unproven erasure mechanism within this work.

**P1A-M4: Missing Factor of π in Four-Fermion Interaction**
*   **Location:** p. 6, Eq. (4).
*   **Problem:** The standard Hehl-Datta derivation of the four-fermion contact term from integrating out torsion in the Einstein-Cartan action (with coupling `κ = 8πG`) yields a coefficient of `(3/16)κ = 3πG/2`. The paper's Holst-modified version in Eq. (4) is given as `Lint = (3GN/2) * (γ^2/(γ^2+1)) * J5^μ J5μ`. Assuming `GN` is Newton's constant `G`, this expression appears to be missing a factor of `π`.
*   **Required Fix:** The authors must clarify the normalization of `GN` or correct the coefficient in Eq. (4). While this does not affect the main conclusions of the paper (since Route 1 is closed regardless of the exact coefficient), it is a matter of correctness in the theoretical framework.

#### MINOR REVISIONS

**P1A-m1: Ambiguity in the Definition of the Scale `M`**
*   **Location:** Sec. II A 2 (p. 6).
*   **Problem:** The mass scale `M` is introduced in Eq. (5) and defined as `M = M_area-gap ~ M_Pl / sqrt(γ)`. However, the combination `α/M` is later treated as a single phenomenological parameter constrained by data.
*   **Required Fix:** At its first introduction, clarify that while `M` has a theoretical origin as the LQG area-gap scale, the full coupling `α/M` is treated as an effective parameter whose value is determined phenomenologically. This would resolve any potential confusion.

**P1A-m2: Clarification of Birefringence Discrimination Significance**
*   **Location:** Sec. XV (p. 24).
*   **Problem:** The paper correctly computes that LiteBIRD will distinguish the `β=0.27°` benchmark from the current `β=0.342°` central value at only `~0.73σ`. However, the preceding sentence mentions a `~9σ` detection. This refers to two different null hypotheses (`β=0` vs. `β=0.342°`), which could be confusing.
*   **Required Fix:** Rephrase to make the distinction between the two statistical tests explicit. For example: "While LiteBIRD is forecast to detect a non-zero signal at high significance (~9σ against the `β=0` null hypothesis), it will not by itself distinguish the `β=0.27°` benchmark from the current observational central value at high significance (a ~0.73σ separation)."

**P1A-m3: Non-Standard Terminology**
*   **Location:** Sec. IX M (p. 18).
*   **Problem:** Barrier 13 is named "Gravitational Democracy." This term is not standard in the literature.
*   **Required Fix:** For clarity, consider renaming this to a more standard term like "Universal Torsion Coupling," perhaps retaining the author's preferred term in parentheses.

**P1A-m4: Incorrect Internal Cross-Reference**
*   **Location:** p. 21, first paragraph of Sec. B.
*   **Problem:** The text discusses the `m_ϕ ~ H0` tuning and cites `§IV D` and `§XI`. The reference to `§XI` ("The Hybrid Dark-Energy Loophole") is incorrect, as this section does not address the `m_ϕ ~ H0` tuning.
*   **Required Fix:** Correct the cross-reference from `§XI` to the more appropriate section(s), e.g., `§XIII`.

#### NIT-PICKS / COSMETIC

**P1A-N1:** The date of the paper is set in the future ("June 12, 2026"). This should be corrected. (p. 1)
**P1A-N2:** The notation for the dual Riemann tensor in the abstract ("RAŘ") is unconventional. Please use standard notation like `R \tilde{R}`. (p. 1)
**P1A-N3:** Footnote `a` in the table of contents (p. 2) contains a crucial technical clarification about the Bianchi-identity vanishing. This point is important enough to be moved into the main text of Section X where the result is derived.
**P1A-N4:** A redundant phrase appears in Sec. XIV D: "bounce-era physical scales kphys kbounce". This should be corrected to "bounce-era physical scales k_bounce^phys". (p. 23)
**P1A-N5:** The abstract uses `B_obs` for the observed birefringence angle, while the body often uses `β_obs`. Please use consistent notation throughout. (p. 1, 13)

---
## Summary Recommendation

**MAJOR REVISIONS**

This paper presents novel and significant theoretical results concerning the viability of minimal ECH gravity as a source for dark energy. The perturbation transparency theorem and the structural tension between dark energy generation and bounce observables are valuable contributions. However, the paper cannot be published in its current form due to two essential issues: its reliance on a phenomenological ansatz for the dark energy mechanism and its dependence on unpublished companion papers for all key quantitative results.

I recommend that the paper undergo major revisions to address these points. The authors must make the work self-contained by incorporating the necessary methodological details and results from the companion papers. They must also reframe the manuscript to more clearly reflect the phenomenological nature of the dark energy model being constrained. If these structural problems are resolved, the revised manuscript would likely be suitable for publication in Physical Review D.