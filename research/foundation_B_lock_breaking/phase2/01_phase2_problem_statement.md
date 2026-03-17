# Foundation B Phase 2 — Problem Statement

**Date:** 2026-03-14

---

## Context

Phase 1 surveyed five candidate mechanisms for breaking the mass-coupling
lock. The ALP architecture (Model B) was identified as the unique
fully-unlocking structure with technically natural mass:

```
m = Lambda^2 / f     (shift-symmetry-protected)
g = alpha / f         (independent geometric coupling)
R = m/g = Lambda^2 / alpha   (depends on Lambda and alpha, NOT on f alone)
```

The open question is whether a geometric theory produces this structure
without collapsing to the already-closed Route T1 (dynamical Immirzi
field = generic ALP after torsion elimination).

---

## The Precise Question

**In metric-affine gravity (MAG), does the Nieh-Yan 4-form
N_4 = T^I wedge T_I - R_{IJ} wedge e^I wedge e^J remain exact (topological),
or does non-metricity Q != 0 render it non-exact (non-topological)?**

If N_4 is non-exact in MAG:
- A pseudoscalar theta coupled to N_4 retains local dynamical content
  (not a boundary term)
- The coupling has genuine geometric origin (surviving field elimination)
- Model B is viable as a geometric ALP

If N_4 is still effectively exact in MAG:
- The theta-N_4 coupling reduces to a total derivative
- Model B collapses to Route T1
- Foundation B (Nieh-Yan route) is closed

---

## What Must Be Checked

1. **Mathematical identity:** Compute d(e^I wedge T_I) in MAG (with
   non-metricity). Does the standard Nieh-Yan identity
   N_4 = d(e^I wedge T_I) acquire correction terms from Q?

2. **Shift symmetry compatibility:** If N_4 is non-exact, does the
   non-topological piece preserve or break the shift symmetry
   theta -> theta + c? This is critical for mass naturalness.

3. **Equivalence to T1:** After torsion and non-metricity elimination
   from the MAG field equations, does the reduced action for theta
   differ from a generic ALP? If not, Model B IS T1 in disguise.

4. **Distinctive prediction:** If Model B survives, does it predict
   anything that a generic ALP does not? (DR3 requirement)

5. **Lock test on concrete actions:** Construct toy Lagrangians
   realizing Model B and check R = m/g for parameter dependence.

---

## Success Criteria

| Outcome | Criterion |
|---------|-----------|
| GEOMETRIC_ALP_CANDIDATE_ALIVE | N_4 non-exact, shift symmetry compatible, coupling survives elimination, distinctive prediction exists |
| PARTIAL_PROGRESS_BUT_STILL_GENERIC | N_4 non-exact, but coupling reduces to generic ALP after elimination |
| COLLAPSES_TO_GENERIC_ALP | N_4 non-exact but dynamically equivalent to T1 |
| FOUNDATION_B_CLOSED | N_4 exact in MAG, or all toy actions fail lock test |

---

## Key Definitions

**Nieh-Yan 4-form (standard):**
N_4 = T^I wedge T_I - R_{IJ} wedge e^I wedge e^J

In Riemann-Cartan (metric-compatible): N_4 = d(e^I wedge T_I). Exact.
In MAG (non-metric-compatible): to be determined.

**Non-metricity:**
Q_{IJ} = -D eta_{IJ} = 2 omega_{(IJ)}

where omega_{(IJ)} is the symmetric part of the connection 1-form.
In RC: omega_{(IJ)} = 0. In MAG: omega_{(IJ)} != 0 generically.

**Route T1 (closed):**
Dynamical Immirzi field theta coupled to N_4 in Riemann-Cartan geometry.
After torsion elimination, theta-N_4 = d(theta e^I wedge T_I) - d(theta)
wedge e^I wedge T_I. The first term is a boundary. The second reduces
to a generic ALP-fermion coupling after T -> fermion bilinears.
No geometric fingerprint survives.

**Mass-coupling lock:**
R = m/g = const in all free parameters. The 0- PGT mode has
R = M_Pl^2 / (4 sqrt(pi)), independent of t_3.
