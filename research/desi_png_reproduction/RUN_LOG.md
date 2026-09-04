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

## Step 1 — package install (in progress)
See below for outcome (pypower/cosmoprimo/desilike vs pure-python fallback).

## Step 2 — remaining QSO randoms download
TBD.

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
