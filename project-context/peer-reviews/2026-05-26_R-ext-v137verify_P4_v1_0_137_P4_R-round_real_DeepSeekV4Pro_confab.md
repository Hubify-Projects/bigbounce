# P4 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-v137verify_P4_v1_0_137
**Wall time**: 142.9s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=100254, completion=9603, reasoning=8971, total=109857

---

## P4-ADV1 (minor) — Canonical-mask pixel count in joint nuisance model fit is inconsistent with the canonical mask used elsewhere

- **Location:** New §VI.D paragraph (Conclusions, near “Joint nuisance-marginalized model fit (v1.0.137)”) and v1.0.137 round context.
- **Issue:** The fit uses `n = 36,418` in‑mask pixels, but the paper’s established canonical mask (≥10 spirals per pixel) has only ~24,087 pixels (Table III caption, Table VI caption). The paragraph calls this “canonical NSIDE=64 in‑mask pixels” without stating the minimum‑pixel‑count threshold, making the pixel sample ambiguous. The discrepancy could affect the regression because sparsely populated boundary pixels, excluded by the canonical cut, are included here.
- **Fix:** Clarify whether the fit uses all pixels with `n_total > 0` (the raw survey footprint) or a different threshold, explain why the pixel count differs from the canonical‑mask definition, and either reconcile the numbers or rename the mask to avoid confusion.

## P4-ADV2 (minor) — No explicit script provenance for the joint nuisance fit in the paper body

- **Location:** Conclusions, same paragraph.
- **Issue:** The companion artifact path (`joint_nuisance_model_fit.json`) is given, but the Python script that produced it (`scripts/joint_nuisance_model_fit.py`, mentioned in the v1.0.137 header comment) is not referenced in the manuscript text. A reader who wants to reproduce the fit from the design matrix and weighting would need the script; citing only the JSON is insufficient for full algorithmic traceability.
- **Fix:** Add a sentence citing the script path (e.g., “Driver: `pipelines/p2_chirality/scripts/joint_nuisance_model_fit.py`”) alongside the artifact reference.

## P4-ADV3 (nit) — Conversion between A_dipole map units and f_CW units is not stated explicitly

- **Location:** Same paragraph.
- **Issue:** The fit yields `A_dipole^best = 4.55×10⁻³` and states “equivalent to 0.23% in f_CW units”, but the conversion factor (map‑unit amplitude = 2 × f_CW‑dipole amplitude) is not spelled out; readers must infer it from the earlier “full‑amplitude convention” discussion or from the statement that `A=1.7%` corresponds to `A_dipole=0.034`. A one‑line reminder would eliminate any risk of factor‑of‑2 confusion.
- **Fix:** Add a brief parenthetical note: “(since the A_p field has amplitude 2·(f_CW − 0.5), a dipole amplitude A_f in f_CW corresponds to A_dipole = 2·A_f in map units).”
