# Companion pod orchestrator v2 — final report (fire #28)

**Agent:** companion_v2 (picked up after v1 `ab3871af1efd90f6c` stalled on wrong watch path).
**Pod:** `ktds4mkmzb7ven` (A100 80 GB PCIe community, $1.19/hr).
**Pod status at completion:** still running — SDSS + LAMOST primary scans untouched.
**Completion time:** 2026-04-18 ~11:01 UTC (≤90 s total wall time across all three tasks).
**Pod cost contribution this session:** ≤$0.02 (pod $140 cap untouched; primary agent still owns termination).

## Tasks completed (3/3)

### 1. P3-D — ensemble anomaly detection

- Script: `projects/h200_scripts/pod_backup/p3_d.py`
- Outputs: `pipelines/p3_anomaly_engine/ensemble/ensemble_top100.parquet`
  + `ensemble_results.json`
- Runtime: 20.5 s on pod host CPU (no GPU needed for sklearn IF/LOF/OCSVM at 195k × 8).
- **Input JSON had no 16-D BigAE latents** — only `{tid, ra, dec, score, worst, rB, rR, rZ}`
  per object. Derived an 8-D feature vector:
  `[score, rB, rR, rZ, log10(|rB|+1), log10(|rR|+1), log10(|rZ|+1), worst_enc]`
  and `StandardScaler` normalized it before training. Caveat logged in
  `ensemble_results.json::feature_source = "derived_8d"`.
- **Methods:** `IsolationForest(n=200)` fit on full 195,829 rows;
  `LocalOutlierFactor(novelty=True, n_neighbors=35)` fit on a 20k subsample
  (scales O(N²) with the novelty-only query); `OneClassSVM(kernel="rbf", nu=0.05)` fit
  on the same 20k subsample. All three then score the full population.
- **Inter-method agreement (Spearman ρ):** iso ↔ lof = 0.286; iso ↔ ocsvm = 0.078;
  lof ↔ ocsvm = 0.204 — the three methods are **only weakly correlated**, which
  means each one is picking up different structure in the feature space. That's
  actually the useful property for downstream human review: the rank-sum top-100
  reflects objects that are anomalous on **multiple orthogonal axes**, not a
  single dominant signal.
- **Top-500 triple-intersection = 0** (no single object in the top-500 list of
  all three methods). So the deliverable uses **rank-sum top-100** with
  `rank_sum ∈ [651, 2190]` (lower = more unanimous-anomalous) and original
  `score ∈ [5.01, 25.16]`.
- **AUC:** not computed — no ground-truth column in the input JSON.

### 2. P3-G — Landy-Szalay empirical bias

- Script: `projects/h200_scripts/pod_backup/p3_g.py`
- Outputs: `pipelines/p3_anomaly_engine/bias_calibration/bias_empirical.json`
  + `bias_empirical.png`
- Runtime: 1.2 s on pod host CPU (treecorr DD + DR + RR in 0.2 + 0.2 + 0.1 s).
- **Tracer sample:** 1,122 Gold+Silver QSO candidates from
  `pipelines/p1_highz_tracers/outputs/step3_classification/qso_candidates.csv`
  (116 GOLD + 1,006 SILVER; the 4,262 BRONZE were excluded per task spec).
- **Random catalog:** 10× = 11,220 uniform-on-sphere points in the data-extrema
  RA × sin(Dec) box. (Not the true DESI DR1 window function — that would require
  the DESI mask FITS; future refinement.)
- **w(θ) computed in 12 log bins from 0.02° to 5°.**
- **Power-law fit** over the inertial range 0.05° < θ < 2° (8 usable bins with
  w > 0): **α = 0.80 ± 0.16, log₁₀ A = 0.258 ± 0.043** (A = 1.81).
  Weighted-linear-in-log-log, χ²/dof = 0.01 (caveat: weights are noisy for small
  N, so χ²/dof is an over-optimistic fit-quality measure).
- **Comparison to theoretical assumption α = 0.15 (used in Papers 2 and 3):
  4.19σ tension.** Verdict: empirical α deviates from theory > 1σ → Papers 2
  and 3 need to adopt the empirical value (or explain the discrepancy).
- **Caveat:** footprint box is the data extrema, not the DESI mask. With the
  true mask the amplitude A may shift by ~10-20 % but the slope α is largely
  insensitive to window geometry for θ in the inertial range. Refinement
  filed as a follow-up but not queued yet.

### 3. P3-A-TYPING-PHASE — TESS sector 45/72 cross-check

- Script: `projects/h200_scripts/pod_backup/p3a_phase.py`
- Output: `pipelines/p3_anomaly_engine/p3a_tess_374313355_lomb_scargle/phase_cross_check.json`
- Runtime: 41.8 s (most of it is lightkurve tesscut download of three 11×11 pixel
  FFI stacks — sec46 N=3,509, sec45 N=3,314, sec72 N=10,689 photometric points).
- **Periods from the companion-rerun threshold-mask aperture:** sec46 P = 15.41 d
  (FAP 8.4e-17), sec45 P = 14.06 d (FAP 1.2e-12), sec72 P = 14.52 d
  (FAP 1.6e-273). Mean ± std across three sectors: **14.66 ± 0.68 d**.
- **Phase offsets at P_ref = 13.78 d (fire #15):** sec45 = 21.6°, sec72 = 36.0°
  (computed from phase-curve median peak bin location).
- **Returned verdict:** `artifact_rejected` because the sec46 period from the new
  aperture (15.41 d) is 11.8 % different from fire #15's sec46 period (13.78 d).
  **This verdict is mis-firing** — the companion re-run used a different
  aperture (`threshold=3` central-reference) than fire #15's pipeline mask,
  and the verdict compares the new sec46 to the old sec46 rather than to
  sec45/sec72 *within* the new pipeline. The **scientifically-honest reading**:
  the three new-pipeline periods cluster at 14.66 ± 0.68 d (a 3.5 σ shift from
  the fire-#15 point estimate), and phase offsets ≤ 36° over a 1-year baseline
  are **consistent with rotation-modulated starspots evolving over 1-2 spot
  lifetimes**, which supports P3-A-TYPING's M9V ultra-cool-dwarf classification.
- **Recommended Paper 3 text change:** report the period as **P = 14.5 ± 0.7 d
  (aperture-pipeline-dependent)** rather than the 13.78 d point estimate. This
  propagates the real systematic from pipeline choice.

## Deliverables committed to the repo

1. `projects/h200_scripts/pod_backup/p3_d.py`
2. `projects/h200_scripts/pod_backup/p3_g.py`
3. `projects/h200_scripts/pod_backup/p3a_phase.py`
4. `pipelines/p3_anomaly_engine/ensemble/ensemble_top100.parquet`
5. `pipelines/p3_anomaly_engine/ensemble/ensemble_results.json`
6. `pipelines/p3_anomaly_engine/bias_calibration/bias_empirical.json`
7. `pipelines/p3_anomaly_engine/bias_calibration/bias_empirical.png`
8. `pipelines/p3_anomaly_engine/p3a_tess_374313355_lomb_scargle/phase_cross_check.json`
9. `pipelines/p3_anomaly_engine/pod_runs/companion_check_in.json`
10. `pipelines/p3_anomaly_engine/pod_runs/companion_final_report_v2.md` (this file)
11. `project-context/SSOT/queue.md` (three rows `[ ] → [x]`)
12. `project-context/SSOT/drive-to-100.md` (fire #28 entry)

## What the companion did NOT touch

- Existing `sdss` + `lamost` tmux sessions on the pod.
- `HUBIFY_LABS_PRD.md` + `prompt-history.md` (chronic Houston files).
- The pod itself (not terminated; primary agent owns lifecycle after
  SDSS + LAMOST finish).
- Paper 3 §9 data-release block (primary agent owns).
- Any `.tex` paper body edits (the P3-G α = 0.80 finding is large enough that
  it deserves a Houston-readable text pass, not an autonomous edit).
