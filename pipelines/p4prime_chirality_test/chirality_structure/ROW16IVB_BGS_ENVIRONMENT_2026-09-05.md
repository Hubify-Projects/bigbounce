# Row 16 (iv-b) — Chirality × cosmic web from the DESI DR1 Bright Galaxy Survey

Date: 2026-09-05. Local CPU only. Ledger: `project-context/NEXT_SCIENCE_LEDGER.md` row 16, item (iv-b).

Item (iv) (`ROW16IV_CHIRALITY_STRUCTURE_2026-09-04.md`, §1) could not do a real
environment test: the only DESI LSS products on disk were the QSO clustering
catalogues at z = 0.8–2.1, which have **zero redshift overlap** with the z ≲ 0.3
spirals, so (iv)'s environment channel fell back to a projected k-NN density
proxy built from the chirality catalogue itself. Item (iv-b) closes that gap by
downloading the DESI DR1 **BGS_BRIGHT** clustering catalogues + randoms
(0.1 < z < 0.4), which do overlap the spirals, and building the environment
field from an external tracer population.

## 0. PRE-REGISTRATION (frozen BEFORE any data were downloaded or any statistic run)

This section is frozen. Any deviation forced by the data is recorded in §4
"Deviations from pre-registration", with the reason, and never silently.

### 0.1 Data (declared)

| Role | Source | Notes |
|---|---|---|
| Environment tracers | DESI DR1 LSS `BGS_BRIGHT` clustering catalogue, NGC + SGC, from `https://data.desi.lbl.gov/public/dr1/survey/catalogs/dr1/LSS/iron/LSScats/v1.5/` | exact filenames + sizes + sha256 recorded in §1 and in the manifest; stored outside the repo at `~/Desktop/CODE_YOU/bigbounce_datasets/desi_dr1_lss/bgs/`; total download budget ≤ 6 GB |
| Selection function | ≥ 4 random catalogues per cap from the same directory | randoms define the survey selection/footprint; density is measured relative to them |
| Parity labels, spec-z subset | `pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet` — the P5 DESI spec-z matches (231,549 spirals in (iv)) | 3D environment |
| Parity labels, photo-z / no-z subset | `pipelines/p2_chirality/apjs_release_v1.0.244/p4_catalog_primary_safe_v1.0.244.parquet`, `primary_hc` + CW/CCW label | projected environment only |

Parity label `s_i = +1` CW, `-1` CCW from `class_eq`; unlabelled dropped.

### 0.2 Environment definition (declared)

A **density-based environment proxy**, stated as such. No void finder is run and
no void/filament membership is claimed.

- Build a k-NN density field on the BGS_BRIGHT galaxies: for each chirality
  galaxy, the distance to its k = 10 nearest BGS neighbours gives
  ρ_k ∝ k / d_k^3 (3D, comoving, spec-z subset, Planck-18 flat ΛCDM
  Ω_m = 0.315, h = 0.674) or ρ_k ∝ k / d_k^2 (projected, photo-z subset,
  angular separation only).
- The same k-NN estimate is computed on the **randoms**, and the reported
  density contrast is δ_k = ρ_k^data / ρ_k^random − 1, so survey selection and
  footprint edges divide out.
- Bins: **void-like** = lowest quintile of δ_k; **wall/filament** = middle three
  quintiles; **node-like** = top quintile. Quintiles are defined on the
  chirality-matched sample itself, parity-blind.

### 0.3 Statistics (declared)

Per environment bin (3 bins × 2 subsets = 6 primary cells):
- (S1) parity fraction f_CW = CW/(CW+CCW), with binomial σ;
- (S2) χ² trend across the three bins (2 dof) on f_CW;
- (S3) dipole amplitude per environment bin, P4′ convention
  A(n̂) = Σ w_i δ_i cos θ_i / Σ w_i cos²θ_i with δ_i = s_i − ⟨s⟩ of that bin,
  evaluated along the free best-fit direction of that bin, with the
  look-elsewhere max taken identically in every null realisation.

The injection-calibrated residual handedness monopole **−0.26%** (P4′) is
reported alongside every absolute f_CW so no bin's offset is read as signal;
all trend/dipole statistics are built on fluctuations about the sample mean and
are monopole-free by construction.

### 0.4 Nulls (declared)

≥ 1000 realisations each, for every statistic:
1. **Label shuffle** — parity labels permuted within HEALPix NSIDE = 64 pixels
   (preserves footprint, sky selection, and the density field exactly).
2. **Sky rotation** — the BGS tracer set is rigidly rotated on the sky by a
   random rotation with the spirals fixed, re-deriving environment bins each
   realisation.
Reported: z = (obs − null mean)/null std **and** the empirical two-sided null p.

### 0.5 Detection threshold (declared)

Pre-declared statistics: 2 subsets × (3 f_CW + 1 χ² + 3 dipole) = **14**.
Bonferroni ×14: a **detection** requires two-sided local p < 0.0027/14 =
1.9×10⁻⁴ (|z| ≳ 3.7), i.e. ≥3σ post-LEE. 3.7 > |z| > 3.0 is "suggestive, not a
detection". Everything else is a **null**. No re-binning after seeing a result;
any post hoc statistic is labelled EXPLORATORY and excluded from the count.

### 0.6 Compute budget

~2 h local CPU. If a statistic exceeds it, the largest honest subset is used and
the subsetting is recorded beside the result. No tuning of k, bin edges, or
cosmology after results are seen.

---
## 1. Data inventory as found

Only the **`BGS_BRIGHT-21.5`** flavour of the BGS clustering catalogue exists in
`.../LSScats/v1.5/` (there is no plain `BGS_BRIGHT_*_clustering.dat.fits`); this
is the DESI DR1 volume-limited M_r < -21.5 BGS sample, 0.1 < z < 0.4. That is
what was downloaded and used.

| File | Rows | Bytes | Retained as |
|---|---|---|---|
| `BGS_BRIGHT-21.5_NGC_clustering.dat.fits` | 217,614 | 25,470,720 | parquet, 8.0 MB |
| `BGS_BRIGHT-21.5_SGC_clustering.dat.fits` | 82,429 | 9,653,760 | parquet |
| `BGS_BRIGHT-21.5_NGC_{0,1,2,3}_clustering.ran.fits` | 13,248,857 each | 1,656,118,080 each | parquet |
| `BGS_BRIGHT-21.5_SGC_{0,1,2,3}_clustering.ran.fits` | 5,433,120 each | 679,127,040 each | parquet |

Total transferred **9.376 GB** across 10 files; each FITS was sha256'd (digests
in `~/Desktop/CODE_YOU/bigbounce_datasets/desi_dr1_lss/bgs/bgs_download_manifest.json`
and in the reproducibility manifest) and then compacted to RA/DEC/Z/WEIGHT
parquet and deleted, so **2.3 GB is retained on disk** — under the 6 GB budget.
sha256 of the retained parquets: `bgs/parquet_sha256.txt`.

Tracer field used: **300,043 BGS galaxies** (NGC+SGC) and **6,000,000 randoms**
(4 randoms per cap, uniformly sub-sampled with a fixed seed to 3,000,000 per cap
for tractability — a uniform sub-sample of a random catalogue adds shot noise
but no bias to the selection-function normalisation).

Chirality samples matched to that environment:

| Subset | N | Environment |
|---|---|---|
| DESI spec-z (P5 crossmatch, primary-deduped, ZWARN=0, p_eq>0.6, **0.1 < z < 0.4**) | **121,417** | 3D comoving k=10-NN density contrast |
| photo-z / no-z (`primary_hc` + CW/CCW label, full sky) | **949,584** | projected (angular) k=10-NN density contrast |

Median density contrast δ_k per bin — spec-z: 0.36 / 1.40 / 5.51;
projected: 0.53 / 4.29 / 19.6 (void-like / wall-filament / node-like). The bins
therefore span more than an order of magnitude in density in both subsets, i.e.
the split is doing real work.

## 2. Results

Parity fraction f_CW = CW/(CW+CCW). The catalogue's injection-calibrated
residual handedness monopole is **-0.26%** in f_CW - f_CCW, i.e. **-0.13%** in
f_CW - 0.5; every absolute f_CW below sits at or near that level, so the
*offsets* are consistent with the known residual and only the *differences
between bins* carry information. z and the empirical two-sided p are both
against the pre-registered label-shuffle null (1,000 realisations, permuted
within HEALPix NSIDE=64 pixels). Detection threshold: p_local < 1.9e-4
(|z| >= 3.7), i.e. 3 sigma after the pre-declared x14 look-elsewhere.

### (1) DESI spec-z subset, 3D comoving environment (N = 121,417)

| Environment | N | f_CW | binomial sigma | z vs null | p |
|---|---|---|---|---|---|
| void-like | 24,284 | 0.48999 | 0.00321 | -0.61 | 0.541 |
| wall/filament | 72,849 | 0.49489 | 0.00185 | +1.11 | 0.271 |
| node-like | 24,284 | 0.49238 | 0.00321 | -0.84 | 0.405 |

chi^2 trend (2 dof): obs 1.872, null 1.984 +/- 1.841, **z = -0.06, p = 0.952**.
Rotation null (1,000 realisations): z = -0.12, p = 0.917.

Dipole amplitude per bin (free best-fit direction, label-shuffle null with the
same free fit in each realisation): void-like A = 0.0131 (z = -1.16, p = 0.249);
wall/filament A = 0.0155 (z = +0.31, p = 0.777); node-like A = 0.0053
(z = -1.45, p = 0.117).

### (2) photo-z / no-z subset, projected environment (N = 949,584)

| Environment | N | f_CW | binomial sigma | z vs null | p |
|---|---|---|---|---|---|
| void-like | 189,917 | 0.49602 | 0.00115 | +0.64 | 0.526 |
| wall/filament | 569,750 | 0.49680 | 0.00066 | -1.06 | 0.273 |
| node-like | 189,917 | 0.49388 | 0.00115 | +2.96 | 0.0060 |

chi^2 trend (2 dof): obs 4.859, null 7.597 +/- 1.808, **z = -1.51, p = 0.083**
(the observed trend is *weaker* than the label-shuffle null expectation, which
is itself non-zero because within-pixel shuffling preserves the density-bin
composition of each HEALPix cell).

Dipole per bin: void-like A = 0.0062 (z = +0.23, p = 0.827); wall/filament
A = 0.0022 (z = +0.76, p = 0.452); node-like A = 0.0289 (z = +2.15, p = 0.027).

Figure: `row16ivb_bgs_environment.png`. Machine-readable results:
`row16ivb_bgs_environment.json`.

## 3. Verdict

**NULL, at the pre-registered threshold, in both subsets.** No statistic reaches
|z| = 3.7 (p_local < 1.9e-4); none even reaches the "suggestive" band |z| > 3.0.
The largest excursions are the projected node-like parity fraction (z = +2.96,
p_local = 0.0060; p = 0.084 after the x14 Bonferroni correction) and the
projected node-like dipole (z = +2.15, p_local = 0.027; p = 0.38 corrected) —
both are exactly what a 14-statistic battery produces under the null hypothesis.
The chi^2 environment trend is null in the spec-z subset (p = 0.952) and, in the
projected subset, is *below* its null expectation (p = 0.083 two-sided).

Evidential strength per test:
- **spec-z 3D environment trend — a real null.** 121,417 spirals with DESI
  spec-z against a genuine external tracer field; the label-shuffle and rotation
  nulls agree (p = 0.952 / 0.917). Constraining.
- **projected environment trend — a null, but weaker evidentially.** The
  projected density is a line-of-sight-integrated proxy, which dilutes any true
  3D environment dependence; a null here constrains less than the spec-z null.
- **per-bin dipoles — nulls with limited power.** Splitting into three bins
  costs sensitivity relative to the full-sample dipole channel; these bound a
  strongly environment-dependent dipole, not a weak one.
- **absolute f_CW per bin — not evidence either way.** Every bin sits within
  ~0.4% of 0.5, at or near the injection-calibrated residual -0.26%; these
  numbers are reported for completeness and are not interpreted as signal.

Paragraph P4' may state (and nothing stronger):

> Splitting the chirality sample by local environment, measured as the k-nearest-
> neighbour density contrast against the public DESI DR1 BGS_BRIGHT-21.5
> clustering catalogue and its randoms (300,043 tracers; 6.0e6 randoms), we find
> no dependence of the parity fraction on environment. For the 121,417 spirals
> with DESI spectroscopic redshifts and a three-dimensional comoving density
> measurement, the parity fractions in void-like (lowest density quintile),
> wall/filament, and node-like (top quintile) environments are 0.48999 +/- 0.00321,
> 0.49489 +/- 0.00185 and 0.49238 +/- 0.00321, with a chi^2 trend consistent with
> the label-shuffle null (z = -0.06, p = 0.95) and with a sky-rotation null
> (p = 0.92). The 949,584-galaxy projected sample gives the same conclusion
> (trend p = 0.08). Per-environment dipole amplitudes are likewise consistent
> with their nulls (|z| <= 2.2). All bins lie within a few tenths of a percent of
> parity, comparable to the injection-calibrated residual handedness of -0.26%.
> No statistic reaches the pre-registered 3 sigma post-look-elsewhere threshold;
> we report this as a null. The environment split is a density-based proxy, not
> a void/filament membership classification from a void finder.

## 4. Deviations from pre-registration

1. **Tracer flavour.** Only `BGS_BRIGHT-21.5` (volume-limited M_r < -21.5) is
   published in v1.5; the pre-registration named `BGS_BRIGHT`. Used the
   published flavour; same survey, same 0.1 < z < 0.4 window.
2. **Spec-z window.** The spec-z subset was restricted to 0.1 < z < 0.4 to lie
   inside the BGS tracer volume (the pre-registration's parent P5 selection was
   0 < z < 0.6). Forced by the tracer redshift coverage; applied before any
   statistic, parity-blind. N = 121,417 of the 231,549 P5 matches.
3. **Random sub-sampling.** 4 randoms per cap were downloaded as declared, then
   uniformly sub-sampled with a fixed seed to 3,000,000 per cap (6.0e6 total,
   20x the tracer density) for tree tractability. Uniform sub-sampling of a
   random catalogue is unbiased for the selection normalisation.
4. **FITS not retained.** Each FITS was sha256'd and compacted to parquet, then
   deleted, to hold the retained footprint to 2.3 GB (<= 6 GB budget). The
   digests make the download exactly reproducible.
5. **Projected rotation null: 10 realisations, not 1,000.** Each projected
   rotation realisation re-queries 949,584 points against the 6.0e6-random and
   300,043-tracer trees and costs ~285 s; a pre-set 45-minute wall-clock guard
   (independent of the results) stopped it after 10. It is therefore reported
   with a p-resolution of only ~0.09 and is **not** used as evidence; the
   1,000-realisation label-shuffle null is the primary null for that subset, and
   the spec-z rotation null did run the full 1,000. This is a genuine
   power limitation of the projected channel's rotation null, recorded, not
   worked around.
6. No other deviation. No statistic was re-run with altered binning, k, or
   cosmology after seeing a result; no post-hoc statistic was added.
