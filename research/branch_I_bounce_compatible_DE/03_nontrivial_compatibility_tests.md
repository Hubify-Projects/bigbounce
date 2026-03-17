# Branch I: Nontrivial Compatibility Tests

**Date:** 2026-03-15

---

## Test I-1: Horndeski Sector Stability at the Bounce

### Question
Do Horndeski DE models (G₂, G₃, G₄, G₅ ≠ 0) remain ghost-free
and gradient-stable when the background passes through a
spin-torsion bounce at ρ_crit ~ M_Pl⁴?

### Why this matters
Horndeski models are designed to be healthy at LOW curvature (where
DE operates). But at the bounce, curvature is MAXIMAL:
```
R_bounce ~ M_Pl²
K_bounce ~ M_Pl⁴  (Kretschner scalar)
```

The stability conditions for Horndeski involve:
```
Q_S > 0  (no scalar ghost)
c_S² > 0  (no scalar gradient instability)
Q_T > 0  (no tensor ghost)
c_T² > 0  (no tensor gradient instability)
```

These conditions involve G₂, G₃, G₄, G₅ and their derivatives
evaluated on the background. At the bounce, the background is
EXTREME. The stability conditions may fail.

### What to compute
1. Evaluate Q_S, c_S², Q_T, c_T² on the bounce background for
   representative Horndeski models
2. Identify which Horndeski subclasses violate stability at bounce
3. Map the excluded region in Horndeski parameter space

### Expected outcome
Horndeski models with G₄ or G₅ involving high powers of X or φ
are likely UNSTABLE at the bounce. This would exclude certain DE
models, giving a nontrivial result.

### Priority: HIGH

---

## Test I-2: f(R) Bounce Modification

### Question
For f(R) models that produce late-time acceleration, does the f(R)
modification change the bounce dynamics in an observable way?

### Setup
The bounce occurs when R ~ M_Pl². For Hu-Sawicki f(R):
```
f(R) = R - μ² c₁(R/μ²)^n / (1 + c₂(R/μ²)^n)
```
with μ² ~ H₀² ~ 10⁻⁶⁶ eV².

At the bounce: R/μ² ~ M_Pl²/H₀² ~ 10¹²². The modification:
```
f(R_bounce) - R_bounce ~ -μ² c₁/c₂ ~ -H₀²
```
This is 10⁻¹²² × R_bounce. NEGLIGIBLE.

### Expected outcome
**All viable f(R) DE models are trivially compatible with the
bounce.** The f(R) correction is designed to be small at high
curvature (to pass solar system tests) and is negligible at the
bounce.

### Verdict: NO NONTRIVIAL CONSTRAINT
This test will confirm trivial compatibility. Low priority.

### Priority: LOW

---

## Test I-3: K-essence Sound Speed at the Bounce

### Question
Does the bounce curvature drive the k-essence sound speed c_s²
negative, creating a gradient instability?

### Setup
For general k-essence L = P(X, φ):
```
c_s² = P_X / (P_X + 2X P_XX)
```

At the bounce, if φ is kinetically dominated:
```
X_bounce ~ ρ_crit ~ M_Pl⁴
```

For DBI: P = -f(φ)⁻¹√(1 - 2f(φ)X) + f(φ)⁻¹ - V(φ)
```
c_s² = 1 - 2fX
```
If fX → 1/2: c_s → 0 (sound horizon shrinks to zero)
If fX > 1/2: c_s² < 0 (gradient instability)

At the bounce, X ~ M_Pl⁴. If f ~ M_Pl⁻⁴ (natural scale):
fX ~ 1. The DBI sound speed becomes imaginary.

### Expected outcome
DBI k-essence is likely INCOMPATIBLE with the bounce unless f(φ)
is extremely small (f ≪ M_Pl⁻⁴), which removes the distinctive
DBI signatures at low energy. This would be a genuine constraint:
the bounce EXCLUDES DBI DE models that have observable low-energy
signatures.

### Priority: MEDIUM

---

## Test I-4: Massive Gravity Ghost at Planck Curvature

### Question
Does the Boulware-Deser ghost reappear in dRGT massive gravity
when the physical metric undergoes the bounce transition?

### Setup
dRGT massive gravity is ghost-free at the FULLY NONLINEAR level
in a specific decoupling limit. But the proof assumes:
1. A fixed reference metric f_μν (usually Minkowski)
2. Regular behavior of √(g⁻¹f)

At the bounce:
- g_μν is regular (finite curvature)
- But g_00 changes sign or behavior? No — for FRW, g_00 = -1 always
- However, the scale factor passes through a minimum: a'' > 0

The matrix √(g⁻¹f) for FRW:
```
√(g⁻¹f) = diag(1, a_ref/a, a_ref/a, a_ref/a)
```

At the bounce, a = a_min. If a_min is Planck-scale and a_ref is
cosmological: a_ref/a_min ~ 10⁶⁰. The interaction term is strongly
enhanced.

### Expected outcome
The massive gravity interaction terms are ENORMOUS at the bounce.
This may violate the conditions for ghost-freedom or drive the
theory into a strong-coupling regime where the dRGT structure
breaks down. If so, massive gravity DE is incompatible with the
spin-torsion bounce.

### Priority: MEDIUM

---

## Test I-5: Energy Condition Compatibility

### Question
Do DE models that violate specific energy conditions conflict
with the spin-torsion bounce mechanism?

### Setup
The bounce requires effective NEC violation: ρ + p < 0 at ρ_crit.
In spin-torsion gravity, this comes from the ρ² term.

If a DE model ALSO violates the NEC (phantom DE, w < -1), does
the double violation create a conflict?

Phantom DE: ρ_φ + p_φ < 0 always. At the bounce:
```
ρ_total + p_total = (ρ + p)(1 - 2ρ/ρ_crit) + (ρ_φ + p_φ)
```

Both terms can be negative. This ENHANCES the bounce rather than
conflicting with it.

### Expected outcome
**No conflict.** Phantom DE models are compatible with the bounce
(they help rather than hinder it). No nontrivial constraint from
energy conditions alone.

### Priority: LOW

---

## Master Ranking

| Test | Priority | Likely outcome | Publishable? |
|------|----------|---------------|-------------|
| I-1: Horndeski stability | **HIGH** | Nontrivial exclusion | YES |
| I-3: K-essence sound speed | MEDIUM | DBI exclusion | YES |
| I-4: Massive gravity ghost | MEDIUM | Possible exclusion | YES |
| I-2: f(R) modification | LOW | Trivial compatibility | NO |
| I-5: Energy conditions | LOW | No constraint | NO |

**Recommended first computation: Test I-1 (Horndeski stability
at the bounce).** This has the highest chance of producing a
nontrivial, publishable constraint.
