# P4 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-v137verify_P4_v1_0_137
**Wall time**: 92.0s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=105750, completion=5492, reasoning=4508, total=111242

---

## PAPER-GPT-B1 — BLOCKER

**Section:** v1.0.137 note / §VI.D joint nuisance-marginalized fit  
**Issue:** The joint fit is called “canonical-mask” but uses `n=36,418` NSIDE=64 pixels, implying `f_sky=0.741`, while the canonical mask elsewhere is `24,087` pixels / `f_sky=0.49005`, and the subsample mask is `32,388` pixels / `f_sky=0.659`. This is a different data vector, so the claimed exclusion of the canonical-mask `1.7%` interpretation is not established.  
**Fix:** State the exact mask used by the regression, its `N_pix`, `f_sky`, and selection rule; rerun on the stated canonical mask or relabel the result and recalibrate the `1.7%` reference for that mask.

## PAPER-GPT-B2 — BLOCKER

**Section:** §VI.D joint nuisance-marginalized fit  
**Issue:** The “formal exclusion at 99%” and `z=-264.5` are based on a naive weighted linear-regression covariance with galaxy-count weights, not a validated likelihood with spatial/systematics covariance, template uncertainty, or model-misspecification error. Comparing `0.23% ± 0.006%` to `1.7%` is not a proper profile likelihood / marginalized posterior test of a fixed-amplitude dipole over all directions and nuisance parameters.  
**Fix:** Use GLS or MC-calibrated covariance preserving depth/PSF/morphology correlations; compute a profile likelihood or posterior for fixed `A=1.7%` over dipole direction and nuisance coefficients; quote empirical p/CI, not the `264σ` number.

## PAPER-GPT-B3 — BLOCKER

**Section:** `\artifact{}` macro / Data Availability  
**Issue:** All artifact links are hardcoded to release tag `paper4-v1.0.134`, but the new v1.0.137 joint-fit result cites `joint_nuisance_model_fit.json` and script outputs that cannot be available under that older immutable tag. The v1.0.137 “external clean” result is therefore not reproducible from the cited release.  
**Fix:** Create and cite an immutable `paper4-v1.0.137` release containing the new JSON/script artifacts, update `\artifact{}` and Data Availability, and verify every new link resolves.

## PAPER-GPT-M1 — MAJOR

**Section:** §III.E / hard-label variance widening paragraph  
**Issue:** The XOR flip derivation is wrong: for `x_obs=x_true⊕f`, the observed Bernoulli variance is `p_obs(1-p_obs)`, with signal attenuation by `(1-2p_flip)`, not `p(1-p)+p_flip(1-p_flip)`. The quoted `1.21×`/`1.29×` sigma widening is unsupported.  
**Fix:** Re-derive the misclassification model via the law of total variance and propagate attenuation separately from sampling variance, or replace the analytic factor with an empirical calibration only.

## PAPER-GPT-M2 — MAJOR

**Section:** §VI.D anchor block / §VIII Sensitivity / Conclusions  
**Issue:** Sensitivity claims conflict: one paragraph says the full-catalog injection sweep gives `≤0.50%` 50%-recovery with `86%` recovery at `0.5%`, while later text says a full-catalog sweep is deferred and the falsification criterion uses the HC-subsample `0.75%` threshold. The systematic budget and headline sensitivity are not internally defined.  
**Fix:** Choose one canonical sensitivity data vector; tabulate full-catalog and HC thresholds separately with identical amplitude convention, mask, null, `N_MC`, and pixel cuts; remove “deferred” or remove the full-catalog claim.

## PAPER-GPT-M3 — MAJOR

**Section:** §VI.D joint nuisance design matrix  
**Issue:** The design matrix is rank-deficient because the three leg fractions plus a constant satisfy `f_BASS+f_DECaLS+f_DES=1`; the nullity is one, not “three-dimensional,” and no rank/condition diagnostics are reported. The fit also claims depth/PSF/morphology marginalization while including only leg fractions, density, and density².  
**Fix:** Drop one leg column or impose a sum-to-zero constraint; report weighted rank, condition number, and dipole-template correlations; either include the full PSF/morphology template basis or narrow the claim to density/leg nuisance only.
