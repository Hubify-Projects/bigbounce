# P5 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-v2_P5_v0_1_31
**Wall time**: 198.6s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=24883, completion=9565, reasoning=8778, total=34448

---

# Adversarial Peer Review: P5 v0.1.31 — provenance and reproducibility of load‑bearing scalars

## PAPER-DEE-B1 — MAJOR
**Location:** Abstract (line with “filament‑class concordance $0.026$\,pp”) and §VII.E (Tempel cross‑validation, item “filament\_like\_vs\_filament: 0.026\,pp”).  
**Issue:** The claimed concordance $0.026$ percentage points between V‑Web filament and Tempel filament‑like CW fractions cannot be reproduced from the displayed table values. Table II gives V‑Web filament $f_{\rm CW}=0.4980$, Table III gives Tempel filament‑like $f_{\rm CW}=0.4982$; the absolute difference is $0.0002 = 0.02$ pp, not $0.026$ pp. If the number was derived from the V‑Web filament fraction on the $110{,}586$-spiral overlap subsample, that fraction is not reported and the comparison is untraceable.  
**Fix:** Either (a) provide the exact V‑Web filament $f_{\rm CW}$ computed on the Tempel‑overlap subsample and verify the difference, or (b) correct the number to the difference of the displayed table values, clarifying what is compared. The figure’s side‑by‑side bars must match the quantitative concordance claim.

## PAPER-DEE-M2 — MAJOR
**Location:** Abstract (final sentences on tracer‑program decomposition: “cluster class joint $|z|\approx 0.5\sigma$ … $n_{\rm dark}^{\rm cluster}=4{,}234$”).  
**Issue:** The dark‑program cluster subsample size $n=4{,}234$ and the derived joint $z\approx 0.5\sigma$ appear only in the abstract. No body section or artifact (e.g. a cluster‑class tracer‑decomposition JSON) reports this number, making it an untraceable headline scalar.  
**Fix:** Add a brief paragraph or table in §VII or an artifact (e.g. `cluster_tracer_decomposition.json`) that gives the per‑program CW fractions and σ for the cluster class, and reference it in the abstract.

## PAPER-DEE-m3 — minor
**Location:** Section VI.A (discussion of $\sigma_{\rm pred}$ for filament).  
**Issue:** The text claims $\sigma_{\rm pred}({\rm filament})\approx-3.16$ from $\Delta f_{\rm CW}=-0.0026$, but $2\cdot0.0026\cdot\sqrt{408{,}187}\approx 3.32$. The number $-3.16$ is not reproducible with the given parameters; the error is ~5 % but still a factual mis‑computation.  
**Fix:** Correct to $-3.3$ (or show the actual arithmetic with the exact monopole used), or state explicitly that the prediction is “order‑unity” without quoting a specific value.

## PAPER-DEE-m4 — minor
**Location:** Abstract (“statistical‑dominated for V‑Web void at $n = 428$, ${\sim}2\sigma$ on the binomial null”).  
**Issue:** The measured $\sigma_{\rm from\,half}$ for the void class is $-0.68$ (Table II), far below $2\sigma$. Calling this “${\sim}2\sigma$” is a misrepresentation of the actual statistical significance.  
**Fix:** Replace “${\sim}2\sigma$” with the correct value “$-0.68\sigma$” or describe the constraint as “within $1\sigma$ of parity”.
