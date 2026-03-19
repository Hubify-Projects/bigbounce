# Freeze Boundary: What Is Frozen vs Open

**Created:** 2026-03-19
**Purpose:** Define what must not be touched after submission, and what counts as a legitimate reason to reopen.

---

## FROZEN (do not touch without compelling reason)

### The Focused PNG Paper

| Directory | Content | Status |
|-----------|---------|--------|
| `research/focused_paper_full_draft/` | Complete draft, all 9 sections, claims table | DRAFT COMPLETE |
| `research/live_forecast_packaging/` | 5 publication figures, manuscript skeleton, abstract | PACKAGED |
| `research/bayesian_discrimination_program/` | 800K MC Bayes factors, prior sensitivity | COMPLETE |
| `research/forecast_hardening_program/` | SPHEREx 4-6 sigma, MegaMapper 3-7 sigma | HARDENED |
| `research/survey_realism_reconciliation/` | GR projection marginalization, survey hierarchy | COMPLETE |
| `research/inflation_mimicry_deep_comparison/` | Anti-mimicry analysis, multifield comparison | COMPLETE |
| `research/gr_contamination_claim_hardening/` | Robust vs conditional claims, BF > 329 | COMPLETE |
| `research/cai_action_audit/` | f_NL = -35/8 algebraically verified, 3 mismatches resolved | VERIFIED |
| `research/fnl_symbolic_cancellation/` | SymPy verification, T1-T4 = 35/16, 0.07% match to L-B | VERIFIED |
| `research/gradient_expansion_fnl_derivation/` | Independent formalism cross-check | SUPPORTING |
| `research/ech_bispectrum_gate/` | ECH scalar perturbation transparency: PERMANENT CLOSURE | CLOSED |
| `research/ech_tensor_gate/` | ECH tensor perturbation transparency: PERMANENT CLOSURE | CLOSED |
| `research/fnl_derivation_execution/` | In-in cubic action computation | COMPLETE |
| `research/fnl_discrepancy_resolution/` | Li-Brandenberger vs Cai convention diagnosis | RESOLVED |
| `research/fisher_robustness_surface/` | k_min sensitivity quantified | COMPLETE |
| `research/ultra_large_scale_systematics_audit/` | GR contamination, b_phi, bispectrum channel | COMPLETE |
| `research/last_mile_robustness_program/` | 83% of realizations give BF > 10 | COMPLETE |
| `research/optional_premium_robustness/` | 200K synthetic spectra, BF 425:1 | COMPLETE |

### The MCMC Infrastructure

| Directory | Content | Status |
|-----------|---------|--------|
| `reproducibility/cosmology/paper1_clean_restart_sync/` | Frozen chains, 4 datasets x 5-6 chains | FROZEN |
| `reproducibility/cosmology/` | Cobaya YAML configs, convergence diagnostics | FROZEN |

All chain files (236,000+ posterior samples, 64 chains, R-hat - 1 < 0.005) are science-frozen. They confirm Delta-N_eff approximately 0 with stock CAMB. No rerun produces new information without a custom theory hook.

### The Website

| Component | Status |
|-----------|--------|
| All current page content reflecting the frontier state | FROZEN |
| Activity feed entries through 2026-03-19 | FROZEN |
| Data explorer with 15 embedded datasets | FROZEN |
| 22-figure gallery | FROZEN |

### The Repo-Wide Sync Audit

| Directory | Content | Status |
|-----------|---------|--------|
| `research/repo_wide_sync_audit/` | Final canonical status, 5 reconciliation files | AUTHORITATIVE |
| `research/lqc_specific_openings_audit/` | LQC paths ranked, second observable audit | AUTHORITATIVE |
| `research/remaining_live_paths_audit/` | Deprioritization list, ranked paths | AUTHORITATIVE |
| `research/bounce_evidence_audit/` | 16-claim honest scorecard | AUTHORITATIVE |

---

## What Counts as a LEGITIMATE Post-Submission Correction

### Legitimate reasons to reopen frozen material:

1. **A referee identifies a genuine mathematical error in the forecast.** Example: an algebraic mistake in the Fisher matrix, a wrong survey parameter, a misquoted observational constraint.

2. **A new observational result changes the landscape.** Example: SPHEREx publishes early data with sigma(f_NL) significantly different from forecasted. Or Planck 2024 reanalysis tightens f_NL bounds past -4.375.

3. **A critical paper appears that directly contradicts f_NL = -35/8.** Example: a new independent calculation of the matter-bounce bispectrum that finds a qualitatively different result (not a factor-of-2 convention issue, which is already resolved, but a fundamentally different structure).

4. **A bug is discovered in the Monte Carlo code or Fisher machinery.** Example: an off-by-one error in the survey volume calculation, a wrong cosmological parameter in the fiducial model.

### What is NOT legitimate (do not reopen for these):

1. **Redoing benchmark verification that is already complete.** The Cai action audit resolved all 3 mismatches. The SymPy cancellation verified T1-T4. The gradient expansion confirmed structural features. These are done.

2. **Reopening ECH perturbation loops.** Permanently closed. 14+ structural barriers. Mathematical proof of perturbation transparency. Zero spin -> zero torsion -> Holst topological -> no dynamics. This is a chain of identities.

3. **Restructuring the paper unless a referee demands it.** The 9-section structure covers all necessary content. Reorganization for aesthetic reasons wastes time.

4. **Re-running Monte Carlo with slightly different parameters.** 800K samples with full prior sensitivity already exist. Marginal parameter changes produce marginal result changes.

5. **Adding more supporting evidence.** The evidence base is sufficient: 5 pillars complete, 800K MC samples, 200K synthetic spectra, 5 publication figures. More evidence has diminishing returns.

6. **Extending the gradient expansion.** It is a supporting cross-check, not the frontier. Extension leads to the same mathematical bottleneck without resolution.

7. **Galaxy spin dipole work.** 9-12 OOM coupling gap. Effectively falsified.

8. **Hybrid DE splice in any form.** 7 forms rejected exhaustively.

---

## Freeze Protocol

When in doubt about whether something is frozen, apply this test:

**Does touching this material change the science case presented in the submitted paper?**

- If YES and it STRENGTHENS the case: proceed only if the improvement is material (changes a sigma-level claim or fixes an error).
- If YES and it WEAKENS the case: proceed immediately and issue a correction.
- If NO: do not touch it. Work on the post-submission research stack instead.
