# Phase 5: Primordial Power Spectrum Prediction

**Date:** 2026-03-13
**Status:** PREDICTION PLAN — expected features characterized, not computed

---

## 1. Target Observable

The curvature power spectrum:

```
P_R(k) = k³/(2π²) × |v_k/z|²     (evaluated when k ≪ aH)
```

across the full range:

```
k ∈ [10⁻⁴, 10¹⁶] Mpc⁻¹
```

spanning:
- CMB scales: k ~ 10⁻⁴ to 10⁻¹ Mpc⁻¹ (ℓ ~ 2 to 2500)
- LSS scales: k ~ 10⁻¹ to 10⁰ Mpc⁻¹
- μ-distortion scales: k ~ 10⁰ to 10⁴ Mpc⁻¹
- PBH scales: k ~ 10⁴ to 10¹⁶ Mpc⁻¹
- Bounce-feature scale: k ~ 10¹⁴ to 10¹⁵ Mpc⁻¹

---

## 2. Expected Spectrum Shape

### 2a. Decomposition

The spectrum can be decomposed as:

```
P_R(k) = P_R^{slow-roll}(k) × T_bounce(k)
```

where:
- P_R^{slow-roll}(k) = A_s (k/k_*)^{n_s − 1} is the standard inflationary contribution
- T_bounce(k) is the bounce transfer function encoding all modifications

### 2b. Expected Features of T_bounce(k)

Based on standard LQC results (Agullo et al. 2012-2013, Zhu et al. 2017) and the additional spin-torsion modifications:

**Region 1: CMB scales (k ≪ k_bounce)**
```
T_bounce(k) ≈ 1    (unmodified)
```
CMB-scale modes exited the Hubble radius ~55-60 e-folds before the end of inflation. They were never affected by the bounce (they were already frozen when the bounce happened, 92 e-folds before the end). The spectrum is standard slow-roll.

**Region 2: Intermediate scales (k ~ 10⁸ to 10¹² Mpc⁻¹)**
```
T_bounce(k) ≈ 1 + small corrections
```
These modes exited during the first ~30 pre-observable e-folds. They may carry faint imprints of the bounce-to-inflation transition but not the bounce itself.

**Region 3: Bounce-affected scales (k ~ 10¹² to 10¹⁶ Mpc⁻¹)**
```
T_bounce(k) = complex, model-dependent
```
Features expected:
- **IR suppression:** Power at k slightly below k_bounce is suppressed relative to scale-invariant (modes that were super-Hubble during the bounce)
- **Oscillatory modulation:** At k ~ k_bounce, interference between growing and decaying modes produces oscillations in P_R(k) with period Δ(ln k) ~ π/k_bounce
- **Possible bump/enhancement:** If the spin condensate c_s transition is sharp, it can create an enhancement at a specific k (similar to a particle-production spike)
- **Asymmetry:** If the contraction and expansion phases have different w_eff (due to hysteresis in the spin condensate), the oscillation pattern is asymmetric

**Region 4: Deep UV (k ≫ k_bounce)**
```
T_bounce(k) → 1    (unmodified)
```
These modes were deep inside the Hubble radius during the bounce and were not excited. Standard vacuum fluctuations.

### 2c. Schematic Spectrum

```
ln P_R(k)
  ^
  |  ≈ 2.1 × 10⁻⁹
  |──────────────────────────────────────────── scale-invariant
  |                                    ╱╲╱╲
  |                                   ╱    ╲
  |                              ────╱      ╲──── possible bump
  |                             ╱              ╲
  |                            ╱                ╲
  |────────────────────────────                  ────────
  |
  └──────────────────────────────────────────────────── ln k
   10⁻⁴        10⁴         10¹⁰        10¹⁴    10¹⁶
   CMB         LSS          μ-dist      bounce   UV
```

---

## 3. Spin-Torsion Modifications vs Standard LQC

### 3a. What's the Same

- The bounce mechanism (ρ → ρ_c) is identical in structure
- The basic feature scale k_bounce is set by N_tot (same in both)
- IR suppression and UV recovery are generic to all bounce models

### 3b. What's Different

| Feature | Standard LQC | Spin-Torsion LQC |
|---------|-------------|-------------------|
| w_eff at bounce | w_bare (radiation or inflaton-dominated) | w_bare + Δw_spin (modified by four-fermion interaction) |
| Sound speed c_s | 1 (scalar field) or 1/√3 (radiation) | Variable — depends on spin condensate V_s(n) |
| z''/z peak shape | Determined by a(τ) from standard Friedmann | Modified peak — height, width, asymmetry changed |
| Phase transition | None | Possible tanh transition in V_s(n) at n = n_★ |
| Oscillation period | Fixed by k_bounce | Same k_bounce but modified amplitude and phase |
| Tensor chirality | None (parity-preserving) | Nonzero Δχ(k) from parity-odd operator |

### 3c. Key Question

**Does the spin condensate create a bump in P_R(k) above the PBH threshold?**

For PBH formation: need P_R(k) ≳ 10⁻² at some k.
Standard LQC: oscillations around P_R ~ 10⁻⁹, amplitude ~O(1) modulation → no PBH production.
Spin-torsion: if the phase transition in c_s is sharp enough, it could amplify modes by factor ~10⁷ → P_R ~ 10⁻² → PBHs possible.

This is the central question. It depends on:
1. The steepness parameter α in V_s(n)
2. The energy scale Δρ of the condensate
3. The coupling ξ_s

All of which are currently unknown.

---

## 4. Parity-Odd Signatures in the Power Spectrum

### 4a. Scalar Sector (First Order)

No parity-odd modification to P_R(k) at first order. The parity-odd operator is a pseudo-scalar and does not couple to scalar perturbations at linear order.

### 4b. Tensor Sector (First Order)

```
P_T^L(k) ≠ P_T^R(k)
```

Chirality parameter:
```
Δχ(k) = [P_T^R(k) − P_T^L(k)] / [P_T^R(k) + P_T^L(k)]
```

Expected profile: Δχ(k) peaks at k ~ k_bounce where Φ'(τ) is largest, and decays for k ≪ k_bounce and k ≫ k_bounce.

### 4c. Scalar Sector (Second Order)

Chiral tensor perturbations source scalar perturbations at second order:
```
δP_R(k) ~ r² × Δχ² × P_R^(1)(k) ~ 10⁻⁴ × P_R^(1)(k)
```

This is a ~10⁻¹³ correction — detectable only by PIXIE-class spectral distortion experiments.

---

## 5. Parametric Study Plan

### 5a. Spin Condensate Parameters

Scan over the phenomenological condensate model {Δρ, α, n_★, ξ_s, m}:

| Parameter | Scan Range | Physical Meaning |
|-----------|-----------|------------------|
| Δρ / ρ_c | [10⁻⁶, 10⁻¹] | Energy scale of condensate relative to bounce |
| α × n_★ | [1, 100] | Steepness of phase transition |
| ξ_s | [0, 10] | Coupling to density gradients |
| m / M_Pl | [10⁻⁶, 1] | Fermion mass parameter |

### 5b. Inflaton Potential

Test three benchmark potentials:
1. **Starobinsky R²:** V(φ) = (3M²/4)(1 − e^{−√(2/3)φ/M_Pl})²
2. **Quadratic:** V(φ) = (1/2)m²φ²
3. **Plateau:** V(φ) = V₀(1 − e^{−φ/μ})

### 5c. Vacuum State

Three choices (see Phase 3):
1. Bunch-Davies
2. 4th-order adiabatic
3. No-boundary (symmetric at bounce)

### Total parameter space:
```
5 condensate params × 3 potentials × 3 vacuum choices = 45 model combinations
Per combination: ~1000 grid points for condensate scan
Total: ~45,000 solver evaluations
```

---

## 6. Output Products

### 6a. P_R(k) Library

```
For each model combination:
  - k array: 5200 points from 10⁻⁴ to 10¹⁶ Mpc⁻¹
  - P_R(k) array: dimensionless power spectrum
  - T_bounce(k) = P_R(k) / P_R^{slow-roll}(k)
  - P_T^L(k), P_T^R(k): tensor spectra
  - Δχ(k): chirality parameter
```

### 6b. Feature Characterization

For each P_R(k), extract:
```
- k_feature: location of maximum departure from scale-invariance
- A_feature: amplitude of the feature (P_R_max / P_R_ref)
- Δ_feature: width (FWHM in ln k)
- N_oscillations: number of oscillation cycles
- PBH_viable: boolean (does P_R exceed 10⁻² anywhere?)
```

### 6c. Transfer Function Fits

Fit the fast template:
```
ln T_s(k) = B_s × exp[−ln²(k/k_b)/(2σ_k²)] × [1 + α_k tanh(ln(k/k_b)/Δ_k)]
```

to each computed P_R(k). This provides the fast template parameters {B_s, k_b, σ_k, α_k} as functions of the microphysical parameters {Δρ, α, n_★, ξ_s, m, V(φ), vacuum}.

---

## 7. Comparison with Chain 1A Results

Chain 1A (already completed) used a phenomenological Gaussian bump:
```
P_R(k) = A_cmb(k/k_*)^{n_s−1} + A_b exp[−ln²(k/k_b)/(2s_k²)]
```

and found viable PBH parameter space for:
- A_b ~ 10⁻¹·⁷ to 10⁻⁰·⁹ (for s_k = 0.3)
- All mass scales from 10¹⁶ to 10⁴⁰ g are viable with appropriate A_b

**Phase 5 will determine whether the first-principles calculation lands in this viable window.**

The key comparison:
```
Does the computed T_bounce(k_bounce) correspond to B_s in the viable range?
```

If yes → the framework predicts PBHs from first principles.
If no → the framework does NOT predict PBHs (the bounce feature is too weak).

This is the hard yes/no that the entire research program is designed to answer.
