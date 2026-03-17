# First-Cut Analytic Screening

**Date:** 2026-03-16

---

## Screening Protocol

For each candidate class, evaluate:
1. Are physical stability quantities (Q_S, c_S², Q_T, c_T²) regular at H = 0?
2. Does X → 0 (frozen field) simplify the stability conditions?
3. Is the EFT valid at the bounce?
4. Is there any bounce-specific constraint not already known?

---

## Class A: Quintessence — TRIVIALLY_COMPATIBLE

### Stability check

```
Q_S = 1                    (constant, always positive)
c_S² = 1                   (constant, always subluminal)
Q_T = M_Pl²               (constant, always positive)
c_T² = 1                   (constant, always luminal)
```

All four conditions are FIELD-INDEPENDENT CONSTANTS. They cannot
be violated by any cosmological evolution whatsoever.

### Bounce-specific content: NONE

This result holds for ANY background, not just the bounce. It is
standard textbook knowledge. The bounce adds zero information.

### Verdict: TRIVIALLY_COMPATIBLE

### Tractability: ONE-LINE ARGUMENT

---

## Class B: K-essence — TRIVIALLY_COMPATIBLE

### Stability check

```
Q_S = P_X + 2XP_XX        at X → 0: Q_S → P_X(0, φ)
c_S² = P_X/(P_X + 2XP_XX) at X → 0: c_S² → 1
Q_T = M_Pl²               (constant)
c_T² = 1                   (constant)
```

For any well-defined K-essence with P_X(0, φ) > 0 (required for
the theory to have a stable rest state), Q_S > 0 and c_S² = 1
at the bounce.

### Specific models

**DBI (P = -f⁻¹√(1-2fX) + f⁻¹ - V):**
- P_X = 1/√(1-2fX) → 1 as X → 0
- Q_S → 1, c_S² → 1
- The relativistic sound speed c_S = √(1-2fX) → 1
- No DBI effects at X → 0

**Power-law (P = X + βX²/M⁴ - V):**
- P_X = 1 + 2βX/M⁴ → 1 as X → 0
- Trivially canonical

**Ghost condensate (P = -X + X²/M⁴):**
- P_X = -1 + 2X/M⁴ → -1 as X → 0
- Q_S → -1 < 0: GHOST at X = 0!
- BUT: the ghost condensate is designed to have X = X₀ ≠ 0 as
  its stable minimum. At X₀ = M⁴/2: P_X = 0, Q_S = 2X₀P_XX > 0.
- At the bounce, X → 0 ≠ X₀, so the ghost condensate IS
  destabilized. However, this is a known feature: the ghost
  condensate requires X ≈ X₀ and is unstable at X = 0 always,
  not just at the bounce. The bounce doesn't add new information.

### Bounce-specific content: NONE (for standard K-essence)

The ghost condensate issue at X = 0 is a pre-existing feature,
not a bounce-induced instability. It would also fail during any
epoch where X → 0 (e.g., field oscillation zero-crossings).

### Verdict: TRIVIALLY_COMPATIBLE (standard K-essence)
### Ghost condensate caveat: known pre-existing X = 0 instability

---

## Class C: Cubic Horndeski / Braiding — EFT_INAPPLICABLE

### Stability check (formal)

The physical stability quantities for cubic Horndeski:

```
Θ = -φ̇XG₃X + Hφ̇G₄ - ...
  = -β₃φ̇X/(M³) + ...

Σ = XG₂X + 2X²G₂XX + Hφ̇XG₃X + ...
  = X + 6Hφ̇β₃X/(M³) + ...
```

At H = 0 with X → 0:
- Θ → 0 (both terms vanish)
- Σ → 0 (X → 0)
- Q_S = w₁Σ + 3Θ²/2 → M_Pl² × 0 + 0 = 0

Q_S → 0 at the bounce for a frozen field. This is NOT a ghost
(Q_S ≥ 0), but it means the scalar perturbation becomes
INFINITELY STRONGLY COUPLED at the bounce (perturbation theory
breaks down when Q_S → 0).

This is the STRONG COUPLING problem: even without a ghost, the
effective Planck mass for the scalar perturbation vanishes,
invalidating the linearized analysis.

### EFT validity

The braiding scale M ~ H₀ means:
```
Ḣ/M² ~ M_Pl²/H₀² ~ 10¹²² ≫ 1
```

Higher-order operators in the G₃ expansion become important.
The leading-order analysis cannot be trusted.

### Is Q_S → 0 bounce-specific?

Q_S → 0 occurs whenever BOTH H → 0 AND X → 0. In standard
cosmology, H > 0 always, so the Hφ̇XG₃X term in Θ keeps Q_S
finite even when X is small. The bounce is the ONLY scenario
where H = 0 simultaneously with potentially small X.

**However:** Q_S → 0 also occurs in quintessence at X → 0 (where
Q_S = X → 0). The difference is that for quintessence, the
perturbation equation remains regular (the Q_S → 0 is canceled
by the perturbation potential). For braiding, the cancellation
structure is more complex and may fail.

**This requires a dedicated perturbation analysis (Phase 2) to
determine whether Q_S → 0 is physically problematic or a
coordinate artifact.**

### Bounce-specific content: POTENTIALLY NONTRIVIAL

The simultaneous H = 0 and X → 0 is bounce-specific. Whether
this creates a genuine strong-coupling problem is unresolved.

### Verdict: EFT_INAPPLICABLE (with potentially interesting
### strong-coupling behavior at H = 0)

---

## Class D: Non-Minimal Coupling — COMPATIBLE_WITH_CAVEAT

### Stability check

For G₄ = (M_Pl² + ξφ²)/2:

```
Q_T = M_Pl² + ξφ²
```

For φ ~ M_Pl (typical in some DE models) and ξ > 0:
Q_T = M_Pl²(1 + ξ) > 0. No ghost.

For ξ < -1 and φ ~ M_Pl: Q_T could go negative. But this would
mean negative effective gravitational constant — already excluded
by late-time observations.

```
c_T² = 1     (G₄ = G₄(φ) only, no X dependence)
```

Always luminal. No tensor gradient instability.

Scalar sector: c_S² involves the effective potential and is
regular at H = 0. The tachyonic mass m² = V'' - ξR is transient.

### The tachyonic kick

At the bounce (R ≈ 21 M_Pl²):

```
m_eff² = V''(φ) - ξ × 21 M_Pl²
```

For ξ > 0 (conformal coupling direction):
m_eff² < 0 (tachyonic) for any ξ > V''/(21 M_Pl²) ~ 10⁻¹²².

Growth factor over bounce duration Δt ~ t_Pl:

```
δφ/φ ~ exp(√(21ξ) × M_Pl × t_Pl) = exp(√(21ξ))
```

| ξ | Growth factor | Assessment |
|---|--------------|-----------|
| 0.01 | 1.5 | Negligible |
| 0.1 | 3.1 | Negligible |
| 1 | ~100 | Moderate but bounded |
| 10 | ~2 × 10⁶ | Significant |
| 100 | ~10²⁰ | Potentially problematic |
| 10⁴ | ~10²⁰⁰ | Catastrophic |

For |ξ| ≲ O(1): the kick is mild and the field returns to its
slow-roll DE trajectory after the bounce.

For |ξ| ≳ 10: the kick could displace the field significantly
from its late-time minimum, potentially spoiling DE.

### Is this bounce-specific?

**Partially.** The tachyonic kick requires R ~ M_Pl² (Planck-scale
curvature), which occurs only at the bounce. In standard cosmology
(no bounce), R decreases monotonically and this kick never occurs.

**But:** the same issue arises in inflationary preheating, during
reheating oscillations (R oscillates and can trigger parametric
resonance for non-minimally coupled fields). This is known physics.
The bounce version is a single transient kick rather than
parametric resonance, so it is MILDER than the inflationary analog.

### Bounce-specific content: MARGINAL

The bounce provides a constraint ξ ≲ O(10) for bounce compatibility,
but this is weaker than existing constraints on ξ from:
- Solar system (Cassini): |ξ| ≲ 10⁻² for light fields
- CMB isocurvature: |ξ| ≲ O(1) for DE-mass fields
- Stability during inflation: |ξ| ≲ O(1)

The bounce constraint is WEAKER than pre-existing bounds.

### Verdict: COMPATIBLE_WITH_CAVEAT (transient tachyonic kick,
### bounded, weaker than existing constraints)

---

## Class E: Quartic/Quintic — TRIVIALLY_COMPATIBLE (by GW170817)

### Stability check

Post-GW170817 viable models have:
```
G₄ = G₄(φ)    (no X dependence)
G₅ ≈ 0
```

This reduces to Class D. All stability conditions inherited.

For models that DO have G₄X ≠ 0 or G₅ ≠ 0:

```
c_T² = [G₄ - Xφ̈G₅X - XG₅φ] / [G₄ - 2XG₄X + XG₅φ - Hφ̇XG₅X]
```

At H = 0: the denominator term Hφ̇XG₅X vanishes. With X → 0:
- Numerator → G₄(φ, 0)
- Denominator → G₄(φ, 0)
- c_T² → 1

No singularity. But these models are already excluded by GW170817.

### Bounce-specific content: NONE

GW170817 pre-empts any bounce constraint. The bounce provides
a strictly weaker bound.

### Verdict: TRIVIALLY_COMPATIBLE (pre-empted)

---

## Class F: DHOST — EFT_INAPPLICABLE (degeneracy preserved)

### Stability check

DHOST degeneracy conditions (Class Ia):
```
A₁ + A₂ = 0    (algebraic condition on Lagrangian functions)
```

This is a condition on the FUNCTIONAL FORM of the theory, not
on the background. It holds at H = 0, at H = H₀, at all times.

No ghost reappearance at the bounce.

### EFT validity

The DHOST strong coupling scale:
```
Λ_SC ~ (M_Pl M²)^{1/3}    (where M is the DE internal scale)
```

For M ~ H₀: Λ_SC ~ (M_Pl H₀²)^{1/3} ~ 10⁻⁴⁰ M_Pl ~ 10⁻²¹ eV.

At the bounce, curvature R ~ M_Pl². The ratio R/Λ_SC² ~ 10⁸⁰ ≫ 1.
The EFT has broken down catastrophically.

### Bounce-specific content: NONE (for degeneracy)

The degeneracy is algebraic and background-independent. The
EFT breakdown is generic to any theory with Λ ≪ M_Pl at
Planck curvature, not specific to DHOST.

### Verdict: EFT_INAPPLICABLE (degeneracy preserved, EFT broken)

---

## Screening Summary

| Class | Ghost-free? | Gradient-stable? | c_T ok? | EFT valid? | Verdict |
|-------|-----------|-----------------|---------|-----------|---------|
| A: Quintessence | ✓ (trivial) | ✓ (trivial) | ✓ | ✓ | TRIVIALLY_COMPATIBLE |
| B: K-essence | ✓ (at X→0) | ✓ (at X→0) | ✓ | ✓ | TRIVIALLY_COMPATIBLE |
| C: Braiding | Q_S→0 | ? | ✓ | **NO** | EFT_INAPPLICABLE |
| D: Non-minimal | ✓ | ✓ (transient) | ✓ | ✓ | COMPATIBLE_WITH_CAVEAT |
| E: Quartic/Quintic | ✓ | ✓ | ✓ | ✓ | TRIVIALLY_COMPATIBLE |
| F: DHOST | ✓ (algebraic) | ? | ? | **NO** | EFT_INAPPLICABLE |

---

## Key Findings

### Finding 1 (Methodological): EFT-of-DE breaks at H = 0

The standard α-parameterization (α_K, α_B, α_M) is singular at
H = 0. This is a parameterization artifact — physical quantities
remain finite — but it means that Boltzmann codes using the
α-parameterization (hi_class, EFTCAMB) CANNOT be directly applied
to a bounce background without modification.

**This is a genuine methodological finding.** It tells the
community that EFT-of-DE results derived under H > 0 assumptions
need re-examination for bounce cosmologies, even though the
underlying physics is regular.

### Finding 2 (Scale separation): DE frozen at bounce

The DE kinetic energy X ~ 10⁻¹²² M_Pl⁴ at the bounce makes
all stability conditions trivially satisfied for theories without
low internal scales. The 120-order-of-magnitude hierarchy between
DE and bounce scales prevents any interesting interplay.

### Finding 3 (EFT breakdown): Low-scale theories inapplicable

Theories with internal scales M ≪ M_Pl (braiding with M ~ H₀,
DHOST with Λ ~ 10⁻⁴⁰ M_Pl) cannot be assessed at the bounce.
Their EFT descriptions are invalid at Planck curvature. This
is not a stability failure but a statement that UV completion
is needed to determine bounce compatibility.

### Finding 4 (Transient kick): Non-minimal coupling bounded

The curvature coupling ξRφ² generates a tachyonic kick at the
bounce for ξ > 0, with growth factor exp(√(21ξ)). This is
bounded and WEAKER than existing constraints on ξ from solar
system and CMB observations.

### Finding 5 (Strong coupling): Q_S → 0 for braiding at bounce

The scalar perturbation normalization Q_S → 0 when H → 0 and
X → 0 simultaneously, potentially signaling strong coupling of
the scalar perturbation at the bounce. Whether this is a genuine
pathology or a coordinate/gauge artifact requires Phase 2 analysis.
This is the MOST PROMISING lead for a nontrivial constraint.
