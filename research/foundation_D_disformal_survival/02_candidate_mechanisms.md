# Foundation D — Candidate Mechanisms

**Date:** 2026-03-14

---

## Overview

We examine five candidate mechanisms by which torsion/non-metricity
elimination or metric-affine reduction might produce disformal
effective couplings.

---

## Candidate A: Torsion Elimination in the Fermion Sector (0⁻ Mode)

### Setup

PGT with a propagating 0⁻ pseudoscalar torsion mode B coupled to
Dirac fermions:

```
S_A = ∫ d⁴x √g [
    ½M_Pl² R(g) + ½Z(∂B)² - ½μ²B²
    + g_eff (∂_μ B)(ψ̄ γ^μ γ₅ ψ)
    + ψ̄(iγ^μ ∂_μ - m_f)ψ
]
```

The 0⁻ torsion mode couples to the fermion AXIAL current J^μ₅ = ψ̄γ^μγ₅ψ
through a DERIVATIVE coupling (∂_μB)J^μ₅.

### What survives after analysis

The Dirac equation in the B background:

```
(iγ^μ∂_μ + g_eff(∂_μB)γ^μγ₅ - m_f)ψ = 0
```

For chiral fermions (definite γ₅ eigenvalue):

```
Right-handed: iγ^μ(∂_μ + g_eff ∂_μB)ψ_R = m_f ψ_L
Left-handed:  iγ^μ(∂_μ - g_eff ∂_μB)ψ_L = m_f ψ_R
```

In the eikonal (geometric optics) limit for massless fermions:

```
Right: (k_μ + g_eff ∂_μB)² = 0    [null condition with shifted momentum]
Left:  (k_μ - g_eff ∂_μB)² = 0    [opposite shift]
```

This is a MOMENTUM SHIFT, not a metric modification. The fermions
propagate on null geodesics of the SAME metric g_μν, but with
chirality-dependent effective momenta.

### Is this disformal?

**NO.** The derivative coupling (∂_μB)J^μ₅ is a GAUGE-LIKE coupling
(abelian chiral gauge field A^5_μ = g_eff ∂_μB). It produces:

- Birefringence (left vs right polarizations travel with different
  effective frequencies) — this is standard ALP birefringence
- Phase rotation of CMB polarization — identical to generic ALP
  predictions

It does NOT produce an effective metric modification g̃_μν =
A g_μν + B ∂_μB ∂_νB. The distinction: a disformal metric changes
the NULL CONE, while a chiral gauge coupling shifts momenta along
the existing null cone.

### Biggest risk

This IS Route T1 / generic ALP. The 0⁻ torsion mode couples
exactly like any pseudoscalar ALP. Foundation B already closed this.

### FRW survival

On FRW with a homogeneous B(t): ∂_μB = (Ḃ, 0, 0, 0). The
birefringence effect is proportional to Ḃ. If B is light and
rolling, Ḃ ~ HB ~ H f_a. The CMB rotation angle is:

```
Δα ~ g_eff ΔB ~ g_eff f_a (for f_a ~ M_Pl: Δα ~ g_eff M_Pl)
```

This IS nonzero on FRW but is standard ALP CMB birefringence.

**Verdict: CONFORMAL_ONLY (actually not even conformal — it's a
gauge-like coupling, not a metric modification). Equivalent to
generic ALP. Foundation B territory.**

---

## Candidate B: Torsion Elimination in the Fermion Sector (0⁺ Mode)

### Setup

```
S_B = ∫ d⁴x √g [
    ½M_Pl² R(g) + ½Z(∂φ)² - ½μ²φ²
    + g_eff (∂_μ φ)(ψ̄ γ^μ ψ)
    + ψ̄(iγ^μ ∂_μ - m_f)ψ
]
```

The 0⁺ torsion trace mode φ couples to the fermion VECTOR current
J^μ = ψ̄γ^μψ through a derivative coupling.

### What survives after analysis

The Dirac equation:

```
(iγ^μ∂_μ + g_eff(∂_μφ)γ^μ - m_f)ψ = 0
γ^μ(i∂_μ + g_eff ∂_μφ)ψ = m_f ψ
```

This is an abelian vector gauge coupling with A_μ = g_eff ∂_μφ
(a pure gradient). The field strength vanishes: F_μν = 0.

**This coupling is COMPLETELY REMOVABLE by the field redefinition:**

```
ψ → e^{-ig_eff φ} ψ
```

After redefinition: the fermion kinetic term returns to standard form
(i∂_μ) and the mass term is unchanged (ψ̄ψ is phase-invariant for
this transformation). ALL dependence on φ disappears from the
fermion sector.

### Is this disformal?

**NO.** There is no physical effect AT ALL from the 0⁺ torsion-
fermion coupling. It is gauge-removable.

(Caveat: at the quantum level, the chiral anomaly can prevent
complete removal if fermions have chiral gauge couplings. But this
is a loop effect, suppressed by 1/16π², and produces an effective
θ-angle — standard ALP physics again.)

### Biggest risk

There is nothing here. The coupling is trivial.

**Verdict: NO EFFECT. The 0⁺ torsion-fermion derivative coupling
is a flat gauge connection, removable by field redefinition.**

---

## Candidate C: Non-Metricity Coupling to Fermions in MAG

### Setup

In MAG, the spinor covariant derivative involves the full connection:

```
D_μ ψ = ∂_μ ψ + ¼ ω_{μab} γ^{ab} ψ
```

where ω_{μab} = ω_{μ[ab]} + ω_{μ(ab)} and ω_{μ(ab)} = Q_{μab}/2.

### Key algebraic identity

The spin connection enters through γ^{ab} = ½[γ^a, γ^b], which is
ANTISYMMETRIC in a, b.

The non-metricity part ω_{μ(ab)} is SYMMETRIC in a, b.

Therefore:

```
ω_{μ(ab)} γ^{ab} = ω_{μ(ab)} × (antisymmetric tensor) = 0
```

**Non-metricity DROPS OUT of the Dirac equation in the standard
minimal coupling prescription.**

### Is this disformal?

**N/A — non-metricity does not couple to fermions at all** through
the standard covariant derivative. There is no effective metric
modification, conformal or disformal.

### Non-minimal coupling possibility

One could ADD a non-minimal coupling by hand:

```
L_nm = g_Q Q_μ ψ̄ γ^μ ψ     [coupling to Weyl vector trace]
```

But this is an AD HOC addition, not a consequence of the geometric
structure. And it's another derivative coupling (Q_μ = ∂_μσ for
Stückelberg scalar σ), removable by field redefinition — same as
Candidate B.

**Verdict: NULL. Non-metricity does not couple to fermions in the
standard prescription. Ad hoc additions are removable.**

---

## Candidate D: Integrating Out Heavy Torsion → Higher-Derivative EFT

### Setup

If the torsion mode is HEAVY (m_B >> H), integrate it out to obtain
the low-energy effective action.

```
S = ∫ d⁴x √g [½M_Pl² R(g) - ½Z(∂B)² - ½μ²B² + g_eff(∂_μB)J^μ₅ + L_fermion]
```

B equation of motion:

```
Z□B - μ²B = g_eff ∂_μ J^μ₅
```

At low energies (□ << μ²/Z):

```
B ≈ -(g_eff / μ²) ∂_μ J^μ₅
```

Using the axial current divergence ∂_μ J^μ₅ = 2im_f ψ̄γ₅ψ
(for massive fermions):

```
B ≈ -(2ig_eff m_f / μ²) ψ̄γ₅ψ
```

### Effective action after elimination

Substituting B_cl back:

```
S_eff ⊃ +(g_eff² / 2μ²)(∂_μ J^μ₅)²
       = +(g_eff² / 2μ²)(2m_f)²(ψ̄γ₅ψ)²
       = +(2g_eff² m_f² / μ²)(ψ̄γ₅ψ)²
```

This is a FOUR-FERMION CONTACT INTERACTION with pseudoscalar
structure. It is the well-known Hehl-Datta interaction (generalized
for propagating torsion).

### Is this disformal?

**NO.** A four-fermion contact interaction is a LOCAL operator. It
does not modify the fermion propagation equation (no effective
metric). It only affects scattering amplitudes.

The operator (ψ̄γ₅ψ)² has NO derivatives of ψ — it is a potential-
type interaction, not a kinetic modification.

### What about higher-order corrections?

At next order in the derivative expansion (□/μ²):

```
B ≈ -(g_eff / μ²)[1 + Z□/μ² + ...] ∂_μ J^μ₅
```

The □ correction gives:

```
S_eff ⊃ (g_eff² Z / μ⁴)(∂_μ J^μ₅)(□ ∂_ν J^ν₅)
```

This involves DERIVATIVES of the fermion bilinear — a higher-
derivative four-fermion operator. Does this produce a disformal-
like structure?

No: it is a higher-order CONTACT interaction. It modifies the
fermion self-energy at order p²/μ², not the fermion propagation
speed. For μ ~ M_Pl: the correction is p²/M_Pl² — unobservable.

**Verdict: CONFORMAL_ONLY. Integrating out heavy torsion produces
four-fermion contact interactions, not disformal effective metrics.
The interactions are Planck-suppressed and observationally
irrelevant.**

---

## Candidate E: Curvature-Squared Terms → Modified GW Propagation

### Setup

PGT with curvature-squared (Gauss-Bonnet, Weyl-squared) terms:

```
S_E = ∫ d⁴x √g [
    ½M_Pl² R + b₁ R² + b₂ R_μν R^μν + b₃ R_μνρσ R^μνρσ
    + t_i T²
]
```

The R² terms modify the graviton propagator and can produce a
modified GW speed:

```
c²_GW = 1 + O(b_i R / M_Pl²)
```

### Is this disformal?

**MARGINALLY.** Modified GW speed is equivalent to the tensor sector
propagating on a DISFORMAL effective metric:

```
g̃^tensor_μν = g_μν + (c²_GW - 1) u_μ u_ν
```

where u_μ is the cosmological 4-velocity. This IS a disformal
structure (in the ADM sense).

### Is this geometry-specific?

**NO.** Any theory with R² terms — including f(R) gravity, Gauss-
Bonnet, Horndeski with G₄(φ,X), etc. — produces modified GW speed.
The R² terms are NOT specific to PGT or MAG. A scalar-tensor theory
with G₄(φ) produces exactly the same effect.

Furthermore: GW170817 constrains |c_GW - c|/c < 10⁻¹⁵. This has
already eliminated most of Horndeski parameter space (specifically,
G₄(X) and G₅ must vanish at the current epoch). The PGT R² terms
face the same constraint.

### FRW survival

The modified GW speed IS nonzero on FRW (R ≠ 0 in matter/DE era).
So this survives the FRW test.

But: the effect is O(b_i H² / M_Pl²), which is tiny for b_i ~ O(1).
For a measurable effect: need b_i ~ M_Pl²/H² ~ 10¹²⁰. Unnatural.

### Biggest risk

This IS the GW speed constraint territory. Essentially all theories
with modified GW speed have been excluded or severely constrained
by GW170817. PGT is no exception.

**Verdict: GENERIC_DISFORMAL. Modified GW speed from R² terms is
not geometry-specific and is observationally excluded (GW170817)
unless the R² couplings are fine-tuned or the effect is restricted
to the early universe.**

---

## Candidate F: Parity-Odd Geometric Sector → Gravitational Chern-Simons

### Setup

If the PGT 0⁻ pseudoscalar θ couples to the Pontryagin density:

```
S_F ⊃ ∫ d⁴x √g [α θ R_μνρσ R̃^μνρσ]
```

where R̃ is the dual Riemann tensor. This is gravitational Chern-
Simons gravity.

### What it produces

- Amplitude birefringence of GWs (left/right circular polarizations
  have different amplitudes during propagation)
- Velocity birefringence (left/right have different speeds)
- Parity-violating CMB B-mode signatures

### Is this disformal?

**YES, in a spin-dependent sense.** Left and right circular GW
polarizations propagate on DIFFERENT effective metrics:

```
g̃^L_μν ≠ g̃^R_μν
```

This IS beyond conformal scalar-tensor (which treats all polarizations
equally).

### Is this geometry-specific?

**NO.** Gravitational Chern-Simons gravity is a standard framework
studied extensively (Alexander & Yunes 2009, Jackiw & Pi 2003).
ANY pseudoscalar coupled to RR̃ produces this effect — not just PGT
torsion modes. It is the gravitational analog of the axion-photon
coupling θFF̃.

The PGT origin of θ does not constrain the Chern-Simons coupling in
any distinctive way. It is generic ALP + gravity = standard Chern-
Simons gravity.

### FRW survival

On FRW: R̃R = 0 (the Pontryagin density vanishes on FRW due to
conformal flatness). So the Chern-Simons effects only appear in:
- GW propagation (perturbations, not background)
- Primordial GWs (during inflation)

The background cosmological dynamics are unmodified. This is NOT a
dark-energy mechanism — it is a GW propagation effect.

**Verdict: GENERIC_DISFORMAL (parity-violating sector). NOT geometry-
specific. NOT a dark-energy mechanism. Foundation B territory
(generic ALP coupled to gravity).**

---

## Summary

| Candidate | Disformal? | Geometry-specific? | FRW? | Verdict |
|-----------|------------|-------------------|------|---------|
| A: 0⁻ fermion coupling | No (gauge-like) | No (generic ALP) | ALP birefringence | CONFORMAL_ONLY |
| B: 0⁺ fermion coupling | No (removable) | N/A | N/A | NO EFFECT |
| C: Non-metricity fermion | N/A (decouples) | N/A | N/A | NULL |
| D: Heavy torsion → EFT | No (contact) | No (standard EC) | Contact term | CONFORMAL_ONLY |
| E: R² → GW speed | Marginally | No (any R² theory) | Constrained | GENERIC_DISFORMAL |
| F: Chern-Simons | Spin-dependent | No (any ALP+grav) | Perturbations only | GENERIC_DISFORMAL |

**No candidate produces a geometry-specific disformal effective
metric that survives on FRW and goes beyond known frameworks.**
