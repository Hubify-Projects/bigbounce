# P1B_v1B014_R9 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1230pt
**Wall time**: 93.9s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=17234, completion=6764, reasoning=6175, total=23998

---

## PAPER-DEE-B1 (minor) — NaMaster SNR undefined and unverifiable from text

**Location:** Abstract, line “SNR=20.32”; Sec. 4, Eq. (1).

**Issue:** The abstract and Sec. 4 report a pipeline-recovery SNR of 20.32 for the β=0.27° injection without defining how SNR is computed (e.g., β̂/σ(β̂) from MC, or some other metric). No formula or output file is cited; the number cannot be reproduced from displayed values alone.

**Fix:** Add a one‑sentence definition (e.g., “SNR ≡ β̂/σ(β̂) over 500 MC realizations”) and reference the specific pipeline output file (e.g., `snr_summary.json`) in the reproducibility directory.

---

## PAPER-DEE-B2 (minor) — Conclusions bias bound contradicts paper’s own results

**Location:** Conclusions, “bias ≤ 0.032°”.

**Issue:** The conclusions state the NaMaster pipeline recovers angles with “bias ≤ 0.032°”. However, Sec. 4 explicitly reports a bias of 0.040° for the β=0.342° injection, making the “≤0.032°” claim false. The paper’s own systematic floor is 0.04°.

**Fix:** Change to “bias ≤ 0.040°” or clarify that the 0.032° refers only to the fiducial injection, not the worst case.

---

## PAPER-DEE-B3 (minor) — Abstract MCMC numbers lack a committed static provenance file

**Location:** Abstract, ΔN_eff and H_0 values; Table 1.

**Issue:** The headline MCMC posteriors (−0.020±0.169, 67.68±1.06, etc.) are not backed by a committed static summary file (e.g., a GetDist `.txt` or `.json`) in the reproducibility repository. The paper provides only a script to regenerate the chains (4–12 h), unlike the iter2 posterior which has `posterior_summary.txt`. Immediate independent verification is therefore blocked without re‑running the full MCMC.

**Fix:** Commit a GetDist posterior summary file for the frozen chains and cite it in Table 1 or the abstract (e.g., `frozen_chains_summary.txt`).

---

## PAPER-DEE-B4 (nit) — “frozen samples” misstates raw vs. post‑burnin count

**Location:** Abstract, “309,789 frozen samples”.

**Issue:** The abstract uses “frozen samples” for the raw sample count (176,840+132,949). The footnote clarifies that post‑burnin the total is 216,852. Calling raw samples “frozen samples” may mislead readers into thinking these are effective or post‑burnin samples.

**Fix:** Change “frozen samples” to “raw samples” in the abstract, or explicitly state “raw accepted samples”.
