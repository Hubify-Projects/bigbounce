# NOT READY YET — Final Submission Editing Cannot Proceed

**Date:** 2026-03-09
**Phase:** 0 (Wait for Final Science Freeze)
**Verdict:** BLOCKED — no dataset has reached 8/8 freeze gates

---

## What Is Missing

### 1. Paper 1 GPU Cohort_Main Frozen Pack — DOES NOT EXIST

No frozen pack has been created by `gpu_freeze_manager.py` because no dataset
has met all 8 convergence criteria simultaneously.

**Current freeze gate status (cohort_main, chains 2–7):**

| Dataset | Gates | Rm1(H0) | Rm1(ΔNeff) | Rm1(τ) | ESS(H0) | ESS(ΔNeff) | ESS(τ) | drift(H0) | drift(ΔNeff) |
|---------|-------|---------|------------|--------|---------|------------|--------|-----------|-------------|
| **full_tension** | **6/8** | 0.0036 ✅ | 0.0031 ✅ | 0.0071 ✅ | 781 ❌ | 694 ❌ | 1243 ✅ | +0.007σ ✅ | +0.007σ ✅ |
| planck_only | 5/8 | 0.0042 ✅ | 0.0035 ✅ | 0.0090 ✅ | 569 ❌ | 547 ❌ | 609 ❌ | -0.024σ ✅ | -0.035σ ✅ |
| planck_bao_sn | 4/8 | 0.0081 ✅ | 0.0126 ❌ | 0.0031 ✅ | 691 ❌ | 565 ❌ | 724 ❌ | -0.029σ ✅ | -0.016σ ✅ |
| planck_bao | 3/8 | 0.0266 ❌ | 0.0230 ❌ | 0.0059 ✅ | 479 ❌ | 440 ❌ | 840 ❌ | +0.062σ ✅ | +0.051σ ✅ |

**Freeze thresholds:** Rm1 < 0.01 (H0, ΔNeff), < 0.02 (τ); ESS ≥ 2000 (H0, ΔNeff), ≥ 1000 (τ); drift < 0.2σ

**Blocking factor for full_tension (lead dataset):**
- ESS(H0) = 781 → needs 2,000 (2.6× growth needed)
- ESS(ΔNeff) = 694 → needs 2,000 (2.9× growth needed)
- At current sampling rate (~1,200 samples/hr cohort), ETA ≈ **3–4 days (~March 13)**

### 2. CPU#1 Canonical ΔNeff Frozen Pack — DOES NOT EXIST

CPU1 is running ΔNeff model chains (4 chains × 4 datasets) as independent validation.
Current diagnostics confirm R-hat agreement with GPU but no frozen pack exists.

- CPU1 full_tension: Rm1(H0)=0.0034, Rm1(ΔNeff)=0.0064 — converging, not frozen
- Total CPU1 samples: ~48,820

### 3. CPU#2 ΛCDM Control Frozen Pack — DOES NOT EXIST

CPU2 is running ΛCDM control chains (4 chains × 4 datasets).
Current diagnostics show excellent R-hat but ESS not tracked for freeze.

- CPU2 full_tension: Rm1(H0)=0.0040, ESS(H0)=1369 — converging, not frozen
- Total CPU2 samples: ~49,643

### 4. Ablation Summary Table — DOES NOT EXIST

No standalone ablation table comparing ΔNeff model vs ΛCDM across datasets.
This requires both GPU and CPU2 frozen packs to produce.

### 5. Final Corner / Posterior Plots — DO NOT EXIST

No corner plots or posterior distribution figures have been generated from
the current chains. These require frozen chains to produce meaningful
publication-quality figures. Trace plots exist (8 PNGs) but are diagnostic,
not publication figures.

### 6. Final Convergence Diagnostics — EXIST BUT NOT FINAL

Convergence CSVs exist and are current (synced 2026-03-09) but reflect
in-progress chains, not final frozen state.

### 7. PolyChord Evidence Logs — DO NOT EXIST AND WILL NOT EXIST

Cobaya is configured with Metropolis-Hastings sampler, not PolyChord.
No log-evidence (ln Z) or Bayes factors (ln B) can be computed from
current chains. Model comparison must use Δχ², ΔAIC, ΔBIC only.

**Implication for paper:** Table V and any text claiming Bayes factor
evidence must be removed or replaced with information-criteria comparison.

### 8. WP4 Frozen Outputs — EXIST (COMPLETE)

WP4 parameter scans are finished and reproducible:
- Reheating scan: 24,000 points; 1,680 in target ΔNeff range [0.10, 0.20] (7.0%)
- Decay scan: 32,000 points; 796 in target range (2.5%)
- Best-fit ΔNeff ≈ 0.15 for both mechanisms
- 4 publication-quality figures generated (PDF + PNG)
- ΔNeff viability summary figure exists: `paper/figures/fig_dneff_viability.pdf`

**Status: READY for integration once MCMC chains freeze (figure Panel A
references MCMC posteriors that need final values).**

### 9. WP5 Frozen Outputs — PARTIALLY COMPLETE

WP5 theoretical framework is complete:
- Scaling relation: A₀ ≈ ε_PO × 0.015
- Required coupling: ε_PO ~ 0.2 for observed A₀ ~ 0.003
- Galaxy spin counts data compiled (5 surveys from Shamir 2024)

WP5 Monte Carlo sensitivity analysis: **NOT YET EXECUTED**
- Code is complete and tested (`monte_carlo_sensitivity.py`)
- `runs/` directory is empty — no MC samples generated
- This is low priority for Paper 1 (theoretical scaling is sufficient)

**Status: Theoretical result is usable now. MC validation is optional for Paper 1.**

---

## What IS Available Now (Non-Blocking Work)

The following can proceed without frozen chains:

1. **Galaxy spin section cleanup** (Phase 2D) — no MCMC dependence
2. **WP4 integration text** (Phase 2E) — WP4 scans are complete
3. **WP5 integration text** (Phase 2F) — theoretical scaling is complete
4. **P6/P7 handling** (Phase 2G) — editorial decisions only
5. **Limitations update** (Phase 2H) — editorial work
6. **Stale language grep/cleanup** (Phase 5 partial) — can remove known bad phrases
7. **PolyChord/Bayes factor claim audit** (Phase 2C partial) — can identify what to remove

---

## Estimated Timeline to Full Readiness

| Milestone | Dataset | Current Gates | Target | ETA |
|-----------|---------|---------------|--------|-----|
| full_tension freeze | full_tension | 6/8 | 8/8 | ~March 13 |
| planck_bao_sn freeze | planck_bao_sn | 4/8 | 8/8 | ~March 14 |
| planck_only freeze | planck_only | 5/8 | 8/8 | ~March 15 |
| planck_bao freeze | planck_bao | 3/8 | 8/8 | ~March 23+ |
| Corner plots generated | — | — | — | freeze + 1 day |
| Ablation table | — | — | — | CPU2 freeze + 1 day |
| Full Phase 1–7 execution | — | — | — | ~March 16–20 |

**Note:** The paper can potentially be submitted with 3/4 datasets frozen
(full_tension + planck_only + planck_bao_sn) while noting planck_bao is
still converging. This would allow submission by ~March 18.

---

## Recommendation

**Do not update any numerical values in the manuscript at this time.**

The chains are converging well (R-hat excellent for full_tension) but ESS
is the bottleneck. Premature number updates would need to be redone when
the chains actually freeze, creating unnecessary revision churn.

**What to do now:**
1. Let chains continue running undisturbed on all 3 pods
2. Optionally: begin non-MCMC editorial work (galaxy spin cleanup, WP4/WP5
   integration text, limitations update, stale language removal)
3. Check back in ~4 days (March 13) for full_tension freeze
4. Once full_tension reaches 8/8, run `gpu_freeze_manager.py` to create
   the frozen pack, then re-initiate this workflow from Phase 1

---

## Chain Health Summary

All 64 chains across 3 pods are healthy and actively writing:
- GPU: 28 chains (7 per dataset × 4 datasets), 113,834 total samples
- CPU1: 16 chains (4 per dataset × 4 datasets), 48,820 total samples (ΔNeff model)
- CPU2: 16 chains (4 per dataset × 4 datasets), 49,643 total samples (ΛCDM control)
- **Grand total: 236,622 samples, zero stalls, zero restarts needed**
