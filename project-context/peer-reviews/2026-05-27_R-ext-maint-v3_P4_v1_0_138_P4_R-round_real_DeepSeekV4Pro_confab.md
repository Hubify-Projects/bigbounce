# P4 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-27_R-ext-maint-v3_P4_v1_0_138
**Wall time**: 260.3s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=101059, completion=12509, reasoning=12235, total=113568

---

# Adversarial Peer Review — Provenance Audit

## PAPER-DEE-M1 (MAJOR) — Abstract `~0.6%` residual amplitude has no traceable source

**Section:** Abstract  
**Issue:** The abstract states *“The real-space post-TTA Catalog~C dipole is +0.43σ (p=0.30, ∼0.6% residual amplitude).”* The main text (§4.3, Simple dipole) reports the significance (0.43σ, p=0.30) but never gives the dipole amplitude in percent. No artifact path, JSON file, or script is cited anywhere in the paper that would produce the `∼0.6%` figure. It is a headline number in the abstract without provenance and cannot be reproduced from displayed values.  
**Fix:** Either remove the amplitude claim from the abstract, or add a sentence in §4.3 that states the best-fit dipole amplitude (in percent) together with a pointer to the corresponding artifact (e.g., `pipelines/p2_chirality/outputs/dipole/summary.json`).

---

*No other findings.* The remaining load-bearing scalars in the abstract and conclusions all have corresponding artifact references or are directly derived from values that are linked to on-disk JSON/scripts/tables.
