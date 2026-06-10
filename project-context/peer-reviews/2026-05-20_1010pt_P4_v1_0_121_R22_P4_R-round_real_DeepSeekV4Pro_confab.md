# P4 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-20_1010pt_P4_v1_0_121_R22
**Wall time**: 636.6s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=88264, completion=10773, reasoning=9915, total=99037

---

# Adversarial Peer Review — Traceability Audit

## PAPER-PROV-MINOR-1: Abstract missing direct artifact link for HC-spiral count

**Location:** Abstract L2–L3 (`471,049 high-confidence per-spiral after p_CW^eq > 0.9`)  
**Class:** minor  
**Issue:** The number 471,049 appears in the abstract without an immediate footnote or artifact pointer. The derivation (apply `p_CW_eq > 0.9` to Catalog C) is described later in §X.J, and the corresponding injection‑recovery artifact (`injection_recovery_extended.json`) implicitly carries this sample size, but no direct abstract‑level citation is given.  
**Fix:** Add a footnote in the abstract cross‑referencing the artifact that records the exact HC‑spiral count, or embed a quick catalog‑filtered count script in the repository.

## PAPER-PROV-NIT-2: Canonical-mask `+3.64σ` rounding from displayed values

**Location:** Abstract L11, §V.D multi-null battery (v1.0.107 correction)  
**Class:** nit  
**Issue:** The text displays `C1 = 1.51e-5`, null mean `3.12e-6`, null std `3.31e-6`. Computing `(1.51e-5 - 3.12e-6) / 3.31e-6 = 3.617` → rounds to `+3.62σ`. The paper quotes `+3.64σ`, which may arise from higher‑precision inputs (e.g., `3.116e-6`, `3.309e-6`). The displayed rounded numbers do not reproduce the quoted sigma to two decimals.  
**Fix:** Either quote the null moments to sufficient precision (four significant figures) so that the arithmetic exactly matches `+3.64`, or note that the headline value is rounded from artifact precision.

## PAPER-PROV-NIT-3: MASTER-decoupled monopole‑only null `+4.84σ` rounding

**Location:** §V.D v1.0.121 closure paragraph (`C1 = 6.55e-6`, null mean `8.0e-7`, std `1.19e-6`)  
**Class:** nit  
**Issue:** Computing from the displayed three‑significant‑figure values yields `(6.55e-6 - 0.80e-6) / 1.19e-6 = 4.83` (or `4.83σ`). The text states `+4.84σ`. Again, rounding of the underlying artifact is slightly inconsistent.  
**Fix:** Use the artifact’s full‑precision values for the in‑text calculation or adjust the quoted sigma to match the rounded display values.

## PAPER-PROV-MINOR-4: Leg‑proxy 25% fraction not self‑contained

**Location:** §V.D v1.0.119 closure (leg‑proxy induced ℓ=1 amplitude)  
**Class:** minor  
**Issue:** The derivation `summed induced amplitude = 1.77×10^{-3} → 25% of a1_obs=7.04×10^{-3}` uses leg‑fraction `a1(leg‑fraction)` values that are not displayed in the paper. The artifact `morphology_template_l1_projection.json` is cited, but the arithmetic cannot be reproduced from the paper alone.  
**Fix:** Include the leg‑fraction `a1` values (or the full vector) in a short table or footnote so that a reader can verify the 25% without opening the JSON.

---

**Summary:** No BLOCKER‑grade provenance failures were found. All load‑bearing scalars in the abstract and conclusions trace to a named on‑disk JSON artifact. The four minor/nit flags above concern rounding hygiene and self‑contained arithmetic; they do not undermine the numeric reliability of the paper.
