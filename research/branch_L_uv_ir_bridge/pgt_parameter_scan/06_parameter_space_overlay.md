# Parameter Space Overlay

**Date:** 2026-03-16

---

## 1. The Three Constraints

We overlay three independent requirements on the PGT parameter space
(Sector II: propagating spin-0⁻ mode, t₂ = -2t₁, t₃ < 0):

### Constraint 1: Ghost freedom
```
t₃ < 0                    (0⁻ ghost-free)
t₁ ~ O(1), t₁ > 0         (heavy modes at Planck scale)
t₂ = -2t₁                  (1⁻ decoupled)
```

**Region in (t₁, |t₃|) space:** First quadrant, t₁ > 0, |t₃| > 0.
The ghost-free region is the ENTIRE first quadrant (no upper/lower
bound on |t₃| from ghost freedom alone).

### Constraint 2: Bounce in GW detector band
```
m_T = M_Pl / (2√|t₃|)

LIGO/ET (1–10⁴ Hz):  m_T ~ 10⁻³ to 10⁷ GeV  →  |t₃| ~ 10⁸ to 10⁴⁸
LISA (10⁻⁴–10⁻¹ Hz): m_T ~ 10⁻⁹ to 10⁻⁵ GeV  →  |t₃| ~ 10⁴⁸ to 10⁵⁶
```

**Region:** Horizontal band in log|t₃|, between 10⁸ and 10⁵⁶.

### Constraint 3: Detectable signal amplitude

From File 05, the GW signal amplitude relative to detector
sensitivity:

```
Ω_GW,feature / Ω_sensitivity ~ (m_T/M_Pl)² × (m_T/M_Pl) / Ω_sensitivity
                              ~ (m_T/M_Pl)³ / 10⁻¹³
```

For detection: need Ω_GW,feature ≥ Ω_sensitivity:

```
(m_T/M_Pl)³ ≥ 10⁻¹³
m_T ≥ M_Pl × 10⁻¹³/³ ~ 10¹⁹ × 10⁻⁴·³ ~ 10¹⁴·⁷ GeV
```

**Required: m_T > ~5 × 10¹⁴ GeV.**

In terms of |t₃|:
```
|t₃| ≤ M_Pl² / (4 × m_T²) ~ (10¹⁹)² / (10¹⁴·⁷)² ~ 10⁸·⁶
```

**Region:** |t₃| < ~10⁹.

### The corresponding bounce frequency at m_T ~ 5 × 10¹⁴ GeV:

```
f_b ~ 5.7 × 10¹⁰ × (5 × 10¹⁴ / 1.2 × 10¹⁹)^{1/2}
    ~ 5.7 × 10¹⁰ × (4 × 10⁻⁵)^{1/2}
    ~ 5.7 × 10¹⁰ × 6.3 × 10⁻³
    ~ 3.6 × 10⁸ Hz
    = 360 MHz
```

**This is ABOVE the LIGO band (max ~10⁴ Hz).**

---

## 2. The Incompatibility

### Overlay result

```
Ghost-free:           |t₃| > 0, t₁ > 0     (entire first quadrant)
Bounce in LIGO band:  |t₃| > 10⁸            (m_T < 10⁷ GeV)
Detectable signal:    |t₃| < 10⁹            (m_T > 5 × 10¹⁴ GeV)
```

The intersection:
```
10⁸ < |t₃| < 10⁹
```

corresponds to:
```
m_T ~ 6 × 10¹⁴ to 2 × 10¹⁵ GeV
f_b ~ 4 × 10⁸ to 7 × 10⁸ Hz
```

**The overlap region exists but is at f_b ~ 400–700 MHz.**

This is:
- FAR above LIGO (max ~10⁴ Hz)
- FAR above LISA (max ~10⁻¹ Hz)
- In the microwave range (no GW detector planned)

### Visual summary (log scale)

```
log₁₀|t₃|:  0    10    20    30    40    50    60
             |     |     |     |     |     |     |
Ghost-free:  [======================================]  (all |t₃|)
             |     |     |     |     |     |     |
Detectable:  [===]                                     (|t₃| < 10⁹)
             |     |     |     |     |     |     |
LIGO band:         [===========]                       (10⁸ < |t₃| < 10⁴⁸)
             |     |     |     |     |     |     |
LISA band:                              [=========]    (10⁴⁸ < |t₃| < 10⁵⁶)
             |     |     |     |     |     |     |

Overlap (detectable ∩ LIGO): |t₃| ~ 10⁸–10⁹ → f_b ~ 400 MHz
                              NOT in any GW detector band
```

---

## 3. Why the Overlap Misses All Detectors

The fundamental reason:

**The mass-coupling lock forces:**
```
Signal amplitude ∝ (m_T/M_Pl)^n    with n ≥ 2
```

**The bounce frequency scales as:**
```
f_b ∝ (m_T/M_Pl)^{1/2}
```

To get f_b into detector bands, we need m_T/M_Pl to be very small
(10⁻¹² to 10⁻²⁴). But the signal amplitude drops as a HIGHER
power of the same ratio:

```
Signal ∝ (m_T/M_Pl)³     [from the Ω_GW estimate]
f_b ∝ (m_T/M_Pl)^{1/2}
```

Eliminating m_T/M_Pl:

```
Signal ∝ f_b⁶
```

To go from f_b = 400 MHz (marginally detectable) to f_b = 1 Hz
(LIGO):

```
Signal drops by (1/4×10⁸)⁶ = 10⁻⁵² × 4⁶ ≈ 10⁻⁴⁹
```

**The signal drops by ~10⁴⁹ when moving from 400 MHz to the
LIGO band.**

This is the same scale-separation barrier in a different guise:
lowering the bounce scale helps with frequency but kills the
amplitude faster than it helps.

---

## 4. Revised Estimate: Can Any Enhancement Save It?

### Best-case scenario: coherent torsion background

If the torsion field has a large coherent background amplitude
(not just vacuum fluctuations), the GW signal could be enhanced.

Maximum torsion amplitude at the bounce (from fermion source):
```
τ_max ~ n₅ / m_T² ~ ρ_crit^{3/4} / m_T²
       ~ (m_T M_Pl)^{3/2} / m_T² = M_Pl^{3/2} / m_T^{1/2}
```

Torsion energy at bounce:
```
ρ_τ ~ m_T² τ_max² ~ m_T² × M_Pl³/m_T = m_T M_Pl³
```

Fraction of critical density:
```
ρ_τ / ρ_crit ~ m_T M_Pl³ / (m_T² M_Pl²) = M_Pl / m_T ≫ 1
```

**PROBLEM:** This says the torsion energy EXCEEDS ρ_crit, which
is inconsistent — it means the torsion backreacts on the bounce
and our parametric estimates are not self-consistent.

### Self-consistent estimate

At the bounce, the torsion energy must be ≤ ρ_crit:
```
ρ_τ ≤ ρ_crit ~ m_T² M_Pl²
```

This caps: m_T² τ² ≤ m_T² M_Pl², so τ ≤ M_Pl.

The torsion-generated GW amplitude:
```
h_GW ~ (G × ρ_τ × L²) ~ (ρ_τ/M_Pl²) × (1/m_T)²
     ~ (m_T² M_Pl² / M_Pl²) × (1/m_T²)
     = 1
```

This suggests h_GW ~ O(1) AT THE BOUNCE. The GW amplitude at
emission is not the problem — it's the REDSHIFT from the bounce
to today:

```
h_today = h_bounce × (a_b/a_0)
        ~ 1 × (T₀/T_b)
        ~ T₀ / (m_T M_Pl)^{1/2}
```

For m_T = 10⁻⁵ GeV:
```
h_today ~ 10⁻¹³ / (10⁻⁵ × 10¹⁹)^{1/2} = 10⁻¹³ / 10⁷ = 10⁻²⁰
```

And Ω_GW:
```
Ω_GW ~ h²_today × (f_b/H₀)² × ...
```

This is more optimistic than the coupling-based estimate in File 05.
Let me redo this carefully.

### Careful Ω_GW estimate

The GW energy density parameter from a bounce:

```
Ω_GW(f_b) ~ (ρ_GW,emitted / ρ_crit,today) × (a_b/a_0)⁴ × (radiation transfer)
```

For a bounce that converts fraction ε of its energy to GWs:

```
ρ_GW,emitted = ε × ρ_crit^{eff}
```

After redshifting (GW energy density redshifts as a⁻⁴):

```
ρ_GW,today = ε × ρ_crit^{eff} × (a_b/a_0)⁴
```

With a_b/a_0 = T₀/T_b = T₀/(ρ_crit^{eff})^{1/4}:

```
ρ_GW,today = ε × ρ_crit^{eff} × T₀⁴ / ρ_crit^{eff} = ε × T₀⁴
```

Therefore:
```
Ω_GW = ρ_GW,today / ρ_c,today = ε × T₀⁴ / ρ_c,today
     = ε × T₀⁴ / (3H₀²M_Pl²/8π)
```

With T₀ = 2.35 × 10⁻¹³ GeV, H₀ = 1.44 × 10⁻⁴² GeV:

```
T₀⁴ / (3H₀²M_Pl²/8π) ~ (2.35×10⁻¹³)⁴ / (3×(1.44×10⁻⁴²)²×(1.22×10¹⁹)²/8π)
```

Numerator: (2.35)⁴ × 10⁻⁵² ~ 3.1 × 10⁻⁵¹ GeV⁴
Denominator: 3/(8π) × (1.44)² × (1.22)² × 10⁻⁸⁴ × 10³⁸ ~ 10⁻⁴⁶ GeV⁴

```
Ω_GW ~ ε × 3 × 10⁻⁵
```

**So Ω_GW ~ 3 × 10⁻⁵ × ε, independent of ρ_crit!**

This is a well-known result: the GW background from any early-
universe source, after radiation-like redshifting, gives
Ω_GW h² ~ 10⁻⁵ × ε (up to g_* factors).

### The question becomes: what is ε?

The efficiency ε = fraction of bounce energy converted to GWs.

**For a symmetric radiation bounce (EC minimal model):**
ε ~ |β_k|² ~ (k/k_b)² for k ≪ k_b. For k ~ k_b: ε ~ O(1) but
only at k ~ k_b (which is at GHz, not in detector bands).

For k in the LIGO band (k ≪ k_b): ε(k) ~ (k/k_b)² ~ 10⁻⁵⁶.

**For the PGT lower-scale bounce (Sector II):**
The bounce scale k_b is now lower, so for k in the LIGO band:

```
ε(k) ~ (k/k_b,PGT)²
```

If k_b,PGT is in the LIGO band (f_b ~ 1 Hz), then k ~ k_b and
ε ~ O(1). Then:

```
Ω_GW ~ 3 × 10⁻⁵   at f ~ f_b
```

**This WOULD be detectable by LIGO (sensitivity Ω ~ 10⁻⁹) and
LISA (sensitivity Ω ~ 10⁻¹³)!**

### BUT: the lock suppresses ε

The torsion-mediated bounce has ε determined by the torsion
coupling strength. The bounce is not a "hard wall" collision but
a gradual turning mediated by the torsion repulsion. The efficiency
of GW production depends on the "violence" of the bounce:

For a smooth bounce (t_bounce ≫ 1/k): ε ~ (k × t_bounce)⁻²
For a sharp bounce (t_bounce ~ 1/k): ε ~ O(1)

In the PGT bounce, t_bounce ~ 1/m_T. For modes at k ~ k_b ~ m_T:

```
k × t_bounce ~ m_T / m_T ~ 1
```

**The bounce IS sharp at its own scale.** ε(k_b) ~ O(1).

### Resolution of the contradiction

The estimates in File 05 (coupling-based, giving ε ~ (m_T/M_Pl)³)
and the current estimate (energy-based, giving ε ~ O(1) at k_b)
disagree because they describe different physics:

- **File 05 estimate:** How much the torsion mode DISTORTS an
  existing GW spectrum. This is a PERTURBATIVE effect, suppressed
  by g_eff.

- **Current estimate:** How much GW energy is PRODUCED by the
  bounce itself. This is a NONPERTURBATIVE effect, determined by
  the bounce dynamics.

The correct estimate depends on whether we're looking for:
(a) Features superimposed on a pre-existing GW background
(b) The GW background generated BY the bounce itself

For (b), the bounce-generated background:

```
Ω_GW(f_b) ~ 10⁻⁵ × ε(f_b) ~ 10⁻⁵ × O(1) ~ 10⁻⁵
```

**IF the PGT bounce frequency f_b falls in a detector band,
the bounce-generated GW background is at Ω ~ 10⁻⁵,
well above detector sensitivity.**

---

## 5. Critical Reassessment

### What changed from File 05

File 05 asked: "Can the torsion mode MODIFY the tensor perturbation
spectrum?" The lock kills this (perturbative torsion-tensor
coupling is ~ m_T/M_Pl).

The correct question for the bounce: "Can the bounce PRODUCE a
GW background?" The answer depends on the bounce dynamics (the
time-dependent scale factor), not on the perturbative coupling.

The bounce is a BACKGROUND COSMOLOGICAL EVENT. Its GW production
is determined by the spacetime geometry (a(t)), not by the
torsion-matter coupling g_eff. The bounce occurs because H = 0
and Ḣ > 0, which creates a time-dependent effective potential
for tensor modes. This potential is of order:

```
V_T(η) = a''/a ~ a_b² × ρ_crit^{eff} / M_Pl² ~ a_b² × m_T²
```

The mode function equation:
```
h_k'' + (k² - V_T)h_k = 0
```

For k² ~ V_T (resonance): strong particle production, ε ~ O(1).
For k² ≫ V_T: adiabatic, ε ≪ 1.
For k² ≪ V_T: frozen mode, ε ~ O(1) but mode is super-horizon.

The bounce-scale modes k ~ k_b have k² ~ V_T and experience
maximal amplification.

### Does the lock still matter?

**For the background GW production: NO.** The bounce dynamics are
determined by the PGT action at the background level (Friedmann
equation + torsion equation of motion). The effective coupling
g_eff enters the perturbative corrections but NOT the background
bounce profile.

**For perturbative features: YES.** Any torsion-specific spectral
features (oscillations, dips, chirality) superimposed on the
smooth GW background are suppressed by g_eff.

### Revised picture

The PGT lower-scale bounce produces:

1. **A smooth GW background** at Ω ~ 10⁻⁵ centered at f ~ f_b.
   This is determined by the bounce geometry (ρ_crit, a(t)) and
   is NOT suppressed by the lock.

2. **Torsion-specific spectral features** (oscillations) at
   f ~ f_b with amplitude A_osc ~ m_T/M_Pl relative to the smooth
   background. These ARE suppressed by the lock.

The smooth background is generic (any bounce at the same ρ_crit
produces the same background). The torsion-specific features are
suppressed. This is the same FAIL_NOT_BOUNCE_SPECIFIC problem
from Phase 1 screening — the detectable part is generic, the
specific part is undetectable.

---

## 6. Final Overlay

### Parameter space status

| Region | Ghost-free? | f_b in band? | Signal? | Torsion-specific? |
|--------|:-----------:|:------------:|:-------:|:-----------------:|
| |t₃| ~ 1 (EC limit) | ✓ | ✗ (40 GHz) | ✓ but undetectable |
| |t₃| ~ 10⁸–10⁹ | ✓ | ✗ (400 MHz) | Marginal |
| |t₃| ~ 10¹²–10¹⁶ | ✓ | ✓ (LIGO) | Generic: ✓, Specific: ✗ |
| |t₃| ~ 10²⁰–10²⁸ | ✓ | ✓ (LISA) | Generic: ✓, Specific: ✗ |
| |t₃| ~ 10⁴⁸+ | ✓ | ✗ (sub-PTA) | ✗ |

### The dilemma in one sentence

> **The bounce-generated GW background is detectable, but it is
> NOT torsion-specific. The torsion-specific features are
> suppressed by the mass-coupling lock.**

### Comparison with LQC

LQC also produces a bounce-generated GW background. If LQC and PGT
have the same ρ_crit, they produce the same smooth GW background.
The ONLY way to distinguish them is via the spectral features —
which are suppressed in PGT by the lock.

---

## 7. Summary

| Finding | Status |
|---------|--------|
| Ghost-free parameter space | **EXISTS** (Sector II, all |t₃|) |
| Bounce in GW band | **YES** (for |t₃| ~ 10¹²–10²⁸) |
| Smooth GW background detectable | **YES** (Ω ~ 10⁻⁵ at f_b) |
| Torsion-specific features detectable | **NO** (A_osc ~ m_T/M_Pl ≪ 1) |
| Lock evadable? | **NO** (4 attempts failed) |
| Distinguishable from generic bounce? | **NO** (smooth part is universal) |
| Distinguishable from LQC? | **NO** (same smooth spectrum) |

> **The PGT lower-scale bounce is ghost-free, occurs at observable
> frequencies, and produces a detectable GW background — but the
> detectable part is GENERIC to any bounce at that scale, and the
> SPECIFIC torsion features are killed by the mass-coupling lock.**
