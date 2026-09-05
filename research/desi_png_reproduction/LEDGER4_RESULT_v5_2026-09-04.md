# Ledger #4 result v5 — full 5-row systematics table on one convention (supersedes v4)

**Date:** 2026-09-04 · **Supersedes:** `LEDGER4_RESULT_v4_2026-09-04.md`
(kept as record). Full log: `RUN_LOG.md` v5 section. Wide-angle finding
(v4 §1) is unaffected and carried forward unchanged.

## 1. What this round closes

v4 left two systematics checks (WEIGHT_SYS on/off, Galactic-latitude
split) at v1/v2 fidelity — an ad-hoc diagonal-sigma covariance, not the
OFFICIAL DESI window + OFFICIAL EZmock covariance used for v3's headline
fit and v4's three imaging-property splits. This round re-measures both
at v4 fidelity: `pk_estimator_qso_weightsys_v5.py` and
`pk_estimator_qso_gallat_v5.py` (NGC+SGC, nmesh=256, N_RAN=4, ell=0,2,4 —
identical settings to v4's EBV/STARDENS/GALDEPTH_Z splits), then
`fit_fnl_splits_v5.py` reuses v4's `fit_split()` unchanged so all five
systematics tests sit on the exact same fitting machinery (p=1.6,
n_shot=0 fixed, official window/covariance, NGC+SGC n_data-weighted
combine, KMIN/KMAX = 0.003/0.08). Same disclosed covariance-reuse caveat
as v4: no split-specific official covariance exists, so the full-sample
covariance is reused for each half — this under-estimates true sigma by
roughly a factor ~sqrt(2) in the wrong direction (conservative for
significance, not for the central Δf_NL).

## 2. The full systematics table (one convention, all 5 rows)

| Systematic | f_NL(high) | f_NL(low) | Δf_NL | σ_Δ | Δ/σ | Δ/σ (√2-corrected) |
|---|---|---|---|---|---|---|
| E(B-V) | −20.70 ± 21.17 | −19.01 ± 20.26 | −1.69 | 29.30 | −0.06 | −0.04 |
| Stellar density | −6.37 ± 21.69 | −4.00 ± 27.08 | −2.37 | 34.70 | −0.07 | −0.05 |
| Galactic depth (z-band) | −36.90 ± 21.03 | −18.25 ± 23.76 | −18.66 | 31.73 | −0.59 | −0.42 |
| **WEIGHT_SYS on/off** | −4.91 ± 19.04 | +83.24 ± 7.46 | −88.15 | 20.44 | **−4.31** | **−3.05** |
| **Galactic latitude (\|b\|>40 vs ≤40)** | −18.51 ± 17.28 | +23.04 ± 15.63 | −41.55 | 23.30 | **−1.78** | **−1.26** |

"high"/"low" are the fit_fnl_splits.py naming convention: for
WEIGHT_SYS, "high" = DESI's default WEIGHT (includes WEIGHT_SYS), "low"
= WEIGHT with WEIGHT_SYS divided out. For Galactic latitude, "high" =
|b|>40deg, "low" = |b|<=40deg. Full artifact:
`outputs/systematics_table_v5.json`.

## 3. Honest reading: WEIGHT_SYS is a real, large, and *expected* effect — not a null

Unlike the three imaging-property splits (all |Δ/σ| < 0.6, unchanged
from v4), **WEIGHT_SYS on/off is the one test in this table that crosses
the 2σ flag even after the conservative √2 correction** (−4.31σ raw,
−3.05σ corrected) — consistent with, and *more* significant than, v1's
earlier lower-fidelity measurement (Δ=+62.4, >3σ). The fit diagnostics
explain why: with WEIGHT_SYS applied (DESI's own imaging-systematics
correction), the (b1, f_NL) model fits well against the official
covariance (χ²/dof ≈ 25.5/30 ≈ 0.85); with WEIGHT_SYS divided out, the
fit is poor (χ²/dof ≈ 131/30 ≈ 4.4). This is the expected signature of a
real, uncorrected imaging systematic faking large-scale power that mimics
scale-dependent bias — exactly what WEIGHT_SYS is constructed by the
DESI pipeline to remove. **This is not evidence against the headline
measurement**: `fit_fnl_official.py`'s headline fit (and every published
DESI QSO f_NL result) already applies WEIGHT_SYS, matching the "high"
row here. It IS evidence that WEIGHT_SYS is doing necessary, large work,
and that the pipeline's f_NL result is only as good as DESI's own
imaging-systematics correction — the single largest lever in this lab's
systematics budget, larger than the statistical σ of the headline fit
itself (~19–25).

The Galactic-latitude split (−1.78σ raw, −1.26σ corrected) is marginal:
below the 2σ flag but the second-largest effect measured, well above the
three imaging-property splits. It is not dispositioned as a null; it is
flagged as a watch item, consistent with Galactic latitude being a proxy
for several correlated imaging effects (stellar density, dust, depth) at
once rather than a single clean property.

## 4. Headline f_NL — unchanged

This round does not touch `fit_fnl_official.py` or its inputs (the
official WEIGHT column, which already includes WEIGHT_SYS). The
headline values from v3/v4 stand exactly as reported:

| p (bias model) | f_NL | 1σ (profile-likelihood) |
|---|---|---|
| p=1.6 (QSO merger, DESI default) | −2.169 | ±25.3 |
| p=1.0 (universality) | −1.127 | ±13.1 |
| p-marginalised [1.0,1.6], midpoint | −1.648 | ~19.2 |

## 5. The lab's own systematics budget, stated honestly

- Three of five tested systematics (E(B-V), stellar density, Galactic
  depth in z) show no detectable sensitivity at official-covariance
  fidelity, even before the √2 correction.
- One (WEIGHT_SYS on/off) shows a large, real, expected effect — but it
  is a validation that DESI's own correction is necessary and already
  applied in the headline, not an unaccounted-for residual in the
  headline number.
- One (Galactic latitude) is marginal (−1.3σ to −1.8σ depending on the
  covariance convention) and is flagged, not dismissed.
- **The LRG channel is NOT now "the only remaining residual."** The
  Galactic-latitude marginal sensitivity (§3) is an open item in the QSO
  channel itself, independent of any LRG-channel work. The honest
  standing list of open residuals is: (a) Galactic-latitude marginal
  signal in QSO (this round, new), (b) the LRG channel entirely
  untouched (unchanged from v1–v4), (c) split-specific covariance/window
  products do not exist for any of the five tests above (disclosed
  approximation, all five rows).

## 6. Scope vs. plan (v5 additions only; v1–v4 items carry forward unchanged)

| Item | Status |
|---|---|
| WEIGHT_SYS re-test at official fidelity | DONE — real, large, expected effect (−3.05σ to −4.31σ); not a headline concern (already applied), IS the largest budget item |
| Galactic-latitude re-test at official fidelity, NGC+SGC | DONE — marginal (−1.26σ to −1.78σ); flagged as an open watch item, not dispositioned as null |
| One covariance convention across all 5 systematics tests | DONE — this table (§2) |
| Wide-angle correction | UNCHANGED from v4 (genuine null, carried forward) |
| LRG channel | NOT STARTED (unchanged from v1–v4) |

**Never tuned toward the published value.** WEIGHT_SYS's large effect
was not adjusted, suppressed, or reframed to minimize it — it is
reported as the most significant finding in this table, exactly as
measured, with the physical mechanism (imaging-systematics correction
doing its job) stated plainly rather than explained away.
