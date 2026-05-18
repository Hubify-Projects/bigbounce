# P3_v3152_R14 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1500pt
**Wall time**: 149.5s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=64657, completion=7229, reasoning=6214, total=71886

---

## PAPER-GPT-B1 — BLOCKER

**Section:** Title, Abstract, Table I, §4.3, Conclusions, Data availability  
**Issue:** The headline `378,280` unique count remains arithmetically unsupported: `388,493` survey-level detections minus `637` pairwise-only coincidences gives `387,856`, leaving an unexplained `9,576`–`10,213` collapse while the paper itself says the union-find recompute is pending.  
**Fix:** Recompute and publish the union-find cluster manifest proving the `10,213` collapsed detections, or replace all exact `378,280` headline/title claims with the verified `387,856` upper bound / provisional range.

## PAPER-GPT-B2 — BLOCKER

**Section:** §2.2 “In-sample scoring and held-out validation” vs Abstract / §6.4(i)  
**Issue:** §2.2 still says each fold scores only the held-out `9,400` spectra, but then reports `546` union objects and `399` objects appearing in all five folds; that is impossible for disjoint held-out splits. The corrected full-pool scoring narrative landed elsewhere but not here.  
**Fix:** Change §2.2 to state each fold scores the full `47,000`-spectrum pool with `470` top-1% objects per fold, or recompute all Jaccard/union/all-five statistics for true held-out-only folds.

## PAPER-GPT-B3 — BLOCKER

**Section:** §5 Cosmological Applications; Conclusions item 5; §6.4 caveats  
**Issue:** The Fisher-positivity fix is not consistently propagated. §5 still presents `σ(f_NL)=8.27±2.37` and the linear `[3.62,12.95]` interval as “canonical,” and the Conclusions still headline `8.27±2.37` plus GS `2.28±7.43`, including unphysical tails.  
**Fix:** Make the primary forecasts everywhere `8.14` with 1σ envelope `[3.92,8.98]` and GS `1.95` with `[0.94,8.98]`; retain `8.27±2.37` / `2.28±7.43` only as explicitly secondary local-linear reference values.

## PAPER-GPT-M1 — MAJOR

**Section:** Table I caption/footnotes; §2.2 threshold policy  
**Issue:** Table I still says a fixed `S>5` cut applies to the three spectroscopic surveys and that they share a DESI-trained score scale, but Path-C native counts use mixed thresholds: DESI strict `S>5`, SDSS native continuity `S≥0.1060` / strict `S>5=12`, and LAMOST native `p99 S≥0.4613` / strict `S>5=2054`.  
**Fix:** Split Table I into explicit threshold columns/rows: cross-transfer `S>5`, native strict `S>5`, and native published percentile/continuity cuts. Remove the blanket “`S>5` for three spectroscopic surveys” wording.

## PAPER-GPT-M2 — MAJOR

**Section:** §2.2 threshold paragraph; Table I caption; §3.4 eROSITA  
**Issue:** The eROSITA score axis is internally contradictory. §3.4 says the published 298-source catalog is defined on BigAE canonical-`S` MSE with `S>0.259`, while §2.2/Table I describe eROSITA as an IsolationForest raw-score axis; IF raw scores are `~4,000–34,000`, so `S>0.259` cannot be an IF raw-score cut.  
**Fix:** Define the published eROSITA threshold solely as BigAE canonical-`S>0.259`; describe IsolationForest only as a separate cross-validation diagnostic unless an explicit calibrated mapping is provided.

## PAPER-GPT-M3 — MAJOR

**Section:** §3.3 LAMOST; §3.2 SDSS; §6.2 Model-dependence  
**Issue:** Stale cross-transfer/native language remains load-bearing. §3.3 says the `44,075` LAMOST scan used a natively trained model, but later the native result is `2,054` strict `S>5` / `113,342` top-1%; §6.2 still treats SDSS transfer-learning as the operative catalog despite Path-C native supersession.  
**Fix:** Relabel `44,075` LAMOST and original SDSS `77,905` narratives as cross-transfer baselines only; make the Path-C native counts and their thresholds the sole primary per-survey results.
