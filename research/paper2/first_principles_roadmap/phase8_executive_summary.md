# Phase 8: Executive Summary — First-Principles PBH Research Plan

**Date:** 2026-03-13
**Status:** COMPLETE ROADMAP

---

## 1. What Is Already Derived in the Current Paper (v1.6.0)

### Background cosmology (COMPLETE):
- Modified Friedmann equation: H² = (8πG/3) ρ(1 − ρ/ρ_c) with ρ_c ≈ 0.27 ρ_Pl
- Dark energy from parity-odd operator: ρ_Λ = [(α/M)M_Pl] × D_inf × M_Pl⁴
- Inflationary dilution: D_inf = exp(−3N_tot) × (T_reh/M_GUT)^{3/2}
- N_tot = 92 e-folds (fitted to observed ρ_Λ)
- Bounce scale: k_bounce ~ 5.86 × 10¹⁴ Mpc⁻¹ → M_bounce ~ 10¹⁷ g ~ 10⁻¹⁶ M_☉

### Observational fits (COMPLETE):
- MCMC constraints on {H₀, σ₈, ΔN_eff} — consistent with data
- Cosmic birefringence consistency check: f_photon ≈ 1.7 ± 0.4 (O(1))

### Perturbation spectrum (NOT DONE):
- P_R(k) through the bounce has NOT been computed
- All PBH/SMBH claims are explicitly flagged as future work
- The paper makes no prediction about small-scale structure from the bounce

---

## 2. What Is Still Missing

### Irreducible theoretical unknowns:

| Unknown | What it determines | Can it be computed? |
|---------|-------------------|-------------------|
| Spin condensate V_s(n) at Planck density | Effective EOS w_eff through bounce → shape of z''/z → P_R(k) features | NO — requires non-perturbative Planck-scale QCD. Must be parameterized. |
| Perturbation prescription (dressed vs hybrid vs deformed algebra) | Effective mass U_s(τ) = z''/z | NO — genuine theoretical ambiguity. Must run separate model classes. |
| Vacuum state at the bounce | Initial conditions for mode evolution | NO — genuine ambiguity. Must compare BD, adiabatic, no-boundary. |
| Parity-odd condensate dynamics Φ(τ) | Tensor chirality Δχ(k) | PARTIALLY — order of magnitude from α/M, time dependence unknown. |
| Inflaton potential V(φ) | Bounce-to-inflation transition | ASSUMED — standard choices (Starobinsky R², quadratic, plateau). |

### Computable but not yet computed:

| Calculation | Input required | Output |
|------------|---------------|--------|
| Background trajectory a(τ) through bounce | V(φ), V_s(n) (parameterized) | a(τ), H(τ), ε₁(τ), c_s(τ) |
| z''/z pump function | a(τ) solution | U_s(τ) on conformal time grid |
| Mode evolution v_k(τ) | z''/z, initial conditions | v_k at late times for each k |
| P_R(k) extraction | v_k solutions | Full power spectrum |
| f_PBH(M) from P_R | P_R at small scales | PBH abundance prediction |
| μ-distortion from P_R | P_R at intermediate scales | Spectral distortion prediction |

---

## 3. Exact Steps Required

### Step 1: Build the background solver (Weeks 1-2)

Solve the coupled system:
```
H² = (κ/3) ρ_eff(1 − ρ_eff/ρ_c)
φ̈ + 3Hφ̇ + V'(φ) = 0
ṅ = −3Hn
ρ_eff = (1/2)φ̇² + V(φ) + V_s(n)
```

from deep contraction through bounce to slow-roll inflation.

**Validation:** Reproduce published LQC background solutions with V_s = 0.

### Step 2: Compute z''/z (Week 3)

From the background solution a(τ), compute:
```
z(τ) = a √(2ε₁) M_Pl / c_s
U_s(τ) = z''/z
```

using spectral differentiation (NOT finite differences).

**Validation:** Check z''/z reduces to 2/τ² in the de Sitter limit.

### Step 3: Evolve perturbation modes (Weeks 3-4)

For each k ∈ [10⁻⁴, 10¹⁶] Mpc⁻¹:
```
v_k'' + [c_s² k² − U_s(τ)] v_k = 0
```

with three initial condition choices (BD, adiabatic, no-boundary).

**Validation:** Reproduce published LQC P_R(k) spectra.

### Step 4: Extract P_R(k) and identify features (Week 5)

```
P_R(k) = k³/(2π²) |v_k/z|²
```

Characterize: bump location, amplitude, width, oscillation structure.

### Step 5: Grid scan over condensate parameters (Weeks 5-6)

Scan {Δρ, α, n_★, ξ_s, m} × 3 vacuum choices × 3 potentials.
~30,000 solver evaluations → ~5 days on 8-core CPU.

### Step 6: Map to observables (Week 7)

For each P_R(k):
- Compute f_PBH(M) via Press-Schechter
- Compute μ-distortion via Silk damping integral
- Compute induced GW background
- Test against PBHbounds constraint tables

### Step 7: Fit fast templates and run MCMC (Week 7-8)

Regress the grid of P_R(k) onto the fast template:
```
ln T_s(k) = B_s exp[−ln²(k/k_b)/(2σ_k²)] [1 + α_k tanh(ln(k/k_b)/Δ_k)]
```

Run MCMC chains with Cobaya using PBH + μ-distortion likelihoods.

### Step 8: Write Paper 2 (Weeks 9-10)

Report:
- P_R(k) predictions for all model/vacuum/potential combinations
- Which combinations produce PBHs (if any)
- Observable predictions
- Comparison between model classes
- Honest assessment of theoretical ambiguities

---

## 4. Estimated Time Scale

| Phase | Duration | Dependencies |
|-------|----------|-------------|
| Background solver | 2 weeks | None |
| z''/z + mode solver | 2 weeks | Background solver |
| Validation against LQC | 2 weeks | Mode solver (can overlap) |
| Grid scan | 1 week (compute) + 1 week (analysis) | Mode solver |
| Observable mapping + MCMC | 1 week | Grid scan |
| Paper writing | 2 weeks | All above |
| **Total** | **8-10 weeks** | |

**With buffer for debugging and iteration: 3-4 months.**

This is a MINIMAL timeline assuming:
- One person working full-time
- No major theoretical obstacles
- No need for collaborator input on perturbation prescriptions

**More realistic with collaboration and iteration: 6-9 months.**

The original perturbation sketch estimated 12-18 months. This is reduced because:
1. We will use fast templates for MCMC (not full solver in every step)
2. The grid scan is computationally cheap (~$60 on RunPod)
3. We separate the theoretical ambiguities (prescription, vacuum) into model classes rather than trying to derive a unique answer

---

## 5. Feasibility Assessment — Brutally Honest

### What is DEFINITELY feasible (weeks):
- Building the background solver
- Reproducing standard LQC results
- Grid scan over condensate parameters
- PBH abundance computation from any given P_R(k)
- Fast template + MCMC

### What is feasible but requires care (months):
- Accurate z''/z computation through the bounce (spectral differentiation)
- Mode evolution at the bounce scale k ~ 10¹⁴ Mpc⁻¹ (numerical precision)
- Validation against published LQC results (require careful comparison)
- Writing a rigorous paper with honest uncertainty quantification

### What CANNOT be resolved (theoretical ambiguity):
- The perturbation prescription (dressed vs hybrid vs deformed algebra)
- The vacuum state at the bounce
- The spin condensate at Planck densities

**These are not computational problems. They are open questions in quantum gravity.** Paper 2 should present results for multiple choices and identify observational discriminators, NOT claim to have computed "the" prediction.

### The central question:

**Does ANY combination of condensate parameters, vacuum state, and perturbation prescription produce P_R(k) large enough for PBH formation at the bounce scale?**

Chain 1A (phenomenological) shows the REQUIRED bump amplitude is A_b ~ 10⁻² to 10⁻¹.
Standard LQC produces oscillatory features with amplitude modulation of O(1) around the baseline P_R ~ 10⁻⁹.

**This means the bounce feature needs to AMPLIFY power by a factor of ~10⁷ at k ~ 10¹⁴ Mpc⁻¹.**

In standard LQC: this does NOT happen. The bounce produces O(1) modulation, not 10⁷× amplification.

For the spin-torsion variant: the four-fermion interaction could create a sharper transition (larger z''/z spike) and the sound speed feature could create parametric amplification. Whether this reaches 10⁷× depends entirely on the condensate model parameters.

**Likely outcome:** Most of the condensate parameter space will NOT produce PBHs. A narrow region with very sharp phase transitions (large α) MIGHT. The paper should map this boundary honestly.

### The honest conclusion:

The spin-torsion bounce framework currently has:
1. **A well-defined background cosmology** — tested against data
2. **A predictive perturbation equation** — standard Mukhanov-Sasaki with modified z''/z
3. **Irreducible theoretical ambiguities** — prescription, vacuum, condensate
4. **A feasible numerical program** — ~$60, ~1 week on RunPod
5. **No guarantee of PBH production** — requires 10⁷× amplification that may not occur

The research program is worth doing because:
- It converts a phenomenological framework into a computational one
- It produces a definitive answer (within model assumptions) about PBH viability
- Even a null result ("no PBH production") is a publishable outcome
- The tensor chirality prediction is an independent output regardless of PBH results
- The fast template + MCMC infrastructure is reusable for future refinements

---

## 6. File Index

| Phase | File | Content |
|-------|------|---------|
| 1 | `phase1_bounce_background_equations.md` | Complete background equation set with audit |
| 2 | `phase2_perturbation_equation_derivation.md` | Full perturbation ODE system with unknowns |
| 3 | `phase3_perturbation_initial_conditions.md` | Three vacuum state candidates with consequences |
| 4 | `phase4_perturbation_numerical_pipeline.md` | Solver algorithm, stiffness analysis, validation |
| 5 | `phase5_power_spectrum_prediction_plan.md` | Expected features, parametric study plan |
| 6 | `phase6_observable_mapping.md` | P_R(k) → PBH, μ-distortion, GW, CMB parity |
| 7 | `phase7_perturbation_compute_requirements.md` | Cost estimates, infrastructure assessment |
| 8 | `phase8_executive_summary.md` | This file |
