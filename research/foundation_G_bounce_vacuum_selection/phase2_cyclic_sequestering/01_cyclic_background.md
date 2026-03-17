# Phase 2 — Cyclic Background Model

**Date:** 2026-03-15

---

## Minimal Cyclic FRW Model

### Setup

A cyclic cosmology requires:
1. A BOUNCE at a = a_min (contraction → expansion)
2. A TURNAROUND at a = a_max (expansion → contraction)
3. Matter/radiation content that drives the dynamics
4. A cosmological constant Λ that governs the late-time behavior

The spin-torsion bounce provides the bounce. The turnaround requires
Λ to eventually become subdominant to a component with w < -1/3
that causes recollapse — OR Λ itself must be negative at some point.

### The Problem With Λ > 0 Cyclic Cosmology

With Λ > 0 (as observed), a spatially flat FRW universe expands
forever. There is NO turnaround. The scale factor grows as
a(t) ~ e^{Ht} at late times, approaching de Sitter space.

For a cyclic cosmology with Λ > 0, one needs EITHER:
1. Spatial curvature k > 0 (closed universe) with Λ small enough
   that the universe recollapses before de Sitter domination
2. An additional component (phantom energy, w < -1) that triggers
   recollapse
3. A time-dependent effective Λ that eventually becomes negative

**Option 1 is the simplest.** Use a closed FRW universe (k = +1)
with Λ > 0 and matter/radiation. If the matter density is high
enough relative to Λ, the universe recollapses.

### Modified Friedmann Equation (Spin-Torsion + Curvature + Λ)

```
H² = (8πG/3)(ρ - ρ²/ρ_crit) - k/a² + Λ/3
```

where:
- ρ = ρ_r/a⁴ + ρ_m/a³ (radiation + matter, with ρ_r, ρ_m the
  present-day densities scaled to a = 1)
- ρ_crit ~ M_Pl⁴ (spin-torsion critical density)
- k = +1 for closed spatial sections
- Λ is the cosmological constant

### Bounce Condition (H = 0, ρ → ρ_crit)

At the bounce: ρ = ρ_crit, a = a_min. The Friedmann equation gives:

```
0 = (8πG/3)(ρ_crit - ρ_crit²/ρ_crit) - k/a_min² + Λ/3
0 = 0 - k/a_min² + Λ/3
```

Therefore:
```
k/a_min² = Λ/3
a_min² = 3k/Λ
a_min = √(3/Λ)     [for k = 1]
```

**Key result:** The bounce scale factor is determined by Λ:
```
a_min = √(3/Λ)
```

For Λ ~ 10⁻¹²² M_Pl⁴ ~ 10⁻⁵² m⁻²:
```
a_min ~ √(3/10⁻⁵²) ~ 10²⁶ m ~ 10 Gpc
```

This is approximately the CURRENT Hubble radius. This means:
**the bounce scale factor in a closed cyclic cosmology with
Λ ~ Λ_obs is comparable to the current size of the universe.**

This is NOT a Planck-scale bounce. The spin-torsion bounce
occurs at Planck density, which for a closed universe at
a = a_min ~ 10²⁶ m requires:

```
ρ_crit = ρ_r/a_min⁴ + ρ_m/a_min³
```

For ρ_crit ~ M_Pl⁴ ~ 10⁷⁶ GeV⁴ and a_min ~ 10²⁶ m ~ 10⁵⁹ l_Pl:

```
ρ_m/a_min³ ~ M_Pl⁴ → ρ_m ~ M_Pl⁴ × a_min³ ~ M_Pl⁴ × 10¹⁷⁷ l_Pl³
```

This requires an ENORMOUS matter density parameter. In a closed
universe of radius a_min ~ 10²⁶ m, the total mass would be:

```
M ~ ρ_crit × a_min³ ~ 10⁷⁶ GeV⁴ × (10⁵⁹)³ ~ 10²⁵³ GeV
```

This is absurd — it is 10²⁰⁰ times the mass of the observable
universe.

### The Incompatibility

**A spin-torsion bounce with Λ ~ Λ_obs in a closed universe is
incompatible with observed matter content.**

The issue: the spin-torsion bounce occurs at ρ = ρ_crit ~ M_Pl⁴.
In a closed universe, this requires a_min such that k/a_min² = Λ/3.
For small Λ, a_min is huge. But huge a_min with ρ ~ M_Pl⁴ requires
enormous total matter content — far exceeding what is observed.

### Alternative: Planck-Scale Bounce With k = +1

If instead we allow a_min ~ l_Pl (Planck-scale bounce), then:

```
k/a_min² ~ M_Pl²
Λ/3 = k/a_min² ~ M_Pl²
Λ ~ M_Pl²
```

This gives Λ ~ M_Pl² — the Planck scale, not the DE scale. This
is the SEVENTH BARRIER (Planck-scale matching) from Foundation G
Phase 1.

### Resolution Attempt: Two Separate Scales

Perhaps the bounce occurs at a_min ~ l_Pl with a DIFFERENT mechanism
for satisfying H = 0 than the Λ/k balance. In pure spin-torsion
cosmology (flat k = 0):

```
H² = (8πG/3)(ρ - ρ²/ρ_crit) + Λ/3
```

At H = 0 with k = 0:
```
0 = (8πG/3)(ρ_b - ρ_b²/ρ_crit) + Λ/3
```

For ρ_b = ρ_crit:
```
0 = 0 + Λ/3 → Λ = 0
```

**For flat spatial sections: the bounce requires Λ = 0.**

For Λ > 0: the bounce density shifts:
```
ρ_b² - ρ_crit ρ_b + ρ_crit Λ/(8πG) = 0
ρ_b = (ρ_crit/2)[1 ± √(1 - 4Λ/(8πG ρ_crit))]
    ≈ ρ_crit [1 - Λ/(8πG ρ_crit)]     [for small Λ]
```

The correction to ρ_b from Λ is:
```
δρ_b/ρ_crit ~ Λ/(8πG ρ_crit) ~ Λ M_Pl²/ρ_crit ~ Λ/M_Pl² ~ 10⁻¹²²
```

Negligible. The bounce occurs at essentially ρ = ρ_crit regardless
of Λ. The bounce is completely INSENSITIVE to Λ.

### Turnaround for k = 0

With k = 0 and Λ > 0: there is NO turnaround. The universe expands
forever. **Cyclic cosmology is impossible with k = 0 and Λ > 0.**

### Summary of Background Model

| Configuration | Bounce? | Turnaround? | Cyclic? | Compatible with Λ_obs? |
|--------------|---------|-------------|---------|----------------------|
| k = 0, Λ > 0 | YES (ρ_b ≈ ρ_crit) | NO | NO | — |
| k = 0, Λ = 0 | YES (ρ_b = ρ_crit) | NO (matter era decelerates but doesn't recollapse) | NO | NO (Λ=0 ≠ obs) |
| k = +1, Λ > 0 small | YES (a_min ~ √(3/Λ) ~ huge) | YES (if Λ small enough) | YES | NO (matter content absurd) |
| k = +1, Λ ~ M_Pl² | YES (a_min ~ l_Pl) | Possibly | Possibly | NO (Λ too large) |

**No configuration produces a viable cyclic cosmology with both
spin-torsion bounce AND Λ ~ Λ_obs.**

This is a FUNDAMENTAL obstacle for cyclic sequestering: the cyclic
model that sequestering requires is incompatible with the observed
cosmological constant.
