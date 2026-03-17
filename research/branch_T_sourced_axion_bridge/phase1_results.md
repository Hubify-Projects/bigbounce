# Branch T Phase 1 Results: Sourced Axion Bridge

**Date:** 2026-03-16
**Verdict: CLOSED**

---

## Branch hypothesis

An external axion-like particle, coupled to the fermionic axial current via (partial_mu a / f_a) J^{5 mu}, could be "kicked" by the spin-torsion bounce, then amplify gauge fields via the standard a F F-tilde coupling. The axion serves as an information bridge between the Planck-scale bounce and low-energy observables.

## What was tested

Seven candidate source terms (A-G) were enumerated and screened against three gates: nonzero source on FRW, sufficient amplitude (xi >= 1), and mappability to a detectable observable.

## Results

**Zero candidates survive all three gates.**

- Candidates B, D, E, F, G are FATAL (identically zero source on FRW)
- Candidate C reduces to Candidate A after torsion elimination
- Candidate A (the only survivor) FAILS at two gates:
  - Source requires pre-existing chiral asymmetry n_5, a free parameter not predicted by the bounce
  - Symmetric bounce cancellation: the time-reversal symmetry T -> -T of the ECH/PGT bounce gives zero net kick at leading order

Even granting optimistic parameters (maximal n_5, maximal dissipation):
- ECH bounce: xi ~ 1, but backreaction limits xi < 1.1; GW signal at 10^{11} Hz (undetectable); birefringence degenerate with generic ALP misalignment
- PGT bounce: xi ~ (m_T/M_Pl)^{1/2} << 1; no significant amplification

## New barriers identified

| # | Name | Statement |
|---|------|-----------|
| 18 | Bounce symmetry cancellation | Time-reversal symmetry of the ECH/PGT bounce causes the integrated parity-odd source to vanish at leading order |
| 19 | Amplification duration | The bounce lasts ~ 1 e-fold; gauge tachyonic instability requires >> 1 e-folds for significant growth |
| 20 | Backreaction ceiling | At Planck-scale bounce, xi ~ 1 produces rho_X ~ rho_crit; no perturbative amplification regime exists |

## Relation to prior branches

Branch T was designed to circumvent Barrier 14 (Z_2 parity protecting the PGT pseudoscalar mode) by using an EXTERNAL field rather than the torsion mode itself. This bypass works — the external axion is not protected by Z_2. But three new barriers arise that are independent of the Z_2 issue:

- Barrier 18 is a property of the bounce geometry (time-reversal symmetry), not the field content
- Barrier 19 is a property of the bounce duration (too short), not the coupling strength
- Barrier 20 is a property of the energy scale (too high for perturbative treatment), not the field species

These barriers apply to ANY external field coupled to the bounce on FRW, not just axions. They represent a general obstruction to using the spin-torsion bounce as a source for any perturbative signal channel.

## Cumulative barrier count

Branches H through T have now identified 20 independent barriers to extracting observable signals from the spin-torsion bounce. The pattern is clear: the bounce is a Planck-scale, parity-symmetric, single-e-fold event on an FRW background. These three properties — scale, symmetry, and brevity — individually and collectively prevent any perturbative observable from surviving to the present epoch.

## Implications for the program

The "axion bridge" was arguably the most promising remaining strategy: it traded direct torsion observables (Planck-suppressed) for indirect amplification through a well-understood instability (axion-gauge tachyonic production). The failure of this strategy, through three barriers that apply to ANY intermediary field, strongly suggests that no perturbative signal channel exists for the minimal spin-torsion bounce on FRW.

Remaining logical possibilities:
1. Non-perturbative effects (instantons, phase transitions) — but these are even harder to calculate and control
2. Anisotropic bounce (Bianchi-I) — breaks FRW assumption, different model
3. Extended bounce (matter bounce, ekpyrotic) — breaks the ECH/PGT bounce mechanism
4. Non-minimal gravity (f(R), higher curvature) — leaves the spin-torsion framework

None of these preserve the identity of the program (minimal spin-torsion cosmology on FRW).

---

**Branch T: CLOSED. No Phase 2 warranted.**
