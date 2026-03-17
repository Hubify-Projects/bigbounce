# Candidate Model Classes

**Date:** 2026-03-16

---

## The Horndeski Action

The most general scalar-tensor theory with second-order equations:

```
S = ∫ d⁴x √g Σ_{i=2}^{5} L_i
```

```
L₂ = G₂(φ, X)
L₃ = -G₃(φ, X) □φ
L₄ = G₄(φ, X) R + G₄X [(□φ)² - (∇μ∇νφ)²]
L₅ = G₅(φ, X) G_μν ∇^μ∇^ν φ
     - (G₅X/6)[(□φ)³ - 3□φ(∇μ∇νφ)² + 2(∇μ∇νφ)³]
```

where X = -(1/2)(∂φ)² and subscripts denote partial derivatives.

---

## Class A: Canonical Quintessence

### Action
```
G₂ = X - V(φ),  G₃ = G₅ = 0,  G₄ = M_Pl²/2
```

### Stability quantities
- Q_S = 1 (always positive)
- c_S² = 1 (always subluminal)
- Q_T = M_Pl² (always positive)
- c_T² = 1 (always luminal)

### Why bounce embedding could matter
Quintessence fields have m ~ H₀ ~ 10⁻³³ eV. At the bounce
(H ~ M_Pl), the field is effectively FROZEN (m/H_bounce ~ 10⁻⁶⁰).
The stability conditions are trivially satisfied because they are
FIELD-INDEPENDENT (Q_S = 1, c_S² = 1 always).

### Risk assessment
**NONE.** This is the safest DE model. All stability conditions
are constants, independent of the background. Cannot be destabilized
by any cosmological evolution, including a bounce.

### Expected result: TRIVIALLY_COMPATIBLE

### Tractability: IMMEDIATE (analytic, one-line argument)

---

## Class B: K-essence / P(X, φ)

### Action
```
G₂ = P(X, φ),  G₃ = G₅ = 0,  G₄ = M_Pl²/2
```

Representative models:
- DBI: P = -f(φ)⁻¹√(1 - 2f(φ)X) + f(φ)⁻¹ - V(φ)
- Power-law: P = X + βX²/M⁴ - V(φ)
- Ghost condensate: P = -X + X²/M⁴

### Stability quantities
- Q_S = P_X + 2XP_XX
- c_S² = P_X / (P_X + 2XP_XX)
- Q_T = M_Pl², c_T² = 1 (tensor sector standard)

### Why bounce embedding could matter
c_S² depends on X = φ̇²/2. If the scalar kinetic energy becomes
large at the bounce, c_S² could change sign (gradient instability).

**Key question:** Does X become large at the bounce?

For a DE field with V ~ 10⁻¹²² M_Pl⁴ and m ~ H₀: the field
is frozen during the bounce. X_DE ≈ 0. So c_S² ≈ P_X(0,φ)/
P_X(0,φ) = 1. No issue.

For DBI with f ~ M_Pl⁻⁴: fX ~ 10⁻¹²² × M_Pl⁻⁴ × M_Pl⁴ ≈ 10⁻¹²².
c_S² ≈ 1 - 0 = 1. Safe.

### Risk assessment
**LOW.** Only dangerous if X ~ 1/(2f) ~ M_Pl⁴ (DBI limit).
For a DE field, X is negligible at the bounce.

### Expected result: TRIVIALLY_COMPATIBLE

### Tractability: IMMEDIATE

---

## Class C: Cubic Horndeski / Kinetic Gravity Braiding

### Action
```
G₂ = X - V(φ),  G₃ = β₃ X / M³,  G₄ = M_Pl²/2,  G₅ = 0
```

This is the "braiding" model where the scalar field couples
kinetically to gravity through φ̈φ̇² and Hφ̇³ terms.

### Stability quantities

The scalar sector stability involves the "braiding" parameter:

```
α_B = φ̇ X G₃X / (H M²) = β₃ φ̇ X / (H M³ M_Pl²)
```

This is defined with a factor of 1/H in the denominator.

At H = 0: **α_B diverges** (formally).

However, the PHYSICAL stability quantities Q_S and c_S²
do NOT contain 1/H. The α_B divergence is a parameterization
artifact. The underlying Horndeski stability conditions are:

```
Q_S ~ Σ + 3Θ²/(2w₁)
```

where Σ and Θ are specific combinations of G₂, G₃ and
background quantities. At H = 0, the H-dependent terms in
Σ and Θ vanish, leaving regular expressions.

### Why bounce embedding could matter

The braiding equation of motion contains:

```
φ̈(1 + 2β₃ Hφ̇/M³) + 3Hφ̇ + V' + β₃(2Ḣ + 3H²)φ̇²/M³ = 0
```

At H = 0:
```
φ̈ + V' + 2β₃ Ḣ φ̇²/M³ = 0
```

The term 2β₃ Ḣ φ̇²/M³ is an additional force proportional to
Ḣ ~ M_Pl². For M ~ H₀ (DE braiding scale):

```
2β₃ M_Pl² φ̇² / H₀³ ~ ENORMOUS if φ̇ ≠ 0
```

BUT: for a frozen DE field (φ̇ ≈ 0 at the bounce), this
force is zero. The question is whether φ̇ builds up during
the pre-bounce contraction.

During contraction (H < 0): the 3Hφ̇ term acts as ANTI-FRICTION,
potentially driving φ̇ to grow. If φ̇ grows significantly,
the braiding force at the bounce could be important.

### Risk assessment
**MODERATE.** The braiding anti-friction mechanism during
contraction could amplify φ̇ before the bounce, activating the
Ḣφ̇²/M³ force. This requires numerical investigation.

**Most promising candidate for non-trivial effect.**

### Expected result: WORTH_PHASE2

### Tractability: MODERATE (requires contraction+bounce numerics)

---

## Class D: Non-Minimal Coupling / Brans-Dicke / f(R)

### Action
```
G₂ = X - V(φ),  G₃ = G₅ = 0,  G₄ = f(φ)/2
```

Representative models:
- Brans-Dicke: f(φ) = φ (with kinetic term rescaling)
- Induced gravity: f(φ) = M_Pl² + ξφ²
- f(R): equivalent to G₄ = f'(R)/2 with appropriate φ(R)

### Stability quantities
- Q_T = f(φ) (must be > 0)
- c_T² = 1 (for G₄(φ) without X-dependence)
- Q_S involves f and f', regular for smooth f

### Why bounce embedding could matter

The curvature at the bounce: R = 6Ḣ ≈ 21 M_Pl².

For non-minimal coupling ξRφ²: this gives an effective mass
m_eff² = ξR ~ 21ξ M_Pl² at the bounce. For ξ < 0, this is
TACHYONIC. The field experiences a Planck-scale tachyonic
instability for ~ t_Pl.

Growth factor: exp(|ξ|^{1/2} × M_Pl × t_Pl) ≈ exp(|ξ|^{1/2}).
For |ξ| ~ O(1): factor of ~ e ≈ 2.7.

This is a BOUNDED perturbation, not a runaway instability.
The field gets an O(1) "kick" at the bounce but doesn't diverge.

For f(R) DE (Hu-Sawicki): f(R_bounce) - R_bounce ~ H₀²/R_bounce
~ 10⁻¹²² M_Pl². Negligible correction.

### Risk assessment
**LOW.** Transient tachyonic kick for ξ < 0 but bounded by
the brevity of the bounce. f(R) DE corrections negligible at
Planck curvature. No ghost or gradient instability.

### Expected result: TRIVIALLY_COMPATIBLE (with caveat for ξ < 0)

### Tractability: IMMEDIATE (analytic)

---

## Class E: Quartic/Quintic Horndeski (G₄(X), G₅)

### Action (quartic)
```
G₄ = M_Pl²/2 + g₄(φ)X/M²
```

### Action (quintic)
```
G₅ = g₅(φ)/M³
```

### Stability quantities

Tensor sector:
```
c_T² = [G₄ - XG₅φ - XG₅Xφ̈] / [G₄ - 2XG₄X + XG₅φ - Hφ̇XG₅X]
```

At H = 0: the Hφ̇XG₅X term in the denominator VANISHES.

### Why bounce embedding could matter

**Post-GW170817 constraint:** |c_T - 1| < 10⁻¹⁵ at z ≈ 0.
This requires G₄X ≈ 0 and G₅ ≈ 0 at late times (luminal
Horndeski). Models violating this are already excluded.

For models satisfying GW170817: the G₄X and G₅ terms are tiny
at late times. At the bounce (X → 0 for frozen DE), these terms
are ALSO tiny. The bounce adds no additional constraint.

**Note:** The Hφ̇XG₅X term that drops out at H = 0 was already
constrained to be negligible by GW170817. The bounce doesn't
provide a tighter constraint than existing observations.

### Risk assessment
**VERY LOW.** GW170817 has already eliminated the dangerous
parameter space. The bounce adds nothing.

### Expected result: TRIVIALLY_COMPATIBLE

### Tractability: IMMEDIATE (argument by GW170817 pre-emption)

---

## Class F: Beyond-Horndeski / DHOST

### Action
Extends Horndeski with terms like:

```
L_BH = F₄(φ,X) ε^{μνρσ} ε^{αβγ}_σ φ_μ φ_α ∇_ν∇_β φ ∇_ρ∇_γ φ
     + F₅(φ,X) ε^{μνρσ} ε^{αβγδ} φ_μ φ_α ∇_ν∇_β φ ∇_ρ∇_γ φ ∇_σ∇_δ φ
```

These have higher-order equations of motion but are DEGENERATE
(the extra degree of freedom has a constraint that removes it).

### Stability quantities
Same as Horndeski plus corrections from F₄, F₅.
The degeneracy conditions are ALGEBRAIC (conditions on the
Lagrangian functions, not on the background):

```
Class Ia: F₄ + F₅ = 0 (or equivalent)
```

### Why bounce embedding could matter

**Most promising in principle:** If the degeneracy conditions
involve background quantities (H, Ḣ), they could fail at H = 0,
reintroducing the ghost.

**Reality:** Standard DHOST degeneracy conditions are algebraic
conditions on F₄, F₅ and the G_i functions. They do NOT involve
the background. They hold for ALL field configurations.

The SECONDARY constraint (time evolution of the primary constraint)
does involve the background. But for standard DHOST, the secondary
constraint is automatically satisfied.

### Risk assessment
**LOW.** Degeneracy conditions are algebraic, background-independent.
No ghost reappearance at H = 0.

However: the strong coupling scale of DHOST could change at the
bounce (approaching the cutoff). This is an EFT validity question,
not a stability question.

### Expected result: TRIVIALLY_COMPATIBLE (for degeneracy);
possibly interesting for strong coupling (requires Phase 2)

### Tractability: MODERATE (degeneracy check: immediate;
strong coupling analysis: harder)

---

## Tractability Ranking

| Rank | Class | Tractability | Expected result |
|------|-------|-------------|----------------|
| 1 | A: Quintessence | Immediate | Trivially compatible |
| 2 | B: K-essence | Immediate | Trivially compatible |
| 3 | D: Non-minimal | Immediate | Trivially compatible |
| 4 | E: Quartic/Quintic | Immediate (GW170817) | Trivially compatible |
| 5 | C: Braiding | Moderate | **Worth Phase 2** |
| 6 | F: DHOST | Moderate-Hard | Probably compatible |

**Most promising for non-trivial constraint: Class C (braiding).**
