# Phase 2 — Sequestering Equation

**Date:** 2026-03-15

---

## The Self-Consistency Equation

From sequestering:
```
Λ_residual = μ⁴ / V₄(Λ)
```

With V₄(Λ) computed from the cyclic model:
```
Λ = μ⁴ / V₄(Λ)
```

This is a self-consistency equation: Λ appears on both sides.

---

## Graphical Analysis

### V₄(Λ) behavior (closed universe, matter + Λ)

From Task 2:
- V₄(Λ = 0) = V₄⁰ ~ a_max(0)⁴ (finite, determined by matter alone)
- V₄(Λ) increases monotonically as Λ increases (larger a_max)
- V₄(Λ) → ∞ as Λ → Λ_crit (universe approaches Einstein static)
- V₄(Λ) is undefined for Λ > Λ_crit (no cycle exists)

### Rewriting the equation

```
Λ × V₄(Λ) = μ⁴
```

Define F(Λ) ≡ Λ × V₄(Λ). The solution is F(Λ) = μ⁴.

### Behavior of F(Λ)

- F(0) = 0 (Λ = 0 gives zero)
- F(Λ) increases initially (both Λ and V₄ increase)
- As Λ → Λ_crit: V₄ → ∞, so F → ∞
- F is continuous and monotonically increasing on [0, Λ_crit)

Since F(0) = 0 and F(Λ → Λ_crit) → ∞, by the intermediate value
theorem:

**For ANY μ⁴ > 0, there exists exactly one Λ* ∈ (0, Λ_crit) such
that F(Λ*) = μ⁴.**

### Solution structure

The equation Λ = μ⁴/V₄(Λ) has a UNIQUE solution for each μ⁴ > 0.

This means:
- The solution is NOT discrete. It is a continuous one-parameter
  family parametrized by μ⁴.
- For each μ⁴, there is exactly one Λ*. Changing μ⁴ changes Λ*.
- The solution Λ*(μ⁴) is a monotonically increasing function of μ⁴:
  larger μ⁴ → larger Λ*.

---

## Does the Equation Yield Unique Λ?

**No — Λ is uniquely determined GIVEN μ⁴, but μ⁴ is free.**

The self-consistency equation converts the parameter μ⁴ into Λ.
But μ⁴ itself is not determined by the mechanism. It is a free
parameter in the sequestering action.

This is the same situation as in Foundation E Phase 1: sequestering
produces Λ_residual as a function of its internal parameters, but
those parameters are free.

### Explicit Λ*(μ⁴) estimate

For small Λ (Λ ≪ Λ_crit): V₄ ≈ V₄⁰ + V₄'(0)Λ + ... ≈ V₄⁰ (weakly dependent on Λ).

Then:
```
Λ ≈ μ⁴/V₄⁰
```

For V₄⁰ ~ a_max(0)⁴ and a_max determined by matter content:

```
a_max ~ (4πG ρ_m)^{1/3} / k^{1/2}    [closed matter universe]
```

So:
```
Λ ~ μ⁴ / a_max⁴ ~ μ⁴ k² / (4πGρ_m)^{4/3}
```

For Λ ~ 10⁻¹²² M_Pl⁴ and a_max ~ 10²⁶ m ~ 10⁶¹ M_Pl⁻¹:

```
μ⁴ ~ Λ × V₄⁰ ~ 10⁻¹²² M_Pl⁴ × (10⁶¹)⁴ M_Pl⁻⁴
   ~ 10⁻¹²² × 10²⁴⁴ M_Pl⁰
   ~ 10¹²² [dimensionless in appropriate units]
```

Wait — units need care. In natural units:
```
V₄ ~ a_max⁴ [in length⁴ = mass⁻⁴]
Λ [in mass²]
μ⁴ = Λ V₄ [in mass² × mass⁻⁴ = mass⁻²]
```

This doesn't have the right dimensions for μ as a mass. The issue
is that the sequestering action has specific normalization. In
Kaloper-Padilla:

```
σ₁[Λ V₄/μ₁⁴ - 1] = 0 → Λ = μ₁⁴/V₄
```

Here μ₁⁴ has dimensions of [mass⁴ × length⁴] = [mass⁴ × mass⁻⁴]
= dimensionless. Actually in natural units (ℏ = c = 1):
[V₄] = [length⁴] = [mass⁻⁴]. [Λ] = [mass⁴] (energy density).
So [μ₁⁴] = [Λ × V₄] = [mass⁴ × mass⁻⁴] = dimensionless.

So μ₁⁴ is a DIMENSIONLESS number.

```
μ₁⁴ = Λ_obs × V₄
     ~ (10⁻¹²² M_Pl⁴) × (a_max⁴)
     ~ 10⁻¹²² M_Pl⁴ × (10⁶¹/M_Pl)⁴
     ~ 10⁻¹²² × 10²⁴⁴
     ~ 10¹²²
```

So μ₁⁴ ~ 10¹²² — a large dimensionless number. This is the
Kaloper-Padilla version of the CC problem: why is μ₁⁴ so large
(or equivalently, why is Λ so small given V₄)?

---

## Does the Equation Yield Discrete Solutions?

**No.** F(Λ) = Λ × V₄(Λ) is a smooth, monotonically increasing
function. For each μ⁴, there is exactly one root. No discreteness
emerges from the self-consistency equation itself.

Discreteness could arise if:
1. μ⁴ is quantized (but there is no reason for this in sequestering)
2. V₄ has discontinuities (but V₄ is a smooth functional of the
   cosmological evolution)
3. Additional constraints impose selection among solutions (but no
   such constraints have been identified)

**The solution is a continuous one-parameter family parametrized
by μ⁴.**

---

## Summary

| Question | Answer |
|----------|--------|
| Unique Λ for given μ⁴? | YES (unique root of F(Λ) = μ⁴) |
| μ⁴ determined? | NO (free parameter) |
| Discrete solutions? | NO (continuous family) |
| Λ range? | (0, Λ_crit) for μ⁴ ∈ (0, ∞) |
| μ⁴ needed for Λ_obs? | μ⁴ ~ 10¹²² (large dimensionless number) |

**The self-consistency equation does not determine Λ. It maps the
free parameter μ⁴ to Λ one-to-one. The CC problem is repackaged as
"why is μ⁴ ~ 10¹²²?" — which is the same question in different
notation.**
