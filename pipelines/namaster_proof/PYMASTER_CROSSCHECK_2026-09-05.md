# PyMaster (NaMaster) cross-check of the in-house MASTER estimator — 2026-09-05

Closes the open science item from the P1B v2B.0.18 R2 truth-audit
(`project-context/peer-reviews/INT_v3/P1B_v2B.0.18_R2_TRUTH_AUDIT_2026-09-04.md`):
"PyMaster cross-check (wheels resolve — feasible)".

## Install

- Homebrew `pip3 install pymaster` failed: no wheel for macOS/arm64 + Python
  3.14, and the source build (`libnmt`, needs GSL/FFTW/CFITSIO/HEALPix) failed
  at `configure` with "C compiler cannot create executables" under the
  Homebrew Python's PEP-668 externally-managed environment.
- Resolved via **conda-forge through a throwaway micromamba env** (as
  instructed as the fallback path):
  ```
  brew install micromamba
  MAMBA_ROOT_PREFIX=/tmp/mamba_root micromamba create -y -n pymaster_env \
    -c conda-forge python=3.11 namaster numpy scipy healpy
  ```
- Installed: **NaMaster (pymaster) 3.0.1** (`nmt.__version__` reports `3.0`),
  Python 3.11.16, numpy 2.4.6, healpy 1.20.0, on the same Apple-silicon Mac
  used for the rest of the lab (`Houstons-MacBook-Air.local`, macOS 25.5.0
  arm64). Env is throwaway/local-only, not committed.

## Method

Script: `pipelines/namaster_proof/blind_test/pymaster_crosscheck.py`
(sha256 `4c79aeaa43a5b78ead155caa2cc5dabab159ae0cedb076055c20aef1788e8db5`).

Same map, mask, binning, and ell-range fed to both estimators:

- Mask: `pcl.make_mask(nside=64, seed=11)` (galactic cut + 12 patches).
- Sky: `pcl.make_map(nside=64, lmax=95, seed=42)` (power-law Gaussian
  realization, same generator the blind test uses).
- In-house honest path: `pcl.mask_power` → `pcl.coupling_matrix` (full
  spin-0 MASTER matrix, all rows, no bandwidth restriction) → `pcl.decouple`
  (per-multipole linear solve, lmin=2).
- NaMaster: `nmt.NmtField(mask, [sky], spin=0, lmax=95)`,
  `nmt.NmtBin.from_lmax_linear(95, 1, is_Dell=False)` (bin width 1 so bands
  == individual ells over the same 2..95 range), `NmtWorkspace.from_fields`,
  `wsp.get_coupling_matrix()` (raw unbinned M, l=0..95), `wsp.decouple_cell`.
- S6 shortcut: `variants2.run_variant("S6_effective_multipole", ...)` — same
  map/mask/seed, band width 8 — output compared to NaMaster's exact
  decoupled Cl in the same 8-wide bands.

Full numeric result: `pipelines/namaster_proof/blind_test/pymaster_crosscheck_result.json`.

## Results

**(1) Coupling matrix M_ℓℓ′, l = 2..95 (94×94), in-house vs NaMaster raw:**

| metric | value |
|---|---|
| max abs diff | 7.36e-14 |
| max relative diff | 4.25e-13 |
| median relative diff | 6.43e-14 |

Agreement is at floating-point round-off — the in-house formula
`(2l2+1)/(4π) Σ_l3 (2l3+1) W_l3 (l1 l2 l3;000)²` and NaMaster's internal
spin-0 mode-coupling matrix are numerically identical on this map/mask.

**(2) Decoupled bandpowers, same l-range:**

| metric | value |
|---|---|
| max relative diff | 1.54e-12 |
| median relative diff | 1.25e-12 |

Also floating-point-level — the in-house per-multipole linear solve and
NaMaster's `decouple_cell` (nlb=1, so bin windows are delta functions) agree
to machine precision.

**(3) S6 effective-multipole shortcut vs NaMaster exact, per 8-wide band:**

| band (ℓ) | max rel. err | mean rel. err |
|---|---|---|
| 2–9 | 1.177 | 0.618 |
| 10–17 | 0.673 | 0.317 |
| 18–25 | 0.430 | 0.202 |
| 26–33 | 0.609 | 0.183 |
| 34–41 | 0.495 | 0.199 |
| 42–49 | 0.261 | 0.127 |
| 50–57 | 0.380 | 0.169 |
| 58–65 | 0.397 | 0.176 |
| 66–73 | 0.319 | 0.138 |
| 74–81 | 0.284 | 0.115 |
| 82–89 | 0.459 | 0.165 |
| 90–95 | 0.232 | 0.095 |

The shortcut (dividing every multipole in a band by a single scalar transfer
factor evaluated at the band's effective ℓ) is O(10–100%) wrong per-multipole
relative to the NaMaster-verified exact result, worst at low ℓ where the
coupling operator varies fastest across a band, improving (but not
vanishing) toward higher ℓ. It never approaches the honest path's
machine-precision agreement.

## Two sentences the paper may state

1. "We validated our spin-0 MASTER implementation against the public
   NaMaster library (Alonso et al. 2019) on an identical map, mask, and
   ℓ-range: the mode-coupling matrix and decoupled bandpowers agree with
   NaMaster to machine precision (max relative difference ≲5×10⁻¹³ and
   ≲2×10⁻¹², respectively), confirming our estimator is a correct
   implementation of the MASTER formalism NaMaster also implements."
2. "This validates the pointwise MASTER formalism itself, not NaMaster's
   own binned-bandpower or single-field convenience APIs, which this study
   does not exercise; the effective-multipole shortcut characterized in the
   blind test remains an in-house-only diagnostic (S6), quantified here as
   O(10–100%) per-multipole relative to the NaMaster-verified exact
   decoupling rather than against a NaMaster-shortcut equivalent."

## Reproducibility manifest

`reproducibility/manifests/experiments/p1b-pymaster-crosscheck-2026-09-05.json`
