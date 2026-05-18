# P3 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1640pt_P3_v3154_R16
**Wall time**: 89.4s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=65441, completion=4754, reasoning=3624, total=70195

---

## PAPER-GPT-B1

**Classification:** BLOCKER  
**Section:** Abstract; Table I footnote `^\|`; §4.3; Conclusions; Acknowledgments/Data availability  
**Issue:** The headline `378,280` unique count is arithmetically unsupported. With `388,493` detections and only `637` pairwise multi-survey coincidences, the unique count is `388,493 - 637 = 387,856`, leaving `9,576` collapsed detections unexplained; the paper admits this but still uses `378,280` in title/headlines/data release.  
**Fix:** Either publish the union-find cluster manifest proving `10,213` total collapsed detections, including intra-survey duplicates, or change the headline unique count to the arithmetically supported value and remove `378,280`.

## PAPER-GPT-B2

**Classification:** BLOCKER  
**Section:** §2.2 “In-sample scoring and held-out validation” vs abstract and §6.4(i)  
**Issue:** The DESI 5-fold validation text still says each fold scores only the held-out `9,400` spectra, but then reports five top-1% sets of `470`, union `546`, and `399` objects appearing in all five folds. Those statistics are impossible for disjoint held-out scoring; they require full-47,000-pool scoring.  
**Fix:** Rewrite §2.2 to match the actual full-pool scoring protocol, or recompute all Jaccard/union/all-five statistics for true held-out-only folds.

## PAPER-GPT-B3

**Classification:** BLOCKER  
**Section:** Abstract; §5; §6.3 limitation 4; Appendix C; Conclusions item 5  
**Issue:** The Fisher-positivity closure is not propagated. The paper correctly gives the positivity-respecting full-sample result `σ(fNL)=8.14`, envelope `[3.92,8.98]`, and GS result `1.95`, envelope `[0.94,8.98]`, but later reverts to linear/unphysical values as “canonical” or headline: `8.27 ± 2.37`, 95% `[3.62,12.95]`, and `2.28 ± 7.43` with negative lower bound. Appendix C still uses linear scaling in `α`.  
**Fix:** Delete all linear-propagated headline/error-bar language and recompute Appendix C under `1/σ^2=F0+cα^2`; retain linear values only in a clearly labeled historical note, not as forecast intervals.

## PAPER-GPT-M1

**Classification:** MAJOR  
**Section:** §2.2 threshold policy; Table I caption/footnotes; §3.2 SDSS  
**Issue:** SDSS thresholds and rates are internally inconsistent. `77,905` is called a top-1%/top-percentile native slice at `S≥0.1060`, but it is `4.05%` of the actually scored `1,925,279` spectra and `3.38%` of the nominal `2,304,830`; §3.2 says the native top-1% is instead `19,253` at `S≥0.2051`.  
**Fix:** Split SDSS into explicit rows/counts: cross-transfer `77,905/2,304,830`, native continuity `77,905/1,925,279`, native top-1% `19,253`, and native `S>5` `12`; choose one primary threshold and stop labeling `S≥0.1060` as top-1%.

## PAPER-GPT-M2

**Classification:** MAJOR  
**Section:** Table I; §3.5 Planck CMB; §7 scale claim  
**Issue:** Planck Path-C denominator is inconsistent. Table I reports `20,000` patches and `200` anomalies as `1.00%` top-1%, but §3.5 says the native model scores `2×10^5` patches and selects the top `200`, i.e. `0.1%` near the 99.9th percentile. The total processed volume `37.3M` also appears to keep the obsolete `20,000` denominator.  
**Fix:** Decide whether the primary Planck catalog is the 20k cross-transfer scan or the 200k native scan; update `N_total`, anomaly rate, total processed count, and all “top-1%” language accordingly.

## PAPER-GPT-M3

**Classification:** MAJOR  
**Section:** §5.2 NANOGrav; Appendix “PTA MCMC documentation”  
**Issue:** The PTA “likelihood” multiplies per-frequency KDE posterior densities as independent likelihood factors. These KDEs are marginal posteriors with priors and inter-bin covariance already folded in; the product is not the joint likelihood, so the quoted `γ=2.567±0.382`, `4.61σ` SMBHB parameter-shift, and “strongly disfavored” language are not methodologically secure.  
**Fix:** Use a joint free-spectrum likelihood/sample product with covariance and prior/Jacobian correction, or raw timing likelihood; until then, remove quantitative exclusion language and report the PTA result as an illustrative, non-model-comparison diagnostic only.
