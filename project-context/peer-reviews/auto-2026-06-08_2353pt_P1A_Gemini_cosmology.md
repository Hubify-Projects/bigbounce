# P1A auto-2026-06-08_2353pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 160.2s

---

**Referee Report on "Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter"**

This manuscript presents a systematic, channel-level investigation into whether minimal Einstein-Cartan-Holst (ECH) gravity can serve as a source for late-time dark energy. The central theoretical result is a "perturbation-transparency theorem," which demonstrates that for canonical scalar matter, the Holst sector decouples from all scalar and tensor perturbations, rendering it invisible to standard cosmological probes. The authors then argue that four primary routes to generate dark energy or parity-odd signatures from ECH are closed at the amplitude level, based on a catalog of 13 independent structural and observational constraints. The paper concludes that while the ECH dark-energy mechanism fails, the broader bounce-cosmology program makes testable predictions, such as a specific non-Gaussianity signature (`fNL = -35/8`), which are independent of the ECH framework.

The paper's core idea—the perturbation transparency—is elegant and appears correct. The systematic cataloging of constraints is a valuable exercise. However, the manuscript is critically flawed by fundamental issues in its dimensional analysis and the presentation of its core operators, which undermine the quantitative aspects of its central argument. Furthermore, several figures and internal-history comments render the paper unsuitable for publication in its current form. Major revisions are required to address these foundational problems.

Below is a detailed list of required revisions.

---
### Detailed Findings

**ESSENTIAL**

*   **P1A-E1 (Dimensionality of Action):** The central parity-odd operator in Eq. (6) has an off-shell mass dimension of +1, and the corresponding action `S_eff` is not dimensionless. This is a fundamental error. An operator in an effective action that contributes to the energy-momentum tensor must have a mass dimension of +4. The author acknowledges this in Appendix B, suggesting a fix by adding powers of `M_Pl` to the coupling (`α/M -> α M_Pl^3 / M^4`). This is not an "equivalent reading"; it is a necessary correction. The entire manuscript must be rewritten using a dimensionally correct, dimension-4 operator from the outset (i.e., in Sec. II), and all subsequent dimensional arguments and numerical estimates must be updated accordingly. The current presentation via an "on-shell scaling ansatz" is not rigorous and is unacceptable for PRD. (Location: Sec II C, Appendix B; pp. 5, 6, 20).
*   **P1A-E2 (Inconsistent Energy Density Equation):** Equation (B2) in the appendix, `ρ_bounce ~ (α/M) M_Pl^3 ~ 10^-2 M_Pl^4`, is dimensionally inconsistent, as a term with mass dimension +3 cannot be equal to a term with mass dimension +4. This equation is central to the quantitative estimate of `N_tot` and must be corrected. The text on p. 21 further confuses the issue by referring to `ρ_bounce ~ M_Pl^4` and a "pseudo-density" `~ 10^-2 M_Pl^4`. The framework must be made internally consistent. (Location: Appendix B; p. 20).
*   **P1A-E3 (Figure/Caption Mismatch):** The legend of Figure 4 ("CMB E-B", "Galaxy Spins") is in direct contradiction with its caption, which describes forecasts for "matter-bounce fNL" and "spectator-ALP cosmic birefringence". The figure is nonsensical as presented; for instance, it shows a rising significance for "Galaxy Spins," which the paper repeatedly states is a confirmed null result. The figure must be completely remade to accurately represent the forecasts discussed in the text and caption. (Location: Sec XIII; p. 18).
*   **P1A-E4 (Internal Version History Comments):** The manuscript contains several remarks about how it was corrected from "earlier versions". Such internal-review artifacts are unprofessional and must be removed from the final publication draft.
    *   Page 2, footnote: "Earlier versions of this manuscript erroneously identified the two..."
    *   Page 16, footnote 2: "An earlier version of this manuscript misidentified the Holst dual contraction with the Pontryagin density."
    (Location: pp. 2, 16).
*   **P1A-E5 (Incomplete Sentence):** A formatting error on page 1 cuts off footnote 'a' mid-sentence ("...distinct from and should"). This must be corrected so the footnote reads as a single, complete block of text. (Location: p. 1).

**MAJOR**

*   **P1A-M1 (Hand-wavy Derivation of Dilution Prefactor):** The `(T_reh/M_GUT)^(3/2)` prefactor in the inflationary dilution formula (Eq. 11) is justified by a "dimensional-analysis aesthetic" and as a "phenomenological phase-space ansatz". This falls far short of a derivation. This factor is crucial for the numerical estimate of `N_tot ≈ 92`, which in turn is central to the "structural tension" argument. The author must either provide a more rigorous justification for this term (e.g., from a density-of-states calculation) or significantly temper the claims that rely on the precise value of `N_tot`. (Location: Sec II C; p. 6).
*   **P1A-M2 (Ambiguous Diagram):** Figure 1, the "observable-prediction map," is confusing. The convention of using crossed-out red arrows to denote a closed channel is not standard and should be explicitly defined in the caption. The diagram also presents a contradictory logic for the Ekpyrotic scenario, which is shown to "produce ECH" but is also "structurally closed". Furthermore, the arrow for the `fNL` prediction should more clearly originate from the "Matter bounce" box, as the text states it is a class-level prediction, not specific to the ECH mechanism being closed. (Location: Sec I; p. 4).
*   **P1A-M3 (Unclear ALP Rotation Angle Formula):** The derivation for the cosmic birefringence angle `β` in Route 4 (Eq. 17) is opaque. The standard result relates `Δβ` to the change in the pseudoscalar field, `Δθ`. The formula presented, involving `ρ_θ/m_θ^2`, is not standard and is given without derivation or a specific citation for that form. This derivation must be clarified to be convincing. (Location: Sec IV D; p. 10).

**MINOR**

*   **P1A-m1 (Confusing Figure Axis):** The y-axis of Figure 2 is labeled with numerical values ("This work 10^5", "ΛCDM 10^120") rather than a physical quantity. It should be relabeled to something more descriptive, such as "Fine-Tuning Hierarchy (Orders of Magnitude)" or "log10(ρ_theory/ρ_obs)". (Location: Sec II A; p. 5).
*   **P1A-m2 (Overly Detailed MCMC Footnote):** The footnote in Table III (p. 17) describing the status of the companion paper's `w_0w_a` MCMC analysis contains excessive internal project details (e.g., "dedicated MPI pod," "GetDist-built posterior covmat"). This should be condensed to a professional statement that the analysis is ongoing and its results are not yet finalized for inclusion. (Location: Sec XII; p. 17).
*   **P1A-m3 (Redundant Subscript):** In the abstract, the expression for the physical wavenumber includes the term `e^32 k_SPHEREx phys`. The final subscript "phys" is redundant and should be removed. (Location: Abstract; p. 1).

**NIT**

*   **P1A-N1 (Future Date):** The paper is dated "June 8, 2026 PDT". The date should be updated to the date of submission. (Location: p. 1).

---
## Summary recommendation
**MAJOR REVISIONS**

The manuscript addresses an important question in theoretical cosmology and presents a novel and compelling theoretical result in its "perturbation-transparency theorem." The systematic approach to constraining theory space is also commendable. However, the paper is critically undermined by fundamental errors in dimensional analysis that invalidate the quantitative foundation of its dark energy argument. These are not simple typos but point to a flawed construction of the core effective operator. Until these essential issues are rectified—requiring a substantial rewrite of the theoretical framework starting from a dimensionally sound action—the paper cannot be accepted. If the authors can successfully reformulate their argument on a solid theoretical footing and correct the numerous other major and minor issues, the revised manuscript could represent a significant contribution to the literature.