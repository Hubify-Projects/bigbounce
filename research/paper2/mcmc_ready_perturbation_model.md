# MCMC-Ready Perturbation Model for Paper 2

**Date:** 2026-03-13
**Status:** RESEARCH PROGRAM DEFINITION — replaces the naive perturbation sketch
**Source:** Houston's model specification (informed by recent LQC perturbation literature)

---

## Key Insight: Why the Naive Approach Fails

A unique first-principles z_ST(τ) cannot be derived from the framework alone because:

1. **Perturbation prescription ambiguity:** Different effective Mukhanov-Sasaki mass functions (dressed-like, hybrid-like, etc.) produce different bounce signatures. This is not a calculational difficulty — it is a genuine theoretical ambiguity.

2. **Vacuum state ambiguity:** Different adiabatic initial states change the amplification in the intermediate regime. The choice of initial conditions at the bounce is not determined by the theory.

**The correct approach:** Build an MCMC-ready effective model class whose parameters are tied to the bounce physics, and treat the ambiguities as separate model choices (separate chains + model comparison), NOT as nuisance parameters within a single chain.

---

## 1. Background Sector: Spin-Condensate Phase-Transition Model

### Modified Friedmann equation (from Paper 1)

H² = (κ/3) ρ_eff (1 − ρ_eff/ρ_c),    κ ≡ 8πG

### Spin-condensate closure

Evolve a conserved fermion-density proxy:

ṅ = −3Hn    (n ∝ a⁻³)

Define an effective condensate energy density V_s(n) via a tanh-smoothed transition:

V_s(n) = m·n · [1 − tanh(α(n − n_★))]/2
       + [m·n_★ + Δρ + ξ_s·κ·(n − n_★)²] · [1 + tanh(α(n − n_★))]/2

Then set:

ρ_eff = ρ_{P1} + V_s(n)
P_eff = P_{P1} + n·dV_s/dn − V_s(n)

This gives a thermodynamically closed effective fluid with:

w_eff = P_eff / ρ_eff
c_s² = (dP_eff/dn) / (dρ_eff/dn)

### Why this choice

- Directly inspired by fermionic-bounce/condensate literature (arXiv:1406.1456)
- The a⁻⁶ condensate term and tanh phase transition are standard in that literature
- Paper 1's bounce factor (1 − ρ/ρ_c) already creates the bounce; the condensate sector controls the SHAPE of the bounce-era pressure/sound-speed feature

### Raychaudhuri equation (needed at every MCMC sample)

Ḣ = −(κ/2)(ρ_eff + P_eff)(1 − 2ρ_eff/ρ_c)

(follows from differentiating the modified Friedmann equation + continuity)

### Background parameters

{Δρ, α, n_★, ξ_s, m}

---

## 2. Scalar Sector: Inference on U_s(τ) ≡ z''/z

### Mode equation

v_k'' + [c_s²(τ)·k² − U_s(τ)] v_k = 0

### Split the effective mass function

U_s(τ) = U₀(τ; M) + ΔU_ST(τ)

where:
- M = discrete perturbation prescription (dressed-like, hybrid-like, alternative)
- ΔU_ST(τ) = (A_s/σ_s²) exp(−τ²/(2σ_s²)) × (1 + α_s τ/σ_s)

### Interpretation of ΔU_ST parameters

| Parameter | Physical meaning |
|-----------|-----------------|
| A_s | Height of the bounce feature in the effective potential |
| σ_s | Width of the feature in conformal time |
| α_s | Odd/asymmetric deformation (breaks time-reversal around bounce) |

This is the minimal useful scalar model. It changes the height, width, and asymmetry of the bounce-era effective potential — exactly what matters for P(k) features.

### CRITICAL: Perturbation prescription is a MODEL CHOICE, not a nuisance

Different prescriptions M and different vacuum choices V produce visibly different spectra. Run SEPARATE CHAINS for each (M, V) combination, then do model comparison. Do NOT mix them into one chain.

---

## 3. Fast Scalar Template for MCMC

### Why a template

Full mode integration at each MCMC step is too slow and too sensitive to unresolved quantization choices.

### Approach

1. Use the background/mode solver to generate TRAINING SPECTRA
2. Fit a fast spectrum-level transfer function

### Transfer function

P_R(k) = P_R^{ref}(k) × T_s(k)

ln T_s(k) = B_s × exp[−ln²(k/k_b) / (2σ_k²)] × [1 + α_k tanh(ln(k/k_b)/Δ_k)]

### Approximate mapping to microphysics

k_b ~ σ_s⁻¹
B_s ∝ A_s
α_k ~ α_s

### Fast scalar chain parameters

θ_scalar^fast = {B_s, ln k_b, σ_k, α_k}

This is what the FIRST chain should fit — not raw microphysics. Then map back to {A_s, σ_s, α_s, Δρ, α, n_★, ξ_s} after narrowing.

---

## 4. PBH / Compact-Seed Channel

### Density spectrum at formation

P_δ(R, k) = [4(1+w_f)² / (5+3w_f)²] × (kR)⁴ × T²(R,k) × P_R(k)

(reduces to standard 16/81 factor when w_f = 1/3)

### Smoothed variance

σ²(M) = ∫ d ln k W²(kR) P_δ(R,k)

### Collapse fraction (Gaussian)

β(M) ≈ (1/√(2π)) × (σ(M)/δ_c) × exp[−δ_c² / (2σ²(M))]

### Critical collapse (optional refinement)

M_PBH = K × M_H × (δ − δ_c)^γ

with benchmark K ~ 4, γ ~ 0.36.

### Integrated abundance

f_PBH = (1/Ω_CDM) ∫ d ln M (M_eq/M)^{1/2} β(M)

### PBH chain parameters

θ_PBH = {B_s, ln k_b, σ_k, α_k, δ_c, K, γ}

### Constraint handling

For extended mass functions, do NOT compare to monochromatic bounds by eye. Use the conservative integrated test:

I_i(θ) ≡ ∫ d ln M ψ(M; θ) / f_{i,max}^{mono}(M) ≤ 1

for each experimental bound i. Penalize only violations.

### Public data: PBHbounds (GitHub: bradkav/PBHbounds, MIT license)

---

## 5. Tensor/Parity Sector

### Chiral tensor mode equation

u_{λ,k}'' + [k² − a''/a + λ·μ_PV·k·Φ'(τ)] u_{λ,k} = 0,    λ = ±1

### Localized parity source

Φ'(τ) = (ΔΦ / √(2π)σ_φ) × exp[−(τ − τ_φ)² / (2σ_φ²)]

### Chirality parameter

χ(k) = [P_h^R(k) − P_h^L(k)] / [P_h^R(k) + P_h^L(k)]

### 5a. Direct photon birefringence submodel

If the parity-odd field couples to photons:

β = (g_γ/2) × [Φ(η₀) − Φ(η_dec)]

Under constant-β approximation:

C_ℓ^{EB} = (1/2) sin(4β) × (C̃_ℓ^{EE} − C̃_ℓ^{BB})
C_ℓ^{TB} = sin(2β) × C̃_ℓ^{TE}

Fast parity chain: θ_parity^fast = {β}

### 5b. Tensor-chirality submodel

C_ℓ^{TB,tens} = 4π ∫ d ln k χ(k) P_t(k) Δ_ℓ^{T,T}(k) Δ_ℓ^{B,T}(k)
C_ℓ^{EB,tens} = 4π ∫ d ln k χ(k) P_t(k) Δ_ℓ^{E,T}(k) Δ_ℓ^{B,T}(k)

Template chirality:

χ(k) = χ₀ × exp[−ln²(k/k_χ) / (2σ_χ²)]

Fast chirality chain: θ_chirality^fast = {χ₀, ln k_χ, σ_χ, r}

---

## 6. Likelihoods

### CMB (EB/TB): Gaussian binned-spectrum

−2 ln L_CMB = (D − M(θ))ᵀ Σ⁻¹ (D − M(θ))

where D = binned observed EB/TB spectrum, M(θ) = model prediction, Σ = covariance.

### PBH: constraint table with integrated test

For each bound i: I_i(θ) ≤ 1. Penalize violations.

### Public data products

| Dataset | Source | Status |
|---------|--------|--------|
| Planck PR4 NPIPE EB spectra | NERSC portal | Public |
| ACT DR6 spectra + likelihood | arXiv:2503.14452 | Public |
| PBHbounds constraint tables | GitHub bradkav/PBHbounds | Public, MIT license |
| PBHconstraints (2026 review) | arXiv:2601.06024 | Public, GitHub |

---

## 7. Execution Order

### Chain 1: Fast scalar/PBH (FIRST — gives hard yes/no)

Fit {B_s, ln k_b, σ_k, α_k, δ_c, K, γ} against PBH bounds.
→ Does the bounce feature parameter space support a compact-seed channel?

### Chain 2: Fast parity

Fit {β} to public EB/TB products.
→ What β range does the data support? (Refines Paper 1's consistency check into a real constraint.)

### Chain 3: Full solver calibration

Generate grid in {Δρ, α, n_★, ξ_s, A_s, σ_s, α_s}, solve mode equations, regress the mapping to {B_s, k_b, σ_k, α_k}.
→ Connects fast templates back to microphysics.

### Chain 4: Separate model-class runs

Repeat for each perturbation prescription M and each vacuum choice V.
→ Model comparison, not parameter estimation within a single model.

---

## 8. What This Means for the Paper 2 Research Program

### What's implementable NOW (weeks, not months)
- Chain 1 (fast scalar/PBH): all ingredients exist — PBHbounds data, Press-Schechter, template P(k)
- Chain 2 (fast parity β): public EB spectra exist, Gaussian likelihood is standard

### What requires the full perturbation solver (months)
- Chain 3 (solver calibration): requires solving the mode equation for O(10⁴) k-values × O(10³) parameter combinations
- Chain 4 (model comparison): same solver, different prescriptions

### What remains genuinely uncertain
- Perturbation prescription choice (model class, not parameter)
- Vacuum state choice (model class, not parameter)
- Spin condensate microphysics at Planck densities

### The clean scientific statement

Track B (PBH) becomes real once you define the scalar bounce feature and push it through PBH abundance.
Track C (parity) becomes real immediately with a direct-birefringence β chain.
The exact microphysical z_ST(τ) remains a later paper unless you commit to a specific perturbation prescription and vacuum state.
