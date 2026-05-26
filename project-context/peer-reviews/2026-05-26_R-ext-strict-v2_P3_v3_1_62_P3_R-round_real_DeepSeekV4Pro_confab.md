# P3 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-strict-v2_P3_v3_1_62
**Wall time**: 102.3s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=65487, completion=7157, reasoning=6604, total=72644

---

## PAPER-DEE-M1 (MAJOR) — Genuine-novelty fraction lacks on‑disk artifact

**Location:** Abstract (paragraph beginning “Extended archival cross‑matching…”) and Section 4.1 (“Archival cross‑match and genuine novelty fraction”).  
**Issue:** The headline discovery metric “∼17.8% genuine novelty fraction” (178/1000 DESI top‑anomalies absent from 20 all‑sky catalogs) is not accompanied by a direct file path, script, or even a raw matched/unmatched count table. The paper promises a “companion data release” and a “deeper NED+VizieR sweep,” but no specific JSON, Parquet, or CSV artifact is named in the vicinity of the number. A reader cannot reproduce or audit the fraction from the displayed values alone.  
**Fix:** Cite the exact artifact (e.g., `crossmatch_novelty_top1000.json`) in the text and include a brief summary of the raw counts (e.g., 822 matched, 178 unmatched) so that the arithmetic and provenance are self‑contained.

---

## PAPER-DEE-m1 (minor) — Fisher‑positivity parameters not directly traceable to a single output file

**Location:** Abstract (Fisher forecast: “$1/\sigma_{f_{\rm NL}}^2 = F_0 + c\,\alpha^2$ with $F_0 = 1/8.98^2$ and $c = 0.0747$”) and Section 5.  
**Issue:** The constants $F_0$ and $c$ are derived from Fisher‑matrix runs at $\alpha=0$ and $\alpha=0.15$, yet the paper references only a script directory (`pipelines/…wave_14_ii_fisher_systematics/`) **without naming a specific output JSON** that records the baseline $\sigma_{f_{\rm NL}}(0)=8.98$ and the enhanced $\sigma_{f_{\rm NL}}(0.15)=8.43$ used to fit $c$. The abstract’s central forecast $\sigma_{f_{\rm NL}} = 8.14$ and its envelope $[3.92, 8.98]$ therefore depend on a coefficient whose exact provenance is not pinned to a single, auditable on‑disk file.  
**Fix:** Provide the path to the JSON/Parquet output that contains the anchor‑point Fisher numbers (e.g., `fisher_anchors.json`) so that the $c$ coefficient can be recomputed exactly from the same file that produced the numbers.
