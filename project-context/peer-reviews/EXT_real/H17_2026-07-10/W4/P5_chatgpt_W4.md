(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:

[MAJOR] Section VIII A–E, DESIVAST void membership: The primary VoidFinder calculation appears to use all 101,863 hole spheres associated with 3,765 maximal voids, although the manuscript elsewhere quotes only 1,489 interior voids and does not document a mapping of each hole’s VOID identifier to the maximal-sphere EDGE flag or exclusion of “near-edge” voids. For V2, requiring the per-galaxy EDGE=0 flag is not equivalent to excluding voids whose volumes are boundary affected; the catalog defines V2 edge status through void-level boundary-surface information. DESIVAST explicitly distinguishes these cases because the thin DR1 mask makes most catalog voids edge affected. The headline contrast must be recomputed using non-edge voids, a stated near-edge buffer, and the appropriate void-level boundary criteria. 

ext_P5_W4

 
arXiv
+2
arXiv
+2

[MAJOR] Section VIII B, “footprint-restricted” primary control: The control footprint is an author-constructed union of projected hole-sphere discs intersected with a radial span, not the DESIVAST angular mask, completeness model, veto mask, or random catalog. The manuscript acknowledges this and nevertheless repeatedly describes the contrast as a “same-selection-function” estimand. Sharing gross angular–radial support does not balance fibre completeness, imaging depth, redshift, apparent magnitude, angular size, inclination, morphology, or classifier confidence. DESIVAST itself uses a specifically smoothed angular mask. The primary result requires the official mask/randoms and either a matched non-void control or a covariate-adjusted model with sky-region and redshift control. 
arXiv

[MAJOR] Sections V and VIII B, uncertainty on the primary contrast: The quoted SE(Δ)=0.0023 treats 57,081 void galaxies and 253,276 controls as independent Bernoulli observations. Galaxies share voids, large-scale structures, imaging tiles, sky-calibration residuals, and classifier systematics, so the binomial interval need not have its advertised coverage. The duplicate-row check does not address this clustering. A spatial block jackknife, sky-region cluster-robust covariance, and resampling at the void level are required; the result should report the effective design effect and the covariance between the two arms.

[MAJOR] Section V B and Tables X/XIV, definition of the Bonferroni family: The designated primary estimand—exact membership with the footprint-restricted n
nonvoid
	​

=253,276 control—is not one of the five rows in Table XIV; that table instead contains the approximate k=20, unrestricted VoidFinder contrast. The other rows also use materially different parent populations, including a 145,789-object GALZONE-joined parent rather than the 678,945-object low-redshift parent. They are therefore not five measurements of one common estimand. The exact primary must either replace the approximate row in a prospectively defined family or be included as an additional test, and all methods should be evaluated on a common target population and mask.

[MAJOR] Table XI and the abstract/conclusions, claimed ≃0.9 percentage-point bound: The “effective 2σ” envelope is obtained by adding in quadrature a frequentist counting interval, maxima over Monte Carlo perturbations, and deterministic shifts between correlated analysis definitions. These quantities do not share a probabilistic interpretation, their independence is not established, and several are alternative estimands rather than nuisance errors. The calculation also omits the unquantified selection-function mismatch, spatial covariance, environment-dependent label error, and uncertainty in the reconstructed void catalog itself. Moreover, the resulting 0.9 pp number is tighter than the manuscript’s own least-constraining Bonferroni simultaneous statistical limit of about 1.1 pp and therefore cannot serve as the advertised family-wise model bound. The terms should remain separate sensitivity results unless a calibrated nuisance model or mock-based coverage study is supplied.

[MAJOR] Appendix A and Sections XII–XIII, classifier selection and physical de-attenuation: Only 791,635 of 2,232,212 matched objects enter the CW/CCW analysis; 1,440,577 are assigned NS. The paper does not establish that selection into the CW/CCW subset, rather than only the CW↔CCW error rate conditional on selection, is independent of environment. This is especially important because morphology, surface brightness, inclination, and image quality vary with environment. The conversion by 1/(2a−1) additionally requires sensitivity and specificity to be equal and stable across environments. The void human-label validation has a quoted uncertainty of approximately ±3.7 pp and therefore cannot validate a sub-percent classifier-label bound. The ≃2.26 pp physical-chirality limit should be removed unless environment-conditioned selection and the full confusion matrix are measured with adequate precision.

[MAJOR] Section VIII, redshift-space-distortion and membership Monte Carlo: Independently displacing test galaxies by a Gaussian while holding void centers, radii, shapes, and the tracer catalog fixed does not model coherent peculiar velocities or the response of the void finder to reconstruction. The inference that a >0.5 pp shift would require 1.3× more membership changes assumes an unsupported linear relation between the number of flips and their chirality composition. Either rerun the void construction on realistic redshift-space/real-space mocks or restrict the result strictly to the published redshift-space catalog and remove this Monte Carlo from the quantitative systematic bound.

[MAJOR] Sections IV, VII, and IX A, secondary T-Web analysis: The canonical T-Web density field is constructed from an unweighted, strongly redshift-dependent mixture of DESI tracers using a global mean density, masked FFT boundary conditions, and a smoothing scale comparable to one grid cell. The manuscript’s own randoms-weighted rebuild changes the void volume fraction from 17.6% to 0.75% and reassigns roughly 73% of matched galaxies. This demonstrates that the canonical labels primarily trace the selection function, not that the physical classification is robust. Obtaining a null after two radically different relabelings can simply reflect signal dilution. This analysis should be rebuilt with tracer-specific randoms, bias/evolution treatment, validated survey-window handling, and mocks, or removed as evidentiary support.

[MAJOR] Sections XII B and Appendix B, physical interpretation: No forward model connects the measured projected CW label to the proposed parity-violating operator, the galaxy-spin distribution, line-of-sight projection, environmental selection, or the classifier response. The toy operator is also internally problematic: for a pseudoscalar ϕ, both ∇ϕ⋅∇ρ and 
L
^
⋅
∇ρ
	​

 are parity odd, so their product is parity even as written; the dimensional normalization of g
ϕ
	​

∇ϕ/H
0
	​

 is likewise unspecified. The manuscript therefore does not constrain a bounce, inflationary, axion-like, or EFT coupling. Appendix B and the associated model-builder claims should be removed unless a covariant operator and complete observable transfer calculation are provided.

[MAJOR] Sections II and Appendices D–E, companion-paper dependence and reproducibility: The per-galaxy labels are the essential measurement input, yet Paper IV retains an arXiv:XXXX.XXXXX placeholder and the immutable archival DOI is stated to be pending. A mutable repository tag and manuscript assertions are insufficient for auditing the many derived counts and sensitivity variants. Review or acceptance requires the final companion manuscript, exact catalog version, trained weights, commit hash, checksums, executable environment, and immutable data/code archive; coordinated review with Paper IV is necessary.

[MINOR] Sections V, VI, and VIII F, statistical terminology: Non-rejection should not be called evidence for “environment independence” except within a formally defined equivalence interval. Jeffreys credible intervals, frequentist confidence intervals, permutation p-values, and heuristic “2σ” envelopes are currently mixed. In addition, the Table XVI residuals use an overall monopole estimated from the same observations without including the resulting covariance, so they are not standard-normal z-scores; the contingency test or a correctly specified contrast should carry the inference.

[MINOR] Abstract, cross-references, and presentation: The pre-Introduction summary occupies several pages and repeats most of the paper; it should be replaced by a normal PRD-length abstract, with diagnostics moved to supplemental material. Internal inconsistencies must also be removed, including the residual “0.5–0.6 pp” language after adoption of 0.9 pp, references to Table XIII where the five-member family is in Table XIV, characterization of REVOLVER and VIDE as independent algorithms although they are two prunings of the same watershed construction, and the numerous encoding artifacts.

(3) The central claim is supported only as a qualitative non-detection in the reported classifier-labelled samples; the advertised ≃0.9 pp family-wise bound and ≃2.26 pp physical-chirality bound are not supported.
