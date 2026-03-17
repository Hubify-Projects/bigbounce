# Foundation F — Candidate Field Models

**Date:** 2026-03-15

---

## Candidate A: Quintessence With Bounce-Set Displacement

### Potential

Inverse-power-law (Ratra-Peebles):
```
V(φ) = M^{4+α} / φ^α       (α > 0)
```

or exponential:
```
V(φ) = V₀ exp(-λ φ/M_Pl)
```

### Field equation
```
φ̈ + 3Hφ̇ + V'(φ) = 0
```

### How bounce sets initial conditions

At the bounce, the scalar is displaced by curvature coupling.
With a non-minimal coupling ξRφ²/2 in the action:

```
V_eff(φ) = V(φ) + ½ξRφ²
```

At the bounce: R ~ M_Pl². The curvature term ½ξM_Pl²φ² creates
an effective mass m²_eff = ξM_Pl² that pushes φ toward zero (for
ξ > 0). The equilibrium at the bounce is:

```
V'(φ_bounce) + ξM_Pl² φ_bounce = 0
```

For the inverse-power potential:
```
-αM^{4+α}/φ^{α+1} + ξM_Pl² φ = 0
φ_bounce^{α+2} = αM^{4+α}/(ξM_Pl²)
φ_bounce = [αM^{4+α}/(ξM_Pl²)]^{1/(α+2)}
```

### Parameters controlled by the bounce

- φ_bounce depends on M (potential scale), α, and ξ (coupling to curvature)
- ξ is a free parameter but of gravitational origin
- The bounce curvature M_Pl² enters explicitly

### Bounce-specific prediction?

φ_bounce is set by the balance between V'(φ) and ξM_Pl²φ. But M and
α are properties of the POTENTIAL, not of the bounce. The bounce
only contributes through M_Pl² (the curvature scale), which is the
same regardless of the specific bounce model.

**Any high-curvature epoch (inflation, bounce, Planck era) gives the
same φ_bounce.** The result is bounce-compatible but not bounce-specific.

### Attractor behavior

The inverse-power quintessence has a well-known TRACKER attractor:
for a wide range of φ_i, the field converges to a common late-time
trajectory. The tracker is:

```
ρ_φ/ρ_background = α/(α + 2) × (1 + w_bg)     [during tracking]
```

**If the tracker attractor operates, φ_i is irrelevant — all initial
conditions converge to the same late-time state.** This is GOOD for
avoiding fine-tuning but BAD for predictive power: the bounce initial
conditions are washed out.

---

## Candidate B: Pseudo-Nambu-Goldstone Boson (pNGB) With Bounce-Set Misalignment

### Potential

```
V(θ) = Λ⁴(1 - cos(θ/f))
```

where θ is the angular variable, f is the decay constant, and Λ is
the symmetry-breaking scale.

### Field equation
```
θ̈ + 3Hθ̇ + (Λ⁴/f) sin(θ/f) = 0
```

### How bounce sets initial conditions

The misalignment angle θ_i is the key parameter. In standard axion
cosmology, θ_i is a random initial condition (set during inflation).
In a bounce cosmology, the question is whether the bounce determines θ_i.

**Mechanism 1: Curvature-induced misalignment**

If θ couples to R through a term like (α/f)θR in the action, the
bounce curvature pushes θ away from θ = 0:

```
θ̈ + 3Hθ̇ + (Λ⁴/f)sin(θ/f) = -(α/f)R

At the bounce: R ~ M_Pl², so the driving term is ~ (α/f)M_Pl²
```

The induced displacement is:
```
θ_i ~ (α/f) M_Pl² / (Λ⁴/f²) = α f / Λ⁴ × M_Pl²
```

For Λ ~ 10⁻³ eV (DE scale) and f ~ M_Pl:
```
θ_i/f ~ α M_Pl² / Λ⁴ × f ~ α × 10¹²² × M_Pl
```

This is ENORMOUS — far beyond the periodic range [0, 2πf]. The
field wraps many times and θ_i mod 2π is effectively RANDOM.

**The curvature-induced displacement is too large to be useful.
θ_i becomes effectively random, not predictive.**

**Mechanism 2: Torsion-induced misalignment**

If θ couples to the Nieh-Yan density (αθN₄), the bounce torsion
drives θ. But Foundation B showed that this coupling either
preserves shift symmetry (topological N₄, no geometric content) or
breaks it (mass unprotected). The topological-shift duality applies.

**Mechanism 3: Freeze-out at bounce Hubble scale**

Just after the bounce, H rises rapidly to H ~ M_Pl. If
m_θ = Λ²/f ≪ H_bounce ~ M_Pl (which is always true for DE-scale
masses), the field is FROZEN by Hubble friction during and after
the bounce:

```
θ̈ + 3H_bounce θ̇ ≈ 0     (V' negligible when m ≪ H)
```

θ is frozen at whatever value it had during the contracting phase.
The bounce does not SET θ_i — it merely PRESERVES the pre-bounce
value.

### Parameters controlled by the bounce

- The bounce does NOT determine θ_i (it's inherited from the pre-bounce era)
- The bounce curvature over-drives θ_i to random values if coupled
- The pNGB mass Λ²/f is NOT set by the bounce

### Attractor behavior

For θ_i ≲ πf (not too close to the hilltop): the field oscillates
after H drops below m_θ, giving w ~ 0 (dark matter, not DE).

For θ_i very close to πf (hilltop): the field is nearly frozen,
giving w ≈ -1 (thawing DE). But this requires:

```
|θ_i - πf| / f < H₀/m_θ ~ 10⁻³⁰ (for m_θ ~ meV)
```

**Hilltop quintessence from a pNGB requires extreme fine-tuning of
θ_i.** The bounce provides no mechanism to place θ_i near the hilltop
with this precision.

---

## Candidate C: Thawing/Freezing Scalar With Bounce-Prepared Attractor Entry

### Concept

Use a scalar field that enters a tracking or scaling attractor
during the radiation era, with the attractor entry time determined
by bounce-era initial conditions.

### Potential

Exponential:
```
V(φ) = V₀ exp(-λφ/M_Pl)
```

The exponential potential has the scaling solution:
```
Ω_φ = 3(1 + w_bg)/λ²
w_φ = w_bg
```

The field "scales" with the background (ρ_φ ∝ ρ_bg) during radiation
and matter eras.

### How bounce sets initial conditions

The field starts at φ_i set by the bounce (curvature displacement
as in Candidate A). The time to reach the scaling attractor depends
on φ_i:

- If φ_i is far from the attractor: the field overshoots, oscillates,
  and eventually settles onto the attractor. The transient duration
  depends on φ_i.
- If φ_i is on the attractor from the start: immediate tracking.

### The problem

The scaling solution has Ω_φ = const ≠ 1 during radiation and matter
eras. For the field to produce dark energy (Ω_φ → 1 today), the
potential must STEEPEN or the field must EXIT the attractor.

Standard resolution: use a potential that transitions from exponential
to flat (e.g., SUGRA-inspired or double-exponential). The exit from
scaling occurs when the potential changes shape at φ ~ φ_exit.

### Parameters controlled by the bounce

- φ_i: set by curvature coupling (as in Candidate A)
- The attractor entry time: depends on φ_i, but the attractor
  itself is independent of φ_i
- φ_exit: set by the POTENTIAL, not by the bounce
- V₀: set by the requirement ρ_DE ~ 10⁻¹²² M_Pl⁴, not by the bounce

### Attractor behavior

**The tracker attractor ERASES memory of φ_i.** By definition,
the attractor is the solution to which all initial conditions
converge. Once the field is tracking, φ_i is forgotten.

The only information that survives is WHEN the field reached the
attractor. If φ_i is large, the field takes longer to settle.
But this timing difference is logarithmic in φ_i:

```
Δt_entry ~ (1/H) ln(φ_i/φ_attractor)
```

For φ_i ~ M_Pl (bounce-set) vs φ_i ~ 10M_Pl: Δt_entry ~ ln(10)/H,
which is ~ 1 Hubble time. This is not observationally distinguishable.

---

## Candidate D: Hilltop Field Displaced by Spin-Torsion Coupling

### Concept

A scalar field sitting at the top of a very flat potential (hilltop
quintessence). The bounce provides a tiny kick that determines which
direction it rolls.

### Potential
```
V(φ) = V₀ - ½μ²φ² + λφ⁴/4     (μ ~ H₀ ~ 10⁻³³ eV)
```

### How bounce sets initial conditions

The spin-torsion interaction at the bounce generates a coupling
between φ and fermion bilinears. If this coupling is parity-violating,
it generates a tiny asymmetric displacement:

```
δφ ~ (coupling) × ⟨spin density⟩ / m²_eff
```

At the bounce: ⟨s⟩ ~ M_Pl³, coupling ~ 1/M_Pl². So:

```
δφ ~ M_Pl³/M_Pl² / μ² = M_Pl/μ² ~ M_Pl/H₀² ~ 10⁹³ M_Pl
```

This is absurdly large. The field is displaced far from the hilltop
immediately.

Alternatively, if the coupling is gravitational strength (~ 1/M_Pl⁴):
```
δφ ~ M_Pl³/M_Pl⁴ / μ² = 1/(M_Pl μ²) ~ 1/(M_Pl H₀²) ~ 10²⁷ eV⁻¹
```

Still enormous in units of the field range (which is ~ V₀^{1/4}/μ
~ H₀/H₀ ~ 1 in natural units around the hilltop).

**The bounce kick is too strong for hilltop quintessence.** The field
is immediately knocked off the hilltop, rolls to the minimum, and
gives w ~ -1 only transiently (if at all).

### The fine-tuning problem

Hilltop quintessence requires the field to start within:
```
|φ_i| < φ_c ~ μ/√λ ~ H₀/(coupling)
```

of the hilltop. The bounce displacement δφ ~ M_Pl (or larger)
vastly exceeds φ_c ~ H₀. The bounce does not provide the required
precision.

---

## Summary

| Candidate | φ_i from bounce | Attractor? | DE produced? | Predictive? |
|-----------|----------------|-----------|-------------|------------|
| A: Quintessence | φ_i ~ (M^{4+α}/M_Pl²)^{1/(α+2)} | Tracker erases φ_i | Yes (generic) | No (attractor washout) |
| B: pNGB | Random (curvature over-drives) | Hilltop requires 10⁻³⁰ tuning | Only near hilltop | No (random + tuned) |
| C: Thawing/freezing | φ_i ~ M_Pl (generic) | Tracker erases φ_i | Yes (generic) | No (logarithmic sensitivity) |
| D: Hilltop + spin kick | δφ ~ M_Pl (too large) | Kicked off hilltop | No (falls to minimum) | No (kick too strong) |

**No candidate produces a predictive bounce-DE connection.**

The fundamental tension: either
1. The attractor erases bounce information (A, C) → DE is generic, bounce irrelevant
2. The bounce displacement is too large for sensitive potentials (B, D) → fine-tuning required anyway
