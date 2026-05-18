# P1B_v1B012_R7 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1100pt
**Wall time**: 136.1s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=13899, completion=8417, reasoning=7250, total=22316

---

## PAPER-GPT-B1 — BLOCKER

**Section:** Secs. 2, 3/Table 1, 5.1  
**Issue:** The “full-tension” posterior \(H_0=67.68\pm1.06\) is inconsistent with an active SH0ES prior. Combining the quoted no-SH0ES posterior \(67.79\pm1.09\) with a Riess2022-like \(H_0\simeq73.0\pm1.0\) prior gives \(\sim70.5\pm0.75\), not an unchanged Planck-like value with unchanged error.  
**Fix:** Inspect the Cobaya YAML/logs and prove the SH0ES likelihood is active with the intended parameter name/units. If not, relabel the row and remove SH0ES claims; if yes, rerun/update the posterior table.

## PAPER-GPT-B2 — MAJOR

**Section:** Sec. 7, Tables `crosspaper`/`mcmc_inventory`, Sec. 7.1, Conclusions “Forward”, App. A/B  
**Issue:** The DESI \(w_0w_a\) chain status is internally inconsistent: the paper marks it **CONVERGED**, but Sec. 7.1 still says “Until that chain converges,” Table caption says it is future work “once it reaches” convergence, Sec. 5 defers to v1B.0.12+ while this is v1B.0.12, App. A says v1B.0.10+, and the cross-paper row still lists P1(b) v1B.0.11.  
**Fix:** Choose one state. If converged, replace all convergence-gated language with “posterior extraction/model-comparison pending” and update deferral target/version; if not publication-ready, remove **CONVERGED**.

## PAPER-GPT-B3 — MAJOR

**Section:** Sec. 5 “Model-comparison statistics”, App. A  
**Issue:** The text still proposes recomputing “any evidence value from the final frozen-thinned chain.” Ordinary posterior MCMC samples do not give a robust Bayesian evidence/Bayes factor; Savage-Dickey requires explicit prior density and nuisance-marginalized posterior density at the nested point, not a thinned-chain readout.  
**Fix:** Limit chain-based recomputation to posterior summaries and max-likelihood/\(\chi^2\)-style diagnostics. For Bayes factors, use PolyChord/MultiNest/thermodynamic integration or a documented Savage-Dickey calculation with priors and nuisance marginalization.

## PAPER-GPT-B4 — MAJOR

**Section:** Sec. 4 NaMaster pipeline validation  
**Issue:** The reported bias is statistically large under the paper’s own SNR numbers: \(0.238/20.32\simeq0.0117^\circ\), so the \(0.032^\circ\) bias is \(\sim2.7\sigma\); for \(0.302/25.71\simeq0.0117^\circ\), the \(0.040^\circ\) bias is \(\sim3.4\sigma\). Calling the pipeline “unbiased at the \(0.04^\circ\) level” and “stable across all three injections” is unsupported without estimator variance/covariance and a null bias table.  
**Fix:** Report \(\hat\beta\pm\sigma_{\rm MC}\), define the SNR, tabulate all injection biases including \(\beta=0\), and either bias-correct or carry \(\sim0.04^\circ\) as a systematic.

## PAPER-GPT-B5 — MAJOR

**Section:** Sec. 6 “Spectator ALP consistency check”  
**Issue:** The ALP is not dynamically spectator for the stated natural parameters. With \(f_a\sim M_{\rm Pl}\), \(m\sim H_0\), \(\theta_i\sim1\), \(\rho_a\sim m^2 f_a^2(1-\cos\theta_i)\) is \(\mathcal{O}(0.1\!-\!1)\rho_{\rm crit}\), so evolving \(\phi\) in a fixed \(\Lambda\)CDM background while ignoring its energy density is inconsistent.  
**Fix:** Solve the coupled Friedmann+ALP system and impose \(\Omega_a\)/dark-energy constraints, or restrict \(f_a,m,\theta_i\) so the ALP energy density is demonstrably negligible.

## PAPER-GPT-B6 — MAJOR

**Section:** Sec. 6 “Birefringence value”  
**Issue:** The quoted ALP prediction range is arithmetically wrong. Using \(\beta[^\circ]\simeq0.0333\,C_{a\gamma}(\Delta\phi/f_a)\), the stated ranges \(C_{a\gamma}\in[4,12]\) and \(\Delta\phi/f_a\in[0.2,1.1]\) give \([0.027^\circ,0.44^\circ]\), not \([0.17^\circ,0.43^\circ]\).  
**Fix:** Recompute the range, or state the correlated parameter cuts that exclude the low-\(\beta\) region. Also reconcile this with the later claim that the observed signal may require \(C_{a\gamma}\sim 9\)–51, partly outside the earlier “natural” \(4\)–12 range.
