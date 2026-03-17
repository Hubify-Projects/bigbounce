# Perturbation Calculation Through the Spin-Torsion Bounce: Research Program Sketch

**Date:** 2026-03-13
**Purpose:** Define the single calculation that would upgrade the framework from "phenomenological" to "predictive"
**Status:** RESEARCH PROGRAM DESIGN — no calculation performed

---

## 0. Why This Calculation Matters

The current paper (Paper 1) derives **background cosmology**: the modified Friedmann equation, inflationary dilution, dark energy. All MCMC chains test the background expansion history.

To predict PBHs, SMBH seeds, or any structure formation observable, we need the **perturbation spectrum** P_R(k). This requires solving the Mukhanov-Sasaki equation through the bounce, modified by spin-torsion physics.

This is the single calculation that would simultaneously unlock:
- Primordial power spectrum features
- PBH predictions (and asteroid-mass PBH dark matter)
- Tensor chirality predictions (gravitational wave parity violation)
- A derived (not assumed) initial condition for inflation

---

## 1. Standard Mukhanov-Sasaki Equation (Review)

For scalar perturbations in single-field inflation, the gauge-invariant Mukhanov variable v_k satisfies:

```
v_k'' + (k² − z''/z) v_k = 0                    [MS equation]
```

where:
- Primes denote conformal time τ derivatives
- k is the comoving wavenumber
- z = a √(2ε₁) M_Pl is the "pump field"
- ε₁ = −Ḣ/H² is the first Hubble flow parameter
- a(τ) is the scale factor

The curvature power spectrum is:

```
P_R(k) = k³/(2π²) × |v_k/z|²    evaluated at late times (k ≪ aH)
```

The physics is entirely encoded in the pump term z''/z, which depends on the background evolution a(τ), H(τ).

For standard slow-roll inflation: z''/z ≈ 2/τ² (de Sitter limit), giving the nearly scale-invariant spectrum P_R ∝ k^{n_s−1}.

---

## 2. How the Spin-Torsion Bounce Modifies the Background

### 2a. Modified Friedmann Equation (already in Paper 1)

```
H² = (8πG/3) ρ [1 − ρ/ρ_c]                      [Eq. from LQC]
```

with ρ_c = (√3 / 32π²γ³) ρ_Pl ≈ 0.27 ρ_Pl for γ = 0.274.

This creates a smooth bounce: H → 0 at ρ → ρ_c, with ä > 0 (deceleration → acceleration).

### 2b. Four-Fermion Contact Interaction (modifies equation of state)

From Einstein-Cartan theory, torsion is non-propagating. The Cartan equation:

```
T^a_{bc} = −8πG S^a_{bc}
```

determines torsion algebraically from the spin density S. Substituting back gives an effective four-fermion interaction:

```
L_int = −(3πG/2) × [γ²/(γ²+1)] × J^μ_A J_{Aμ}     [Hehl 1976]
```

At Planck densities (ρ ~ ρ_c), this modifies the effective equation of state:

```
w_eff(ρ) = w_bare + Δw_spin(ρ)
```

where Δw_spin depends on the spin condensate of the fermion field at Planck densities. The key effect: w_eff ≠ w_bare during the bounce, which changes the trajectory a(τ) through the bounce.

**What's known:** The form of the four-fermion interaction (standard EC result).
**What needs computation:** The spin condensate ⟨J_A J_A⟩ at Planck densities, and hence Δw_spin(ρ). This determines how the bounce trajectory differs from standard LQC.

### 2c. Modified Background Trajectory

The bounce trajectory a(τ) is found by solving:

```
a'' = a × [H² + Ḣ]    (conformal time)
     = a × (8πG/3) × [(ρ + 3P_eff)/2 × (1 − ρ/ρ_c) − ρ²/ρ_c]
```

where P_eff includes the four-fermion pressure correction.

This determines a(τ), H(τ), ε₁(τ) — and hence z(τ) and z''/z — through the entire bounce-to-inflation transition.

---

## 3. The Modified Mukhanov-Sasaki Equation: Scalar Sector

### 3a. First-Order Scalar Perturbations

The scalar Mukhanov-Sasaki equation retains its standard form:

```
v_k'' + (k² − z_ST''/z_ST) v_k = 0
```

but with z_ST computed from the MODIFIED background:

```
z_ST(τ) = a(τ) × √(2 ε₁_ST(τ)) × M_Pl
```

where ε₁_ST = −Ḣ/H² uses the spin-torsion-modified H(τ).

**The pump term z_ST''/z_ST is the central object to compute.**

In terms of the Hubble flow parameters:

```
z''/z = a²H² × [2 − ε₁ + (3/2)ε₂ − (1/2)ε₁ε₂ + (1/4)ε₂² + (1/2)ε₂ε₃]
```

where:
- ε₁ = −Ḣ/H²
- ε₂ = ε̇₁/(H ε₁)
- ε₃ = ε̇₂/(H ε₂)

Through the bounce, H → 0 and ε₁ → ∞ (or becomes ill-defined), making these expressions singular. The standard approach is to work directly with a(τ) and its derivatives.

### 3b. What's Different from Standard LQC

In standard LQC (no torsion), the pump term z''/z has been computed by Agullo, Ashtekar, Nelson (2012-2013) and Zhu, Cleaver, Ashtekar (2017). The results:

- **IR suppression:** Modes with k < k_LQC (modes that were super-Hubble during the bounce) show suppressed power relative to the standard nearly scale-invariant spectrum.
- **Oscillatory features:** At k ~ k_LQC, there are oscillations in P(k) from interference between growing and decaying modes that were excited during the bounce.
- **Near-scale-invariance at large k:** Modes with k >> k_LQC are unaffected (they were deep inside the Hubble radius and didn't feel the bounce).

The spin-torsion modifications change this picture in two ways:

1. **Modified w_eff during the bounce** changes the shape of z''/z near τ = 0 (the bounce). This alters the oscillatory features and could enhance or suppress power at specific scales.

2. **The parity-odd operator** does not enter the scalar sector at first order (it's a pseudo-scalar coupling). But it does enter at second order (see Section 5 below).

### 3c. The Crucial z''/z Profile

Schematically, z''/z through the bounce looks like:

```
        z''/z
          |
          |    ╱╲         Standard LQC
     ─────|───╱──╲────────── slow-roll inflation (≈ 2/τ²)
          |  ╱    ╲
          | ╱      ╲
          |╱        ╲
          |          ╲
   ───────┼───────────╲─── bounce (τ = 0)
          |
          |
```

The peak and width of the z''/z feature near the bounce determine:
- **k_feature**: modes with k ≈ √(z''/z)|_peak are maximally affected
- **A_feature**: the amplitude of the departure from scale-invariance
- **Δ_feature**: the width of the affected k-range

The four-fermion interaction changes the SHAPE of this peak (its height, width, and asymmetry), which changes the resulting P(k).

---

## 4. The Modified Mukhanov-Sasaki Equation: Tensor Sector

### 4a. Standard Tensor Equation

For tensor perturbations h_{ij}, decomposed into circular polarization modes:

```
u_k^{L,R}'' + (k² − a''/a) u_k^{L,R} = 0           [standard]
```

where u = a h / (√(32πG)).

### 4b. Parity-Odd Modification

The parity-odd operator (α/M) ε^{abcd} K_{ab} R_{cd} breaks L/R symmetry in the tensor sector.

At linear order in perturbations, this modifies the tensor equation to:

```
u_k^L'' + [k² − a''/a + λ k Φ'(τ)] u_k^L = 0
u_k^R'' + [k² − a''/a − λ k Φ'(τ)] u_k^R = 0
```

where:
- λ is a coupling constant proportional to α/M
- Φ(τ) is a background pseudo-scalar field sourced by the torsion sector
- The ± sign is what breaks parity: L and R modes see different effective potentials

**This is the gravitational Chern-Simons modification to tensor perturbations.**

The key new physics: during the bounce (when torsion is active), Φ'(τ) is nonzero and potentially large, creating a chiral gravitational wave background where:

```
P_T^L(k) ≠ P_T^R(k)
```

This chirality is the tensor counterpart of the scalar birefringence already discussed in Paper 1.

### 4c. What's Known

- The structure of the Chern-Simons modification to tensor perturbations is well-studied (Alexander & Yunes 2009, Jackiw & Pi 2003).
- The specific form of Φ(τ) for the spin-torsion case has NOT been derived.
- Φ(τ) depends on the dynamics of the torsion pseudo-scalar condensate through the bounce.

### 4d. Observable: Tensor Chirality Parameter

Define:

```
Δχ(k) ≡ [P_T^R(k) − P_T^L(k)] / [P_T^R(k) + P_T^L(k)]
```

Δχ = 0: parity-preserving (standard GR)
Δχ ≠ 0: parity-violating (spin-torsion prediction)

This is directly observable through:
- CMB TB and EB cross-correlations (already partially measured)
- Gravitational wave circular polarization (LISA, pulsar timing arrays)

---

## 5. Second-Order Scalar Perturbations from Chiral Tensors

### 5a. Scalar-Induced Perturbations

At second order in perturbation theory, tensor perturbations source scalar perturbations:

```
v_k'' + (k² − z''/z) v_k = S_k^(2)[h_L, h_R]
```

The source term S_k^(2) involves convolutions of the first-order tensor modes:

```
S_k^(2) ∝ ∫ d³p [h_p h_{k-p}] × (geometric kernel)
```

If the tensor spectrum is chiral (P_T^L ≠ P_T^R), this source term is NONZERO even if the first-order scalar spectrum is standard. This is the "parity-odd tensor → scalar induction" pathway.

### 5b. Amplitude Estimate

The induced scalar perturbation is suppressed by:

```
P_R^(induced) / P_R^(standard) ~ r² × Δχ² × (geometric factor)
```

where r is the tensor-to-scalar ratio (r < 0.036 from BICEP/Keck).

For r ~ 0.01 and Δχ ~ O(1) (which requires the parity-odd operator to be maximally active during the bounce), this gives:

```
P_R^(induced) / P_R^(standard) ~ 10^{-4} × (geometric factor)
```

This is small — likely too small to produce PBHs (which need P_R ~ 10^{-2}). But it could produce a detectable feature in the scalar spectrum at the ~10^{-13} level.

**Honest assessment:** The second-order channel is probably too weak for PBH formation. The first-order scalar modification from the modified z''/z is the more promising route.

---

## 6. Computational Program

### Phase 1: Background Solution (~2 months)

**Goal:** Solve for a(τ) through the entire bounce-to-inflation transition.

Steps:
1. Specify the scalar field potential V(φ) (e.g., Starobinsky R² or quadratic)
2. Determine the spin condensate ⟨J_A J_A⟩ as a function of ρ
   - For a thermal fermion gas: ⟨J_A J_A⟩ ∝ T⁴ at high T
   - At Planck density: T ~ T_Pl, so ⟨J_A J_A⟩ ~ ρ_Pl²
3. Solve the modified Friedmann equation + Klein-Gordon equation for φ:
   ```
   H² = (8πG/3) ρ_eff (1 − ρ_eff/ρ_c)
   φ̈ + 3Hφ̇ + V'(φ) = 0
   ```
   with ρ_eff = (1/2)φ̇² + V(φ) + ρ_spin(ρ)
4. Track the solution from contraction → bounce → inflation → slow-roll

**Output:** a(τ), H(τ), φ(τ), ε₁(τ) from τ = −∞ to τ → ∞

**Existing code that could be adapted:**
- LQC perturbation codes from Agullo/Ashtekar group
- CosmoSIS or CLASS modified for bounce cosmologies
- Custom ODE integrator (Python/Julia) — bounce is stiff, needs adaptive stepping

### Phase 2: Scalar Power Spectrum (~3 months)

**Goal:** Solve the Mukhanov-Sasaki equation for each k and extract P_R(k).

Steps:
1. Compute z_ST(τ) and z_ST''/z_ST from the background solution
2. For each wavenumber k (~ 10^4 values spanning 10^{-4} to 10^{20} Mpc^{-1}):
   a. Set initial conditions in the contracting phase:
      v_k → (1/√(2k)) e^{-ikτ}  (Bunch-Davies-like, but care needed at bounce)
   b. Numerically integrate v_k'' + (k² − z''/z) v_k = 0 through the bounce
   c. Extract P_R(k) = k³/(2π²) |v_k/z|² at late times
3. Identify features: bumps, oscillations, suppression relative to standard P_R

**Critical subtlety — initial conditions:**
The choice of vacuum state at the bounce is ambiguous. Options:
- 4th-order adiabatic vacuum (Agullo+ approach)
- NO-boundary-like state
- Thermal state from the pre-bounce contraction

Different choices give different P_R(k). This is a genuine theoretical ambiguity that must be explored and reported honestly.

**Output:** P_R(k) for multiple initial state choices and multiple V(φ) potentials

### Phase 3: Tensor Chirality (~2 months, can overlap with Phase 2)

**Goal:** Solve the chiral tensor equation and extract Δχ(k).

Steps:
1. Determine Φ(τ) from the torsion pseudo-scalar dynamics through the bounce
   - This requires modeling how the parity-odd condensate ⟨ε^{abcd} K_{ab} R_{cd}⟩ evolves
   - At the bounce: K_{ab} ~ ρ_c^{1/2} M_Pl^{-1}, R_{cd} ~ ρ_c M_Pl^{-2}
   - The condensate is proportional to (α/M) × M_Pl² × ρ_c / M_Pl⁴ ~ (α/M) × ρ_c / M_Pl²
2. Solve the chiral tensor equations for each k:
   u_k^{L,R}'' + [k² − a''/a ± λk Φ'] u_k^{L,R} = 0
3. Extract P_T^L(k), P_T^R(k), and Δχ(k)

**Output:** Tensor power spectra and chirality parameter

### Phase 4: Observational Mapping (~3 months)

**Goal:** Map P_R(k) and P_T(k) to observables.

Steps:
1. **CMB:** Modify CAMB/CLASS to use the computed P_R(k) and P_T(k) instead of the standard power-law. Compute C_ℓ^{TT}, C_ℓ^{EE}, C_ℓ^{BB}, C_ℓ^{EB}, C_ℓ^{TB}.
2. **PBHs:** If P_R(k) has features at k ~ 10^{15} Mpc^{-1} (the N_tot = 92 scale), compute f_PBH(M) using Press-Schechter.
3. **μ-distortions:** Integrate the enhanced P_R(k) against the μ-distortion window function.
4. **MCMC:** If the above produce testable predictions, set up a Cobaya chain with P_R(k) feature parameters derived from the bounce calculation.

**Output:** Predictions for CMB, PBH abundance, spectral distortions

### Phase 5: Paper 2 (~2 months)

**Goal:** Write and submit "Primordial Perturbations from the Spin-Torsion Bounce"

---

## 7. Key Unknowns and Honest Uncertainties

| Unknown | Impact | Reducible? |
|---------|--------|-----------|
| Spin condensate at Planck densities | Changes w_eff, hence z''/z | Partially — lattice QCD at high T gives guidance, but ρ_Pl is far beyond |
| Vacuum state choice at bounce | Changes P_R(k) qualitatively | NO — this is a genuine theoretical ambiguity. Must be explored parametrically. |
| Parity-odd condensate dynamics | Determines tensor chirality | Partially — order-of-magnitude from (α/M) × ρ_c, but time dependence unknown |
| Non-linear corrections to Press-Schechter | Changes f_PBH by O(1) | YES — computable with standard N-body/peak theory |
| Scalar-tensor coupling at 2nd order | May enhance or suppress scalar features | YES — straightforward but tedious |

The **vacuum state ambiguity** is the most fundamental. It's not a calculational difficulty — it's a genuine question about the physics. Paper 2 should present results for MULTIPLE vacuum state choices and discuss how observations could distinguish them.

---

## 8. What This Calculation Could Produce

### Best case:
The spin-torsion bounce produces a distinctive P_R(k) feature at k ~ 10^{15} Mpc^{-1} with amplitude above the PBH threshold. This would predict asteroid-mass PBH dark matter — a concrete, testable prediction unique to the framework. Combined with the tensor chirality prediction, this would give Paper 2 two independent observables derived from first principles.

### Likely case:
The P_R(k) feature is at k ~ 10^{15} Mpc^{-1} but with uncertain amplitude (dependent on vacuum state choice and spin condensate model). The tensor chirality Δχ is nonzero but small. Paper 2 identifies the parameter space and the required observations. Still publishable and honest.

### Worst case:
The spin-torsion modifications to z''/z are negligible (the spin condensate washes out, or the four-fermion interaction doesn't significantly change w_eff at the bounce). P_R(k) is essentially the same as standard LQC. Paper 2 reports a null result — which is still informative and publishable ("spin-torsion corrections do not significantly modify the primordial perturbation spectrum from LQC bounces").

---

## 9. Required Expertise and Resources

| Requirement | Status |
|-------------|--------|
| LQC perturbation theory | Need collaborator (Agullo, Wilson-Ewing, or Ashtekar group) |
| Numerical ODE integration (stiff systems) | Available (Python/Julia) |
| Chern-Simons perturbation theory | Published literature (Alexander & Yunes 2009) |
| Modified CAMB/CLASS | Feasible (parameterized P(k) input) |
| MCMC infrastructure | Already built (Cobaya on RunPod) |
| Total compute time | ~100 CPU-hours for perturbation integration; ~1000 CPU-hours for MCMC |
| Total research time | **12-18 months** for a thorough job |

---

## 10. Summary: The One Equation That Matters

The entire research program reduces to computing ONE function:

```
z_ST(τ) = a(τ) × √(2 ε₁_ST(τ)) × M_Pl
```

through the spin-torsion bounce, where:
- a(τ) comes from the modified Friedmann equation with four-fermion pressure correction
- ε₁_ST(τ) = −Ḣ/H² with H from the same modified equation
- The four-fermion interaction changes w_eff(ρ) near the bounce
- The parity-odd operator is irrelevant for z_ST at first order (enters tensors only)

Once z_ST(τ) is known, everything else follows:
- P_R(k) from the Mukhanov-Sasaki equation
- PBH abundance from Press-Schechter
- CMB observables from CAMB/CLASS
- Tensor chirality from the separate chiral equation

**z_ST(τ) is the bridge between the framework and the perturbation spectrum.**
