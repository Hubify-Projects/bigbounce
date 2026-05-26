# P3 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-strict-v3_P3_v3_1_62
**Wall time**: 130.1s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=68125, completion=7718, reasoning=6633, total=75843

---

## PAPER-GPT-B1 — BLOCKER

**Location:** Sec. 2.2 “Training and Scoring”; Table I caption/footnotes; Sec. 3.2 SDSS; Conclusions item 8  
**Issue:** SDSS thresholding is internally contradictory and directly affects the headline 378,280 count. Sec. 2.2 says SDSS uses absolute `S>5` and has a 3.4% anomaly rate; Sec. 3.2 says native SDSS has only **12** objects at `S>5`, top-1% is **19,253**, and **77,905** is a bookkeeping top-4.05% slice of the scored subset, while Table I reports 77,905 as if it were the canonical anomaly count/rate.  
**Fix:** Pick one SDSS catalog rule (`S>5`, top-1%, or explicitly named continuity slice), recompute Path-C sums/dedup/rates, and make Method/Table/Conclusions use that single rule.

## PAPER-GPT-B2 — BLOCKER

**Location:** Sec. 5 “Cosmological Applications”; Sec. 6.3 “Limitations”; Conclusions item 5; Appendix “Sensitivity to Bias Enhancement”  
**Issue:** The Fisher error propagation remains stale and self-contradictory. The paper correctly introduces the positivity-respecting form with full-sample `σ_fNL=8.14` and envelope `[3.92, 8.98]`, but later still calls the linear `8.27 ± 2.37` / 95% `[3.62,12.95]` interval canonical, and the Conclusions headline still reports the unphysical GS `2.28 ± 7.43` value with a negative lower bound.  
**Fix:** Replace every headline/canonical Fisher number with the positivity-mapped values: full sample `8.14 [3.92,8.98]`, GS `1.95 [0.94,8.98]`. Move linear values to a clearly labeled noncanonical legacy parenthetical or delete them; rebuild Appendix sensitivity with the same `F0+cα²` mapping.

## PAPER-GPT-M1 — MAJOR

**Location:** Sec. 2.2 “In-sample scoring and held-out validation” vs Sec. 6.4 caveat (i)  
**Issue:** The DESI 5-fold Jaccard methodology is still described incorrectly in the Method section. It says each fold scores only the held-out 9,400 spectra, but the reported `470`-object top-1% sets, union `546`, and `399` objects in all five folds are only possible if each fold scores the full 47,000-spectrum pool.  
**Fix:** Rewrite Sec. 2.2 to match the actual full-pool scoring convention, or recompute and report a true held-out-only stability statistic. Do not state or imply “each object was scored by a model that never saw it” for the published Jaccard numbers.

## PAPER-GPT-M2 — MAJOR

**Location:** Sec. 2.2 DESI OOD validation; Sec. 3.1 DESI rate interpretation  
**Issue:** The absolute `S>5` threshold is not calibrated as a portable “5σ” anomaly criterion: the independent 100k SPARCL sample has median MSE above the threshold and would classify >50% as anomalies. The paper asserts the 22.5M production catalog is more curated, but does not show the full production-score distribution needed to reconcile the 0.87% rate quantitatively.  
**Fix:** Publish the full 22.5M DESI MSE/S quantiles and the fraction above the exact `S>5` threshold, or reframe `S>5` as a training-pool-relative ranking cut only. Avoid using “5σ” language as if it implied a calibrated false-positive probability.

## PAPER-GPT-M3 — MAJOR

**Location:** Sec. 5 systematics-marginalized Fisher paragraph  
**Issue:** The systematics budget is not propagated into the headline `σ_fNL` forecast. The text gives zero-systematics DESI/anomaly values near `σ_fNL≈8`, then separately quotes an internal marginalized Fisher floor `0.067–0.116` for different SPHEREx/DESI/anomaly configurations, with no matched unmarginalized baseline or degradation ratio.  
**Fix:** Either run the nuisance-parameter Fisher on the same configuration used for the headline empirical-α forecast, or remove the absolute `0.067–0.116` numbers from the main argument and report only the qualitative ranking of nuisance axes.

## PAPER-GPT-m1 — minor

**Location:** Appendix PTA MCMC diagnostics  
**Issue:** The appendix says the mean `emcee` acceptance fraction `0.632` is “within the recommended [0.2,0.5] range,” which is arithmetically false.  
**Fix:** Change to “above the usual 0.2–0.5 heuristic but acceptable for this simple 2-parameter posterior,” or provide independent-chain convergence diagnostics.
