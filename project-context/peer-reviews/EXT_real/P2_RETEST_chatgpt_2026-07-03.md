# P2 v1.7.86 EXT RETEST — ChatGPT (Pro Extended) — 2026-07-03

- reviewer: chatgpt
- model: ChatGPT Pro Extended (thinking)
- account: BAMF DEV Personal (ChatGPT Pro, visible gstack browser)
- chat_url: https://chatgpt.com/c/6a48ad60-6c60-83e8-9d40-f75c2383e37b
- verdict (from '(1) VERDICT:' line, verbatim): REJECT
- captured: 2026-07-03

## RAW RESPONSE (verbatim)

(1) VERDICT: REJECT

(2) ISSUES:

[MAJOR] Abstract/Scope and Sec. IV — the headline “2.6–5.5σ SPHEREx test” is not an internally derived forecast but a scalar recast of Heinrich et al.’s local-template σ(fNL)=0.7, with no bounce-template multi-tracer bispectrum Fisher matrix, no survey-window covariance, and no joint nuisance marginalization; the manuscript itself admits this, so the headline precision is not established as a PRD-level result. 

ext_retest_P2

 Heinrich et al. is indeed a local-template SPHEREx bispectrum forecast, not a bounce-bispectrum forecast. 
arXiv

[MAJOR] Secs. II C, IX E, and X — the central theoretical premise, faithful cubic-order bispectrum transmission through the nonsingular bounce, is not calculated; the manuscript states that only linear transfer is verified and that cubic transfer is supported only by an order-of-magnitude superhorizon scaling estimate, which is insufficient for a claimed prediction of fNL = −35/8.

[MAJOR] Sec. II C and Appendix A — the manuscript acknowledges an unresolved factor-of-two discrepancy between Cai et al. fNL = −35/8 and Li et al. fNL = −35/16 in the same normalization and squeezed limit, yet adopts the larger value for the headline; because the alternative branch halves every significance and removes the ≥5σ claim, the central forecast is conditional on an unresolved literature ambiguity rather than a settled benchmark.

[MAJOR] Sec. II A and Sec. III B — the bounce-shape polynomial used for the template-overlap factor is underdetermined by construction: six symmetrized coefficients are constrained by only three benchmark configurations, and the null-space sampling measure is explicitly basis-dependent; using this construction to quote r = 0.84 ± 0.02 as a quantitative survey degradation is not justified.

[MAJOR] Sec. III B — the 200-realization injection/recovery validation uses a two-dimensional flat-sky, CMB-style KSW estimator with isotropic Gaussian noise and no Galactic mask, while the claimed observable is a three-dimensional SPHEREx galaxy bispectrum with photometric-redshift errors, selection functions, shot noise, redshift-space effects, bias nuisance parameters, and survey-window mode coupling; this does not validate the LSS estimator or the quoted σ(fNL).

[MAJOR] Sec. VII and Table IV — the systematic budget is an additive-in-quadrature heuristic that mixes numerator degradations, denominator widenings, baseline replacements, distributional null-space floors, GR projection effects, and bϕ priors as if they were independent Gaussian nuisance terms; the resulting 2.6σ lower endpoint is therefore not a statistically defined marginalized constraint or conservative bound.

[MAJOR] Sec. IV and Eq. (7) — the argument that the Heinrich local-template covariance can be used at the bounce fiducial relies on a heuristic primordial-field scaling δC/C ∼ fNL²Δζ²/Nmodes, but the relevant covariance is the galaxy bispectrum covariance including bias operators, shot noise, redshift errors, tracer covariance, and non-local shape tails; the claimed sub-percent fiducial-shift effect is not derived.

[MAJOR] Sec. VI and Tables II–III — the Bayes factors are prior-engineered illustrative quantities, not robust model-selection evidence: they assume a mock detection exactly at the adopted Cai value, compare against broad or narrow hand-chosen competitor intervals, mix delta and Gaussian bounce priors, and use r→1 table entries while the abstract applies r≈0.84 “rebooking”; the resulting BF≈9–14 should not be presented as evidential support for the physical model.

[MAJOR] Sec. IX D — the only independent Fisher calculation reported in the manuscript, the scale-dependent-bias joint (fNL,nfNL) analysis, gives σ(fNL)=3.08–7.06 after running/bias marginalization and only a 0.6–1.4σ detection of fNL=−4.375; this undercuts rather than supports the headline and is not reconciled by a joint bispectrum-plus-SDB covariance.

[MAJOR] Sec. V — the MegaMapper “3–7σ” outlook is not a calibrated forecast: the instrument is not finalized, the SPHEREx systematic budget is ported to a higher-redshift survey despite acknowledged larger relativistic-projection sensitivity, and no MegaMapper bounce-template Fisher calculation is performed.

[MAJOR] Data and Code Availability — many load-bearing numerical claims depend on named JSON artifacts and scripts not included in the manuscript and on a Zenodo DOI “inserted at submission”; the paper is not self-contained enough for refereeing of the template overlap, null-space scan, Bayes-factor recomputations, or SDB Fisher.

[MINOR] Secs. I, VI, and X — the gauge-frame versus conformal-Fermi-frame discussion is overextended: the manuscript correctly notes that survey estimators measure the gauge-frame local-template quantity, but it continues to use physical-frame consistency-relation language as a discriminator without propagating the corresponding projection/gauge corrections into the observable forecast.

[MINOR] Sec. IV — the anomaly-selected tracer discussion and claimed 10–20% improvement are speculative, not supported by a displayed Fisher matrix, and partly contradicted by the manuscript’s own shot-noise caveat for sparse anomaly subsamples.

[MINOR] Sec. IX C — the cosmic-birefringence paragraph is tangential, model-dependent, and not connected quantitatively to the matter-bounce fNL forecast; it should be removed from a focused PRD submission unless a concrete ALP-bounce model and likelihood are supplied.

(3) The central claim is not supported by the evidence presented, because both the theoretical input fNL = −35/8 and the observational significance assigned to it rely on unresolved or uncomputed steps rather than on a self-consistent bounce-template forecast.
