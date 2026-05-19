# P5 env_finder — Cosmic-Web Environment Sub-Project Scope

**Goal:** Unblock the P5 cosmic-web headline analysis by producing the DESI environmental VAC ourselves, since the "187 DESI-derived attributes" catalog is exhaustively confirmed not in repo (audit subagent 2026-05-15 + reconfirmed tick 114) and the official DESI DR1 LSS VAC is not yet released.

**Acceptance criterion:** Produce a parquet file at `pipelines/p5_desi_chirality/data/desi_env/desi_env_vweb.parquet` matching the schema contract enforced by `pipelines/p5_desi_chirality/scripts/08_analysis_cosmic_web.py`:

| Column | Type | Notes |
|---|---|---|
| `TARGETID` | int64 | DESI DR1 join key — must intersect the matched chirality catalog's TARGETID |
| `env_class` | category{"void","wall","filament","cluster"} | V-Web tidal-tensor classification |
| `env_density` | float64 | Smoothed log-density at the galaxy's position (optional but useful) |
| `vac_provenance` | str | e.g., `"env_finder-vweb-v0.1-{git_sha}-{config_hash}"` |

When this file lands, `08_analysis_cosmic_web.py` will run-not-skip and produce the headline `cw_fraction_by_env` table — closing P5's biggest open scientific question.

---

## Input data (all on disk)

| Asset | Path | Rows / size |
|---|---|---|
| DESI DR1 zall (iron reduction) | `pipelines/p5_desi_chirality/data/desi_zall.parquet` | 28,425,963 rows / 2.0 GB |
| Quality-selected galaxy subsample | (filter: `ZWARN==0` + `SPECTYPE=="GALAXY"` + `0.01<Z<2.0`) | **14,622,283** galaxies — verified tick 114 |
| Matched chirality × DESI catalog | `results/p5_matched_chirality_desi.parquet` | 2,232,212 deduped rows (TARGETID join target) |

The env_finder operates on the full **14.6M galaxy** spectroscopic sample (not just the 2.2M chirality-matched subset) so the resulting environment map is a property of the cosmic-web density field, not of the P4 morphology selection. The matched-catalog TARGETID join happens downstream in `08_analysis_cosmic_web.py`.

---

## Algorithm choice — V-Web (recommended)

### Comparison of candidates

| Approach | Output | Maturity | Cost | Verdict |
|---|---|---|---|---|
| **V-Web / T-Web** (Hahn+ 2007; Hoffman+ 2012) | 4-class label (void/wall/filament/cluster) per cell on 3D grid → interpolate to galaxies | Gold standard in cosmo N-body sims, BOSS, Illustris-TNG | ~10-15 min wall on laptop | ✅ **Recommended** — matches schema exactly |
| **DisPerSE** (Sousbie 2011) | Explicit filament network via Morse-Smale topology | Mature C++ binary, pyDisPerSE wrappers; widely cited | ~1-2 hr wall, more setup | Strong alternative; output is filaments-only (need separate void/cluster classifier) |
| **DBSCAN** (Ester+ 1996) | Cluster labels only (no void/filament distinction) | Standard scikit-learn | ~minutes | ❌ Insufficient — doesn't produce the 4-class schema |
| **Friends-of-Friends** | Halo-level cluster ID (no filament/void) | Classic in cosmo (FoF6D, halo finders) | ~minutes | ❌ Insufficient — same reason as DBSCAN |
| **Tempel+ 2014/2018 FoF + cylinder** | FoF clusters + cylinder filaments + void by complement | Published methodology; rolled-our-own possible | ~half-day work | Workable but bespoke — V-Web is the standard reference |

### Why V-Web

1. **Schema match**: V-Web's 4-class output (3 negative eigenvalues = void / 1 positive = wall / 2 positive = filament / 3 positive = cluster) maps directly to the `env_class` schema enforced by `08_analysis_cosmic_web.py`.
2. **Literature standard**: Used in every modern cosmic-web paper on cosmological simulations and surveys (Hahn+ 2007 originally, Cautun+ 2014 for SDSS, Suárez-Pérez+ 2021 for BOSS, Lim+ 2024 for DESI sims).
3. **Cost**: ~10-15 min wall on a laptop. Zero pod compute.
4. **One tunable**: eigenvalue threshold $\lambda_{\rm th}$ — defensible at literature values (0.1–0.2). Grid resolution and smoothing scale are also tunables but standard choices exist (256³ grid, 2 Mpc/h Gaussian smoothing).
5. **Validation path**: comparable to Tempel+ 2018 SDSS DR12 voids on the overlap footprint, and to published Illustris-TNG V-Web baselines.

### Algorithm in detail

1. **Cosmology + comoving distances**: assume Planck 2018 (H₀=67.66, Ωₘ=0.3111, Ωᵦh²=0.02242, default `astropy.cosmology.Planck18`). Compute comoving distance χ(z) for each galaxy.
2. **3D Cartesian positions**: (X, Y, Z) = χ × (cos·Dec·cos·RA, cos·Dec·sin·RA, sin·Dec). First-pass uses redshift-space coordinates (no FoG correction); RSD-corrected variant in Phase 2.
3. **Density field via CIC**: Cloud-In-Cell interpolation of the 14.6M galaxy positions onto a uniform 256³ comoving-Mpc grid covering the DESI footprint bounding box (~3 Gpc/h cube, dx ≈ 12 Mpc/h).
4. **Gaussian smoothing**: convolve density field with a Gaussian kernel of width R_s = 2 Mpc/h (Hahn+ 2007 default). FFT-based.
5. **Tidal tensor**: T_ij(x) = ∂²Φ/∂xᵢ∂xⱼ where ∇²Φ = δ. Computed via FFT in Fourier space (T_ij in k-space is -kᵢkⱼ/k² · δ_k); equivalent to the Hessian of the Newtonian potential.
6. **Eigendecomposition**: at each grid cell, diagonalize T_ij to get eigenvalues λ₁ ≥ λ₂ ≥ λ₃. Vectorized via `numpy.linalg.eigvalsh` on the 256³ stack.
7. **Classify**: count of eigenvalues > λ_th:
   - 0 → **void**
   - 1 → **wall** (a.k.a. sheet)
   - 2 → **filament**
   - 3 → **cluster** (a.k.a. knot)
8. **Interpolate label to galaxy positions**: nearest-neighbor (or trilinear if env_density is computed too). For env_density use the smoothed log-density at the cell.
9. **Write parquet**: TARGETID + env_class + env_density + vac_provenance, indexed.

### Tunable defaults

| Parameter | Value | Source |
|---|---|---|
| Cosmology | Planck 2018 | `astropy.cosmology.Planck18` |
| Grid resolution | 256³ | Standard literature choice; bumps to 512³ for paper-grade |
| Smoothing scale R_s | 2 Mpc/h | Hahn+ 2007 default |
| Eigenvalue threshold λ_th | 0.0 (geometric) + sensitivity sweep at 0.1, 0.2 | Cautun+ 2014 recommends 0.0 baseline + sensitivity |
| RSD handling | Redshift-space (first pass) | FoG correction in Phase 2 |

---

## Implementation phases

### Phase 1 — MVP env catalog (~1 day work)

**Deliverables:**
- `pipelines/p5_desi_chirality/env_finder/01_compute_vweb.py` — single end-to-end script (input: zall.parquet, output: desi_env_vweb.parquet)
- `pipelines/p5_desi_chirality/env_finder/config.yaml` — cosmology + grid + smoothing + threshold
- `pipelines/p5_desi_chirality/data/desi_env/desi_env_vweb.parquet` — 14.6M-row env catalog matching schema contract
- Provenance sidecar `desi_env_vweb.parquet.provenance.json`
- `pipelines/p5_desi_chirality/env_finder/reports/01_volume_fractions.json` — V₆oid/V_wall/V_filament/V_cluster fractions for sanity check (literature: ~70/15/12/3 %)

**Exit criterion:** Running `python pipelines/p5_desi_chirality/scripts/08_analysis_cosmic_web.py` produces a non-blocked `summary.json` with `cw_fraction_by_env` table on the matched 791,635-spiral subset.

### Phase 2 — Production env catalog (~2-3 days work)

**Deliverables:**
- Hyperparameter sensitivity sweep: grid resolution {256³, 512³} × smoothing scale {2, 4 Mpc/h} × λ_th {0.0, 0.1, 0.2} = 12 catalogs.
- Comparison vs Tempel+ 2018 SDSS DR12 voids on the DESI×SDSS overlap footprint.
- RSD-corrected variant (real-space comoving positions via linear Kaiser correction or FoG-only via z-cluster compression).
- Label-shuffled null test: shuffle env_class labels independently of TARGETID, re-run cw_fraction_by_env, confirm null is consistent with no-signal.
- Uncertainty quantification: jackknife errorbars on cw_fraction_by_env per env_class.

**Exit criterion:** P5 §sec:cosmic_web has the central headline number with sensitivity table showing the result is robust against hyperparameter choices.

### Phase 3 — Paper-ready (~1-2 days work)

**Deliverables:**
- Figures: density-field slice + tidal-tensor slice + env_class sky map + cw_fraction_by_env bar chart with errors.
- Methodology paragraph in P5 LaTeX describing the V-Web procedure (with Hahn+/Hoffman+/Cautun+ citations).
- Full provenance audit per `feedback_houston_method` (QC gate + analysis + interpretation + cross-survey connection + site sync + queue expansion + backup).
- First R-round adversarial review on the populated paper (only after Phase 2 lands).

---

## Compute estimate

| Step | Wall | Where |
|---|---|---|
| Galaxy filter + comoving distance | 30s | local laptop |
| CIC onto 256³ grid | 1 min | local laptop |
| Gaussian smoothing (FFT) | 30s | local laptop |
| Tidal tensor in k-space | 30s | local laptop |
| Eigendecomposition (16.8M cells, vectorized) | 5 min | local laptop |
| NN interpolation to 14.6M galaxies | 30s | local laptop |
| Parquet write + provenance | 10s | local laptop |
| **Phase 1 MVP total wall** | **~10 min** | **local laptop, $0 marginal** |
| Phase 2 sweep (12 catalogs) | ~2 hr wall | local laptop |
| Phase 2 RSD correction | ~30 min | local laptop |
| Tempel+ overlap comparison | ~1 hr (mostly data fetch) | local laptop + network |

Bumping to 512³ grid adds ~6× to grid steps (CIC, FFT, eigvalues): Phase 1 wall becomes ~30 min. Still trivial. **No pod needed at any phase.**

---

## Dependencies

- `numpy`, `scipy.fft`, `scipy.ndimage` — standard
- `astropy.cosmology` — for Planck18 distances
- `pyarrow` — for parquet I/O (already used across P5)
- `pandas` — for the join step
- **No new pip installs** beyond what P5 already uses (verified by `pipelines/p5_desi_chirality/scripts/` already importing these)

Optional Phase 2:
- `pydisperse` — only if running DisPerSE as a cross-check (Phase 2 validation)
- `corrfunc` — for jackknife errorbars on correlation-function-derived densities (overkill for V-Web; deferred)

---

## Validation strategy

1. **Volume-fraction sanity check** (Phase 1): V_void / V_wall / V_filament / V_cluster should be roughly 70 / 15 / 12 / 3 % at λ_th=0 for a typical galaxy density field. Big departures indicate a smoothing-scale or grid-resolution issue.
2. **Visual sanity check** (Phase 1): plot a density-slice + env_class slice through the LSS at z~0.3. Should look like the classic cosmic-web cartoon: cells are voids, planes are walls, fibers are filaments, knots are clusters.
3. **Cross-validation vs Tempel+ 2018** (Phase 2): on the DESI × SDSS DR12 spatial overlap, compare env_class agreement on common-TARGETID galaxies. Expect 60-80% agreement (perfect agreement is not achievable since the two methods use different algorithms; published cross-comparisons show this range).
4. **Label-shuffle null** (Phase 2): shuffle env_class independently of TARGETID, run cw_fraction_by_env, confirm consistent-with-no-signal (already enforced as a Phase 2 deliverable).
5. **RSD sensitivity** (Phase 2): redshift-space vs real-space env labels should agree on >90% of galaxies (small Kaiser shift, ~few Mpc/h displacements within a single smoothing scale).
6. **Internal jackknife** (Phase 2): k=10 spatial jackknife on the DESI footprint, confirm cw_fraction_by_env per env_class has stable mean across folds.

---

## Output schema (parquet)

```python
{
  "TARGETID": int64,        # DESI DR1 join key
  "env_class": category,    # {"void","wall","filament","cluster"}
  "env_density": float64,   # log(1+δ) at galaxy position
  "vac_provenance": str,    # "env_finder-vweb-v0.1-{git_sha}-{config_hash}"
  "env_lambda1": float64,   # tidal-tensor eigenvalues (optional, for downstream Phase 3)
  "env_lambda2": float64,
  "env_lambda3": float64,
}
```

The first 4 columns satisfy the `08_analysis_cosmic_web.py` schema contract. The 3 eigenvalue columns are extra audit-trail (allows downstream users to re-classify with a different λ_th without re-running the pipeline).

---

## Decision points needing Houston input

1. **Go/no-go**: scope this Phase 1 MVP for the next session? Estimated half-day-of-Houston-attention work. The matched-catalog is already 1.3 GB on disk, so the input data is free.
2. **Cosmology**: confirm Planck 2018 (matches P1A/P1B/P3 conventions) vs DESI BAO-derived ΛCDM (slightly different Ωₘ).
3. **Grid resolution default**: 256³ (faster, ~10 min) or 512³ (paper-grade, ~30 min)?
4. **Eigenvalue threshold**: λ_th = 0.0 (geometric, Cautun+ default) or 0.1-0.2 (literature-tuned to match Tempel-style voids)?
5. **Phase 2 priority order**: hyperparameter sweep first vs RSD correction first vs Tempel cross-validation first?

Defaults if Houston says "just pick reasonable" per `feedback_no_questions_full_hard_fix`:
- Cosmology: Planck 2018
- Grid: 256³ (with 512³ in Phase 2 sensitivity)
- λ_th: 0.0 (with sweep at 0.1, 0.2 in Phase 2)
- Phase 2 order: hyperparameter sweep → RSD correction → Tempel cross-validation

---

## Risks

1. **Footprint geometry artifacts**: DESI DR1 has a complex non-convex footprint. Grid cells near the survey edge will have under-counted density and may be mis-classified. **Mitigation**: mask cells with effective volume < 50% inside footprint; exclude those galaxies from headline analysis.
2. **Redshift completeness**: DESI is z-magnitude-limited (different limits for BGS / LRG / ELG / QSO programs). Density field is biased toward bright populations at low z. **Mitigation**: optionally compute density field on BGS-only subsample (more uniform completeness, z<0.6) and report cw_fraction_by_env separately for BGS vs full sample.
3. **Bias of env_class against P4 spiral classification**: P4's chirality model was trained on DESI Legacy DR8 imaging, which has its own selection. A density-environment bias against spiral fraction would NOT mean a real chirality-environment signal. **Mitigation**: report `spiral_fraction_by_env` first, regress out, then quote residual cw_fraction-vs-environment.
4. **Smoothing-scale degeneracy**: at R_s=2 Mpc/h some clusters get classified as "wall" because the smoothing washes out the central density. **Mitigation**: Phase 2 sensitivity sweep on R_s ∈ {2, 4} Mpc/h.

---

## Timeline (if Houston says "go")

| Phase | Wall | Outcome |
|---|---|---|
| Phase 1 MVP | ~half-day | Unblocks `08_analysis_cosmic_web.py` → P5 headline analysis runs |
| Phase 2 production | ~2-3 days | Sensitivity-table + RSD + Tempel cross-validation in paper |
| Phase 3 paper-ready | ~1-2 days | First PDF compile + first R-round → P5 readiness 15 → 60+ |

Total: ~1 week of focused attention to take P5 from bootstrap (15%) to paper-draft-with-R-round (~70%). Combined with the matched-catalog work already done, P5 would converge fast once env_finder lands.

---

## Status: SCOPED, awaiting Houston go/no-go on Phase 1 MVP
