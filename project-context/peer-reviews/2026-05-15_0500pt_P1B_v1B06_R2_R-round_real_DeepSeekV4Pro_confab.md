# P1B_v1B06_R2 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-15_0500pt
**Wall time**: 111.0s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=12720, completion=5964, reasoning=5240, total=18684

---

## PAPER-DEE-B1 (MAJOR) — Model-comparison statistics in Table 2 and Conclusions are not traceable to the final frozen-thinned chain

**Location:** Table 2, Sec. 5 (Cosmological Fits), and Conclusions (Sec. 8).  
**Issue:** The paper presents \(\Delta\chi^2_{\rm eff} = -7.9\), \(\Delta\text{AIC} = -5.9\), \(\Delta\text{BIC} = -0.7\), and \(\ln B = +4.8\) as model-comparison metrics, and the Conclusions call the AIC/BIC differences “the primary cross-references.” However, the paper itself states (Sec. 5, “Real cross-vendor adversarial-review deferrals”) that these numbers were taken from earlier sweep-phase outputs and are **not** recomputed from the final frozen-thinned chain; the recomputation is an on-record deferral. The numbers therefore cannot be reproduced from the current chain state and are explicitly flagged as preliminary, yet they are still used as load-bearing cross-references in the Conclusions.  
**Fix:** Either remove these numbers from the Conclusions until the one-pass recomputation from the final chain is complete and documented, or add an unambiguous statement that they are **not** verified against the final chain and must not be used for model comparison.

---

## PAPER-DEE-B2 (MAJOR) — Savage-Dickey \(\ln B = +4.8\) lacks a provenance script

**Location:** Sec. 5 (footnote 2 and displayed equation) and Conclusions (Sec. 8).  
**Issue:** The paper quotes \(\ln B = +4.8 \pm 0.5\) (full-tension) as a Savage-Dickey indicative figure. The round context confirms that the Savage-Dickey provenance script is one of the five compute-bound items deferred to v1B.0.7 and is **not** present in the current repository. The number is therefore not reproducible from the provided materials, and no script or auditable derivation is available.  
**Fix:** Provide the Savage-Dickey computation script in the reproducibility repository, or remove the \(\ln B\) value from the paper until the script is delivered.

---

## PAPER-DEE-B3 (minor) — NaMaster pipeline-recovery SNR is undefined

**Location:** Sec. 4 (Eq. (1) and surrounding text).  
**Issue:** The paper reports “pipeline-recovery SNR=20.32” (and 25.71) for the NaMaster injection tests, but never defines how SNR is computed from the 500 Monte Carlo realizations (e.g., mean recovered \(\beta\) divided by standard error of the mean, or some other metric). The driver script is referenced, but the text itself gives no definition, making the number opaque without executing the code.  
**Fix:** Add a one-sentence definition of the SNR metric (e.g., “SNR is the mean recovered \(\beta\) divided by the standard error of the mean across the 500 MC realizations”).

---

## PAPER-DEE-B4 (minor) — Abstract implies a single \(H_0\) for both frozen dataset combinations

**Location:** Abstract, line “\(H_0 = 67.68\pm 1.06\,\text{km\,s}^{-1}\,\text{Mpc}^{-1}\)”.  
**Issue:** The abstract says “Both frozen dataset combinations find … \(H_0 = 67.68\pm 1.06\)”, but Table 1 shows the Planck+BAO+SN combination gives \(H_0 = 67.79\pm 1.09\). The abstract incorrectly suggests a single value applies to both combinations.  
**Fix:** Either quote both \(H_0\) values or explicitly state that the quoted \(H_0\) is from the full-tension combination only.

---

## PAPER-DEE-B5 (nit) — Cross-paper readiness percentages are subjective and untraceable

**Location:** Table 1 (Cross-paper status table), readiness column (73%, 64%, 81%, 84%, 95%).  
**Issue:** The readiness percentages are presented as quantitative status indicators but are not derived from any objective, reproducible metric; they are effectively author judgments. While not load-bearing for the science, they appear as numerical claims with no provenance.  
**Fix:** Either remove the percentages and replace with qualitative status labels (e.g., “in progress”, “near completion”), or provide a defined rubric that maps checklist items to the percentages.
