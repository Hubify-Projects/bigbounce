# Phase 2: Model-to-Observable Map (v2)

**Date:** 2026-03-13
**Status:** UPGRADED — formal likelihood structure with explicit epistemic classification

---

## 1. Parameter Definitions

### 1a. Inference Parameters

| Parameter | Symbol | Physical Meaning | Status | Prior |
|-----------|--------|-----------------|--------|-------|
| Birefringence angle | β | Rotation of CMB polarization plane | **Directly measured** | Uniform on [−1°, 1°] |
| Photon-torsion coupling | f_photon | Effective vertex factor coupling parity-odd sector to photons | **NOT derived** (the gap) | Log-uniform on [0.01, 100] |
| Cosmological integral | C₀ | Integrated pseudo-scalar field excursion (radians) | **NOT derived** — O(1) expected | Log-uniform on [0.1, 10] |

### 1b. Fixed Framework Parameters

| Parameter | Symbol | Value | Origin |
|-----------|--------|-------|--------|
| Parity-odd coefficient | (α/M)·M_Pl | 2.435 × 10⁻³ ≡ ε | One-loop estimate (phenomenological) |
| Planck mass | M_Pl | 2.435 × 10¹⁸ GeV | Fundamental constant |
| Operator scale | α/M | 10⁻²¹ GeV⁻¹ | Paper 1 fit |

---

## 2. Transformation Equations

### Chain: Framework → Observable

**Step 1: Parity-odd operator (DERIVED)**
```
S_eff = (α/M) ∫ e_I ∧ e_J ∧ F^{IJ}[K, R̊]
```
Status: Exists in the action. Well-defined.

**Step 2: Photon-torsion coupling (GAP)**
```
L ⊃ (g_eff/2) φ(τ) F_μν F̃^{μν}
g_eff = ε × f_photon = (α/M) × M_Pl × f_photon
```
Status: NOT derived. f_photon parameterizes the unknown vertex.

**Step 3: Birefringence angle (SCALING ANSATZ)**
```
β = g_eff × C₀ = ε × f_photon × C₀
```
where C₀ encodes the integrated field excursion from recombination to today.
Status: Standard axion-like coupling result (Carroll 1998). The functional form is secure; the coefficient (f_photon × C₀) is undetermined.

**Step 4: EB/TB spectra (DERIVED, given β)**
```
C_ℓ^{EB} = sin(4β)/2 × (C_ℓ^{EE} − C_ℓ^{BB}) ≈ 2β(C_ℓ^{EE} − C_ℓ^{BB})
C_ℓ^{TB} = sin(2β) × C_ℓ^{TE} ≈ 2β × C_ℓ^{TE}
```
Status: Exact for uniform rotation. No model dependence beyond β.

### Inverse Chain: Observable → Framework

```
β_obs → f_photon = β_obs / (ε × C₀)
```

For C₀ = 1: f_photon = β_rad / ε = β_rad / 2.435×10⁻³

---

## 3. Epistemic Classification (Explicit)

| Quantity | Classification | Can we improve it? |
|----------|---------------|-------------------|
| Operator S_eff exists | **Derived** | Already done |
| α/M ~ 10⁻²¹ GeV⁻¹ | **Phenomenological fit** | Constrained by dark energy scale |
| f_photon (photon-torsion vertex) | **Not derived** | Requires one-loop computation (Paper 2+) |
| C₀ (field excursion integral) | **Not derived** | Requires solving pseudo-scalar evolution (Paper 2+) |
| β from framework | **Not predictable** without f_photon × C₀ | Both unknown |
| C_ℓ^{EB} given β | **Derived** (standard CMB physics) | Exact |
| EB shape ∝ (EE − BB) | **Generic** to ANY uniform rotation | Not specific to this framework |

### What the upgrade adds:

The v1 analysis computed f_photon = β_obs/(ε × C₀) algebraically. The v2 analysis:

1. **Frames this as a proper Gaussian summary-likelihood inference** with explicit priors
2. **Computes Bayesian evidence** for β ≠ 0 (Savage-Dickey ratio)
3. **Maps the (f_photon, C₀) degeneracy** as a proper 2D posterior
4. **Tests the EB shape** against published bandpowers (goodness-of-fit)

### What the upgrade does NOT add:

- It does NOT derive f_photon from first principles
- It does NOT break the (f_photon, C₀) degeneracy
- It does NOT distinguish this framework from other birefringence sources
- It does NOT constitute a map-level CMB analysis
