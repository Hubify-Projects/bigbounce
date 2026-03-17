# Toy Model Map for UV→IR Bridge Candidates

**Date:** 2026-03-16

---

## Toy Model 1: PGT Lower-Scale Bounce (Candidate A)

### Setup

Poincaré gauge theory with propagating torsion. The gravitational
Lagrangian includes torsion kinetic and mass terms:

```
L = (M_Pl²/2) R + α₁ T_μνρ T^μνρ + α₂ T_μνρ T^νμρ + α₃ T_μ T^μ
    + β₁ R_μνρσ R^μνρσ + β₂ R_μνρσ R^ρσμν + β₃ R_μν R^μν + ...
```

where T_μνρ is the torsion tensor and R_μνρσ is the full
Riemann-Cartan curvature.

### Minimal toy version

Keep only the torsion trace mode T_μ (spin-0 torsion, vector part):

```
L = (M_Pl²/2) R - (1/4) F_μν F^μν + (m_T²/2) T_μ T^μ + g_T T_μ J^μ
```

where F_μν = ∂_μ T_ν - ∂_ν T_μ is the torsion field strength
and J^μ is the fermion axial current.

### Modified Friedmann equation

With propagating torsion, the effective energy density that sources
the bounce is modified:

```
H² = (8πG/3)(ρ_rad + ρ_torsion - ρ_total²/ρ_crit^{eff})
```

where ρ_crit^{eff} depends on the PGT parameters:

```
ρ_crit^{eff} ~ m_T² M_Pl²  (parametric estimate)
```

For the full expression, define:
```
κ₁ = α₁ + α₂/2,  κ₂ = α₃ + α₁/2
ρ_crit^{eff} = M_Pl⁴ / (1 + M_Pl²/κ₁)  ≈  κ₁ M_Pl²  for κ₁ ≪ M_Pl²
```

Setting κ₁ ~ m_T² (the torsion mass squared), we recover
ρ_crit ~ m_T² M_Pl².

### Bounce feature frequency

```
f_b = T₀ × (ρ_crit^{eff})^{1/4} / M_Pl
    = T₀ × (m_T M_Pl)^{1/2} / M_Pl
    = T₀ × (m_T / M_Pl)^{1/2}
```

| m_T (GeV) | f_b (Hz) | Band |
|-----------|---------|------|
| 10⁹ | ~1 | LIGO/ET |
| 10⁷ | ~0.1 | LIGO/ET |
| 10⁵ | ~0.01 | LISA |
| 10³ | ~10⁻³ | LISA |
| 10¹ | ~10⁻⁴ | LISA/sub-LISA |
| 10⁻¹ | ~10⁻⁵ | Sub-LISA |

### Tensor spectrum through PGT bounce

The tensor power spectrum acquires oscillatory features at k ~ k_b:

```
P_T(k) = P_T^{smooth}(k) × [1 + A_osc sin(k/k_b + φ)]
```

where A_osc depends on the bounce profile (sharper bounce → larger
oscillations) and k_b = a_b × (ρ_crit^{eff})^{1/2} / M_Pl.

For the toy model, the amplitude of oscillations:

```
A_osc ~ (Δt_bounce × k_b)⁻¹ ~ O(1) near k ~ k_b
```

(The bounce is sharp, so oscillations are prominent at k ~ k_b.)

### Constraint from Foundation A

The mass-coupling lock from Foundation A:

```
g_eff ~ 1 / (M_Pl √|t₃|)
```

where t₃ is a dimensionless PGT parameter. This constrains the
(m_T, g_T) parameter space. Specifically:

- For m_T ~ 10⁵ GeV: need |t₃| ~ (M_Pl/m_T)² ~ 10²⁸
- This requires a large hierarchy in the PGT parameters
- No known symmetry protects this hierarchy

### Key question for Phase 2
Is there a region of PGT parameter space where:
1. ρ_crit^{eff} is in the LISA/LIGO band (m_T ~ 10³–10⁹ GeV)
2. The mass-coupling lock is satisfied
3. The torsion sector is ghost-free and stable
4. The GW signal amplitude exceeds detector sensitivity

---

## Toy Model 2: Torsion-Curvaton (Candidate E)

### Setup

PGT with propagating torsion, where the torsion trace T_μ (or the
axial torsion pseudoscalar mode) acts as a curvaton during the
contraction phase.

### Effective scalar description

In the FRW reduction, the torsion trace T₀(t) behaves as a massive
scalar field τ(t):

```
L_eff = (1/2) τ̇² - (1/2) m_T² τ² + g_T τ n₅(t)
```

where n₅ is the fermion number density (axial current source).

### Perturbation spectrum during contraction

During contraction, if m_T < H(t_exit) at the time modes exit the
Hubble radius:

```
δτ_k ~ H_exit / (2π)    (light field, nearly scale-invariant)
P_τ(k) ~ (H_exit / 2π)²
```

After the bounce, τ oscillates and decays to radiation. The
curvaton conversion:

```
ζ = (2/3) × (ρ_τ / ρ_total) × (δτ / τ̄)  at decay
```

### Spectral index

```
n_s - 1 = 2 d ln H_exit / d ln k
```

For a radiation-dominated contraction (a ∝ (-η)):
```
H ∝ 1/η²,  k ~ aH  →  n_s - 1 ≈ -4  (too red!)
```

For a matter-dominated contraction (a ∝ (-η)²):
```
H ∝ 1/η³,  k ~ aH  →  n_s - 1 ≈ 0  (scale-invariant)
```

Getting n_s ≈ 0.965 requires a contraction with w slightly > 0:
```
n_s - 1 = -2(1 + 3w)/(1 + 3w/2)  →  w ≈ 0.006 for n_s = 0.965
```

### Bounce-specific vs generic

The curvaton mechanism works with ANY bounce. The torsion-specific
aspects:

1. **Natural presence:** Torsion is the geometric degree of freedom
   of EC/PGT gravity. No ad hoc scalar needed.

2. **Mass from geometry:** m_T is determined by PGT Lagrangian
   parameters, not a free parameter.

3. **Coupling from geometry:** g_T is the torsion-fermion coupling,
   geometrically determined.

4. **Foundation A constraint:** The mass-coupling lock constrains
   the viable (m_T, g_T) space.

### Key question for Phase 2
Can the torsion curvaton produce n_s ≈ 0.965 with parameters
consistent with the mass-coupling lock?

---

## Toy Model 3: Time-Asymmetric Bounce (Candidate C)

### Setup

The contracting phase is matter-dominated (w = 0), the expanding
phase is radiation-dominated (w = 1/3). The bounce connects them.

### Scale factor

```
Contracting:  a(η) = a_b (η/η_b)²    for η < -η_b
Bounce:       a(η) = a_b [1 + (η/η_b)²]^{1/2}    near η = 0
Expanding:    a(η) = a_b (η/η_b)       for η > η_b
```

(Schematic; the exact interpolation through the bounce is model-
dependent.)

### Scalar perturbation transfer

The growing mode in matter contraction:
```
Φ_grow ∝ const.    (constant Bardeen potential)
```

In radiation expansion:
```
Φ_const ∝ cos(kη/√3) / (kη)²
Φ_decay ∝ sin(kη/√3) / (kη)²
```

The asymmetry (w changes across bounce) means the transfer
function T(k) ≠ 1:

```
T(k) = Φ_out / Φ_in = α(k) + β(k) × (decaying/constant)
```

For k ≪ k_b: T → 1 (long wavelengths unaffected)
For k ~ k_b: T has oscillatory features
For k ≫ k_b: T depends on bounce profile details

### Predictions

```
n_s = 1           (matter contraction → scale-invariant)
r = 16/ε ~ O(1)   (matter bounce generic)
```

Both are problematic:
- n_s = 1 excluded at 8σ by Planck (n_s = 0.965 ± 0.004)
- r ~ O(1) excluded by r < 0.03

### Fixes needed
- n_s < 1: requires tilt mechanism (potential curvature, running)
- r < 0.03: requires tensor suppression (curvaton, ekpyrotic
  contraction phase)

### BKL instability

In matter contraction, anisotropy grows as:
```
σ²/ρ ∝ a⁻⁶/a⁻³ = a⁻³  →  grows without bound
```

The universe becomes anisotropic before reaching the bounce
unless initial conditions are extremely isotropic. This is
the Belinski-Khalatnikov-Lifshitz (BKL) instability.

### Verdict preview: MODERATE (fixable but requires additional
ingredients beyond minimal model)

---

## Toy Model 4: Bounce + Brief Inflation (Candidate B)

### Setup

A scalar field φ with a flat potential near φ = φ_b is displaced
from its minimum by curvature coupling during the bounce:

```
L = (1/2)(∂φ)² - V(φ) + (1/2)ξRφ²
```

### Dynamics

1. **Pre-bounce:** φ sits at φ = 0 (minimum). R ~ 0 in radiation
   domination.

2. **At bounce:** R spikes to R_max ~ 12α² ~ 21 M_Pl². The
   coupling ξRφ² displaces φ:
   ```
   δφ ~ ξ R_max φ_0 / m_φ²    (if adiabatic)
   δφ ~ ξ R_max t_bounce²      (if impulsive)
   ```

3. **Post-bounce:** If δφ lands on a flat region of V(φ), the
   field slow-rolls for N e-folds:
   ```
   N ~ (3H_inf² / |V''|) ln(φ_initial / φ_end)
   ```

4. **Inflation ends:** φ rolls to its minimum, reheats, standard
   hot Big Bang continues.

### The e-fold problem

For CMB observability, need N ≥ 60. The inflationary predictions
(n_s, r) are determined by V(φ), NOT by the bounce:

```
n_s ≈ 1 - 2/N ~ 0.967    (for N = 60)
r ≈ 12/N² ~ 0.003         (for N = 60, quadratic potential)
```

The bounce's contribution to the initial displacement is:
```
δφ/M_Pl ~ ξ × O(1)
```

For ξ ~ O(1), the displacement is Planckian. For ξ ≪ 1, the
displacement is sub-Planckian and N may be insufficient.

### Bounce-imprint on inflationary observables

Pre-inflationary bouncing modifies the Bunch-Davies vacuum.
The correction to the power spectrum:

```
ΔP_S/P_S ~ exp(-2N)    (exponentially suppressed)
```

For N = 60: ΔP_S/P_S ~ 10⁻⁵² (undetectable).

### Verdict preview: FAIL_JUST_INFLATION
The predictions are those of inflation. The bounce is decorative.

---

## Toy Model 5: Bounce-Triggered Phase Transition (Candidate F)

### Setup

The universe cools from T_bounce ~ ρ_crit^{1/4} ~ 0.68 M_Pl
after the bounce. As it passes through T_GUT ~ 10¹⁶ GeV, a
GUT phase transition occurs.

### Bounce modification

In standard cosmology, the GUT phase transition occurs during
radiation expansion from the initial singularity. In the bounce
model, it occurs during radiation expansion from the bounce.

The bounce provides global causal connection (H = 0 at the bounce
→ infinite Hubble radius → all points causally connected). This
could affect:

1. **Correlation length at transition:**
   Standard: ξ ~ 1/T_GUT
   Bounce: ξ potentially larger (causally connected at bounce)

2. **Defect density:**
   Kibble mechanism: n_defect ~ 1/ξ³
   If ξ is larger, fewer defects form.

### Quantitative estimate

The causal horizon at T_GUT in the bounce model:

```
d_H(T_GUT) ~ t_GUT ~ M_Pl / T_GUT²
```

This is the SAME as in standard cosmology (the bounce is long
forgotten by T_GUT). The bounce's causal connection is at T ~ T_Pl,
not T ~ T_GUT.

The correction:
```
Δn_defect / n_defect ~ (T_GUT / T_bounce)⁴ ~ 10⁻¹²
```

(Negligible.)

### Verdict preview: FAIL_NOT_BOUNCE_SPECIFIC

The phase transition physics is standard. The bounce correction
is suppressed by (T_transition / T_bounce)⁴ ~ 10⁻¹².

---

## Toy Model Summary

| Model | Observable | Amplitude estimate | Viable? |
|-------|-----------|-------------------|---------|
| 1: PGT lower scale | GW spectral features | Detector-band if m_T ~ 10³–10⁹ GeV | **YES** (if lock permits) |
| 2: Torsion-curvaton | CMB scalar spectrum | n_s calculable | **CONDITIONAL** (needs contraction model) |
| 3: Asymmetric bounce | CMB scalars + tensors | n_s = 1, r ~ O(1) | **PROBLEMATIC** (n_s, r excluded) |
| 4: Bounce + inflation | CMB (inflationary) | Standard inflation | **NO** (bounce decorative) |
| 5: Phase transition | Relic densities | Correction ~ 10⁻¹² | **NO** (negligible) |

### Models NOT given toy treatment (killed at screening)

- **Candidate D (generic curvaton):** Same as Toy Model 2 but with
  an arbitrary scalar instead of torsion. Less motivated, not
  bounce-specific.

- **Candidate G (cyclic):** Requires a turnaround mechanism not
  provided by EC gravity. The cyclic framework is a separate
  research program, not a minimal extension.
