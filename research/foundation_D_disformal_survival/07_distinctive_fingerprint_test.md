# Foundation D — Distinctive Fingerprint Test

**Date:** 2026-03-14

---

## Purpose

Assess whether any surviving candidate produces a genuinely geometry-
specific observable or structural fingerprint that cannot be
reproduced by non-geometric theories.

---

## The Question

After the reduction and FRW tests, no candidate produces an
observable disformal effect from geometric structure. But we should
still ask: if we IGNORE observability for a moment, does any
candidate have a STRUCTURAL feature that is uniquely geometric?

---

## Structural Features Examined

### 1. Universal four-fermion coupling (EC/PGT)

The Einstein-Cartan four-fermion interaction:

```
L_4f = -(3πG/2)(ψ̄γ^μγ₅ψ)(ψ̄γ_μγ₅ψ)
```

is UNIVERSAL: same coupling for all fermion species, with strength
fixed by Newton's constant G alone. No free parameters.

**Is this distinctive?**

YES — structurally. A generic four-fermion EFT would have independent
coupling constants for each fermion species. The EC interaction has
a SPECIFIC form (axial-axial, attractive) with a SPECIFIC coefficient
(3πG/2) determined entirely by the gravitational constant.

**But:** The effect is Planck-suppressed (G ~ 1/M_Pl²). At
accessible energies, it is undetectable. The universality is a
prediction but not a testable one.

**Verdict: GEOMETRY_SPECIFIC but UNOBSERVABLE.**

### 2. Chiral coupling asymmetry from 0⁻ mode

The 0⁻ torsion mode couples with OPPOSITE signs to left- and
right-handed fermions:

```
L_chiral = g_eff(∂_μB)(ψ̄_L γ^μ ψ_L - ψ̄_R γ^μ ψ_R)
```

In PGT, the coupling g_eff is related to the gravitational constant
and the torsion coupling t₃:

```
g_eff = 1/(M_Pl √|t₃|)
```

A generic ALP has g_eff as a free parameter. In PGT, g_eff is
CONSTRAINED by the gravitational action.

**Is this distinctive?**

MARGINALLY. The constraint is that g_eff is gravitational strength
(~ 1/M_Pl) unless |t₃| deviates from O(1). But the mass-coupling
lock (Foundation A) means that if t₃ is large enough to make the
mode light, g_eff is too small. The constraint is self-defeating.

**Verdict: Distinctive in principle but DEFEATED by the lock.**

### 3. GW speed constrained by torsion parameters

In PGT with R² terms, the GW speed depends on both curvature-squared
couplings (b_i) and torsion couplings (t_i) through mixing effects.
The specific relation:

```
c²_GW = f(b_i, t_i)     [determined by PGT action]
```

constrains the EFT parameters. In a generic Horndeski theory,
c²_GW is a free function of time.

**Is this distinctive?**

YES — the PGT parameter space is more constrained than generic
Horndeski. The GW speed is determined by a FINITE number of
dimensionless couplings (b₁, b₂, t₁, t₂, t₃), not by arbitrary
functions.

**But:** The effect is ~ 10⁻¹²⁰ for O(1) couplings. The constraint
is testable only if the torsion sector happens to produce O(1)
corrections to GW speed, which requires b_i ~ M_Pl²/H² ~ 10¹²⁰.
Unnatural.

**Verdict: GEOMETRY_SPECIFIC but UNOBSERVABLE (Planck-suppressed).**

### 4. Disformal coefficient fixed by gravitational couplings

In Toy IV (non-minimal coupling), the disformal coefficient is:

```
B_dis = c₁ c₂ / M_Pl⁴
```

where c₁, c₂ are determined by the PGT/MAG action. In a generic
disformal theory, B is a free function B(φ,X).

**Is this distinctive?**

YES — the coefficient is FIXED by the gravitational action, not
freely adjustable. The PGT origin predicts a specific value of
B_dis (up to the c₁, c₂ couplings).

**But:** B_dis ~ 1/M_Pl⁴ gives effects of order 10⁻¹²² on FRW.
Unobservable by any conceivable experiment.

**Verdict: GEOMETRY_SPECIFIC but UNOBSERVABLE (M_Pl⁻⁴).**

---

## The Observability Gap

All four structural features above are GEOMETRY_SPECIFIC but
UNOBSERVABLE. This creates a fundamental problem:

**The geometric fingerprint exists but is hidden behind the Planck
suppression of gravitational effects.**

Any distinctive feature of PGT/MAG is suppressed by powers of G
(or equivalently M_Pl⁻²). At cosmological energies (E ~ H ~ 10⁻³³ eV),
the ratio H/M_Pl ~ 10⁻⁶⁰ ensures that all geometry-specific effects
are negligible.

This is not a failure of specific models — it is a structural
feature of gravitational theories. The geometric content is encoded
at the Planck scale, and its low-energy remnants are too weak to
observe.

---

## Comparison with Known Observable Signatures

### Signatures that ARE observable

| Effect | Mechanism | Geometric? |
|--------|-----------|-----------|
| CMB birefringence | ALP rolling through CMB epoch | No (generic ALP) |
| Modified GW speed | Horndeski G₄(X), G₅ | No (generic scalar-tensor) |
| Vainshtein screening | Galileon self-interaction | No (generic Horndeski) |
| Chameleon screening | Non-minimal coupling + potential | No (generic scalar-tensor) |
| GW amplitude birefringence | Chern-Simons coupling | No (generic ALP + gravity) |

All observationally accessible effects in modified gravity are
GENERIC — they exist in ANY scalar-tensor or ALP theory regardless
of geometric origin. The geometry-specific effects are Planck-
suppressed and inaccessible.

### Why this pattern persists

In any gravity theory, the coupling of new degrees of freedom to
matter goes through the GRAVITATIONAL constant G = 1/(8πM_Pl²).
This sets a MAXIMUM coupling strength for any geometrically derived
interaction:

```
g_geometric ≤ O(1/M_Pl)
```

Observable effects from new scalars require g × (field amplitude)
to be comparable to known physics. For g ~ 1/M_Pl and field ~ M_Pl:
the effect is O(1). But:

- If the scalar field has Planck-scale amplitude: it affects the
  background geometry (it IS the metric). This is standard GR.
- If the scalar field has sub-Planck amplitude: its effects are
  suppressed by (field/M_Pl) × (g × M_Pl) < 1.

The only way around this is to give the scalar a LARGE coupling
g >> 1/M_Pl. But in a geometric theory, g is fixed by G. You
cannot make the geometric coupling larger than gravitational
strength without introducing new (non-geometric) interactions.

---

## DR3 Verdict

| Fingerprint | Geometry-specific? | Observable? |
|-------------|-------------------|------------|
| Universal 4-fermion (EC) | YES | NO (G-suppressed) |
| Chiral coupling (0⁻) | YES (but locked) | NO (lock + G) |
| GW speed from PGT | YES | NO (10⁻¹²⁰) |
| Fixed disformal coeff. | YES | NO (M_Pl⁻⁴) |

**Overall DR3: FAILS on observability.**

The geometric fingerprints EXIST but are UNOBSERVABLE. This is a
stronger statement than Foundation C (where the fingerprints didn't
exist after reduction). Here, the fingerprints exist but are hidden
behind the Planck scale.

---

## Implications

### The Planck Suppression Theorem (informal)

In any gravitational theory where the new degrees of freedom couple
to matter ONLY through the connection (covariant derivative), the
coupling strength is bounded by:

```
g ≤ O(1/M_Pl)
```

All distinctive geometric effects are therefore suppressed by at
least (E/M_Pl)² relative to standard physics, where E is the
observation energy scale.

For cosmology (E ~ H₀ ~ 10⁻³³ eV): suppression ~ (H₀/M_Pl)² ~ 10⁻¹²².

**No geometric fingerprint from connection coupling can produce
observable effects in cosmology.**

### The escape clause

The Planck suppression theorem has one loophole: if the scalar has
a MACROSCOPIC field value (φ ~ M_Pl), the coupling g_eff × φ can be
O(1). This is the regime where the scalar is part of the metric
(conformal factor, scale connection, etc.) — standard scalar-tensor
gravity.

But scalar-tensor gravity IS Foundation C territory: generic,
with no distinctive geometric fingerprint.

**The circle closes: observable effects are generic (scalar-tensor),
while distinctive effects are unobservable (Planck-suppressed).**
