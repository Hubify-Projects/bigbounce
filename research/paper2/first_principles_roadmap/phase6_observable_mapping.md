# Phase 6: Observable Mapping — P_R(k) → Measurable Quantities

**Date:** 2026-03-13
**Status:** EQUATIONS DEFINED — mapping from power spectrum to five observable channels

---

## 1. PBH Abundance

### 1a. Smoothed Variance

```
σ²(M) = ∫ d ln k  W²(kR)  [4(1+w_f)² / (5+3w_f)²]  (kR)⁴  T²(R,k)  P_R(k)
```

For radiation domination (w_f = 1/3):
```
σ²(M) = (16/81) ∫ d ln k  W²(kR)  (kR)⁴  P_R(k)
```

Window functions:
- Gaussian: W(x) = exp(−x²/2)
- Top-hat: W(x) = 3(sin x − x cos x)/x³

Smoothing scale R and horizon mass M:
```
R = 1/k_H(M)
M_H(k) = (3/2) M_{H,eq} (k_eq/k)² (g_{*,eq}/g_*)^{1/3}
```

with M_{H,eq} = 2.8 × 10¹⁷ M_☉, k_eq ≈ 0.01 Mpc⁻¹, g_{*,eq} = 3.36.

### 1b. Collapse Fraction

**Gaussian Press-Schechter:**
```
β(M) = (1/2) erfc(δ_c / (√2 σ(M)))
```

**Press-Schechter with critical collapse:**
```
β(M) ≈ (1/√(2π)) × (σ(M)/δ_c) × exp[−δ_c²/(2σ²(M))]
```

Critical collapse refinement:
```
M_PBH = K_c × M_H × (δ − δ_c)^{γ_c}
```

Benchmark values: δ_c = 0.45, K_c ∈ [3, 10], γ_c = 0.36

### 1c. Present-Day PBH Fraction

```
f_PBH = (1/Ω_CDM) ∫ d ln M  (M_eq/M)^{1/2}  β(M)
```

where Ω_CDM ≈ 0.265 and M_eq ≈ 5.57 × 10⁵⁰ g.

### 1d. PBH Mass Function

```
ψ(M) = (1/f_PBH) × (M_eq/M)^{1/2} × β(M) / Ω_CDM
```

normalized so that ∫ ψ(M) d ln M = 1.

### 1e. Constraint Test

For each observational bound i with monochromatic limit f_{i,max}^{mono}(M):

```
I_i(θ) = ∫ d ln M  f_PBH(θ) × ψ(M; θ) / f_{i,max}^{mono}(M)  ≤  1
```

Violation penalty:
```
−2 ln L_PBH = Σ_i [max(0, I_i − 1) / ε]²,    ε = 0.05
```

### 1f. Constraint Datasets

| Channel | Mass Range (g) | Source |
|---------|---------------|--------|
| Hawking evaporation (γ-ray) | 10¹⁴ – 10¹⁷ | Carr et al. (2020) |
| Femtolensing (GRB) | 10¹⁷ – 10²⁰ | Barnacka et al. (2012) |
| Neutron star capture | 10¹⁸ – 10²⁴ | Capela et al. (2013) |
| HSC microlensing | 10²² – 10²⁸ | Niikura et al. (2019) |
| EROS/MACHO microlensing | 10²⁶ – 10³⁴ | Tisserand et al. (2007) |
| CMB accretion | 10³³ – 10³⁸ | Ali-Haimoud & Kamionkowski (2017) |
| Dynamical (wide binaries, dwarfs) | 10³⁶ – 10⁴⁰ | Monroy-Rodriguez & Allen (2014) |

**Data source:** PBHbounds (GitHub: bradkav/PBHbounds, MIT license)

---

## 2. CMB μ-Distortion

### 2a. μ-Parameter

Spectral distortions of the CMB blackbody arise from energy injection at redshifts 5 × 10⁴ < z < 2 × 10⁶ (Sunyaev & Zeldovich 1970):

```
μ = 2.27 ∫_{k_min}^{k_max} d ln k  P_R(k)  W_μ(k)
```

where the μ-distortion window function:
```
W_μ(k) = exp(−[k/k_D(z_μ)]²) − exp(−[k/k_D(z_th)]²)
```

with:
- k_D(z_μ) ≈ 46 Mpc⁻¹ (dissipation scale at z_μ = 5 × 10⁴)
- k_D(z_th) ≈ 740 Mpc⁻¹ (dissipation scale at thermalization redshift z_th = 2 × 10⁶)

Effective range: k ~ 50 to 10⁴ Mpc⁻¹

### 2b. y-Distortion

For energy injection at z < 5 × 10⁴:

```
y = (1/4) ∫ d ln k  P_R(k)  W_y(k)
```

with W_y(k) peaking at k ~ 1 – 50 Mpc⁻¹.

### 2c. Observational Status

| Experiment | μ sensitivity | Status |
|-----------|--------------|--------|
| COBE/FIRAS | |μ| < 9 × 10⁻⁵ | Existing bound |
| PIXIE (proposed) | |μ| ~ 10⁻⁸ | Not funded |
| PRISTINE (proposed) | |μ| ~ 10⁻⁹ | Concept |

Standard slow-roll predicts μ ~ 2 × 10⁻⁸ (just at PIXIE sensitivity).

### 2d. Relevance to Spin-Torsion Bounce

The bounce feature at k ~ 10¹⁴ Mpc⁻¹ is FAR above the μ-distortion window (k ~ 50 – 10⁴ Mpc⁻¹). The bounce feature does NOT directly produce μ-distortions.

However:
- If there is a tail or pre-cursor oscillation at k ~ 10³ – 10⁴ Mpc⁻¹ (from the bounce-to-inflation transition), it could produce detectable μ-distortions.
- The intermediate e-fold range (30 pre-observable e-folds) corresponds to k ~ 10⁰ – 10⁸ Mpc⁻¹, partially overlapping the μ-window.

**Assessment:** μ-distortion signal from this framework is likely BELOW current bounds but possibly within reach of next-generation experiments. Requires full computation to quantify.

---

## 3. Small-Scale Structure

### 3a. Ultracompact Minihalos (UCMHs)

Enhanced P_R(k) at small scales produces ultracompact minihalos at early times:

```
δ_UCMH(z) = (D(z)/D(z_eq)) × σ(M, k)
```

UCMHs form when δ ≳ 10⁻³ (much below PBH threshold δ_c ~ 0.45).

Observable through:
- Gravitational lensing (astrometric microlensing)
- Dark matter annihilation signals (if WIMPs)
- Pulsar timing

### 3b. Induced Gravitational Waves

Enhanced scalar perturbations at second order produce a stochastic gravitational wave background:

```
Ω_GW(k) ∝ ∫ dk' P_R(k') P_R(|k − k'|) × (kernel)
```

For P_R ~ 10⁻² at k_bounce ~ 10¹⁴ Mpc⁻¹:
```
Frequency: f ~ k_bounce / (2π) × (a₀/a_entry) ~ 10⁻⁴ Hz (LISA band?)
Ω_GW ~ (P_R)² ~ 10⁻⁴
```

This is potentially detectable by LISA if the frequency falls in the right range.

**Frequency mapping:**
```
f = k/(2π) × c × (3.086 × 10²² m/Mpc)⁻¹
For k = 10¹⁴ Mpc⁻¹: f ~ 5 × 10⁵ Hz (far above LISA band)
For k = 10⁸ Mpc⁻¹: f ~ 5 × 10⁻¹ Hz (marginally in LISA band)
For k = 10⁴ Mpc⁻¹: f ~ 5 × 10⁻⁵ Hz (in LISA band)
```

The bounce feature at k ~ 10¹⁴ is at ~MHz frequencies — inaccessible. But oscillatory tails at lower k could produce signals at detectable frequencies.

---

## 4. Gravitational Wave Backgrounds (Primordial Tensor Spectrum)

### 4a. Tensor Power Spectrum

```
P_T(k) = P_T^L(k) + P_T^R(k)
```

Standard parameterization:
```
P_T(k) = r × A_s × (k/k_*)^{n_T}
```

with r < 0.036 (BICEP/Keck 2021).

### 4b. Chiral Contribution

From the parity-odd operator:
```
Δχ(k) = [P_T^R(k) − P_T^L(k)] / [P_T^R(k) + P_T^L(k)]
```

Observable through:
- **CMB TB:** C_ℓ^{TB} = sin(2β) C̃_ℓ^{TE} (if from birefringence)
- **CMB TB (tensors):** C_ℓ^{TB,tens} = 4π ∫ d ln k Δχ(k) P_T(k) Δ_ℓ^{T,T}(k) Δ_ℓ^{B,T}(k)
- **GW circular polarization:** Directly measurable by LISA (cross-correlation of TDI channels)

### 4c. Connection to Framework

The tensor chirality is sourced by the parity-odd condensate Φ'(τ) during the bounce. The peak chirality is at k ~ k_bounce ~ 10¹⁴ Mpc⁻¹ — completely inaccessible at CMB scales.

For CMB-observable scales (k ~ 10⁻² Mpc⁻¹), the parity-odd effect is through the RESIDUAL birefringence angle β, not through direct tensor chirality.

---

## 5. CMB Parity Signatures

### 5a. Birefringence Angle

From the parity-odd coupling to photons:
```
β = (g_γ/2) × [Φ(η₀) − Φ(η_dec)]
```

Under constant-β approximation:
```
C_ℓ^{EB} = (1/2) sin(4β) × (C̃_ℓ^{EE} − C̃_ℓ^{BB})
C_ℓ^{TB} = sin(2β) × C̃_ℓ^{TE}
```

### 5b. Current Measurements

| Experiment | β (degrees) | Significance |
|-----------|-------------|--------------|
| Planck PR4 | 0.30 ± 0.11 | 2.7σ |
| ACT DR6 | 0.215 ± 0.074 | 2.9σ |
| Combined (inverse-variance) | 0.24 ± 0.06 | 3.9σ |

### 5c. Framework Prediction

The framework predicts β ≠ 0 from the parity-odd operator. The photon-torsion vertex factor:
```
f_photon = β_obs / β_predicted ≈ 1.7 ± 0.4
```

is O(1), consistent with a one-loop estimate. This is a CONSISTENCY CHECK (Paper 1), not an independent constraint.

### 5d. What the Perturbation Calculation Adds

The full perturbation calculation through the bounce would:
1. Determine Φ(τ) from first principles
2. Predict β without the f_photon fudge factor
3. Predict the scale-dependent part of β (currently assumed constant)
4. Predict the tensor chirality Δχ(k) as a function of k

If β turns out to be SCALE-DEPENDENT, it would leave a distinctive imprint in the ℓ-dependence of C_ℓ^{EB} that is distinguishable from a constant rotation.

---

## 6. Summary: Observable Mapping Table

| Observable | Equation | k-Range | Current Bound | Framework Prediction |
|-----------|---------|---------|--------------|---------------------|
| f_PBH(M) | Press-Schechter + constraints | 10⁴ – 10¹⁶ Mpc⁻¹ | Multiple (PBHbounds) | UNKNOWN — requires P_R at bounce scale |
| μ-distortion | Silk damping integral | 50 – 10⁴ Mpc⁻¹ | μ < 9 × 10⁻⁵ (FIRAS) | Likely below current bound |
| UCMHs | Early structure | 10⁴ – 10¹⁴ Mpc⁻¹ | Weak bounds | UNKNOWN |
| Induced GWs | Second-order P_R² | k ~ k_feature | LIGO/LISA depending on f | Probably above detectable frequency |
| CMB birefringence β | Photon-torsion coupling | All CMB ℓ | 0.24° ± 0.06° | Consistent at O(1) |
| Tensor chirality Δχ | Parity-odd tensor modes | k ~ k_bounce | No measurement | Inaccessible at CMB scales |
| C_ℓ^{TB} anomaly | Tensor chirality + birefringence | ℓ ~ 50-200 | Noisy | Potentially detectable by LiteBIRD |

---

## 7. Which Observables Discriminate This Framework?

**Unique predictions (if perturbation calculation is done):**
1. PBH mass function peaked at M ~ 10⁻¹⁶ M_☉ (asteroid mass, if feature amplitude is large enough)
2. Oscillatory features in P_R(k) at k ~ 10¹⁴ Mpc⁻¹ (currently unmeasurable)
3. Correlated tensor chirality and scalar feature at the SAME k-scale

**Testable with current data:**
1. β ≈ 0.24° (already measured, consistent)
2. ΔN_eff (MCMC chains running, consistent with zero)
3. H₀, σ₈ (MCMC fits, partial tension relief)

**Testable with upcoming experiments:**
1. LiteBIRD: β with σ ~ 0.02° (will sharpen birefringence measurement 3×)
2. CMB-S4: B-mode polarization, tensor-to-scalar ratio
3. PIXIE/PRISTINE: μ-distortion at 10⁻⁸ level
4. LISA: GW background at mHz
