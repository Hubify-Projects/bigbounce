# Foundation G — Candidate Mechanism Classes

**Date:** 2026-03-15

---

## Candidate A: Bounce-Conditioned Sequestering

### Core idea
Standard Kaloper-Padilla sequestering requires spacetime with finite
4-volume (V₄ < ∞). A cyclic bounce cosmology naturally provides
this: each bounce-to-bounce cycle has finite V₄. The BOUNCE
REGULARITY CONDITION (H = 0, nonsingular transition) imposes a
MATCHING CONDITION on the global Lagrange multipliers σ₁, σ₂ across
each cycle.

### Key variable being selected
The global Lagrange multipliers σ₁, σ₂ — which determine the
residual Λ through Λ_residual = f(σ₁, σ₂, V₄).

### How the bounce enters
The bounce is the BOUNDARY where cycle-to-cycle matching conditions
are imposed. Regularity at the bounce (no divergences in curvature,
no δ-function sources in the constraint equations) constrains the
allowed values of σ₁, σ₂.

Specifically: at H = 0, the Friedmann equation becomes:
```
0 = ρ + Λ    →    Λ = -ρ_bounce
```

If ρ_bounce = ρ_crit (fixed by spin-torsion physics), this
DETERMINES Λ at the bounce. But Λ during the expanding phase
may differ from Λ at the bounce (if Λ is an effective quantity
that includes the global constraint).

### Difference from plain sequestering
Plain sequestering: V₄ depends on the full cosmological history.
Λ_residual is a self-consistency condition with no preferred value.

Bounce-conditioned: V₄ is FINITE PER CYCLE. The bounce imposes
matching conditions that relate σ values in consecutive cycles.
If the matching is constraining, Λ_residual may be narrowed.

### Biggest risk
The matching condition at H = 0 may be trivially satisfied for
ANY σ values. The bounce provides a boundary but not necessarily
a CONSTRAINING boundary. If the matching is automatic (no
restriction), the mechanism collapses to generic sequestering.

---

## Candidate B: 4-Form Flux Branch Selection at the Bounce

### Core idea
A 4-form field F₄ = dA₃ has a constant flux q that contributes
an effective Λ_eff = q²/2. The flux can change by discrete amounts
Δq through membrane nucleation. At the bounce, the extreme
conditions (ρ ~ M_Pl⁴) may trigger flux transitions that adjust
q to a specific value.

### Key variable being selected
The 4-form flux quantum number n, where q = nΔq and
Λ_eff = n²(Δq)²/2.

### How the bounce enters
The bounce is the epoch of MAXIMUM energy density. Membrane
nucleation rates depend on the energy available:

```
Γ_nucleation ~ exp(-S_membrane / T_eff)
```

At the bounce: T_eff ~ M_Pl (Planck temperature). Membrane
nucleation is maximally efficient. The bounce is a "selection
bottleneck" where the flux adjusts most rapidly.

After the bounce, as ρ decreases, nucleation rates drop
exponentially. The flux is FROZEN at the value selected during
the bounce epoch.

### Difference from plain 4-form
Plain 4-form: flux selection occurs at unspecified time/mechanism.
Usually requires anthropic reasoning or landscape scanning.

Bounce-conditioned: the bounce EPOCH is when selection occurs.
The Planck-scale conditions at the bounce determine the selection
probability and possibly the final flux value.

### Biggest risk
The bounce does not RESTRICT the flux value — it merely provides
a high-energy environment where ANY transition is possible. If all
flux values are equally accessible at the bounce, the selection is
random, not predictive. The mechanism would require anthropic or
landscape reasoning to explain why a small Λ is selected.

Also: requires a landscape of vacua and membrane nucleation dynamics,
both of which are speculative.

---

## Candidate C: Nonsingular Regularity as Boundary Condition

### Core idea
In classical GR, the Big Bang singularity provides NO boundary
condition (it is a boundary of spacetime where the equations break
down). In bounce cosmology, the bounce is a REGULAR surface where
the equations are well-defined. Regularity at the bounce may impose
a constraint that restricts the allowed vacuum sector.

### Key variable being selected
The effective cosmological constant Λ_eff, constrained by requiring
that the bounce solution be nonsingular and regular.

### How the bounce enters
At the bounce: H = 0, Ḣ > 0, and all curvature invariants are
finite. The Friedmann equation at the bounce gives:

```
0 = (8πG/3)(ρ_bounce + Λ/M_Pl²)   [schematic]
```

Wait — more precisely, in spin-torsion cosmology:

```
H² = (8πG/3)(ρ - ρ²/ρ_crit) + Λ/3
```

At H = 0:
```
0 = (8πG/3)(ρ_bounce - ρ_bounce²/ρ_crit) + Λ/3
```

Since ρ_bounce = ρ_crit (the bounce occurs when ρ = ρ_crit):
```
0 = (8πG/3)(ρ_crit - ρ_crit) + Λ/3 = Λ/3
```

This gives **Λ = 0 at the bounce.**

But this is a condition at the bounce moment, not throughout the
cosmological evolution. The effective Λ during the expanding phase
could differ if Λ is a dynamical or constrained quantity.

### Difference from plain cosmology
In singular Big Bang cosmology: no boundary condition at t = 0.
Λ is a free parameter.

In bounce cosmology: the bounce is a regular surface where H = 0.
The equation H² = (...) + Λ/3 at the bounce imposes Λ/3 = 0 minus
matter contributions. This IS a condition on Λ.

### Biggest risk
The condition "Λ = 0 at the bounce" is trivially satisfied if we
interpret it as evaluating the Friedmann equation at H = 0. It does
not constrain the LATE-TIME Λ unless the theory somehow forbids Λ
from evolving (but constant Λ gives Λ = 0 always, contradicting
observations).

The condition may be VACUOUS: it tells us that H = 0 requires
matter density to exactly compensate Λ at one moment, which is
just the Friedmann equation evaluated at a specific time. This is
not a CONSTRAINT on Λ — it is a CONSEQUENCE of the dynamics.

---

## Candidate D: Topological Sector Selection

### Core idea
The spin-torsion bounce may change or constrain TOPOLOGICAL labels
of the spacetime: instanton number, Pontryagin charge, Euler
characteristic, or analogous discrete quantum numbers. If the
vacuum energy depends on the topological sector, the bounce
determines Λ by selecting the sector.

### Key variable being selected
A discrete topological quantum number N (instanton number, flux
integer, winding number) that enters the vacuum energy as:

```
Λ_eff = Λ_bare + f(N) × Λ_scale
```

### How the bounce enters
During the bounce, curvature and torsion are Planck-scale. The
Pontryagin density RR̃ and the Nieh-Yan density may be large.
If these are related to topological charge:

```
N = (1/32π²) ∫ d⁴x √g RR̃    [Pontryagin number]
```

the bounce epoch contributes a large PULSE to the integrand. The
integral over the bounce determines (or shifts) N.

If Λ depends on N, then the bounce determines Λ through N.

### Difference from plain topology
In a singular cosmology: the spacetime topology is often trivial
or undefined near the singularity. Topological invariants may not
be well-defined.

In bounce cosmology: the spacetime is everywhere smooth. Topological
invariants are well-defined and calculable. The bounce provides a
specific contribution to N that can be computed.

### Biggest risk
1. For FRW backgrounds: RR̃ = 0 (Pontryagin density vanishes on
   conformally flat spacetimes). The bounce does not contribute to
   the Pontryagin number unless perturbations are included.

2. The Nieh-Yan density N₄ is topological in EC gravity (Foundation B)
   and non-topological in MAG. But Foundation B showed that
   non-topological N₄ breaks shift symmetry.

3. The vacuum energy's dependence on N is typically θ-vacuum-like:
   E(θ) = E₀ - χ cos(θ), where χ ~ Λ_QCD⁴ for QCD. This has nothing
   to do with the gravitational bounce.

4. If N is an integer, Λ_eff changes in discrete steps. The step
   size is set by the underlying theory (QCD, GUT, etc.), not by
   the bounce. The bounce selects WHICH step, but the step values
   are pre-determined.

---

## Candidate E: Global Constraint With Bounce Matching

### Core idea
A global Lagrange multiplier λ exists (as in the curvature
constraint ∫√g R = χ₀), but instead of being a free parameter,
χ₀ is DETERMINED by a matching condition at the bounce.

### Key variable being selected
The global constraint parameter χ₀, which determines Λ_residual.

### How the bounce enters
At the bounce surface Σ_b (where H = 0), impose a matching
condition:

```
[R]_Σ_b = prescribed value    (curvature matching)
[K]_Σ_b = prescribed value    (extrinsic curvature matching)
[∇_n R]_Σ_b = 0               (smoothness condition)
```

These conditions relate the pre-bounce and post-bounce curvature,
which constrains the global integral ∫√g R and hence χ₀.

Specifically: if the pre-bounce contracting phase and post-bounce
expanding phase are related by time-reversal symmetry at the bounce:

```
R(t_b + τ) = R(t_b - τ)     [time-symmetric bounce]
```

This doubles the contribution from each era and imposes a symmetry
constraint on the full spacetime.

### Difference from plain global constraint
Plain constraint: χ₀ is a free parameter (Foundation E result).

Bounce-conditioned: χ₀ is DETERMINED by the bounce matching
condition. The bounce provides additional information (regularity,
symmetry, matching) that removes the freedom in χ₀.

### Biggest risk
Foundation E showed that ∫√g R is dominated by late-time evolution.
The bounce matching condition constrains R LOCALLY at the bounce
surface, but this local condition may not PROPAGATE to a constraint
on the global integral.

The bounce is one moment in a long cosmological history. Its
matching conditions determine the LOCAL curvature at t = t_b, but
the GLOBAL integral involves the entire evolution. A local condition
at one time cannot determine a global integral over all time.

This is the same scale-separation barrier from Foundation E,
repackaged.

---

## Summary

| Candidate | Variable selected | Bounce role | Biggest risk |
|-----------|------------------|-------------|-------------|
| A: Bounce-conditioned sequestering | σ₁, σ₂ | Cycle matching conditions | Matching may be trivial |
| B: 4-form flux at bounce | Flux quantum n | Selection bottleneck at ρ_max | Random selection, landscape needed |
| C: Regularity boundary condition | Λ_eff | H=0 regularity | Condition may be vacuous |
| D: Topological sector selection | Topological N | Curvature/torsion pulse contributes to N | RR̃=0 on FRW; N unrelated to Λ |
| E: Global constraint + bounce matching | χ₀ | Bounce matching determines χ₀ | Local condition ≠ global constraint |

### Initial ranking (before testing)

Most promising: **Candidate A** (bounce-conditioned sequestering).
Uses the most developed framework and the clearest bounce role
(cycle boundary conditions). Requires cyclic cosmology.

Least promising: **Candidate C** (regularity condition). The H=0
condition likely reduces to a trivial evaluation of the Friedmann
equation, not a new constraint on Λ.
