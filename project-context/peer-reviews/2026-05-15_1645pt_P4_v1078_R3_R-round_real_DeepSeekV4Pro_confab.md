# P4_v1078_R3 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-15_1645pt
**Wall time**: 306.8s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=68368, completion=13134, reasoning=12386, total=81502

---

## Findings

### PAPER-DEE-B1
**Section** 4.4 (Monopole+Mask Leakage Generative Null), Table II and abstract  
**Classification** BLOCKER  
**Issue**  
The null‑standard‑deviation column in Table II shows `(1.685 ± 0.068)×10⁻²` (i.e. 6.8×10⁻⁴). Dividing the observed‑null difference `(1.696−1.685)×10⁻² = 1.1×10⁻⁴` by `6.8×10⁻⁴` gives a z‑score of +0.16, not the quoted `+1.69`. Moreover the abstract states the null mean as `1.68×10⁻² ± 0.07×10⁻³` (mean 1.68e‑2, std 7e‑5) while the body text gives `1.685×10⁻² ± 6.8×10⁻⁵` (std 6.8e‑5, mean 1.685e‑2). No single set of displayed figures reproduces the headline +1.69 σ.  
**Fix** Correct the Table II std to `0.0068×10⁻²` (i.e. 6.8×10⁻⁵) and provide the observed value, null mean and null std with sufficient precision (at least four significant digits) so that the z‑score computed from the table equals `+1.69`. Unify the abstract, text and table to the same baseline values.

### PAPER-DEE-M1
**Section** Abstract and §4.9 (Sensitivity floor)  
**Classification** minor  
**Issue**  
The paper claims a 50%-recovery‑at‑3σ injection threshold at `A = 0.75%` based on a nine‑amplitude sweep up to 2%. However, the only injection‑recovery table (Table VI) stops at `A = 0.5%`. The reader cannot verify the critical 0.75% threshold from the displayed data.  
**Fix** Extend Table VI (or add a supplementary table) to include at least the `A = 0.75%` and `1.00%` rows, together with the corresponding `⟨σ⟩`, `P(σ>2)`, `P(σ>3)` and direction‑recovery probabilities.

### PAPER-DEE-M2
**Section** Abstract and §4.4 text  
**Classification** minor  
**Issue**  
The abstract states that the monopole‑only null reproduces “99.3%” of the observed pre‑MASTER pseudo‑C₁ power. Using the paper’s own displayed values (null mean 1.685×10⁻², observed 1.696×10⁻²) the ratio is 0.9935 → 99.35%, which rounds to 99.4% under standard rounding conventions. The abstract also rounds the null mean to 1.68×10⁻², introducing a second unnecessary inconsistency.  
**Fix** Round the fraction to 99.4% (or present it as 99.35% if precision is desired) and ensure the abstract’s numerical values match those in the body.
