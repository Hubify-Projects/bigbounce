# Phase 1 Gating Results: PGT Sector II Pseudoscalar Torsion Relic

**Date:** 2026-03-16
**Branch:** P (PGT bounce program)
**Verdict: TORSION_RELIC_CLOSED**

---

## Executive Summary

The Sector II spin-0^- pseudoscalar torsion mode phi(t) = S_0(t) is
kinematically allowed on FRW but has NO dynamical population mechanism
at the bounce. The mode sits at phi = 0 as a stable fixed point, and
the bounce does not excite it. The relic program has no foundation.

---

## Detailed Findings

### 1. Does the pseudoscalar mode exist on FRW?

**YES, but with a caveat.** The axial vector S_mu = (S_0(t), 0, 0, 0) is
consistent with homogeneity and isotropy. However, S_0 != 0 spontaneously
breaks parity. The FRW field equations (parity-invariant) always admit
S_0 = 0 as a solution. (File 01)

### 2. Is S_0 = 0 stable?

**YES.** The effective mass-squared m_T^2 > 0 means S_0 = 0 is a stable
minimum of the effective potential V = (1/2) m_T^2 phi^2. There is no
tachyonic instability, no symmetry-breaking phase transition. (File 02)

### 3. Does the bounce excite phi from zero?

**NO.** The Klein-Gordon equation phi-ddot + 3H phi-dot + m_T^2 phi = 0
preserves phi = 0 exactly. The Z_2 parity symmetry (phi -> -phi) of the
equations means phi = 0 is a fixed point that cannot be departed without
an explicit parity-breaking source. The time-varying H(t) during the bounce
does NOT break this symmetry. (Files 02, 04)

### 4. What is the natural amplitude phi(0)?

**Zero.** No mechanism sets phi(0) to a nonzero value:
- Self-consistent bounce: works with phi = 0 (contact term alone) (File 03)
- Quantum fluctuations: produce pairs, not a condensate (File 03)
- Chiral matter source: gives phi << M_Pl even for maximal asymmetry (File 03)
- Pre-bounce contraction: amplifies existing phi but cannot create it (File 03)

### 5. IF phi(0) were nonzero (free IC), what happens?

- rho_phi/rho_crit = (1/2)(phi_0/M_Pl)^2 at the bounce
- Post-bounce: frozen (H >> m_T), then oscillating as matter (rho ~ a^{-3})
- Fraction grows relative to radiation (standard moduli problem)
- Decay rate: Gamma ~ m_T^3/M_Pl^2
- But this entire scenario requires ASSUMING phi(0) ~ M_Pl with no justification

### 6. Literature status

The PGT literature (Baekler/Hehl/Nester 2011; Shie/Nester/Yo 2008) confirms
that S_0 is allowed on FRW but does not address the population question in
the context of a bounce. Our analysis fills this gap with a negative result.
The parity-EVEN trace vector T_0 (spin-0+ sector) is naturally nonzero on
FRW; the parity-ODD axial vector S_0 is not. (File 06)

---

## Why CLOSED (not MARGINAL)

The verdict is CLOSED rather than MARGINAL because:

1. **No population mechanism exists.** This is not a quantitative uncertainty
   (e.g., "the amplitude might be small"). It is a structural result: the
   Z_2 parity symmetry of the equations protects phi = 0 as a fixed point.

2. **The bounce is irrelevant to the propagating mode.** The bounce comes from
   the contact interaction (J^5)^2, which is a constraint-level effect. The
   propagating mode is a spectator that does not participate in the bounce
   dynamics.

3. **Assuming phi(0) ~ M_Pl is ad hoc.** There is no theoretical principle
   that selects this initial condition. It would be equivalent to assuming
   any other massive relic starts at O(M_Pl) — possible but unmotivated.

4. **The spin-0+ (trace) sector is qualitatively different.** The trace vector
   T_0 is parity-even and naturally sourced on FRW. If the relic program
   has any future, it would need to use the spin-0+ sector, not the spin-0-.
   But the spin-0+ sector is Sector I, NOT Sector II, and has different
   ghost-free conditions and a different mass spectrum. This would be a
   different program entirely.

---

## Structural lesson

**Barrier 8 (Parity-protection of the pseudoscalar vacuum):** On FRW, the
pseudoscalar torsion mode sits at a parity-symmetric fixed point phi = 0
that cannot be departed by parity-invariant dynamics. The bounce, being a
parity-even event, does not break this symmetry. Population requires either
an explicit parity-breaking source or a tachyonic instability, neither of
which is present in the minimal PGT Sector II model.

This is analogous to the axion misalignment problem: the axion VEV is a free
initial condition set by unknown pre-inflationary physics. But for the axion,
inflation provides a natural mechanism (quantum fluctuations stretched to
superhorizon scales). For the torsion pseudoscalar at a bounce, there is no
analogous mechanism.

---

## Recommended next move

**Branch P (PGT bounce relic program): CLOSE.**

No Phase 2 is warranted. The obstruction is structural (parity symmetry),
not parametric. No parameter choice within Sector II can overcome it.

**Alternative directions (if relic phenomenology is desired):**

1. **Sector I (spin-0+, trace vector):** The trace mode T_0 is parity-even
   and naturally sourced on FRW. Different ghost-free conditions, different
   mass spectrum. Would require a separate gating analysis from scratch.
   Caveat: the mass-coupling lock (Barrier 1) likely applies here too.

2. **Explicit parity violation in the gravity sector:** Adding a gravitational
   Chern-Simons or Nieh-Yan term could source S_0 directly. But this changes
   the model and introduces new parameters. Not minimal.

3. **Abandon relic program, focus on tensor spectrum:** The bounce itself
   (from the contact term) has a distinctive tensor perturbation spectrum
   that does NOT require a propagating torsion relic. This is Branch H
   (already identified). Recommend pursuing Branch H instead.

---

## Files in this analysis

| File | Content | Key result |
|------|---------|------------|
| 01_frw_pseudoscalar_mode.md | FRW symmetry analysis | S_0 allowed but S_0=0 is stable |
| 02_effective_equations.md | Background equations | No source term, phi=0 is fixed point |
| 03_bounce_amplitude_estimate.md | Amplitude estimates | No population mechanism |
| 04_coupled_ode_analysis.ipynb | Numerical verification | Confirms analytical results |
| 05_redshift_behavior.md | Post-bounce evolution | Standard moduli behavior IF populated |
| 06_literature_crosscheck.md | Literature review | Gap in literature, our result is novel |
| phase1_results.md | This file | TORSION_RELIC_CLOSED |
