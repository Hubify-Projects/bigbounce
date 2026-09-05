# Row 16(i) — FULL-PARENT chirality dipole (2026-09-04)

## Data path: REUSE, not re-inference

The production equivariant Z2-TTA classifier had **already been run on all
8,474,531** DESI Legacy DR8 galaxies — `class_eq` labels for the full parent
ship in the committed, immutable
`pipelines/p2_chirality/apjs_release_v1.0.244/p4_catalog_primary_safe_v1.0.244.parquet`
(SHA-256 `139b761f...28dfd3`, verified byte-identical this run). No pod, no
re-inference: this closes the row as a **local-CPU dipole-fit-on-parent** job
per the task's own reuse-first framing.

## Selection

Full parent, all `class_eq in {CW, CCW}` — **no** `primary_hc` /
`raw_flip_qc_unsafe` restriction (that restriction is what produces P4''s
887,472-galaxy strict-primary subset). N_spiral = 3,201,160 of 8,474,531
total rows; N in the NSIDE=64, `N_spiral(pixel)>=10` support = **3,200,420**
across 24,087 pixels.

## Estimator (imported verbatim, not re-derived)

`build_projector()` imported directly from the committed
`pipelines/p2_chirality/generate_p4_primary_label_shuffle_strict_v1_0_257.py`
— unweighted `healpy.fit_dipole` on per-pixel `(2*n_CW-total)/total`, same
NSIDE=64 / support>=10 convention P4' cites. Null: a fresh 10,000-draw
fixed-occupancy multivariate-hypergeometric label randomization (seed
20260904, distinct from P4''s 20260715). A_95: the same 14-point
amplitude-grid, 2000-axis observed-label injection-recovery sweep
convention as `a95_observed_label_upper_limit_v1_0_265.py` (seed 20260905).

## Result

| Quantity | 887,472 strict-primary (P4') | 8,474,531 full parent (this run) |
|---|---|---|
| N in support | 887,472 | **3,200,420** |
| Observed amplitude $A_{\rm obs}$ | 0.4665% | **0.5660%** |
| Axis (RA, Dec) | 195.48°, −57.16° | **278.63°, +25.32°** |
| z (fixed-occ. null) | +0.635 | **+4.440** |
| One-sided rank p | 0.238 | **0.0002** |
| $A_{95}^{\rm obs}$ (injection-recovery) | 0.98% | **0.51%** |

The full-parent test is **formally significant** (z=+4.44, p=0.0002) and
$A_{\rm obs}=0.566\%$ exceeds its own injection-calibrated $A_{95}^{\rm
obs}=0.51\%$ sensitivity floor — a materially different outcome from P4''s
null-consistent 887k-subset result, and at a **different sky axis**.

## Verdict — evidential strength

This is **not** treated as a confirmed physical/cosmological detection.
P4''s 887,472-row `primary_hc && !raw_flip_qc_unsafe` selection exists
specifically to exclude rows flagged by post-review raw-flip QC and
low-confidence classifications — exactly the population this full-parent run
restores. The catalog's own documented systematics (per-imaging-leg
BASS+MzLS/DECaLS/DES boundary effects, monopole+mask leakage, the known
0.26%/9.5σ CW-label monopole bias) are known, catalog-wide effects that a
footprint-correlated (non-isotropic) systematic can imitate as a spurious
dipole under a fixed-occupancy null — which is the precise failure mode the
strict selection was built to guard against. The differing axis (295° arc
separation) between the two subsets is consistent with a QC/footprint origin
rather than a shared physical signal. **Verdict: OPEN, non-null, likely
systematic-driven** — this is a genuinely new positive finding that narrows
the search, not a null result to shelve. The row16(ii) N=20,000 image-level
injection-calibrated postprocess residual bias (−0.26% full-amplitude,
`scale20k_injection_results.json`) is reported for context only and was
**not** subtracted (no tuning).

## Null tests re-run on the parent

- Fixed-occupancy multivariate-hypergeometric label-shuffle null (P4''s
  primary null): re-run fresh on the full-parent support, 10,000 draws
  (above).
- Observed-label injection-recovery detection-power sweep (source of
  $A_{95}^{\rm obs}$): re-run fresh on the full-parent support, 2000
  axes/amplitude x 14 amplitudes (above).
- **Not** re-run on the parent this pass (flagged, not silently skipped):
  the MASTER pseudo-$C_\ell$ deconvolution, per-imaging-leg systematics
  table, and monopole+mask-leakage simulation that P4/P4' also carry —
  these are the natural next diagnostic given the axis mismatch above.

## Next research direction (not a stopping point)

The full parent is 3.6x the strict-primary N and shows a stronger,
axis-shifted signal — this narrows, not closes, the search. Next: (1) rerun
the monopole+mask-leakage null and per-imaging-leg systematics table
specifically on the full-parent selection to test whether the 278.6°/+25.3°
axis tracks a footprint boundary; (2) a graded QC sweep (interpolating
between the 887k strict set and the 3.2M full parent by relaxing
`raw_flip_qc_unsafe` first, then `primary_hc`) to localize which quality cut
drives the shift.

## Artifacts

- `run_full_parent_dipole.py`, `full_parent_estimator_lib.py` — estimator.
- `row16i_full_parent_dipole.json` — full numeric result.
- `fig_row16i_full_parent_injection_recovery.png` — detection-power curve.
- `reproducibility/manifests/experiments/p4p-row16i-full-parent-dipole.json`
  — manifest, registered in `reproducibility/manifests/programs/galaxy-chirality.json`.
