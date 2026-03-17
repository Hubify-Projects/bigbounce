# Phase 2 — Bounce Curvature Profile

**Date:** 2026-03-15

---

## Spin-Torsion Bounce Solution

### Modified Friedmann equation

In Einstein-Cartan cosmology with spin-torsion coupling, the
effective Friedmann equation is:

```
H² = (8πG/3)(ρ - ρ²/ρ_crit)
```

where:
- ρ_crit = 3/(32πκ⁴σ²) ~ M_Pl² / l_Pl² ~ ρ_Pl ~ 10⁹³ g/cm³
- κ² = 8πG
- σ is the spin density parameter

The bounce occurs when ρ = ρ_crit: H = 0, the universe transitions
from contraction to expansion.

### Curvature scalar on FRW

```
R = 6(Ḣ + 2H²)
```

From the modified Friedmann equation:
```
H² = (8πG/3) ρ (1 - ρ/ρ_crit)
```

Time derivative (using ρ̇ = -3H(ρ + p)):
```
2HḢ = (8πG/3)[ρ̇(1 - 2ρ/ρ_crit)]
     = (8πG/3)[-3H(ρ + p)(1 - 2ρ/ρ_crit)]
```

For radiation-dominated bounce (p = ρ/3):
```
Ḣ = -(8πG/2)(ρ + p)(1 - 2ρ/ρ_crit)
   = -4πG × (4ρ/3)(1 - 2ρ/ρ_crit)
```

Therefore:
```
R = 6Ḣ + 12H²
  = 6[-4πG(4ρ/3)(1 - 2ρ/ρ_crit)] + 12(8πG/3)ρ(1 - ρ/ρ_crit)
  = -32πGρ(1 - 2ρ/ρ_crit) + 32πGρ(1 - ρ/ρ_crit)
  = -32πGρ + 64πGρ²/ρ_crit + 32πGρ - 32πGρ²/ρ_crit
  = 32πGρ²/ρ_crit
```

Wait — this is for radiation where the standard R = 0. Let me redo
this more carefully.

### Careful computation

For standard FRW with radiation: R = 6(Ḣ + 2H²). With ρ̇ = -4Hρ
(radiation):

```
2HḢ = (8πG/3)[(-4Hρ)(1 - 2ρ/ρ_crit)]

Ḣ = -(16πG/3)ρ(1 - 2ρ/ρ_crit)
```

And:
```
H² = (8πG/3)ρ(1 - ρ/ρ_crit)
```

So:
```
R = 6Ḣ + 12H²
  = -32πGρ(1 - 2ρ/ρ_crit) + 32πGρ(1 - ρ/ρ_crit)
  = 32πGρ[-1 + 2ρ/ρ_crit + 1 - ρ/ρ_crit]
  = 32πGρ × (ρ/ρ_crit)
  = 32πG ρ²/ρ_crit
```

**Key result:**
```
R_bounce(ρ) = 32πG ρ²/ρ_crit
```

This is POSITIVE and proportional to ρ². It vanishes at low density
(recovering R = 0 for standard radiation) and peaks at the bounce.

### Peak curvature at the bounce

At ρ = ρ_crit:
```
R_peak = 32πG ρ_crit = 32π/l_Pl² ~ 10⁶⁶ cm⁻² ~ 10¹³² eV²
```

In Planck units: R_peak ~ M_Pl².

### For matter-dominated bounce (p = 0)

```
ρ̇ = -3Hρ

Ḣ = -4πG ρ(1 - 2ρ/ρ_crit)

R = 6Ḣ + 12H²
  = -24πGρ(1 - 2ρ/ρ_crit) + 32πGρ(1 - ρ/ρ_crit)
  = 8πGρ[(-3 + 6ρ/ρ_crit + 4 - 4ρ/ρ_crit)]
  = 8πGρ[1 + 2ρ/ρ_crit]
```

At low density: R → 8πGρ (standard matter-era result, since
R = 12H² for matter with Ḣ = -H²/2 gives R = 3H², and 3H² =
8πGρ ✓).

At the bounce (ρ = ρ_crit):
```
R_peak = 8πGρ_crit × 3 = 24πGρ_crit ~ M_Pl²
```

Same order as the radiation case.

---

## Duration of the Bounce

### Characteristic timescale

The bounce occurs over a timescale set by the Planck time:

```
Δt_bounce ~ 1/√(Gρ_crit) ~ t_Pl ~ 5.4 × 10⁻⁴⁴ s
```

More precisely, R is significant (say, R > R_peak/e) when
ρ > ρ_crit/√e, which corresponds to a time window of order t_Pl
around the bounce.

### Scale factor at the bounce

At the bounce, a(t_bounce) = a_min. For a radiation-dominated
contraction/expansion:

```
a(t) ≈ a_min (1 + t²/τ²)^{1/4}
```

where τ ~ t_Pl. The scale factor barely changes during the bounce.

---

## Bounce Contribution to ∫√g R

### The integral

```
I_bounce = ∫_bounce d⁴x √g R
         = V_spatial × ∫ dt a³(t) R(t)
```

where V_spatial is the comoving spatial volume.

### Order-of-magnitude estimate

During the bounce:
- a(t) ≈ a_min (approximately constant over Δt ~ t_Pl)
- R(t) ~ R_peak ~ M_Pl²
- Duration: Δt ~ t_Pl

```
I_bounce ~ V_spatial × a_min³ × M_Pl² × t_Pl
         = V_spatial × a_min³ × M_Pl² × M_Pl⁻¹
         = V_spatial × a_min³ × M_Pl
```

In natural units (ℏ = c = 1):
```
I_bounce ~ V_spatial × a_min³ × M_Pl     [units: length⁴ × mass = length³]
```

Let me work in consistent units. With √g = a³(t) and d⁴x = dt d³x:

```
[∫ d⁴x √g R] = [length⁴] × [length⁻²] = [length²] = [mass⁻²]
```

(using d⁴x in comoving coordinates with V_spatial dimensionless,
and absorbing spatial coordinates into a³).

Actually, let me use physical coordinates more carefully:

```
ds² = -dt² + a²(t)(dx² + dy² + dz²)

√g = a³(t)

∫ d⁴x √g R = (∫ d³x) × ∫ dt a³(t) R(t)
```

For flat spatial sections, ∫d³x is the comoving volume V_c (which
can be infinite for non-compact topology or finite for compact
topology like a 3-torus with comoving size L: V_c = L³).

**Assume compact spatial topology with comoving size L.** Then:

```
I_bounce = L³ × ∫_bounce dt a³(t) R(t)
         ~ L³ × a_min³ × R_peak × t_Pl
         ~ L³ × a_min³ × M_Pl² × t_Pl
```

In natural units (t_Pl = 1/M_Pl):
```
I_bounce ~ L³ × a_min³ × M_Pl
```

---

## Post-Bounce Contributions for Comparison

### Radiation era (t_Pl < t < t_eq ~ 10⁵⁰ t_Pl)

For standard radiation: R_rad = 32πG ρ²/ρ_crit (from the modified
Friedmann equation at ρ ≪ ρ_crit) → R_rad ≈ 0 to leading order.

The standard radiation-era curvature is R = 0 (traceless stress-energy).
The correction from the ρ² term is R ~ 32πGρ²/ρ_crit ~ (ρ/ρ_crit) × ρ/M_Pl².

For ρ ≪ ρ_crit: this is negligible.

**I_radiation ≈ 0.**

### Matter era (t_eq < t < t_Λ)

Standard matter domination: R_matter = 8πGρ_m = 3H².

```
a(t) = a_eq (t/t_eq)^{2/3}
H = 2/(3t)
R = 4/(3t²)
```

```
I_matter = L³ × ∫_{t_eq}^{t_Λ} dt × a³(t) × R(t)
         = L³ × a_eq³ × ∫_{t_eq}^{t_Λ} dt (t/t_eq)² × 4/(3t²)
         = L³ × a_eq³ × (4/3) × ∫_{t_eq}^{t_Λ} dt / t_eq²
         = L³ × a_eq³ × (4/3) × (t_Λ - t_eq) / t_eq²
         ≈ L³ × a_eq³ × (4/3) × t_Λ / t_eq²
```

With t_eq ~ 10⁵⁰ t_Pl, t_Λ ~ 10⁶⁰ t_Pl, a_eq ~ a_min × (t_eq/t_Pl)^{1/2}
(radiation scaling from bounce to equality):

```
a_eq = a_min × (t_eq/t_Pl)^{1/2} ~ a_min × 10²⁵
```

```
I_matter ~ L³ × (a_min × 10²⁵)³ × (4/3) × 10⁶⁰ t_Pl / (10⁵⁰ t_Pl)²
         = L³ × a_min³ × 10⁷⁵ × (4/3) × 10⁶⁰ / (10¹⁰⁰ × t_Pl)
         = L³ × a_min³ × (4/3) × 10³⁵ / t_Pl
         = L³ × a_min³ × (4/3) × 10³⁵ × M_Pl
```

**I_matter ~ L³ × a_min³ × 10³⁵ × M_Pl**

### Dark energy era (t > t_Λ)

De Sitter: R_Λ = 12H_Λ², a(t) = a_Λ e^{H_Λ(t - t_Λ)}.

```
I_Λ = L³ × ∫_{t_Λ}^{∞} dt × a³(t) × 12H_Λ²
    = L³ × a_Λ³ × 12H_Λ² × ∫_{t_Λ}^{∞} dt e^{3H_Λ(t-t_Λ)}
    = L³ × a_Λ³ × 12H_Λ² × 1/(3H_Λ)
    = L³ × a_Λ³ × 4H_Λ
```

This integral DIVERGES if we integrate to t = ∞. For a future
cutoff at time T_future:

```
I_Λ = L³ × a_Λ³ × 4H_Λ × [e^{3H_Λ(T_future - t_Λ)} - 1] / (3H_Λ)
```

For T_future → ∞: I_Λ → ∞.

**The de Sitter era contribution DIVERGES.**

This is the same problem encountered in sequestering: the future
de Sitter expansion produces infinite spacetime volume and infinite
integrated curvature.

---

## Comparison

| Era | I_R contribution | Relative to bounce |
|-----|-----------------|-------------------|
| Bounce | L³ a_min³ M_Pl | **1** |
| Radiation | ~0 | negligible |
| Matter | L³ a_min³ × 10³⁵ M_Pl | **10³⁵** |
| Dark energy | **DIVERGENT** | **∞** |

---

## Critical Finding

**The bounce contribution to ∫√g R is NEGLIGIBLE compared to the
matter era, and INFINITELY smaller than the dark energy era.**

The matter era alone contributes 10³⁵ times more integrated curvature
than the bounce. The dark energy era contributes infinitely more
(if the universe accelerates forever).

The ratio:
```
I_bounce / I_matter ~ M_Pl / (10³⁵ M_Pl) = 10⁻³⁵
```

**The bounce is 35 orders of magnitude subdominant to the matter era
in the curvature integral.**

This is because:
1. The bounce has R ~ M_Pl² but over volume ~ a_min³ × t_Pl (tiny)
2. The matter era has R ~ H² ≪ M_Pl² but over volume ~
   a_eq³ × t_Λ (enormous)
3. The product (R × volume) is dominated by the matter era
4. The dark energy era makes it even worse: R is constant and
   volume grows exponentially

---

## Implication

The global curvature constraint ∫√g R = χ₀ is dominated by the
matter and dark energy eras. The bounce contribution is negligible.

**The constraint cannot link bounce physics to the late-time Λ
because the bounce's contribution to the integral is washed out
by subsequent cosmological evolution.**

This is the same scale separation problem identified in Phase 1
for the sequestering mechanism, now confirmed quantitatively for
the curvature constraint.
