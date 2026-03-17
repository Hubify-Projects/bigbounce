# Stability Framework for Horndeski DE at the Bounce

**Date:** 2026-03-16

---

## The Four Stability Conditions

For any Horndeski theory on an FRW background, the absence of
pathological perturbations requires four conditions:

### 1. Scalar ghost freedom: Q_S > 0

The kinetic matrix for the scalar perturbation ζ must be positive
definite. Q_S is constructed from the Horndeski functions G_i
and background quantities.

**Ghost** = wrong-sign kinetic term → unbounded negative energy
→ vacuum instability on arbitrarily short timescales.

### 2. Scalar gradient stability: c_S² > 0

The scalar sound speed squared must be positive. c_S² < 0 means
exponential growth of short-wavelength perturbations.

**Gradient instability** = exponential growth rate ~ k|c_S|
→ UV catastrophe on timescale ~ 1/(k|c_S|) → instantaneous
for k → ∞.

### 3. Tensor ghost freedom: Q_T > 0

The kinetic matrix for tensor perturbations h_ij must be
positive definite.

### 4. Tensor gradient stability: c_T² > 0

Additionally, c_T² ≈ 1 is required by GW170817 at late times,
but at the bounce only c_T² > 0 is needed for stability.

---

## Horndeski Stability Quantities (Bellini-Sawicki Form)

For general Horndeski with functions G₂, G₃, G₄, G₅:

### Tensor sector

```
Q_T = 2(G₄ - 2XG₄X + XG₅φ - Hφ̇XG₅X)
c_T² = [G₄ - Xφ̈G₅X - XG₅φ] / [G₄ - 2XG₄X + XG₅φ - Hφ̇XG₅X]
```

At H = 0 and X → 0:
```
Q_T → 2G₄(φ, 0) = 2 × M_Pl²/2 = M_Pl²     (for standard G₄)
c_T² → G₄(φ, 0) / G₄(φ, 0) = 1
```

**Regular at H = 0.** The Hφ̇XG₅X term that drops out is already
constrained to be negligible by GW170817.

### Scalar sector

The scalar stability quantities are more complex. In the
Bellini-Sawicki α-parameterization:

```
α_K = (2X/H²)(G₂X + 2XG₂XX + ...)
α_B = (φ̇/H)(XG₃X/M² + ...)
α_M = ...
α_T = ...
```

**PROBLEM:** α_K has a factor of 1/H² and α_B has 1/H.
These DIVERGE at H = 0.

### The α-parameterization breakdown

The EFT-of-DE α-parameterization (Bellini & Sawicki 2014) was
designed for an EXPANDING universe (H > 0). At H = 0:

| Parameter | H-dependence | At H = 0 |
|-----------|-------------|---------|
| α_K | ∝ 1/H² | DIVERGENT |
| α_B | ∝ 1/H | DIVERGENT |
| α_M | ∝ 1/H | DIVERGENT |
| α_T | none | Regular |

**This is a PARAMETERIZATION ARTIFACT, not a physical instability.**

The physical quantities Q_S and c_S² are RATIOS of the divergent
α parameters that remain finite. Specifically:

```
Q_S ∝ (α_K + 6α_B²) × H² / c_S²    [schematic]
```

The H² factor cancels the 1/H² in α_K and the (1/H)² in α_B².

### Direct Lagrangian stability conditions

Working directly with the G_i functions (not the α parameters):

**Scalar no-ghost (Q_S > 0):**
```
Q_S = w₁[Σ(w₁ + 3Θ²/2)] / (w₁Σ + 9Θ²/2)²
```

where:
```
w₁ = 2(G₄ - 2XG₄X + XG₅φ) - 2Xφ̇HG₅X      [= Q_T/2]
Σ = Xφ̇HG₃X + 2XG₂X + ... (long expression)
Θ = -φ̇HG₃X/2 + ... (long expression)
```

At H = 0 with X → 0:
- w₁ → G₄(φ, 0) = M_Pl²/2
- Terms with H factors → 0
- Remaining terms are regular functions of φ and X → 0

**The stability conditions are REGULAR at H = 0 when expressed
in terms of the original Lagrangian functions.**

---

## Verdict Labels

For each model class, we assign one of:

| Label | Meaning |
|-------|---------|
| **TRIVIALLY_COMPATIBLE** | All stability conditions trivially satisfied at bounce; no parameter restriction |
| **COMPATIBLE_WITH_CAVEAT** | Stable at bounce but with a quantifiable transient effect (kick, amplification) that does not destroy DE viability |
| **CONDITIONALLY_COMPATIBLE** | Stable only for restricted parameter range; bounce provides nontrivial constraint |
| **EFT_INAPPLICABLE** | Theory's EFT breaks down at bounce energy scale; cannot assess stability |
| **INCOMPATIBLE** | Genuine ghost or gradient instability at the bounce for generic parameters |

---

## Applying the Framework

### What counts as a nontrivial result

A nontrivial result requires that the bounce provides information
BEYOND what is already known from:
1. Late-time stability (standard Horndeski analysis)
2. GW170817 constraint
3. Solar system tests
4. General EFT validity

If the bounce merely re-derives a known constraint, that is
NOT nontrivial. The bounce must add a NEW restriction.

### What the H = 0 crossing tells us

The bounce is the ONLY known physical scenario where H passes
smoothly through zero. In standard cosmology (Big Bang → expansion),
H > 0 always. The bounce provides a unique test of:

1. Whether stability conditions have 1/H singularities
   → If physical quantities are singular: INCOMPATIBLE
   → If only parameterization is singular: TRIVIALLY_COMPATIBLE
   (with methodological finding about EFT-of-DE)

2. Whether Ḣ > 0 + H = 0 creates new instability channels
   → The combination (H = 0, Ḣ > 0) never occurs in standard
   cosmology (where Ḣ < 0 in matter/radiation domination)
   → Could reveal instabilities hidden by H > 0 assumption

3. Whether the contraction phase (H < 0) preceding the bounce
   creates conditions (amplified φ̇, modified initial conditions)
   that trigger instabilities AT the bounce

### What counts as an EFT breakdown

An EFT breakdown occurs when the theory's cutoff scale Λ is
exceeded by the background curvature. At the bounce:

```
R ≈ 21 M_Pl²,  ρ ≈ 0.21 M_Pl⁴
```

Any DE theory with internal scale M ≪ M_Pl has:
```
R/M² ≫ 1
```

This means the EFT expansion parameter is large and higher-order
operators (suppressed by M in the low-energy theory) become
important. The theory cannot make reliable predictions.

This is NOT a failure of the DE model — it is a statement that
the DE model was never designed to operate at Planck curvature.

**An EFT breakdown is a METHODOLOGICAL finding, not a stability
exclusion.** It tells us that assessing bounce compatibility
requires UV completion of the DE sector — additional information
beyond what the low-energy EFT provides.

---

## Summary

The stability framework reveals a three-way classification:

1. **Theories with Planck-scale or no internal scale** (quintessence,
   k-essence with M ~ M_Pl): stability conditions regular at bounce,
   trivially satisfied because X ≈ 0.

2. **Theories with sub-Planckian internal scale** (braiding with
   M ~ H₀, DHOST with Λ ~ 10⁻⁴⁰ M_Pl): EFT breaks down at
   bounce, cannot assess stability within the low-energy theory.

3. **Theories with curvature coupling** (non-minimal with ξ):
   transient effects at bounce (tachyonic kick), bounded by
   bounce duration, not genuine instabilities for |ξ| ≲ O(10).

**The dominant finding is methodological: the EFT-of-DE
parameterization breaks down at H = 0, and DE theories with
low internal scales cannot be assessed at Planck curvature.
This is success criterion 4 (methodological constraint).**
