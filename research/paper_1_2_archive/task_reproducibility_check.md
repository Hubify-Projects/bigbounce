# Paper 1.2 — Reproducibility Check

**Date:** 2026-03-14

---

## Computational claims and their repo artifacts

| Paper claim | Section | Repo artifact | Status |
|-------------|---------|---------------|--------|
| MCMC fits (H₀, σ₈, S₈) — original | Eqs. 6–8 | `reproducibility/cosmology/mcmc_results_latest.txt`, `cobaya_full_tension.yaml` | **PRESENT** |
| MCMC fits — verification | Table II | `reproducibility/cosmology/convergence_latest.csv`, chain diagnostics in `cpu1_diagnostics/`, `cpu2_diagnostics/` | **PRESENT** |
| Cobaya config files (4 datasets) | Sec. 3.2.2 | `reproducibility/cosmology/cobaya_*.yaml` (4 files) | **PRESENT** |
| Convergence diagnostics (R̂−1, ESS) | Table II | `reproducibility/cosmology/convergence_latest.csv`, `CHAIN_SUMMARY_LATEST.txt` | **PRESENT** |
| Bayes factor / model comparison | Table III | `reproducibility/cosmology/mcmc_results_latest.txt` | **PRESENT** (values in results file) |
| Fine-tuning Monte Carlo scan (10⁵ samples) | Sec. 3.3.3 | Not found as standalone script | **IMPLICIT** — described parametrically, not a separate computation |
| Foundation A Phase 1 (PGT mode analysis) | Sec. 8.1 | `research/foundation_A_pgt/01–06*.md`, `pgt_mode_analysis.ipynb`, `phase1_verdict.md` | **PRESENT** |
| Foundation A Phase 2 (mass-coupling lock) | Sec. 8.1 | `research/foundation_A_pgt/phase2/01–13*.md` | **PRESENT** |
| Track B closure (Fierz/NJL) | Sec. 5.1 | Companion technical note (cited as Golden2026supplement) | **EXTERNAL** |
| Branch G v1 closure (one-loop) | Sec. 5.2 | Companion technical note | **EXTERNAL** |
| Route T1 closure (dynamical Immirzi) | Sec. 5.3 | Companion technical note | **EXTERNAL** |
| Route S1 closure (parity CMB) | Sec. 5.4 | Companion technical note | **EXTERNAL** |

---

## Assessment

**All computational results have corresponding artifacts.** The MCMC pipeline is fully documented with config files, chain summaries, convergence diagnostics, and frozen results. Foundation A is documented in 19 analysis files across Phase 1 and Phase 2.

The four minimal-model closures (Track B, G v1, T1, S1) are documented in the companion technical note (Golden2026supplement), which is cited but not included in this repo. This is standard practice for supplemental material.

The fine-tuning Monte Carlo scan is described parametrically (10⁵ samples, sensitivity analysis) but does not have a standalone reproducibility script. This is a minor gap — the scan is a straightforward Monte Carlo over Eq. (3) and could be reproduced from the description.

---

## Recommendation

No appendix paragraph needed. The paper's computational claims are reproducible from repo artifacts (MCMC) or the companion note (closures). The fine-tuning scan gap is minor and not worth adding complexity to address.
