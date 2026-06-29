# P1A RA-INT — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/arxiv/paper1a_ech_nogo.pdf` md5=b5197dc0 pages=32
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (13482 chars)
**Wall time**: 194.9s

---

Here is a complete referee report for the submitted paper.

## Referee Report: P1A

**Paper ID:** P1A
**Title:** Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter

### General Comments

This paper undertakes a systematic assessment of minimal Einstein-Cartan-Holst (ECH) gravity as a source for late-time dark energy. It presents two primary results: (1) a "perturbation transparency" theorem for canonical scalar matter, showing that the Holst sector decouples from standard cosmological perturbations, and (2) a "channel-level closure" of four enumerated routes to dark energy, arguing that none are viable under the stated assumptions. The paper also identifies a structural tension between the requirements for the dark-energy mechanism and the observability of a matter-bounce `fNL` signature.

The perturbation transparency result (Sec. X) is a clear, rigorous, and valuable contribution. It correctly applies the first Bianchi identity to demonstrate the decoupling of the Holst term for a torsion-free connection, generalizing previous results. This finding clarifies which observational channels are (and are not) sensitive to the Holst sector in this context.

The four-route closure analysis (Sec. IV) and the associated 14-barrier catalog (Sec. IX) represent a substantial and systematic effort. The arguments for closing routes R1, R2, and R3 are sound within the standard frameworks of torsion elimination and effective field theory power counting. The closure of route R4 via a naturalness argument is also a valid, albeit different style of, constraint.

However, the entire framework for connecting the ECH parity-odd sector to dark energy rests on a "phenomenological on-shell scaling ansatz" (Sec. I.a, Appendix B). This ansatz is required to promote a mass-dimension +1 operator to a dimension +4 energy density. The paper is commendably transparent about this being an assumption rather than a derivation, but this is a foundational weakness that makes all dark-energy-related conclusions conditional. Furthermore, the mathematical expression of this ansatz is dimensionally inconsistent as written, which is an essential issue that must be corrected.

The paper is well-structured, but dense and long. The self-contained nature of the core analytical arguments is a strength, and the practice of isolating imported numerical values (Table II) is appreciated. The distinction between "channel-level" and "operator-level" closure is appropriate and well-maintained.

The paper has the potential to be a valuable contribution to the literature, particularly due to the robust perturbation-transparency result and the systematic barrier analysis. However, it requires major revisions to address the dimensional analysis of its core ansatz and to more carefully frame the conditionality of its dark-energy conclusions.

---
### Findings

#### ESSENTIAL

*   **P1A-E1: Dimensional Inconsistency in the Core Dark-Energy Ansatz**
    *   **Location:** Appendix B (p. 25), Eq. (B2); also impacts Eq. (10) (p. 8) and related discussions.
    *   **Problem:** The central phenomenological relation for the bounce-era energy density, Eq. (B2), is given as `ρ_bounce ~ (α/M) M_Pl^4`. This equation is dimensionally inconsistent. The coupling `α/M` has mass dimension `[α/M] = -1`, while `[M_Pl^4] = +4`. The resulting dimension for `ρ_bounce` is `+3`, not the required `+4` for an energy density. The paper's logic consistently uses the dimensionless combination `[(α/M) M_Pl] ~ 10^-2`. The correct formulation for the energy density should be `ρ_bounce ~ [(α/M) M_Pl] M_Pl^4`, which is dimensionally `[ρ] = (0) * (+4) = +4`. This notational error propagates through the logic connecting the parity-odd operator to the cosmological constant.
    *   **Fix:** Systematically correct this error. All equations and textual descriptions of the energy density derived from the parity-odd sector must be written in a dimensionally consistent form. The most direct fix is to consistently use the dimensionless grouping `[(α/M) M_Pl]` where a dimensionless coupling is intended, and ensure all energy densities scale as `M_Pl^4`. This correction must be applied to Eq. (B2) and verified for consistency in Sec. II.C, Sec. XII.A, and Appendix B.

#### MAJOR

*   **P1A-M1: Foundational Weakness from Und-derived Ansatz**
    *   **Location:** Abstract (p. 1), Sec. I.a (p. 3), Appendix B (p. 25).
    *   **Problem:** The paper's entire dark-energy analysis hinges on a phenomenological ansatz to solve the dimensional mismatch of the parity-odd operator. While the paper is explicit about this, the strength of the "closure" claims should be more carefully qualified. The paper does not close the ECH dark-energy channel in general; it closes four routes *that rely on this specific, un-derived ansatz*. The abstract and conclusions should more strongly reflect this conditionality.
    *   **Fix:** Revise the abstract and conclusions to state more explicitly that the dark-energy channel closures are contingent on the validity of the phenomenological scaling ansatz used to construct a dimension-4 energy density. For example, change "find that each is constrained under stated assumptions" to "find that each is constrained under a key phenomenological scaling ansatz and other stated assumptions." This emphasizes the central role of this non-trivial assumption.

*   **P1A-M2: Hand-waving Nature of Inflationary Prefactor**
    *   **Location:** Sec. II.C.1 (p. 9), Sec. XII.A (p. 21).
    *   **Problem:** The derivation of the inflationary suppression factor `D_inf` includes a prefactor `(T_reh/M_GUT)^(3/2)`, which is described as a "dimensional-analysis aesthetic" and "not calculated from a thermal partition function." This introduces an unquantified theoretical uncertainty into the calculation of `N_tot ≈ 92` and the subsequent "residual fine-tuning" score of `10^5`. While the exponential dependence on `N_tot` dominates, the lack of rigor for the prefactor undermines the precision of these quoted numbers.
    *   **Fix:** The paper should explicitly state that the value `N_tot ≈ 92` has an intrinsic theoretical uncertainty of `O(few)` e-folds from the unknown physics of the bounce-reheating transition, which translates to an order-of-magnitude uncertainty in the `10^5` fine-tuning score. This provides a more accurate representation of the argument's robustness.

#### MINOR

*   **P1A-m1: Misleading Visual Representation of H(z) Deviation**
    *   **Location:** Fig. 3 (p. 29).
    *   **Problem:** The figure compares an ECH benchmark with a Planck-VI ΛCDM reference. The caption correctly states that the visible `~2-3%` deviation in `ΔH/H` is dominated by the different baseline `H_0` values chosen for the two models, not by the dynamical evolution sourced by the ECH term. This makes the plot potentially misleading, as a reader might interpret the orange curve's deviation as the signature of the model itself.
    *   **Fix:** Either replace the figure with an `H_0`-matched comparison to isolate the true dynamical differences (which the caption implies are sub-percent), or revise the figure title to more clearly indicate its illustrative nature, e.g., "Illustrative Comparison of Cosmological Benchmarks" instead of "ECH dark-energy model vs. ACDM Hubble evolution."

*   **P1A-m2: Confusing Text in Appendix B**
    *   **Location:** Appendix B (p. 25).
    *   **Problem:** The text in this appendix is internally inconsistent and confusing. For example, it mentions inserting a "factor of M_Pl^3", which is dimensionally incorrect for an energy density and appears to contradict the (also incorrect) Eq. (B2). The distinction between the "on-shell ansatz" and the "local-operator-promotion" is not as clear as it could be.
    *   **Fix:** Rewrite Appendix B for clarity and correctness once P1A-E1 is addressed. Clearly define the dimensionless coupling `g_eff ≡ (α/M) M_Pl`. Then, write the on-shell ansatz as `ρ_bounce = g_eff M_Pl^4`. Separately, define the local operator promotion as modifying the Lagrangian term to `L_odd' = g_eff (M_Pl^3) εe e F`, ensuring the text and equations are unambiguous and dimensionally sound.

*   **P1A-m3: Imprecise Phrasing of Mode Erasure in Abstract**
    *   **Location:** Abstract (p. 1).
    *   **Problem:** The sentence describing the erasure of the `fNL` signal states that a comoving mode `k_SPHEREx` is "pushed to k_phys ~ ... e^32 k_SPHEREx". This mixes comoving and physical scales in a confusing way. The argument is that a comoving scale `k` corresponds to a physical scale `k/a` that becomes deeply sub-horizon during inflation.
    *   **Fix:** Rephrase for clarity. For example: "...by that many e-folds (a contracting-phase mode with a comoving wavenumber `k` accessible to SPHEREx is pushed to a physical wavenumber `k_phys = k/a` that is `~e^32` times larger than the Hubble scale at the bounce, deep inside the inflationary subhorizon regime...)."

#### NIT

*   **P1A-N1: Overly Complex Sentence Structure**
    *   **Location:** Throughout the manuscript.
    *   **Problem:** Many sentences are excessively long and contain multiple nested clauses and parenthetical statements. This significantly impedes readability. For example, the first sentence of the abstract is 71 words long.
    *   **Fix:** Perform a stylistic revision to shorten and simplify sentences throughout the paper. This will improve clarity and impact.

*   **P1A-N2: Informal Punctuation**
    *   **Location:** Abstract (p. 1).
    *   **Problem:** The phrase "explanatory-deficit / cosmological-constant fine-tuning objection" uses an informal slash.
    *   **Fix:** Rephrase using standard conjunctions, e.g., "an objection based on an explanatory deficit and the re-emergence of the cosmological-constant fine-tuning problem."

---
## Summary recommendation

**MAJOR REVISIONS**

This paper presents a rigorous and valuable perturbation-transparency theorem for ECH gravity and a comprehensive, systematic analysis of potential dark-energy channels within this framework. These are significant contributions. However, the central claim of "closing" the dark-energy routes is conditional on a phenomenological ansatz that is not derived from theory and is expressed with a dimensionally inconsistent formula. This essential error in the paper's core equation must be fixed. The reliance on this ansatz as a foundational assumption must be framed with greater caution and clarity in the abstract and conclusions. Once these major issues are addressed, the paper will represent a strong and publishable work suitable for Physical Review D.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the complete referee report for the submitted paper.

## Referee Report: P1A

**Paper ID:** P1A
**Title:** Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter

### General Comments

This paper undertakes a systematic assessment of minimal Einstein-Cartan-Holst (ECH) gravity as a source for late-time dark energy. It presents two primary results: (1) a "perturbation transparency" theorem for canonical scalar matter, showing that the Holst sector decouples from standard cosmological perturbations, and (2) a "channel-level closure" of four enumerated routes to dark energy, arguing that none are viable under the stated assumptions. The paper also identifies a structural tension between the requirements for the dark-energy mechanism and the observability of a matter-bounce `fNL` signature.

The perturbation transparency result (Sec. X) is a clear, rigorous, and valuable contribution. It correctly applies the first Bianchi identity to demonstrate the decoupling of the Holst term for a torsion-free connection, generalizing previous results. This finding clarifies which observational channels are (and are not) sensitive to the Holst sector in this context.

The four-route closure analysis (Sec. IV) and the associated 14-barrier catalog (Sec. IX) represent a substantial and systematic effort. The arguments for closing routes R1, R2, and R3 are sound within the standard frameworks of torsion elimination and effective field theory power counting. The closure of route R4 via a naturalness argument is also a valid, albeit different style of, constraint.

However, the entire framework for connecting the ECH parity-odd sector to dark energy rests on a "phenomenological on-shell scaling ansatz" (Sec. I.a, Appendix B). This ansatz is required to promote a mass-dimension +1 operator to a dimension +4 energy density. The paper is commendably transparent about this being an assumption rather than a derivation, but this is a foundational weakness that makes all dark-energy-related conclusions conditional. Furthermore, the mathematical expression of this ansatz is dimensionally inconsistent as written, which is an essential issue that must be corrected.

The paper is well-structured, but dense and long. The self-contained nature of the core analytical arguments is a strength, and the practice of isolating imported numerical values (Table II) is appreciated. The distinction between "channel-level" and "operator-level" closure is appropriate and well-maintained.

The paper has the potential to be a valuable contribution to the literature, particularly due to the robust perturbation-transparency result and the systematic barrier analysis. However, it requires major revisions to address the dimensional analysis of its core ansatz and to more carefully frame the conditionality of its dark-energy conclusions.

---
### Findings

#### ESSENTIAL

*   **P1A-E1: Dimensional Inconsistency in the Core Dark-Energy Ansatz**
    *   **Location:** Appendix B (p. 25), Eq. (B2); also impacts Eq. (10) (p. 8) and related discussions.
    *   **Problem:** The central phenomenological relation for the bounce-era energy density, Eq. (B2), is given as `ρ_bounce ~ (α/M) M_Pl^4`. This equation is dimensionally inconsistent. The coupling `α/M` has mass dimension `[α/M] = -1`, while `[M_Pl^4] = +4`. The resulting dimension for `ρ_bounce` is `+3`, not the required `+4` for an energy density. The paper's logic consistently uses the dimensionless combination `[(α/M) M_Pl] ~ 10^-2`. The correct formulation for the energy density should be `ρ_bounce ~ [(α/M) M_Pl] M_Pl^4`, which is dimensionally `[ρ] = (0) * (+4) = +4`. This notational error propagates through the logic connecting the parity-odd operator to the cosmological constant.
    *   **Fix:** Systematically correct this error. All equations and textual descriptions of the energy density derived from the parity-odd sector must be written in a dimensionally consistent form. The most direct fix is to consistently use the dimensionless grouping `[(α/M) M_Pl]` where a dimensionless coupling is intended, and ensure all energy densities scale as `M_Pl^4`. This correction must be applied to Eq. (B2) and verified for consistency in Sec. II.C, Sec. XII.A, and Appendix B.

*   **P1A-E2: Dimensional Inconsistency in `Λ_eff` Definition**
    *   **Location:** Eq. (10) (p. 8).
    *   **Problem:** The effective cosmological constant `Λ_eff` is defined with units of `[mass]^2`, as is standard. However, the first term on the right-hand side, `Ξ M_Pl^4`, has units of `[mass]^4` (since `Ξ` is dimensionless). This makes the equation dimensionally inconsistent. The text below the equation states `ρ_Λ = Λ_eff M_Pl^2 = Ξ M_Pl^4`, which correctly implies `Λ_eff = Ξ M_Pl^2`. The equation as written is incorrect.
    *   **Fix:** Correct Eq. (10) to be dimensionally consistent. Based on the surrounding text, it should likely read `Λ_eff = Ξ M_Pl^2 + c_ω ω^2`.

#### MAJOR

*   **P1A-M1: Foundational Weakness from Und-derived Ansatz**
    *   **Location:** Abstract (p. 1), Sec. I.a (p. 3), Appendix B (p. 25).
    *   **Problem:** The paper's entire dark-energy analysis hinges on a phenomenological ansatz to solve the dimensional mismatch of the parity-odd operator. While the paper is explicit about this, the strength of the "closure" claims should be more carefully qualified. The paper does not close the ECH dark-energy channel in general; it closes four routes *that rely on this specific, un-derived ansatz*. The abstract and conclusions should more strongly reflect this conditionality.
    *   **Fix:** Revise the abstract and conclusions to state more explicitly that the dark-energy channel closures are contingent on the validity of the phenomenological scaling ansatz used to construct a dimension-4 energy density. For example, change "find that each is constrained under stated assumptions" to "find that each is constrained under a key phenomenological scaling ansatz and other stated assumptions." This emphasizes the central role of this non-trivial assumption.

*   **P1A-M2: Hand-waving Nature of Inflationary Prefactor**
    *   **Location:** Sec. II.C.1 (p. 9), Sec. XII.A (p. 21).
    *   **Problem:** The derivation of the inflationary suppression factor `D_inf` includes a prefactor `(T_reh/M_GUT)^(3/2)`, which is described as a "dimensional-analysis aesthetic" and "not calculated from a thermal partition function." This introduces an unquantified theoretical uncertainty into the calculation of `N_tot ≈ 92` and the subsequent "residual fine-tuning" score of `10^5`. While the exponential dependence on `N_tot` dominates, the lack of rigor for the prefactor undermines the precision of these quoted numbers.
    *   **Fix:** The paper should explicitly state that the value `N_tot ≈ 92` has an intrinsic theoretical uncertainty of `O(few)` e-folds from the unknown physics of the bounce-reheating transition, which translates to an order-of-magnitude uncertainty in the `10^5` fine-tuning score. This provides a more accurate representation of the argument's robustness.

*   **P1A-M3: Misleading "Vacuum Energy" Language and Figure**
    *   **Location:** Fig. 2 (p. 8), Sec. II.C.1 (p. 9).
    *   **Problem:** The paper (e.g., in Fig. 2) repeatedly refers to the energy density sourced by the parity-odd term as "vacuum energy." However, the entire argument for its dilution during inflation (`D_inf ∝ e^(-3N_tot)`) is based on the fact that the underlying contorsion field is algebraically sourced by the fermion axial current, which dilutes like a matter species (`n ∝ a⁻³`). A true vacuum energy would have `w = -1` and would not dilute. This is a significant conceptual contradiction.
    *   **Fix:** Remove the "vacuum energy" terminology for this component. Refer to it as "torsion-sourced energy density" or "axial-current energy density." The label `ρ_vac` in Figure 2 is incorrect and must be changed. The figure's text "Parity-odd vacuum energy" should be corrected to reflect its matter-like dilution behavior.

*   **P1A-M4: Contradictory Definition of Coupling `α`**
    *   **Location:** Sec. II.A.2, Eq. (7) (p. 7).
    *   **Problem:** The text explicitly states that `α` is a "dimensionless coupling." However, Eq. (7) is only dimensionally consistent if it is an equation for the quantity `α/M`, which has mass dimension -1. The left-hand side (`α`) and right-hand side (`g²/M * log(...)`) cannot be equal if `α` is dimensionless. This is a fundamental contradiction in the definition of a key parameter.
    *   **Fix:** Clarify the definitions. Either `α` is not dimensionless, or Eq. (7) is an equation for a different quantity (e.g., `α/M`). The text and equations must be made consistent throughout the manuscript.

#### MINOR

*   **P1A-m1: Misleading Visual Representation of H(z) Deviation**
    *   **Location:** Fig. 3 (p. 29).
    *   **Problem:** The figure compares an ECH benchmark with a Planck-VI ΛCDM reference. The caption correctly states that the visible `~2-3%` deviation in `ΔH/H` is dominated by the different baseline `H_0` values chosen for the two models, not by the dynamical evolution sourced by the ECH term. This makes the plot potentially misleading, as a reader might interpret the orange curve's deviation as the signature of the model itself.
    *   **Fix:** Either replace the figure with an `H_0`-matched comparison to isolate the true dynamical differences (which the caption implies are sub-percent), or revise the figure title to more clearly indicate its illustrative nature, e.g., "Illustrative Comparison of Cosmological Benchmarks" instead of "ECH dark-energy model vs. ACDM Hubble evolution."

*   **P1A-m2: Confusing Text in Appendix B**
    *   **Location:** Appendix B (p. 25).
    *   **Problem:** The text in this appendix is internally inconsistent and confusing. For example, it mentions inserting a "factor of M_Pl^3", which is dimensionally incorrect for an energy density and appears to contradict the (also incorrect) Eq. (B2). The distinction between the "on-shell ansatz" and the "local-operator-promotion" is not as clear as it could be.
    *   **Fix:** Rewrite Appendix B for clarity and correctness once P1A-E1 is addressed. Clearly define the dimensionless coupling `g_eff ≡ (α/M) M_Pl`. Then, write the on-shell ansatz as `ρ_bounce = g_eff M_Pl^4`. Separately, define the local operator promotion as modifying the Lagrangian term to `L_odd' = g_eff (M_Pl^3) εe e F`, ensuring the text and equations are unambiguous and dimensionally sound.

*   **P1A-m3: Imprecise Phrasing of Mode Erasure in Abstract**
    *   **Location:** Abstract (p. 1).
    *   **Problem:** The sentence describing the erasure of the `fNL` signal states that a comoving mode `k_SPHEREx` is "pushed to k_phys ~ ... e^32 k_SPHEREx". This mixes comoving and physical scales in a confusing way. The argument is that a comoving scale `k` corresponds to a physical scale `k/a` that becomes deeply sub-horizon during inflation.
    *   **Fix:** Rephrase for clarity. For example: "...by that many e-folds (a contracting-phase mode with a comoving wavenumber `k` accessible to SPHEREx is pushed to a physical wavenumber `k_phys = k/a` that is `~e^32` times larger than the Hubble scale at the bounce, deep inside the inflationary subhorizon regime...)."

#### NIT

*   **P1A-N1: Overly Complex Sentence Structure**
    *   **Location:** Throughout the manuscript.
    *   **Problem:** Many sentences are excessively long and contain multiple nested clauses and parenthetical statements. This significantly impedes readability. For example, the first sentence of the abstract is 71 words long.
    *   **Fix:** Perform a stylistic revision to shorten and simplify sentences throughout the paper. This will improve clarity and impact.

*   **P1A-N2: Informal Punctuation**
    *   **Location:** Abstract (p. 1).
    *   **Problem:** The phrase "explanatory-deficit / cosmological-constant fine-tuning objection" uses an informal slash.
    *   **Fix:** Rephrase using standard conjunctions, e.g., "an objection based on an explanatory deficit and the re-emergence of the cosmological-constant fine-tuning problem."

*   **P1A-N3: Minor Number Mismatch in Figure Caption**
    *   **Location:** Fig. 5 (p. 31).
    *   **Problem:** The caption for the bottom panel quotes the ΛCDM fine-tuning score as `10^120`, while the main text (e.g., Sec. XII.A) uses the more precise `10^122`.
    *   **Fix:** Update the figure's y-axis label or caption to be consistent with the value used in the text.

---
## Summary recommendation

**MAJOR REVISIONS**

This paper presents a rigorous and valuable perturbation-transparency theorem for ECH gravity and a comprehensive, systematic analysis of potential dark-energy channels within this framework. These are significant contributions. However, the central claim of "closing" the dark-energy routes is conditional on a phenomenological ansatz that is not derived from theory and is expressed with multiple, fundamental dimensional and conceptual inconsistencies. These essential errors in the paper's core equations and terminology must be fixed. The reliance on this ansatz as a foundational assumption must be framed with greater caution and clarity in the abstract and conclusions. Once these major issues are addressed, the paper will represent a strong and publishable work suitable for Physical Review D.