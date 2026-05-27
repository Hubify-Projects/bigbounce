# P4 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-27_R-ext-maint-v3_P4_v1_0_138
**Wall time**: 97.8s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=106585, completion=4385, reasoning=3106, total=110970

---

## PAPER-GPT-B1 — BLOCKER

**Section:** §IV.D / “Joint nuisance-marginalized model fit” paragraph; also Abstract/Conclusions.  
**Issue:** The claimed “formal exclusion” of a 1.7% cosmological dipole at \(z=-250\) is invalid. A weighted linear regression with count weights is not a nuisance-marginalized likelihood: it ignores spatial covariance, mask-induced covariance, template uncertainty, dipole-direction profiling, and the non-Gaussian radial posterior for \(A=\sqrt{a_x^2+a_y^2+a_z^2}\).  
**Fix:** Retract the \(250\sigma\)/\(264\sigma\) exclusion. Build a likelihood with full pixel or harmonic covariance, profile/marginalize over dipole direction and nuisance templates with priors, validate with injected 1.7% dipoles, and report \(\Delta\chi^2\), posterior odds, or a properly marginalized amplitude interval.

## PAPER-GPT-B2 — BLOCKER

**Section:** §§III.A, IV.A–D, Conclusions, NaMaster appendix.  
**Issue:** The headline null depends on switching to the \(f_{\rm sky}=0.659\) “subsample mask” while the same catalog on the canonical mask gives \(+3.64\sigma\). The hierarchy was “fixed” only after initial catalog results, the subsample mask is not demonstrably pre-specified, and no common data-vector/injection/systematics validation shows that a real dipole would be recovered equivalently across the two masks.  
**Fix:** Declare one primary mask/data vector and run all nulls, injections, and nuisance fits on it. If multiple masks are retained, treat mask choice as an analysis variant with trials/model-selection penalty and stop using the null mask to override the canonical residual.

## PAPER-GPT-B3 — BLOCKER

**Section:** Conclusions, “Canonical-\(N\) MASTER \(\ell=1\) direct compute”; NaMaster appendix.  
**Issue:** Internal arithmetic for the canonical \(+3.64\sigma\) residual is inconsistent. The quoted values \(C_1=2.298\times10^{-5}\), null mean \(8.004\times10^{-6}\), std \(8.097\times10^{-6}\) give \((2.298-0.8004)/0.8097=1.85\sigma\), not \(3.64\sigma\); the \(3.64\sigma\) value corresponds to a different “proper monopole-subtracted” data/null/std set. \(f_{\rm sky}\) and pixel counts also vary between 0.49005/24087 and 0.494/24269.  
**Fix:** Replace all legacy canonical numbers with one canonical post-subtraction table containing \(C_1\), null mean, null std, empirical \(p\), mask definition, \(f_{\rm sky}\), and pixel count. Delete or quarantine the legacy \(+1.85\sigma\) arithmetic.

## PAPER-GPT-M1 — MAJOR

**Section:** §III.E “Hard-label variance widening”; Table I footnote c.  
**Issue:** The flip-noise variance derivation is wrong. For \(x_{\rm obs}=x_{\rm true}\oplus f\), the marginal is Bernoulli with \(q=r+(1-2r)p\), so \(\mathrm{Var}(\bar x_{\rm obs})=q(1-q)/N\); adding \(r(1-r)\) to \(p(1-p)\) double-counts randomness under the usual Bernoulli model. The adopted \(1.21\times\) factor is also called “more conservative” than \(1.29\times\), which is false.  
**Fix:** Re-derive the hard-label uncertainty under the actual conditioning used by the diagnostics, then recompute hard-label bin errors and injection thresholds. Remove the unsupported \(1.21\times\) propagation unless empirically calibrated from repeated \(D_4\) runs.

## PAPER-GPT-M2 — MAJOR

**Section:** §§IV.D, IV.H, IV.I, Conclusions.  
**Issue:** Statistical significance is repeatedly overclaimed or mixed across incompatible nulls. Examples: moment-\(z=+3.64\) is paired with empirical \(p=15/500=0.030\); \(+4.84\sigma\) is paired with \(p=2/500=0.006\); zero exceedances in 10,000 MC trials are treated as a measured \(p_{\rm LEE}\le10^{-4}\) and converted to \(>3.7\sigma\). These are non-Gaussian empirical tails, not Gaussian-\(\sigma\) detections.  
**Fix:** Report empirical \(p=(k+1)/(N+1)\) with binomial confidence intervals and avoid Gaussian-\(\sigma\) language unless the null distribution is validated Gaussian. Keep random-label, bootstrap, Bonferroni, and systematics-preserving nulls separate and do not combine their significances rhetorically.

## PAPER-GPT-M3 — MAJOR

**Section:** §VI.C Sensitivity; Abstract; Conclusions/falsification criterion.  
**Issue:** The sensitivity budget is internally inconsistent: the paper alternates between \(0.2\%\) half-modulation, \(0.29\%\) full-amplitude Fisher, \(0.4\%\) conservative full-amplitude, \(0.75\%\) HC empirical threshold, and \(\le0.50\%\) full-catalog injection threshold. It also calls per-pixel-shuffle thresholds “systematic-inclusive” even though that null explicitly destroys depth/PSF/morphology covariance.  
**Fix:** Provide one sensitivity table with columns: amplitude convention, sample, mask, null, \(N_{\rm MC}\), recovery criterion, and threshold. Reserve “systematic-inclusive” for a covariance-preserving null; otherwise call the injection thresholds statistical/per-pixel-shuffle thresholds.
