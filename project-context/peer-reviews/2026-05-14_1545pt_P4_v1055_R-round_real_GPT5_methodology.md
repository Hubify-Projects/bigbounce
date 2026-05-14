# P4_v1055 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Round**: 2026-05-14_1545pt
**Wall time**: 67.7s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=55207, completion=2649, total=57856

---

## PAPER-GPT-B1 — BLOCKER — Sec. Hemisphere Asymmetry / Abstract / Conclusions

**Issue:** The hemisphere look-elsewhere result is internally contradictory. Text says the $3.05\sigma$ hemisphere peak “does not survive” LEE and is “$<1\sigma$,” but the direct MC footnote says zero of 10,000 nulls exceed the data, i.e. $p_{\rm LEE}\lesssim10^{-4}$, which is strong evidence *against* the null, not “consistent with no large-scale dipole.” The abstract repeats this sign error.

**Fix:** Recompute/verify the hemisphere statistic and null distribution. If $p_{\rm LEE}<10^{-4}$ is correct, it must be treated as a detected large-scale asymmetry requiring systematics explanation; if not, correct the MC result and all abstract/conclusion claims.

## PAPER-GPT-B2 — BLOCKER — Sec. Sensitivity / Introduction / Conclusions

**Issue:** The amplitude-convention correction is not consistently closed. The abstract quotes the corrected Fisher $3\sigma$ full-amplitude floor $\sim0.29\%$, but the Introduction, Sec. Sensitivity derivation, and Conclusions still quote $\sim0.2\%$ as the statistical floor. The empirical injection table also does **not** establish a $0.5\%$ “at $3\sigma$” threshold: at $A=0.5\%$, $P(\sigma>2)=0.18$, and no $P(\sigma>3)$ recovery threshold is shown.

**Fix:** Replace all “$0.2\%$” Fisher full-amplitude claims with the corrected $\sim0.29\%$ or explicitly define them as half-modulation uncertainty. State the empirical result as “$>0.5\%$ under the tested grid” unless larger-amplitude injections demonstrate 50% recovery at the claimed $3\sigma$ criterion.

## PAPER-GPT-B3 — BLOCKER — Sec. Dipole / Table III / Conclusions

**Issue:** The canonical-$N$ MASTER $\ell=1$ closure is not a direct canonical result. Table III’s load-bearing $\ell=1$ value is still from a subsample/mask ($n=5{,}547{,}858$, $f_{\rm sky}=0.659$), while the canonical $N_{\rm spiral}=3{,}201{,}160$, $f_{\rm sky}\simeq0.491$ result is only an analytic projection; the Conclusions say that projection gives $+0.2595\sigma$, but the abstract/table still call $-0.122\sigma$ “canonical primary.”

**Fix:** Either run the direct canonical single-mode NaMaster/MASTER MC and use that value everywhere, or label $-0.122\sigma$ as the subsample-mask result and $+0.2595\sigma$ as an approximate canonical projection. Do not call both “canonical primary.”

## PAPER-GPT-M1 — MAJOR — Sec. Dipole / Table III

**Issue:** The paper claims “all higher multipoles are likewise consistent with null,” but Table III reports $\ell_{\rm eff}=4$ at $+6.097\sigma$ and joint $\chi^2/{\rm dof}=161.2/38=4.24$. Calling this “mask-coupled monopole leakage” is not a null result; it is evidence that the estimator/covariance/model is missing a large systematic component.

**Fix:** Model and marginalize/subtract the monopole leakage through the actual mask, then recompute the covariance and post-fit $p$-values. Until then, remove “higher multipoles are null” claims and restrict the conclusion to the specifically tested $\ell=1$ statistic.

## PAPER-GPT-M2 — MAJOR — Sec. Sensitivity / Systematics Budget

**Issue:** Systematic errors are not propagated into the quoted dipole limits. The paper reports significant morphology/PSF correlations ($|r|\simeq0.042$, morphology-bin CW spreads up to $1.41\%$) but then treats them narratively rather than as nuisance fields in the dipole covariance; the “$0.5\%$ empirical floor” is not tied to a full systematics covariance.

**Fix:** Build a systematic covariance or nuisance-template regression including PSF, depth, morphology, confidence, and mask terms, then propagate it into the dipole amplitude uncertainty/limit. Quote the final sensitivity only after this inflation.

## PAPER-GPT-M3 — MAJOR — Sec. Labels / Catalog Tiers / Dipole Inference

**Issue:** The classifier’s independent CW/CCW agreement with GZ1 is only $69.91\%$ with $\kappa=0.40$, yet downstream dipole fits treat hard labels as direct chirality measurements. Misclassification/dilution and asymmetric confusion rates are not marginalized, so dipole amplitudes and sensitivity floors are over-precise.

**Fix:** Include a confusion-matrix nuisance model for true-vs-observed chirality, with priors from GZ1/CE-ResNet/SpArcFiRe comparisons, and marginalize over it in the dipole likelihood or injection-recovery pipeline. Report limits on the true dipole after dilution correction and uncertainty propagation.
