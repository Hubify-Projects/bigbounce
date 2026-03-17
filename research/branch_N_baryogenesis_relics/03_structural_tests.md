# Branch N: Structural Tests

**Date:** 2026-03-16

---

## Test N1 -- Torsion-Essential Test

**Question:** Is torsion or spin density actually essential to the
mechanism, or would ANY bounce (or any high-temperature epoch)
produce the same effect?

**Procedure:**
1. Write down the mechanism.
2. Remove all torsion-specific terms ((J^5)^2, mu_5^eff, G_torsion).
3. Replace the bounce with a generic radiation bounce at the same
   energy scale (same H_b, same t_bounce, same T_bounce).
4. Does the mechanism still work? If yes: FAIL_NOT_TORSION_SPECIFIC.

**Subtlety:** Some mechanisms use torsion as an ENHANCEMENT of a
pre-existing effect (e.g., torsion modifies sphaleron rates). These
pass N1 only if the enhancement is quantitatively significant
(>10% change in the observable) AND depends on torsion parameters
(gamma, rho_crit) in a way that constrains them.

### Application to Candidates

| Candidate | Remove torsion | Same result? | Verdict |
|-----------|---------------|-------------|---------|
| A: Axial mu_5 | mu_5 -> 0 | No mu_5, but standard baryogenesis still works via CKM | **MARGINAL** -- torsion adds mu_5 but CP still needs external source |
| B: Modified decay | delta_M -> 0 | Standard leptogenesis unchanged | **FAIL** -- mass hierarchy survives without torsion, works better |
| C: Grav. DM | Any bounce a(t) | Same |beta_k|^2 to leading order | **FAIL** -- generic gravitational production |
| D: Axion relic | Any H(t) | Same (axion frozen for 10^{56} e-folds after bounce) | **FAIL** -- bounce irrelevant to axion |
| E: Leptogenesis | Remove (J^5)^2 | Standard leptogenesis unchanged; torsion conserves B,L anyway | **FAIL** -- torsion adds B,L-conserving channel |
| F: PBH window | Any bounce T(k) | Same T(k) shape for any symmetric bounce | **FAIL** -- generic (Branch K result) |
| G: Sterile relics | Remove cross-term | Standard gravitational scattering thermalizes at same T | **FAIL** -- gravitational thermalization dominates |

**Result: 6 FAIL, 1 MARGINAL. Only Candidate A has even marginal
torsion-specificity, and even that is conditional on mu_5 being
quantitatively significant.**

---

## Test N2 -- Event-Strength Test

**Question:** Is the bounce interaction strong enough to affect the
target abundance or asymmetry?

**Procedure:**
1. Compute the relevant interaction rate Gamma at the bounce.
2. Compare to H at the bounce.
3. Compute the integrated effect over the bounce duration.
4. Compare to the target observable.

**Key scales:**
- ECH: H_b ~ M_Pl, t_bounce ~ t_Pl
- PGT: H_b ~ m_T, t_bounce ~ 1/m_T
- Target eta_B ~ 6 x 10^{-10}
- Target Omega_DM h^2 ~ 0.12

### Application to Candidates

| Candidate | Gamma/H at bounce | Integrated effect | Target | Sufficient? |
|-----------|------------------|-------------------|--------|------------|
| A: Axial mu_5 | mu_5/T ~ G*n_5/T ~ 1 (at T~M_Pl) | mu_5 * t_bounce ~ 1 | eta_B ~ 10^{-10} | Possibly (see OOM in File 05) |
| B: Modified decay | delta_M/M_N >> 1 | Erases M_N | eta_B ~ 10^{-10} | **NO** -- destroys mechanism |
| C: Grav. DM | |beta|^2 ~ O(1) for m < H_b | n_chi ~ H_b^3 | Omega_DM ~ m/M_Pl | YES but generic |
| D: Axion relic | None (bounce irrelevant) | 0 | Omega_a | **NO** |
| E: Leptogenesis | Gamma_4f ~ H at T~M_Pl | ~1 scattering per t_Pl | eta_B ~ 10^{-10} | YES in rate, but conserves B,L |
| F: PBH window | T(k_b) ~ O(1) | Planck-mass PBHs | surviving PBHs | **NO** -- evaporate |
| G: Sterile relics | Gamma_cross ~ H at T~M_Pl | Full thermalization | Delta N_eff ~ 0.03 | YES but generic |

---

## Test N3 -- Generic-Collapse Test

**Question:** Does the mechanism reduce to a well-known standard
mechanism (standard gravitational production, standard leptogenesis,
standard freeze-out) once the calculation is done carefully?

**Procedure:**
1. Write the full calculation.
2. Take the limit where torsion-specific corrections are small.
3. Identify the leading contribution.
4. Is the leading contribution a known standard result?

### Application to Candidates

| Candidate | Reduces to? | Standard mechanism | Verdict |
|-----------|------------|-------------------|---------|
| A: Axial mu_5 | Standard baryogenesis + O(G n_5 / T) correction | Baryogenesis with torsion as perturbative correction | **MARGINAL** -- correction is O(1) at bounce but O(10^{-34}) at EW scale |
| B: Modified decay | Standard leptogenesis in Planck-temperature limit | All fermions degenerate at M_Pl | **FAIL_GENERIC** |
| C: Grav. DM | Standard gravitational production | Parker (1968), Zeldovich-Starobinsky (1971) | **FAIL_GENERIC** |
| D: Axion relic | Standard misalignment | Preskill-Wise-Wilczek (1983) | **FAIL_GENERIC** |
| E: Leptogenesis | Standard leptogenesis + B,L-conserving correction | Additional scattering channel | **FAIL_GENERIC** |
| F: PBH window | Standard PBH formation + instant evaporation | Hawking (1975) | **FAIL_GENERIC** |
| G: Sterile relics | Standard gravitational thermalization | Graviton thermalization at T ~ M_Pl | **FAIL_GENERIC** |

---

## Test N4 -- Predictive-Yield Test

**Question:** Does the mechanism predict or meaningfully narrow
a relic yield or asymmetry, or does it have enough free parameters
to accommodate any value?

**Procedure:**
1. Count free parameters of the mechanism.
2. Count observables it predicts.
3. If parameters >= observables: FAIL_NO_PREDICTIVE_YIELD (tunable
   storytelling).
4. If the prediction depends on unknown initial conditions (e.g.,
   pre-bounce n_5): CONDITIONAL -- need to assess whether initial
   conditions are constrained.

### Application to Candidates

| Candidate | Free parameters | Observables | Predictive? |
|-----------|----------------|------------|------------|
| A: Axial mu_5 | n_5(initial), gamma, SM CP phases | eta_B | **NO** -- n_5(initial) is unconstrained |
| B: Modified decay | (killed by N2) | -- | -- |
| C: Grav. DM | m_chi, xi_R (non-minimal coupling) | Omega_DM | **NO** -- m_chi free |
| D: Axion relic | (killed by N2) | -- | -- |
| E: Leptogenesis | (killed by N1, N3) | -- | -- |
| F: PBH window | (killed by N2) | -- | -- |
| G: Sterile relics | Number of sterile species | Delta N_eff | **YES** -- but prediction is same as gravitational (killed by N1) |

---

## Test N5 -- Observability/Constraint Test

**Question:** Can the predicted relic/asymmetry be confronted by
data or produce a meaningful bound on model parameters?

**Procedure:**
1. Compute the predicted observable value.
2. Compare to current experimental sensitivity.
3. Does a detection or non-detection constrain model parameters?

### Application to Candidates

| Candidate | Predicted value | Current data | Constraining? |
|-----------|----------------|-------------|--------------|
| A: Axial mu_5 | eta_B depends on n_5(initial) | eta_B = 6.1 x 10^{-10} (BBN) | **NO** -- free parameter absorbs any value |
| C: Grav. DM | Omega_DM depends on m_chi | Omega_DM h^2 = 0.12 | **NO** -- constrains m_chi, not torsion |
| G: Sterile relics | Delta N_eff ~ 0.03/species | CMB-S4 sensitivity ~0.03 | **MARGINAL** -- but indistinguishable from graviton |

---

## Aggregate Scorecard

| Candidate | N1 | N2 | N3 | N4 | N5 | Overall |
|-----------|----|----|----|----|----|----|
| A: Axial mu_5 | MARGINAL | Possibly | MARGINAL | FAIL | NO | **FAIL_NO_PREDICTIVE_YIELD** |
| B: Modified decay | FAIL | NO | FAIL | -- | -- | **FAIL_GENERIC** |
| C: Grav. DM | FAIL | YES | FAIL | FAIL | NO | **FAIL_GENERIC** |
| D: Axion relic | FAIL | NO | FAIL | -- | -- | **FAIL_TOO_WEAK** |
| E: Leptogenesis | FAIL | YES(rate) | FAIL | -- | -- | **FAIL_NOT_TORSION_SPECIFIC** |
| F: PBH window | FAIL | NO | FAIL | -- | -- | **FAIL_TOO_WEAK** |
| G: Sterile relics | FAIL | YES | FAIL | YES | MARGINAL | **FAIL_NOT_TORSION_SPECIFIC** |

**No candidate achieves SURVIVES_PHASE1.**

The best performer is Candidate A (axial chemical potential
baryogenesis), which fails only on N4 (no predictive yield due to
unconstrained initial n_5) but is marginal on N1 and N3. However,
the combination of marginal torsion-specificity + no predictive
yield + O(1) sensitivity only at T ~ M_Pl makes this a weak
candidate at best.

---

## Structural Observation

The common failure mode across ALL candidates is the combination of:

1. **(J^5)^2 conserves B and L.** Torsion cannot generate asymmetry
   by itself.

2. **Generic gravitational effects dominate at T ~ M_Pl.** Any
   gravitational-strength interaction produces the same effects as
   torsion at Planck temperatures.

3. **No initial condition anchor.** The bounce does not specify
   pre-bounce conditions (n_5, particle content, field values).

These three facts constitute a structural barrier for baryogenesis
and relic production from the spin-torsion bounce, analogous to the
barriers identified in previous branches.
