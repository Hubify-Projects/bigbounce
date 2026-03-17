# Foundation G — Toy Selection Frameworks

**Date:** 2026-03-15

---

## Purpose

Construct three toy frameworks illustrating how the bounce might
condition a global variable, to identify the structural possibilities
before detailed computation.

---

## Toy Framework 1: Cyclic Sequestering With Bounce Boundaries

### Variable
The global Lagrange multiplier σ and the cycle 4-volume V₄^(n)
for the n-th cycle.

### Action (per cycle)
```
S^(n) = ∫_cycle_n d⁴x √g [½M_Pl² R - Λ^(n) + L_matter]
        + σ^(n) [Λ^(n) V₄^(n) / μ⁴ - 1]
```

### Bounce condition
At each bounce (boundary between cycle n and cycle n+1), impose
continuity of the metric and its first derivative:

```
[g_μν]_bounce = 0     (continuous metric)
[K_μν]_bounce = 0     (continuous extrinsic curvature)
```

On FRW, this means:
```
a(t_b⁻) = a(t_b⁺) = a_min
ȧ(t_b⁻) = ȧ(t_b⁺)     [but ȧ = aH = 0 at bounce]
ä(t_b⁻) = ä(t_b⁺)     [requires Ḣ continuous]
```

### What late-time quantity is affected
Λ^(n) = μ⁴/V₄^(n). The cosmological constant in each cycle is
determined by the cycle's 4-volume.

### Bounce condition's effect
If the bounce enforces IDENTICAL physics in each cycle
(σ^(n) = σ^(n+1), same matter content, same topology), then
V₄^(n) is the same for each cycle and:

```
Λ_residual = μ⁴/V₄^per_cycle
```

The bounce does not determine μ⁴ — that remains free. But V₄^per_cycle
IS determined by the dynamics (it depends on Λ_residual, matter
content, and the bounce conditions). This creates a SELF-CONSISTENCY
equation:

```
Λ = μ⁴/V₄(Λ, matter)
```

This is a transcendental equation that may have discrete solutions,
possibly including Λ = 0 or small Λ.

### Biggest ambiguity
Does the self-consistency equation have a solution with
Λ ~ 10⁻¹²² M_Pl⁴? The answer depends on V₄(Λ), which depends
on the full cosmological evolution within a cycle. Computing V₄(Λ)
requires knowing the cycle duration, maximum expansion, and
turnaround physics — none of which are established for spin-torsion
cyclic cosmology.

Also: μ⁴ is a free parameter. Changing μ⁴ shifts the solution.
The bounce does NOT determine μ⁴.

### Structural assessment
The bounce provides FINITE V₄ (essential for sequestering) and
CYCLIC structure (self-consistency equation). But μ⁴ is free,
so Λ_residual is still tunable. The bounce is HELPFUL but NOT
SUFFICIENT for fixing Λ.

**Rating: bounce is necessary but not sufficient.**

---

## Toy Framework 2: Discrete Vacuum Label at Maximal Density

### Variable
A discrete label N ∈ {0, 1, 2, ...} representing the vacuum sector,
with effective vacuum energy:

```
Λ_eff(N) = Λ_bare + N × Δ
```

where Δ is the step size (determined by the underlying theory, e.g.,
flux quanta).

### Action
```
S = ∫ d⁴x √g [½M_Pl² R - Λ_eff(N) + L_matter] + S_transitions(N)
```

S_transitions describes the dynamics of transitions between N values
(membrane nucleation, tunneling).

### Bounce condition
At the bounce (ρ = ρ_crit ~ M_Pl⁴), the transition rate between
vacuum sectors is:

```
Γ(N → N±1) = A exp(-B/ρ^{1/4})
```

At the bounce: ρ^{1/4} ~ M_Pl, so Γ ~ A exp(-B/M_Pl). For B ~ M_Pl:
Γ ~ A × O(1). Transitions are UNSUPPRESSED at the bounce.

The system reaches EQUILIBRIUM among accessible sectors during the
bounce epoch. The equilibrium distribution:

```
P(N) ∝ exp(-Λ_eff(N) × V₃ × Δt_bounce / T_bounce)
```

where V₃ is the spatial volume at the bounce, Δt is the bounce
duration, and T_bounce ~ M_Pl.

### What late-time quantity is affected
The vacuum sector N selected during the bounce determines
Λ_eff = Λ_bare + NΔ for the expanding phase.

### Bounce condition's effect
The selection probability depends on Λ_eff, V₃, and T_bounce.
If V₃ × Δt_bounce / T_bounce is small (it is: V₃ ~ a_min³ × L³,
Δt ~ t_Pl, T ~ M_Pl → product ~ a_min³ L³), then:

```
P(N) ∝ exp(-Λ_eff × a_min³ L³ / M_Pl)
```

For Λ_eff ~ M_Pl⁴ and a_min³ L³ ~ O(1) in Planck units:
```
P(N) ∝ exp(-O(M_Pl³ L³))
```

This is exponentially sensitive to Λ_eff if M_Pl³ L³ ≫ 1. The
distribution STRONGLY favors N with smallest |Λ_eff|.

### Biggest ambiguity
1. The step size Δ is NOT determined by the bounce. It is set by
   the underlying theory (string flux quanta, gauge theory scales, etc.).
   For Λ_eff ~ 10⁻¹²² M_Pl⁴: need N × Δ to scan to this precision,
   requiring N ~ M_Pl⁴/Δ ~ enormous.

2. The bounce provides the SELECTION EPOCH but not the SELECTION
   CRITERION. The criterion (minimum |Λ_eff|) is thermodynamic,
   not geometric. Any sufficiently hot epoch gives the same selection.

3. a_min is not well-determined in spin-torsion cosmology. The
   entire distribution depends on a_min³ L³, which is essentially
   the number of Planck volumes at the bounce.

### Structural assessment
The bounce provides a natural SELECTION EPOCH (highest temperature,
fastest transitions). But the selection criterion is THERMAL
equilibrium, not geometric. Inflation followed by reheating provides
a similar high-temperature epoch.

**Rating: bounce is one of several possible selection epochs.
Not bounce-SPECIFIC.**

---

## Toy Framework 3: Matching Condition Across Bounce Constraining
Global Multiplier

### Variable
A global Lagrange multiplier λ in the action:

```
S = ∫ d⁴x √g [(M_Pl²/2 + λ)R - Λ + L_matter]
```

where λ is a spacetime constant (not a field).

### Bounce condition
At the bounce surface Σ_b, require REGULARITY of the second
fundamental form (extrinsic curvature). For FRW, this means:

```
Ḣ is continuous at the bounce
```

From the modified Friedmann equations:
```
(M_Pl² + 2λ)(Ḣ + H²) = -(4πG/3)(ρ + 3p) + Λ/3
```

At the bounce (H = 0):
```
(M_Pl² + 2λ) Ḣ_b = -(4πG/3)(ρ_b + 3p_b) + Λ/3
```

In spin-torsion cosmology, Ḣ_b is DETERMINED by the bounce
dynamics (it depends on ρ_crit and the equation of state at the
bounce). So:

```
(M_Pl² + 2λ) = [-(4πG/3)(ρ_b + 3p_b) + Λ/3] / Ḣ_b
```

This gives a RELATION between λ and Λ. Combined with the global
constraint equation (e.g., ∫√g R = χ₀ with χ₀ determined by
another condition), this could fix both λ and Λ.

### What late-time quantity is affected
The effective Planck mass M̃_Pl² = M_Pl² + 2λ and the effective
cosmological constant Λ_eff = Λ/(1 + 2λ/M_Pl²).

### Bounce condition's effect
The matching condition relates λ to Λ through bounce-era quantities
(ρ_b, p_b, Ḣ_b). But this is ONE equation in TWO unknowns (λ, Λ).
A second equation is needed to determine both.

The second equation could come from:
- The global constraint (∫√g R = χ₀)
- A normalization condition (M̃_Pl² matches observed Newton's constant)
- Another boundary condition (at the turnaround, if cyclic)

### Biggest ambiguity
The matching condition is ONE equation. It does not by itself
determine Λ. A second condition is needed, and that second
condition introduces either:
- Another free parameter (χ₀, which Foundation E showed is tuned)
- An observational input (G_observed, which is measured not predicted)

If the second condition is G_observed = 1/(8πM̃_Pl²), then:
```
M̃_Pl² = M_Pl² + 2λ = M_Pl_observed²
→ λ = (M_Pl_observed² - M_Pl²)/2
```

And from the bounce matching:
```
Λ = M_Pl_observed² Ḣ_b + (4πG/3)(ρ_b + 3p_b)
  = M_Pl_observed² Ḣ_b + (ρ_b + 3p_b)/(6M_Pl_observed²)
```

For radiation at the bounce (p = ρ/3):
```
Λ = M_Pl² Ḣ_b + 2ρ_crit/(3M_Pl²)
```

With Ḣ_b and ρ_crit both ~ M_Pl²: Λ ~ M_Pl⁴. This gives
**Λ ~ M_Pl⁴, 122 orders of magnitude too large.**

The matching condition DETERMINES Λ but gives the WRONG value.
The bounce curvature is Planck-scale, and the matching condition
inherits this scale.

### Structural assessment
The matching condition provides a DETERMINISTIC Λ (no free
parameter!). But the determined value is Λ ~ M_Pl⁴ — the natural
gravitational scale, not the observed DE scale. The 10¹²²
suppression from M_Pl⁴ to ρ_DE is not produced.

**Rating: deterministic but wrong. The CC problem reappears as
"why is Ḣ_b so much smaller than the naive estimate?"**

---

## Summary of Toy Frameworks

| Toy | Bounce role | Λ determined? | Correct value? | Bounce essential? |
|-----|-----------|--------------|---------------|-------------------|
| 1: Cyclic sequestering | Provides finite V₄ | Partially (μ⁴ free) | Tunable | YES (finite V₄) |
| 2: Discrete vacuum selection | Selection epoch | Probabilistically | Requires landscape | NO (any hot epoch) |
| 3: Matching condition | Fixes λ-Λ relation | YES (deterministic) | NO (Λ ~ M_Pl⁴) | YES (uses Ḣ_b) |

### Key insight from the toys

**Toy 3 is the most revealing.** It shows that a DETERMINISTIC
mechanism (no free parameters!) gives Λ ~ M_Pl⁴ — because the
bounce curvature is Planck-scale and any matching condition inherits
the Planck scale.

This is the fundamental problem: the bounce operates at M_Pl, and
any condition evaluated at the bounce produces quantities of order
M_Pl^n. Getting Λ ~ 10⁻¹²² M_Pl⁴ from a Planck-scale matching
condition requires a suppression mechanism — which is the CC problem
all over again.

**Toy 1 is the most viable.** It does not try to DERIVE Λ from the
bounce. Instead, it uses the bounce to make sequestering WELL-DEFINED
(finite V₄). The CC problem is addressed by sequestering, and the
bounce provides the infrastructure. But μ⁴ remains free — the bounce
is necessary but not sufficient.
