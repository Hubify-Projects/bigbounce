# paper2 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-21_R25_P2_v1_7_30
**Wall time**: 99.2s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=30709, completion=4566, reasoning=3624, total=35275

---

## PAPER-GPT-B1 — BLOCKER

**Section:** Secs. 2.1, 3.2; Abstract  
**Issue:** The bispectrum shape is reconstructed from three benchmark triangles despite six polynomial coefficients being needed. Arbitrary null-space coefficient sets that match squeezed/equilateral/folded values are not “valid” physical bispectra, so the quoted overlap \(r=0.84\pm0.02\), null-space scan, and \(5.2\)–\(5.5\sigma\) forecast are not established.  
**Fix:** Use the full published Cai et al. polynomial or perform an independent vertex-level derivation; recompute the Fisher overlap only for physically derived shapes.

## PAPER-GPT-B2 — BLOCKER

**Section:** Appendix A; Sec. 2.3; Conclusion  
**Issue:** The \(f_{\rm NL}\) convention audit is internally inconsistent. The paper states Planck/SPHEREx use \(B_\zeta=(6/5)f_{\rm NL}PP\) in the abstract, but Appendix A defines the Planck \(\zeta\) convention with \(c=2\); it also claims the physical bispectrum is convention-independent while saying the detection significance halves under the Li/Brandenberger normalization.  
**Fix:** Define one observable convention consistently for \(\zeta\) vs. \(\Phi\), transform both \(f_{\rm NL}\) and \(\sigma(f_{\rm NL})\) together, and separate a true missing in-in factor from a mere normalization convention.

## PAPER-GPT-M1 — MAJOR

**Section:** Secs. 3.2, 4, 7.1; Abstract  
**Issue:** The headline SPHEREx significance is an external \(\sigma(f_{\rm NL})=0.7\) local-template forecast with ad hoc multiplicative degradations. There is no full Fisher/marginal likelihood for the bounce template including \(b_\phi\), GR projections, photo-\(z\), nonlinear bias, mask, and template mismatch jointly, so the claimed post-systematic \(3\)–\(5\sigma\) is not a propagated error budget.  
**Fix:** Either run the full Heinrich-style Fisher analysis for the bounce template with all nuisance parameters jointly marginalized, or downgrade the result to a rough recast and remove discovery-level language.

## PAPER-GPT-M2 — MAJOR

**Section:** Secs. 2.1, 3.2; Abstract  
**Issue:** The polynomial null-space scatter is not propagated consistently. The body reports \(r=0.85\pm0.13\) with range \(0.55\)–\(1.14\), which would reduce the pre-systematic significance to \(\sim3.4\sigma\) at the low end before GR/\(b_\phi\) degradation, but the headline uses only \(r=0.84\pm0.02\).  
**Fix:** Marginalize over the full allowed \(r\) distribution or justify excluding the low-\(r\) coefficient sets; quote the resulting widened significance range.

## PAPER-GPT-M3 — MAJOR

**Section:** Sec. 6; Tables 2–3; Conclusion  
**Issue:** The Bayes factors are not proper model evidences over common nuisance spaces. The procedure draws survey performance and GR shifts in mock realizations generated under the bounce, then evaluates closed-form \(f_{\rm NL}\)-only Bayes factors; this is an expected-BF exercise, not a marginalized likelihood ratio for data, and the tables mix fixed/varied GR, delta/Gaussian bounce priors, and different competitor prior widths.  
**Fix:** Write the full evidence integrals over \(f_{\rm NL}\), theory uncertainty, GR/systematic shifts, \(b_\phi\), and survey nuisance parameters with model-specific priors; report prior sensitivity without calling the MC count a validation of model selection.

## PAPER-GPT-m1 — minor

**Section:** Conclusion vs. Abstract/Sec. 6  
**Issue:** The conclusion says the Bayesian comparison was validated over \(>6\times10^5\) realizations, contradicting the abstract and Sec. 6 statement that the canonical count is \(3\times10^5\) across three ensembles.  
**Fix:** Replace \(>6\times10^5\) with \(3\times10^5\) or explicitly justify any additional ensembles.
