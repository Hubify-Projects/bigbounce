# Branch N: First Calculation Target Assessment

**Date:** 2026-03-16

---

## Is There a Phase 2 Target?

After OOM screening and structural tests, the honest answer is:
**no candidate clearly justifies a Phase 2 calculation.**

However, the question is whether the BEST candidate (Candidate A:
axial chemical potential baryogenesis) has enough residual interest
to warrant a single focused calculation.

---

## The Best Candidate: Candidate A (Axial mu_5 Baryogenesis)

### What it has going for it

1. The OOM estimate gives eta_B ~ 10^{-9} for maximal initial
   chirality -- within an order of magnitude of the observed value.

2. The mechanism is physically transparent: torsion creates an
   effective axial chemical potential that biases sphaleron
   transitions.

3. The (J^5)^2 interaction IS the unique non-standard term from
   spin-torsion gravity. If it has any observational consequence,
   this is the most natural place to look.

### What kills it

1. **n_5 is a free parameter.** The initial axial charge density at
   the bounce is unconstrained. Setting n_5 = n_5^max is an extreme
   assumption with no justification.

2. **Torsion contributes ~1% of the total effect.** At T ~ M_Pl,
   gravitational scattering provides ~100 channels of comparable
   strength. The torsion-specific contribution is sub-dominant.

3. **(J^5)^2 conserves B and L.** Torsion cannot GENERATE the
   asymmetry. It can only modify the rate of processes that already
   violate B or L (sphalerons).

4. **Sphalerons are already in equilibrium at T ~ M_Pl.** Adding
   more scattering does not increase the asymmetry beyond the
   equilibrium value.

### What a Phase 2 calculation would look like

**Calculation:** Solve the coupled Boltzmann equations for n_B, n_L,
n_5 through the bounce, including:
- Sphaleron rate Gamma_sph(T)
- Torsion four-fermion rate Gamma_{(J5)^2}(T)
- Chirality-flipping rates from Yukawa interactions
- Time-dependent H(t) from the bounce background

**Input:** Initial n_5 (free), SM parameters (CKM, Yukawa, alpha_W).

**Output:** eta_B as a function of n_5(initial) and gamma.

**Quick kill:** If eta_B is independent of gamma (the Barbero-Immirzi
parameter), the mechanism is not torsion-specific and the calculation
is worthless.

**Problem:** This calculation has been done in related contexts
(torsion baryogenesis, e.g., Alexander, Peskin, Sheikh-Jabbari 2006;
de Cesare, Mavromatos, Sarkar 2015). The results confirm that:
- eta_B propto n_5 (linear in the free parameter)
- The Barbero-Immirzi parameter enters through the denominator
  (1 - 3gamma^2 kappa xi^2) but this is O(1) for any gamma
- The prediction is not falsifiable because n_5 absorbs any value

---

## Why I Recommend AGAINST a Phase 2

1. **The literature already contains this calculation.** Torsion
   baryogenesis via mu_5 has been studied by multiple groups. The
   result is always: eta_B ~ G n_5, with n_5 unconstrained. Our
   specific bounce model changes the H(t) during the Planck epoch
   but not the parametric dependence.

2. **No clean kill is possible.** The mechanism cannot be killed by
   calculation because it has a free parameter (n_5) that absorbs
   any desired eta_B. A Phase 2 would confirm what we already know:
   the mechanism works for suitable n_5 and fails to predict eta_B.

3. **No falsifiable prediction emerges.** The Barbero-Immirzi
   parameter gamma enters at O(1) level and does not produce a
   sharp constraint.

4. **The torsion contribution is sub-dominant** to generic
   gravitational effects at T ~ M_Pl. Even if we compute it
   precisely, it is ~1% of the total baryogenesis from
   gravitational-strength interactions.

---

## What WOULD Change This Assessment

A Phase 2 becomes justified if ANY of the following is shown:

1. **A mechanism to SET n_5 from the bounce dynamics.** If the
   bounce itself generates a specific n_5 (e.g., from the chiral
   anomaly or from the bounce dynamics), then eta_B becomes a
   prediction. But R-tilde R = 0 on FRW (Branch H result), so the
   gravitational chiral anomaly does not generate n_5 at the bounce.

2. **A torsion interaction that violates B or L.** If the effective
   action contained a B- or L-violating operator (beyond (J^5)^2),
   torsion could generate the asymmetry directly. In minimal EC,
   no such operator exists.

3. **A mechanism that operates BELOW T ~ M_Pl** where torsion
   dominates over gravitational scattering. This would require
   propagating torsion with mass m_T << M_Pl (PGT), but the
   mass-coupling lock ensures g_eff ~ m_T/M_Pl^2, making the
   interaction WEAKER than gravity at all scales.

**None of these loopholes appear viable given the established
barriers.**

---

## Recommendation

**Do not proceed to Phase 2.** The best candidate (axial mu_5
baryogenesis) is:
- Not predictive (n_5 free)
- Not torsion-dominant (~1% of gravitational effect)
- Already studied in the literature
- Not cleanly killable (free parameter absorbs any result)

A Phase 2 calculation would consume a session and produce a result
that confirms what OOM analysis and existing literature already
establish.

---

## If Forced to Choose

If a Phase 2 is required despite the above, the single most useful
calculation would be:

**Compute the ratio of torsion-specific to gravitational-generic
baryogenesis rates at T ~ M_Pl, as a function of gamma.**

This would establish definitively whether torsion is a 1% correction
(as estimated) or whether there is a gamma-dependent enhancement.
The (1 - 3gamma^2 kappa xi^2) denominator COULD diverge for
gamma^2 kappa xi^2 -> 1/3, but this corresponds to the BOUNCE
CONDITION (rho -> rho_crit), so it is self-consistently regulated.

Expected result: the ratio is O(1/g_*) ~ 1/100 for all gamma, with
no divergence. Quick calculation, clean negative result.

Time estimate: 1-2 hours.
Publishable: No (confirms existing literature).
