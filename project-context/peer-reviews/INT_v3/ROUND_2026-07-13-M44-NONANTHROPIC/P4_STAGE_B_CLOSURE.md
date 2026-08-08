# P4 v1.0.241 Stage-B closure report

Date: 2026-07-14  
Scope: P4-local only; no SSOT, Convex, site, mirror, or root-version cascade.

## Verdict

Stage A is a full-catalog original/mirror transfer and equivariance sweep, not a physical injection. Stage B is now a completed **paired-image-to-field surrogate**, but not an unconditional physical calibration. DP4-15 and DP4-17 remain open.

## Integrity seam

- Catalog and 192 Stage-A shards: 8,474,531 rows each; full sequence SHA-256 matches.
- Released production spirals: 3,201,160.
- Stage-A/released-production hard-label disagreements: 5,464 overall; 4,369 within production spirals.
- Pair-concordant production-spiral pool used: 3,196,791 (99.864%). Forced pairing of the 4,369 discordant rows is unavailable/not defensible.
- Canonical released HC membership: 949,584. Stage-A fresh class/probability path: 949,650 (+66; noncanonical; membership symmetric difference 3,376).
- Crucially, Stage-A/released-production hard-label disagreement within canonical HC: **0**. All 949,584 HC rows have valid pair semantics.

## Stage-B design

- Amplitudes: 0.5%, 0.75%, 1.0%, 1.5%, 2.0%.
- Axes: 20 deterministic Fibonacci-sphere directions.
- Production hard label/confidence, NS triage, `p_eq` cuts, NSIDE=64, `N_spiral >= 10`, uniform-pixel `healpy.fit_dipole`.
- Reference null: 500 fixed-count, per-pixel `p=0.5` binomial draws per stratum. It is not a label permutation or joint spatial nuisance likelihood.
- Strata: confidence, imaging leg, depth quartile, PSF quartile, `b/a`, and `FRACDEV`.

## Recovery results

| Stratum | N | A50 grid | A95 grid | Per-axis first-3sigma p16/median/p84 | Axes without crossing |
|---|---:|---:|---:|---:|---:|
| Full pair-concordant | 3,196,791 | 0.50% | 0.75% | 0.50 / 0.50 / 0.75% | 0 |
| Canonical HC `p_eq>0.6` | 949,584 | 0.75% | 1.50% | 0.75 / 0.75 / 0.99% | 0 |
| `p_eq>0.7` | 756,024 | 0.75% | 1.50% | 0.75 / 0.75 / 1.00% | 0 |
| `p_eq>0.8` | 624,660 | 0.75% | 1.50% | 0.75 / 0.75 / 1.00% | 0 |
| `p_eq>0.9` | 496,531 | 1.50% | 1.50% | 1.00 / 1.25 / 1.50% | 0 |
| DECaLS | 527,852 | 1.50% | 2.00% | 1.50 / 1.50 / 1.98% | 0 |
| Face-on `b/a>=0.5` | 561,322 | 1.00% | 1.50% | 0.75 / 1.00 / 1.00% | 0 |
| `FRACDEV<0.5` | 592,344 | 0.75% | 2.00% | 0.75 / 0.75 / 1.00% | 0 |

Uncrossed strata are reported, not extrapolated: BASS+MzLS and DES do not reach A50/A95 on the tested grid; edge-on and multiple depth/PSF quartiles also have many axes without a 3-sigma crossing; `FRACDEV>=0.5` and all PSF/depth strata fail to reach A95 by 2% in at least one case. The four PSF-quartile counts sum to 949,580 because four canonical-HC rows lack a finite mean-PSF value; those rows are unavailable for PSF stratification and are not silently reassigned. The JSON contains every recovered amplitude, signed projection, angular error, p16/p50/p84 range, selected count, and NS-triage count.

For canonical HC, median recovered/injected amplitude ratios across 0.5/0.75/1.0/1.5/2.0% are 1.091/1.282/1.038/1.076/0.969. The non-monotone 80% recovery at both 0.75% and 1.0%, followed by 100% at 1.5%, is retained honestly; the grid-level HC A95 is therefore 1.5%.

## Cross-estimator residual injection

The former comparison was wrong: the full 0.695% residual is above the like-for-like full-sample A95=0.63%, not below the HC floor. A deterministic pure-l=1 map injection into the HC real-space field gives:

- baseline amplitude 0.4597%;
- full observed l=1 template: 0.6710% (+46.0%);
- scalar 47%-remainder template: 0.5533% (+20.4%);
- direct vector-subtraction remainder: 0.5694% (+23.9%).

The scalar remainder is 47.0%, while direct vector subtraction leaves 62.3% because the observed and fitted systematic vectors are not parallel. This stress test does not establish a detection, physical origin, estimator independence, or joint covariance closure.

## Corrected arithmetic/method text

- Physical 1.7% signal after `g=0.398`: `0.017*0.398=0.006766`; relative to fit 0.00455 and sigma 0.00163: `z=1.36`, not -7.6. Physical A95 corresponding to observed 1.0-1.5% is 2.51-3.77%.
- The 648-direction 10-degree local scan and authoritative 768-direction NSIDE=8 max-stat Monte Carlo are distinct. The latter is not an exact correction of the former.
- Bonferroni family-wise control does not require independent tests. The Gaussian heuristic is non-authoritative here because the statistic is positive-definite/non-Gaussian and the scan grids differ.

## Open limitations

- No validated continuous image-plane morphology transform.
- No independent full-catalog per-object physical chirality truth or NS/NS physical-spiral truth.
- No per-pixel conditional physical confusion matrix jointly in depth, PSF, morphology, confidence, and imaging leg (DP4-15).
- No joint real-space x harmonic covariance/nuisance likelihood (DP4-17).

Primary artifacts:

- `pipelines/p2_chirality/outputs/canonical_provenance/stage_b_hybrid_image_field_recovery.json`
- `pipelines/p2_chirality/outputs/canonical_provenance/residual_template_cross_estimator_injection.json`
- `pipelines/p2_chirality/scripts/stage_b_hybrid_image_field_recovery.py`
- `pipelines/p2_chirality/scripts/residual_template_cross_estimator_injection.py`

## Verification

- Final Tectonic passes 5 and 6 completed successfully; the compiled PDF is 35 letter-size pages.
- Log gate: zero overfull boxes, undefined references/citations, LaTeX errors, emergency stops, or fatal errors. The remaining Latin Modern bold-small-caps font substitution is non-structural.
- RevTeX emits deferred-float warnings for seven float groups during `\clearpage`; this was treated as a visual gate, not waived from the log alone. All 35 rendered pages were inspected. Every affected figure/table is present, readable, non-overlapping, and not stranded, including the estimator callout (p. 6), Stage A/B text (pp. 19--20), GZ1 tables (pp. 26--27), and WLS/cross-spectrum material (pp. 29--30).
- Page 1 visibly carries the July 14, 2026 date and the corrected abstract claims; page 33 was re-rendered after converting the canonical-provenance directory reference to a breakable artifact link.
- All five manuscript `\url{}` targets returned HTTP 200 on 2026-07-14.
- Both new Python scripts pass `py_compile`; both new JSON artifacts pass `jq empty`; the scoped diff passes `git diff --check`.
