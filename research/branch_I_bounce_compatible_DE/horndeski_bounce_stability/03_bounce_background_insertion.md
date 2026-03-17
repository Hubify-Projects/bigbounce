# Bounce Background Insertion

**Date:** 2026-03-16

---

## The Bounce Background

The spin-torsion bounce has the exact radiation-dominated solution:

```
a(t) = a_b (1 + 4α²t²)^{1/4}
H(t) = 2α²t / (1 + 4α²t²)
Ḣ(t) = 2α² / (1 + 4α²t²)²
```

where α² = 8πGρ_crit/3 ≈ 1.76 M_Pl².

At the bounce (t = 0):
- H = 0
- Ḣ = 2α² ≈ 3.52 M_Pl²
- R = 6(Ḣ + 2H²) = 6Ḣ ≈ 21.1 M_Pl²
- ρ = ρ_crit ≈ 0.21 M_Pl⁴

---

## How a DE Scalar Field Embeds on This Background

A Horndeski DE field φ lives on the bounce background as a
spectator. The total energy density is:

```
ρ_total = ρ_rad + ρ_DE
```

with ρ_DE/ρ_rad ~ 10⁻¹²² at the bounce. The DE field does NOT
modify the background dynamics. This is the key simplification.

### The DE field equation on the bounce background

For general Horndeski, the scalar equation of motion is:

```
E_φ[φ, g_μν] = 0
```

where g_μν is the FRW metric with a(t) given above. The equation
involves H(t) and Ḣ(t) from the bounce solution.

### State of the DE field at the bounce

The DE field has mass m ~ H₀ ~ 10⁻³³ eV and evolves on timescale
t_DE ~ 1/H₀ ~ 10⁶⁰ t_Pl. The bounce occurs over t_bounce ~ t_Pl.

During the bounce:
```
φ(t) ≈ φ_b + φ̇_b t + O(t²)
```

where φ̇_b is the field velocity at the bounce. For a field that
was evolving on DE timescales:

```
φ̇_b ~ H₀ M_Pl ~ 10⁻⁶⁰ M_Pl²
```

The kinetic energy:
```
X = φ̇²/2 ~ H₀² M_Pl² ~ 10⁻¹²² M_Pl⁴
```

This is negligible compared to ALL Planck-scale quantities.

---

## Class-by-Class Background Insertion

### Class A: Quintessence (G₂ = X - V(φ))

Field equation:
```
φ̈ + 3Hφ̇ + V'(φ) = 0
```

At H = 0:
```
φ̈ + V'(φ) = 0
```

This is just the flat-space Klein-Gordon equation. Regular,
no pathology. The 3Hφ̇ friction term simply vanishes.

During contraction (H < 0): the friction becomes anti-friction
(3Hφ̇ with H < 0 accelerates the field). However, for m ~ H₀,
the acceleration timescale is t ~ 1/H₀ ≫ t_bounce. The field
doesn't accelerate appreciably during the bounce.

**Quantitative estimate:** Maximum anti-friction occurs at
H_min ~ -α/√3 ≈ -0.76 M_Pl. The anti-friction force is
3|H|φ̇ ~ 3 × 0.76 × 10⁻⁶⁰ M_Pl³ ~ 10⁻⁶⁰ M_Pl³.
Compare to V'(φ) ~ H₀² M_Pl ~ 10⁻¹²² M_Pl³. The anti-friction
exceeds V' by a factor of 10⁶², but it acts for only ~ t_Pl,
giving Δφ̇ ~ 10⁻⁶⁰ M_Pl². This is still tiny: X ~ 10⁻¹²⁰ M_Pl⁴.

**Verdict:** φ effectively frozen throughout the bounce. X ≈ 0.

### Class B: K-essence (G₂ = P(X, φ))

Field equation:
```
(P_X + 2XP_XX)φ̈ + 3HP_X φ̇ + 2XP_Xφ - P_φ = 0
```

At X → 0: P_X(0, φ) is typically O(1) (canonical normalization
at low energy). The equation reduces to:

```
P_X(0,φ) φ̈ + P_φ(0,φ) = 0
```

Same as quintessence with rescaled field. Regular at H = 0.

**DBI model:** P = -f⁻¹√(1 - 2fX) + f⁻¹ - V(φ). At X → 0:
P_X = 1, P_XX = f. The Lorentz factor γ = 1/√(1-2fX) → 1.
No relativistic effects. DBI reduces to canonical quintessence.

**Verdict:** K-essence fields frozen, reduce to canonical at bounce.

### Class C: Cubic Horndeski / Kinetic Gravity Braiding

Field equation (from document 02):
```
φ̈(1 + 2β₃Hφ̇/M³) + 3Hφ̇ + V' + β₃(2Ḣ + 3H²)φ̇²/M³ = 0
```

At H = 0:
```
φ̈ + V' + 2β₃Ḣφ̇²/M³ = 0
```

The braiding force at the bounce:
```
F_braid = 2β₃Ḣφ̇²/M³ = 2β₃ × 3.52 M_Pl² × φ̇² / M³
```

**For M ~ H₀ (DE braiding scale):**
```
F_braid ~ 7 M_Pl² × (10⁻⁶⁰ M_Pl²)² / (10⁻⁶⁰ M_Pl)³
        = 7 × 10⁻¹²⁰ M_Pl⁶ / 10⁻¹⁸⁰ M_Pl³
        = 7 × 10⁶⁰ M_Pl³
```

This is ENORMOUS — 10⁶⁰ M_Pl³ for a field with V' ~ 10⁻¹²² M_Pl³.

**BUT WAIT:** This assumes φ̇ ~ 10⁻⁶⁰ M_Pl² (DE velocity) is
maintained through the bounce. The CRITICAL question is whether
φ̇ is amplified during the pre-bounce contraction.

### The anti-friction amplification problem

During contraction, H < 0 and the Hubble friction becomes
anti-friction. For a braiding field, the effective friction is:

```
γ_eff = 3H(P_X + 2β₃Hφ̇/M³) + ...
```

The braiding term 2β₃Hφ̇/M³ ~ 2β₃ × M_Pl × 10⁻⁶⁰ M_Pl² / (10⁻⁶⁰ M_Pl)³
~ 2 × 10¹²⁰ M_Pl⁻¹

This is an enormous coefficient. BUT: it multiplies φ̈, modifying
the effective inertia of the field, not directly driving it.

The actual amplification depends on the FULL contraction history,
not just the bounce instant. If the contraction starts from a
low-density state (H ~ -H₀) and contracts to Planck density over
cosmological timescales, the braiding effects accumulate gradually.

**Key issue:** The braiding scale M ~ H₀ means the braiding
becomes important when H ~ M ~ H₀, i.e., in the LATE universe.
During contraction from H ~ -H₀ to H ~ -M_Pl, the braiding
terms grow as H/M ~ M_Pl/H₀ ~ 10⁶⁰. The effective EOM becomes
strongly modified well before the bounce.

This COULD amplify φ̇ significantly, but calculating the actual
amplification requires solving the full ODE through contraction.
This is a Phase 2 problem requiring numerics.

**Order-of-magnitude bound:** Even if anti-friction amplifies φ̇
by a factor of 10⁶⁰ (unrealistically large), X would reach
~ (10⁰ M_Pl²)² / 2 ~ M_Pl⁴. At this point, the braiding force
would be F_braid ~ M_Pl² × M_Pl⁴ / M³ ~ (M_Pl/H₀)³ M_Pl³.
The EFT would have broken down LONG before this point.

**Conservative assessment:** For the EFT to remain valid, we need
the braiding corrections to remain perturbative:
β₃Hφ̇/M³ < 1, requiring φ̇ < M³/H < H₀³/M_Pl ~ 10⁻¹⁸³ M_Pl².
If this is satisfied, the braiding force at bounce is:
F_braid < 2 × 3.52 M_Pl² × (10⁻¹⁸³)² / 10⁻¹⁸⁰ = negligible.

**The catch:** The EFT validity condition is extremely restrictive
near the bounce (H ~ M_Pl). The braiding EFT with M ~ H₀
CANNOT be trusted at the bounce. This is not a stability failure
but an EFT BREAKDOWN — the theory doesn't make predictions at
Planck curvature for DE-scale M.

**Verdict:** Class C has an EFT validity issue, not a stability
issue. The braiding scale M ~ H₀ means the theory is outside
its domain of validity at the bounce. This is a METHODOLOGICAL
finding (success criterion 4), not a stability exclusion.

### Class D: Non-Minimal Coupling (G₄ = f(φ)/2)

Field equation:
```
φ̈ + 3Hφ̇ + V'(φ) - f'(φ)R/2 = 0
```

At the bounce:
```
φ̈ + V' - f'(φ) × 21.1 M_Pl² / 2 = 0
```

For f(φ) = M_Pl² + ξφ²:
```
φ̈ + V' - ξφ × 21.1 M_Pl² = 0
```

The curvature coupling gives an effective mass:
```
m_eff² = V''(φ) - 21.1 ξ M_Pl²
```

For ξ < 0: m_eff² = V'' + 21.1|ξ|M_Pl² > 0 (stabilizing).
For ξ > 0: m_eff² = V'' - 21.1ξ M_Pl² < 0 if ξ > V''/(21 M_Pl²).

Since V'' ~ H₀² ~ 10⁻¹²² M_Pl², ANY ξ > 10⁻¹²² gives a
tachyonic mass at the bounce. But this acts for ~ t_Pl:

Growth: exp(m_eff × t_Pl) ≈ exp(√(21ξ)) for ξ ~ O(1).

For ξ = 1: growth factor ≈ e^{4.6} ≈ 100. A transient kick.
For ξ = 10: growth factor ≈ e^{14.5} ≈ 2 × 10⁶. Significant but bounded.
For ξ = 100: growth factor ≈ e^{46} ≈ 10²⁰. Potentially problematic.

**Verdict:** Transient tachyonic kick for ξ > 0, bounded by
bounce duration. Not a genuine instability for |ξ| ≲ O(10).
For large |ξ|, need to check if the kick destabilizes the
late-time DE trajectory — a Phase 2 question.

### Class E: Quartic/Quintic Horndeski

Already constrained by GW170817: |c_T - 1| < 10⁻¹⁵ at z ~ 0.
This requires G₄X ≈ 0 and G₅ ≈ 0 (or fine-tuned cancellations).

For the surviving models (luminal Horndeski): G₄ = G₄(φ) and
G₅ = 0. These reduce to Class D (non-minimal coupling).

The bounce adds no constraint beyond GW170817.

**Verdict:** Pre-empted. No bounce-specific content.

### Class F: DHOST / Beyond-Horndeski

Degeneracy conditions are ALGEBRAIC (conditions on F₄, F₅, G_i):
```
Class Ia: XF₄ + ... = 0
```

These hold for all field configurations including H = 0.
The ghost is absent at the bounce if it is absent anywhere.

The strong coupling scale Λ_strong could change at the bounce.
For DE-scale DHOST, Λ_strong ~ (M_Pl H₀²)^{1/3} ~ 10⁻⁴⁰ M_Pl.
At the bounce (H ~ 0, Ḣ ~ M_Pl²), the strong coupling scale
could shift — but the EFT is already inapplicable at M_Pl.

**Verdict:** Degeneracy preserved. EFT validity question only.

---

## Summary: Field States at the Bounce

| Class | φ̇ at bounce | X at bounce | EFT valid? | Pathology? |
|-------|-------------|------------|-----------|-----------|
| A: Quintessence | ~10⁻⁶⁰ M_Pl² | ~10⁻¹²² M_Pl⁴ | YES | NONE |
| B: K-essence | ~10⁻⁶⁰ M_Pl² | ~10⁻¹²² M_Pl⁴ | YES | NONE |
| C: Braiding | Unknown (amplified?) | Unknown | **NO** (M~H₀) | EFT breakdown |
| D: Non-minimal | ~10⁻⁶⁰ M_Pl² | ~10⁻¹²² M_Pl⁴ | YES | Tachyonic kick |
| E: Quartic/Quintic | N/A | N/A | Pre-empted | Pre-empted |
| F: DHOST | ~10⁻⁶⁰ M_Pl² | ~10⁻¹²² M_Pl⁴ | **NO** (Λ~10⁻⁴⁰) | EFT breakdown |

**The dominant theme: DE fields are frozen at the bounce (X ≈ 0),
making stability conditions trivially satisfied. The interesting
finding is EFT breakdown for theories with low cutoff scales.**
