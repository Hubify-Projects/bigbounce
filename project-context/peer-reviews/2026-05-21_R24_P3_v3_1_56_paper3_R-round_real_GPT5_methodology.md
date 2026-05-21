# paper3 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-21_R24_P3_v3_1_56
**Wall time**: 140.2s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=66809, completion=7615, reasoning=6503, total=74424

---

## PAPER-GPT-B1

**Classification:** BLOCKER  
**Location:** Abstract; §5; §6.4 caveats (c),(i),(j); Conclusions item 5  
**Issue:** Fisher-positivity fix is not propagated. The paper alternates between canonical `σ(f_NL)=8.14, [3.92,8.98]`, noncanonical `8.27±2.37`, 95% `[3.62,12.95]`, caveat `[2.4,8.98]`, and GS `2.28±7.43` despite admitting the linear mapping is unphysical.  
**Fix:** Make the α² Fisher mapping the only canonical result everywhere; quote full-sample `8.14` with its mapped interval and GS `1.95 [0.94,8.98]`. Move all linear `8.27±2.37` / `2.28±7.43` values to a clearly labeled historical/noncanonical note or delete them.

## PAPER-GPT-B2

**Classification:** BLOCKER  
**Location:** §2.2; Table I caption/footnotes; §3.2 SDSS; Conclusions item 8  
**Issue:** The SDSS threshold policy is internally inconsistent and changes the headline catalog size. §2.2 says SDSS uses absolute `S>5`, Table I uses `77,905` at `S≥0.1060`, and the caption calls that “top-1%” even though `77,905/1,925,279=4.05%`; the actual top-1% is `19,253` at `S≥0.2051`.  
**Fix:** Define one canonical SDSS threshold before counting, then recompute the `388,493 → 378,280` dedup headline. If `77,905` is retained only for continuity bookkeeping, keep it out of the primary Path-C total.

## PAPER-GPT-B3

**Classification:** BLOCKER  
**Location:** §2.2 “In-sample scoring and held-out validation”; §6.4(i)  
**Issue:** DESI 5-fold validation is still self-contradictory. §2.2 says each fold scores only its held-out `9,400` spectra, but then reports `470` top-1% objects per fold, union `546`, and `399` objects appearing in all five folds; held-out-only folds would have `94` objects each and disjoint object sets.  
**Fix:** Rewrite §2.2 to match §6.4(i): each fold-trained model scores the full `47,000`-spectrum pool for the Jaccard statistic. If held-out-only validation is desired, compute and report it separately.

## PAPER-GPT-M1

**Classification:** MAJOR  
**Location:** §4.3 Cross-Survey Matches; §6.4(a); Table I footnote `^\|`  
**Issue:** The `637 + 9,576 = 10,213` arithmetic is correct, but the interpretation of all `9,576` residual collapses as “intra-survey duplicates / same physical objects” is only by subtraction. A 5″ same-survey FoF merge can also collapse distinct close pairs, blends, crowded-field sources, or repeated pipeline entries without proving physical identity.  
**Fix:** Publish the same-survey cluster manifest with survey, source IDs, separations, cluster sizes, and observation/tile provenance; estimate same-survey chance-collapse rates. Until then call the result “5″ positional clusters,” not “unique physical objects,” or propagate the ambiguity.

## PAPER-GPT-M2

**Classification:** MAJOR  
**Location:** Abstract; Table I; §3.4 Planck; Appendix E  
**Issue:** The retained-survey denominator is inconsistent. Path-C Planck native retrain scores `2×10^5` patches, but Table I and the Path-C total use the old `20,000` Planck-patch denominator (`37,272,042`); using the native Planck denominator gives `37,452,042`. The cross-transfer total `37,292,042` also includes quarantined ACT despite repeated “ACT excluded” framing.  
**Fix:** Choose one denominator for the primary Path-C catalog: six point-source surveys plus the native Planck patch count, ACT excluded. Update title/abstract/table/rates, and keep ACT only in the appendix/sensitivity file.

## PAPER-GPT-M3

**Classification:** MAJOR  
**Location:** §5.2 NANOGrav Bounce Consistency; Appendix D′ likelihood  
**Issue:** The PTA “likelihood” is a product of 1D free-spectrum posterior KDEs, assuming independent bins and not undoing priors/Jacobians; this is not a valid joint data likelihood. The paper correctly says it is not a Bayes factor, but still quotes formal `γ=2.567±0.382` and “SMBHB 4.61σ strongly disfavored” as if the covariance/prior problem were harmless.  
**Fix:** Either evaluate the official joint likelihood / chain with covariance and priors, or downgrade the result to an illustrative posterior-shape fit and remove formal exclusion / parameter-shift significance language.
