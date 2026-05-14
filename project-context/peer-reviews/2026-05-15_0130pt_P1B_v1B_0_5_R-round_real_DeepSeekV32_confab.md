# P1B_v1B_0_5 R-round — REAL cross-vendor — DeepSeek-V3.2 confabulation-hunter

**Model**: `deepseek/deepseek-v3.2` (via OpenRouter)
**Round**: 2026-05-15_0130pt
**Wall time**: 44.2s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=12383, completion=1520, total=13903

---

**Adversarial Peer Review Findings**

**BLOCKER 1 – PAPER-DEE-B1**  
**Section:** Abstract, Sec. 3 (footnote), Sec. 7 (Table 1 inventory)  
**Issue:** Sample-count arithmetic irreproducible from displayed values. Abstract claims “309,789 frozen MCMC samples across 2 converged dataset combinations.” Sec. 3 footnote breaks this into 176,840 + 132,949 = 309,789 raw samples, then states post-burnin = 0.7 × 309,789 = 216,852. But 0.7 × 309,789 = 216,852.3, while the footnote also gives a “full-tension subset alone” post-burnin count of 123,129 and calls the earlier 123,129 figure an “arithmetic error.” The text then says the correct both-chains post-burnin total is 216,852, but no script or JSON is cited that computes these numbers from the raw samples. The 114,992 Planck-only ongoing samples are mentioned but not included in the 309,789 total, yet Table 1 lists “Planck-only” as 114,992 samples with status “Ongoing” – implying it is part of the MCMC program but not part of the frozen headline count. This is internally inconsistent and lacks a single reproducible script that outputs these stratified counts.  
**Fix:** Provide a single script (`sample_counts.py` or `convergence_summary.json`) that outputs raw samples, burnin fraction, and post-burnin counts for each dataset combination, and clearly separate frozen vs. ongoing chains in the abstract.

**BLOCKER 2 – PAPER-DEE-B2**  
**Section:** Sec. 5 (model comparison paragraph)  
**Issue:** Δχ²eff = –7.9 incompatibility with ΔNeff posterior. The text states Δχ²eff = –7.9 for one extra parameter is “in apparent tension with the full-tension posterior ΔNeff = –0.020 ± 0.169 (the nested value ΔNeff = 0 sits at 0.12σ from the posterior mean, where a Gaussian nested likelihood predicts Δχ²eff closer to zero than to –8).” This is a direct statistical contradiction: if ΔNeff posterior is consistent with zero at 0.12σ, the likelihood ratio should be ~0, not –7.9. The paper acknowledges this as an “on-record deferral” pending recomputation, but the Δχ²eff = –7.9, AIC, BIC values are still presented in Table 2 and the conclusions. Using inconsistent numbers in the results table is a blocker.  
**Fix:** Remove the model-comparison table (Table 2) and all Δχ²eff/AIC/BIC/ln B references until a single recomputation from the frozen-thinned chain is provided and validated.

**BLOCKER 3 – PAPER-DEE-B3**  
**Section:** Sec. 5 (footnote and paragraph), Sec. 7 (Table 1)  
**Issue:** ln B = +4.8 Savage‑Dickey provenance missing. The text states the Savage‑Dickey figure is “indicative only” and biased due to high correlation (r = –0.89), but no script or method is cited that computes it from the chains. The footnote says it is “dataset‑dependent” and gives two values (–1.2 ± 0.3 and +4.8 ± 0.5) but no provenance. The paper deferral mentions that `convergence_summary.json` carries ΔNeff = –0.020 ± 0.169 but not the SD numerator/denominator estimates. This is a blocker because the Bayes factor is a load‑bearing scalar in the model‑comparison section without traceable source.  
**Fix:** Provide a script (`bayes_factor.py`) that computes Savage‑Dickey from the frozen‑thinned chains and outputs numerator/denominator estimates, or remove all ln B claims.

**MAJOR 1 – PAPER-DEE-M1**  
**Section:** Sec. 3 (paragraph on cross‑validation), Sec. 7 (cross‑paper status table)  
**Issue:** Independent cross‑validation citation mismatched. Sec. 3 cites “Liu et al. (2025) constrained an EC torsion model using DESI DR2 + Pantheon+ + DES‑SN5YR + Planck 2018, finding torsion preferred by AIC (ΔAIC = –5.7 to –6.6). Our MCMC agrees at 0.5σ in H0 and 0.4σ in σ8.” But the cross‑paper status table (Table 1) lists Paper 2 as “SPHEREx fNL forecast, MegaMapper outlook” and Paper 3 as “Multi‑survey anomaly catalog,” not an EC torsion model paper. The Liu et al. reference is not in the bibliography, and the claim of agreement at 0.5σ/0.4σ is not backed by a direct comparison table or script.  
**Fix:** Add the Liu et al. reference to the bibliography and provide a small table or script output comparing H0 and σ8 posteriors between this work and Liu et al.

**MAJOR 2 – PAPER-DEE-M2**  
**Section:** Sec. 4 (NaMaster pipeline description)  
**Issue:** Pipeline‑recovery SNR numbers (20.32, 25.71) lack provenance. The text says injecting β = 0.27° recovers 0.238° at SNR = 20.32, and β = 0.342° recovers 0.302° at SNR = 25.71. No script or JSON is cited that computes these SNR values from the 500 MC realizations. The paper states the driver script, mask, MC seeds, and binning spec are in `pipelines/h200_results/pod1_namaster_umap_2026‑04‑29/`, but that path is not a reproducible artifact in the repository (the reproducibility appendix points to a GitHub repo, but no such subdirectory is listed).  
**Fix:** Provide a script (`namaster_snr.py`) in the reproducibility materials that outputs the recovery angle and SNR for each injection, or remove the SNR numbers.

**minor 1 – PAPER-DEE‑m1**  
**Section:** Sec. 7 (DESI DR2 w0wa chain status)  
**Issue:** DESI DR2 chain compute‑stall not acknowledged. The text says the DESI DR2 w0wa chain is “running on a dedicated MPI pod” and “convergence expected in ~3 days from 2026‑05‑05.” But the round context states the chain has been stalled for ~12 hours (last checkpoint flushed 15:43 UTC). The paper does not mention this stall or update the expected convergence time. This is a minor transparency issue.  
**Fix:** Add a sentence in Sec. 7 or the conclusions noting that the DESI DR2 chain is currently stalled at ~53,736 samples and convergence is delayed pending debugging.
