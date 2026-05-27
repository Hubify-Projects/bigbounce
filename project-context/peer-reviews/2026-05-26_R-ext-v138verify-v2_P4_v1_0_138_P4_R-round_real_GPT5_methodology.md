# P4 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-v138verify-v2_P4_v1_0_138
**Wall time**: 190.4s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=106586, completion=6820, reasoning=5696, total=113406

---

## PAPER-GPT-B1 — BLOCKER

**Location:** Abstract; Sec. “Dipole Analysis”; Sec. “Edge-On Galaxy Contamination”, Table `face_on`.  
**Issue:** The same Catalog C full-sample dipole is reported as `+0.43σ, p=0.30` and also as `+4.31/+4.43σ, p=0.001`. The explanation “different estimators/nulls” is not acceptable for a headline null claim; a valid `4σ` dipole estimator is either a detection or an unmodeled systematic.  
**Fix:** Freeze one primary real-space dipole data vector with explicit mask, weights, monopole subtraction, and null. Recompute all robustness rows under that same definition or remove the incompatible `+4.31σ` table row.

## PAPER-GPT-B2 — BLOCKER

**Location:** Sec. “Monopole+Mask Leakage Generative Null”, joint nuisance-marginalized fit paragraph.  
**Issue:** The claimed nuisance-marginalized dipole error `σ(A_dipole)=1.11e-4` in `A_p` units is below the binomial Fisher floor: for `A_p=2f_CW-1` and `N=3,201,160`, `σ_A ≥ sqrt(3/N)=9.7e-4` before mask/systematics inflation. The resulting `250σ` / “formally excluded” claim is a parameter-shift artifact, not a valid marginalized likelihood result.  
**Fix:** Use a binomial/overdispersed pixel covariance or full GLS covariance, include spatial correlations, and profile/marginalize over the 3-component dipole vector plus nuisance templates. Delete the `250σ` and “formal exclusion” language until this is redone.

## PAPER-GPT-B3 — MAJOR

**Location:** Sec. “Sensitivity Floor”; v1.0.135 full-catalog injection-recovery paragraph; Conclusions falsification criterion.  
**Issue:** The full-catalog injection claim that `A=0.5%` gives median `σ=+12.62` is not reconciled with the paper’s own Fisher scaling: for `N=3.20M`, a full-amplitude `0.5%` dipole is only `~5.2σ` in the ideal amplitude estimator before mask losses. This indicates an amplitude-convention, null-variance, or statistic mismatch.  
**Fix:** Re-audit the injection code and state whether `A` is in `f_CW`, `A_p`, half-modulation, or power-spectrum units. Quote sensitivity/falsification thresholds only from a validated like-for-like amplitude estimator.

## PAPER-GPT-M1 — MAJOR

**Location:** Sec. “Test-Time Equivariant Averaging”, hard-label variance widening paragraph; Table `headline_summary` footnote c.  
**Issue:** The `21.4%` argmax-flip variance propagation is mathematically wrong. For an XOR flip model, `q=e+(1-2e)p`; near `p=0.5` the marginal binomial variance is not inflated by `p_flip(1-p_flip)/(p(1-p))`, while deconvolving to the true fraction inflates variance by `(1-2e)^{-2}` and dilutes signal by `(1-2e)`. The adopted `1.21×` factor has no valid derivation.  
**Fix:** Re-derive using a 2×2 confusion matrix and propagate both signal dilution and variance inflation consistently. Update all hard-label diagnostic error bars.

## PAPER-GPT-M2 — MAJOR

**Location:** Sec. “Hemisphere Asymmetry”; Table `headline_summary` footnote d; Conclusions.  
**Issue:** MC p-values are over-interpreted. “Zero of 10,000 nulls” is an MC-resolution statement, not a measured `p≤1e-4` detection; the 95% upper limit is `~3e-4`, and converting this to `>3.7σ` as a rejection overstates precision. Similarly, `moment-z=3.64` is repeatedly juxtaposed with empirical `p_MC=15/500=0.030` as if both were calibrated significances.  
**Fix:** Use rank p-values with finite-MC confidence intervals, e.g. `(k+1)/(N+1)` plus binomial CI. Do not quote Gaussian-equivalent sigmas unless the null tail is validated or MC is large enough.

## PAPER-GPT-M3 — MAJOR

**Location:** Table `multipole`; Sec. “NaMaster MASTER configuration”.  
**Issue:** The power-spectrum table mixes incompatible data vectors: the `ℓ=1` row uses the subsample mask/null, while higher rows use canonical-mask bandpowers with different MC/null treatment; then a joint `χ²/dof=161.2/38` is quoted. Negative “`C_ℓ` power” entries and hidden null means make the reported z-scores non-reproducible.  
**Fix:** Split subsample-mask and canonical-mask spectra into separate tables. For each bandpower list data, null mean, null std, covariance/null type, mask, and MC count; compute joint `χ²` only for one consistent data vector with its full covariance.
