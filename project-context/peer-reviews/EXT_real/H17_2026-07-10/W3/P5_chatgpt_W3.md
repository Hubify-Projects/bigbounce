(1) VERDICT: REJECT

(2) ISSUES:

[MAJOR] Section VIII B/E and Table X, “primary same-footprint estimand”: the control volume is not the DESIVAST/BGS usable survey mask. It is an author-constructed union of projected void-hole discs intersected with a global radial span. The manuscript explicitly concedes that this is neither the published completeness mask nor a random-catalog representation of the selection function, yet elsewhere calls the comparison “same-selection-function” and makes it the load-bearing result. Redshift, angular completeness, imaging depth, morphology, and classifier-confidence balance between void and control samples are not demonstrated or adjusted. The primary contrast must be recomputed using the official mask/randoms or a matched, inverse-probability-weighted, or covariate-adjusted control. 

ext_P5_W3

[MAJOR] Sections III B and VIII B-D, Tables XIII-XIV, sample and membership definitions: the 678,945-object z≤0.24 parent is not shown to satisfy the DESIVAST volume-limited BGS selection; the input permits QSO and other non-BGS targets, whereas the catalog-native GALZONE-valid parent contains only 145,789 objects. The V2 sphere-PIS rows replace irregular watershed zones by effective-radius spheres, and the VoidFinder row retains a knowingly incomplete k=20 query even though an exact result is available. These rows therefore measure different populations and different environment definitions, not five interchangeable “DESIVAST void definitions.” The discrepancy between the quoted 1,489 interior VoidFinder voids and the 3,765 maximal objects subsequently used also requires an explicit quality-cut reconciliation.

[MAJOR] Section V B and Tables IV/XIV, multiplicity and null inference: the designated exact, footprint-restricted primary estimate is not one of the five tests in Table XIV; that table instead contains the approximate, unrestricted k=20 VoidFinder result. Exact versus approximate membership, unrestricted versus footprint-restricted controls, maximal-sphere membership, confidence cuts, and other analyzed variants add further trials. With no timestamped analysis plan, the asserted Bonferroni-5 family does not cover the actual analysis-selection process. Moreover, failure to reject five null hypotheses is not “family-wise evidence for the null.” A complete multiverse must be enumerated, and a scientifically pre-specified equivalence margin must be tested using simultaneous confidence intervals.

[MAJOR] Table XI, Abstract, Section XII B, and Conclusions, the claimed ≃0.9 percentage-point “honest 2σ systematic envelope”: this number has no defensible coverage interpretation. It combines a statistical 95% half-width with maxima from correlated alternative definitions, treats them as independent zero-mean errors, and mixes changes in different estimands and different parent samples. In particular, Section XI reports confidence-threshold and match-radius changes in the catalog-wide f
CW
	​

, not demonstrated changes in the primary void/non-void contrast, yet Table XI treats them as Δf
CW
	​

 systematics. Selection-function uncertainty, differential classification error, spatially correlated imaging errors, void-catalog uncertainty, and full RSD uncertainty are omitted. The manuscript’s own Bonferroni simultaneous counting interval permits an effect of approximately 1.1 percentage points, already wider than the advertised 0.9-point bound. The 0.9-point number cannot be presented as an exclusion or supplied to model builders.

[MAJOR] Appendix A and Sections XII B/XIII, conversion from classifier labels to physical chirality: division by 2a−1 using a global 69.91% accuracy assumes symmetric, nondifferential sensitivity and specificity across environments. The void-specific validation permits an error-asymmetry difference of several percentage points—far larger than the claimed sub-percent bound—and tests only directional error asymmetry, not environment dependence of sensitivity, specificity, attenuation, confidence, or CW/CCW/NS selection. Conditioning on predicted CW/CCW while excluding 1.44 million NS-labelled matched objects can itself produce environment-dependent selection. The global Galaxy Zoo parity test does not validate the environmental contrast. Consequently, the quoted 2.26-percentage-point physical-chirality bound is unsupported; a sufficiently powered, environment-stratified full confusion model or a forward-modelled measurement-error analysis is required.

[MAJOR] Section VIII, RSD robustness: perturbing only the test galaxies’ radial positions while holding the redshift-space void centers and radii fixed is not a physical model of redshift-space distortions, because the void catalog and its tracer galaxies are affected coherently by the same velocity field. The test changes approximately 34% of memberships, the maximum of 200 realizations is not a calibrated 2σ uncertainty, and the extrapolation that a 0.5-point shift would require only “1.3 times” the tested perturbation has no demonstrated scaling law. A redshift-space/real-space mock comparison or reconstructed-position rerun is needed; until then this can only be reported as a fixed-redshift-space measurement with unquantified RSD systematics.

[MAJOR] Sections IV, VII, and IX A, T-Web construction: the canonical field is built from heterogeneous, flux-limited DESI tracers without completeness or tracer-bias weights, with only 4.64 galaxies per occupied cell, a 25.9 h
−1
 Mpc cell size for a 25 h
−1
 Mpc Gaussian smoothing scale, and an FFT Poisson solve in a highly non-periodic masked cube. The nominal smoothing is therefore barely one grid cell and is not demonstrably converged. Most decisively, the randoms-weighted rebuild changes roughly 73% of galaxy classifications and reduces the void volume fraction from 17.6% to 0.75%, establishing that the canonical labels primarily trace the selection function. Obtaining a similar chirality null after radically repartitioning an almost globally balanced label catalog does not validate either environmental classification. The T-Web analysis must be rebuilt with a controlled tracer sample, appropriate randoms, boundary treatment, and adequate resolution, or removed from the evidentiary claims.

[MAJOR] Sections V, VI A, and VIII F, uncertainty and covariance: the principal intervals treat galaxy labels as independent Bernoulli draws, despite shared void membership, spatially correlated imaging/classifier errors, and common survey regions. No void-level hierarchical model, spatial block bootstrap, or survey jackknife is supplied. In addition, the “σ
vsmonopole
	​

” values use a global fraction estimated from the same galaxies but divide by 0.5/
n
class
	​

	​

, omitting the covariance between a class fraction and the containing total; Table XVI is therefore not correctly standardized. The primary result needs spatially robust uncertainty estimation and a regression or hierarchical model conditioned on the relevant survey covariates.

[MAJOR] Sections II and Appendix D, dependence on Paper IV and archival reproducibility: the classifier labels are the indispensable measurement input, but the companion paper still has a placeholder arXiv identifier, the final catalog/version has not been tied to an immutable DOI in the manuscript, and the paper requests acceptance conditional on later co-review. A Git tag is not an immutable archival record, and an appendix-level summary cannot substitute for review of training leakage, label construction, calibration, and validation. The present analysis must be rerun against the final frozen catalog, and the companion manuscript, weights, data snapshot, and executable provenance must be available during—not after—review.

[MAJOR] Introduction, Section XII B, and Appendix B, physical interpretation and PRD relevance: the measured quantity is projected image winding as assigned by a classifier, not a demonstrated intrinsic three-dimensional spin or fundamental parity observable. No near-side determination, trailing-arm assumption, spin-transfer model, or concrete bounce/inflation prediction connects the measured contrast to the proposed physics. The Appendix B operator is explicitly non-covariant and dimensionally unspecified; moreover, for an axion-like pseudoscalar ϕ, both ∇ϕ⋅∇ρ and 
L
^
⋅
∇ρ
	​

 are parity-odd, so their product is parity-even unless an additional parity-breaking background and transformation prescription are supplied. The EFT and model-exclusion discussion should be removed or replaced by an actual forward calculation; without one, the work is principally an exploratory astronomical catalog analysis rather than a supported fundamental-physics constraint.

[MINOR] Section III C, angular cross-match: shared astrometric provenance explains the very small separations but does not quantify false associations or one-to-one ambiguities. A shifted-coordinate control, conflict statistics for both catalogs, and the effect of match radius on the primary Δf
CW
	​

—rather than only on the global fraction—should be reported.

[MINOR] Section VI D and Table XII, program interaction: the dark-program void/non-void difference is approximately 4.7 percentage points at about 2σ, but it is dismissed without a formal environment-by-program interaction test. The claimed 0.001-point leakage estimate assumes no interaction and is calculated on the unrestricted approximate membership sample rather than the exact footprint-restricted primary parent. The interaction and its uncertainty should be estimated on the actual primary sample.

[MINOR] Abstract, cross-references, and figures: the manuscript is excessively repetitive and reads partly as a sequence of rebuttal notes; the abstract alone extends over several pages. Terminology alternates between “same footprint” and “same selection function,” Table XIII is sometimes cited where the consolidated family is in Table XIV, and Figure 6’s upper panel is labelled as maximal-void counts although its pixel count/scale is not reconciled with that description or with the caption. A substantial condensation and consistency audit are required.

(3) The narrow claim that these particular classifier labels show no statistically significant void/non-void difference in the analyzed samples is supported, but the advertised family-wise ≃0.9-percentage-point constraint on physical spiral chirality is not.
