# P3_v3145_R7 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1100pt
**Wall time**: 145.7s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=59760, completion=8854, reasoning=7756, total=68614

---

## PAPER-GPT-B1 — BLOCKER

**Section:** Title; Abstract; Table 1 footnote; §4.3; §6.4(a); Conclusions; Data availability  
**Issue:** The paper still headlines **378,280 unique anomalies** as a settled catalog count while §4.3/§6.4(a) admits the arithmetic only supports `388,493 - 637 = 387,856` unless an unverified extra **9,576** intra-survey duplicate collapse exists. This is not a caveat; it invalidates the exact headline/title/count.  
**Fix:** Recompute and publish the union-find cluster manifest with intra-/inter-survey duplicate cardinalities, then update every headline/table/file row count. Until then, replace 378,280 with a range or the arithmetic upper bound 387,856 and remove “unique physical objects” claims.

## PAPER-GPT-B2 — BLOCKER

**Section:** Abstract; §2.2 “In-sample scoring and held-out validation”; §6.4(i)  
**Issue:** The DESI 5-fold stability protocol is internally impossible as written. Abstract says each fold scores the full 47,000 pool with top-1% sets of 470; §2.2/§6.4(i) say each fold scores only its disjoint 9,400 held-out split, in which case top-1% sets have 94 objects, pairwise Jaccard across folds is zero by construction, and “399 appear in all five folds” cannot occur.  
**Fix:** State the actual evaluation population. If full-pool scoring was used, remove “held-out” robustness claims; if held-out-only was used, recompute stability on a common independent evaluation set.

## PAPER-GPT-M1 — MAJOR

**Section:** §2.2 DESI OOD validation; §6.4(b)  
**Issue:** The OOD MSE normalization remains mathematically inconsistent. The claimed DESI threshold is MSE ≈ 0.143, but the 100k OOD median MSE is 0.178; on the same scale, more than half the OOD sample should exceed threshold, contradicting the claim that the 0.87% anomaly rate is preserved.  
**Fix:** Report the OOD fraction above the exact production threshold after identical preprocessing and Eq. 2 standardization. If scales differ, give the explicit conversion; otherwise remove the preserved-rate claim.

## PAPER-GPT-M2 — MAJOR

**Section:** Table 1 caption/footnotes; §2.2; §3.2–§3.5; Abstract tier split  
**Issue:** Catalog counts and thresholds are not internally consistent. Table 1 says spectroscopic surveys use fixed `S>5`, but SDSS headline 77,905 uses `S≥0.1060` while `S>5` gives 12, and LAMOST headline 113,342 uses p99 `S≥0.4613` while `S>5` gives 2,054; Planck is listed as 20,000 patches / 1.00%, but the native result is top 200 from 200,000 patches = 0.10%. The table footnote also gives an exact 264,938 catalog-grade tier including Planck map patches, contradicting the abstract’s approximate point-source-only ~265k split.  
**Fix:** Add an explicit threshold/count column per survey and recompute totals/rates from those exact cuts. Keep point-source catalog-grade counts separate from Planck patches and from LAMOST exploratory rows.

## PAPER-GPT-M3 — MAJOR

**Section:** §5; §6.4(c)  
**Issue:** The Fisher CI fix is not propagated: §5 correctly retracts the asymmetric envelope and gives `[3.64, 12.93]`, but §6.4(c) still tells readers to use the stale asymmetric `[5.91, 12.92]`. Also, the “0.06σ agreement” with fiducial α is over-interpreted as tight agreement despite α being consistent with zero with huge uncertainty.  
**Fix:** Replace §6.4(c) with the current `[3.64, 12.93]` linear-propagation interval and state that ±2.37 propagates only α, not observational/theoretical systematics. Remove language implying evidential support for the fiducial α from a broad null-consistent measurement.

## PAPER-GPT-M4 — MAJOR

**Section:** §3.4 eROSITA; Table 1 footnote §; §6.4(v)/(f)  
**Issue:** The BigAE-vs-IsolationForest “strict subset/superset” regression reappears. §3.4/Table soften to “high overlap” and defer the intersection count, but §6.4(v) again calls the IF top-9,303 “a strict superset” of the BigAE top-298 without verification.  
**Fix:** Publish the intersection table: `|BigAE top-298 ∩ IF top-9303|`, fraction of 298 recovered, and rank distribution. Until then, use only “unverified high-overlap candidate,” not strict subset/superset.
