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
## 3. Verdicts
## 4. Deviations from pre-registration
## 5. Paragraph P4′ (or a new note) may state
