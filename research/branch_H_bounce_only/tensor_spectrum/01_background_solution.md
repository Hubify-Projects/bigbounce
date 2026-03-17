# Background Solution for Spin-Torsion Bounce

**Date:** 2026-03-15

---

## Modified Friedmann Equation

The spin-torsion bounce modifies the Friedmann equation:

```
H² = (8πG/3)(ρ - ρ²/ρ_crit)
```

where ρ_crit is the critical density set by the spin-torsion
coupling:

```
ρ_crit = 8 ρ_Pl / (3 κ_s²) ≈ 0.21 M_Pl⁴
```

## Assumptions

1. **Radiation domination** near the bounce: ρ ∝ a⁻⁴
2. **Flat spatial sections:** k = 0
3. **No cosmological constant** (Λ negligible at bounce energy)
4. **Symmetric bounce:** contraction is time-reverse of expansion

With these assumptions:

```
ρ = ρ_crit (a_b/a)⁴
```

where a_b is the scale factor at the bounce minimum.

---

## Exact Solution in Cosmic Time

### Derivation

Define x = a/a_b and α² = 8πGρ_crit/3. Then:

```
H² = α²(x⁻⁴ - x⁻⁸)
```

Substituting ξ = x⁴ = (a/a_b)⁴:

```
H = ȧ/a  →  ξ̇ = 4aH·a³/a_b⁴ = 4a⁴H/a_b⁴ = 4ξH
```

```
ξ̇² = 16ξ²H² = 16α²(ξ⁻¹ - ξ⁻²)ξ² = 16α²(ξ - 1)
```

This gives ξ̇ = 4α√(ξ - 1), which integrates to:

```
ξ - 1 = 4α²t²    (setting t_bounce = 0)
```

Therefore:

```
┌─────────────────────────────────────────────┐
│                                             │
│   a(t) = a_b (1 + 4α²t²)^{1/4}            │
│                                             │
│   where α² = 8πGρ_crit/3 ≈ 1.76 M_Pl²     │
│                                             │
└─────────────────────────────────────────────┘
```

### Verification

At t = 0: a = a_b ✓

```
ȧ = a_b × (1/4)(1+4α²t²)^{-3/4} × 8α²t = 2α²t × a_b(1+4α²t²)^{-3/4}
```

```
H = ȧ/a = 2α²t/(1+4α²t²)
```

At t = 0: H = 0 ✓

Check Friedmann equation:
```
H² = 4α⁴t²/(1+4α²t²)²
```

```
α²(ρ/ρ_crit)(1 - ρ/ρ_crit) = α²(1+4α²t²)⁻¹[1-(1+4α²t²)⁻¹]
= α² × 4α²t² / (1+4α²t²)² = 4α⁴t²/(1+4α²t²)² ✓
```

---

## Hubble Parameter

```
H(t) = 2α²t / (1 + 4α²t²)
```

Properties:
- H(0) = 0 (bounce)
- H → 1/(2t) as t → ∞ (standard radiation)
- Maximum |H| at t = 1/(2α): H_max = α/2

---

## Time Derivative of Hubble Parameter

```
Ḣ(t) = 2α²(1 - 4α²t²) / (1 + 4α²t²)²
```

Properties:
- Ḣ(0) = 2α² > 0 (expanding from bounce) ✓
- Ḣ = 0 at t = 1/(2α) (transition from acceleration to deceleration)
- Ḣ → -1/(2t²) as t → ∞ (standard radiation deceleration) ✓

---

## Conformal Time

Define conformal time η by dt = a dη. Then:

```
dη = dt / a(t) = dt / [a_b(1+4α²t²)^{1/4}]
```

This integral has no closed-form expression. Numerically:

```
η(t) = (1/a_b) ∫₀ᵗ dt' (1+4α²t'²)^{-1/4}
```

Near the bounce (4α²t² ≪ 1):
```
η ≈ t/a_b
```

Far from bounce (4α²t² ≫ 1):
```
a ≈ a_b(2α|t|)^{1/2} ∝ |t|^{1/2}  (standard radiation)
η ≈ (2/a_b)(t/(2α))^{1/2} = (2t)^{1/2}/(a_b(2α)^{1/2})
```

This gives a ∝ η in the radiation-dominated limit, as expected.

---

## Effective Potential a''/a

The tensor perturbation equation involves a''/a where primes
denote conformal time derivatives.

Using the identity:

```
a''/a = a²(Ḣ + 2H²)
```

Compute:

```
Ḣ + 2H² = 2α²(1-4α²t²)/(1+4α²t²)² + 8α⁴t²/(1+4α²t²)²
         = [2α² - 8α⁴t² + 8α⁴t²]/(1+4α²t²)²
         = 2α²/(1+4α²t²)²
```

Therefore:

```
┌──────────────────────────────────────────────────────┐
│                                                      │
│   a''/a = 2α²a_b² / (1 + 4α²t²)^{3/2}             │
│                                                      │
│   Peak value:  (a''/a)_max = 2α²a_b²  at t = 0     │
│                                                      │
└──────────────────────────────────────────────────────┘
```

Key properties:

| Property | Value |
|----------|-------|
| Maximum of a''/a | 2α²a_b² ≈ 3.52 M_Pl² a_b² |
| Width (FWHM in cosmic time) | Δt ~ 0.64/α ~ 0.48 M_Pl⁻¹ |
| Sign | ALWAYS POSITIVE (potential barrier) |
| Asymptotic behavior | → 0 as t → ±∞ (radiation: a''/a = 0) |

**Critical observation:** For pure radiation domination (without
bounce), a''/a = 0 EXACTLY (since a ∝ η → a'' = 0). The bounce
creates a LOCALIZED positive potential bump that exists ONLY during
the bounce transition.

---

## Characteristic Bounce Scale

The potential bump defines a characteristic comoving wavenumber:

```
k_b² = (a''/a)_max = 2α²a_b²
```

```
k_b = a_b√2 α ≈ 1.88 a_b M_Pl
```

Physical momentum at the bounce: k_b/a_b = √2 α ≈ 1.88 M_Pl
(Planck scale).

Modes with k ≪ k_b are strongly affected by the bounce.
Modes with k ≫ k_b pass through the bounce unaffected.

---

## Physical Frequency Today

Using entropy conservation (g_{s,b} = 106.75, g_{s,0} = 3.91,
T_b ≈ 0.68 M_Pl, T_0 = 2.35 × 10⁻⁴ eV):

```
a_b/a_0 = (g_{s,0}/g_{s,b})^{1/3} × T_0/T_b ≈ 9.3 × 10⁻³³
```

The characteristic frequency today:

```
f_b = k_b/(2π a_0) = 1.88 × a_b M_Pl / (2π a_0)
    ≈ 1.88 × 9.3 × 10⁻³³ × 1.22 × 10¹⁹ GeV / (2π)
    ≈ 8 × 10⁹ Hz
    ≈ 8 GHz
```

**The characteristic bounce frequency is ~10 GHz** — in the
microwave range, far above all current gravitational wave
detector bands.

---

## Summary of Background

| Quantity | Expression | Value at bounce |
|----------|-----------|----------------|
| a(t) | a_b(1+4α²t²)^{1/4} | a_b |
| H(t) | 2α²t/(1+4α²t²) | 0 |
| ρ(t) | ρ_crit/(1+4α²t²) | ρ_crit ≈ 0.21 M_Pl⁴ |
| Ḣ(t) | 2α²(1-4α²t²)/(1+4α²t²)² | 2α² ≈ 3.52 M_Pl² |
| a''/a | 2α²a_b²/(1+4α²t²)^{3/2} | 2α²a_b² |
| k_b | a_b√2α | ~ a_b × 1.88 M_Pl |
| f_b (today) | — | ~ 8 GHz |
