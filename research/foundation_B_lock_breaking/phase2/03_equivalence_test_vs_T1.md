# Foundation B Phase 2 — Equivalence Test vs Route T1

**Date:** 2026-03-14

---

## Purpose

Determine whether Model B (geometric ALP from MAG Nieh-Yan coupling)
is genuinely distinct from the already-closed Route T1 (dynamical
Immirzi field), or whether it collapses to the same effective theory
after field elimination.

---

## Route T1 Recap

### Setup
In Riemann-Cartan (metric-compatible) gravity, couple a pseudoscalar
theta to the Nieh-Yan density:

```
S_T1 = integral [-1/2 f^2 (d theta)^2 + alpha theta N_4 + S_EC]
```

### Why it failed

1. N_4 = d(e^I wedge T_I) in RC — exact form.
2. Integration by parts: alpha theta N_4 = boundary - alpha d(theta) wedge e^I wedge T_I.
3. Torsion is algebraic in EC: T^I -> (fermion bilinears) / M_Pl^2.
4. After substitution: alpha d(theta) wedge e^I wedge T_I -> (alpha/M_Pl^2) d(theta) wedge (psi-bar gamma_5 psi) + ...
5. This is a standard axion-fermion derivative coupling.
6. No geometric fingerprint survives — the result is a generic ALP
   with derivative coupling to fermion axial current.

### T1 failure mode
The coupling is indistinguishable from any other ALP. The "geometric
origin" is invisible in the low-energy EFT. DR3 fails.

---

## Model B: What Changes in MAG

### The full coupling

From the analysis in 02_nieh_yan_mag_analysis.md:

```
S_B = integral [-1/2 f^2 (d theta)^2 + alpha theta N_4 + S_MAG]

     = boundary + integral [
         -1/2 f^2 (d theta)^2
         - alpha d(theta) wedge e^I wedge T_I        ... (T1-like piece)
         + alpha theta Q_{AB} wedge e^B wedge T^A     ... (MAG correction)
         + S_MAG
       ]
```

### Term-by-term comparison with T1

**Term 1: Kinetic term -1/2 f^2 (d theta)^2**
Same in both T1 and Model B. Not diagnostic.

**Term 2: -alpha d(theta) wedge e^I wedge T_I**
IDENTICAL to the T1 coupling. After torsion elimination, this gives the
same generic ALP-fermion coupling as in T1. No new information.

**Term 3: +alpha theta Q_{AB} wedge e^B wedge T^A**
NEW in Model B. Not present in T1. This is the non-topological correction
from non-metricity.

### Analysis of the new term

The term alpha theta Q_{AB} wedge e^B wedge T^A has the following properties:

1. **Linear in theta (not d(theta)):** This is a potential-like term, not
   a kinetic coupling. It contributes to the mass/potential of theta, not
   to its coupling to matter.

2. **Bilinear in Q and T:** Requires both non-metricity and torsion.
   In MAG, both are typically algebraic (determined by field equations,
   not independent dynamical fields). After solving the MAG field equations:
   - Torsion T -> function of spin density (as in EC)
   - Non-metricity Q -> function of hypermomentum (dilatation current,
     shear current, etc.)

3. **After field elimination:**
   ```
   alpha theta Q_{AB} wedge e^B wedge T^A
   -> alpha theta * f(matter hypermomentum) * g(matter spin density)
   -> alpha theta * (composite matter operator)
   ```
   This is a NON-DERIVATIVE coupling of theta to matter — structurally
   different from the derivative coupling in T1.

4. **But:** A non-derivative coupling theta * O(matter) is just a Yukawa-
   like interaction. In the ALP context, this is a mass-mixing term
   between theta and the composite operator. It does NOT have a distinctive
   geometric form after field elimination.

---

## Equivalence Verdict

### What is the same as T1

- The derivative coupling d(theta) wedge e wedge T -> standard ALP-fermion
  coupling. This is IDENTICAL to T1.
- After all geometric fields are eliminated, the derivative coupling
  sector is indistinguishable from a generic ALP.

### What is different from T1

- The non-derivative term alpha theta Q wedge e wedge T is new.
- After field elimination, it becomes a non-derivative coupling of theta
  to matter (a mass-like or Yukawa-like term).
- This term is NOT present in T1 (where N_4 is exact and there is no
  non-derivative piece after integration by parts).

### Does the difference matter?

**For the coupling structure:**
The derivative coupling (from T1 piece) dominates at high energies
(E >> m_theta). The non-derivative coupling (from MAG piece) dominates
at low energies or contributes to the mass. In the cosmological context
(E ~ H_0 ~ m_theta), both contribute.

However: the non-derivative piece has the form theta * (spin density) * (hypermomentum density).
In the cosmological background (zero spin density), this term VANISHES.
The only coupling in the cosmological background is the T1-like derivative
coupling.

**For the mass:**
The non-derivative piece contributes to the effective potential of theta.
If Q and T have background values (in dense environments), theta acquires
an environment-dependent mass. But in cosmological backgrounds where
T_0 = 0, this contribution vanishes and the mass is set entirely by
other sources (explicit potential, radiative corrections).

### Summary

```
Model B = T1 + (environment-dependent mass term from Q*T cross-coupling)
```

In the cosmological background: Model B = T1. The MAG correction is
invisible.

In dense environments (neutron stars, early universe with spin density):
Model B differs from T1 through an environment-dependent mass for theta.

---

## Comparison Table

| Feature | Route T1 (RC) | Model B (MAG) |
|---------|---------------|---------------|
| Derivative coupling | Yes (generic ALP) | Yes (same as T1) |
| Non-derivative coupling | No | Yes (from Q*T term) |
| Shift symmetry | Exact | Broken by Q*T term |
| Mass in vacuum | From external potential only | Same + environment-dependent piece |
| Cosmological coupling | Generic ALP | Generic ALP (identical) |
| Dense-matter coupling | Generic ALP | Generic ALP + Yukawa-like piece |
| Geometric fingerprint | None | Weak (environment-dependent mass) |
| DR3 (distinctive prediction) | FAILS | MARGINAL — prediction exists but requires dense-matter environment |

---

## Conclusion

**Model B does NOT collapse entirely to T1.** The non-topological piece
of N_4 in MAG provides a genuinely new term (non-derivative coupling of
theta to the Q*T cross-product of geometric fields). After field
elimination, this becomes an environment-dependent mass/coupling for theta.

**But the distinction is WEAK:**
- In cosmological backgrounds, Model B IS T1.
- The new effects appear only in dense-matter environments.
- The coupling structure is still dominated by the generic ALP piece.
- The "geometric fingerprint" is an environment-dependent mass, which
  is phenomenologically similar to chameleon/symmetron mechanisms
  (not unique to geometry).

**Equivalence verdict: PARTIALLY_DISTINCT.**
Model B is not T1 in disguise, but the new content is insufficient to
claim a genuinely distinctive geometric dark-energy mechanism.
