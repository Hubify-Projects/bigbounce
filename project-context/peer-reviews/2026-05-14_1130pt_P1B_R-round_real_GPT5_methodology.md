# P1B R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Round**: 2026-05-14_1130pt
**Wall time**: 59.1s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=11604, completion=3092, total=14696

---

## PAPER-GPT-B1 — BLOCKER — Secs. 3, 7, 8; fn. 1; Tables I/III

Concrete issue: MCMC sample accounting is still internally inconsistent. Sec. 3/abstract say **309,789** frozen samples; conclusions say **424,781**; Table III includes Planck-only **114,992** ongoing; fn. 1 says 30% burn-in leaves **123,129** from both frozen chains, but \(0.7\times309{,}789=216{,}852\). Table III also says DESI DR2 \(w_0w_a\) has \(\sim109\) accepted samples while Sec. 7/conclusions say \(\sim3.8\times10^4\).

Fix: Make one authoritative inventory. Exclude ongoing chains from headline frozen counts, recompute burn-in/thinning numbers per dataset, and update Table III to match the text.

## PAPER-GPT-B2 — BLOCKER — Sec. 5, Table II

Concrete issue: The model-comparison \(\Delta\chi^2_{\rm eff}=-7.9\) for one extra parameter is incompatible with the reported full-tension posterior \(\Delta N_{\rm eff}=-0.020\pm0.169\), where the nested value zero is only \(0.12\sigma\) from the mean. A Gaussian nested likelihood would give negligible improvement, not \(\Delta\chi^2\simeq8\).

Fix: Recompute \(\chi^2_{\rm eff}\), AIC, and BIC from the same chains/dataset used for the quoted posterior, or remove the model-comparison table.

## PAPER-GPT-B3 — BLOCKER — Sec. 5, Table II; fn. 3

Concrete issue: The reported \(\ln B=+4.8\) is not a valid evidence claim. Savage-Dickey must use the marginalized posterior density at the nested point with the correct prior density; with \(\Delta N_{\rm eff}\) centered essentially at zero, a large Bayes factor favoring the extended model is implausible and contradicts the stated null result. The correlation caveat does not fix the calculation.

Fix: Delete \(\ln B\) from the table or replace it with a proper nested-sampling evidence calculation. Do not quote a biased Savage-Dickey number as indicative support.

## PAPER-GPT-B4 — MAJOR — Sec. 5, Table II

Concrete issue: BIC arithmetic uses inconsistent effective data counts. From \( \mathrm{BIC}=\chi^2+k\ln n \): LCDM implies \(\ln n=6.55\), \(w\)CDM implies \(6.34\), and \(\Lambda\)CDM+\(\Delta N_{\rm eff}\) implies \(6.64\). Same dataset comparison cannot use different \(n\).

Fix: Define \(n\) once for the full-tension likelihood and recompute all BIC values. If \(n\) is ambiguous for compressed/compound likelihoods, do not use BIC.

## PAPER-GPT-B5 — MAJOR — Sec. 6

Concrete issue: The ALP coupling product is arithmetically inconsistent. For \(\beta_{\rm obs}=0.342^\circ=5.97\times10^{-3}\,\mathrm{rad}\), the relation \(\beta=(\alpha_{\rm EM}/4\pi)C_{a\gamma}\Delta\phi/f_a\) requires \(C_{a\gamma}\Delta\phi/f_a\simeq10.3\), not \(C_{a\gamma}\theta_i=3.4\pm1.1\). The quoted product would predict only \(\sim0.11^\circ\) absent an unstated transfer factor.

Fix: State the exact mapping from \(\theta_i\) to \(\Delta\phi/f_a\) used in the MCMC and recompute the reported \(C_{a\gamma}\theta_i\) constraint.

## PAPER-GPT-B6 — MAJOR — Sec. 4

Concrete issue: NaMaster bias handling is not statistically rigorous. A recovered \(0.238^\circ\) for injected \(0.270^\circ\) is a \(0.032^\circ\) multiplicative/additive bias, comparable to future LiteBIRD errors, yet no uncertainty on the bias, debiasing prescription, or systematic propagation is given. The claim that the pipeline is “unbiased at the \(0.04^\circ\) level” is not justified.

Fix: Report the MC mean and scatter of \(\hat\beta-\beta_{\rm inj}\), distinguish additive vs multiplicative bias, and propagate this as a systematic if any pipeline-derived \(\beta\) is used.
