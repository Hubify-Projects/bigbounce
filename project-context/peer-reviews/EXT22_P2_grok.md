# EXT22 P2 grok — chat: https://grok.com/c/58d9d4f6-43bd-46e9-92ce-1e755f77590f

Referee report for MNRAS
Paper: Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook
Author: Houston Golden

Recommendation: MINOR REVISIONS

BLOCKERS: None.
The core scientific claims rest on published forecasts (Heinrich et al. 2024), an explicit operator-algebra audit of the Cai et al. bispectrum, a documented null-space analysis of the underdetermined polynomial, and a transparent (if heuristic) systematics budget. All load-bearing results are conditional on the six assumptions of Sec. II C, with (d) — faithful cubic-order transmission through the bounce — correctly identified as the weakest link and supported only by linear-order verification plus a superhorizon scaling estimate. No unsupported central claims exist. Reproducibility is excellent (full code/scripts + named artifacts on GitHub/Zenodo). The work is scoped appropriately as a sensitivity recast rather than an independent end-to-end forecast.

MAJORS: None.
The joint (fNL, nfNL) scale-dependent-bias subsection (IX.D) is explicitly labeled a subordinate cross-check using a distinct Fisher matrix from the headline multi-tracer bispectrum channel; this distinction is clear and avoids confusion. The additive-quadrature systematics combination is repeatedly flagged as a "transparent scoping choice" whose correlations would require a full joint Fisher to confirm; this is intellectually honest scoping, not a flaw requiring rework.

MINORS:

Assumption (d) transmission caveat (Sec. II C and Conclusion). The paper already states that cubic-order faithfulness is verified only at linear order and supported by a superhorizon scaling estimate (δfNL ∼ 10^{-3}). Elevate this to a short, prominent "Verification path" sentence or footnote: a full numerical evaluation of all four Maldacena cubic integrals with bounce-modified mode functions would constitute the definitive upgrade from scaling estimate to derived bound. This is minor polish; the existing scoping is already strong.

Additive-quadrature systematics (Table IV and Sec. VII). The text correctly notes that correlations between systematics (e.g., bϕ and GR projection) could tighten or loosen the combined budget. Add one explicit clause acknowledging that the sign of the covariance and which nuisances are co-marginalized will determine the net effect. This matches the paper's own transparent language elsewhere and requires no new calculation.

Figure captions and standalone readability (Figs. 2, 4, 5). Ensure each caption restates the noise-weighted central r = 0.84 (with range) and the optimistic (5.2–5.5σ) vs. realistic post-budget (2.6–5σ) envelopes. Readers should not need to cross-reference Sec. III B / IV for the headline numbers.

Minor presentational consistency (Bayes section and Table II). Standardize phrasing around "template-mismatch bookkeeping" (currently mixes "rebooked/rebooking" with "r → 1 bookkeeping endpoint"). Minor LaTeX/table spacing and one or two hyphenation points are submission-day items.

References (submission-day). Update any 2025/2026 preprints (e.g., Addis et al., Jung et al. Planck PR4) to final citations if they have appeared; concurrent arXiv placeholders are acceptable per journal norms.

These are all clarifications or polish. No new computations, re-derivations, or re-forecasts are required.

Strengths (selected):

Exemplary template-mismatch quantification. The 10,000-sample null-space scan over the 3-dimensional coefficient freedom (3 benchmark constraints, 6 monomials) demonstrates both shape-cosine stability (rcos > 0.97) and noise-weighted amplitude recovery r = 0.84 ± 0.02 across physically motivated weightings. Validation at three independent levels (ℓ-space Fisher overlap, 200-realization flat-sky MC injection-recovery, literature search) is rigorous and reproducible.

Clean operator-algebra resolution of the Cai/Li factor-of-two. Appendix A supplies an explicit Wick-contraction derivation of the in-in identity i⟨[ζ³, L]⟩ = −2 Im ⟨ζ³ L⟩, cleanly separating the c = 2 Planck/Komatsu-Spergel normalization convention from the missing second time-ordering. Table V stress-tests the single-ordering branch as a non-physical robustness check. This is a genuine service to the literature.

Scrupulous assumption scoping and conditional forecasting. Sec. II C lists the six assumptions (a)–(f) with precision; (d) cubic transmission and (e) no prolonged post-bounce inflation are repeatedly emphasized as scope conditions. The ϵ-correction is bounded (|ΔfNL| ≲ 0.36, inside the recommended σtheory = 1.0 prior) rather than ignored. Forecasts and Bayes factors are caveated at every stage as applying only to the Wilson-Ewing scalar-only class.

Conservative, explicitly heuristic systematics budget. Table IV consolidates template overlap, ϵ-correction, null-space scatter, bϕ marginalization (three scenarios), GR projection (σGR grid), and photo-z degradation. The additive-quadrature rule is labeled a scoping choice whose conservatism requires future joint-Fisher confirmation. The resulting 2.6–5σ realistic envelope is appropriately broad and intellectually honest.

Closed-form Bayesian model comparison with mapped prior sensitivity. The analytic Bayes-factor formula (Eq. 9) is derived, validated on 3 × 10^5 Monte Carlo realizations across three frameworks, and presented with a four-corner grid plus continuous hyperprior marginalization over σtheory. Explicit bookkeeping for the r ≈ 0.84 rescaling is provided. The factors are correctly framed as "illustrative of discriminating power… not definitive model-selection evidence."

Outstanding reproducibility practices. Full GitHub/Zenodo release with named artifacts (null-space JSONs, Fisher overlap outputs, recompute scripts for Tables II–III, continuous marginalization checks). No new observational data; all sensitivities drawn from published works. Monte Carlo convergence and self-consistency diagnostics are documented.

Summary. This is a careful, transparent sensitivity recast that makes a sharp, falsifiable prediction for the imminent SPHEREx data release while maintaining rigorous scoping on theoretical assumptions and observational systematics. It advances the bounce-vs-inflation discrimination discussion without overclaiming. The manuscript requires only minor clarifications and presentational polish; it is suitable for MNRAS (or PRD/JCAP) after these revisions. No substantial scientific rework is needed.
