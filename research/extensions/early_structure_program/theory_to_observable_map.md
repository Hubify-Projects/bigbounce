# Theory-to-Observable Map: Early Structure from Bounce Cosmology

**Date:** 2026-03-13
**Program:** Early Structure Phenomenology

---

## LAYER A — Framework Quantities

### A1. Bounce energy scale
- **Definition:** ρ_crit = (√3 / 32π²γ³) ρ_Pl ≈ 0.27 ρ_Pl ≈ 1.4 × 10^{93} g/cm³
- **Status:** DERIVED from LQG with γ = 0.274
- **Pathway to observable:** Sets the energy scale at which the modified Friedmann equation activates. Perturbations evolving through the bounce feel this modification. The bounce energy scale determines the comoving scale k_bounce at which P(k) features would be imprinted: k_bounce ~ a_bounce × H_bounce ~ a_bounce × √(8πGρ_crit/3).
- **Key issue:** The comoving scale k_bounce depends on a_bounce (the scale factor at the bounce), which is set by the pre-bounce contraction history. This is model-dependent.

### A2. Modified Friedmann equation
- **Definition:** H² = (8πG/3)ρ[1 − ρ/ρ_crit]
- **Status:** DERIVED (standard LQC result)
- **Pathway to observable:** Modifies the background dynamics through which perturbation modes evolve. The [1 − ρ/ρ_crit] factor creates a smooth bounce (H → 0 at ρ → ρ_crit). Perturbation modes that are inside the Hubble radius during the bounce-to-inflation transition feel this modification.
- **What's known from LQC literature:**
  - Agullo, Ashtekar, Nelson (2012-2013): Perturbations through LQC bounce produce oscillations in P(k) at large scales, suppression of IR power, possible enhancement at intermediate scales depending on initial state
  - Wilson-Ewing (2013): Matter bounce scenarios can produce scale-invariant P(k) directly from the bounce
  - Zhu, Cleaver, Ashtekar (2017): Pre-inflationary dynamics leave imprints on the primordial spectrum at scales that exited the horizon during the bounce-to-inflation transition
- **What's NOT known:** How the spin-torsion modification (four-fermion + parity-odd) changes these results.

### A3. Four-fermion contact interaction
- **Definition:** L_int = −(3πG/2) × [γ²/(γ²+1)] × J^μ_A J_{Aμ}
- **Status:** DERIVED (standard EC result, Hehl 1976)
- **Pathway to observable:** At Planck densities during the bounce, this interaction is O(1) in strength and could modify the equation of state. The equation of state at the bounce affects perturbation evolution (the collapse threshold δ_c for PBH formation depends on w). At all lower densities, this interaction is negligible.
- **Honest assessment:** The four-fermion interaction modifies the pressure at Planck densities, potentially altering the bounce dynamics and hence the perturbation spectrum. But the effect on P(k) has not been calculated.

### A4. Parity-odd operator
- **Definition:** S_eff = (α/M) ∫ e_I ∧ e_J ∧ F^{IJ}[K, R̊], with α/M ≈ 10^{-21} GeV^{-1}
- **Status:** FRAMEWORK-MOTIVATED SCALING ANSATZ (one-loop existence established; exact value scheme-dependent)
- **Pathway to observable:** During inflation (when torsion sources are still significant, i.e., in the first few e-folds after the bounce), this operator breaks the left-right symmetry of tensor perturbations. Chiral tensor perturbations at second order can source scalar perturbations via the gravitational wave → scalar induced perturbation mechanism. This is a 2nd-order effect and has NOT been calculated.
- **Honest assessment:** Three levels of speculation: (1) chiral tensor production from parity-odd operator (plausible but uncalculated), (2) scalar induction at 2nd order (standard mechanism but amplitude unknown), (3) resulting P(k) modification sufficient for early structure effects (extremely uncertain).

### A5. Inflationary dilution parameters
- **Definition:** D_inf = exp(−3N_tot) × (T_reh/M_GUT)^{3/2}, with N_tot ≈ 92 (fitted)
- **Status:** FITTED (N_tot adjusted to match ρ_Λ)
- **Pathway to observable:** N_tot determines how many e-folds of inflation erase pre-inflationary perturbation features. With N_tot ≈ 92 and N_obs ≈ 55-60, there are ~30 "pre-observable" e-folds. Perturbation features from the bounce-to-inflation transition would be pushed to comoving scales k ~ k_CMB × e^{30} ≈ 10^{13} × k_CMB, corresponding to mass scales M ~ 10^{-13} M_☉ (sub-planetary). This is in the PBH constraint window but FAR below SMBH seed scales.
- **Critical implication:** Standard slow-roll with N_tot = 92 pushes bounce features to extremely small scales. For bounce features to affect SMBH-relevant scales (M ~ 10^3-10^6 M_☉, corresponding to k ~ 10^6 × k_CMB), one would need N_tot ≈ 70, which is inconsistent with the dark energy constraint.

---

## LAYER B — Phenomenological Bridge Parameters

### B1. P(k) bump amplitude: A_bump
- **Physical meaning:** Fractional enhancement of scalar power above the standard nearly scale-invariant A_s × (k/k_*)^{n_s−1} at a specific scale
- **Theory status:** PHENOMENOLOGICAL PROXY. Not derived from the bounce. Parameterizes the unknown result of the perturbation calculation.
- **Data constraints:** CMB constrains P(k) at k ~ 0.002-0.2 Mpc^{-1}. Small-scale enhancement is unconstrained by CMB but constrained by PBH non-detection, CMB spectral distortions (μ and y parameters), and ultracompact minihalo searches.
- **Viable range:** A_bump / A_s ∈ [1, 10^7] — must be < 10^7 to avoid PBH overproduction

### B2. P(k) bump scale: k_bump
- **Physical meaning:** Comoving wavenumber at which the bounce-induced feature peaks
- **Theory status:** PHENOMENOLOGICAL PROXY. Set by a_bounce × H_bounce and the number of pre-observable e-folds.
- **Data constraints:** Different k_bump values correspond to different PBH mass scales: M_PBH ≈ (k_bump / 10^6 Mpc^{-1})^{-2} M_☉. SMBH seeds need k_bump ~ 10^5-10^6 Mpc^{-1} (corresponding to ~10^3-10^6 M_☉).
- **Honest issue:** k_bump is determined by the number of pre-observable e-folds. N_tot = 92 pushes k_bump to ~10^{13} Mpc^{-1}, far above SMBH-relevant scales.

### B3. Seed mass: log₁₀(M_seed / M_☉)
- **Physical meaning:** Characteristic mass of the seed BHs that eventually grow into SMBHs
- **Theory status:** PURELY PHENOMENOLOGICAL in our framework. Standard astrophysics distinguishes light seeds (~100 M_☉, Pop III remnants), medium seeds (~10^3 M_☉, runaway stellar mergers), and heavy seeds (~10^4-10^5 M_☉, direct collapse BHs).
- **Data constraints:** JWST observations of z > 6 quasars constrain minimum seed masses through growth time arguments.

### B4. Seed formation redshift: z_seed
- **Physical meaning:** Redshift at which seeds form
- **Theory status:** PURELY PHENOMENOLOGICAL
- **Data constraints:** Must be z_seed > z_obs of the observed SMBH. For z_obs ~ 10, need z_seed ≳ 15-20.

### B5. Growth efficiency: ε_growth
- **Physical meaning:** Time-averaged accretion rate as fraction of Eddington: Ṁ/Ṁ_Edd
- **Theory status:** STANDARD ASTROPHYSICS. Typically 0.5-1.0 for Eddington-limited growth, can exceed 1 for super-Eddington accretion.
- **Data constraints:** Constrained by luminosity functions and BH mass estimates.

### B6. PBH abundance fraction: f_PBH
- **Physical meaning:** Fraction of dark matter in PBHs: f_PBH ≡ Ω_PBH / Ω_DM
- **Theory status:** NOT PREDICTED by framework. Would be derived from P(k) if the perturbation calculation existed.
- **Data constraints:** Stringent upper limits across 30+ orders of magnitude in mass (see PBHbounds).

---

## LAYER C — Observables

### C1. High-z quasar/AGN abundance
- **What is measured:** Number density of luminous quasars / AGN at z > 6
- **Parameters constrained:** M_seed × ε_growth × t_growth → minimum seed mass
- **Likelihood feasibility:** YES — forward model comparison with published quasar luminosity functions. Not a full likelihood (too few objects for statistical inference on seed parameters), but minimum-seed-mass consistency checks are standard.

### C2. SMBH mass estimates at high z
- **What is measured:** Individual BH mass estimates from broad-line widths, SED fitting, or dynamical arguments
- **Parameters constrained:** M_BH(z_obs) → minimum M_seed for given z_seed and ε_growth
- **Likelihood feasibility:** INDIVIDUAL OBJECTS only. Not a population likelihood. Growth-time arguments are robust.

### C3. PBH constraint bands
- **What is measured:** Upper limits on f_PBH(M) from microlensing, CMB accretion, GW merger rates, Hawking evaporation, dynamical effects
- **Parameters constrained:** f_PBH(M) → A_bump(k_bump) via Press-Schechter collapse
- **Likelihood feasibility:** YES — constraint overlay on P(k) bump parameter space. PBHbounds provides machine-readable constraint curves.

### C4. CMB spectral distortions (μ and y)
- **What is measured:** Departures from blackbody in CMB frequency spectrum (FIRAS/PIXIE)
- **Parameters constrained:** Integrated P(k) enhancement at 1 < k < 10^4 Mpc^{-1}
- **Likelihood feasibility:** YES — Gaussian constraint from FIRAS: μ < 9 × 10^{-5}. Constrains P(k) enhancement at intermediate scales.

### C5. Minimum growth time consistency
- **What is measured:** t(z_obs) − t(z_seed) vs. Salpeter time × ln(M_obs/M_seed)
- **Parameters constrained:** Model-independent minimum seed mass
- **Likelihood feasibility:** YES — simple consistency check. Standard in the literature.

---

## Summary: The Honest Picture

The theory-to-observable map has **one critical missing link**: the primordial perturbation spectrum through the bounce. Everything else is standard astrophysics.

```
FRAMEWORK                    BRIDGE (MISSING)              OBSERVABLES
──────────                   ──────────────               ────────────
Modified Friedmann  ─────┐
                         ├──→ P(k) features ──→ SMBH seed abundance
Four-fermion at          │    (NOT CALCULATED)    PBH constraints
Planck densities ────────┤                        CMB distortions
                         │
Parity-odd tensor ───────┘
asymmetry (2nd order)
```

The program is: **parameterize the unknown P(k) feature, compute its observable consequences, and identify the target the actual bounce calculation would need to hit.**
