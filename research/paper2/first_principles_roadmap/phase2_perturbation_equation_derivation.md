# Phase 2: Linear Perturbation Equations Through the Spin-Torsion Bounce

**Date:** 2026-03-13
**Status:** DERIVATION PLAN — equations identified, key unknowns flagged

---

## 1. Starting Point: Gauge-Invariant Perturbation Theory

### 1a. Scalar Perturbations — Mukhanov-Sasaki Equation

The gauge-invariant Mukhanov variable v_k satisfies:

```
v_k'' + [c_s²(τ) k² − U_s(τ)] v_k = 0
```

where:
- Primes: d/dτ (conformal time)
- k: comoving wavenumber
- c_s²(τ): sound speed squared (may differ from 1/3 through the bounce)
- U_s(τ) ≡ z''/z: effective mass / pump term

Standard definitions:
```
z(τ) = a(τ) √(2ε₁(τ)) M_Pl / c_s(τ)
ε₁ = −Ḣ/H²
```

The curvature power spectrum:
```
P_R(k) = k³/(2π²) × |v_k/z|²   (evaluated when k ≪ aH)
```

### 1b. The Central Object: U_s(τ) = z''/z

In terms of Hubble flow parameters:

```
z''/z = a²H² [2 − ε₁ + (3/2)ε₂ − (1/2)ε₁ε₂ + (1/4)ε₂² + (1/2)ε₂ε₃]
```

where:
```
ε₁ = −Ḣ/H²
ε₂ = ε̇₁/(H ε₁)
ε₃ = ε̇₂/(H ε₂)
```

**PROBLEM:** Through the bounce, H → 0 and ε₁ → ∞. The Hubble flow expansion is singular. Must work directly with a(τ) and compute z''/z numerically.

---

## 2. What Torsion Modifies

### 2a. Sound Speed c_s

In standard single-field inflation: c_s = 1.

With the four-fermion interaction, the effective fluid has:
```
c_s² = (dP_eff/dn) / (dρ_eff/dn)
```

where n is a conserved fermion density proxy (n ∝ a⁻³), and:
```
ρ_eff = ρ_inflaton + V_s(n)     [inflaton + spin condensate]
P_eff = P_inflaton + n dV_s/dn − V_s(n)
```

**Key effect:** c_s² can deviate from 1/3 (radiation) or 1 (stiff matter) during the bounce. If the spin condensate has a phase transition (as modeled by the tanh closure), c_s² can have a sharp feature.

**Status:** FUNCTIONAL FORM requires specifying V_s(n). The tanh model from the MCMC-ready document:
```
V_s(n) = m·n·[1 − tanh(α(n − n_★))]/2
       + [m·n_★ + Δρ + ξ_s·κ·(n − n_★)²]·[1 + tanh(α(n − n_★))]/2
```
is phenomenological. A first-principles V_s(n) requires computing the fermion spin condensate at Planck densities.

### 2b. Effective Mass Term z''/z

The pump field z_ST is computed from the MODIFIED background:
```
z_ST(τ) = a(τ) √(2ε₁_ST(τ)) M_Pl / c_s(τ)
```

where a(τ), H(τ), ε₁(τ), c_s(τ) all come from the spin-torsion-modified equations.

**Changes from standard LQC:**

1. The four-fermion interaction changes w_eff during the bounce → changes the trajectory a(τ) → changes the shape of z''/z near τ = 0

2. If c_s ≠ 1, the mode equation becomes:
```
v_k'' + [c_s²(τ) k² − z''/z] v_k = 0
```
This effectively rescales k → c_s k, shifting the feature scale.

3. The spin condensate phase transition (if sharp) can create an additional spike or dip in z''/z beyond the standard LQC bounce feature.

### 2c. Profile of z''/z Through the Bounce

Schematic (standard LQC without torsion corrections):

```
z''/z
  ^
  |         ╱╲
  |        ╱  ╲         ← peak at bounce, height ~ (a_bounce H_max)²
  |       ╱    ╲
  |      ╱      ╲
  |─────╱────────╲───── → 2/τ² (slow-roll de Sitter)
  |    ╱          ╲
  |───╱────────────╲─── → 0 (deep contraction)
  |
  └──────────────────── τ
     contraction  bounce  expansion
```

The peak determines:
- **k_feature ~ √(z''/z)|_peak:** wavenumber most affected
- **A_feature ~ height/width ratio:** amplitude of departure from scale invariance
- **Δk/k_feature ~ width:** breadth of affected k-range

With spin-torsion corrections, the peak shape changes — potentially becoming:
- Taller/shorter (different w_eff at bounce)
- Wider/narrower (different transition timescale)
- Asymmetric (different contraction vs expansion dynamics)
- Multi-peaked (if phase transition in c_s or w_eff)

### 2d. Scalar-Vector Mode Coupling

In standard FLRW perturbation theory, scalar, vector, and tensor modes decouple at linear order.

**Does torsion couple them?**

At linear order in perturbations around FLRW: NO, provided the background is isotropic. The FLRW symmetry guarantees decoupling of the SVT decomposition even with torsion, because torsion only modifies the background EOS (torsion is algebraic, not propagating).

However, if the background has anisotropy (e.g., from the rotating BH interior), then scalar-vector coupling can occur through the background vorticity. The coupling strength is proportional to (ω/H)², which is bounded by < 10⁻²¹ from CMB isotropy.

**Conclusion:** Scalar-vector coupling is negligible at linear order. Can be safely ignored.

### 2e. Parity-Odd Terms in the Scalar Sector

The parity-odd operator ε^{abcd} K_{ab} R_{cd} is a PSEUDO-SCALAR. At first order in perturbation theory:

- It does NOT modify the scalar Mukhanov-Sasaki equation (scalar perturbations are parity-even)
- It DOES modify the tensor equation (see below)
- At second order, it induces scalar perturbations from tensor modes (see Section 5)

**Conclusion:** The scalar sector is modified ONLY through the background (modified a(τ), w_eff, c_s), not through additional parity-odd source terms at first order.

---

## 3. Tensor Perturbations

### 3a. Standard Tensor Equation

For tensor perturbations h_{ij} decomposed into circular polarizations (L, R):

```
u_k^{L,R}'' + [k² − a''/a] u_k^{L,R} = 0    (standard GR)
```

where u = a h / √(32πG).

### 3b. Parity-Odd Modification (Gravitational Chern-Simons)

The parity-odd operator modifies the tensor equation to:

```
u_k^L'' + [k² − a''/a + λ k Φ'(τ)] u_k^L = 0
u_k^R'' + [k² − a''/a − λ k Φ'(τ)] u_k^R = 0
```

where:
- λ: coupling proportional to α/M
- Φ(τ): background pseudo-scalar field from the torsion sector
- The ± sign breaks parity: L and R see different effective potentials

**Source of chirality:** During the bounce, when torsion is active, Φ'(τ) is nonzero and potentially large.

### 3c. The Unknown: Φ(τ)

The pseudo-scalar Φ(τ) is sourced by the torsion condensate:
```
Φ(τ) ~ ⟨ε^{abcd} K_{ab} R_{cd}⟩|_background
```

At the bounce:
- K_{ab} ~ ρ_c^{1/2} M_Pl⁻¹ (contorsion from spin density)
- R_{cd} ~ ρ_c M_Pl⁻² (curvature at Planck scale)
- Therefore Φ ~ (α/M) × ρ_c^{3/2} / M_Pl³

The TIME DEPENDENCE Φ(τ) is not known. The MCMC-ready model parameterizes it as:
```
Φ'(τ) = (ΔΦ/√(2π)σ_φ) exp[−(τ − τ_φ)²/(2σ_φ²)]
```
which is a Gaussian pulse localized near the bounce. This is a phenomenological template.

### 3d. Observable: Tensor Chirality

```
Δχ(k) ≡ [P_T^R(k) − P_T^L(k)] / [P_T^R(k) + P_T^L(k)]
```

Observable through:
- CMB TB and EB cross-correlations
- Gravitational wave circular polarization (LISA, PTA)

---

## 4. Second-Order Scalar Perturbations from Chiral Tensors

At second order, tensor perturbations source scalar perturbations:

```
v_k'' + [k² − z''/z] v_k = S_k^(2)[h_L, h_R]
```

Source term:
```
S_k^(2) ∝ ∫ d³p [h_p h_{k−p}] × (geometric kernel)
```

If P_T^L ≠ P_T^R (chiral), the source is nonzero.

**Amplitude estimate:**
```
P_R^(induced) / P_R^(standard) ~ r² × Δχ² × (geometric factor)
```

For r ~ 0.01, Δχ ~ O(1): ratio ~ 10⁻⁴. **Too small for PBH formation** (needs P_R ~ 10⁻²). Potentially detectable as a spectral feature at ~10⁻¹³ level.

---

## 5. Perturbation Prescription Ambiguity

### 5a. The Problem

In loop quantum cosmology, there is no unique way to "quantize" the perturbations on the quantum bounce background. Different approaches give different effective mass functions U_s(τ):

| Prescription | Reference | Key Difference |
|-------------|-----------|----------------|
| Dressed metric | Agullo, Ashtekar, Nelson (2012-2013) | Uses dressed background at quantum level |
| Hybrid | Fernandez-Mendez, Mena Marugan, Olmedo (2012) | Quantizes background and perturbations separately |
| Effective | Bojowald (various) | Uses effective equations throughout |
| Deformed algebra | Barrau, Cailleteau, Grain (2012) | Modifies constraint algebra |

**These are not approximations to the same answer. They are genuinely different theories that agree in the classical limit but differ through the bounce.**

### 5b. For Spin-Torsion Variant

The spin-torsion framework adds another layer of ambiguity:
- How does the four-fermion interaction enter the perturbation Hamiltonian?
- Does the spin condensate contribute to the perturbation mass term?
- Is the contorsion treated as a background or perturbed quantity?

**CRITICAL DECISION:** These must be treated as separate model classes (separate chains), not nuisance parameters within a single chain.

---

## 6. Summary: The ODE System

For scalar perturbations, the full ODE system is:

**Background ODEs (Phase 1 input):**
```
a' = a²H                                    [scale factor]
H' = a × Ḣ                                  [where Ḣ = −(κ/2)(ρ + P)(1 − 2ρ/ρ_c)]
φ' = a × φ̇                                  [inflaton field]
φ̇' = a × [−3Hφ̇ − V'(φ)]                   [Klein-Gordon]
n' = −3aHn                                   [fermion density]
```

**Perturbation ODE (for each k):**
```
v_k'' + [c_s²(τ) k² − U_s(τ)] v_k = 0
```

where U_s(τ) = z''/z is computed from the background solution.

**Tensor ODE (for each k and polarization λ = ±1):**
```
u_{λ,k}'' + [k² − a''/a + λ μ_PV k Φ'(τ)] u_{λ,k} = 0
```

---

## 7. Unknown Coefficients

| Coefficient | Appears in | Physical origin | Status |
|------------|-----------|----------------|--------|
| V_s(n) | ρ_eff, P_eff | Spin condensate energy | UNKNOWN — requires Planck-density physics |
| c_s²(τ) | Mode equation | Effective sound speed | DERIVED once V_s(n) is specified |
| U_s(τ) = z''/z | Mode equation | Pump term | DERIVED once background is solved |
| λ μ_PV | Tensor equation | Parity-odd coupling | UNKNOWN — requires Φ(τ) dynamics |
| Φ'(τ) | Tensor equation | Parity-odd pseudo-scalar | UNKNOWN — requires condensate dynamics |
| V(φ) | Inflaton potential | Inflation model | ASSUMED (e.g., Starobinsky R²) |

The irreducible unknowns are V_s(n) (spin condensate) and Φ(τ) (parity-odd condensate dynamics). Everything else follows once these are specified.
