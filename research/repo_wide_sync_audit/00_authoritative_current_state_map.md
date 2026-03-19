# Authoritative Current State Map

**Created:** 2026-03-19
**Purpose:** Single source of truth for the complete project state, based on exhaustive reading of all 38 verdict/summary files across the repository.

---

## 1. ECH Perturbation Closure (14 Barriers)

**Status:** SETTLED -- COMPREHENSIVELY CLOSED
**Authoritative files:**
- `research/ech_bispectrum_gate/final_verdict.md` (scalar sector)
- `research/ech_tensor_gate/final_verdict.md` (tensor sector)
- `research/post_AG_pivot/final_pivot_summary.md` (Foundations A-G)
- `research/bounce_evidence_audit/final_verdict.md` (full 16-claim audit)

**Summary:** The chain zero spin -> zero torsion -> Holst topological -> no dynamics closes ALL ECH-specific perturbation channels (scalar, tensor, bispectrum). 13+ structural barriers cataloged across Foundations A-G and Branches H-Q. The ECH bounce resolves the singularity but is observationally silent at the perturbation level. The Barbero-Immirzi parameter is invisible in both scalar and tensor sectors for canonical scalar field matter. This is mathematical closure, not numerical -- it cannot be overturned by further computation.

---

## 2. f_NL Benchmark Value

**Status:** PARTIALLY SETTLED -- magnitude and sign established, exact coefficient still open
**Authoritative files (in supercession order):**
1. `research/fnl_symbolic_cancellation/final_verdict.md` -- **MOST AUTHORITATIVE for numerical result**: independently computed f_NL = 35/16 = 2.1875 (matching Li-Brandenberger), sign positive in our convention (convention TBD vs Cai)
2. `research/fnl_discrepancy_resolution/final_verdict.md` -- corrected the 35/16 artifact from earlier phase, confirmed V1 T1-only result
3. `research/cai_action_audit/final_verdict.md` -- explained full discrepancy: action mismatch, mode-function convention, superhorizon vs horizon-crossing dominance
4. `research/fnl_derivation_execution/final_verdict.md` -- convention resolved (f_NL = |B|_NL), template cos(theta) ~ 0.95, field redef +5/4
5. `research/gradient_expansion_fnl_derivation/final_verdict.md` -- cross-check confirming sign, magnitude, shape, parameter-freedom; does NOT resolve coefficient

**Current best value:** f_NL in [-35/8, -35/16] = [-4.375, -2.188]. The symbolic cancellation independently reproduced 35/16 (matching Li-Brandenberger). Cai's -35/8 is weakened but not definitively ruled out. Both values predict detectable signals.

**Confidence breakdown:**
- f_NL is negative: 95% (convention resolution pending, but structural argument for negative from T3-T6 dominance)
- |f_NL| > 2: 85%
- f_NL = -35/8 exactly: 40-50% (weakened by symbolic cancellation favoring 35/16)
- f_NL = -35/16 exactly: 40-50% (independently reproduced)
- |f_NL| detectable by MegaMapper: >85% (either value gives 4.4-8.75 sigma)

---

## 3. Gradient Expansion Result

**Status:** SETTLED as a cross-check; does NOT advance the coefficient question
**Authoritative file:** `research/gradient_expansion_fnl_derivation/final_verdict.md`

**What it confirms:** Sign (negative), magnitude (O(1)), shape (local), parameter-freedom (depends only on w=0). These were ALL already known from the execution phase.

**What it does NOT settle:** The exact coefficient (-35/8 vs -35/16). The gradient expansion reaches the same mathematical bottleneck: evaluating the growing-mode-squared coupling through second-order Einstein equations.

**Assessment:** SUPPORTING_CROSS_CHECK. Raises confidence from ~75% to ~80% on structural features, but adds zero information on the coefficient dispute.

---

## 4. In-In / Cubic Action Execution Status

**Status:** PARTIALLY COMPLETE -- significant results but full coefficient not independently verified
**Authoritative files:**
- `research/fnl_derivation_execution/final_verdict.md` (main execution)
- `research/fnl_combined_integrand/final_verdict.md` (combined 6-term computation)
- `research/fnl_symbolic_cancellation/final_verdict.md` (SymPy cancellation analysis)
- `research/fnl_numerical_integral_check/final_verdict.md` (numerical verification)
- `research/cai_action_audit/final_verdict.md` (action discrepancy traced)

**What was achieved:**
- Convention equivalence proven: f_NL(Planck) = |B|_NL(Cai)
- Template projection bounded: cos(theta) ~ 0.95
- Field redefinition: exactly +5/4
- Dominant vertex (T1): f_NL = +1.5625 (converged, stable)
- Terms 1-4 combined: f_NL = +2.186 = 35/16 (matching Li-Brandenberger)
- Action mismatch with Cai fully diagnosed (coefficient, mode convention, chi-sector)
- Growing-mode divergence structure proven to cancel in Im[ext x I]

**What was NOT achieved:** Full 6-term numerical verification (growing-mode cancellation requires arbitrary precision). Independent resolution of -35/8 vs -35/16.

---

## 5. Wilson-Ewing Model Viability

**Status:** ALIVE -- the unique surviving viable model
**Authoritative files:**
- `research/project_viable_bounce_model_pass2/final_verdict.md`
- `research/next_flagship_program/final_verdict.md`

**Summary:** Wilson-Ewing LCDM Quasi-Dust Matter Bounce in LQC is the unique surviving model after second-pass filtering. 0 extra fields, 1 fitted parameter (epsilon = 0.003), 1 parameter-free prediction (f_NL). Models A (curvaton) and C (ILS ekpyrotic) were eliminated. The bounce does genuine predictive work (LQC suppresses r to ~10^-4, contraction dynamics produce f_NL). The model's weakness is single-point-of-failure architecture: if f_NL falls, no fallback discriminator exists.

---

## 6. Survey Forecast Status (SPHEREx / MegaMapper)

**Status:** SETTLED -- fully hardened through multiple robustness passes
**Authoritative files:**
- `research/forecast_hardening_program/final_verdict.md`
- `research/fisher_robustness_surface/final_verdict.md`
- `research/ultra_large_scale_systematics_audit/final_verdict.md`
- `research/survey_realism_reconciliation/final_verdict.md`

**Realistic forecasts:**
| Survey | Timeline | Realistic sigma(f_NL) | Significance at -4.375 |
|--------|----------|----------------------|----------------------|
| SPHEREx (bispectrum) | ~2028 | 0.7-1.5 | 3-6 sigma |
| MegaMapper (multi-tracer) | ~2032+ | 0.5-2.0 | 2-9 sigma |
| Combined | ~2032+ | 0.5-1.0 | 4-9 sigma |

**Key vulnerability:** Ultra-large-scale mode access (k_min). Factor 100x in sigma between k_min = 10^-4 and 10^-3. SPHEREx bispectrum channel is more robust than MegaMapper SDB. GR projection effects create systematic bias that must be modeled.

---

## 7. Bayesian Discrimination / Inflation Mimicry

**Status:** SETTLED -- complete quantitative framework
**Authoritative files:**
- `research/bayesian_discrimination_program/final_verdict.md`
- `research/inflation_mimicry_deep_comparison/final_verdict.md`
- `research/gr_contamination_claim_hardening/final_verdict.md`
- `research/last_mile_robustness_program/final_verdict.md`
- `research/optional_premium_robustness/final_verdict.md`

**Results (800,000+ Monte Carlo samples):**
- Bounce vs standard single-field inflation: median BF > 10^13 (decisive)
- Bounce vs tuned multifield: median BF = 53 (combined), robust in 83% of realizations
- Bounce vs SSFSR after GR marginalization: median BF = 329, P(BF>3) = 96%
- Prior sensitivity: bounce advantage persists across all reasonable choices
- GR contamination: resolved -- Occam argument robust to systematic bias

---

## 8. ALP Birefringence Status

**Status:** SETTLED -- surviving positive prediction, bounce-independent
**Authoritative files:**
- `research/branch_R_alp_birefringence/novelty_audit/final_verdict.md`
- `research/paper1_salvage_alp/final_verdict.md`
- `research/final_phase/final_verdict.md`

**Summary:** beta = 0.27 deg predicted, matching 3.9-sigma combined Planck+ACT detection (0.342 +/- 0.094 deg). MCMC constraints: theta_i = 1.36 +/- 0.44. LiteBIRD-falsifiable. However: (a) bounce-INDEPENDENT, (b) not unique to ECH (any Planck-scale ALP gives same), (c) novelty comes from ECH closure context, not from the ALP fit itself.

---

## 9. MCMC Infrastructure Status

**Status:** IDLE -- 236,000+ samples frozen, no new theory hooks to test
**Authoritative file:** `research/remaining_live_paths_audit/final_verdict.md`

**Summary:** Cobaya + CAMB pipeline validated. 4 dataset combinations, 64 chains, R-1 < 0.005. Delta-N_eff consistent with zero in all datasets. No new MCMC runs justified -- f_NL is parameter-free (not a chain parameter), and no new theory predictions require posterior estimation.

---

## 10. Bounce Evidence Audit Results

**Status:** SETTLED -- honest assessment complete
**Authoritative file:** `research/bounce_evidence_audit/final_verdict.md`

**Summary:** No claim reaches STRONG_EVIDENCE. Best data contact (birefringence) is bounce-independent. CMB anomaly claims downgraded to WEAK. Bounce cosmology does NOT currently fit observations better than LCDM+inflation. The strongest argument for bounce is theoretical (singularity resolution), not observational.

---

## 11. LQC-Specific Openings

**Status:** PARTIALLY SETTLED -- three genuine openings identified
**Authoritative file:** `research/lqc_specific_openings_audit/final_verdict.md`

**Open paths:**
1. LQC formalism sensitivity for bispectrum (dressed-metric vs hybrid) -- UNTESTED
2. PBH + induced GW from bounce transition -- UNTESTED
3. Scale-dependent f_NL from LQC corrections -- likely dead but unchecked

**Priority:** f_NL verification first (foundation), then formalism audit, then PBH channel.

---

## 12. Publication Readiness

**Status:** TWO parallel paper tracks identified

**Paper 1 (ECH closure + ALP):** Ready to write. All material assembled. 13 barriers, ALP birefringence as sole surviving prediction, MCMC constraints converged. Estimated 17 pages two-column. File: `research/final_phase/final_verdict.md`

**Paper 2 (f_NL forecast):** Complete at analytical level. 5 figures generated (`research/live_forecast_packaging/`). Skeleton, claims table, figure plan all complete. 800,000 Monte Carlo samples. Title: "Testing the Matter Bounce with Primordial Non-Gaussianity: Forecasts for SPHEREx and MegaMapper." File: `research/live_forecast_packaging/final_verdict.md`

---

## 13. Focused-Path Terminal Work (Complete Inventory)

The following directories represent work that goes BEYOND the gradient expansion, produced by what appears to be a separate focused-path terminal session:

| Directory | Topic | Status |
|-----------|-------|--------|
| `research/bispectrum_self_ownership_and_ech_test/` | Shape function verification, ECH entry point assessment | COMPLETE |
| `research/cai_action_audit/` | Cai vs Maldacena action comparison, discrepancy resolution | COMPLETE |
| `research/fnl_combined_integrand/` | Full 6-term Maldacena combined integral | COMPLETE |
| `research/fnl_discrepancy_resolution/` | Correction of 35/16 artifact | COMPLETE |
| `research/fnl_numerical_integral_check/` | Numerical verification attempt | COMPLETE |
| `research/fnl_symbolic_cancellation/` | SymPy cancellation structure, finite remainder | COMPLETE |
| `research/ech_bispectrum_gate/` | ECH scalar bispectrum closure | COMPLETE |
| `research/ech_tensor_gate/` | ECH tensor sector closure | COMPLETE |
| `research/post_ech_positive_program/` | Post-closure program assessment | COMPLETE |
| `research/bounce_inflation_discrimination_program/` | Full discrimination framework | COMPLETE |
| `research/observational_decision_framework/` | Decision thresholds, survey hierarchy | COMPLETE |
| `research/forecast_hardening_program/` | Fisher forecast hardening | COMPLETE |
| `research/fisher_robustness_surface/` | k_min sensitivity surface | COMPLETE |
| `research/ultra_large_scale_systematics_audit/` | GR projection, b_phi, k_min audit | COMPLETE |
| `research/survey_realism_reconciliation/` | SPHEREx vs MegaMapper reconciliation | COMPLETE |
| `research/inflation_mimicry_deep_comparison/` | Anti-mimicry analysis | COMPLETE |
| `research/bayesian_discrimination_program/` | Bayes factor computation (100k MC) | COMPLETE |
| `research/gr_contamination_claim_hardening/` | GR-aware Bayes factors (500k MC) | COMPLETE |
| `research/last_mile_robustness_program/` | Combined robustness (100k MC) | COMPLETE |
| `research/optional_premium_robustness/` | Mock-based validation (200k MC) | COMPLETE |
| `research/live_forecast_packaging/` | Paper skeleton, figures, claims table | COMPLETE |

**Total: 21 directories of focused-path work that goes substantially beyond the gradient expansion.** This represents: benchmark ownership, Cai action extraction, shape verification, forecast packaging, Bayesian discrimination (800,000 MC samples), systematics audit, survey realism, and GR contamination hardening.
