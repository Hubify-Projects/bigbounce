# P5 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-strict_P5_v0_1_31
**Wall time**: 106.4s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=26425, completion=6674, reasoning=5563, total=33099

---

## PAPER-GPT-B1 — BLOCKER

**Section:** Preamble comments; Abstract robustness paragraph; §Tempel; Conclusions.  
**Issue:** The source and rendered manuscript contain audit/vendor/version contamination: “cron fire,” “5-VENDOR,” “GPT-5 reviewer failed,” “Truth-audit,” “per R-ext-GRO-M2,” and “R-ext-GRO-min1.” The date/version metadata are also inconsistent (`v0.1.31-2026-05-25` vs `May 24, 2026 PDT`).  
**Fix:** Purge all review/audit/vendor/version-history prose from source and body. Keep only scientific provenance and align or remove submission version/date tags.

## PAPER-GPT-B2 — BLOCKER

**Section:** Table I; §Results/Table II; §Phase 2; §T-Web/DESIVAST residual discussion.  
**Issue:** The headline data vector is arithmetically inconsistent. Table II environment counts sum to 812,793 and CW counts to 404,111, but the declared chirality sample is 791,635 with 393,592 CW; §Phase 2 then quotes a filament bin with `n=3,696,152`, exceeding the matched and chirality samples. The canonical range is 1.98 pp in Table II but 0.165 pp for the same `(25,0)` cell in Phase 2.  
**Fix:** Add a data-vector definition table for every analysis sample and regenerate every table/figure from one frozen cut flow. Do not mix the 791,635 sample with the later 812,793 superset.

## PAPER-GPT-B3 — BLOCKER

**Section:** §V-Web cosmic-web classification; §Limitations; §Concurrent-literature comparison.  
**Issue:** The claimed “V-Web” is not V-Web: the algorithm computes a density-potential tidal tensor, i.e. T-Web, not a velocity-shear V-Web. It also uses raw flux-limited redshift-space DESI counts in a periodic FFT cube with a global mean and ad hoc dilated mask, without radial selection/random correction or boundary treatment; the DESIVAST 0/6 void agreement demonstrates the canonical void labels are not reliable cosmic voids.  
**Fix:** Rename as T-Web or implement a true velocity-shear V-Web. Rebuild the density field with volume-limited/weighted tracers, survey randoms, mask-aware boundary treatment, and mock validation, or make an official DESI/DESIVAST environment catalog the primary classifier.

## PAPER-GPT-B4 — BLOCKER

**Section:** §Statistical methods; §Results; §Discussion/Conclusions.  
**Issue:** “Statistically independent,” “clean null,” and “entirely driven by the monopole” are overclaims. The paper uses σ-from-0.5 plus post-hoc fixed Paper IV/P5 monopole subtraction, not a joint nuisance-marginalized likelihood over environment, imaging leg, DESI program, redshift, confidence, match radius, and environment-assignment uncertainty; a `-4.66σ` cluster bin and `≈3.4σ` bright/dark filament sign flip cannot be dismissed descriptively.  
**Fix:** Fit a predeclared hierarchical/logistic model with a global chirality monopole and nuisance terms, test environment coefficients jointly, and propagate Paper IV/P5 monopole uncertainty and covariance. Until then, weaken all independence/upper-bound language.

## PAPER-GPT-B5 — MAJOR

**Section:** §Statistical methods/LEE; §Redshift; §HEALPix; §Systematics.  
**Issue:** Empirical max-stat p-values are based on only 1,000 shuffles while the paper claims α=0.01/3σ look-elsewhere control; the tail resolution and p99 estimates are inadequate. The nulls are also non-commensurate: binomial-from-half, label-shuffle, position-shuffle, monopole-subtracted residuals, and Paper IV MASTER results are mixed without a declared primary cosmological null and systematics-preserving null.  
**Fix:** Declare one primary cosmological null and one systematics-preserving null. Use ≥10⁴ permutations minimum, preferably ≥10⁵ for 3σ tails, report MC uncertainty, and demote all other nulls to diagnostics.

## PAPER-GPT-B6 — MAJOR

**Section:** §Tempel cross-validation; Abstract robustness; §Systematics.  
**Issue:** The robustness claims are non-commensurate and internally contradictory. The “0.026 pp concordance” compares V-Web filament on the full DESI matched sample to Tempel SDSS-overlap galaxies with different footprint, redshift range, and class definition, not a paired classifier validation; §Systematics says BGS vs LRG/ELG/QSO differs by <0.001 while the abstract/§Results report bright 0.4970 vs dark 0.5051 and a filament `|z|≈3.4` opposite-sign split.  
**Fix:** Recompute cross-classifier comparisons on identical galaxies and cuts with paired two-sample tests. Reconcile the DESI-program split, include it in the nuisance/error budget, and remove arbitrary “0.2 pp spec”/“load-bearing” validation language.
