# Final Gate: Problem Statement

**Date:** 2026-03-16
**Calculation:** Exact torsion elimination with dynamical Barbero-Immirzi field
**Stakes:** This is the FINAL gating calculation for the spin-torsion cosmology program.

---

## What Branch Q Phase 1 Established

The dynamical Barbero-Immirzi field (promoting gamma -> gamma(x) = gamma_0 + phi(x)/f_phi)
is the strongest candidate for ECH-specific parity-violating physics. Phase 1 found:

1. The induced phi-F-Ftilde coupling through the ABJ anomaly has strength
   ~ alpha N_eff / (4 pi f_phi), giving birefringence beta ~ 0.13 deg for
   f_phi ~ M_Pl and O(1) misalignment. This is within a factor ~3 of the
   observed 0.35 +/- 0.09 deg.

2. The Nieh-Yan-specific contribution is ~38 orders of magnitude below the
   standard ABJ route. It is phenomenologically irrelevant.

3. At LEADING ORDER in phi/f_phi, the dynamical Immirzi field is
   indistinguishable from a standard ALP with derivative fermion coupling.

4. The ECH framework provides theoretical priors (f_phi ~ M_Pl, no direct
   tree-level phi-F-Ftilde) but no distinctive observable signature at
   leading order.

---

## Why the Current Result Is Weak but Not Closed

The Phase 1 analysis was performed to LEADING ORDER in phi/f_phi. The four-fermion
coupling after torsion elimination is:

```
G_torsion(gamma) = (3 kappa / 32) * 1 / (1 - 3/(4 gamma^2))
```

When gamma -> gamma_0 + phi/f_phi, this generates a Taylor series:

```
G_torsion(phi) = G_0 + G_1 (phi/f_phi) + G_2 (phi/f_phi)^2 + ...
```

The G_1 term is the standard ALP derivative coupling. The G_2 and higher terms
are phi^n (J^5)^2 operators that are NOT present in the minimal ALP Lagrangian.

Additionally, when gamma is dynamical, the torsion equation of motion is MODIFIED.
The variation of the Holst term with respect to the connection generates terms
proportional to d_mu gamma = (1/f_phi) d_mu phi. This means the torsion solution
itself depends on d_mu phi, potentially generating new structures in the
torsion-eliminated action.

Neither of these effects was computed in Phase 1.

---

## What This Calculation Must Settle

Perform exact torsion elimination (all orders in phi/f_phi) with the dynamical
Immirzi field. Determine the complete reduced action. Compare term-by-term
to a generic ALP effective field theory.

### Three possible outcomes:

**Outcome 1: EXACTLY_GENERIC_ALP**
The exact elimination gives only standard ALP operators: kinetic term, mass,
derivative fermion coupling (d_mu phi) psibar gamma^mu gamma_5 psi, and the
anomaly-induced phi F Ftilde. The Wilson coefficients may be specific functions
of gamma_0, but the operator basis is identical to any ALP. No ECH-specific
physics survives.

**Outcome 2: GENERIC_ALP_PLUS_RELATION**
The exact elimination gives standard ALP operators, but with specific coefficient
RELATIONS between the fermion coupling constant, the decay constant, and gamma_0
that are not present in a generic ALP. The operator basis is still standard, but
the coefficient pattern is distinctive. ECH-specific only if the relation is
observationally testable.

**Outcome 3: GENUINELY_NEW_OPERATOR**
The exact elimination generates operators not present in any standard ALP EFT.
These could be: non-standard derivative structures, direct phi-photon couplings
at tree level, or higher-order operators with no ALP analog. This would constitute
genuinely new ECH-specific physics.

---

## Success Criterion

**Success (BRANCH_Q_PROMISING):** Outcome 3 with the new operator being
observationally accessible (not Planck-suppressed beyond reach).

**Partial success (BRANCH_Q_WEAK_PLUS_RELATION):** Outcome 2 with the
coefficient relation being testable in principle (even if difficult).

**Failure (BRANCH_Q_CLOSED):** Outcome 1, or Outcome 2/3 with all
non-standard terms being unobservably Planck-suppressed.

---

## Why This Is the Final Gate

If the exact elimination produces no new physics:
- The dynamical Immirzi field is a generic ALP (Outcome 1)
- All ECH-specific content is limited to theoretical priors on f_phi
- The broader ECH program (Foundations A-G + Branch Q) is comprehensively closed
- No mechanism within ECH can produce distinctive low-energy observables

This result, combined with the seven structural barriers from Foundations A-G,
would constitute a complete no-go result for the ECH phenomenology program.
