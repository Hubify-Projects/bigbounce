# Foundation D — Reduction / Equivalence Test

**Date:** 2026-03-14

---

## Purpose

Determine the equivalence class of each candidate mechanism after
all auxiliary and geometric fields are integrated out. The question
is: does the reduced EFT belong to a class BEYOND conformal
scalar-tensor, and if so, is it distinctively geometric?

---

## Equivalence Classes

```
1. GENERIC_CONFORMAL:    g̃_μν = A(φ) g_μν
   - Includes: Brans-Dicke, quintessence, f(R), conformal coupling
   - Foundation C territory: closed

2. GENERIC_DISFORMAL:    g̃_μν = A(φ,X) g_μν + B(φ,X) ∂_μφ ∂_νφ
   - Includes: Horndeski, beyond-Horndeski, DHOST
   - Goes beyond conformal, but freely parameterized: not distinctive

3. GEOMETRY_SPECIFIC:    As above but with A, B constrained by
                         geometric structure (fixed ratios, consistency
                         relations from PGT/MAG couplings)
   - Would be genuinely new: geometric origin visible in EFT

4. PATHOLOGICAL:         Disformal structure present but introduces
                         ghosts, gradient instabilities, or
                         Ostrogradski modes
```

---

## The Fundamental Reduction Theorem

### Why torsion elimination cannot produce disformal couplings

**Theorem:** In PGT or EC gravity with standard (minimal) coupling
of fermions to the connection, torsion elimination produces GAUGE-
LIKE couplings (derivative of scalar × matter current) or four-
fermion CONTACT terms. Neither structure is disformal.

**Proof sketch:**

1. Torsion couples to matter through the covariant derivative:
   D_μψ = ∂_μψ + ¼ω_μ^{ab}γ_{ab}ψ.

2. The torsion contribution to ω enters as a CONTORTION tensor
   K^{ab}_μ, linear in torsion.

3. For irreducible torsion components:
   - Axial vector (0⁻): K_μ ~ A_μ γ₅ where A_μ = ∂_μB. This
     produces (∂_μB)(ψ̄γ^μγ₅ψ) — a chiral gauge coupling.
   - Trace vector (0⁺): K_μ ~ T_μ where T_μ = ∂_μφ. This
     produces (∂_μφ)(ψ̄γ^μψ) — a vector gauge coupling.
   - Tensor (2⁺): produces non-abelian-like spin-spin couplings.

4. All three structures involve the FIRST derivative of the torsion
   mode contracted with a fermion CURRENT (zero derivatives of ψ
   beyond the kinetic term).

5. A disformal effective metric g̃_μν = g_μν + B∂_μφ∂_νφ would
   require a modification of the fermion KINETIC term of the form
   (∂_μφ)(∂_νφ)(ψ̄γ^μ∂^νψ) — involving a PRODUCT of two scalar
   derivatives with a fermion derivative.

6. The connection structure ω_μ^{ab}γ_{ab} involves only ONE index
   μ contracted with the fermion kinetic term γ^μ∂_μψ. There is
   no second free index to create the ∂_μφ∂_νφ structure.

**Therefore: the connection coupling prescription (one covariant
derivative) can produce at most ONE power of ∂φ contracted with
the fermion current, not TWO powers needed for disformal structure.**

This is not a limitation of specific models — it is a structural
property of how connections couple to matter through covariant
derivatives.

### Corollary: Non-metricity also fails

The same argument applies to non-metricity. Even if non-metricity
DID couple to fermions (which it doesn't in the standard prescription
due to the γ^{ab} antisymmetry), it would couple through a single
covariant derivative, producing at most a gauge-like coupling —
not a disformal structure.

---

## Candidate-by-Candidate Reduction

### Candidate A (0⁻ torsion-fermion): GENERIC_CONFORMAL

```
(∂_μB)(ψ̄γ^μγ₅ψ) → ALP-fermion derivative coupling
```

After reduction: standard ALP effective theory. Equivalent to any
pseudoscalar with derivative coupling to axial current.

Conformal? Actually not even conformal — it's an independent
derivative coupling, not a metric modification. But it's within
the ALP EFT framework, which is a SUBCLASS of conformal scalar-
tensor theory (the ALP can be dualized to a conformal coupling
in specific limits).

**Class: GENERIC_CONFORMAL (ALP subclass)**

### Candidate B (0⁺ torsion-fermion): TRIVIAL

```
(∂_μφ)(ψ̄γ^μψ) → removable by ψ → e^{-ig_eff φ}ψ
```

After reduction: NO COUPLING. The 0⁺ derivative coupling to the
vector current is a flat U(1) connection and can be gauged away.

**Class: TRIVIAL (no physical coupling)**

### Candidate C (non-metricity-fermion): NULL

```
ω_{μ(ab)} γ^{ab} = 0     [antisymmetric γ kills symmetric ω]
```

Non-metricity does not couple to fermions through the standard
covariant derivative.

**Class: NULL (no coupling exists)**

### Candidate D (heavy torsion → contact EFT): GENERIC_CONFORMAL

```
integrate out B: → (g_eff²/μ²)(ψ̄γ₅ψ)² + higher-derivative corrections
```

A four-fermion contact interaction. Does not modify propagation.
Equivalent to the standard Einstein-Cartan four-fermion term.

**Class: GENERIC_CONFORMAL (contact subclass)**

### Candidate E (R² → GW speed): GENERIC_DISFORMAL

```
c²_GW = 1 + O(b_i R/M_Pl²) → g̃^tensor_μν = g_μν + Δc² u_μ u_ν
```

This IS disformal (for the tensor sector), but:
1. Not specific to PGT (any R² theory gives this)
2. Constrained to |Δc²| < 10⁻¹⁵ by GW170817
3. Would need b_i ~ 10¹²⁰ for cosmological relevance

**Class: GENERIC_DISFORMAL (not geometry-specific)**

### Candidate F (Chern-Simons): GENERIC_DISFORMAL

```
θRR̃ → polarization-dependent GW propagation
```

Disformal in the spin-dependent sense. But:
1. Standard Chern-Simons gravity (any ALP + gravity)
2. Not cosmological background effect (RR̃ = 0 on FRW)
3. Already studied extensively

**Class: GENERIC_DISFORMAL (not geometry-specific)**

---

## Why Disformal Structures Cannot Arise From Connection Coupling

### The structural argument

Disformal effective metrics arise in scalar-tensor theories through
HIGHER-DERIVATIVE interactions of the scalar with itself and with
matter:

```
Horndeski L₃: G₃(φ,X) □φ     → kinetic braiding
Horndeski L₄: G₄(φ,X) R      → disformal if G₄ depends on X
Horndeski L₅: G₅(φ,X) G_μν   → disformal
```

These terms involve SECOND derivatives of φ (through □φ, R, G_μν).
They arise when the scalar has non-trivial self-interactions beyond
the canonical kinetic term.

In PGT/MAG, the scalar degrees of freedom (torsion modes) DO have
non-trivial self-interactions from the quadratic torsion/curvature
action. But these self-interactions produce the MASS and KINETIC
terms for the torsion mode — they are already accounted for in the
canonical normalization of the propagating mode.

The COUPLING to matter comes through the covariant derivative (one
derivative, one contraction with γ^μ). This is structurally
insufficient for disformal couplings (which need two derivatives of
the scalar in the matter kinetic term).

### The exception that doesn't help

There IS one way to get higher-derivative couplings from geometry:
if the CURVATURE (not torsion) itself produces a non-minimal coupling
to matter through terms like:

```
R_μν ψ̄ γ^μ ∂^ν ψ     [non-minimal gravitational coupling]
```

In PGT, R_μν(Γ) includes torsion-dependent terms. After torsion
elimination, this could produce:

```
T_μν × ψ̄ γ^μ ∂^ν ψ → (∂_μB)(∂_νB) × ψ̄ γ^μ ∂^ν ψ
```

This IS a disformal-type coupling! But:

1. The R_μν coupling to fermions is a DIMENSION-5 operator
   (suppressed by 1/M_Pl).
2. After torsion elimination: the coefficient is (t_i/M_Pl²).
3. The resulting disformal coupling is:
   ```
   B_disformal ~ (t_i g_eff² / M_Pl² μ²) × (∂_μφ)(∂_νφ)
   ```
   This is O(1/M_Pl⁴) — unobservable.

Even at the structural level, this "disformal" coupling exists but
is Planck-suppressed and indistinguishable from generic higher-
dimensional operators in any gravitational EFT.

---

## Summary

| Candidate | Equivalence class | Geometry-specific? |
|-----------|------------------|-------------------|
| A: 0⁻ fermion | GENERIC_CONFORMAL | No |
| B: 0⁺ fermion | TRIVIAL | N/A |
| C: Q-fermion | NULL | N/A |
| D: Heavy torsion EFT | GENERIC_CONFORMAL | No |
| E: R² GW speed | GENERIC_DISFORMAL | No |
| F: Chern-Simons | GENERIC_DISFORMAL | No |

**No candidate achieves GEOMETRY_SPECIFIC classification.**

The fundamental reason: connections couple to matter through a
SINGLE covariant derivative, which produces gauge-like couplings
(one derivative of the scalar × one fermion current). Disformal
couplings require TWO derivatives of the scalar in the matter
kinetic term, which the connection structure cannot provide.
