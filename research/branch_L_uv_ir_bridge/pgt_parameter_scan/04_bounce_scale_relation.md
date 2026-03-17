# Bounce Scale Relation in PGT

**Date:** 2026-03-16

---

## 1. From EC to PGT: How ρ_crit Changes

### Einstein-Cartan (minimal model)

In EC gravity, torsion is non-propagating. The Cartan equation
is algebraic:

```
T^a_{μν} = (8πG / 4) ε^a_{μνρ} J^{5ρ}
```

Substituting back into the Friedmann equation:

```
H² = (8πG/3)(ρ - ρ²/ρ_crit)
```

with:
```
ρ_crit = 3/(8πGκ²) = (3/8π)(M_Pl²/κ²)
```

where κ is the spin-torsion coupling constant. For N_f fermion
species with standard Dirac coupling:

```
κ² = (8πG)² × (n_f / a³)² / ρ² → ρ_crit ≈ 0.21 M_Pl⁴
```

The critical density is fixed at the Planck scale. No free
parameter to lower it.

### PGT with propagating torsion (Sector II)

In PGT, the torsion equation of motion is DYNAMICAL:

```
□T^a_{μν} + m_T² T^a_{μν} = (8πG) × source
```

(schematic; the exact form involves index contractions and PGT
parameter combinations).

The torsion amplitude at the bounce is no longer set by the
algebraic Cartan equation but by the balance of kinetic energy,
mass term, and source:

```
T_bounce ~ source / m_T² ~ (ρ_f / M_Pl²) / m_T²
```

where ρ_f is the fermion energy density.

### Modified Friedmann equation

The effective Friedmann equation in PGT:

```
H² = (8πG/3)(ρ_rad + ρ_torsion) × [1 - (ρ_rad + ρ_torsion)/ρ_crit^{eff}]
```

The torsion energy density:
```
ρ_torsion = (1/2)m_T² τ² + (1/2)τ̇²
```

where τ is the torsion scalar mode (0⁻ in Sector II).

At the bounce, the fermion source drives the torsion to:
```
τ_bounce ~ n₅ / m_T²    (n₅ = axial fermion number density)
```

The critical density where H = 0:
```
ρ_crit^{eff} = ρ_rad + ρ_torsion|_{max}
```

### Parametric estimate

For the spin-0⁻ mode in Sector II:

```
ρ_crit^{eff} ~ m_T² M_Pl²
```

**Derivation sketch:**

The bounce occurs when the total effective energy density satisfies
the modified Friedmann equation H² = 0. The torsion contribution
to the effective energy density scales as:

```
ρ_torsion ~ m_T² τ² ~ m_T² × (M_Pl² / m_T²)² × ρ_f² / M_Pl⁴
          = ρ_f² / (m_T² × M_Pl²/M_Pl⁴)
          = ρ_f² M_Pl² / m_T²    ... [need careful tracking]
```

More carefully: In the EC limit (m_T → M_Pl), torsion is
integrated out algebraically and ρ_crit → M_Pl⁴. In PGT with
finite m_T, the torsion responds dynamically, and the effective
repulsive spin-spin interaction has strength ~ 1/m_T² instead of
~ 1/M_Pl². The critical density where the repulsion balances
attraction:

```
ρ_crit^{eff} ~ M_Pl² × m_T²
```

This can also be seen dimensionally: ρ_crit must have dimensions
[mass]⁴, and the only mass scales are M_Pl and m_T.

---

## 2. Detailed Bounce Scale Mapping

### Bounce frequency today

Using the standard redshift relation:

```
f_b = (k_b / 2π) × (a_b / a_0)
```

where a_b/a_0 ~ T₀/T_b and T_b ~ ρ_crit^{1/4}:

```
f_b ~ T₀ × (ρ_crit^{eff})^{1/4} / M_Pl
    = T₀ × (m_T M_Pl)^{1/2} / M_Pl
    = T₀ × (m_T / M_Pl)^{1/2}
```

with T₀ = 2.35 × 10⁻⁴ eV = 2.35 × 10⁻¹³ GeV.

Converting to Hz: T₀ / (2π ħ) ≈ 5.7 × 10¹⁰ Hz (as a frequency).

```
f_b ≈ 5.7 × 10¹⁰ Hz × (m_T / M_Pl)^{1/2}
    = 5.7 × 10¹⁰ Hz × (m_T / 1.22 × 10¹⁹ GeV)^{1/2}
```

### Complete mapping table

| m_T (GeV) | m_T/M_Pl | ρ_crit^{eff} (GeV⁴) | ρ_crit^{1/4} (GeV) | f_b (Hz) | Band |
|-----------|---------|--------------------|--------------------|---------|------|
| 10¹⁸ | 0.082 | 1.5 × 10⁷⁴ | 6.2 × 10¹⁸ | 1.6 × 10¹⁰ | None (too high) |
| 10¹⁵ | 8.2 × 10⁻⁵ | 1.5 × 10⁶⁸ | 6.2 × 10¹⁷ | 5.2 × 10⁸ | None |
| 10¹² | 8.2 × 10⁻⁸ | 1.5 × 10⁶² | 6.2 × 10¹⁵ | 1.6 × 10⁷ | None |
| 10⁹ | 8.2 × 10⁻¹¹ | 1.5 × 10⁵⁶ | 6.2 × 10¹³ | 5.2 × 10⁵ | None (high f) |
| 10⁷ | 8.2 × 10⁻¹³ | 1.5 × 10⁵² | 6.2 × 10¹² | 5.2 × 10⁴ | LIGO upper edge |
| 10⁵ | 8.2 × 10⁻¹⁵ | 1.5 × 10⁴⁸ | 6.2 × 10¹¹ | 5.2 × 10³ | LIGO |
| 10³ | 8.2 × 10⁻¹⁷ | 1.5 × 10⁴⁴ | 6.2 × 10¹⁰ | 5.2 × 10² | LIGO |
| 10¹ | 8.2 × 10⁻¹⁹ | 1.5 × 10⁴⁰ | 6.2 × 10⁹ | 52 | LIGO |
| 10⁻¹ | 8.2 × 10⁻²¹ | 1.5 × 10³⁶ | 6.2 × 10⁸ | 5.2 | LIGO/ET |
| 10⁻³ | 8.2 × 10⁻²³ | 1.5 × 10³² | 6.2 × 10⁷ | 0.52 | LIGO/ET |
| 10⁻⁵ | 8.2 × 10⁻²⁵ | 1.5 × 10²⁸ | 6.2 × 10⁶ | 0.052 | LISA/Decihertz |
| 10⁻⁷ | 8.2 × 10⁻²⁷ | 1.5 × 10²⁴ | 6.2 × 10⁵ | 5.2 × 10⁻³ | LISA |
| 10⁻⁹ | 8.2 × 10⁻²⁹ | 1.5 × 10²⁰ | 6.2 × 10⁴ | 5.2 × 10⁻⁴ | LISA |
| 10⁻¹¹ | 8.2 × 10⁻³¹ | 1.5 × 10¹⁶ | 6.2 × 10³ | 5.2 × 10⁻⁵ | Sub-LISA |
| 10⁻¹⁵ | 8.2 × 10⁻³⁵ | 1.5 × 10⁸ | 6.2 × 10¹ | 5.2 × 10⁻⁷ | PTA |
| 10⁻¹⁹ | 8.2 × 10⁻³⁹ | 1.5 × 10⁰ | 6.2 × 10⁻¹ | 5.2 × 10⁻⁹ | PTA |

### Band summary

```
LIGO/ET (1–10⁴ Hz):        m_T ~ 10⁻³ to 10⁷ GeV
LISA (10⁻⁴ to 10⁻¹ Hz):    m_T ~ 10⁻⁹ to 10⁻⁵ GeV
Decihertz (0.01–1 Hz):     m_T ~ 10⁻⁵ to 10⁻³ GeV
PTA (10⁻⁹ to 10⁻⁷ Hz):     m_T ~ 10⁻¹⁹ to 10⁻¹⁵ GeV
```

---

## 3. Cross-Check: EC Limit

In the EC limit, m_T → M_Pl (t₃ → O(1)):

```
ρ_crit^{eff} → M_Pl⁴    ✓
f_b → T₀ ~ 5.7 × 10¹⁰ Hz ~ 40 GHz    ✓ (matches minimal model)
```

The PGT result smoothly reduces to the EC result as m_T → M_Pl.

---

## 4. Bounce Duration and Profile

### Bounce timescale

In the minimal EC model:
```
t_bounce ~ 1/√(ρ_crit/M_Pl²) ~ t_Pl
```

In PGT with lower ρ_crit:
```
t_bounce ~ 1/√(ρ_crit^{eff}/M_Pl²) = 1/(m_T)   (in natural units)
```

For m_T = 10⁻⁵ GeV (LISA band):
```
t_bounce ~ 1/m_T ~ 10⁵ GeV⁻¹ ~ 6.6 × 10⁻²⁰ s
```

Compare with EC: t_bounce ~ t_Pl ~ 5.4 × 10⁻⁴⁴ s.

**The PGT bounce is 10²⁴ times LONGER than the EC bounce.**
This is a direct consequence of the lower bounce scale.

### Bounce profile

The scale factor near the PGT bounce (by analogy with EC):

```
a(t) = a_b [1 + (t/t_bounce)²]^{1/4}
```

where t_bounce ~ 1/m_T. The bounce is still symmetric and smooth,
but occurs over a much longer duration.

### Number of e-folds during bounce

The bounce contributes:
```
ΔN_bounce ~ ln(a(t_bounce)/a_b) ~ ln(2^{1/4}) ≈ 0.17
```

Same as EC — the bounce is still a brief event (< 1 e-fold),
just at a lower energy scale.

---

## 5. Observable Mode Interaction with Bounce

### Which modes "see" the bounce?

A cosmological perturbation mode with comoving wavenumber k
interacts with the bounce if k ~ k_b = a_b / t_bounce.

In the PGT bounce:
```
k_b ~ a_b × m_T
```

Modes with k ≫ k_b oscillate freely through the bounce (adiabatic).
Modes with k ≪ k_b are frozen (super-horizon). Modes with k ~ k_b
interact maximally with the bounce potential.

### Comparison with observable modes

For CMB modes: k_CMB ~ 10⁻²⁵ GeV (comoving).

```
k_CMB / k_b ~ 10⁻²⁵ / (a_b × m_T)
```

The ratio a_b depends on the thermal history. If the bounce
occurs at temperature T_b ~ ρ_crit^{1/4}:

```
a_b / a_0 ~ T₀ / T_b ~ 10⁻¹³ GeV / (m_T M_Pl)^{1/2}
k_b,physical = k_b / a_0 = (a_b/a_0) × m_T
             = T₀ × m_T / (m_T M_Pl)^{1/2}
             = T₀ × (m_T / M_Pl)^{1/2}
```

This is the bounce feature frequency f_b derived above.

For LISA-band features (m_T ~ 10⁻⁷ GeV):
```
f_b ~ 5 × 10⁻³ Hz
k_b ~ 2π f_b / c ~ 10⁻¹¹ m⁻¹
k_CMB ~ 10⁻² Mpc⁻¹ ~ 3 × 10⁻²⁵ m⁻¹
```

**k_CMB / k_b ~ 3 × 10⁻¹⁴.** The CMB modes are still far below
the bounce scale, even in PGT. The bounce features are NOT at CMB
scales.

However, the bounce features ARE at GW detector scales, which is
the entire point of the PGT extension.

---

## 6. What the PGT Bounce Achieves

| Property | EC (minimal) | PGT (Sector II) |
|----------|-------------|-----------------|
| ρ_crit | 0.21 M_Pl⁴ | m_T² M_Pl² |
| f_b | ~40 GHz | Tunable (PTA to LIGO) |
| t_bounce | t_Pl | 1/m_T |
| Bounce features at CMB? | NO | NO |
| Bounce features at GW detectors? | NO | **POTENTIALLY YES** |
| Free parameter | None | m_T (via |t₃|) |
| Ghost-free? | Automatic | YES (Sector II) |

### The key shift

The PGT extension does NOT make the bounce visible to the CMB.
It makes the bounce visible to GRAVITATIONAL WAVE DETECTORS.

This is a qualitatively different observable channel — direct
detection of bounce-era tensor modes, rather than indirect
imprints on the scalar spectrum.

---

## 7. Validity Conditions

### EFT validity

The PGT is treated as a classical field theory. For the effective
description to be valid, the energy scale of interest must be below
the UV cutoff:

```
E_bounce ~ ρ_crit^{1/4} ~ (m_T M_Pl)^{1/2}
```

If the PGT is the full theory (not an EFT truncation), there is
no cutoff concern. If the PGT is an EFT of some UV completion,
the cutoff must satisfy Λ_UV > (m_T M_Pl)^{1/2}.

For m_T = 10⁻⁵ GeV: E_bounce ~ 10⁷ GeV. Need Λ_UV > 10⁷ GeV.
This is very mild — well below the GUT scale.

### Semiclassical approximation

The bounce must be describable semiclassically (quantum gravity
corrections small). This requires:

```
ρ_crit^{eff} ≪ M_Pl⁴
```

For m_T ≪ M_Pl: ρ_crit ~ m_T² M_Pl² ≪ M_Pl⁴. **Automatically
satisfied.** The PGT bounce is FURTHER from the quantum gravity
regime than the EC bounce.

This is a significant advantage: the PGT bounce is more
calculable because it occurs at lower energy.
