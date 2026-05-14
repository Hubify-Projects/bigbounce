# P2_v17_28 R-round — REAL cross-vendor — DeepSeek-V3.2 confabulation-hunter

**Model**: `deepseek/deepseek-v3.2` (via OpenRouter)
**Round**: 2026-05-14_2310pt
**Wall time**: 40.9s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=28946, completion=1180, total=30126

---

## PAPER-DEE-B1
**Classification:** BLOCKER  
**Location:** Abstract, lines 1-4 (physical-frame f_NL_inf=0 narrative)  
**Issue:** The claim "single-field slow-roll inflation predicts f_NL^local → 0 at leading order (consistency relation in the physical frame)" is presented as a load-bearing discriminator (bounce vs. inflation contrast is between -4.375 and exactly zero), but no source JSON/script/dataset is provided that computes this physical-frame value or validates the frame transformation. The cited papers (Pajer:2013, TanakaUrakawa:2011) discuss the consistency relation in different gauges/frames, but the paper does not demonstrate that their results yield f_NL^local = 0 in the "conformal-Fermi physical-observer frame" used here. This scalar is central to the abstract's narrative but lacks traceable provenance.  
**Fix:** Either remove the "exactly zero" claim from the abstract and retain only the gauge-frame ratio (~290), or add a short appendix with explicit computation/transformation from the cited papers to f_NL=0 in the chosen frame, backed by a script in the repository.

## PAPER-DEE-B2
**Classification:** MAJOR  
**Location:** Abstract, lines ~30-35 (9.9σ joint-Fisher figure) and Section 8.3 Discussion  
**Issue:** The 9.9σ joint-Fisher detection significance (σ(n_fNL)=0.086, ρ=0.966) is labeled as an "illustrative idealized-Fisher check," but its derivation is opaque. The paper states the full Fisher-input release (six-bin k_min(z), n(z), b_1, b_ϕ, etc.) is deferred to a companion artifact. Therefore, the 9.9σ figure has no traceable source in the current paper or its repository. It cannot be reproduced from displayed values alone.  
**Fix:** Either remove the 9.9σ figure entirely, or provide the Fisher matrix (or sufficient inputs) in the current repository so the number can be recomputed. Clearly separate it from the bispectrum-only forecast.

## PAPER-DEE-B3
**Classification:** MAJOR  
**Location:** Abstract, lines ~15-17 (r ∈ [0.821,0.879]) and Section 3.2 Template Projection (Eq. r_noise)  
**Issue:** The abstract reports r ∈ [0.821,0.879] for template mismatch, but the body text gives r = 0.84 ± 0.02 with range [0.829,0.876], and a footnote mentions a JSON file gives [0.856,0.895]. These ranges are inconsistent. The provenance of the abstract range is unclear; it appears to be a different aggregation (maybe including Monte Carlo noise) than the body's "physically motivated weighting schemes." This scalar is load-bearing for significance degradation.  
**Fix:** Unify the ranges. Specify which weighting schemes correspond to the abstract interval. Ensure the JSON file (phase3_fisher_overlap.json) is cited and its data matches the quoted range.

## PAPER-DEE-B4
**Classification:** minor  
**Location:** Section 2.4 Assumptions, Hehl-Datta-Mercuri 4f caveat  
**Issue:** The caveat about fermion matter reactivating the Barbero-Immirzi parameter post-bounce is correctly added to close the prior ECH decoupling gap. However, the statement "the matter-bounce f_NL = -35/8 prediction in this work is robust because the contracting-phase mode functions are scalar-dominated" is an assertion without supporting reference or calculation showing that fermion contributions during contraction are negligible.  
**Fix:** Add a brief justification citing relevant literature on fermion density during matter-dominated contraction, or note that this is an assumption (add to list (a)-(e)).

## PAPER-DEE-B5
**Classification:** nit  
**Location:** Bibliography fixes (CaiBrandenberger:2014, Cabass:2022, Heinrich:2023, etc.)  
**Issue:** The bib metadata fixes appear correct (IDs match titles, no fused metadata). However, the Heinrich:2023 citation is updated from JCAP to PRD 109 123511, but in the text (Section 4 SPHEREx Forecast) it is still cited as "Heinrich et al. 2024" (abstract) and "Heinrich et al. 2023" (body). This is a minor inconsistency.  
**Fix:** Ensure all in-text citations use the same year (2023) and match the bib entry.

## PAPER-DEE-B6
**Classification:** MAJOR  
**Location:** Abstract, lines ~40-45 (Bayes factor BF ~6–17 envelope) and Section 6.3 Bayesian Comparison  
**Issue:** The Bayes factor range BF ~6–17 is derived from a "four-corner prior grid" computed analytically. The paper mentions Monte Carlo ensembles (3×10^5 realizations) but says they only cover a subset of the grid; the analytic formula is used for the full grid. However, no script or JSON is provided that computes the analytic Bayes factor for the reported prior combinations. The load-bearing scalars (BF ~8, BF ~17) lack immediate reproducibility.  
**Fix:** Include a script (e.g., bayes_factor_prior_grid.py) that computes the analytic Bayes factors for all four corners and outputs the numbers in the abstract/table. Reference it in the text.
