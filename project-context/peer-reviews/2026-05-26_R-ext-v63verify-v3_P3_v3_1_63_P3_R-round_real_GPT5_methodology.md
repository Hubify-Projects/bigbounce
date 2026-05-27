# P3 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-v63verify-v3_P3_v3_1_63
**Wall time**: 127.5s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=69017, completion=7889, reasoning=6687, total=76906

---

## PAPER-GPT-B1 — BLOCKER — “Canonical” anomaly score is used inconsistently

**Section:** §2.2 Eq. (2), Table I, §3.4 eROSITA, §3.5 Planck  
**Issue:** The paper states that \(S\) is *always* the standardized residual \((\mathrm{MSE}-\mu_{\rm val})/\sigma_{\rm val}\), but Planck “scores” are raw MSE values matching `val_loss`/p99 MSE (0.437, 0.520, 0.558–0.621), eROSITA mixes BigAE \(S\) with IsolationForest raw scores, and survey thresholds are described interchangeably as \(S\), raw MSE, IF score, and percentiles. This breaks dimensional consistency and makes the catalog thresholds/rates non-auditable.  
**Fix:** Publish separate columns/notation for raw MSE, standardized \(S\), IF raw score, and percentile rank; convert every quoted threshold to the Eq. (2) \(S\) scale or remove the “one definition for the whole paper” claim.

## PAPER-GPT-B2 — BLOCKER — DESI 5-fold Jaccard validation is internally contradictory

**Section:** §2.2 “In-sample scoring and held-out validation”; compare Abstract and §6.4(i)  
**Issue:** §2.2 says each fold scores only its disjoint 9,400-spectrum held-out split, but then reports 546 objects in the union and 399 objects appearing in all five folds. That is impossible for disjoint held-out folds; those numbers require scoring the full 47,000-object pool per fold.  
**Fix:** Rewrite §2.2 to match §6.4(i): full-pool scoring with fold-specific checkpoints. Do not call the reported Jaccard a held-out-only validation; label it training-partition/ranking stability, or recompute true held-out-only statistics.

## PAPER-GPT-B3 — BLOCKER — \(f_{\rm NL}\) forecast summaries still use invalid linear error propagation

**Section:** Abstract, §5, §7 Conclusions item 5, Appendix “Sensitivity to Bias Enhancement”  
**Issue:** The paper says the positivity-respecting canonical forecast is \(\sigma(f_{\rm NL})=8.14\) with envelope \([3.92,8.98]\), and GS is \(1.95\) with \([0.94,8.98]\), but the Abstract/Conclusions still quote \(\sigma=8.27\pm2.37\) and \(\sigma_{\rm GS}=2.28\pm7.43\). The GS lower bound is negative and the full-sample \(+1\sigma\) tail exceeds the single-tracer floor, which the paper itself says is unphysical.  
**Fix:** Replace all headline, abstract, conclusion, and table references with the positivity-respecting or exact Fisher mapping. Keep the linear numbers only in a clearly labeled historical/diagnostic note, not in summaries.

## PAPER-GPT-M1 — MAJOR — Fisher/systematics budget mixes incompatible baselines

**Section:** §5 Cosmological Applications; Appendix “Shot-noise sensitivity”  
**Issue:** The paper compares \(\sigma_{\rm std}=8.98\), empirical \(\sigma=8.14\), internal “systematics-marginalized” \(\sigma=0.067\)–0.116, Heinrich \(\sigma\simeq0.7\), and appendix baselines 16.85/12.72/11.71 as if they are connected forecasts. They are different Fisher problems with different surveys, observables, nuisance priors, and covariance assumptions; no coherent systematic degradation/error propagation is provided.  
**Fix:** Add a configuration table specifying survey, observable, tracer densities, bias model, \(k/z\) range, covariance, nuisance priors, and baseline for each Fisher number. Quote percentage improvements only within the same configuration; otherwise remove cross-comparisons.

## PAPER-GPT-M2 — MAJOR — PTA “likelihood” remains a product of marginal posterior KDEs

**Section:** §5.1 NANOGrav Bounce Consistency; Appendix PTA MCMC  
**Issue:** The PTA fit multiplies 30 one-dimensional free-spectrum posterior KDEs as independent likelihood factors, ignoring inter-bin covariance and the prior/Jacobian structure of the released posterior product. The paper caveats Bayes factors, but still quotes \(\gamma=2.567\pm0.382\) and “SMBHB strongly disfavored at \(4.61\sigma\)” as a robust parameter-shift result.  
**Fix:** Downgrade this to an approximate marginal-posterior projection and remove “strongly disfavored” language, or compute the joint/profile likelihood with the full covariance/prior treatment and marginalization over \(\log_{10}A\).

## PAPER-GPT-M3 — MAJOR — Catalog-grade/exploratory split arithmetic assumes zero LAMOST overlaps

**Section:** Abstract; Table I footnote \(\spadesuit\); Data availability  
**Issue:** The paper gives an exact catalog-grade count \(264{,}938 = 378{,}280-113{,}342\), treating every LAMOST detection as a unique LAMOST-only object. That contradicts the stated 637 multi-survey clusters and the text noting SDSS\(\times\)LAMOST overlap affects the partition.  
**Fix:** Recompute the unique-object count after excluding LAMOST with the union-find cluster manifest, or report only an approximate catalog-grade count until per-cluster attribution is published.
