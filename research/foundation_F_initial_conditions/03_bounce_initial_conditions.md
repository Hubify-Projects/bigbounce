# Foundation F — Bounce Initial Conditions

**Date:** 2026-03-15

---

## Goal

Estimate the scalar displacement φ_i and velocity φ̇_i at the bounce
for different coupling mechanisms.

---

## Bounce-Era Scales

```
ρ_bounce ~ ρ_crit ~ M_Pl⁴ / (32πκ⁴σ²) ~ M_Pl⁴      [Planck density]
H_bounce = 0                                           [by definition]
Ḣ_bounce > 0                                           [~M_Pl² in magnitude]
R_bounce ~ 32πG ρ_crit ~ M_Pl²                        [from Foundation E]
T_bounce ~ κ² s ~ M_Pl                                 [torsion from spin]
s_bounce ~ n × ℏ/2 ~ M_Pl³                            [spin density at Planck]
Duration: Δt_bounce ~ t_Pl = M_Pl⁻¹
a_bounce = a_min                                        [minimum scale factor]
```

---

## Mechanism 1: Non-Minimal Curvature Coupling

### Action term
```
S ⊃ ½ξ ∫ d⁴x √g R φ²
```

This generates an effective mass at the bounce:
```
m²_eff(bounce) = V''(φ) + ξR_bounce ~ V''(φ) + ξM_Pl²
```

### Displacement estimate

For V(φ) with a minimum at φ = 0 and V''(0) = m₀²:

The curvature term shifts the effective minimum. For a potential
V = ½m₀²φ² + ..., the equilibrium becomes:

```
(m₀² + ξM_Pl²) φ_eq = 0 → φ_eq = 0
```

For a potential like V = V₀ - ½μ²φ² + ... (unstable at origin):
```
(-μ² + ξM_Pl²) φ_eq = 0 → φ_eq = 0 if ξM_Pl² > μ²
```

The curvature STABILIZES the field at φ = 0 during the bounce
(for ξ > 0). After the bounce, as R decreases, the field becomes
unstable and rolls.

### Key insight

The curvature coupling does not DISPLACE the field — it STABILIZES
it. The displacement occurs AFTER the bounce as R → 0 and the
bare potential takes over. The initial condition at the bounce is
φ_i ≈ 0, φ̇_i ≈ 0 (held at the minimum of V_eff).

**For non-minimal curvature coupling: the bounce sets φ_i ≈ 0,
not a displaced value.** The subsequent evolution depends entirely
on the bare potential V(φ), not on the bounce.

### Exception: conformal coupling ξ = 1/6

For ξ = 1/6, the coupling is conformally invariant. In this case,
the field equation becomes:

```
□φ + (1/6)Rφ + V'(φ) = 0
```

On FRW with a(t) = a_min(1 + t²/τ²)^{1/4} near the bounce:

The R(t) pulse acts as a TIME-DEPENDENT MASS. The field oscillates
during the bounce and emerges with a velocity φ̇_i that depends on
the bounce profile. But:

```
φ̇_i ~ R_bounce × φ × Δt_bounce ~ M_Pl² × φ × M_Pl⁻¹ ~ M_Pl φ
```

If φ is already O(M_Pl), then φ̇_i ~ M_Pl². If φ starts at 0,
then φ̇_i = 0 (no kick from a symmetric potential at the origin).

---

## Mechanism 2: Torsion-Scalar Coupling

### Action term
```
S ⊃ g_T ∫ d⁴x √g T² φ²     [or T²φ, or other structure]
```

where T² ≡ T^λ_μν T_λ^μν is the torsion-squared invariant.

### At the bounce

```
T² ~ M_Pl²    [torsion is Planck-scale]
```

The effective potential contribution:
```
V_eff = V(φ) + g_T M_Pl² φ²     [at the bounce]
V_eff = V(φ)                      [after bounce, when T → 0]
```

Same analysis as Mechanism 1: the torsion coupling STABILIZES φ at
the bounce (if g_T > 0) and releases it afterward. The initial
condition is φ_i ≈ 0.

### Torsion-scalar derivative coupling

```
S ⊃ α ∫ d⁴x √g T_μ (∂^μ φ)
```

where T_μ = T^λ_μλ is the torsion trace. At the bounce:

```
T_μ ~ (M_Pl, 0, 0, 0)    [time component, from homogeneous spin]
```

This generates a FORCE on φ:

```
φ̈ + 3Hφ̇ + V'(φ) = α Ṫ₀ ~ α M_Pl/t_Pl = α M_Pl²
```

The induced displacement over Δt ~ t_Pl:

```
δφ ~ ½ α M_Pl² × t_Pl² = ½ α M_Pl² / M_Pl² = α/2
```

For α ~ O(1): δφ ~ M_Pl (in Planck units, so δφ ~ 1).
For α ~ 1/M_Pl (gravitational strength): δφ ~ 1/M_Pl.

**With torsion derivative coupling: δφ ~ α × O(M_Pl) at best.
The displacement is Planck-scale if α ~ 1, or gravitationally
suppressed if α ~ 1/M_Pl.**

---

## Mechanism 3: Spin Density Sourcing

### Action term
```
S ⊃ (g_s/M_Pl²) ∫ d⁴x √g (s^μ s_μ) φ
```

where s^μ is the spin density 4-vector.

### At the bounce

```
s² ~ M_Pl⁶    [spin density squared at Planck density]
```

Force on φ:
```
V'_eff = V'(φ) + g_s M_Pl⁶/M_Pl² = V'(φ) + g_s M_Pl⁴
```

Displacement:
```
δφ ~ g_s M_Pl⁴ × t_Pl² / (effective mass)
```

For a massless field during the bounce (m ≪ M_Pl):
```
δφ ~ g_s M_Pl⁴ / M_Pl² = g_s M_Pl²
```

For g_s ~ 1: δφ ~ M_Pl².

**The displacement is Planck-scale or larger.** This is the generic
conclusion for any coupling to bounce-era quantities.

---

## General Result

### All mechanisms give φ_i ~ O(M_Pl) or φ_i ~ 0

There are only two outcomes:

**Case 1: Strong coupling to bounce-era quantities.**
The force on φ is Planck-scale. The displacement is δφ ~ M_Pl or
larger. The field is thrown to Planck-scale field values.

**Case 2: Stabilizing coupling.**
The coupling creates an effective mass ~ M_Pl at the bounce. The
field is held at φ = 0 during the bounce and released afterward.
φ_i ≈ 0.

**Case 3: Gravitational-strength coupling.**
The force is suppressed by 1/M_Pl². The displacement is δφ ~ O(1)
in Planck units, or δφ ~ M_Pl in natural units.

In all cases: **φ_i is either O(M_Pl) or O(0).** There is no
mechanism to set φ_i to a specific intermediate value like
10⁻³⁰ M_Pl or 10⁻⁶⁰ M_Pl.

### The DE-relevant scale

Dark energy requires:
```
V(φ_today) ~ 10⁻¹²² M_Pl⁴
```

For a power-law potential V = M^{4+α}/φ^α:
```
φ_today ~ (M^{4+α}/ρ_DE)^{1/α}
```

For V = ½m²φ²: φ_today = √(2ρ_DE)/m.

The DE-relevant field value depends on the POTENTIAL parameters
(M, α, m), not on the initial conditions — because attractor
dynamics bring the field to the tracker regardless of φ_i (for
tracker potentials) or because the field sits near a special
point regardless of φ_i (for hilltop potentials, which require
separate fine-tuning).

---

## Summary of Initial Condition Estimates

| Mechanism | φ_i | φ̇_i | Predictive? |
|-----------|-----|------|------------|
| Non-minimal curvature (stabilizing) | ~0 | ~0 | No — generic starting point |
| Conformal coupling ξ=1/6 | ~0 (or O(M_Pl)) | ~M_Pl φ_i | No — depends on pre-bounce state |
| Torsion-scalar coupling | ~0 (stabilizing) | ~0 | No — generic starting point |
| Torsion derivative coupling | ~αM_Pl | ~αM_Pl² | Partially — but α is free |
| Spin density sourcing | ~g_s M_Pl² | ~g_s M_Pl³ | Partially — but g_s is free |

**No mechanism produces a SPECIFIC, PREDICTIVE initial condition
that differs from what any generic high-energy epoch would provide.**

The bounce gives φ_i ~ O(M_Pl) or φ_i ~ 0. Any high-curvature epoch
(inflation, Planck era, bounce) gives the same generic result. The
initial condition is bounce-COMPATIBLE but not bounce-SPECIFIC.
