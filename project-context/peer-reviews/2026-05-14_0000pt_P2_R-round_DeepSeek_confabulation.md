# P2 v1.7.27 — DeepSeek-V3.5 Confabulation-Hunter R-Round

**Reviewer model:** DeepSeek-V3.5 (simulated)
**Date:** 2026-05-14 00:00 PT
**Paper:** `research/focused_paper_source_integration/02_full_draft.tex`
**Posture:** Adversarial. Single question per claim — *show me the file that produces this number*.
**Round:** 4th R-round on P2. Prior rounds flagged the 9.9σ joint-Fisher provenance issue; this round is a clean re-sweep of every load-bearing scalar in abstract + headline.

---

## Summary

The headline `84% ± 2%` template-overlap claim and the `200 injection-recovery realizations` claim are traceable to scripts on disk (`template_overlap_robustness.py`, `phase3_fisher_overlap.py`, `estimator_grade_r_summary.md`), but the **specific numeric envelope `r ∈ [0.821, 0.879]` printed in the abstract does NOT match the one on-disk JSON output (`phase3_fisher_overlap.json` gives `r_range = [0.856, 0.895]`)**. The Bayes-factor grid `BF ≈ 6 → 17`, the `BF ≈ 8` headline baseline, the `BF ≈ 8–11` GR-marginalization variation, and the `~13%` null-space amplitude scatter have **no on-disk script that produces them under the prior shapes cited in the paper** — the one BF script (`bayes_and_forecasts.py`) uses a single uniform `[-10,+10]` prior, never the four-corner `[-5,+5] × [-15,+15] × δ × σ_theory=1.0` grid the paper claims to scan. The `>6×10⁵ Monte Carlo` claim is the sum of three independent 100k-realization scripts (`04b_fast_ensemble.py`, `03b_fast_mock_validation.py`, `02_compute_gr_aware_bayes_update.py`), each with its own random seed and prior, never run as a single ensemble — the aggregate count is rhetorical, not statistical.

---

## Findings

### P2-DS-B1 — **BLOCKER**: abstract overlap range `r ∈ [0.821, 0.879]` contradicts the one on-disk JSON

**Claim location:** abstract L29; body L140.
**Paper:** `r ∈ [0.821, 0.879]` … `CMB Fisher signal-only r = 0.876, realistic LSS/SPHEREx noise-weighted r ≈ 0.83`.
**On-disk JSON:** `research/matter_bounce_parameters/phase3_fisher_overlap.json`:
```json
"r_mean": 0.8784,
"r_std":  0.0118,
"r_range": [0.8557, 0.8947],
```
**Discrepancy:** the JSON's `min = 0.856` and `max = 0.895` — both endpoints differ from the abstract's `0.821 / 0.879`. The lower bound `0.821` is ~0.035 below anything in the JSON; the upper bound `0.879` is ~0.016 below the JSON's max. This is **the** load-bearing range that anchors the `84% ± 2%` headline.
**Where does `0.821` come from?** `template_overlap_robustness.py` L411 hard-codes `min(r_main.min(), 0.83)` as the "Conservative LSS" floor — i.e. `0.83` is a **floor**, not a measured minimum. The number `0.821` appears nowhere in the JSON outputs in `research/matter_bounce_parameters/`. The script has no JSON output (only the `.py` file).
**Impact:** the abstract's headline range is unreproducible from the artifacts on disk. The body table at L140 lists three "noise-weighted" numbers (`0.829`, `0.830`, `0.835`) and a CMB number (`0.876`) — `min=0.829, max=0.876` → that range is `[0.829, 0.876]`, again not `[0.821, 0.879]`.
**Fix:** (a) commit the JSON output of `template_overlap_robustness.py` to disk, (b) reconcile the abstract range with the actual computed min/max, or (c) explicitly footnote that `[0.821, 0.879]` is `[r_LSS_floor − 1σ, r_CMB + 1σ]` if that is what was intended.

---

### P2-DS-B2 — **BLOCKER**: 4-corner Bayes-factor prior grid (BF ≈ 6 / 17 / 8 / 8–11) has no script that scans it

**Claim location:** abstract L29; body §6 "Bayesian Comparison" (referenced at L240+ Tab. `tab:bayes`).
**Paper:** "BF ≈ 6 (curvaton-natural `[-5,+5]` prior, σ_theory=1.0 Gaussian) up to BF ≈ 17 (delta bounce prior, broad multifield `[-15,+15]`)"; "headline BF ≈ 8 at recommended baseline (σ_theory=1.0 Gaussian, broad `[-15,+15]`)"; "BF ≈ 8–11 GR-marginalization variation on the delta-prior row".
**On-disk script:** `research/matter_bounce_parameters/bayes_and_forecasts.py` L55: `a_multi = 10.0  # uniform on [-10, +10]` — **the only prior implemented is `[-10,+10]`**. There is no `[-5,+5]`, no `[-15,+15]`, no σ_theory=1.0 Gaussian bounce prior, no delta-vs-flat × four-corner grid, and no JSON output file from any script that produces the BF values 6, 8, 11, or 17.
**Last-mile script** `research/last_mile_robustness_program/04b_fast_ensemble.py` does use `prior_lo=-15, prior_hi=15` but only against a delta bounce prior — it cannot produce the σ_theory=1.0 Gaussian row.
**Impact:** the abstract's BF envelope is the central quantitative discrimination claim of the paper. Without a script that scans the four-corner grid and emits each row of Tab. `tab:bayes`, every BF number in the abstract is unsourced.
**Fix:** add a single script `bayes_factor_grid.py` that takes the 2×2×2 prior corner combinations as inputs, emits a JSON with all 8 BF values, and reference its hash in §6.

---

### P2-DS-B3 — **BLOCKER**: `~13%` null-space amplitude scatter quoted in abstract does not appear in the null-space script output

**Claim location:** abstract L29 — "polynomial-coefficient null-space amplitude scatter ~13% from the underdetermined c₁–c₆ benchmark".
**On-disk script:** `research/focused_paper_source_integration/null_space_analysis.py` L240: `r_amp_all.std()` is computed but the script has **no JSON output**, and the body of the paper (L70-ish) reports `r = 0.85 ± 0.13` (range 0.55–1.14) — so `0.13` is the *absolute* std of r_amp, not a *percent* scatter. The abstract collapses `±0.13 absolute` (~15% relative to r̄ = 0.85) into "~13%" without showing the arithmetic. There is no file with the value `0.13` or `13%` saved.
**Why this matters:** the systematic-budget chain `5.2σ → 3σ` depends on this scatter being treated as a multiplicative degradation on σ(f_NL). If the actual scatter is 15% relative (not 13%), the post-systematic significance bound shifts. The number is also used to justify the headline "3–5σ" abstract range, which is the most-quoted figure in the project.
**Fix:** commit the `null_space_analysis.py` output JSON. Be explicit whether 13% is `r_amp.std()` absolute or relative to r̄. Reconcile with the L70 body number `±0.13` so the reader knows they are the same quantity.

---

### P2-DS-M1 — **MAJOR**: `>6×10⁵ Monte Carlo realizations` is a sum across three different scripts with three different priors

**Claim location:** abstract L29 — "validated over >6×10⁵ Monte Carlo realizations … across analytic, mock-based, and parameterized-GR-degradation frameworks".
**On-disk scripts:**
- `research/last_mile_robustness_program/04b_fast_ensemble.py` — `N_REAL = 100000`
- `research/optional_premium_robustness/03b_fast_mock_validation.py` — `N_MOCKS = 100000`
- `research/gr_contamination_claim_hardening/02_compute_gr_aware_bayes_update.py` — `N = 100000`
**Aggregate:** 300,000. Even if the older slower variants (`04_compute_*.py`, `03_optional_addon_code.py`) doubled this, the realistic total is `~6×10⁵` only if every script's realizations are counted once. But the three scripts use **different priors** (`[-15,+15]` delta-vs-flat, lognormal σ-base, σ_GR Gaussian) — they are not three frames of the same ensemble; they are three independent experiments.
**Fix:** rewrite as "validated across three independent ensembles, each of 10⁵ realizations, with framework-specific priors detailed in §6 and App. X". Drop the aggregate `6×10⁵` figure — it is a sum of incommensurable counts and reads as a single Monte Carlo when it is not. The abstract footnote does say "which serve primarily to confirm the analytic Bayes factor formula" — good — but the *count* itself misleads.

---

### P2-DS-M2 — **MAJOR**: `σ(f_NL) ≈ 0.7` attributed to "Heinrich et al. 2024, Fig. 6 / Table 3" — primary source is Heinrich et al. 2023 in the bibliography

**Claim location:** abstract L29; multiple body sections.
**Paper text:** "Heinrich \etal~2024~\cite{Heinrich:2023}, Fig.~6 / Table~3".
**Bibliography (`focused_paper_refs.bib`):** `Heinrich:2023` resolves to a 2023 arXiv preprint per the citekey. The paper text writes "2024" — and the abstract attributes a specific Fig. 6 / Table 3 to this reference.
**Verification I cannot perform from disk:** whether Fig. 6 / Table 3 of the cited Heinrich paper actually reports `σ(f_NL) = 0.7` for SPHEREx multi-tracer bispectrum under the local-template normalization stated in the paper. The CLAUDE.md note says this number was corrected from `σ=16.85/12.72/11.71` (fire #25 / skeptical-statistician finding) — the correction was made by editing prose, not by re-deriving σ from a script.
**Impact:** σ(f_NL) = 0.7 is the divisor in every detection-significance number in the paper. If Heinrich+2023's Fig. 6 / Table 3 is actually a forecast for power-spectrum-only or a different fiducial b_φ, the multiplier on `f_NL = -4.375` is wrong and the headline `5.2–5.5σ` shifts.
**Fix:** (a) reconcile year discrepancy (2023 vs 2024 in text), (b) pull the exact figure number, table number, and quoted value from the Heinrich paper into a short Appendix table with the page reference, (c) note explicitly which b_φ / k_min / multi-tracer assumption gives `0.7`.

---

### P2-DS-M3 — **MAJOR**: `0.500 ± 0.001` per-configuration ε-order ratios are computed but no output file is on disk

**Claim location:** abstract L29 — "per-configuration ratios 0.500 ± 0.001 at equilateral, folded, and squeezed".
**On-disk scripts:** `eq37_final_verification.py`, `eq37_squeezed_analysis.py`, `eq37_sum_convention_test.py`, `cai_eq37_direct_check.py`, `general_epsilon_bispectrum.py` — all in `research/matter_bounce_parameters/`. These collectively compute the ratios.
**Missing:** no JSON output file containing the three values, no `tier1a_results.json` row for "equilateral / folded / squeezed ratio = 0.500". The closest is `general_epsilon_scan.json`, which scans ε but does not emit per-configuration ratios.
**Impact:** the `0.500 ± 0.001` is the **only quantitative support** for the abstract's claim that "the intermediate ε-order decomposition reproduces approximately half the full polynomial at each of the three benchmark configurations". This is the audit-trail for f_NL = -35/8 being the correct Planck normalization. The ±0.001 looks load-bearing-precise but cannot be reproduced without running the scripts and saving their output.
**Fix:** add a script `compute_eq37_ratios.py` (one-shot) that emits a JSON with the three configurations and their ratios, ±0.001 with the explicit error definition (machine precision? grid convergence? Monte Carlo?). Reference the hash from Tab. `tab:benchmarks`.

---

### P2-DS-M4 — **MAJOR**: `200 injection-recovery realizations → r_meas = 0.90 ± 0.01` cited as primary validation, but the only mention on disk is in a markdown summary, not a script

**Claim location:** abstract L29; body L140 (validation level (ii)).
**On-disk source:** `research/matter_bounce_parameters/estimator_grade_r_summary.md` L14:
```
| Monte Carlo injection recovery (200 realizations) | 0.900 | ±0.012 | Injection-validated |
```
**No script:** I cannot find a `.py` file in `research/matter_bounce_parameters/` or `research/focused_paper_source_integration/` that runs 200 KSW-type injection-recovery realizations with SPHEREx photometric-z noise covariance and outputs `r = 0.90 ± 0.01`. The `injection_recovery.py` scripts elsewhere (`h200_scripts/experiments/injection_recovery.py`, `pipelines/p3_anomaly_engine/injection_recovery_*.py`) are for different tasks (anomaly detection, spectral injection), not for KSW bispectrum estimator validation.
**Why this matters:** the abstract claims "validated via … 200 injection-recovery realizations". This is one of three orthogonal validations supporting the `84% ± 2%` overlap. If only a summary markdown exists — no code, no seed, no random state, no per-realization output — the validation is asserted not demonstrated.
**Fix:** either commit the script (with seed, noise covariance file path, and per-realization output), or downgrade the body claim from "validated via … injection-recovery" to "estimated via Fisher-space injection-recovery; full simulation pipeline deferred to a companion paper". The current paper L140 already includes a partial caveat ("The injection-recovery approach here is a Fisher-space test of amplitude recovery, not a full simulation pipeline") — good — but the abstract still leads with the result as if it were a direct sim.

---

### P2-DS-M5 — **MAJOR**: `5.2–5.5σ` optimistic and `3–5σ` post-systematic headline are arithmetic from unsourced inputs

**Claim location:** abstract L29 ("3–5σ … with 5.2–5.5σ as the optimistic case"); body L142.
**Arithmetic chain in body L142:** `|f_NL| / σ(f_NL) × r → 4.375 / 0.7 × {0.876 or 0.83} = 5.47 or 5.18` → reported as `5.5σ` and `5.2σ`. Each input has its own unresolved provenance:
- `0.7` ← P2-DS-M2 (Heinrich attribution unverified)
- `0.876` ← `phase3_fisher_overlap.json` (this one *is* on disk, but the JSON range [0.856, 0.895] disagrees with the abstract envelope per P2-DS-B1)
- `0.83` ← `template_overlap_robustness.py` floor (P2-DS-B1)
- `→ 3–5σ` after "GR marginalization, b_φ uncertainty, photo-z degradation" — the multiplicative factors from each of these have no per-systematic budget table in the paper that I can locate. The body asserts "the realistic range is ~3–5σ" without showing the chain.
**Impact:** the **headline number of the paper** is `3–5σ`. It depends on three inputs each of which has a separate provenance question. The 5.2 vs 5.5 split is two-digit precise but derives from two-decimal-place inputs none of which has a reproducible artifact.
**Fix:** add a "systematic budget" subsection table with columns [systematic / multiplicative factor / source / reference]. Make the chain `5.5σ → 3.0σ` explicit row-by-row. This is the standard prim-cosm-systematic-budget format (cf. Planck non-Gaussianity papers' Table 1).

---

**End of findings (3 BLOCKERs, 5 MAJORs, 8 total — at the requested cap).**

---

## Notes for prior-round comparison

- The 9.9σ joint-Fisher issue (3rd round) is now explicitly demoted to "illustrative idealized estimate pending the full Fisher-input release rather than as the lead detection number" (abstract L29). Good demotion.
- The σ(f_NL) = 0.7 source attribution is now Heinrich 2023/2024 (CLAUDE.md confirms 2026-05-05 correction). Still unverified against the actual Heinrich paper figures (P2-DS-M2).
- The Li & Brandenberger convention caveat is now in the abstract — appropriate.
- The polynomial null-space stability (`r_cos > 0.97`) IS reproducible from `null_space_analysis.py` and the script's stdout. Good.

**Recommendation:** close P2-DS-B1, P2-DS-B2, P2-DS-B3 before next submission attempt. The other five are MAJORs that should be addressed in the same revision but are not standalone publication blockers. Readiness: **78%** post-this-review (was 86% per CLAUDE.md line for P4; P2 was previously 92% before this confab sweep; recommend roll-back to ~78% per the readiness-oscillation directive).
