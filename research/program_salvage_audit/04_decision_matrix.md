# Decision Matrix: Candidate Program Scoring

**Date:** 2026-03-16

---

## Scoring Criteria (1-5 scale, 5 = best)

| Criterion | Description |
|-----------|-------------|
| **Novelty** | Does this produce something new that does not already exist in the literature? |
| **Reuse** | How much of the existing repo work (code, manuscripts, results) is directly leveraged? |
| **Tractability** | Can the first decisive test be completed in weeks, not months? |
| **Low speculative dependence** | Does the result depend on assumptions that might fail? (5 = minimal dependence) |
| **Chance of positive result** | What is the probability of a publishable positive outcome? |
| **Scientific importance** | If successful, how significant is the result for the field? |

---

## Scoring Table

| Criterion | A: Updated MCMC | B: Birefr. Vertex | C: Galaxy Spin | D: Closure Paper | E: Mod. Gravity | F: Hybrid B+D |
|-----------|:-:|:-:|:-:|:-:|:-:|:-:|
| Novelty | 1 | 4 | 2 | 4 | 2 | 5 |
| Reuse of existing work | 4 | 4 | 3 | 5 | 3 | 5 |
| Tractability | 5 | 3 | 2 | 5 | 3 | 4 |
| Low speculative dependence | 5 | 3 | 2 | 5 | 3 | 4 |
| Chance of positive result | 2 | 3 | 2 | 5 | 2 | 4 |
| Scientific importance | 1 | 4 | 2 | 3 | 2 | 4 |
| **TOTAL** | **18** | **21** | **13** | **27** | **15** | **26** |

---

## Score Justifications

### A: Updated MCMC (Total: 18)
- Novelty (1): Lambda-CDM + Delta-Neff is routine. Hundreds of papers do this.
- Reuse (4): Cobaya configs, RunPod scripts, chain analysis all reusable.
- Tractability (5): Straightforward parameter estimation. Days of GPU time.
- Speculative dependence (5): Pure data fitting -- no theory assumptions.
- Positive result (2): Delta-Neff will likely remain consistent with zero. No novel finding expected.
- Importance (1): One more Lambda-CDM extension fit in a sea of them.

### B: Birefringence Vertex (Total: 21)
- Novelty (4): The one-loop photon-torsion vertex in ECH gravity has not been computed. If nonzero, it gives a first-principles prediction for cosmic birefringence from a specific gravity theory.
- Reuse (4): Track C scripts, consistency window, literature registry all directly used.
- Tractability (3): One-loop calculation in curved spacetime with torsion. Well-defined but technically demanding. Heat kernel methods apply.
- Speculative dependence (3): Result depends on the vertex being nonzero. Route S1 noted "no photon coupling" in the minimal model, which is a warning sign. But the one-loop calculation has not been done explicitly.
- Positive result (3): ~40-50% chance the vertex is nonzero at one loop. If zero, the negative result is still clean and publishable.
- Importance (4): A first-principles prediction for cosmic birefringence from ECH gravity, testable by LiteBIRD/CMB-S4, would be a significant result.

### C: Galaxy Spin (Total: 13)
- Novelty (2): Galaxy spin chirality is an existing observational program. Adding ECH framing does not create novelty.
- Reuse (3): Monte Carlo sensitivity and parity model reusable. CNN pipeline needs rebuild.
- Tractability (2): Requires real galaxy images (50,000+), CNN retraining, systematic error control. Months of pipeline engineering.
- Speculative dependence (2): Depends on Shamir dipole being real (controversial). Depends on CNN being able to classify real galaxies (failed on synthetic).
- Positive result (2): Even if the dipole is confirmed, it does not test ECH specifically.
- Importance (2): Confirming/refuting galaxy spin dipole is interesting for observational cosmology but does not advance the theory program.

### D: Closure Paper (Total: 27)
- Novelty (4): No comparable comprehensive no-go catalog exists for spin-torsion bounce cosmology. 14 barriers across 10 branches is unprecedented.
- Reuse (5): Paper 1.2 is nearly complete. All branch results exist.
- Tractability (5): Write-up and submission. No new calculations needed.
- Speculative dependence (5): The barriers are proven results. No speculation.
- Positive result (5): Certainty of publishable output. The question is journal choice, not scientific validity.
- Importance (3): Comprehensive negative results serve the field by closing unproductive directions. But negative results have lower impact than positive predictions.

### E: Modified Gravity Phenomenology (Total: 15)
- Novelty (2): ECH as modified gravity competes with Chern-Simons, ALP models, and generic parity-violating gravity. No competitive advantage identified.
- Reuse (3): ECH action, reduced action, some birefringence work.
- Tractability (3): Systematic comparison requires Boltzmann code modifications or semi-analytic perturbation theory.
- Speculative dependence (3): Depends on ECH being distinguishable from alternatives. Route S1 suggests it is not.
- Positive result (2): The structural lessons argue against distinctive ECH phenomenology on FRW.
- Importance (2): One more modified gravity model in a crowded field.

### F: Hybrid B+D (Total: 26)
- Novelty (5): Combines the closure catalog (novel) with the vertex calculation (novel). The two-part structure (comprehensive closure + single surviving open question + calculation addressing it) is a compelling narrative.
- Reuse (5): Maximum reuse -- Paper 1.2 manuscript, Track C infrastructure, all branch results.
- Tractability (4): Closure paper is ready now. Vertex calculation is the only new work, and it is well-defined.
- Speculative dependence (4): The closure paper has zero speculative dependence. The vertex calculation has moderate dependence (it might vanish), but even a null result is clean.
- Positive result (4): Closure paper is certain. Vertex has ~40-50% chance. Expected value: 1.4-1.5 papers.
- Importance (4): If the vertex is nonzero, this becomes the first first-principles cosmic birefringence prediction from a specific quantum gravity theory, anchored by a comprehensive assessment of what the theory cannot do.

---

## Final Ranking

| Rank | Candidate | Score | Assessment |
|------|-----------|-------|------------|
| 1 | **D: Closure Paper** | **27** | Highest certainty. Ready now. |
| 2 | **F: Hybrid (B+D)** | **26** | Highest expected value. Best narrative. |
| 3 | B: Birefringence Vertex | 21 | Highest upside if positive. |
| 4 | A: Updated MCMC | 18 | Safe but scientifically empty. |
| 5 | E: Modified Gravity | 15 | No competitive advantage. |
| 6 | C: Galaxy Spin | 13 | High effort, uncertain foundations. |

**Note:** D and F are separated by 1 point. The difference is that F has higher upside but slightly more risk (the vertex might vanish). If risk tolerance is low, D is optimal. If risk tolerance is moderate, F dominates because the closure paper component has the same certainty as D, and the vertex calculation adds pure upside.
