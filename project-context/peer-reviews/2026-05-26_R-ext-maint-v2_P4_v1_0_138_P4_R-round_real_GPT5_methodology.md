# P4 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-maint-v2_P4_v1_0_138
**Wall time**: 85.4s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=106584, completion=4227, reasoning=3105, total=110811

---

## PAPER-GPT-B1 — BLOCKER

- **Location:** §VI.D / §“Joint nuisance-marginalized model fit”
- **Issue:** The claimed “formal exclusion” of a 1.7% clean dipole at \(z=-250\) is not a valid nuisance-marginalized likelihood result. It is a weighted linear-regression parameter-shift with no demonstrated pixel covariance, no residual/systematic covariance, no profiling over dipole direction, and no valid treatment of the positive-definite amplitude \(A=\sqrt{a_x^2+a_y^2+a_z^2}\).
- **Fix:** Remove “formally excluded” / “250σ” language. Recompute with a declared likelihood using full covariance or validated block/bootstrap covariance, profile/marginalize over direction and nuisance templates, and report likelihood-ratio or posterior intervals only after calibration on injected signals.

## PAPER-GPT-B2 — BLOCKER

- **Location:** §III/§IV/§VIII.E; Table “face-on robustness”; Conclusions
- **Issue:** The same Catalog C dipole is reported as \(0.43\sigma\) headline, \(-0.12\sigma\) MASTER, \(+3.64\sigma\) canonical MASTER, and \(+4.31\sigma\) in the “Catalog C full” face-on robustness table. Hand-waving this as “different estimators” is insufficient; at least one estimator/null normalization is incompatible with the stated no-dipole conclusion.
- **Fix:** Define one primary data vector, mask, monopole treatment, weights, and null. Re-run all dipole estimators on identical inputs and provide a covariance/cross-calibration table; demote non-identical estimator results to exploratory diagnostics.

## PAPER-GPT-M1 — MAJOR

- **Location:** §VI.D joint fit; §VIII.E sensitivity; Conclusions
- **Issue:** The amplitude convention is inconsistent by a factor of two. The paper alternates between full amplitude \(A\) in \(p_{\rm CW}= \tfrac12(1+A\cos\theta)\), CW-fraction modulation \(A/2\), and \(A_p=2f_{\rm CW}-1\); the joint fit states that 1.7% in \(f_{\rm CW}\) corresponds to \(A_p=0.034\), while the injection/falsification convention treats 1.7% as full amplitude.
- **Fix:** Pick one convention and add a conversion table. Recompute all quoted sensitivity thresholds, injected amplitudes, nuisance-fit comparisons, and “1.7%” exclusion statements under that convention.

## PAPER-GPT-M2 — MAJOR

- **Location:** §III.E “Hard-label variance widening”
- **Issue:** The flip-noise variance derivation is wrong. For independent label flips with rate \(r\), \(x_{\rm obs}\sim{\rm Bern}(q)\) with \(q=r+(1-2r)p\); at \(p\simeq0.5\), the observed Bernoulli variance remains \(\simeq0.25/N\), while deattenuating to infer \(p\) inflates variance by \((1-2r)^{-2}\), not by the paper’s ad hoc \(1.21\times\) or “upper-bound” \(1.29\times\).
- **Fix:** Replace the derivation with the standard misclassification/attenuation model. Propagate either observed-label variance or deattenuated true-label variance consistently through all hard-label diagnostics and injection floors.

## PAPER-GPT-M3 — MAJOR

- **Location:** §IV.D, §Hemisphere Asymmetry, Tables I/III/VI
- **Issue:** MC significance is repeatedly over-interpreted. Examples: zero exceedances in \(10^4\) trials are described as \(>3.7\sigma\) without tail uncertainty; \(p_{\rm MC}=15/500=0.030\) is juxtaposed with “\(+3.64\sigma\)” as if calibrated; moment-\(z\), empirical-rank \(p\), Gaussian-equivalent \(z\), and look-elsewhere-corrected values are mixed.
- **Fix:** Use \((k+1)/(N+1)\) rank p-values with binomial uncertainty for MC tails, clearly separate moment-\(z\) from calibrated significance, and increase MC where claiming \(p<10^{-3}\). Do not translate unvalidated non-Gaussian nulls into Gaussian σ.

## PAPER-GPT-M4 — MAJOR

- **Location:** §IV.B global CW fraction; §VIII.E sensitivity; Data Availability limitations
- **Issue:** Error bars and sensitivity limits still rely on naive binomial/Fisher errors despite documented classifier disagreement, 21.4% argmax instability, PSF/morphology correlations, leg×confidence systematics, and spatially correlated depth structure. The systematic budget is not propagated into the quoted \(9.5\sigma\), \(0.29\%\), \(0.75\%\), or falsification thresholds.
- **Fix:** Build a systematic covariance from spatial blocks, imaging legs, confidence/morphology bins, and PSF/depth templates. Quote statistical-only and systematic-inclusive limits separately, with the headline using the systematic-inclusive budget.
