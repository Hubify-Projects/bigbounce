# paper1b R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-21_R23_P1B_v1B_0_20
**Wall time**: 190.2s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=19182, completion=11018, reasoning=9701, total=30200

---

## PAPER-GPT-B1 — BLOCKER

**Location:** Sec. 6, “ALP field evolution” / “Caveats”; Abstract ALP claim.  
**Issue:** The stated “spectator” ALP is not spectator for \(f_a\sim M_{\rm Pl}\), \(m\sim H_0\), \(\theta_i\sim1\): \(\Omega_a \sim (m/H_0)^2(f_a/M_{\rm Pl})^2[1-\cos\theta_i]/3\), giving \(\Omega_a\sim0.15\) at \(m=H_0\) and \(\sim0.6\) at the fiducial \(m\simeq2H_0\), with the stated range exceeding unity. Fixed-\(\Lambda\)CDM-background ALP evolution and “does not participate in dynamics” are invalid.  
**Fix:** Solve the coupled Friedmann+ALP system and refit/constraint-check against CMB+SN+BAO, or restrict \(f_a,\theta_i,m\) so \(\Omega_a\ll1\) and recompute \(\Delta\phi/f_a\) and \(\beta\). Otherwise remove the ALP consistency claim from the abstract.

## PAPER-GPT-M1 — MAJOR

**Location:** Sec. 3, Table `iter2_posterior` interpretation; Sec. 5 “Results”; Sec. 7 cross-paper anchor.  
**Issue:** “Empirically rules out LCDM at the joint level” is not supported by quoting marginal shifts \(w_0=+4.3\sigma\) and \(w_a=-3.6\sigma\). Joint exclusion requires the full covariance/profile likelihood or a nested-model \(\Delta\chi^2\); the reported \(w_{\rm pivot}=-1.034\pm0.030\) already shows the \(w_0\) marginal shift is covariance-dependent.  
**Fix:** Replace “jointly rules out” with marginal-shift language, and report a Mahalanobis distance/profile \(\Delta\chi^2\) for \((w_0,w_a)=(-1,0)\) or wait for the promised nested-sampling/evidence run.

## PAPER-GPT-M2 — MAJOR

**Location:** Abstract; Sec. 3 sample-count footnote; Table `mcmc_inventory`; Conclusions.  
**Issue:** \(424{,}781=176{,}840+132{,}949+114{,}992\) is only a raw accepted-sample total including the Planck-only row with \(\hat R-1\sim0.05\), explicitly “Ongoing”; it is not three frozen posterior chains, not post-burn-in, and not ESS. The iter2 caption also mislabels a 30% burn-in remainder as \(N_{\rm effective}\), conflating post-burn-in count with effective sample size.  
**Fix:** Keep the frozen headline at \(309{,}789\) raw / \(216{,}852\) post-burn-in for two converged chains unless Planck-only converges. Rename iter2 \(N_{\rm effective}\) to \(N_{\rm postburn}\) and report actual ESS.

## PAPER-GPT-M3 — MAJOR

**Location:** Sec. 6, “Birefringence value” and “MCMC parameter estimation.”  
**Issue:** The ALP range arithmetic is wrong. From \(\beta[^\circ]\simeq0.0333\,C_{a\gamma}\Delta\phi/f_a\), the stated ranges \(C_{a\gamma}\in[4,12]\), \(\Delta\phi/f_a\in[0.2,1.1]\) give \(\beta\simeq0.027^\circ\)–\(0.44^\circ\), not \(0.17^\circ\)–\(0.43^\circ\); moreover \(\beta=0.342^\circ\) requires \(C_{a\gamma}\Delta\phi/f_a\simeq10.3\), so fixed \(C_{a\gamma}=8\) needs \(\Delta\phi/f_a\simeq1.29\), outside the stated max 1.1.  
**Fix:** Recompute the allowed \(\beta\) interval directly from the stated priors/EOM output, and either widen the displacement/coupling range or stop claiming the fixed-\(C_{a\gamma}=8\) mean naturally matches the observed value.

## PAPER-GPT-M4 — MAJOR

**Location:** Sec. 4 “Independent verification”; Conclusions “NaMaster pipeline validation.”  
**Issue:** The body says the worst-case NaMaster recovery bias is \(0.040^\circ\) at \(\beta=0.342^\circ\) and that this is carried as the systematic floor, but the conclusion says the pipeline recovers injected angles with bias \(\le 0.032^\circ\). That understates the systematic budget.  
**Fix:** Use \(\le0.040^\circ\) everywhere for the generalized systematic floor, reserving \(0.032^\circ\) only for the \(\beta=0.27^\circ\) fiducial injection.

## PAPER-GPT-M5 — MAJOR

**Location:** Sec. 6 “MCMC parameter estimation”; Appendix A.  
**Issue:** The ALP MCMC is not reproducible: the text says priors and dataset details are in Appendix A, but Appendix A contains no ALP priors, likelihood definition, covariance, chain split, ESS, or per-parameter \(\hat R\). The same \(9{,}720\) accepted samples are also described as supporting both fixed-\(C_{a\gamma}=8\) ALP inference and a model-independent \(\beta_{\rm free}\) fit, which are distinct parameterizations.  
**Fix:** Add a real ALP-MCMC appendix/table with separate configurations for fixed-\(C_{a\gamma}\) and \(\beta_{\rm free}\), priors, likelihood inputs, sample counts after burn-in, ESS, and convergence diagnostics.
