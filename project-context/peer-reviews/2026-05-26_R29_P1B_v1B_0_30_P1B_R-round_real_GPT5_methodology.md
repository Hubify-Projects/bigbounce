# P1B R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R29_P1B_v1B_0_30
**Wall time**: 61.7s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=23988, completion=3697, reasoning=2586, total=27685

---

# v1B.0.30 Review

## PAPER-GPT-B1 — BLOCKER — Rendered body still contains reviewer-ID/audit-log text

**Section:** Table 1B footnote; §III caveats; §IV NaMaster paragraph; §V; §VII tables/captions; Conclusions; Appendix A.  
**Issue:** Scrub did not land. Rendered text still contains `R8 GEM-B3`, `R5 + R7 GEM-B1 + GPT-B1`, `R14 GEM-B1`, `R7 GEM-B2 + GPT-B4`, `GPT-M6`, `R12 GEM-M2`, “3-vendor convergent R2 BLOCKER”, version-audit prose, and stale internal-version markers.  
**Fix:** Remove all reviewer IDs, audit-history prose, and version-gating text from rendered body/captions/footnotes; keep only scientific statements or move audit history to TeX comments not shipped.

## PAPER-GPT-B2 — MAJOR — Marginal σ values are overused as joint evidence for $w_0w_a$

**Section:** Table 1B; §III physics interpretation; §V; §VII; Conclusions.  
**Issue:** The paper says LCDM is disfavored “at the joint level” using only marginal $w_0$ and $w_a$ σ distances. Without the $w_0$–$w_a$ covariance, Mahalanobis distance, profile likelihood, or nested-model evidence, the joint exclusion/“phantom-crossing required” framing is not justified.  
**Fix:** Provide the 2D covariance/contours and compute $\Delta\chi^2$ or posterior mass relative to $(w_0,w_a)=(-1,0)$; otherwise state only marginal posterior offsets and remove “joint-level”/“required” language.

## PAPER-GPT-B3 — MAJOR — Dataset/model stacks are internally inconsistent

**Section:** §V.1, §V.2, Table 1B, Table inventory.  
**Issue:** §V claims four dataset combinations using DESI 2024 DR1 / Pantheon+ / SH0ES / DES Y3, while Table 1B uses DESI DR2 + Planck NPIPE + DES-Y5 + Pantheon+, and the model-comparison paragraph mixes the $\Delta N_{\rm eff}$ frozen-chain discussion with the separate iter2 $w_0w_a$ chain. This prevents a clean methodological audit of which likelihood stack produced which posterior.  
**Fix:** Split the $\Delta N_{\rm eff}$ proxy and $w_0w_a$ iter2 analyses into separate method blocks with exact YAML likelihood names, dataset releases, sampled parameters, priors, and chain IDs.

## PAPER-GPT-B4 — MAJOR — SH0ES likelihood framing is wrong/misleading

**Section:** §II; §III caveats, “M$_B$--H$_0$ joint-posterior offset check.”  
**Issue:** The text repeatedly calls the full-tension run a “SH0ES $H_0$ prior,” but later says the active likelihood is `H0.riess2020Mb`, an $M_B$ calibration prior. The 3.2σ $M_B$--$H_0$ offset check uses the marginal $\sigma_{M_B}$ instead of the covariance/error of the constrained combination.  
**Fix:** Call the likelihood an SH0ES/Cepheid $M_B$ calibration prior unless a direct Gaussian $H_0$ prior is actually used; recompute the tension in the correct variable with the full covariance.

## PAPER-GPT-B5 — MAJOR — ALP parameter inference/range claims are under-specified and inconsistent

**Section:** §VI, “Birefringence value” and “MCMC parameter estimation.”  
**Issue:** The claimed natural scan $C_{a\gamma}\in[4,12]$ gives $\beta=0.17$--$0.43^\circ$ only via an undocumented “joint-trajectory” restriction, while the later inversion of the observed $\beta$ requires $C_{a\gamma}\sim9$--$51$. The ALP-MCMC description also conflates fixed-$C_{a\gamma}=8$ and free-$\beta$ fits over the same 9,720 samples.  
**Fix:** Publish the actual ALP priors, trajectory map, likelihood, and posterior summaries; separate fixed-coupling ALP fits from free-$\beta$ fits and align the “natural” coupling range with the reported posterior/inversion.

## PAPER-GPT-B6 — minor — NaMaster systematic budget is not propagated

**Section:** §IV; Conclusions.  
**Issue:** The pipeline bias $0.032$--$0.040^\circ$ is carried as a “systematic floor,” but no uncertainty on the bias estimate, SNR definition, or propagation rule is given. “Unbiased at the $0.04^\circ$ level” is too strong from two nonzero injections plus a null.  
**Fix:** Define SNR and the $\hat\beta$ estimator, quote MC mean/error for each injection, and state explicitly whether the $0.040^\circ$ floor is added linearly or in quadrature when used downstream.
