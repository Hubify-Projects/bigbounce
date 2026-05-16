# P4_v1093 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-16_0030pt_P4_v1093_R12_R-round_real
**Wall time**: 533.2s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=77272, completion=16000, reasoning=15350, total=93272

---

# Adversarial Peer Review — `chirality_catalog_paper` v1.0.93

**Overall verdict:** No blocker‑grade issues found. The paper has meticulously linked load‑bearing numbers to on‑disk artifacts. A handful of minor provenance‑clarity and precision inconsistencies remain, which should be fixed before external review.

## Findings Summary

| ID | Class | Location | Issue | Fix | Truth‑Audit |
|----|-------|----------|-------|-----|-------------|
| REVIEW‑F1 | minor | Abstract, two occurrences of monopole‑null numbers | The same null mean and uncertainty are given with different precision: first `1.6846×10⁻² ± 6.8×10⁻⁵`, then `1.68×10⁻² ± 0.07×10⁻³`. | Use the same rounding (preferably the higher‑precision `1.6846`/`6.8e-5`) in both sentences. | Artifact `monopole_mask_null_results.json` carries the higher‑precision values; no data error, just rounding mismatch. |
| REVIEW‑F2 | minor | Abstract + Sec. 4 (Dipole) | The `+6.48σ` pre‑MASTER pseudo‑\(C_\ell\) bandpower is not directly footnoted with its artifact in the abstract; the reader must cross‑reference the corrected‑shot‑noise footnote later in the body. | Add a brief parenthetical or footnote in the abstract pointing to the recompute artifact (`wave11c_nspiral_recompute_2026-05-01/results.json`). | Artifact exists and produces `+6.48σ` when using \(N_\mathrm{spiral}=3{,}201{,}160\) normalisation; the number is reproducible. |
| REVIEW‑F3 | nit | Table V footnote | The footnote explains a 4,758‑galaxy gap via “`abs(p_cw_eq) > 0.6` inclusion convention”, but `abs(p_cw_eq)` is not a meaningful expression for a probability in [0,1]; the intended HC‑spiral cut is `max(p_CW_eq, p_CCW_eq) > 0.6`. | Rewrite the footnote to use the correct predicate, e.g. `max(p_CW_eq, p_CCW_eq) > 0.6`. | The underlying cut is defined correctly elsewhere; the discrepancy is purely a textual slip. |
| REVIEW‑F4 | minor | Table III | The bandpower significance `z`‑scores are given without the null‑mean column; the reader cannot verify the \(z\)‑values without the companion MC log. | Add a column for \(\langle C_\ell^{\mathrm{null}}\rangle\) (the paper already plans this for the next revision). | The on‑disk MC log provides the null means; the `z`‑values can be recomputed and match the table. |

---

## REVIEW‑
