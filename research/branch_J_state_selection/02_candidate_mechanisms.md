# Candidate State-Selection Mechanisms

**Date:** 2026-03-16

---

## The Unique Channel: Curvature Coupling

From the problem statement, curvature coupling (ξRφ²) is the
unique channel that is both strong at the bounce and naturally
weak at late times. All five candidates below use some form of
curvature coupling as the bounce-to-dark-sector bridge.

The spin-torsion-specific coupling (J⁵)² requires introducing
dark fermions AND a dark-fermion-to-dark-scalar coupling, which
is not minimal. We note it where relevant but do not build
entire mechanisms around it.

---

## Candidate A: pNGB Misalignment via Curvature Kick

### Action

```
L = (∂φ)²/2 + Λ⁴[1 - cos(φ/f)] + ξRφ²/2
```

φ is an axion-like DE field with:
- f ~ M_Pl (decay constant)
- m² = Λ⁴/f² ~ H₀² (DE mass)
- Λ⁴ ~ m²f² ~ H₀² M_Pl² ~ 10⁻¹²² M_Pl⁴

### Bounce coupling

The non-minimal coupling ξRφ² gives an effective potential
at the bounce:

```
V_eff = Λ⁴[1 - cos(φ/f)] + ξR_b φ²/2
```

where R_b ≈ 21 M_Pl².

For ξ ~ O(1): the curvature term ξR_b ~ 21 M_Pl² dominates
over the axion mass m² ~ H₀² by a factor of 10¹²². The
effective potential is a steep parabola centered at φ = 0,
with the cosine potential negligible.

### How the bounce changes the state

**During the bounce:** The field experiences a force
F = -ξRφ toward φ = 0 (for ξ > 0). The effective frequency:

```
ω_eff = √(ξR_b) ≈ √(21ξ) M_Pl
```

The bounce duration is t_b ~ 1/M_Pl (more precisely, R(t)
is significant for |t| ≲ t_Pl). So the field completes:

```
N_osc = ω_eff × t_b / (2π) ≈ √(21ξ)/(2π)
```

For ξ = 1: N_osc ≈ 0.73 (less than one oscillation).
For ξ = 10: N_osc ≈ 2.3 (about two oscillations).

The field is DRIVEN toward φ = 0 but does NOT settle there
(no dissipation during the bounce — H ≈ 0 means no Hubble
friction at the bounce instant).

### What late-time quantity is affected

The misalignment angle θ_i = φ(t_after)/f, which determines:

```
ρ_DE = Λ⁴[1 - cos(θ_i)] ≈ Λ⁴ θ_i²/2   (for small θ_i)
```

### Biggest theoretical risk

**Arbitrary initial conditions collapse.** The post-bounce θ_i
depends on the pre-bounce θ and θ̇. The bounce modifies θ by
O(1) (for ξ ~ 1) but does not erase the pre-bounce information.
The mapping θ_pre → θ_post is approximately:

```
θ_post ≈ θ_pre × cos(√(21ξ) × effective_time)
        + θ̇_pre/(√(21ξ) M_Pl) × sin(√(21ξ) × effective_time)
```

This is a ROTATION in (θ, θ̇) phase space, not a CONTRACTION.
Information is preserved, not narrowed.

**For narrowing to occur, we need DISSIPATION or IRREVERSIBILITY
during the bounce.** The bounce provides neither (H ≈ 0,
time-symmetric about t = 0 at leading order).

### Risk assessment: HIGH (likely collapses to initial conditions)

---

## Candidate B: Discrete Multi-Vacuum Branch Selection

### Action

```
L = (∂φ)²/2 + V(φ) + ξRφ²/2
```

where V(φ) has N degenerate (or near-degenerate) minima at
φ = φ_1, φ_2, ..., φ_N with barriers V_barrier between them.

Example: V = V₀[1 - cos(Nφ/f)]²/4 gives N minima.

### Bounce coupling

At the bounce: the curvature coupling adds ξR_b φ²/2 to V(φ).
If ξR_b ≫ V_barrier/φ²: the barriers are washed out and the
effective potential has a single minimum at φ = 0 (for ξ > 0).

```
ξR_b φ² ~ ξ × 21 M_Pl² × v²    (for φ ~ v ~ min separation)
V_barrier ~ Λ⁴ ~ 10⁻¹²² M_Pl⁴
```

For v ~ f ~ M_Pl: ξR_b v² ~ 21ξ M_Pl⁴ ≫ V_barrier.
The barriers are obliterated during the bounce.

### How the bounce changes the state

**Phase 1 (bounce peak):** All barriers erased. Single minimum
at φ ≈ 0. Field driven toward 0.

**Phase 2 (bounce exit):** R(t) decreases, barriers re-form.
The field is near φ ≈ 0 (the symmetric point). As barriers
re-form, the field falls into the nearest minimum.

**Which minimum?** The one closest to φ = 0 in the original
potential. For a Z_N-symmetric potential: this is the minimum
at φ = 0 (if it exists) or the two minima straddling φ = 0
(with selection determined by residual velocity).

### What late-time quantity is affected

The vacuum label (which of the N minima the field occupies).
Each minimum has a slightly different vacuum energy:

```
V(φ_n) = V₀ + ΔV_n    (with ΔV_n = landscape splitting)
```

### Biggest theoretical risk

**Selection is determined by the POTENTIAL, not the bounce.**

The bounce drives φ → 0 and the potential then determines
where the field falls. The bounce acts as a RESET to the
symmetric point — any sufficiently violent event (inflation,
reheating) would do the same. The spin-torsion bounce has no
special role.

Moreover, "the field falls to the minimum closest to φ = 0"
is a property of V(φ), not of the bounce. The bounce provides
no predictive content about V(φ).

### Risk assessment: HIGH (bounce is generic reset, not specific selector)

---

## Candidate C: Symmetry Restoration and Re-Breaking

### Action

```
L = (∂φ)²/2 + μ²φ²/2 - λφ⁴/4 + ξRφ²/2
```

Standard Mexican-hat potential with curvature coupling.
Symmetry-breaking scale: v² = μ²/λ.

### Bounce coupling

Effective mass at the bounce:

```
m_eff² = -μ² + ξR_b = -μ² + 21ξ M_Pl²
```

For μ ~ meV and ξ ~ O(1): m_eff² ≈ 21ξ M_Pl² > 0.
The symmetry is RESTORED at the bounce (the field is driven
to the symmetric point φ = 0).

### How the bounce changes the state

**Pre-bounce:** Field in one of two minima (φ = ±v).
**At bounce:** Symmetry restored, field driven to φ = 0.
**Post-bounce:** Symmetry re-breaks. Field at φ ≈ 0 (unstable
maximum) rolls to one of the two minima.

### Which minimum?

Determined by:
1. Residual velocity from pre-bounce state (memory)
2. Quantum fluctuations (random)
3. Explicit symmetry breaking (if any small ε φ term exists)

For exact Z₂ symmetry: the selection is determined by the
pre-bounce velocity. Field coming from φ = +v has positive
velocity → rolls back to φ = +v. NO CHANGE. The bounce
merely temporarily displaces the field but it returns to its
original vacuum.

**The bounce does not change the vacuum branch for a
Z₂-symmetric potential.** The pre-bounce state is restored.

For broken Z₂ (small ε φ): the field always ends up in the
lower-energy minimum, regardless of pre-bounce state. But
this is determined by ε (a parameter of V), not by the bounce.

### What late-time quantity is affected

The vacuum label (±v). The vacuum energy V(±v) = -μ⁴/(4λ)
is the SAME for both minima (Z₂ symmetry). No observable
difference.

### Biggest theoretical risk

**No physical distinction between vacua** (for Z₂-symmetric case).
**Selection by potential, not bounce** (for broken Z₂).

### Risk assessment: VERY HIGH (no predictive content)

---

## Candidate D: Metastable Vacuum Trapping via Bounce Potential Deformation

### Action

```
L = (∂φ)²/2 + V(φ) + ξRφ²/2
```

where V(φ) has a metastable minimum (local minimum) at φ_meta
and a global minimum at φ_true, separated by a barrier.

Example: V = V₀[(φ/v)² - 1]²[(φ/v) - a]   with a ≪ 1
(slightly tilted double-well).

### Bounce coupling

At the bounce, the effective potential:

```
V_eff = V(φ) + ξR_b φ²/2
```

The curvature term can:
1. RAISE the barrier (if ξ > 0 and the barrier is between
   φ_meta and φ_true where both are away from φ = 0)
2. LOWER the barrier (if the barrier region is near φ = 0)
3. CREATE a new minimum (if ξR_b provides a restoring force
   to φ = 0 that competes with V(φ))

### How the bounce changes the state

**Scenario 1 (trapping):** If the field is in a shallow
metastable minimum and the bounce raises the barrier, the
field is TRAPPED. After the bounce, the enhanced barrier
persists briefly, preventing tunneling. The field remains in
the metastable state.

BUT: the barrier enhancement is proportional to R, which
decreases after the bounce. The barrier returns to its original
height. The trapping is TRANSIENT — the field's tunneling rate
returns to its pre-bounce value. No permanent change.

**Scenario 2 (release):** If the field is in a metastable
minimum and the bounce lowers the barrier, the field escapes
to the true vacuum. This IS a permanent change.

The release condition: ξR_b > V_barrier. For V_barrier ~ Λ⁴/v²
and ξR_b ~ M_Pl²: release occurs when M_Pl² > Λ⁴/v². With
Λ⁴ ~ 10⁻¹²² M_Pl⁴ and v ~ M_Pl: V_barrier ~ 10⁻¹²² M_Pl²
≪ M_Pl². The barrier is ALWAYS negligible compared to the
curvature coupling.

**Consequence:** The bounce ALWAYS releases the field from any
metastable minimum with DE-scale barriers. The field ends up
near φ = 0 (the curvature-coupling minimum) during the bounce,
then falls into whatever basin of V(φ) contains φ = 0.

This is the SAME outcome as Candidate B: the bounce resets the
field to φ ≈ 0, and V(φ) determines the rest.

### What late-time quantity is affected

Which vacuum (metastable or true) the field occupies post-bounce.
Answer: always the basin containing φ = 0 (for ξ > 0).

### Biggest theoretical risk

**Collapses to Candidate B.** The trapping is transient (no
permanent enhancement). The release is generic (all DE-scale
barriers are demolished). The outcome is determined by V(φ)
near φ = 0, not by the bounce.

### Risk assessment: HIGH (collapses to potential-determined reset)

---

## Candidate E: Nonadiabatic Excitation of a Dark Condensate

### Action

```
L = (∂χ)²/2 + m²χ²/2 + ξRχ²/2
```

χ is a dark scalar with mass m that forms a coherent condensate
(like axion dark matter). The bounce produces particle excitations
through nonadiabatic evolution.

### Bounce coupling

The mode equation for χ_k in conformal time:

```
v_k'' + [k² + (m² + ξR)a² - a''/a] v_k = 0
```

The effective frequency:

```
ω_k² = k²/a² + m² + ξR
```

At the bounce: ω̇/ω² ~ Ṙ/(ξR)^{3/2} ~ M_Pl³/M_Pl³ ~ 1.
The evolution is NONADIABATIC for modes with ω ~ M_Pl.

### How the bounce changes the state

Particle production via Bogoliubov transformation. The number
of produced particles:

```
n_k = |β_k|²
```

From the Branch H tensor calculation (same mathematical
structure): |β_k|² ~ (k_b/k)² for k ≪ k_b, with k_b ~ a_b M_Pl.

Energy density in produced particles:

```
ρ_prod = ∫ dk k² ω_k |β_k|² / (2π²a⁴)
```

After redshifting to today:

```
ρ_prod(today) ~ m × n_total × (a_b/a_0)³   (for non-relativistic)
                                              or
              ~ T_prod × (a_b/a_0)  × n_total  (for relativistic at production)
```

The (a_b/a_0)³ factor ~ 10⁻⁹⁷ provides enormous dilution.

### What late-time quantity is affected

The occupation number n_k, which determines:
- Energy density: ρ_DE = ω × n_total / a³
- Equation of state: w depends on whether χ is coherent
  (w ≈ -1 for slow-roll) or particle-like (w ≈ 0 for CDM)

### Biggest theoretical risk

**Same dilution as Branch H.** The energy in produced particles
is diluted by (a_b/a_0)³ ~ 10⁻⁹⁷ (for matter-like) or
(a_b/a_0)⁴ ~ 10⁻¹³⁰ (for radiation-like). The initial energy
at production is at most ~ M_Pl⁴ (for maximally efficient
production). After dilution:

```
ρ_today ≤ M_Pl⁴ × 10⁻⁹⁷ ~ 10⁻⁹⁷ M_Pl⁴
```

This is 10²⁵ times LARGER than ρ_DE ~ 10⁻¹²² M_Pl⁴.

**Wait — this might OVERPRODUCE, not underproduce!**

The issue: if the bounce produces too many particles in the
dark sector, the dark sector energy density exceeds the
observed DE value. This is the OPPOSITE of the dilution problem.

For m ~ H₀: the field starts oscillating when H ~ m ~ H₀
(i.e., today). Before that, the condensate energy is frozen:

```
ρ_χ ≈ m² χ₀² / 2    (frozen condensate)
```

The condensate amplitude: χ₀ = Δφ (the displacement at the
bounce). For ξ ~ 1: Δφ ~ M_Pl (Planck-scale displacement).
After redshifting from bounce: χ₀(today) ~ M_Pl × (a_b/a_0)
~ M_Pl × 10⁻³² ~ 10⁻³² M_Pl.

Then: ρ_χ ~ m² χ₀² ~ H₀² × (10⁻³² M_Pl)² ~ 10⁻⁶⁴ × 10⁻⁶⁴ M_Pl⁴
= 10⁻¹²⁸ M_Pl⁴.

This is 10⁶ BELOW ρ_DE. Close but not matching.

Hmm — this is actually the most QUANTITATIVELY INTERESTING
result so far. The bounce-produced condensate has energy
density within a few orders of magnitude of ρ_DE, unlike the
tensor spectrum which was off by 10⁶⁴.

BUT: the result depends sensitively on the field displacement
Δφ, which depends on the initial conditions. And the equation
of state would be w ≈ 0 (matter, not DE) once the field starts
oscillating at H ~ m.

For this to act as DE (w ≈ -1), we need m ≪ H₀ (the field
hasn't started oscillating yet). Then: ρ_χ = V(χ₀) ≈ m²χ₀²/2
is effectively a cosmological constant.

### Risk assessment: MODERATE (interesting numerology but
sensitive to initial conditions and doesn't give w ≈ -1
generically)

---

## Candidate Summary

| Candidate | Mechanism | Coupling | Risk | Most Promising? |
|-----------|-----------|----------|------|----------------|
| A: pNGB misalignment | Curvature drives θ toward 0 | ξRφ² | HIGH (rotation, not contraction) | Possibly |
| B: Multi-vacuum selection | Curvature erases barriers, field resets to φ ≈ 0 | ξRφ² | HIGH (determined by V, not bounce) | No |
| C: Symmetry restoration | Z₂ restored then re-broken | ξRφ² | VERY HIGH (no predictive content) | No |
| D: Metastable trapping | Curvature deforms barriers | ξRφ² | HIGH (collapses to B) | No |
| E: Nonadiabatic excitation | Particle production / condensate | ξRχ² + m² | MODERATE (interesting scaling) | Possibly |

**All five candidates rely on the same curvature coupling.**
**The bounce acts as a generic Planck-scale reset, not a
specific state selector.**

---

## The Overarching Problem

All five candidates share a common failure mode:

**The curvature coupling at the bounce (ξR ~ M_Pl²) completely
dominates over the DE potential (V ~ 10⁻¹²² M_Pl⁴). During
the bounce, the field moves in the curvature-induced potential,
ignoring the DE potential. After the bounce, the curvature drops
and the field evolves in the DE potential from whatever position
the curvature left it.**

**The post-bounce position depends on:**
1. The coupling ξ (a parameter, not determined by the bounce)
2. The pre-bounce state (an initial condition)
3. The time profile of R(t) (determined by the bounce, but
   gives only an O(1) factor)

**The bounce provides factor (3) only — an O(1) modification
to the state. Factors (1) and (2) are external inputs.**

This is the state-selection analog of the scale-separation
barrier: the bounce is too brief and too violent for the
delicate DE potential to matter during it, and the bounce
coupling is too crude to select a specific post-bounce state.

---

## What Would Save Branch J

The ONLY way out of this impasse:

1. **A non-perturbative or topological mechanism** where the
   bounce selects a discrete state label (not a continuous
   field value). The label persists regardless of the continuous
   evolution afterward.

2. **A dissipation mechanism at the bounce** that contracts phase
   space (many pre-bounce states → few post-bounce states). But
   the bounce has H ≈ 0 (no Hubble friction) and is essentially
   time-symmetric at leading order.

3. **A specific resonance** between the bounce time profile and
   a dark-sector frequency, amplifying a particular mode. This
   requires m_dark ~ M_Pl (Planck-scale dark sector), which is
   incompatible with DE (m_DE ~ H₀).

4. **Causal structure:** H = 0 at the bounce means the Hubble
   radius is infinite → the entire universe is causally connected
   at the bounce instant. This is unique to bouncing cosmologies.
   Could this prevent topological defect formation or enforce
   homogeneity in the dark sector?

Item (4) is the most interesting but leads to a NEGATIVE
prediction (suppression of defects/inhomogeneities, not creation
of a specific state).
