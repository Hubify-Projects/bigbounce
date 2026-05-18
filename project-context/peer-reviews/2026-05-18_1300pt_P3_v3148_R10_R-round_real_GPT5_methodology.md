# P3_v3148_R10 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1300pt
**Wall time**: 166.7s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=62946, completion=9045, reasoning=7434, total=71991

---

## PAPER-GPT-B1 — BLOCKER — Fisher-positivity correction not propagated

**Location:** Abstract; §5 “Cosmological Applications”; Conclusions item 5; Appendix “Sensitivity to Bias Enhancement”; §6.4 caveats (i,j).  
**Issue:** The caveat (j) arithmetic is now internally consistent: with \(F_0=1/8.98^2\simeq0.01240\), \(c\simeq0.0747\), \(\sigma(\alpha)=(F_0+c\alpha^2)^{-1/2}\), the GS remap is \(\alpha=1.83\pm2.03\Rightarrow [0.94,8.98]\) centered at \(1.95\). But the abstract/§5/conclusions still quote the unphysical linear result \(\sigma^{\rm GS}_{f_{\rm NL}}=2.28\pm7.43\), and §5 still quotes the full-sample linear 95% interval \([3.62,12.95]\) plus a \(+1\sigma\) tail \(10.64>8.98\), contradicting the positivity-respecting form where the upper bound is the single-tracer baseline \(8.98\).  
**Fix:** Replace all abstract/§5/conclusion Fisher intervals with positivity-mapped envelopes: full-sample 95% \(\sigma(f_{\rm NL})\in[2.41,8.98]\) for \(\alpha\in[-1.084,1.464]\), and GS \(1\sigma\) \([0.94,8.98]\) centered \(1.95\). Remove or relabel \(\pm2.37\) and \(\pm7.43\) as local linear diagnostics only, not physical confidence intervals; update Appendix sensitivity table instead of using stale linear scaling to \(\alpha=0.50\).

## PAPER-GPT-B2 — BLOCKER — Headline dedup count remains arithmetically unsupported

**Location:** Title; Abstract; Table 1 footnote \(\|\); §4.3 “Cross-Survey Matches”; Conclusions item 8; Data availability.  
**Issue:** The paper claims \(388{,}493\) survey-level detections collapse to \(378{,}280\) unique objects, requiring \(10{,}213\) duplicate-detection removals. But §4.3 reports only \(637\) all-pairwise multi-survey coincidences and no triples, which collapses to \(388{,}493-637=387{,}856\), leaving \(9{,}576\) removals unexplained.  
**Fix:** Produce the union-find manifest with cluster-size histogram and intra-survey duplicate accounting that sums exactly to \(10{,}213\). Until then, remove exact \(378{,}280\) from title/abstract/conclusions or explicitly mark it pending recompute and quote \(387{,}856\) as the pairwise-supported upper bound.

## PAPER-GPT-M1 — MAJOR — DESI OOD MSE validation contradicts the stated \(S>5\) threshold

**Location:** §2.2 “In-sample scoring and held-out validation”; §6.4 deferral (b).  
**Issue:** DESI \(S>5\) is stated to correspond to MSE \(\sim0.143\), but the independent 100k OOD sample has median MSE \(0.178\). If these are on the same scale, more than half the OOD sample exceeds the catalog threshold, not the claimed preserved \(0.87\%\) anomaly rate; if they are not on the same scale, the comparison is invalid.  
**Fix:** Report \(\mu_{\rm val}\), \(\sigma_{\rm val}\), the exact threshold \(T=\mu_{\rm val}+5\sigma_{\rm val}\), and the OOD exceedance fraction in the same preprocessing/MSE units. Delete “0.87% preserved” until the threshold-in-OOD-units audit is shown.

## PAPER-GPT-M2 — MAJOR — DESI 5-fold Jaccard narrative is still mathematically inconsistent

**Location:** Abstract; §2.2 “In-sample scoring and held-out validation”; §6.4 caveats (g) and (i); Conclusions item 7.  
**Issue:** The abstract says each fold scores the full 47k pool, making top-1% sets of 470 and union 546 feasible. But §2.2 and caveat (i) still say each fold scores only its disjoint 9,400 held-out split; then each top-1% set has 94 objects, the maximum union is 470, pairwise Jaccard across disjoint held-out IDs should be zero, and “399 appear in all five folds” is impossible.  
**Fix:** Pick one scoring convention and make every section match it. If full-pool scoring was used, remove “held-out-only” language; if held-out-only was used, recompute stability with a valid metric and discard the 546/399 numbers.

## PAPER-GPT-M3 — MAJOR — Spectroscopic threshold policy is internally inconsistent and changes the catalog size

**Location:** §2.2 threshold paragraph; Table 1 caption/footnotes \(\ddagger,\heartsuit,\spadesuit\); §3.2 SDSS; §3.3 LAMOST; Abstract; Conclusions.  
**Issue:** The paper repeatedly says spectroscopic surveys use a fixed canonical \(S>5\) threshold, but the headline Path-C counts use SDSS \(77{,}905\) at \(S\ge0.1060\) while only \(12\) pass \(S>5\), and LAMOST \(113{,}342\) at \(S\ge0.4613\) while only \(2{,}054\) pass \(S>5\) and the detector fails the \(5\sigma\) gate. The “catalog-grade \(\sim265{,}000\)” number depends on these non-\(S>5\), partly exploratory continuity slices.  
**Fix:** Split strict-\(S>5\) validated counts from percentile/continuity/exploratory slices in the main table. Recompute headline and catalog-grade subset under the declared threshold, or stop calling SDSS/LAMOST headline counts \(S>5\) catalog-grade anomalies.

## PAPER-GPT-M4 — MAJOR — Planck native count/rate uses two incompatible sample sizes

**Location:** Table 1 Planck row and total \(N_{\rm total}\); §3.5 “Planck CMB”; §2.3 Path-C Step 2; Abstract/Conclusions scale claims.  
**Issue:** Table 1 keeps Planck at \(N_{\rm total}=20{,}000\), \(N_{\rm anom}=200\), rate \(1.00\%\). But the Path-C native retrain/re-score says the full \(2\times10^5\)-patch set was scored and the top 200 were selected, which is \(0.10\%\), not \(1\%\), and would increase the total processed count by \(180{,}000\).  
**Fix:** Either publish a 20k native-scored Planck set with top-1% selection, or update Table 1 and all totals to \(200{,}000\) Planck patches, rate \(0.10\%\), and revised total processed count.
