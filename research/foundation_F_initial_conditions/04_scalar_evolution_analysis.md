# Foundation F — Scalar Evolution Analysis

**Date:** 2026-03-15

---

## Question

Given bounce-set initial conditions (φ_i ~ M_Pl or φ_i ~ 0), does
the scalar field evolve to produce dark energy at late times? And does
the result depend meaningfully on the specific φ_i?

---

## Evolution Through Cosmological Eras

### The field equation

```
φ̈ + 3H(t)φ̇ + V'(φ) = 0
```

The Hubble parameter H(t) acts as FRICTION. When H ≫ m_φ = √V''(φ),
the field is frozen. When H < m_φ, the field rolls or oscillates.

### Timeline

```
Bounce: t ~ t_Pl,     H ~ 0 → M_Pl (rapidly)
Rad.:   t ~ 10⁻¹⁰ s,  H ~ 10¹⁸ GeV → decreasing as 1/2t
Equal.: t ~ 10¹² s,    H ~ 10⁻²⁸ eV
Today:  t ~ 10¹⁷ s,    H ~ 10⁻³³ eV
```

For a DE-scale scalar: m_φ ~ H₀ ~ 10⁻³³ eV. This means:

```
H ≫ m_φ for t < t_today    (frozen for entire cosmic history)
H ~ m_φ at t ~ t_today     (begins to thaw NOW)
```

### The freezing problem

A scalar with m ~ H₀ is frozen by Hubble friction for the ENTIRE
history from the bounce to today. Its value at t_today is
approximately equal to its initial value:

```
φ(t_today) ≈ φ_i     (to excellent approximation)
```

The field barely moves. Its kinetic energy is negligible. It acts
as a cosmological constant with:

```
ρ_φ ≈ V(φ_i)
w_φ ≈ -1
```

**The DE density is V(φ_i), determined entirely by the initial
condition and the potential.**

---

## Model-by-Model Evolution

### Candidate A: Inverse-Power Quintessence

```
V = M^{4+α}/φ^α
```

**Tracker behavior:**

For α > 0, there exists a tracking attractor where ρ_φ tracks the
background density:

```
ρ_φ/ρ_bg → const     [for tracker initial conditions]
w_φ → w_bg - α(1+w_bg)/(α+2)     [during tracking]
```

The tracker is reached when φ reaches φ_track where V''/V ~ H²,
which gives:

```
φ_track ~ (M^{4+α}/H²)^{1/(α+2)}
```

**At what epoch does the tracker activate?**

For φ_i ~ M_Pl (bounce-set): the field starts frozen at φ = M_Pl.
It stays there until H drops enough that V'(M_Pl) can overcome
the Hubble friction. This happens when:

```
3H × |φ̇| ~ |V'(M_Pl)|
H ~ V'(M_Pl)/(3φ̇) ~ V'(M_Pl)/φ ~ V(M_Pl)/(M_Pl²)
```

For V(M_Pl) = M^{4+α}/M_Pl^α:

```
H_thaw ~ M^{4+α}/(M_Pl^{α+2})
```

For this to be H₀ ~ 10⁻³³ eV:
```
M^{4+α} = H₀ × M_Pl^{α+2} = 10⁻³³ × (2.4 × 10²⁷)^{α+2}
```

For α = 1: M⁵ = 10⁻³³ × (2.4 × 10²⁷)³ ~ 10⁴⁹ eV⁵ → M ~ 10¹⁰ eV.
For α = 2: M⁶ = 10⁻³³ × (2.4 × 10²⁷)⁴ ~ 10⁷⁶ eV⁶ → M ~ 10¹³ eV.

**The scale M must be tuned to produce H_thaw ~ H₀.** This is
the standard quintessence fine-tuning: M is adjusted to match
the observed DE density. The bounce provides no constraint on M.

**Sensitivity to φ_i:**

For tracker quintessence, the attractor behavior ERASES dependence
on φ_i for a wide range of initial conditions. The late-time
evolution depends on the POTENTIAL (M, α), not on φ_i.

Specifically, for φ_i in the range [0.1 M_Pl, 100 M_Pl]:
the tracker is reached within ~1 e-fold of each case. The
resulting ρ_DE differs by O(1) factors, not by orders of magnitude.

**Result: φ_i has NO useful predictive power for DE through tracker
quintessence.**

### Candidate B: pNGB (Cosine Potential)

```
V = Λ⁴(1 - cos(θ/f))
```

**For θ_i ~ f (order-one misalignment):**

The field oscillates when H drops below m_θ = Λ²/f. For this
to happen today: m_θ ~ H₀ → Λ² ~ H₀f.

For f ~ M_Pl: Λ ~ √(H₀ M_Pl) ~ 10⁻³ eV.

The energy density at oscillation onset is:
```
ρ_θ ~ Λ⁴ (1 - cos(θ_i/f)) ~ Λ⁴ × O(1) ~ (10⁻³ eV)⁴ ~ 10⁻¹² eV⁴
```

Compare to ρ_DE ~ (10⁻³ eV)⁴ ~ 10⁻¹² eV⁴. ✓

**This works!** But:

1. The mass m_θ = Λ²/f must be tuned to ~ H₀ (one parameter).
2. θ_i ~ f is generic (any O(1) misalignment works).
3. The bounce contributes θ_i ~ M_Pl (for strongly coupled) or
   θ_i ~ 0 (for stabilized). Both give O(1) misalignment if
   f ~ M_Pl.

**The pNGB model works but is NOT bounce-specific.** Any initial
condition θ_i ~ O(f) gives the same answer. The bounce just
provides one among many high-energy mechanisms that produce
generic O(1) displacement.

**Sensitivity to θ_i:**

ρ_DE ~ Λ⁴(1 - cos(θ_i/f)). For θ_i randomly distributed:

```
⟨1 - cos(θ/f)⟩ = 1     [averaged over θ ∈ [0, 2πf]]
```

The factor (1 - cos(θ_i/f)) varies between 0 and 2. This gives
a factor-of-2 uncertainty in ρ_DE — not enough to distinguish
bounce from non-bounce initial conditions.

### Candidate C: Exponential Quintessence

```
V = V₀ exp(-λφ/M_Pl)
```

**Scaling solution:**

During radiation: Ω_φ → 3/λ² (for λ² > 3).
During matter: Ω_φ → 3/λ² (for λ² > 3).

For Ω_φ → 1 today: need λ² ≲ 3, but this gives Ω_φ ~ 1 at ALL
times (inconsistent with BBN, CMB).

Standard resolution: λ must be time-dependent or the potential must
change shape. This introduces free functions that are NOT constrained
by the bounce.

**The exponential potential either tracks (Ω_φ constant, too small
for DE) or dominates (Ω_φ → 1, too early). The bounce initial
conditions are irrelevant — the attractor behavior determines the
outcome.**

---

## The Attractor Washout Theorem (Informal)

For any scalar potential with a late-time attractor (tracking,
scaling, or cosmological constant-like behavior):

**The late-time state depends on the POTENTIAL PARAMETERS, not on
the INITIAL CONDITIONS.**

This is a FEATURE of well-designed quintessence models (it solves
the "initial condition problem" of standard cosmology) but it is
a BUG for Foundation F, because it means:

**If the model has an attractor: bounce initial conditions are erased.**
**If the model lacks an attractor: initial conditions must be fine-tuned.**

There is no middle ground where:
- The initial conditions matter (no attractor washout) AND
- The initial conditions do not require fine-tuning

These are contradictory: if the result is sensitive to φ_i, then
the RIGHT φ_i must be achieved precisely — and the bounce provides
only generic Planck-scale displacements.

---

## Summary

| Model | Attractor? | Sensitive to φ_i? | DE produced? | Bounce-specific? |
|-------|-----------|-------------------|-------------|-----------------|
| Inverse-power quintessence | YES (tracker) | NO | YES (tune M) | NO |
| pNGB misalignment | NO (depends on θ_i) | MODERATE | YES (tune Λ, f) | NO (generic O(1)) |
| Exponential quintessence | YES (scaling) | NO | Problematic | NO |
| Hilltop quintessence | NO (sensitive) | EXTREME | Only if φ_i ~ 10⁻³⁰ | NO (bounce too violent) |

**No model produces a predictive bounce-DE connection through initial
conditions.**
