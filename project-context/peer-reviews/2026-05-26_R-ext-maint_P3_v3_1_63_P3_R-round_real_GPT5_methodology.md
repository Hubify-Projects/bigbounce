# P3 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-maint_P3_v3_1_63
**Wall time**: 208.7s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=68971, completion=8379, reasoning=7331, total=77350

---

## PAPER-GPT-B1 — BLOCKER

**Section:** §2.2 Eq. (2), Table I, §3.4 Planck, §3.5 eROSITA  
**Issue:** The paper defines canonical score \(S\) universally as z-scored MSE, but later uses raw MSE/IF scores as “S”: Planck median score \(0.437\) “matching val_loss” and top range \([0.558,0.621]\) are raw MSE, not z-scores; SDSS/LAMOST/eROSITA thresholds \(0.106,0.4613,0.259\) mix raw/native/IF axes. Thresholds and rates are therefore not dimensionally reproducible.  
**Fix:** Split columns into raw MSE, standardized \(S\), IF raw score, and percentile rank. Recompute all thresholds/counts using one declared axis per survey.

## PAPER-GPT-B2 — BLOCKER

**Section:** §2.2 “In-sample scoring and held-out validation”; §6.4(i)  
**Issue:** Main text says each fold scores only its held-out 9,400 spectra, but reports top-1% sets of 470, union 546, and 399 objects in all five folds. Under held-out-only scoring each fold has 94 objects and disjoint folds cannot have “all five” overlap.  
**Fix:** Correct §2.2 to state full-pool scoring by each fold checkpoint, with 470 objects per fold, or recompute true held-out-only stability metrics.

## PAPER-GPT-B3 — BLOCKER

**Section:** Abstract; §5; §6 limitations/caveats (c,i,j); Conclusions item 5  
**Issue:** Fisher-positivity closure is not converged. The paper alternates between canonical \( \sigma_{f_{\rm NL}}=8.14\,[3.92,8.98]\), obsolete linear \(8.27\pm2.37\) / \([3.62,12.95]\), and GS \(2.28\pm7.43\) with an impossible negative lower bound. The GS nonlinear lower bound \(0.94\) is also extrapolated to \(\alpha=3.86\), where the paper itself says the \(F_0+c\alpha^2\) form saturates and over-constrains.  
**Fix:** Provide one canonical forecast table. Remove linear intervals from abstract/conclusions or label them obsolete diagnostics; recompute exact multi-tracer Fisher over the \(\alpha\) posterior with shot noise, nuisance parameters, and GR terms before quoting intervals.

## PAPER-GPT-M1 — MAJOR

**Section:** Table I; §3.4 Planck; Data availability  
**Issue:** Path-C processed-count arithmetic is inconsistent. Table I Path-C total uses \(37{,}272{,}042\), implying the old 20k Planck patch count, but §3.4 says the canonical native Planck re-score used \(2\times10^5\) patches. SDSS/LAMOST native denominators also differ from table denominators.  
**Fix:** Add separate columns for available, successfully scored, and selected objects/patches for cross-transfer and Path-C. Recompute totals and rates from the Path-C scored denominators.

## PAPER-GPT-M2 — MAJOR

**Section:** Title/Abstract; Table I footnotes; §3.2–§3.3; Conclusions item 8  
**Issue:** The \(378{,}280\) “unique anomalies” headline combines validated detections with arbitrary/exploratory slices: SDSS uses a count-preserving top-77,905 slice, about 4.05% of scored spectra, not \(S>5\) or top-1%; LAMOST contributes \(\sim113\)k despite failing the 5σ gate; Gaia is marked exploratory with 41% stability. This overclaims catalog-grade anomaly yield.  
**Fix:** Make the validated catalog-grade tier the headline count. Move LAMOST/Gaia/continuity slices to explicitly exploratory tables and state their thresholds/gate failures in the abstract.

## PAPER-GPT-M3 — MAJOR

**Section:** §5.2 NANOGrav; Appendix “PTA MCMC documentation”  
**Issue:** The PTA “real-KDE likelihood” multiplies per-bin posterior KDEs as independent likelihood factors and then quotes a \(4.61\sigma\) SMBHB parameter-shift. There is no inter-bin covariance, posterior-to-likelihood prior correction, amplitude profiling/marginalization, or SMBHB amplitude-prior evidence integral. The “not a Bayes factor” disclaimer is insufficient while saying “strongly disfavored.”  
**Fix:** Call it only a diagonal-KDE parameter-shift diagnostic, or compute a joint likelihood/evidence with covariance and marginalized \(\log_{10}A\) priors before using exclusion language.
