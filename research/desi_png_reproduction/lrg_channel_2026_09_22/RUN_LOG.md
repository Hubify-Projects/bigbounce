# Ledger row 4 — LRG channel run log (lane LS11-row4-lrg, 2026-09-22)

All times PT. Pre-registration `PRE_REGISTRATION.md` was committed
(`87b850b8`) before any statistic was computed.

## 0. Premise check (before anything else)

The lane brief stated `research/desi_png_reproduction/official_products/` is
empty (0 B). Verified: that repo-internal directory *is* empty, but it was
never where the products live — `official_window_io.py` reads
`/Users/…/bigbounce_datasets/desi_dr1_lss/official_products`, which is
intact (9 QSO files, 1.27 GB, sha256s in `../official_products_sha256.txt`).
No LRG official product existed anywhere on this machine, so every LRG input
was streamed fresh regardless. Free disk at start: **11 GB**.

Reachability confirmed before pre-registering (HEAD requests and HDF5
attribute reads only — not statistics):

- `data.desi.lbl.gov` returns `Accept-Ranges: bytes` on both the VAC and the
  LSS catalogue trees, so HTTP range reads work.
- All three LRG z-bins have the exact analogues of the six QSO products v3–v5
  used: `spectrum-poles_LRG_{NGC,SGC,GCcomb}_z{ZB}.h5` (111,684 B),
  `window_spectrum-poles_LRG_GCcomb_z{ZB}.h5` (216,704,470 B),
  `covariance_spectrum-poles_LRG_GCcomb_z{ZB}.h5` (511,062 B).
- `zeff` attributes: **0.50963, 0.70580, 0.91859**.
- LRG catalogue row counts from the FITS headers: 1,476,135 (NGC data),
  662,492 (SGC data), 9,389,588 / 4,959,721 per random realisation.

## 1. Streaming infrastructure (`http_stream.py`)

Two surfaces, both reusing lane `bb-LS10-indomain-d180`'s "pull the bytes,
decode in memory, drop them" pattern:

- `RangeFile` — a seekable file-like object over HTTPS with a block cache,
  so `h5py` can open a remote HDF5 with **zero bytes on disk**. Used for the
  first reconnaissance reads.
- `stream_fits_sequential` — a strictly sequential byte-0→EOF pass over a
  remote FITS binary table. Because the pass is sequential and complete, the
  **whole-file sha256 costs no extra network traffic**, while only the six
  needed columns are ever materialised.

## 2. Derived-column cache (`stream_lrg_cache.py`)

Streamed the two LRG data catalogues and 4 random realisations per cap
(N_RAN = 4, matching v5's QSO runs). Kept `RA, DEC, Z, WEIGHT, WEIGHT_SYS,
WEIGHT_FKP`, attached `EBV, STARDENS, GALDEPTH_Z` from the LOCAL
`pixweight-dark.fits` (nside 256 nested, identical to
`../imaging_splits_crossmatch.py`), computed Galactic latitude, applied the
0.4 < z < 1.1 cut, wrote float32 arrays outside the repo.

- **Streamed: 6,233,140,800 B (6.23 GB).** Bulk catalogue bytes written to
  disk: **0**.
- Derived cache: 2,381,031,400 B (2.38 GB) — 10 files, 59,525,171 rows.
- `n_unmatched_pixweight` = **0** across all 10 files.
- The vectorised Galactic-latitude formula was checked against
  `astropy.SkyCoord` (what v5 used) on 20,000 random sky positions:
  **max |Δb| = 3.06e-06 deg**, seven orders of magnitude below the 40° split
  threshold.
- Receipts (per-file whole-file sha256, byte count, rows read, rows kept,
  seconds): `outputs/stream_manifest.json`.

## 3. Fitting core (`lrg_fit_core.py`) and its regression test

`b(k) = b1 + 3 f_NL δ_c (b1 − p)/α(k) = A(k) b1 + B(k)` makes the multipole
model exactly quadratic in b1, so the windowed, rebinned model vector is
`M(b1) = M0 + M1 b1 + M2 b1²` and χ²(b1) is an exact quartic whose minimum
is a cubic root. Profiling b1 out therefore costs three matrix-vector
products per f_NL grid point instead of ~50 Nelder-Mead evaluations. This is
an algebraic reorganisation of v3/v4/v5's fit, not a different fit:

- `verify_quadratic()` compares the decomposition against a verbatim copy of
  `../fit_fnl_splits.py`'s expression: **max relative difference 6.8e-12**
  (float64 roundoff).
- `tests/regress_qso.py` runs the whole core on the **local QSO official
  products** and must reproduce v5's published headline. Result:

  | | this core | v5 published | Δ |
  |---|---|---|---|
  | p=1.6 f_NL | −2.1698 | −2.1692 | 0.0006 (2e-5 σ) |
  | p=1.6 σ | 25.100 | 25.287 | −0.7 % |
  | p=1.0 f_NL | −1.1278 | −1.1274 | 0.0004 |
  | p=1.0 σ | 13.087 | 13.149 | −0.5 % |
  | b1 | 2.24932 | 2.24932 | <1e-5 |
  | χ²_min | 62.4010 | 62.4010 | 1e-5 |
  | n_data_bins | 48 | 48 | — |

  χ² and b1 agree to the last printed digit; the sub-1 % σ difference is
  grid/interpolation resolution (v5 located Δχ²=1 with a 121-point
  Nelder-Mead scan, this core with a fine grid plus a parabolic vertex). The
  regression is asserted at the 2 %-of-σ level and **PASSES**; had it not,
  no LRG number would have been reported (pre-registration §6 item 4).

## 4. Headline fit (`fit_lrg_headline.py`)

Streams the three z-bins' official window + measured P_ell + EZmock
covariance (652 MB, nothing on disk), asserts the z_eff parameterisation is
bit-for-bit the same code path as the QSO fits at z_eff = 1.491, then
profiles b1 out on an f_NL grid per bin and per p.

## 5. Systematics table (`pk_lrg_splits.py` → `fit_lrg_splits.py`)

60 `pypower.CatalogFFTPower` measurements (5 properties × 2 halves × 2 caps
× 3 z-bins) at v5's exact settings, from the derived cache; then the
pre-registered fits with the official window + official EZmock covariance
and the disclosed √2 covariance-reuse correction.

## 6. Provenance check (lab-native count vs the published sample)

Counting the streamed LRG data catalogues in the published PNG sample's own
redshift range gives **1,631,715** objects in 0.6 < z < 1.1 against the
**1,631,716** quoted by Chaussidon et al. 2024 (as cited in A3M §VI) — a
difference of exactly one object, which is the strict (`z > lo & z < hi`)
versus inclusive edge cut. This is a provenance match, not a measurement.
Per-bin counts: 506,911 (z0.4–0.6), 771,893 (z0.6–0.8), 859,821 (z0.8–1.1);
2,138,627 over the full 0.4 < z < 1.1. Artifact: `outputs/lrg_counts.json`.

**Consequence for presentation:** the published LRG PNG sample is
0.6 < z < 1.1, i.e. the upper two of the three official z-bins. The
pre-registered headline remains the **three-bin** combination; the
published-sample-matched **two-bin** (0.6 < z < 1.1) combination is reported
**alongside** it in `outputs/lrg_vs_qso.json`, never in place of it, so the
comparison against the published constraint is made on the published sample
definition. Both numbers are stated whichever way they fall.

## 7. Verbatim console receipts

Console logs (`*.log`) are gitignored repo-wide (`.gitignore:76`), so the raw
output of every run in this lane is transcribed here.

### `stream_lrg_cache.py`

```
gal_b vs astropy: max |delta| = 3.06e-06 deg
[LRG_NGC_data] 1476135 rows -> 1476135 kept (143 MB streamed, 8s)
[LRG_NGC_ran0] 9389588 rows -> 9389588 kept (986 MB streamed, 52s)
[LRG_NGC_ran1] 9384611 rows -> 9384611 kept (985 MB streamed, 62s)
[LRG_NGC_ran2] 9386285 rows -> 9386285 kept (986 MB streamed, 58s)
[LRG_NGC_ran3] 9390153 rows -> 9390153 kept (986 MB streamed, 63s)
[LRG_SGC_data] 662492 rows -> 662492 kept (64 MB streamed, 8s)
[LRG_SGC_ran0] 4959721 rows -> 4959721 kept (521 MB streamed, 40s)
[LRG_SGC_ran1] 4959267 rows -> 4959267 kept (521 MB streamed, 26s)
[LRG_SGC_ran2] 4959422 rows -> 4959422 kept (521 MB streamed, 30s)
[LRG_SGC_ran3] 4957497 rows -> 4957497 kept (521 MB streamed, 29s)
{
  "_galb_vs_astropy_max_absdeg": 3.056556582947678e-06,
  "_total_streamed_bytes": 6233140800,
  "_cache_bytes": 2381031400
}
```

### `fit_lrg_headline.py`

```
[stream] LRG z0.4-0.6 zeff=0.50963 n_bins=48 cum 217 MB
[stream] LRG z0.6-0.8 zeff=0.70580 n_bins=48 cum 435 MB
[stream] LRG z0.8-1.1 zeff=0.91859 n_bins=48 cum 652 MB
  p=1.0 z0.4-0.6: f_NL=-7.916 +/- 9.909  b1=1.8656 chi2/dof=1.286
  p=1.0 z0.6-0.8: f_NL=-1.378 +/- 8.982  b1=2.0546 chi2/dof=1.193
  p=1.0 z0.8-1.1: f_NL=-0.795 +/- 10.380  b1=2.2132 chi2/dof=1.350
  p=1.0 COMBINED: f_NL=-3.403 +/- 5.745
  p=1.6 z0.4-0.6: f_NL=-25.798 +/- 32.177  b1=1.8656 chi2/dof=1.286
  p=1.6 z0.6-0.8: f_NL=-3.197 +/- 20.826  b1=2.0546 chi2/dof=1.193
  p=1.6 z0.8-1.1: f_NL=-1.573 +/- 20.522  b1=2.2132 chi2/dof=1.350
  p=1.6 COMBINED: f_NL=-6.633 +/- 13.684
{
  "1.0": {
    "f_nl": -3.4032819964709917,
    "lo_68": -9.191717978227114,
    "hi_68": 2.2981161010717712,
    "sigma": 5.744917039649443,
    "chi2_min": 176.41584217727086,
    "n_bins": 144,
    "note": "three z-bins combined by summing the b1-profiled chi2 curves (independent b1 per bin, one shared f_NL). Bins treated as independent: no cross-bin official covariance product exists. Disclosed approximation, same class as the v4/v5 split covariance reuse."
  },
  "1.6": {
    "f_nl": -6.632951593815755,
    "lo_68": -20.39584569258143,
    "hi_68": 6.971228523797765,
    "sigma": 13.683537108189599,
    "chi2_min": 176.53466915463196,
    "n_bins": 144,
    "note": "three z-bins combined by summing the b1-profiled chi2 curves (independent b1 per bin, one shared f_NL). Bins treated as independent: no cross-bin official covariance product exists. Disclosed approximation, same class as the v4/v5 split covariance reuse."
  }
}
streamed 652 MB, 1299s
```

### `pk_lrg_splits.py` (60 measurements)

```
== z0.8-1.1 medians {'EBV': 0.03908361494541168, 'STARDENS': 667.2276611328125, 'GALDEPTH_Z': 68.14195251464844, '_n_data': 859821}
[pk_LRG_z0.8-1.1_NGC_EBV_high] N=237213 Nran=6015974 63s
[pk_LRG_z0.8-1.1_NGC_EBV_low] N=358206 Nran=9070907 64s
[pk_LRG_z0.8-1.1_SGC_EBV_high] N=192691 Nran=5688892 54s
[pk_LRG_z0.8-1.1_SGC_EBV_low] N=71711 Nran=2291307 44s
[pk_LRG_z0.8-1.1_NGC_STARDENS_high] N=307116 Nran=7848343 68s
[pk_LRG_z0.8-1.1_NGC_STARDENS_low] N=288303 Nran=7238538 64s
[pk_LRG_z0.8-1.1_SGC_STARDENS_high] N=105540 Nran=3192055 48s
[pk_LRG_z0.8-1.1_SGC_STARDENS_low] N=158862 Nran=4788144 46s
[pk_LRG_z0.8-1.1_NGC_GALDEPTH_Z_high] N=237049 Nran=5947346 58s
[pk_LRG_z0.8-1.1_NGC_GALDEPTH_Z_low] N=358370 Nran=9139535 64s
[pk_LRG_z0.8-1.1_SGC_GALDEPTH_Z_high] N=192857 Nran=5760772 52s
[pk_LRG_z0.8-1.1_SGC_GALDEPTH_Z_low] N=71545 Nran=2219427 39s
[pk_LRG_z0.8-1.1_NGC_WEIGHTSYS_high] N=595419 Nran=15086881 86s
[pk_LRG_z0.8-1.1_NGC_WEIGHTSYS_low] N=595419 Nran=15086881 50s
[pk_LRG_z0.8-1.1_SGC_WEIGHTSYS_high] N=264402 Nran=7980199 28s
[pk_LRG_z0.8-1.1_SGC_WEIGHTSYS_low] N=264402 Nran=7980199 28s
[pk_LRG_z0.8-1.1_NGC_GALLAT_high] N=382295 Nran=9466680 30s
[pk_LRG_z0.8-1.1_NGC_GALLAT_low] N=213124 Nran=5620201 26s
[pk_LRG_z0.8-1.1_SGC_GALLAT_high] N=184512 Nran=5592164 24s
[pk_LRG_z0.8-1.1_SGC_GALLAT_low] N=79890 Nran=2388035 22s
== z0.6-0.8 medians {'EBV': 0.03924260288476944, 'STARDENS': 667.2276611328125, 'GALDEPTH_Z': 68.10872650146484, '_n_data': 771893}
[pk_LRG_z0.6-0.8_NGC_EBV_high] N=213773 Nran=5360799 24s
[pk_LRG_z0.6-0.8_NGC_EBV_low] N=320181 Nran=8216197 27s
[pk_LRG_z0.6-0.8_SGC_EBV_high] N=172168 Nran=5075218 26s
[pk_LRG_z0.6-0.8_SGC_EBV_low] N=65771 Nran=2064734 19s
[pk_LRG_z0.6-0.8_NGC_STARDENS_high] N=278463 Nran=7056167 27s
[pk_LRG_z0.6-0.8_NGC_STARDENS_low] N=255491 Nran=6520829 24s
[pk_LRG_z0.6-0.8_SGC_STARDENS_high] N=96362 Nran=2857677 15s
[pk_LRG_z0.6-0.8_SGC_STARDENS_low] N=141577 Nran=4282275 18s
[pk_LRG_z0.6-0.8_NGC_GALDEPTH_Z_high] N=212880 Nran=5372104 26s
[pk_LRG_z0.6-0.8_NGC_GALDEPTH_Z_low] N=321074 Nran=8204892 30s
[pk_LRG_z0.6-0.8_SGC_GALDEPTH_Z_high] N=173066 Nran=5156981 25s
[pk_LRG_z0.6-0.8_SGC_GALDEPTH_Z_low] N=64873 Nran=1982971 17s
[pk_LRG_z0.6-0.8_NGC_WEIGHTSYS_high] N=533954 Nran=13576996 32s
[pk_LRG_z0.6-0.8_NGC_WEIGHTSYS_low] N=533954 Nran=13576996 28s
[pk_LRG_z0.6-0.8_SGC_WEIGHTSYS_high] N=237939 Nran=7139952 16s
[pk_LRG_z0.6-0.8_SGC_WEIGHTSYS_low] N=237939 Nran=7139952 16s
[pk_LRG_z0.6-0.8_NGC_GALLAT_high] N=339734 Nran=8520471 20s
[pk_LRG_z0.6-0.8_NGC_GALLAT_low] N=194220 Nran=5056525 16s
[pk_LRG_z0.6-0.8_SGC_GALLAT_high] N=164879 Nran=5004639 19s
[pk_LRG_z0.6-0.8_SGC_GALLAT_low] N=73060 Nran=2135313 15s
== z0.4-0.6 medians {'EBV': 0.03953113034367561, 'STARDENS': 667.2276611328125, 'GALDEPTH_Z': 68.45207214355469, '_n_data': 506911}
[pk_LRG_z0.4-0.6_NGC_EBV_high] N=138495 Nran=3472996 19s
[pk_LRG_z0.4-0.6_NGC_EBV_low] N=208266 Nran=5413726 27s
[pk_LRG_z0.4-0.6_SGC_EBV_high] N=114960 Nran=3331824 22s
[pk_LRG_z0.4-0.6_SGC_EBV_low] N=45190 Nran=1383900 20s
[pk_LRG_z0.4-0.6_NGC_STARDENS_high] N=181674 Nran=4622985 26s
[pk_LRG_z0.4-0.6_NGC_STARDENS_low] N=165087 Nran=4263737 17s
[pk_LRG_z0.4-0.6_SGC_STARDENS_high] N=63024 Nran=1886966 14s
[pk_LRG_z0.4-0.6_SGC_STARDENS_low] N=97126 Nran=2828758 14s
[pk_LRG_z0.4-0.6_NGC_GALDEPTH_Z_high] N=136948 Nran=3435752 17s
[pk_LRG_z0.4-0.6_NGC_GALDEPTH_Z_low] N=209813 Nran=5450970 17s
[pk_LRG_z0.4-0.6_SGC_GALDEPTH_Z_high] N=116507 Nran=3383200 16s
[pk_LRG_z0.4-0.6_SGC_GALDEPTH_Z_low] N=43643 Nran=1332524 13s
[pk_LRG_z0.4-0.6_NGC_WEIGHTSYS_high] N=346761 Nran=8886722 22s
[pk_LRG_z0.4-0.6_NGC_WEIGHTSYS_low] N=346761 Nran=8886722 21s
[pk_LRG_z0.4-0.6_SGC_WEIGHTSYS_high] N=160150 Nran=4715724 16s
[pk_LRG_z0.4-0.6_SGC_WEIGHTSYS_low] N=160150 Nran=4715724 17s
[pk_LRG_z0.4-0.6_NGC_GALLAT_high] N=218324 Nran=5577730 18s
[pk_LRG_z0.4-0.6_NGC_GALLAT_low] N=128437 Nran=3308992 15s
[pk_LRG_z0.4-0.6_SGC_GALLAT_high] N=112076 Nran=3304448 15s
[pk_LRG_z0.4-0.6_SGC_GALLAT_low] N=48074 Nran=1411276 13s
DONE
```

### `fit_lrg_splits.py`

```
[basis] z0.8-1.1 p=1.0 in 55s
z0.8-1.1 p=1.0 EBV: high=-17.62+/-8.47 low=-0.27+/-8.95 d=-17.35 sd=12.32 raw=-1.41 corr=-1.00 -> no detectable sensitivity
z0.8-1.1 p=1.0 STARDENS: high=-11.89+/-19.60 low=-4.12+/-7.39 d=-7.77 sd=20.95 raw=-0.37 corr=-0.26 -> no detectable sensitivity
z0.8-1.1 p=1.0 GALDEPTH_Z: high=-11.02+/-8.52 low=-10.50+/-11.05 d=-0.52 sd=13.96 raw=-0.04 corr=-0.03 -> no detectable sensitivity
z0.8-1.1 p=1.0 WEIGHTSYS: high=+0.45+/-14.13 low=+4.93+/-15.45 d=-4.48 sd=20.93 raw=-0.21 corr=-0.15 -> no detectable sensitivity
z0.8-1.1 p=1.0 GALLAT: high=-3.46+/-9.58 low=-11.28+/-9.90 d=+7.82 sd=13.78 raw=+0.57 corr=+0.40 -> no detectable sensitivity
[basis] z0.8-1.1 p=1.6 in 101s
z0.8-1.1 p=1.6 EBV: high=-35.33+/-16.88 low=-0.54+/-17.90 d=-34.79 sd=24.60 raw=-1.41 corr=-1.00 -> no detectable sensitivity
z0.8-1.1 p=1.6 STARDENS: high=-23.74+/-39.09 low=-8.34+/-14.97 d=-15.40 sd=41.86 raw=-0.37 corr=-0.26 -> no detectable sensitivity
z0.8-1.1 p=1.6 GALDEPTH_Z: high=-23.21+/-17.88 low=-22.28+/-23.40 d=-0.94 sd=29.44 raw=-0.03 corr=-0.02 -> no detectable sensitivity
z0.8-1.1 p=1.6 WEIGHTSYS: high=+0.89+/-27.89 low=+9.82+/-30.54 d=-8.92 sd=41.36 raw=-0.22 corr=-0.15 -> no detectable sensitivity
z0.8-1.1 p=1.6 GALLAT: high=-6.86+/-18.99 low=-22.22+/-19.45 d=+15.37 sd=27.18 raw=+0.57 corr=+0.40 -> no detectable sensitivity
DONE
[basis] z0.6-0.8 p=1.0 in 61s
z0.6-0.8 p=1.0 EBV: high=-4.49+/-9.74 low=-5.60+/-9.98 d=+1.12 sd=13.95 raw=+0.08 corr=+0.06 -> no detectable sensitivity
z0.6-0.8 p=1.0 STARDENS: high=-1.00+/-8.43 low=-4.03+/-9.68 d=+3.03 sd=12.83 raw=+0.24 corr=+0.17 -> no detectable sensitivity
z0.6-0.8 p=1.0 GALDEPTH_Z: high=-9.20+/-9.02 low=-5.16+/-13.91 d=-4.04 sd=16.58 raw=-0.24 corr=-0.17 -> no detectable sensitivity
z0.6-0.8 p=1.0 WEIGHTSYS: high=-1.32+/-8.93 low=+7.12+/-10.16 d=-8.44 sd=13.53 raw=-0.62 corr=-0.44 -> no detectable sensitivity
z0.6-0.8 p=1.0 GALLAT: high=+0.59+/-11.86 low=-1.60+/-11.67 d=+2.19 sd=16.64 raw=+0.13 corr=+0.09 -> no detectable sensitivity
[basis] z0.6-0.8 p=1.6 in 109s
z0.6-0.8 p=1.6 EBV: high=-10.45+/-22.67 low=-13.46+/-23.97 d=+3.01 sd=32.99 raw=+0.09 corr=+0.06 -> no detectable sensitivity
z0.6-0.8 p=1.6 STARDENS: high=-2.28+/-19.24 low=-9.84+/-23.63 d=+7.56 sd=30.48 raw=+0.25 corr=+0.18 -> no detectable sensitivity
z0.6-0.8 p=1.6 GALDEPTH_Z: high=-23.80+/-23.23 low=-12.96+/-34.87 d=-10.83 sd=41.90 raw=-0.26 corr=-0.18 -> no detectable sensitivity
z0.6-0.8 p=1.6 WEIGHTSYS: high=-3.05+/-20.74 low=+16.55+/-23.65 d=-19.60 sd=31.45 raw=-0.62 corr=-0.44 -> no detectable sensitivity
z0.6-0.8 p=1.6 GALLAT: high=+1.40+/-28.09 low=-3.61+/-26.27 d=+5.01 sd=38.46 raw=+0.13 corr=+0.09 -> no detectable sensitivity
DONE
[basis] z0.4-0.6 p=1.0 in 50s
z0.4-0.6 p=1.0 EBV: high=-12.68+/-11.14 low=-7.78+/-10.57 d=-4.90 sd=15.36 raw=-0.32 corr=-0.23 -> no detectable sensitivity
z0.4-0.6 p=1.0 STARDENS: high=-13.17+/-10.08 low=-5.68+/-9.93 d=-7.48 sd=14.15 raw=-0.53 corr=-0.37 -> no detectable sensitivity
z0.4-0.6 p=1.0 GALDEPTH_Z: high=-13.51+/-11.53 low=-9.56+/-9.55 d=-3.95 sd=14.97 raw=-0.26 corr=-0.19 -> no detectable sensitivity
z0.4-0.6 p=1.0 WEIGHTSYS: high=-8.17+/-9.65 low=-6.39+/-7.66 d=-1.78 sd=12.32 raw=-0.14 corr=-0.10 -> no detectable sensitivity
z0.4-0.6 p=1.0 GALLAT: high=-5.84+/-9.85 low=-21.35+/-14.71 d=+15.51 sd=17.70 raw=+0.88 corr=+0.62 -> no detectable sensitivity
[basis] z0.4-0.6 p=1.6 in 84s
z0.4-0.6 p=1.6 EBV: high=-45.56+/-39.83 low=-27.36+/-37.04 d=-18.20 sd=54.39 raw=-0.33 corr=-0.24 -> no detectable sensitivity
z0.4-0.6 p=1.6 STARDENS: high=-48.20+/-36.67 low=-17.85+/-31.15 d=-30.35 sd=48.12 raw=-0.63 corr=-0.45 -> no detectable sensitivity
z0.4-0.6 p=1.6 GALDEPTH_Z: high=-55.60+/-47.17 low=-39.45+/-39.23 d=-16.15 sd=61.35 raw=-0.26 corr=-0.19 -> no detectable sensitivity
z0.4-0.6 p=1.6 WEIGHTSYS: high=-26.52+/-31.22 low=-20.82+/-24.90 d=-5.70 sd=39.93 raw=-0.14 corr=-0.10 -> no detectable sensitivity
z0.4-0.6 p=1.6 GALLAT: high=-18.15+/-30.54 low=-82.62+/-56.46 d=+64.47 sd=64.19 raw=+1.00 corr=+0.71 -> no detectable sensitivity
DONE
```
