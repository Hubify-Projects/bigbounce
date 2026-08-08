(1) VERDICT: REJECT

(2) ISSUES:

[MAJOR] Section VIII A–D and Tables X–XIV — edge-void handling is absent or misinterpreted. The manuscript states that the VoidFinder analysis uses all 101,863 holes associated with 3,765 maximal voids, while separately quoting only 1,489 voids as interior; no void-ID EDGE=0 selection or boundary-buffer/fiducial-volume cut is documented. For the V2 catalogs, the GALZONE.EDGE flag invoked in §VIII D describes whether an individual Voronoi cell reaches outside the mask, not whether its containing void is an edge void. DESIVAST reports that more than 60% of its detected voids are edge affected and defines V2 edge status from the void-level boundary area, so the five reported contrasts may be dominated by structures created or distorted by the thin survey boundary. All headline analyses must be repeated using explicitly non-edge void IDs and an interior fiducial volume. 

ext_P5_W2

 
arXiv
+1

[MAJOR] Section VIII B/E and Table X — the “footprint-restricted” control is not selection-function matched. The footprint is constructed from the angular projections of the detected hole spheres intersected with a radial span; it is neither the published DESIVAST/BGS mask nor a random-catalog estimate of angular and radial completeness, as the authors acknowledge. It conditions the control region on the locations of the voids themselves and does not demonstrate balance in redshift, cap, imaging depth, apparent magnitude, size, morphology, inclination, classifier confidence, or fibre-assignment completeness. The primary result therefore requires an official-mask/randoms-defined parent and either matched controls, inverse-probability weighting, or a covariate-standardized regression, with balance diagnostics and separate NGC/SGC results. 

ext_P5_W2

[MAJOR] Section V B and Tables IV, X, and XIV — the declared primary estimand is not contained in the advertised Bonferroni-5 family. The narrative primary is the exact, footprint-restricted contrast with n
void
	​

=57,081 and n
nonvoid
	​

=253,276, whereas Table XIV substitutes the approximate k=20, unrestricted contrast with 56,981 and 621,964 objects. The other family members use still different valid-parent populations, including the 145,789-object GALZONE parent. Bonferroni can control a collection of tests, but these rows do not estimate one common contrast, and the family-wise statement does not cover the manuscript’s stated primary estimator. A single estimand and parent population must be fixed, the actual primary included in the family, and the multiplicity count revised accordingly. 

ext_P5_W2

[MAJOR] Table XI, the abstract, and Section XII B — the quoted “≈0.9 pp effective 2σ envelope” has no defensible statistical coverage. The table combines a two-sample 95% counting interval with maxima of deterministic sensitivity changes, treats strongly correlated membership, geometry, footprint, and catalog-definition variations as independent Gaussian errors, and then adds them in quadrature. Several entries are not even excursions of the primary Δf
CW
	​

: the confidence and match-radius values in Table XIX are shifts in the catalog-wide f
CW
	​

, while the stated 0.37 pp “sphere-PIS vs GALZONE” term is the magnitude of one GALZONE point estimate rather than the actual sphere-to-GALZONE changes, which are approximately 0.18 and 0.20 pp from Tables XIII–XIV. The manuscript also derives a 1.1 pp simultaneous statistical bound elsewhere, inconsistent with presenting 0.9 pp—and hence 2.26 pp after de-attenuation—as the model-building bound. The sensitivity variations should be reported separately unless a nuisance-parameter model, mocks, or calibrated resampling procedure supplies a genuine interval with known coverage. 

ext_P5_W2

[MAJOR] Appendix A and Sections XII–XIII — the physical-chirality de-attenuation is unsupported. Dividing the classifier-label bound by 2a−1 assumes a purely binary classifier with symmetric, environment-invariant sensitivity and specificity and no environment-dependent selection into the analyzed sample. Here the same three-class classifier both determines CW/CCW and excludes the predicted NS population, while the adopted 69.91% “accuracy floor” is treated as an exact attenuation parameter. The manuscript’s own void-stratified GZ1 comparison has an error-asymmetry uncertainty of roughly ±3.7 pp, several times larger than the claimed classifier-label bound. A full environment-stratified three-class confusion model, including uncertainty and differential abstention/NS rates, is required; absent that analysis, the 2.26 pp physical bound must be withdrawn and the conclusion restricted to hard classifier labels. 

ext_P5_W2

[MAJOR] Sections V and VIII — the headline standard errors assume independent Bernoulli galaxies and ignore spatial and void-level covariance. Tens of thousands of galaxies are nested within the same voids, sky sectors, imaging fields, and selection-function regions, and classifier errors can be coherent within those groups. Deduplicating TARGETIDs does not address this design effect. The global and leg-by-program label shuffles used for secondary scans also assume exchangeability and do not provide a covariance estimate for the primary DESIVAST contrast. The principal intervals and z
Δ
	​

 values must be recomputed with void-level and spatial-block bootstrap or jackknife estimates, cluster-robust or hierarchical models, and preferably survey mocks that include cosmic variance and imaging-systematic correlations. 

ext_P5_W2

[MAJOR] Section VIII’s RSD discussion and the membership term in Table XI — the fixed-geometry perturbation is not an RSD uncertainty calculation. Independently perturbing each galaxy’s line-of-sight distance while holding every void center, radius, watershed, and survey boundary fixed does not transform consistently between real and redshift space; coherent velocity fields displace both the tracers and the inferred void geometry. The resulting approximately 34% increase in the assigned void population is itself evidence of asymmetric scattering against fixed boundaries. Neither the claimed ±0.37 pp RSD bound nor the extrapolation that a 0.5 pp change would require about 1.3 times more reassignments follows from this experiment. The paper should either remain explicitly a fixed-redshift-space measurement without an RSD error estimate or use reconstructed catalogs and realistic velocity-field mocks. 

ext_P5_W2

[MAJOR] Sections IV, VII, and IX A — the canonical T-Web classifier is not a scientifically controlled environment reconstruction. It is built from a flux-limited, redshift-dependent, multi-tracer density field normalized by one global mean inside an irregular mask. The manuscript’s own randoms-weighted rebuild changes roughly 73% of matched-galaxy class assignments and reduces the void volume fraction from 17.6% to 0.75%, demonstrating that the canonical labels are principally selection- and boundary-driven. Hyperparameter and grid sweeps around that biased construction do not establish physical robustness, and obtaining a null after massive class reassignment may simply demonstrate low sensitivity. The canonical T-Web analysis should be replaced by a fully randoms-weighted, window-controlled reconstruction or removed from the scientific conclusions; the inconsistent explanation in §VI A that the full n=428 void bin results from a z≤0.24 cut, despite only six such objects lying at z≤0.24, must also be corrected. 

ext_P5_W2

[MAJOR] Section XII B and Appendix B — the theoretical interpretation is not valid. No transfer function is supplied between a parity-violating theory and the measured scalar void/non-void fraction. Moreover, for the stated pseudoscalar ϕ, ∇ϕ is axial and ∇ρ is polar, so ∇ϕ⋅∇ρ is parity odd; 
L
^
⋅
∇ρ
	​

 is also parity odd, making their product parity even rather than the claimed parity-violating operator, assuming the coupling is an ordinary scalar. Its dimensions and normalization are also unspecified, and the manuscript acknowledges that it is noncovariant and gauge dependent. Appendix B and the claimed bounce/inflation or coupling constraints should be removed unless a covariant operator and a quantitative projection onto the measured observable are derived. 

ext_P5_W2

[MAJOR] Sections II and XIII and Appendix D — the central measurement depends on an unresolved companion-paper input. The per-object chirality labels, training history, calibration, parity handling, and label-selection function come from Paper IV, which is cited with an unresolved arXiv placeholder, while the archival DOI is described as pending. Public availability of a label column does not establish its scientific validity, independence of validation data, WCS-parity consistency, or environment-conditioned error behavior. Paper IV and the exact frozen catalog/weights/code snapshot must be available for coordinated review before this analysis can be assessed or accepted. 

ext_P5_W2

[MINOR] Sections III, IX B, and X — several supporting estimators require technically correct matching and paired inference. Because the chirality and DESI coordinates share Tractor provenance, a stable source-identifier join should replace or validate the 1-arcsec nearest-neighbor association, including a random-shift false-match estimate and second-neighbor ambiguity rate; objects classified spectroscopically as QSO should be excluded from, or explicitly quantified in, a “spiral galaxy” sample. Comparisons between T-Web, Tempel, and ASTRA classifications on overlapping galaxies should use paired permutations or sandwich covariance rather than independent two-proportion tests, and the richness-to-cosmic-web mapping should remain purely descriptive. 

ext_P5_W2

[MINOR] Abstract, Sections V–XV, and table cross-references — the manuscript requires a complete editorial rewrite. Several pages of headline, setup, rebuttal, and robustness material precede the Introduction; the same caveats and numbers are repeated throughout; the superseded 0.5–0.6 pp envelope remains in §VIII after the manuscript adopts 0.9 pp; “three independent algorithms” conflicts with the acknowledged two algorithmic families; and the five-row family is occasionally attributed to Table XIII rather than Table XIV. A conventional abstract, one clearly defined primary analysis, a compact results section, and removal of defensive or prospective material are necessary. 

ext_P5_W2

(3) The central claim is not supported at the stated level: the counts provide a descriptive non-detection in the chosen classifier labels, but neither the advertised family-wise sub-percent bound nor the de-attenuated physical-chirality bound is presently valid.
