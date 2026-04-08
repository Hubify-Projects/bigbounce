# Current Status: BigBounce Research Program

**Last updated: 2026-04-08**

## Papers

| Paper | Version | Pages | Status | Notes |
|-------|---------|-------|--------|-------|
| Paper 1 (Spin-Torsion Cosmology) | v2.2.0 | 24 | Ready for submission | 14 ECH barriers, ALP birefringence, bounce model discrimination, 63+ refs |
| Paper 2 (f_NL Forecast) | v1.3.0 | 12 | Ready for submission | f_NL = -35/8, SPHEREx testable, Fisher forecast |
| Paper 3 (Anomaly Catalog) | v1.0 | ~35 | ~98% ready (ApJS) | 14 figures + Pipeline 1 Step 3 complete (12,902 high-z QSOs from anomalies) |
| Paper 4 (Chirality Catalog) | v1.0 | ~20 | ~85% ready (MNRAS) | 11 figures compiled, 8.47M galaxies. Needs confusion matrix, training curves |

### Compiled PDFs (with figures)
- Paper 1: `arxiv/main.pdf` (484 KB)
- Paper 2: `public/focused_paper_bounce_fnl_forecast.pdf` (544 KB, 5 figures)
- Paper 3: `public/papers/anomaly_catalog_paper.pdf` (6.0 MB, 14 figures)
- Paper 4: `public/papers/chirality_catalog_paper.pdf` (18 MB, 11 figures)
- All compiled locally with `tectonic` (no pod needed)

## Multi-Survey Anomaly Sweep — 33.5M sources, 328K+ anomalies

| Survey | Sources | Anomalies | QC |
|--------|---------|-----------|-----|
| DESI DR1 | 22.5M | 195,829 (0.87%) | PASS |
| SDSS DR18 | 2.3M | 77,905 (3.4%) | PASS |
| LAMOST DR10 | 11.4M | 44,075 (0.39%) | PASS |
| eROSITA DR1 | 930K | 9,303 (1%) | PASS |
| Planck CMB | 20K | 193 | FIXED (galactic mask) |
| ACT DR6 | 20K | 200 | FIXED (100 epochs) |
| NEOWISE | 43.5K | 444 | FIXED (ecliptic mask) |
| Gaia DR3 | 500K | 5,000 | FIXED (10x expansion) |
| BOSS/eBOSS | — | — | COMPLETE |
| DES DR2 | — | — | COMPLETE |
| VLASS Radio | — | — | COMPLETE (77 USS candidates) |
| LOFAR LoTSS | — | — | COMPLETE |
| JWST MAST | — | 500 | COMPLETE |
| Chandra CSC | — | 800 | COMPLETE |
| XMM 4XMM | — | 1,000 | COMPLETE |

## NEW: Pipeline 1 (f_NL Tracer Purification) — Step 3 COMPLETE

| Step | Task | Status | Result |
|------|------|--------|--------|
| 1 | Anomaly detection (BigAE) | COMPLETE | 195,829 anomalies |
| 2 | Cross-match Legacy DR10 photometry | FAILED (KeyError 'z') | needs script fix |
| 3 | **High-z QSO classifier** | **COMPLETE** | **13,367 high-z QSO candidates (8.1%), F1=0.97, AUC=0.9997, median z=3.25** |
| 4 | Validate bias enhancement (direct Landy-Szalay) | PARTIAL (bias_evolution.py done) | mean ratio 3.27x, z-dependent |
| 5 | Re-measure σ(f_NL) with calibrated α | PENDING | |
| 6 | Write up for Paper 3 | PENDING | |

**12,902 high-confidence QSOs (P>0.7)** from anomaly catalog with median z=3.25, median anomaly score=11.5, median W1-W2=1.01 — these are the key tracer population for Paper 3's f_NL multi-tracer measurement.

## H200 Queue v2 — Phase Status

| Phase | Exp | Status | Key Results |
|-------|-----|--------|-------------|
| 1: Re-run broken | 6 | **COMPLETE** | Planck masked, ACT trained, NEOWISE masked, Gaia 10x |
| 2: Validation | 6 | **COMPLETE** | SIMBAD cross-match (479 known), injection recovery, spatial clustering |
| 3: Cross-survey | 6 | **COMPLETE** | SDSS×LAMOST (30), multi-messenger (40 joint), Planck×ACT (independent) |
| 4: Science | 5 | **COMPLETE** | f_NL bias 2.28×, threshold optimal=5, NANOGrav γ=3.32±0.37, PTA BF=27.6 |
| 5: New surveys | 4 | **COMPLETE** | BOSS, DES, VLASS, LOFAR |
| 6: X-ray/space | 3 | **COMPLETE** | JWST 500, Chandra 800, XMM 1,000 |
| 7: Speculations | 3 | **COMPLETE** | Dyson sphere, GW echoes, FRB |
| 8: Advanced ML | 3 | **COMPLETE** | Multi-modal joint AUC +0.22, Transformer, SDSS native |
| Novel batch | 5 | **COMPLETE** | 2nd-level autoencoder, taxonomy deep (15 clusters, ARI=0.93), emission line finder, anomaly cross-correlation, multi-messenger stack |
| Pipeline 1 | 3 partial | **STEP 3 COMPLETE** | 12,902 high-z QSO candidates |
| Bias evolution | 1 | **COMPLETE** | 6 z-bins, mean bias ratio 3.27x |
| 9: Full-scale | 2 | PENDING | NEOWISE 170B rows, Gaia 1.8B epoch |
| 10: Papers | 2 | PENDING | Final compilation |

## Compute

**Pod status:** STOPPED 2026-04-08 after full backup. `sleepy_blush_crane` (`o76k3jfzbfh25e`) had RunPod infrastructure error + crashed pipeline (numpy.trapz removed in numpy 2.x).

**Backup location:** `pipelines/h200_results/pod_backup_20260408_full/` — 3.4 GB, 134 experiment dirs, 296 JSON, 104 CSV, 28 .pt models, 143 logs. Pushed to GitHub.

**Local LaTeX:** `tectonic` installed — papers compile locally.

**Next pod actions before re-running:** Fix `np.trapz` → `np.trapezoid` in `redshift_tomography.py`. Fix `KeyError: 'z'` in `p1_legacy_crossmatch.py`. Fix divide-by-zero in `fisher_forecast_spherex.py`.

## MCMC & Cosmology Results

- 475,000+ posterior samples across 5 dataset combinations
- **Quintom-B REVISED:** 39.6% (was 98.6%), 1.09σ from ΛCDM (was 2.3σ) on mock DR2 data. The earlier 98.6% was DR1 mock; new analysis with mock DR2 weakens the signal. **Need real DR2 BAO when released.**
- NANOGrav: γ = 3.0 (bounce) vs 3.2 ± 0.6 (observed), 0.33σ
- Combined PTA: γ = 3.32 ± 0.37, Bayes factor = 27.6
- ΔNeff ≈ 0; H0 = 67.68 (standard ΛCDM)

## Key Scientific Results

- 14 structural barriers (ECH bounce→DE closed)
- ALP birefringence β = 0.27° (matches 3.6σ signal)
- f_NL = -35/8 = -4.375 (parameter-free, SPHEREx ~5σ by 2028)
- Template mismatch r ≈ 0.85-0.90 (first quantification)
- Pipeline 1: **12,902 high-z QSO candidates** (median z=3.25) classified from anomalies with F1=0.97
- Anomaly bias enhancement: 3.27× standard (z-dependent: 6.4× at low-z, ~1× at high-z)
- Multi-tracer σ(f_NL) improvement: 9.5% (low-z bins up to 92%, high-z 2-7%)
- Spectral taxonomy deep: 15 clusters, silhouette=0.82, ARI=0.93, NMI=0.95
- 8.47M galaxy chirality: parity conserved at 0.4σ, Shamir refuted
- 1,127 uncataloged objects in 10 astrophysical families

## Bugs to Fix Before Next Pod Run

| Script | Bug | Fix |
|--------|-----|-----|
| `redshift_tomography.py` | numpy 2.x removed `np.trapz` | use `np.trapezoid` |
| `p1_legacy_crossmatch.py` | `KeyError: 'z'` in DESI dataframe | check column name |
| `fisher_forecast_spherex.py` | divide-by-zero, NaN output | guard with epsilon |
| `planck_lensing_xcorr.py` | bias=977 (synthetic data, no real data) | needs real Planck lensing maps |

## Next Steps (Priority)

1. **Fix script bugs** (above) before next pod run
2. **Pipeline 1 Step 4-6**: validate bias enhancement, recompute σ(f_NL), write up for Paper 3
3. **Paper 4: confusion matrix + training curves** (~2h on pod)
4. **NaMaster birefringence** — independent EB for Paper 1
5. **Phase 9: full-scale scans** when ready
6. **Submit Paper 2** (ready now), then Paper 1

## Backups

| Location | Last Updated |
|----------|-------------|
| Local disk | 2026-04-08 |
| GitHub main | 2026-04-08 |
| Backblaze B2 | 2026-04-03 |
| HuggingFace (3 datasets) | 2026-04-03 |
| Convex (8.47M chirality) | 2026-03-28 |
