# P1A R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-maint_P1A_v1A_0_35
**Wall time**: 175.2s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=28535, completion=8160, reasoning=7458, total=36695

---

## PAPER-DDE-M1 (MAJOR)
**Section:** Abstract, §14 (structural tension), §15 (conclusions)  
**Issue:** The load‑bearing scalar `N_tot ≈ 92` appears repeatedly as the e‑fold count required for the dark‑energy ansatz and as the pivot of the structural incompatibility argument. The abstract states this number with only the phrase “requires N_tot ≈ 92 post‑bounce e‑folds,” and the body of the paper provides no self‑contained arithmetic that derives 92 from the displayed equations and numerical inputs (`(α/M) M_Pl ∼ 10⁻²`, `(T_reh/M_GUT)^{3/2} ≈ 0.03`, `ρ_Λ^obs ≈ (2.3 meV)⁴`). Appendix B computes the genuine hierarchy’s `N_tot ≈ 94` but never explicitly maps the ansatz to `92`. No script, Jupyter notebook, or explicit line‑by‑line calculation in the repository produces the number 92.  
**Fix:** In the section where `N_tot` is first introduced, show the algebraic steps that lead from the phenomenological parameters to `N_tot ≈ 92`, or provide a short script/notebook in the reproducibility repository that carries out the matching and prints the resulting `N_tot`.

## PAPER-DDE-m1 (minor)
**Section:** Abstract (Executive Summary Table I), §9 (Table V)  
**Issue:** The abstract’s summary table gives the headline posterior `H₀ = 67.68 ± 1.06` and `ΔN_eff ≈ 0` as evidence that the framework recovers ΛCDM. These values are stated to come from the companion Paper I(b) and are not produced by any dataset, chain file, or script provided alongside this paper. A reader of the present paper alone cannot reproduce or validate these numbers.  
**Fix:** In the abstract and table, add an explicit note that these numbers are entirely taken from the companion’s MCMC chains and are not independently recomputed here, or direct the reader to the specific chain file (e.g., `paper1b/chains/lcdm_plus_DeltaNeff_424781.pt`) if it is publicly available.

## PAPER-DDE-n1 (nit)
**Section:** §7 (Falsification), footnote 1  
**Issue:** The “3–5σ realistic significance” interval for SPHEREx is built by hand‑adjusting the Fisher‑ideal σ(f_NL) ≈ 0.7 with a template‑overlap correction factor r ≈ 0.84 and further degradation from GR‑projection and photo‑z marginalisation. The r ≈ 0.84 factor appears without a reference, a script, or a derivation from the multi‑tracer Fisher matrix, and the subsequent “∼5–5.5σ optimistic” and “3–5σ realistic” ranges are not traceable to any on‑disk computation.  
**Fix:** Supply a script or a short appendix table that computes the corrected σ(f_NL) from the Fisher elements, or at minimum cite a specific intermediate result (e.g., Heinrich et al. 2024, Section 3.4) that yields r ≈ 0.84 and the degraded uncertainties.
