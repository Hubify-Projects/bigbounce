# paper1b R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-21_R23_P1B_v1B_0_20
**Wall time**: 201.7s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=18514, completion=7086, reasoning=6618, total=25600

---

## PAPER-DEE-B1 (MAJOR)
**Section:** Conclusions, the NaMaster bias statement.
**Line:** The conclusion says *“the deconvolution pipeline recovers injected birefringence angles with bias ≤0.032°”*.
**Issue:** The paper’s own Data Methods section documents an amplitude‑dependent bias: 0.032° for injection 0.27° but **0.040° for injection 0.342°** (the published Planck+ACT value), and explicitly adopts *“the 0.04° level in the worst‑case injection”* as the systematic floor. The conclusion’s “≤0.032°” contradicts the body’s measurement and in‑practice worst‑case, misrepresenting the pipeline bias.
**Fix:** Change the conclusion to *“bias ≤0.04° (worst‑case)”* or *“bias 0.032°–0.040°”*, and cite the injection‑dependent bias table.

## PAPER-DEE-B2 (minor)
**Section:** Section 6 (Cosmic Birefringence: Spectator ALP Consistency Check).
**Lines:** *“Numerical integration … yields the field displacement from recombination to today: Δϕ/fa ≈ 0.65 (m = H0, θi = 1).”* and the resulting range [0.2, 1.1].
**Issue:** The scalar 0.65 and the full range [0.2, 1.1] are load‑bearing for the subsequent β ≈ 0.29° and the derived β‑range (0.17–0.43°), but the paper provides **no script, repository path, or detailed integration setup** that produced them. The reproducibility materials only cover MCMC chains and NaMaster, so these numbers are not verifiable from the described disk artefacts.
**Fix:** Add the ALP equation‑of‑motion integration script to the reproducibility repository and include a reference (e.g., `pipelines/alp_eom_integration.py`) in the text, or at least state the integration method, step size, and initial conditions in a footnote so the arithmetic can be reproduced independently.
