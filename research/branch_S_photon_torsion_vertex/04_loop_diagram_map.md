# Branch S: Loop Diagram Map

**Date:** 2026-03-16

---

## Classification of All Relevant Diagrams

### Diagram 1: VVA Triangle (One-Loop)

**Topology:**

```
          A_nu (photon, k1)
         /
        / (QED vertex: e gamma^nu)
       /
   [fermion loop]
       \
        \ (QED vertex: e gamma^rho)
         \
          A_rho (photon, k2)
           |
           | (Axial torsion vertex: (3/2) gamma^mu gamma_5)
           |
          S_mu (external torsion)
```

Three fermion propagators, two vector vertices, one axial vertex.

**Zero by symmetry?** NO. This is the ABJ anomaly triangle.
Furry's theorem does not apply (gamma_5 insertion breaks C-symmetry
of the loop).

**Generated operator:**

```
L_VVA = (e^2 / 8 pi^2) * (3/2) * (sum_f Q_f^2) * S_mu epsilon^{mu nu alpha beta} A_nu partial_alpha A_beta
      = (e^2 / 8 pi^2) * (3/2) * (sum_f Q_f^2) * S_mu K^mu_{CS}
```

where K^mu_{CS} = epsilon^{mu nu alpha beta} A_nu F_{alpha beta} / 2 is
the Chern-Simons current and the sum is over fermion species with
electric charge Q_f.

This IS the standard ABJ anomaly with the axial current replaced by
the torsion coupling.

**After torsion elimination:** S_mu -> -(kappa/4) C(gamma) J^5_mu.
The operator becomes:

```
L_eff = -(3 e^2 kappa / 32 pi^2) * C(gamma) * (sum_f Q_f^2)
        * J^5_mu K^mu_{CS}
```

This is a FOUR-POINT operator: two fermion fields (in J^5) and two
photon fields (in K_{CS}). It requires matter to be present.

**Parity:** ODD (birefringent). Correct structure for polarization rotation.

**Cosmological relevance:** Requires <J^5_mu> != 0. Dead on FRW with
unpolarized matter.

---

### Diagram 2: VVS Bubble (One-Loop, Scalar Torsion Insertion)

**Topology:** Fermion loop with two photon vertices and one scalar
insertion from the trace part of torsion.

**Zero by symmetry?** YES, for Dirac fermions. The trace part of torsion
couples as T_mu psi-bar gamma^mu psi (vector coupling). A VVV triangle
with three vector insertions vanishes by Furry's theorem (charge conjugation).

Actually, the trace torsion is zero for Dirac fermions (only the axial
part is sourced). So this diagram is absent entirely.

**VERDICT: Zero (trace torsion not sourced).**

---

### Diagram 3: VVAA Box (One-Loop)

**Topology:** Fermion loop with two photon vertices and two axial
torsion vertices.

```
   A --- [fermion] --- S
   |                   |
   [fermion]      [fermion]
   |                   |
   A --- [fermion] --- S
```

Four fermion propagators, two vector vertices (e gamma^mu), two
axial vertices ((3/2) gamma^mu gamma_5).

**Zero by symmetry?** Not obviously zero. But:

- Two axial insertions: gamma_5 * gamma_5 = 1. The net effect is
  TWO vector-like insertions (axial x axial = vector). Combined with
  two actual vector insertions: VVVV box.
- By Furry's theorem, a loop with an EVEN number of (effectively)
  vector insertions is NOT zero.

**Generated operator:**

```
L_box ~ (e^2 g_axial^2 / (4pi)^4) * S_mu S_nu * T^{mu nu}_{alpha beta} * F^{alpha beta} F^{gamma delta}
```

The tensor structure: with two S and two F, the possible structures are:
- S^2 F^2: parity-even (S_mu S^mu is a scalar, F^2 is a scalar)
- S^2 F F-tilde: parity-odd only if there is an epsilon tensor from
  the loop. But with two gamma_5 insertions (even number), the loop
  trace has NO net epsilon tensor.

**The box with two axial insertions is parity-EVEN.** It generates
S^2 F^2 type corrections to the photon propagator, NOT birefringence.

After torsion elimination: S_mu -> const * J^5_mu. This becomes
(J^5)^2 F^2, which is just a correction to the photon kinetic term
in the presence of a chiral medium. Non-birefringent.

**VERDICT: Nonzero but parity-even. Does not produce birefringence.**

---

### Diagram 4: Modified Propagator — Bubble with (J^5)^2 Insertion

**Topology:** In the torsion-eliminated theory, consider the fermion
propagator modified by the (J^5)^2 four-fermion vertex (mean-field
or Hartree-Fock approximation):

```
G(p) = G_0(p) + G_0(p) * Sigma_{4f} * G_0(p) + ...
```

where Sigma_{4f} is the self-energy from the (J^5)^2 interaction
(tadpole or exchange diagram).

The tadpole gives:

```
Sigma_tadpole ~ G_torsion * <J^5_mu> * gamma^mu gamma_5
```

If <J^5_mu> = 0 (no chiral asymmetry), the tadpole vanishes.

The exchange (Fock) term gives a momentum-dependent self-energy
that modifies the fermion propagator. Using this modified propagator
in the standard vacuum polarization bubble:

```
   A --- [modified fermion] --- A
   |                            |
   [modified fermion]           |
   |____________________________|
```

**Zero by symmetry?** The Fock self-energy from (J^5)^2 is
parity-even (since (J^5)^2 is parity-even). A parity-even
modification of the fermion propagator in a two-vector-vertex
bubble gives a parity-even result: correction to F^2, not F F-tilde.

**VERDICT: Parity-even. Non-birefringent.**

---

### Diagram 5: Two-Loop Pure Photon Operator

**Topology:** Integrate out ALL fermions to get a pure photon
effective action.

```
Loop 1: fermion bubble with (J^5)^2 vertex and some structure
Loop 2: fermion bubble with two photon legs
Connected via the (J^5)^2 vertex
```

Concretely, the leading two-loop diagram connecting (J^5)^2 to
photons is:

```
[fermion loop: J^5_mu] ---(J^5)^2 vertex--- [fermion loop: J^5_nu, A_alpha, A_beta]
```

The left loop produces <J^5_mu> (vacuum expectation of axial current).
In the vacuum: <J^5_mu> = 0 by Lorentz invariance and parity.

Even if evaluated in a thermal/dense medium, the connection between
the two loops is through the parity-even (J^5)^2 vertex. The generated
pure photon operator is parity-even (F^2 correction).

**VERDICT: Zero in vacuum. Parity-even in medium. Non-birefringent.**

---

### Diagram 6: Graviton-Mediated Diagrams

**Topology:** Fermion loop with one or two graviton vertices and
photon vertices.

These exist in ANY theory of gravity + fermions + photons (GR
included). They are not ECH-specific. The ECH modification enters
only through:
(a) The contortion coupling (Diagram 1 above)
(b) Modified graviton propagator from torsion

In the minimal ECH model, torsion is non-propagating, so (b) does
not exist — the graviton propagator is identical to GR.

**VERDICT: Not ECH-specific. Standard GR + QED effect.**

---

## Master Diagram Table

| # | Topology | Loop order | Parity | Zero? | Birefringent? | Pure photon? | ECH-specific? |
|---|----------|-----------|--------|-------|--------------|-------------|---------------|
| 1 | VVA triangle | 1 | ODD | NO | YES | NO (needs S_mu/J^5) | YES (via S elimination) |
| 2 | VVS bubble | 1 | — | YES (no source) | — | — | — |
| 3 | VVAA box | 1 | EVEN | NO | NO | NO | YES |
| 4 | Modified propagator | 1+mean field | EVEN | Conditional | NO | NO | YES |
| 5 | Two-loop pure photon | 2 | EVEN | YES (in vacuum) | NO | YES but zero | YES |
| 6 | Graviton-mediated | 1+ | EVEN | NO | NO | YES | NO |

---

## The Critical Conclusion from the Diagram Map

```
+--------------------------------------------------+
|                                                    |
|  ONLY Diagram 1 (VVA triangle) produces a          |
|  birefringent operator.                            |
|                                                    |
|  Diagram 1 requires an external torsion field      |
|  S_mu, which after elimination equals const*J^5.   |
|                                                    |
|  ALL other diagrams are parity-even and cannot     |
|  produce birefringence at any order.               |
|                                                    |
|  There is NO pure-photon birefringent operator.    |
|  Birefringence requires matter with J^5 != 0.     |
|                                                    |
+--------------------------------------------------+
```

The diagram map confirms the symmetry analysis (File 03):
the VVA triangle is the ONLY route to birefringence, and it
requires a macroscopic chiral asymmetry that does not exist in
the standard cosmological background.
