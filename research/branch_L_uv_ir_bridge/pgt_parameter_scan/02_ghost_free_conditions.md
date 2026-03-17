# Ghost-Free Conditions in Quadratic PGT

**Date:** 2026-03-16

---

## 1. Literature Sources

The ghost/tachyon analysis of quadratic PGT was established by:

- **Sezgin & van Nieuwenhuizen (1980):** First systematic
  classification of propagating modes and ghost conditions
- **Hayashi & Shirafuji (1980):** Independent derivation in
  tetrad formulation
- **Neville (1980):** Ghost-free sectors enumerated
- **Kuhfuss & Nitsch (1986):** Refined conditions including
  tachyon absence
- **Yo & Nester (1999, 2002):** Updated conditions, FRW
  cosmology applications
- **Karananas (2015):** Modern rederivation with explicit
  propagator analysis
- **Blagojević & Cvetković (2018):** Hamiltonian constraint
  analysis

---

## 2. Mode Spectrum and Conditions

### Spin-parity content

The 24 components of the Lorentz connection ω^{ab}_μ decompose
on Minkowski into:

| J^P | Source | DOF | Kinetic sign condition | Mass² condition |
|:---:|--------|:---:|----------------------|----------------|
| 2⁺ | Tensor torsion ⁽²⁾T | 5 | A₂ > 0 | M₂² > 0 |
| 2⁻ | Curvature sector | 5 | B₂ > 0 | N₂² > 0 |
| 1⁺ | Axial vector S_μ | 3 | A₁⁺ > 0 | M₁⁺² > 0 |
| 1⁻ | Trace vector T_μ | 3 | A₁⁻ > 0 | M₁⁻² > 0 |
| 0⁺ | Axial scalar (from S_μ) | 1 | A₀⁺ > 0 | M₀⁺² > 0 |
| 0⁻ | Trace scalar (from T_μ) | 1 | A₀⁻ > 0 | M₀⁻² > 0 |

where A_i are kinetic coefficients (must be positive for no ghosts)
and M_i² are mass-squared values (must be positive for no tachyons).

### Explicit conditions (Hayashi-Shirafuji / Yo-Nester parametrization)

Using the (t₁, t₂, t₃) torsion parameters from File 01:

**Spin-0⁻ (trace pseudoscalar):**
```
A₀⁻ = -(4t₃ + 2t₁ + t₂)      Ghost-free: 4t₃ + 2t₁ + t₂ < 0
M₀⁻² = M_Pl² / A₀⁻            Tachyon-free: M₀⁻² > 0 (auto if A₀⁻ > 0)
```

**Spin-0⁺ (axial scalar):**
```
A₀⁺ = (t₁ + 2t₂)              Ghost-free: t₁ + 2t₂ > 0
M₀⁺² = M_Pl² / A₀⁺            Tachyon-free: auto
```

**Spin-1⁻ (trace vector):**
```
A₁⁻ = -(2t₁ + t₂)             Ghost-free: 2t₁ + t₂ < 0
M₁⁻² = M_Pl² / A₁⁻            Tachyon-free: auto
```

**Spin-1⁺ (axial vector):**
```
A₁⁺ = (t₁ - t₂)               Ghost-free: t₁ - t₂ > 0
M₁⁺² = M_Pl² / A₁⁺            Tachyon-free: auto
```

**Spin-2⁺ (tensor torsion):**
```
A₂ = t₁                        Ghost-free: t₁ > 0
M₂² involves (t_i, b_i)        Tachyon-free: requires b_i conditions
```

**Spin-2⁻ (curvature sector):**
```
A₂⁻ involves b_i only          Ghost-free: b_i conditions
M₂⁻² involves b_i              Tachyon-free: b_i conditions
```

---

## 3. The Ghost-Free Dilemma

### All modes propagating simultaneously

If ALL six mode types propagate, ghost freedom requires
ALL kinetic conditions simultaneously:

```
t₁ > 0                         (from 2⁺)
t₁ - t₂ > 0                    (from 1⁺)
t₁ + 2t₂ > 0                   (from 0⁺)
2t₁ + t₂ < 0                   (from 1⁻)
4t₃ + 2t₁ + t₂ < 0             (from 0⁻)
```

The first three conditions give:
```
t₁ > 0
-t₁/2 < t₂ < t₁
```

The fourth condition gives:
```
t₂ < -2t₁
```

**CONTRADICTION:** t₂ < t₁ and t₂ < -2t₁ with t₁ > 0 requires
t₂ < -2t₁ < 0, but also t₂ > -t₁/2. This gives:

```
-t₁/2 < t₂ < -2t₁
```

For t₁ > 0: -t₁/2 > -2t₁, so the interval is NON-EMPTY:
-t₁/2 < t₂ < -2t₁ requires -t₁/2 < -2t₁, i.e., 2t₁ < t₁/2,
i.e., t₁ < 0.

**CONTRADICTION with t₁ > 0.** Therefore:

> **All six torsion modes CANNOT simultaneously propagate
> ghost-free.** This is a well-known result (Neville 1980,
> Sezgin & van Nieuwenhuizen 1980).

### Resolution: project out dangerous modes

The viable strategy is to choose parameters so that only a SUBSET
of modes propagates, with the others having infinite mass (frozen)
or zero kinetic term (non-dynamical).

---

## 4. Viable Ghost-Free Sectors

### Sector I: Only spin-0⁺ propagates

**Conditions:**
```
t₁ + 2t₂ > 0           (0⁺ has healthy kinetic term)
A₁⁺ = 0  →  t₁ = t₂   (1⁺ non-propagating: degenerate)
A₁⁻ → 0                (1⁻ non-propagating or infinitely massive)
A₂ → 0                  (2⁺ non-propagating or infinitely massive)
```

**Simplest realization:** t₁ = t₂ > 0, with t₃ chosen freely.

Mass of the propagating 0⁺ mode:
```
m₀⁺² = M_Pl² / (t₁ + 2t₂) = M_Pl² / (3t₁)    (when t₁ = t₂)
```

For m₀⁺ ≪ M_Pl: need t₁ = t₂ ≫ 1.

**Ghost-free?** YES — the 0⁺ mode has positive kinetic term for
t₁ + 2t₂ > 0. The other modes are non-propagating.

**Tachyon-free?** YES — m₀⁺² > 0 automatically.

**Caveat:** Setting t₁ = t₂ exactly is a fine-tuning (measure-zero
in parameter space). Small deviations t₁ ≠ t₂ reactivate the 1⁺
mode with mass m₁⁺² = M_Pl² / (t₁ - t₂). If |t₁ - t₂| ≪ t₁,
this mode is ultra-heavy and decouples. The fine-tuning is soft:
deviations are phenomenologically harmless if small.

---

### Sector II: Only spin-0⁻ propagates

**Conditions:**
```
4t₃ + 2t₁ + t₂ < 0     (0⁻ has healthy kinetic term)
2t₁ + t₂ = 0            (1⁻ non-propagating: t₂ = -2t₁)
t₁ + 2t₂ ≤ 0            (0⁺ non-propagating or ghostly → decouple)
```

With t₂ = -2t₁:
```
t₁ + 2t₂ = t₁ - 4t₁ = -3t₁
```

For t₁ > 0: t₁ + 2t₂ = -3t₁ < 0, so 0⁺ is indeed non-propagating
(negative kinetic → ghost if propagating, but here it's a
constraint mode).

The 0⁻ kinetic coefficient:
```
A₀⁻ = -(4t₃ + 2t₁ + t₂) = -(4t₃ + 2t₁ - 2t₁) = -4t₃
```

Ghost-free: -4t₃ > 0 → t₃ < 0.

Mass:
```
m₀⁻² = M_Pl² / (-4t₃) = M_Pl² / (4|t₃|)
```

For m₀⁻ ≪ M_Pl: need |t₃| ≫ 1.

**This is the sector most relevant to the bounce.** The spin-0⁻
mode is a pseudoscalar that couples to the fermion axial current
(same structure as the EC torsion coupling). In the FRW limit,
it reduces to a dynamical torsion that modifies the Friedmann
equation.

---

### Sector III: Only spin-2⁺ propagates

Requires t₁ > 0 with all spin-0 and spin-1 modes decoupled.

**DANGEROUS:** A massive spin-2 field generically suffers from the
Boulware-Deser ghost (extra scalar degree of freedom at nonlinear
level). In PGT, this may be avoided because the spin-2 arises from
the torsion (antisymmetric part of the connection) rather than the
metric (symmetric). However, the nonlinear ghost analysis is
incomplete in the literature.

**Status:** NOT SAFE for our purposes. We exclude this sector.

---

### Sector IV: Mixed spin-0⁺ + spin-0⁻

Both scalar modes propagate, all spin-1 and spin-2 decoupled.

Requires:
```
t₁ + 2t₂ > 0            (0⁺ healthy)
4t₃ + 2t₁ + t₂ < 0      (0⁻ healthy)
2t₁ + t₂ = 0             (1⁻ decoupled → t₂ = -2t₁)
t₁ = t₂                  (1⁺ decoupled)
```

**CONTRADICTION:** t₂ = -2t₁ and t₂ = t₁ requires t₁ = -2t₁,
i.e., t₁ = 0. Then all torsion kinetic terms vanish.

**Cannot have both scalars with both vectors decoupled.**

Alternative: decouple vectors by making them super-heavy rather
than exactly non-propagating. This relaxes the exact conditions
but introduces two nearly-degenerate heavy modes.

---

## 5. Summary of Viable Ghost-Free Sectors

| Sector | Propagating mode | Key parameter relation | Mass formula | Status |
|--------|-----------------|----------------------|-------------|--------|
| I | 0⁺ (axial scalar) | t₁ = t₂ > 0 | m² = M_Pl²/(3t₁) | **SAFE** |
| II | 0⁻ (trace pseudoscalar) | t₂ = -2t₁, t₃ < 0 | m² = M_Pl²/(4\|t₃\|) | **SAFE** |
| III | 2⁺ (tensor) | t₁ > 0, others decoupled | Involves b_i | UNSAFE (BD ghost) |
| IV | 0⁺ + 0⁻ | Cannot exactly decouple both vectors | — | REQUIRES SOFT TUNING |

**Bottom line: Sectors I and II are the cleanly ghost-free options.**

---

## 6. Light Torsion in Ghost-Free Sectors

### Sector I (0⁺)

```
m₀⁺ = M_Pl / √(3t₁)

m₀⁺ = 10⁹ GeV  →  t₁ = 10²⁰ / 3
m₀⁺ = 10⁵ GeV  →  t₁ = 10²⁸ / 3
m₀⁺ = 10³ GeV  →  t₁ = 10³² / 3
```

Ghost-free condition t₁ = t₂ > 0 is COMPATIBLE with large t₁.
No sign conflict. The hierarchy t₁ ≫ 1 is the only requirement.

### Sector II (0⁻)

```
m₀⁻ = M_Pl / (2√|t₃|)

m₀⁻ = 10⁹ GeV  →  |t₃| = 10²⁰ / 4
m₀⁻ = 10⁵ GeV  →  |t₃| = 10²⁸ / 4
m₀⁻ = 10³ GeV  →  |t₃| = 10³² / 4
```

Ghost-free condition t₃ < 0 with |t₃| ≫ 1 is COMPATIBLE.
No sign conflict.

### Key finding

> **Ghost freedom does NOT prevent light torsion.** The ghost-free
> conditions constrain SIGNS, not magnitudes. Large |t_i| ≫ 1
> (light torsion) is compatible with ghost-free sign conditions
> in both Sectors I and II.

---

## 7. Tachyon Absence

In both Sectors I and II, the mass-squared is automatically positive
when the ghost-free conditions hold (the sign of the kinetic term
ensures m² = M_Pl² / A > 0 when A > 0).

No additional tachyon conditions are needed.

---

## 8. Hierarchy Problem

The large values of |t_i| (10²⁰ to 10³²) required for light
torsion constitute a HIERARCHY PROBLEM:

**Q: Is |t_i| ≫ 1 technically natural?**

The t_i are dimensionless couplings in the PGT Lagrangian. In a
natural EFT, dimensionless couplings are O(1). Having t_i ~ 10²⁸
is analogous to having a gauge coupling g ~ 10¹⁴ — unnaturally
large.

**Possible protections:**

1. **Shift symmetry:** In the limit t_i → ∞ with t_i/t_j fixed,
   the torsion kinetic term dominates over the Einstein-Hilbert
   term. This limit has enhanced symmetry (torsion decouples from
   curvature). Radiative corrections to 1/t_i would be proportional
   to 1/t_i itself → technically natural.

2. **Large-N mechanism:** If the PGT arises from a theory with N
   fermion species, t_i ~ N. For N ~ 10²⁸, this would require
   an astronomically large number of species — unrealistic.

3. **No protection:** The hierarchy is simply a fine-tuning of the
   PGT Lagrangian with no known mechanism to stabilize it.

**Assessment:** Option 1 (shift-symmetry protection) is the most
plausible. In the limit m_T → 0 (t_i → ∞), the torsion becomes
a massless field with an enhanced global symmetry. Radiative
corrections to m_T² go as m_T² × (loops), preserving the hierarchy.
This is the same technical naturalness that protects scalar masses
below the cutoff in the Standard Model.

**Verdict: The hierarchy is technically natural** (in the 't Hooft
sense) because the limit m_T → 0 enhances the symmetry of the
theory. Radiative corrections to m_T² are proportional to m_T²
itself.
