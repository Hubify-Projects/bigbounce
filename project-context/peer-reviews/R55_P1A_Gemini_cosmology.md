# P1A R55 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/private/tmp/R55_P1A/paper1a_ech_nogo.pdf` md5=304331a0 pages=29
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (2618 chars)
**Wall time**: 151.7s

---

Here is a complete referee report for the submitted paper.

## Referee Report: P1A

**Paper Title:** Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter
**Author:** Houston Golden
**Manuscript ID:** P1A

### Summary of the Paper

This manuscript undertakes a systematic assessment of four potential channels within minimal Einstein-Cartan-Holst (ECH) gravity to source late-time dark energy. The author concludes that all four channels are closed under a set of stated assumptions. The closure mechanisms are: amplitude suppression for Nambu-Jona-Lasinio (NJL) contact interactions (R1) and one-loop/running-Immirzi effects (R2-R3), and a naturalness/fine-tuning objection for a spectator-field coupling (R4). The paper's central positive result is a "perturbation-transparency" theorem, demonstrating that for canonical scalar matter, the Holst sector decouples from all scalar and tensor perturbation equations of motion, rendering its effects invisible in standard cosmological observables like the power spectrum and bispectrum. The paper also identifies a structural tension between the number of e-folds required for the (failed) dark-energy mechanism and the survival of a matter-bounce signature (`fNL = -35/8`). The work frames surviving observables (`fNL` and cosmic birefringence `β`) as class-level tests of bounce cosmologies and spectator fields, respectively, not as specific predictions of the minimal ECH model.

### General Comments

The paper presents a comprehensive and systematic analysis of a well-defined theoretical framework. The scope is ambitious, and the author is commendably transparent about the assumptions and limitations of the analysis. The distinction between channel-level closure and a full operator-level theorem is crucial and well-maintained. The perturbation-transparency result (Sec. X) is a clean, rigorous, and valuable contribution. The catalog of 13 independent barriers (Sec. IX) provides a robust framework for constraining this class of models.

However, the paper has several significant issues that preclude its publication in the present form. The most critical are its reliance on results from a companion paper that is not yet available, making the current manuscript not self-contained, and the foundational role of a non-standard effective operator with mass dimension +1. While the paper's ultimate conclusion is that the dark-energy mapping based on this operator fails, its prominent role in the framing requires more careful justification and context. The paper would be significantly strengthened by addressing these and other points detailed below.

### Findings

#### ESSENTIAL

*   **P1A-E1: Lack of Self-Containment (Violates Standalone-Reader Test)**
    *   **Location:** Throughout, e.g., Abstract (p. 1), Sec. I (p. 3), Sec. IV (p. 10), Sec. VII (p. 15), Sec. XI (p. 21), Table III (p. 22), Table IV (p. 27).
    *   **Problem:** The paper repeatedly cites a companion paper, "[6] H. Golden, Cobaya MCMC + NaMaster Birefringence + ALP Companion...", for essential results, including MCMC cosmological parameter fits (`H₀`, `ΔN_eff`), pipeline validation, and detailed forecasts. As this companion paper is "in preparation," the current manuscript is not self-contained and its claims cannot be fully verified by a referee. A published paper must stand on its own.
    *   **Fix:** All load-bearing results, parameter values, and methodological details necessary to support the claims of *this* paper must be included within it, either in the main text or in appendices. At a minimum, this includes: the final posterior values and uncertainties for cosmological parameters with a summary of the datasets and priors used (as in Table IV, but with full context), a summary of the MCMC setup and convergence diagnostics, and the core methodology for the `fNL` and `β` forecasts. Placeholder citations to works "in preparation" are not acceptable for central results.

*   **P1A-E2: Non-Standard Effective Operator**
    *   **Location:** Abstract (p. 1), Sec. IIC (p. 7), Appendix B (p. 26).
    *   **Problem:** The entire dark-energy mapping rests on a phenomenological operator (Eq. 6) that has an off-shell mass dimension of +1. This is not a valid local operator in a 4D effective field theory Lagrangian, which must have mass dimension +4. Appendix B acknowledges this and attempts to resolve it via an "on-shell scaling ansatz" that inserts powers of the Planck mass by appealing to bounce-scale geometry. While the author is transparent that this is an ansatz and not a derivation, this premise is physically questionable and violates standard EFT principles. The paper's argument is that this route fails, but building the argument on such a fragile foundation weakens the overall impact.
    *   **Fix:** The status of this operator needs to be addressed more directly in the main text. The introduction and theoretical framework sections should state upfront and unequivocally that the proposed dark-energy mapping requires a departure from standard EFT construction. The discussion should clarify whether any precedent exists for such operators. The paper's conclusion (that the route is closed by other means) remains valid, but the framing must be more cautious to avoid giving the impression that this is a standard starting point.

*   **P1A-E3: Incomparable Significance Values**
    *   **Location:** Abstract (p. 1).
    *   **Problem:** The abstract states: "...WMAP+Planck 1σ band β_obs = 0.342° ± 0.094° (~3.6σ from β = 0, first reported by Minami & Komatsu [3] and refined by Eskilt & Komatsu [4]), and is comparable to the independent ACT DR6 follow-up β = 0.215° ± 0.074° at ~2.9σ... these significances... arise from different null procedures and are not directly comparable...". While the caveat is present, juxtaposing the `~3.6σ` and `~2.9σ` values is still misleading. These are simple "central value / error" ratios against a null of β=0, not proper significances from a full likelihood analysis.
    *   **Fix:** Remove the calculated sigma values (`~3.6σ`, `~2.9σ`) from the abstract. Report the measured values and their uncertainties (`value ± error`) as published. The statement that they are "not directly comparable" is correct and sufficient. The significance of any tension or detection should be discussed in the main body with proper statistical context.

#### MAJOR

*   **P1A-M1: Justification for SPHEREx Forecast Range**
    *   **Location:** Abstract (p. 1, footnote b), Sec. VII (p. 15), Sec. XIII (p. 23).
    *   **Problem:** The paper quotes a "2.6-5σ realistic significance" for SPHEREx detecting `fNL = -35/8`. Footnote `b` (p. 4) and footnote 6 (p. 15) provide some context, citing `σ(fNL) ~ 0.7` (ideal) and `~1.0` (degraded with systematics) from Heinrich et al. [36]. The calculation `fNL / σ(fNL) = |-35/8| / 1.0 = 4.375σ` explains the upper end of the range (rounded to 5σ). However, the origin of the lower `2.6σ` bound is not explained.
    *   **Fix:** Provide a clear, step-by-step derivation for the full `2.6-5σ` range. If this range corresponds to different assumptions about systematics, tracer samples, or analysis methods, these must be explicitly stated. The current explanation is incomplete.

*   **P1A-M2: Proof of Perturbation Transparency**
    *   **Location:** Sec. X.B (p. 20).
    *   **Problem:** The proof of the main theoretical result contains a potentially confusing step. Step 4 states the Holst term vanishes by the first Bianchi identity, `R_μ[νρσ] = 0`. The argument given ("the cyclic-sum identity... contracted with the totally antisymmetric ε^μνρσ leaves no non-trivial component") is correct. However, for many readers, the vanishing of `ε^μνρσ R_μνρσ` is more commonly associated with the pair symmetry `R_μνρσ = R_ρσμν` of the Riemann tensor (which itself depends on the connection being torsion-free).
    *   **Fix:** To improve clarity and rigor, the proof should be slightly expanded. Explicitly write out the contraction of `ε^μνρσ` with the cyclic sum `(R_μνρσ + R_μρσν + R_μσνρ) = 0` to show how the three identical terms sum to zero. Additionally, it would be beneficial to mention that this result can also be seen as a consequence of the index symmetries of the Riemann tensor in a torsion-free geometry.

*   **P1A-M3: Hand-wavy Justification for Thermal Prefactor**
    *   **Location:** Sec. II C 1 (p. 8).
    *   **Problem:** The derivation of the inflationary suppression factor `D_inf` in Eq. (11) includes a prefactor `(T_reh / M_GUT)^(3/2)`. The justification for this half-integer power is described as a "dimensional-analysis aesthetic" and a "phenomenological phase-space ansatz". This is insufficient for a rigorous paper. While the exponential factor dominates, this prefactor is part of a central equation.
    *   **Fix:** The author must either provide a more rigorous derivation for this factor (e.g., from a density-of-states calculation in the relevant thermal context) or explicitly state that it is a toy parameterization and demonstrate that the paper's conclusions are entirely insensitive to its value (e.g., by showing the `N_tot` calculation changes by << 1 e-fold if the prefactor is set to unity). The "thermal-reset barrier" argument on p. 9 is much stronger and should be emphasized as the primary physical closure mechanism for this channel.

#### MINOR

*   **P1A-N1: Future Date on Manuscript**
    *   **Location:** p. 1.
    *   **Problem:** The paper is dated "June 19, 2026". This is presumably a placeholder or a typo.
    *   **Fix:** Correct the date to the date of submission.

*   **P1A-N2: Ambiguity in `fNL` Prediction Status**
    *   **Location:** Table I (p. 4), Abstract (p. 1).
    *   **Problem:** Table I lists `fNL = -35/8` under "Testable prediction?". The abstract correctly clarifies this is "a property of the matter-bounce class... not... ECH itself". The table entry could be misinterpreted.
    *   **Fix:** In Table I, modify the "Testable prediction?" row to read "Surviving class-level prediction?" or add a footnote clarifying that this is not a unique ECH prediction, consistent with the abstract and main text.

*   **P1A-N3: PTA Spectral Index Notation**
    *   **Location:** Fig. 1 (p. 5), Sec. X G (p. 21), Table IV (p. 27).
    *   **Problem:** The paper uses `γ_PTA` for the gravitational-wave background power-law spectral index, while `γ` is used for the Barbero-Immirzi parameter. While the subscript `PTA` provides distinction, the overlapping notation for two key parameters is potentially confusing.
    *   **Fix:** Consider changing the notation for the PTA spectral index to something unambiguous, such as `α_PTA` or `n_GW`, to avoid any possible confusion with the Barbero-Immirzi parameter.

#### NIT

*   **P1A-T1: Typo in Equation Reference**
    *   **Location:** Sec. II A 2 (p. 6, footnote 2).
    *   **Problem:** The text refers to "Hehl 1976 Eq. (3.20)-(3.21) and Freidel-Minic-Takeuchi 2005 Eqs. (7)-(13)". While likely correct, such detailed cross-publisher equation references are fragile.
    *   **Fix:** No change required, but the author should double-check these references for accuracy.

*   **P1A-T2: Redundant Phrasing**
    *   **Location:** Sec. XIV D (p. 24).
    *   **Problem:** The text reads "...bounce-era physical scales k_bounce^phys ~ k_SPHEREx^phys e^(N_tot - N_exit) ~ e^32 k_SPHEREx^phys...". The superscript "phys" is used multiple times.
    *   **Fix:** Simplify to "...bounce-era physical scales k_phys,bounce ~ e^(N_tot - N_exit) k_phys,SPHEREx ~ e^32 k_phys,SPHEREx...".

### Summary Recommendation

**MAJOR REVISIONS**

This paper presents a valuable and rigorous investigation into the viability of minimal ECH gravity as a source for dark energy. The perturbation-transparency theorem is a significant, publishable result, and the systematic closure of the four dark-energy routes is a useful contribution to the literature. The author's transparency regarding assumptions is a major strength.

However, the manuscript in its current form is not acceptable for publication. The reliance on an "in preparation" companion paper for key results makes the work unverifiable and not self-contained. This is an essential flaw that must be rectified. Furthermore, the framing around a non-standard, dimensionally-inconsistent operator, even if to show it fails, requires more careful handling and justification.

I recommend that the paper be reconsidered after major revisions that address the points listed above, with the highest priority on making the paper a self-contained scientific document. If these revisions are carried out successfully, the resulting manuscript would be a strong candidate for publication in Physical Review D.

---

## PASS 2 — self-critique findings (what initial review missed)

Here are the additional findings from the second, more rigorous review.

### Additional Findings

#### MAJOR

*   **P1A-M4: Incorrect Cosmological Baryon Density**
    *   **Location:** Sec. IV A (p. 11).
    *   **Problem:** The calculation of the NJL four-fermion energy density `ρ_NJL` uses a "post-recombination baryon densities `n_b ~ O(10²) cm⁻³`". This value is incorrect for the *cosmological average* baryon density by approximately 9 orders of magnitude (the correct value is `n_b,0 ≈ 2.5 × 10⁻⁷ cm⁻³`). The value used corresponds to a dense interstellar medium, not a cosmologically relevant average. While the ultimate conclusion—that `ρ_NJL` is negligible—is made even stronger by using the correct `n_b`, the use of a physically incorrect input value in a quantitative argument is a serious error.
    *   **Fix:** The calculation must be redone using the correct cosmological average baryon density. The text should be updated to reflect the even greater level of suppression (`~18` additional orders of magnitude) that results.

*   **P1A-M5: Critical Error in Hubble Constant Value**
    *   **Location:** Sec. IV D (p. 14).
    *   **Problem:** The argument for closing Route 4 (spectator ALP) rests on a fine-tuning objection: that matching both `β_obs` and `ρ_Λ` requires tuning the ALP mass `m_ϕ ~ H₀`. This calculation uses the value `H₀ ≈ 1.5 × 10⁻³³ eV`. This is incorrect; the correct value is `H₀ ≈ 1.5 × 10⁻³⁵ eV`. The value used in the paper is off by a factor of 100. The spectator energy density scales as `ρ_ϕ ∝ m_ϕ²`. Therefore, the `ρ_ϕ` calculated in the paper is `100² = 10,000` times larger than it should be. With the correct value for `H₀`, the resulting energy density would be `ρ_ϕ ≈ 1.6 × 10⁻¹⁴ eV⁴`, which is more than three orders of magnitude *smaller* than the observed dark energy density `ρ_Λ ≈ 2.8 × 10⁻¹¹ eV⁴`.
    *   **Impact:** This error completely changes the conclusion for Route 4. The route is not closed by a "naturalness objection" or "re-importing the CC problem". It is closed by a straightforward **amplitude mismatch**. The same coupling that fits `β_obs` underpredicts `ρ_Λ` by over three orders of magnitude, assuming `m_ϕ ~ H₀`. This is a critical flaw that undermines one of the paper's central claims about the four routes.
    *   **Fix:** The entire argument in Sec. IV D must be rewritten. The calculation must use the correct value for `H₀`. The conclusion must be changed to reflect that Route 4, like Routes 1-3, is closed by an amplitude suppression, not a fine-tuning objection. This will also require updates to the abstract and conclusions.