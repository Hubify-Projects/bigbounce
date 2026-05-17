# P1B_v1B09 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-17_1030pt_P1B_v1B09_R5_R-round_real
**Wall time**: 235.0s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=12723, completion=6622, reasoning=5956, total=19345

---

## PAPER-DEE-B1 — BLOCKER
**Sec. 4 (Data Methods), Eq. (1), and Abstract.**  
The pipeline-recovery SNR values (20.32 for β=0.27°, 25.71 for β=0.342°) are stated as headline validation metrics, but the standard deviation of the recovered β from the 500 MC realizations is not given anywhere in the paper. Without σ(β̂) the SNR cannot be verified from displayed numbers, and no output file (e.g., a JSON with mean and std) is cited.  
**Fix:** Add the MC standard deviation (e.g., σ=0.0117° for SNR=20.32) in the text or reference the exact file in `pipelines/h200_results/pod1_namaster_umap_2026-04-29/` that contains the SNR calculation.

## PAPER-DEE-M1 — MAJOR
**Sec. 6 (Cosmic Birefringence), paragraph “MCMC parameter estimation”.**  
The value `β_free = 0.344° ± 0.096°` is introduced as a “model-independent fit” and used to claim consistency with the ALP MCMC result, but its origin is never defined. No description of the fit (data, likelihood, priors) or citation is provided. The number appears untraceable.  
**Fix:** Either remove the β_free comparison entirely, or explicitly state that it comes from a separate MCMC run (e.g., with β as a free parameter using the same birefringence data) and give the configuration details.

## PAPER-DEE-M2 — MAJOR
**Sec. 6, “MCMC parameter estimation”.**  
The ALP MCMC sampling is reported with 9,720 samples and a posterior `β_ALP = 0.336° ± 0.107°`, but the likelihood function is never defined. The reader cannot know what data were fitted (the published β measurements? the combined value?) or what priors were used.  
**Fix:** Add a sentence specifying the likelihood (e.g., Gaussian likelihood using the Eskilt et al. β = 0.342° ± 0.094° measurement) and the prior ranges for the ALP parameters.

## PAPER-DEE-m1 — minor
**Sec. 3 (Table I) and Sec. 5.2 (Table II).**  
The raw MCMC sample counts (176,840; 132,949) and the parameter constraints in Table I are not directly linked to a specific output file in the reproducibility repository. The paper mentions `convergence_summary.json` for post-burnin counts, but no file is cited as the source of the raw counts or the GetDist summary statistics.  
**Fix:** Add a footnote pointing to the exact CSV/JSON file(s) on HuggingFace or in the repository that contain the raw chain lengths and the parameter means/errors.

## PAPER-DEE-m2 — minor
**Sec. 6, “ALP field evolution”.**  
The field displacement `Δφ/f_a ≈ 0.65` and the range `[0.2, 1.1]` are stated to come from numerical integration of the ALP equation of motion, but the integration code is not referenced in the paper or the listed reproducibility materials.  
**Fix:** Include the integration script in the repository and add a sentence pointing to its location (e.g., `pipelines/alp_field_evolution.py`).

## PAPER-DEE-m3 — minor
**Sec. 3 and Sec. 6 (MCMC diagnostics).**  
The R5 context lists “MCMC acceptance/autocorr diagnostics” as a deferred item now closeable, but the paper provides no acceptance rates or autocorrelation lengths for any of the MCMC chains (only R̂−1 and min ESS). The item remains unaddressed.  
**Fix:** Either add a brief diagnostic table (acceptance fraction, autocorrelation time) for the frozen chains, or explicitly state that these diagnostics are not required for the proxy verification scope and close the item.
