# P1B R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R29_P1B_v1B_0_30
**Wall time**: 138.1s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=23404, completion=5865, reasoning=5391, total=29269

---

## PAPER-DEE-B1 (MAJOR) — ALP field-displacement range [0.2, 1.1] lacks a traceable source

**Section:** §VI (Spectator-ALP consistency check), echoed in Conclusions.  
**Issue:** The headline range $\Delta\phi/f_a \in [0.2, 1.1]$ (and the fiducial value $0.65$) is stated as the output of numerical integration of the ALP equation of motion, but no script, notebook, or data file is referenced in the paper or the reproducibility appendix. The ALP MCMC chains are provided, but the field-evolution integration that produces these numbers is not. A reviewer cannot verify the range without re‑implementing the integration from scratch.  
**Fix:** Add the integration script (or a pre‑computed CSV of $\Delta\phi/f_a$ vs. $m/H_0$, $\theta_i$) to `reproducibility/alp/` and cite it in the text (e.g., “see `alp_field_displacement.py` in the reproducibility repository”).

---

## PAPER-DEE-B2 (minor) — NaMaster recovery values not linked to a static output artifact

**Section:** §IV (Data Methods: CMB E-B Analysis) / Conclusions.  
**Issue:** The paper claims $\hat\beta = 0.238^\circ$ (bias $0.032^\circ$) and $\hat\beta = 0.302^\circ$ (bias $0.040^\circ$) from the 500‑MC pipeline. The driver script is referenced (`pipelines/h200_results/pod1_namaster_umap_2026-04-29/`), but no specific output file (JSON, log, or summary table) containing these exact numbers is identified. A reviewer must re‑run the full pipeline to confirm the values, which is unnecessarily heavy for a static verification.  
**Fix:** Include a `recovery_summary.json` (or similar) in the pipeline directory that stores the injected $\beta$, recovered $\hat\beta$, and bias for each injection, and point to it in the text (e.g., “see `recovery_summary.json` for the per‑injection values”).
