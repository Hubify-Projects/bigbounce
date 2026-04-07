# Current Status: BigBounce Research Program

**Last updated: 2026-04-07**

## Papers

| Paper | Version | Pages | Status | Notes |
|-------|---------|-------|--------|-------|
| Paper 1 (Spin-Torsion Cosmology) | v2.2.0 | 24 | Ready for submission | 14 ECH barriers, ALP birefringence, bounce model discrimination, 63+ refs |
| Paper 2 (f_NL Forecast) | v1.3.0 | 12 | Ready for submission | f_NL = -35/8, SPHEREx testable, Fisher forecast |
| Paper 3 (Anomaly Catalog) | v1.0 | ~35 | ~95% ready (ApJS) | 14 figures compiled, 22.5M spectra, 1,127 uncataloged, 9.5% σ(f_NL) improvement |
| Paper 4 (Chirality Catalog) | v1.0 | ~20 | ~85% ready (MNRAS) | 11 figures compiled, 8.47M galaxies, parity conserved. Needs confusion matrix |

### Compiled PDFs (all with figures)
- Paper 1: `arxiv/main.pdf` (484 KB)
- Paper 2: `public/focused_paper_bounce_fnl_forecast.pdf` (544 KB, 5 figures)
- Paper 3: `public/papers/anomaly_catalog_paper.pdf` (6.0 MB, 14 figures)
- Paper 4: `public/papers/chirality_catalog_paper.pdf` (18 MB, 11 figures)
- LaTeX compiled locally with `tectonic` (no pod needed)

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
| BOSS/eBOSS | — | — | COMPLETE (Phase 5) |
| DES DR2 | — | — | COMPLETE (Phase 5) |
| VLASS Radio | — | — | COMPLETE (77 USS candidates) |
| LOFAR LoTSS | — | — | COMPLETE (Phase 5) |
| JWST MAST | — | 500 | COMPLETE (Phase 6) |
| Chandra CSC | — | 800 | COMPLETE (Phase 6) |
| XMM 4XMM | — | 1,000 | COMPLETE (Phase 6) |

## H200 Queue v2 — Full Phase Status

| Phase | Exp | Status | Key Results |
|-------|-----|--------|-------------|
| 1: Re-run broken | 6 | **COMPLETE** | Planck masked, ACT trained, NEOWISE masked, Gaia 10x |
| 2: Validation | 6 | **COMPLETE** | SIMBAD cross-match (479 known), injection recovery, spatial clustering |
| 3: Cross-survey | 6 | **COMPLETE** | SDSS×LAMOST (30), multi-messenger (40 joint), Planck×ACT (independent) |
| 4: Science | 5 | **COMPLETE** | f_NL bias 2.28×, threshold optimal=5, NANOGrav γ=3.32±0.37, PTA BF=27.6 |
| 5: New surveys | 4 | **COMPLETE** | BOSS, DES, VLASS, LOFAR |
| 6: X-ray/space | 3 | **COMPLETE** | JWST, Chandra, XMM |
| 7: Speculations | 3 | **COMPLETE** | Dyson sphere, GW echoes, FRB |
| 8: Advanced ML | 3 | **COMPLETE** | Transformer, SDSS native, multi-modal |
| Novel batch | 4 | **COMPLETE** | 2nd-level anomalies, taxonomy, Planck lensing, multi-messenger stack |
| 9: Full-scale | 2 | PENDING | NEOWISE 170B rows, Gaia 1.8B epoch (~$517) |
| 10: Papers | 2 | PENDING | Final compilation (~$22) |

### Experiment Scripts
All 33 scripts in `h200_scripts/experiments/` — ready to deploy on any new pod.

## Compute

**Current pod:** CRITICAL ERROR (RunPod infrastructure failure on `sleepy_blush_crane`)
**Action needed:** Create new H200 pod for Phases 9-10 + Pipeline 1
**Local LaTeX:** `tectonic` installed — papers compile locally

## MCMC & Cosmology Results

- 475,000+ posterior samples across 5 dataset combinations
- w0-wa quintom: P(quintom-B) = 98.6%, 2.3σ
- NANOGrav: γ = 3.0 (bounce) vs 3.2 ± 0.6 (observed), 0.33σ
- Combined PTA: γ = 3.32 ± 0.37, Bayes factor = 27.6
- ΔNeff ≈ 0; H0 = 67.68 (standard ΛCDM)

## Key Scientific Results

- 14 structural barriers (ECH bounce→DE closed)
- ALP birefringence β = 0.27° (matches 3.6σ signal)
- f_NL = -35/8 = -4.375 (parameter-free, SPHEREx ~5σ by 2028)
- Template mismatch r ≈ 0.85-0.90 (first quantification)
- 9.5% σ(f_NL) improvement via latent-space multi-tracer
- 8.47M galaxy chirality: parity conserved at 0.4σ, Shamir refuted
- 1,127 uncataloged objects in 10 astrophysical families

## Next Steps (Priority)

1. Create new H200 pod
2. Pipeline 1: f_NL tracer purification (Steps 2-6) — novel work for Paper 3
3. Paper 4: confusion matrix + training curves (~2h)
4. NaMaster birefringence — independent EB for Paper 1
5. Phase 9: full-scale scans
6. Submit Paper 2 (ready now), then Paper 1

## Backups

| Location | Last Updated |
|----------|-------------|
| Local disk | 2026-04-07 |
| GitHub main | 2026-04-07 |
| Backblaze B2 | 2026-04-03 |
| HuggingFace (3 datasets) | 2026-04-03 |
| Convex (8.47M chirality) | 2026-03-28 |
