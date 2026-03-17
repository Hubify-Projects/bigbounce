# 01 — General Quadratic Poincare Gauge Theory Action

**Date:** 2026-03-13
**Purpose:** Define the complete quadratic PGT action including all torsion and curvature terms, establishing notation for the Foundation A test program.
**Status:** Reference document (literature compilation, not new derivation)

---

## 1. Gauge Structure

Poincare gauge theory (PGT) gauges the full Poincare group ISO(1,3) = SO(1,3) x T(1,3). The gauge fields are:

- **Tetrad (coframe):** e^I_mu — gauges translations T(1,3)
- **Lorentz connection:** omega^{IJ}_mu — gauges Lorentz rotations SO(1,3)

Both are independent dynamical variables. This is the critical difference from Einstein-Cartan theory, where the connection equation of motion is algebraic (non-propagating torsion). In PGT, the connection has its own kinetic term, so torsion propagates.

The field strengths are:

- **Torsion:** T^I_{mu nu} = partial_mu e^I_nu - partial_nu e^I_mu + omega^I_{J mu} e^J_nu - omega^I_{J nu} e^J_mu
- **Curvature:** R^{IJ}_{mu nu} = partial_mu omega^{IJ}_nu - partial_nu omega^{IJ}_mu + omega^I_{K mu} omega^{KJ}_nu - omega^I_{K nu} omega^{KJ}_mu

Convention: I, J, K = 0,1,2,3 are Lorentz (internal) indices; mu, nu = 0,1,2,3 are spacetime indices.

---

## 2. Irreducible Decomposition of Torsion

The torsion tensor T^I_{mu nu} (24 independent components in 4D) decomposes into three irreducible pieces under the Lorentz group:

### (1) Tensor (hook) torsion: ^(1)T — 16 components
The traceless part with mixed symmetry.

### (2) Vector (trace) torsion: ^(2)T — 4 components
The trace: V_mu = T^nu_{mu nu} (the "vector" or "trace" piece).

### (3) Axial-vector torsion: ^(3)T — 4 components
The totally antisymmetric part: A_mu = (1/6) epsilon_{mu nu rho sigma} T^{nu rho sigma}.

Total: 16 + 4 + 4 = 24.

In index notation:
```
T_{lambda mu nu} = ^(1)T_{lambda mu nu} + ^(2)T_{lambda mu nu} + ^(3)T_{lambda mu nu}
```
where:
- ^(2)T_{lambda mu nu} = (1/3)(g_{lambda mu} V_nu - g_{lambda nu} V_mu)
- ^(3)T_{lambda mu nu} = epsilon_{lambda mu nu rho} A^rho
- ^(1)T is the remainder (traceless, no totally antisymmetric part)

**Reference:** Hayashi & Shirafuji (1979), Hehl et al. (1995).

---

## 3. Irreducible Decomposition of Curvature

The curvature R^{IJ}_{mu nu} (36 independent components) decomposes into six irreducible pieces under the Lorentz group. Following the notation of Hayashi & Shirafuji and Blagojevic & Hehl:

### Parity-even curvature invariants (3):
- W: Weyl-like (traceless part)
- R: Ricci-like (trace part, symmetric)
- S: Scalar curvature piece

### Parity-odd curvature invariants (3):
- *W: Dual of Weyl-like
- *R: Dual of Ricci-like
- *S: Dual of scalar

For the purposes of this document, the precise decomposition matters mainly through the quadratic invariants it generates. See Section 4.

---

## 4. The General Quadratic PGT Lagrangian

The most general PGT Lagrangian quadratic in torsion and curvature, up to parity-odd terms, is:

```
L_PGT = L_EC + L_T^2 + L_R^2
```

where:

### (a) Einstein-Cartan piece (dimension 2):
```
L_EC = (1/2kappa^2) * (- a_0 R + 2 Lambda_0)
```
with R the Ricci scalar of the full connection (includes torsion contributions), kappa^2 = 8 pi G, and Lambda_0 a bare cosmological constant. We set a_0 = 1 by convention (canonically normalized graviton).

### (b) Torsion-squared piece (dimension 2):
```
L_T^2 = (1/2kappa^2) * sum_{I=1}^{3} t_I * ^(I)T_{lambda mu nu} ^(I)T^{lambda mu nu}
```

Three independent coupling constants: **t_1, t_2, t_3**

Explicitly:
- t_1 terms: ^(1)T . ^(1)T (tensor torsion squared)
- t_2 terms: ^(2)T . ^(2)T = (2/3) V_mu V^mu (vector torsion squared)
- t_3 terms: ^(3)T . ^(3)T = -6 A_mu A^mu (axial torsion squared)

Note the conventional numerical factors. Different authors use different normalizations. We follow Hayashi-Shirafuji (1979) conventions as standardized in Blagojevic & Hehl (2013).

### (c) Curvature-squared piece (dimension 0 couplings x dimension 4):
```
L_R^2 = (1/2) * sum_{I=1}^{6} r_I * (curvature invariant)_I
```

Six independent coupling constants: **r_1, ..., r_6**

These couple to the six irreducible quadratic curvature invariants:
- r_1: R_{mu nu rho sigma} R^{mu nu rho sigma} (Kretschner-like)
- r_2: R_{mu nu} R^{mu nu} (Ricci-squared, symmetric)
- r_3: R^2 (scalar curvature squared)
- r_4: epsilon^{mu nu rho sigma} R_{alpha beta mu nu} R^{alpha beta}_{rho sigma} (parity-odd Gauss-Bonnet dual)
- r_5: epsilon^{mu nu rho sigma} R_{alpha mu rho nu} R^{alpha}_{sigma} (parity-odd Ricci)
- r_6: (parity-odd scalar, related to Pontryagin/Nieh-Yan)

**Note:** The curvature here is of the full Lorentz connection (including torsion), NOT the Levi-Civita curvature.

### Total parameter count

| Parameter | Physical role | Dimension |
|-----------|--------------|-----------|
| a_0 | Einstein-Hilbert normalization | fixed = 1 |
| Lambda_0 | Bare cosmological constant | mass^2 |
| t_1, t_2, t_3 | Torsion-squared couplings | dimensionless |
| r_1, ..., r_6 | Curvature-squared couplings | mass^{-2} |

**Total free parameters in quadratic PGT: 3 (torsion) + 6 (curvature) + 1 (Lambda_0) = 10.**

This is the "10-parameter landscape" referenced in the model reconsideration memo.

---

## 5. Relation to Minimal ECH (Our Closed Model)

The minimal Einstein-Cartan-Holst action corresponds to:

```
t_1 = t_2 = t_3 = 0    (no explicit torsion kinetic terms)
r_1 = r_2 = r_3 = r_4 = r_5 = r_6 = 0    (no curvature-squared terms)
```

plus the Holst term (1/gamma) epsilon^{IJKL} e_I wedge e_J wedge R_{KL}, which is parity-odd and equivalent to a specific linear combination of curvature invariants when reduced to component form.

In this limit, the connection equation of motion is algebraic: torsion = (algebraic function of spin density). Torsion does not propagate. This is the structural reason for Lesson 1 (algebraic torsion washes out).

**Foundation A asks: what happens when we turn on t_I and/or r_I?**

When t_I != 0, the torsion equation of motion acquires second-derivative terms — torsion becomes dynamical. When r_I != 0, the curvature-squared terms give the connection its own propagator. Either way, torsion propagates.

---

## 6. Linearization Strategy

To study the spectrum, we linearize around Minkowski spacetime:
```
e^I_mu = delta^I_mu + h^I_mu
omega^{IJ}_mu = 0 + omega^{IJ}_mu (perturbation)
```

The linearized field equations decompose into sectors labeled by the spin and parity of the torsion modes. The key question is which sectors have:
- Correct sign kinetic terms (no ghosts)
- Non-negative mass-squared (no tachyons)
- Finite, well-defined propagators (no higher-derivative pathologies)

This analysis is carried out in documents 02-04.

---

## Key References

1. Hayashi, K. & Shirafuji, T. (1979). "New general relativity." Phys. Rev. D 19, 3524.
2. Sezgin, E. & van Nieuwenhuizen, P. (1980). "New ghost-free gravity Lagrangians with propagating torsion." Phys. Rev. D 21, 3269.
3. Hehl, F.W. et al. (1995). "Metric-affine gauge theory of gravity." Phys. Rept. 258, 1.
4. Yo, H.-J. & Nester, J.M. (1999). "Hamiltonian analysis of Poincare gauge theory." Int. J. Mod. Phys. D 8, 459.
5. Yo, H.-J. & Nester, J.M. (2002). "Hamiltonian analysis of Poincare gauge theory: higher spin modes." Int. J. Mod. Phys. D 11, 747.
6. Nikiforova, V., Randjbar-Daemi, S. & Rubakov, V. (2009). "Infrared modified gravity with propagating torsion." Phys. Rev. D 80, 124050.
7. Karananas, G.K. (2015). "Poincare gauge theory: unitarity, stability, and fundamental interactions." Phys. Rev. D 91, 084054.
8. Blagojevic, M. & Hehl, F.W. (2013). "Gauge Theories of Gravitation." Imperial College Press.
9. Blagojevic, M. & Cvetkovic, B. (2018). "General Poincare gauge theory: Hamiltonian approach and particle spectrum." Phys. Rev. D 98, 104018.
10. Lin, Y.-C., Hobson, M.P. & Sherrill, A.N. (2019). "Ghost and tachyon free Poincare gauge theories." Phys. Rev. D 99, 064001.
