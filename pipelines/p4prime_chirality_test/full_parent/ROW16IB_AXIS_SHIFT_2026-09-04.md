# Row 16(i-b) — is the full-parent chirality dipole a QC/footprint systematic?

**Status: PRE-REGISTERED (this header committed BEFORE any fit was run).**
Date 2026-09-04. Lane: local CPU. Never tune; every fit below is reported
whatever it returns.

## Question

Row 16(i) (`ROW16I_FULL_PARENT_2026-09-04.md`) found, on the FULL parent
selection (`class_eq ∈ {CW,CCW}`, no QC restriction; N_support = 3,200,420):
A_obs = 0.566%, z = +4.44 at (RA 278.63°, Dec +25.32°) — while P4′'s strict
887,472-row `primary_hc && !raw_flip_qc_unsafe` subset is null-consistent
(A_obs = 0.4665%, z = +0.635) at a nearly antipodal axis (195.48°, −57.16°).
Is the parent signal a footprint/QC systematic, or does it survive?

## Pre-registered plan

**Estimator — frozen, reused verbatim.** `full_parent_estimator_lib.py`
(which imports `build_projector` from the committed
`p2_chirality/generate_p4_primary_label_shuffle_strict_v1_0_257.py`):
NSIDE = 64, pixel support ≥ 10 spirals, unweighted `healpy.fit_dipole` on
per-pixel `(2·n_CW − total)/total`; monopole projected out. No re-derivation.
Catalog: immutable `p2_chirality/apjs_release_v1.0.244/
p4_catalog_primary_safe_v1.0.244.parquet` (SHA-256 re-verified each run).

**A. Graded QC sweep** (four selections, same estimator):
- `C0_full_parent` — no QC cut (row-16(i) reference).
- `C1_relax_primary_hc` — require `!raw_flip_qc_unsafe` only.
- `C2_relax_rawflip` — require `primary_hc` only.
- `C3_strict` — `primary_hc && !raw_flip_qc_unsafe` (P4′'s 887,472).

**B. Per-imaging-leg / footprint table.** Legs by the P4′ canonical
declination boundaries `DEC_LEG_BOUNDARIES = (-20.0, 32.0)` from the
committed `p2_chirality/c12b_wls_conditioning.py`: `BASS+MzLS` (Dec > 32),
`DECaLS` (−20 < Dec ≤ 32), `DES` (Dec ≤ −20). For each leg: in-leg fit and
leg-removed ("drop-one") fit, on C0 and on C3. Plus Galactic-latitude cuts
|b| > 20°, |b| > 30° (dust/stellar-density proxy) on C0.
*Honest scope limit, pre-registered:* the immutable release parquet carries
only `object_id, ra_deg, dec_deg, class_eq, score_*_eq, is_spiral,
primary_hc, raw_flip_qc_unsafe`. Per-object DR8 brick quality, PSF depth,
seeing and E(B−V) are NOT in it, and the DR8 sweep join used by
`wave_14_qq_systematics_regression.py` lives on a retired pod path
(`/workspace/dr8_sweep_fetch/...`). Those four legs are therefore reported
as NOT RUN (proxied by leg + |b| only) — not silently omitted, not faked.

**C. Nulls on the parent selection.** (1) Fixed-occupancy multivariate-
hypergeometric label-shuffle-strict null, ≥1000 draws per selection/leg
(10,000 for C0), z from moments + one-sided rank p. (2) Monopole +
mask-leakage null: inject a pure monopole (no dipole) at the measured
monopole and at the row-16(ii) −0.26% postprocess-bias level, ≥1000
realisations on the C0 footprint, and measure the dipole amplitude that
leaks through the mask. (3) Random-axis sky-rotation control inside the
injection-recovery machinery (already in `detection_fraction`).

**D. Reported correction.** The row-16(ii) injection-calibrated postprocess
bias (−0.26% full amplitude, `injection_pilot/scale20k_injection_results.json`)
is reported as a correction alongside each amplitude; it is NEVER subtracted
into the headline number and never used to move a verdict.

## Pre-registered decision rule (fixed before seeing any output)

- **SYSTEMATIC** if ANY single cut or leg removes the signal (that fit's
  z < 2), OR if the C0 axis tracks a footprint boundary / a single imaging
  leg (i.e. the axis is driven by one leg, or |Dec_axis| sits at a leg
  boundary, or drop-one-leg moves the axis by > 45°).
- **OPEN** otherwise. This lane can NEVER return "detection"; the strongest
  available verdict is OPEN (non-null, survives the checks run here).

## Outputs

`row16ib_qc_leg_sweep.py`, `row16ib_axis_shift.json`,
`fig_row16ib_axis_shift.png`, manifest
`reproducibility/manifests/experiments/p4p-row16ib-axis-shift.json`
registered in `reproducibility/manifests/programs/galaxy-chirality.json`.

<!-- RESULTS AND VERDICT APPENDED BELOW AFTER THE RUN -->
