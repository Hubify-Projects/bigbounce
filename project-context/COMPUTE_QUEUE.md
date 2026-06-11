# COMPUTE_QUEUE — bounded compute tasks deferred from the EXT3 closure wave

Created 2026-06-11 during the EXT3 final closure wave. Rule applied: each EXT3
compute item was attempted ONLY if it runs locally from existing artifacts in
<30 min CPU. Two of the three bounded tasks ran locally and are CLOSED; the
items below did not meet the bound (remote data / network / pod-bound) and are
queued with exact specs.

## Status of the three EXT3 bounded compute tasks

| Task | Status |
|------|--------|
| P4 flip-identity QC (NF-M1) | ✅ DONE locally — artifacts `pipelines/p2_chirality/outputs/canonical_provenance/ext3_nfm1_flip_identity_qc.json` + `ext3_nfm1_hc_dipole_qc_rerun.json`; tex updated (App B). Finding: violations are a raw/eq pipeline-pass mismatch (2.9% any-channel / 1.27% single-channel, excursions ≤0.09), NOT float32; HC dipole unchanged (z=+0.48 excluded vs +0.52 baseline). |
| P5 footprint retabulation (B1, thrice-flagged) | ✅ DONE locally — artifact `pipelines/p5_desi_chirality/outputs/29_ext3_desivast_footprint_retabulation.json`; tex updated (§VIII HEALPix scan). Footprint-restricted Δf_CW=+0.0018, z=+0.78, p=0.43 — clean null; proxy attribution confirmed. |
| P3 DESI TARGETTYPE recount (B2, thrice-flagged) | ✅ DONE locally 2026-06-11 via the documented fallback (positional rejoin of the 190,015 DESI clusters vs `desi_zall.parquet` at 1″, cKDTree unit vectors) — artifact `pipelines/p3_anomaly_engine/ext3_b2_targettype_recount.json`; tex updated at 5 sites, v3.1.93. **Result: 2,468 science-class matches (1.3%) → restricted catalog ≈0.9× Liang 2023, NOT 73×; ~98.7% of DESI anomaly clusters sit on sky/secondary/filler spectra (86% DESI_TARGET==0). Control match vs full zall: 99.8% — join sound.** |

## Queued tasks

### 1. ✅ DONE (2026-06-11, landed in v3.1.93) — P3 DESI TARGETTYPE-restricted anomaly recount (EXT3 B2, thrice-flagged)
- **What:** Re-count the DESI DR1 anomaly headline restricted to spectra with a
  validated science `TARGETTYPE` in the five primary classes (BGS, LRG, ELG,
  QSO, MWS; ~6.5M of the 22,504,897 scanned), using the existing per-spectrum
  canonical-S scores at the published S > 5.0 cut.
- **Why:** The 195,829 / 0.87% / "~73×" headline is a full-22.5M-scan figure
  (incl. ~16M filler/sky/calibration spectra) while the size benchmark
  (Liang 2023) is science-target-only; disclosed at `paper3_draft.tex` l.256 +
  §III.A (l.408) with the recount labeled queued.
- **Needs:** pod-side per-spectrum DESI anomaly table WITH TARGETIDs (the
  local `hf_staging/pathc_unique_objects_no_act.parquet` carries only synthetic
  `desi_dr1_N` member ids — checked 2026-06-11, no TARGETID join possible
  locally). Local fallback if the pod table is lost: positional rejoin of the
  190,015 DESI cluster (ra_mean, dec_mean) against
  `pipelines/p5_desi_chirality/data/desi_zall.parquet` (carries
  DESI_TARGET/BGS_TARGET bits) at 1", then count anomalies and the ~6.5M
  denominator under the five primary TARGETTYPE classes. ~1 hr either way.
- **Lands in:** `pipelines/p3_anomaly_engine/paper3_draft.tex` l.256 + l.408 +
  new artifact JSON (suggested: `pipelines/p3_anomaly_engine/ext3_b2_targettype_recount.json`).

### 2. ✅ eROSITA leg DONE (2026-06-11, v3.1.96) / NEOWISE+Gaia legs still queued — P3 FM1 scaler-refit robustness check
- **eROSITA result** (artifact `pipelines/p3_anomaly_engine/ext3_fm1_erosita_scaler_refit.json`, run on the c15 pod A4000): controlled A-vs-B (identical seeds; only scaler-fit population differs) → top-298 overlap 257/298 (J=0.76), top-1% J=0.64, full-catalog Spearman 0.94. Anchor: production recipe re-run reproduces 247/298 of the published membership → **scaler effect ≤ model-retrain reproducibility floor (~15–17% tail churn either way); rates/rankings robust**. §II.B tex updated.
- **NEOWISE/Gaia**: feature tables are derived products that existed only pod-side (H200 pods EXITED); remain queued with the spec below.
- **What:** Refit the eROSITA / NEOWISE (and lineage-inferred Gaia) feature
  scalers on the training split ONLY, re-score, and report top-298 / top-1%
  Jaccard + Spearman rank correlation against the published selections.
- **Why:** EXT3 FM1 — full-sample scaler fit leaks validation/tail info into
  the normalization constants; the paper now states the no-ranking-effect
  assumption explicitly and cites this queued test (§II preprocessing
  paragraph, `paper3_draft.tex` l.311 area).
- **Needs:** the 930K-source eROSITA 47-feature table + NEOWISE/Gaia feature
  tables (pod-side; scripts at `pipelines/p3_anomaly_engine/recovered_pod_scripts/`).
- **Lands in:** results sentence in the same paragraph + artifact JSON.

### 3. P1B — SN-overlap control chains (standing, EXT2-queued; do NOT fake)
- **What:** Two Cobaya control chains: DESI DR2 + Planck NPIPE + Pantheon+ only;
  DESI DR2 + Planck NPIPE + DES-SN5YR only (same priors/burn-in as iter2
  baseline), to R̂−1 < 10⁻². Report (w0, wa) shifts vs the combined chain.
- **Why:** The product-likelihood overlap caveat (§III caveat (e)) — the one
  substantive P1B residual. Conclusion heading already demoted to
  "Exploratory w0wa cross-check" pending these chains.
- **Needs:** MPI pod (multi-hour MCMC). Already queued on the dedicated pod
  per EXT2; fold the (w0, wa) shifts into §III/Table II when converged.

### 4. P4 — HuggingFace model-repo version tag (EXT2 EF16 carryover)
- **What:** Create/verify a versioned tag on `bamfai/galaxy-chirality-v2`
  (model repo) matching the catalog tag `v2026.04`, and add the tag to the
  Data Availability model link.
- **Why:** Catalog link is tag-pinned; model link is not (Grok EF16, confirmed
  EXT3). External release mutation — not done in the EXT3 source-edit wave.
- **Needs:** HF write token (`.env.local`), 5 min.

### 5. P5 — Fig 3 baked-in title regen (Nm1, blocked on HOUSTON-DECISION NM1)
- **What:** Regenerate Fig 3 so the rendered panel title count matches the
  final title/abstract convention (791,635 chirality-relevant matched vs
  783,820 environment-matched). Houston must first rule on the title text
  (EXT3 NM1 options in `EXT3_P5_TRUTH_AUDIT.md`).
- **Needs:** figure script in `pipelines/p5_desi_chirality/scripts/` (local,
  minutes) — run after the title ruling.
