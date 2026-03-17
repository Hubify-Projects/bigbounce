# Torsion Mass Spectrum

**Date:** 2026-03-16

---

## 1. Physical Mass Scales from PGT Parameters

### General structure

All torsion masses in quadratic PGT take the form:

```
m²_J = M_Pl² / f_J(t₁, t₂, t₃)
```

where f_J is a linear combination of the dimensionless torsion
couplings, specific to each spin-parity sector J^P.

| Mode | f_J | Mass formula |
|------|-----|-------------|
| 0⁺ (axial scalar) | t₁ + 2t₂ | m₀⁺² = M_Pl² / (t₁ + 2t₂) |
| 0⁻ (trace pseudoscalar) | 4\|t₃\| (with t₂ = -2t₁) | m₀⁻² = M_Pl² / (4\|t₃\|) |
| 1⁺ (axial vector) | t₁ - t₂ | m₁⁺² = M_Pl² / (t₁ - t₂) |
| 1⁻ (trace vector) | \|2t₁ + t₂\| | m₁⁻² = M_Pl² / \|2t₁ + t₂\| |
| 2⁺ (tensor) | t₁ (× b_i factors) | m₂⁺² ~ M_Pl² / t₁ |

### Light torsion condition

For any mode to have m_J ≪ M_Pl:

```
|f_J| ≫ 1
```

This means the relevant combination of dimensionless PGT
couplings must be large.

---

## 2. Sector I: Spin-0⁺ Mass Spectrum

### Single propagating mode

With the ghost-free choice t₁ = t₂ ≡ t > 0:

```
m₀⁺² = M_Pl² / (3t)
m₀⁺ = M_Pl / √(3t) ≈ 0.577 M_Pl / √t
```

### Mass table

| t | m₀⁺ (GeV) | m₀⁺ (M_Pl) | ρ_crit^{1/4} (GeV) |
|---|-----------|------------|-------------------|
| 1 | 7.0 × 10¹⁸ | 0.58 | 1.3 × 10¹⁹ |
| 10² | 7.0 × 10¹⁷ | 0.058 | 4.1 × 10¹⁸ |
| 10⁶ | 7.0 × 10¹⁵ | 5.8 × 10⁻⁴ | 4.1 × 10¹⁷ |
| 10¹⁰ | 7.0 × 10¹³ | 5.8 × 10⁻⁶ | 4.1 × 10¹⁶ |
| 10¹⁴ | 7.0 × 10¹¹ | 5.8 × 10⁻⁸ | 4.1 × 10¹⁵ |
| 10²⁰ | 7.0 × 10⁸ | 5.8 × 10⁻¹¹ | 4.1 × 10¹³ |
| 10²⁸ | 7.0 × 10⁴ | 5.8 × 10⁻¹⁵ | 4.1 × 10¹¹ |
| 10³² | 7.0 × 10² | 5.8 × 10⁻¹⁷ | 4.1 × 10¹⁰ |

### Target range for LISA/LIGO

```
LIGO/ET band: f_b ~ 1–10³ Hz → ρ_crit^{1/4} ~ 10¹³–10¹⁵ GeV
  → m₀⁺ ~ 10⁸–10¹¹ GeV → t ~ 10¹⁶–10²²

LISA band: f_b ~ 10⁻⁴–10⁻¹ Hz → ρ_crit^{1/4} ~ 10¹⁰–10¹³ GeV
  → m₀⁺ ~ 10¹–10⁸ GeV → t ~ 10²²–10³⁶
```

---

## 3. Sector II: Spin-0⁻ Mass Spectrum

### Single propagating mode

With t₂ = -2t₁ and t₃ < 0:

```
m₀⁻² = M_Pl² / (4|t₃|)
m₀⁻ = M_Pl / (2√|t₃|) ≈ 0.5 M_Pl / √|t₃|
```

### Mass table

| |t₃| | m₀⁻ (GeV) | m₀⁻ (M_Pl) | ρ_crit^{1/4} (GeV) |
|------|-----------|------------|-------------------|
| 1 | 6.1 × 10¹⁸ | 0.50 | 1.2 × 10¹⁹ |
| 10² | 6.1 × 10¹⁷ | 0.050 | 3.8 × 10¹⁸ |
| 10¹⁰ | 6.1 × 10¹³ | 5.0 × 10⁻⁶ | 3.8 × 10¹⁶ |
| 10²⁰ | 6.1 × 10⁸ | 5.0 × 10⁻¹¹ | 3.8 × 10¹³ |
| 10²⁸ | 6.1 × 10⁴ | 5.0 × 10⁻¹⁵ | 3.8 × 10¹¹ |
| 10³² | 6.1 × 10² | 5.0 × 10⁻¹⁷ | 3.8 × 10¹⁰ |

### Comparison with Sector I

For the same target mass, Sectors I and II require similar
hierarchies in their respective parameters (t vs |t₃|). The
physics is qualitatively identical.

---

## 4. Non-Propagating Mode Masses (Decoupled Modes)

In each sector, the non-propagating modes are either:

**Case (a): Infinitely massive** — the mode has zero kinetic term
(A_J = 0). The mass is formally infinite, the mode is a constraint
(non-dynamical). It can be integrated out, yielding a local contact
interaction.

**Case (b): Formally present but ghostly** — the mode has wrong-sign
kinetic term (A_J < 0). If also heavy (|m_J| ≫ m_T), the ghost
mode's vacuum instability timescale is τ ~ 1/m_ghost, which is
short. However, if the ghost is super-heavy (m_ghost ~ M_Pl),
the instability timescale is τ ~ t_Pl, and the ghost is at the
UV cutoff of the theory — arguably harmless.

**Assessment for Sector I:** With t₁ = t₂ = t ≫ 1:

| Mode | A_J | m²_J | Status |
|------|-----|------|--------|
| 0⁺ | 3t | M_Pl²/(3t) ~ m_T² | **PROPAGATING (healthy)** |
| 0⁻ | -(4t₃ + 3t) | M_Pl²/\|4t₃+3t\| | Non-propagating if t₃ ~ -3t/4 |
| 1⁺ | 0 | ∞ (constraint) | **DECOUPLED** (A₁⁺ = t₁ - t₂ = 0) |
| 1⁻ | -3t | M_Pl²/(3t) ~ m_T² | Ghostly but same mass scale! |

**PROBLEM:** The spin-1⁻ (trace vector) mode has A₁⁻ = -(2t₁+t₂)
= -3t < 0 (ghost) and mass m₁⁻² = M_Pl²/(3t) ~ m_T². This
ghost has the SAME mass as the healthy 0⁺ mode.

**This is dangerous.** A ghost at the same mass scale as the healthy
mode means the vacuum is unstable at the torsion mass scale.

### Resolution attempts

1. **Exact t₁ = t₂:** The 1⁺ mode is exactly a constraint (A₁⁺ = 0).
   But the 1⁻ mode still has |A₁⁻| = 3t with ghost sign. The 1⁻
   mode propagates as a ghost with mass ~ m_T.

2. **Make 1⁻ super-heavy:** Need |2t₁ + t₂| ≪ 1 (i.e., t₂ ≈ -2t₁).
   But this contradicts t₁ = t₂ (Sector I requirement).

3. **Accept the ghost:** If the theory is an EFT valid up to some
   cutoff Λ < m_ghost, the ghost is above the cutoff and harmless.
   But m_ghost ~ m_T is the scale we want to be BELOW the cutoff.

**Sector I has a GHOST PROBLEM at the target mass scale.**

---

## 5. Reassessment of Sector II

**Assessment for Sector II:** With t₂ = -2t₁, t₃ < 0, |t₃| ≫ 1:

| Mode | A_J | m²_J | Status |
|------|-----|------|--------|
| 0⁻ | 4\|t₃\| | M_Pl²/(4\|t₃\|) ~ m_T² | **PROPAGATING (healthy)** |
| 0⁺ | t₁ + 2t₂ = -3t₁ | If t₁ > 0: ghost; if t₁ < 0: healthy but then... | Problematic |
| 1⁻ | \|2t₁ + t₂\| = 0 | ∞ (constraint) | **DECOUPLED** (exact) |
| 1⁺ | t₁ - t₂ = 3t₁ | If t₁ > 0: healthy | Mass: M_Pl²/(3t₁) |
| 2⁺ | t₁ | If t₁ > 0: healthy | Mass involves b_i |

The 1⁻ mode is EXACTLY decoupled (t₂ = -2t₁ gives A₁⁻ = 0).

For t₁ > 0: The 0⁺ mode is ghostly (A₀⁺ = -3t₁ < 0). Its mass:
```
m₀⁺² = M_Pl² / (3t₁)
```

If t₁ ~ O(1): m₀⁺ ~ M_Pl (super-heavy ghost, harmless).
If t₁ ≫ 1: m₀⁺ ≪ M_Pl (light ghost, DANGEROUS).

**For Sector II to work with t₁ ~ O(1):**
- The 0⁺ ghost has mass ~ M_Pl (harmless at low energies)
- The 1⁺ and 2⁺ modes also have mass ~ M_Pl (heavy, decouple)
- Only the 0⁻ mode is light (mass ~ m_T = M_Pl / √|t₃|)

**This works!** The key insight: in Sector II, the light mass
comes from |t₃| ≫ 1, while the dangerous modes have masses
controlled by t₁ ~ O(1) (Planck scale). The hierarchy is in
t₃ ONLY, and t₃ does not enter the ghost conditions of the
other modes.

---

## 6. Viable Mass Spectrum: Sector II with t₁ ~ O(1)

### Parameter choice

```
t₁ ~ O(1)     (positive, order unity)
t₂ = -2t₁     (exact or approximate, decouples 1⁻)
t₃ < 0         (ghost-free for 0⁻)
|t₃| ≫ 1       (light 0⁻ mode)
```

### Mass spectrum

| Mode | Mass | Ghost? | Status |
|------|------|--------|--------|
| 0⁻ (trace pseudoscalar) | M_Pl/(2√\|t₃\|) ≪ M_Pl | NO | **LIGHT, HEALTHY** |
| 0⁺ (axial scalar) | M_Pl/√(3t₁) ~ M_Pl | YES (ghost) | Heavy ghost, harmless |
| 1⁻ (trace vector) | ∞ (constraint) | — | Decoupled |
| 1⁺ (axial vector) | M_Pl/√(3t₁) ~ M_Pl | NO | Heavy, decoupled |
| 2⁺ (tensor) | ~ M_Pl | NO (if b_i chosen) | Heavy, decoupled |

### Physical picture

At energies E ≪ M_Pl, the effective theory contains:
- **Gravity** (massless spin-2)
- **One light pseudoscalar** τ (the 0⁻ torsion mode) with mass m_T

All other modes are at the Planck scale and decouple. The low-energy
effective theory is GR + massive pseudoscalar.

---

## 7. Torsion Mass vs Observable Bounce Scale

Using Sector II:

```
m_T = m₀⁻ = M_Pl / (2√|t₃|)
ρ_crit ~ m_T² M_Pl² = M_Pl⁴ / (4|t₃|)
ρ_crit^{1/4} = M_Pl / (4|t₃|)^{1/4} ≈ 0.71 M_Pl / |t₃|^{1/4}
```

| |t₃| | m_T (GeV) | ρ_crit^{1/4} (GeV) | f_b (Hz) | Band |
|------|----------|-------------------|---------|------|
| 10⁴ | 6.1 × 10¹⁶ | 1.2 × 10¹⁸ | ~10⁴ | Above LIGO |
| 10⁸ | 6.1 × 10¹⁴ | 1.2 × 10¹⁷ | ~10² | LIGO/ET |
| 10¹² | 6.1 × 10¹² | 1.2 × 10¹⁶ | ~1 | LIGO/ET |
| 10¹⁶ | 6.1 × 10¹⁰ | 1.2 × 10¹⁵ | ~10⁻¹ | LIGO/ET edge |
| 10²⁰ | 6.1 × 10⁸ | 1.2 × 10¹⁴ | ~10⁻² | LISA upper |
| 10²⁴ | 6.1 × 10⁶ | 1.2 × 10¹³ | ~10⁻³ | LISA |
| 10²⁸ | 6.1 × 10⁴ | 1.2 × 10¹² | ~10⁻⁴ | LISA |
| 10³² | 6.1 × 10² | 1.2 × 10¹¹ | ~10⁻⁵ | Sub-LISA |

### Target ranges

```
LIGO/ET (1–10⁴ Hz):     |t₃| ~ 10⁸ to 10¹⁶
LISA (10⁻⁴ to 10⁻¹ Hz): |t₃| ~ 10¹⁶ to 10²⁸
```

---

## 8. Summary

| Finding | Detail |
|---------|--------|
| Ghost-free light torsion possible? | **YES, in Sector II** |
| Viable sector | 0⁻ pseudoscalar, t₂ = -2t₁, t₃ < 0 |
| Light mode | Trace pseudoscalar, mass m_T = M_Pl/(2√\|t₃\|) |
| Hierarchy required | \|t₃\| ≫ 1 (10⁸ to 10²⁸ for GW bands) |
| Technical naturalness | YES (m_T → 0 enhances symmetry) |
| Other modes | All at ~ M_Pl (decouple, harmless) |
| Sector I status | **PROBLEMATIC** (ghost at target mass scale) |
| Sector II status | **VIABLE** |
