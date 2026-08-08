(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:

[MAJOR] Section VIII B/E, “footprint-restricted primary estimand” — The void and control samples are not demonstrably selection-function matched. The adopted “footprint” is an NSIDE-64 union of projected hole discs intersected with a radial span, not the published BGS completeness mask or a random-catalog estimate; the manuscript itself acknowledges that it does not match fibre completeness, imaging depth, or radial selection. No balancing is performed in redshift, luminosity, size, morphology, classifier confidence, or imaging conditions, although several of these variables demonstrably affect the classifier output. The primary contrast must be recomputed using the DESIVAST/BGS mask and randoms, together with covariate-matched, inverse-probability-weighted, or per-void matched controls. 

ext_P5_M34

[MAJOR] Section V B and Tables X–XIV, primary-family definition — The designated headline statistic, namely the exact, footprint-restricted VoidFinder contrast with n
void
	​

=57,081, is not the VoidFinder statistic included in the stated Bonferroni-5 family; Table XIV instead uses the unrestricted k=20 contrast with n
void
	​

=56,981. Exact versus approximate membership, footprint-restricted versus unrestricted controls, maximal-sphere membership, and other inspected variants add further analysis choices beyond the declared five. Consequently, the claimed family-wise coverage does not apply cleanly to the advertised primary estimator. The hypothesis family and all estimator choices must be fixed explicitly, and simultaneous intervals must be recomputed for that complete family.

[MAJOR] Section VIII B and Table XI, “honest effective 2σ systematic envelope” — The 0.9-percentage-point envelope has no defensible confidence interpretation. It combines a statistical confidence half-width, shifts between different void definitions, excursions from different parent samples, and quantities that are not measured on the primary Δf
CW
	​

 estimand; for example, the confidence and match-radius entries in Section XI are changes in the catalog-wide f
CW
	​

, not in the void-minus-control contrast. The terms are also correlated and are not independently distributed 2σ uncertainties, so quadrature is unjustified. Moreover, even treating 0.94 pp as a valid half-width, the observed central value of 0.18 pp must be included, giving an absolute upper extent near 1.1 pp, not 0.9 pp. A nuisance-parameter model, block bootstrap, or explicitly conservative union interval is required.

[MAJOR] Sections V and VIII, uncertainty model for the primary contrast — The two-sample binomial standard error treats 57,081 void galaxies as independent Bernoulli observations, although galaxies are clustered within the same voids, sky regions, imaging fields, and classifier-systematic patches. Individual-label shuffles likewise destroy spatially correlated errors and can be anticonservative. The primary uncertainty should be estimated with a bootstrap or jackknife over voids and large sky blocks, or with a cluster-robust hierarchical/logistic model; the resulting design effect must be reported before any sub-percent limit is quoted.

[MAJOR] Appendix A and Section XII B, conversion to a 2.26-pp “physical-chirality bound” — The attenuation formula 2a−1 requires nondifferential, environment-independent sensitivity and specificity, not merely a global accuracy estimate. The direct void-stratum validation has only 933 objects and permits directional error asymmetries of several percentage points, much larger than the claimed 0.9-pp classifier-label bound. Void and non-void galaxies also differ in morphology, apparent size, surface brightness, and confidence, all of which can change classification error. The 2.26-pp physical bound is therefore unsupported and should be removed unless an environment-stratified calibration or injection–recovery analysis is supplied with calibration uncertainty propagated.

[MAJOR] Section VIII, redshift-space-distortion bound — Independently perturbing galaxy distances while holding the void catalog fixed is not a physical RSD realization, and displacing galaxies and published holes with an assumed analytic profile without rerunning the void finder is not a reconstruction of the environment catalog. Stability under symmetric random membership exchanges does not bound a coherent or label-correlated membership error. The assertion that producing a larger Δf
CW
	​

 would require proportionally more reassigned galaxies is also incorrect: a much smaller, chirality-biased subset can shift the contrast appreciably. The 0.02-pp and 0.37-pp terms should be described only as sensitivity tests unless the void catalog is rebuilt on reconstructed positions.

[MAJOR] Sections IV, VII, and IX A, physical validity of the T-Web analysis — The random-catalog-weighted rebuild changes the void volume fraction from 17.6% to 0.75% and preserves only 26.6% of matched-spiral class assignments. This demonstrates that the canonical T-Web labels are dominated by the survey selection function and mask treatment rather than being a stable physical environment classification. That analysis cannot be used as independent cosmic-web validation, nor can it justify the claimed sensitivity at a well-defined 25 h
−1
 Mpc physical scale. It should either be rebuilt from the outset with randoms, completeness weights, and validated boundary conditions or reduced to a clearly non-inferential appendix.

[MAJOR] Appendix B and Section XII B, theoretical interpretation — For a pseudoscalar ϕ, ∇ϕ is an axial vector; both (∇ϕ⋅∇ρ) and (
L
^
⋅
∇ρ
	​

) are parity-odd, so their product is parity-even, contrary to the appendix’s stated parity assignment. The operator normalization and dimensions are also unspecified, and no transfer function connects its coupling to the measured galaxy statistic. The proposed EFT bound is therefore not valid. More generally, because no identified bounce or inflation model predicts the measured observable, the manuscript does not presently establish the advertised model constraint; this appendix should be removed or completely rederived.

[MAJOR] Section XIII and Appendices A/D, dependence on Paper IV — The entire outcome variable comes from a concurrently submitted classifier paper whose arXiv identifier is still a placeholder and whose definitive catalog snapshot and archival DOI are not yet fixed. The environmental analysis cannot be fully refereed without the final training, validation, confusion matrices, label provenance, and immutable catalog version. Publication should be conditional on coordinated review of Paper IV and on a frozen public archive from which every quoted count can be regenerated.

[MINOR] Title, abstract, and Section VIII C — “Three independent void-finding algorithms” is inaccurate. V2-REVOLVER and V2-VIDE are two pruning prescriptions applied to the same ZOBOV/V2 watershed construction, as the manuscript later acknowledges; the correct description is two algorithm families and five correlated definitions.

[MINOR] Sections III B and VIII, spectroscopic selection — The analysis admits objects with SPECTYPE == QSO while presenting the sample as spectroscopically confirmed spiral galaxies. The primary result should be repeated with SPECTYPE == GALAXY only, and the QSO counts in the void and control samples should be disclosed.

[MINOR] Organization and presentation — The same caveats and null results are repeated across Sections V–XV, while several weakly informative secondary tests occupy more space than the primary estimator. The manuscript should be substantially shortened, with T-Web, ASTRA, Tempel, and detailed scan diagnostics moved to supplementary material and one internally consistent primary analysis retained in the main text.

(3) The reported counts support a qualitative non-detection, but they do not support the advertised 0.9-pp classifier-label bound or its 2.26-pp physical de-attenuation.
