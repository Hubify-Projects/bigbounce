# P2 — ChatGPT (Pro Extended) — FINAL ROUND
- paper: P2 (f_NL forecast)
- version: v1.7.95
- model: ChatGPT Pro Extended (chatgpt.com)
- timestamp: 2026-07-07T03:16:56Z
- chat_url: https://chatgpt.com/c/6a4c6db5-9058-83e8-a9b4-ac1833110b82

## RAW VERBATIM RESPONSE

(1) VERDICT: REJECT

(2) ISSUES:

[MAJOR] Abstract/Secs. III–IV/Table IV — the headline SPHEREx significance is not a forecast. The manuscript rescales a single external local-template result, σ(fNL)=0.7, by a scalar overlap r and then adds heuristic systematics; it does not compute the SPHEREx multi-tracer redshift-space bispectrum Fisher matrix for the bounce template, its nuisance parameters, or its covariance. Heinrich et al. forecast σfNL=0.7 for the local template and note σfNL=0.5 only after adding the power spectrum, but this manuscript’s bounce sensitivity requires the full cross-Fisher/covariance, not a post-hoc scalar degradation. 
arXiv
 

final_P2

[MAJOR] Sec. II C/Conclusion — the “faithful cubic-order transmission through the bounce” claim is not demonstrated. The manuscript upgrades a linear LQC result and a separate-universe argument into a claimed ≤10⁻³ cubic bispectrum bound, but no third-order dressed-metric or deformed-algebra action, matching calculation, numerical mode evolution, or in-in calculation through the bounce is provided. This is the load-bearing assumption for applying the contracting-phase fNL to late-time observables, and it remains an assumption, not a result.

[MAJOR] Sec. II C/Sec. IX E — the ζ-conservation argument conflicts with the mechanism used to generate the matter-bounce bispectrum. The original matter-bounce non-Gaussianity calculation explicitly relies on ζ growing on super-Hubble scales in contraction and notes that perturbations are not conserved outside the Hubble radius, while the manuscript’s bounce-transfer closure assumes single-clock superhorizon conservation of ζ at nonlinear order. This tension is not resolved by degree-of-freedom counting. 
arXiv
+1

[MAJOR] Secs. II C/II D/VI and model definition — the paper combines incompatible ingredients into one “Wilson-Ewing/LQC” benchmark. It uses the cs=1 amplitude −35/16, invokes low sound speed and LQC effects to evade tensor/no-go constraints, and treats the scalar sector as standard GR/canonical during contraction; Li et al. show that in generalized single-field matter-bounce models fNL depends strongly on cs, with fNLlocal=−165/16+65/(8cs²), so the paper must specify one consistent action and perturbation theory rather than mix the cs=1 bispectrum with low-cs phenomenology. 
arXiv

[MAJOR] Appendix A — the claimed resolution of the Cai–Li factor of two is not sufficiently established for publication. Cai et al. explicitly quote −35/8, while Li et al. give −35/16 at cs=1; the manuscript asserts an arithmetic error in Cai’s final polynomial but also admits that the identified +(99/128)∑ki³ term by itself has the wrong sign/magnitude to explain the doubling. That is not a complete algebraic proof of the correction, and the paper cannot claim to have “settled” the discrepancy without a fully transparent term-by-term derivation in the manuscript. 
arXiv
+1

[MAJOR] Sec. II/Sec. III B — the template-overlap factor r is not robustly defined. The manuscript first says the physical shape is known, then introduces a three-dimensional null space from its own symmetrized monomial representation and samples arbitrary coefficients with an arbitrary Euclidean radius; if the vertex-derived shape is known, this null space is artificial, and if it is not known, the forecast is underdetermined. The r=0.84 degradation therefore lacks a well-defined physical or Fisher-covariance meaning.

[MAJOR] Sec. VII/Table IV — the systematic budget is not a valid marginalized likelihood. Adding bϕ, GR projection, photo-z, template mismatch, ε-corrections, and null-space scatter in quadrature ignores correlations among exactly the parameters most degenerate with local PNG. The later use of an SDB-derived ρ=−0.868 as a proxy for the bispectrum GR covariance is not justified; the manuscript itself says the channel-native covariance is missing. The quoted 1.3–2.75σ range is therefore not a defensible “realistic” sensitivity interval.

[MAJOR] Sec. VI/Tables II–III — the Bayesian comparison is prior-dominated and does not constitute model-selection evidence. The Bayes factors are computed from assumed top-hat competitor priors and point/Gaussian bounce priors rather than from predictive distributions of specified inflationary and bounce models. The comparison to standard single-field slow roll as a point hypothesis near zero gives large Bayes factors by construction and is not a meaningful model comparison at PRD standard.

[MAJOR] Sec. IX D — the separately computed SDB Fisher result weakens rather than supports the headline. After marginalizing over nfNL and biases, the manuscript reports only 0.31–0.71σ sensitivity to the corrected matter-bounce amplitude in the SDB channel, yet it transfers SDB degeneracy information into the bispectrum systematic discussion. This mixes distinct observables, samples, and Fisher matrices without a joint analysis.

[MAJOR] Figures 1 and 4/Table VI — the central amplitude correction is not consistently propagated through the manuscript. The page-6 plot legend still labels the squeezed/equilateral/folded values as −35/8, −255/64, and −9/4 while the caption claims the corrected half-amplitudes; the page-20 right panel is titled “Significance for fNL=−35/8” while the caption says it is for −35/16. These are not cosmetic errors because the claimed novelty is precisely the factor-of-two correction.

[MAJOR] Data and Code Availability — essential numerical claims are external to the manuscript and not presently reproducible from the PDF. The overlap scans, null-space propagation, Bayes-factor recomputations, GR proxy analysis, and SDB Fisher matrices are repeatedly invoked by filename, while the Zenodo DOI is still a placeholder. PRD refereeing cannot rely on unarchived code artifacts for central numerical claims.

[MINOR] Abstract/Introduction — the manuscript is structurally unsuitable in its current form. The “Scope” paragraph is effectively a referee-response document embedded in the abstract, and the paper repeatedly restates caveats, rebuttals, and bookkeeping conventions rather than presenting a clean derivation and result.

[MINOR] Secs. IV/VII/IX — ancillary claims about anomaly-selected tracers, cosmic birefringence, DESI/SDSS anomaly samples, and ALP spectator sectors are speculative and not part of the calculation. They should be removed unless supported by a quantitative forecast with defined samples, covariances, and priors.

[MINOR] Notation and terminology — the manuscript uses r for template overlap, rt for tensor-to-scalar ratio, σeff for multiple inequivalent quantities, “realistic,” “conservative,” “post-budget,” and “headline” with shifting definitions. This makes the numerical results difficult to audit and should be standardized.

(3) The central claim is not supported by the evidence presented: the paper shows at most a speculative sensitivity recast contingent on uncomputed cubic bounce transmission, an unvalidated scalar template projection, and heuristic systematics, not a publishable PRD-level test of the matter bounce.
