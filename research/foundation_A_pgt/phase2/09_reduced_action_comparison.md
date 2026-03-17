# Phase 2B — Reduced Action: Does Model B Reduce to a Generic Pseudoscalar?

**Date:** 2026-03-13
**Status:** Original analysis

---

## 1. The Question

After integrating out all non-propagating fields (non-dynamical connection
components, auxiliary fields), does the 0- axial torsion mode retain any
non-generic structure that distinguishes it from GR + a free massive
pseudoscalar (i.e., an ALP)?

This is the reduced-action version of Phase 1's "closure lesson L3":
dynamical gamma reduces to ALP. Does dynamical torsion reduce to ALP?

---

## 2. The Reduction Procedure

Start with the full PGT Lagrangian restricted to Model B:

```
L = (1/2kappa^2)(-R(Gamma) + 6|t_3| A_mu A^mu) + L_Dirac(psi, Gamma)
```

where R(Gamma) is the curvature of the full (torsion-including) connection
Gamma, and A_mu is the axial torsion vector.

### Step 1: Decompose the connection

```
Gamma^lambda_{mu nu} = {lambda, mu nu} + K^lambda_{mu nu}
```

where {lambda, mu nu} is the Levi-Civita connection and K is the contortion.
For Model B (only axial torsion), the contortion is:

```
K^lambda_{mu nu} = -epsilon^lambda_{mu nu rho} A^rho
```

### Step 2: Expand the curvature

```
R(Gamma) = R({}) + nabla_mu V^mu + Q(K, K)
```

where R({}) is the Riemannian curvature, nabla is the Levi-Civita
covariant derivative, V^mu is a vector built from K, and Q is quadratic
in K.

For the axial torsion mode:

```
Q(K, K) = -6 A_mu A^mu + (terms involving partial_mu A_nu)
```

The kinetic term for A_mu comes from the Q(K,K) piece.

### Step 3: Write the reduced action

After collecting terms (and dropping total derivatives):

```
L_reduced = (1/2kappa^2)(-R({}))
          + (alpha_kin/2) F_{mu nu}(A) F^{mu nu}(A)
          - (1/2) m_B^2 A_mu A^mu
          + kappa A_mu J_5^mu(psi)
          + gravitational couplings
```

where:
- alpha_kin is a kinetic normalization depending on |t_3|
- F_{mu nu}(A) = partial_mu A_nu - partial_nu A_mu
- m_B^2 = M_Pl^2 / (16 pi |t_3|)

---

## 3. What Structure Survives?

### 3a. Kinetic structure: Proca, not ALP

The reduced action for A_mu is a **massive Proca field**, not a
pseudoscalar ALP. The difference:

- ALP: L = -(1/2)(partial phi)^2 - (1/2) m^2 phi^2 - (phi/f) F_em F~_em
  - 1 propagating DOF (scalar)
  - Couples to F F~ (topological density)

- Model B: L = -(1/4) F^2(A) - (1/2) m^2 A^2 + g_eff A_mu J_5^mu
  - 3 propagating DOF (massive vector = 2 transverse + 1 longitudinal)
  - Couples to axial current J_5^mu

The longitudinal mode of A_mu is a pseudoscalar, but the two transverse
modes are additional DOF not present in an ALP.

**Model B does NOT reduce to GR + ALP.** It reduces to GR + massive
Proca pseudovector.

### 3b. Coupling structure: axial current, not F F~

The coupling is to the fermion axial current J_5^mu, not to the photon
topological density F F~. This is a physically different interaction:

- ALP-photon coupling produces birefringence through photon propagation
  modification
- A_mu - J_5^mu coupling produces spin-dependent forces through
  fermion interactions

These are distinct observational channels with different signatures.

### 3c. Parity structure: pseudovector, not pseudoscalar

A_mu transforms as a pseudovector (axial vector) under parity. A
pseudoscalar ALP transforms as P: phi -> -phi. The parity structures
in cosmological perturbation theory are different:

- Pseudoscalar: generates E-B mixing in CMB through scalar perturbations
- Pseudovector: generates both E-B mixing AND vector perturbation modes

The vector perturbations from A_mu are a geometrically distinct
contribution not available from a pseudoscalar.

---

## 4. What Does NOT Survive Reduction

### 4a. The geometric origin is erased

After reduction, A_mu is just a massive vector field minimally coupled
to gravity and axialy coupled to fermions. The fact that it originated
from the spin connection (torsion) is invisible in the reduced action.
There is no term in L_reduced that "knows" A_mu came from geometry.

This means:
- Any massive Proca field with the same mass and coupling is
  indistinguishable from Model B
- The "geometric dark energy" label is a property of the UV action,
  not of the IR physics
- No observation at energies E << M_Pl can determine whether A_mu is
  torsion or a fundamental Proca field

### 4b. The connection to the Barbero-Immirzi parameter is lost

In ECH gravity, the axial torsion coupling was related to the
Barbero-Immirzi parameter gamma. In PGT Model B, the coupling is
|t_3|. After reduction, there is no gamma anywhere in the action.
The PGT framework has its own parameterization, disconnected from
the ECH structure.

### 4c. No non-minimal gravitational couplings survive at leading order

The torsion-gravity coupling (through the curvature expansion) produces
corrections to the graviton-A_mu vertex at order kappa^2. These are
gravitationally suppressed and observationally irrelevant — they are
the same order as graviton-graviton-A vertices that any minimally
coupled field would have.

---

## 5. The Honest Assessment

Model B retains three features that distinguish it from an ALP:

1. **It is a vector, not a scalar** (3 DOF vs 1 DOF)
2. **It couples to J_5^mu, not F F~** (different interaction channel)
3. **It produces vector perturbations** (geometrically distinct CMB pattern)

But it loses:
1. **Any trace of geometric origin** (torsion vs fundamental is invisible)
2. **Connection to Barbero-Immirzi** (ECH parameter is absent)
3. **Non-generic gravitational coupling** (same as any massive field)

And the critical finding from Phase 2A:
4. **All distinctive couplings are suppressed by 1/sqrt(|t_3|)** at the
   parameter values needed for cosmological mass

---

## 6. Does This Close Foundation A?

**Not completely.** The reduced action is genuinely different from GR + ALP:
it is GR + massive Proca pseudovector. This is a larger theory with
different phenomenology. The distinction matters at |t_3| = O(1) where
the coupling is gravitational strength.

But at |t_3| >> 1 (cosmologically light mass), the distinction is
unobservable because all couplings are suppressed. The theory is
distinguishable in principle (different Lagrangian) but indistinguishable
in practice (same observational predictions: none).

**The reduced action comparison reinforces the Phase 2A finding: Model B
is structurally richer than an ALP but operationally equivalent to
generic quintessence at the parameter values needed for dark energy.**
