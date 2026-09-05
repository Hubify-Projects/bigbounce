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

_(to be filled at run time)_

## 2. Results

_(to be filled)_

## 3. Verdict

_(to be filled)_

## 4. Deviations from pre-registration

_(to be filled)_
