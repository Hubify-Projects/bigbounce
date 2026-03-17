# Foundation C — Candidate Action Classes

**Date:** 2026-03-14

---

## Overview

We construct five candidate actions involving curvature-dependent
mass generation. Each is analyzed for its mass mechanism, coupling
structure, evasion of previous obstructions, and primary risk.

---

## Candidate A: Conformally Coupled Geometric Scalar

### Action

```
S_A = ∫ d⁴x √g [
    ½M_Pl² R
    - ½(∂φ)² - (1/12) R φ²           [conformal kinetic sector]
    + (α/M_Pl) φ T^μ_μ               [coupling to matter trace]
]
```

The combination -½(∂φ)² - (1/12)Rφ² is conformally invariant in 4D
(with φ → Ω⁻¹φ under g_μν → Ω²g_μν). The conformal value ξ = 1/6
is not a tuning — it is enforced by the symmetry.

### What sets the mass

```
m²_eff = ξR = R/6
```

On FRW: R = 8πGρ(1 - 3w).
- Radiation (w = 1/3): R = 0 → m_eff = 0. Field is massless.
- Matter (w = 0): R = 3H² → m_eff = H/√2.
- de Sitter (w = -1): R = 12H² → m_eff = √2 H.
- Current epoch: R ≈ several H₀² → m_eff ~ H₀ ~ 10⁻³³ eV.

The mass TRACKS the Hubble scale through cosmic history.

### What sets the coupling

```
g_eff = α/M_Pl
```

This is a gravitational-strength coupling. Independent of ξ and R.

### Why it might evade previous obstructions

1. **Lock:** m depends on R (environment), g depends on α/M_Pl
   (Lagrangian parameter). These are independent. LOCK BROKEN.

2. **Duality:** φ is a scalar, not pseudoscalar. No shift symmetry
   needed. Conformal symmetry protects m₀ = 0 without requiring
   topological structure. DUALITY EVADED.

3. **FRW:** R ≠ 0 in matter/DE eras. The mass is O(H). FRW SURVIVES.

### Biggest risk

**This is standard scalar-tensor theory.** A conformally coupled
scalar with gravitational-strength coupling to T^μ_μ is the
Jordan-frame Brans-Dicke scalar in a specific limit. After a conformal
transformation to the Einstein frame, φ becomes a quintessence field
with a specific potential determined by the matter content.

The geometric "origin" of φ (from torsion trace, non-metricity trace,
or conformal factor) is invisible in the Einstein-frame description.
No distinctive geometric fingerprint survives.

**Radiative stability:** Conformal symmetry protects m₀ = 0 at
classical level. At one loop, the conformal anomaly generates:

```
δm₀² ~ (1/16π²) × (curvature-dependent terms) ~ O(H⁴/M_Pl²)
```

This is negligibly small compared to ξR ~ H². The environmental
mass is radiatively stable. This is a genuine positive feature.

---

## Candidate B: PGT 0⁺ Torsion Mode with Curvature Correction

### Action

```
S_B = ∫ d⁴x √g [
    ½M_Pl² R(Γ)
    + t₂ T^μ T_μ                      [torsion trace kinetic/mass]
    - ½ξ R(g) B₀²                     [curvature-dependent mass]
    + B₀ J_matter                      [matter coupling]
]
```

where B₀ is the scalar (0⁺) torsion trace and R(Γ) includes torsion
contributions.

### What sets the mass

```
m²_eff = m²_PGT + ξR

where m²_PGT = M_Pl² / (16π|t₂|)     [PGT bare mass, from the lock]
```

### What sets the coupling

```
g_eff = 1 / (M_Pl √|t₂|)             [from gravitational torsion-matter vertex]
```

### Why it might evade previous obstructions

It doesn't. The environmental correction ξR is negligible compared
to the locked PGT bare mass:

```
ξR / m²_PGT = 16π ξ |t₂| R / M_Pl²
            ~ 16π ξ |t₂| H₀² / M_Pl²
            ~ 10⁻¹²⁰ × ξ|t₂|
```

For |t₂| ~ O(1) and ξ ~ O(1): the ratio is 10⁻¹²⁰. The
environmental correction is utterly irrelevant.

To make the environmental term dominate: need ξ|t₂| ~ 10¹²⁰.
Either ξ or |t₂| must be enormous — a worse fine-tuning than
the original problem.

### Biggest risk

**The mass-coupling lock makes the bare mass ~M_Pl.** The
environmental correction ~H is 60 orders of magnitude smaller.
Adding ξR to a locked mass is like adding a grain of sand to
a mountain.

**Verdict: DEAD ON ARRIVAL.** The lock must be broken FIRST before
environmental corrections can matter. This candidate does not
evade Foundation A.

---

## Candidate C: Geometric Symmetron (Quartic Torsion Self-Interaction)

### Action

```
S_C = ∫ d⁴x √g [
    ½M_Pl² R
    - ½(∂φ)²
    + ½μ² φ² - ¼λ φ⁴                   [symmetry-breaking potential]
    - ½ξ R φ²                            [curvature-dependent mass]
    + (α/M_Pl) φ J                       [matter coupling]
]
```

The key feature: the quartic self-interaction ¼λφ⁴ allows a symmetron
mechanism where the field's VEV depends on the curvature.

### What sets the mass

**Low curvature (R < μ²/ξ):**
```
φ₀ = ±√((μ² - ξR)/λ)    [broken phase]
m² = 2(μ² - ξR)           [mass around VEV]
```

**High curvature (R > μ²/ξ):**
```
φ₀ = 0                     [symmetric phase]
m² = ξR - μ²               [mass at origin]
```

The transition occurs at R_crit = μ²/ξ. For R < R_crit: φ ≠ 0,
field mediates a fifth force. For R > R_crit: φ = 0, field decouples.

### What sets the coupling

In the broken phase:
```
g_eff = α φ₀ / M_Pl = (α/M_Pl) √((μ² - ξR)/λ)
```

The coupling depends on R through φ₀ — the coupling is ALSO
environment-dependent. This is the symmetron screening mechanism.

### Why it might evade previous obstructions

1. **Lock:** m and g both depend on R but through DIFFERENT functions.
   The mass goes as √(μ² - ξR), the coupling goes as √((μ² - ξR)/λ).
   These are not simply proportional unless λ = const. PARTIALLY BROKEN.

2. **Duality:** Scalar field, no shift symmetry needed. EVADED.

3. **FRW:** R ≠ 0 on FRW. The symmetron transition IS cosmologically
   relevant. FRW SURVIVES.

### Biggest risk

**μ² must be tuned.** For the symmetron transition to occur at
cosmological curvatures: need R_crit = μ²/ξ ~ H₀². With ξ ~ O(1):
μ ~ H₀ ~ 10⁻³³ eV. This is a NEW fine-tuning of μ.

No symmetry protects this small μ. Conformal symmetry sets μ = 0,
but then the symmetron mechanism doesn't work (no broken phase).

The geometric origin (torsion self-interaction for λ, curvature
coupling for ξ) provides structure but does not protect μ. The
naturalness problem is transferred from "why is m tiny?" to
"why is μ tiny?"

**Verdict: FAILS NATURALNESS.** The symmetron mechanism works but
requires a tuned scale μ ~ H₀ that no known geometric symmetry
protects.

---

## Candidate D: Weyl Geometry / Trace Non-Metricity Scalar

### Action

In Weyl geometry, non-metricity is pure trace: Q_μαβ = Q_μ g_αβ.
The Weyl vector Q_μ has local scale gauge invariance Q_μ → Q_μ + ∂_μΛ.

```
S_D = ∫ d⁴x √g [
    ½M_Pl² R_W                          [Weyl-invariant curvature]
    + β Q_μν Q^{μν}                     [Weyl field strength]
    + (matter coupled through Weyl-covariant derivative)
]
```

where R_W = R + 6∇_μQ^μ - 6Q_μQ^μ is the Weyl-invariant Ricci scalar
and Q_μν = ∂_μQ_ν - ∂_νQ_μ.

### Stückelberg decomposition

Write Q_μ = A_μ + ∂_μσ where A_μ is transverse and σ is the
longitudinal (Stückelberg) scalar. After gauge fixing:

```
S_D → ∫ d⁴x √g [
    ½M_Pl² R
    - ½(∂σ)²(6M_Pl² + ...)              [kinetic term for σ]
    - 3M_Pl² R σ + ...                   [non-minimal coupling]
    + β (∂A)²                            [transverse vector, decouples]
    + ...
]
```

The scalar σ has a non-minimal coupling to R with coefficient set by
M_Pl. After canonical normalization:

```
m²_eff ~ R (from non-minimal coupling)
g ~ 1/M_Pl (from geometric coupling)
```

### What sets the mass

The Weyl gauge symmetry forces m₀ = 0 exactly (mass term would break
gauge invariance). The only mass is environmental: m² ~ R ~ H².

### What sets the coupling

The matter coupling comes from the Weyl-covariant derivative and is
gravitational strength: g ~ 1/M_Pl.

### Why it might evade previous obstructions

1. **Lock:** m depends on R (environment), g depends on 1/M_Pl
   (fixed by Newton's constant). LOCK BROKEN.

2. **Duality:** σ is a scalar. No shift/topological issues. EVADED.

3. **FRW:** R ≠ 0 in matter/DE eras. FRW SURVIVES.

4. **Naturalness:** m₀ = 0 is GAUGE-PROTECTED (Weyl symmetry).
   This is as robust as the photon mass being zero (U(1) gauge
   symmetry). NATURAL.

### Biggest risk

**After Stückelberg decomposition, σ is a conformally coupled scalar.**
The Weyl geometric origin is invisible — the Einstein-frame action
is equivalent to Candidate A with specific parameter values.

The Weyl gauge symmetry is a STRONGER motivation for m₀ = 0 than
conformal symmetry (gauge protection vs. global symmetry). But the
phenomenological output is the same.

**Additional risk:** The transverse vector A_μ may have ghost
instabilities in some parameter ranges. The ghost-free conditions
for Weyl geometry vectors are known (Percacci et al.) but constrain
the action significantly.

**Verdict: STRUCTURALLY STRONGEST but phenomenologically equivalent
to Candidate A.** The gauge protection of m₀ = 0 is the most
robust argument among all candidates. But the low-energy EFT is
standard scalar-tensor theory.

---

## Candidate E: Curvature-Dependent Kinetic Normalization (PGT + R²)

### Action

```
S_E = ∫ d⁴x √g [
    ½M_Pl² R + b₁ R²                    [Einstein-Hilbert + Starobinsky]
    + t₃ (∂B)²                           [torsion 0⁻ kinetic]
    + μ² B²                              [torsion mass]
    + (1/M_Pl) B J                       [matter coupling]
]
```

On curved backgrounds, the R² term generates kinetic mixing between
the scalaron and the torsion mode. The effective kinetic normalization
Z_eff depends on R.

### What sets the mass

After diagonalization on FRW:

```
m_phys = μ / √Z_eff(R)
g_phys = g_bare / √Z_eff(R)
```

Both m and g scale with the SAME power of Z_eff. The ratio:

```
R_ratio = m/g = μ / g_bare = (independent of Z_eff)
```

### Lock test

**STILL LOCKED.** Curvature-dependent kinetic normalization rescales
BOTH mass and coupling by the same factor. The ratio R = m/g is
unchanged. The lock is a property of the ratio, not of the individual
values.

### Why it fails

The lock is a structural property: m and g share the same kinetic
normalization. Any modification to Z affects both equally. Only an
INDEPENDENT contribution to the mass (not through Z) can break the lock.

This candidate does not introduce an independent mass contribution —
it only modifies Z. The lock persists.

**Verdict: FAILS LOCK TEST.** Curvature-dependent kinetic mixing
does not break the mass-coupling lock.

---

## Summary Table

| Candidate | Lock | Duality | FRW | Naturalness | Distinctiveness |
|-----------|------|---------|-----|-------------|-----------------|
| A: Conformal scalar | **BROKEN** | **EVADED** | **SURVIVES** | **GOOD** (conformal sym.) | FAILS (= scalar-tensor) |
| B: PGT 0⁺ + ξR | IRRELEVANT | N/A | IRRELEVANT | FAILS (bare mass dominates) | N/A |
| C: Symmetron | **BROKEN** | **EVADED** | **SURVIVES** | FAILS (μ tuned) | Marginal |
| D: Weyl scalar | **BROKEN** | **EVADED** | **SURVIVES** | **BEST** (gauge sym.) | FAILS (= Candidate A) |
| E: Kinetic mixing | **LOCKED** | N/A | N/A | N/A | N/A |

### Priority ranking

1. **Candidate D (Weyl scalar):** Strongest theoretical motivation
   (gauge-protected m₀ = 0). But phenomenologically = Candidate A.

2. **Candidate A (Conformal scalar):** Simplest realization.
   Conformally protected m₀ = 0. Standard scalar-tensor after reduction.

3. **Candidate C (Geometric symmetron):** Interesting mechanism but
   requires tuned μ ~ H₀.

4. **Candidate B (PGT + ξR):** Dead on arrival. Lock makes bare mass
   too large.

5. **Candidate E (Kinetic mixing):** Lock persists. No progress.
