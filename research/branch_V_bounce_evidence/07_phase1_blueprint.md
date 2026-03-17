# Branch V Phase 1: Execution Blueprint

**Created:** 2026-03-17
**Target:** V2a — Matter Bounce through ECH
**Goal:** Compute P_ζ(k), n_s, r, n_T, and f_NL for dust contraction → ECH bounce → radiation expansion

---

## Phase 1a: Background Cosmology

### Objective
Build a numerical solver for the background scale factor a(t) that smoothly interpolates between:
1. Dust contraction (t ≪ -t_trans): a(t) ∝ (-t)^{2/3}
2. Transition to radiation (t ~ -t_trans): smooth EOS change w: 0 → 1/3
3. ECH bounce (t ~ 0): a(t) = a_b(1 + 4α²t²)^{1/4}
4. Radiation expansion (t ≫ t_bounce): a(t) ∝ t^{1/2}

### Background Equations

The modified Friedmann equation:
```
H² = (8πG/3) ρ (1 - ρ/ρ_crit)
```

Conservation equation:
```
ρ̇ + 3H(ρ + p) = 0
```

Equation of state:
```
w(t) = w_dust × f(t) + w_rad × (1 - f(t))
```
where f(t) is a smooth interpolation function (tanh or similar) centered at t = -t_trans.

### Parameters

| Parameter | Value | Source |
|-----------|-------|--------|
| ρ_crit | 0.21 M_Pl⁴ | ECH framework (fixed) |
| α² | 8πGρ_crit/3 ≈ 1.76 M_Pl² | Derived |
| a_b | Set to 1 (normalization) | Convention |
| w_dust | 0 | Dust |
| w_rad | 1/3 | Radiation |
| t_trans | Free (explore 10–10⁴ t_Pl) | Transition timing |
| Δt_trans | Free (explore 1–100 t_Pl) | Transition duration |

### Implementation
- Language: Python (scipy.integrate.solve_ivp with DOP853)
- Build on existing tensor solver: `research/branch_H_bounce_only/tensor_spectrum/03_tensor_mode_solver.ipynb`
- Output: a(t), H(t), ρ(t), w(t), z(t) as callable interpolation functions

### Deliverable
`research/branch_V_bounce_evidence/phase1_mcmc/01_background_solver.py`

### Validation checks
- [ ] a(t) is monotonically decreasing for t < 0, monotonically increasing for t > 0
- [ ] H = 0 at exactly one point (the bounce)
- [ ] Ḣ(0) > 0 (expansion begins)
- [ ] ρ → ρ_crit at bounce
- [ ] w → 0 for t ≪ -t_trans
- [ ] w → 1/3 for t ≫ t_bounce
- [ ] Matches analytic ECH solution near t = 0

---

## Phase 1b: Scalar Perturbations

### Objective
Solve the Mukhanov-Sasaki equation for scalar perturbations:
```
v_k'' + (c_s² k² - z''/z) v_k = 0
```
where:
- v_k = z ζ_k (Mukhanov variable)
- z = a √(ρ + p) / (c_s H) = a √(2ε) M_Pl / c_s
- ε = -Ḣ/H² (generalized slow-roll parameter)
- c_s² = dp/dρ (adiabatic sound speed)
- Primes are d/dη (conformal time)

### Technical Challenges

**Challenge 1: z diverges at the bounce (H = 0)**

At the bounce, H = 0, so z = a√(2ε)M_Pl/c_s involves ε = -Ḣ/H² which diverges. This is the standard problem of matching perturbations through a bounce.

**Resolution:** Work in terms of the curvature perturbation ζ directly in the Deruelle-Mukhanov (1995) formalism, or use the Hwang-Noh (2002) variable v = aδφ which is regular at H = 0. Alternatively, use the "deformed algebra" approach of Cai et al. (2014) where the effective Mukhanov potential is regularized.

The key insight: the Mukhanov-Sasaki equation in cosmic time is:
```
ζ̈_k + (3H + 2ż/z)ζ̇_k + (c_s k/a)² ζ_k = 0
```
At H = 0, this becomes:
```
ζ̈_k + (2ż/z)ζ̇_k + (c_s k/a_b)² ζ_k = 0
```
which is regular if z is regular. For dust+radiation, z is proportional to a × √(ρ+p)/H, which can be regularized by writing it in terms of Ḣ:
```
z = a² √(2|Ḣ|) M_Pl / (c_s |H|)
```
This still diverges at H = 0. The standard approach is to match solutions on either side of the bounce using the Israel junction conditions for perturbations.

**Our approach:** Numerically evolve in cosmic time with regularized variables. Define:
```
u_k = a × δq    (where q is the Bardeen variable)
```
The equation for u_k is regular through the bounce. Extract ζ_k from u_k after the bounce when H ≠ 0.

**Challenge 2: Initial conditions**

During dust contraction, the Bunch-Davies vacuum in the asymptotic past is:
```
v_k → (1/√(2k)) e^{-ikη}    as η → -∞
```
This must be imposed deep in the contracting phase where WKB is valid.

**Challenge 3: Mode extraction**

After the bounce, extract P_ζ(k) = (k³/2π²)|ζ_k|² on super-Hubble scales. The spectral index is:
```
n_s - 1 = d ln P_ζ / d ln k
```
evaluated at the pivot scale k_* = 0.05 Mpc⁻¹.

### Implementation Plan
1. Choose conformal time η or cosmic time t (cosmic time avoids the η-divergence at the bounce)
2. Evolve mode functions for k = 10⁻⁴ to 1 Mpc⁻¹ (50–100 modes, log-spaced)
3. For each k: initialize in WKB regime → integrate through bounce → extract on super-Hubble scales
4. Compute P_ζ(k), n_s(k), and running α_s

### Deliverable
`research/branch_V_bounce_evidence/phase1_mcmc/02_scalar_perturbations.py`

### Validation checks
- [ ] Matches analytic dust contraction result (v_k ∝ (-kη)^{-1/2} on super-Hubble)
- [ ] Recovers n_s = 1 for pure matter bounce (no EOS transition)
- [ ] P_ζ normalization: A_s ≈ 2.1 × 10⁻⁹ determines a_b or initial amplitude
- [ ] Converges with timestep refinement
- [ ] No numerical instability at the bounce

---

## Phase 1c: Tensor Perturbations

### Objective
Extend the existing tensor solver to the dust contraction background. The mode equation is:
```
h_k'' + 2(a'/a) h_k' + k² h_k = 0    (conformal time)
```
or equivalently:
```
μ_k'' + (k² - a''/a) μ_k = 0    (Mukhanov form, μ = ah)
```

### Key Differences from Branch H Calculation
- **Branch H** used pure radiation (w = 1/3) throughout → symmetric bounce → n_T = 0
- **Phase 1c** uses dust contraction → transition → radiation → bounce dynamics change

### Expected Results
For dust contraction (w = 0):
```
a''/a = 2/η²    → P_T(k) ∝ k^{n_T}  with  n_T = 0
```
This is the same tilt as radiation! The dust matter bounce also gives n_T = 0 for tensors.

For the tensor-to-scalar ratio, the standard matter bounce result is:
```
r = P_T/P_ζ ~ (k/k_b)²  for  k ≪ k_b
```
which is extremely small. The exact value depends on the bounce dynamics.

### Deliverable
`research/branch_V_bounce_evidence/phase1_mcmc/03_tensor_perturbations.py`

### Validation
- [ ] Matches Branch H result in the radiation-only limit
- [ ] Gives n_T = 0 for dust background
- [ ] r is consistent with Planck upper bound r < 0.036

---

## Phase 1d: Consistency Relations

### Objective
Compute the consistency relation r(n_T) and compare to inflation.

### Inflation prediction:
```
r = -8 n_T    (single-field slow-roll)
```

### Matter bounce prediction:
```
r = 24(1 - n_s)/5 c_s²    (Cai & Wilson-Ewing 2014)
```
This is a completely different relation. If both n_s and r are measured, this discriminates between inflation and matter bounce with no free parameters.

### Additional consistency tests:
- **f_NL vs n_s**: Inflation predicts f_NL ~ (n_s - 1) ~ 0.035; matter bounce predicts f_NL = 5/12 independent of n_s
- **Running vs n_s**: Matter bounce gives α_s = (n_s - 1)/ln(k/k_*) which has a specific shape

### Deliverable
`research/branch_V_bounce_evidence/phase1_mcmc/04_consistency_relations.py`

---

## Phase 2a: Spectral Tilt Analysis

### Objective
Systematically identify which mechanism (if any) tilts the matter bounce spectrum from n_s = 1 to n_s = 0.965.

### Approach
Run the Phase 1b solver with different EOS transition profiles and extract n_s for each:

1. **Sharp transition** (Δt_trans → 0): Compute the Bogoliubov coefficient correction
2. **Gradual transition** (Δt_trans ~ 10–1000 t_Pl): Sweep parameter space
3. **ALP-assisted tilt**: Add the birefringence ALP as a subdominant component during contraction; compute the tilt contribution from its mass
4. **Entropy mechanism**: Two-field model where isocurvature → curvature conversion provides the tilt

### Deliverable
`research/branch_V_bounce_evidence/phase1_mcmc/05_spectral_tilt_analysis.py`

---

## Phase 2b: Non-Gaussianity

### Objective
Compute f_NL^local at tree level for the matter bounce + ECH.

### Method
The tree-level bispectrum from matter contraction is (Cai 2009):
```
⟨ζ_k1 ζ_k2 ζ_k3⟩ = (2π)³ δ(k1+k2+k3) × B(k1,k2,k3)
```
with
```
f_NL^local = (5/18) × B_squeezed / [P(k1)P(k3) + cyclic]
```

For pure dust contraction, this gives f_NL^local = 5/12 exactly.

The ECH bounce correction is of order:
```
δf_NL ~ (k/k_b)²    for  k ≪ k_b
```
which is negligible at CMB scales.

### Deliverable
Document the analytic result and compute numerical corrections from the ECH bounce.

---

## Phase 2c: Low-ℓ Cutoff

### Objective
Predict the IR cutoff in P(k) from finite contraction duration and compare to Planck low-ℓ deficit.

### Method
For a contracting phase that begins at t = -T_contract:
```
k_min = aH|_{t = -T_contract} ≈ (2/3) × a(-T_contract) / T_contract
```
Modes with k < k_min never enter the Hubble radius and have no primordial perturbation.

Map k_min to ℓ_min via:
```
ℓ_min ≈ k_min × D_A(z_rec) ≈ k_min × 14 Gpc
```

If ℓ_min ~ 2–4, this matches the Planck low-quadrupole anomaly. This constrains T_contract.

### Deliverable
`research/branch_V_bounce_evidence/phase1_mcmc/06_lowl_cutoff.py`

---

## Directory Structure

```
research/branch_V_bounce_evidence/
├── 01_program_definition.md
├── 02_observable_channel_map.md
├── 03_minimal_nontransparent_extensions.md
├── 04_upside_matrix.md
├── 05_top3_candidates.md
├── 06_best_single_target.md
├── 07_phase1_blueprint.md
├── final_verdict.md
└── phase1_mcmc/
    ├── 01_background_solver.py
    ├── 02_scalar_perturbations.py
    ├── 03_tensor_perturbations.py
    ├── 04_consistency_relations.py
    ├── 05_spectral_tilt_analysis.py
    └── 06_lowl_cutoff.py
```

---

## Dependencies and Prerequisites

### From existing work
- Branch H tensor solver (template for numerical integration)
- Branch H background solution (ECH bounce analytics)
- Branch K scalar results (baseline T(k) = 1 for symmetric bounce)
- ALP birefringence model (potential spectator field for tilt mechanism)

### External references (key papers)
- Wands (1999): Duality of cosmological perturbations in pre-Big-Bang cosmology
- Finelli & Brandenberger (2002): Matter bounce perturbation theory
- Cai, Qiu, Brandenberger, Piao, Zhang (2008): Non-singular matter bounce
- Cai & Wilson-Ewing (2014): Non-singular matter bounce in LQC
- Quintin, Chen, Brandenberger (2015): Matter bounce with spectral tilt
- de Haro & Cai (2015): Matter bounce in teleparallel gravity (closest analog)

### Tools
- Python 3 with numpy, scipy, matplotlib
- scipy.integrate.solve_ivp (DOP853 method)
- Potential: CLASS/CAMB for transfer function comparison

---

## Go/No-Go Gates

### Gate 1 (after Phase 1a)
Background solver produces smooth a(t) matching all boundary conditions? If NO → debug or reformulate.

### Gate 2 (after Phase 1b)
Scalar perturbations are numerically stable through the bounce? If NO → try alternative variable formulation.

### Gate 3 (after Phase 1b+1c)
Pure matter bounce limit reproduces n_s = 1 and n_T = 0? If NO → there is a bug.

### Gate 4 (after Phase 2a)
At least one tilt mechanism produces n_s ∈ [0.95, 0.98] with ≤ 2 parameters? If YES → proceed to Phase 3. If NO → record negative result, assess V4 (ekpyrotic) as alternative.

### Gate 5 (after Phase 2b)
f_NL = 5/12 is preserved through the ECH bounce to within 10%? If YES → major result. If NO → compute the ECH correction precisely.
