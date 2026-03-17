# Scale Mismatch Derivation

**Date:** 2026-03-13
**Purpose:** Rigorous derivation of the scale mismatch between framework-predicted P(k) feature location and SMBH/PBH-relevant scales

---

## 1. Framework P(k) Feature Scale

### Setup

The bounce-to-inflation transition occurs at the beginning of inflation. Perturbation modes affected by the bounce dynamics are those that were inside the Hubble radius during the transition. These modes exit the horizon during the first few e-folds of inflation.

The CMB pivot scale k_pivot = 0.05 Mpc⁻¹ exited the horizon N_pivot ≈ 55 e-folds before the end of inflation (standard slow-roll result, weakly dependent on reheating temperature).

### Derivation

A mode that exits the horizon at N e-folds before the end of inflation has comoving wavenumber:

k(N) = k_pivot × exp(N − N_pivot)

Bounce-affected modes exit during the first ~1-5 e-folds of inflation. The earliest such mode exits at N ≈ N_tot. With N_tot = 92 (fitted to the dark energy constraint ρ_Λ ≈ (2.3 meV)⁴):

**k_bounce = k_pivot × exp(N_tot − N_pivot)**
**k_bounce = 0.05 × exp(92 − 55)**
**k_bounce = 0.05 × exp(37)**
**k_bounce = 0.05 × 1.17 × 10¹⁶**
**k_bounce = 5.86 × 10¹⁴ Mpc⁻¹**

### Sensitivity to N_pivot

| N_pivot | k_bounce (Mpc⁻¹) |
|---------|-------------------|
| 50 | 3.38 × 10¹⁶ |
| 55 | 5.86 × 10¹⁴ |
| 60 | 1.02 × 10¹³ |

The uncertainty in N_pivot spans ~2 orders of magnitude in k_bounce. This does not change the qualitative conclusion.

---

## 2. SMBH Seed Scales

### PBH mass from comoving wavenumber

The horizon mass at re-entry during radiation domination:

M_PBH / M_☉ ≈ 33 × (k / 10⁶ Mpc⁻¹)⁻²

This is the standard result from Carr et al. (2020), assuming γ = 0.2 (fraction of horizon mass that collapses) and g_* = 10.75.

### SMBH seed mass requirements

JWST observations of massive black holes at z > 6-10 require seed masses:

| Seed type | M_seed (M_☉) | Required k (Mpc⁻¹) |
|-----------|--------------|---------------------|
| Light seed (Pop III remnant) | ~10²  | 5.7 × 10⁵ |
| Medium seed (stellar merger) | ~10³  | 1.8 × 10⁵ |
| Heavy seed (DCBH) | ~10⁴  | 5.7 × 10⁴ |
| Very heavy seed | ~10⁵  | 1.8 × 10⁴ |

**SMBH-relevant scales: k ~ 2 × 10⁴ to 6 × 10⁵ Mpc⁻¹**

---

## 3. Scale Mismatch

### In wavenumber:

k_bounce / k_SMBH ≈ 5.86 × 10¹⁴ / (2 × 10⁴ to 6 × 10⁵)

**Mismatch: 10⁹·⁰ to 10¹⁰·⁵ in comoving wavenumber**

### In mass:

M_bounce = 33 × (5.86 × 10¹⁴ / 10⁶)⁻² = 33 / (3.43 × 10¹⁷) ≈ 10⁻¹⁶·⁰ M_☉

**Mismatch: 10¹⁸ to 10²¹ in mass scale**

The bounce feature corresponds to M ~ 10⁻¹⁶ M_☉ ≈ 2 × 10¹⁷ g — sub-asteroid mass, in the weakly constrained PBH dark matter window.

### What N_tot would be needed?

For the bounce feature to appear at SMBH-relevant scales:

k_target = k_pivot × exp(N_target − N_pivot)

For k_target = 10⁵ Mpc⁻¹ (middle of SMBH range):
N_target − N_pivot = ln(10⁵ / 0.05) = ln(2 × 10⁶) = 14.5
N_target = 55 + 14.5 = 69.5

**Required N_tot ≈ 70 for SMBH-relevant features.**

The framework requires N_tot = 92 from the dark energy constraint. The mismatch:

ΔN = 92 − 70 = 22 e-folds

This corresponds to a scale ratio of exp(22) ≈ 3.6 × 10⁹ — exactly the ~10¹⁰ mismatch computed above.

---

## 4. Other Relevant Scales

### μ-distortion sensitivity (FIRAS)

FIRAS constrains spectral distortions from energy injection at:
- k_μ ~ 1 to 10⁴ Mpc⁻¹ (modes dissipating at 5 × 10⁴ < z < 2 × 10⁶)

This is BELOW the SMBH seed scales and far below k_bounce. A P(k) feature at k_bounce would be invisible to FIRAS.

### Asteroid-mass PBH window

The bounce feature at M ~ 10⁻¹⁶ M_☉ falls in the mass range:
- M ~ 10⁻¹⁶ to 10⁻¹³ M_☉: the "asteroid-mass window" where PBH constraints are weakest
- f_PBH ≲ 1 is permitted (PBHs could constitute all dark matter)

This is potentially interesting for PBH dark matter — but irrelevant for SMBH seeds.

---

## 5. Summary

| Question | Answer |
|----------|--------|
| Does the framework naturally place P(k) features at SMBH-relevant scales? | **NO** |
| By how much is it off? | **~10¹⁰ in wavenumber, ~10²⁰ in mass** |
| What N_tot is needed for SMBH-relevant features? | **N_tot ≈ 70** |
| Is N_tot = 70 consistent with the dark energy constraint? | **NO — requires N_tot = 92** |
| Could broader-than-expected features bridge the gap? | **No — 22 e-folds of mismatch cannot be bridged by any reasonable feature width** |
| Are the framework-predicted scales interesting for anything? | **Possibly for PBH dark matter (asteroid-mass window), but NOT for SMBH seeds** |

### The Mismatch Is Devastating

The scale mismatch is not a factor of 10 that might be resolved by theoretical uncertainties. It is a factor of 10¹⁰ in wavenumber (10²⁰ in mass). No plausible broadening of the P(k) feature, no reasonable uncertainty in N_pivot, and no modification of the bounce dynamics can bridge this gap while maintaining the dark energy constraint.

**The only way to get P(k) features at SMBH-relevant scales is to abandon the N_tot = 92 dark energy constraint.** This would break the paper's central result.
