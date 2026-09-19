# Ledger #6, second discriminator — PRE-REGISTRATION

**Written and committed 2026-09-19, BEFORE any statistic was computed.**
Lane `bb-LS2-ledger6` of campaign `CAMPAIGN_2026-09-18_publication_push.md`.
Ledger item: `NEXT_SCIENCE_LEDGER.md` row 6 (early-universe anomaly map).
Vision route: `VISION.md` route 3.

## 0. Why this test, and why now

Row 6 names three anomaly classes. Two already have a current-data verdict:

| Class | Verdict | Where |
|---|---|---|
| z > 10 over-massive galaxies | NULL — not yet testable, and local PNG at −35/16 *suppresses* the tail (wrong sign for the anomaly) | `research/anomaly_map/LEDGER6_DISCRIMINATOR_BRIEF_2026-09-02.md` §3 |
| isolated early SMBHs | NULL — required seed Δ²_ζ ≈ 0.012–0.014 is ~1.8×10³ × over COBE/FIRAS μ; the lab's own spectrum is 7 dex below the seed requirement | row 6 status cell, 2026-09-03 (via A3-1b) |
| **hemispherical / large-angle asymmetry** | **no data-side test yet** — the *theory* route (Erickcek–Kamionkowski–Carroll modulation) was killed at \|f_NL\| = 2.19 (EKC needs ~10²), but the *measurement* was never made | this document |

The first brief closed the asymmetry class on the theory side only ("the temperature-dipole
route is dead"). That is not a current-data verdict on the anomaly itself. The open
question that matters to route 3 is empirical and answerable today with data already on
this disk:

> **Is the Planck dipolar power modulation a genuine, scale-independent primordial
> modulation of the initial conditions — in which case an independent tracer of the same
> initial conditions, at a different epoch and different scales, must show it along the
> same axis — or is it CMB-specific?**

If it *is* primordial and shared, it strains single-field inflation and becomes a real
target for bounce-scale physics. If an independent tracer bounds it below the CMB value on
the same axis, the anomaly cannot be cited as evidence for bounce-scale initial conditions,
and row 6's third class is closed *by data* rather than deferred.

The abundance channel of the first test is not repeated here; this is a different
observable, a different dataset, and a different failure mode.

## 1. Data (already local — nothing is downloaded)

DESI DR1 LSS clustering catalogues, QSO tracer, at
`~/Desktop/CODE_YOU/bigbounce_datasets/desi_dr1_lss/` (the same products used for ledger
row 4, `research/desi_png_reproduction/`; SHA-256 of the official spectra in
`research/desi_png_reproduction/official_products_sha256.txt`).

- Data: `QSO_NGC_clustering.dat.fits`, `QSO_SGC_clustering.dat.fits`.
- Randoms: files **0–3** per cap (`QSO_{cap}_{0..3}_clustering.ran.fits`). Randoms define
  the angular+radial selection function; four files per cap give ≳ 20× the data density,
  so random shot noise is subdominant by construction.
- Redshift cut **0.8 < z < 2.1** (the official DR1 QSO clustering range).
  Sample sizes fixed in advance from the catalogue headers: **N = 555,913 (NGC) +
  300,918 (SGC) = 856,831** quasars.
- Weights: the catalogue's `WEIGHT` column (completeness × imaging-systematics ×
  redshift-failure × radial). **FKP weights are NOT applied** — this is an angular-
  modulation test, not a P(k) measurement.

## 2. Maps

HEALPix `nside = 64` (pixel area 0.8393 deg²), RING, built in equatorial coordinates and
rotated to Galactic for all axis work. Per pixel *i*:

- `D_i` = Σ_data w, `Q_i` = Σ_data w², `R_i` = Σ_randoms w, `n_i` = raw data count.
- Mask: keep pixel if `R_i ≥ 0.5 × median(R_j over all pixels with R_j > 0)`
  (drops partially-covered edge pixels). Robustness variant: 0.8 × median.
- Overdensity `δ_i = D_i / (α_c R_i) − 1`, with `α_c = Σ_mask D / Σ_mask R` computed
  **per cap** (primary; this removes the known NGC/SGC mean-density offset by
  construction and is the conservative choice). Joint-α is a reported variant.
- Per-pixel shot-noise variance of the weighted count: `s_i = Q_i / (α_c R_i)²`.

## 3. Statistics (both fixed in advance)

**S1 — number-count dipole.** Weighted least squares of
`δ_i = m_c + d·n̂_i` over masked pixels (`m_c` = per-cap monopole nuisance, `d` = one
shared 3-vector), pixel weights `W_i = 1/(s_i + σ²_c)` with the excess ("cosmic") variance
`σ²_c` set per cap by requiring χ²/dof = 1. Reported: `|d|` and the projection
`d·p̂` on the Planck axis.
*Role:* primarily a **systematics diagnostic** (a true primordial power modulation does not
produce a mean-density dipole; residual imaging systematics do), secondarily a bound on a
super-horizon density gradient. The kinematic expectation for a quasar sample,
`D_kin = [2 + x(1+α_ν)]β ≈ 0.005`, is stated in advance as far below the expected
sensitivity of a 7,000 deg² footprint.

**S2 — dipolar modulation of the degree-scale clustering amplitude (the CMB analogue).**
For masked pixels form `e_i = δ_i² − s_i`, whose expectation is the local clustering
variance. Fit

&nbsp;&nbsp;&nbsp;&nbsp;`⟨e_i⟩ = σ²_c,cap · (1 + 2A · n̂_i·p̂)`

for one shared modulation amplitude `A` and per-cap `σ²_c`, by weighted least squares with
`W_i = 1/[2(σ̂²_c + s_i)²]`. This mirrors the CMB observable
`Δ²(k, n̂) = Δ²(k)[1 + 2A n̂·p̂]`, for which Planck 2018 VII (arXiv:1906.02552) reports
**A ≈ 0.07 at ℓ ≲ 60 toward (l, b) = (209°, −15°)**, ~3σ before look-elsewhere correction.
`p̂` = that axis. **S2 is the primary statistic.**

Geometric leverage is declared in advance as a reported quantity: `L = rms(n̂_i·p̂)` over
the mask, weighted by `W_i`. A small `L` means the footprint has little hemispheric
leverage on this axis and the resulting bound is weak — that is an outcome, not a failure.

## 4. Nulls

**N1 — Poisson / selection null (no clustering).** 500 realisations in which each pixel's
weighted data count is redrawn as `D_i^sim = (Q_i/α_cR_i) · Poisson(λ_i)`,
`λ_i = (α_cR_i)²/Q_i` (moment-matched: mean `α_cR_i`, variance `Q_i`). Tests "is the
statistic larger than shot noise through the actual selection function?".

**N2 — random-axis null (look-elsewhere).** S1 and S2 recomputed for the 3,072 directions
of an `nside = 16` HEALPix grid, keeping only axes for which each hemisphere holds ≥ 20% of
the masked pixel weight. `p_LEE` = fraction of admissible axes whose statistic is at least
as extreme as the Planck axis's. This is self-calibrating: it measures whether the
CMB-flagged axis is special *relative to this sky's own axis-to-axis scatter*, which
already contains cosmic variance and residual systematics.

**N3 — systematics bracket (stability requirement, not a null).** Recompute S1/S2 with
(a) `WEIGHT_SYS` divided out of the weights, (b) `|b_gal| > 30°`, (c) NGC alone and SGC
alone, (d) mask threshold 0.8 × median, (e) `nside` 32 and 128, (f) joint-α normalisation.

## 5. Decision rule (pre-registered; no post-hoc adjustment)

**DETECTION** of a large-angle anisotropy requires **all** of:

1. `p < 0.01` against the Poisson null N1;
2. `p_LEE < 0.05` against the random-axis null N2 for the Planck axis specifically;
3. sign preserved and amplitude stable within a factor 2 across the entire N3 bracket,
   with NGC and SGC individually consistent within 2σ.

Anything else is reported as a **NULL with a one-sided 95% upper bound** on `|d|` and on
`A`, the bound built from the N1 null width and the fit error added in quadrature.
A statistically significant S1 dipole that fails the N3 stability test is reported as a
**systematics detection**, explicitly not as cosmology.

## 6. What each outcome means for bounce vs single-field inflation (written in advance)

Both single-field slow-roll inflation and the lab's nonsingular matter bounce predict a
statistically isotropic primordial power spectrum. Neither has a mechanism for a
scale-independent dipolar modulation at the observed amplitude: for single-field inflation
the EKC super-horizon-mode route requires `f_NL^loc ~ 10²` (Planck: −0.9 ± 5.1), and the
lab's own matter-contraction value is `f_NL^loc = −35/16 = −2.1875`, which the first ledger-6
brief already showed is ~2 orders of magnitude too small for that route. So:

- **Detection** (`A_QSO ≈ 0.07` on the Planck axis, N3-stable) → the CMB asymmetry is a
  genuine primordial modulation shared by an independent tracer at a different epoch and
  different scales. This **strains single-field inflation** and makes the asymmetry a real
  route-3 anomaly. It does **not** select a bounce: the lab's `f_NL` cannot produce it
  either. It would instead open a specific new derivation — a bounce-scale preferred
  direction or pre-bounce inhomogeneity — as the next ledger item, and that derivation
  would have to predict the amplitude *before* it could be claimed as bounce evidence.
- **Null with the 95% bound below `A_CMB ≈ 0.07`** on the same axis → the CMB modulation
  is **not** a scale-independent primordial modulation of `Δ²_ζ`. It is then either
  strongly scale-dependent (decaying before QSO scales, the direction Hirata 2009's quasar
  bound already pointed), a CMB-specific systematic, or a large-angle fluke. Consequence
  for the lab, stated now: **the hemispherical asymmetry may not be cited as evidence for
  bounce-scale initial conditions**, and row 6's third anomaly class receives a
  current-data verdict instead of a deferral.
- **Null with the bound above 0.07** → sensitivity-limited. Report the bound and the
  geometric leverage `L`, state what sample would reach 0.07, and record the class as
  "measured, not yet constraining".

A null is published as a null. No number in the result document may be anything other than
a literature citation or an output of the committed script.

## 7. Compute and cost

Local CPU only (no GPU, no pod, no network). One pass over ~128 MB of data catalogues and
~8 GB of random catalogues read column-wise with memory mapping. New bytes written to disk:
≲ 20 MB (HEALPix maps + JSON + one figure). Estimated wall clock ≤ 40 min. Cost ≈ $0.
