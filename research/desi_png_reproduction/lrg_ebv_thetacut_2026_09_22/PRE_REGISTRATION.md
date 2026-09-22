# Ledger row 4 — LRG E(B−V) at 0.8 < z < 1.1 on the θ-cut products: PRE-REGISTRATION

**Lane:** `LS14-row4-ebv` · **Date:** 2026-09-22 · **Committed BEFORE any
f_NL statistic was computed.** Nothing below was chosen after seeing an f_NL
value.

## 0. Why this lane exists

Lane `LS11-row4-lrg` closed ledger row 4's LRG channel
(`../lrg_channel_2026_09_22/LEDGER4_LRG_RESULT_2026-09-22.md`). Its fifteen
systematics rows were all nulls, but one row came within **0.005σ** of the
pre-registered MARGINAL-WATCH threshold: **E(B−V) at 0.8 < z < 1.1,
√2-corrected Δ/σ = −0.995** (raw −1.41). LS11's own §6 item 1 names it the
first thing to re-test, and its §6 item 6 names the untouched
`_thetacut0.05` official variants as the bounded next step. This lane does
exactly that one thing: re-test **that one row**, on those products.

A systematic sitting 0.005σ from its threshold must not be left as a
coincidence. The verdict may move either way and **both directions are
reported as measured**.

## 1. Inputs and their reachability (checked before pre-registering)

All six files below returned a `Content-Length` over HTTP range reads on
2026-09-22 (a HEAD-equivalent probe, not a statistic):

| file (under `…/full-shape-bao-clustering/v1.0/data/`) | bytes |
|---|---|
| `spectrum/window_spectrum-poles_LRG_GCcomb_z0.8-1.1_thetacut0.05.h5` | 216,704,470 |
| `spectrum/window_spectrum-poles_LRG_GCcomb_z0.8-1.1.h5` | 216,704,470 |
| `spectrum/spectrum-poles_LRG_{GCcomb,NGC,SGC}_z0.8-1.1[_thetacut0.05].h5` | 111,684 each |
| `covariance/EZmock/covariance_spectrum-poles_LRG_GCcomb_z0.8-1.1[_thetacut0.05].h5` | 497,102 / 497,102 |

**Input characterisation already performed (official products only; no
f_NL was fitted).** Disclosed here rather than hidden, exactly as LS11
disclosed reading the `zeff` attribute before pre-registering:

- the θ-cut and untreated spectra share an identical k grid and identical
  `nmodes`; the θ-cut and untreated covariances share identical k grids and
  k-edges;
- over the fit range 0.003 ≤ k ≤ 0.08 the ratio
  T_ℓ(k) = P_ℓ^{θcut}/P_ℓ^{untreated} on GCcomb is
  **ℓ=0: 0.9375 → 0.9873 (median 0.9634)**, **ℓ=2: 0.9470 → 0.9960
  (median 0.9845)**, ℓ=4 noisy because P_4 crosses zero;
- the θ-cut EZmock covariance diagonal differs from the untreated one by
  **≤ 0.32 %** (median 0.06 %) across the 48 fitted bins.

**Consequence, stated before any fit.** The θ-cut is a change to the
**estimator applied to the data**, not only to the window. It removes ~3.7 %
of P_0 with a ~5 % tilt across the fit range — precisely the kind of
large-scale tilt f_NL is sensitive to. LS11's split power spectra were
measured from the catalogues with `pypower.CatalogFFTPower` **without** the
θ-cut. Therefore **swapping only the window and covariance to `_thetacut0.05`
while keeping an untreated data vector is NOT a self-consistent fit**, and
this lane will not present such a fit as the θ-cut answer (it is reported
only as a labelled diagnostic, §3 variant D2).

**A genuine θ-cut re-measurement of the split halves is out of this lane's
budget and is not attempted.** `pypower` supports it
(`direct_selection_attrs={'theta': (0., 0.05)}`), but the θ-cut power
spectrum requires the direct small-angle D–D, D–R and R–R pair sums; the
R–R term alone for one E(B−V) half at this z-bin is ~10⁸ pairs
(6.0 × 10⁶ randoms, ~17 angular neighbours each within 0.05°) against 300
k-bins, i.e. ~10¹¹ pair–mode evaluations per half, four halves. DESI runs
this on NERSC. It is named as this lane's next bounded step, not faked here.

## 2. The convention this lane must not break

LS11 and `../LEDGER4_RESULT_v5_2026-09-04.md` (QSO) are on ONE convention:
b(k) = b1 + 3 f_NL δ_c (b1 − p)/α(k), δ_c = 1.686, **n_shot fixed = 0**,
b1 free, official window matrix applied to the theory vector, official
EZmock covariance, NGC+SGC combined by n_data-weighted mean before
rebinning onto the covariance's coarse grid, **0.003 ≤ k ≤ 0.08**,
ℓ = 0, 2, 4, profile likelihood Δχ² = 1. Headline **p = 1.0**, with
**p = 1.6** reported alongside. This lane changes **nothing** in that
convention. It reuses `../lrg_channel_2026_09_22/lrg_fit_core.py`,
`fit_lrg_splits.py`'s `combine_caps`/`verdict`/fit block and
`fit_lrg_headline.cosmo_at` unmodified; the only new code is a product
selector that points `lrg_official_io`'s three URLs at the `_thetacut0.05`
names, and the transfer application of §3.

## 3. What is computed, and in what order

**G — Gate (runs first; nothing downstream is believed until it passes).**
Re-run the E(B−V) z0.8–1.1 split fit on the **untreated** products with this
lane's code and reproduce LS11's published row:
high = −17.62 ± 8.47, low = −0.27 ± 8.95, Δ = −17.35, σ_Δ = 12.32,
raw Δ/σ = −1.41, √2-corrected = −0.995.
**Pass criterion: the √2-corrected Δ/σ agrees with −0.995 to ≤ 0.02, and
both half f_NL values agree to ≤ 0.05.** If the gate fails, this lane
reports BLOCKED and publishes no θ-cut number.

**A — Anchor (fully self-consistent, no approximation).** Fit the
**official full-sample** z0.8–1.1 spectrum on the complete θ-cut triple
(measured P_ℓ + window + covariance, all `_thetacut0.05`) and on the
complete untreated triple. The difference δ_θ = f_NL^{θcut} − f_NL^{untreated}
is an exact, approximation-free measurement of how much the θ-cut convention
moves f_NL for this z-bin, at p = 1.0 and p = 1.6.

**D1 — The θ-cut split test (this lane's primary result).** Each split
half's measured P_ℓ is put on the θ-cut convention by the **cap-specific
official transfer**
T_ℓ^C(k) = P_ℓ^{C,θcut}(k) / P_ℓ^{C,untreated}(k), C ∈ {NGC, SGC},
built from the official cap spectra on the native fine k grid and applied to
that cap's half before the n_data-weighted NGC+SGC combination. ℓ = 4 is
transferred on the same rule as ℓ = 0, 2; because P_4 crosses zero the ratio
is unstable there, so **T_4 is clipped to [0.5, 1.5]** and the number of
clipped bins is reported. The fit then uses the **θ-cut window + θ-cut
covariance**. *Disclosed approximation:* the transfer is measured on the
full cap, not on each E(B−V) half, so any dependence of the θ-cut on the
half's own angular geometry is unmodelled.

**D2 — Diagnostic (labelled inconsistent, never the headline).** θ-cut
window + θ-cut covariance on the **untreated** split data vectors. Reported
only to show how much of any change comes from the window/covariance side
alone.

**V — Validation of the D1 approximation.** Refit D1 with the two caps'
transfers **swapped** (NGC's half transferred by T^SGC and vice versa),
which is a deliberately wrong-geometry transfer and therefore a conservative
proxy for the unmodelled half-to-half geometry dependence. Report the
induced change in the √2-corrected Δ/σ as ε_T, plus
max_{ℓ∈{0,2}, k∈[0.003,0.08]} |T^NGC − T^SGC|.

## 4. Decision rules — fixed now, not changed afterwards

**Verdict thresholds are LS11's, inherited verbatim**, applied to the
**√2-corrected |Δ/σ|** (the same disclosed √2 covariance-reuse correction,
for the same reason: no split-specific official covariance exists at either
convention):

- |Δ/σ|_corr ≥ 2 → **FLAGS**
- 1 ≤ |Δ/σ|_corr < 2 → **MARGINAL WATCH ITEM**
- |Δ/σ|_corr < 1 → **no detectable sensitivity at this fidelity**

**Robustness rule (fixed now).** The D1 verdict is reported as **ROBUST**
only if the verdict word is unchanged under the swapped-cap transfer V.
If the verdict word differs between D1 and V, the lane reports
**INCONCLUSIVE at this fidelity** and says so in the headline sentence — it
does **not** pick the more interesting of the two.

**Propagation rule if the row stops being a null (fixed now).** If D1 gives
|Δ/σ|_corr ≥ 1 the lane reports, in this order: (a) the raw Δf_NL and σ_Δ;
(b) each half's f_NL alone; (c) the three-bin LRG headline recombined with
the z0.8–1.1 bin's σ inflated in quadrature by the **half-difference
systematic |Δ|/2**, stated as a disclosed systematic and never as a new
measurement; (d) the QSO-side E(B−V) rows from
`../LEDGER4_RESULT_v5_2026-09-04.md` quoted verbatim, with a plain statement
of whether the QSO channel behaves consistently. If D1 gives
|Δ/σ|_corr < 1 the row stays a null and the headline is unchanged; the
number is still reported to three decimals so the next lane knows how close
it sits.

**No threshold, fit range, weight, bin, k-cut, p value or combination rule
will be changed after seeing a number.** A result that moves the verdict and
a result that leaves it a null are equally publishable outcomes of this lane.

## 5. Pre-committed fallbacks

1. If any `_thetacut0.05` product is unreachable by streaming, the **exact
   file name and the exact HTTP failure** are named in the result and the
   lane stops. **No other product is silently substituted.**
2. If gate G fails, the lane reports **BLOCKED** and publishes no θ-cut
   f_NL.
3. If the ℓ=4 transfer clipping touches more than 25 % of the fitted ℓ=4
   bins, the lane additionally reports the ℓ = 0,2-only fit and says which
   number the verdict is taken from (the ℓ = 0,2,4 fit, to stay on LS11's
   convention).
4. No bulk catalogue is written to disk; streamed bytes and peak disk are
   recorded in the manifest.

## 6. Deliverables

`RESULT_2026-09-22.md`, `RUN_LOG.md`, a Q2 reproducibility manifest at
`reproducibility/manifests/experiments/ledger4-lrg-ebv-thetacut.json`,
`PROPAGATION_NOTE.md` with exact printable sentences naming the paper that
owns the f_NL forecast material, and the **row-4 status cell only** of
`project-context/NEXT_SCIENCE_LEDGER.md`. **No paper `.tex`, no SSOT, no
site data is touched by this lane.**
