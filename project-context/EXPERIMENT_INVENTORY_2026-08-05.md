# BigBounce experiment inventory — 2026-08-05

**Sweep for directive Q2 reproducibility manifests.** Venue/cost/time cited only where evidence exists in-repo; gaps listed at the end are real gaps, not omissions.

# BigBounce Reproducibility Manifest Sweep — Discrete Experiment Inventory

Repo: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce`. This is a search/inventory pass per Houston directive 2026-08-05 (standing directive Q in `CLAUDE.md`) ahead of building per-experiment reproducibility manifests. Programs follow the canonical map in `project-context/PUBLICATION_AND_RELEASE_MASTER_MAP_2026-08-04.md`: **bounce-theory** (P2, P1A, P1B), **anomaly** (rebuilt DESI flagship + P3 supporting release), **chirality** (P4, P5).

---

## PROGRAM: bounce-theory

### P2 — f_NL forecast / exact matter-contraction non-Gaussianity (PRD)
Source: `research/focused_paper_source_integration/02_full_draft.tex`, `research/cubic_bounce_transmission/`. SSOT: `project-context/SSOT/paper-2/status.md`, `COMPUTE_CAMPAIGN_2026-07-17.md`.

- **exp: vertex-check / four-vertex −35/16 amplitude derivation**
  scripts: `research/focused_paper_source_integration/scripts/p2_vertex_check.py`, `fig_4vertex_sum.py`, `exact_shape_analysis.py`
  inputs: none external (pure sympy symbolic algebra)
  outputs: quadruple-certified `f_NL^local = -35/16`, equilateral `-255/128`
  venue: local CPU, sympy · cost: $0 · runtime: minutes
  reproducibility: runnable-now

- **exp: G1 gradient-transmission scheme-dependence (Phase 1)**
  script: `research/cubic_bounce_transmission/g1_gradient_transmission_scheme.py`
  outputs: `g1_gradient_transmission_results.json` + `.log` — demonstrates transmission-coefficient scheme-dependence (c ~ 1/dcut)
  venue: local CPU · cost: $0 · runtime: seconds-minutes (log timestamp 2026-07-17 13:47)
  reproducibility: runnable-now

- **exp: G1 dressed-metric (Wilson–Ewing) transmission closure**
  scripts: `research/cubic_bounce_transmission/g1_dressedmetric_transmission.py`, `g1_dressedmetric_ic_close.py`
  outputs: `g1_dressedmetric_transmission.json`, `g1_dressedmetric_ic_close.json` — T_c(k)=1, |δf_NL| ≤ 6.8e-8 at kη_B=1e-2, folded into v1.7.125 (commit `e641cb1c`)
  venue: local CPU · cost: $0 · runtime: seconds (logs dated 2026-07-17)
  reproducibility: runnable-now

- **exp: G3 torsion four-fermion bound (Einstein–Cartan estimate)**
  script: `research/cubic_bounce_transmission/g3_torsion_fourfermion_bound.py`
  outputs: `g3_torsion_fourfermion_bound.json`/`.log`, folded into v1.7.123 Eq. 5 (commit `275846c5`)
  venue: local CPU, sympy · cost: $0 · runtime: seconds
  reproducibility: runnable-now

- **exp: honest-negative in-in bounce attempts (superseded, retained as provenance)**
  scripts: `pathz_full_inin_bounce.py` (2026-07-02, `pathz_results.json`), `pathz2_calibrated_inin.py` (2026-07-03, `pathz2_results.json`)
  venue: local CPU · cost: $0
  reproducibility: runnable-now (historical-negative, not re-run for headline)

- **exp: channel-native Fisher surrogate (c15) + covariance chain (c8–c15)**
  scripts: `research/focused_paper_source_integration/scripts/c8_fnl_running_fisher.py` … `c15_channel_native_fisher.py`, `c10_joint_covariance_marginalization.py`, `p2_joint_cov.py`
  inputs: CAMB (via `c13`); Heinrich et al. 2023 SPHEREx covariance NOT publicly released (external-data-gated, DP2-26/-29)
  outputs: `outputs/c15_channel_native_fisher.json` — nuisance ladder 3.5σ/3.1σ/2.3σ/0.4σ
  venue: local CPU · cost: $0 · runtime: hours-scale (CAMB calls)
  reproducibility: runnable-now (surrogate); needs-data-restore (true Cov_B — external author release required)

### P1A — algebraic Cartan elimination (CQG Note)
Source: `arxiv/main.tex` (+ `paper1a_arxiv_v1A.0.x.tar.gz` waves). Zenodo `10.5281/zenodo.21481838`.
- **exp: MCMC — full-tension / Planck+BAO+SN / third combo (ΔNeff)**
  configs: `reproducibility/cosmology/cobaya_full_tension.yaml`, `cobaya_planck_bao_sn.yaml`, `cobaya_planck.yaml`, `cobaya_planck_bao.yaml`
  outputs: `reproducibility/cosmology/paper1_clean_restart_sync/chains/dneff/{full_tension,planck_bao_sn,<combo>}/` — 176,240 / 132,949 / ~114,992 samples (424,181 total)
  venue: **RunPod — "CPU5 Compute-Optimized" pod, 32 vCPU/64GB** (`manifests/MANIFEST.md`) — no GPU used
  cost/time: not explicitly dollar-logged in manifest; hourly manifest snapshots span 2026-03-11 02:00→17:00 UTC (≥15h wall-clock observed from timestamped manifest series)
  reproducibility: runnable-now (Cobaya configs + covmats committed)

- **exp: 500-MC NaMaster EB birefringence recovery (β)**
  script family: `reproducibility/p1_namaster_500mc/scripts/` (`physical_spectra.py`, checkpoint/resume harness)
  outputs: `reproducibility/p1_namaster_500mc/results/summary.json` — nside 512, lmax 1024, f_sky 0.3226, 500 MC realizations; recovered β=0.238° (input 0.27°) SNR 20.3
  venue: RunPod (budget launcher `runpod_budget_launcher.py`, `runpod_production_contract.json` — zero-spend preflight contract; watchdog-deletion gates documented as open)
  cost/time: not dollar-logged in this artifact; C1 companion (`h200_scripts/experiments/c1_p1b_namaster_fsky_sweep.py`) ran on pod `5i2td3deu3hojr` (A4000, jobs CPU-bound, **$0.17/hr**), ETA ~1.3h at NSIDE=512 (`project-context/SSOT/compute-queue.md`)
  reproducibility: runnable-now

- **exp: 100,000-sample N_tot sensitivity Monte Carlo**
  path: `research/sensitivity_scan/` — Spearman |ρ_s|=0.996
  venue: local CPU (implied — no pod reference) · cost: $0
  reproducibility: runnable-now

- **exp: ALP prior-predictive / spectator-conditioned prior-predictive**
  scripts: `reproducibility/cosmology/alp_prior_predictive.py`, `alp_spectator_conditioned_prior_predictive.py`
  outputs: `alp_prior_predictive_result.json`, `alp_spectator_conditioned_prior_predictive_receipt.json`
  venue: local CPU · cost: $0
  reproducibility: runnable-now

### P1B — `namaster-proof` software metapaper (JORS). Zenodo `10.5281/zenodo.21481753` (software), `10.5281/zenodo.21481842` (paper).
- **exp: SN-overlap control chains A (Pantheon+) / B (DES-SN5YR)**
  configs: `reproducibility/cosmology/cobaya_control_pantheonplus.yaml`, `cobaya_control_desy5.yaml`
  venue: **RunPod pod `99srknm4s1cc3l` ("bigbounce-p1b-snctrl"), RTX A4000, EUR-IS-1, $0.17/hr**, network volume `bigbounce-paper1-canonical`
  outputs: Control A w0=-0.874±0.059/wa=-0.530±0.241; Control B w0=-0.787±0.063/wa=-0.785±0.263 (`w0wa_control_chains_result.json`); DONE 2026-07-01
  cost/time: RunPod balance ~$7.86 at launch (from queue notes); explicit $ total not logged, only $/hr rate
  reproducibility: runnable-now

- **exp: NaMaster window regenerability check (pymaster 3.0)**
  script: `packages/namaster-proof/examples/rebuild_workspace_check.py`
  venue: RunPod A4000 pod `580dgszgib3ti4` (shared with P4 G3 MASTER-leg session, 2026-07-18)
  outputs: `rebuild_workspace_check_2026-07-18_podA4000.log` — max|Δ|=9.926e-24 < 1e-10 PASS
  cost/time: bundled into the ~2.1h/$0.36 phase-2 pod session (see P4 G3 below)
  reproducibility: runnable-now

---

## PROGRAM: chirality

### P4 — Galaxy Chirality Catalog (ApJS). HF `bamfai/galaxy-chirality-catalog`, `bamfai/galaxy-chirality-v2`. Zenodo `10.5281/zenodo.21461899`. SSOT: `project-context/SSOT/paper-4/status.md` + `COMPUTE_CAMPAIGN_2026-07-17.md`.

- **exp: v2 ViT-Small production training (26,616-object historical realization)**
  script: `pipelines/p2_chirality/train_chirality_v2.py`
  inputs: `Smith42/galaxies` HF (rev `bdd1b063…`), GZ1 CW/CCW S3 labels, CE-ResNet Zenodo `10.5281/zenodo.7167388` (`pre_desi.fits`), Galaxy Zoo DESI predictions (Walmsley 2023)
  outputs: HF `bamfai/galaxy-chirality-v2` checkpoint
  venue: historical H200 pod (checkpoint SHA `618d170f…`) · reproducibility: superseded (labels/manifest not retained — see G1 below)

- **exp: G1 — regenerable ViT-Small retrain w/ manifest (supersedes historical training)**
  scripts: `pipelines/p2_chirality/train_g1_manifest.py`, `scripts/g1_ce_composition_assembly.py`
  inputs: `Smith42/galaxies` HF, GZ1 S3, GZ-DESI crossmatch rev `b7583bb2…`, CE-ResNet Zenodo `10.5281/zenodo.7167388`
  venue: **RunPod A4000 — pod `580dgszgib3ti4` (smoke), fresh on-demand pod `th0o0l1tp1se4e` (full retrain, $0.17/hr)**
  cost/time: smoke ~$0.26 (1.5h); full G1 lane running total < $1 (per-uptime spans ~4.2h ≈ $0.71 recorded for one pod window); best_val_acc=0.9931 @ epoch 47, early-stop epoch 62
  outputs: `outputs/g1_retrain/g1_ckpt_best.pt` (sha256 `aed109dc…`), `g1_training_manifest.json`, `g1_training_result.json`; 3-location backup verified (local + HF `g1-retrain-2026-07-17/` + pod, hash round-trip MATCH)
  reproducibility: runnable-now (manifest-bound)

- **exp: G1 CE-included full composition (826-vs-846 adjudication)**
  script: `pipelines/p2_chirality/scripts/g1_ce_composition_assembly.py`
  outputs: `outputs/g1_full_composition/g1_full_composition_manifest.json` (26,609 objects; ce_not_spiral=819, adjudicated)
  venue: local CPU (GPU host was capacity-full; CPU-only composition-assembly stage) · cost: $0
  reproducibility: runnable-now

- **exp: G2 — training-disjoint held-out GZ1 validation**
  script: `pipelines/p2_chirality/analysis/g2_disjoint_validation_v1_0_266.py`
  venue: RunPod A4000 (pod inference) · runtime: 358s
  outputs: `g2_disjoint_validation_v1_0_266.json` — accuracy 0.9867, κ=0.9733 on n=3000 disjoint GZ1 spirals
  reproducibility: runnable-now

- **exp: G3 — joint estimator covariance (local + MASTER-leg refinement)**
  scripts: `scripts/g3_joint_estimator_covariance.py` (local), `scripts/g3_joint_estimator_covariance_master_v2.py` (pod, pymaster)
  venue: local leg = local CPU, $0, ~573s (N=2000 bootstrap); MASTER-leg = RunPod A4000 pod `580dgszgib3ti4`, ~62 min within a 2.1h/$0.36 phase-2 session
  outputs: `outputs/canonical_provenance/g3_joint_estimator_covariance.json` + `..._master_v2.json`; backed up local+HF(`p4_compute_phase2_2026-07-18/`, sha256-verified)+pod
  reproducibility: runnable-now (closed-by-artifact)

- **exp: G4 — per-pixel confusion + generative parity-null (monopole mechanism)**
  script: `pipelines/p2_chirality/scripts/g4_monopole_mechanism_injection.py`
  inputs: reuses banked `e2e_mirror_pairs.parquet` (see e2e run below) — **no new GPU inference required**
  venue: RunPod A4000 (aggregation only) — **$0 H200 spend**, avoided est. $20–50
  outputs: `outputs/canonical_provenance/g4_monopole_mechanism_injection.json`, `g4_perpixel_confusion_nside64.npz`
  reproducibility: runnable-now

- **exp: e2e mirror-flip full-catalog inference (8.47M galaxies × 2 passes)**
  scripts: `scripts/e2e_mirror_flip_fullrun.py`, `scripts/e2e_mirror_flip_transfer_function.py`
  venue: **RunPod A100 pod `0hh3humgpacgz1`, "bigbounce-p4-e2e-mirror" ($1.19/hr rate quoted elsewhere)**
  cost/time: **wall 10.45h, cost ≈ $12.44 (cap $20)**, 192/192 shards, 16,949,062 inferences (2026-07-11/12)
  outputs: `e2e_transfer_function_full.json` (md5 `925649b7…`); T_raw=0.2303, T_eq=0.99974; backed to HF + B2 + local (685MB shards not in git)
  reproducibility: runnable-now (this is the best-documented cost/venue/time experiment in the repo)

- **exp: A_95^obs coverage-calibrated dipole injection upper limit**
  script: `pipelines/p2_chirality/analysis/a95_observed_label_upper_limit_v1_0_265.py`
  venue: local CPU · cost: $0 · runtime: **597.7s (~10 min)**, logged exactly (`a95_run.log`)
  outputs: `a95_observed_label_upper_limit_v1_0_265.json` — A_95^obs = 0.98%
  reproducibility: runnable-now (best time-logged example)

- **exp: C1/C2/C3 NaMaster MC batch (monopole/dipole nulls, fsky sweep)**
  scripts: `h200_scripts/experiments/c2_p4_nall_binomial_null.py`, `c3_p4_wp_invariance_fsky.py`, `c1_p1b_namaster_fsky_sweep.py`, `launch_c123_pod.sh`
  venue: **RunPod pod `5i2td3deu3hojr`, RTX A4000, $0.17/hr, 12 vCPU/62GB** (jobs CPU-bound NaMaster MC)
  cost/time: C2 DONE 358s; C3 DONE 387s; C1 ETA ~1.3h (`project-context/SSOT/compute-queue.md`)
  outputs: `pipelines/p2_chirality/outputs/canonical_provenance/{c2_nall_binomial_null,c3_wp_invariance_fsky}.json`
  reproducibility: runnable-now

- **exp: GZ1-only classifier retrain + dipole null (pseudo-label independence check)**
  script variant: `train_chirality_gz1only.py` (staged from `train_chirality_v2.py`)
  venue: RunPod pod `8ol1r8eew7h6br`, "bigbounce-p4-gz1only", RTX A4000 16GB community, $0.17/hr
  outputs: `outputs/gz1only_dipole_result.json` — dipole z=-0.04σ; DONE 2026-07-01
  reproducibility: runnable-now

- **exp: empirical b/a (axis-ratio) DR8 morphology cross-match**
  inputs: `ls_dr8.tractor` via NOIRLab Astro Data Lab TAP (external API)
  outputs: `outputs/spiral_morphology_dr8.parquet`, `edge_on_contamination_metric.json` — f_edge=15.8%
  venue: "spot A4000 that is now EXITED" (no dollar figure recorded) · DONE 2026-07-02
  reproducibility: needs-data-restore (pod exited, TAP-pulled data not re-fetched, though script is runnable)

- **exp: dipole analysis (8.47M full-catalog)**
  script: `run_dipole_8M.py`
  outputs: `pipelines/p2_chirality/outputs/dipole/summary.json`, figures — 2.31σ raw, 0.43σ post-TTA
  venue: H200 pod (historical, terminated 2026-04-17) · reproducibility: needs-data-restore (full dipole JSON partially reconstructed from log, not re-run)

### P5 — Environmental Dependence of Spiral Chirality (AJ). SSOT: `project-context/SSOT/paper-5/status.md`.
- **exp: P4×DESI DR1 crossmatch + matched catalog build**
  scripts: `pipelines/p5_desi_chirality/scripts/01_fetch_p4_catalog.py`, `02_fetch_desi_dr1.py`, `03_crossmatch.py`
  outputs: `results/p5_matched_chirality_desi.parquet` (1.3GB, 2,232,212 rows)
  venue: not explicitly logged (implied local/CPU-bound crossmatch) · reproducibility: runnable-now

- **exp: redshift / density / HEALPix / systematics analyses (scripts 05–09)**
  outputs: `results/analysis_{redshift,density,healpix,systematics}/`
  venue: local CPU (no pod reference found) · reproducibility: runnable-now

- **exp: cosmic-web / DESIVAST void analysis (16, 27, 35–39 series)**
  scripts: `16_cosmic_web_zshell_corrected.py`, `27_rsd_void_recon_bound.py`, `35_desivast_cluster_bootstrap.py`, `36_desivast_native_selection_control.py`
  inputs: DESI DR1 DESIVAST VAC — `https://data.desi.lbl.gov/public/dr1/vac/dr1/desivast/v1.0/`
  outputs: `27_rsd_void_recon_bound.json` (DP5-12 closure, 2026-07-12)
  venue: not dollar/hour logged (grep found no RunPod hit in p5 scripts) · reproducibility: runnable-now, gap = no venue/cost evidence
  **Note:** the original "187-DESI-attribute cosmic-web catalog" blocker (SSOT: "Houston-mediated, confirmed not in repo") was later resolved via DESIVAST VAC (r24conf/r27conf closures) — superseding the earlier `env_finder/` "run our own cosmic-web finder" fallback plan.

- **exp: r23conf/r24conf/r27conf closure recomputes + focal cluster inference**
  scripts: `21_r23conf_meta_closures.py`, `22_r24conf_local_batch.py`, `24_r24conf_pod_session.py`, `26_r27conf_ess_recomputes.py`, `38_focal_cluster_inference_sensitivity.py`, `39_focal_interaction_clustering_robustness.py`
  venue: `24_r24conf_pod_session.py` name implies RunPod use but no pod ID/cost found in status.md grep — gap
  reproducibility: runnable-now (code present) / venue evidence missing

- **exp: astra per-object crossmatch + HF mirror**
  scripts: `15_astra_per_object_crossmatch.py`, `mirror_astra_to_hf.py`
  outputs: HF `bamfai/astra-desi-edr-mirror` (from repo-wide HF grep)
  reproducibility: runnable-now

---

## PROGRAM: anomaly

### Rebuilt DESI anomaly-science flagship (future primary paper) — `pipelines/p1_highz_tracers/`
Per `project-context/ANOMALY_SCIENCE_CLAIM_INVENTORY_2026-08-03.md`, these are historical/pre-rebuild experiments, now labeled comparison-only, PLUS the in-progress `clean_rerun` campaign.

- **exp: BigAE enhanced 18M/22.5M-row DESI inference (historical, unreconciled)**
  script: `pipelines/p1_highz_tracers/scripts/enhanced_18M_inference.py`
  outputs: `outputs/enhanced_18M_deduped/catalog_summary.json` — 22,504,897 rows claimed, 46 Parquets absent locally
  model: `best_model_47k.pt` (archived, 4 byte-identical local copies, sha256 `f5266ba4…`; HF rev `8100e093…` matches)
  venue: historical pod (unlogged) · reproducibility: **superseded / needs-data-restore** (restoration gate FAILED 2026-08-04 — cannot be truthfully reconstructed)

- **exp: silver crossmatch (2,145-row SNR-filtered slice)**
  script: `pipelines/p1_highz_tracers/scripts/silver_crossmatch.py`
  outputs: `outputs/silver_crossmatch/silver_crossmatch_summary.json`
  reproducibility: runnable-now (result JSON preserved; recountable per audit)

- **exp: uncataloged taxonomy (1,127 objects, 10 families)**
  outputs: `outputs/uncataloged_taxonomy/taxonomy_results.json`, `taxonomy_summary.md`
  reproducibility: runnable-now (recountable, "strongest candidate-science centerpiece" per audit)

- **exp: injection recovery (per-class completeness/false-positive)**
  script: `pipelines/p1_highz_tracers/scripts/injection_recovery_test.py`
  outputs: `outputs/injection_recovery/{false_positive_analysis,injection_recovery_results}.json`
  reproducibility: runnable-now, but headline "0% FP / 10-1,377x enrichment" claim is **contradicted/overstated** per audit — needs re-derivation

- **exp: NEOWISE crossmatch (IR variability)**
  outputs: `outputs/neowise_crossmatch/crossmatch_summary.json` — 16/283 meet variability rule
  reproducibility: runnable-now

- **exp: gold anomalies — z6 QSO spectra**
  scripts: `download_z6_qso_spectra.py`, `replot_z6_spectra.py`
  outputs: `outputs/gold_anomalies/spectra/z6_qsos_detailed.json` — 12 DESI Redrock z>6 QSO candidates (no independent redshift validation)
  reproducibility: runnable-now

- **exp: photo-z from latent vectors**
  outputs: `outputs/photo_z/metrics.json` — σ_NMAD=0.0279 (supervised MLP, 800k train/200k test)
  reproducibility: needs-data-restore (depends on the absent 22.5M enhanced parent's latent features)

- **exp: f_NL tracer selection / step4-6 (bias validation, alpha empirical)**
  scripts: `step4_bias_validation.py`, `wave_14_vvv_alpha_empirical.py`
  outputs: `outputs/fnl_tracer_selection/fnl_forecast.json`, `step6_alpha_empirical/alpha_empirical_results.json` — **"not a result," α consistent with 0** per audit
  reproducibility: runnable-now (negative result — do not headline)

- **exp: clean_rerun campaign (AUG-011) — completed sealed generation 2026-08-07**
  scripts: `pipelines/p1_highz_tracers/clean_rerun/{derive_locator_inventory.py,build_calibration.py,run_scan.py}`, contract `clean_rerun_contract.py`
  inputs: DESI DR1 `iron` zcatalog `https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/zcatalog/v1/zall-pix-iron.fits` (sha256-pinned, ~27GB), full coadd corpus (multi-TB, streamed/deleted per-pixel), archived `best_model_47k.pt`
  venue: **RunPod, "A4000-class GPU or CPU-strong instance," ~200GB volume** (download-bound not GPU-bound, per RUNBOOK.md §0)
  outputs: sealed calibration/contract plus `clean_rerun/results_2026-08-07/{summary,comparison}.json`. The full scan receipt check verified 36,634/36,634 shards; the independent post-dedup generation has 28,425,963 raw rows, 27,547,223 unique TARGETIDs, 878,740 duplicate rows removed, and 52,188 `S>5` candidates.
  cost/time: completed in about 45.5h on RunPod A4000 `tc291bka0r6fl3` at $0.17/hr (about $7.74); this is a recorded run, not a prospective estimate.
  reproducibility: scan completed and provenance-bound. The full shard/receipt corpus and downstream selected sample are not in this checkout; the named HF mirror was not anonymously accessible at this audit. Sample selection, validation, taxonomy, and manuscript work remain pending.

### P3 — DESI Public-ID Recovery Catalog (supporting release, not standalone paper). HF `bamfai/bigbounce-anomaly-catalog`, GitHub `Hubify-Projects/bigbounce`, Zenodo `10.5281/zenodo.21461888`.
- **exp: DP3-15 held-out re-inference (structural-ceiling demonstration)**
  script: `pipelines/p3_anomaly_engine/dp3_15_heldout_reinference.py`
  venue: **local CPU, $0, 0 GPU-hours** (explicitly stated in status.md line 63)
  outputs: bound = ~1.3% of released rows re-pullable via SPARCL; 5-seed BigAE ensemble reproduces MSE median 0.233 + injection-recovery 99-100%@5σ
  reproducibility: runnable-now

- **exp: 6-way / 7-way / 8-way positional dedup**
  scripts: `pipelines/p3_anomaly_engine/reproduce_headline_dedup.py`, (historical `sixway_dedup.py`, `pathc_positional_dedup.py`)
  venue: local CPU, $0 · DONE 2026-06-30
  outputs: `outputs/sixway_dedup_artifact.{json,csv}` — 275,151→269,317 unique (2.12% collapse)
  reproducibility: runnable-now

- **exp: DESI 5-fold cross-validation reproducibility gate**
  path: `pathc_desi_kfold/results/` — mean pairwise Jaccard 0.862 (≥0.70 gate PASS)
  reproducibility: runnable-now

- **exp: Planck held-out membership test + native re-inference (partial)**
  outputs: `held_out_rescore_result.json` — 48/200 in held-out split vs 30 expected
  venue: needs `best_cmb_native.pt` + `cmb_native_patches.npy`, on a now-EXITED pod, not in HF release
  reproducibility: **needs-data-restore** (full native re-inference BLOCKED)

- **exp: eROSITA scaler-leakage bounded control**
  output: `pipelines/p3_anomaly_engine/erosita_scaler_refit.json` — top-298 overlap 257/298 (J=0.76)
  reproducibility: runnable-now; NEOWISE/Gaia train-split scaler refits remain **compute-gated, not yet run**

- **exp: NANOGrav 15-yr free-spectrum PTA MCMC**
  script: `pipelines/p3_pta_mcmc/free_spectrum_real_2026-05-01/emcee_freespec.py`
  outputs: `results.json`, `chain_real_freespec.npy` — γ=3.20±0.42, 192,000 samples (32 walkers × 6,000 steps); ΔBIC=7.0 (`savage_dickey_2026-05-29.json`)
  venue: not dollar/pod-logged in this directory (likely local emcee, CPU) — gap
  reproducibility: runnable-now (code present) / venue evidence missing

- **exp: multi-survey summary / cross-match / spatial-clustering / score-distributions (8 surveys)**
  raw source: `pipelines/h200_results/pod_backup_20260408_full/…` (H200 snapshot, pod rotated/exited)
  reproducibility: needs-data-restore (raw per-survey outputs only survive in an old pod-backup snapshot dir, not regenerated)

- **exp: UMAP multi-seed stability (Pod 1 production)**
  output: `pipelines/h200_results/pod1_namaster_umap_2026-04-29/results/umap/umap_stability.json`
  venue: implied H200 pod (dir name `pod1_namaster_umap_2026-04-29`) — no $/hr logged in the artifact itself
  reproducibility: needs-data-restore (pod exited)

---

## Counts per program (discrete experiments/compute-runs identified)

| Program | Papers | Discrete experiments found |
|---|---|---|
| bounce-theory | P1A, P1B, P2 | 13 (P2: 6 · P1A: 4 · P1B: 2, minus double-count of shared pod session) |
| chirality | P4, P5 | 20 (P4: 13 · P5: 7) |
| anomaly | P3 + rebuilt flagship (p1_highz_tracers) | 18 (flagship/historical: 9 · clean_rerun complete: 1 · P3: 8) |
| **Total** | 6 papers + 1 supporting release | **~51 discrete experiments/runs** inventoried (not exhaustive — h200_results/ alone holds 30+ additional per-survey artifact directories not individually itemized above, e.g. `taxonomy-retuned`, `spatial-clustering`, `emission_lines`, `desi-taxonomy`, each with its own JSON but no dedicated compute-manifest doc) |

---

## Top 5 gaps — venue/cost/time evidence missing

1. **P1 highz_tracers `clean_rerun` full scan (AUG-011)** — the single highest-priority gap is now the follow-on work: the completed scan verified 36,634/36,634 shards, produced the post-dedup summary with 28,425,963 raw rows, 27,547,223 unique TARGETIDs, 878,740 duplicate rows removed, and 52,188 `S>5` candidates, and ran for about 45.5h on RunPod A4000 `tc291bka0r6fl3` at $0.17/hr (about $7.74). RUNBOOK's venue note ("A4000-class or CPU-strong, download-bound") remains useful for provenance; the open gap is the defensible selected sample, validation contract, taxonomy, named follow-up set, and manuscript.

2. **P3 NANOGrav PTA MCMC (`free_spectrum_real_2026-05-01/emcee_freespec.py`)** — 192,000-sample run with a full results JSON and chain file, but no RunPod pod ID, GPU/CPU class, $/hr, or wall-clock anywhere in `pipelines/p3_pta_mcmc/` or the referencing SSOT sections found.

3. **P5 cosmic-web / DESIVAST + r24conf "pod session" scripts (`24_r24conf_pod_session.py`, `36_desivast_native_selection_control.py`, etc.)** — script names imply RunPod use but no pod ID, GPU class, cost, or runtime was found in `pipelines/p5_desi_chirality/` or in the reachable sections of `paper-5/status.md`.

4. **P3 multi-survey raw per-survey outputs (`pipelines/h200_results/pod_backup_20260408_full/…`, `pod1_namaster_umap_2026-04-29/`, and ~28 sibling `h200_results/` subdirectories)** — dozens of historical H200-pod artifact directories exist with result JSONs but essentially no accompanying $/hr or wall-clock manifest; venue is inferable only from directory naming convention ("h200_results"), not from a receipt.

5. **P4 empirical b/a DR8 morphology cross-match** (`edge_on_contamination_metric.json`) — status.md states it ran on "a spot A4000 that is now EXITED" with no dollar figure or duration recorded, and the NOIRLab Astro Data Lab TAP query parameters (the external API call itself) aren't captured as a standalone provenance artifact.

Honorable mention: P2's `c13`/CAMB-based Fisher chain (`c8`–`c15` scripts) is explicitly local-CPU with no $/hr issue, but none of the individual script runtimes are logged (only "a few hours" estimates in `COMPUTE_CAMPAIGN`), so exact wall-clock is missing across that whole family.
