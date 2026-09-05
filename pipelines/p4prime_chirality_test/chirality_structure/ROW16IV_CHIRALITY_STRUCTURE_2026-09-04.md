# Row 16 (iv) — Chirality × structure: first measurements on the lab's own catalogues

Date: 2026-09-04. Local CPU only. Ledger: `project-context/NEXT_SCIENCE_LEDGER.md` row 16, item (iv).

## 0. PRE-REGISTRATION (committed BEFORE any statistic was run)

This section is frozen. Any deviation forced by the data is recorded in §4
"Deviations from pre-registration" with the reason, and never silently.

### 0.1 Data (declared)

| Role | File | Rows |
|---|---|---|
| Parity labels (primary) | `pipelines/p2_chirality/apjs_release_v1.0.244/p4_catalog_primary_safe_v1.0.244.parquet`, `primary_hc==True` subset | ~887k of 8,474,531 |
| Parity labels (secondary, if feasible) | same file, full parent | 8,474,531 |
| Anomaly targets | `pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3_v2/flagship_sample_v2_enriched.parquet` (`target_ra`,`target_dec`) | 1,244 |
| Redshifts | `pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet` (DESI spec-z matched to the same chirality catalogue) | TBD at run time |
| Cosmic web | `~/Desktop/CODE_YOU/bigbounce_datasets/desi_dr1_lss/` — inventory recorded in §1; QSO clustering + randoms are known present. If no LRG/BGS/void product covers the spiral footprint and redshift range (z<0.3), the environment test uses a **projected density proxy built from the chirality catalogue itself** (k-NN surface density over ALL spirals, parity-blind by construction), flagged as a proxy, NOT a 3D void/filament classification. |

Parity label: `s_i = +1` for CW, `-1` for CCW from `class_eq`. Objects with
neither label are dropped.

### 0.2 Selection-function correction (declared)

The catalogue carries a residual handedness monopole (P4′: injection-calibrated
residual, HC monopole f_CW − 1/2 = +1.2656%). **Every statistic below is built
on parity *fluctuations* about the sample's own global mean**,
`δ_i = s_i − ⟨s⟩_sample`, so a spatially constant monopole cancels exactly and
no external correction value is applied. Where a sub-sample mean is used
(z-bins, density bins) the comparison is between bins, i.e. differences of
means, which are also monopole-free. Spatially *varying* selection is
controlled by the label-shuffle null (§0.4), which is run **within HEALPix
NSIDE=64 pixels** so any pixel-level selection gradient is preserved under the
null.

### 0.3 Statistics (declared, one per test)

- **(a) Environment.** Local surface density Σ_i from the k=20 nearest spiral
  neighbours (all spirals, parity-blind). Galaxies binned into density
  quartiles Q1–Q4. Statistics: (a1) χ² over the 4 bin means of δ; (a2)
  Spearman/linear trend slope of ⟨δ⟩ vs log Σ. If a real void/filament
  catalogue overlapping the footprint is found in §1, (a3) void-vs-non-void
  difference of means replaces the proxy as primary.
- **(b) Anomaly cross-correlation.** w(θ) = ⟨δ⟩ over spirals in log-spaced
  annuli θ ∈ [0.02°, 5°] (8 bins) around each of the 1,244 anomaly positions.
  Statistics: (b1) per-bin z; (b2) nearest-neighbour parity excess ⟨δ⟩ of the
  single nearest spiral to each anomaly.
- **(c) Redshift.** ⟨δ⟩ in 5 equal-count spec-z bins. Statistics: (c1) χ² over
  bins; (c2) linear trend slope vs z.
- **(d) Axes.** Dipole amplitude along a fixed axis n̂:
  A(n̂) = Σ_i w_i δ_i cos θ_i / Σ_i w_i cos²θ_i, with uniform pixel weights
  (P4′ convention). Fixed axes: CMB dipole (l=264°, b=48°); CMB
  quadrupole–octopole axis (l≈250°, b≈60°, Planck-era value, cited);
  Shamir's claimed axis as quoted in the P4′ paper (§1 records the exact
  quoted value; if the P4′ paper quotes no explicit RA/Dec, this axis is
  recorded as UNAVAILABLE and not fabricated); and the **free best-fit dipole
  direction from this catalogue itself**, refit here.
  Statistics: (d1) z of A along each fixed axis; (d2) max-|A| over free
  directions with a look-elsewhere null (the same max taken in each null
  realisation).

### 0.4 Nulls (declared)

Both, ≥1000 realisations each, for every statistic:
1. **Label shuffle** — parity labels permuted *within* HEALPix NSIDE=64 pixels
   (preserves sky selection, footprint, and density field exactly; destroys
   only the parity–position association).
2. **Sky rotation** — for (b) and (d): the tracer set (anomaly positions /
   test axis) is rigidly rotated on the sky by a random rotation, spirals
   fixed; 1000 realisations.
Reported z = (observed − null mean) / null std, with the empirical two-sided
null p also reported (never only the Gaussian z).

### 0.5 Detection threshold (declared)

Number of pre-declared statistics: (a) 2 + (b) 9 (8 bins + NN) + (c) 2 +
(d) 4 (3 fixed axes + 1 free) = **17**. Look-elsewhere correction: Bonferroni
×17. A **detection** requires two-sided null p_local < 0.0027/17 = 1.6×10⁻⁴
(i.e. |z| ≳ 3.8 local, ≥3σ global). 3.8 > |z| > 3.0 local is reported as
"suggestive, not a detection". Everything else is a **null**. Free-direction
(d2) additionally carries its own internal look-elsewhere via the max-null.
No test is re-run with altered binning after seeing its result; no statistic
is added post hoc without being labelled EXPLORATORY and excluded from the
detection count.

### 0.6 Compute budget

~3 h local CPU. If a statistic exceeds it, the largest honest subset is used
and the subsetting is recorded beside the result.

---
## 1. Data inventory as found

| Asked for | Found | Used |
|---|---|---|
| 8.47M-galaxy chirality catalogue, 887k HC subset | `p4_catalog_primary_safe_v1.0.244.parquet`: 8,474,531 rows; 3,201,160 with `is_spiral`; **949,584 rows with `primary_hc` AND a CW/CCW `class_eq` label** | HC parity sample N = 949,584 (the paper's 887,472 is the further *supported-pixel* cut used for its dipole channel; we use the full HC labelled set and pixelize independently). Sample mean s = f_CW − f_CCW = **−0.788%** |
| DESI DR1 LSS void/filament products | `~/Desktop/CODE_YOU/bigbounce_datasets/desi_dr1_lss/` holds **QSO clustering catalogues + 7 random sets (NGC/SGC) and QSO power-spectrum/window/covariance products only**, all at z = 0.8–2.1. **No LRG, no BGS, no void catalogue on disk**, and no public DESI DR1 void catalogue was available offline. | NOT USED — the QSO products have **zero redshift overlap** with the z ≲ 0.3 spiral sample, so they cannot classify the spirals' environment. Per the pre-registered fallback, environment is a **projected k-NN density proxy built from the chirality catalogue's own spirals** (parity-blind), explicitly *not* a 3D void/filament membership. |
| Anomaly catalogue v2 positions | `flagship_sample_v2_enriched.parquet`, 1,244 rows with `target_ra`/`target_dec` | all 1,244 used |
| Redshifts | chirality catalogue carries **no redshift**; the P5 DESI crossmatch does | `p5_matched_chirality_desi.parquet`, primary-deduped, ZWARN=0, p_eq>0.6, 0<z<0.6 → **231,549 spirals with spec-z** |
| Shamir's claimed axis (RA/Dec) | The P4′ paper cites Shamir 2012/2020/2022/2025 for **amplitudes only** (Table `tab:bh_exclusion`); it quotes **no explicit RA/Dec for a Shamir axis**. | Recorded **UNAVAILABLE — not fabricated**. The axis battery therefore tests the CMB dipole, the CMB quadrupole–octopole axis, and the **free best-fit dipole direction refit from this catalogue** (the P4′-style dipole direction). |

Selection function: no external correction value is applied; every statistic is
built on parity fluctuations δ = s − ⟨s⟩ about the sample's own mean, so the
residual handedness monopole (whatever its calibrated value) cancels identically.

## 2. Results

All parity numbers are fluctuations δ = s − ⟨s⟩ (s = +1 CW, −1 CCW); 1,000 realisations per null; z and the empirical two-sided p are both quoted. Detection threshold (pre-registered): local p < 1.6×10⁻⁴ (|z| ≳ 3.8), i.e. 3σ after ×17 look-elsewhere.

### (a) Environment — parity vs local spiral surface density

Density = k=20 nearest-neighbour projected surface density from the catalogue's own 3,201,160 spirals (parity-blind); 949,584 HC-labelled spirals split into density quartiles (237,396 each).

| Quartile | median log₁₀Σ₂₀ [sr⁻¹] | ⟨δ⟩ [%] | ±1σ [%] |
|---|---|---|---|
| Q1 | 5.542 | +0.061 | 0.205 |
| Q2 | 5.709 | -0.019 | 0.205 |
| Q3 | 5.845 | -0.210 | 0.205 |
| Q4 | 6.042 | +0.167 | 0.205 |

χ² across quartiles = 1.810 (null 2.585 ± 2.041) → **z = -0.38, p = 0.708**.
Linear trend of ⟨δ⟩ vs log Σ = +0.00127 (null +0.00054 ± 0.00414) → **z = +0.17, p = 0.857**.

### (b) Anomaly catalogue v2 × parity — angular cross-correlation

1,244 anomaly positions × 949,584 HC spirals; 4,126,067 pairs inside 5°. Median anomaly→nearest-spiral separation 0.066°.

| θ bin [deg] | pairs | w(θ) = ⟨δ⟩ [%] | z (label shuffle) | p | z (sky rotation) | p |
|---|---|---|---|---|---|---|
| 0.020–0.040 | 297 | -0.895 | +0.16 | 0.854 | -0.06 | 0.959 |
| 0.040–0.080 | 892 | +6.618 | +1.80 | 0.070 | +1.17 | 0.239 |
| 0.080–0.159 | 3,564 | -1.905 | -0.82 | 0.438 | -0.58 | 0.582 |
| 0.159–0.316 | 13,849 | +0.160 | +0.10 | 0.912 | +0.01 | 0.998 |
| 0.316–0.631 | 53,264 | +0.815 | +0.90 | 0.371 | +0.48 | 0.601 |
| 0.631–1.257 | 211,609 | +1.116 | +0.44 | 0.655 | +1.04 | 0.294 |
| 1.257–2.507 | 807,727 | +0.085 | -0.16 | 0.883 | +0.03 | 0.974 |
| 2.507–5.000 | 3,034,865 | -0.406 | -2.37 | 0.019 | -1.05 | 0.291 |

Nearest-neighbour parity excess: ⟨δ⟩ = -6.607% → z = -1.76 (p = 0.084) vs label shuffle, z = -0.81 (p = 0.455) vs sky rotation.

The largest excursion anywhere in the battery is the outer 2.5–5° bin at z = −2.37 (p = 0.019) against the label-shuffle null — but the **same bin sits at z = −1.05 (p = 0.29) against the sky-rotation null**, i.e. it is an excursion of the large-scale selection/footprint structure that the rotation null absorbs, not a parity–anomaly association. It is a factor ~120 above the pre-registered detection p-threshold and is reported as noise.

### (c) Redshift — parity in spec-z bins

231,549 spirals with DESI spec-z (ZWARN=0, p_eq>0.6, matched-primary-deduped), 5 equal-count bins (46,310 each).

| median z | ⟨δ⟩ [%] | ±1σ [%] |
|---|---|---|
| 0.038 | +0.957 | 0.465 |
| 0.074 | +0.235 | 0.465 |
| 0.106 | -0.397 | 0.465 |
| 0.149 | -0.542 | 0.465 |
| 0.233 | -0.253 | 0.465 |

χ² across bins = 6.882 (null 3.777 ± 2.595) → **z = +1.20, p = 0.180**.
Linear trend vs z = -0.0562 (null -0.0083 ± 0.0293) → **z = -1.63, p = 0.109**. The monotone-looking decline from +0.96% at z≈0.04 to −0.54% at z≈0.15 is a 1.6σ effect against its own null and is **not** a detection.

### (d) Preferred axes — parity dipole amplitude

Uniform-pixel-weight dipole on the NSIDE=64 map of the HC sample (24,149 occupied pixels, 949,584 galaxies).

| Axis | A [%] | z (pixel-permutation null) | p | z (random-axis null) | p |
|---|---|---|---|---|---|
| CMB dipole (l=264°, b=48°) | -0.200 | +0.21 | 0.849 | +0.04 | 0.974 |
| CMB quadrupole–octopole (l≈250°, b≈60°; Planck) | -0.138 | -0.13 | 0.908 | -0.43 | 0.764 |
| Free best-fit (max over all directions) | 0.437 | +0.32 | 0.758 | — | — |

Free best-fit direction: (l, b) = (67.0°, -3.6°), (RA, Dec) = (303.4°, 28.0°), amplitude 0.437%, against a max-amplitude null of 0.385% ± 0.162% — the look-elsewhere-corrected significance is z = +0.32. It is **not** aligned with either CMB axis (>60° away), which is what an unconstrained fit to noise looks like.

UNAVAILABLE - no explicit RA/Dec quoted for Shamir's axis in the P4-prime paper; not fabricated.

Figure: `chirality_structure_summary.png` (all four tests, observed vs null, with the 3.8σ local threshold marked).

## 3. Verdicts

| Test | Statistic | Result | Verdict |
|---|---|---|---|
| (a) environment | χ² over density quartiles | z = -0.38, p = 0.71 | **NULL** |
| (a) environment | trend vs log Σ | z = +0.17, p = 0.86 | **NULL** |
| (b) anomaly × parity | w(θ), 8 bins | max \|z\| = 2.37 (2.5–5°, shuffle null), 1.05 under the rotation null | **NULL** |
| (b) anomaly × parity | nearest-neighbour excess | z = -1.76, p = 0.08 | **NULL** |
| (c) redshift | χ² over 5 spec-z bins | z = +1.20, p = 0.18 | **NULL** |
| (c) redshift | linear trend vs z | z = -1.63, p = 0.11 | **NULL (suggestive threshold not reached)** |
| (d) CMB dipole axis | A = -0.200% | z = +0.21, p = 0.85 | **NULL** |
| (d) CMB quad/oct axis | A = -0.138% | z = -0.13, p = 0.91 | **NULL** |
| (d) Shamir axis | — | no RA/Dec quoted in P4′; not fabricated | **NOT TESTED (unavailable)** |
| (d) free best-fit dipole | A = 0.437%, LEE-corrected | z = +0.32, p = 0.76 | **NULL** |

**Zero of the 15 executed pre-registered statistics reaches even the local 3σ
mark, let alone the 3.8σ look-elsewhere-corrected threshold.** At the evidential
strength these data support: the lab's own galaxy-spin parity field shows **no
association with local environment density, with the anomaly catalogue's
positions, with redshift, or with any of the tested preferred axes**. The
strongest single excursion (2.37σ local, p = 0.019) is footprint structure, not
signal — it drops to 1.05σ when the null is a rigid rotation of the tracers
rather than a relabelling.

These are null results and are published as nulls (directive R6). They extend the
P4′ dipole null from "no preferred axis" to "no parity structure correlated with
any of the environmental, positional, redshift, or axis handles the lab can
currently apply" — a strictly stronger statement about the same catalogue, and a
constraint on any bounce/parity-violation mechanism that would imprint handedness
correlated with structure at these scales and amplitudes.

## 4. Deviations from pre-registration

1. **Cosmic-web environment → density proxy.** Pre-registered fallback exercised:
   the DESI DR1 LSS products on disk are QSO-only at z = 0.8–2.1 with no overlap
   with the z ≲ 0.3 spirals and no void/filament product. The environment test is
   therefore a projected k-NN density proxy, **not** void-vs-filament membership.
   A real void test needs a low-z void catalogue (SDSS/DESI BGS) the lab does not
   currently hold.
2. **Shamir axis not tested.** The P4′ paper quotes Shamir's *amplitudes* only,
   with no RA/Dec for an axis. Recorded UNAVAILABLE rather than invented; the
   free best-fit direction stands in as the catalogue's own dipole direction.
3. **Null for test (d) changed.** The pre-registered within-pixel label shuffle is
   *degenerate* for any pixel-level dipole statistic — it preserves every pixel
   mean exactly, so the null variance is identically zero. Substituted:
   (i) random-axis rotation (already pre-registered for (d)) and (ii) permutation
   of the per-pixel parity means among occupied pixels. Both are strictly harder
   nulls than a galaxy-level shuffle for a large-scale statistic. Documented in
   the script header.
4. **Test count.** 15 of the 17 pre-registered statistics were executed (the
   Shamir-axis statistic is unavailable; a third fixed axis therefore drops, and
   the free fit absorbs its slot). The ×17 Bonferroni threshold was **kept**
   rather than loosened to ×15.
5. **HC sample size.** 949,584 HC rows carry a CW/CCW label, versus the 887,472
   quoted in P4′ — the latter is a further *supported-pixel* cut specific to that
   paper's dipole channel. The larger, cleanly-defined set is used here and the
   difference is stated rather than reconciled by cutting to match.
6. Full parent (8.47M) parity run not executed: only 3.2M rows carry `is_spiral`
   and only the HC subset carries a trustworthy CW/CCW label, so the parent adds
   selection noise rather than statistics. The parent **is** used, parity-blind,
   as the density field for test (a).

## 5. Paragraph P4′ (or a new note) may state

> Beyond the all-sky dipole, we tested whether the catalogue's handedness field
> correlates with any structural handle available to us. Using parity
> fluctuations about the sample mean (so the residual handedness monopole
> cancels identically), and 1,000-realisation label-shuffle and sky-rotation
> nulls, we find no association between spin parity and (i) local projected
> spiral surface density, in quartiles spanning a factor of three (χ² z = -0.38,
> trend z = +0.17); (ii) the angular positions of 1,244 spectroscopic anomaly
> targets, over 0.02°–5° (all eight w(θ) bins and the nearest-neighbour parity
> excess consistent with null; the largest excursion, -2.37σ in the outermost
> bin against a relabelling null, falls to -1.05σ against a rigid-rotation null
> and is footprint structure); (iii) redshift, in five equal-count spectroscopic
> bins to z = 0.3 (trend z = -1.63); or (iv) the CMB dipole (l = 264°, b = 48°)
> and CMB quadrupole-octopole (l ~ 250°, b ~ 60°) axes, whose parity dipole
> amplitudes are -0.20% and -0.14% at z = +0.21 and -0.13. A free best-fit
> dipole reaches 0.44%, below its own look-elsewhere-corrected null
> (0.38% +/- 0.16%, z = +0.32), and points nowhere near either CMB axis. With a
> 3-sigma-after-look-elsewhere threshold declared in advance, none of the fifteen
> statistics is a detection. The catalogue's null therefore extends from
> "no preferred spin axis" to "no parity structure correlated with environment,
> anomaly positions, redshift, or the CMB axes" at these amplitudes.

