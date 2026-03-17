# Phase 2 — Λ Determination

**Date:** 2026-03-15

---

## Question

Assuming the constraint ∫√g R = χ₀, can the late-time Λ be
determined? And does it depend on bounce curvature?

---

## Formal Derivation

### The system

The modified Friedmann equations (from Task 1) are:

```
G_μν + Λ/M̃_Pl² g_μν = T_μν/M̃_Pl²
```

where M̃_Pl² = M_Pl² + 2λ, plus the constraint:

```
I_R = V_c × ∫ dt a³(t) R(t) = χ₀
```

On FRW, the Friedmann equations give:

```
3M̃_Pl² H² = ρ + Λ
-2M̃_Pl² Ḣ = ρ + p
```

The Ricci scalar:
```
R = 6(Ḣ + 2H²) = -6(ρ + p)/M̃_Pl² + 12(ρ + Λ)/(3M̃_Pl²)
  = (-6ρ - 6p + 4ρ + 4Λ) / M̃_Pl²
  = (-2ρ - 6p + 4Λ) / M̃_Pl²
```

For matter (p = 0): R = (-2ρ_m + 4Λ)/M̃_Pl² = 4Λ/M̃_Pl² - 2ρ_m/M̃_Pl²
For radiation (p = ρ/3): R = (-2ρ - 2ρ + 4Λ)/M̃_Pl² = 4Λ/M̃_Pl² - 4ρ_r/M̃_Pl²
For de Sitter (ρ → 0): R = 4Λ/M̃_Pl² = 12H_Λ²

### The integral

```
I_R = V_c ∫ dt a³ R = V_c ∫ dt a³ [4Λ/M̃_Pl² - (2ρ + 6p)/M̃_Pl²]
```

Split:
```
I_R = (4Λ/M̃_Pl²) V_c ∫ dt a³ - (1/M̃_Pl²) V_c ∫ dt a³(2ρ + 6p)
    = (4Λ/M̃_Pl²) V₄ - (1/M̃_Pl²) V_c ∫ dt a³(2ρ + 6p)
```

where V₄ = V_c ∫ dt a³ is the spacetime 4-volume.

Define:
```
I_matter ≡ V_c ∫ dt a³(2ρ + 6p)
```

Then:
```
I_R = (4Λ V₄ - I_matter) / M̃_Pl²
```

Setting I_R = χ₀:
```
4Λ V₄ - I_matter = χ₀ M̃_Pl²

Λ = (χ₀ M̃_Pl² + I_matter) / (4V₄)
```

---

## Analysis of the Λ Formula

```
Λ = (χ₀ M̃_Pl² + I_matter) / (4V₄)
```

### The V₄ divergence problem

If the universe accelerates forever, V₄ → ∞. Then:

```
Λ → I_matter / (4V₄) → 0    (if I_matter is finite)
```

But Λ = 0 is inconsistent with eternal acceleration, which is needed
for V₄ → ∞. **Self-consistency requires either Λ = 0 (no acceleration,
finite V₄) or a recollapsing universe (finite V₄ with Λ > 0
eventually overcome by matter).**

### Self-consistent solutions

For a recollapsing universe (V₄ finite):

```
Λ = (χ₀ M̃_Pl² + I_matter) / (4V₄)
```

Both V₄ and I_matter depend on Λ (through the Friedmann equations).
This is a SELF-CONSISTENCY equation, not an explicit formula.

Schematically:
```
Λ = F(Λ, χ₀, matter content)
```

This transcendental equation determines Λ as a function of χ₀ and
the matter content. Its solution (if it exists) is the effective
cosmological constant.

### Does Λ depend on the bounce?

The bounce contributes to both V₄ and I_matter:

```
V₄ = V₄^bounce + V₄^post-bounce

I_matter = I_matter^bounce + I_matter^post-bounce
```

From the curvature integral analysis:

```
V₄^bounce / V₄^post-bounce ~ (a_min³ t_Pl) / (a_max³ t_universe) ~ 10⁻¹⁸⁵
```

(using a_max/a_min ~ 10⁶⁰ and t_universe/t_Pl ~ 10⁶⁰)

Similarly:
```
I_matter^bounce / I_matter^post-bounce ~ 10⁻³² (same scaling as I_R)
```

**The bounce contributions to V₄ and I_matter are negligible.**

Therefore:
```
Λ ≈ (χ₀ M̃_Pl² + I_matter^post-bounce) / (4V₄^post-bounce)
```

**Λ does NOT depend on bounce physics.** It depends on χ₀, the
matter content, and the post-bounce cosmological evolution.

---

## Does χ₀ Need to Be Tuned?

### What determines χ₀?

χ₀ is a free parameter in the action. For Λ to take the observed
value, χ₀ must satisfy:

```
χ₀ = (4Λ_obs V₄ - I_matter) / M̃_Pl²
```

The right side involves V₄ and I_matter, which are determined by the
full cosmological history. In a recollapsing universe, these are
finite but model-dependent.

**χ₀ must be chosen to reproduce Λ_obs.** This is fine-tuning of a
different kind: instead of tuning Λ directly, we tune χ₀.

### Could topology fix χ₀?

In principle, ∫√g R is related to the Euler characteristic χ(M)
through the Gauss-Bonnet theorem in 4D:

```
χ(M) = (1/32π²) ∫ d⁴x √g (R² - 4R_μν R^μν + R_μνρσ R^μνρσ) + boundary
```

But this involves the Gauss-Bonnet COMBINATION of curvature
invariants, NOT just R alone. The integral ∫√g R is NOT a
topological invariant. It depends on the dynamics, not just topology.

**χ₀ cannot be fixed by topology.** It is a free parameter that
must be tuned.

### Could boundary conditions fix χ₀?

If the spacetime has boundaries (the bounce as past boundary,
a future crunch as future boundary), boundary conditions might
constrain χ₀. But this requires:

1. A specific boundary theory (Gibbons-Hawking-York + corrections)
2. A well-defined variational principle with boundary data

In practice, the boundary conditions at the bounce are determined
by the bounce dynamics (matching conditions across the bounce).
These do not directly constrain ∫√g R.

**χ₀ is not fixed by boundary conditions in any known framework.**

---

## Summary

| Question | Answer |
|----------|--------|
| Can Λ be determined from the constraint? | YES, formally (self-consistency equation) |
| Does Λ depend on bounce curvature? | NO (bounce contribution negligible by ~10³²) |
| Must χ₀ be tuned? | YES (χ₀ is a free parameter, not topological) |
| Can topology fix χ₀? | NO (∫√g R is not a topological invariant) |
| Can boundary conditions fix χ₀? | NO (no known framework) |

**The constraint ∫√g R = χ₀ relocates the fine-tuning from Λ to χ₀.
It does not solve the cosmological constant problem, and it does not
connect the bounce to dark energy.**
