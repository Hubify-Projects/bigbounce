# Foundation B Phase 2 — Nieh-Yan Form in Metric-Affine Gravity

**Date:** 2026-03-14

---

## Setup

### Notation

- e^I: vierbein 1-form (I = 0,1,2,3 internal Lorentz index)
- omega^I_J: full connection 1-form (NOT assumed metric-compatible)
- T^I = de^I + omega^I_J wedge e^J: torsion 2-form
- R^I_J = d(omega^I_J) + omega^I_K wedge omega^K_J: curvature 2-form
- eta_{IJ} = diag(-1,1,1,1): Minkowski metric (constant in frame basis)
- T_I = eta_{IJ} T^J, R_{IJ} = eta_{IK} R^K_J, omega_{IJ} = eta_{IK} omega^K_J

### Metric compatibility

In Riemann-Cartan (RC): D(eta_{IJ}) = 0, which implies omega_{IJ} = -omega_{JI}
(antisymmetric). Non-metricity vanishes.

In metric-affine gravity (MAG): D(eta_{IJ}) != 0. The non-metricity
1-form is:

```
Q_{IJ} = -D(eta_{IJ}) = -(d eta_{IJ} - omega^K_I eta_{KJ} - omega^K_J eta_{IK})
       = omega_{JI} + omega_{IJ}
       = 2 omega_{(IJ)}
```

(using d(eta_{IJ}) = 0 since eta is constant in the frame basis).

So the symmetric part of the connection encodes the non-metricity:

```
omega_{(IJ)} = Q_{IJ} / 2
```

The antisymmetric part omega_{[IJ]} contains the Levi-Civita + contortion
pieces (same as in RC).

### First Bianchi identity

The first Bianchi identity holds in BOTH RC and MAG:

```
DT^I = R^I_J wedge e^J
```

This is an algebraic identity following from d^2 = 0 and the definition
of T^I and R^I_J. It does NOT require metric compatibility.

Proof: DT^I = d(de^I + omega^I_J wedge e^J) + omega^I_K wedge T^K
            = d(omega^I_J) wedge e^J - omega^I_J wedge de^J + omega^I_K wedge T^K
            = d(omega^I_J) wedge e^J - omega^I_J wedge (T^J - omega^J_K wedge e^K) + omega^I_K wedge T^K
            = [d(omega^I_J) + omega^I_K wedge omega^K_J] wedge e^J
            = R^I_J wedge e^J     QED

---

## Main Computation: d(e^I wedge T_I) in MAG

### Step 1: Apply Leibniz rule

e^I is a 1-form, T_I is a 2-form. By the graded Leibniz rule:

```
d(e^I wedge T_I) = de^I wedge T_I + (-1)^1 e^I wedge dT_I
                  = de^I wedge T_I - e^I wedge dT_I
```

### Step 2: Expand de^I

From the definition of torsion:

```
de^I = T^I - omega^I_J wedge e^J
```

Therefore:

```
de^I wedge T_I = T^I wedge T_I - omega^I_J wedge e^J wedge T_I    ... (A)
```

### Step 3: Expand dT_I

Lower the index: T_I = eta_{IJ} T^J, and eta_{IJ} is constant, so
dT_I = eta_{IJ} dT^J.

From the first Bianchi identity DT^J = R^J_K wedge e^K:

```
dT^J = R^J_K wedge e^K - omega^J_K wedge T^K
```

Therefore:

```
dT_I = eta_{IJ}(R^J_K wedge e^K - omega^J_K wedge T^K)
     = R_{IK} wedge e^K - omega_{IK} wedge T^K
```

And:

```
-e^I wedge dT_I = -e^I wedge R_{IK} wedge e^K + e^I wedge omega_{IK} wedge T^K    ... (B)
```

### Step 4: Combine (A) and (B)

```
d(e^I wedge T_I) = T^I wedge T_I - omega^I_J wedge e^J wedge T_I
                   - e^I wedge R_{IK} wedge e^K + e^I wedge omega_{IK} wedge T^K
```

### Step 5: Simplify the R term

R_{IK} is a 2-form, e^I is a 1-form. Using the graded commutativity rule
(alpha^p wedge beta^q = (-1)^{pq} beta^q wedge alpha^p):

```
e^I wedge R_{IK} = (-1)^{1*2} R_{IK} wedge e^I = R_{IK} wedge e^I
```

Therefore: -e^I wedge R_{IK} wedge e^K = -R_{IK} wedge e^I wedge e^K.

### Step 6: Simplify the omega terms

**Term from (A):** -omega^I_J wedge e^J wedge T_I

Rewrite with all indices lowered. omega^I_J = eta^{IM} omega_{MJ}, and
T_I = eta_{IN} T^N:

```
-omega^I_J wedge e^J wedge T_I = -eta^{IM} omega_{MJ} wedge e^J wedge eta_{IN} T^N
                                = -delta^M_N omega_{MJ} wedge e^J wedge T^N
                                = -omega_{NJ} wedge e^J wedge T^N
```

Relabel N -> A, J -> B:

```
Term from (A) = -omega_{AB} wedge e^B wedge T^A
```

**Term from (B):** +e^I wedge omega_{IK} wedge T^K

omega_{IK} is a 1-form, so e^I wedge omega_{IK} = -omega_{IK} wedge e^I
(swapping two 1-forms). Relabel I -> B, K -> A:

```
Term from (B) = -omega_{BA} wedge e^B wedge T^A
```

**Sum of omega terms:**

```
-(omega_{AB} + omega_{BA}) wedge e^B wedge T^A = -2 omega_{(AB)} wedge e^B wedge T^A
```

Using omega_{(AB)} = Q_{AB}/2:

```
Sum = -Q_{AB} wedge e^B wedge T^A
```

### Step 7: Final result

```
d(e^I wedge T_I) = T^I wedge T_I - R_{IK} wedge e^I wedge e^K - Q_{AB} wedge e^B wedge T^A
```

---

## The Modified Nieh-Yan Identity in MAG

Define the Nieh-Yan 4-form as in RC:

```
N_4 := T^I wedge T_I - R_{IJ} wedge e^I wedge e^J
```

Then:

```
N_4 = d(e^I wedge T_I) + Q_{AB} wedge e^B wedge T^A      ... (*)
```

### Interpretation

**In RC (Q = 0):** N_4 = d(e^I wedge T_I). The Nieh-Yan form is EXACT.

**In MAG (Q != 0):** N_4 = d(e^I wedge T_I) + Q_{AB} wedge e^B wedge T^A.
N_4 is NOT exact — it has a correction proportional to the non-metricity-
torsion cross-term.

The correction Q_{AB} wedge e^B wedge T^A is:
- Algebraic in Q and T (no derivatives of Q or T)
- Bilinear: one factor of non-metricity, one factor of torsion
- Vanishes if either Q = 0 (RC limit) OR T = 0 (symmetric connection)
- A 4-form (correct degree for an action density in 4D)

### Corollary: dN_4 in MAG

```
dN_4 = d[d(e^I wedge T_I)] + d[Q_{AB} wedge e^B wedge T^A]
     = 0 + d(Q_{AB} wedge e^B wedge T^A)
```

dN_4 != 0 generically when Q != 0 and T != 0.

N_4 is a CLOSED form in RC (dN_4 = 0) but NOT closed in MAG.

---

## Phase 2 First-Check: PASSED

**The Nieh-Yan form IS non-topological in metric-affine gravity.**

This is an algebraic identity — it holds OFF SHELL and does not depend
on the dynamics of any specific MAG action.

The correction term Q_{AB} wedge e^B wedge T^A requires BOTH non-metricity
AND torsion to be present. In a purely torsion-free or purely metric-compatible
theory, the correction vanishes.

---

## Critical Follow-Up: Shift Symmetry Analysis

### The theta-N_4 coupling in MAG

Consider the coupling:

```
S_coupling = integral alpha theta N_4
           = integral alpha theta [d(e^I wedge T_I) + Q_{AB} wedge e^B wedge T^A]
```

Integrate the first term by parts:

```
alpha theta d(e^I wedge T_I) = alpha d(theta e^I wedge T_I) - alpha d(theta) wedge e^I wedge T_I
```

The first piece is a boundary term. So:

```
S_coupling = boundary + integral [-alpha d(theta) wedge e^I wedge T_I + alpha theta Q_{AB} wedge e^B wedge T^A]
```

### Shift symmetry test

Under theta -> theta + c:

- Term 1: -alpha d(theta) wedge e^I wedge T_I -> same (only d(theta) appears). **INVARIANT.**
- Term 2: alpha theta Q_{AB} wedge e^B wedge T^A -> shifts by alpha c Q_{AB} wedge e^B wedge T^A. **NOT INVARIANT.**

**The non-topological piece of N_4 EXPLICITLY BREAKS the shift symmetry
of theta.**

This is not a small correction or a soft breaking — it is a structural
consequence of the non-exactness of N_4. The very feature that makes N_4
non-topological (the Q-T cross-term) is also the feature that breaks the
shift symmetry that would protect the mass.

---

## The Fundamental Dilemma

**Theorem (Topological-Shift Duality):**

For any pseudoscalar theta coupled linearly to a geometric 4-form
density Omega_4 via S = integral alpha theta Omega_4:

- If Omega_4 = d(Omega_3) (exact/topological): the coupling reduces to
  -alpha d(theta) wedge Omega_3 after integration by parts. Only d(theta)
  enters -> shift symmetry theta -> theta + c is preserved ->
  mass is technically natural. BUT: the coupling is a total derivative
  and carries no local geometric content beyond what d(theta) provides.

- If Omega_4 != d(Omega_3) (non-exact/non-topological): the coupling
  contains a piece proportional to theta (not d(theta)) that cannot be
  removed by integration by parts -> shift symmetry is broken ->
  mass is NOT technically natural. BUT: the coupling has genuine local
  geometric content.

**Conclusion: For a LINEAR theta-Omega_4 coupling, mass protection (shift
symmetry) and geometric content (non-topological density) are mutually
exclusive.**

This is a STRUCTURAL obstruction, not a technical difficulty. It applies
to ANY geometric 4-form in any gravitational theory, not just the
Nieh-Yan form in MAG.

---

## Possible Escape Routes

### 1. Derivative coupling (preserves shift symmetry by construction)

Replace theta Omega_4 with d(theta) wedge Omega_3 where Omega_3 is a
geometric 3-form. Shift symmetry is automatic. But after field elimination,
the d(theta) coupling generically reduces to a standard ALP-matter
coupling with no geometric fingerprint. This IS Route T1.

### 2. Soft breaking by small non-metricity

If Q is dynamically small (Q ~ Q_0 << 1 in natural units), the shift
symmetry is approximately preserved and the mass receives a small
contribution:

```
delta m^2 ~ alpha Q_0 T_0 / f^2    (schematic)
```

But this is NOT technically natural — no symmetry is restored at m = 0
unless Q_0 = 0, which is the RC limit (T1).

However: the shift-breaking term alpha theta Q wedge e wedge T requires BOTH
Q != 0 AND T != 0. In cosmology, background torsion T_0 is zero (no
macroscopic spin density), so the shift-breaking term VANISHES in
the cosmological background. It is only activated in high-density
environments where torsion is sourced by spin.

This means:
- In the cosmological background: shift symmetry is EXACT -> mass is
  protected -> theta is light.
- Near matter (stars, neutron stars): torsion is sourced -> shift
  symmetry is broken -> theta acquires an environment-dependent mass.

This is structurally similar to a chameleon/symmetron mechanism, but
arising from the geometric structure of MAG rather than from an ad hoc
scalar potential. This is INTERESTING but requires detailed cosmological
analysis to determine if it's viable.

### 3. Non-linear coupling

Replace alpha theta N_4 with V(theta) N_4 where V has specific shift-
symmetry-breaking structure (e.g., V = Lambda^4 [1 - cos(theta/f)]).
The mass comes from V''(0), not from the geometric sector. The coupling
to geometry comes from V'(theta) N_4.

But: after torsion/non-metricity elimination, V'(theta) N_4 reduces to
V'(theta) times algebraic functions of matter fields. The geometric
origin is opaque and the predictions are indistinguishable from a
scalar-tensor theory with a non-minimal coupling.

---

## Summary of Key Results

| Result | Status |
|--------|--------|
| N_4 exact in MAG? | **NO** — correction Q_{AB} wedge e^B wedge T^A |
| Phase 2 first-check | **PASSED** |
| Shift symmetry preserved? | **NO** — non-topological piece breaks it |
| Mass-coupling lock broken? | **CONDITIONALLY** — m depends on Q, g depends on alpha/f |
| Geometric fingerprint in coupling? | **NO** — coupling reduces to generic ALP |
| Distinct from T1? | **PARTIALLY** — mass origin different, coupling same |
| Chameleon-like escape? | **POSSIBLE** — requires detailed cosmological analysis |
