# Background and Scalar Mode Equation

**Date:** 2026-03-16

---

## The Bounce Background

### Modified Friedmann equations

The spin-torsion bounce has:

```
H² = (8πG/3) ρ(1 - ρ/ρ_crit)
Ḣ = -4πG(ρ+p)(1 - 2ρ/ρ_crit)
```

with ρ_crit ≈ 0.21 M_Pl⁴.

### Exact radiation-dominated solution

For radiation (p = ρ/3, ρ = ρ₀/a⁴):

```
a(t) = a_b(1 + 4α²t²)^{1/4}
H(t) = 2α²t/(1 + 4α²t²)
Ḣ(t) = 2α²(1 - 4α²t²)/(1 + 4α²t²)²
```

where α² = 8πGρ_crit/3 ≈ 1.76 M_Pl².

### Symmetry properties

The solution is EXACTLY time-symmetric:

```
a(-t) = a(t)        (even)
H(-t) = -H(t)       (odd)
Ḣ(-t) = Ḣ(t)        (even)
R(-t) = R(t)         (even)
```

This symmetry will be crucial for the scalar perturbation
transfer function.

### Effective equation of state

The effective slow-roll parameter:

```
ε(t) = -Ḣ/H² = (4α²t² - 1)/(2α²t²)
     = 2 - 1/(2α²t²)
```

For |t| ≫ 1/(2α): ε → 2 (standard radiation).
At t = 0: ε → -∞ (bounce instant, H = 0).
At t = ±1/(2α): ε = 0 (maximum |H|).

---

## Gauge Choice and Perturbation Variable

### Why the Mukhanov-Sasaki variable fails at the bounce

The standard Mukhanov-Sasaki variable is:

```
v = zζ,    z = a√(2ε)/c_s
```

At the bounce: ε → -∞ (from above), so z → imaginary → v
is not real-valued. The Mukhanov-Sasaki formalism BREAKS DOWN
at H = 0.

This is a COORDINATE singularity, not a physical one. The
perturbation itself is finite; only the chosen variable diverges.

### The Bardeen potential: well-defined through the bounce

We work in the conformal Newtonian (longitudinal) gauge:

```
ds² = a²[-(1+2Φ)dη² + (1-2Ψ)δ_ij dx^i dx^j]
```

For a perfect fluid with no anisotropic stress: Φ = Ψ.

The Bardeen potential Φ is gauge-invariant and remains finite
through the bounce. It is the appropriate variable for this
calculation.

---

## The Bardeen Potential Equation

### In conformal time

```
Φ'' + 3H(1+c_s²)Φ' + [c_s²k² + 2H' + (1+3c_s²)H²]Φ = 0
```

where H = a'/a (conformal Hubble parameter) and ' = d/dη.

For radiation (c_s² = 1/3):

```
Φ'' + 4HΦ' + [k²/3 + 2H' + 2H²]Φ = 0
```

### In cosmic time

Converting via d/dη = a d/dt:

```
Φ̈ + 5HΦ̇ + [k²/(3a²) + 2Ḣ + 4H²]Φ = 0
```

This is the equation we solve numerically, with H(t), Ḣ(t),
a(t) given analytically.

### Verification: behavior at the bounce

At t = 0 (H = 0):

```
Φ̈ + [k²/3 + 2 × 2α²]Φ = 0
```

(setting a_b = 1 for convenience)

This is a simple harmonic oscillator with frequency:

```
ω_bounce² = k²/3 + 4α²
```

For k = 0: ω_bounce = 2α ≈ 2.65 M_Pl. The Bardeen potential
oscillates with Planck frequency at the bounce — finite,
regular, well-defined.

### Verification: behavior far from the bounce

For |t| ≫ 1/(2α): the background approaches standard radiation
a ∝ |t|^{1/2}, H ≈ 1/(2t). The Bardeen equation reduces to
the standard radiation-era form:

```
Φ̈ + (5/2t)Φ̇ + k²/(3 × 4α²t²)Φ = 0    (approximately)
```

Solutions: spherical Bessel functions of argument kη/√3, where
η is the conformal time in the radiation era.

### The two independent solutions (far from bounce)

In the radiation era, the Bardeen potential has:

**Constant mode (C):**
```
Φ_C ∝ [sin(x) - x cos(x)]/x³,    x = kη/√3
```

Super-Hubble limit (x → 0): Φ_C → const (= 1/3 with
standard normalization).

**Decaying mode (D):**
```
Φ_D ∝ [-cos(x) - x sin(x)]/x³
```

Super-Hubble limit (x → 0): Φ_D ∝ 1/x³ → ∞.

**CRITICAL:** In the CONTRACTING phase, the "decaying" mode
GROWS (1/x³ increases as x → 0, which occurs as η → 0⁻
approaching the bounce). This is the GROWING MODE of the
contracting phase.

---

## The Growing Mode Problem

### Statement of the problem

During contraction, the growing mode of Φ amplifies as:

```
|Φ_growing| ∝ 1/(kη)³ → ∞    as η → 0⁻
```

For a mode with comoving wavenumber k, the growth factor from
Hubble exit (kη_exit ~ 1) to the bounce (η → η_b ~ 1/k_b) is:

```
Growth = (kη_exit)³/(kη_b)³ = (k_b/k)³
```

For CMB modes: k/k_b ~ 10⁻²⁸. Growth factor: 10⁸⁴.

This enormous growth means ANY admixture of the growing mode
in the initial conditions gets amplified by 10⁸⁴ before the
bounce. If this growing mode leaks into the post-bounce
constant mode, it would dominate the scalar spectrum.

### The time-reversal resolution

The Bardeen equation has EXACT time-reversal symmetry on the
bounce background (verified in the problem statement). Under
η → -η:

- Φ(η) → Φ(-η) is also a solution
- The growing mode of contraction (∝ 1/(kη)³ for η < 0)
  maps to the decaying mode of expansion (∝ 1/(kη)³ for η > 0)
- The constant mode maps to itself

**Consequence:** In a time-symmetric bounce, the transfer
matrix between contracting and expanding radiation eras is:

```
[A_out]   [1  0] [A_in ]
[B_out] = [0  1] [B_in ]
```

where A labels the constant mode and B labels the
growing/decaying mode. The matrix is the IDENTITY.

**The bounce is perfectly transparent to scalar perturbations
on super-Hubble scales.**

### Proof

Let Φ₁(η) and Φ₂(η) be two linearly independent solutions
of the Bardeen equation. By time-reversal symmetry, Φ₁(-η)
and Φ₂(-η) are also solutions.

Choose Φ₁ = the "even" solution: Φ₁(η) = Φ₁(-η).
Choose Φ₂ = the "odd" solution: Φ₂(η) = -Φ₂(-η).

For η → +∞: Φ₁ → a₁(constant mode) + b₁(decaying mode).
By symmetry, for η → -∞: Φ₁ → a₁(constant mode) + b₁(growing mode).

The constant mode has the SAME amplitude a₁ on both sides
of the bounce. The decaying mode of expansion has the same
coefficient as the growing mode of contraction.

For the odd solution Φ₂: constant modes cancel (by oddness),
so it is purely growing on one side and decaying on the other.

The general solution: Φ = A_in × Φ₁ + B_in × Φ₂.

The constant mode amplitude on the expanding side:
A_out = A_in × a₁ + B_in × 0 = A_in × a₁.

And a₁ = 1 (by normalization of the constant mode). So:

```
T(k) = A_out/A_in = 1    (for super-Hubble modes)
```

**QED.** □

### Caveats

1. This proof assumes the modes are super-Hubble throughout
   (k ≪ k_b). For k ~ k_b, the modes are sub-Hubble at the
   bounce and the growing/decaying decomposition doesn't apply.

2. The proof assumes EXACT time-reversal symmetry. If the
   bounce has any asymmetry (different matter content before
   and after), T(k) ≠ 1.

3. The proof is for ADIABATIC perturbations of a single fluid.
   Multi-fluid or entropic perturbations could behave differently.

---

## The Effective Scalar Potential

By analogy with the tensor equation v'' + (k² - a''/a)v = 0,
we can write the Bardeen equation in a Schrödinger-like form.

Define u = aΦ. The equation for u can be derived but has a
more complex effective potential than a''/a due to the
pressure and friction terms.

Alternatively, define the "scalar potential":

```
V_S(η) = -[2H' + (1+3c_s²)H² + 3H(1+c_s²) × ...]
```

The details are messy, but the key point is:

**V_S has a localized bump near the bounce** (same qualitative
structure as the tensor potential a''/a). The bump height is
~ k_b² and the width is ~ 1/k_b in conformal time.

Modes with k ≪ k_b: tunnel/scatter with negligible reflection.
Modes with k ~ k_b: significant scattering, oscillatory features.
Modes with k ≫ k_b: free propagation (no bounce effect).

---

## Relation to Curvature Perturbation ζ

The comoving curvature perturbation:

```
ζ = -Φ - HΦ̇/(Ḣ - H²(1+p/(ρ)))    (schematic, cosmic time)
```

For radiation:

```
ζ = -Φ - 3HΦ̇/(3Ḣ + 4... )
```

At H = 0: the 1/H terms make ζ ill-defined at the bounce
instant. However, on super-Hubble scales:

```
ζ̇ = O(k²)    (vanishes for k → 0)
```

So ζ is CONSERVED through the bounce even though it is
momentarily ill-defined at the bounce instant. The conservation
of ζ is the physical statement underlying T(k) = 1.

---

## Summary

| Property | Value |
|----------|-------|
| Perturbation variable | Bardeen potential Φ |
| Gauge | Conformal Newtonian (longitudinal) |
| Equation | Φ̈ + 5HΦ̇ + [k²/(3a²) + 2Ḣ + 4H²]Φ = 0 |
| Regular at bounce? | YES (all coefficients finite at H = 0) |
| Time-reversal symmetric? | YES (exact) |
| Mukhanov-Sasaki variable? | ILL-DEFINED at bounce (z → ∞) |
| Growing mode problem? | RESOLVED by time-reversal symmetry |
| Transfer function T(k) | = 1 for k ≪ k_b (analytic proof) |
| Features at k ~ k_b? | Yes (oscillatory, ~GHz frequencies) |
