# paper1b R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-21_R25_P1B_v1B_0_20
**Wall time**: 418.3s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=18520, completion=12675, reasoning=12236, total=31195

---

## PAPER-DEE-M1 (MAJOR) — NaMaster pipeline-recovery figures lack uncertainty quantification and SNR provenance

**Location:** Abstract (lines ~47–50) and §4 (Eq. 1, discussion after).  
**Issue:** The headline recovery values \(\hat\beta=0.238^\circ\) (SNR = 20.32) and \(\hat\beta=0.302^\circ\) (SNR = 25.71) are reported as point estimates with zero uncertainty. No standard deviation, standard error of the mean, or MC dispersion is given anywhere in the paper, and the text does not define how SNR is computed from the 500 realisations (e.g., mean / standard error). A reader cannot verify the SNR from displayed numbers, nor judge whether the bias \(0.032^\circ\) is statistically significant.  
**Fix:** Add a table with the MC ensemble mean, the MC standard deviation, the standard error of the mean, and the SNR formula explicitly; point to the specific output file (e.g. a CSV/JSON) in the `pipelines/h200_results/…` directory that contains those summary statistics. Declare the MC noise level used for the SNR denominator.

---

## PAPER-DEE-M2 (minor) — No explicit output file for the recovered angles cited in the abstract

**Location:** §4 and Appendix A (reproducibility).  
**Issue:** The abstract states \(\hat\beta_{\rm NaMaster}=0.238^\circ\) as a load-bearing scalar. The paper says the driver script is in `pipelines/h200_results/pod1_namaster_umap_2026-04-29/` but does not name a file containing the numerical result (e.g. `summary_stats.json`). A reader must execute the full pipeline to obtain the number; no static provenance is provided.  
**Fix:** Include a direct link to a static artifact (e.g. a CSV or JSON) that contains the recovery values, so the headline number can be audited without re-running the pipeline.
