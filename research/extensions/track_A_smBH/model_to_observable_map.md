# Track A -- Early SMBH Seed Abundance: Model-to-Observable Map

**Date**: 2026-03-12
**Status**: FUTURE WORK ONLY
**Verdict**: The spin-torsion bounce framework has no direct, calculable mechanism for producing or modifying SMBH seeds. Any Track A analysis would be standard astrophysics with, at best, a marginal parameterization inherited from the bounce cosmology. This document explains why, in detail.

---

## 1. Honest Assessment of Framework--SMBH Connections

### 1.1 What the framework actually says

The spin-torsion bounce cosmology modifies physics in two regimes:

1. **At Planck densities** (rho ~ 0.27 rho_Pl ~ 10^{93} g/cm^3): The modified Friedmann equation H^2 = (8piG/3) rho [1 - rho/rho_crit] causes a bounce instead of a singularity. This is the core prediction.

2. **At all sub-Planckian densities**: The [1 - rho/rho_crit] factor is unity to extraordinary precision. Standard GR is recovered exactly. The four-fermion contact interaction L_int = -(3piG/2) [gamma^2/(gamma^2+1)] J^mu_A J_{A,mu} has coupling strength ~ G ~ 10^{-38} GeV^{-2}, which is negligible at any astrophysical density.

### 1.2 Where SMBH seeds form

SMBH seeds form at densities rho ~ 10^{-10} to 10^{10} g/cm^3 (depending on the formation channel: direct collapse, Pop III remnants, runaway mergers in dense clusters). This is **at least 83 orders of magnitude** below the bounce density:

    rho_seed / rho_crit ~ 10^{-83} to 10^{-103}

The torsion correction to the Friedmann equation at these densities is:

    [1 - rho/rho_crit] = 1 - O(10^{-83})

This is not a small effect that might matter at the margins. It is zero for all practical purposes.

### 1.3 The four-fermion interaction at astrophysical densities

The torsion-induced four-fermion coupling strength relative to electromagnetic interactions:

    G_torsion / G_Fermi ~ (M_W / M_Pl)^2 ~ 10^{-34}

At the densities relevant to SMBH seed formation (even in the most extreme direct-collapse scenarios), torsion effects on the gas dynamics, cooling, fragmentation, and accretion are suppressed by factors of order (rho/rho_Pl)^2. This ratio is identically negligible.

### 1.4 The "baby universe" connection is a non-sequitur

The framework proposes that our universe was born inside a rotating black hole. This is a statement about cosmogenesis -- it says nothing about SMBHs forming *within* our universe. Black holes in our universe do not spawn visible baby universes that affect our observables. The causal structure explicitly prevents this.

---

## 2. Candidate Connections: Evaluated One by One

### 2.1 Modified primordial perturbation spectrum

**Claim**: The bounce might alter the primordial power spectrum in ways that affect early structure formation and hence SMBH seed abundance.

**Evaluation**:
- The paper fits standard LCDM cosmological parameters {omega_b, omega_c, theta_s, tau, n_s, ln(10^10 A_s)} plus extensions {Delta_N_eff, Omega_k, (omega/H)_0, (alpha/M)_0}.
- The scalar spectral index n_s is fitted from data with a standard prior [0.92, 1.00]. The paper does NOT derive a modified primordial spectrum from the bounce.
- N_tot ~ 92 e-folds is stated as fitted, not predicted.
- **No prediction exists** for scale-dependent features, enhanced small-scale power, or any modification to P(k) that would preferentially produce early seeds.

**Status**: NOT A PREDICTION. The framework does not modify P(k) relative to standard inflation in any calculated way.

### 2.2 Delta_N_eff and early expansion rate

**Claim**: Extra relativistic species from the bounce (Delta_N_eff) could change the expansion rate during the epoch of seed formation, altering the available time for growth.

**Evaluation**:
- MCMC result: Delta_N_eff = 0.24 +/- 0.18 (consistent with zero at ~1.3 sigma).
- Even taking the central value, Delta_N_eff ~ 0.24 changes H(z) by ~1% during radiation domination.
- SMBH seeds need to grow by factors of 10^3 to 10^6 between z ~ 20 and z ~ 6. A 1% change in H(z) changes the available growth time by ~1%.
- This is a **standard cosmological effect** that any model with nonzero Delta_N_eff would produce. It is not specific to spin-torsion cosmology.
- More importantly: Delta_N_eff is a phenomenological parameter in this framework. It is not derived from the bounce dynamics. Any model that adds Delta_N_eff = 0.24 gives the same effect.

**Status**: GENERIC EFFECT, NOT FRAMEWORK-SPECIFIC. Could be parameterized, but there is nothing to distinguish this from any other Delta_N_eff model.

### 2.3 Positive spatial curvature (Omega_k > 0)

**Claim**: The bounce geometry imprints small positive curvature Omega_k ~ +0.001, which could affect structure formation.

**Evaluation**:
- Omega_k = 0.0010 +/- 0.0018, consistent with flat at 0.6 sigma.
- Positive curvature at this level has negligible effect on structure formation at z ~ 10-20.
- The growth factor D(a) changes by < 0.1% relative to flat LCDM.

**Status**: NEGLIGIBLE EFFECT.

### 2.4 Cosmic rotation and angular momentum of proto-galactic halos

**Claim**: Background vorticity could bias angular momentum acquisition of collapsing halos, potentially affecting whether direct-collapse black holes can form (since DCBH formation requires low angular momentum).

**Evaluation**:
- The paper constrains (omega/H)_0 < 2.1 x 10^{-11} (95% CL).
- The rotation contribution to any dynamical quantity scales as (omega/H)^2 < 10^{-21}.
- The tidal torque on a proto-galactic halo from cosmic rotation is smaller than the random tidal field by a factor of at least 10^{-10}.
- **There is no physically meaningful effect on DCBH formation from cosmic rotation at this level.**

**Status**: NEGLIGIBLE EFFECT.

### 2.5 Parity-odd operator and SMBH accretion physics

**Claim**: The parity-odd term S_eff = integral d^4x sqrt(-g) (alpha/M) epsilon^{abcd} K_{ab} R_{cd} might affect accretion disk physics or jet formation near SMBHs.

**Evaluation**:
- alpha/M ~ 10^{-21} GeV^{-1} = 10^{-21} / (1.22 x 10^{19} GeV) M_Pl^{-1} ~ 10^{-40} M_Pl^{-1}.
- This operator is a correction to gravitational dynamics. Near a 10^6 M_sun SMBH, curvature R ~ GM/r^3 ~ 10^{-20} cm^{-2} at the ISCO.
- The ratio of the parity-odd correction to standard curvature is ~ (alpha/M) * K ~ 10^{-40} in natural units.
- **Completely unobservable.**

**Status**: NEGLIGIBLE EFFECT.

---

## 3. What Would An Honest Analysis Look Like?

If one were forced to write a Track A analysis, the only legitimate approach would be:

### 3.1 Standard SMBH seed formation models with modified background cosmology

One could run standard semi-analytic SMBH seed formation models (e.g., Lodato & Natarajan 2006; Volonteri 2010; Inayoshi, Visbal & Haiman 2020) with the slightly modified background cosmology from the spin-torsion fits:

- H_0 = 69.2 +/- 0.8 km/s/Mpc (vs 67.36 in LCDM)
- sigma_8 = 0.785 +/- 0.016 (vs 0.811 in LCDM)
- Delta_N_eff = 0.24 +/- 0.18

The effect of these shifts on SMBH seed abundance would be:

1. **Higher H_0**: Earlier structure formation (slightly), more seeds at fixed redshift. Effect: ~5-10% change in seed number density at z > 10.
2. **Lower sigma_8**: Later structure formation, fewer seeds. Effect: ~10-20% change at z > 10. This partially cancels the H_0 effect.
3. **Delta_N_eff ~ 0.24**: Faster expansion during radiation era, earlier matter-radiation equality by ~2%. Marginal effect on seed formation, which occurs well after equality.

**Net effect**: O(10%) change in predicted SMBH seed abundance, entirely from standard cosmological parameter shifts. Nothing specific to spin-torsion physics.

### 3.2 Why this is not worth an MCMC

- The O(10%) effect is **smaller than the theoretical uncertainty** in any SMBH seed formation model (which spans orders of magnitude depending on assumed physics: Pop III IMF, Lyman-Werner background, metal enrichment, dynamical friction timescales).
- The effect is **degenerate with astrophysical parameters**: changing the critical Lyman-Werner flux J_crit by a factor of 2 has a larger effect than any cosmological modification from our framework.
- Current JWST data on high-z quasars (Bogdan et al. 2024, Maiolino et al. 2024, Larson et al. 2023) constrain the SMBH mass function at z > 6 to perhaps a factor of 3. The framework predicts modifications at the ~10% level. **The signal is buried in the noise.**

---

## 4. Public Data Inventory

For completeness, here is what exists if someone wanted to pursue this despite the above:

### 4.1 High-z quasar/AGN catalogs
- **JWST JADES**: ~10 AGN candidates at z > 4 (Maiolino et al. 2024)
- **JWST CEERS**: Little Red Dots catalog, some with BH mass estimates (Kocevski et al. 2024)
- **JWST UNCOVERed**: BH mass estimates at z ~ 4-7 (Furtak et al. 2024; Bogdan et al. 2024 for UHZ1 at z=10.1)
- **Pre-JWST compilations**: Inayoshi, Visbal & Haiman (2020) Table 1; Volonteri et al. (2021)
- **SDSS high-z quasars**: ~300 quasars at z > 5.7 (Fan et al. 2023 compilation)

### 4.2 Theoretical seed formation models
- Lodato & Natarajan (2006): Direct collapse model
- Volonteri (2010): Comprehensive seed formation review
- Inayoshi, Visbal & Haiman (2020): Modern review with JWST forecasts
- Latif & Ferrara (2016): Direct collapse BH formation

### 4.3 What would be needed for a likelihood
A legitimate likelihood L(data | theta_cosmo, theta_astro) would require:
- A forward model mapping cosmological parameters to halo mass function at z > 10
- A seed formation prescription (DCBH, Pop III, runaway) with its own ~5-10 astrophysical parameters
- A growth/accretion model with Eddington ratio distribution, duty cycle, mergers
- Selection function modeling for each survey
- **The cosmological parameters from our framework modify only the first step, and only at the ~10% level**

---

## 5. Classification Table

| Connection | Type | Magnitude | Framework-specific? | Calculable? |
|---|---|---|---|---|
| Modified Friedmann at seed densities | Derived | 10^{-83} | Yes | Yes, but zero |
| Four-fermion at seed densities | Derived | 10^{-34} x G_Fermi | Yes | Yes, but zero |
| Delta_N_eff effect on H(z) | Phenomenological fit | ~1% on H(z) | No (generic) | Yes |
| H_0 shift effect on halo formation | Phenomenological fit | ~5-10% on n_seed | No (generic) | Yes |
| sigma_8 shift effect on growth | Phenomenological fit | ~10-20% on n_seed | No (generic) | Yes |
| Cosmic rotation on halo angular momentum | Upper bound only | < 10^{-10} of tidal | Yes | Yes, but zero |
| Parity-odd operator near SMBHs | Derived | 10^{-40} relative | Yes | Yes, but zero |
| Primordial spectrum modifications | Not calculated | Unknown | Potentially | No |

---

## 6. Recommendation

### FUTURE WORK ONLY

**Rationale**:

1. **No framework-specific mechanism exists** for early SMBH seed formation in spin-torsion bounce cosmology. The equations are explicit: all torsion/bounce effects vanish at astrophysical densities.

2. **The only non-trivial effects** are shifts in standard cosmological parameters (H_0, sigma_8, Delta_N_eff), which are:
   - Not specific to this framework (any model with these parameter values gives the same result)
   - Smaller than current observational uncertainties by an order of magnitude
   - Smaller than theoretical modeling uncertainties by one to two orders of magnitude

3. **An MCMC would be misleading**: It would appear to constrain spin-torsion parameters using SMBH data, but in reality it would only constrain standard cosmological parameters through an unnecessarily indirect route. The "spin-torsion" label would be cosmetic.

4. **No legitimate likelihood can be constructed** that would tell us anything about the bounce, torsion, parity violation, or cosmic rotation from SMBH seed abundances. The physics simply does not connect.

### What would change this assessment?

- A **calculated modification to P(k)** from the bounce (e.g., enhanced small-scale power from trans-Planckian effects) that is specific to this framework and not a free parameter.
- A **new theoretical mechanism** connecting EC torsion to seed formation at sub-Planckian densities (none currently exists in the literature).
- **Observational evidence** for anomalous SMBH abundances at z > 15 that cannot be explained by any standard astrophysical model, motivating exotic cosmological explanations.

### Comparison with other tracks

This track is significantly weaker than:
- **Track B (PBH)**: Where the modified power spectrum could, in principle, be connected to PBH formation if a bounce-specific P(k) calculation existed.
- **Track C (Parity CMB)**: Where the framework makes direct, calculable predictions (C_l^{EB}) that are testable.

---

## 7. Bottom Line

Writing a Track A paper would be dishonest unless it is framed as: "We compute SMBH seed abundances in a cosmology with slightly modified H_0 and sigma_8, motivated by but not specifically predicted by spin-torsion bounce cosmology." This is a legitimate but unexciting exercise in standard semi-analytic modeling. It does not test the bounce, does not test torsion, and does not test parity violation.

The spin-torsion framework's testable predictions lie elsewhere: CMB E-B correlations, galaxy spin asymmetries, and the specific value of alpha/M. SMBH seeds are not among them.
