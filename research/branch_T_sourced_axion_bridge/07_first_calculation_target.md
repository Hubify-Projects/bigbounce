# Branch T: First Calculation Target Assessment

**Date:** 2026-03-16

---

## Does any candidate survive for Phase 2?

**No.**

The screening in File 06 shows zero candidates passing all three gates (source, amplitude, observable). The best candidate (A: derivative coupling to axial current) fails at two gates independently:

1. **Source gate failure:** The net axion kick through a symmetric bounce vanishes at leading order. The subleading contribution requires both a pre-existing chiral asymmetry n_5 (free parameter) and significant dissipation (model-dependent). Neither is a prediction of spin-torsion cosmology.

2. **Observable gate failure:** Even granting xi ~ 1, the resulting signal is either (a) at undetectable frequencies (GW at 10^{11} Hz), (b) at unresolvable coherence scales (B-fields at mm scale), or (c) degenerate with generic ALP initial conditions (birefringence).

---

## What a Phase 2 calculation would look like (hypothetically)

If one were to proceed despite these failures, the natural first calculation would be:

**Numerical integration of the axion EOM through the ECH bounce:**

    a-ddot + 3 H(t) a-dot + m_a^2 a = (1/f_a) [J-dot^5_0(t) + 3 H(t) J^5_0(t)]

with H(t) from the modified Friedmann equation and J^5_0(t) from a thermal model with specified n_5.

This calculation is straightforward (single ODE, ~ 10 lines of code) but would only confirm what the analytic estimates already show: Delta(a-dot) ~ n_5/f_a with the result depending linearly on the free parameter n_5.

**This calculation would not resolve the branch.** It would parametrize the degeneracy, not break it.

---

## What WOULD resolve the branch

The branch could only be revived if one of the following were established:

1. **The bounce is NOT time-reversal symmetric.** This would require dissipative processes during the bounce (particle production, viscosity) that break t -> -t symmetry. But these are model-dependent additions, not features of the minimal ECH or PGT framework.

2. **The gravitational chiral anomaly is nonzero at the bounce.** This requires R-tilde-R != 0, which requires departing from FRW (anisotropic bounce, e.g., Bianchi-I). But anisotropic bouncing cosmology is a different research program, and the ECH bounce is derived assuming FRW.

3. **A new coupling exists that sources a at the background level on FRW.** All known couplings (A-G) have been screened. A new one would require physics beyond Riemann-Cartan geometry (e.g., non-metricity, higher-dimensional operators). This is beyond the scope of the current program.

4. **The bounce occurs at a scale low enough to produce signals in detector bands, while simultaneously having xi >> 1.** These requirements are contradictory: lower bounce scale reduces xi (File 03).

---

## Recommendation

**Do not proceed to Phase 2.** The branch is closed by three independent barriers:
- Barrier 18 (symmetric bounce cancellation)
- Barrier 19 (amplification duration too short)
- Barrier 20 (backreaction ceiling)

The honest assessment is that the "axion bridge" idea, while creative, inherits the same fundamental problem as all prior branches: the spin-torsion bounce on FRW is too symmetric, too brief, and too energetic to produce perturbative observable signatures through any known coupling.

Record the three new barriers and close Branch T.
