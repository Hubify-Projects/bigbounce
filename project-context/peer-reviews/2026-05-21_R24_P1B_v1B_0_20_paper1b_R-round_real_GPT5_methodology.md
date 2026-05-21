# paper1b R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-21_R24_P1B_v1B_0_20
**Wall time**: 101.2s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=19198, completion=5115, reasoning=4128, total=24313

---

No blocker-grade findings.

## PAPER-GPT-M1 — MAJOR — Abstract; Sec. 3 footnote; Table `mcmc_inventory`; Conclusions

**Issue:** The manuscript reports **309,789 raw samples across 2 frozen chains** and explicitly labels the 114,992-sample Planck-only run as **ongoing** with \(\hat R-1\sim0.05\), not frozen/posterior. It therefore cannot support any “424,781 posterior samples across 3 frozen dataset combinations” framing.

**Fix:** Either converge/freeze the Planck-only chain and update all sample-count, burn-in, ESS, and posterior summaries, or keep the headline strictly at **309,789 raw / 216,852 post-burn-in across 2 frozen chains**.

## PAPER-GPT-M2 — MAJOR — Table `iter2_posterior`; Sec. 3 “Physics interpretation”; Sec. 5 model comparison

**Issue:** “Empirically rules out LCDM at the joint level” is overclaimed from marginal shifts \(w_0=+4.3\sigma\), \(w_a=-3.6\sigma\). Joint exclusion requires the full \(2\times2\) covariance/profile likelihood or a same-stack nested-model comparison; marginal parameter shifts are not a Bayes factor or likelihood-ratio result.

**Fix:** Replace with “marginal posteriors disfavour the LCDM coordinates” unless a joint Mahalanobis distance/profile \(\Delta\chi^2\) or nested-sampling evidence on the identical likelihood stack is reported.

## PAPER-GPT-M3 — MAJOR — Table `iter2_posterior` caption

**Issue:** The caption calls \(N_{\rm effective}=89{,}871\) “after 30% burn-in discard”; that is a post-burn-in sample count, not an effective sample size. Without per-parameter ESS/autocorrelation/MCSE for \(w_0,w_a\), the quoted tight errors and significance are not auditable.

**Fix:** Rename it to \(N_{\rm postburn}\), and add true ESS, integrated autocorrelation time, and Monte Carlo standard error for all load-bearing parameters.

## PAPER-GPT-M4 — MAJOR — Sec. 4 NaMaster; Conclusions

**Issue:** Sec. 4 says the \(\beta=0.342^\circ\) injection has bias \(0.040^\circ\) and that this is the systematic floor, but the abstract/conclusions still headline \(0.032^\circ\) and claim bias \(\le 0.032^\circ\). The systematic budget is internally inconsistent.

**Fix:** Use \(0.040^\circ\) everywhere as the quoted NaMaster systematic floor, or explicitly make the floor injection-dependent and propagate it in quadrature wherever pipeline-derived \(\beta\) values are compared.

## PAPER-GPT-M5 — MAJOR — Sec. 6 “Birefringence value”

**Issue:** The stated range \(\beta\simeq0.17\)--\(0.43^\circ\) over \(C_{a\gamma}\in[4,12]\), \(\Delta\phi/f_a\in[0.2,1.1]\) is arithmetically wrong. Since \(\beta[^\circ]\simeq0.0333\,C_{a\gamma}\Delta\phi/f_a\), the range is \(\simeq0.027\)--\(0.44^\circ\).

**Fix:** Recompute the range and remove the “comfortably bracketing without fine-tuning” claim unless the parameter priors are restricted or correlated to exclude the low-\(\beta\) region.

## PAPER-GPT-M6 — MAJOR — Sec. 6 ALP field evolution / spectator assumption

**Issue:** For \(f_a\sim M_{\rm Pl}\), \(m\sim H_0\), \(\theta_i\sim1\), the ALP energy density is generically \(\rho_\phi\sim m^2 f_a^2(1-\cos\theta_i)\), i.e. an \(\mathcal{O}(0.1{-}1)\) fraction of today’s critical density for the fiducial range. Treating it as a spectator evolved on a fixed \(\Lambda\)CDM background is not self-consistent.

**Fix:** Either solve the coupled Friedmann+ALP system and include its dark-energy contribution in the cosmological fit, or restrict \(f_a,m,\theta_i\) so \(\Omega_\phi\ll1\) and show that the birefringence amplitude remains achievable.
