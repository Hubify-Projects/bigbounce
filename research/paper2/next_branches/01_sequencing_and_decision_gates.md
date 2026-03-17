# Next-Stage Program — Sequencing and Decision Gates

**Date:** 2026-03-13

---

## Sequencing Table

| Week | S1 | T1 | S2 | T2 |
|------|----|----|----|----|
| 1–2 | Phase 1: mapping assessment | Phase 1: literature review | — | — |
| 2–3 | **Gate S1-1 decision** | Phase 1 continues | Phase 1: parameterization | — |
| 3–4 | Phase 2: pipeline (if S1-1 ✓) | **Literature assessment** | Phase 1 continues | — |
| 4–5 | Phase 2 continues | Phase 2: torsion elim. (if warranted) | **Gate S2-1 decision** | — |
| 5–6 | **Gate S1-2 decision** | **Gate T1-1 decision** | Phase 2: Boltzmann (if S2-1 ✓) | — |
| 6–8 | Phase 3: results (if S1-2 ✓) | Phase 3: V_eff (if T1-1 ✓) | Phase 2–3 continues | — |
| 8–10 | **Final S1 verdict** | Phase 4: viability (if T1-2 ✓) | **Final S2 verdict** | Assess T1 closure |
| 10–12 | — | **Final T1 verdict** | — | **Open? (conditional)** |

---

## Critical Path Analysis

```
Week 0                                          Week 12
  │                                                │
  ├── S1 ━━━━━━━━━[S1-1]━━━━━━━[S1-2]━━━[S1-3]    │
  │                                                │
  ├── T1 ━━━━━━━━━━━━━━[Lit]━━━[T1-1]━━━━━[T1-2]━[T1-3]
  │                                                │
  ├── S2 ━━━━━━━━━━━━━━━━━━[S2-1]━━━━[S2-2]━[S2-3]│
  │                                                │
  └── T2 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[Conditional]
```

- **S1** and **T1** can run in parallel from week 1
- **S2** starts 1–2 weeks after S1/T1 (lower priority, independent)
- **T2** starts only after T1 reaches a verdict

---

## Gate Dependencies

| Gate | Depends on | If PASS | If FAIL |
|------|-----------|---------|---------|
| S1-1 | Nothing | Proceed to S1-2 | Close S1 |
| S1-2 | S1-1 | Proceed to S1-3 | Close S1 |
| S1-3 | S1-2 | Publish constraint/consistency | Document null |
| T1-1 | Literature review | Proceed to T1-2 | Close T1; assess T2 trigger |
| T1-2 | T1-1 | Proceed to T1-3 | Close T1; document closure |
| T1-3 | T1-2 | Publish mechanism | — |
| S2-1 | Nothing | Proceed to S2-2 | Close S2 |
| S2-2 | S2-1 | Proceed to S2-3 | Close S2 |
| S2-3 | S2-2 | Publish feature constraint | Document null |
| T2 opening | T1 verdict | If T1 provides structural insight → open T2 | T2 stays closed |

---

## Decision Checkpoints

### Checkpoint 1 (Week 2–3): S1-1 + T1 Literature Assessment
**Decision:** Are S1 and T1 worth pursuing past Phase 1?
- If both fail Phase 1 → major reassessment needed
- If S1 passes, T1 fails → focus on signal branches
- If T1 passes, S1 fails → focus on theory branches
- If both pass → continue parallel pursuit

### Checkpoint 2 (Week 5–6): S1-2 + T1-1 + S2-1
**Decision:** Which branches have survived their first hard gate?
- Allocate effort to surviving branches
- Close failed branches with documented reasoning

### Checkpoint 3 (Week 8–10): Final verdicts
**Decision:** What is publishable?
- Surviving branches → draft papers/notes
- Failed branches → add to negative-result supplement
- T2 → open or leave closed based on T1 results

---

## Compute/Tool Notes by Branch

| Branch | Phase 1 | Phase 2 | Phase 3 |
|--------|---------|---------|---------|
| S1 | Literature only | Planck/ACT likelihoods, Python | MCMC (Cobaya) if needed |
| T1 | Literature only | SymPy symbolic, local CPU | NumPy/SciPy numerical |
| S2 | Literature + pen-and-paper | CAMB modifications, local CPU | MCMC (Cobaya), cloud CPU |
| T2 | Depends on T1 | SymPy symbolic | Depends on candidate |

**GPU needed:** None for any branch.
**Cloud CPU needed:** Only S2 Phase 3 and S1 Phase 2 if MCMC is required.

---

## Publication Pathways Summary

| Result class | Publication format |
|-------------|-------------------|
| S1 birefringence consistency check | Short letter (PRL/JCAP) |
| S1 birefringence constraint | Short letter |
| T1 new mechanism | Full paper or major supplement |
| T1 closure | Add to negative-result note |
| S2 feature constraint | Short letter or Paper 2 section |
| S2 null | Internal note |
| T2 any result | Depends on scope |
| All branches close | Expanded negative-result supplement |

---

## Most Promising Branch for Each Goal

| Goal | Best branch | Reasoning |
|------|------------|-----------|
| First-principles mechanism | T1 | Most structurally motivated new theory direction |
| Small but real cosmology signal | S1 | Birefringence is already detected; just need defensible mapping |
| Strongest publishable result even if negative | S1 | A constraint paper is fastest and most defensible |
| Deepest theoretical insight | T1 → T2 | Understanding WHY minimal routes fail informs future work |
