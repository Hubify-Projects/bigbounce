# P2 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-24_Rnext_P2_v1_7_37
**Wall time**: 151.2s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=33140, completion=6709, reasoning=5696, total=39849

---

## PAPER-GPT-B1 — BLOCKER

- **Section:** Sec. “The Matter-Bounce Bispectrum Benchmark” / Sec. “Template Projection”
- **Issue:** The full bispectrum shape used for the template-overlap factor `r` is reconstructed from only three benchmark configurations, leaving a 3D null space; choosing `(2,7,3,-12,-69,19)` and scanning arbitrary null-space balls does not determine the physical matter-bounce shape. The headline `r=0.84±0.02` and all significance forecasts depend on this unphysical prior over unknown polynomial coefficients.
- **Fix:** Use the full published Cai et al. analytic polynomial with correct symmetrization/normalization, or redo the in-in derivation. If the shape remains ambiguous, remove precise `r` and detection-significance claims.

## PAPER-GPT-B2 — BLOCKER

- **Section:** Appendix A / Abstract / Conclusion
- **Issue:** The paper simultaneously says the Cai vs. Li-Brandenberger difference is a convention and that detection significance is convention-independent, but then holds `σ(f_NL)=0.7` fixed and halves the significance for `f_NL=-35/16`. A pure normalization convention requires rescaling both `f_NL` and `σ(f_NL)`, so the significance cannot halve.
- **Fix:** Decide whether `-35/16` is a physically different single-ordering amplitude or merely a parameter convention. If convention, remove the halved-significance caveat; if physical, stop calling it a convention and justify rejecting it.

## PAPER-GPT-M1 — MAJOR

- **Section:** Abstract; Secs. “SPHEREx Forecast” and “Systematics and Robustness”
- **Issue:** The post-systematic `3–5σ` headline is not derived from a documented joint error propagation. Including the stated null-space scatter `r=0.85±0.13` / range `0.55–1.14` plus `b_φ`, GR, and photo-z degradations can push the lower significance below `3σ`.
- **Fix:** Provide an explicit systematic-budget table/equation with multiplicative or marginalized degradations and correlations. Separate the narrow “physically motivated weighting” `r=0.84±0.02` from the arbitrary polynomial-null-space scatter, or lower the headline.

## PAPER-GPT-M2 — MAJOR

- **Section:** Sec. “Quantitative Bayesian Comparison”; Tables `bayes` and `gr`
- **Issue:** The Bayes factors use a mock detection at `f_NL=-4.375` with `σ=0.7`, but the observable local-template estimator measures `r f_NL` or equivalently a bounce-amplitude uncertainty `σ/r`, and the GR/`b_φ`/photo-z/template nuisances are not consistently marginalized in the evidence. Current BF values are therefore idealized likelihood-ratio numbers, not the advertised post-systematic model evidences.
- **Fix:** Define the data vector and likelihood in one convention, include `r`, ε-corrections, GR, `b_φ`, and survey-performance nuisance priors in the evidence integrals for both models, and relabel current BF values as upper-bound/idealized if retained.

## PAPER-GPT-M3 — MAJOR

- **Section:** Sec. “Joint `(f_NL,n_{f_NL})` Forecast”
- **Issue:** The `9.9σ` joint-Fisher result is numerically quoted despite the Fisher inputs being deferred/not on disk and despite the paper admitting the implied `σ_unmarg(f_NL)=0.114` is `6×` sharper than published SPHEREx forecasts. The same paragraph also says the bispectrum shape-overlap factor `r` does not apply to SDB, then lists `r=0.84` inside the joint systematic budget.
- **Fix:** Remove the `9.9σ`, `σ(n_fNL)=0.086`, `ρ=0.966`, and `σ(f_NL)=0.44` numbers until the Fisher matrix and inputs are released. Do not apply bispectrum template-overlap degradation to an SDB-only Fisher analysis.

## PAPER-GPT-M4 — MAJOR

- **Section:** Data and Code Availability
- **Issue:** The paper is v1.7.37 but the reproducibility link is pinned to `v1.7.26-paper2`, while the manuscript describes multiple later numerical corrections to Bayes factors and significance bookkeeping. The stated code artifact likely cannot reproduce the submitted numbers.
- **Fix:** Archive and cite the exact v1.7.37 code/data tag, with hashes for scripts and generated tables/figures. If older code is intentionally cited, state which results it reproduces and which were recomputed later.
