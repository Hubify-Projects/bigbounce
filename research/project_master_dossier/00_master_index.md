# Project Master Index

## Project Intelligence Dossier — Spin-Torsion Cosmology Research Program

**Generated:** 2026-03-17
**Author:** Houston Golden
**Repository:** `/Users/houstongolden/Desktop/CODE_2026/bigbounce/`

---

## Project Overview

This research program investigates whether Einstein-Cartan spin-torsion gravity can produce observable cosmological signatures — particularly dark energy, cosmic birefringence, and bouncing-cosmology imprints. Beginning with an ambitious hypothesis that torsion-induced quantum bounce effects could derive dark energy from first principles, the program systematically tested every viable theoretical route through 7 foundation studies and 17+ branches. The core finding is a rigorous negative result: 13 structural barriers close all minimal routes from bounce to dark energy. However, the program produced two genuinely positive results — a spectator ALP birefringence prediction matching observed data at 1-sigma, and a matter-bounce phenomenology framework (Branch V) with parameter-free predictions testable by SPHEREx. The program also generated a complete MCMC reproducibility infrastructure with 300,000+ posterior samples across 4 dataset combinations.

---

## Current Top-Level Status

| Dimension | Status |
|-----------|--------|
| Paper 1 (main manuscript) | v1.6.0-preaudit; 31pp, arXiv-ready, claims locked |
| Structural closure (Foundations A-G) | COMPLETE — 7 barriers established |
| Extended closure (Branches H-O) | COMPLETE — 6 additional barriers (13 total) |
| ALP birefringence (Branch R) | PROMISING — Phase 2 MCMC initiated |
| Matter bounce phenomenology (Branch V) | ACTIVE — Phase 1 blueprint ready |
| MCMC infrastructure | 2 datasets FROZEN, 2 running/paused |
| Next-gen bounce signals | CLOSED — frequency gate failed |
| Chiral GW program | CLOSED — GHz signals permanently inaccessible |

---

## Major Program Eras

### Era 1 — Original Paper 1 (2025-07 to 2026-03-02)
Initial hypothesis: ECH torsion bounce derives dark energy. Built framework, ran MCMC, wrote 31-page paper. Multiple peer review rounds revealed internal contradictions and overclaims.

### Era 2 — Derivation / Closure Testing (2026-03-02 to 2026-03-14)
Systematic test of all 4 routes to w = -1. Track B (condensate), Branch G v1 (one-loop), Route T1 (scalar reduction), Route S1 (ALP reduction) — all closed. IR vacuum program compiled negative-result supplement.

### Era 3 — Foundations A-G / Paper 1.2 Salvage (2026-03-13 to 2026-03-15)
Seven foundations tested propagating torsion, lock-breaking, environmental mass, disformal couplings, global vacuum, initial conditions, and cyclic vacuum selection. All closed with named structural barriers. Paper 1.2 restructured around honest closure.

### Era 4 — Post-AG Pivot / Branches H-O (2026-03-15 to 2026-03-16)
Pivot to bounce-only early-universe program. Eight new branches tested tensor spectrum, compatibility, state selection, scalar perturbations, UV-IR bridge, PGT GW, baryogenesis, and hidden-sector vacuum. Six additional barriers identified. Total: 13.

### Era 5 — ALP Birefringence / Next-Gen Search (2026-03-16 to 2026-03-17)
Branches P-W tested parity violation, ALP phenomenology, photon-torsion vertex, axion bridge, two-field models, bounce evidence, perturbation gate, and curvaton tilt. Branch R (ALP birefringence) emerged as strongest surviving positive result. Branch V (generic matter-bounce (LQC-viable)) identified as flagship future direction. Chiral GW frequency gate failed.

---

## Dossier Navigation

| File | Contents |
|------|----------|
| [01_project_timeline.md](01_project_timeline.md) | Chronological history of the research program |
| [02_branch_registry.md](02_branch_registry.md) | Structured registry of all branches/foundations with status |
| [03_deliverables_inventory.md](03_deliverables_inventory.md) | All deliverables grouped by type |
| [04_reproducibility_assets.md](04_reproducibility_assets.md) | MCMC chains, configs, scripts, validation docs |
| [05_results_matrix.md](05_results_matrix.md) | High-signal matrix: one row per scientific attempt |
| [06_novelty_assessment.md](06_novelty_assessment.md) | Honest novelty ratings with justifications |
| [07_publication_packaging_options.md](07_publication_packaging_options.md) | How to package the work into papers |
| [08_open_questions_and_next_moves.md](08_open_questions_and_next_moves.md) | What is open, dead, or worth doing next |
| [09_file_nav_map.md](09_file_nav_map.md) | Key file paths organized by function |
| [10_status_legend.md](10_status_legend.md) | Consistent labels for status, novelty, and publication potential |
| [index.html](index.html) | Interactive HTML dashboard |

---

## Where to Start (for a future collaborator)

1. **Understand the question:** Read `research/paper_1_2_archive/01_model_reconsideration_memo.md` for why the original dark energy derivation failed and what replaced it.

2. **See the barrier map:** Read `05_results_matrix.md` in this dossier — it shows every scientific attempt, its result, and its status in one table.

3. **Understand what survives:** Two positive results survive:
   - **ALP birefringence** (Branch R): spectator ALP predicts beta = 0.27 deg, observed 0.35 +/- 0.09 deg. Files in `research/branch_R_alp_birefringence/`.
   - **Generic matter-bounce (LQC-viable)** (Branch V): dust contraction through matter contraction produces f_NL = -35/8 = -4.375, testable by SPHEREx. Files in `research/branch_V_bounce_evidence/`.

4. **Run the MCMC:** Reproducibility bundle is in `reproducibility/`. Start with `reproducibility/README.md`. Frozen chains are in `reproducibility/cosmology/paper1_clean_restart_sync/chains/dneff/`.

5. **Read the manuscript:** Canonical source is `arxiv/main.tex`. Claims table is in Appendix K. Known gaps are in `reproducibility/docs/KNOWN_GAPS.md`.

6. **See what failed:** Foundations A-G in `research/foundation_*/` each have a `phase1_results.md` explaining the structural barrier. Branches H-O in `research/branch_*/` each have a `phase1_results.md`. The joint barrier catalog is in the results matrix.

---

## What This Project Has Genuinely Established

1. The minimal Einstein-Cartan-Holst framework produces a well-defined quantum bounce at rho_crit ~ 0.27 rho_Pl.
2. The (J^5)^2 four-fermion interaction from torsion integration is mathematically correct and unique.
3. All 4 minimal routes to deriving w = -1 from the bounce are structurally closed (IR vacuum program).
4. 13 independent structural barriers close all standard mechanism classes for bounce-to-DE connection.
5. A spectator ALP with f_a ~ M_Pl and m ~ H_0 predicts cosmic birefringence beta ~ 0.27 deg, consistent with 3.9-sigma combined observations.
6. The f_a cancellation in the birefringence formula makes the prediction independent of the ALP decay constant.
7. The MCMC pipeline (Cobaya + stock CAMB, 4 datasets, 236,622+ samples) is reproducible and converged (R-hat - 1 < 0.005).
8. Delta-N_eff is consistent with zero in all dataset combinations (the spin-torsion bounce does not produce detectable dark radiation).

## What This Project Has Not Established

1. Dark energy derived from first principles via torsion (all routes closed).
2. Hubble tension reduction (H_0 = 67.68 +/- 1.06, standard LCDM value; earlier claim of 69.2 was artifact of SH0ES prior).
3. Any bounce-specific observable signature in CMB, GW, or relics (13 barriers).
4. Galaxy spin dipole from ECH (9-12 orders of magnitude coupling gap).
5. ALP = dark energy (rolling-vs-freezing tension prevents simultaneous explanation).
6. Chiral gravitational waves from the bounce (frequency gate: GHz signals, detectors at mHz-kHz).
7. Any result unique to ECH that cannot be obtained from a generic ALP or scalar-tensor theory.
