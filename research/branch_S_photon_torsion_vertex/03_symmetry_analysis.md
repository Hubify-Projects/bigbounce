# Branch S: Symmetry Analysis (Cheap-Kill Tests)

**Date:** 2026-03-16

---

## Purpose

Before computing any diagrams, determine which operators are allowed
or forbidden by symmetry. The goal is cheap kills: if symmetry forbids
the desired operator, no diagram calculation is needed.

---

## Test 1: U(1)_EM Gauge Invariance

### Question
Does the effective operator respect electromagnetic gauge invariance?

### Analysis
F_mu_nu F-tilde^{mu nu} IS gauge invariant (constructed from field
strengths only).

A_mu F-tilde^{mu nu} is NOT gauge invariant (contains bare A_mu).
However, a Chern-Simons-like coupling B(x) * A ^ F can be gauge
invariant if B(x) is an external non-dynamical background — under
gauge transformation A -> A + d Lambda, the Chern-Simons term
shifts by a total derivative. This is the standard structure of
the theta-term.

For our purposes: the ABJ triangle diagram generates an operator
that is gauge invariant because the anomaly satisfies the
Wess-Zumino consistency conditions. The effective operator from
the triangle is:

```
L_eff ~ S_mu epsilon^{mu nu alpha beta} A_nu F_{alpha beta}
      = S_mu epsilon^{mu nu alpha beta} partial_alpha (A_nu A_beta)
```

Under A -> A + d Lambda: this shifts by a term proportional to
partial_mu S^mu (total divergence). If S_mu is conserved (divergence-free)
or if it is an on-shell torsion, the operator is effectively gauge
invariant (up to boundary terms).

**RESULT: No kill from gauge invariance. The operator is allowed.**

---

## Test 2: Parity

### Question
What parity does the generated operator have? Birefringence requires
a parity-ODD operator.

### Analysis

The triangle diagram with two vector vertices and one axial vertex
generates a PARITY-ODD operator. This is the structure of the ABJ
anomaly: the axial anomaly is P-odd.

Explicitly:
- S_mu is a PSEUDOVECTOR (parity-odd)
- F_mu_nu F-tilde^{mu nu} is a PSEUDOSCALAR (parity-odd)
- The product S_mu * (something parity-even involving F) can be
  parity-odd overall

The triangle gives:

```
L_eff ~ S^mu epsilon_{mu nu alpha beta} F^{nu alpha} A^beta
```

Under parity: S^mu -> +S_mu (spatial flip with axial sign),
epsilon -> -epsilon, F -> +F, A -> -A. The net parity is
(+1)(-1)(+1)(-1) = +1. Wait, let me be more careful.

Under parity P:
- S^0 -> +S^0, S^i -> -S^i (pseudovector)
- A^0 -> +A^0, A^i -> -A^i (vector)
- F_{0i} -> -F_{0i}, F_{ij} -> +F_{ij}
- F-tilde^{mu nu}: F-tilde_{0i} = (1/2) epsilon_{0ijk} F^{jk} -> +F-tilde_{0i}
- epsilon^{mu nu alpha beta} -> -epsilon^{mu nu alpha beta} (parity-odd tensor)

Actually, the cleanest statement: the triangle diagram with VVA
(vector-vector-axial) vertices generates the anomaly:

```
partial_mu J^{5 mu} = (e^2 / 16 pi^2) F_{mu nu} F-tilde^{mu nu}
```

The effective action term that produces this anomaly equation is:

```
S_eff ~ integral S_mu J^{5 mu} ~ integral S_mu (e^2/16pi^2) * (1/partial) * F F-tilde
```

This is not quite right. The actual Feynman diagram gives:

```
Gamma^{mu nu rho}(k1, k2) = (e^2 / 4 pi^2) * epsilon^{mu nu alpha beta}
                              k_{1 alpha} k_{2 beta} * (1/(k1+k2)^2 + ...)
```

where mu is the axial index (torsion leg) and nu, rho are photon indices.

The point: the operator is parity-odd. F F-tilde is a pseudoscalar.
S_mu is a pseudovector. Their contraction S_mu * (partial^mu F F-tilde)
would be a scalar (parity-even), but the actual operator structure from
the triangle is different — it's S_mu contracted with the Chern-Simons
current K^mu where partial_mu K^mu = F F-tilde.

**RESULT: The triangle diagram IS parity-odd. This is the correct
structure for birefringence. No kill from parity.**

---

## Test 3: Furry's Theorem

### Question
Does Furry's theorem (or its analog) force the diagram to zero?

### Analysis
Standard Furry's theorem: a fermion loop with an ODD number of
VECTOR current insertions vanishes by charge conjugation symmetry.

The ABJ triangle has TWO vector insertions (photon vertices) and
ONE axial insertion (torsion vertex). This is VVA, not VVV.
The gamma_5 at the axial vertex breaks charge conjugation symmetry
of the loop. Furry's theorem does NOT apply.

This is precisely WHY the ABJ anomaly is nonzero: the VVA triangle
evades Furry's theorem.

**RESULT: No kill from Furry's theorem. The VVA triangle is allowed.**

---

## Test 4: C and CP Properties

### Analysis
- The VVA triangle is C-odd (the axial current is C-odd)
- The resulting operator S_mu K^mu (where K is the Chern-Simons current)
  is C-odd and P-odd, hence CP-even
- CP-even operators are allowed in the Standard Model

Actually wait: J^5_mu under charge conjugation C:
- J^5_mu = psi-bar gamma_mu gamma_5 psi -> +psi-bar gamma_mu gamma_5 psi
  (axial current is C-EVEN for Dirac fermions)

And the vector current J_mu = psi-bar gamma_mu psi -> -psi-bar gamma_mu psi
(C-odd).

The anomaly equation partial_mu J^5_mu = (e^2/16pi^2) F F-tilde:
- LHS: C-even
- RHS: F F-tilde under C: F -> -F (since A -> -A), so F F-tilde -> F F-tilde
  (even number of sign flips). C-even.

Consistent. The operator is C-even, P-odd, CP-odd.

For cosmological birefringence: a CP-odd operator IS what is needed.
The rotation of the polarization plane is a CP-odd effect.

**RESULT: CP properties are consistent with birefringence. No kill.**

---

## Test 5: Does J^5 = 0 Kill the Operator?

### This is the CRITICAL test.

### Analysis

After torsion elimination, the "external" torsion S_mu is replaced by:

```
S_mu = -(kappa/4) * C(gamma) * J^5_mu
```

The effective operator from the triangle becomes:

```
L_eff ~ S_mu * (anomaly) ~ kappa * C(gamma) * J^5_mu * K^mu_{CS}
```

where K^mu_{CS} is the Chern-Simons current of the photon field.

This operator has FOUR fields: two fermion fields (in J^5_mu) and
two photon fields (in K^mu_{CS} or equivalently in A_mu F_nu_rho).

**For pure photon birefringence in vacuum (no matter), you need a
PURE photon operator — no external fermion legs.**

The operator above requires J^5_mu != 0, which means:
- Fermions must be PRESENT
- They must have a net CHIRAL ASYMMETRY (J^5_0 = n_R - n_L != 0)

In a universe with equal left- and right-handed fermions:
```
<J^5_mu> = 0
```

Therefore the operator VANISHES on the cosmological background.

### Can we go to higher loops to get a pure photon operator?

At two loops: integrate out the fermion in the J^5_mu factor as well.
This gives a fermion loop with the (J^5)^2 vertex AND photon vertices.
The topology is:

```
[fermion loop 1] -- (J^5)^2 vertex -- [fermion loop 2 with 2 photon legs]
```

But (J^5)^2 is a scalar (parity-EVEN). A parity-even insertion into
a fermion loop with two photon vertices gives:
- VV bubble with scalar insertion -> F_{mu nu} F^{mu nu} (parity-even)
- NOT F F-tilde (parity-odd)

So the two-loop diagram generates F F (non-birefringent), not F F-tilde
(birefringent).

### The deeper reason

The four-fermion interaction (J^5)^2 is parity-EVEN. After integrating
out torsion, ALL gamma-dependent physics resides in this parity-even
operator. Any further loop integration using this operator as a vertex
can only generate parity-even effective operators.

To get F F-tilde (parity-odd) you need a parity-odd insertion in the
fermion loop. The only parity-odd element in the original theory is
the Holst term, but after torsion elimination, the Holst term has
been absorbed into the (parity-even) coefficient of (J^5)^2.

```
+--------------------------------------------------+
|                                                    |
|  THE PARITY TRAP:                                  |
|                                                    |
|  Torsion (pseudovector) is parity-odd              |
|  (J^5)^2 (pseudovector squared) is parity-even    |
|  After torsion elimination, all ECH-specific       |
|  physics is in the parity-even (J^5)^2.           |
|  Therefore: no parity-odd PURE photon operator    |
|  can be generated from ECH at any loop order.      |
|                                                    |
+--------------------------------------------------+
```

**RESULT: THIS IS THE KILL.**

In vacuum (J^5 = 0): the one-loop operator vanishes because it
requires matter.

Even with matter present: the two-loop pure photon operator is
parity-EVEN (non-birefringent) because (J^5)^2 is parity-even.

The ONLY way to get birefringence is through the one-loop operator
with MACROSCOPIC J^5 != 0, which requires a chiral asymmetry that
does not exist in the standard cosmological background.

---

## Test 6: Is There a Pure Photon Operator?

### Question
After integrating out ALL fermions (not just torsion), is there a
pure photon effective operator with ECH-specific (gamma-dependent)
content?

### Analysis

Consider the full path integral: integrate out torsion first (algebraic),
then integrate out fermions (one-loop).

After torsion elimination, the fermion action is:

```
S_f = integral [i psi-bar D-ring psi - m psi-bar psi
       + e psi-bar gamma^mu A_mu psi
       + G_torsion (psi-bar gamma^mu gamma_5 psi)^2]
```

where D-ring is the torsion-free covariant derivative (gamma-independent
by Branch G v1).

The one-loop effective action for photons:

```
Gamma[A] = -i Tr ln [i D-ring + e A-slash - m + G_torsion * (J^5)^2 terms]
```

Expanding in powers of A and G_torsion:

- O(A^2, G^0): Standard vacuum polarization Pi_{mu nu}(k). This is the
  standard QED result. Parity-even. Gamma-independent.

- O(A^2, G^1): This requires one (J^5)^2 insertion in the fermion loop.
  But (J^5)^2 is a FOUR-FERMION vertex, not a two-fermion vertex. In a
  one-loop diagram, you cannot insert a four-fermion vertex — it would
  require additional fermion propagators, making it a two-loop diagram.

  At one loop with only two-fermion vertices available (QED vertex and
  mass term), there is NO gamma-dependent correction to the photon
  propagator.

- O(A^2, G^1) at two loops: A fermion bubble with two photon legs,
  connected to another fermion line via (J^5)^2. This CAN produce a
  gamma-dependent correction. But as argued above, the (J^5)^2 insertion
  is parity-even, so it corrects F^2 (vacuum polarization), not F F-tilde
  (birefringence).

### Explicit operator analysis at two loops

The two-loop contribution with one (J^5)^2 insertion and two photon
vertices generates (schematically):

```
delta L ~ G_torsion * (e^2 / 16 pi^2)^2 * Lambda^2 * F_{mu nu} F^{mu nu}
```

This is a (divergent, requiring renormalization) correction to the
photon kinetic term. It is:
- Parity-EVEN (F F, not F F-tilde)
- Proportional to G_torsion ~ kappa * C(gamma)
- Numerically tiny: G_torsion ~ kappa ~ 1/M_Pl^2

It does NOT produce birefringence.

**RESULT: No pure photon birefringent operator exists at any loop order
in the torsion-eliminated theory. The parity of (J^5)^2 forbids it.**

---

## Summary of Cheap-Kill Tests

| Test | Result | Kills the operator? |
|------|--------|-------------------|
| U(1) gauge invariance | Allowed | NO |
| Parity (operator structure) | P-odd operator exists (VVA triangle) | NO |
| Furry's theorem | Does not apply (gamma_5 breaks it) | NO |
| C/CP properties | CP-odd, as needed | NO |
| J^5 = 0 in vacuum | **Kills the one-loop operator** | **YES (conditionally)** |
| Pure photon operator | **Does not exist (parity blocks it)** | **YES (unconditionally)** |

### The verdict from symmetry alone:

```
+--------------------------------------------------+
|                                                    |
|  1. The one-loop VVA triangle IS nonzero.          |
|     It generates S_mu * K^mu_{CS} (torsion-        |
|     Chern-Simons coupling).                        |
|                                                    |
|  2. After torsion elimination, this requires        |
|     J^5_mu != 0 (matter with chiral asymmetry).   |
|                                                    |
|  3. In vacuum or with unpolarized matter:          |
|     J^5 = 0 and the operator VANISHES.            |
|                                                    |
|  4. A pure photon birefringent operator CANNOT     |
|     be generated at any loop order because          |
|     (J^5)^2 is parity-even.                        |
|                                                    |
|  5. Cosmological birefringence from minimal ECH    |
|     requires a macroscopic chiral asymmetry that   |
|     does not exist in the standard universe.        |
|                                                    |
+--------------------------------------------------+
```

The symmetry analysis is sufficient to determine the outcome.
The diagram calculation in the next files confirms and quantifies
this result, but cannot overturn it.
