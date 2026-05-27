# P1B R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-27_R-ext-maint_P1B_v1B_0_30
**Wall time**: 160.0s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=23981, completion=8332, reasoning=7243, total=32313

---

No BLOCKER-grade findings. Stated $\hat R$ convergence is not internally contradicted.

## PAPER-GPT-M1 — MAJOR — Sec. VI, “ALP field evolution” / “Caveats”

Concrete issue: The “spectator” ALP is not generically spectator for $f_a\sim M_{\rm Pl}$, $m\sim H_0$, $\theta_i\in[0.5,2]$: $\Omega_a\sim (m/H_0)^2(f_a/M_{\rm Pl})^2(1-\cos\theta_i)/3$, giving $\Omega_a\sim0.15$ already at the fiducial $m=H_0,\theta_i=1$ and exceeding the total density at the upper prior end. Fixed-$\Lambda$CDM-background evolution is therefore not self-consistent over the stated range.

Fix: Either solve the coupled Friedmann+ALP system and impose cosmological density constraints, or restrict the prior so $\Omega_a\ll1$ and report that restriction explicitly.

## PAPER-GPT-M2 — MAJOR — Sec. VI, “Birefringence value” / “MCMC parameter estimation”

Concrete issue: The claimed $\beta\simeq0.17$--$0.43^\circ$ range over $C_{a\gamma}\in[4,12]$ and $\Delta\phi/f_a\in[0.2,1.1]$ does not follow: $C_{a\gamma}$ does not enter the ALP EOM, so the low corner gives $\beta\simeq0.027^\circ$. Also $\beta=0.342^\circ$ requires $C_{a\gamma}\Delta\phi/f_a\simeq10.3$, i.e. $C_{a\gamma}\simeq9$--$51$ for the stated displacement range, inconsistent with presenting $[4,12]$ as the natural bracket; $C_{a\gamma}=8$ would require $\Delta\phi/f_a\simeq1.29$.

Fix: Publish the actual joint prior/scan correlation that removes the low corner, or quote the full independent-prior envelope $0.027$--$0.44^\circ$ and revise the “without fine-tuning” language.

## PAPER-GPT-M3 — MAJOR — Table 1B; Sec. III “Physics interpretation”; Sec. V “Results”

Concrete issue: The text claims LCDM is disfavored “at the joint level” using marginal $w_0$ and $w_a$ sigma distances. With $\sigma(w_0+w_a)=0.1485$, the implied $w_0$--$w_a$ correlation is $\rho\simeq-0.90$, so joint distance/model tension cannot be inferred from the two 1D z-scores; “phantom-crossing required” is also stated without a posterior probability.

Fix: Report the 2D likelihood/profile $\Delta\chi^2$ at $(w_0,w_a)=(-1,0)$ or the posterior probability of crossing. Keep Bayes-factor/model-selection claims deferred until nested sampling or thermodynamic integration is done.

## PAPER-GPT-M4 — MAJOR — Sec. VII, point (iii)

Concrete issue: The phrase “queued … alongside the Savage-Dickey $\ln B$ pull” contradicts the paper’s repeated statement that Savage-Dickey is not viable because the LCDM point is unsampled in the Metropolis-Hastings chain. This reintroduces the improper Bayes-factor framing the paper says it removed.

Fix: Delete “Savage-Dickey $\ln B$ pull” everywhere. Say only “nested sampling or thermodynamic integration on the identical likelihood stack.”

## PAPER-GPT-m1 — minor — Table 1B caption; Table “MCMC program inventory”

Concrete issue: Iter2 convergence is documented only by $\hat R-1=0.00820$ over two flushes. No per-parameter rank-normalized split-$\hat R$, bulk/tail ESS, autocorrelation length, or trace stability is shown for $w_0$, $w_a$, $w_0+w_a$, or log-posterior.

Fix: Add a compact diagnostics table with per-parameter $\hat R$, ESS$_{\rm bulk}$, ESS$_{\rm tail}$, and autocorrelation lengths. Otherwise soften “publication-grade convergence” to “meets the stated $\hat R$ threshold.”

## PAPER-GPT-m2 — minor — Sec. IV “NaMaster”; Conclusions “systematic floor”

Concrete issue: The 500-MC NaMaster validation reports $\hat\beta$, SNR, and bias values but no MC scatter, standard error of the mean, null-distribution width, or covariance. The $0.040^\circ$ “systematic floor” is not propagated into any uncertainty budget.

Fix: Report $\hat\beta\pm\sigma_{\rm MC}$, null mean $\pm\sigma$, and the uncertainty on the bias estimate. If the floor is used in comparisons, combine it with statistical errors in quadrature or state explicitly that it is an unpropagated validation bias.
