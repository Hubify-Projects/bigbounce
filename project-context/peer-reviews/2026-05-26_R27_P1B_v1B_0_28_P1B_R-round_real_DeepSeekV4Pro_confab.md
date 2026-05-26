# P1B R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R27_P1B_v1B_0_28
**Wall time**: 245.6s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=23066, completion=8358, reasoning=7545, total=31424

---

## Finding PAPER-DEE-B1 (BLOCKER)  
**Section:** Abstract (L130–L150) and §IV (NaMaster pipeline)  
**Issue:** The abstract reports pipeline-recovery numbers (β̂=0.238°, bias=0.032°, SNR=20.32 for β=0.27°; bias=0.040°, SNR=25.71 for β=0.342°) that are load‑bearing verification claims, yet **no static output file** (JSON, CSV, or HDF5) exists in the repository to store these exact quantities. The paper points only to a script directory (`pipelines/h200_results/pod1_namaster_umap_2026-04-29/`), which defines the method but provides no locked artifact; re‑running the Monte Carlo is not a substitute for a checksummed file that precisely reproduces the stated numbers. This defeats the companion paper’s reproducibility commitment.  
**Fix:** Add a summary file (e.g., `namaster_recovery_summary.json` or a CSV containing the mean β̂, bias, and SNR for each injection) to the repository and update the NaMaster section to cite its exact path, so a reviewer can inspect the values without re‑executing the full 500‑MC pipeline.

## Finding PAPER-DEE-B2 (MAJOR)  
**Section:** Abstract (L135–L140) and §VI (ALP consistency check)  
**Issue:** The fiducial ALP birefringence prediction β≈0.27° and the broad range [0.17,0.43]° are headline numbers used to claim consistency, yet **no script or execution trace for the underlying numerical integration of the ALP equation of motion** (Δφ/fa) is provided or referenced. The paper mentions ALP MCMC chains but not the direct trajectory integrator that produces Δφ/fa ≈ 0.65, 1.0, etc. Without that integrator and its output, the stated β values are irreproducible.  
**Fix:** Include the integration script (e.g., `alp_field_evolution.py`) and a small output file (a CSV of (m/H₀, θᵢ, Δφ/fa) tuples) in the repository, and add a pointer to this artifact in §VI so the derivation from Cₐγ and Δφ/fa is fully auditable.

## Finding PAPER-DEE-B3 (minor)  
**Section:** §IV (NaMaster pipeline) and Abstract  
**Issue:** The reported pipeline‑recovery SNR figures (20.32, 25.71) are given **without a definition** (e.g., SNR ≡ β̂/σ_β̂, where σ_β̂ is the standard error from the 500‑MC ensemble). This ambiguity prevents a reviewer from independently verifying the SNR from the raw MC output, should output files ever be provided.  
**Fix:** Add a one‑sentence statement: “SNR is defined as the recovered mean β̂ divided by its standard error σ_β̂ = std({β̂ᵢ})/√500,” preferably in the NaMaster paragraph that first uses the term.

## Finding PAPER-DEE-B4 (minor)  
**Section:** Abstract (L100)  
**Issue:** The headline sample count “309,189 frozen samples” appears in the abstract **without a footnote or parenthetical that links it to the body’s explicit breakdown** (fn:sample_stratification). A reader scanning the abstract cannot immediately see that this sum comes from 176,240 + 132,949 without hunting through the body text, weakening rapid auditability.  
**Fix:** Add a short parenthetical “(= 176,240 + 132,949; see §III footnote)” in the abstract to make the provenance instantly visible.
