# Branch S: Photon-Torsion Vertex — Problem Statement

**Date:** 2026-03-16

---

## Why This Calculation Matters

This is the single remaining open calculation in the entire program. The
salvage audit (2026-03-16) identified one surviving positive path: compute
the one-loop photon-torsion vertex in ECH gravity and determine whether
it gives a first-principles prediction for cosmic birefringence.

All other routes are closed:
- Dark energy derivation: 7 structural barriers (Foundations A-G)
- Bounce observables: 7+ additional barriers (Branches H-P)
- Tension reduction: MCMC verification shows Delta-Neff consistent with zero

If this vertex is nonzero and cosmologically relevant, the project has a
publishable positive result (PRL/JCAP Letters). If it is zero, the result
is Barrier 15 and the program is comprehensively closed.

---

## The Question in Precise Terms

**Does the minimal Einstein-Cartan-Holst (ECH) framework generate an
effective photon-polarization rotation at one loop?**

More specifically: consider the one-loop fermion diagrams with

- Two external photon legs (from the standard QED vertex)
- Insertions of the torsion/contortion coupling (from the
  spin-connection coupling to fermions)

Do these generate an effective operator of the form:

```
L_eff = c_eff * B(x) * F_{mu nu} F-tilde^{mu nu}
```

where B(x) is some background field (torsion, contortion, or composite
fermion bilinear) and F-tilde is the dual field strength?

If so: is c_eff nonzero, is it gamma-dependent (ECH-specific), and does
B(x) survive on cosmological backgrounds?

---

## What Route S1 Previously Found

Route S1 established: "No photon coupling in the minimal model" at
tree level. Photons do not couple directly to torsion or to the
gravitational connection in the minimal ECH action. The question is
whether INTEGRATING OUT FERMIONS at one loop generates such a coupling
radiatively.

## What Branch G v1 Established

The Dirac operator is gamma-independent after torsion elimination.
Specifically: after solving for torsion algebraically and substituting
back, the fermion kinetic term returns to its standard GR form. The
Barbero-Immirzi parameter gamma enters ONLY through the coefficient
of the four-fermion interaction (J^5)^2. The question is whether this
gamma-dependent four-fermion coupling leaves an imprint in the
one-loop photon effective action.

## What Branch H Established

- (J^5)^2 is parity-EVEN (pseudovector squared = scalar)
- Pontryagin density R-tilde R = 0 on exact FRW
- No parity-odd background in the minimal model on FRW
- Barrier 8: parity-even effective interaction

---

## Success vs Failure Criteria

### SUCCESS (PHOTON_TORSION_VERTEX_SURVIVES):
All of the following must hold simultaneously:
1. A nonzero one-loop vertex exists coupling photons to torsion/contortion
2. The vertex generates F F-tilde (not just F F) — i.e., it is parity-odd
3. The coupling coefficient is gamma-dependent (ECH-specific, not generic QED)
4. The background field B(x) is nonzero on cosmological FRW backgrounds
5. The resulting birefringence angle is in the observable range

### CONDITIONAL (PHOTON_TORSION_VERTEX_CONDITIONAL):
The vertex exists at one loop BUT fails one or more of criteria 3-5:
- It exists but is gamma-independent (= standard axial anomaly, not ECH-specific)
- It exists but requires matter (J^5 != 0) that vanishes cosmologically
- It exists but the magnitude is unobservably small

### FAILURE (PHOTON_TORSION_VERTEX_ZERO):
The vertex is identically zero at one loop, OR it reduces entirely
to the standard QED axial anomaly with no ECH-specific content.

---

## Prior Assessment of Probability

The salvage audit estimated ~40-50% probability of a nonzero,
publishable vertex. However, the specific analysis below will show
that the honest probability is significantly lower once the operator
ordering and torsion elimination are carefully tracked.

The most likely outcome, based on established results, is that the
vertex either vanishes or is cosmologically irrelevant. This document
will establish which case holds and why.
