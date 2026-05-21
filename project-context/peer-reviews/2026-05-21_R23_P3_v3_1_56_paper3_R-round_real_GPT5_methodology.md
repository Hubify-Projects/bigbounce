# paper3 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-21_R23_P3_v3_1_56
**Wall time**: 136.2s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=66841, completion=7276, reasoning=6214, total=74117

---

## PAPER-GPT-B1 — BLOCKER

**Section:** Abstract; §5; §6 “Limitations”; §7 item 5  
**Issue:** The paper still reports invalid local-linear Fisher results as principal conclusions: `σ(f_NL)=8.27±2.37` and `σ_GS=2.28±7.43`, despite §5/§6.4 stating these are unphysical under the positivity-respecting mapping. The quoted tails violate the stated Fisher bound (`10.64 > 8.98`; GS lower bound negative), so the cosmology headline is internally contradictory.  
**Fix:** Replace every summary/conclusion occurrence with the canonical positivity-respecting values: full sample `σ=8.14`, 1σ envelope `[3.92, 8.98]`; GS `σ=1.95`, envelope `[0.94, 8.98]`. Move linear values to a clearly labeled deprecated diagnostic only.

## PAPER-GPT-B2 — BLOCKER

**Section:** Table I caption/footnotes; §3.1 SDSS; §7 Path-C rebuild  
**Issue:** The SDSS Path-C count `77,905` used in the `388,493 → 378,280` headline is neither the strict `S>5` count (`12`) nor the native top-1% count (`19,253` at `S≥0.2051`). §3.1 admits `S≥0.1060` is the 96th percentile chosen to preserve the old cross-transfer row count, so the catalog headline depends on a bookkeeping target, not a defined anomaly threshold.  
**Fix:** Choose one a priori SDSS threshold, recompute the SDSS count, 7-way dedup, compression, and headline. If `77,905` is retained, label it “continuity slice,” not the primary catalog anomaly set.

## PAPER-GPT-M1 — MAJOR

**Section:** Table I; §3.5 Planck; §7; abstract scale claim  
**Issue:** The native Planck analysis scores `2×10^5` patches and selects top `200`, but Table I and the Path-C total still use `20,000` Planck patches and call `200` a `1%` selection. If the native sample is used, Planck’s rate is `0.1%`, and the processed total is larger by `180,000` patches (`37,452,042`, not `37,272,042`).  
**Fix:** Update all denominators, rates, and “37.3M” scale arithmetic to the native Planck sample, or explicitly restrict the released Planck catalog to the original 20k patch set.

## PAPER-GPT-M2 — MAJOR

**Section:** §2.2 “In-sample scoring and held-out validation”; §6.4(i)  
**Issue:** §2.2 still says each fold scores only the held-out `9,400` spectra, but the reported union `546` and “399 in all five folds” are impossible under disjoint held-out scoring. §6.4(i) says the real statistic came from scoring the full 47k pool, which is not a held-out validation and does not support the “model never saw it” claim.  
**Fix:** Rewrite §2.2 to match the actual full-pool scoring convention and demote the statistic to rank-stability, or recompute true held-out-only Jaccards and report those.

## PAPER-GPT-M3 — MAJOR

**Section:** §4.3 Cross-Survey Matches; §6.4(a); Data availability  
**Issue:** The `9,576` intra-survey duplicate collapses are inferred by subtraction (`10,213−637`), not demonstrated by a per-cluster manifest. A same-survey `5″` FoF can merge real close pairs/blends, and including 10° Planck map-patch centers in a “unique physical objects” FoF count is dimensionally invalid.  
**Fix:** Release/report the intra-survey cluster manifest with survey IDs, per-survey duplicate counts, and radius-sensitivity checks. Call the result “5″ FoF components,” and keep Planck patches outside any “physical-object” count.

## PAPER-GPT-M4 — MAJOR

**Section:** §5 Fisher systematics paragraph; Appendix “Sensitivity” and “Shot-noise sensitivity”  
**Issue:** The systematic budget is not consistently propagated. §5 gives zero-systematics `σ=8.14`, then quotes a separate “fully marginalized” Fisher floor `0.067–0.116`, while Appendix shot-noise uses incompatible baselines (`σ_std=16.85`, dense limit `11.71` vs main `8.98`). These are different Fisher problems presented as one error budget.  
**Fix:** Split the forecasts into separate labeled calculations with explicit survey assumptions, or recompute one consistent Fisher including shot noise, photo-z, fiber assignment, selection, and nuisance priors, and use only that for the reported uncertainty.
