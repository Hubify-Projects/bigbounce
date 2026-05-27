# P3 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-27_R-ext-maint-v2_P3_v3_1_63
**Wall time**: 116.1s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=68961, completion=6499, reasoning=5425, total=75460

---

## PAPER-GPT-B1 — BLOCKER

**Section:** Table I; §3 Planck CMB; Abstract/Conclusions totals  
**Issue:** Planck Path-C is internally inconsistent: Table I uses `N_total=20,000`, `N_anom=200`, rate `1.00%`/top-1%, but §3 says the native Planck model rescored `2×10^5` patches and selected the top 200, which is `0.1%`, not `1%`. The headline processed total `37,272,042` is therefore off by `180,000` if the native Planck run is canonical.  
**Fix:** Choose the canonical Planck sample size. Update Table I, processed totals, anomaly rate, “top-1%” language, abstract/conclusion counts, and released artifact descriptions consistently.

## PAPER-GPT-B2 — BLOCKER

**Section:** Abstract; §5; §6 Limitations/Caveats; §7; Appendix Sensitivity  
**Issue:** The `σ(f_NL)` uncertainty propagation is contradictory. §5 first adopts the Fisher-positivity envelope `σ=8.14 [3.92,8.98]`, then calls the invalid local-linear `8.27±2.37` / `[3.62,12.95]` interval “canonical”; conclusions still headline `8.27±2.37` and GS `2.28±7.43`, while caveat (i) says that linear mapping violates Fisher positivity. Appendix sensitivity also retains the invalid linear scaling.  
**Fix:** Remove the linear intervals from all headline/conclusion sites. Propagate the full `α` posterior through the exact multi-tracer Fisher form including shot noise and nuisance/systematics marginalization, or report only a central zero-systematics sensitivity with no credible-interval claim.

## PAPER-GPT-M1 — MAJOR

**Section:** §2.2 In-sample scoring vs §6.4 caveat (i)  
**Issue:** §2.2 still says each fold “scores the held-out 20% (9,400 spectra)” while reporting `546` union objects and `399` appearing in all five folds. Those counts are impossible for disjoint held-out top-1% sets (`5×94=470` total memberships). Later caveat text says the full 47,000 pool was scored per fold, contradicting §2.2.  
**Fix:** Rewrite §2.2 to state that each fold model scores the full 47,000-object pool, or recompute Jaccard statistics using true held-out-only folds.

## PAPER-GPT-M2 — MAJOR

**Section:** §2.2/Table I caption and footnotes; §3 eROSITA  
**Issue:** The eROSITA catalog axis is inconsistent. The methods/table describe eROSITA as an IsolationForest/raw-score detector with a cut near `S>0.259`, while §3 states the published 298-source catalog is defined on BigAE canonical z-scored MSE and IF is only a diagnostic. The quoted 81.5% stability is for an IF top-1% set, not demonstrably for the published BigAE top-298.  
**Fix:** Define one published eROSITA detector/score axis. Recompute validation on that same axis or provide the exact BigAE-top-298 ∩ IF-top-9303 intersection and label the two score systems separately everywhere.

## PAPER-GPT-M3 — MAJOR

**Section:** Abstract; Table I; §3; §6.4; §7  
**Issue:** The `378,280 unique anomalies` headline combines incompatible threshold policies and validation states: SDSS uses a bookkeeping top-77,905 slice at the 96th percentile, LAMOST contributes a gate-failed top-1% exploratory slice, Gaia is explicitly exploratory at 41% stability, and eROSITA fails injection recovery. The “catalog-grade ∼265k” split is also arithmetically ambiguous: the abstract excludes Planck, while the table footnote’s exact `264,938` includes the 200 Planck patches.  
**Fix:** Separate “validated/catalog-grade” and “exploratory/top-percentile candidate” catalogs with exact deduplicated counts and thresholds. Do not present the combined gate-failed/top-percentile aggregate as a single anomaly catalog.

## PAPER-GPT-M4 — MAJOR

**Section:** §5.2 NANOGrav; Appendix PTA MCMC  
**Issue:** The PTA likelihood is a product of marginal per-bin posterior KDEs, ignoring inter-bin covariance and prior/Jacobian corrections; it is not a valid joint likelihood for model comparison or robust parameter-shift significance. Despite disclaimers, the paper still concludes SMBHB is “strongly disfavored” at `4.61σ` and bounce is favored by smaller deviation.  
**Fix:** Remove “strongly disfavored/favored” language. Either keep the PTA result as illustrative only or compute a proper joint free-spectrum/PTA likelihood with covariance and amplitude priors marginalized before quoting sigma or Bayes-factor-style comparisons.
