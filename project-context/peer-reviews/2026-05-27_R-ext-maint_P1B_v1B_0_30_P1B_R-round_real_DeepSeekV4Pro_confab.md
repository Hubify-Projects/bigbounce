# P1B R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-27_R-ext-maint_P1B_v1B_0_30
**Wall time**: 415.5s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=23394, completion=13000, reasoning=12308, total=36394

---

# Adversarial Peer Review — Paper 1B (MCMC companion)

**Scope:** Numbers in abstract and conclusions must have traceable on‑disk provenance. Headline figures without a JSON/script/dataset that directly produces the value are flagged.

---

## PAPER‑DEE‑B1 (minor) SNR values 20.32 and 25.71 not verifiable from displayed numbers
- **Section:** VI (NaMaster pipeline validation), body text
- **Issue:** The pipeline‑recovery SNR values `20.32` (for injection β=0.27°) and `25.71` (for β=0.342°) are stated without the underlying uncertainty σ(β̂). The reader cannot reproduce the SNR from the paper: e.g., 0.238° / 20.32 requires σ≈0.0117°, but that σ is never reported. No explicit script output file or formula is provided.
- **Fix:** Report the recovered mean and its standard error from the 500‑MC ensemble (e.g., β̂ = 0.238° ± 0.012°) and define SNR = β̂/σ(β̂). Or point to a specific output file in `pipelines/h200_results/…` that contains the SNR.

---

## PAPER‑DEE‑B2 (minor) Planck‑only sample count 114,992 has no on‑disk pointer
- **Section:** Abstract, Table `tab:mcmc_inventory`, Conclusions
- **Issue:** The ongoing Planck‑only chain is quoted with 114,992 samples and ̂R−1∼0.05, but no chain directory, snapshot file, or diagnostic CSV is cited to anchor the number. The frozen chains are clearly traced; this one is not.
- **Fix:** Add a footnote or parenthetical stating the path to the chain directory or the specific convergence‑diagnostic file that gave the 114,992 count (e.g., `reproducibility/cosmology/planck_only_YYYYMMDD/`).

---

## PAPER‑DEE‑B3 (nit) Abstract’s sample‑count arithmetic depends on table values but no direct verification artefact
- **Section:** Abstract (309,189 frozen samples)
- **Issue:** The sum 176,240 + 132,949 is reconstructible from Tables I and `tab:mcmc_inventory`, and the stratification footnote explains burn‑in arithmetic. However, a paranoid reader who wants to confirm the raw counts without re‑running the chains would need a line‑count script or a pre‑computed totals CSV; the paper does not name such an artefact.
- **Fix:** Optionally note that the raw chain sample counts can be obtained via `wc -l` on the chain files in `reproducibility/cosmology/frozen/` or include a `sample_counts.json`.

---

**No BLOCKER or MAJOR provenance issues were found in the abstract or conclusions.** All load‑bearing scalars (ΔN_eff, H₀, bias values, iter2 w₀/wa/physical) are either directly displayed in tables linked to regenerable chains or derived from simple arithmetic on displayed constants. The two minor findings concern missing provenance for secondary pipeline‑quality metrics and the ongoing Planck‑only chain.
