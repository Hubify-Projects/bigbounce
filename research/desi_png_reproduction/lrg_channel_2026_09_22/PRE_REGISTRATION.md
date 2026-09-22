# Ledger row 4 — LRG channel: PRE-REGISTRATION

**Lane:** `LS11-row4-lrg` · **Date:** 2026-09-22 · **Committed BEFORE any
statistic was computed.** Nothing below was chosen after seeing an f_NL value.

## 0. Why this lane exists

Ledger row 4 (an independent f_NL^loc measurement from DESI DR1 public
clustering) has carried "**LRG channel NOT STARTED**" through five result
versions (v1–v5, 2026-09-04). The stated blocker was data volume against a
~10 GB free disk: ≈64 GB of LRG+QSO clustering catalogues and randoms.

Lane `bb-LS10-indomain-d180` removed that blocker on 2026-09-22 by
demonstrating HTTP-range streaming with zero image bytes written to disk
(`pipelines/p4prime_chirality_test/row16_indomain_d180_2026_09_22/run_indomain_rotations.py`).
This lane reuses the pattern for FITS binary tables and remote HDF5
(`http_stream.py`, committed with this pre-registration): sequential range
reads, columns extracted in memory, bytes dropped. No bulk catalogue is
written to disk.

**Correction to the lane brief:** the brief states
`research/desi_png_reproduction/official_products/` is EMPTY (0 B) on this
machine. That repo-internal directory *is* empty, but it was never the
product location: `official_window_io.py` points at
`/Users/houstongolden/Desktop/CODE_YOU/bigbounce_datasets/desi_dr1_lss/official_products`,
which is intact (9 QSO files, 1.27 GB, sha256s in
`../official_products_sha256.txt`). No LRG official product exists there —
every LRG input below is streamed fresh regardless, and every stream is
sha256-recorded in the manifest.

## 1. Objective

Open the LRG channel at **exactly the fidelity v5 established for QSO**, so
the two channels are directly comparable on one convention, and state
whether they agree or tension. **A null or an inconclusive channel is a
publishable outcome and will be reported at exactly its evidential
strength.**

## 2. Inputs (all streamed; nothing assumed cached)

**Official DESI DR1 full-shape-bao-clustering VAC v1.0** (`data/`), read
remotely with `h5py` over `http_stream.RangeFile` — zero bytes on disk:

| Product | Path under `.../v1.0/data/` |
|---|---|
| measured P_ell | `spectrum/spectrum-poles_LRG_{NGC,SGC,GCcomb}_z{ZB}.h5` |
| window matrix | `spectrum/window_spectrum-poles_LRG_GCcomb_z{ZB}.h5` (216.7 MB each) |
| EZmock covariance | `covariance/EZmock/covariance_spectrum-poles_LRG_GCcomb_z{ZB}.h5` |

with `ZB ∈ {0.4-0.6, 0.6-0.8, 0.8-1.1}`. These are the exact LRG analogues
of the six QSO files v3–v5 used. `zeff` read from the file attribute:
**0.50963, 0.70580, 0.91859** (verified 2026-09-22 before pre-registration;
reading a file attribute is not a statistic). `_thetacut0.05` and
`-rotated` variants are NOT used — v5 used the untreated QSO products.

**Clustering catalogues** (`dr1/survey/catalogs/dr1/LSS/iron/LSScats/v1.5/`,
the same version v5 used for QSO), streamed by range read:
`LRG_{NGC,SGC}_clustering.dat.fits` (1,476,135 + 662,492 rows) and
`LRG_{NGC,SGC}_{0,1,2,3}_clustering.ran.fits` (9,389,588 / 4,959,721 rows
each). Columns kept: `RA, DEC, Z, WEIGHT, WEIGHT_SYS, WEIGHT_FKP`. Total
catalogue bytes on the wire ≈ 6.2 GB; **peak disk from catalogues = 0**.

**Imaging properties:** `imaging_pixweight/pixweight-dark.fits` (local,
104 MB, already sha256-bound from v4), nside=256 nested, `EBV`, `STARDENS`,
`GALDEPTH_Z` — identical to `imaging_splits_crossmatch.py`.

A **small derived cache** (float32, only the ten needed columns) is written
outside the repo to `bigbounce_datasets/desi_dr1_lss/lrg_stream_cache/` so
the 60 P(k) measurements do not re-stream 6.2 GB each. Its size is reported
as peak disk. It is a derived column cache, not a catalogue.

## 3. Headline fit — frozen before running

Identical machinery to `fit_fnl_official.py` (v3) / `fit_fnl_splits.py` (v4/v5):

- Model: b(k) = b1 + 3 f_NL δ_c (b1 − p) / α(k), δ_c = 1.686;
  P_0 = (b² + 2/3 b f + f²/5) P_lin, P_2 = (4/3 b f + 4/7 f²) P_lin,
  P_4 = 8/35 f² P_lin. **n_shot fixed = 0** (v3's documented 3-parameter
  degeneracy finding), b1 free.
- α(k) and P_lin from `fit_fnl_v2.get_cosmo_funcs("camb")` — CAMB transfer,
  A_s-matched, DESI fiducial background/growth (cosmoprimo `DESI`,
  eisenstein_hu engine) — **re-parameterised in z_eff only**. The
  z-parameterised function is asserted to reproduce
  `get_cosmo_funcs("camb")` bit-for-bit at z_eff = 1.491 (QSO) before any
  LRG fit is accepted; if that assertion fails the lane reports BLOCKED
  rather than a number.
- Data vector: official measured P_ell rebinned (nmodes-weighted) onto the
  official covariance's coarse grid; model = official window matrix applied
  to the theory vector, then rebinned the same way.
- Range: **KMIN = 0.003, KMAX = 0.08 h/Mpc**, ell = 0, 2, 4 — as v3–v5.
- Uncertainty: **profile likelihood**, Δχ² = 1, same 121-point scan as
  `fit_fnl_splits.fit_split`.
- **p (bias response):** headline **p = 1.0** (universality; the DESI/
  Chaussidon+2024 default for LRG), alternate **p = 1.6** reported as well
  so both QSO rows have a matched LRG row, plus the p-marginalised midpoint
  — exactly the three-row presentation v3/v5 used for QSO.
- **Three z-bins are fitted separately, then combined** by summing the three
  χ²(f_NL) profile curves with **one shared f_NL and an independent b1 per
  bin**. *Disclosed approximation:* no cross-bin official covariance exists,
  so the bins are treated as independent. This is the same class of
  disclosed approximation as v4/v5's split covariance reuse and is stated
  wherever the combined number appears.

## 4. Systematics table — the same five rows, frozen before running

Measured with `pypower.CatalogFFTPower` at **identical settings to v5**:
`nmesh=256`, `N_RAN=4`, `ells=(0,2,4)`, `edges=np.arange(0,0.31,0.001)`,
`los="firstpoint"`, `resampler="tsc"`, `interlacing=2`, `dtype="f8"`;
NGC+SGC combined by n_data-weighted mean before rebinning; fitted by
`fit_fnl_splits.fit_split`'s machinery unchanged.

| Row | Split definition (fixed now) |
|---|---|
| E(B−V) | median of the DATA catalogue, applied identically to data+randoms |
| Stellar density | median, same rule |
| Galactic depth (z) | median, same rule |
| **WEIGHT_SYS on/off** | "high" = full `WEIGHT`; "low" = `WEIGHT / WEIGHT_SYS` |
| **Galactic latitude** | "high" = \|b\| > 40°; "low" = \|b\| ≤ 40° |

Medians are computed on the LRG data catalogue (per z-bin) — **not** copied
from the QSO run.

**√2 covariance-reuse correction, disclosed identically to v5:** no
split-specific official covariance exists, so the full-sample covariance is
reused for each ~50 % half; this under-estimates σ_Δ by roughly √2. Both the
raw and √2-corrected Δ/σ are tabulated, as in v5's table.

## 5. Decision rules — fixed before any number is seen

**Systematics verdicts** (on the √2-corrected \|Δ/σ\|):
- ≥ 2 → **FLAGS** (a real sensitivity; reported as the measurement's largest
  budget item, never explained away).
- 1 ≤ \|Δ/σ\| < 2 → **MARGINAL WATCH ITEM** (flagged, not dispositioned as a
  null) — the same language v5 used for QSO Galactic latitude.
- < 1 → **no detectable sensitivity at this fidelity**.

**LRG-vs-QSO comparison**, at matched p, with
T = (f_LRG − f_QSO) / sqrt(σ_LRG² + σ_QSO²):
- \|T\| < 2 → **AGREE**; 2 ≤ \|T\| < 3 → **MILD TENSION**; ≥ 3 → **TENSION**.
- The two channels are treated as **independent** (different tracers, mostly
  non-overlapping volume). Any shared-volume correlation is NOT modelled;
  this is disclosed and makes T conservative in the direction of finding
  tension where there may be none.

**Discrimination statement:** the posterior distance from the flagship
−35/16 and from the superseded −35/8 will be quoted in units of the LRG σ,
whatever it comes out to. Ledger rows 3 and 4 already record that this
measurement's reach (≈0.16–0.32σ separation) cannot discriminate them; if
the LRG σ does not change that, it is stated plainly as "still not
discriminated", not dressed up.

**Nothing is tuned toward the published value.** Chaussidon+2024's
f_NL^loc = −3.6 (+9.0/−9.1) and Brown+2026's −3 ± 12 are comparison targets
recorded here in advance; agreement or disagreement with them is reported as
measured. No fit range, weight, bin, or convention will be changed after
seeing an f_NL value.

## 6. Pre-committed fallbacks (so a shortfall can never masquerade as a result)

1. If an official LRG product is unreachable by streaming, the exact file
   and the exact HTTP failure are named in the result, and that z-bin is
   reported as NOT RUN.
2. If compute overruns the lane budget, the systematics table is run on
   z-bins **in this order: z0.8–1.1, z0.6–0.8, z0.4–0.6** (descending
   volume/constraining power). Any bin not completed is reported as
   **NOT RUN** — never as a null, never omitted.
3. Any subset used in place of a full channel is labelled a subset, with its
   exact object count, in every sentence that quotes a number from it.
4. If the z-parameterised cosmology assertion (§3) fails, the lane reports
   BLOCKED and publishes no f_NL.

## 7. Deliverables

`LEDGER4_LRG_RESULT_2026-09-22.md` (headline + 5-row table + comparison),
`RUN_LOG.md` (this directory), a Q2 reproducibility manifest at
`reproducibility/manifests/experiments/ledger4-desi-dr1-lrg-fnl-channel.json`
(external sources + links, APIs, exact scripts, compute venue, cost, wall
clock, streamed bytes, peak disk), `PROPAGATION_NOTE.md` with exact
printable sentences, and the row-4 status cell of
`project-context/NEXT_SCIENCE_LEDGER.md`. No paper `.tex`, SSOT or site data
is touched by this lane.
