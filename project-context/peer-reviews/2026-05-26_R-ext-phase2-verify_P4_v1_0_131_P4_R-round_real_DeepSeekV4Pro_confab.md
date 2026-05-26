# P4 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-phase2-verify_P4_v1_0_131
**Wall time**: 169.4s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=95027, completion=7891, reasoning=6893, total=102918

---

## Adversarial Peer Review — v1.0.131 (MNRAS/PRD/JCAP‑grade)

### FINDING PAPER‑DEE‑B1 (MAJOR)
**Section:** Conclusions, paragraph “Sensitivity convention and remaining caveats” (near “P(σ > 3) = 0.50 at A = 0.75%”).

**Issue:** The Conclusions state that the 50%‑recovery‑at‑3σ threshold corresponds to `P(σ > 3) = 0.50` at amplitude `A = 0.75%`. The paper’s own injection‑recovery table (Table XI / `mc_injection`) gives `P(σ > 3) = 0.55` for that same amplitude. The abstract and the table caption correctly use 0.55, but the Conclusions text contradicts them.

**Fix:** Replace `0.50` with `0.55` in the Conclusions; if the intent is to quote an interpolated 50%‑recovery point, state the interpolated amplitude (≈0.71%) explicitly and cross‑reference the table.

---

### FINDING PAPER‑DEE‑B2 (MAJOR)
**Section:** Conclusions, paragraph “Headline finding: a quantifiable monopole‑mask leakage channel” (the post‑MASTER monopole‑only null numbers).

**Issue:** The Conclusions still quote the `N = 500` run for the post‑MASTER monopole‑only null (`null mean 8.0 × 10⁻⁷`, `moment‑z = +4.84`, `p = 0.006`). The authors state (Round Context, v1.0.131 closure M3) that they have since executed a `N = 10,000` run with updated statistics (`null mean 7.59 × 10⁻⁷`, `std 1.13 × 10⁻⁶`, `moment‑z = +5.14`, `p = 22/10000 = 0.0023`) and that this supersedes the earlier result. The manuscript body was not updated to reflect the new, more precise null, so the Conclusions present an outdated measurement.

**Fix:** Replace the 500‑run figures in the Conclusions with the 10 000‑run values, and add a brief stability remark (e.g., “the null mean and std are stable to ≈5% between the two sample sizes”).

---

### FINDING PAPER‑DEE‑B3 (minor)
**Section:** Abstract and §4.8 (“Sky Region Balance”); the claim “uniform across 7 equatorial coordinate slabs”.

**Issue:** The per‑region CW‑fraction values in Table `sky_balance` are not backed by a companion JSON artifact; the paper itself notes “a dedicated per‑region JSON is queued for the next post‑submission revision”. While the global statistic is provenanced, the regional uniformity statement currently lacks a traceable on‑disk source.

**Fix:** Generate the missing per‑region artifact (a simple JSON with the 7 per‑region counts and fractions) and cite it in the table caption, or explicitly note that the values can be trivially reproduced from the public catalog.

---

### FINDING PAPER‑DEE‑B4 (minor)
**Section:** Abstract, “+0.43σ (p = 0.30, ∼0.6% residual amplitude)”.

**Issue:** The “∼0.6%” residual amplitude describes the fitted real‑space dipole amplitude, but the precise dipole amplitude `|A|` (in percent) is not tabulated anywhere in the manuscript. The reader cannot directly verify the 0.6% figure against any displayed value or companion JSON without performing their own Healpix fit.

**Fix:** In the abstract or in §4.4, state the exact best‑fit dipole amplitude (e.g., `|A| = 0.58%`) alongside the σ and p‑value, or cite the row in `dipole/summary.json` that contains it.

---

### FINAL NOTE
No BLOCKER‑grade issues were found that would undermine the headline null‑dipole result. The two MAJOR findings are factual inconsistencies that can be corrected without re‑analysis. The two minor findings concern traceability of supporting numbers; fixing them will bring the paper to full MNRAS/PRD reproducibility standards.
