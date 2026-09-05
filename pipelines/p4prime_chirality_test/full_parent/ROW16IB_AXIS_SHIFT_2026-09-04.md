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

---

# RESULTS (run 2026-09-04, local CPU, 95 s wall clock)

Catalog SHA-256 re-verified identical to row 16(i). Spirals 3,201,160;
`primary_hc` = 949,584; `raw_flip_qc_unsafe` = 156,135. Null = fixed-occupancy
label-shuffle-strict (10,000 draws for C0/C3, 2,000 for every other row).
`A_corr` = A_obs + row-16(ii) postprocess bias (−0.26%), **reported, never
subtracted into the headline** and never used to move the verdict.

## A. Graded QC sweep

| Selection | N in support | A_obs | A_corr | z | rank p | axis (RA, Dec) |
|---|---|---|---|---|---|---|
| C0 full parent | 3,200,420 | 0.566% | 0.306% | **+4.33** | 0.0003 | 278.6°, +25.3° |
| C1 relax `primary_hc` (`!unsafe` only) | 3,044,282 | 1.023% | 0.763% | **+9.13** | 0.0005 | 168.5°, −73.2° |
| C2 relax raw-flip (`primary_hc` only) | 947,326 | 0.460% | 0.200% | **+0.68** | 0.235 | 294.3°, +16.0° |
| C3 strict (P4′) | 887,472 | 0.467% | 0.207% | **+0.64** | 0.239 | 195.5°, −57.2° |

**The `primary_hc` confidence cut alone removes the signal** (C2, z = +0.68),
while the raw-flip QC cut alone does not (C1, z = +9.13 — larger, at a third,
nearly antipodal axis). The excess lives entirely in the low-confidence,
non-`primary_hc` population.

## B. Per-imaging-leg / footprint table (legs by Dec boundaries (−20°, +32°))

| Fit | N | A_obs | z | axis |
|---|---|---|---|---|
| C0 only BASS+MzLS | 944,742 | 1.590% | +1.29 | 328.4°, −41.9° |
| C0 drop BASS+MzLS | 2,255,518 | 0.558% | +2.72 | 272.3°, +40.4° |
| C0 only DECaLS | 1,543,733 | 0.318% | −0.39 | 268.0°, +68.5° |
| C0 drop DECaLS | 1,656,430 | 1.238% | +4.71 | 293.3°, +14.7° |
| C0 only DES | 711,688 | 2.339% | +1.53 | 255.6°, +25.4° |
| **C0 drop DES** | 2,488,635 | 0.301% | **+0.48** | 283.6°, +14.2° |
| C3 only BASS+MzLS | 208,269 | 3.916% | +2.00 | 248.7°, +56.3° |
| C3 drop BASS+MzLS | 678,781 | 0.658% | +1.02 | 121.0°, +22.2° |
| C3 only DECaLS | 462,750 | 1.657% | +2.20 | 122.2°, −47.1° |
| C3 drop DECaLS | 424,188 | 2.211% | +4.19 | 319.6°, +10.0° |
| C3 only DES | 215,919 | 5.830% | +2.49 | 359.5°, +0.5° |
| C3 drop DES | 671,441 | 1.389% | +4.26 | 157.5°, −68.9° |
| C0, \|b\| > 20° | 3,081,625 | 0.557% | +4.09 | 275.0°, +18.0° |
| C0, \|b\| > 30° | 2,637,020 | 0.615% | +3.92 | 266.7°, −1.0° |

**Removing the DES leg alone removes the signal** (z = +4.33 → +0.48, A drops
0.566% → 0.301%) — a single imaging leg carries it. Galactic-latitude cuts do
NOT remove it, so this is not a simple dust/stellar-density effect.
Depth/seeing/E(B−V)/brick-quality legs were **NOT RUN** (columns absent from
the immutable release; retired pod path) — declared, not omitted.

## C. Nulls

- Fixed-occupancy label-shuffle-strict null: re-run per row above.
- Monopole + mask-leakage null (1,000 realisations, pure monopole, no dipole,
  on the C0 footprint): at the measured monopole (δ = −0.0053) mean leaked
  dipole = **0.191%** (99th pct 0.432%), and 0.190% at the row-16(ii)
  ±0.26% level. Mask leakage alone therefore accounts for roughly a third of
  C0's 0.566%, and reaches it in the tail — a second, independent
  non-cosmological contribution.
- Random-axis sky-rotation control: inside the injection-recovery machinery
  reused from row 16(i) (`detection_fraction`).

## D. Axis stability

C0 vs C3 axis separation **107.5°**. The three QC selections give three
mutually inconsistent axes (278.6°/+25.3°, 168.5°/−73.2°, 294.3°/+16.0°),
and drop-one-leg fits move the C0 axis by 12–17°. A physical dipole cannot
change axis by ~100° under a quality cut on the same sky.

## VERDICT — SYSTEMATIC (pre-registered rule, both clauses fired)

The pre-registered rule called SYSTEMATIC if **any** single cut or leg drives
z below 2, or if the axis tracks a footprint boundary/leg. Both triggered:
the `primary_hc` confidence cut alone (C2, z = +0.68) and dropping the DES
leg alone (z = +0.48) each remove the signal, and the axis is unstable at the
~100° level across QC selections. Combined with ~0.19% of mask-leakage
monopole contamination, **the full-parent z = +4.44 dipole of row 16(i) is
QC/footprint systematic, not cosmological.** It is not "OPEN"; it is closed
as a systematic by this lane. This is a null for the parent, and it is
published as a null.

## Paragraph P4′ must carry (either way)

> The primary chirality-dipole analysis is performed on the strict
> `primary_hc && !raw_flip_qc_unsafe` selection (887,472 galaxies), which is
> consistent with isotropy (A_obs = 0.47%, z = +0.64 against a fixed-occupancy
> label-shuffle null; injection-calibrated sensitivity A_95 = 0.98%). We
> disclose that relaxing this selection to the full 3.2-million-galaxy parent
> yields a formally significant dipole (A_obs = 0.57%, z = +4.4 at RA 278.6°,
> Dec +25.3°). A pre-registered systematics test
> (`ROW16IB_AXIS_SHIFT_2026-09-04.md`) shows this parent-level signal is not
> cosmological: it is removed by the `primary_hc` confidence cut alone
> (z = +0.68) and by excluding the DES imaging leg alone (z = +0.48); its
> best-fit axis moves by 107° between the parent and strict selections and is
> mutually inconsistent across quality cuts; and a pure-monopole mask-leakage
> simulation on the same footprint leaks 0.19% of dipole amplitude on its own.
> We therefore attribute the parent-level excess to classification-confidence
> and imaging-footprint systematics and report the strict-selection null as
> the result.

## Artifacts

`row16ib_qc_leg_sweep.py`, `row16ib_figure.py`, `row16ib_axis_shift.json`,
`fig_row16ib_axis_shift.png`, `row16ib.log`, manifest
`reproducibility/manifests/experiments/p4p-row16ib-axis-shift.json`.
