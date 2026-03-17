# Branch S: Photon-Torsion Vertex — Phase 1 Results

**Date:** 2026-03-16

---

## Verdict: PHOTON_TORSION_VERTEX_CONDITIONAL

More precisely: the vertex EXISTS at one loop but is COSMOLOGICALLY DEAD.

---

## What Was Computed

The one-loop photon-torsion vertex in the minimal Einstein-Cartan-Holst
(ECH) framework. Specifically: the VVA (vector-vector-axial) triangle
diagram with two QED photon vertices and one axial torsion-fermion vertex.

---

## Key Results

### 1. The vertex EXISTS at one loop

The VVA triangle is nonzero. It is the standard Adler-Bell-Jackiw (ABJ)
anomaly triangle with the axial current sourced by torsion instead of
an external gauge field.

The effective operator is:

```
L_eff = C_eff * J^5_mu * K^mu_{CS}
```

where:
- J^5_mu = psi-bar gamma_mu gamma_5 psi (axial current)
- K^mu_{CS} = (1/2) epsilon^{mu nu alpha beta} A_nu F_{alpha beta} (Chern-Simons current)
- C_eff = (3 alpha_{EM} kappa) / (2 pi) * C(gamma) * (sum_f Q_f^2)
- C(gamma) = gamma^2 / (1 + gamma^2)
- sum_f Q_f^2 = 8 (three SM generations)

Numerically: C_eff ~ 10^{-41} GeV^{-2} (Planck-suppressed).

### 2. The operator is PARITY-ODD (birefringent)

The VVA triangle generates a parity-odd operator, which is the correct
structure for cosmic birefringence. It rotates left- and right-circular
polarizations of photons differently.

### 3. The vertex is the STANDARD ABJ anomaly (NOT ECH-specific)

The anomaly coefficient is determined by the fermion charge assignments
only. It is:
- Independent of the Barbero-Immirzi parameter gamma (the anomaly coefficient is universal)
- Independent of the gravitational theory (same in GR, EC, or flat space)
- The SAME operator that any axial vector coupling would generate

The ECH-specific content is limited to:
- The coupling constant g_axial = 3/2 at the torsion-fermion vertex
- The coefficient C(gamma) from the torsion equation of motion
- The identification of the external field S_mu with the fermion axial current J^5_mu

None of these modify the OPERATOR STRUCTURE. They only affect the
overall coefficient of a standard operator.

### 4. After torsion elimination: requires MATTER (J^5 != 0)

The external torsion S_mu is algebraically determined by J^5_mu.
After substitution, the operator requires a nonzero fermion chiral
density. It is NOT a pure photon operator.

There is NO pure photon birefringent operator at any loop order in
the torsion-eliminated theory, because the four-fermion interaction
(J^5)^2 is parity-EVEN. This is a STRUCTURAL result.

### 5. Cosmologically DEAD: J^5 = 0 in the standard universe

At every cosmological epoch relevant for CMB birefringence:
- Recombination (z ~ 1100): fermions are non-relativistic, n_5 ~ (v/c) n_e ~ 10^{-3} n_e
- Post-recombination: neutral universe, very few free fermions
- Late universe: n_5 -> 0

Even with the most generous estimate of n_5, the birefringence angle is:

```
beta_ECH ~ 10^{-30} degrees
```

The observed birefringence is beta ~ 0.35 degrees.

**The ECH prediction is 28-40 ORDERS OF MAGNITUDE too small.**

### 6. The result is regularization-independent and exact

The Adler-Bardeen theorem guarantees that the one-loop anomaly
coefficient is exact (no higher-loop corrections). The result is
independent of the regularization scheme.

---

## Why the Verdict is CONDITIONAL (Not ZERO)

The vertex is technically nonzero at one loop — the diagram exists
and gives a finite, unambiguous result. In a hypothetical universe
with a large chiral asymmetry, the operator would produce birefringence.
The reason it fails is cosmological (no chiral density), not algebraic
(the operator itself is fine).

However, "CONDITIONAL" should not be misread as "promising." The
conditions required for the operator to produce observable birefringence
(macroscopic J^5 != 0 at 10^{30} times the baryon asymmetry level)
are physically impossible in the standard cosmological history.

---

## The Three Independent Kills

The birefringence program is killed three times over:

```
+--------------------------------------------------+
|                                                    |
|  KILL 1: PLANCK SUPPRESSION                        |
|  The coupling C_eff ~ alpha/(pi M_Pl^2) is         |
|  40 orders of magnitude below what is needed.       |
|  This is Barrier 4 in a new context.                |
|                                                    |
|  KILL 2: NO CHIRAL DENSITY                          |
|  n_5 = 0 for all charged fermions at               |
|  recombination and after. The operator has no       |
|  cosmological source.                               |
|                                                    |
|  KILL 3: NOT ECH-SPECIFIC                           |
|  The operator is the standard ABJ anomaly.           |
|  Any axial coupling gives the same structure.        |
|  Even if the magnitude were right, it would          |
|  not be a distinctive ECH prediction.                |
|                                                    |
+--------------------------------------------------+
```

---

## The Ninth Barrier

This result establishes:

```
+--------------------------------------------------+
|                                                    |
|  BARRIER 9: Anomaly universality + Planck          |
|  suppression of the photon-torsion vertex           |
|                                                    |
|  The one-loop photon-torsion coupling is the        |
|  standard ABJ anomaly (not ECH-specific),           |
|  Planck-suppressed (C_eff ~ alpha/M_Pl^2),          |
|  and requires a cosmological chiral density          |
|  that does not exist.                                |
|                                                    |
|  No observable birefringence from minimal ECH.       |
|                                                    |
+--------------------------------------------------+
```

This joins the eight previously established barriers:

1. Mass-coupling lock (A)
2. Topological-shift duality (B)
3. Scalar-tensor universality (C)
4. Planck suppression (D)
5. Scale separation (E/H-tensor)
6. Attractor-sensitivity dilemma (F)
7. Parameter immunity (G)
8. Parity-even effective interaction (H-parity)
9. **Anomaly universality + Planck suppression (S)**

---

## Implications for the Program

### The birefringence route is CLOSED

The salvage audit identified this as the single remaining positive
path. It is now closed. The ECH framework cannot explain the
observed cosmic birefringence.

The consistency noted in the salvage audit — that the ECH coupling
scale requires f_photon ~ O(1) — was a coincidence of dimensional
analysis, not a physical prediction. The actual one-loop calculation
shows that f_photon is not a free parameter: it is determined by
the ABJ anomaly coefficient and is the same for ANY theory with the
same fermion content. The "O(1)" compatibility was comparing apples
to oranges.

### What remains

After this closure, the project status is:

| Component | Status |
|-----------|--------|
| Dark energy derivation | CLOSED (7 barriers) |
| Bounce observables | CLOSED (8+ barriers) |
| Tension reduction | CLOSED (MCMC verification) |
| Birefringence | **CLOSED (this calculation)** |
| Closure paper (Paper 1.2) | VIABLE (the negative result is publishable) |

The closure paper is the sole remaining output. This result (Barrier 9)
should be added to it.

---

## Assessment Against Success Criteria

| Criterion | Met? |
|-----------|------|
| Nonzero one-loop vertex | **YES** (formally) |
| Generates F F-tilde (birefringent) | **YES** (formally) |
| Gamma-dependent (ECH-specific) | **NO** (anomaly coefficient is universal) |
| Background nonzero on FRW | **NO** (J^5 = 0) |
| Observable magnitude | **NO** (28+ orders too small) |

**One of five criteria met (vertex exists). Four of five failed.**

The single "success" (vertex exists) is Pyrrhic: the vertex exists
in the same sense that any axial coupling generates the ABJ anomaly.
There is no ECH-specific content.

---

## Exact Next Move

1. Add Barrier 9 to Paper 1.2 manuscript
2. Update the barrier count from 14 to 15 (or renumber as appropriate)
3. Finalize and submit Paper 1.2 as a comprehensive closure paper
4. No further calculations are warranted in the ECH program
5. The birefringence observation (beta ~ 0.35 deg) should be attributed
   to physics beyond the minimal ECH framework (most likely an ALP or
   early dark energy model)

---

## Summary Table

| Item | Result |
|------|--------|
| One-loop vertex exists? | **YES** (ABJ anomaly triangle) |
| Operator structure | J^5_mu * K^mu_{CS} (axial current times Chern-Simons current) |
| Parity | ODD (birefringent) |
| ECH-specific? | **NO** (standard ABJ anomaly, universal coefficient) |
| Pure photon operator? | **NO** (requires matter with J^5 != 0) |
| Gamma-dependent? | Only through overall coefficient, not anomaly |
| Cosmological source? | **NO** (n_5 = 0 at recombination and after) |
| Predicted beta | ~ 10^{-30} degrees |
| Observed beta | 0.35 +/- 0.09 degrees |
| Gap | **28-40 orders of magnitude** |
| Regularization-independent? | YES (Adler-Bardeen theorem) |
| Verdict | **PHOTON_TORSION_VERTEX_CONDITIONAL** |
| Meaning | Vertex exists formally; cosmologically dead |
| Barrier number | 9 (Anomaly universality + Planck suppression) |
| Birefringence route | **CLOSED** |
| Program status | **COMPREHENSIVELY CLOSED** |
