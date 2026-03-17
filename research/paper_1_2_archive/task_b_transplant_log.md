# Task B — Transplant Log

**Date:** 2026-03-13
**Source:** Paper 1.01 (`research/paper_1_01_archive/main.tex`)
**Target:** Paper 1.2 (`research/paper_1_2/paper_1_2_draft.tex`)

---

## Material Reused (with rewritten framing)

### Section 3.2 — Cosmological Parameters (expanded from 30 → 100+ lines)
- **Datasets** (Paper 1.01 Sec 7.1): Four dataset combinations with full descriptions. Reused verbatim — factual content.
- **MCMC Configuration** (Paper 1.01 Sec 7.2): Cobaya version, CAMB, convergence criteria, parameter count. Reused with explicit "statistical equivalence" note that this is generic ΛCDM+ΔNeff, not unique to spin-torsion.
- **Independent Verification** (Paper 1.01 Sec 3.4): Full verification table (176,840 + 132,949 samples), key findings, Liu et al. cross-validation. Reused with reframed interpretive note.
- **Bayesian Model Comparison** (Paper 1.01 Sec 7.3): Model comparison table, dataset-dependent Bayes factors. Reused with explicit caveat about dataset dependence and Occam penalty.

### Section 3.3 — Observational Consistency Checks (expanded from 20 → 90+ lines)
- **Birefringence consistency check** (Paper 1.01 Sec 10.4): Gaussian summary-likelihood, combined posterior β = 0.242° ± 0.061°, f_photon × C_0 constraint. Reused with explicit "not a prediction" framing.
- **Galaxy spin methodology** (Paper 1.01 App C): Hierarchical Bayesian likelihood, parametric model, null tests. Reused with explicit "empirical, not derived" framing.
- **Fine-tuning sensitivity scan** (Paper 1.01 Sec 7.5): 100,000-sample Monte Carlo, Spearman correlations, viable N_tot range. Reused with fine-tuning comparison table and explicit "parametric observation" label.
- **Limit behavior** (Paper 1.01 Sec 10.2): Five physical limits. Condensed to paragraph form.

### Appendix A — Notation (expanded from 4 → 30 lines)
- Full symbol list from Paper 1.01 App A, pruned of rotation-specific entries (ω_μν, σ_μν). Added closure-relevant symbols (G_eff, G_SP, PGT, NJL abbreviations).

### Appendix B — Parameter Summary (expanded from simple table → full table*)
- Full parameter table from Paper 1.01 App B, reorganized into three groups (framework / standard cosmological / extended). Added "Status" column with honest classifications. Added verification footnote and correlation note.

### Appendix C — Claims Classification (expanded from 15 → 22 rows)
- Added section headers (Derived / Phenomenological / Retired).
- Added new derived entries: Nieh-Yan topological in 4D.
- Added new phenomenological entries: birefringence consistency, galaxy spin A₀.
- Added new retired entries: ΔNeff as distinctive signal, galaxy spin as prediction.

### Section 9.3 — Comparison with other geometric programs (expanded)
- Removed [NOTE] placeholder, added substantive comparison with Popławski, Liu et al., and metric-affine programs.

### Bibliography (expanded from 22 → 25 entries)
- Added: Cobaya2021, ECTorsionDESI2025, Saadeh2016.

---

## Material Excluded (per task constraints)

| Paper 1.01 Content | Reason for Exclusion |
|---|---|
| First-principles dark energy origin claims | Closed by derivation program |
| "Minimal EC+Holst+Dirac is enough" rhetoric | Explicitly retired |
| Birefringence as prediction | Route S1 closure — no photon coupling |
| ΔNeff as distinctive signal | Verification shows consistent with 0 |
| Galaxy spin as prediction of framework | Order-of-magnitude gap unresolved |
| Condensate dark energy mechanism | Track B closure — G_SP < 0 |
| γ drives late-time physics | B, G, T1 closures — UV-scale only |
| Black hole universe origin narrative | Not part of phenomenological framework |
| Cosmic rotation formalism (App F) | Rotation negligible; not needed for Part I |
| Joint likelihood analysis (App D) | Depends on signal amplitudes not derived |
| Nieh-Yan treatment (App E) | Covered by closure discussion in Part II |
| Falsification criteria (Sec 10) | Premature without derived signal amplitudes |
| Observational forecast section | Removed in Paper 1.01 already |
| Fisher matrix error analysis (App G) | Superseded by full MCMC verification |

---

## Material Rewritten (new framing, not copy-paste)

- All interpretive paragraphs rewritten to emphasize phenomenological status
- All "prediction" language replaced with "consistency check" or "empirical"
- Bayesian model comparison framed as "statistical flexibility" not "evidence for spin-torsion"
- Verification section positioned as honest assessment, not confirmation
- Fine-tuning discussion: "reduces" not "solves"; "concentrates into N_tot" not "eliminates"
- Model comparison table: renamed "Spin-Torsion" → "ECH phenom." throughout

---

## Compilation Result
- **PDF size:** 172 KiB (up from 134 KiB)
- **Errors:** 0
- **Warnings:** Cosmetic underfull hboxes, expected revtex4-2 bbl consistency note
