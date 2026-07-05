# P2 — Cubic-order bounce transmission of the bispectrum: does nonlinear superhorizon ζ-conservation remove the "conditional"?

Date: 2026-07-04
Reviewer MAJOR addressed: "the f_NL forecast is conditional on an UNVERIFIED cubic-order bounce transmission (assumption (d)); the 3rd-order bispectrum transfer through the bounce is backed only by an order-of-magnitude superhorizon estimate, not a real calculation."

Verdict: **PARTIAL RESOLUTION — the conditional can be SOFTENED and given a real physical argument, but NOT removed outright.** The nonlinear superhorizon ζ-conservation theorem (Lyth-Wands-Malik / Salopek-Bond / Maldacena / δN) applies to P2's Wilson-Ewing LQC bounce *conditionally on ζ not growing through the bounce*, which is exactly the property the Wilson-Ewing model was constructed to satisfy (LQC tensor suppression + c_s ≪ 1, not scalar amplification). This is a genuine strengthening — it converts "backed only by a scaling estimate" into "supported by nonlinear superhorizon ζ-conservation, valid in the sub-class of bounces (Wilson-Ewing/LQC) that suppress r without amplifying ζ" — but there remains a real residual: (i) the Quintin–Sherkatghanad–Cai–Brandenberger no-go (arXiv:1508.04141) shows a *generic* single-field NEC-violating bounce in GR that suppresses r by growing ζ WOULD modify f_NL, and (ii) whether the specific LQC bounce dynamics keep ζ̇→0 through the NEC-violating phase at *cubic* order has not been computed for this model. So the honest upgrade is "conditional → argued-plausible, with the obstruction now named precisely," not "conditional → derived."

---

## 1. The bounce model and the matching structure P2 assumes

P2's model (Sec. "The Viable Model", `02_full_draft.tex:762`) is the **Cai–Wilson-Ewing ΛCDM quasi-dust matter bounce** (`WilsonEwing:2012`; the ΛCDM-bounce realization is Cai & Wilson-Ewing arXiv:1412.2914):

- Single scalar-like matter sector, matter-dominated contraction (w = 0, ε = 3/2), Bunch-Davies vacuum on sub-Hubble scales (assumptions (a)–(c)).
- The nonsingular bounce is provided by **Loop Quantum Cosmology quantum-geometry** effects at high curvature, NOT by a NEC-violating classical scalar in pure GR.
- Tensor-to-scalar ratio r_t ≈ 10⁻⁴ comes from **LQC quantum-geometry tensor suppression during the bounce** (`02_full_draft.tex:762`), and the scalar amplitude / red tilt come from a slightly-negative effective w and a CDM sound speed c_s (Cai–Wilson-Ewing).
- Assumption (d): "faithful transmission of the bispectrum through the bounce at third order." Verified at linear order (Wilson-Ewing 2012); at cubic order backed only by (kη_bounce)² ~ 10⁻⁴ ⇒ δf_NL ~ 10⁻³ (a scaling estimate, `02_full_draft.tex:758`).

The observationally relevant modes are **deep superhorizon at the bounce**: P2's own estimate gives kη_bounce ~ 10⁻², i.e. (kη_bounce)² ~ 10⁻⁴. This is the regime in which superhorizon conservation theorems live.

## 2. The standard result: nonlinear superhorizon ζ-conservation

The relevant theorems:

- **Lyth, Malik & Sasaki (astro-ph/0411220) / Lyth & Wands / Wands-Malik-Lyth-Liddle (astro-ph/0003278):** on scales far outside the horizon, the curvature perturbation ζ on uniform-density slices is conserved **to all (nonlinear) orders** provided the pressure perturbation is **adiabatic** (non-adiabatic/entropy pressure negligible). This is a consequence of local energy conservation + the separate-universe (long-wavelength gradient-expansion) picture and is **independent of the gravitational field equations**.
- **Separate-universe / δN at nonlinear order (Sasaki-Stewart → Lyth-Rodriguez):** ζ(x) = δN(x) is conserved on superhorizon scales for adiabatic single-clock evolution; the nonlinear consistency (Maldacena squeezed-limit / single-clock) follows.
- Consequence: if ζ is conserved at all orders across the bounce, then **every equal-time n-point correlator of ζ (including the bispectrum) is preserved through the bounce with amplitude ≈ 1**, up to gradient corrections O((kη_bounce)²) — which is exactly P2's 10⁻⁴ estimate, now upgraded from "scaling guess" to "the leading gradient correction to an all-orders conservation theorem."

**The single load-bearing hypothesis of this theorem is ζ̇ → 0 on superhorizon scales (adiabatic, single-clock, no active growing mode).**

## 3. Why it is NOT automatic through a bounce — the Quintin et al. no-go

Quintin, Sherkatghanad, Cai & Brandenberger, arXiv:1508.04141 (PRD 92, 063532) — note two of P2's own cited authors (Cai; and Li-Quintin is `LiQuintin:2017`) — computed the **cubic action and f_NL THROUGH a nonsingular bounce** and found (their Eqs. 41–44, Conjecture 1, Conclusions):

- On super-Hubble scales the spatial-gradient cubic terms vanish (∂_iζ ≃ 0), so the cubic interaction Lagrangian is dominated by the **time-derivative** channel:
  L₃/M_p² ≃ (ε² − ε³/2) a³ ζ ζ̇² − (1/H) ζ ζ̇ d/dt(a z² ζ̇)  (their Eq. 41).
- If ζ **grows** during the bounce (ζ̇ ≠ 0, Δζ = ζ̇ Δt_B), then f_NL is **enhanced**: f_NL ~ (Δζ)²/(Δt_B) · M_p² (their Eq. 44).
- **Conjecture 1 (the no-go):** for a single NEC-violating scalar with c_s = 1 in pure GR and Bunch-Davies vacuum, suppressing r to the observational bound (their Eq. 30–31: |1 + Δζ/ζ| ≳ 50) **requires** amplifying ζ during the bounce, which **necessarily enhances f_NL** beyond observational bounds. Suppressing r and keeping f_NL small cannot be done simultaneously in that class.

**Physics content for P2:** transmission ≈ 1 is NOT model-independent. It holds iff ζ̇ → 0 through the bounce (no scalar growing-mode active). A bounce that suppresses tensors *by growing the scalar* breaks the adiabatic hypothesis of the conservation theorem and modifies the bispectrum at the order being tested. So assumption (d) is genuinely non-trivial — the reviewer MAJOR is correct that it cannot be waved away.

## 4. But P2's Wilson-Ewing/LQC bounce sits in the escape sub-class

Quintin et al. themselves flag the escape routes (their Conclusions, p.20):

1. "*if the initial Bunch-Davies vacuum is noncanonical (e.g., in the ΛCDM bounce [their ref 6], the initial quantum vacuum has c_s ≪ 1), the initial ratio of the tensor modes to the scalar modes can be suppressed, in which case there is no need for the curvature perturbations to be enhanced during the bounce.*" — Their ref [6] IS the Cai–Wilson-Ewing ΛCDM bounce = **P2's model**.
2. "*Our analysis also does not immediately apply to nonsingular matter bounce models in which the violation of the NEC is obtained by changes in the gravitational action (e.g., in Loop Quantum Cosmology ...).*" — LQC is precisely how Wilson-Ewing gets the bounce.

Both escape conditions are satisfied by P2's model **by construction**:
- r_t ≈ 10⁻⁴ comes from **LQC quantum-geometry tensor suppression** (a modified-gravity/quantum-geometry effect at the bounce), NOT from growing ζ. The scalar amplitude is set in the contracting phase; the small c_s of the CDM sound sector further suppresses the tensor-to-scalar ratio at horizon exit.
- Because r is suppressed by the *gravity/quantum-geometry sector and c_s*, the scalar ζ does **not** need to be amplified during the bounce ⇒ ζ̇ → 0 is *allowed* and is the natural expectation for the superhorizon adiabatic mode ⇒ the nonlinear conservation theorem of §2 applies ⇒ transmission ≈ 1 up to O((kη_B)²) ~ 10⁻⁴ gradient corrections.

This is consistent with Wilson-Ewing's own linear result (assumption (d) verified at linear order): the linear ζ is conserved through the LQC bounce precisely because ζ̇ → 0. The nonlinear theorem says: **if the linear superhorizon ζ is conserved (ζ̇→0) for the adiabatic single-clock mode, the same separate-universe argument extends to all orders**, so the bispectrum is conserved with it. The linear verification is therefore *evidence for* the nonlinear conservation, not merely silent about it.

## 5. What still separates "argued" from "derived"

The residual gap the reviewer is entitled to (honest limits):

- The nonlinear conservation theorem requires **adiabaticity through the entire NEC-violating LQC phase**. Verifying ζ̇ → 0 at cubic order across the explicit LQC bounce (not just at linear order) is the calculation not yet done. If the LQC bounce transiently sources an **entropy/non-adiabatic** perturbation, or if the effective z² = a²(ε or c_s-modified) passes through a zero making ζ̇ blow up momentarily (the Appendix-A `z² ~ 1/(η−η_s)²` structure near the classical singular point, regularized by LQC), the adiabatic hypothesis could be locally violated. Wilson-Ewing's LQC regularization removes the singular z² → the constant mode ζ'=0 solution is recovered (their Eq. A6–A7), which is exactly the ζ̇→0 we need — but this has been shown at **linear** order only.
- Multi-component subtlety: during the bounce the effective single-field description could break (LQC effective dynamics + CDM + radiation + Λ), introducing entropy modes that the single-clock theorem excludes.

So the correct honest status is: **transmission ≈ 1 is now supported by (i) an all-orders superhorizon conservation theorem whose single hypothesis (ζ̇→0, adiabatic) is (ii) satisfied at linear order in exactly this model and (iii) NOT forced to fail by the Quintin no-go because P2's bounce escapes it via LQC/c_s tensor suppression rather than scalar growth.** The remaining follow-up is the explicit cubic-order check that ζ̇→0 (adiabaticity) survives the LQC NEC-violating phase — a much more sharply-defined and narrower task than "compute the full cubic in-in across the bounce from scratch."

## 6. Proposed P2 strengthening (NOT applied — proposal only)

Rewrite the assumption-(d) discussion and the load-bearing caveat to replace "supported only by an order-of-magnitude superhorizon-scaling estimate" with the argued version. Suggested insertion into Sec. Assumptions (after the sentence ending "...not a derived bound).", `02_full_draft.tex:758`) and mirrored into the abstract star-caveat and the "Leading theoretical uncertainty" paragraph (`:1142`):

> *Physical support for assumption (d).* The relevant modes are deep superhorizon at the bounce (kη_bounce ~ 10⁻², so gradient corrections are O((kη_bounce)²) ~ 10⁻⁴). For the adiabatic single-clock curvature perturbation, ζ is conserved on superhorizon scales **to all orders in perturbation theory** (Lyth-Malik-Sasaki; Wands-Malik-Lyth-Liddle; Maldacena/δN separate-universe), so if the *linear* superhorizon ζ is conserved through the bounce (ζ̇ → 0), the full bispectrum is conserved with it up to the same O((kη_bounce)²) gradient correction — upgrading the 10⁻⁴ estimate from a scaling guess to the leading gradient correction of a conservation theorem. This conservation is NOT automatic for a generic bounce: Quintin, Sherkatghanad, Cai & Brandenberger [arXiv:1508.04141] show that a single NEC-violating scalar in GR (c_s = 1) that suppresses r *by growing ζ during the bounce* enhances f_NL (their Eq. 44, Conjecture 1). The Wilson-Ewing ΛCDM/LQC bounce **escapes this no-go by construction**: r is suppressed by LQC quantum-geometry tensor suppression and the CDM sound speed c_s ≪ 1 (both flagged as escape routes in [1508.04141], their Conclusions), so ζ need not be amplified and ζ̇ → 0 is the natural adiabatic behavior — consistent with the linear conservation verified in Wilson-Ewing [WilsonEwing:2012]. Assumption (d) is therefore supported by nonlinear superhorizon ζ-conservation in the LQC escape sub-class, and the one remaining check is that adiabaticity (ζ̇ → 0, no transient entropy mode) survives the cubic-order LQC NEC-violating phase — a narrower and sharper computation than a from-scratch full cubic in-in evaluation.

This (a) keeps the caveat honest (still not "derived"), (b) removes the impression that (d) rests on nothing but dimensional analysis, (c) cites the correct standard theorems and the correct counterexample, and (d) names the precise remaining obstruction. **No number changes; no claim of resolution.** Recommend flagging the residual cubic-order adiabaticity check as the refined #1 follow-up (replacing the vaguer "full cubic in-in across the bounce").

## Sources
- Quintin, Sherkatghanad, Cai, Brandenberger, "Evolution of cosmological perturbations and the production of non-Gaussianities through a nonsingular bounce: Indications for a no-go theorem...", arXiv:1508.04141, PRD 92 063532 — Eqs. 30–31, 41–44, Conjecture 1, Conclusions (LQC + c_s≪1 escape routes).
- Cai & Wilson-Ewing, "A ΛCDM bounce scenario", arXiv:1412.2914 — LQC tensor suppression + c_s.
- Lyth, Malik, Sasaki, astro-ph/0411220; Wands, Malik, Lyth, Liddle, astro-ph/0003278 — all-orders superhorizon adiabatic ζ-conservation.
- Maldacena astro-ph/0210603; Lyth-Rodriguez nonlinear δN — nonlinear separate-universe conservation.
