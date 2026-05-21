# paper2 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-21_R24_P2_v1_7_30
**Wall time**: 99.1s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=30729, completion=4686, reasoning=3618, total=35415

---

## PAPER-GPT-B1 — BLOCKER — Abstract; Appendix A/A.2

**Issue:** The local-bispectrum normalization is internally inconsistent and partly wrong. The abstract uses the Planck/SPHEREx curvature convention \(B_\zeta^{\rm local}=(6f_{\rm NL}/5)[PP+\mathrm{perms}]\), but Appendix A states the Planck convention is \(c=2\); then A.2 says detection significance is convention-independent while holding \(\sigma(f_{\rm NL})=0.7\) fixed and halving the significance in the alternate row.  
**Fix:** Rewrite the convention chain using the actual \(6/5\) curvature convention and explicitly distinguish physical missing-commutator factors from mere \(f_{\rm NL}\)-normalization relabelings. If it is a pure convention, rescale both \(f_{\rm NL}\) and \(\sigma\); if it is a physical factor, stop calling it convention sensitivity.

## PAPER-GPT-B2 — BLOCKER — Secs. 2.1, 3.2; Abstract

**Issue:** The template-overlap forecast rests on an arbitrary underdetermined polynomial. Three benchmark triangles cannot determine the six coefficients or the intermediate-shape Fisher overlap; sampling a radius-50 null-space ball is not a physical prior, yet the paper quotes \(r=0.84\pm0.02\) while also admitting \(r=0.85\pm0.13\), range \(0.55\)–\(1.14\).  
**Fix:** Use the actual published full Cai polynomial or perform an independent vertex-level derivation. Otherwise treat \(r\) as unresolved and propagate the full allowed range, not the hand-picked \(\pm0.02\).

## PAPER-GPT-B3 — BLOCKER — Abstract; Secs. 3.2, 4, 7

**Issue:** The advertised post-systematic \(3\)–\(5\sigma\) range is not produced by a joint error budget. Multiplying the stated degradations gives lower significances: e.g. \(4.02\times0.83/[0.7\times1.5\times1.3\times1.05]\approx2.3\sigma\), before including the admitted \(r\)-null-space tail.  
**Fix:** Provide a table with explicit multiplicative/additive nuisance model, covariance/marginalization assumptions, and min/median/max significance. Downgrade the headline if the conservative combined case falls below \(3\sigma\).

## PAPER-GPT-M1 — MAJOR — Sec. 5.3; Table 1

**Issue:** The Bayes-factor numbers for finite-width bounce priors do not follow from the stated closed-form marginal likelihood. For \(d=-4.375\), \(\sigma=0.7\), and a Gaussian bounce prior with \(\sigma_{\rm theory}=1\), the broad \([-15,15]\) competitor gives roughly \(30/\sqrt{2\pi(0.7^2+1^2)}\simeq9.8\), while the narrow \([-5,5]\) competitor gives \(\sim4\), not the quoted \(\sim8\) and \(\sim6\).  
**Fix:** Recompute all BF entries from one explicit likelihood/prior model, including nuisance marginalization, and state whether values are conditional on an observed datum or averaged over bounce-generated mocks.

## PAPER-GPT-M2 — MAJOR — Sec. 8.3

**Issue:** The joint \((f_{\rm NL},n_{f_{\rm NL}})\) SDB Fisher forecast quotes \(\sigma(f_{\rm NL})=0.44\) and \(9.9\sigma\) without released inputs and admits it is \(6\times\) sharper than published SPHEREx forecasts. The section also says the bispectrum shape-overlap factor \(r\) does not apply to SDB, then lists it in the joint systematic budget.  
**Fix:** Remove the \(9.9\sigma\) numerical claim until the six-bin Fisher inputs are released and externally reproducible. Do not apply bispectrum-shape mismatch to SDB; build a separate SDB nuisance budget.

## PAPER-GPT-M3 — MAJOR — Secs. 4, 7.2

**Issue:** The use of Heinrich et al. \(\sigma(f_{\rm NL})=0.7\) is a sensitivity recast, not an independent forecast, but the paper repeatedly treats it as if the full SPHEREx systematic marginalization were already inherited. The stated \(b_\phi\), GR, photo-\(z\), and nonlinear-bias degradations are patched on qualitatively, not through the Heinrich Fisher matrix.  
**Fix:** State the headline as “conditional recast of Heinrich et al.” and either reproduce the Fisher matrix with these nuisance parameters or present only scenario-level degraded \(\sigma(f_{\rm NL})\) values with no discovery-significance claim beyond those scenarios.
