# Foundation E — Baseline Sequestering Model

**Date:** 2026-03-14

---

## The Kaloper-Padilla Sequestering Mechanism

### The Problem It Addresses

The cosmological constant receives radiative corrections from every
massive particle in the Standard Model:

```
δΛ = Σ_i (±1) M_i⁴/(64π²) ln(M_i²/μ²)
```

Each contribution is enormous compared to Λ_obs ~ 10⁻⁴⁷ GeV⁴.
Cancellation to 122 decimal places requires fine-tuning that must
be redone at every loop order and every phase transition.

### Core Idea

Introduce global (spacetime-averaged) variables that AUTOMATICALLY
absorb arbitrary constant shifts of the vacuum energy. The mechanism
does not cancel each contribution individually — it enforces a global
constraint that makes the TOTAL contribution to the effective Λ
insensitive to constant vacuum shifts.

---

## Minimal Sequestering Action

### Standard formulation (Kaloper-Padilla 2013)

```
S = ∫ d⁴x √g [½M_Pl² R - Λ + L_matter(g_μν, ψ)]
    + σ₁[Λ ∫ d⁴x √g / μ₁⁴ - 1]
    + σ₂[∫ d⁴x √g L_matter / (μ₂⁴ ∫ d⁴x √g) - 1]
```

where:
- Λ is the bare cosmological constant (NOT a free parameter — it is
  determined by the σ₁ equation)
- σ₁, σ₂ are global Lagrange multipliers (spacetime constants)
- μ₁, μ₂ are mass scales (the only free parameters)

### Equations from global variation

**Varying σ₁:**
```
Λ = μ₁⁴ / ∫ d⁴x √g
```
This fixes Λ in terms of the spacetime 4-volume V₄ = ∫ d⁴x √g.

**Varying σ₂:**
```
⟨L_matter⟩ ≡ ∫ d⁴x √g L_matter / ∫ d⁴x √g = μ₂⁴
```
This fixes the spacetime-averaged matter Lagrangian.

**Varying Λ:**
```
σ₁ ∫ d⁴x √g / μ₁⁴ = ∫ d⁴x √g
```
→ σ₁ = μ₁⁴. (Consistency condition.)

**Varying g_μν locally:**
Standard Einstein equations with effective cosmological constant:
```
G_μν + Λ_eff g_μν = (8πG) T_μν
```
where Λ_eff = Λ + ⟨vacuum contribution⟩.

### How vacuum energy is neutralized

Under a constant shift of the matter Lagrangian:
```
L_matter → L_matter + V₀
```
(e.g., from a phase transition that shifts the vacuum by V₀), the
σ₂ constraint absorbs V₀:

```
⟨L_matter + V₀⟩ = μ₂⁴
→ ⟨L_matter⟩ = μ₂⁴ - V₀
```

The effective Λ is then:
```
Λ_eff = μ₁⁴/V₄ - (μ₂⁴ - V₀) + V₀ = μ₁⁴/V₄ - μ₂⁴ + 2V₀
```

Wait — this does NOT cancel V₀. The standard Kaloper-Padilla mechanism
is more subtle. Let me restate carefully.

### Correct sequestering mechanism

The key insight is that the GRAVITATIONAL equations of motion see
an effective stress-energy that has its vacuum component PROJECTED
OUT by the global constraint:

```
T^eff_μν = T_μν - ⟨T⟩ g_μν + (σ-dependent terms)
```

The constant piece of T_μν (the vacuum energy) is absorbed by the
global variables. Only the FLUCTUATING part of T_μν sources gravity.

More precisely: the local Einstein equations are:
```
G_μν = 8πG (T_μν - ⟨T^μ_μ⟩/4 × g_μν) + Λ_residual g_μν
```

where Λ_residual depends on μ₁, μ₂, and the 4-volume V₄, but NOT
on the vacuum energy contributions from matter loops.

### The residual cosmological constant

```
Λ_residual = μ₁⁴/V₄ + (function of μ₂, V₄, ⟨non-vacuum T⟩)
```

This is the HISTORICAL residual: it depends on the full spacetime
4-volume, which is determined by the entire evolution of the universe.

---

## Key Assumptions

1. **Spacetime has finite 4-volume.** The mechanism requires V₄ = ∫d⁴x√g
   to be finite. In standard ΛCDM with Λ > 0, the universe expands
   forever and V₄ → ∞, giving Λ_residual → 0. This is consistent only
   if the universe eventually recollapses or has a future boundary.

2. **Global variables are physical.** The Lagrange multipliers σ₁, σ₂
   are spacetime constants determined by boundary conditions. They are
   not local fields and cannot be observed locally.

3. **The variational principle is well-defined.** Varying the action
   requires knowing the full spacetime (including the future). This
   is potentially acausal, though the LOCAL equations of motion are
   standard Einstein equations with a specific Λ_residual.

4. **Radiative stability.** The mechanism must survive loop corrections.
   This is the most debated aspect. Kaloper and Padilla argue it does;
   others have raised concerns.

---

## What the Mechanism Does NOT Do

- It does NOT explain WHY Λ_residual has the observed value. It only
  ensures that Λ_residual is INSENSITIVE to vacuum energy shifts from
  phase transitions and matter loops.

- It does NOT solve the coincidence problem (why ρ_Λ ~ ρ_matter today).

- It does NOT eliminate the need for a small scale. The scales μ₁, μ₂
  are free parameters that ultimately determine Λ_residual.

---

## Relation to This Research Program

### The bounce provides finite 4-volume

In a spin-torsion bounce cosmology, the universe has a finite past
(beginning at the bounce, not at a singularity). If the universe
also has a finite future (recollapse or future bounce), then V₄ is
naturally finite — exactly what sequestering requires.

This is a structural connection: **the bounce cosmology provides an
ingredient (finite V₄) that the sequestering mechanism needs.**

### Torsion at the bounce

The bounce occurs at ρ ~ M_Pl⁴ where torsion is dynamically
important. The sequestering action must be formulated in EC or PGT
gravity to be compatible. The question is whether the global
constraints are modified by torsion.

In EC gravity: R(Γ) = R(g) + (torsion)². The integral ∫√g R(Γ)
differs from ∫√g R(g) at the bounce. This could modify the
residual Λ formula.

### The key test

Does formulating Kaloper-Padilla sequestering in EC/PGT gravity
with a spin-torsion bounce produce:

1. A well-defined residual Λ_residual?
2. A Λ_residual that depends on bounce-era parameters?
3. A Λ_residual that is naturally small?

If yes to all three: **Foundation E produces a bounce-specific
prediction for the cosmological constant.**

If Λ_residual is generic (independent of bounce physics):
the mechanism works but the bounce connection is vacuous.

If Λ_residual requires tuning of μ₁, μ₂ to 122 digits:
the mechanism has relocated the tuning, not solved it.
