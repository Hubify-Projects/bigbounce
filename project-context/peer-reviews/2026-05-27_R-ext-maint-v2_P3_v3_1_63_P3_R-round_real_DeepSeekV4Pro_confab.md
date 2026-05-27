# P3 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-27_R-ext-maint-v2_P3_v3_1_63
**Wall time**: 175.7s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=66355, completion=7749, reasoning=7063, total=74104

---

## Findings

### PAPER-DEE-B1 (BLOCKER)
**Location:** Abstract and Section 5 (Cosmological Applications)  
**Issue:** The multi-tracer Fisher forecast values—$\sigma(f_{\rm NL})=8.98$ (baseline), $8.43$ (at $\alpha=0.15$), $8.14$ (empirical $\alpha=0.19$), and the derived $c=0.0747$—are load‑bearing headline numbers with no traceable on‑disk artifact. The paper references a Fisher pipeline but does not cite a specific JSON/script that produced these outputs (e.g., a `fisher_results.json`). The $\alpha^2$ form coefficients rely on two anchor points whose provenance is not linked to a concrete file.  
**Fix:** Provide a companion artifact (e.g., `pipelines/.../fisher_anchor_results.json`) containing the baseline and fiducial $\sigma(f_{\rm NL})$ values, or explicitly document the exact input parameters and code commit that reproduce these numbers.

### PAPER-DEE-M1 (MAJOR)
**Location:** Abstract and §4.1 (SIMBAD Cross‑Match)  
**Issue:** The genuine novelty fraction of $17.8\%$ (178/1,000) for DESI top‑1,000 anomalies is presented as a key discovery metric, but the paper does not point to a cross‑match artifact that lists the 20 catalogs used, the matched/unmatched status of each object, or the script that generated the count. The data release may contain it, but no file path is specified.  
**Fix:** Add a reference to a released parquet or JSON file (e.g., `desi_top1000_xmatch_20cats.json`) and state the exact catalog list in the data‑availability section.

### PAPER-DEE-min1 (minor)
**Location:** Abstract opening sentence  
**Issue:** The abstract states “37.3~million sources and CMB map patches”, but the Path‑C processed total in Table 1 is $37{,}272{,}042$ (summing the seven retained surveys). This is a $\sim 28{,}000$‑source rounding discrepancy that does not match the explicit total used elsewhere.  
**Fix:** Replace “37.3~million” with “37.27~million” to match the table sum, or clarify that it is a rounded value with a note.

### PAPER-DEE-min2 (minor)
**Location:** Abstract (cosmological paragraph)  
**Issue:** The abstract uses both “central $7.9\%$ improvement” (referring to the $8.27$ vs. $8.98$ case) and later “central $\sim 9\%$ improvement” (likely from $8.14$ vs. $8.98$) without clear differentiation or labelling; this can cause confusion about which number is being quoted as the central-value forecast.  
**Fix:** Replace the two inconsistent percentages with a single well‑defined statement (e.g., “the central multi‑tracer improvement is $7.9\%$ (linear approximation) and $9.4\%$ (positivity‑respecting form)”), and assign the appropriate qualifier.
