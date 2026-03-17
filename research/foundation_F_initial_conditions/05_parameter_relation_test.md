# Foundation F — Parameter Relation Test

**Date:** 2026-03-15

---

## Question

Do bounce parameters (ρ_bounce, torsion scale, spin density)
determine any dark-energy parameters (ρ_DE, w, onset epoch)?

---

## Test 1: Does ρ_bounce Determine ρ_DE?

### Bounce energy scale
```
ρ_bounce ~ M_Pl⁴ ~ 10⁷⁶ GeV⁴
```

### DE energy scale
```
ρ_DE ~ (10⁻³ eV)⁴ ~ 10⁻⁴⁷ GeV⁴
```

### Ratio
```
ρ_DE / ρ_bounce ~ 10⁻¹²³
```

For ρ_bounce to determine ρ_DE, there must be a mechanism that
produces this 123-order-of-magnitude suppression from first principles.

### Possible mechanisms

**Exponential suppression:**
```
ρ_DE ~ ρ_bounce × e^{-S}
```

For S ~ 283 (a specific instanton action): this works numerically.
But S must be tuned to 3 significant figures (S = 283.1 ± 0.5).
This is fine-tuning of S, not a prediction.

**Power-law suppression:**
```
ρ_DE ~ ρ_bounce × (H₀/M_Pl)^n
```

For n = 2: ρ_DE ~ M_Pl⁴ × 10⁻¹²² ~ 10⁻⁴⁶ GeV⁴ (close!). This
gives ρ_DE ~ M_Pl² H₀², which is the "geometric mean" of Planck
and Hubble scales. But H₀ is NOT a bounce parameter — it is
determined by the full cosmological evolution.

**Conclusion: NO direct ρ_bounce → ρ_DE relation exists.** The
scales are separated by 10¹²³, and no mechanism bridges this gap
without introducing additional tuned parameters.

---

## Test 2: Does the Torsion Scale Determine the Scalar Mass?

### Torsion at the bounce
```
T_bounce ~ M_Pl     [torsion trace, from spin-torsion]
```

### Required scalar mass for DE
```
m_φ ~ H₀ ~ 10⁻³³ eV ~ 10⁻⁶⁰ M_Pl
```

### Could torsion set m_φ?

In PGT, the torsion mode mass is m ~ M_Pl/√|t₃| (Foundation A).
For m ~ H₀: t₃ ~ (M_Pl/H₀)² ~ 10¹²⁰. This is the mass-coupling
lock — Foundation A already showed this fails.

For a SEPARATE scalar (not the torsion mode): its mass is set by
its OWN potential parameters, not by torsion. Torsion could couple
to the scalar and modify its effective mass at the bounce, but:

```
m²_eff(bounce) = m₀² + (coupling) × T² ~ m₀² + (coupling) × M_Pl²
```

This INCREASES the mass at the bounce (stabilization), not decreases
it. After the bounce (T → 0): m_eff → m₀. The bare mass m₀ must
still be tuned to ~ H₀.

**The torsion scale does NOT determine the scalar mass.**

---

## Test 3: Does Spin Density Set the Scalar Displacement?

### Spin density at the bounce
```
s_bounce ~ M_Pl³
```

### Required displacement for DE

For V(φ) = ½m²φ² with m ~ H₀:
```
ρ_DE = ½m²φ² → φ_DE = √(2ρ_DE)/m ~ 10⁻³ eV / 10⁻³³ eV ~ 10³⁰ eV ~ 10³ GeV
```

For a pNGB with f ~ M_Pl: θ_i ~ O(f) ~ M_Pl.

### Spin-induced displacement

From Task 3 analysis:
```
δφ ~ (g_s/M_Pl²) s² × Δt² ~ g_s M_Pl⁴ / M_Pl² = g_s M_Pl²
```

For g_s ~ 1: δφ ~ M_Pl² (in natural units, this is M_Pl in eV).

**The spin-induced displacement is generically O(M_Pl), regardless
of the specific spin density value.** Since s_bounce ~ M_Pl³ always
(at Planck density), the displacement is always the same order.

There is no ADJUSTABLE parameter that connects s_bounce to a
specific φ_DE. The displacement is either M_Pl-scale (too large
for hilltop, adequate for pNGB) or zero (stabilized).

**The spin density does not usefully constrain the scalar displacement.**

---

## Test 4: Does the Bounce Set the DE Onset Epoch?

### When does DE dominate?

DE domination occurs when ρ_φ ~ ρ_matter, which happens at:
```
z_DE ~ (ρ_DE / ρ_m0)^{1/3} - 1 ~ 0.3     [observed]
```

For tracker quintessence: z_DE is set by V₀ (the potential
normalization) and λ (the slope), not by φ_i.

For frozen-field DE: z_DE is set by V(φ_i), which requires V(φ_i)
~ ρ_DE ~ 10⁻¹²² M_Pl⁴. This is a condition on the POTENTIAL
evaluated at φ_i, not on φ_i alone.

### Does the bounce control the onset?

Only if V(φ_bounce) ~ ρ_DE. This requires:

```
V(φ_i) ~ 10⁻¹²² M_Pl⁴
```

For φ_i ~ M_Pl: V must satisfy V(M_Pl) ~ 10⁻¹²² M_Pl⁴. This is
a fine-tuning of the potential, not a bounce prediction.

**The bounce does not set the DE onset epoch.**

---

## Test 5: Any Relation At All?

### Dimensional analysis

The bounce provides one scale: M_Pl (or equivalently, ρ_crit ~ M_Pl⁴).
DE requires one scale: ρ_DE^{1/4} ~ 10⁻³ eV ~ 10⁻³⁰ M_Pl.

A relation between these would require:
```
ρ_DE = f(M_Pl, other parameters)
```

The ONLY way to get 10⁻¹²² from M_Pl without fine-tuning is through
a MECHANISM that generates exponential or high-power suppression.
Known mechanisms:

1. **Instanton:** e^{-S} with S ~ 283. But S is a new parameter.
2. **Seesaw:** ρ_DE ~ Λ_low⁴ where Λ_low = Λ_high²/M_Pl. But
   Λ_high ~ 10⁻³ eV × (M_Pl/10⁻³ eV)^{1/2} ~ 10¹² eV. This is
   a new scale (not from the bounce).
3. **Running coupling:** ρ_DE ~ M_Pl⁴ exp(-8π²/g²). For g² ~ 0.27:
   ρ_DE ~ 10⁻¹²² M_Pl⁴. But g is not a bounce parameter.

**No mechanism connects M_Pl (the only bounce scale) to ρ_DE without
introducing at least one additional tuned parameter.**

---

## Summary

| Relation tested | Exists? | Mechanism | Tuning required? |
|----------------|---------|-----------|-----------------|
| ρ_bounce → ρ_DE | NO | 10¹²³ gap, no bridge | YES (exponential or new scale) |
| T_bounce → m_φ | NO | Torsion stabilizes, doesn't set mass | YES (m₀ must be tuned) |
| s_bounce → φ_i | WEAK | δφ ~ M_Pl (generic, not specific) | NO (but not predictive) |
| Bounce → z_DE | NO | Onset set by V, not φ_i | YES (V must be tuned) |
| Any M_Pl → ρ_DE | NO | Requires additional scale or instanton | YES (always) |

**The bounce provides one scale (M_Pl). Dark energy requires a
separate scale (10⁻³⁰ M_Pl). No known mechanism bridges the gap
without introducing at least one new tuned parameter.**

---

## The Fundamental Obstacle

The 122-order-of-magnitude gap between M_Pl⁴ and ρ_DE is the
cosmological constant problem. Foundation F does not solve it —
it relocates the question from "why is Λ small?" to "why does
the scalar potential have V(φ_i) ~ 10⁻¹²² M_Pl⁴?"

This is the SAME problem in different clothing. The bounce does
not help because it operates at M_Pl, not at 10⁻³⁰ M_Pl. No
initial condition set at the Planck scale can produce a prediction
for a quantity that is 10¹²² times smaller, without an additional
mechanism (and that mechanism requires its own explanation).
