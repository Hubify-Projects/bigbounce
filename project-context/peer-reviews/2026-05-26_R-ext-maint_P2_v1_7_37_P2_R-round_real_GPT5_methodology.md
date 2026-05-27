# P2 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-maint_P2_v1_7_37
**Wall time**: 201.4s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=33134, completion=7710, reasoning=6732, total=40844

---

## PAPER-GPT-B1 — BLOCKER — Abstract; Conclusion; Appendix A/A.2

**Issue:** The paper says a pure $c=1$ vs $c=2$ normalization change halves the SPHEREx significance, but Appendix A also states significance is convention-invariant because $\sigma(f_{\rm NL})$ transforms with the convention. Table A.2 holds $\sigma(f_{\rm NL})=0.7$ fixed while changing the predicted $f_{\rm NL}$, which is invalid for a convention change.

**Fix:** Separate “different physical amplitude in Planck convention” from “different $f_{\rm NL}$ normalization convention.” If it is only convention, transform both $f_{\rm NL}$ and $\sigma$ and do not halve significance; if it is a physical single-time-ordering alternative, label it that way.

## PAPER-GPT-M1 — MAJOR — Abstract; Secs. 4, 6, 7.2; Conclusion

**Issue:** The claimed post-systematic $3$–$5\sigma$ and null-exclusion $>4\sigma$ are not backed by a joint propagation of the stated degradations. Multiplying the paper’s own effects—$b_\phi$ degradation, GR degradation, photo-$z$, $\epsilon$ correction, and possibly the lower $r$ tail—can push the conservative significance below $3\sigma$, while the null-exclusion claim is inconsistent with the same “$3$–$5\sigma$” budget.

**Fix:** Provide a single systematic-budget table or joint Fisher/marginalization calculation with all degradations applied simultaneously. Quote the resulting lower bound and make the null-exclusion significance use the identical post-budget uncertainty.

## PAPER-GPT-M2 — MAJOR — Sec. 5; Table 2; Abstract Bayes-factor claim

**Issue:** The Bayes factors use $f_{\rm NL}^{\rm obs}=-4.375$ with $\sigma=0.7$, but the forecast pipeline says the local estimator measures $r f_{\rm NL}^{\rm bounce}$ or, equivalently, a deprojected bounce amplitude with $\sigma=0.7/r\simeq0.83$. The reported BF $\sim10$–$17$ therefore does not use the same likelihood as the detection forecast and ignores $r$ and systematics as nuisance parameters.

**Fix:** Recompute evidences with the actual observable: either local-template data centered on $r f_{\rm NL}$ or deprojected data with $\sigma/r$, marginalizing over $r$, GR, $b_\phi$, and survey-performance priors. Otherwise label the BF as an idealized no-systematics conditional BF.

## PAPER-GPT-M3 — MAJOR — Sec. 5 Tables `tab:bayes` and `tab:gr`

**Issue:** The Bayes-factor arithmetic is internally inconsistent. The closed-form delta-prior, narrow $[-5,5]$ competitor case at $\sigma=0.7$ is stated as BF $=7.00$, but Table `tab:gr` reports 10.9/9.4/7.9 for the same “narrow prior, delta bounce” framing, and Table `tab:bayes` calls this an 8–11 GR variation.

**Fix:** Recompute all BF tables from one explicit formula with stated $\sigma$, observed value, competitor prior, and GR treatment. If `tab:gr` uses a different $\sigma$ distribution or prior, state that and stop cross-identifying it with the analytic narrow-prior row.

## PAPER-GPT-M4 — MAJOR — Sec. 2.1 / template-overlap uncertainty

**Issue:** The null-space coefficient scan is not a physical prior. Matching three benchmark configurations does not make arbitrary radius-50/500 null-space coefficient sets valid bispectra from the cubic action, so using the resulting $r=0.85\pm0.13$ or range 0.55–1.14 as a systematic budget is unjustified.

**Fix:** Either derive/use the full Cai polynomial coefficients and drop the arbitrary null-space ensemble, or define a physically motivated prior over allowed cubic-action coefficients and propagate that prior quantitatively.

## PAPER-GPT-m1 — minor — Data and Code Availability

**Issue:** The manuscript is v1.7.37 but the reproducibility link is pinned to `v1.7.26-paper2`. That tag cannot verify the corrected Bayes-factor and systematic-budget numbers claimed in the current version.

**Fix:** Pin the repository to the exact manuscript release or archive a DOI/tag for v1.7.37 with scripts and outputs matching every table value.
