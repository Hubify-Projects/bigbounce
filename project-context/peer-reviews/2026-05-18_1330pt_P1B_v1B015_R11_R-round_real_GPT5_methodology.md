# P1B_v1B015_R11 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1330pt
**Wall time**: 117.2s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=18056, completion=5712, reasoning=4660, total=23768

---

No blocker-grade findings.

## PAPER-GPT-M1 — MAJOR

**Section:** Secs. 7.2(ii–iii), Appendix B Table `tab:claims`  
**Issue:** Savage-Dickey/Bayes-factor language survives: “Savage-Dickey $\ln B$ recompute,” “Savage-Dickey pull,” and Table B claims model-comparison $\Delta$AIC/BIC/$\ln B$ status as `Tab. iter2_posterior` / “v1B.0.13+ Savage-Dickey.” This contradicts the v1B.0.15 nested-sampling closure and falsely maps evidence quantities to a posterior-summary table.  
**Fix:** Replace all residual Savage-Dickey references with “dedicated PolyChord/MultiNest or thermodynamic-integration evidence pending.” Set Appendix B model-comparison status to “Not reported / pending nested sampling,” not Table `iter2_posterior`.

## PAPER-GPT-M2 — MAJOR

**Section:** Sec. 3, Table `tab:iter2_posterior` interpretation; Sec. 5 Results  
**Issue:** “Empirically rules out LCDM at the joint level” is asserted from marginal shifts $w_0=4.3\sigma$, $w_a=3.6\sigma$ without reporting the 2D covariance, profile-likelihood $\Delta\chi^2$, or a restricted LCDM fit. Marginal parameter displacement is not a model-comparison significance.  
**Fix:** Report the $(w_0,w_a)$ covariance and the Mahalanobis/profile-likelihood distance to $(-1,0)$, or a matched LCDM-vs-$w_0w_a$ likelihood-ratio/evidence calculation. Rephrase as “posterior parameter tension with LCDM” until that is done.

## PAPER-GPT-M3 — MAJOR

**Section:** Sec. 6 “ALP field evolution” / “Caveats”; Abstract ALP claim  
**Issue:** The claimed spectator ALP with $f_a\sim M_{\rm Pl}$, $m\sim H_0$, $\theta_i\sim1$ has energy density $\rho_a\sim m^2 f_a^2(1-\cos\theta_i)$, i.e. an $\mathcal{O}(0.1$–$1)\rho_{\rm crit}$ component for the quoted fiducials. It is not automatically a spectator in a fixed $\Lambda$CDM background.  
**Fix:** Either solve the coupled Friedmann+ALP system and include the induced dark-energy contribution in the cosmological fit, or restrict $f_a$, $m$, and $\theta_i$ so that $\Omega_a\ll1$ over the quoted parameter range.

## PAPER-GPT-M4 — MAJOR

**Section:** Sec. 6 “Birefringence value”  
**Issue:** The ALP range arithmetic is still wrong. With $\beta[^\circ]=(\alpha_{\rm EM}/4\pi)(180/\pi)\,C_{a\gamma}\Delta\phi/f_a\simeq0.0333\,C_{a\gamma}\Delta\phi/f_a$, the stated ranges $C_{a\gamma}\in[4,12]$ and $\Delta\phi/f_a\in[0.2,1.1]$ give $\beta\simeq0.027^\circ$–$0.44^\circ$, not $0.17^\circ$–$0.43^\circ$.  
**Fix:** Correct the span to $0.027^\circ$–$0.44^\circ$, or explicitly state extra cuts that exclude the low-displacement/low-coupling corner.

## PAPER-GPT-m1 — minor

**Section:** Sec. 4 NaMaster; Conclusions “NaMaster pipeline validation”  
**Issue:** The body correctly carries a worst-case NaMaster systematic floor of $0.040^\circ$ from the $0.342^\circ$ injection, but the Conclusions say the bias is $\le0.032^\circ$. That underreports the propagated systematic floor.  
**Fix:** Change the conclusion to “bias $\le0.040^\circ$,” with $0.032^\circ$ only for the $\beta=0.27^\circ$ injection.

## PAPER-GPT-m2 — minor

**Section:** Sec. 7/Table `tab:crosspaper`; Conclusions “Forward”  
**Issue:** Stale convergence/version text remains: P1(b) is listed as v1B.0.13 / 67% with $\ln B$ pending, and the Forward paragraph says the DESI chain is “running” and the mpirun process “remains alive,” despite the round context saying the iter2 chain is final/terminated at convergence.  
**Fix:** Update the status table and Forward paragraph to final-chain language; remove “running/alive” and stale v1B.0.12+/v1B.0.13+ queue wording.
