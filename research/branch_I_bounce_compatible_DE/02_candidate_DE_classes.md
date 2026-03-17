# Branch I: Candidate DE Classes

**Date:** 2026-03-15

---

## Class 1: Cosmological Constant (Λ)

### Description
Λ is a constant in the action. It does not evolve, does not
couple to matter, and has no dynamics.

### Compatibility with bounce
**TRIVIALLY COMPATIBLE.** Λ enters the Friedmann equation as an
additive constant. At the bounce (ρ ~ M_Pl⁴), Λ ~ 10⁻¹²² M_Pl⁴
is negligible. The bounce is completely insensitive to Λ:

```
δρ_b / ρ_crit ~ Λ/ρ_crit ~ 10⁻¹²²
```

### Nontrivial constraint?
**NONE.** The bounce neither constrains nor is constrained by Λ.

---

## Class 2: Quintessence (Canonical Scalar Field)

### Description
A light scalar φ with potential V(φ) and canonical kinetic term.
Various potentials: inverse power-law, exponential, PNGB, etc.

### Compatibility with bounce
**GENERALLY COMPATIBLE** with caveats:

1. At the bounce, φ has kinetic + potential energy. Both contribute
   to ρ_total. As long as ρ_φ ≪ ρ_crit, the scalar does not affect
   the bounce.

2. For V(φ) ~ ρ_DE ~ 10⁻¹²² M_Pl⁴: negligible at bounce.

3. **Potential concern:** If φ has a steep potential, the bounce
   curvature (R ~ M_Pl²) may displace φ through non-minimal
   coupling ξRφ². This was studied in Foundation F — the
   displacement is to φ ~ O(M_Pl) or φ ~ 0, neither of which is
   problematic for late-time DE (attractor erases initial condition
   anyway).

### Nontrivial constraint?
**WEAK.** The bounce may exclude quintessence models where
ρ_φ(early) > ρ_crit, but this is an extreme fine-tuning regime
that is already excluded by other considerations.

---

## Class 3: K-essence (Non-Canonical Kinetic Terms)

### Description
Scalar field with Lagrangian L = P(X, φ) where X = -½(∂φ)².
Includes DBI, ghost condensate, kinetic gravity braiding, etc.

### Compatibility with bounce
**POTENTIALLY NONTRIVIAL.**

The bounce modifies the effective metric for perturbations. In
k-essence, the sound speed c_s² = P_X/(P_X + 2X P_XX) depends on
the background. At the bounce:

1. If P_XX is large (DBI-like), the sound speed may become
   imaginary during the bounce → gradient instability
2. The effective metric for scalar perturbations may have wrong
   signature during the bounce transition
3. Ghost condensate requires NEC violation — the bounce provides
   NEC violation through spin-torsion, potential conflict

### Nontrivial constraint?
**POSSIBLE.** K-essence models with c_s² sensitive to background
curvature may be destabilized by the bounce. This requires
explicit computation.

---

## Class 4: Modified Gravity DE (f(R), Horndeski, DHOST)

### Description
Dark energy from modifications to gravity: f(R), Brans-Dicke,
Horndeski (generalized scalar-tensor), DHOST (beyond Horndeski).

### Compatibility with bounce
**POTENTIALLY INCOMPATIBLE.**

Key issues:
1. **f(R):** In EC gravity, f(R) includes torsion contributions
   to R. The f(R) modification changes the bounce dynamics.
   Compatibility requires f(R_bounce) ≈ R_bounce (modification
   negligible at Planck curvature).

2. **Horndeski:** The four Horndeski functions G₂, G₃, G₄, G₅
   couple to curvature. At the bounce, curvature is maximal.
   The Horndeski sector is NOT negligible — it is MAXIMALLY
   active at the bounce. This could prevent the bounce or
   introduce instabilities.

3. **DHOST:** Beyond-Horndeski theories may violate the conditions
   needed for a healthy bounce (e.g., may introduce Ostrogradski
   ghosts that are excited at Planck curvature).

### Nontrivial constraint?
**LIKELY YES.** Modified gravity DE operates at low curvature but
its UV behavior at the bounce may be pathological. This is the
most promising direction for nontrivial constraints.

---

## Class 5: Vacuum Energy Sequestering

### Description
Kaloper-Padilla mechanism: global Lagrange multipliers cancel
vacuum energy, leaving a residual Λ determined by spacetime
four-volume.

### Compatibility with bounce
**COMPATIBLE BUT DISCONNECTED** (Foundation E result).

The bounce provides finite four-volume (needed for sequestering),
but the bounce contributes negligibly to V₄ (scale separation:
V₄^bounce/V₄^total ~ 10⁻³²). Sequestering works with or without
the bounce.

### Nontrivial constraint?
**NONE.** Confirmed by Foundations E and G.

---

## Class 6: Interacting Dark Energy (DE-DM Coupling)

### Description
Dark energy coupled to dark matter through energy exchange:
Q_μ = ξ H ρ_DM u_μ or similar.

### Compatibility with bounce
**COMPATIBLE** if the interaction is weak enough to be negligible
at the bounce. At ρ ~ M_Pl⁴, the dark matter density is a
negligible fraction, so DE-DM interactions are irrelevant.

### Nontrivial constraint?
**WEAK.** The bounce constrains only the UV behavior of the
interaction, which is already required to be well-behaved by other
considerations.

---

## Class 7: Massive Gravity / Bigravity

### Description
Dark energy from a graviton mass m_g ~ H₀ ~ 10⁻³³ eV.

### Compatibility with bounce
**POTENTIALLY INCOMPATIBLE.**

In massive gravity, the reference metric f_μν must be specified.
At the bounce, the physical metric g_μν undergoes extreme
dynamics. The massive gravity interaction term:

```
S_mass ~ m_g² ∫ √g Σ_n β_n e_n(√(g⁻¹f))
```

may become singular or ill-defined when g_μν passes through the
bounce (where ȧ = 0 and ä > 0).

Additionally: the Boulware-Deser ghost, which is absent in dRGT
massive gravity at low energy, may reappear at Planck curvature.

### Nontrivial constraint?
**POSSIBLE.** Requires checking the ghost structure of dRGT at
Planck curvature.

---

## Summary

| DE Class | Compatible? | Nontrivial constraint? | Priority |
|----------|------------|----------------------|----------|
| Λ | YES (trivial) | NONE | LOW |
| Quintessence | YES | WEAK | LOW |
| K-essence | LIKELY | POSSIBLE (stability) | MEDIUM |
| Modified gravity | POSSIBLY NOT | LIKELY (UV behavior) | **HIGH** |
| Sequestering | YES | NONE (confirmed) | LOW |
| Interacting DE | YES | WEAK | LOW |
| Massive gravity | POSSIBLY NOT | POSSIBLE (ghost) | **MEDIUM** |
