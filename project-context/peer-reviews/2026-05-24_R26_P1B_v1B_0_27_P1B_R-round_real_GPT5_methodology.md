# P1B R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-24_R26_P1B_v1B_0_27
**Wall time**: 85.6s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=22703, completion=4679, reasoning=3624, total=27382

---

No blocker-grade findings.

## PAPER-GPT-B1 — MAJOR

**Location:** Table `tab:iter2_posterior`; Sec. 3 “Physics interpretation”; Sec. 5 model-comparison paragraph; Sec. 7 cross-paper anchor.  
**Issue:** The paper calls LCDM disfavored “at the joint level” using separate 1D marginal pulls of \(w_0\) and \(w_a\). That is not a joint significance; it requires the full \((w_0,w_a)\) covariance and a \(\Delta\chi^2\) or posterior-content calculation.  
**Fix:** Replace “joint level” / “LCDM lies \(>4\sigma\)” with marginal-only language, or report the 2D covariance and compute the actual joint distance/posterior mass around \((-1,0)\).

## PAPER-GPT-B2 — MAJOR

**Location:** Table `tab:iter2_posterior` caption.  
**Issue:** “\(N_{\rm effective}=89{,}871\) after 30% burn-in discard” is not an effective sample size; it is just the post-burn-in retained sample count. This mislabels autocorrelation/weight-adjusted ESS and weakens the tail-significance claims.  
**Fix:** Rename it to \(N_{\rm postburn}\), and report true ESS/min-ESS for \(w_0,w_a,w_0+w_a\) from GetDist/Cobaya.

## PAPER-GPT-B3 — MAJOR

**Location:** Sec. 6 “MCMC parameter estimation”; Table `tab:mcmc_inventory`.  
**Issue:** The ALP-MCMC sample accounting appears to pool “3 configurations” with different fixed \(C_{a\gamma}=4,8,12\), while quoting \(\beta_{\rm ALP}=0.336\pm0.107\) for \(C_{a\gamma}=8\) fixed. Pooling configurations is not a single posterior and \(\hat R\) across different fixed-model runs is meaningless.  
**Fix:** Report per-configuration sample counts, priors, likelihoods, ESS, and \(\hat R\); do not aggregate fixed-\(C_{a\gamma}\) configurations unless \(C_{a\gamma}\) is actually sampled in one joint model.

## PAPER-GPT-B4 — MAJOR

**Location:** Sec. 6 “Birefringence value” and “MCMC parameter estimation”; Conclusions “Spectator-ALP consistency.”  
**Issue:** The ALP natural-range arithmetic is internally inconsistent. With \(\Delta\phi/f_a\le1.1\), \(C_{a\gamma}=8\) gives \(\beta_{\max}\simeq0.29^\circ\), below the quoted observed central value \(0.342^\circ\); matching the central value requires \(C_{a\gamma}\Delta\phi/f_a\simeq10.3\), hence \(C_{a\gamma}\gtrsim9.4\) for the stated displacement range.  
**Fix:** State that \(C_{a\gamma}=8\) matches only within errors, not the central value, or broaden/justify the displacement prior beyond 1.1; make the \(C_{a\gamma}\in[4,12]\) scan and the later \(C_{a\gamma}\sim9\)–51 requirement mutually consistent.

## PAPER-GPT-B5 — MAJOR

**Location:** Sec. 4 NaMaster validation; Conclusions “NaMaster pipeline validation.”  
**Issue:** The injected-signal recovery is biased by \(0.032^\circ\)–\(0.040^\circ\), but no uncertainty on that bias from 500 MC realizations is reported and the systematic floor is not propagated into any quoted recovery uncertainty/SNR. Calling the estimator “unbiased at the \(0.04^\circ\) level” is also misleading.  
**Fix:** Report \(\sigma_{\rm MC}\) on the mean recovered bias, define whether the correction is additive or multiplicative, and propagate the \(0.040^\circ\) systematic floor in quadrature wherever recovery uncertainties or SNR-like quantities are quoted.

## PAPER-GPT-B6 — minor

**Location:** Sec. 3 caveat paragraph “M\(_B\)–H\(_0\) joint-posterior offset check.”  
**Issue:** The claimed \(0.155\) mag offset is assessed against the marginal \(\sigma_{M_B}=0.049\), ignoring the \(H_0\) uncertainty and the \(M_B\)–\(H_0\) covariance along the SN degeneracy. The resulting “\(\sim3.2\sigma\)” interpretation is not statistically valid.  
**Fix:** Compute the uncertainty of \(M_B-5\log_{10}H_0\) using the joint covariance matrix, or remove the sigma interpretation and keep only the arithmetic offset.
