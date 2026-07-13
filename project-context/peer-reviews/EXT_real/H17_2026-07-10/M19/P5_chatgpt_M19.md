(1) VERDICT: REJECT

(2) ISSUES:

[MAJOR] Section VIII A–E, DESIVAST VoidFinder sample definition: the analysis uses all 101,863 hole spheres associated with approximately 3,765 total VoidFinder voids while repeatedly describing them as “interior.” DESIVAST distinguishes only approximately 1,489 interior VoidFinder voids and reports that more than 60% of its detected voids are edge voids whose geometry is affected by the thin survey boundary. The primary result must be recomputed using the DESIVAST edge flag, with interior and edge voids reported separately. Moreover, VAST defines a VoidFinder void as the union of its hole spheres; the maximal-sphere-only sample is therefore a different central-void estimand, not an equally valid geometry realization whose 0.60-pp difference can be treated as an additive uncertainty. 

ext_P5_M19

 
arXiv
+2
arXiv
+2

[MAJOR] Section VIII B/E, “footprint-restricted” control: the adopted footprint—the union of hole-sphere angular discs intersected with a global radial range—is not the DESIVAST angular mask, the BGS selection function, or a random-catalog completeness estimate. The manuscript explicitly concedes that fibre assignment, imaging depth, radial completeness, and other selection variables remain unmatched, yet elsewhere calls this a “same-selection-function” estimator. The primary analysis requires the actual survey mask and randoms, or per-void controls matched at minimum in redshift, sky position, imaging leg, apparent magnitude, angular size, axial ratio, morphology, and classifier confidence. The standard VoidFinder workflow explicitly uses a survey mask and provides object-environment classification relative to that mask. 

ext_P5_M19

 
arXiv
+1

[MAJOR] Section V B and Tables X/XIV, multiplicity accounting: the designated primary estimator is the exact, footprint-restricted VoidFinder contrast, Δf
CW
	​

=0.0018, but the VoidFinder member of the stated Bonferroni-5 family in Table XIV is the approximate k=20, unrestricted-control contrast, Δf
CW
	​

=0.0007. Thus the claimed family-wise correction does not actually cover the reported primary estimator. Other data-inspected choices—exact versus k=20, footprint versus unrestricted control, maximal-sphere versus hole union, edge/depth cuts, and confidence cuts—are also omitted from the five-test family despite affecting the bound. A complete analysis tree must be included in one global simultaneous inference, or the DR1 result must be presented solely as exploratory without a family-controlled exclusion. 

ext_P5_M19

[MAJOR] Abstract, Table XI, and Sections VIII/XII, the “honest effective 2σ envelope” of 0.9 percentage points: this is not a statistically defined confidence interval. The table combines a binomial 2σ half-width with peak shifts between correlated alternative estimands, treats all entries as independent Gaussian standard deviations, and partially double-counts membership and geometry changes. A maximum excursion under an analysis variant is not a 2σ nuisance uncertainty. The manuscript’s separate approximately 1.1-pp Bonferroni simultaneous interval is at least formally interpretable, but it still omits selection-function, spatial-correlation, and differential-label uncertainties. The 0.9-pp number should not be advertised as having 95% coverage without an end-to-end mock, bootstrap, or explicit nuisance-parameter likelihood. 

ext_P5_M19

[MAJOR] Section V and the primary two-proportion inference: the quoted standard errors and z-scores treat tens of thousands of galaxies as independent Bernoulli observations. Galaxies share voids, angular regions, imaging conditions, target-selection residuals, and overlapping VoidFinder spheres; these dependencies are exactly the channels capable of producing sub-percent classifier-label correlations. Individual-galaxy label shuffles destroy this dependence and are not a valid null for spatially correlated systematics. The primary contrast needs a block jackknife or bootstrap over independent sky regions and voids, together with cluster-robust or hierarchical uncertainty propagation. 

ext_P5_M19

[MAJOR] Section VIII B/XI, lack of covariate adjustment in the load-bearing analysis: the manuscript performs adjusted regressions only for the secondary T-Web sample and explicitly defers the corresponding DESIVAST regression or matched-control analysis. Near-equality of the bright/dark program fractions does not establish balance in redshift, luminosity, apparent size, surface brightness, axial ratio, morphology, confidence, or imaging conditions. Because these variables affect both environment membership and chirality-label performance, an unadjusted null contrast cannot support a sub-percent environmental bound. The adjusted analysis must be carried out on the exact primary DESIVAST parent rather than deferred to DR2. 

ext_P5_M19

[MAJOR] Appendix A and Section XII, conversion from classifier labels to “physical chirality”: the de-attenuation by 2a−1 is identified only under nondifferential, environment-independent, symmetric sensitivity and specificity. In general the attenuation is sensitivity+specificity−1, plus terms from differential errors; overall accuracy alone does not determine it. The manuscript’s own void human-label validation has only 933 void objects and a directional-error-asymmetry interval several percentage points wide, nearly an order of magnitude broader than the claimed classifier-label bound. It therefore cannot validate the needed assumption at sub-percent precision. The use of hard argmax labels and exclusion of the predicted NS class also introduces an unmodelled environment-dependent selection step. The public classifier documentation further states that production uses only Z
2
	​

 augmentation and records an approximately 20–21% full-D
4
	​

 argmax-instability concern for individual labels. A probabilistic-posterior analysis with environment-stratified external validation is required; the 2.26-pp physical bound is presently unsupported. 

ext_P5_M19

 
Hugging Face
+1

[MAJOR] Sections IV, VII, and IX A, secondary T-Web classification: the manuscript itself demonstrates that the canonical T-Web field is dominated by survey selection—the shell mean varies by a factor of roughly 640, while a randoms-weighted rebuild changes approximately 73% of matched-galaxy class labels and reduces the inferred void volume fraction by about a factor of 23 in the tested window. Obtaining another null after replacing most environment labels is not evidence of robustness; it shows that the original labels do not define a stable physical environment. The T-Web analysis must either be rebuilt from the outset with tracer-specific selection functions, random catalogs, proper boundary treatment, and resolved grids, or removed as supporting evidence. It also cannot supply a 25h
−1
Mpc physical scale to the DESIVAST primary result, which has no such smoothing parameter. 

ext_P5_M19

[MAJOR] Section VIII, redshift-space-distortion bound: displacing galaxies and already-published hole centers with an assumed first-order velocity profile, without reconstructing the tracer density and rerunning the void finder, is not an end-to-end reconstruction of DESIVAST membership. Likewise, adding chirality-independent Gaussian line-of-sight perturbations will generally leave a chirality fraction nearly unchanged by construction and does not test correlations between RSD, survey selection, and label bias. The reported 0.024-pp change is a fixed-catalog sensitivity diagnostic, not a bound on the RSD systematic, and should not enter Table XI as such. A suitable test requires realistic mocks or reconstructed catalogs followed by complete void refinding and remeasurement. 

ext_P5_M19

[MAJOR] Sections II, XII, XV, and Appendix B, cosmological interpretation: no bounce or inflation model is shown to predict the measured statistic, and no transfer function connects a primordial parity-odd degree of freedom to the observed projected winding-label contrast. Consequently, the statement that the result constrains bounce or inflation models is not quantitative. The toy operator is also incorrectly described as parity odd: for pseudoscalar ϕ, both ∇ϕ⋅∇ρ and 
L
^
⋅
∇ρ
	​

 are pseudoscalars, so their displayed product is parity even. Its dimensions and normalization are unspecified as well. Appendix B and the claimed EFT bound should be removed unless replaced by a covariant, symmetry-consistent derivation with a calculable observable. 

ext_P5_M19

[MAJOR] Sections II/XIII and Appendices A/D, companion-paper dependency and frozen provenance: the load-bearing labels come from an unpublished companion manuscript with an arXiv placeholder, while the archival DOI is still pending. The currently linked public model documentation is itself internally inconsistent—for example, its displayed CW and CCW counts do not sum to its stated number of spirals, and it describes 0.4974±0.000279 as approximately 1σ from parity while also reporting the same residual as approximately 9.5σ. The manuscript cannot be reviewed reproducibly until the exact catalog, weights, source, configurations, and derived primary table are frozen under one immutable DOI/hash and Paper IV is simultaneously available for substantive review. 

ext_P5_M19

 
Hugging Face
+1

[MINOR] Title, abstract, and overall presentation: DESIVAST contains two void-finding families—VoidFinder and V2—with REVOLVER and VIDE being two V2 pruning prescriptions, not three independent algorithms. The manuscript should use that terminology consistently, eliminate repeated “headline/load-bearing/honest” assertions, resolve contradictions over exact versus k=20 membership and “footprint” versus “selection function,” and reduce the 42-page presentation to the primary analysis plus essential validation. 

ext_P5_M19

 
arXiv

(3) No—the reported hard labels do give a non-significant contrast in the author’s selected samples, but the central quantitative claim of a family-controlled 0.9-pp classifier-label bound, its 2.26-pp physical conversion, and the associated cosmological interpretation are not supported.
