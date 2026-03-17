# Phase 2 — Bounce Matching Conditions

**Date:** 2026-03-15

---

## Question

Do the bounce matching conditions (H = 0, metric continuity,
spin-torsion Friedmann equation) constrain the sequestering
scale μ⁴?

---

## Matching Conditions at the Bounce

### Condition 1: H = 0

At the bounce surface:
```
H(t_b) = 0
```

This is the DEFINITION of the bounce. It does not constrain μ⁴.
It is satisfied for any Λ (and hence any μ⁴) by adjusting the
matter density at the bounce.

From the modified Friedmann equation:
```
0 = (8πG/3)(ρ_b - ρ_b²/ρ_crit) - k/a_min² + Λ/3
```

This determines a_min as a function of ρ_b, Λ, and k. It does NOT
constrain Λ independently — it constrains the COMBINATION of a_min
and Λ.

### Condition 2: Metric continuity

```
[g_μν]_{t_b} = 0    (no jump in the metric)
[ȧ]_{t_b} = 0       (no jump in ȧ; but ȧ = aH = 0 anyway)
```

These are automatically satisfied for a smooth bounce (no
discontinuity). They provide NO additional constraint on μ⁴.

### Condition 3: Extrinsic curvature continuity

```
[K_μν]_{t_b} = 0    (no jump in extrinsic curvature)
```

On FRW, K_ij = Hg_ij. At the bounce, H = 0 from both sides. So
[K] = 0 is automatically satisfied.

The SECOND derivative matters:
```
[Ḣ]_{t_b} = 0    (Ḣ continuous across the bounce)
```

From the Friedmann equation:
```
Ḣ = -(4πG)(ρ + p)(1 - 2ρ/ρ_crit) + Λ/3 - H²
```

At H = 0:
```
Ḣ_b = -(4πG)(ρ_b + p_b)(1 - 2ρ_b/ρ_crit) + Λ/3
```

For a time-symmetric bounce (contraction is the time-reverse of
expansion): Ḣ is the SAME from both sides. Continuity of Ḣ is
automatic.

For an ASYMMETRIC bounce (different matter composition before and
after): [Ḣ] = 0 gives:

```
(ρ_b + p_b)_before(1 - 2ρ_b/ρ_crit) = (ρ_b + p_b)_after(1 - 2ρ_b/ρ_crit)
```

Since (1 - 2ρ_b/ρ_crit) is the same from both sides (ρ_b is
continuous), this requires:

```
(ρ + p)_before = (ρ + p)_after
```

at the bounce. This constrains the MATTER CONTENT, not Λ or μ⁴.

### Condition 4: Spin-torsion specific conditions

In Einstein-Cartan theory, torsion is algebraically determined by
spin density: T = -κ²s. At the bounce, s is determined by the
matter content. The torsion matching conditions are automatically
satisfied when the matter content is smooth.

The spin-torsion modification enters the Friedmann equation through
the ρ²/ρ_crit term. This is a smooth modification that does not
introduce additional matching conditions.

---

## Do ANY Matching Conditions Constrain μ⁴?

### Analysis

The sequestering action contains the global constraint:
```
σ₁[Λ V₄/μ₁⁴ - 1] = 0
```

σ₁ is a global (spacetime-constant) Lagrange multiplier. It is NOT
a local field. It does not have a value at the bounce that could be
"matched."

The constraint equation determines Λ = μ₁⁴/V₄ globally, for the
ENTIRE spacetime. It is not an equation that is evaluated at the
bounce — it involves the integral over the full cycle.

### Can the bounce impose a condition on σ₁?

No. σ₁ is a single number for the entire spacetime. The bounce is
a single moment. The number σ₁ is determined by the variational
principle over the whole spacetime, not at any particular surface.

### Can the bounce impose a condition on μ₁?

μ₁ is a PARAMETER in the action, not a dynamical variable. It is
not subject to equations of motion, matching conditions, or boundary
conditions. It is a constant that must be specified from outside
the theory.

No dynamical equation or boundary condition determines μ₁.

### Can the bounce regularity select μ₁?

Only if singular behavior (divergence, discontinuity) occurs for
SOME values of μ₁ and not others. Since μ₁ enters only through
Λ = μ₁⁴/V₄, and Λ enters the Friedmann equation smoothly, the
bounce is regular for ALL values of μ₁ (as long as Λ < Λ_crit so
a cycle exists).

There is no value of μ₁ that is singular or special from the
bounce regularity perspective.

---

## The Structural Impossibility

The matching conditions at the bounce constrain:
- a_min (scale factor at the bounce)
- ρ_b (density at the bounce)
- Ḣ_b (curvature rate at the bounce)
- The matter content across the bounce

They do NOT constrain:
- μ₁ (a parameter in the action, not a dynamical variable)
- σ₁ (a global constant, not a local quantity)
- V₄ (a global integral, not evaluable at a point)
- Λ_residual (determined by V₄ and μ₁, both non-local/parametric)

**The mismatch is structural:** matching conditions are LOCAL
conditions at a single spacetime surface. Sequestering parameters
are GLOBAL quantities determined by the full spacetime. Local
conditions cannot constrain global parameters.

This is a manifestation of a general principle: **boundary conditions
constrain the SOLUTION of the equations of motion (trajectories,
field values), not the PARAMETERS of the action (couplings,
masses, constraint scales).**

μ₁ is an action parameter. The bounce is a boundary. The boundary
cannot fix the action parameter.

---

## Summary

| Matching condition | What it constrains | Constrains μ⁴? |
|-------------------|-------------------|----------------|
| H = 0 | a_min vs ρ_b vs Λ | NO |
| Metric continuity | Smoothness of a(t) | NO (automatic) |
| Extrinsic curvature | (ρ+p) continuity | NO (constrains matter) |
| Spin-torsion | Torsion = -κ²s | NO (automatic from matter) |

**No bounce matching condition constrains μ⁴.** The sequestering
scale is an action parameter that is structurally immune to
boundary conditions at the bounce.
