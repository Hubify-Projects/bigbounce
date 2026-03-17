# Full Action: ECH with Dynamical Barbero-Immirzi Field

**Date:** 2026-03-16

---

## Conventions

- Spacetime indices: mu, nu, rho, sigma = 0,1,2,3
- Internal Lorentz indices: I, J, K, L = 0,1,2,3
- Tetrad: e^I_mu, with g_{mu nu} = eta_{IJ} e^I_mu e^J_nu
- Lorentz connection: omega^{IJ}_mu (independent variable in first-order formalism)
- Curvature 2-form: F^{IJ} = d omega^{IJ} + omega^I_K wedge omega^{KJ}
- Torsion 2-form: T^I = de^I + omega^I_J wedge e^J
- kappa = 8 pi G = 1/M_Pl^2
- Levi-Civita symbol: epsilon_{IJKL} with epsilon_{0123} = +1
- Dual: *F_{IJ} = (1/2) epsilon_{IJKL} F^{KL}

---

## The Gravitational Action

The first-order Palatini-Holst action with dynamical gamma(x):

```
S_grav = (1/4 kappa) integral epsilon_{IJKL} e^I wedge e^J wedge F^{KL}
       + (1/2 kappa gamma(x)) integral e^I wedge e^J wedge F_{IJ}
```

In component form:

```
S_grav = (1/2 kappa) integral d^4x |e| [e^mu_I e^nu_J F^{IJ}_{mu nu}
       + (1/gamma(x)) e^mu_I e^nu_J (*F)^{IJ}_{mu nu}]
```

where (*F)^{IJ}_{mu nu} = (1/2) epsilon^{IJ}_{KL} F^{KL}_{mu nu}.

The first term is the standard Palatini (Einstein-Cartan) action.
The second term is the Holst term, weighted by 1/gamma(x).

### How gamma(x) enters

```
gamma(x) = gamma_0 + phi(x) / f_phi
```

where gamma_0 is the background Immirzi parameter (real, nonzero), phi(x) is
the pseudoscalar Immirzi field, and f_phi is the decay constant (~ M_Pl).

The Holst term becomes:

```
S_Holst = (1/2 kappa) integral d^4x |e| [1/(gamma_0 + phi/f_phi)] e^mu_I e^nu_J (*F)^{IJ}_{mu nu}
```

---

## The Scalar Sector

The kinetic term for phi:

```
S_phi = integral d^4x sqrt(-g) [(1/2) g^{mu nu} partial_mu phi partial_nu phi - V(phi)]
```

V(phi) must be supplied externally (e.g., from non-perturbative effects).
The ECH framework does not generate V(phi).

---

## The Dirac Action

Fermions couple to the FULL connection (including torsion):

```
S_Dirac = integral d^4x |e| psibar [i gamma^mu (partial_mu + (1/4) omega^{IJ}_mu sigma_{IJ}) - m] psi
```

where sigma_{IJ} = (i/2)[gamma_I, gamma_J] are the Lorentz generators, and
gamma^mu = e^mu_I gamma^I with gamma^I the flat-space Dirac matrices.

### Connection decomposition

```
omega^{IJ}_mu = omega-ring^{IJ}_mu + K^{IJ}_mu
```

where omega-ring is the torsion-free Levi-Civita spin connection (determined
by the tetrad) and K^{IJ}_mu is the contortion tensor:

```
K^I_{mu nu} = (1/2)(T^I_{mu nu} - T_{mu}^{I}_{nu} + T_{nu}^{I}_{mu})
```

with T^I_{mu nu} = partial_mu e^I_nu - partial_nu e^I_mu + omega^I_{J mu} e^J_nu - omega^I_{J nu} e^J_mu.

The Dirac action thus splits:

```
S_Dirac = S_Dirac^{LC} + S_Dirac^{torsion}
```

where S_Dirac^{LC} uses only the Levi-Civita connection, and:

```
S_Dirac^{torsion} = integral d^4x |e| (i/4) K^{IJ}_mu psibar gamma^mu sigma_{IJ} psi
```

Using the identity gamma^mu sigma_{IJ} = ... and the irreducible decomposition
of torsion (vector, axial, tensor parts), the axial torsion a_mu couples as:

```
S_Dirac^{torsion} superset (3/4) integral d^4x |e| a_mu psibar gamma^mu gamma_5 psi
```

where a_mu = (1/3!) epsilon_{mu nu rho sigma} T^{nu rho sigma} is the axial
component of torsion.

---

## The Maxwell Action

```
S_Maxwell = -(1/4) integral d^4x sqrt(-g) F_{mu nu} F^{mu nu}
```

where F_{mu nu} = partial_mu A_nu - partial_nu A_mu is the U(1) field strength.

IMPORTANT: In the minimal ECH framework, photons do NOT couple directly to
torsion. The electromagnetic field strength is defined using the ordinary
partial derivative, not the covariant derivative with the full connection.
This is because A_mu is a U(1) gauge field, not a Lorentz-valued field, so
it does not see the spin connection.

The only photon-torsion coupling arises INDIRECTLY through fermion loops
(the ABJ anomaly triangle).

---

## The Complete Action

```
S = S_grav[e, omega, gamma(x)] + S_phi[phi, g] + S_Dirac[psi, e, omega] + S_Maxwell[A, e]
```

Explicitly:

```
S = (1/2 kappa) integral d^4x |e| [e^mu_I e^nu_J R^{IJ}_{mu nu}(omega)
    + (1/gamma(x)) e^mu_I e^nu_J (*R)^{IJ}_{mu nu}(omega)]

  + integral d^4x sqrt(-g) [(1/2)(partial phi)^2 - V(phi)]

  + integral d^4x |e| psibar [i gamma^mu D_mu(omega) - m] psi

  - (1/4) integral d^4x sqrt(-g) F_{mu nu} F^{mu nu}
```

### Degrees of freedom and equations of motion

The independent variables are: e^I_mu (tetrad), omega^{IJ}_mu (connection),
phi (Immirzi field), psi (fermions), A_mu (photon).

The connection equation of motion (varying S with respect to omega) determines
the torsion in terms of phi, d_mu phi, and the fermion spin density. This is
the equation we solve in the next file.

### Key point: where gamma(x) enters

gamma(x) appears ONLY in the Holst term of the gravitational action. It does
NOT appear in:
- The Palatini (Einstein-Hilbert) term
- The scalar kinetic term
- The Dirac action
- The Maxwell action

Therefore, the only way gamma(x) affects the dynamics is through:
1. The torsion equation of motion (modified by the gamma-dependent Holst term)
2. The direct coupling of d_mu gamma = (1/f_phi) d_mu phi to geometry through
   the variation of 1/gamma(x) in the Holst term

This is why the torsion elimination is the decisive calculation.
