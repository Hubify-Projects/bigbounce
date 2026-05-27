# P5 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-v3_P5_v0_1_31
**Wall time**: 137.1s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=27610, completion=7102, reasoning=6141, total=34712

---

## PAPER-GPT-B1 — BLOCKER

- **Section:** Abstract; §VI.A/Table I; §VII.E “Cross-survey P4-monopole-residual analysis”
- **Issue:** Headline sample arithmetic is inconsistent. The paper says the per-environment results are on the **791,635** chirality-relevant spirals, but Table I counts sum to **812,793** and CW counts sum to **404,111**, exceeding the matched-summary CW total **393,592** by **10,519**.
- **Fix:** Freeze one analysis sample and regenerate every headline table/abstract number from it. If using the 812,793 relaxed env-label superset, stop calling the Table I result the 791,635-sample result.

## PAPER-GPT-B2 — BLOCKER

- **Section:** §VIII/Table Phase 2; Abstract; Conclusions
- **Issue:** The Phase 2 sweep contradicts the canonical result. The canonical $(R_s=25,\lambda_{\rm th}=0)$ table has range $0.5034-0.4836=0.0198=1.98$ pp, but the Phase 2 row for the same cell reports **0.165 pp**, and the abstract claims the sweep max is **0.22 pp**.
- **Fix:** Recompute the sweep using the same class definitions/sample as the canonical table, or explicitly state the different sample/filter. Until reconciled, the robustness claim is unusable.

## PAPER-GPT-B3 — BLOCKER

- **Section:** §IV.A V-Web algorithm
- **Issue:** The environment classifier is not methodologically valid as written. It calls a density-Hessian T-Web calculation “V-Web,” omits the Fourier Hessian minus sign after $\Phi_k=-\delta_k/k^2$ so eigenvalue signs are flipped as written, and applies periodic FFT Poisson solving to raw flux-limited redshift-space counts without a radial selection function, random catalog/window correction, or boundary treatment.
- **Fix:** Either implement a survey-window/selection-corrected T-Web/V-Web with validated sign convention and mask handling, or demote the V-Web labels to exploratory and base the headline on an external calibrated catalog.

## PAPER-GPT-M1 — MAJOR

- **Section:** Introduction; §II
- **Issue:** The quoted Paper IV global fraction $0.4974\pm0.000279$ is not “consistent with parity at $\sim1\sigma$.” It is $(0.4974-0.5)/0.000279 \simeq -9.3\sigma$, matching the later “$\sim9.5\sigma$ monopole” statement.
- **Fix:** Replace the “$\sim1\sigma$” parity statement with the correct $\sim9\sigma$ statistical offset and explicitly identify it as a classifier/systematic monopole with its systematic uncertainty.

## PAPER-GPT-M2 — MAJOR

- **Section:** §V Statistical methods; §VII.E monopole residuals; Systematics
- **Issue:** The environment-null test is not a proper likelihood/model comparison. The paper treats $\Delta f_{\rm CW}=-0.0026$ or $f_{\rm CW}^{\rm P5}=0.4972$ as exact, subtracts it bin-by-bin, and thresholds residual “sigma” values without propagating monopole uncertainty, covariance from estimating the monopole on overlapping data, env-label uncertainty, or target/leg systematics.
- **Fix:** Fit a binomial/logistic or beta-binomial model with a nuisance global monopole and environment coefficients, include covariates/leg/tracer terms, and report marginalized/profiled intervals for environment effects plus a coherent systematic budget.

## PAPER-GPT-M3 — MAJOR

- **Section:** §VI.D tracer-program stratification; §X Systematics
- **Issue:** The target/tracer systematics statements contradict each other. §VI.D reports bright $f_{\rm CW}=0.4970$ vs dark $0.5051$ and a filament bright-vs-dark difference of $|z|\approx3.4\sigma$, while §X claims BGS vs LRG/ELG/QSO are within $\pm0.001$ and no test produces $>3\sigma$ after correction.
- **Fix:** Use one consistent target split, recompute the z-test and monopole-corrected residuals, and update the systematics section; do not claim the split is null if the reported difference is 0.8 pp and $3.4\sigma$.
