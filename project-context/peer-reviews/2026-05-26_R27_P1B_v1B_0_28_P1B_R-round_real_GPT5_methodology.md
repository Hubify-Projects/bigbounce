# P1B R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R27_P1B_v1B_0_28
**Wall time**: 152.9s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=23683, completion=8394, reasoning=7169, total=32077

---

## PAPER-GPT-B1 — BLOCKER

- **Section:** Abstract; Sec. VI “Spectator-ALP consistency check”
- **Issue:** Grok scope-pushback is acceptable for the $\Delta N_{\rm eff}$ and NaMaster null/pipeline checks, but escalates for the ALP: with $f_a\sim M_{\rm Pl}$, $m\sim H_0$, $\theta_i\sim0.5$–2, the ALP energy density is $\Omega_\phi\sim (m/H_0)^2(f_a/M_{\rm Pl})^2[1-\cos\theta_i]/3\sim0.04$ to $>1$, so it is not a spectator and fixed-background $\Lambda$CDM evolution is inconsistent.
- **Fix:** Either solve the coupled Friedmann+ALP system with cosmological constraints or restrict parameters so $\Omega_\phi\ll1$ and recompute $\Delta\phi/f_a$, $\beta$, and the allowed coupling range. Otherwise remove/demote the ALP “consistency without fine-tuning” claim.

## PAPER-GPT-B2 — MAJOR

- **Section:** Table 1B; Sec. III “Physics interpretation”; Sec. V model-comparison paragraph
- **Issue:** The paper claims the LCDM point is “disfavored at the joint level” from separate 1D marginal shifts, $w_0=+4.3\sigma$ and $w_a=-3.6\sigma$. That is not a joint likelihood ratio, Bayes factor, or properly marginalized exclusion; the LCDM point being unsampled by an MH chain is not evidence by itself.
- **Fix:** Report only component-wise posterior shifts, or compute the 2D Mahalanobis/profile $\Delta\chi^2$ using the full $(w_0,w_a)$ covariance and validate with a dedicated nested/profile run. Add the same marginal-tail caveat to $w_a$ and remove “joint-level” language until then.

## PAPER-GPT-B3 — MAJOR

- **Section:** Table 1B caption; Table “MCMC program inventory”
- **Issue:** “$N_{\rm effective}=89{,}871$ after 30% burn-in discard” is not an effective sample size; it is just a post-burn-in accepted-sample count. The iter2 chain gives no true ESS/autocorrelation or Monte Carlo error for the tail-sensitive $w_0,w_a,w_0+w_a$ claims.
- **Fix:** Rename this quantity to post-burn-in samples and report GetDist/Cobaya ESS, autocorrelation lengths, MC errors on means/standard deviations, and split-chain stability for $w_0,w_a,w_0+w_a$.

## PAPER-GPT-B4 — MAJOR

- **Section:** Sec. IV NaMaster; Sec. VI ALP; Conclusions LiteBIRD forecast
- **Issue:** The NaMaster bias floor $0.032$–$0.040^\circ$ is “carried forward” but not propagated into any $\beta$ uncertainty or forecast. If applicable as a systematic, $\beta=0.342\pm0.094^\circ$ becomes $\sigma_{\rm tot}=\sqrt{0.094^2+0.040^2}=0.102^\circ$ and $3.35\sigma$, while LiteBIRD’s $0.03^\circ$ forecast becomes $\sigma_{\rm tot}=0.05^\circ$, not a $9\sigma$ test.
- **Fix:** State explicitly whether the NaMaster floor is only an internal-pipeline validation number or part of the observational systematic budget. If it is a systematic, propagate it in quadrature or via a covariance model everywhere $\beta$ significance is quoted.

## PAPER-GPT-B5 — MAJOR

- **Section:** Sec. VI “MCMC parameter estimation” and “Birefringence value”
- **Issue:** The ALP coupling/displacement arithmetic is internally inconsistent. For $\beta_{\rm ALP}=0.336^\circ$ with $C_{a\gamma}=8$, the required displacement is $\Delta\phi/f_a\simeq1.26$, outside the quoted EOM range $[0.2,1.1]$; observed $\beta=0.342^\circ$ requires $C_{a\gamma}\simeq9.4$ even at $\Delta\phi/f_a=1.1$, yet the text calls $C_{a\gamma}\sim9$–51 “comfortably natural” after earlier defining the natural scan as $[4,12]$.
- **Fix:** Define one prior/range for $C_{a\gamma}$ and $\Delta\phi/f_a$, enforce it consistently in the MCMC, and recompute the posterior. If $C_{a\gamma}=8$ is fixed, the posterior mean cannot exceed the stated displacement range without explaining the changed prior.

## PAPER-GPT-B6 — minor

- **Section:** Sec. III caveat paragraph “$M_B$–$H_0$ joint-posterior offset check”
- **Issue:** The offset in $M_B-5\log_{10}H_0$ is divided by the marginal $\sigma_{M_B}=0.049$ and interpreted as a $3.2\sigma$ tension. That is the wrong error bar for a derived correlated combination; the uncertainty must come from the full joint posterior covariance of $M_B$ and $H_0$.
- **Fix:** Compute $X=M_B-5\log_{10}H_0$ per posterior sample and quote $\langle X\rangle$, $\sigma_X$, and its offset from the relevant anchor. Remove the $3.2\sigma$ statement unless it uses $\sigma_X$.
