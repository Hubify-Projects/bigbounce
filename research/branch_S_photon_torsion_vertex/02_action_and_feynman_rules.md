# Branch S: Action and Feynman Rules

**Date:** 2026-03-16

---

## 1. The Microscopic Action

The full Einstein-Cartan-Holst action with Dirac fermions and photons:

```
S = S_grav + S_fermion + S_photon
```

### Gravitational sector

```
S_grav = (1/2kappa) integral [e^I ^ e^J ^ (F_IJ + (1/2gamma) epsilon_IJ^{KL} F_{KL})]
```

where:
- kappa = 8 pi G = 1/M_Pl^2
- gamma = Barbero-Immirzi parameter
- e^I = vierbein one-form
- F_IJ = curvature two-form of the spin connection omega^{IJ}

### Fermion sector

```
S_fermion = integral d^4x |e| [i psi-bar gamma^mu D_mu(omega) psi - m psi-bar psi]
```

where the covariant derivative on spinors is:

```
D_mu(omega) psi = partial_mu psi + (1/4) omega^{IJ}_mu sigma_{IJ} psi
```

with sigma_{IJ} = (1/2)[gamma_I, gamma_J].

### Photon sector

```
S_photon = -(1/4) integral d^4x |e| g^{mu alpha} g^{nu beta} F_{mu nu} F_{alpha beta}
```

where F_{mu nu} = partial_mu A_nu - partial_nu A_mu is the standard
U(1) field strength. Photons couple to gravity through the metric/vierbein
ONLY. There is NO direct photon-torsion coupling.

---

## 2. Decomposing the Spin Connection

The full spin connection decomposes as:

```
omega^{IJ}_mu = omega-ring^{IJ}_mu + K^{IJ}_mu
```

where omega-ring is the torsion-free (Levi-Civita) connection and
K is the contortion tensor:

```
K^{IJ}_mu = (1/2)(T^I_{mu}^J - T^J_{mu}^I - T_{mu}^{IJ})
```

---

## 3. Torsion Equation of Motion

Varying the action with respect to the connection gives the torsion
equation. In ECH gravity with Dirac fermions, the totally antisymmetric
part of torsion (the axial torsion) is:

```
S_mu = (1/6) epsilon_{mu nu rho sigma} T^{nu rho sigma}
```

The equation of motion for S_mu (including the Holst term) is:

```
S_mu = -(kappa/4) * (gamma^2 / (1 + gamma^2)) * J^5_mu
```

where J^5_mu = psi-bar gamma_mu gamma_5 psi is the fermion axial current.

Note the gamma-dependent prefactor: gamma^2/(1 + gamma^2). In the limit
gamma -> infinity (no Holst term), this becomes 1. For finite gamma,
the coupling is modified.

The trace and tensor parts of torsion are zero for Dirac fermions
(they couple only through the axial current).

---

## 4. The Contortion-Fermion Vertex

### Before torsion elimination

The fermion-contortion interaction comes from expanding D_mu(omega):

```
L_{int} = (1/4) K^{IJ}_mu psi-bar sigma_{IJ} gamma^mu psi
```

For axial torsion (the only nonzero component), the contortion takes
the form:

```
K^{IJ}_mu = epsilon^{IJ}_{KL} S^K e^L_mu  (+ permutations)
```

Working out the spinor algebra:

```
(1/4) K^{IJ}_mu sigma_{IJ} = (3/2) S_mu gamma_5
```

Wait -- let me be more careful. The axial torsion vector S_mu
contributes to the contortion as:

```
K_{mu nu rho} = -2 (g_{mu[nu} S_{rho]} + epsilon_{mu nu rho sigma} S^sigma)
```

The coupling to the fermion is:

```
L_{K-psi} = -(3/2) S_mu psi-bar gamma^mu gamma_5 psi = -(3/2) S_mu J^{5 mu}
```

This is an AXIAL VECTOR coupling of the torsion to the fermion.

### The vertex in momentum space

```
Vertex (S-psi-psi): V^mu = -i(3/2) gamma^mu gamma_5
```

This is exactly the structure of an axial vector current insertion.
The coupling constant is g_axial = 3/2 (in units where kappa = 1).

### Restoring dimensions

The axial torsion S_mu has dimensions [mass], and the coupling to
fermions in the full action is:

```
L_{S-psi} = -(3/2) S_mu * psi-bar gamma^mu gamma_5 psi
```

This is already dimensionless (S has mass dimension 1, fermion bilinear
has mass dimension 3, and the Lagrangian has mass dimension 4, so
with the d^4x measure this works). The vertex factor is:

```
V^mu_{axial-torsion} = -i (3/2) gamma^mu gamma_5
```

---

## 5. The QED Vertex

Standard:

```
V^mu_{QED} = -i e gamma^mu
```

where e is the electromagnetic coupling (e^2 = 4 pi alpha_EM).

---

## 6. After Torsion Elimination

Substituting S_mu = -(kappa/4)(gamma^2/(1+gamma^2)) J^5_mu back into
the action gives the effective four-fermion interaction:

```
L_4f = (3 kappa / 32) * (gamma^2 / (1 + gamma^2)) * (J^5_mu)^2
```

The standard result in the literature (Hehl et al., de Sabbata-Gasperini)
uses the coefficient:

```
G_torsion = (3 kappa) / (16) * C(gamma)
```

where C(gamma) = gamma^2 / (1 + gamma^2) for the Holst action.

Note: some references use a different convention. The key point is that
C(gamma) -> 1 as gamma -> infinity, and C(gamma) -> 0 as gamma -> 0.
For the LQG value gamma ~ 0.274: C(gamma) = 0.274^2/(1+0.274^2) = 0.070.

### The effective four-fermion vertex

In the reduced (torsion-eliminated) theory, the four-fermion vertex is:

```
V_{4f} = i G_torsion (gamma^mu gamma_5) x (gamma_mu gamma_5)
```

This is an NJL-type (Nambu-Jona-Lasinio) axial-axial current-current
interaction. The gamma dependence enters ONLY through G_torsion.

---

## 7. Two Formulations of the Problem

### Formulation A: Before torsion elimination

External torsion background S_mu, fermion loop with:
- 2 photon vertices (QED, vector)
- 1 torsion vertex (axial)

This is the ABJ triangle.

### Formulation B: After torsion elimination

No external torsion. The four-fermion interaction (J^5)^2 is present.
Fermion loops with:
- 2 photon vertices
- 1 or more (J^5)^2 insertions

This generates operators with external fermion legs (not pure photon).

### Critical observation

Formulation A treats S_mu as an EXTERNAL background field. The triangle
diagram then gives an effective operator S_mu F F-tilde.

Formulation B treats torsion as already eliminated. There is no external
S_mu; the four-fermion interaction is the ONLY non-standard term.

These formulations MUST give the same physical answer. The resolution
is that in Formulation A, S_mu is not an independent field — it is
constrained to equal S_mu ~ J^5_mu. So the "external" S_mu is really
a fermion bilinear, and the triangle with an "external" S_mu line is
really a diagram with two additional fermion legs.

This distinction is CRUCIAL for cosmology: there is no "vacuum torsion"
to source birefringence. The torsion is always proportional to the
spin density of matter.

---

## 8. Summary of Vertices and Couplings

| Vertex | Coupling | Structure | Gamma-dependent? |
|--------|----------|-----------|------------------|
| QED (psi-A-psi) | e | gamma^mu | NO |
| Axial torsion (psi-S-psi) | 3/2 | gamma^mu gamma_5 | NO (coupling is fixed) |
| Torsion EOM (S = f(J^5)) | kappa/4 * C(gamma) | S = -const * J^5 | YES |
| Four-fermion (J^5)^2 | G_torsion | (gamma^mu gamma_5)^2 | YES (through G_torsion) |
| Photon-torsion (direct) | 0 | — | — |

The gamma-dependence enters ONLY through the constraint equation
S = -(kappa/4) C(gamma) J^5, which sets the coefficient of the
four-fermion interaction.
