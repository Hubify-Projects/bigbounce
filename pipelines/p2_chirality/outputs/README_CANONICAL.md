# Paper 4 canonical artifact map

This file maps each headline number reported in
`pipelines/p2_chirality/chirality_catalog_paper.tex` to the
canonical on-disk artifact that supports it. Closes external-review
finding CG-G-6 (raw vs canonical output disambiguation).

| Paper claim | Section | Canonical artifact (commit current to v1.0.69) |
|---|---|---|
| Total catalog: 8,474,531 galaxies | Abstract, §IV.A | `outputs/canonical_provenance/global_cw_fraction.json` (n_total field) |
| Equivariant spirals: 3,201,160 (CW 1,592,107 + CCW 1,609,053) | Abstract, §IV.A | `outputs/canonical_provenance/global_cw_fraction.json` + `outputs/canonical_provenance/spiral_count_verification.json` |
| CW fraction 0.4974 ± 0.000279, 9.5σ deficit | §IV.B | `outputs/canonical_provenance/global_cw_fraction.json` |
| Real-space dipole, σ = 0.43, p = 0.30 (Catalog C, post-TTA) | Abstract, §IV.C | `outputs/canonical_provenance/catalog_c_post_tta_dipole_summary.json` (v1.0.67+) |
| MASTER-deconvolved C_1 on subsample mask: −0.122σ | Abstract, §IV.C, Table IV | `master_results/master_power_spectrum.json` |
| Canonical-N direct-MC ℓ=1: +1.85σ | §VII, Table VII | `outputs/canonical_provenance/canonical_n_master_l1_direct.json` + `outputs/canonical_provenance/canonical_n_master_l1_direct_null_distribution.npy` |
| Hemisphere max-statistic: 3.05σ local, p_LEE ≤ 10⁻⁴ | Abstract, §IV.D | `r42_results/wave_12_hemisphere_GPU_v4.json` |
| Empirical injection-recovery floor: >0.5% | §VI.C | `outputs/canonical_provenance/wave_14_nn_injection_recovery.json` |
| Fisher Poisson floor: 0.29% (full-amp, 3σ) | §VI.C | `outputs/canonical_provenance/fisher_sensitivity_floor.json` |
| MC seed manifest (all randomized analyses) | §IV.C / §IV.D / §VI.B | `outputs/canonical_provenance/mc_seed_manifest.json` |
| Validation accuracy: 93.7% internal three-class | §II.B / Table I | `r42_results/B20_B21_results.json` |
| Independent GZ1 CW/CCW agreement: 69.91%, κ = 0.40 | Abstract, §II.B, §III.F | `r42_results/B20_B21_results.json` |
| Per-imaging-leg systematics (BASS+MzLS / DECaLS / DES) | §IV.E (new in v1.0.69), Table | `outputs/canonical_provenance/per_imaging_leg_systematics.json` (v1.0.69) |
| Face-on (HC-spiral) robustness rerun | §VI.D | `outputs/canonical_provenance/face_on_robustness_results.json` (v1.0.69) |
| Monopole+mask leakage null simulation | §VI.B (new in v1.0.69) | `outputs/canonical_provenance/monopole_mask_null_results.json` + `*.npy` distributions (v1.0.69) |
| PSF-ellipticity correlation results | §VI.C, Fig 13 | `r42_results/wave_14_jj_psf_xcorr_results.json` |

## Non-canonical (raw / historical) files that should NOT be cited as headline:

| File | Why it is NOT canonical |
|---|---|
| `outputs/dipole/summary.json` | PRE-TTA (Catalog A) 2.31σ pipeline run, retained for historical comparison only |
| `outputs/chirality_summary.json` | Raw Catalog A counts; status "100% COMPLETE" refers to pipeline-run completeness, not to canonical analysis |
| `outputs/canonical_provenance/canonical_n_master_l1_projection.json` | v1.0.55-era analytic projection, superseded by canonical_n_master_l1_direct.json |
| All `r42_results/wave_14_oo_*.json` | Wave-14 OO sweep diagnostics; canonical bin-by-bin flatness summary lives in `wave_14_oo_bin_flatness.json` |

## Reproduction:

See `reproduce_paper4.sh` for a one-shot wrapper that downloads the
catalog and recomputes the headline numbers. Each step prints
the expected paper value and the computed value side-by-side.

## Schema notes for HuggingFace dataset users:

The HF dataset (`bamfai/galaxy-chirality-catalog`) ships
`catalog_production.parquet` with the following load-bearing columns:

| Column | Type | Meaning |
|---|---|---|
| `dr8_id` | string | DESI Legacy DR8 brick + objid (cross-match key) |
| `ra`, `dec` | float | J2000 in degrees |
| `class_eq` | enum | `CW`, `CCW`, or `NOT_SPIRAL` (post-TTA, **canonical**) |
| `class_raw_x` | enum | Catalog A raw label (pre-TTA; for diagnostic comparison) |
| `p_cw_eq`, `p_ccw_eq`, `p_ns_eq` | float | Post-TTA class probabilities |
| `confidence_eq` | float | max class probability (post-TTA) |
| `p_cw_raw_x`, `p_ccw_raw_x`, `p_ns_raw_x` | float | Pre-TTA probabilities |
| `image_url` | string | DESI Legacy Survey cutout URL (uses ls-dr9 viewer because that endpoint serves DR8 imagery via the unified viewer; underlying photometry is DR8) |

Users running their own analyses should use `class_eq` (canonical) and
the `_eq` probability columns; the `_raw_x` / `_raw_y` columns are for
robustness checks against the pre-TTA pipeline only.

## Catalog usage limitations

The catalog labels carry a measured spatially-uniform CW-bias residual
of 0.26% (9.5σ) attributed to GZ1 human-handedness training bias
propagating through CE-ResNet pseudo-labels. The catalog labels are
**not** ground-truth chirality and should not be used for precision
parity tests below the empirical >0.5% amplitude floor without local
re-normalization of the per-region monopole. The independent GZ1
CW/CCW agreement on the 234,282-galaxy disjoint cross-match is 69.91%
(Cohen's κ = 0.40); per-galaxy labels are probabilistic classifier
outputs, not deterministic visual classifications.
