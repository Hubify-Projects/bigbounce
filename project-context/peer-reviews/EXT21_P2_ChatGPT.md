# EXT21 P2 ChatGPT — chat: https://chatgpt.com/c/6a3e4ea7-d770-83e8-b499-ccc3330aa745

Recommendation: MINOR REVISIONS

This is a careful and unusually transparent sensitivity recast of the matter-bounce local-type non-Gaussianity prediction, focused on the benchmark f_NL^local = -35/8, with SPHEREx as the near-term observational test and MegaMapper as an illustrative longer-term extension. The manuscript is clear that it is not an independent SPHEREx Fisher forecast, but a recast of published sensitivity with template-overlap, theoretical, and observational systematic degradations applied.

I do not find a blocker or a major scientific problem requiring substantial rework. The headline claims are appropriately scoped: the 5.2–5.5σ optimistic SPHEREx estimate is separated from the realistic 2.6–5σ post-systematic range; the MegaMapper forecast is labeled as proposed/design-dependent; the Bayesian factors are explicitly prior-sensitive; and the strongest theoretical assumption, cubic-order bispectrum transmission through the bounce, is stated rather than hidden.

The paper should be accepted after minor revisions, mainly to correct one residual mathematical explanatory phrase and tighten a few places where caveat language could prevent misreadings.

BLOCKERS
None.

MAJORS
None. I do not require a new Fisher matrix, a new SPHEREx mock pipeline, or a full independent re-derivation of the Cai et al. in-in calculation for publication, because the manuscript now consistently presents itself as a sensitivity recast and explicitly identifies those items as future/full-analysis requirements rather than as completed work.

MINORS

Sec. VI.C, p. 13, "Numerical self-consistency check," Gaussian-bounce-prior narrow-competitor bullet.
The explanatory CDF-tail sentence is still mathematically misleading. The text says the narrow-prior correction involves Φ endpoint terms ≈0.006 and an ≈18% correction from each tail. For the delta-prior narrow competitor [-5,+5], f_obs = -35/8, and σ_eff = 0.7, the lower CDF tail is approximately 0.186, not 0.006, while the upper tail is negligible. This is why the exact delta-prior narrow value rises from the large-W approximation (5.69) to approximately 7.0. The Gaussian-bounce-prior value (4.01) is lowered primarily by the prior convolution / predictive-width broadening.
Proposed fix: replace the relevant sentence with: "For the delta-prior narrow competitor, the exact competitor-prior denominator is Φ[(5+35/8)/0.7]-Φ[(-5+35/8)/0.7] ≃ 0.814, so the finite lower tail (≃0.186) raises the exact delta-prior result from the large-W approximation (5.69) to B ≃ 7.0. The Gaussian-bounce-prior narrow value (B=4.01) is lower because the bounce predictive likelihood is broadened by the σ_theory=1.0 prior convolution; Eq. (10) is therefore inapplicable to that row."

Sec. IV / Table IV / Fig. 2, pp. 10–11 and 20.
The significance windows are internally consistent but numerous: naive 6.25σ, template-corrected 5.2–5.5σ, realistic 2.6–5σ, all-combined 2.6–2.8σ, and MegaMapper 3–7σ. Table IV helps, but the reader still has to reconcile several conventions.
Proposed fix: add a short "headline convention" sentence near the start of Sec. IV or immediately before Table IV: "Unless otherwise stated, the SPHEREx headline uses the noise-weighted template overlap (r≃0.84); 5.2–5.5σ denotes template-corrected/no-GR optimistic SPHEREx, 2.6–5σ denotes the post-systematic SPHEREx envelope, and 2.6–2.8σ denotes the most conservative all-combined endpoint."

Sec. IV, p. 10, shot-noise caveat for anomaly-selected tracers.
The anomaly-tracer paragraph gives both a simple Poisson estimate implying √11 ≈ 3.3× inflation and a later statement that the effective bispectrum degradation is only 15–30%. That may be true after squeezed-limit weighting, but it is not shown in the paper.
Proposed fix: either provide a short derivation/artifact reference for the 15–30% effective degradation, or soften the claim to: "The 15–30% figure should be read as an order-of-magnitude expectation for the squeezed-weighted bispectrum estimator, not as a substitute for a shot-noise-corrected anomaly-tracer Fisher matrix."

Sec. VII.B, pp. 16–17, b_ϕ wording.
The current wording says Heinrich et al. "marginalize over b_ϕ" while also saying the universal-mass-function relation fixes b_ϕ per tracer. This could confuse readers, because fixing/tieing b_ϕ via UMF is not the same as independently marginalizing a free b_ϕ per tracer bin.
Proposed fix: replace "marginalize over b_ϕ" with "tie b_ϕ to b_1 through the UMF relation" or "do not independently marginalize b_ϕ per tracer bin."

Sec. IX.C / Fig. 6, p. 22.
The plotted/legend phrase "bounce excluded" is too broad if read outside the caption. The text correctly says a null result disfavors the quasi-dust matter-bounce benchmark conditional on assumptions (a)–(f), not every possible bounce cosmology.
Proposed fix: change the plot/legend label to "quasi-dust benchmark excluded" or "this benchmark disfavored."

Appendix A.2 / Table V, p. 28.
The table column is labeled "Convention," but the appendix correctly argues that the Li row is not an alternative convention; it is a single-time-ordering stress test. The table itself explains this, but the column label partially undermines the point.
Proposed fix: rename the column to "Normalization / time-ordering branch" or "Case."

Data and Code Availability, pp. 24–25.
The code/artifact list is strong, but final acceptance should require the Zenodo DOI and/or immutable commit hash before publication.
Proposed fix: replace "DOI inserted at submission" with the actual DOI or a permanent archived commit reference in the final version.

Strengths

- The paper is admirably explicit about scope. It repeatedly distinguishes a sensitivity recast from an independent survey Fisher forecast, and it separates the optimistic, realistic, and conservative significance ranges.

- The template mismatch between the matter-bounce and local bispectrum shapes is treated quantitatively rather than hand-waved. The use of multiple weightings, injection/recovery tests, and a null-space coefficient scan makes the r ≃ 0.84 degradation credible at the level needed for a recast.

- The systematic budget is transparent. Table IV is especially useful because it shows which effects act on the numerator, denominator, or both, and it gives the cumulative impact on the final SPHEREx significance.

- The theoretical caveats are not buried. Assumptions about no prolonged post-bounce inflation, negligible fermion/torsion sourcing, and faithful cubic-order transfer through the bounce are stated clearly.

- The Bayesian comparison is more careful than is typical for this kind of forecast paper. The manuscript distinguishes the delta-prior theoretical maximum from the recommended finite-width bounce prior and reports competitor-prior sensitivity rather than presenting a single overconfident Bayes factor.

- The gauge-frame versus conformal-Fermi-frame discussion is handled responsibly: the manuscript identifies the survey observable as the gauge-frame local-template f_NL, while keeping the physical-frame consistency-relation point as a complementary theoretical discriminator.

- The manuscript provides extensive reproducibility hooks through named scripts and artifacts, including the overlap scan, Bayes-factor recomputations, continuous-prior checks, and GR-marginalization checks.

Final assessment

The remaining issues are not scientific blockers. The main quantitative forecast is sufficiently caveated and reproducible for a sensitivity-recast paper. After correcting the residual CDF-tail explanation in Sec. VI.C and tightening the minor wording issues above, I would support publication.
