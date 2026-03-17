# Foundation C — FRW Background Relevance Test

**Date:** 2026-03-14

---

## Purpose

Evaluate each candidate action on a flat FRW background to determine
whether the environmental mass mechanism is cosmologically relevant
or only relevant in local/dense-matter environments.

This is the most discriminating test. A mechanism that only works
near stars or in compact objects is NOT a dark energy solution.

---

## FRW Background Values

### Metric

```
ds² = -dt² + a²(t)(dx² + dy² + dz²)
```

### Ricci scalar

```
R = 6(Ḣ + 2H²) = 8πGρ(1 - 3w)
```

| Epoch | w | R | m²_eff = ξR (ξ=1/6) |
|-------|---|---|---------------------|
| Radiation | 1/3 | 0 | 0 |
| Matter | 0 | 3H² | H²/2 |
| de Sitter | -1 | 12H² | 2H² |
| Today (Ω_m≈0.3, Ω_Λ≈0.7) | ~-0.7 | ~9H₀² | ~1.5H₀² |

### Torsion

In standard Einstein-Cartan / PGT cosmology, torsion is sourced by
spin density:

```
T^λ_μν ~ (1/M_Pl²) × (spin density)
```

On cosmological (FRW) backgrounds: spin density is zero (no
macroscopic spin alignment). Therefore:

```
T₀ = 0    on FRW
```

**Any mass term depending on torsion VANISHES on FRW.**

### Non-metricity

In standard MAG cosmology (quadratic action), non-metricity is
algebraic and sourced by hypermomentum:

```
Q_μαβ ~ (1/a_2) × (hypermomentum density)
```

For standard matter (scalar fields, perfect fluids): hypermomentum
is zero. Therefore:

```
Q₀ = 0    on FRW (for standard matter)
```

**Exception:** In Weyl geometry, the Weyl vector Q_μ can acquire a
cosmological background value if the action sources it. This depends
on the specific theory.

**Any mass term depending on Q VANISHES on FRW for standard matter.**

### Curvature invariants

Higher curvature invariants on FRW:

```
R_μν R^μν = 3(Ḣ + 2H²)² + 3(Ḣ + H²)² = R²/4 + 3(Ḣ + H²)²
R_μνρσ R^μνρσ = 12(Ḣ + H²)² + 12H⁴
Gauss-Bonnet: G = R² - 4R_μνR^μν + R_μνρσR^μνρσ
```

All are non-zero on FRW (except during radiation for R-dependent ones).

---

## Candidate-by-Candidate FRW Analysis

### Candidate A: Conformally Coupled Scalar

**Environmental mass on FRW:**
```
m²_eff = R/6 = (Ḣ + 2H²)
```

| Epoch | m²_eff | m_eff/H |
|-------|--------|---------|
| Radiation | 0 | 0 |
| Matter | H²/2 | 1/√2 |
| de Sitter | 2H² | √2 |
| Today | ~1.5H₀² | ~1.2 |

**FRW Verdict: SURVIVES.**

m_eff ~ H throughout the matter and dark energy eras. The field is
dynamically relevant on cosmological backgrounds.

During radiation: m = 0. The field is massless. This means:
- No contribution to dark energy during radiation era (good — dark
  energy should be negligible then).
- Field fluctuations are generated during inflation (like any light
  scalar).
- The field "turns on" at matter-radiation equality.

**Dynamics:** The equation of motion on FRW:
```
φ̈ + 3Hφ̇ + (R/6)φ = source terms
```

With R/6 ~ H²: the mass term is comparable to the Hubble friction
term 3Hφ̇. The field evolves on the Hubble timescale. This is the
quintessence regime — slow-roll evolution of a light scalar.

The effective equation of state depends on the balance between
kinetic and potential energy:
- If φ̇² >> (R/6)φ²: kinetic-dominated, w_φ ≈ 1 (stiff)
- If φ̇² << (R/6)φ²: potential-dominated, w_φ ≈ -1 (vacuum-like)
- In practice: w_φ is between -1 and 0, tracking the background

This is standard quintessence phenomenology. No geometric signature.

---

### Candidate B: PGT 0⁺ + ξR

**Environmental mass on FRW:**
```
m²_eff = M_Pl²/(16π|t₂|) + ξR ≈ M_Pl²/(16π|t₂|)
```

The ξR term is O(H²) ~ 10⁻⁶⁶ M_Pl². The bare PGT mass is
O(M_Pl²/|t₂|). For |t₂| ~ O(1): the ratio is 10⁻⁶⁶.

**FRW Verdict: FAILS.**

The environmental correction is 10⁶⁰ times smaller than the bare
mass. The field is super-heavy (m ~ M_Pl) on ALL backgrounds.
It has no cosmological relevance.

---

### Candidate C: Geometric Symmetron

**Environmental mass on FRW:**

In the symmetric phase (R > μ²/ξ):
```
m²_eff = ξR - μ²
φ₀ = 0
```

In the broken phase (R < μ²/ξ):
```
m²_eff = 2(μ² - ξR)
φ₀ = ±√((μ² - ξR)/λ)
```

For the symmetron transition to occur at the current epoch:
R_crit = μ²/ξ ~ H₀². With ξ ~ O(1): μ ~ H₀.

**FRW Verdict: SURVIVES but requires μ ~ H₀.**

The mechanism works on FRW, but μ ~ H₀ ~ 10⁻³³ eV is a free
parameter with no symmetry protection. This is a fine-tuning.

**Cosmological history:**
- During radiation (R = 0 < R_crit): broken phase, φ ≠ 0.
  Wait — this is backwards. For R_crit > 0: radiation era has R = 0 <
  R_crit, so we're in the broken phase. The field is active during
  radiation era — potentially problematic for BBN.

Actually, the standard symmetron has the opposite sign: the field
decouples at HIGH density (R >> R_crit) and activates at LOW density.
Let me reconsider the sign.

With potential V = -½μ²φ² + ¼λφ⁴ + ½ξRφ²:
- High R: effective mass² = ξR - μ² > 0. Field at φ = 0. Decoupled.
- Low R: effective mass² = ξR - μ² < 0. Field at φ ≠ 0. Active.

In radiation (R = 0): effective mass² = -μ². TACHYONIC. The field
rolls to φ = ±μ/√λ immediately.

In matter/de Sitter: R > 0. If R > μ²/ξ: field at origin, decoupled.

So the symmetron transition happens when R DROPS below μ²/ξ as the
universe expands. For this to happen in the recent past:
μ²/ξ ~ R_today ~ several H₀². With ξ ~ O(1): μ ~ H₀.

This IS the correct phenomenology: the field activates at late times
when the curvature drops below the threshold.

But the tachyonic phase during radiation (R = 0 → m² = -μ²) means
the field is at its VEV throughout the radiation era. It only becomes
cosmologically interesting when R becomes comparable to μ²/ξ, which
is at late times.

**FRW dynamics are viable but require tuned μ.**

---

### Candidate D: Weyl Scalar

**Environmental mass on FRW:**

After Stückelberg decomposition, the scalar σ has:
```
m²_eff = c × R    [with c determined by the Weyl action parameters]
```

For the simplest Weyl action: c ~ O(1). So m²_eff ~ R ~ H².

**FRW Verdict: SURVIVES.**

Identical to Candidate A in the FRW analysis. The gauge protection
of m₀ = 0 is the only difference — the FRW dynamics are the same.

---

### Candidate E: Curvature-Dependent Kinetic Mixing

**FRW analysis:**

The kinetic normalization Z_eff(R) changes on FRW, but m and g scale
with the SAME power of Z. The ratio m/g is unchanged.

**FRW Verdict: IRRELEVANT (lock not broken).**

---

## Summary

| Candidate | FRW survival | m_eff on FRW | Cosmologically relevant? |
|-----------|-------------|-------------|------------------------|
| A: Conformal | **YES** | ~H | Yes (quintessence-like) |
| B: PGT+ξR | **NO** | ~M_Pl | No (bare mass dominates) |
| C: Symmetron | **YES*** | ~H (tuned) | Yes, but μ~H₀ is tuned |
| D: Weyl | **YES** | ~H | Yes (= Candidate A) |
| E: Kinetic | **NO** | locked | No (lock preserved) |

\* Requires μ ~ H₀ with no symmetry protection.

---

## Critical Assessment

The FRW test eliminates two candidates (B and E) and reveals that
the surviving candidates (A, C, D) all produce the SAME cosmological
dynamics: a scalar with mass ~H evolving on the Hubble timescale.

This is quintessence. The specific geometric origin (conformal
symmetry, Weyl gauge symmetry, symmetron mechanism) affects the
theoretical motivation but NOT the FRW phenomenology.

**No candidate produces FRW dynamics that differ from standard
scalar-tensor cosmology.**

The terms that could provide geometric distinctiveness — torsion-
dependent masses, non-metricity corrections, torsion-curvature
cross-terms — all VANISH on FRW because T₀ = 0 and Q₀ = 0 in
standard FRW cosmology.

**This is a fundamental limitation:** FRW cosmology has no torsion
and no non-metricity (for standard matter). Any geometric effect
that relies on these quantities is cosmologically irrelevant.

The only geometric quantity that survives on FRW is the metric
curvature R(g). But R(g) is the same in GR, PGT, MAG, and any
other metric theory. So R-dependent masses are not uniquely
geometric — they exist in ANY theory of gravity.
