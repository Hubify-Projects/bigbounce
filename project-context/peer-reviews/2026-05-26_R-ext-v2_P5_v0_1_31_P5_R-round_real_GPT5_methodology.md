# P5 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-v2_P5_v0_1_31
**Wall time**: 99.7s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=26051, completion=6276, reasoning=5178, total=32327

---

## PAPER-GPT-B1 — BLOCKER

- **Section:** Abstract; §VI.A Table `cw_vs_env`; §VII.E “Cross-survey P4-monopole-residual analysis”; §VIII Systematics.
- **Issue:** Headline cohort arithmetic is internally impossible: V-Web class counts sum to `428+6673+408187+397505 = 812,793`, not the stated `791,635` chirality-relevant spirals. Later “relaxed” 812,793-sample explanation does not repair the abstract/Table claim; filament bright `n=416,701` also exceeds the stated filament total `n=408,187`, and §VIII’s BGS-vs-dark “within ±0.001” contradicts the earlier bright/dark split `0.4970` vs `0.5051`.
- **Fix:** Define one analysis mask per result table and rerun every count/fraction from it. Update abstract, tables, figures, and systematics so all `n`, `n_CW`, and totals close exactly.

## PAPER-GPT-B2 — BLOCKER

- **Section:** Abstract; §VI.A Table `cw_vs_env`; §VII Phase 2 sensitivity sweep; Conclusions.
- **Issue:** The Phase 2 robustness claim is arithmetically incompatible with the canonical table. The canonical V-Web range is `0.5034−0.4836 = 0.0198 = 1.98 pp`, but Phase 2 says the same `(R_s=25, λ=0)` cell has range `0.165 pp` and that the maximum over all cells is only `0.220 pp`.
- **Fix:** Recompute Phase 2 using the same cohort and definition as Table `cw_vs_env`, or explicitly state a different statistic/sample. Do not claim “max 0.22 pp” unless the canonical cell also satisfies it.

## PAPER-GPT-B3 — BLOCKER

- **Section:** §IV.A V-Web algorithm, steps 8–11.
- **Issue:** The tensor derivation has the wrong Fourier sign as written. With `Φ(k)=-δ_k/k^2`, the Hessian is `T_ij=∂i∂jΦ=-k_i k_j Φ(k)=+k_i k_j δ_k/k^2`; the paper states `T_ij=k_i k_j Φ(k)`, flipping eigenvalue signs and therefore web classes under a `λ>λ_th` rule.
- **Fix:** Correct the tensor definition, rerun the environment labels, and validate on a known overdensity/void toy field or mocks. Also rename this as T-Web unless an actual velocity-shear V-Web is implemented.

## PAPER-GPT-B4 — BLOCKER

- **Section:** §IV V-Web classification; §VII.E DESIVAST/T-Web comparison.
- **Issue:** The density field is built from raw DESI counts in a masked flux/tracer-selected survey shell, then FFT-Poisson solved in a rectangular box with no random catalog, radial selection correction, angular completeness correction, or controlled boundary treatment. The paper itself observes edge artifacts and `0/6` DESIVAST agreement for V-Web voids, so the headline environment labels are not methodologically reliable.
- **Fix:** Build `δ=(n-α n_rand)/(α n_rand)` using DESI randoms/selection functions, restrict to a controlled volume-limited sample or model tracer selection, treat boundaries with padding/constrained mocks, and validate class purity against mocks or a DESI VAC before using labels for chirality inference.

## PAPER-GPT-M1 — MAJOR

- **Section:** §I; §V Statistical methods; §VII.E P4-monopole residual analysis.
- **Issue:** Statistical treatment of the monopole is not rigorous. `f_CW=0.4974±0.000279` is `~9.3σ` from 0.5, not “~1σ”; later residual tests treat the Paper IV/P5 monopole as exact and ignore its uncertainty/covariance when it is estimated from the same bins.
- **Fix:** Fit a binomial/logistic model with a nuisance intercept for the global monopole and environment coefficients as contrasts; propagate Paper IV systematic/statistical uncertainty or use the in-sample multinomial covariance. Report LRT/χ²/permutation p-values for environment dependence, not `|σ_obs−σ_pred|` heuristics.

## PAPER-GPT-M2 — MAJOR

- **Section:** §VII Tempel+2014 cross-validation; §VII.E DESIVAST discussion.
- **Issue:** The external “cross-validation” is overframed. Tempel concordance compares different footprints/redshift ranges and an arbitrary richness-to-web mapping; the `0.026 pp` filament agreement mostly shows both samples sit near the global monopole, not that classifiers agree on the same galaxies. DESIVAST results actually show V-Web void purity failure, not validation of the V-Web headline.
- **Fix:** For Tempel, compute paired same-galaxy overlap tests/confusion matrices and same-footprint chirality contrasts. Reframe DESIVAST as a replacement low-z void analysis, not as validation of the V-Web void class.
