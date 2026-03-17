# Branch S: Effective Operator Derivation

**Date:** 2026-03-16

---

## 1. The VVA Triangle: Setup

Consider the one-loop fermion triangle with:
- Vertex 1: QED vertex, e gamma^nu, photon momentum k1
- Vertex 2: QED vertex, e gamma^rho, photon momentum k2
- Vertex 3: Axial torsion vertex, (3/2) gamma^mu gamma_5, torsion momentum q = k1 + k2

The triangle amplitude is:

```
Gamma^{mu nu rho}(q, k1, k2) = (-1) * integral [d^4 p / (2pi)^4]
    Tr [ (3/2) gamma^mu gamma_5 * S(p) * e gamma^nu * S(p+k1)
         * e gamma^rho * S(p+k1+k2) ]
    + (k1 <-> k2, nu <-> rho)
```

where S(p) = i / (p-slash - m) is the fermion propagator, the (-1)
is from the fermion loop, and the second term is the crossed diagram.

This is EXACTLY the ABJ anomaly triangle with the replacement:

```
(axial current coupling g_A gamma^mu gamma_5) -> (3/2) gamma^mu gamma_5
```

So g_A = 3/2 for the torsion-fermion vertex.

---

## 2. The Anomaly Coefficient

The ABJ anomaly for a single fermion species with charge Q_f gives:

```
Gamma^{mu nu rho}_{anomaly} = (g_A / 4 pi^2) * Q_f^2 * e^2
                               * epsilon^{mu nu rho sigma} * k_{1 sigma}
```

Wait -- let me write this more carefully. The standard result for the
VVA triangle (Adler-Bell-Jackiw) is:

```
q_mu Gamma^{mu nu rho} = (e^2 Q_f^2 / 2 pi^2) * epsilon^{nu rho alpha beta} k_{1 alpha} k_{2 beta}
```

This is the anomalous Ward identity: the divergence of the axial
current equals the topological density.

The full triangle amplitude (in the limit of zero fermion mass, which
is appropriate at energies much above m_f) is:

```
Gamma^{mu nu rho} = -(e^2 Q_f^2 / 4 pi^2) * epsilon^{mu nu rho sigma}
                     * (k1 - k2)_sigma / q^2
                     + (non-anomalous, longitudinal parts)
```

For our purposes, the relevant effective Lagrangian is obtained by
contracting with the external torsion field S_mu and photon fields:

```
L_eff = S_mu * Gamma^{mu nu rho} * A_nu * A_rho
```

---

## 3. The Effective Lagrangian

Summing over all fermion species and including the torsion coupling:

```
L_triangle = (3/2) * (e^2 / 16 pi^2) * (sum_f Q_f^2)
             * S^mu * epsilon_{mu nu alpha beta} * F^{nu alpha} * A^beta
```

Or equivalently:

```
L_triangle = (3 e^2 / 32 pi^2) * (sum_f Q_f^2) * S_mu * K^mu_{CS}
```

where K^mu_{CS} = (1/2) epsilon^{mu nu alpha beta} A_nu F_{alpha beta}
is the abelian Chern-Simons current, satisfying partial_mu K^mu = (1/4) F F-tilde.

### The anomaly coefficient

For the Standard Model fermion content:

```
sum_f Q_f^2 = sum over all Dirac fermions of Q_f^2
```

Per generation:
- up quark: Q = 2/3, color factor 3: contribution = 3 * (4/9) = 4/3
- down quark: Q = -1/3, color factor 3: contribution = 3 * (1/9) = 1/3
- electron: Q = -1: contribution = 1
- neutrino: Q = 0: contribution = 0

Total per generation: 4/3 + 1/3 + 1 = 8/3
Three generations: sum_f Q_f^2 = 8

So:

```
L_triangle = (3 e^2 / 32 pi^2) * 8 * S_mu * K^mu_{CS}
           = (3 alpha_{EM} / 4 pi) * 8 * S_mu * K^mu_{CS}
           = (6 alpha_{EM} / pi) * S_mu * K^mu_{CS}
```

where alpha_{EM} = e^2 / (4 pi) ~ 1/137.

---

## 4. After Torsion Elimination

Now substitute the torsion equation of motion:

```
S_mu = -(kappa/4) * C(gamma) * J^5_mu
```

where C(gamma) = gamma^2 / (1 + gamma^2) and kappa = 8 pi G = 8 pi / M_Pl^2.

```
L_eff = -(6 alpha_{EM} / pi) * (kappa/4) * C(gamma) * J^5_mu * K^mu_{CS}
      = -(3 alpha_{EM} kappa / (2 pi)) * C(gamma) * J^5_mu * K^mu_{CS}
```

Numerically:
- alpha_{EM} ~ 1/137
- kappa = 8 pi / M_Pl^2 ~ 5.1 * 10^{-38} GeV^{-2}
- C(gamma) ~ 0.070 (for gamma = 0.274, LQG value)

```
Coefficient = (3 * (1/137) * 5.1e-38) / (2 pi) * 0.070
            ~ 3 * 3.7e-40 / 6.28 * 0.070
            ~ 1.2e-41 GeV^{-2}
```

This is Planck-suppressed: coefficient ~ alpha / (pi M_Pl^2).

---

## 5. Operator Structure After Torsion Elimination

The operator:

```
L_eff = -C_eff * J^5_mu * K^mu_{CS}
```

with C_eff = (3 alpha_{EM} kappa) / (2 pi) * C(gamma) ~ 10^{-41} GeV^{-2}

This is a DIMENSION-8 operator (four fermion fields + two photon
fields, or equivalently: J^5 has dimension 3, K_{CS} has dimension 3,
plus the coefficient has dimension -2, giving total action dimension 4).

Wait, let me recount. J^5_mu = psi-bar gamma_mu gamma_5 psi has mass
dimension 3. K^mu_{CS} = epsilon^{...} A F has mass dimension 3. So
J^5 K has dimension 6. The coefficient has dimension -2 (GeV^{-2}).
The Lagrangian density has dimension 4. Correct: 6 + (-2) = 4.

This is a FOUR-POINT contact interaction between two fermions and
two photons, suppressed by 1/M_Pl^2.

**Key distinction from a birefringent pseudoscalar:**

A pseudoscalar field phi coupled as phi F F-tilde gives birefringence
when phi has a nonzero gradient (phi-dot != 0). This is a TWO-photon
operator with an external classical background.

The ECH operator J^5_mu K^mu_{CS} is a FOUR-POINT quantum operator.
It does not have a classical background component unless J^5_mu
develops a vacuum expectation value.

---

## 6. Cosmological Evaluation: Does J^5 Have a VEV?

On a cosmological FRW background:

### Spatial components
By isotropy: <J^5_i> = 0 (no preferred direction).

### Temporal component
<J^5_0> = <n_R - n_L> = net chiral number density.

In the standard cosmological history:
- Above the electroweak scale (T > 100 GeV): left and right chiralities
  are distinct. But in thermal equilibrium, the chiral chemical potential
  mu_5 = 0 unless something sources it.
- Below the electroweak scale: chirality is violated by fermion masses.
  Massive fermions have helicity flip, and <J^5_0> relaxes to zero on
  a timescale ~ 1/m_f.
- In the late universe (recombination, T ~ 0.3 eV): all charged fermions
  are non-relativistic. Their chirality is not a good quantum number.
  <J^5_0> = 0 to exponential accuracy.
- Neutrinos: if massless, <J^5_0> could be nonzero. But neutrinos
  are electrically neutral (Q = 0), so they do not contribute to the
  photon operator (no QED vertex).

### The one possible exception: chiral asymmetry from the electroweak anomaly

The electroweak sphaleron processes can convert baryon number to
chiral asymmetry. In the early universe (T > T_EW ~ 160 GeV),
sphalerons are active and maintain:

```
mu_5 ~ mu_B (baryon chemical potential)
```

But at recombination (when CMB polarization is generated):
- T ~ 0.3 eV << T_EW
- Sphalerons are frozen out
- Chirality has been washed out by mass effects
- <J^5_0> = 0

**There is no chiral asymmetry at recombination.**

### What about between recombination and today?

CMB photons propagate from z ~ 1100 to z = 0 through a universe
with essentially no free fermions (after recombination, the universe
is neutral). Even if a chiral asymmetry existed, there are no free
charged fermions to source J^5_mu.

---

## 7. The Birefringence Angle (Hypothetical)

IF there were a nonzero <J^5_0> = n_5 at some epoch, the
birefringence angle would be:

```
Delta beta = C_eff * integral n_5(t) dt (along the photon path)
```

For a rough estimate with n_5 ~ n_baryon ~ 10^{-7} T^3 (generous
upper bound from the baryon asymmetry):

At recombination, T ~ 0.3 eV, so n_5 ~ 10^{-7} * (0.3)^3 eV^3
~ 3 * 10^{-9} eV^3.

```
Delta beta ~ 10^{-41} GeV^{-2} * 3e-9 eV^3 * (age of universe)
           ~ 10^{-41} * (10^{-9})^{-2} * 3e-9 * 10^{41} (eV * seconds)
```

Let me do this more carefully in natural units.

C_eff ~ 10^{-41} GeV^{-2} = 10^{-41} * (10^{-9})^{-2} eV^{-2} = 10^{-23} eV^{-2}

n_5 ~ 3 * 10^{-9} eV^3

The effective "mass" for birefringence:

```
mu_bire = C_eff * n_5 ~ 10^{-23} * 3e-9 = 3 * 10^{-32} eV
```

The birefringence angle accumulated over the Hubble time:

```
Delta beta ~ mu_bire * t_H ~ 3e-32 eV * (4.3e17 s * 6.6e-16 eV*s)
           ~ 3e-32 * 2.8e2
           ~ 10^{-29} radians
           ~ 6 * 10^{-28} degrees
```

The observed birefringence is beta ~ 0.35 degrees.

**The ECH prediction is 28 ORDERS OF MAGNITUDE too small.**

Even with the most generous assumptions (n_5 at the baryon
asymmetry level), the effect is unobservably tiny because:
1. The coupling is Planck-suppressed (1/M_Pl^2)
2. The chiral density is at best baryon-asymmetry level (10^{-7} n_gamma)
3. Both suppressions multiply

---

## 8. The Operator Identity: Relation to the Standard Axial Anomaly

### Critical question: Is the VVA triangle ECH-specific?

The VVA triangle with the torsion vertex is:

```
L_VVA = g_axial * (anomaly) * S_mu * K^mu_{CS}
```

where g_axial = 3/2.

Now, the STANDARD axial anomaly in QED (no torsion, no gravity) gives:

```
partial_mu J^{5 mu} = (N_f alpha / 2 pi) * F F-tilde
```

This anomaly exists in FLAT SPACE QED with NO ECH gravity.

The torsion coupling to J^5_mu (S_mu J^{5 mu} vertex) simply probes
the same anomaly through a different external leg. The anomaly
coefficient is UNIVERSAL — it depends only on the fermion charge
assignments, not on the source of the axial coupling.

So: the VVA triangle with a torsion vertex gives EXACTLY THE SAME
anomaly coefficient as the standard ABJ anomaly. The ONLY ECH-specific
content is:
1. The coupling constant g_axial = 3/2 at the torsion vertex
2. The torsion-to-J^5 relation S = -const * J^5

Neither of these modifies the ANOMALY COEFFICIENT. They modify the
overall coefficient of the effective operator, but the operator is
the SAME one that any axial vector coupling would generate.

**The ECH framework does not produce a new operator. It produces the
standard ABJ anomaly operator with a specific (Planck-suppressed)
coefficient.**

Any theory with an axial vector coupling to fermions (e.g., a massive
Z' boson, an ALP derivative coupling, etc.) would give an analogous
operator. The ECH origin provides no distinctive signature.

---

## 9. Summary

```
+------------------------------------------------------------+
|                                                              |
|  EFFECTIVE OPERATOR EXISTS at one loop: YES                  |
|  (it is the ABJ anomaly triangle with a torsion leg)         |
|                                                              |
|  Structure: L = C_eff * J^5_mu * K^mu_{CS}                  |
|  with C_eff ~ alpha / (pi M_Pl^2) * C(gamma) ~ 10^{-41}/GeV^2 |
|                                                              |
|  It is BIREFRINGENT (parity-odd): YES                        |
|                                                              |
|  It survives torsion elimination: NO (becomes J^5 * K_CS)    |
|  It is a PURE photon operator: NO (requires matter)          |
|  It works in vacuum: NO (J^5 = 0)                            |
|  It works with standard cosmological matter: NO (n_5 = 0)    |
|  Even with n_5 != 0: 28 ORDERS OF MAGNITUDE too small        |
|  It is ECH-specific: NO (same as standard ABJ anomaly)       |
|                                                              |
|  VERDICT: The operator exists formally but is cosmologically  |
|  dead. It cannot produce observable birefringence.            |
|                                                              |
+------------------------------------------------------------+
```
