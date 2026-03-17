# Best Phase 2 Target

**Date:** 2026-03-16

---

## Recommendation: Candidate A — PGT Ghost-Free Parameter Space
with Observable ρ_crit

### Why this target

Candidate A (PGT lower-scale bounce) is the only candidate that
survived screening unconditionally. The single outstanding question
is whether the PGT parameter space simultaneously allows:

1. **Ghost freedom** for propagating torsion modes
2. **ρ_crit^{eff} in the LISA/LIGO range** (m_T ~ 10³–10⁹ GeV)
3. **Consistency with Foundation A mass-coupling lock**
4. **Detectable GW signal amplitude**

This is a well-defined, closed-form question that can be answered
with a single calculation.

---

## Calculation Specification

### Step 1: PGT parameter space mapping

The general PGT Lagrangian has 10 free parameters (3 torsion
quadratic, 6 curvature quadratic, plus M_Pl). For the spin-0
torsion mode (vector trace T_μ), the relevant subset is:

```
L_torsion = α₁ T_μνρ T^μνρ + α₂ T_μνρ T^νμρ + α₃ T_μ T^μ
```

Decomposing torsion into irreducible representations:
- Tensor part (spin-2): 16 components
- Vector trace T_μ (spin-1): 4 components
- Axial vector S_μ (spin-1): 4 components

The trace mode mass and kinetic terms are:

```
m_T² = f(α₁, α₂, α₃)
K_T = g(α₁, α₂, α₃)    (kinetic coefficient; K_T > 0 for ghost-free)
```

### Step 2: Ghost-free conditions

The no-ghost conditions for all three torsion irreps impose
inequalities on (α₁, α₂, α₃). Literature results (Hayashi-Shirafuji,
Sezgin-van Nieuwenhuizen, Neville):

```
Spin-2 ghost-free:  α₁ > 0
Spin-1 (trace) ghost-free:  2α₁ + α₂ + 3α₃ > 0   (or < 0, sign convention dependent)
Spin-1 (axial) ghost-free:  α₁ + α₂ > 0           (or < 0)
```

(Exact conditions depend on sign conventions; Phase 2 must fix
conventions from a specific PGT reference.)

### Step 3: ρ_crit^{eff} as function of PGT parameters

The modified Friedmann equation in PGT with FRW symmetry:

```
H² = (8πG/3) ρ × [1 - ρ/ρ_crit^{eff}(α_i, β_i)]
```

where ρ_crit^{eff} includes contributions from torsion kinetic
and mass terms. The parametric form:

```
ρ_crit^{eff} ~ M_Pl⁴ / (1 + M_Pl² / Λ_PGT²)
```

where Λ_PGT² ~ α_i M_Pl² is the torsion parameter scale. For
Λ_PGT ≪ M_Pl:

```
ρ_crit^{eff} ~ Λ_PGT² M_Pl²
```

### Step 4: Mass-coupling lock check

Foundation A established:

```
g_eff ~ 1 / (M_Pl √|t₃|)
```

where t₃ is a dimensionless PGT parameter. For the target
ρ_crit^{eff}:

```
ρ_crit^{eff} ~ m_T² M_Pl²  →  m_T ~ Λ_PGT
```

The lock constrains:
```
g_eff m_T ~ m_T / (M_Pl √|t₃|)
```

If t₃ ~ (M_Pl / m_T)²: g_eff ~ m_T / M_Pl² ≪ 1 (very weak).
Question: is g_eff strong enough to produce detectable GW features?

### Step 5: GW amplitude estimate

The tensor spectrum features from the PGT bounce:

```
Ω_GW(f) = Ω_GW^{smooth}(f) × |1 + A_osc(f/f_b)|²
```

The oscillation amplitude A_osc depends on:
- Bounce sharpness: Δη_b ~ 1/k_b
- Torsion coupling strength: g_eff
- Number of torsion oscillations during bounce

For A_osc ~ g_eff² × (torsion oscillation enhancement):

Need A_osc × Ω_GW^{smooth} > Ω_GW^{sensitivity}

---

## Expected Outcome

### Optimistic scenario (probability ~20%)

The ghost-free region of PGT parameter space DOES overlap with
m_T ~ 10³–10⁹ GeV. The mass-coupling lock permits this range.
The GW signal amplitude is within 2–3 orders of magnitude of
LISA/ET sensitivity.

→ Publishable positive result: "PGT bounce features in the
LISA/ET band."

### Moderate scenario (probability ~50%)

The ghost-free region exists but the GW amplitude is too low
(suppressed by weak g_eff from the mass-coupling lock). The
signal is 5–10 orders below sensitivity.

→ Publishable parameter-space constraint: "PGT parameters
required for observable GW features from spin-torsion bounce."

### Pessimistic scenario (probability ~30%)

The ghost-free conditions and mass-coupling lock are incompatible
with m_T in the target range. No viable parameter point exists.

→ Publishable no-go result: "Observable spin-torsion bounce
features require ghostly torsion modes."

**All three outcomes are publishable.** This is the mark of a
good Phase 2 target.

---

## Scope and Resources

### What Phase 2 requires

1. **Fix PGT conventions:** Choose a specific PGT Lagrangian from
   the literature (Hayashi-Shirafuji or Sezgin-van Nieuwenhuizen)
   and write all conditions in consistent notation.

2. **Map ghost-free region:** Plot the ghost-free parameter space
   in (α₁, α₂, α₃) or equivalent reduced coordinates.

3. **Overlay ρ_crit^{eff} contours:** On the ghost-free region,
   draw contours of constant ρ_crit^{eff}.

4. **Apply mass-coupling lock:** Overlay the Foundation A constraint
   on the same parameter space.

5. **Estimate GW amplitude:** For viable parameter points (if any),
   compute the tensor spectrum through the PGT bounce and compare
   with LISA/ET sensitivity curves.

### Estimated effort
- Steps 1–4: 1 session (algebraic, literature-based)
- Step 5: 1–2 sessions (numerical, requires mode equation solver)

### Dependencies
- Foundation A results (already computed in Paper 1.2)
- PGT ghost-free conditions (literature; Hayashi-Shirafuji 1979,
  Sezgin-van Nieuwenhuizen 1980, Neville 1980)
- LISA/ET sensitivity curves (publicly available)

---

## Alternative Target: Candidate E (Torsion-Curvaton)

If Candidate A is ruled out in Phase 2, the fallback is Candidate E
(torsion-curvaton). However, Candidate E has a much lower survival
probability (~3%) due to the three-condition requirement:

1. Viable contraction model with large H_exit
2. Mass-coupling lock permits light m_T
3. Ghost-free PGT parameters

**Do NOT pursue Candidate E unless Candidate A yields a positive
or moderately positive result.** Candidate E extends the same
PGT framework, so a negative result for A would likely kill E as
well (via the same ghost-free and lock constraints).

---

## Decision Tree

```
Phase 2: PGT parameter space mapping
         │
         ├── Ghost-free + lock-compatible region EXISTS with m_T in target range
         │         │
         │         ├── GW amplitude detectable → PUBLISH (positive)
         │         │
         │         └── GW amplitude too low → PUBLISH (parameter constraint)
         │                   │
         │                   └── Check Candidate E as fallback
         │
         └── No viable region exists
                   │
                   └── PUBLISH (no-go) → Branch L CLOSED
```

---

## Non-Target: What NOT to Compute in Phase 2

- Do NOT compute the matter bounce (Candidate C) in detail.
  It is not bounce-specific.
- Do NOT pursue bounce + inflation (Candidate B). It reduces
  to inflation.
- Do NOT attempt cyclic models (Candidate G). The turnaround
  mechanism is outside the EC framework.
- Do NOT compute generic curvaton models (Candidate D). They
  are not torsion-specific.
- Do NOT compute relic production (Candidate F). The corrections
  are 10⁻¹² and negligible.
