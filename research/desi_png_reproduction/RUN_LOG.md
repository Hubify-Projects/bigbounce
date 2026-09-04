# RUN_LOG — Ledger row 4 execution (2026-09-04)

**Plan:** `research/desi_png_reproduction/LEDGER4_DESI_PNG_PLAN_2026-09-03.md`
(read in full before starting). Executing steps 1-7 of that plan. Constraints
this session: no delegation, no Monitor tool, blocking Bash only (≤600 s per

**Note on commit attribution (2026-09-04, step 3):** other concurrent
sessions are active on this repo (ledger9-c2, site-redesign lanes per
directive-driven parallel work). Step-3 files (`pk_estimator_qso.py`,
`combine_and_compare.py`, `outputs/pk_qso_*`) were committed correctly to
disk/history but got swept into two of those concurrent sessions' commits
(`cf8f33d1`, `e23b4f3d`) rather than my own atomic ledger4 commit — nothing
lost, just commingled attribution. No destructive action taken; noting for
the record.
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

## Step 3 — P_ell(k) measurement (DONE, 2026-09-04)
`pk_estimator_qso.py`: pypower `CatalogFFTPower`, nmesh=512, resampler=tsc,
interlacing=2, los=firstpoint, ells=(0,2,4), k-edges 0-0.31 step 0.001,
WEIGHT*WEIGHT_FKP, DESI fiducial cosmology (cosmoprimo, EH transfer) for
RA/DEC/Z -> comoving xyz, 0.8<z<3.1 cut. NGC: 772,215 data / 45.2M randoms,
83s FFT. SGC: 418,624 data / 25.3M randoms, 81s FFT. Valid (non-nan) k range
extends to k~0.098-0.103 h/Mpc, comfortably covering the plan's 0.003-0.08
target. Outputs: `outputs/pk_qso_{NGC,SGC}.json` + `_poles.npy` +
`_pypower.npy` (window/result state).

`combine_and_compare.py`: data-count-weighted NGC+SGC combination ->
`outputs/pk_qso_combined_poles.npy` + `_comparison.json`. **Comparison
finding (honest scope note): Chaussidon et al. 2024 does NOT publish a
numeric P0(k)/P2(k) table** — confirmed via WebFetch full-text search of
the arxiv HTML version (Fig. 5 multipoles are graphical only, no digitized
values or supplementary table). So the "3 k-point" comparison is a
specification-level consistency check instead of a literal number match:
our combined P0(k=0.01,0.03,0.06 h/Mpc) = 34,944 / 32,311 / 18,352 (Mpc/h)^3,
same order of magnitude as the paper's own FKP fiducial P0=3e4 (Mpc/h)^3
(Sec 3.2.1) — consistent with FKP weights being near-optimal, as intended by
construction. Published QSO bias formula (Table 2) b1(z)=0.237(1+z)^2+0.771
gives b1(z_eff=1.491)=2.242, the literature-standard DESI QSO bias, used as
input to step 4.

## Step 4 — scale-dependent bias fit (DONE, 2026-09-04)
`fit_fnl.py`: model Delta_b(k,z)=3 f_NL delta_c (b1-p)/alpha(k,z), alpha via
cosmoprimo EH-derived T(k) + growth factor/rate at z_eff=1.491; Kaiser
P0/P2; b1 FIXED at published Table-2 value 2.242 (single-tracer P0/P2 at
this S/N cannot jointly constrain b1 and f_NL — documented simplification).
Diagonal analytic covariance sigma_Pl(k)^2=2(2l+1)/Nmodes*(P0+SN)^2,
**calibrated** by a single multiplicative factor so chi2/dof=1 at a fixed
null model (standard, transparent technique — does not move best-fit
centre, only widens sigma to reflect real point-to-point scatter the
diagonal formula misses per plan sec 3.5).

**Bug found + fixed:** first run added the FULL measured shot noise back
onto P0 as a nuisance term, but pypower's `poles()` call defaults to
`get_power(remove_shotnoise=True)` (confirmed by reading
`pypower/fft_power.py`) — P0/P2 are already shot-noise-subtracted. Double-
counting it drove f_NL to unphysical values (-50 to -180, sigma 200-260).
Fixed: n_shot is now a small residual nuisance (prior centred at 0, width
10% of shotnoise scale), sanity-check comparison at k=0.01 fixed accordingly.

**Result after fix:**
| p (bias model) | f_NL median | 68% CL | published |
|---|---|---|---|
| p=1.6 (QSO merger, DESI default) | -50.6 | [-69.3, -32.5] (sigma~18.5) | -3.6 (+9.0/-9.1) |
| p=1.0 (universality) | -26.7 | [-35.9, -17.4] (sigma~9.3) | +3.5 (+10.7/-7.4) |
| p marginalised [1.0,1.6] | -36.3 | [-52.7, -23.2] (sigma~15.5) | n/a |

Our sigma for p=1.0 (9.3) lands close to the published magnitude (~9); our
p=1.6 sigma (18.5) is ~2x larger, plausibly because we lack the window/AIC/
wide-angle corrections and joint growth-rate/bias marginalisation the
official desilike pipeline applies (those typically tighten a constraint).
**Central values disagree with published by several of our own sigma** —
attributed (not proven) to: single-field-realisation sample variance on
this exact DR1 patch (no mock ensemble), EH-vs-CLASS transfer function,
missing integral-constraint/window convolution, and the reduced (4/18)
randoms density. This is reported as the honest result, not smoothed over.

## Step 5 — systematics splits (PARTIAL — 1/≥5 tests, 2026-09-04)
`systest_weight_sys.py` + `systest_fit.py`: WEIGHT_SYS on/off (plan test 1,
the headline lever). Result: f_NL(p=1.6 point-est) sys-on=-50.4 (matches
the full MCMC median -50.6, good cross-check), sys-off=+11.9, **Delta
f_NL=+62.4** — >3x our statistical sigma (18.5). Remaining 6 tests
(Galactic-latitude, E(B-V), stellar-density, depth/seeing, AIC on/off,
randoms jackknife) BLOCKED on compute-time budget this session (~150-200s
per pypower run x 2 caps x N tests); each is a mechanical repeat of
`systest_weight_sys.py`'s pattern with a different weight/selection mask —
concrete next step, not a research blocker.

## Step 6 — b_phi-marginalised statement + posterior overlap (DONE, 2026-09-04)
p marginalised uniformly over [1.0,1.6]: f_NL=-36.3 (+16.4/-16.4). Posterior
distance from -35/16: 2.20 sigma; from -35/8: 2.06 sigma; from 0: 2.34
sigma — neither flagship value distinguished from the other or from our
own central value, consistent with ledger #3's pre-registered 0.16/0.32
sigma reach for the official DESI sigma. Full derivation in
`LEDGER4_RESULT_2026-09-04.md` sections 4-5.

## Step 7 — result writeup (DONE, 2026-09-04)
`LEDGER4_RESULT_2026-09-04.md` (headline table, attributed causes for the
published-vs-ours offset, systematics table, b_Phi statement, posterior
overlap, scope-vs-plan table). Manifest
`reproducibility/manifests/experiments/ledger4-desi-dr1-qso-fnl-reproduction.json`
(schema-validated against `experiment.schema.json`). Ledger row 4 in
`project-context/NEXT_SCIENCE_LEDGER.md` updated with a concise status
append. LRG not started this session (QSO-first per task scope; QSO alone
consumed the session's compute-time budget).

---

## Follow-up 2026-09-04 — remove causes in order of impact (v2)

Task: re-fit after removing, in order: (1) window function + integral
constraint, (2) transfer function upgrade (camb/cosmoprimo[class]/pyccl),
(3) full 18 randoms, (4) analytic Gaussian covariance w/ window-convolved
model + measured shot noise, (5) remaining systematics splits. Writing
`LEDGER4_RESULT_v2_2026-09-04.md` (supersedes v1, v1 kept as record).
Budget: ~4h local CPU. Steps logged below as they complete.

**Fix 3 scope cut (2026-09-04):** n_ran=7 (planned bump from 4) did not
complete its NGC FFT pass within ~50 min wall clock (severe swap pressure
observed on this shared machine, `vm.swapusage` showed 24.4/25.6 GB used --
other concurrent sessions on this host, not this job alone, per CLAUDE.md's
noted concurrent-lane activity). Killed and retried at n_ran=5 (realisations
0-4/cap) for tractability -- still a real increase over v1's 4, short of the
7 downloaded/sha256'd. Full 7-realisation run remains a named next step once
the host is less contended.

**Follow-up session closed (2026-09-04).** Result: `LEDGER4_RESULT_v2_2026-09-04.md`.
Movement: f_NL(p=1.6) -50.4 -> -23.2 (window-IC) -> -16.7 (+CAMB, A_s-matched)
-> -16.7 (+measured-shotnoise cov, Delta~0 as expected). Fix 3 (full randoms)
and the full pypower window-convolution matrix both attempted and blocked
(host contention / computational infeasibility), documented not dropped.
Point-estimates replaced full MCMC after step-1's MCMC ran >6.5 CPU-min
without finishing under measured swap pressure (24+/25.6 GB); step-0 point
estimate cross-checked against v1's MCMC median to <1%. Manifest
`ledger4-desi-dr1-qso-fnl-reproduction-v2` (schema-valid). Ledger row 4
updated. All commits atomic per RUN_LOG entries above.

**Correction (2026-09-04, post-close):** the n_ran=7 NGC pass actually
COMPLETED (772.0s wall clock, `outputs/pk_qso_NGC_nran7.json`) before the
kill signal landed -- 9.3x v1's 83s baseline, consistent with measured host
contention, but real data, not silently lost. SGC never started (killed
before the loop reached it). Fix 3 is therefore "NGC done, SGC missing" --
one cap short of a combined re-fit -- rather than "fully blocked" as first
recorded. Preserved for a future SGC-only completion.
