# Lane LS14-row4-ebv run log (2026-09-22, all times PT)

Pre-registration `PRE_REGISTRATION.md` was committed (`34db5010`) before any
f_NL statistic was computed. Result: `RESULT_2026-09-22.md`.

## 0. Premise and reachability (before pre-registering — no statistics)

Listed the DESI DR1 full-shape-bao-clustering VAC v1.0 `spectrum/` and
`covariance/EZmock/` directories and confirmed the LRG z0.8–1.1
`_thetacut0.05` products exist and return `Content-Length` over HTTP range
reads: window (216,704,470 B), GCcomb/NGC/SGC measured P_ℓ (111,684 B each)
and EZmock covariance (497,102 B), in both conventions. Nothing was
substituted; pre-registration fallback 1 was never triggered.

Environment: `research/desi_png_reproduction/.venv312` (the env LS11 used —
`pypower`, `cosmoprimo`, `h5py`, numpy 2.5.2). Free disk at lane start
≈ 8 GB with three other lanes live in the same checkout.

## 1. Input characterisation (official products only, no f_NL)

```
nmodes identical: True
k identical: True
ell=0 nk_in_range=77 thetacut/untreated P: min=0.9375 med=0.9634 max=0.9873
ell=2 nk_in_range=77 thetacut/untreated P: min=0.9470 med=0.9845 max=0.9960
ell=4 nk_in_range=77 thetacut/untreated P: min=-14.0778 med=0.9682 max=3.8312
cov shapes (240, 240) (240, 240)
cov k grids identical: True | edges identical: True
n_fit_bins=48  sigma_thetacut/sigma_untreated: min=0.9968 med=0.9994 max=1.0000
TOTAL STREAMED BYTES 1217572
```

This is what fixed the lane's method **before** any fit: the θ-cut changes
the data-side estimator by ~3.7 % with a ~5 % tilt across the fit range
while leaving the covariance essentially untouched, so a window/covariance-
only swap is not self-consistent and was demoted to diagnostic D2 in the
pre-registration.

## 2. Code

- `thetacut_io.py` — `../lrg_channel_2026_09_22/lrg_official_io.py` with one
  added `variant` argument and cap-resolved spectra; same fetch/sha256/
  BytesIO mechanics, nothing written to disk.
- `run_ebv_thetacut.py` — the driver. Every fit goes through LS11's
  `lrg_fit_core.py` unchanged, on LS11's grid (`np.linspace(-400,400,801)`),
  LS11's k-range (0.003–0.08), LS11's `verdict()` and LS11's
  `fit_lrg_headline.cosmo_at`. The only new arithmetic is the transfer
  multiplication, asserted at run time to reduce **bitwise** to
  `fit_lrg_splits.combine_caps` when the transfer is identically 1.

Two defects found and fixed before the numbers were produced, both in this
lane's own new code, neither touching any fitted quantity: the bitwise
identity assertion compared k arrays containing NaN without `equal_nan`,
and the streamed-byte/sha256 accumulators overwrote instead of merging on a
resumed run.

## 3. Verbatim console output of `run_ebv_thetacut.py`

Console logs are gitignored repo-wide (`.gitignore:76`), so the run is
transcribed here.

```
[transfer] {
 "NGC": {
  "0": {"n_fine_in_range": 77, "ratio_min": 0.9349985249633547,
        "ratio_med": 0.9614710380761794, "ratio_max": 0.986282846739431},
  "2": {"n_fine_in_range": 77, "ratio_min": 0.946956539886806,
        "ratio_med": 0.9884346035275396, "ratio_max": 0.9991840520727784},
  "4": {"n_fine_in_range": 77, "n_clipped_in_range": 4}
 },
 "SGC": {
  "0": {"n_fine_in_range": 77, "ratio_min": 0.9432758709838356,
        "ratio_med": 0.9676620104445115, "ratio_max": 0.9911562050295278},
  "2": {"n_fine_in_range": 77, "ratio_min": 0.7308738746589114,
        "ratio_med": 0.9768774163765073, "ratio_max": 1.2403642018923486},
  "4": {"n_fine_in_range": 77, "n_clipped_in_range": 4}
 },
 "cap_spread": {"0": 0.015876982020401442, "2": 0.25464120112544175}
}
[identity] bitwise OK
[basis] untreated p=1.0 in 15s (streamed 218 MB)
  A  untreated p=1.0: full-sample f_NL=-0.801 +/- 10.374 b1=2.2133 chi2/dof=1.350
  G_gate                       p=1.0: high=-17.62+/-8.47 low=-0.27+/-8.95 d=-17.35 sd=12.32 raw=-1.408 corr=-0.995 -> no detectable sensitivity
[basis] untreated p=1.6 in 16s (streamed 218 MB)
  A  untreated p=1.6: full-sample f_NL=-1.574 +/- 20.518 b1=2.2133 chi2/dof=1.350
  G_gate                       p=1.6: high=-35.33+/-16.88 low=-0.54+/-17.90 d=-34.79 sd=24.60 raw=-1.414 corr=-1.000 -> no detectable sensitivity
[basis] thetacut0.05 p=1.0 in 14s (streamed 435 MB)
  A  thetacut0.05 p=1.0: full-sample f_NL=+1.092 +/- 10.329 b1=2.1883 chi2/dof=1.359
  D2_diagnostic_inconsistent   p=1.0: high=-18.35+/-7.63 low=-1.92+/-8.82 d=-16.43 sd=11.66 raw=-1.409 corr=-0.996 -> no detectable sensitivity
  D1_primary                   p=1.0: high=-16.33+/-9.40 low=+0.94+/-9.06 d=-17.27 sd=13.06 raw=-1.322 corr=-0.935 -> no detectable sensitivity
  V_swapped_cap                p=1.0: high=-16.82+/-9.32 low=+1.28+/-9.03 d=-18.10 sd=12.97 raw=-1.395 corr=-0.986 -> no detectable sensitivity
[basis] thetacut0.05 p=1.6 in 15s (streamed 435 MB)
  A  thetacut0.05 p=1.6: full-sample f_NL=+2.222 +/- 20.878 b1=2.1883 chi2/dof=1.359
  D2_diagnostic_inconsistent   p=1.6: high=-35.62+/-14.72 low=-3.70+/-17.05 d=-31.92 sd=22.53 raw=-1.417 corr=-1.002 -> MARGINAL WATCH ITEM
  D1_primary                   p=1.6: high=-33.43+/-19.14 low=+1.92+/-18.54 d=-35.35 sd=26.65 raw=-1.326 corr=-0.938 -> no detectable sensitivity
  V_swapped_cap                p=1.6: high=-34.41+/-18.96 low=+2.60+/-18.36 d=-37.02 sd=26.39 raw=-1.403 corr=-0.992 -> no detectable sensitivity
[GATE] d_corr=0.0004 d_high=0.0005 d_low=0.0037 -> PASS
streamed 435 MB, 84s
DONE
```

## 4. Order of belief

The gate ran first and passed to 0.0004 in the corrected Δ/σ, so LS11's
published row is reproduced by this lane's code on the products it used
before any θ-cut number was reported. The anchor (complete official θ-cut
triple vs complete untreated triple) is approximation-free. D1 is the
primary θ-cut answer; V bounds its one approximation; D2 is labelled
inconsistent and is never quoted as the θ-cut result.

## 5. What was not done

No genuine θ-cut re-measurement of the split halves (the direct
small-angle pair sums, ~10⁸ R–R pairs per half, need an HPC venue). No
`-rotated` variant. No catalogue was read; no bulk data was written; the
split P(k) are LS11's committed JSONs. Peak disk for this lane is its own
output directory, 56 KB.
