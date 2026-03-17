# Single Best Next Move

**Date:** 2026-03-16

---

## The Choice: Program 3 (Hybrid -- Closure Paper + Photon-Torsion Vertex)

---

## Why This Is Best

The hybrid program dominates every alternative on expected value. Here is the argument:

**Against the closure paper alone (Program 1):** The closure paper is ready and should be submitted. But submitting it alone leaves the birefringence question unaddressed. The Track C analysis already identified f_photon as the single critical unknown, and the one-loop calculation is well-defined. Not attempting it is leaving value on the table.

**Against the vertex alone (Program 2):** The vertex calculation might fail (f_photon = 0). Without the closure paper as a fallback, a null vertex result produces only a minor negative result instead of a comprehensive assessment.

**Against updated MCMC (Candidate A):** The Cobaya verification already showed Delta-Neff is consistent with zero. Updating the data does not fix this. The model is Lambda-CDM + one irrelevant parameter.

**Against galaxy spin (Candidate C):** High-effort observational pipeline engineering with uncertain foundations (Shamir's dipole may not be real) and no theory content specific to ECH.

**Against modified gravity phenomenology (Candidate E):** The program's own structural lessons (Lessons 1-6) argue that ECH phenomenology is indistinguishable from generic scalar-tensor/ALP on FRW backgrounds.

---

## Why It Reuses Existing Work

The hybrid program has the highest reuse factor of any candidate:

1. **Paper 1.2 manuscript** (2053 lines): 90%+ complete, needs only final integration check and editorial pass
2. **14 branch derivation directories**: All results exist and are documented
3. **Track C birefringence pipeline**: Scripts, figures, model-to-observable map, consistency window
4. **MCMC verification chains**: 300,000+ samples across 4 dataset combinations
5. **ECH reduced action**: Fully derived, documented, with structural analysis
6. **Literature base**: 35+ references already compiled and cited

The ONLY new work is the one-loop vertex calculation, which is a single well-defined QFT computation.

---

## What Exact Calculation/Test to Run First

### Day 1-2: Literature Gate

Check whether the photon-torsion vertex has already been computed in the literature:

1. Review Shapiro 2002 (Phys. Rept. 357) for one-loop photon-graviton-torsion vertices
2. Review Shapiro & Teixeira 2014 for ECH-specific one-loop structure
3. Check whether the standard ABJ (Adler-Bell-Jackiw) anomaly with contorsion insertions has been computed
4. Search for "torsion birefringence one-loop" in arXiv

If the calculation already exists in the literature, extract the result and apply it. If not, proceed to the computation.

### Day 3-5: Structural Quick Check

Before computing, answer this structural question:

After torsion elimination, the reduced ECH action is S_EH[g] + S_Dirac[g,psi] + S_4f[psi;BI]. Add photons: S_Maxwell[g,A]. The question: does the fermion loop with external photon legs and internal BI-dependent four-fermion vertices generate a BI-dependent F * F-tilde term?

The Branch G v1 result showed that the Dirac operator is BI-independent (it is the standard Levi-Civita operator). But the four-fermion interaction IS BI-dependent. At one loop, the four-fermion interaction does not contribute to the fermion determinant (it is quartic). But at TWO loops (or one loop with four-fermion vertex insertions treated as effective background), it could generate photon vertices.

The critical diagram: fermion triangle with two (J5)^2 vertex insertions and one photon vertex. This is equivalent to the standard axial anomaly triangle with the axial current sourced by the BI-dependent coupling constant.

If the coefficient of F * F-tilde is proportional to G_eff(BI) rather than the standard gravitational coupling, then f_photon is nonzero and BI-dependent. If it is proportional to the standard coupling (BI-independent), then f_photon = 0 in the ECH-specific sense.

THIS CHECK CAN BE DONE BY POWER-COUNTING IN DAYS, NOT WEEKS.

### Week 2-3: Full Calculation (if gate passes)

If the structural check indicates a nonzero BI-dependent vertex is possible, perform the full calculation:
- Compute the one-loop effective action for photons in the ECH background after torsion elimination
- Extract the coefficient of F * F-tilde as a function of BI
- Evaluate numerically for BI = 0.274
- Compare with the consistency window: is f_photon in the range 0.1-10?

### Concurrent: Paper 1.2 Finalization

While the vertex calculation proceeds:
- Review Paper 1.2 for completeness (Branches N, O, P integration)
- Final editorial pass
- Compile PDF, verify references
- Prepare PRD submission

---

## What Kills It

Two kill conditions:

**Kill 1 (Vertex = 0):** The one-loop photon-torsion vertex vanishes. This likely happens if the BI-dependent four-fermion interaction does not contribute to the photon effective action at one loop (which is the most probable outcome based on the Branch G v1 result). In this case, the birefringence program is dead and the closure paper is submitted alone. The null vertex result is added as Barrier 15.

**Kill 2 (f_photon far from O(1)):** The vertex is nonzero but f_photon is extremely small (< 10^{-6}) or extremely large (> 10^6), placing the prediction outside the consistency window. The ECH framework would then be inconsistent with observed birefringence, which is itself an interesting negative result.

Neither kill condition affects the closure paper, which is submitted regardless.

---

## What Would Be a Real Positive Win

**f_photon comes out O(0.1-10) from a first-principles one-loop calculation.**

This would mean:
1. The ECH framework makes a SPECIFIC, DERIVED prediction for cosmic birefringence
2. The prediction is CONSISTENT with current data (beta ~ 0.2-0.4 deg)
3. The prediction is TESTABLE by LiteBIRD (launch ~2028, sigma(beta) ~ 0.01 deg)
4. The prediction is DISTINGUISHABLE from generic ALP models (because the coupling constant is BI-dependent and BI is fixed by LQG)

This would be the first first-principles prediction for cosmic birefringence from a specific quantum gravity theory, anchored by a comprehensive closure of all other ECH cosmological predictions. It would transform the program from "everything is dead" to "everything is dead EXCEPT this one specific, testable prediction."

That is a real scientific contribution, not a relabeling of failure.

---

## No Hedging

I am not recommending this because it is emotionally satisfying or because it rescues the program. I am recommending it because:

1. The closure paper is ready and should be submitted regardless
2. The vertex calculation is well-defined and tractable (1-3 weeks)
3. The probability of a positive vertex result is nontrivial (~30-50%)
4. Even a null result produces value (Barrier 15)
5. No other candidate program has comparable expected value per unit effort
6. The existing infrastructure (Track C) directly supports the follow-through

The program has earned the right to attempt this one calculation before closing the book entirely.
