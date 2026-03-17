# Foundation E — Bounce Compatibility Analysis

**Date:** 2026-03-14

---

## Question

Is the vacuum energy sequestering mechanism compatible with a
spin-torsion bounce phase?

---

## Check 1: Does the Global Constraint Survive Through the Bounce?

### The constraint
The sequestering mechanism imposes:
```
Λ_bare = μ₁⁴ / V₄        where V₄ = ∫ d⁴x √g
```

This is a GLOBAL constraint on the entire spacetime. It is not a local
equation that could be "violated" at the bounce — it is a condition
on the spacetime as a whole.

### At the bounce
The bounce is a smooth transition (no singularity). The metric g_μν
is continuous and differentiable through the bounce point. Therefore
√g is well-defined and finite everywhere, including at the bounce.

The 4-volume integral V₄ receives contributions from ALL eras:
```
V₄ = V₄^pre-bounce + V₄^bounce + V₄^post-bounce
```

The bounce era has very high curvature but very short duration
(Δt_bounce ~ t_Pl ~ 10⁻⁴³ s). Its contribution to V₄ is:
```
V₄^bounce ~ a³(t_bounce) × Δt_bounce × V_spatial
```

For a universe that has expanded for ~10¹⁷ s after the bounce,
the bounce contribution to V₄ is negligible:
```
V₄^bounce / V₄^total ~ (a_bounce/a_today)³ × (Δt_bounce/t_today)
                      ~ (a_bounce/a_today)³ × 10⁻⁶⁰
```

**Verdict: The global constraint is compatible with the bounce. The
bounce contributes negligibly to V₄.**

### Implication
Since V₄ is dominated by the late-time expanding phase, Λ_residual
= μ₁⁴/V₄ is primarily determined by the late-time evolution, not
by the bounce. This means:

- The bounce does not DISRUPT the sequestering mechanism (good)
- The bounce does not DETERMINE Λ_residual through V₄ (disappointing)

---

## Check 2: Do Torsion/Spin Densities Modify the Constraint?

### EC gravity formulation
In Einstein-Cartan gravity, the Ricci scalar of the full connection is:
```
R(Γ) = R(g) + (torsion)² terms
```

Specifically, for the Cartan spin-torsion interaction:
```
R(Γ) = R(g) - 4κ²(s^μ s_μ)
```
where s^μ is the spin density and κ² = 24πG.

### Sequestering in EC gravity
If we write the sequestering action with R(Γ) instead of R(g):
```
S_EC = ∫ d⁴x √g [½M_Pl² R(Γ) - Λ + L_matter + L_spin]
       + σ₁[Λ V₄ / μ₁⁴ - 1]
       + σ₂[⟨L_matter⟩/μ₂⁴ - 1]
```

The torsion field equation (algebraic in EC) gives:
```
T^λ_μν = -κ² s^λ_μν
```

After torsion elimination:
```
S_eff = ∫ d⁴x √g [½M_Pl² R(g) - κ²(s²) - Λ + L_matter]
        + global constraints
```

The spin-squared term κ²s² is a LOCAL term that enters L_matter.
It is part of the matter Lagrangian that the σ₂ constraint averages.

### Does torsion modify the sequestering?

**No, not structurally.** The torsion contribution -κ²s² is a specific
matter interaction term. The sequestering mechanism handles it the
same way it handles any other matter interaction: the constant
(vacuum) part is absorbed by the global constraint, and the
fluctuating part sources gravity normally.

At the bounce, s² is enormous (~M_Pl⁴) but confined to a tiny
spacetime volume. Its spacetime average is:
```
⟨κ²s²⟩ = ∫ d⁴x √g κ²s² / V₄ ~ κ²M_Pl⁴ × V₄^bounce / V₄ ~ negligible
```

**Verdict: Torsion does not modify the sequestering constraint in
any important way. The spin-torsion interaction is a local matter
term that is handled normally by the global mechanism.**

---

## Check 3: Does the Bounce Set or Select the Effective Vacuum Sector?

### What would be needed
For the bounce to DETERMINE Λ_residual, we would need the bounce
to contribute DOMINANTLY to one of the global quantities (V₄ or
⟨L_matter⟩). As shown above, the bounce's contribution to V₄ is
negligible.

Could the bounce contribute dominantly to ⟨L_matter⟩? The matter
Lagrangian at the bounce is L ~ M_Pl⁴ (extreme density), but over
a tiny volume. The spacetime average is still dominated by the
late-time evolution where L ~ ρ_matter ~ T⁴.

### What about the σ₁ scale μ₁?
The residual Λ is:
```
Λ_residual ~ μ₁⁴/V₄
```

If μ₁ is related to the bounce energy scale (μ₁ ~ M_Pl), then:
```
Λ_residual ~ M_Pl⁴ / V₄
```

For V₄ ~ (H₀⁻¹)⁴ ~ (10⁶⁰ l_Pl)⁴:
```
Λ_residual ~ M_Pl⁴ / (10²⁴⁰ l_Pl⁴) ~ M_Pl⁴ × 10⁻²⁴⁰ / M_Pl⁻⁴
           ~ 10⁻²⁴⁰ M_Pl⁴
```

This is FAR too small — 10⁻¹¹⁸ times smaller than observed.

For Λ_residual ~ 10⁻¹²² M_Pl⁴, we need:
```
μ₁⁴ / V₄ ~ 10⁻¹²² M_Pl⁴
μ₁⁴ ~ 10⁻¹²² × V₄ × M_Pl⁴
```

This does NOT naturally give μ₁ ~ M_Pl. The scale μ₁ must be
adjusted to match observations. The bounce does not fix it.

### Verdict: The bounce does NOT select Λ_residual

The global quantities (V₄, ⟨L_matter⟩) are dominated by late-time
evolution, not by the bounce. The bounce contributes negligibly to
both. The residual Λ depends on the scales μ₁, μ₂, which are NOT
determined by bounce physics.

**The sequestering mechanism is COMPATIBLE with the bounce but not
LINKED to it.**

---

## Check 4: Finite 4-Volume Requirement

### The issue
Sequestering requires V₄ < ∞. In standard ΛCDM with Λ > 0, the
spatial volume grows as a(t)³ ~ e³ᴴᵗ, and V₄ diverges.

### Does the bounce help?
The bounce provides a finite PAST (no singularity, finite a_min > 0).
But the future is still infinite in an accelerating universe.

V₄ divergence comes from the FUTURE, not the past:
```
V₄ = ∫₀^∞ dt a³(t) × V_spatial
```

For a(t) ~ e^{Ht} at late times: V₄ ~ ∫ e³ᴴᵗ dt → ∞.

The bounce does NOT solve the finite-4-volume problem. It only
addresses the past boundary.

### What would solve it
- Future recollapse (ρ_Λ eventually becomes negative)
- Future bounce (cyclic cosmology)
- Compact spatial sections (V_spatial finite)
- A future boundary condition

Kaloper and Padilla (2015) argued that the universe MUST eventually
transition to a crunching phase. This is a PREDICTION of sequestering,
not a bug. But it requires physics beyond the standard Λ > 0 de Sitter
future.

### Verdict: The bounce provides a finite past, but sequestering
requires a finite FUTURE. Additional structure is needed.

---

## Summary

| Check | Result | Implication |
|-------|--------|------------|
| Constraint survival | Compatible | Bounce doesn't disrupt sequestering |
| Torsion modification | Negligible | Spin-torsion is a local matter term |
| Bounce sets Λ? | NO | V₄ and ⟨L⟩ dominated by late-time evolution |
| Finite 4-volume | PARTIAL | Bounce fixes past; future still diverges |

### Overall Assessment

**The sequestering mechanism is compatible with but not linked to
bounce cosmology.** The bounce neither disrupts nor determines the
sequestering. The global quantities that set Λ_residual are dominated
by late-time cosmological evolution, not by bounce-era physics.

The finite-4-volume requirement is only partially addressed: the
bounce provides a finite past, but a finite future requires
additional physics (recollapse, cyclic evolution, or compact spatial
topology).

### Implication for Foundation E

The sequestering + bounce combination does not produce a
bounce-specific prediction for Λ. The mechanism works (it absorbs
vacuum energy shifts) but the residual Λ depends on global
parameters (μ₁, μ₂) and the full spacetime evolution, not on
bounce physics specifically.

This means: **sequestering is bounce-compatible but bounce-generic.**
Any cosmological history (with or without a bounce) is equally
compatible with sequestering.
