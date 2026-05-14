# P2_v1729_R2 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-15_0230pt
**Wall time**: 312.8s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=29522, completion=11198, reasoning=9685, total=40720

---

# Adversarial Peer Review — P2 v1.7.29 (DeepSeek-V4-Pro, confabulation‑hunter)

## PAPER-DEE-B1 (MAJOR) — Template‑mismatch range provenance is incomplete and miscounted
**Location:** Abstract (r ∈ [0.829, 0.876], 84% ± 2%) and Sec. 3.2 (Template Projection).  
**Issue:** The paper states that the amplitude recovery factor *r* was computed under “10 physically motivated weighting schemes” and reports a central value 0.84 ± 0.02 with a range [0.829, 0.876]. However, the body lists only **four** numbers: “the four noise‑weighted values {0.829, 0.830, 0.835}” (three values, not four) and the signal‑only CMB‑Fisher value 0.876. The remaining six weighting schemes are neither named nor tabulated. A reader cannot verify that the claimed range indeed spans all physically motivated schemes, nor can they reproduce the ±0.02 uncertainty from the three‑plus‑one numbers alone. The abstract’s “84% ± 2%” and the precise range are load‑bearing for the detection significance, yet their provenance is opaque.  
**Fix:** Provide a table of all 10 weighting schemes with their individual *r* values, or reduce the claim to the actually reported schemes and adjust the uncertainty accordingly. If the range is derived from a JSON file (`phase3_fisher_overlap.json`), state explicitly which entries correspond to which scheme and correct the “four noise‑weighted values” miscount.

## PAPER-DEE-B2 (MAJOR) — Headline 3–5σ post‑systematic significance is not produced by a single traceable calculation
**Location:** Abstract (“template‑corrected significance ∼ 3–5σ after the combined systematic budget”) and Sec. 7 (Systematics).  
**Issue:** The paper’s primary forecast is a 3–5σ detection significance after all systematics. This number is assembled by hand from separate, non‑unified estimates: a 20–50% degradation from *b_φ* marginalisation (giving ∼4.0–4.5σ or ∼3.5–3.7σ), an additional 10–30% from other effects (photo‑z, lensing, integral constraint), and GR marginalisation. No single script, Fisher matrix, or combined error budget table is presented that outputs the 3–5σ range. The abstract presents it as a result of “the combined systematic budget”, but the paper contains no combined budget calculation. The number is therefore a qualitative expert assessment, not a reproducible figure.  
**Fix:** Either (a) construct a unified Fisher matrix that simultaneously marginalises over all listed systematics and report the resulting σ(f_NL) and significance, or (b) downgrade the 3–5σ claim to an explicitly qualitative “expected to remain at ≳3σ” statement and remove the false implication of a single combined analysis.

## PAPER-DEE-B3 (minor) — Injection‑recovery validation is misrepresented as covering the noise‑weighted case
**Location:** Abstract (“validated via … 200 injection‑recovery realizations”) and Sec. 2.1, 3.2.  
**Issue:** The abstract cites the 200‑realization injection‑recovery test (r_meas = 0.90 ± 0.01) as validation of the template mismatch. However, the body clarifies that this test used isotropic Gaussian noise (CMB‑like weighting) and a fixed coefficient set, making it a validation only of the CMB Fisher (signal‑only) overlap (r=0.876), not of the noise‑weighted r≈0.83 that drives the headline 5.2σ and 3–5σ figures. The abstract’s wording implies the injection‑recovery validates the full 84% ± 2% claim, which is misleading.  
**Fix:** In the abstract, qualify the injection‑recovery validation as applying to the CMB‑Fisher weighting case, or add a separate noise‑weighted injection‑recovery test.

## PAPER-DEE-B4 (minor) — Monte‑Carlo realization count inconsistent between abstract and conclusion
**Location:** Abstract (“aggregate 3×10^5 count”) vs. Conclusion (“>6×10^5 Monte Carlo realizations”).  
**Issue:** The abstract states the Bayesian comparison uses three ensembles of 10^5 each (3×10^5 total). The conclusion inflates this to >6×10^5, with a body note that “older slower variants contribute the residual”. The two numbers are contradictory and the provenance of the extra 3×10^5 is not documented. While not a load‑bearing scalar, it erodes trust in the paper’s numerical precision.  
**Fix:** Use a single, consistent realization count throughout, or explicitly break down the total in the conclusion as done in the body.

## PAPER-DEE-B5 (minor) — ℓ‑space Fisher overlap lacks sufficient methodological detail for reproducibility
**Location:** Sec. 3.2 (“ℓ‑space Fisher overlap using fiducial C_ℓ from CAMB with a Planck noise model (r = 0.878 ± 0.012)”).  
**Issue:** The paper reports a validation number from an ℓ‑space Fisher overlap but does not specify the CAMB cosmological parameters, the Planck noise model (which Planck release, frequency channels, noise levels), or the ℓ‑range integration. The code is said to be available, but the paper itself should contain enough information for a reader to understand the calculation without reverse‑engineering the repository.  
**Fix:** Add a sentence listing the CAMB parameter set (e.g., Planck 2018 TT,TE,EE+lowE best‑fit) and the noise model used (e.g., Planck 143 GHz, 4 μK‑arcmin, Gaussian beam).

## PAPER-DEE-B6 (nit) — Heinrich et al. σ(f_NL) ≈ 0.7 used as exact without uncertainty propagation
**Location:** Abstract and throughout.  
**Issue:** The entire detection significance chain rests on σ(f_NL) = 0.7 from Heinrich et al. (2024). The paper treats this as a point value; no uncertainty in the Heinrich forecast itself (e.g., from photo‑z assumptions, bias modelling, or sample variance) is propagated. While this is common in sensitivity recasts, the paper’s own emphasis on systematic budgets makes the omission noteworthy.  
**Fix:** Add a sentence acknowledging that the Heinrich forecast has its own uncertainties and that the 0.7 value is adopted as a fiducial baseline, with a note that a ±0.1 shift would scale the significances linearly.
