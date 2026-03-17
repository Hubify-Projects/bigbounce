# Foundation C — Distinctiveness Test (DR3)

**Date:** 2026-03-14

---

## Purpose

For each surviving candidate (A, C, D), determine whether the
mechanism produces anything beyond standard scalar-tensor dark
energy after reduction.

---

## The Reduction Theorem

**Claim:** Any single propagating scalar degree of freedom from a
geometric theory (PGT, MAG, Weyl geometry, f(R), etc.) reduces
to a scalar-tensor theory in the Einstein frame after all non-metric
fields are eliminated.

**Sketch of proof:**

1. In quadratic gravity theories, torsion and non-metricity are
   algebraic (non-propagating). Their field equations are constraint
   equations that express them as functions of matter fields and the
   remaining propagating degrees of freedom.

2. After substituting these solutions, the action depends only on
   the metric g_μν, the propagating scalar(s), and matter fields.

3. The most general local action for a single scalar + metric with
   at most two derivatives is the Horndeski Lagrangian (or a
   subclass thereof).

4. For the candidates considered here, the actions are SUBSETS of
   Horndeski: specifically, they are Brans-Dicke / quintessence /
   f(R) type theories.

**Implication:** The geometric origin constrains which SUBCLASS of
scalar-tensor theory the model falls into, but does not produce
anything OUTSIDE the scalar-tensor framework.

---

## Candidate A: Conformally Coupled Scalar

### After reduction

The Einstein-frame action:

```
S_EF = ∫ d⁴x √g_E [
    ½M_Pl² R_E
    - ½(∂ψ)²
    - V_eff(ψ)
    + matter minimally coupled to g_E
]
```

where ψ is the canonically normalized scalar (related to φ by a
field redefinition) and V_eff(ψ) is determined by the conformal
factor and the original coupling.

### What class?

This is **quintessence** with a specific potential V_eff(ψ). The
potential is determined by the conformal coupling ξ = 1/6 and
the matter coupling α.

### Is V_eff distinctive?

For a conformally coupled scalar on FRW, the effective potential in
the Einstein frame is:

```
V_eff(ψ) ~ (conformal anomaly) ~ Λ_QCD⁴ × function(ψ/M_Pl)
```

This is a radiatively generated potential from the trace anomaly
of matter fields. Its form is determined by the matter content
(QCD scale, particle masses) — NOT by the geometric origin of ψ.

A generic quintessence model with the same potential would produce
identical predictions.

**Verdict: NOT DISTINCTIVE.**

### Possible distinctive element

In the Jordan frame, the conformal coupling means that the scalar
modifies the effective Newton's constant:

```
G_eff = G / (1 + 2α²)
```

This is a specific prediction: G_eff differs from G_N by a factor
determined by α. But this is standard Brans-Dicke phenomenology.
Current constraints (Cassini, lunar laser ranging) require α² < 10⁻⁵,
meaning the scalar is essentially decoupled in the local environment.

---

## Candidate C: Geometric Symmetron

### After reduction

The symmetron mechanism produces a scalar with:
- Environment-dependent VEV: φ₀(R)
- Environment-dependent coupling: g_eff ∝ φ₀
- Screening in high-curvature regions

### What class?

This is a **symmetron** — a well-studied screening mechanism
(Hinterbichler & Khoury 2010).

### Is the geometric version distinctive?

In the geometric version, the curvature R replaces the density ρ
as the control parameter for the symmetron transition. Since
R = 8πGρ(1-3w), these are closely related.

Differences:
1. **R vs ρ:** The curvature R depends on pressure as well as
   density (through the 1-3w factor). During radiation (w = 1/3),
   R = 0 while ρ ≠ 0. So the geometric symmetron behaves
   differently from the density-based symmetron during radiation.

2. **Transition epoch:** The curvature-based transition occurs when
   R drops below R_crit = μ²/ξ. The density-based transition
   occurs when ρ drops below ρ_crit = μ²M²/α. These have
   different time-dependences because R and ρ evolve differently
   (R ∝ a⁻³(1-3w) vs ρ ∝ a⁻³(1+w)).

3. **Radiation era behavior:** The geometric symmetron has φ ≠ 0
   during radiation (R = 0 < R_crit), while the density-based
   symmetron has φ = 0 during radiation (ρ > ρ_crit, assuming
   ρ_crit is set at late times). This is a QUALITATIVE difference.

### Assessment

The R-vs-ρ distinction is a genuine structural difference, but:

1. **It's not uniquely geometric.** Any scalar with a ξRφ² coupling
   (regardless of origin) shows the same behavior. The PGT/MAG
   origin doesn't add anything.

2. **The radiation-era behavior** (φ ≠ 0 when R = 0) could be
   either a feature or a bug. It means the scalar is active during
   BBN, which is tightly constrained. This may RULE OUT the
   geometric symmetron rather than distinguish it.

3. **The μ tuning** (μ ~ H₀) is the same as in the standard
   symmetron. No geometric symmetry protects it.

**Verdict: MARGINALLY DISTINCTIVE** (R-vs-ρ difference exists but
is not uniquely geometric and may be observationally disfavored).

---

## Candidate D: Weyl Scalar

### After reduction

Identical to Candidate A (conformally coupled scalar with gauge-
protected m₀ = 0).

### Is the gauge protection distinctive?

The Weyl gauge symmetry provides a STRONGER theoretical motivation
for m₀ = 0 than conformal symmetry:
- Conformal symmetry is a GLOBAL symmetry (can be broken by anomalies).
- Weyl gauge symmetry is a LOCAL symmetry (mass term is gauge-forbidden).

This is analogous to the photon mass being exactly zero (protected by
U(1) gauge invariance) vs. a neutrino mass being small (protected
only by a global symmetry that could be weakly broken).

However: the PHENOMENOLOGICAL predictions are the same. The Weyl
gauge protection affects the UV completion, not the IR observables.

**Verdict: NOT DISTINCTIVE in phenomenology.** Strongest theoretical
motivation, but indistinguishable from Candidate A observationally.

---

## The Fundamental Problem

### Why no candidate is distinctive

The environmental mass mechanism (m² ~ ξR) is a NON-MINIMAL COUPLING
between a scalar and the Ricci scalar. This is the defining feature
of scalar-tensor gravity.

In scalar-tensor gravity, the complete phenomenology is determined by:
1. The coupling function ω(φ) or equivalently α(φ)
2. The scalar potential V(φ)
3. The matter coupling (minimal or disformal)

The geometric origin (from torsion, non-metricity, connection dynamics)
determines the SPECIFIC form of ω(φ) and V(φ) — but any form can
be achieved by a generic scalar-tensor theory with appropriately
chosen functions.

**The geometric origin constrains the EFT parameters but does not
produce novel EFT operators.**

This is the same conclusion as Foundation B (for pseudoscalars):
at low energies, all weakly coupled scalars look like scalar-tensor
theories, regardless of their UV origin.

---

## What Would Genuine Distinctiveness Look Like?

To produce something beyond scalar-tensor gravity, a geometric
theory would need to generate:

1. **Multiple correlated scalars** with specific mass and coupling
   relations derived from the geometry. (But multi-scalar theories
   are also generic — no unique geometric prediction.)

2. **Higher-derivative operators** (Horndeski L₃, L₄, L₅ terms)
   with coefficients determined by the gravitational action. These
   produce Vainshtein screening, which is different from chameleon/
   symmetron screening.

3. **Disformal couplings** (g̃_μν = A(φ)g_μν + B(φ)∂_μφ∂_νφ) that
   arise naturally from torsion elimination. The disformal piece
   B(φ) would be a genuinely geometric contribution.

4. **Parity-violating effects** (gravitational birefringence, chiral
   gravitational waves) from the pseudoscalar sector of the geometry.
   But Foundation B showed these reduce to generic ALP effects.

Option 3 (disformal couplings from torsion) is the most promising
unexplored direction. In PGT, the torsion-fermion coupling has the
form T_μ ψ̄γ^μγ₅ψ. After torsion elimination, this produces
four-fermion terms AND (if a propagating scalar is present)
disformal-type couplings. The disformal coefficient would be
determined by the PGT couplings — potentially a distinctive
geometric prediction.

But this is beyond the scope of Foundation C Phase 1.

---

## DR3 Verdict Summary

| Candidate | Reduces to | Distinctive? | Geometric fingerprint? |
|-----------|-----------|-------------|----------------------|
| A | Quintessence (conformal) | NO | None (standard ξRφ²) |
| C | Symmetron (curvature-based) | MARGINAL | R-vs-ρ difference |
| D | Quintessence (= A) | NO | None (gauge motivation only) |

**Overall DR3 verdict: FAILS.**

No surviving candidate produces phenomenology that is both:
- Uniquely traceable to geometric origin
- Observationally distinguishable from generic scalar-tensor models
