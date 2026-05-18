# P1B_v1B014_R9 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1230pt
**Wall time**: 118.3s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=17911, completion=5610, reasoning=4660, total=23521

---

No BLOCKER-grade findings.

## PAPER-GPT-M1 — MAJOR — Sec. 3/Table 1B interpretation

**Issue:** The paper claims the converged \(w_0w_a\) posterior “empirically rules out the LCDM point at the joint level” from marginal shifts \(w_0=+4.3\sigma\), \(w_a=-3.6\sigma\), and “zero samples at the LCDM point.” This is not a valid joint-significance calculation; continuous MCMC chains will have zero samples exactly at a point, and the joint exclusion requires the \(2\times2\) covariance/profile likelihood/\(\Delta\chi^2\) or a nuisance-marginalized posterior density ratio.  
**Fix:** Replace “rules out at the joint level” with “marginal posterior shifts” unless a documented joint \(\Delta\chi^2\), Mahalanobis distance with covariance, profile likelihood, or Savage-Dickey/evidence calculation is added.

## PAPER-GPT-M2 — MAJOR — Table 1B caption / convergence reporting

**Issue:** Table 1B calls \(N_{\rm effective}=89{,}871\) “effective” samples, but this is just \(0.7\times128{,}385\) post-burn-in samples, not an ESS. The load-bearing \(w_0w_a\) posterior reports no per-parameter ESS or Monte Carlo error despite using \(\hat R-1=0.0082\) as “publication-grade” convergence.  
**Fix:** Rename to \(N_{\rm postburnin}\); report GetDist/Cobaya ESS and MCSE for \(w_0,w_a,w_0+w_a,H_0,\tau\), or weaken the convergence claim.

## PAPER-GPT-M3 — MAJOR — Secs. 2 and 5.1 SH0ES wording

**Issue:** The text still calls the active SH0ES likelihood an “\(H_0\) prior” in Sec. 2 and Sec. 5.1, contradicting the corrected caveat that the YAML uses `H0.riess2020Mb`, i.e. an \(M_B\) calibrator constraint, not a direct Gaussian \(H_0\) prior. This reintroduces the exact methodological ambiguity the audit was supposed to close.  
**Fix:** Replace “SH0ES \(H_0\) prior” everywhere with “SH0ES/Riess2020 \(M_B\) likelihood/calibrator constraint”; reserve “\(H_0\) tension” for the posterior comparison to Riess \(H_0\).

## PAPER-GPT-M4 — MAJOR — Sec. 5.2 / Appendix B model-comparison status

**Issue:** Sec. 5.2 says a recomputation of \(\chi^2_{\rm eff}\), AIC, BIC, and evidence “is reported in Table 1B,” but Table 1B reports only posterior means and \(\chi^2\) channel means. Appendix B also marks “Model-comparison \(\Delta\)AIC/BIC/\(\ln B\)” as “Tab. 1B,” contradicting the stated removal of Bayes-factor/information-criterion claims.  
**Fix:** Delete the AIC/BIC/evidence reporting claim and set Appendix B status to “Not reported / pending nested sampling or documented Savage-Dickey.”

## PAPER-GPT-m1 — minor — Conclusions NaMaster systematic floor

**Issue:** The conclusions say the NaMaster pipeline recovers injected angles with bias \(\le 0.032^\circ\), but Sec. 4 reports \(0.040^\circ\) bias for the \(\beta=0.342^\circ\) injection and adopts \(0.04^\circ\) as the systematic floor. The conclusion understates the systematic by 25%.  
**Fix:** Change the conclusion to “bias \(\le 0.040^\circ\)” and keep \(0.04^\circ\) as the propagated NaMaster systematic floor.

## PAPER-GPT-n1 — nit — Sec. 8 / Appendix A bad reference

**Issue:** The manuscript references Sec. `\ref{sec:results}`, but no `sec:results` label exists; the relevant section is `sec:cosmo_fits` or its Results subsection.  
**Fix:** Add the missing label or repoint the references to `\ref{sec:cosmo_fits}`.
