# Foundation E — Candidate Mechanisms

**Date:** 2026-03-14

---

## Candidate A: Vacuum Energy Sequestering (Kaloper-Padilla)

### Core idea
Introduce global (spacetime-averaged) variables that enforce
cancellation of vacuum energy contributions from matter loops.
The residual Λ is determined by the HISTORY of the universe,
not by the current vacuum.

### Action structure
```
S = ∫ d⁴x √g [½M_Pl² R - Λ_bare + L_matter]
    + σ₁[Λ_bare ∫d⁴x √g - μ₁⁴]
    + σ₂[∫d⁴x √g L_matter / ∫d⁴x √g - μ₂⁴]
```
where σ₁, σ₂ are global Lagrange multipliers (spacetime constants)
and μ₁, μ₂ are mass scales.

The σ equations enforce:
- Λ_bare adjusts to cancel any constant vacuum shift
- The effective Λ is set by the ratio μ₁⁴/μ₂⁴ and the spacetime
  4-volume, which is a GLOBAL quantity

### Why it could evade A–D barriers
- No local propagating field needed (no lock, no suppression)
- Not a scalar-tensor EFT (no universality collapse)
- Operates on the action integral, not on field equations
- The cancellation is exact for any constant vacuum shift

### Biggest risk
- Requires integration over the FULL spacetime 4-volume (potentially
  acausal or requires future boundary conditions)
- The residual Λ depends on global quantities that may not be
  calculable
- The mechanism may relocate tuning to the choice of μ₁, μ₂

### Potential observable signature
- Modified vacuum energy evolution near phase transitions
- Constraint: total vacuum energy shift across a transition must
  be absorbed by the global variables
- Possible relation between spacetime 4-volume and Λ

### Addresses: naturalness (partial), coincidence (no)

---

## Candidate B: 4-Form / Flux Adjustment Sectors

### Core idea
Introduce a 4-form field strength F₄ = dA₃ whose equation of
motion enforces a constant flux q. The vacuum energy is neutralized
by adjusting q to cancel matter-loop contributions.

### Action structure
```
S = ∫ d⁴x √g [½M_Pl² R - (1/48)F_μνρσF^μνρσ + qF₄ε⁴ + L_matter]
```
F₄ = dA₃ has no propagating d.o.f. in 4D. Its equation of motion
gives F_μνρσ = q ε_μνρσ, contributing an effective Λ_eff = q²/2.

Membrane nucleation can adjust q in discrete steps Δq ~ e/M_Pl²,
relaxing the CC toward zero (Bousso-Polchinski mechanism).

### Why it could evade A–D barriers
- F₄ has NO propagating degrees of freedom → no mass, no coupling, no lock
- Purely topological/algebraic in 4D → not a scalar-tensor EFT
- Compatible with ANY gravity theory (including EC/PGT with torsion)

### Biggest risk
- Requires a landscape of vacua → anthropic reasoning may be unavoidable
- Discrete adjustment: Δq sets the minimum achievable Λ, which
  requires an exponentially large number of flux values to reach
  Λ ~ 10⁻¹²² M_Pl⁴
- Membrane nucleation dynamics are speculative

### Potential observable signature
- Discrete vacuum energy spectrum → possible relics of transitions
- Constraints on membrane nucleation rates
- In a bounce context: the bounce may select a specific q sector

### Addresses: naturalness (partial, via adjustment), coincidence (no)

---

## Candidate C: Global Constraint / Lagrange Multiplier Vacuum Selection

### Core idea
Impose a global constraint on the spacetime integral of a geometric
quantity (scalar curvature, Gauss-Bonnet, Euler density) through a
Lagrange multiplier. The constraint fixes the effective Λ.

### Action structure
```
S = ∫ d⁴x √g [½M_Pl² R + L_matter]
    + λ[∫d⁴x √g R - χ₀]
```
where λ is a global Lagrange multiplier and χ₀ is a topological
or fixed parameter.

The λ equation enforces ∫√g R = χ₀, which constrains the average
curvature and hence the effective vacuum energy.

### Why it could evade A–D barriers
- λ is a GLOBAL variable, not a local field → no propagation, no lock
- Constraint is geometric (∫R) → potentially connects to torsion/bounce
- Not a scalar-tensor EFT (it modifies the variational principle, not
  the local equations)

### Biggest risk
- The constraint is a SINGLE equation for one global variable. It may
  not have enough structure to control vacuum energy at each scale.
- May be equivalent to choosing Λ by hand (if χ₀ must be tuned)
- The variational principle may be ill-posed (boundary terms, non-locality)

### Potential observable signature
- The constraint ∫√g R = χ₀ links the TOTAL curvature history to a
  fixed value. In a bounce cosmology, the bounce contributes a large
  positive curvature pulse. This constrains the late-time curvature
  (and hence Λ).
- Possible bounce-Λ correlation

### Addresses: naturalness (no), coincidence (potentially)

---

## Candidate D: Nonlocal Gravitational Action Terms

### Core idea
Modify the gravitational action with nonlocal terms (involving □⁻¹R
or similar) that generate a late-time effective cosmological constant
without a local scalar field.

### Action structure (Deser-Woodard type)
```
S = ∫ d⁴x √g [½M_Pl² R(1 + f(□⁻¹R)) + L_matter]
```
where f is a dimensionless function and □⁻¹ is the retarded Green's
function of the d'Alembertian.

On FRW, □⁻¹R is a monotonically growing function of time. If f is
chosen appropriately, the effective Newton's constant evolves to
produce late-time acceleration.

### Why it could evade A–D barriers
- No new propagating d.o.f. at the fundamental level → no lock
- The nonlocality is RETARDED (causal) → no acausality
- Not a standard scalar-tensor EFT (though it can be rewritten as one
  with auxiliary fields — this is the main risk)

### Biggest risk
- **Auxiliary field equivalence:** Deser-Woodard models can be rewritten
  as local scalar-tensor theories with two auxiliary scalars. If this
  rewriting is physical (not just mathematical), the model IS a
  scalar-tensor EFT, and Foundation C applies.
- The function f must be chosen to match observations → potential
  hidden fine-tuning
- Nonlocal actions have subtleties with initial conditions and
  quantization

### Potential observable signature
- Modified growth rate of structure (different from ΛCDM)
- Time-dependent effective Newton's constant
- Specific f(□⁻¹R) functional form may be constrained by data

### Addresses: naturalness (no), coincidence (partially, via dynamical mechanism)

---

## Candidate E: Boundary / Topological Vacuum Selection

### Core idea
The vacuum energy is determined by boundary conditions or topological
data of the spacetime, not by bulk dynamics. In a bounce cosmology,
the "boundary" is the bounce itself — the transition from contraction
to expansion.

### Action structure
```
S = S_bulk + S_boundary
S_boundary = ∫_∂M d³x √h [K + α₁ R_∂ + α₂ ...]
```
where the boundary terms determine the effective Λ through junction
conditions at the bounce.

Alternatively, topological invariants (Euler characteristic, Pontryagin
class) of the full spacetime may constrain the integrated curvature
and hence the average vacuum energy.

### Why it could evade A–D barriers
- Boundary/topological data is global → no local propagating field
- Operates at the level of the spacetime manifold → not EFT
- The bounce provides a natural "boundary" even in a compact spacetime

### Biggest risk
- Topological invariants of FRW spacetimes are trivial (χ = 0 for
  non-compact spatial sections). The mechanism may require non-trivial
  topology.
- Junction conditions at the bounce may not constrain Λ — they
  typically constrain the Hubble rate and its derivative, not the
  vacuum energy separately.
- Speculative: no well-developed framework exists

### Potential observable signature
- Relations between spacetime topology and Λ
- Bounce junction conditions constraining Λ
- Requires non-trivial spatial topology → testable through CMB
  topology searches

### Addresses: naturalness (potentially), coincidence (no)

---

## Summary

| Candidate | Core idea | Evades A–D? | Biggest risk | Addresses |
|-----------|-----------|-------------|-------------|-----------|
| A: Sequestering | Global Lagrange multipliers cancel Λ_vac | Yes | Acausality / hidden tuning | Naturalness (partial) |
| B: 4-form flux | Membrane nucleation adjusts flux | Yes | Landscape / anthropic | Naturalness (partial) |
| C: Global constraint | ∫√g R = χ₀ fixes average curvature | Yes | Equivalent to hand-tuning? | Coincidence (potential) |
| D: Nonlocal action | □⁻¹R generates late-time Λ | Partially | Reduces to scalar-tensor | Coincidence (partial) |
| E: Boundary/topological | Bounce boundary conditions fix Λ | Yes | No developed framework | Naturalness (potential) |

### Initial Assessment

**Most promising for Phase 2:** Candidates A (sequestering) and C
(global constraint), because they have the clearest action structure
and the most natural connection to bounce cosmology.

**Highest risk of collapse:** Candidate D (nonlocal action), because
it may reduce to a scalar-tensor theory via auxiliary fields.

**Most speculative:** Candidate E (boundary/topological), because no
calculational framework exists.
