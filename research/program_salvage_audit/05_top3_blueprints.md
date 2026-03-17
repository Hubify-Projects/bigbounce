# Top 3 Program Blueprints

**Date:** 2026-03-16

---

## Program 1: Comprehensive Closure Paper (Paper 1.2 Completion)

### Exact scientific question
Does the minimal Einstein-Cartan-Holst framework (with or without PGT extensions) produce any distinctive, observable cosmological consequences?

### Exact output
A single paper (~30 pages, PRD format) presenting:
- Part I: The phenomenological ansatz and its MCMC fits (reframed as consistency checks, not predictions)
- Part II: The systematic failure of 11 derivation/foundation routes (7 barriers)
- Part III: The comprehensive null result across all perturbation channels (7 additional barriers)
- Total: 14 structural barriers, 10 research branches, 5 failure modes
- Conclusion: The spin-torsion bounce is theoretically consistent but observationally inert

### What from Paper 1/1.2 is reusable
- Paper 1.2 manuscript (2053 lines, ~90% complete)
- All branch derivations (tensor spectrum, scalar transfer function, Horndeski stability, state selection, UV-IR bridge, PGT parameter space, baryogenesis, hidden-sector vacuum, torsion relic)
- MCMC verification results (Cobaya chains)
- Birefringence consistency window (Track C)

### Minimal new ingredient
- Integration of Branch N/O/P results into the manuscript (may already be done or nearly done)
- One final editorial pass for consistency and completeness
- Updated bibliography (Liu et al. 2025, Legner et al. 2025, Fabbri 2025 are already cited)

### First cheap test
Review Paper 1.2 main.tex end-to-end for completeness. Check whether Branches N, O, P are fully integrated. Compile PDF and verify 0 undefined references.

### First expensive test
Not applicable -- no new calculations needed.

### Quick-kill condition
None. This program cannot fail. The work is done.

### What counts as a win
Accepted publication in PRD or JCAP. The paper establishes the scientific status of spin-torsion bounce cosmology definitively, saving other researchers from pursuing closed directions.

---

## Program 2: Photon-Torsion Vertex Calculation

### Exact scientific question
Does the ECH effective action generate a nonzero photon-polarization rotation at one loop? Specifically: after integrating out torsion and fermion loops with an external photon propagator in the ECH background, is there a term of the form (alpha_eff / f) * F * F-tilde that produces cosmic birefringence?

### Exact output
Either:
- (a) A nonzero vertex f_photon, yielding a first-principles prediction: beta = f_photon * [(alpha/M) * M_Pl] * Delta-tau_eff. Combined with the observed beta = 0.242 +/- 0.061 deg, this constrains the ECH coupling. Publishable as a short letter (PRL or JCAP Letters).
- (b) A zero vertex, establishing Barrier 15: "No radiative photon-torsion coupling in minimal ECH." This is an additional no-go result, publishable as an addendum to the closure paper.

### What from Paper 1/1.2 is reusable
- Track C consistency window analysis (scripts, figures, model-to-observable map)
- ECH reduced action derivation (Paper 1.2 Secs. 2-3)
- One-loop structure analysis (Branch G v1 result: the Dirac operator is BI-independent after torsion elimination)
- Literature on Holst term + fermion loops (Freidel et al. 2005, Shapiro & Teixeira 2014, Mercuri 2009)

### Minimal new ingredient
The one-loop Feynman diagram: fermion triangle with one external photon vertex and two contorsion insertions (from the four-fermion interaction after Fierz rearrangement, or equivalently from the torsion-fermion vertex before elimination). The calculation uses standard heat kernel or dimensional regularization technology.

Specifically:
1. Write the ECH-fermion-photon system in the reduced action (torsion eliminated)
2. The four-fermion term (J5)^2 generates, at one loop, an effective operator coupling to F * F-tilde via the axial anomaly triangle
3. Compute the coefficient. The key question: does the BI-dependent prefactor in the four-fermion coupling survive into the one-loop effective action for photons?

### First cheap test
Literature search for existing calculations of one-loop photon vertices in Einstein-Cartan gravity. Check whether the axial anomaly triangle (fermion loop with two gravitational/torsion vertices and one photon vertex) has been computed. Specifically check Shapiro & Teixeira 2014 and the review by Shapiro 2002 (Phys. Rept. 357).

### First expensive test
Explicit calculation of the triangle diagram. This is a standard QFT calculation (axial anomaly in curved spacetime with torsion), not a numerical simulation. Estimated effort: 1-3 weeks for a careful computation.

### Quick-kill condition
If the Branch G v1 result (Dirac operator is BI-independent) extends to the photon sector -- i.e., if the four-fermion interaction does not generate BI-dependent photon vertices at one loop because the contorsion has already been integrated out before the fermion loop is performed -- then the vertex is zero by construction. This can be checked in days by examining the operator ordering.

IMPORTANT WARNING: Route S1 already noted "no photon coupling" in the minimal ECH action. The question is whether this extends to one loop. The four-fermion (J5)^2 interaction is a current-current contact term; the axial anomaly could generate F * F-tilde through the standard ABJ mechanism. But if torsion is already eliminated (reduced action), the four-fermion term is just a standard NJL-type interaction, and its one-loop photon vertex is the standard axial anomaly -- which is BI-independent.

This is the critical gate: if the one-loop vertex reduces to the standard QED axial anomaly (BI-independent), then f_photon = 0 in the ECH-specific sense, and the birefringence is identical to any theory with the same fermion content. The ECH framework adds nothing.

### What counts as a win
- f_photon nonzero AND O(0.1-10): The ECH framework makes a specific, testable prediction for cosmic birefringence distinguishable from the standard axial anomaly. This would be a genuine positive result.
- f_photon = 0: Clean no-go (Barrier 15). Birefringence requires physics beyond ECH. This is still valuable but not a positive program.

---

## Program 3: Hybrid Publication Strategy (Programs 1 + 2 Combined)

### Exact scientific question
Two questions, pursued in parallel:
1. What is the complete scientific status of spin-torsion bounce cosmology? (Program 1)
2. Does the surviving open question (photon-torsion vertex) yield a positive result? (Program 2)

### Exact output
- Paper A (certain): The comprehensive closure paper (Paper 1.2), submittable within weeks
- Paper B (conditional): If f_photon is nonzero, a short letter predicting cosmic birefringence from ECH gravity

### What from Paper 1/1.2 is reusable
Everything from Programs 1 and 2 combined:
- Paper 1.2 manuscript
- All branch results
- Track C birefringence infrastructure
- MCMC verification chains
- ECH action derivations

### Minimal new ingredient
The one-loop vertex calculation (same as Program 2). This is pursued WHILE the closure paper is being finalized.

### First cheap test
(a) Review Paper 1.2 for completeness -- can be done today.
(b) Literature check on photon-torsion vertex -- can be done today.

### First expensive test
The vertex calculation (1-3 weeks).

### Quick-kill condition
For Paper B only: vertex is zero. Paper A is unaffected.

### What counts as a win
- Minimum win: Paper A accepted (closure paper). This is near-certain.
- Maximum win: Paper A accepted + Paper B accepted (closure + birefringence prediction). Two publications from the same program.
- Expected outcome: 1.4-1.5 papers (Paper A certain, Paper B ~40-50% chance).

### Timeline

| Week | Activity |
|------|----------|
| 1 | Review Paper 1.2 completeness. Literature search on vertex. Begin vertex calculation. |
| 2-3 | Vertex calculation. Finalize Paper 1.2 manuscript. |
| 4 | If vertex nonzero: write Paper B draft. Submit Paper A. |
| 5 | If vertex nonzero: finalize Paper B, prepare submission. |
| 5 (alt) | If vertex zero: add Barrier 15 to Paper A, submit enhanced closure paper. |

---

## Comparison

| Dimension | Program 1 | Program 2 | Program 3 |
|-----------|-----------|-----------|-----------|
| Certainty of output | 95%+ | 40-50% | 95%+ (Paper A) |
| Upside | 1 paper | 1 high-impact paper | 1-2 papers |
| New work required | Minimal | Moderate | Moderate |
| Timeline | 2-3 weeks | 3-5 weeks | 4-5 weeks |
| Risk | Near zero | Vertex might be zero | Near zero (Paper A hedges) |
| Reuse of existing work | Maximum | High | Maximum |
