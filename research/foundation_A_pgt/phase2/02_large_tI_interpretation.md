# Phase 2A — Physical Interpretation of Large |t_3|

**Date:** 2026-03-13
**Status:** Original analysis (derivations below, not literature summary)

---

## 1. The Lagrangian Structure

Model B (the 0- pseudoscalar axial torsion mode) corresponds to the PGT
action with only t_3 nonzero:

```
L = (1/2kappa^2)(-R) + (1/2kappa^2)(t_3)(^(3)T . ^(3)T) + L_Dirac
```

Using ^(3)T_{lmn} ^(3)T^{lmn} = -6 A_mu A^mu, this becomes:

```
L = (1/2kappa^2)(-R - 6 t_3 A_mu A^mu) + L_Dirac
```

where A_mu = (1/6) epsilon_{mu nu rho sigma} T^{nu rho sigma} is the
axial torsion vector. Since t_3 < 0 for ghost-freedom, write t_3 = -|t_3|:

```
L = (1/2kappa^2)(-R + 6|t_3| A_mu A^mu) + L_Dirac
```

Now: in this formulation, the A_mu field has no separate kinetic term of
the form (dA)^2. Its kinetic energy comes from the curvature scalar R when
expanded in terms of the full (torsion-including) connection. The torsion
equation of motion is no longer algebraic precisely because the 6|t_3| A^2
term modifies the connection field equation. The result, after
linearization around flat space, is that A_mu has an effective kinetic
term and mass:

```
L_eff(A) = -(1/2) Z_A F_{mu nu}(A) F^{mu nu}(A) - (1/2) m_B^2 A_mu A^mu + ...
```

where the kinetic normalization Z_A and mass m_B depend on t_3 and kappa.

---

## 2. What Does Large |t_3| Mean?

There are several equivalent ways to see what happens when |t_3| >> 1:

### Interpretation A: Large torsion-squared coupling relative to Einstein-Hilbert

The Lagrangian has the schematic form:

```
L ~ (M_Pl^2 / 2)(R + |t_3| A^2)
```

At |t_3| = O(1), the torsion-squared term and the Einstein-Hilbert term
have comparable coefficients. At |t_3| >> 1, the torsion-squared term
dominates over the minimal torsion coupling implicit in R. This means:

**Large |t_3| amplifies the torsion self-interaction relative to the
gravitational curvature terms.**

### Interpretation B: Small mass relative to Planck scale

The mass formula is:

```
m_B^2 = M_Pl^2 / (16 pi |t_3|)
```

Large |t_3| directly gives a small mass. This is not surprising — it
is simply the statement that a large kinetic/self-interaction coefficient
suppresses the mass. This is structurally identical to what happens with
any massive gauge boson when the gauge coupling is taken small:

```
m_W = g v / 2  =>  small g => small m_W for fixed v
```

Except here the "symmetry-breaking scale" is M_Pl and the "coupling" is
1/sqrt(|t_3|).

### Interpretation C: Canonical normalization reveals the physics

To understand the physical content, canonically normalize A_mu. Define:

```
A_mu^(can) = sqrt(Z_A) A_mu
```

where Z_A is the kinetic normalization. From the linearized PGT analysis,
the canonically normalized Lagrangian is:

```
L = -(1/4) F_{mu nu}^(can) F^{mu nu, (can)} - (1/2) m_B^2 (A^(can))^2
    + (kappa / sqrt(Z_A)) A_mu^(can) J^mu_5 + ...
```

The matter coupling strength (to the axial current) is:

```
g_eff = kappa / sqrt(Z_A) ~ 1 / (M_Pl sqrt(|t_3|))
```

**This is the crucial result.** As |t_3| increases:
- The mass decreases: m_B ~ M_Pl / sqrt(|t_3|)
- The matter coupling decreases: g_eff ~ 1 / (M_Pl sqrt(|t_3|))
- The ratio m_B / g_eff remains fixed: m_B / g_eff ~ M_Pl^2

**Large |t_3| is a DECOUPLING LIMIT.** The torsion mode becomes lighter
AND more weakly coupled simultaneously. It does not become strongly
coupled. It becomes irrelevantly weakly coupled.

### Interpretation D: Comparison with Proca theory

Model B is effectively a massive Proca-like field A_mu (the longitudinal
mode being the physical pseudoscalar). The Proca Lagrangian:

```
L_Proca = -(1/4) F^2 - (1/2) m^2 A^2
```

has no free dimensionless parameter. The PGT Model B Lagrangian is the
same structure but with the kinetic and mass terms both determined by
M_Pl and |t_3|:

```
kinetic normalization ~ M_Pl^2 |t_3|
mass^2 ~ M_Pl^2 / |t_3|
coupling to matter ~ 1 / (M_Pl sqrt(|t_3|))
```

So the theory at large |t_3| is:
- A very weakly coupled massive pseudovector
- With mass much below M_Pl
- With gravitationally suppressed interactions further suppressed by
  1/sqrt(|t_3|)

---

## 3. Is This a Strong-Coupling Problem?

**No.** Large |t_3| does NOT produce strong coupling. The opposite
happens: the theory becomes MORE weakly coupled as |t_3| increases.

The reason is that t_3 multiplies the torsion kinetic term (in disguise),
not a coupling constant. Increasing |t_3| is like increasing the kinetic
normalization Z of a scalar field: the canonically normalized field has
a suppressed coupling.

Compare with a scalar field phi with large kinetic normalization:

```
L = -(Z/2)(partial phi)^2 - (lambda/4) phi^4
```

Canonically normalize: phi_can = sqrt(Z) phi:

```
L = -(1/2)(partial phi_can)^2 - (lambda/(4 Z^2)) phi_can^4
```

The effective self-coupling is lambda/Z^2, which goes to zero at
large Z. The theory becomes free (trivial), not strongly coupled.

The same structure applies to Model B at large |t_3|.

---

## 4. Is This a Problem for Cosmological Relevance?

**YES — and this is the key finding of this document.**

If the matter coupling goes as g_eff ~ 1/(M_Pl sqrt(|t_3|)), then for
cosmologically relevant masses:

| Mass scale | |t_3| | g_eff (eV^{-1}) | g_eff relative to gravity |
|-----------|-------|-----------------|--------------------------|
| m ~ M_Pl  | 1     | 1/M_Pl          | = kappa (gravitational)  |
| m ~ TeV   | 10^{10} | 10^{-5}/M_Pl  | 10^{-5} x gravity       |
| m ~ eV    | 10^{52} | 10^{-26}/M_Pl | 10^{-26} x gravity      |
| m ~ meV   | 10^{58} | 10^{-29}/M_Pl | 10^{-29} x gravity      |
| m ~ H_0   | 10^{118}| 10^{-59}/M_Pl | 10^{-59} x gravity      |

At the dark energy scale (m ~ meV), the torsion mode couples to matter
roughly 10^{29} times more weakly than gravity. At the Hubble scale,
10^{59} times weaker.

**A field that couples this weakly to matter is cosmologically inert.**
It cannot:
- Be produced thermally (coupling too weak for thermalization)
- Mediate observationally detectable fifth forces
- Produce birefringence at observable levels
- Drive any dynamics coupled to the matter sector

The ONLY way such a field could affect cosmology is through its
gravitational effects (stress-energy), which do not depend on g_eff
but only on the field's energy density. This is possible if the field
has appropriate initial conditions — but then it is purely gravitational
quintessence with no distinctive "torsion" signature.

---

## 5. Summary

| Property | Behavior at large |t_3| |
|----------|---------------------|
| Mass m_B | Decreases as M_Pl/sqrt(|t_3|) |
| Matter coupling g_eff | Decreases as 1/(M_Pl sqrt(|t_3|)) |
| Strong coupling? | NO — theory becomes weakly coupled |
| EFT consistent? | YES — perturbative expansion improves |
| Cosmologically relevant? | ONLY through gravitational sector |
| Distinctive torsion signature? | **NO — matter coupling too suppressed** |

**The large-|t_3| limit is a decoupling limit, not a strong-coupling
limit. The theory is consistent but physically empty: the torsion
mode becomes an ultra-weakly coupled massive field distinguishable
from generic quintessence only by its geometric origin in the action,
not by any observable coupling.**
