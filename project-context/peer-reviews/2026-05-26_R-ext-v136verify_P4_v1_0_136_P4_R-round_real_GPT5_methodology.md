# P4 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-v136verify_P4_v1_0_136
**Wall time**: 91.9s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=104201, completion=5653, reasoning=4508, total=109854

---

## PAPER-GPT-B1 — BLOCKER

**Location:** §III “Declared Analysis Hierarchy”; §IV “Dipole Analysis”; Table `tab:face_on`; Table `tab:l1_estimators`  
**Issue:** The same Catalog C dipole channel is reported as `+0.43σ`, `-0.12σ`, `+3.64σ`, and `+4.31σ/+4.43σ` depending on mask/estimator/null, with “different estimator” used as reconciliation. This is not a coherent primary data vector; the null headline is estimator-selection dependent.  
**Fix:** Define one primary mask/map/null/estimator and report all variants under the same null calibration. If the full-sample LSQ `+4.31σ` persists, the headline must be reframed around estimator-dependent systematics, not a clean null.

## PAPER-GPT-M1 — MAJOR

**Location:** §III.E / §`sec:tta`, paragraph “Hard-label variance widening from the 21.4% argmax-flip rate”; Table `tab:data_vectors` caption/footnote c  
**Issue:** The XOR flip variance derivation is wrong. For `x_obs=x_true XOR f`, `Var(x_obs)=q(1-q)+(1-2q)^2p(1-p)`, not `p(1-p)+q(1-q)`; at `p≈0.5` the marginal observed Bernoulli variance is ≈0.25, not inflated by `sqrt(1.672)=1.29`. The adopted `1+p_flip=1.214` factor is also not “more conservative” than 1.29 and has no derivation from this model.  
**Fix:** Replace with a correct law-of-total-variance derivation and state whether the target is observed-label variance or deattenuated true-label amplitude. If deattenuating, propagate the appropriate `(1-2q)^{-1}`-type factor or fit an empirical nuisance model.

## PAPER-GPT-M2 — MAJOR

**Location:** Tables `tab:confidence_bins`, `tab:mc_injection`, `tab:face_on`; §`sec:tta` hard-label note  
**Issue:** The paper says the 21.4% D4 argmax-flip uncertainty is propagated into all hard-label diagnostics, but the tables only show one set of sigmas/probabilities with no raw-vs-inflated values. A 1.21 or 1.29 widening would move several “~3σ” hard-bin claims below threshold and alter injection-recovery thresholds.  
**Fix:** Add adjusted columns or recompute the nulls with a D4/flip nuisance model. Update all claims using the adjusted sigmas/detection probabilities.

## PAPER-GPT-M3 — MAJOR

**Location:** Abstract; §`sec:sensitivity`; §`sec:monopole_mask_null` “Full-catalog injection-recovery sensitivity”; Conclusions item 1/falsification criterion  
**Issue:** Sensitivity claims are internally inconsistent. The HC sweep says `A=0.5%` is a non-detection and `0.75%` is the 50%-recovery threshold, while the new full-catalog sweep says `A=0.5%` gives 86% recovery with median `+12.62σ`; later text still says a full-catalog injection sweep is deferred. The `+12.62σ` at 0.5% is also not reconciled with the Fisher full-catalog expectation of order `~5σ`.  
**Fix:** Separate HC and full-catalog sensitivity everywhere, delete the stale “deferred” language, and reconcile the full-catalog injection metric with the Fisher/amplitude convention. Use one declared sensitivity in the abstract and falsification criterion.

## PAPER-GPT-M4 — MAJOR

**Location:** Table `tab:headline_summary` footnote b; §`sec:hemisphere`; §`sec:conclusions` canonical-MASTER paragraph  
**Issue:** Moment-z values and empirical-rank p-values are mixed as if interchangeable. Example: canonical `+3.64σ` has empirical `p_MC=15/500=0.030`, not a calibrated 3.64σ tail. Similarly, hemisphere `0/10000` exceedances is an MC-resolution statement, not a measured `p≤10^{-4}` discovery-level tail.  
**Fix:** Use empirical-rank p-values with binomial confidence intervals as the primary significance, or run enough MC/tail modeling to support Gaussian-equivalent sigmas. Stop quoting moment-z as detection significance for non-Gaussian MC nulls.

## PAPER-GPT-M5 — MAJOR

**Location:** §`sec:monopole_mask_null`; §`sec:dipole_symmetry_caveat`; Conclusions “remaining 88% requires depth/PSF/morphology”  
**Issue:** The “12% monopole-only / 88% requires depth/PSF/morphology” statement is a parameter-shift decomposition, not a nuisance-marginalized likelihood or variance budget. Cross-spectrum and leg-proxy diagnostics are suggestive, but they do not establish an additive systematic budget or exclude a mixed primordial+systematic model.  
**Fix:** Rephrase to “monopole-only does not explain the residual.” Defer quantitative allocation until a joint fit marginalizing over primordial dipole plus depth/PSF/morphology templates is performed.
