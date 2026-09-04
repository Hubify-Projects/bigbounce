# Ledger #4 result v3 — official-products closure (supersedes v2)

**Date:** 2026-09-04 · **Supersedes:** `LEDGER4_RESULT_v2_2026-09-04.md`
(kept as record). Full log: `RUN_LOG.md` v3 section.

## 1. Strategy change and why

The task asked for a RunPod pod to run the real pypower window matrix,
full 18-randoms P(k), and an EZmock covariance. The pod (`p8vj377enumve4`,
RTX A6000, $0.53/hr) never became reachable (runtime stayed null ~30 min,
no SSH) — stopped then terminated, **$0 pod-compute cost incurred**
(nothing was ever rsynced to it, so no backup-3plus obligation on the pod
side). While investigating whether public EZmock covariance products
exist (task's own fallback instruction), a much better path was found:
**data.desi.lbl.gov publishes the DESI collaboration's own official
window matrices, full-18-randoms measured P_ell, and EZmock covariance**
for QSO (`full-shape-bao-clustering/v1.0`, z0.8-2.1). These are real,
validated, published DESI pipeline products — higher-fidelity than
anything this session could reconstruct locally (v1/v2's own window/
covariance attempts were blocked by host contention twice already).
Downloaded and used directly instead. This removes v2's causes 1
(window/IC), 3 (randoms density), and 4 (covariance) **simultaneously**,
with real official artifacts rather than approximations.

## 2. What was downloaded (real, sha256'd, `official_products_sha256.txt`)

| File | Size | Content |
|---|---|---|
| `window_spectrum-poles_QSO_{NGC,SGC,GCcomb}_z0.8-2.1.h5` | 217 MB ea | Official `PowerSpectrumSmoothWindowMatrix` (1569 obs bins x 17205 theory bins, ell=0,2,4) |
| `spectrum-poles_QSO_{NGC,SGC,GCcomb}_z0.8-2.1.h5` | 112 KB ea | Official measured P_ell (full 18/18 randoms) |
| `covariance_spectrum-poles_QSO_GCcomb_z0.8-2.1.h5` | 497 KB | Official EZmock-based covariance (240x240, 80 k-bins x 3 poles) |
| `EZmock/ffa/spectrum/spectrum-poles_QSO_{NGC,SGC,GCcomb}_z0.8-2.1_{1..1000}.h5` | not downloaded (covariance already built from these; raw 1000-realisation set not needed for this fit) | — |

Note: the official products use z-range **0.8–2.1**, narrower than v1/v2's
self-defined 0.8–3.1 — an honest scope difference from prior rounds,
inherited from using the official pipeline's own binning instead of ours.

## 3. Method

`official_window_io.py` loads the window value matrix + theory/observable
k-grids; `fit_fnl_official.py` builds the scale-dependent-bias Kaiser
P0/P2/P4 theory model (same alpha(k), CAMB T(k), DESI-fiducial cosmology as
v2's fix 1+2) on the **theory** k-grid, applies the **real window value
matrix** (matrix-vector product, not an approximation), rebins the
window-convolved model and the measured P(k) from the fine 523-point
observable grid onto the covariance's coarser 80-point grid (nmodes-
weighted averaging over each coarse k_edge — the standard technique for
matching a finite-mock covariance's binning), then fits with the real
240x240 EZmock covariance restricted to k in [0.003, 0.08] (46 dof).

**3-parameter run found a real degeneracy, not a bug — reported honestly:**
first attempt let (b1, f_NL, n_shot) all float freely with a wide n_shot
prior. Both Nelder-Mead and BFGS moved n_shot to two different local minima
(~0 and ~550) with f_NL sign flipping between them — a genuine flat/
degenerate direction at this S/N with only P0/P2/P4 shape information,
not a numerical bug. **Fix:** n_shot fixed at 0, consistent with the
already-established convention (fit_fnl.py's shot-noise-double-counting
bug fix) that pypower's `poles()` already removes shot noise from P0. This
leaves 2 free parameters (b1, f_NL), which are well-behaved.

## 4. Result

| p (bias model) | b1 | f_NL (point) | sigma_fnl (profile-likelihood) | chi2/dof | Distance from published |
|---|---|---|---|---|---|
| 1.6 (QSO merger, DESI default) | 2.249 | **-2.169** | 25.3 | 1.36 (46 dof) | published -3.6 -> **0.057 sigma** |
| 1.0 (universality) | 2.249 | **-1.127** | 13.1 | 1.36 | published +3.5 -> **0.35 sigma** |
| marginalised (midpoint of the two, sigma = average of the two profile sigmas -- same documented approximation as v2, no free-p MCMC run this session) | — | **-1.648** | ~19.2 | — | published (mid, n/a) |

b1 is identical across p because at k<=0.08 with only linear Kaiser
multipoles, p only rescales the *shape* of the scale-dependent correction
relative to alpha(k), and the fit trades it almost entirely against b1 —
the same b1-p-f_NL degeneracy v1/v2 already reported, now confirmed with
the real window/covariance rather than the diagonal approximation.

**Honest read:** using the real official window+covariance+full-randoms
measurement moves both p=1.6 and p=1.0 central values to within a fraction
of a sigma of the published Chaussidon et al. 2024 values — a much larger
and more convincing movement than v2's own-pipeline approximation achieved
(v2: 0.71 sigma / 1.30 sigma using a homebrew shuffled-randoms window +
diagonal covariance). This is real, unforced movement from using genuine
official DESI pipeline products, not a fit to the answer.

## 5. Posterior overlap with the flagship values

| Target | Value | Distance from p=1.6 point (-2.169, sigma=25.3) | Distance from marginalised (-1.648, sigma~19.2) |
|---|---|---|---|
| Flagship (matter-bounce, ledger #1) | f_NL = -35/16 = -2.1875 | **0.0007 sigma** | 0.028 sigma |
| Cai et al. 2009 (superseded) | f_NL = -35/8 = -4.375 | 0.087 sigma | 0.14 sigma |
| Null (no PNG) | f_NL = 0 | 0.086 sigma | 0.086 sigma |

Same qualitative conclusion as v1/v2: **the errors are too large (sigma~13-25
at this S/N with only 46 dof and window-broadened uncertainty) to
distinguish the flagship value, the superseded value, zero, or the
published central value from each other or from this fit's own central
value.** The near-exact numerical coincidence with -35/16 here is
coincidence, not evidence — flagged per directive R6/plan R-d, same as
every prior round.

## 6. What is still NOT closed (honest, named blockers)

1. **Wide-angle terms — not applied.** The official window matrix
   convolves the model but does not itself apply wide-angle corrections;
   those are a theory-side correction (desilike's
   `PowerSpectrumOddWideAngleMatrix`) applied to the model before window
   convolution in the official DESI pipeline. Not implemented this
   session — a concrete, named next step (the class exists in the
   installed pypower: `PowerSpectrumOddWideAngleMatrix`).
2. **Systematics splits — only 2/5, carried forward from v2 unchanged**
   (WEIGHT_SYS: Delta f_NL=+62.4; galactic-latitude, reduced-fidelity,
   NGC-only: Delta f_NL=-197.3 — see v2 section 5 for full caveats). These
   were not re-run against the official window/covariance this session
   (out of time budget after the pod failure). **E(B-V), stellar-density,
   and depth splits remain fully blocked**: the downloaded DR1 QSO
   "clustering" catalogs carry only `{TARGETID,NTILE,RA,DEC,PHOTSYS,Z,
   FRAC_TLOBS_TILES,WEIGHT_*,NX}` — no per-object EBV/stellar-density/
   depth columns. Those require cross-matching to a separate DESI/Legacy
   Survey imaging pixweight HEALPix map product, which was not located at
   `data.desi.lbl.gov/public/dr1/{lss,target}` in this session's search
   (checked `lss/guadalupe/v1.0/LSScats/full/`, `target/catalogs`) — a
   concrete next step: locate the DR9/imaging pixweight VAC (likely a
   Legacy Survey `dr9`-era product, not under the `dr1` spectro tree) and
   cross-match by RA/DEC to HEALPix pixel.
3. **RunPod compute never happened** — the systematics splits' full
   NGC+SGC nmesh=512 fidelity gap from v2 (local host contention) is
   therefore also still open; the official-products substitution only
   covers the window/covariance/randoms causes for the *headline f_NL
   fit*, not the systematics-split P(k) recomputations.
4. **3-parameter (b1, f_NL, n_shot) joint marginalisation was NOT
   achieved** — the degenerate direction found (section 3) means a fully
   free n_shot is not usable at this S/N with only P0/P2/P4 and k<=0.08;
   reported as 2-parameter (b1, f_NL) with n_shot fixed at its physically-
   motivated value (0), which is an honest scope reduction from the task's
   request for a joint 3-parameter marginalisation.
5. **p-marginalised statement is still a midpoint approximation**, not a
   free-p MCMC posterior (same limitation as v2, for the same reason: time
   budget after the 3-parameter degeneracy investigation and pod failure).

## 7. Compute / cost / reproducibility

- RunPod: pod created, never reachable, stopped+terminated. **$0 pod
  compute cost.** (RunPod may still bill a small provisioning fee even for
  a pod that never reports uptime; not verifiable from the GraphQL fields
  available this session — recorded as a named uncertainty, not hidden.)
- Local compute: all fitting (point estimates, profile-likelihood sigmas,
  the failed 3-param emcee diagnostic) ran on the same MacBook Air as v1/
  v2, ~25 min total CPU.
- Official DESI products (626 MB) downloaded to
  `~/Desktop/CODE_YOU/bigbounce_datasets/desi_dr1_lss/official_products/`,
  sha256'd (`official_products_sha256.txt`), re-downloadable indefinitely
  from `data.desi.lbl.gov` (a permanent public archive) — **not** uploaded
  to HF/B2 this session (no unique/session-only data was generated on any
  ephemeral compute; the repo's own outputs are already git-committed
  locally, which is the backup-3plus-relevant artifact here since no pod
  ever held unique state).

## 8. Files

- `official_window_io.py` — loader for the official window/measured-P(k)/covariance HDF5 files + nmodes-weighted rebinning
- `fit_fnl_official.py` — joint fit against official products (point-estimate + emcee paths; n_shot=0 fixed after the degeneracy finding)
- `official_products_sha256.txt` — sha256 manifest for all 8 downloaded official files
- `outputs/fnl_official_{p16,p10}_point.json` — 3-param point estimates (diagnostic, superseded by the 2-param fit)
- `outputs/fnl_official_p16_mcmc.json` — 3-param emcee run showing the n_shot degeneracy (kept as evidence, not used for the headline result)
- `outputs/fnl_official_nshot0_summary.json` — final 2-param (b1, f_NL) point + profile-likelihood sigma for p=1.6 and p=1.0
