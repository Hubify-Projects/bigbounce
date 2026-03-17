# Branch V: Best Single Target

**Created:** 2026-03-17
**Decision:** V2a — Matter Bounce through ECH

---

## THE TARGET

**Compute the primordial perturbation spectrum (scalar + tensor) for a dust-dominated contraction that terminates at an ECH torsion bounce.**

This is the single most impactful calculation the program can perform, for the following reasons:

---

## Why V2a (Matter Bounce + ECH) Is the Best Target

### 1. It produces parameter-free predictions

The matter bounce f_NL prediction is:

```
f_NL^local = 5/12 ≈ 1.25
```

This number has zero free parameters. It follows from the structure of the curvature perturbation in a pressureless contracting universe:

```
ζ = ζ_linear + (5/12) ζ²_linear
```

The coefficient 5/12 is purely kinematic — it depends only on w = 0 during contraction. The ECH bounce doesn't modify it (at leading order) because the bounce happens after the mode has already frozen out.

**This is the sharpest prediction the program can make.** SPHEREx (launch ~2025, data ~2027) will measure f_NL^local with σ ≈ 0.5, making this a 2.5σ detection or a definitive exclusion.

### 2. It connects to an existing anomaly

Planck observed a low-ℓ deficit in the TT power spectrum at 2–3σ significance. In a matter bounce scenario:

- The contracting phase has a finite duration T_contract
- Modes with physical wavelength λ > c_s × T_contract were never inside the Hubble radius
- These modes are absent from the primordial spectrum → IR cutoff
- If T_contract ~ 10⁶⁰ t_Pl, the cutoff falls at ℓ ~ 2–10, matching the observed deficit

This is not a prediction — it is a postdiction requiring one parameter (T_contract). But it transforms the Planck anomaly from "statistical fluke" to "evidence for finite contracting phase."

### 3. The key technical challenge (n_s ≠ 1) is itself the main result

The pure matter bounce gives n_s = 1 (scale-invariant), which is 8σ from the observed n_s = 0.965. To save the model, we need a mechanism that produces a red tilt Δn_s ≈ -0.035.

There are three known possibilities:
1. **Finite bounce duration**: The ECH bounce has duration Δt ~ t_Pl. Modes that are not deeply super-Hubble during the bounce get modified. This produces a scale-dependent correction δn_s(k) ∝ (k/k_b)² — but this is far too small at CMB scales.

2. **Dust-to-radiation transition**: Before the bounce, the contracting universe must transition from dust to radiation (otherwise the bounce occurs in dust, not radiation). During this transition, modes near the Hubble radius get a tilt correction. The magnitude depends on the transition profile.

3. **Running from entropic perturbation**: If a second field (such as the birefringence ALP) participates in the contraction, entropic-to-curvature conversion at the transition can produce a red tilt. This has been shown to work by Cai, Quintin, and Wilson-Ewing (2015).

**The calculation of which mechanism produces n_s = 0.965 — and what parameter values are required — is THE key result.** If it works naturally, we have a complete alternative to inflation. If it requires fine-tuning, we quantify the cost and compare to inflation's own tuning costs.

### 4. ECH adds genuine value

Standard matter bounce literature uses one of:
- A scalar field with non-standard kinetic term (Lee-Wick model)
- A quantum gravity bounce (LQC with holonomy corrections)
- A "generic" non-singular bounce (no specific mechanism)
- A ghost condensate (problematic ghost issues)

ECH provides:
- **Explicit bounce mechanism** from standard physics (torsion of fermion condensate)
- **Known critical density** ρ_crit ≈ 0.21 M_Pl⁴ (not a free parameter)
- **Known bounce duration** Δt ~ t_Pl (sets the scale for perturbation corrections)
- **Parity structure**: (J⁵)² is parity-even, constraining which corrections arise
- **Connection to ALP birefringence**: The same framework that motivates the spectator ALP also provides the bounce mechanism

No existing paper has combined "explicit ECH bounce" with "matter contraction perturbation spectrum." This calculation is original.

### 5. The calculation is tractable

The background cosmology is:
- **Contraction phase** (t < -t_transition): a(t) ∝ t²/³ (dust), H = 2/(3t)
- **Transition phase** (-t_transition < t < -t_bounce): smooth interpolation from w = 0 to w = 1/3
- **Bounce phase** (|t| < t_bounce): a(t) = a_b(1 + 4α²t²)^{1/4}, known analytically
- **Expansion phase** (t > t_bounce): standard hot Big Bang

The perturbation equations are:
```
v'' + (c_s² k² - z''/z) v = 0    (Mukhanov-Sasaki for scalars)
u'' + (k² - a''/a) u = 0          (tensor modes)
```

where z = a√(ρ+p)/c_s H (depends only on background).

This is a standard ODE system. The Branch H tensor solver (already built as a Jupyter notebook at `branch_H_bounce_only/tensor_spectrum/03_tensor_mode_solver.ipynb`) provides the template. We extend it to:
1. Include the dust contraction phase
2. Solve the scalar Mukhanov-Sasaki equation
3. Extract P_ζ(k), n_s, r, n_T from numerical solutions
4. Compute the bispectrum at tree level

---

## What This Calculation Will Produce

### Tier 1 outputs (essential)
1. **P_ζ(k)**: Scalar power spectrum across CMB scales (k = 10⁻⁴ to 1 Mpc⁻¹)
2. **n_s(k)**: Spectral index and running, including bounce corrections
3. **P_T(k)**: Tensor power spectrum
4. **r**: Tensor-to-scalar ratio
5. **n_T**: Tensor spectral index

### Tier 2 outputs (high value)
6. **f_NL^local**: Non-Gaussianity from matter bounce, including ECH corrections
7. **Low-ℓ cutoff**: Prediction for ℓ_min as function of T_contraction
8. **Consistency relation**: r(n_T) compared to inflation prediction r = -8n_T

### Tier 3 outputs (bonus)
9. **Comparison with LQC**: Same calculation in loop quantum cosmology (for benchmarking)
10. **Parameter space scan**: (T_contraction, t_transition, EOS profile) → (n_s, r, f_NL) mapping
11. **Forecast**: Fisher matrix for CMB-S4/LiteBIRD/SPHEREx sensitivity

---

## The n_s Problem: How to Solve It

The n_s = 1 prediction is the matter bounce's Achilles' heel. Here is the systematic approach:

### Step 1: Compute n_s from the ECH bounce itself
Calculate the finite-duration correction from the ECH bounce with known Δt ~ t_Pl. This will give δn_s ∝ (k/k_b)² which is too small, but it establishes the baseline.

### Step 2: Compute n_s from dust → radiation transition
The transition from w = 0 to w = 1/3 before the bounce modifies modes near the Hubble radius at the transition time. For a smooth transition with duration Δt_trans, compute the spectral tilt correction.

### Step 3: Check whether the birefringence ALP contributes
If the ALP (already in the model) participates in the contraction dynamics, its mass m_a ~ 10⁻³¹ eV creates a slight deviation from w = 0, producing:
```
n_s - 1 ≈ -2m_a² / (3H²_transition)
```
For m_a ~ H_0, this is negligible at the bounce scale. But for a heavier ALP with m_a ~ H_transition, this could work. The ALP mass becomes a prediction, not a free parameter.

### Step 4: Curvaton mechanism
If the ALP acts as a curvaton (subdominant during contraction, dominant contribution to perturbations at late times), the spectral tilt is:
```
n_s - 1 = -2ε_contraction
```
where ε = -Ḣ/H² is the slow-roll parameter of the contracting phase. For dust, ε = 3/2, giving n_s = 1 - 3 = -2, which is too red. But for a mixture of dust + ALP with tuned ratio, n_s ~ 0.965 may be achievable.

### Step 5: Identify the minimal mechanism
After Steps 1–4, identify which mechanism (if any) produces n_s = 0.965 with the fewest new parameters. If none works without fine-tuning, this is a NEGATIVE RESULT worth publishing.

---

## Success / Failure Criteria

### SUCCESS (Grade A)
n_s = 0.965 ± 0.01 emerges from a mechanism with ≤ 1 free parameter AND f_NL = 5/12 is preserved. The model provides a complete, testable alternative to inflation with specific predictions for LiteBIRD, CMB-S4, and SPHEREx.

### PARTIAL SUCCESS (Grade B)
n_s can be tuned to 0.965 with 2–3 parameters OR n_s is slightly off but f_NL remains parameter-free. The model makes enough predictions to be publishable and testable.

### INSTRUCTIVE FAILURE (Grade C)
n_s = 1 cannot be modified to match observations without ruining f_NL or adding > 3 new parameters. This is a publishable negative result: "ECH matter bounce requires additional mechanism for spectral tilt" — still narrows the theoretical landscape.

### FATAL FAILURE (Grade F)
The ECH bounce disrupts the standard matter bounce predictions (e.g., introduces new instabilities, makes f_NL diverge, breaks gauge invariance of perturbations). This would kill the program.

---

## Timeline Estimate

| Phase | Task | Deliverable |
|-------|------|-------------|
| Phase 1a | Background cosmology: code up a(t) for dust → transition → ECH → radiation | Background solver notebook |
| Phase 1b | Scalar Mukhanov-Sasaki equation: numerical solution through bounce | P_ζ(k), n_s |
| Phase 1c | Tensor mode equation: extend existing solver to dust background | P_T(k), r, n_T |
| Phase 1d | Consistency relation and comparison to inflation | r(n_T) plot |
| Phase 2a | n_s correction mechanisms: Steps 1–5 above | δn_s analysis |
| Phase 2b | Non-Gaussianity: tree-level bispectrum | f_NL value |
| Phase 2c | Low-ℓ cutoff prediction | ℓ_min(T_contraction) |
| Phase 3 | Parameter space mapping and forecasts | Publication-ready results |

**This is the program. Start with Phase 1a.**
