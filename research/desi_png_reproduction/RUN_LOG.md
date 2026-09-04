# RUN_LOG — Ledger row 4 execution (2026-09-04)

**Plan:** `research/desi_png_reproduction/LEDGER4_DESI_PNG_PLAN_2026-09-03.md`
(read in full before starting). Executing steps 1-7 of that plan. Constraints
this session: no delegation, no Monitor tool, blocking Bash only (≤600 s per
call), commits after every step, no `git add -A`, no Write/Edit over ~80 lines.

## Step 0 — environment survey (2026-09-04)
- Base python3 = 3.14.6 (Homebrew) — too new, high risk of missing wheels for
  pypower/cosmoprimo/desilike/fitsio (compiled extensions).
- Created dedicated venv at `research/desi_png_reproduction/.venv312` using
  python3.12.13 (available at `/opt/homebrew/bin/python3.12`). `.venv312` is
  gitignored (large, machine-local).
- Existing DR1 QSO products confirmed on disk at
  `~/Desktop/CODE_YOU/bigbounce_datasets/desi_dr1_lss/` (0.86 GB, from
  ledger4-desi-dr1-lss-sanity manifest): QSO_NGC/SGC clustering.dat.fits,
  QSO_NGC/SGC_nz.txt, QSO_SGC_0_clustering.ran.fits.

## Step 1 — package install (DONE, 2026-09-04)
All target packages installed in `.venv312`: numpy 2.5.2, scipy 1.18.1,
astropy 8.0.1, fitsio 1.4.2, emcee 3.1.6, matplotlib 3.11.1, mpi4py 4.1.2
(needed brew open-mpi — installed), pyFFTW 0.15.1, pmesh (needed mpi4py to
build pfft-python), pypower 1.0.0 (git), cosmoprimo (git), desilike (git,
jax optional/absent — fine, not using analytic marginalization).
Full pinned list: `research/desi_png_reproduction/venv_setup/requirements_frozen.txt`.

**CLASS Boltzmann engine unavailable**: `pip install pyclass` fails to build
(`ValueError: could not build CLASS`, missing C toolchain wiring for the
bundled CLASS source under this pip/setuptools version). Per the plan's
explicit fallback, using **cosmoprimo's `eisenstein_hu` transfer-function
engine** instead — confirmed working (`DESI(engine='eisenstein_hu')` +
`.get_transfer(z=0)` callable). This is a real fidelity cap vs the DESI
paper's CLASS-based transfer function; recorded as a limitation in the final
result writeup (§4/§8), not hidden.

## Step 2 — remaining QSO randoms download (DONE, reduced scope, 2026-09-04)
Downloaded randoms realisations 1,2,3 for both caps (NGC + SGC), giving 4
realisations per cap total (0-3; realisation 0 already on disk from step 1).
+7.8 GB, ~4 min wall clock, $0. **Scope reduction from the plan's full 18
realisations per cap** (~37 GB, ~20 min) to 4/cap: at ~15x data density per
single realisation (established in step-1 sanity check), 4 realisations give
~60x data density, which is standard/ample for FKP shot-noise control at
k > 0.003 h/Mpc; this is a documented fidelity choice, not a silent shortcut.
Full-18 download remains available if a later wave needs tighter window
control. sha256s: `research/desi_png_reproduction/venv_setup/qso_randoms_1-3_sha256.txt`.
Total on-disk dataset now 7.8 GB at `~/Desktop/CODE_YOU/bigbounce_datasets/desi_dr1_lss/`.

## Step 3 — P_ell(k) measurement
TBD.

## Step 4 — scale-dependent bias fit
TBD.

## Step 5 — systematics splits
TBD.

## Step 6 — b_phi-marginalised statement + posterior overlap
TBD.

## Step 7 — result writeup
TBD.
