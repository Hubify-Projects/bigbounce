VERDICT: MAJOR REVISIONS

ISSUES:

[MAJOR] Section VIII B/E and Table X, primary “same-footprint” estimand: the control footprint is constructed from the union of the detected hole-sphere angular discs and their radial span, not from the published DESIVAST/BGS mask or completeness model; the manuscript itself concedes that this does not match fiber completeness, imaging depth, vetoes, or radial selection, yet later calls it a “same-selection-function” estimator. Official DESIVAST instead uses a separately constructed smoothed angular mask and defines an interior fiducial volume by removing regions within 30h
−1
Mpc of survey boundaries. The primary contrast must be rerun with the official mask/randoms or a demonstrably selection-matched non-void control. 

ext_P5_FR1b

 

ext_P5_FR1b

 
Cambridge Repository
+1

[MAJOR] Sections V B, VIII, and XIII, “volume-limited BGS anchor”: imposing only z≤0.24 does not make the analyzed chirality sample the DESIVAST volume-limited BGS Bright tracer sample. The manuscript’s test sample remains a separate flux-limited imaging catalog, includes multiple DESI programs and SPECTYPE GALAXY/QSO objects, and does not impose the DESIVAST absolute-magnitude, spectroscopic-quality, and angular-mask selection. Claims that volume limitation eliminates target-selection mixing are therefore unsupported; the paper must state the exact test-galaxy selection and repeat the analysis on the official BGS/mask parent, including a GALAXY-only sensitivity test. 

ext_P5_FR1b

 
Cambridge Repository

[MAJOR] Sections VIII C-D and Tables XIII-XIV, V2 membership: approximating watershed voids by spheres centered on their volume-weighted centers with radius R
eff
	​

 is not a valid representation of V2/REVOLVER or V2/VIDE geometry, which is defined by Voronoi zones and, for VIDE, a hierarchy of linked zones. The official DESIVAST analysis reports that REVOLVER is nearly volume-filling in its fiducial region, whereas the manuscript’s sphere-PIS and catalog-native fractions are radically different and are not reconciled; the V2 sphere-PIS rows should be removed from the inferential family unless validated against the native zone assignments and official membership statistics. 

ext_P5_FR1b

 
Cambridge Repository
+1

[MAJOR] Section V B and Table XIV, definition of the Bonferroni-5 family: the declared primary exact footprint-restricted contrast (57,081,253,276) is absent from Table XIV, which instead includes the approximate unrestricted k=20 VoidFinder row (56,981,621,964); nevertheless, the simultaneous-interval discussion uses the footprint-restricted VoidFinder uncertainty. The other rows also use incompatible parents, including an all-z≤0.24 complement and a 145,789-object GALZONE join. Thus the five-member family and its quoted 1.1-pp simultaneous bound are not reproducible from one consistently defined set of estimands. 

ext_P5_FR1b

 

ext_P5_FR1b

[MAJOR] Sections V B and XV, interpretation of non-rejection: a “family-wise Bonferroni null” based on all p
Δ
	​

≥0.21 does not establish absence of environmental dependence. Bonferroni controls false discoveries; it does not turn failure to reject into evidence of equivalence. The paper should specify a scientifically meaningful equivalence margin before analysis, use simultaneous equivalence tests or confidence intervals for that margin, and phrase this DR1 result as an exploratory non-detection rather than “no dependence.” 

ext_P5_FR1b

 

ext_P5_FR1b

[MAJOR] Table XI and Sections VIII B/XII B, the quoted 0.9-pp “effective 2σ” envelope: the quadrature combines a 95% statistical half-width with maxima from deterministic perturbations, alternative geometries, different membership definitions, confidence cuts, and match-radius changes. These terms have neither common probability interpretations nor demonstrated independence, and several are changes of estimand rather than random nuisance parameters. Consequently the quadrature has no stated frequentist coverage or Bayesian credibility and cannot be quoted as an exclusion bound; the authors must construct an explicit nuisance model or report these variations as a non-probabilistic sensitivity range. 

ext_P5_FR1b

 

ext_P5_FR1b

[MAJOR] Section VIII B, uncertainty of the primary contrast: the two-proportion standard error treats hundreds of thousands of galaxy labels as independent Bernoulli trials, although galaxies share voids, sky regions, imaging conditions, and classifier systematics, and the hole spheres overlap extensively. The analysis requires spatially clustered uncertainty—e.g. void-level and sky-block bootstrap/jackknife, blockwise permutation, or survey mocks—with the resulting covariance propagated into all confidence limits; otherwise the quoted 0.44-pp counting interval and derived bounds are likely too narrow. 

ext_P5_FR1b

[MAJOR] Section VIII B, “adjustment in lieu of a full covariate regression”: target-program balance and a collection of one-at-a-time sensitivity cuts are not substitutes for covariate adjustment in the primary estimator. Void and non-void galaxies differ systematically in luminosity, color, size, surface brightness, inclination, and morphology, precisely the variables that can alter chirality-classification accuracy. A primary logistic, matched-control, or inverse-probability-weighted analysis should adjust at least for redshift, sky position, imaging leg, magnitude, size, inclination/edge-on probability, morphology, classifier confidence, and target program, with spatially robust errors. 
Cambridge Repository

[MAJOR] Appendix A and Section XII B, de-attenuated 2.26-pp “physical-chirality” bound: division by 2a−1 is valid only for known, nondifferential, parity-symmetric error rates that are transportable across environments. The manuscript takes the attenuation magnitude from a 69.91% global accuracy floor while taking symmetry evidence from a much higher-accuracy selected GZ1 subset, and its direct void calibration has a ±3.7-pp uncertainty—larger than the claimed classifier-label bound. A full environment-stratified confusion model with uncertainty and injection-recovery is required; moreover, projected arm-winding sense is not automatically the physical angular-momentum handedness 
L
^
 used in Appendix B. 

ext_P5_FR1b

 

ext_P5_FR1b

[MAJOR] Section VIII, RSD systematic: perturbing only galaxy line-of-sight positions while holding published void centers and radii fixed does not propagate redshift-space distortions through the void-finding algorithm. The resulting 34% increase in hole-union membership demonstrates that this is a highly asymmetric fixed-geometry stress test, not a calibrated RSD uncertainty, and the claim that a 0.5-pp shift would require “1.3 times” more reassignment assumes unsupported linear scaling. This term must be evaluated with redshift-space mocks or a reconstructed/re-found void catalog, or omitted from the quantitative envelope. 

ext_P5_FR1b

[MAJOR] Sections IV, VII, and IX A, T-Web robustness: the canonical field is built from a strongly selection-dependent number density with no complete angular/radial selection correction and an FFT treatment of a thin masked survey. The randoms-weighted rebuild changes approximately 73% of galaxy class assignments and reduces the void volume fraction by roughly a factor of 23; persistence of a null after such wholesale relabeling does not validate the classifier, because an uninformative or strongly mixed environment label will itself drive all class fractions toward the catalog mean. The T-Web material should either be rebuilt with a validated random-corrected, mask-aware, adequately resolved field and mock-based classification tests, or removed as evidence supporting the DESIVAST result. 

ext_P5_FR1b

 

ext_P5_FR1b

[MAJOR] Sections I, XII B, XV, and Appendix B, Physical Review D relevance: the manuscript states that no bounce or inflation model predicts the tested scalar void/non-void CW-fraction contrast, while the proposed EFT operator is acknowledged to be invented for this paper, non-covariant, and lacking a transfer function to the observed statistic. The data therefore do not constrain a defined parity-violating parameter space or discriminate bounce from inflation. The authors must either provide a concrete model and a forward calculation from the fundamental parity-odd quantity to projected spiral winding, or remove the bounce/inflation and EFT constraints and recast the work as an observational catalog study. 

ext_P5_FR1b

 

ext_P5_FR1b

 

ext_P5_FR1b

[MAJOR] Sections II, XIII, and Appendices A/D, dependence on Paper IV and reproducibility: the central outcome labels, training history, held-out validation, and possible train/test overlap reside in a companion paper still cited with a placeholder identifier, while the archival DOI is pending. Review cannot be completed from a self-summary alone. A revised submission must provide the final Paper IV manuscript for coordinated review, an immutable label catalog and code archive with checksums, explicit object-disjoint training/validation/test partitions, and a fully reproducible primary table generated from the frozen archive. 

ext_P5_FR1b

[MINOR] Throughout, presentation and internal consistency: the abstract occupies roughly three pages; “rebuttal note,” “honest,” and “strictly quotable” language is inappropriate for a research article; stale 0.5–0.6-pp statements remain after adoption of 0.9 pp; Tables XIII and XIV are sometimes cited interchangeably; and REVOLVER/VIDE are repeatedly called independent algorithms despite being two pruning prescriptions of the same V2 watershed construction. The manuscript should be shortened substantially and all sample counts, estimands, bounds, and cross-references reconciled. 

ext_P5_FR1b

 

ext_P5_FR1b

[MINOR] Sections III and VIII, object definition: a paper about spiral galaxies should not silently retain spectroscopic QSO matches in the primary selection. Report the number of chirality-labeled QSO objects in every primary parent, repeat the result with SPECTYPE=GALAXY only, and use one unique-TARGETID convention consistently in all headline tables.

The central claim is not supported at the stated 0.9-pp classifier-label or 2.26-pp physical-chirality level, although the reported raw contrasts are individually consistent with zero under the manuscript’s current, author-constructed sample and environment definitions.
