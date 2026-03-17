# Phase 2 — Scale Hierarchy Test

**Date:** 2026-03-15

---

## Scales in the Problem

| Scale | Value | Origin |
|-------|-------|--------|
| Bounce curvature | R_bounce ~ M_Pl² ~ 10⁶⁶ eV² | Spin-torsion dynamics |
| Bounce density | ρ_crit ~ M_Pl⁴ ~ 10⁷⁶ GeV⁴ | Spin-torsion critical density |
| Matter energy | ρ_m,0 ~ 10⁻⁴⁷ GeV⁴ | Observed matter density today |
| DE density | ρ_Λ ~ 10⁻⁴⁷ GeV⁴ | Observed dark energy density |
| Λ | ~ 10⁻¹²² M_Pl⁴ | Observed cosmological constant |
| μ₁⁴ | ~ Λ × V₄ ~ 10¹²² (dimensionless) | Required sequestering parameter |
| a_max | ~ 10⁶¹ M_Pl⁻¹ (if cycle exists) | Turnaround scale factor |
| V₄ per cycle | ~ a_max⁴ ~ 10²⁴⁴ M_Pl⁻⁴ | Four-volume |

---

## Does a Natural Hierarchy Emerge?

### The bounce provides ONE scale: M_Pl

All bounce-era quantities are O(M_Pl^n):
- R_bounce ~ M_Pl²
- ρ_crit ~ M_Pl⁴
- T_bounce ~ M_Pl (torsion)
- s_bounce ~ M_Pl³ (spin density)
- Δt_bounce ~ M_Pl⁻¹

### DE requires a SEPARATE scale: 10⁻³⁰ M_Pl

```
ρ_Λ^{1/4} ~ 10⁻³ eV ~ 10⁻³⁰ M_Pl
```

### The gap

```
M_Pl / ρ_Λ^{1/4} ~ 10³⁰
(M_Pl)⁴ / ρ_Λ ~ 10¹²²
```

No mechanism in this program generates this hierarchy. The gap
persists regardless of the approach:

| Approach | Where the gap appears |
|----------|---------------------|
| Local torsion DE (A) | m_torsion vs H₀ |
| Pseudoscalar (B) | Λ² vs M_Pl f |
| Scalar-tensor (C) | m_eff vs H₀ |
| Disformal (D) | H/M_Pl ~ 10⁻⁶⁰ |
| Volume integrals (E) | V₄^bounce / V₄^total |
| Initial conditions (F) | V(φ_i) vs ρ_DE |
| Sequestering (G) | μ₁⁴ ~ 10¹²² |

**The 10¹²² hierarchy appears in EVERY formulation.** It is the
cosmological constant problem, which is not solved by any tested
mechanism.

---

## Can the Bounce + Sequestering Combination Produce μ₁ Naturally?

### What would be needed

A natural μ₁ would satisfy:
```
μ₁⁴ ~ O(1) × (known physics scales)
```

From Λ = μ₁⁴/V₄:
```
μ₁⁴ = Λ × V₄ ~ 10⁻¹²² M_Pl⁴ × 10²⁴⁴ M_Pl⁻⁴ = 10¹²²
```

For μ₁⁴ to be natural (O(1)), we would need V₄ ~ 1/Λ ~ 10¹²² M_Pl⁻⁴.
But V₄ ~ a_max⁴ ~ 10²⁴⁴ M_Pl⁻⁴. So V₄ is 10¹²² times too large
for μ₁ ~ O(1).

Alternatively: μ₁ is a mass scale. If μ₁ ~ M_Pl:
```
μ₁⁴ ~ M_Pl⁴     [but μ₁⁴ is dimensionless in the KP convention]
```

Actually, let me reconsider the dimensions. In the KP action:
```
σ₁[Λ V₄/μ₁⁴ - 1] = 0
```

[Λ] = mass⁴, [V₄] = mass⁻⁴, [σ₁] = dimensionless, so [μ₁⁴] = dimensionless.

But KP define μ₁ as a mass scale through their specific normalization.
In their convention: μ₁ has dimensions of mass, and μ₁⁴ absorbs the
factor from the integral.

Regardless of conventions: the NUMBER that must be tuned is:

```
Λ_obs × V₄ = (small number) × (huge number) = 10¹²²
```

This requires either:
- μ₁ tuned to produce 10¹²²
- OR a mechanism that generates 10¹²² from O(1) quantities

No such mechanism has been identified.

---

## The Scale Hierarchy as a Structural Feature

The 10¹²² gap is not an accident of the sequestering formulation.
It reflects a PHYSICAL fact:

```
Number of Planck volumes in a cosmological cycle ~ (a_max/l_Pl)⁴ ~ 10²⁴⁰
```

```
Λ in Planck units ~ 10⁻¹²²
```

```
Product ~ 10²⁴⁰ × 10⁻¹²² ~ 10¹¹⁸ [not exactly 10¹²², depends on details]
```

The huge number of Planck volumes in a cosmological cycle TIMES
the tiny cosmological constant always produces a large number.
This is because the universe is 10⁶⁰ times the Planck length in
each spatial direction and 10⁶⁰ Planck times old.

**The bounce does not help because the hierarchy is set by the SIZE
of the universe, not by the BOUNCE.**

---

## Summary

| Question | Answer |
|----------|--------|
| Does a natural hierarchy emerge? | NO |
| Does the bounce provide the DE scale? | NO (provides only M_Pl) |
| Is μ₁ natural? | NO (μ₁⁴ ~ 10¹²²) |
| Could any bounce mechanism generate 10¹²²? | Not identified |
| Is the hierarchy avoidable? | NO — it is the CC problem |

**The scale hierarchy test confirms that cyclic sequestering with
a spin-torsion bounce does not generate a natural cosmological
constant. The 10¹²² gap persists, manifesting as a large μ₁⁴.**
