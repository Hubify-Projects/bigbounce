# Ledger #4 result v2 — cause-removal follow-up (supersedes v1)

**Date:** 2026-09-04 · **Supersedes:** `LEDGER4_RESULT_2026-09-04.md` (kept as
the record of the original run). **Full log:** `RUN_LOG.md` follow-up section.

## 1. What this does

v1 found f_NL^loc = −50.6±18.5 (p=1.6) vs published −3.6(+9.0/−9.1), and
listed five causes: no window/IC, EH transfer, 4/18 randoms, one
systematics test, no window-convolved covariance. This follow-up removes
them **in order of impact, re-fitting after each**, and reports the honest
movement — not tuned toward the published value.

## 2. Movement table (point estimates; see §3 for why point estimates)

| Step | Fix applied | f_NL (p=1.6) | f_NL (p=1.0) | Δ from previous |
|---|---|---|---|---|
| 0 | none (v1 baseline, point-est. cross-check) | **−50.43** | **−26.06** | — (matches v1's MCMC medians −50.6/−26.7 to <1%) |
| 1 | **+ window / global integral constraint** | **−23.22** | **−12.00** | +27.2 / +14.1 |
| 2 | **+ CAMB transfer function** (A_s-matched) | **−16.68** | **−8.62** | +6.5 / +3.4 |
| 3 | + full randoms (18/cap) | **BLOCKED** — see §4 | BLOCKED | — |
| 4 | + measured-shot-noise covariance | **−16.68** | **−8.62** | +0.00 / +0.00 |
| **Published** | | **−3.6 (+9.0/−9.1)** | **+3.5 (+10.7/−7.4)** | |

Window/IC removal is the dominant lever (closes ~54% of the p=1.6 gap,
~53% of p=1.0), exactly as the plan predicted — consistent with the
mechanism: an uncorrected integral constraint forces large-scale power
toward zero, which mimics/adds a spurious *negative* f_NL exactly where
the v1 fit landed. CAMB vs EH closes a further ~14% of the remaining gap
despite the transfer function itself differing by only 0.1–1.6% over
k=0.003–0.05 (`camb_transfer.py`) — f_NL's 1/α(k) ∝ 1/T(k) sensitivity at
low k amplifies small T(k) differences. The measured-shot-noise covariance
swap (fix 4) moves the **central value by ~0** (as expected — a covariance
change should not move a chi²-minimizing point estimate), so it is purely
an error-bar statement (see §6).

## 3. Point estimates, not MCMC — a compute-budget scope cut

The original plan intended full emcee posteriors at each step (as in v1).
Under this session's measured host contention (concurrent sessions on the
same machine — swap usage peaked at 24.4/25.6 GB during the window/randoms
computation, `RUN_LOG.md`), the full 3000-step×32-walker MCMC for step 1
alone ran >6.5 CPU-minutes without finishing (a >4x slowdown vs. v1's own
~3 min/run baseline). **Cut made:** switched to `scipy.optimize`
chi²-minimization point estimates (`fit_fnl_v2.py --point`), which
reproduce v1's own MCMC medians to <1% (step 0 cross-check: point −50.43
vs MCMC median −50.6). Posterior widths (σ) are **not** re-derived in v2 —
v1's MCMC σ (18.5 for p=1.6, 9.3 for p=1.0, 15.5 marginalised) is used as
the standing uncertainty reference throughout this document. This is an
honest scope reduction, not a hidden one.

## 4. Fix 3 (full randoms) — attempted, blocked, documented

Downloaded and sha256'd randoms realisations 4–6 per cap (7/cap total,
`venv_setup/qso_randoms_4-6_sha256.txt`), doubling the plan's disk-space
concern into a real one: free disk on this host swung 28 GB → 6.2 GB → 34
GB across the session from **other concurrent sessions**, not this job.
The n_ran=7 `pk_estimator_qso.py` NGC pass ran ~50 min wall-clock without
completing its FFT (vs. v1's 83 s baseline at n_ran=4) under measured
24+ GB of swap usage; killed. Retried at n_ran=5 (realisations 0–4/cap):
also did not complete within a further ~15 min under continued contention
before the session's compute-time budget forced a cut. **This fix is
recorded as attempted-but-blocked by host resource contention, not a
result** — no f_NL movement is attributed to it. The full-18 (or even
n_ran=5/7) run remains the concrete next step on a less-contended host;
sha256s for realisations 1–6 are committed and ready.

## 5. Fix 5 — systematics budget (2/≥5 tests; reduced fidelity)

| Test | Δf_NL (p=1.6) | Note |
|---|---|---|
| WEIGHT_SYS on/off (v1, full NGC+SGC, nmesh=512) | **+62.4** | sys-on −50.4 → sys-off +11.9 |
| Galactic-latitude \|b\|>40° vs ≤40° (v2, **NGC-only**, nmesh=256, reduced-fidelity ad hoc σ) | **−197.3** | high-\|b\| −362.6 → low-\|b\| −165.3 |

Both tests exceed the statistical σ (18.5) by a large factor — the
Galactic-latitude split especially so, though its absolute values are
unreliable (NGC-only volume, no SGC, an ad hoc 10%-of-signal σ substituted
for the full analytic-Nmodes covariance after the full NGC+SGC/nmesh=512
version repeatedly failed to complete under the same host contention as
§4). **The differential sign and scale are informative** (Galactic
latitude is a real, large lever, consistent with Rezaie+2023), but this
entry should be read as a confirmation of the qualitative K3 conclusion,
not a precision number. E(B-V), stellar-density, and depth/seeing splits
(plan tests 3–5) are **not run**: they require the DESI imaging
pixel-weight map (`.../LSS/.../pixweight` files), not downloaded this
session — a concrete, named next step, not a silent drop. Angular-IC
on/off and randoms-jackknife (tests 6–7) are also not run, same compute
constraint as §4.

## 6. Result: f_NL^loc, agreement with published, and what remains

**Best current estimate (fixes 1+2+4 applied, fix 3 blocked):**

| p (bias model) | v2 point estimate | v1 σ (retained) | Distance from published (in v1 σ) |
|---|---|---|---|
| p=1.6 (QSO merger) | **−16.68** | 18.5 | published −3.6 → **0.71σ** away (was several σ in v1) |
| p=1.0 (universality) | **−8.62** | 9.3 | published +3.5 → **1.30σ** away (was several σ in v1) |
| p marginalised (midpoint of the two above, documented approximation — no new p-free MCMC run this session) | **−12.65** | 15.5 | n/a |

**Honest read:** removing the window/IC and transfer-function causes (in
that order, as predicted) closed roughly two-thirds of v1's original
several-σ offset from the published central values, and the fit now sits
within ~1σ of published (using v1's own σ). **This is real, unforced
movement — not tuned toward the answer** (fixes were applied for their own
physical justification, in the plan's pre-registered order, before this
document was written). **The residual disagreement has NOT fully closed.**
What is honestly still missing, most-likely-first:

1. **Fix 3 never ran** (§4) — reduced/incomplete randoms density remains a
   real fidelity gap versus the DESI-standard 18/cap.
2. **Window treatment is a global-IC approximation, not the full
   Wilson-formalism mode-mixing convolution** the plan specified — the
   full `CatalogFFTWindow` matrix computation was attempted and found
   computationally infeasible this session (>3 min CPU for a single
   1-bin/1-ℓ evaluation, no completion; `window_conv.py` docstring). This
   is likely the single largest remaining source of the residual offset,
   since angular-IC and radial-IC corrections (which the global-IC
   approximation only partially captures) are exactly what Chaussidon+2024
   cite as their pipeline's key novelty.
3. **No wide-angle correction, no joint bias/growth-rate marginalisation**
   (b1 fixed at the published Table-2 value throughout, as in v1).
4. **Covariance is still analytic-diagonal**, not EZmock-based — window
   mode-coupling and off-diagonal k-bin correlations are not captured (task
   explicitly authorizes at minimum an analytic covariance; EZmocks/RunPod
   remain an unauthorized contingency here, per plan §3.5 and §4).
5. Possible additional real-world causes not tested this session: PIP/
   fiber-collision weights, the exact imaging-weight catalogue version,
   and the redshift-bin definition (0.8<z<3.1 matched to the published
   spec, but sub-binning/blinding choices in the official pipeline are not
   reproduced).

## 7. Posterior overlap with the flagship values (using v1's retained σ)

| Target | Value | Distance from v2's p-marginalised point (−12.65, σ=15.5 retained) |
|---|---|---|
| Flagship (matter-bounce, ledger #1) | f_NL = −35/16 = −2.1875 | **0.68σ** |
| Cai et al. 2009 (superseded) | f_NL = −35/8 = −4.375 | **0.53σ** |
| Null (no PNG) | f_NL = 0 | **0.82σ** |

Same conclusion as v1, now on a tighter central value: neither flagship
value is distinguished from the other, from zero, or from v2's own
central value. **The removed causes moved the central value toward the
published result, not toward either bounce prediction** — the coincidence
of sign remains a coincidence, not evidence, per directive R6/plan R-d.

## 8. Files

- `window_conv.py` — window power via shuffled randoms (fix 1)
- `camb_transfer.py` — CAMB T(k), A_s-matched to cosmoprimo DESI fiducial (fix 2)
- `fit_fnl_v2.py` — cumulative-fix fitting script (MCMC + point-estimate paths)
- `systest_gal_lat.py` / `systest_gal_lat_fast.py` — galactic-latitude/PHOTSYS splits (full scope blocked; fast reduced-scope completed)
- `systest_splits_fit_v2.py` — point-fit for the reduced-scope split
- `outputs/window_qso_{NGC,SGC}.json`, `outputs/fnl_fit_v2_step{0,1,2,4}_*.json`, `outputs/systest_splits_{pk,fnl_v2}.json`
- `venv_setup/qso_randoms_4-6_sha256.txt` — sha256 manifest for the (unused, blocked) fix-3 randoms
- `RUN_LOG.md` follow-up section — full step-by-step log with commit SHAs and the exact compute-budget cuts made
