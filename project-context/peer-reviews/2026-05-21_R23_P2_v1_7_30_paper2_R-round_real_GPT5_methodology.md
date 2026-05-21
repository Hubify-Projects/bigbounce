# paper2 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-21_R23_P2_v1_7_30
**Wall time**: 142.9s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=30734, completion=7642, reasoning=6318, total=38376

---

## PAPER-GPT-B1 — BLOCKER

- **Section:** Secs. 2.1, 3.2; Table 1; Appendix A  
- **Issue:** The template-overlap forecast is built from arbitrary degree-9 polynomial coefficients constrained only by three benchmark triangles. By the paper’s own description, Cai Eq. 37 supplies a coefficient set; if that is the physical shape, the system is not underdetermined, and if it is not, matching squeezed/equilateral/folded values is insufficient to determine the bispectrum over the triangle domain. The quoted \(r=0.84\pm0.02\), null-space scan, and injection/recovery validation therefore do not validate the physical matter-bounce template.  
- **Fix:** Use the exact published Cai shape with a fully mapped normalization/permutation convention, or rederive the four in-in integrals and publish the coefficients. Until then, remove the quantitative \(r\) forecast and all derived significances.

## PAPER-GPT-B2 — BLOCKER

- **Section:** Abstract; Conclusion; Appendix A.1–A.2  
- **Issue:** The factor-of-two/convention treatment is internally inconsistent. The paper uses the standard Planck \(\zeta\)-convention \(B_\zeta=(6/5)f_{\rm NL}[PP+\cdots]\) in the abstract, but Appendix A calls the Planck coefficient \(c=2\); it also says S/N is convention-independent while Table A.2 halves the significance by keeping \(\sigma(f_{\rm NL})=0.7\) fixed. A pure convention change cannot halve a detection significance; only a physical amplitude ambiguity can.  
- **Fix:** Define one observational convention and convert every quoted \(f_{\rm NL}\) and \(\sigma\) into it. Treat \(-35/16\) as an alternative physical/theory branch if retained, not as a convention row, and recompute the forecast and Bayes factors.

## PAPER-GPT-B3 — BLOCKER

- **Section:** Abstract; Secs. 3.2, 4, 7.2–7.4, 9.3  
- **Issue:** The headline post-systematic \(3\)–\(5\sigma\) range is asserted, not propagated. The stated ingredients imply lower significances once compounded: e.g. \(S\simeq |f_{\rm NL}|r/[0.7\,D_{b_\phi}D_{\rm GR}D_{\rm photoz}]\), and with \(f_{\rm NL}\simeq4.02\), \(r=0.83\), \(D_{b_\phi}=1.5\), \(D_{\rm GR}=1.3\), \(D_{\rm photoz}=1.05\), \(S\simeq2.3\sigma\); including the stated null-space low \(r=0.55\) gives \(\sim1.5\sigma\).  
- **Fix:** Provide a single explicit systematic-budget table/equation with correlations and percentile intervals. Revise all “\(3\)–\(5\sigma\)” and “null excludes \(>4\sigma\)” claims to the propagated interval.

## PAPER-GPT-M1 — MAJOR

- **Section:** Sec. 4 “SPHEREx Forecast”; Sec. 3.2  
- **Issue:** The Heinrich \(\sigma(f_{\rm NL})=0.7\) local-template Fisher forecast is reused for a nonlocal bounce shape by multiplying by a scalar \(r\). That is not a substitute for a Fisher projection with the bounce template, galaxy-bias nuisance parameters, \(b_\phi\), redshift bins, and the actual multi-tracer covariance; the paper also calls the fiducial shift “of order the parameter uncertainty” although \(|-4.375|/0.7=6.25\sigma\).  
- **Fix:** Either re-run the Heinrich-style Fisher matrix with the bounce template and nuisance marginalization, or downgrade the result to a rough sensitivity recast with no precise \(5.2\)–\(5.5\sigma\) claim.

## PAPER-GPT-M2 — MAJOR

- **Section:** Sec. 9.4 “Joint \((f_{\rm NL},n_{f_{\rm NL}})\) Forecast”  
- **Issue:** The body quotes \(\sigma_{\rm marg}(f_{\rm NL})=0.44\), \(\sigma_{\rm unmarg}=0.114\), and \(\sim9.9\sigma\) from an unreleased six-bin SDB Fisher analysis that the text admits is \(6\times\) sharper than published SPHEREx forecasts. This contradicts the abstract’s statement that the numerical significance is not quoted pending release, and the section also inconsistently says the bispectrum shape-mismatch \(r\) does not apply to SDB while listing it in the joint systematic budget.  
- **Fix:** Remove the numerical \(9.9\sigma\), \(0.44\), and \(0.114\) claims until the full Fisher inputs/code are released and externally checkable. Keep only the qualitative \(n_{f_{\rm NL}}\) discriminator discussion.

## PAPER-GPT-M3 — MAJOR

- **Section:** Sec. 6.3; Tables 2–3; Conclusion  
- **Issue:** The reported “Bayes factors” are mostly one-dimensional prior-volume factors conditional on a mock detection near \(-35/8\), not full model evidences with nuisance/theory marginalization. Drawing \(\sigma\), \(b_\phi\), and GR shifts across scenarios is not the same as integrating them in the likelihood for each model; convention/theory uncertainty and template mismatch are not consistently marginalized. The conclusion also still says \(>6\times10^5\) realizations, contradicting the \(3\times10^5\) count in the abstract and Sec. 6.3.  
- **Fix:** Recast as illustrative conditional likelihood/prior-volume ratios, or write the full hierarchical evidence integral over \(f_{\rm NL}\), theory width, GR shift, \(b_\phi\), template mismatch, and survey performance. Fix the realization count everywhere.
