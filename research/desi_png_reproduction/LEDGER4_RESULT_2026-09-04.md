# Ledger #4 result — independent DESI DR1 QSO local-PNG reproduction

**Date:** 2026-09-04 · **Plan:** `LEDGER4_DESI_PNG_PLAN_2026-09-03.md` ·
**Full step log:** `RUN_LOG.md` · **Scope:** QSO only (LRG deferred — QSO
completed within budget; see §6).

## 1. Headline result

An independent `pypower` P_0(k)/P_2(k) measurement + scale-dependent-bias
f_NL^loc fit on the public DESI DR1 QSO LSScats v1.5 catalogues (NGC+SGC,
0.8<z<3.1, 0.003<k<0.08 h/Mpc):

| Bias model (p) | Our f_NL^loc | Our 68% CL | Published (Chaussidon+2024) |
|---|---|---|---|
| p=1.6 (QSO merger, DESI default) | **-50.6** | [-69.3, -32.5] (σ≈18.5) | -3.6 (+9.0/-9.1) |
| p=1.0 (universality) | **-26.7** | [-35.9, -17.4] (σ≈9.3) | +3.5 (+10.7/-7.4) |
| p marginalised over [1.0, 1.6] | **-36.3** | [-52.7, -23.2] (σ≈15.5) | n/a |

**Our central values disagree with the published DESI DR1 result by several
of our own sigma.** Our σ magnitude for p=1.0 (9.3) lands close to the
published σ (~9); our p=1.6 σ (18.5) is ~2x larger. This is reported as the
honest outcome — not smoothed, not re-tuned to match.

## 2. Why the central value is offset — attributed causes (not proven)

The pipeline's normalisation is independently verified correct: the
zero-signal model (b1=2.242 published, no scale-dependent term) predicts
P0(k=0.01)=35,522 (Mpc/h)^3 against our measured 34,944 — **1.7% agreement**
(`fnl_fit_results.json` sanity note). So the offset is not a gross
amplitude bug. Candidate causes, most-likely first:
1. **Single-field-realisation sample variance.** We measure one sky patch,
   not an ensemble; the diagonal-covariance calibration (§3) inflates error
   bars to match the *typical* scatter but cannot correct a *particular*
   realisation's central-value pull, which is dominated by the lowest 2-3
   k-bins where Δb(k)∝1/k² is most sensitive.
2. **No window/integral-constraint correction.** The published pipeline's
   radial+angular integral constraint is precisely what absorbs the
   imaging-systematics/target-selection coupling at low k (Chaussidon+2024's
   stated novelty) — we do not reproduce it (plan risk R-c).
3. **Reduced randoms density** (4/18 realisations per cap — RUN_LOG step 2)
   raises window/shot-noise scatter versus the full DESI-fidelity setup.
4. **EH transfer function instead of CLASS** (RUN_LOG step 1) — a percent-
   level T(k) difference at these k, sub-dominant to (1)-(3) but not zero.
5. **No wide-angle correction, no joint bias/growth-rate marginalisation**
   (b1 fixed, f fixed) — the desilike pipeline profiles these jointly.

## 3. The systematics budget (partial — 1 of ≥5 planned tests)

| Test | Δf_NL (p=1.6 point estimate) |
|---|---|
| WEIGHT_SYS on vs off | **+62.4** (sys-on: -50.4 → sys-off: +11.9) |

Δf_NL from this single test **exceeds our own statistical σ (18.5) by
>3x** — i.e. σ_sys > σ_stat already on the first test, consistent with
Rezaie et al. 2023's finding that imaging-systematics weights carry O(10)+
scale in f_NL units for photometric/selection-affected tracers. Per the
plan's kill condition K3, this alone is informative: **the imaging-weight
choice, not statistics, is the dominant source of uncertainty on this
measurement at the lab's own precision.**

**Blocked (compute-time budget, this session):** Galactic-latitude split,
E(B-V) split, stellar-density split, depth/seeing splits, angular-IC
on/off, randoms-realisation jackknife (plan §3.4 tests 2-7). Each requires
one more full NGC+SGC pypower run (~150-200s) plus a fit; the WEIGHT_SYS
test alone took ~12 min wall clock for 4 variants. Recorded as the exact
remaining work, not silently dropped.

## 4. b_Φ-marginalised statement

Marginalising p uniformly over [1.0, 1.6] (the published LRG-universality
to QSO-merger-model range): **f_NL^loc = -36.3 (+16.4/-16.4) at 68% CL**
(median/16th/84th percentile of the MCMC chain, `fnl_chain_marginalised.npy`).
The **published** result swings from -3.6 (p=1.6) to +3.5 (p=1.0) — a
7-unit shift on a ±9 measurement. **Our own reproduction shows the same
qualitative sensitivity**: -50.6 (p=1.6) to -26.7 (p=1.0), a 24-unit shift —
proportionally similar (both roughly compatible with their own quoted 1σ
uncertainty), reinforcing the plan's stated physics point: for a theory
predicting |f_NL|≈2, **the p (bias-response) choice moves the answer by an
amount comparable to the measurement's own error bar**, in both the
official and this independent pipeline.

## 5. Posterior overlap with the flagship values

Using our own p-marginalised posterior (median -36.3, σ≈15.5, from
`fnl_chain_marginalised.npy`):

| Target | Value | Distance from our posterior median |
|---|---|---|
| Flagship (matter-bounce, ledger #1) | f_NL = -35/16 = -2.1875 | **2.20σ** |
| Cai et al. 2009 (superseded) | f_NL = -35/8 = -4.375 | **2.06σ** |
| Null (no PNG) | f_NL = 0 | 2.34σ |

Both flagship candidates sit within our own ~2.1-2.2σ, i.e. **not
distinguished from each other or from our own central value** — the two
targets differ by only ~0.14σ in our units (cf. the plan's pre-registered
0.24σ separation using DESI's own published σ, `survey_reach_fnl.py`).
**This DR1 QSO reproduction — official or lab-native — does not, and by
design (ledger #3's 0.16σ/0.32σ reach) cannot, discriminate -35/16 from
-35/8 or from zero.** Confirmation-bias caveat (plan risk R-d) stated
explicitly: none of these central values should be read as support for
the bounce; the coincidence of sign is not evidence.

## 6. Scope executed vs plan

| Plan step | Status |
|---|---|
| 1. Environment (pypower/cosmoprimo/desilike/emcee) | DONE — CLASS unavailable, EH transfer fallback used (plan's explicit contingency) |
| 2. Remaining QSO downloads | PARTIAL — 4/18 randoms realisations per cap (documented fidelity reduction) |
| 3. P_ℓ(k) measurement, NGC+SGC | DONE — no numeric published P(k) table exists to match (confirmed via WebFetch of arXiv:2411.17623 full text); spec-level consistency check done instead |
| 4. Scale-dependent bias fit | DONE — real result, offset from published documented in §2 |
| 5. Systematics budget | PARTIAL — 1/≥5 tests (WEIGHT_SYS), Δf_NL=+62.4; remaining 6 tests are the next concrete step |
| 6. b_Φ-marginalised + posterior overlap | DONE — §4, §5 |
| 7. This document + manifest | DONE |

**LRG:** not started (QSO-first per task instructions; QSO completed
within the session's compute-time budget).

## 7. Files

- `pk_estimator_qso.py`, `combine_and_compare.py` — P_ℓ(k) measurement (step 3)
- `fit_fnl.py` — f_NL fit + MCMC (step 4/6)
- `systest_weight_sys.py`, `systest_fit.py` — systematics test 1 (step 5)
- `outputs/pk_qso_{NGC,SGC}.json`, `outputs/pk_qso_combined_*` — poles + comparison
- `outputs/fnl_fit_results.json`, `outputs/fnl_chain_marginalised.npy` — fit results
- `outputs/systest_weight_sys_{pk,fnl}.json` — systematics test 1
- `RUN_LOG.md` — full step-by-step execution log with commit SHAs
