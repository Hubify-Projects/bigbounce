# The Quadratic Poincaré Gauge Theory Action

**Date:** 2026-03-16

---

## 1. General PGT Action

The Poincaré gauge theory of gravity gauges the full Poincaré group
ISO(1,3) = SO(1,3) ⋉ T(1,3). The independent field variables are
the tetrad e^a_μ (translation gauge field) and the Lorentz
connection ω^{ab}_μ (rotation gauge field). The corresponding
field strengths are:

- **Torsion:** T^a_{μν} = ∂_μ e^a_ν - ∂_ν e^a_μ + ω^a_{bμ} e^b_ν - ω^a_{bν} e^b_μ
- **Curvature:** R^{ab}_{μν} = ∂_μ ω^{ab}_ν - ∂_ν ω^{ab}_μ + ω^a_{cμ} ω^{cb}_ν - ω^a_{cν} ω^{cb}_μ

The most general parity-preserving quadratic PGT Lagrangian is:

```
L_PGT = -(M_Pl²/2) R + L_T² + L_R²
```

where R = e_a^μ e_b^ν R^{ab}_{μν} is the curvature scalar.

### Torsion-squared sector

The torsion tensor decomposes into three irreducible parts under
the Lorentz group:

```
T^a_{μν} = ⁽¹⁾T^a_{μν} + ⁽²⁾T^a_{μν} + ⁽³⁾T^a_{μν}
```

where:
- ⁽²⁾T: **tensor** (hook symmetry, traceless) — 16 components
- ⁽¹⁾T: **trace vector** T_μ = T^ν_{νμ} — 4 components
- ⁽³⁾T: **axial vector** S_μ = ε_{μνρσ} T^{νρσ} — 4 components

The torsion-squared Lagrangian:

```
L_T² = (1/2)[a₁ ⁽¹⁾T_aμν ⁽¹⁾T^{aμν} + a₂ ⁽²⁾T_aμν ⁽²⁾T^{aμν} + a₃ ⁽³⁾T_aμν ⁽³⁾T^{aμν}]
```

Equivalently, in the Hayashi-Shirafuji parametrization using the
three invariants:

```
I₁ = T_{μνρ} T^{μνρ}
I₂ = T_{μνρ} T^{νμρ}
I₃ = T_μ T^μ        (where T_μ = T^ν_{νμ})
```

The decomposition:
```
⁽¹⁾T·⁽¹⁾T = (1/3)(2I₁ + I₂) - (2/3)I₃
⁽²⁾T·⁽²⁾T = (2/3)(I₁ - I₂) + (2/3)I₃
⁽³⁾T·⁽³⁾T = -(1/3)(I₁ + 2I₂) + (2/3)I₃  [Note: normalization conventions vary]
```

We use the parametrization:

```
L_T² = (1/2)(t₁ I₁ + t₂ I₂ + t₃ I₃)
     = (1/2)(t₁ T_{μνρ}T^{μνρ} + t₂ T_{μνρ}T^{νμρ} + t₃ T_μ T^μ)
```

The relation to irreducible couplings:
```
a₁ = (2t₁ + t₂)/3
a₂ = (2t₁ - 2t₂)/3     [or appropriate combination depending on normalization]
a₃ = -(t₁ + 2t₂)/3
```

with the trace coupling mixed in via t₃.

### Curvature-squared sector

```
L_R² = (1/2)(b₁ R_{abμν}R^{abμν} + b₂ R_{abμν}R^{μνab}
        + b₃ R_{abμν}R^{baμν} + b₄ R_{aμ}R^{aμ}
        + b₅ R_{aμ}R^{μa} + b₆ R²)
```

where R_{aμ} = R^b_{aμb} is the Ricci-type contraction.

The b_i parameters control curvature-squared propagation and are
relevant for massive spin-2 modes. For this analysis, we focus
primarily on the torsion sector (t₁, t₂, t₃) and note that the
b_i enter the ghost-free conditions.

---

## 2. Propagating Torsion Modes

### Linearized spectrum

On a Minkowski background, the PGT action propagates the following
modes from the torsion sector (Sezgin & van Nieuwenhuizen 1980,
Hayashi & Shirafuji 1980):

| Mode | Spin-parity J^P | Irrep | DOF | Mass² |
|------|:---------------:|-------|:---:|-------|
| Torsion trace | 0⁻ | Pseudoscalar from T_μ | 1 | m₀²(t_i) |
| Torsion trace | 1⁻ | Vector from T_μ | 3 | m₁²(t_i) |
| Axial torsion | 0⁺ | Scalar from S_μ | 1 | m̃₀²(t_i) |
| Axial torsion | 1⁺ | Axial vector from S_μ | 3 | m̃₁²(t_i) |
| Tensor torsion | 2⁺ | Symmetric tensor from ⁽²⁾T | 5 | m₂²(t_i) |

**Total potential DOF from torsion: up to 13** (beyond the 2 of GR).

Not all modes propagate simultaneously. Which modes propagate
depends on the parameter choices (t_i, b_i). Specific parameter
choices can project out dangerous modes.

### Key result from the literature

The SAFEST scenario (Sezgin & van Nieuwenhuizen 1980, Neville 1980)
is to allow only ONE torsion mode to propagate while keeping all
others non-propagating or decoupled. This minimizes ghost risks.

The viable single-mode sectors identified in the literature:

**Sector I: Spin-0⁺ only** (scalar torsion)
- The axial part S_μ reduces to a single propagating pseudoscalar
- Requires specific parameter tuning to decouple spin-1 and spin-2

**Sector II: Spin-0⁻ only** (pseudoscalar torsion from trace)
- The trace T_μ reduces to a pseudoscalar mode
- Requires decoupling of the vector (spin-1) component

**Sector III: Spin-2⁺ only** (tensor torsion)
- The tensor irrep propagates as a massive spin-2
- DANGEROUS: massive spin-2 is generically ghostly
  (Boulware-Deser ghost) unless specific constraints are imposed

---

## 3. Torsion Mass Parameters

### For the trace vector T_μ

The mass of the spin-0⁻ mode from the trace sector:

```
m₀² = -M_Pl² / (4t₃ + 2t₁ + t₂)
```

(Sign conventions: m₀² > 0 requires appropriate sign of the
denominator.)

For the spin-1⁻ vector mode:

```
m₁² = -M_Pl² / (2t₁ + t₂)
```

### For the axial vector S_μ

The mass of the spin-0⁺ mode from the axial sector:

```
m̃₀² = M_Pl² / (t₁ + 2t₂)     [up to sign convention]
```

For the spin-1⁺ axial vector mode:

```
m̃₁² = M_Pl² / (t₁ - t₂)
```

### For the tensor mode

```
m₂² = M_Pl² / (some combination of b_i)
```

(The tensor torsion mass involves the curvature-squared parameters.)

### Key observation

**All torsion masses scale as M_Pl² / t_i.** To get m_T ≪ M_Pl,
we need |t_i| ≫ 1:

```
m_T ~ M_Pl / √|t_i|

m_T = 10⁹ GeV  →  |t_i| ~ 10²⁰
m_T = 10⁵ GeV  →  |t_i| ~ 10²⁸
m_T = 10³ GeV  →  |t_i| ~ 10³²
```

This is a LARGE HIERARCHY in the dimensionless PGT couplings.

---

## 4. Which Parameters Control Ghost Freedom

### Kinetic terms

The sign of the kinetic term for each torsion mode determines
ghost freedom:

| Mode | Ghost-free condition |
|------|---------------------|
| Spin-0⁻ (trace pseudoscalar) | 4t₃ + 2t₁ + t₂ < 0 |
| Spin-1⁻ (trace vector) | 2t₁ + t₂ < 0 |
| Spin-0⁺ (axial scalar) | t₁ + 2t₂ > 0 |
| Spin-1⁺ (axial vector) | t₁ - t₂ > 0 |
| Spin-2⁺ (tensor) | Requires b_i conditions |

(Signs depend on metric signature and Lagrangian sign conventions.
We use (+,-,-,-) metric and action S = ∫d⁴x √(-g) L.)

### The critical point

Ghost freedom constrains the SIGNS of parameter combinations.
The torsion mass values constrain the MAGNITUDES. These are
independent conditions — in principle, a large |t_i| (light torsion)
can satisfy ghost-free sign conditions.

**However:** having only ONE healthy propagating mode requires the
OTHER modes to be non-propagating. This means specific parameter
RELATIONS (not just sign conditions) that may conflict with the
large-|t_i| requirement.

---

## 5. Minimal Viable PGT Sector

### The safest choice: single propagating spin-0⁺

Following Karananas (2015) and Blagojević & Hehl (2013), the
cleanest ghost-free sector has:

1. **One propagating scalar (spin-0⁺)** from the axial torsion
2. **All other torsion modes non-propagating** (projected out by
   parameter choices)

The conditions:
```
Propagating 0⁺:  t₁ + 2t₂ > 0,  m̃₀² > 0
Non-propagating others:  specific relations among (t₁, t₂, t₃, b_i)
```

### Alternative: single propagating spin-0⁻

```
Propagating 0⁻:  4t₃ + 2t₁ + t₂ < 0,  m₀² > 0
Non-propagating others:  specific relations
```

### In both cases

The propagating mode has mass:
```
m_T² = M_Pl² / |combination of t_i|
```

For m_T ≪ M_Pl: the relevant |t_i| combination ≫ 1.

---

## 6. Summary of Key Structures

| Quantity | Expression | Role |
|----------|-----------|------|
| t₁, t₂, t₃ | Dimensionless PGT torsion-squared couplings | Define torsion dynamics |
| b₁...b₆ | Dimensionless PGT curvature-squared couplings | Affect spin-2 sector |
| m_T² | M_Pl² / f(t_i) | Physical torsion mass |
| Ghost-free | Sign conditions on t_i combinations | Healthy propagation |
| m_T ≪ M_Pl | |t_i| ≫ 1 | Required for lower-scale bounce |
| ρ_crit | ~ m_T² M_Pl² = M_Pl⁴ / |f(t_i)| | Bounce energy density |

### The central question for the next files

Can a ghost-free PGT sector have |t_i| ≫ 1 (light torsion) while:
1. Keeping exactly one healthy propagating mode?
2. Not reintroducing the Foundation A mass-coupling lock?
3. Having the bounce dynamics remain qualitatively similar to EC?
