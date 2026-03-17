# Phase 2B — Shift Symmetry Analysis for the 0- Axial Torsion Mode

**Date:** 2026-03-13
**Status:** Original analysis

---

## 1. The Shift Symmetry Idea

For a pseudoscalar ALP phi, the shift symmetry phi -> phi + c forbids
the mass term (1/2) m^2 phi^2, making the massless limit technically
natural. The mass can only arise from shift-symmetry-breaking effects,
which can be parametrically small.

Can the axial torsion vector A_mu enjoy an analogous symmetry?

---

## 2. Attempt: A_mu -> A_mu + c_mu

Consider the constant shift A_mu -> A_mu + c_mu for constant c_mu.

### Problem 1: This is not a gauge symmetry

For a massless vector, the relevant symmetry is gauge invariance
A_mu -> A_mu + partial_mu alpha, not a constant shift. A constant shift
is a special case of a gauge transformation (with alpha = c_mu x^mu),
but the full gauge symmetry is what protects the mass.

### Problem 2: The PGT origin prevents gauge invariance

The axial vector A_mu = (1/6) epsilon_{mu nu rho sigma} T^{nu rho sigma}
is constructed from the torsion tensor. Torsion is the antisymmetric
part of the connection:

```
T^lambda_{mu nu} = Gamma^lambda_{mu nu} - Gamma^lambda_{nu mu}
```

A gauge transformation A_mu -> A_mu + partial_mu alpha would require
a corresponding transformation of the connection that shifts torsion
by a pure gauge piece. But in PGT, the connection transforms under
local Lorentz transformations, not U(1) gauge transformations. There
is no subgroup of the local Lorentz group that acts as a U(1) on A_mu.

**Conclusion: The U(1) gauge symmetry that would protect a vector mass
is not available within PGT.**

### Problem 3: Even a constant shift is broken

The torsion-squared term A_mu A^mu in the action is not invariant
under A_mu -> A_mu + c_mu. The kinetic structure (which comes from
the curvature scalar when expanded in the full connection) is also
not invariant. The shift symmetry is broken by every term in the
Lagrangian.

---

## 3. Attempt: Pseudoscalar Shift Symmetry

Extract the pseudoscalar degree of freedom. In unitary gauge, the
massive vector A_mu contains a longitudinal mode that can be written as:

```
A_mu^(long) = partial_mu phi / m_B
```

where phi is the physical pseudoscalar. Can phi -> phi + c protect
the mass?

### Problem: The decomposition itself depends on m_B

The identification of phi as the longitudinal mode uses the mass.
Setting m_B = 0 changes the field content (3 DOF -> 2 DOF for a
massless vector in 4D without gauge symmetry — but a massless vector
without gauge symmetry has 3 DOF, not 2). The Stückelberg trick:

```
A_mu -> A_mu + partial_mu pi / m_B
```

with pi the Goldstone boson, formally allows m_B -> 0 if one gives pi
a shift symmetry. But this requires introducing pi as an independent
field, which takes us outside the PGT framework.

**Within PGT, there is no independent Goldstone boson.** The
longitudinal mode of A_mu is part of the torsion, which is part of
the connection. Its shift symmetry would have to be a symmetry of the
connection — which brings us back to the gauge symmetry obstruction.

---

## 4. Attempt: Conformal / Weyl Symmetry

In conformal gravity, mass terms are forbidden by the Weyl symmetry
g_{mu nu} -> Omega^2 g_{mu nu}. Can a conformal extension of PGT
protect m_B = 0?

### Analysis

Conformal PGT (also called Weyl-Cartan geometry) has been studied by
several groups (Blagojevic & Hehl 2013, Obukhov 2006). The conformal
extension of the Poincaré group is the Weyl group, which adds
dilatations. In conformal PGT:

1. The Einstein-Hilbert term R is not conformally invariant. Only R^2
   and Weyl-tensor-squared terms are allowed.
2. The torsion-squared term T^2 is not conformally invariant. Only
   specific combinations with appropriate conformal weights survive.
3. Mass terms for torsion modes are forbidden by conformal invariance.

This looks promising — but there is a fatal issue:

**Conformal invariance also forbids the Einstein-Hilbert term.** To
recover GR at low energies, conformal symmetry must be broken
(spontaneously or explicitly). Once broken, mass terms are generically
regenerated. The mass protection is only as good as the conformal
symmetry breaking mechanism.

If conformal symmetry is broken at scale v_c, the generated mass is:

```
m_B ~ v_c^2 / M_Pl (parametrically)
```

To get m_B ~ meV, one needs v_c ~ 10^7 GeV. This is an intermediate
scale — not obviously natural, but much better than |t_3| ~ 10^58.

**Status: CONCEIVABLE but requires a full conformal PGT model with
a controlled breaking mechanism, which does not currently exist.**

---

## 5. Attempt: Chiral Symmetry Protection

The axial torsion couples to the fermion axial current J^mu_5. If the
matter sector has an exact chiral symmetry, the axial coupling structure
is protected.

### Problem: Chiral symmetry does not protect the torsion mass

Chiral symmetry acts on fermions, not on the connection. It constrains
the COUPLING structure (axial vs. vector) but not the MASS of the
torsion field. The torsion mass comes from the torsion-squared term in
the PGT action, which involves only the connection — no fermions.

A chiral rotation psi -> exp(i alpha gamma_5) psi leaves the torsion
sector untouched. The torsion mass is not a fermion bilinear and is not
protected by fermion symmetries.

**Conclusion: Chiral symmetry is irrelevant to the torsion mass.**

---

## 6. Attempt: Topological Protection

The Holst term is topological in the absence of torsion (it reduces to
the Nieh-Yan invariant, a total derivative). Could the 0- mode inherit
topological protection?

### Analysis

The Nieh-Yan invariant is:

```
N_NY = d(e^a wedge T_a) = T^a wedge T_a - R_{ab} wedge e^a wedge e^b
```

This is a topological invariant — its integral depends only on boundary
conditions. If the 0- torsion mode could be identified with the
fluctuation of a topological quantity, its mass might be protected.

However:

1. The Nieh-Yan density is a 4-form, not a field. It does not have a
   mass.
2. The 0- axial torsion A_mu is a component of T^{lambda}_{mu nu},
   not a topological invariant.
3. The connection between the Holst term and the axial torsion mass
   is indirect: the Holst term contributes to the equation of motion
   for torsion, but it does not provide a topological protection for
   the torsion mass parameter.

**Conclusion: No topological protection mechanism is available.**

---

## 7. Attempt: Supersymmetric Extension

In SUSY gauge theories, the mass of the gauge boson is related to the
SUSY-breaking scale by non-renormalization theorems. Could SUSY PGT
protect m_B?

### Assessment

Supergravity (SUGRA) is the SUSY extension of GR. PGT supergravity
exists (van Nieuwenhuizen 1981, Freedman & van Proeyen 2012) but:

1. The torsion in SUGRA is algebraic (determined by the gravitino
   bilinear) — it does NOT propagate. This is the same algebraic-torsion
   wash-out that motivated Foundation A in the first place.
2. Extended SUGRA with propagating torsion requires additional matter
   multiplets, which takes us far beyond minimal PGT.
3. SUSY is broken in nature. Unless the breaking scale is below the
   torsion mass, SUSY non-renormalization does not help.

**Conclusion: SUSY does not provide a practical protection mechanism
for the PGT torsion mass.**

---

## 8. Radiative Stability Check

Even without a symmetry, we should check: what is the 1-loop radiative
correction to m_B^2?

### Graviton loop

The leading correction from graviton loops:

```
delta m_B^2 ~ kappa^2 Lambda_UV^2 / (16 pi^2) ~ Lambda_UV^2 / (16 pi^2 M_Pl^2) * Lambda_UV^2
```

With Lambda_UV = M_Pl:

```
delta m_B^2 ~ M_Pl^2 / (16 pi^2) ~ (10^{17} GeV)^2
```

This is the standard gravitational contribution to scalar/vector masses.
It makes any mass m_B << M_Pl technically unnatural unless a symmetry
protects it.

### Fermion loop

The fermion loop correction:

```
delta m_B^2 ~ g_eff^2 Lambda_UV^2 / (16 pi^2) ~ Lambda_UV^2 / (16 pi^2 M_Pl^2 |t_3|)
```

With Lambda_UV = M_Pl:

```
delta m_B^2 ~ M_Pl^2 / (16 pi^2 |t_3|) ~ m_B^2 / (16 pi^2)
```

This is proportional to m_B^2 — it does NOT destabilize the mass! But
this is the fermion loop only. The graviton loop dominates and DOES
destabilize the mass.

### Summary of radiative stability

```
delta m_B^2 = M_Pl^2/(16 pi^2) [graviton] + m_B^2/(16 pi^2) [fermion] + ...
```

The graviton loop generates delta m_B^2 ~ (10^{17} GeV)^2 regardless
of the tree-level mass. To maintain m_B ~ meV requires canceling this
correction to 1 part in 10^{62}. This is the standard hierarchy problem,
identical to the Higgs mass problem but 10^{30} times worse.

**The torsion mass is NOT radiatively stable.**

---

## 9. Summary

| Symmetry candidate | Protects m_B? | Status |
|-------------------|--------------|--------|
| U(1) gauge (A -> A + d alpha) | Yes, in principle | NOT AVAILABLE in PGT |
| Constant shift (A -> A + c) | Partially | BROKEN by all Lagrangian terms |
| Pseudoscalar shift (phi -> phi + c) | Yes, for scalars | NOT APPLICABLE (no independent Goldstone) |
| Conformal / Weyl | Yes, forbids all masses | CONCEIVABLE but requires controlled breaking |
| Chiral symmetry | No | IRRELEVANT to torsion mass |
| Topological protection | Possible for topological quantities | NOT APPLICABLE to A_mu mass |
| Supersymmetry | Yes, via non-renormalization | NOT PRACTICAL (torsion is algebraic in SUGRA) |

**No known symmetry of PGT protects the axial torsion mass.**

The only conceivable mechanism (conformal PGT) requires building a full
model that does not currently exist, with a controlled symmetry-breaking
pattern. This is a research program in itself, not a quick calculation.
