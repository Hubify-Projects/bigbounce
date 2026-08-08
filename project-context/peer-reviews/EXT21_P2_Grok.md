# EXT21 P2 Grok — chat: https://grok.com/c/63ac169a-cb07-494b-8b44-905f6a40b1b8

Referee Report – MNRAS / Phys. Rev. D / JCAP
Paper: Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook
Author: Houston Golden
Date of report: 26 June 2026
Recommendation: MINOR REVISIONS

Summary

This is a technically detailed sensitivity recast of published SPHEREx (Heinrich et al. 2024) and illustrative MegaMapper forecasts for the matter-bounce local non-Gaussianity prediction fNL = −35/8. The paper adds substantial value through: (i) an explicit in-in operator-algebra audit that resolves the Cai/Li factor-of-two discrepancy in favour of the physical full-commutator value; (ii) multi-method quantification of the bounce-vs-local template mismatch (r = 0.84±0.02 noise-weighted, with shape-cosine stability); (iii) a consolidated, transparently heuristic systematic budget (Table IV) that degrades the optimistic 5.2–5.5σ template-corrected significance to a realistic 2.6–5σ post-budget range; and (iv) a closed-form Bayesian model comparison (validated by three independent 10^5-realization ensembles) that yields BF ≈ 9–14 (noise-weighted bookkeeping) against tuned multifield competitors under recommended priors. All key claims are appropriately scoped ("recast", "illustrative", "heuristic", "conditional on assumptions (a)–(f)"), code and intermediate artefacts are committed, and the weakest link (assumption (d) on cubic-order bounce transmission) is honestly flagged.

No load-bearing claim lacks support or critical control. The work is reproducible from the committed repository. Minor revisions are requested only for maximal methodological transparency and reader clarity; no new science or recomputation is required.

BLOCKERS
None.

MAJORS
None. (The additive-quadrature combination of systematics is already explicitly labelled a "transparent scoping choice" whose conservatism requires confirmation by a full joint Fisher; this is appropriate scoping rather than an unsupported claim.)

MINORS

Abstract / Sec. IV (recast vs. independent forecast). Explicitly state in the abstract and the opening of Sec. IV that this is a sensitivity recast of the published Heinrich et al. multi-tracer bispectrum Fisher matrices (not a new independent derivation of the survey covariance or window functions). The post-hoc r-degradation factor on σ(fNL) should be described as an amplitude-recovery correction applied to an existing local-template forecast rather than a full shape-matched re-Fisher. (This is already implicit in the text but should be front-loaded for clarity.)

Sec. VII / Table IV (heuristic quadrature). Strengthen the caveat on additive quadrature. While the paper already notes that correlations between nuisances (especially bϕ and GR projection) could tighten or loosen the combined budget, make this statement more prominent in the abstract's "realistic ∼2.6–5σ" sentence and in the Table IV caption. A one-sentence recommendation that a full multi-parameter joint Fisher would be the logical next step would suffice.

Sec. IX.D (joint (fNL, nfNL) SDB analysis). Explicitly label this subsection as a subordinate cross-check on running (not a competing headline forecast). Clearly distinguish the two distinct Fisher matrices in play: (i) the Heinrich et al. multi-tracer bispectrum matrix (σ(fNL) ≈ 0.7) that drives the abstract numbers, and (ii) the separate six-bin SDB matrix used only for the running diagnostic (σ_unmarg(fNL) = 1.53). The different redshift/tracer selections and sufficient statistics should be stated once in a short "channel hierarchy" paragraph to prevent any reader conflating the two σ(fNL) values.

Minor presentation / notation.
- Ensure consistent notation for the local-template quantity (f_local NL vs. plain fNL) throughout; a handful of passages still mix the two.
- Fig. 2 caption: define the exact optimistic-to-conservative span of each bar (template-overlap endpoints, GR/bϕ budget, etc.) in one additional sentence.
- A few equation cross-references in Secs. VI–VII could be tightened (e.g., explicit pointer to Eq. (5) when the r-rebooking is first applied to the Bayes factor).

Data/Code Availability (submission checklist). At submission, confirm that every artefact listed in the Data Availability statement (null-space JSONs, Fisher overlap outputs, continuous-marginalization scripts, etc.) is present in the public GitHub tree / Zenodo deposit and that the main reproducibility notebook runs cleanly with pinned dependencies. This is already excellent practice; a final verification note in the cover letter would be appreciated.

These are all straightforward clarifications that can be addressed in a revised manuscript without new calculations.

Strengths (selected)

- In-in operator-algebra audit (Appendix A). The explicit derivation of the −2 Im commutator identity that fixes the physical bispectrum at −35/8 (rather than the single-time-ordering intermediate) is a genuine service to the literature and cleanly closes a long-standing convention ambiguity between Cai et al. and Li et al.

- Template-overlap quantification. The combination of analytic Fisher overlap, 200-realization flat-sky injection-recovery, and a 10 000-sample null-space Monte Carlo over the underdetermined polynomial coefficients (with shape-cosine stability rcos > 0.97) is technically rigorous and unusually thorough for a forecast paper. The released artefacts make every step reproducible.

- Transparent, conservative systematic budget. Table IV and the surrounding text provide a clear, auditable consolidation of every identified systematic (template mismatch, ε-correction, null-space scatter, bϕ marginalization, GR projection, photo-z). The additive-quadrature rule is labelled as heuristic and the resulting 2.6–5σ realistic envelope is presented with appropriate caution.

- Bayesian model comparison. The closed-form expression (Eqs. 8–9), four-corner prior grid, continuous hyperprior marginalization, and three independent 3×10^5-realization validation ensembles together constitute a high-standard treatment of prior sensitivity. The BF ≈ 9–14 (noise-weighted) result is correctly caveated as "illustrative of discriminating power given current theoretical uncertainty."

- Honest scoping and channel hierarchy. Assumptions (a)–(f) are listed explicitly; assumption (d) is correctly identified as the weakest link. The gauge-frame observable is cleanly separated from the conformal-Fermi theoretical discriminator. The staged SPHEREx → MegaMapper strategy and decision-threshold diagram (Fig. 6) give the community concrete, falsifiable guidance.

- Reproducibility commitment. Full release of analysis code, intermediate JSON artefacts, and recompute scripts is exemplary for a forecast paper.

Overall Assessment

This is a high-quality, self-contained forecast/recast paper that materially advances the observational testability of the matter-bounce scenario. The scientific content is sound, the added technical work (overlap audit, Bayes factor, systematics scoping) is substantial, and the limitations are transparently communicated. With the minor clarifications above, the manuscript will be ready for publication in MNRAS, Phys. Rev. D, or JCAP. I recommend MINOR REVISIONS.
