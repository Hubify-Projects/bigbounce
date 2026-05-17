# P1B_v1B07 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-17_0200pt_P1B_v1B07_R3_R-round_real
**Wall time**: 74.2s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=13179, completion=4932, reasoning=3106, total=18111

---

## PAPER-GPT-B1 — BLOCKER — Stale DESI DR2 chain status

**Section:** Table 2 (`tab:mcmc_inventory`), Sec. 7.1, Conclusions “Forward” paragraph.  

| Claimed in paper | Audited/live state | Verdict |
|---|---:|---|
| DESI DR2 iter2: 59,832 samples, \(\hat R-1=0.01945\), “current status as of 2026-05-14 22:53 UTC” | Current Cobaya iter2 on pod `ijzftpy3klystt`: 101,979 samples, \(\hat R-1=0.01176\) | Contradiction/stale “current” status |

**Issue:** The manuscript presents an obsolete DESI DR2 chain state as current, and repeats it in three load-bearing locations. It neither matches the live state nor clearly labels the numbers as a frozen historical snapshot.

**Fix:** Replace all DESI DR2 status instances with the live \(N=101{,}979\), \(\hat R-1=0.01176\), pod/timestamp, or explicitly mark the 59,832/0.01945 numbers as a frozen archival snapshot and stop calling them current.

---

## PAPER-GPT-B2 — BLOCKER — “Full-tension” posterior is mathematically inconsistent with claimed SH0ES prior

**Section:** Sec. 2; Table 1; Sec. 5.1.  

| Claimed in paper | Internal/statistical check | Verdict |
|---|---:|---|
| Full-tension includes SH0ES \(H_0\) prior | Planck+BAO+SN gives \(H_0=67.79\pm1.09\); multiplying by SH0ES \(\sim73.0\pm1.0\) should shift the marginal near \(\sim70.5\), not \(67.68\pm1.06\) | Likelihood likely not applied, misconfigured, or mislabeled |
| Paper explanation: Planck inverse-variance dominates | The quoted marginal uncertainty is comparable to SH0ES, so SH0ES cannot have negligible effect under a Gaussian prior | Invalid explanation |

**Issue:** The “full-tension” chain is almost identical to the no-SH0ES chain and even shifts slightly lower in \(H_0\), which is incompatible with actually applying a direct SH0ES Gaussian prior of comparable width.

**Fix:** Audit the Cobaya YAML and likelihood logs; report per-likelihood \(\chi^2\) contributions and prior term. If SH0ES was not active, relabel/rerun the chain; if active, show a reproducible posterior-reweighting check explaining the non-shift.

---

## PAPER-GPT-B3 — BLOCKER — Invalid model-comparison numbers are removed in Sec. 5 but reintroduced in Conclusions/Appendix

**Section:** Sec. 5.2; Conclusions; Appendix A.  

| Claimed in paper | Contradictory text | Verdict |
|---|---|---|
| Sec. 5.2 says \(\chi^2_{\rm eff}\)/AIC/BIC/\(\ln B\) block is removed and deferred to v1B.0.8 | Conclusions still cite \(\ln B=+4.8\), \(\Delta{\rm AIC}=-5.9\), \(\Delta{\rm BIC}=-0.7\) as primary cross-references | R2 blocker not closed |
| Appendix A says Bayes factors are estimated via biased Savage-Dickey | Sec. 5.2 says no reproducible script exists and evidence is deferred | Internal contradiction |

**Issue:** The manuscript knowingly retains the exact invalid Bayes-factor/AIC/BIC claims it says were removed. This is a methodological blocker because the posterior is null but the conclusion still implies model preference.

**Fix:** Delete all \(\ln B\), AIC, BIC, and Savage-Dickey claims from Conclusions and Appendix A until recomputed from one auditable final-chain script or nested sampling.

---

## PAPER-GPT-B4 — MAJOR — MCMC convergence reporting is incomplete

**Section:** Table 1; Sec. 3; Sec. 6 ALP MCMC; Appendix A.  

| Required diagnostic | Reported? | Verdict |
|---|---:|---|
| \(\hat R-1\) | Partial | OK for frozen cosmology, vague for ALP |
| ESS per parameter | Partial | Only minimum ESS for cosmology; none for ALP |
| Acceptance rate | No | Missing |
| Autocorrelation length / IACT | No | Missing |
| Priors and parameter bounds | No complete table | Missing |
| Baseline \(\Lambda\)CDM comparison with identical data | No | Missing |

**Issue:** The paper claims publication-quality MCMC convergence but omits acceptance fractions, autocorrelation lengths, full prior table, and ALP chain diagnostics. The DESI chain is also still above the stated \(\hat R-1<0.01\) target.

**Fix:** Add a diagnostics table for every chain: chains, raw/post-burn samples, burn-in, acceptance, IACT, min/median ESS, worst \(\hat R-1\), priors, and exact likelihood set. Add an identical-dataset \(\Lambda\)CDM baseline for any comparison language.

---

## PAPER-GPT-B5 — MAJOR — NaMaster bias arithmetic and systematic budget are wrong

**Section:** Sec. 4; Conclusions.  

| Injection | Reported recovery | Actual bias | Paper claim | Verdict |
|---:|---:|---:|---:|---|
| \(0.270^\circ\) | \(0.238^\circ\) | \(0.032^\circ\) | OK | Correct |
| \(0.342^\circ\) | \(0.302^\circ\) | \(0.040^\circ\) | “bias \(0.032^\circ\) stable”; “\(\le0.032^\circ\)” | False |

**Issue:** The stated stable \(0.032^\circ\) bias is arithmetically false. Also, SNR \(=20.32\) implies a statistical scale \(\sim0.012^\circ\), so a \(0.032\)–\(0.040^\circ\) pipeline bias is not negligible and is not propagated.

**Fix:** Provide a per-injection table with recovered mean, MC scatter, statistical error, bias, and bias-corrected value. Propagate the pipeline systematic into any quoted birefringence consistency statement or explicitly keep it separate from sky inference.

---

## PAPER-GPT-B6 — MAJOR — ALP birefringence ranges are internally inconsistent

**Section:** Sec. 6.  

| Claimed quantity | Arithmetic check | Verdict |
|---|---:|---|
| \(\Delta\phi/f_a\in[0.2,1.1]\), \(C_{a\gamma}\in[4,12]\) gives \(\beta\simeq0.17^\circ\)–\(0.43^\circ\) | Lower bound is \((\alpha/4\pi)4(0.2)=0.0266^\circ\), not \(0.17^\circ\) | Wrong range |
| Observed \(\beta=0.342^\circ\) requires \(C_{a\gamma}\Delta\phi/f_a\simeq10.3\) | With fixed \(C_{a\gamma}=8\), requires \(\Delta\phi/f_a=1.29\), outside stated \([0.2,1.1]\) | Fixed-\(C\) consistency overstated |
| ALP MCMC with \(C_{a\gamma}=8\) gives \(\beta=0.336^\circ\) | This exceeds the max \(\sim0.293^\circ\) implied by \(C=8\), \(\Delta\phi/f_a\le1.1\) | Prior/model mismatch |

**Issue:** The ALP section overclaims “without fine-tuning” while its own displacement range and coupling arithmetic do not support the fixed-\(C_{a\gamma}=8\) headline.

**Fix:** Recompute the allowed \(\beta\) range from the stated priors, disclose the ALP priors used in the MCMC, and either widen the displacement/coupling range or remove the fixed-\(C_{a\gamma}=8\) consistency claim.
