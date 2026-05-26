# P3 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-v63verify_P3_v3_1_63
**Wall time**: 123.6s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=69065, completion=6410, reasoning=5490, total=75475

---

No blocker-grade findings.

## PAPER-GPT-M1 — MAJOR

**Section:** Table I caption/footnotes; §3.2 SDSS  
**Issue:** SDSS `77,905 at S>=0.1060` is repeatedly called “top-1%,” but §3.2 says `p99=0.2051` gives `19,253`; `77,905/1,925,279 = 4.05%`, not 1%, and Table I’s `3.38%` rate uses the unscored 2,304,830 denominator.  
**Fix:** Relabel SDSS as a fixed-count/96th-percentile continuity slice and compute rates using the scored denominator, or replace the catalog count with the true top-1% `19,253` and update dedup totals.

## PAPER-GPT-M2 — MAJOR

**Section:** §2.2 “In-sample scoring and held-out validation”; §6.4(i)  
**Issue:** §2.2 still says each fold “scores the held-out 20% (9,400 spectra)” while reporting `470` top-1% objects per fold, union `546`, and `399` in all five folds; those numbers are impossible under held-out-only scoring and only work for full-47k scoring.  
**Fix:** Rewrite §2.2 to state explicitly that each fold scores the full 47,000 pool for the Jaccard statistic, and separate this from any true held-out-only validation.

## PAPER-GPT-M3 — MAJOR

**Section:** §5 Cosmological Applications; §6.2 Limitations; Conclusions item 5  
**Issue:** The paper gives the Fisher-positivity envelope, then later calls the linear `σ(f_NL)=8.27±2.37` / 95% `[3.62,12.95]` interval “canonical” and repeats `σ_GS=2.28±7.43`; these have unphysical tails and propagate only `α`, not observational/systematic uncertainties.  
**Fix:** Make `σ=8.14` with `1σ [3.92,8.98]` and GS `σ=1.95` with `[0.94,8.98]` the only headline intervals; demote linear values to legacy diagnostics and state they are not credible intervals.

## PAPER-GPT-M4 — MAJOR

**Section:** §5.1 NANOGrav; Appendix “PTA MCMC documentation”  
**Issue:** The PTA fit multiplies per-bin posterior KDEs as if they were independent likelihood factors, ignoring posterior prior factors and inter-bin covariance, yet still quotes `γ=2.567±0.382` and `+4.61σ` SMBHB “strongly disfavored as parameter-shift.”  
**Fix:** Use a joint free-spectrum likelihood/chain with covariance and prior handling, or downgrade this to an illustrative fit and remove sigma/exclusion-strength language.

## PAPER-GPT-M5 — MAJOR

**Section:** Appendix “Shot-noise sensitivity for sparse anomaly tracers”  
**Issue:** The shot-noise subsection uses baselines inconsistent with the main text (`σ_std=8.98` vs figure `16.85`, dense limit `11.71`, baseline-multi `12.72`) and the Fisher-penalty arithmetic is wrong: a 15% information penalty should scale `σ → σ/sqrt(0.85)`, not improve `12.72 → 12.56`.  
**Fix:** Define the Fisher configuration separately from the main DESI baseline and recompute all penalty values with `σ' = σ/sqrt(1-p)` and consistent improvement signs.

## PAPER-GPT-M6 — minor

**Section:** Table I caption/footnotes; §3.4 eROSITA  
**Issue:** Table I says the eROSITA `S>0.259` threshold is on the “IsolationForest raw-score axis,” while §3.4 says `S>0.259` is the canonical BigAE z-scored MSE axis and IF raw scores are a separate diagnostic.  
**Fix:** Use `S_BigAE>0.259` consistently for the published 298-source catalog and list IF raw scores only as a diagnostic; add the actual BigAE–IF intersection count if claiming high overlap.
