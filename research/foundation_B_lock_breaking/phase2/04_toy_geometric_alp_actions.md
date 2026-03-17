# Foundation B Phase 2 — Toy Geometric ALP Actions

**Date:** 2026-03-14

---

## Purpose

Construct at least three concrete toy actions realizing the Model B
(geometric ALP in MAG) structure, and analyze each for:
1. Lock status (is R = m/g parameter-dependent?)
2. Shift symmetry status
3. Fate after field elimination
4. Distinctive predictions

---

## Toy Action I: Direct theta-N_4 Coupling in MAG

### Action

```
S_I = integral {
    -1/(2 kappa) R_{MAG}
    + a_1 T^I wedge *T_I + a_2 Q_{AB} wedge *Q^{AB}    [MAG kinetic sector]
    - 1/2 f^2 (d theta)^2                                 [theta kinetic]
    + alpha theta N_4                                      [Nieh-Yan coupling]
}
```

where kappa = 8 pi G, a_1 and a_2 are dimensionless MAG couplings,
and * denotes the Hodge dual.

### Field equations for torsion and non-metricity

In quadratic MAG, torsion and non-metricity are ALGEBRAIC (their
field equations are constraint equations, not dynamical equations).

Torsion equation (schematic):
```
T^I ~ (1/a_1) [alpha d(theta) wedge e^I + J_spin^I]
```

Non-metricity equation (schematic):
```
Q_{AB} ~ (1/a_2) [alpha theta T_{AB} + Delta_{AB}]
```

where J_spin is the spin current and Delta is the hypermomentum.

Note: The non-metricity equation involves theta itself (not d(theta)),
from the non-topological piece of N_4.

### After field elimination

Substituting T and Q back into the action:

```
S_I^{eff} = integral {
    -1/(2 kappa) R_GR
    - 1/2 [f^2 + alpha^2/(a_1)] (d theta)^2     [modified kinetic term]
    - alpha^2/(a_1 a_2) theta^2 (J_spin)^2         [mass from Q*T]
    + alpha/a_1 d(theta) J_spin                      [ALP coupling]
    + (4-fermion terms)
}
```

Key features:
- Kinetic normalization: Z = f^2 + alpha^2/a_1
- Mass squared: mu^2 ~ alpha^2 J_spin^2 / (a_1 a_2)  [environment-dependent!]
- Coupling: g_bare ~ alpha/a_1

After canonical normalization (theta_can = sqrt(Z) theta):
```
m = mu / sqrt(Z) ~ alpha |J_spin| / (sqrt(a_1 a_2) sqrt(f^2 + alpha^2/a_1))
g_eff = g_bare / sqrt(Z) ~ alpha / (a_1 sqrt(f^2 + alpha^2/a_1))
```

### Lock test

```
R = m / g_eff = |J_spin| sqrt(a_1) / (sqrt(a_2))
```

R depends on a_1, a_2 (MAG couplings), and |J_spin| (environment).
It does NOT depend on f or alpha.

**VERDICT: UNLOCKED** — but the mass is environment-dependent (proportional
to spin density), and the coupling is generic ALP.

### Problems

1. **Mass vanishes in vacuum:** J_spin = 0 in vacuum -> m = 0 exactly.
   theta is MASSLESS in the cosmological background. This is not dark
   energy — it's a massless pseudoscalar.

2. **Shift symmetry:** Broken by the theta^2 J_spin^2 term. Not
   technically natural (m = 0 in vacuum is protected by the vanishing
   of J_spin, not by a symmetry of theta).

3. **DR3:** The coupling is generic ALP. The only distinctive feature
   is the environment-dependent mass, which is similar to chameleon
   mechanisms.

---

## Toy Action II: theta-N_4 + Instanton Potential in MAG

### Action

Add an explicit shift-symmetry-breaking potential (instanton-like):

```
S_II = S_I + integral Lambda^4 [1 - cos(theta/f)]
```

This provides a vacuum mass m_0 = Lambda^2/f independent of the environment.

### After field elimination

```
S_II^{eff} = S_I^{eff} + integral Lambda^4 [1 - cos(theta_can / (f sqrt(Z)))]
```

Effective mass (in vacuum, J_spin = 0):
```
m_vac = Lambda^2 / (f sqrt(Z)) = Lambda^2 / sqrt(f^2 + alpha^2/a_1) * 1/f ???
```

Wait, let me be more careful. After canonical normalization:
```
m_vac^2 = Lambda^4 / (f^2 Z) = Lambda^4 / (f^2 (f^2 + alpha^2/a_1))
```

Coupling (same as Toy I):
```
g_eff = alpha / (a_1 sqrt(f^2 + alpha^2/a_1))
```

### Lock test

```
R = m_vac / g_eff = (Lambda^2 a_1) / (alpha f)  ... (need to verify)
```

Let me compute this properly:
```
m_vac = Lambda^2 / (f sqrt(Z))  where Z = f^2 + alpha^2/a_1
g_eff = alpha / (a_1 sqrt(Z))

R = m_vac / g_eff = (Lambda^2 a_1) / (alpha f)
```

R depends on Lambda, a_1, alpha, f. The coupling g_eff depends on
alpha, a_1, f. The mass depends on Lambda, f, alpha, a_1.

The parameter Lambda appears ONLY in the mass (not in the coupling).
So varying Lambda changes m but not g. **UNLOCKED.**

At Lambda -> 0: m -> 0 while g_eff stays finite. The shift symmetry
theta -> theta + c is restored (the cosine potential vanishes).
**Mass is technically natural.**

### Verdict

This is the ALP paradigm with a geometric coupling. But the coupling
is still generic ALP after field elimination (the geometric origin of
g_eff ~ alpha/a_1 is invisible once torsion is integrated out). The
only new feature compared to T1 is the environment-dependent mass
correction from the Q*T term, which shifts the effective mass near
matter.

**FULLY_UNLOCKED** with technically natural mass, but the coupling
structure is generic ALP. This is EXACTLY the structure identified
in Phase 1 as Model B — the question was whether the geometric origin
provides anything beyond generic ALP. It does not, in the coupling
sector.

---

## Toy Action III: Derivative Coupling to Geometric 3-Form

### Motivation

Preserve shift symmetry by construction: couple only d(theta) (not theta)
to geometric objects.

### Action

```
S_III = integral {
    -1/(2 kappa) R_MAG
    + a_1 T^I wedge *T_I + a_2 Q_{AB} wedge *Q^{AB}
    - 1/2 f^2 (d theta)^2
    + alpha d(theta) wedge e^I wedge T_I                   [RC piece]
    + beta d(theta) wedge Q_{AB} wedge e^A wedge e^B       [MAG piece]
    + Lambda^4 [1 - cos(theta/f)]                           [mass potential]
}
```

The beta term is new — it couples d(theta) to a non-metricity-dependent
3-form. Shift symmetry is EXACT for the geometric couplings (broken only
by the instanton potential, as desired).

### After field elimination

Torsion elimination: T -> spin density + d(theta) dependent terms.
Non-metricity elimination: Q -> hypermomentum + d(theta) dependent terms.

The effective action has the form:

```
S_III^{eff} = integral {
    -1/2 Z_eff (d theta)^2                          [modified kinetic]
    + Lambda^4 [1 - cos(theta/f)]                   [potential]
    + g_1 d(theta) J_axial                            [ALP-fermion, from alpha]
    + g_2 d(theta) J_dilation                         [ALP-dilatation, from beta]
    + (4-fermion terms)
}
```

where J_axial is the axial fermion current (standard ALP) and J_dilation
is the dilatation current (trace of the energy-momentum tensor).

### Lock test

```
m = Lambda^2 / (f sqrt(Z_eff))
g_1 = alpha / (a_1 sqrt(Z_eff))     [axial coupling]
g_2 = beta / (a_2 sqrt(Z_eff))       [dilatation coupling]
```

For the axial coupling: R_1 = m/g_1 = Lambda^2 a_1 / (alpha f).
Depends on Lambda (not in g_1). **UNLOCKED.**

For the dilatation coupling: R_2 = m/g_2 = Lambda^2 a_2 / (beta f).
Depends on Lambda (not in g_2). **UNLOCKED.**

Mass is technically natural (shift symmetry in geometric sector).
**FULLY_UNLOCKED.**

### What is new compared to T1?

The beta coupling provides a SECOND ALP coupling (to the dilatation
current) that is NOT present in T1. In T1, the only coupling is to the
axial current (from torsion). In Model III, there is an additional
coupling to the trace of T_mu_nu (from non-metricity).

**Is this a distinctive geometric fingerprint?**

The coupling to the dilatation current is:
```
g_2 d(theta) J_dilation = (beta / a_2 sqrt(Z)) partial_mu theta T^mu_mu
```

This is a conformal coupling. A generic ALP does NOT have this coupling
unless it is specifically added. In MAG, it arises NATURALLY from the
non-metricity sector.

The ratio g_2/g_1 = (beta a_1) / (alpha a_2) is a PARAMETER-DEPENDENT
ratio. It depends on the MAG couplings (a_1, a_2) and the two geometric
coupling constants (alpha, beta). A generic ALP would have g_2/g_1
as a free parameter; in MAG, the ratio is determined by the gravitational
action.

**However:** alpha and beta are separate coupling constants in the action.
MAG does not DETERMINE their ratio — it merely provides the geometric
framework for both couplings to exist. The predictive power is limited
to the EXISTENCE of both couplings, not their ratio.

### Verdict

Toy III is the most promising structure:
- Shift symmetry preserved -> mass technically natural
- Two independent ALP couplings (axial + conformal) -> richer phenomenology
- Lock fully broken
- But: the two couplings are both "generic" in form (derivative coupling
  to conserved currents). The geometric origin is not uniquely diagnostic.

---

## Toy Action IV: Composite Pseudoscalar from Torsion Condensation

### Motivation (from Phase 1 new idea #1)

Instead of a fundamental theta, consider a composite pseudoscalar
formed from torsion bilinears in a strong-coupling regime.

### Action sketch

```
S_IV = integral {
    -1/(2 kappa) R_PGT
    + t_i (torsion-squared terms)
    + G (four-torsion interaction)     [analog of 4-fermion in NJL]
}
```

If the torsion-squared sector has a strong coupling G > G_crit, a
torsion condensate forms: <T^I T_I> != 0. This breaks a chiral-like
symmetry and produces a pseudo-Goldstone boson Phi.

### Mass and coupling

```
m_Phi ~ Lambda_cond / sqrt(N)     [condensation scale / large-N]
g_Phi ~ 1 / f_Phi ~ Lambda_cond / M_Pl^2     [from torsion-matter vertex]
```

where Lambda_cond is the condensation scale (like Lambda_QCD) and N
is a counting factor.

### Lock test

```
R = m/g ~ M_Pl^2 / sqrt(N)
```

R depends on N (number of torsion species?). If N is a free parameter
of the theory, the lock is broken. But N is typically fixed by the
gauge group (in PGT, the torsion has fixed multiplicity).

**VERDICT: LIKELY_LOCKED** — the composite approach doesn't obviously
introduce new free parameters for mass and coupling separately.

### Additional issue

This requires strong-coupling dynamics in the torsion sector, which
is not under perturbative control. The mass and coupling estimates are
order-of-magnitude at best. Not suitable for a first-principles
analysis.

---

## Summary

| Action | Lock status | Mass natural? | Distinct from T1? | DR3? |
|--------|-------------|---------------|--------------------|----|
| I: theta N_4, no potential | UNLOCKED (env.) | No (env. mass) | Partially (env. mass) | Marginal |
| II: theta N_4 + instanton | FULLY_UNLOCKED | Yes (shift sym.) | Weakly (env. correction) | Weak |
| III: d(theta) coupling | FULLY_UNLOCKED | Yes (shift sym.) | Yes (dual coupling) | Marginal |
| IV: composite | LIKELY_LOCKED | Unknown | Unknown | Unknown |

### Best candidate: Toy Action III

Toy III provides the cleanest structure: shift symmetry is preserved,
the lock is broken, and the dual coupling (axial + conformal) provides
a potentially distinctive signature. However, the two coupling constants
(alpha, beta) are free parameters, so the distinctive prediction is
the EXISTENCE of both couplings, not their ratio.

### Worst candidate: Toy Action IV

The composite approach is not under perturbative control and likely
does not break the lock.
