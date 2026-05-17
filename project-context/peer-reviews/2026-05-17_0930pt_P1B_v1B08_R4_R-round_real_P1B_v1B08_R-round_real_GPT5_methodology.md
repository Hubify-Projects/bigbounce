# P1B_v1B08 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-17_0930pt_P1B_v1B08_R4_R-round_real
**Wall time**: 86.9s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=13346, completion=5685, reasoning=4142, total=19031

---

## PAPER-GPT-B1 — BLOCKER — Zombie model-comparison statistics are not fully removed

**Location:** Sec. 5 “Model-comparison statistics”; Conclusions; Appendix A “What is NOT included”; Appendix B Table “Claims classification”.

| Truth audit | Result |
|---|---|
| Required state | No remaining `ln B=+4.8` / AIC/BIC/Bayes-factor framing after removal. |
| Observed | Sec. 5 still prints `\ln B = +4.8`; Appendix A says “Bayes factors are estimated via Savage-Dickey”; Appendix B keeps “Model-comparison ΔAIC/BIC/lnB” as a claim. |
| Verdict | Not closed. The zombie block is still present in historical/procedural form and contradicts the claimed removal. |

**Issue:** The paper claims the Bayes-factor/AIC/BIC block was removed, but still contains the exact stale `ln B=+4.8` value and continued Savage-Dickey/Bayes-factor language.

**Fix:** Delete all numerical zombie-stat references and all Bayes-factor-estimation language until a single auditable recomputation exists; replace with one sentence: “Model-comparison statistics are deferred and not reported.”

---

## PAPER-GPT-B2 — BLOCKER — Full-tension SH0ES prior appears mathematically inactive

**Location:** Sec. 2; Table 1; Conclusions.

| Truth audit | Result |
|---|---|
| Required state | If SH0ES Gaussian prior is included, posterior should shift relative to Planck+BAO+SN or show explicit likelihood tension. |
| Observed | Planck+BAO+SN: `H0=67.79±1.09`; Full-tension with SH0ES: `H0=67.68±1.06`, essentially unchanged and even slightly lower. |
| Verdict | Inconsistent with an active SH0ES prior unless an unreported counter-likelihood dominates. |

**Issue:** Combining an approximately `73 km/s/Mpc` SH0ES prior with a `67.8±1.1` posterior should not leave the mean/sigma unchanged. This strongly suggests the SH0ES likelihood was not active, was misconfigured, or the “full-tension” dataset definition is wrong.

**Fix:** Show the Cobaya YAML likelihood block, prior center/width, and per-likelihood `-2 ln L` contributions for runs with and without SH0ES; otherwise remove “SH0ES included” and rename the dataset.

---

## PAPER-GPT-B3 — BLOCKER — DESI DR2 chain-status bump did not propagate

**Location:** Table `mcmc_inventory` caption/row vs Sec. 7.1 “Free-$w_0w_a$ chain status”, item (ii).

| Truth audit | Result |
|---|---|
| Required state | Current DESI DR2 status everywhere: `101,979` samples, `Rhat-1=0.01176`, timestamp `2026-05-17 01:29 UTC`. |
| Observed | Table/caption/conclusions use current values, but Sec. 7.1(ii) still says `59,832` samples, `Rhat-1=0.01945`, `2026-05-14 22:53 UTC`. |
| Verdict | Not closed; stale R3 value remains in a load-bearing cross-paper anchor. |

**Issue:** The subsection explicitly described as the Paper I(a) anchor still carries the old chain state, contradicting the updated table and conclusions.

**Fix:** Replace the stale values in Sec. 7.1(ii) with `101,979 / 0.01176 / 2026-05-17 01:29 UTC`, or explicitly label the old values as a superseded historical snapshot.

---

## PAPER-GPT-M1 — MAJOR — Version/status propagation tail remains stale

**Location:** Table `crosspaper`.

| Truth audit | Result |
|---|---|
| Required state | Current manuscript is v1B.0.8 with R4/R3 closures reflected. |
| Observed | Table lists `P1(b) v1B.0.7`, readiness after `2026-05-14`, and key blocker “Model-comparison recompute deferred v1B.0.8”. |
| Verdict | Stale internal status metadata. |

**Issue:** The cross-paper status table says the current P1(b) version is v1B.0.7 and treats v1B.0.8 as future work, while the document macro says v1B.0.8.

**Fix:** Update the table to v1B.0.8, current date/state, and either mark model-comparison as “removed/deferred beyond v1B.0.8” or provide the recomputation.

---

## PAPER-GPT-M2 — MAJOR — NaMaster validation still lacks an auditable estimator/noise-error budget

**Location:** Sec. 4 “Data Methods: CMB E-B Analysis”.

| Truth audit | Result |
|---|---|
| Required state | Bias/SNR claims need estimator definition, covariance, noise model, and MC error bars. |
| Observed | Gives `βhat=0.238°`, SNR `20.32`, bias `0.032°`, but no estimator equation, variance definition, MC scatter, finite-MC uncertainty, or Planck noise/foreground covariance. |
| Verdict | R3 NaMaster noise-injection item not closeable. |

**Issue:** The claimed `≤0.032°` bias and high recovery SNR are not reproducible from the text. ACT-level white-noise injection on a Planck Commander map is not enough to validate Planck-like anisotropic noise, residual foregrounds, calibration angle degeneracy, or EB covariance.

**Fix:** Provide the β estimator, bandpower covariance, noise-generation equation, mean±std over 500 MCs for each injection, finite-MC error on the bias, and clarify that the SNR denominator is the MC scatter, not a sky-measurement uncertainty.

---

## PAPER-GPT-M3 — MAJOR — ALP MCMC likelihood/diagnostics remain under-specified and internally strained

**Location:** Sec. 6 “MCMC parameter estimation”.

| Truth audit | Result |
|---|---|
| Required state | ALP MCMC claim needs likelihood, priors, sampled parameters, convergence diagnostics, acceptance/autocorrelation. |
| Observed | Reports `9,720` accepted samples and `Rhat-1<0.01`, but no likelihood expression, priors, chain count, acceptance fraction, autocorrelation/ESS, or posterior boundary checks. |
| Verdict | R3 ALP-likelihood/MCMC-diagnostics item not closeable. |

**Issue:** With `C_{aγ}=8` fixed, matching `β≈0.336°` requires `Δφ/fa≈1.26`, above the stated natural EOM range `[0.2,1.1]`; the text does not explain whether the MCMC permits values outside that range or is boundary-driven.

**Fix:** Add the ALP likelihood and priors, sampled parameters/ranges, chain diagnostics including ESS/autocorrelation/acceptance, and reconcile the fixed-`C_{aγ}=8` posterior with the stated displacement range.
