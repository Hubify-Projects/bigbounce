# P2 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-strict-v2_P2_v1_7_37
**Wall time**: 139.7s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=33150, completion=7868, reasoning=6728, total=41018

---

## PAPER-GPT-B1 — BLOCKER — Appendix A / A.2

**Issue:** The local-bispectrum normalization is algebraically inconsistent. The paper states Planck/Komatsu-Spergel uses \(c=2\) for \(B_\zeta=c f_{\rm NL}[PP+\mathrm{perms}]\), while the paper itself elsewhere uses the standard curvature convention \(B_\zeta=(6/5)f_{\rm NL}[PP+\mathrm{perms}]\); it also claims \(\sigma(f_{\rm NL})\) and \(f_{\rm NL}\) scale oppositely under convention changes, then holds \(\sigma=0.7\) fixed while halving the signal in Table A.2.

**Fix:** Define explicitly whether \(f_{\rm NL}\) is for \(\Phi\) or \(\zeta\), use the same \(6/5\) normalization as the SPHEREx/Heinrich forecast, and rescale both signal and forecast error consistently. Only halve the significance if the physical bispectrum is actually half, not for a pure convention relabeling.

## PAPER-GPT-B2 — BLOCKER — Secs. “Matter-Bounce Bispectrum Benchmark” / “Template Projection”

**Issue:** The template-overlap forecast rests on arbitrary null-space polynomials constrained only by three benchmark triangle values. Matching squeezed/equilateral/folded values does not define the physical bispectrum; the full cubic-action calculation fixes the intermediate-shape coefficients, so the sampled coefficient family is not a justified theory uncertainty.

**Fix:** Use the actual published full polynomial with a resolved permutation/time-ordering convention, or independently rederive the six coefficients from the in-in integrals. Do not quote quantitative \(r=0.84\pm0.02\) or \(3\)–\(5\sigma\) forecasts from an arbitrary benchmark-matching function family.

## PAPER-GPT-M1 — MAJOR — Abstract / Secs. “SPHEREx Forecast” / “Systematics”

**Issue:** The post-systematic \(3\)–\(5\sigma\) headline is not propagated from a joint systematic budget. The text includes \(r\)-scatter as wide as \(0.55\)–\(1.14\), \(b_\phi\) degradation of \(20\)–\(50\%\), GR degradation of \(10\)–\(30\%\), photo-\(z\) degradation, and \(\epsilon\)-corrections, but only applies selected central degradations; conservative combinations fall below \(3\sigma\).

**Fix:** Provide a single nuisance-parameter propagation table/Monte Carlo with stated priors and correlations, reporting percentiles of the final significance. Otherwise downgrade the headline to “optimistic \(\sim5\sigma\), plausibly lower after uncombined systematics.”

## PAPER-GPT-M2 — MAJOR — Sec. “Quantitative Bayesian Comparison”

**Issue:** The reported “Bayes factors vs tuned multifield competitors” are only one-dimensional prior-predictive ratios over \(f_{\rm NL}\). They do not marginalize over actual curvaton/QSFI/multifield parameters, shapes, \(n_s\), nuisance systematics, or selection effects, so calling them model Bayes factors over inflationary competitors overclaims the statistical result.

**Fix:** Relabel these as “1D \(f_{\rm NL}\) prior-volume evidence ratios” or perform a real model evidence calculation over the competitor parameter spaces with explicit priors and likelihoods.

## PAPER-GPT-M3 — MAJOR — Tables `tab:bayes` and `tab:gr`

**Issue:** The Bayes-factor arithmetic is internally inconsistent. The four-corner grid/caption gives the delta-prior narrow \([-5,+5]\) value as \(BF=7.00\) for \(\sigma=0.7\), but Table `tab:gr` labels the same delta+narrow competitor setup as \(BF=10.9,9.4,7.9\), and Table `tab:bayes` row 4 quotes \(8\)–\(11\).

**Fix:** State the exact likelihood width, observation, and GR treatment used for each table row, or recompute all delta+narrow entries with one common setup. Do not cite the \(8\)–\(11\) GR spread as numerically consistent with the \(BF=7.00\) fixed-\(\sigma\) analytic value unless the differing assumptions are explicit.

## PAPER-GPT-M4 — MAJOR — Secs. “Assumptions” / “Current Data and Consistency Relation”

**Issue:** The quasi-dust correction discussion says the Hankel index diverges at \(\epsilon=3/2\); for constant-\(w\) matter contraction the index is finite there (\(\nu=3/2\) for matter domination). The same section says \(w=-0.003\) gives an \(n_s\) correction of order \(10^{-3}\), but the paper’s own formula gives \(n_s-1=12w\simeq-0.036\).

**Fix:** Replace the singular-point argument with the correct mode-index dependence and recompute/justify the \(\kappa_1\) and \(1\)–\(8\%\) \(\epsilon\)-correction range. Correct the \(n_s\) scaling statement.
