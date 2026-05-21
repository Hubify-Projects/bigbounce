# paper3 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-21_R25_P3_v3_1_56
**Wall time**: 153.9s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=66781, completion=7700, reasoning=6732, total=74481

---

No blocker-grade findings found.

## PAPER-GPT-M1 — MAJOR — §2.2 “In-sample scoring and held-out validation”

**Issue:** The main Methods text says each fold “scores the held-out 20% (9,400 spectra)” but then reports 546 unique top-1% objects and 399 appearing in all five folds; that is mathematically impossible for disjoint held-out folds and contradicts the abstract/§6.4 caveat stating full-pool scoring.  
**Fix:** Replace the §2.2 held-out-scoring language with the full-47,000-pool scoring convention, or recompute the Jaccard statistics for true disjoint held-out top-1% sets.

## PAPER-GPT-M2 — MAJOR — §5, §7, Appendix “Sensitivity to Bias Enhancement”, §6.4(c)/(i)

**Issue:** The Fisher-positivity correction is not propagated globally: the paper still headlines/recurs to the local-linear `σ(f_NL)=8.27±2.37`, Appendix Table “Sensitivity” uses linear scaling in α, and §6.4(c) calls the linear `[3.62,12.95]` envelope canonical while §6.4(i) says it is unphysical.  
**Fix:** Make the positivity-respecting mapping `1/σ^2=F0+cα^2` the only canonical form everywhere; replace the appendix table and conclusion with `σ=8.14`, 1σ envelope `[3.92,8.98]`, and label linear values as noncanonical legacy checks only.

## PAPER-GPT-M3 — MAJOR — Table I / §3.2 SDSS Path-C native count

**Issue:** SDSS `77,905` is repeatedly described as a top-1%/top-percentile native slice, but `77,905/1,925,279 = 4.05%`; §3.2 itself says `S=0.1060` is the 96th percentile, while the actual top-1% is `19,253`. The Table rate also uses the old `2,304,830` denominator, giving `3.38%`, not the native-scored denominator.  
**Fix:** Relabel `77,905` as a top-4.05% bookkeeping continuity slice, or switch the canonical SDSS Path-C count to `19,253`/`12` and recompute the Path-C sum, rate, and dedup products.

## PAPER-GPT-M4 — MAJOR — §2.2 threshold paragraph vs §3.4 eROSITA

**Issue:** Methods says eROSITA “uses an X-ray-feature-space IsolationForest” with a separate raw-isolation score, but §3.4 says the published 298-source catalog is defined by canonical BigAE z-scored MSE and the IsolationForest is only a diagnostic. These are incompatible definitions of the primary detector and score axis.  
**Fix:** State one primary eROSITA catalog axis consistently: either BigAE-MSE canonical `S>0.259` with IF as validation, or IF as the detector with a documented conversion.

## PAPER-GPT-M5 — minor — Table I / §3.5 Planck CMB totals

**Issue:** Table I and the Path-C total use `Planck N_total=20,000`, but §3.5 says the native Planck retrain rescored the full `2×10^5` patch set and selected the top 200 from that distribution. The headline processed total is therefore off by 180,000 map patches if the native Planck set is canonical.  
**Fix:** Either set Planck `N_total=200,000` and update the Path-C total, or explicitly state that only the original 20,000-patch cross-transfer sample contributes to the headline.

## PAPER-GPT-M6 — MAJOR — Abstract / Table I footnote / §7 catalog-grade split

**Issue:** The “catalog-grade ∼265,000” split is treated as exact in places via `378,280−113,342=264,938`, but that is not a tiered union-find result and assumes zero LAMOST overlap/duplicate structure. The pre-dedup non-LAMOST sum is `275,151`, so the exact catalog-grade unique count requires recomputing dedup after excluding LAMOST.  
**Fix:** Remove exact `264,938` language unless a LAMOST-excluded union-find artifact is reported; otherwise keep only approximate `∼265k` and cite the cluster manifest for attribution.
