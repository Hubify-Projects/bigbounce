# P3 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-strict_P3_v3_1_62
**Wall time**: 70.9s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=68469, completion=4120, reasoning=3104, total=72589

---

## PAPER-GPT-B1 — BLOCKER

**Section:** preamble/date; Abstract; Table I footnotes; §5; §6.4 Path-C caveats  
**Issue:** The manuscript contains extensive rendered and source-level audit-trail/AI-vendor/version-history contamination: “R15 GEM-B1 closure,” “v3.1.42,” “R-round,” “OpenRouter,” “Grok,” “Gemini,” “queued for next pod-pull cycle,” etc. This is not journal prose and is disqualifying as a submission artifact.  
**Fix:** Purge all reviewer/vendor/version/closure/deferral language from the manuscript body, captions, footnotes, abstract, and date. Retain only scientific methods/results and reproducibility artifact paths where necessary.

## PAPER-GPT-B2 — BLOCKER

**Section:** §2.2 “In-sample scoring and held-out validation”; §6.4(i); Abstract  
**Issue:** DESI 5-fold validation is internally contradictory. §2.2 says each fold scores only the held-out 9,400 spectra, but the reported union/all-five counts require full-pool scoring with 470 objects per fold; the claimed “held-out” robustness is therefore not what the statistic measures.  
**Fix:** Either recompute true held-out-only stability with valid fold accounting, or rewrite all claims to state full-pool rescoring by models trained on 80% and stop calling the Jaccard statistic held-out validation.

## PAPER-GPT-B3 — BLOCKER

**Section:** §2.2 OOD validation; DESI headline counts throughout  
**Issue:** The DESI OOD test invalidates the absolute $S>5$ threshold: the 100k unseen sample has median MSE 0.178 while the catalog threshold is $\sim0.143$, implying $>50\%$ anomalies, not 0.87%. The “curated catalog” reconciliation is asserted, not demonstrated, and DESI dominates the catalog, novelty rate, and cosmology input.  
**Fix:** Draw a strictly independent holdout from the exact 22.5M scored DR1 parent with identical selection/preprocessing, report its $S$ distribution and anomaly fraction, and rebuild DESI thresholds/counts if the absolute cut is not portable.

## PAPER-GPT-B4 — MAJOR

**Section:** Table I; §3 survey subsections; §7; Data availability  
**Issue:** Survey counts, thresholds, denominators, and tiers are not self-consistent. Examples: Planck native retrain scores 200,000 patches but Table I still lists 20,000 and 1%; SDSS 77,905 is described as top-1% in places but is the 96th percentile of the native scored subset; SDSS rates use 2.304M denominator although only 1.925M were scored; LAMOST is gate-failing/exploratory but still drives the headline aggregate.  
**Fix:** Add a definitive data-vector/counts table with columns: parent available, successfully scored, threshold definition, anomaly count, validation status, catalog tier, and dedup contribution. Recompute all rates and headline sums from that table.

## PAPER-GPT-B5 — MAJOR

**Section:** §5 Cosmological Applications; §7 conclusion; Appendix C  
**Issue:** The $f_{\rm NL}$ Fisher treatment remains internally inconsistent. The body adopts the positivity-respecting $\sigma^{-2}=F_0+c\alpha^2$ mapping, but the conclusion still quotes unphysical linear errors ($8.27\pm2.37$, GS $2.28\pm7.43$); Appendix C uses the invalid linear sensitivity table; shot-noise appendix baselines ($8.98$, $12.72$, $16.85$) are mutually incompatible.  
**Fix:** Remove the linear-propagated headline and appendix table or mark them purely obsolete. Rerun one coherent Fisher forecast with actual $n(z)$, shot noise, transformed $\alpha$ posterior, nuisance marginalization, and GR projection terms; otherwise present this only as a zero-systematics toy diagnostic.

## PAPER-GPT-B6 — MAJOR

**Section:** §5.2 NANOGrav; Appendix D′  
**Issue:** The PTA likelihood is built from a product of per-bin posterior KDEs while explicitly ignoring inter-bin covariance and prior/Jacobian effects, yet the paper still makes strong parameter-shift statements such as SMBHB $\gamma=4.33$ being “strongly disfavored.” This is not a model likelihood or Bayes factor and the covariance omission can change apparent significance.  
**Fix:** Either remove the PTA comparison from conclusions or downgrade it to an illustrative non-independent posterior-summary exercise. A publishable claim requires the joint free-spectrum likelihood/covariance or a proper evidence calculation with amplitude priors marginalized.
