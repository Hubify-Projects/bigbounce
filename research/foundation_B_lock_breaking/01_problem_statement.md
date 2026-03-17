# Foundation B — Problem Statement: Breaking the Mass-Coupling Lock

**Date:** 2026-03-14

---

## The Mass-Coupling Lock

In any geometric theory where a propagating mode inherits its kinetic
term from the gravitational action, canonical normalization generically
locks the physical mass and matter coupling together.

### General mechanism

Consider a field φ with Lagrangian:

```
L = -½ Z (∂φ)² - ½ μ² φ² + g φ J
```

where Z is the kinetic normalization factor, μ is a bare mass parameter,
g is a bare coupling, and J is a matter current.

Canonical normalization φ_can = √Z φ gives:

```
m_phys = μ / √Z
g_eff  = g / √Z
```

When Z, μ², and g all derive from the same sector of the gravitational
action (as they do in PGT), a single parameter controls both m and g_eff.
The ratio m/g_eff = μ/g is fixed — the mass and coupling cannot be
adjusted independently.

### Concrete realization in PGT

In the ghost-free 0⁻ axial torsion mode of Poincaré gauge theory:

```
Z ∝ |t₃|
μ² ∝ M_Pl²
g ∝ 1 (gravitational coupling)
```

Therefore:

```
m_B = M_Pl / (4√(π|t₃|))
g_eff ~ 1 / (M_Pl √|t₃|)
```

For cosmologically light mass (m ~ meV), need |t₃| ~ 10⁵⁸.
At this value: g_eff ~ 10⁻²⁹ × gravitational strength.

The torsion mode is perturbatively healthy but observationally inert.
Large |t₃| is a **decoupling limit**, not a strong-coupling limit.

### Why minimal EC also fails

In minimal Einstein-Cartan-Holst gravity, torsion is algebraic
(non-propagating). It is eliminated exactly, leaving only a four-fermion
contact interaction. There is no propagating geometric degree of freedom
at all — the lock doesn't apply because there is nothing to lock.

The failure is more fundamental: algebraic torsion washes out entirely.
No IR information survives elimination.

### Why the lock is structural, not accidental

The lock arises from a single structural fact: in PGT (and similar
theories), the kinetic term, mass term, and matter coupling of the
torsion mode all originate from the same quadratic gravitational action.
The dimensionless coupling t₃ parameterizes the torsion-squared term in
the action, and all three physical quantities (Z, μ, g) are functions
of t₃ and M_Pl alone.

The lock is NOT:
- A fine-tuning problem (it occurs at all values of t₃)
- A strong-coupling pathology (the theory is well-behaved)
- A ghost problem (the mode is healthy)

It IS:
- A parameter-counting problem: 1 free parameter, 2 physical quantities
  (mass and coupling) that need to be independently adjustable.

---

## The Requirement: Independent Scales

To break the lock, a geometric dark-energy model must have:

**Independent mass scale:** The physical mass m must depend on at least
one parameter that the coupling g_eff does NOT depend on.

**Independent coupling scale:** The matter/photon/graviton coupling must
depend on at least one parameter that the mass does NOT depend on.

Schematically, we need a Lagrangian where canonical normalization gives:

```
m_phys = f(a, b, ...)
g_eff  = h(c, d, ...)
```

with {a, b, ...} ∩ {c, d, ...} not being a singleton that controls both.

---

## Success Condition

A candidate model succeeds (FULLY_UNLOCKED) if:

1. **Light mass is achievable:** m ~ H₀ or m ~ meV is possible without
   requiring an unnaturally large dimensionless coupling.

2. **Coupling remains relevant:** g_eff at the light-mass point is at
   least gravitational strength (g_eff ≳ 1/M_Pl).

3. **Mass is technically natural:** m = 0 restores a symmetry (shift,
   gauge, chiral, discrete) or the mass is radiatively stable by some
   structural mechanism.

4. **No new pathologies:** The model is ghost-free, tachyon-free, and
   perturbatively consistent at the relevant scales.

A model is PARTIALLY_UNLOCKED if it satisfies (1) and (2) but fails (3).

A model is LOCKED if it fails (2) — i.e., the coupling still vanishes
in the light-mass limit.

---

## What we are NOT trying to do

- We are NOT trying to derive w = -1. That remains an open problem.
- We are NOT trying to match specific observational data.
- We ARE trying to find a geometric field theory where a cosmologically
  light degree of freedom retains observable coupling to matter or
  gravity. This is a necessary (not sufficient) condition for geometric
  dark energy.
