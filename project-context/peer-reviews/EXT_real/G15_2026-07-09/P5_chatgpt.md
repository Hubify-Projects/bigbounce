# P5 ChatGPT EXT review — G15 2026-07-09

- Paper: P5 v0.1.112 (43pp), g_P5.pdf
- Reviewer: ChatGPT Pro (Extended Thinking)
- URL: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a50495d-ee70-83e8-8787-84cafb76dbf1
- Verdict: **MAJOR REVISIONS** (F14 baseline: MAJOR)

## Raw response

Referee report for Physical Review D
Overall assessment

The manuscript analyzes a very large matched galaxy sample and reports no statistically significant difference in classifier-assigned clockwise fraction between DESIVAST void and non-void samples. The author has made an unusually extensive effort to disclose post-hoc choices, catalog monopoles, alternative void definitions, and known weaknesses of the T-Web implementation. I do not see evidence that the reported counts conceal a significant positive signal.

However, the present manuscript does not establish its central quantitative claim: a controlled, approximately 0.9-percentage-point upper bound on environment-dependent physical spiral chirality. The primary sample is not demonstrably restricted to reliable DESIVAST interior voids, the control is not selection-function matched, environment-dependent classifier errors are uncalibrated, and the quoted “systematic envelope” has no defined statistical coverage. There are also irreconcilable inconsistencies over which contrast is primary. These are substantive problems requiring new analysis, not merely changes of wording. 

g_P5

Major concerns
1. MAJOR — The primary VoidFinder analysis appears to include the edge-void population, and therefore does not yet define a reliable physical void sample

Section VIII begins by quoting 1,489 interior VoidFinder voids, but §VIII A then constructs the primary membership from all 101,863 holes associated with all 3,765 maximal voids and calls these “interior hole spheres.” No filter on the VoidFinder EDGE flag or on the DESIVAST fiducial interior volume is reported for the primary 56,981/57,081-galaxy sample.

This distinction is critical. The official DESIVAST catalog contains 3,765 total VoidFinder voids but only 1,489 interior voids; the DESIVAST paper states that more than 60% of the detected voids are edge voids and explicitly introduces a fiducial volume excluding regions within 30h
−1
Mpc of survey boundaries when reporting void statistics. 
Cambridge Repository
+1
 The manuscript’s own use of all 3,765 objects therefore appears to admit the exact boundary-dominated population that DESIVAST flags as geometrically distorted. 

g_P5

The custom footprint constructed from the same hole spheres does not cure this: demonstrating that all hole-defined members fall inside a footprint defined from those same holes is tautological, and does not show that the voids are unaffected by the survey boundary.

The primary analysis must be repeated using, at minimum:

VoidFinder voids with the catalog EDGE=0 criterion;

preferably the DESIVAST fiducial-volume boundary cut;

the official angular/radial mask or a faithfully reconstructed equivalent;

a separate report of interior versus edge-void results.

Until that analysis is provided, the headline sample cannot be interpreted as a controlled sample of physical cosmic voids.

2. MAJOR — The primary non-void control is not selection-function matched, and the required confounder adjustment is explicitly deferred

Section VIII B correctly states that the “footprint” is only the union of projected hole-sphere discs intersected with a radial interval. The manuscript expressly acknowledges that this is not the published DESIVAST/BGS completeness mask, does not include its vetoes or DESI randoms, and does not guarantee matched fibre-assignment completeness, imaging depth, or radial selection. Nevertheless, the same section later says that the footprint-restricted estimator “matches the void and control selection functions directly.” Those two statements are incompatible. 

g_P5

The manuscript also acknowledges that the appropriate analysis would be a matched, inverse-probability-weighted, or covariate-adjusted model involving redshift, magnitude, size, morphology, classifier confidence, imaging leg, and sky position—but defers it to DR2. Matching only the broad bright/dark target-program fraction is not an adequate substitute.

This is especially important because the void catalog is constructed from a volume-limited BGS tracer catalog, whereas the analyzed chirality sample is itself flux limited, as admitted in §XIII. Calling the primary spiral sample “volume limited” is therefore incorrect. The two analysis populations may have different redshift, luminosity, apparent-size, inclination, morphology, imaging-depth, and classifier-confidence distributions. Each of those quantities can affect classification quality.

A publishable primary test requires:

distributions of the relevant observables for void and control galaxies;

a matched-control, standardized, or regression-adjusted estimate;

balance diagnostics after adjustment;

use of the actual DESIVAST selection mask and DESI randoms, rather than a mask inferred from the detected voids.

Without this, the reported Δf
CW
	​

 is a raw sample contrast, not a controlled environmental contrast.

3. MAJOR — Differential classifier error by environment is unmeasured, so the manuscript cannot infer physical chirality independence

The statement that a catalog-wide monopole cancels algebraically is correct only for a genuinely common additive label bias. It does not address differential misclassification between environments. The classifier has a reported binary accuracy of 69.91%, and the manuscript explicitly states that no environment-stratified human-label confusion matrix exists. Environmental samples can differ in apparent size, surface brightness, spiral-arm contrast, inclination, crowding, redshift, and morphology, all of which could change CW/CCW error rates.

The Paper IV control using Galaxy Zoo votes is a global parity test; it does not establish that the human/model agreement is the same inside and outside voids. Similarly, exact flip equivariance prevents a particular mirror-augmentation failure but does not guarantee equal classification sensitivity across galaxy populations.

The primary conclusion must therefore be restricted to:

no detected difference in the classifier-assigned label fraction for the stated samples.

A claim about physical spiral chirality requires an environment-stratified validation set or an injection/recovery analysis that estimates the confusion matrix separately in void and control populations.

There is also a numerical error in Appendix A. Under the manuscript’s own symmetric-error approximation, the attenuation factor is

2a−1=2(0.6991)−1=0.3982.

Thus a 0.9-pp classifier-label bound would correspond to approximately 0.9/0.3982=2.26 pp in true chirality, not a bound merely “a few tenths of a percentage point looser.” Likewise, the stale 0.5–0.6-pp bound would map to about 1.26–1.51 pp. This error materially affects the model interpretation. 

g_P5

4. MAJOR — The manuscript does not consistently identify its primary estimand or primary sample

The abstract identifies the footprint-restricted contrast

Δf
CW
	​

=+0.0018,n
nonvoid
	​

=253,276

as primary and identifies +0.0007 as a secondary sensitivity result. The Conclusions instead call the unrestricted +0.0007, n
void
	​

=56,981 result “the primary result.” The title also uses 56,981 galaxies. 

g_P5

At the same time:

the exact unbounded membership calculation gives n
void
	​

=57,081;

Table X tabulates a k=20 approximate void row but an exact footprint-restricted control row;

the author acknowledges that k=20 is algorithmically insufficient because up to 249 hole centers may be relevant and 28% of the sample has more than 20 candidates;

the known approximation is retained “for continuity with the released artifacts” rather than replaced by the correct calculation;

§VIII B and Appendix A still contain obsolete 0.5–0.6-pp statements after Table XI claims to supersede them with 0.9 pp.

The exact membership calculation must replace the approximate one everywhere. The manuscript must then define one primary estimand, one sign convention, one void count, one control count, and one interval consistently in the title, abstract, tables, discussion, and conclusions.

5. MAJOR — Three of the five “primary” estimators are not valid common estimators of the same void-membership quantity

The V2-REVOLVER and V2-VIDE “sphere-PIS” analyses classify galaxies using spheres centered on the watershed void centers with radius equal to the catalog effective radius. An effective radius is the radius of a volume-equivalent sphere; it is not the boundary of an irregular watershed void. The manuscript itself describes these as author-constructed approximations and reports materially different counts for the native GALZONE memberships.

The official GALZONE memberships should be used for the V2 analyses. The effective-radius sphere approximations should not be treated as primary environmental definitions or as independent validations.

Bonferroni correction does not require independent tests, so correlation among the five rows is not the central issue. The problem is that these rows do not estimate one common, well-defined estimand:

VoidFinder hole-union membership;

VoidFinder maximal-sphere membership;

two irregular watershed memberships approximated by effective spheres;

two catalog-native GALZONE memberships;

and different non-void complements and footprints.

A “uniform Bonferroni-5 null” across such heterogeneous quantities is a statement that none of five tests rejected zero. It is not a single physical upper bound applying to “any void/non-void split.” The primary family should contain only valid, catalog-native definitions, with the exact target population and control population stated separately for each. 

g_P5

6. MAJOR — The 0.9-pp “effective 2σ systematic envelope” is not a statistically defined confidence bound

Table XI combines, in quadrature:

a two-sided approximately 95% counting interval;

maxima observed under alternative membership definitions;

a shift between distinct void geometries;

a shift between sphere-PIS and GALZONE estimands;

a footprint-induced change in the control population;

a confidence-threshold sample change;

and a match-radius sample change.

These quantities are neither on a common 1σ scale nor demonstrated to be independent, Gaussian nuisance parameters. Several are strongly overlapping manifestations of membership definition. Others change the estimand rather than perturbing a fixed estimator. Root-sum-squaring them therefore produces no known coverage probability. Calling the result an “honest effective 2σ” bound and saying that it “disfavors” model amplitudes above 0.9 pp is unjustified.

The budget also omits the most consequential unresolved effects:

inclusion of edge voids;

residual selection-function mismatch;

differential classifier confusion;

spatially correlated classifier errors;

clustering/cosmic variance;

uncertainty from choosing the analysis family post hoc.

The RSD contribution is also not estimated correctly. The Monte Carlo adds extra Gaussian radial noise to galaxies that are already in redshift space while keeping the published void centers and radii fixed. This is an added-smearing stress test, not a reconstruction of true real-space membership and not an uncertainty distribution for RSD. The extrapolation that a >0.5-pp shift would require “1.3 times” the observed reassignment is unsupported, because the response need not be linear and random symmetric perturbations do not model coherent anisotropic deformation. 

g_P5

Two defensible alternatives are available:

present the variant results separately as descriptive sensitivity analyses, without assigning a confidence level; or

construct a generative nuisance model, spatial bootstrap, or mock-catalog ensemble from which a calibrated interval with demonstrated coverage can be obtained.

7. MAJOR — The quoted binomial errors assume independent galaxies and do not account for void-level or spatial covariance

The primary confidence intervals use a two-proportion binomial standard error with individual galaxies as independent Bernoulli observations. Galaxies are clustered within the same voids, survey regions, imaging conditions, and large-scale structures. Classifier residuals may also be spatially correlated. The relevant effective number of independent units can therefore be substantially smaller than the raw galaxy count.

The HEALPix diagnostics do not replace a covariance estimate for the primary contrast, and galaxy-level label shuffling destroys rather than preserves any local correlation. Stratification only by imaging leg and target program is insufficient to establish exchangeability.

The primary uncertainty should be recomputed using at least two of the following:

a bootstrap over VoidFinder void IDs, with an appropriate construction for the non-void sample;

a spatial block bootstrap or delete-one-region jackknife;

a cluster-robust logistic model;

mocks carrying survey geometry and classifier-systematic templates;

matched-set permutation within redshift, imaging, and morphology strata.

For a claimed sub-percent bound, this is not optional.

8. MAJOR — The canonical T-Web calculation is not a credible reconstruction of cosmic-web environment

The canonical T-Web field is built from an unweighted galaxy-density field with a single global mean, no DESI random catalog, a non-periodic survey embedded in an FFT cube, and a smoothing scale R
s
	​

=25h
−1
Mpc on cells of size 25.9h
−1
Mpc. Thus even the nominal smoothing scale is slightly smaller than one cell, while second derivatives and tidal eigenvalues are being estimated.

More decisively, §IX A reports that a randoms-weighted rebuild:

changes the void volume fraction by a factor of approximately 23;

leaves only 44% of common-mask cells in the same class;

leaves only 26.6% of matched galaxies in the same class.

That is not a modest robustness variation. It demonstrates that the canonical labels are primarily survey-selection/window labels rather than stable cosmic-web labels. A chirality null surviving a nearly arbitrary repartition of galaxies is not validation of the original environmental classification, especially when the label fraction is already close to a global constant.

Because this path is nominally secondary, the clean remedy is to remove most of it. Otherwise, the T-Web must be rebuilt using the appropriate randoms and selection weights for the actual tracer samples, a defensible window treatment, and a grid with several cells across the smoothing scale. The weighted reconstruction—not the invalid canonical reconstruction—would then need to be the reported T-Web result. 

g_P5

9. MAJOR — Post-hoc multiplicity is disclosed but not resolved, and non-rejection is repeatedly presented as evidence of independence

The manuscript deserves credit for explicitly stating that the primary path was selected post hoc. Nevertheless, calling five DESIVAST rows a “family-wise” primary analysis does not account for the preceding selection of that family from the much larger analysis tree. This matters particularly for upper bounds: choosing the environment definition or analysis family after examining many alternatives can select an artificially tight or reassuring interval even when no positive detection is claimed.

The paper itself recognizes this point but still alternates among:

an approximately 0.9-pp selected systematic envelope;

a 1.1-pp widest Bonferroni interval;

0.4–0.5-pp counting-only language;

stale 0.5–0.6-pp language;

and broad statements that the data “show environment independence.”

A non-significant p-value does not demonstrate independence. A calibrated equivalence interval can support a bounded-effect statement, but the manuscript does not currently provide one after systematics and analysis selection. The DR1 result should be presented as an exploratory set of effect estimates and intervals. “Exclusion,” “disfavors,” and general “environment-independence” language should be removed unless a valid equivalence analysis is supplied.

The conclusion must also be limited to the measured binary contrast. A void-versus-aggregate-nonvoid null cannot exclude compensating or heterogeneous effects in walls, filaments, and clusters. 

g_P5

10. MAJOR — The central chirality labels remain dependent on a companion manuscript that is not bibliographically or editorially resolved

The environmental analysis consumes the Paper IV per-galaxy labels. The current manuscript contains a placeholder arXiv identifier, a pending archival DOI, and repeated statements that acceptance should be conditional on Paper IV. The classifier summary in Appendix A cannot substitute for review of the training splits, confusion matrices, calibration, QC flags, image-orientation conventions, and released model.

Before this manuscript can be accepted, the referee must have access to:

the final Paper IV manuscript;

the exact frozen catalog version used here;

hashes or immutable identifiers for the labels and weights;

the full environment-relevant validation information;

and a synchronized revision if Paper IV labels change.

The manuscript itself acknowledges this dependency. That acknowledgment is appropriate, but it does not eliminate the dependency.

11. MAJOR — Appendix B and the associated bounce/inflation interpretation are not theoretically defensible

Appendix B introduces an operator involving a late-time galaxy angular-momentum direction and a density gradient, while explicitly admitting that the expression is neither covariant nor derived from the cited parity-violating gravity literature. No dimensions for the coupling are established, no response model connects the operator to projected galaxy handedness, and no transfer function connects it to the DESIVAST contrast. The subsequent numerical statement involving g
ϕ
	​

∇ϕ/H
0
	​

 is therefore not a constraint.

This appendix should be removed. So should statements that the result constrains a “bounce-chirality coupling class” unless an actual model supplies a calculated prediction for this observable. The manuscript states that neither bounce nor inflation models currently predict the tested effect; accordingly, the data do not discriminate between them.

An empirical catalog-level null may still be scientifically useful, but it should be presented as such. The speculative operator does not provide the theoretical foundation needed to turn the analysis into a fundamental-physics constraint and currently weakens the case for publication in PRD. 

g_P5

Minor concerns
12. MINOR — Figure 6 is internally inconsistent and appears mislabeled

Figure 6(a) is labeled “maximal voids per pixel,” with a displayed range of 50–734 over 3,303 occupied pixels. This is incompatible with the manuscript’s total of only 3,765 maximal voids and with Figure 8, which shows the plausible 1–20 range over 885 occupied pixels. Figure 6(a) is likely a map of galaxy counts or another quantity. Its caption discusses only the chirality panel and does not explain panel (a).

Figure 9 also titles the T-Web panel with n=791,635, while the displayed class counts sum to 812,793. Every figure and caption should be regenerated directly from the final declared parent sample.

13. MINOR — The manuscript misuses “minimum detectable effect”

The approximately 4.8-pp quantity for the n=428 T-Web void sample is a two-sided approximately 95% binomial half-width. A minimum detectable effect requires a specified significance level, desired power, test statistic, and alternative. The text should either provide an actual power calculation or call this quantity a confidence-interval/counting-error scale.

14. MINOR — Chance-coincidence contamination in the angular match should be measured directly

The shared astrometric provenance and very small median separation make the 1-arcsec matching choice plausible. Nevertheless, a match-radius sweep does not estimate false-match contamination. A shifted-coordinate or randomized-sky match should be reported, particularly for the tail and for the 2–5-arcsec sensitivity samples.

15. MINOR — The manuscript is excessively long and repetitive

The paper repeatedly restates the primary/secondary designation, the monopole caveat, the RSD caveat, and the same numerical results. Several paragraphs read as responses to earlier referee objections rather than as a coherent scientific narrative. The invalid canonical T-Web material, speculative EFT appendix, repeated “reader’s guides,” and detailed artifact bookkeeping should be removed or moved to supplemental material.

A focused manuscript would contain:

catalog and classifier validation;

exact interior-DESIVAST membership;

matched primary analysis;

calibrated uncertainty;

a concise set of robustness tests;

limitations and data release.

16. MINOR — Statistical presentation should prioritize effect estimates rather than numerous deviations from one-half

The many σ
fromhalf
	​

 values are largely projections of the known catalog monopole and are repeatedly explained as non-comparable. Their prominence nevertheless invites misinterpretation—for example, the repeated description of the cluster row as a “−4.7σ signal.” The main tables should emphasize:

Δf
CW
	​

;

confidence intervals;

adjusted contrasts;

omnibus association tests;

and spatially robust uncertainties.

The one-sample deviations from 0.5 can be moved to supplemental diagnostics.

Recommendation

The observed raw fractions are consistent with no difference, and the central null may survive a corrected analysis. But the present paper does not establish that the galaxies were assigned to reliable interior voids, that the control is comparable, that classifier errors are environment independent, or that the quoted sub-percent bound has calibrated coverage. The necessary corrections require a new primary analysis and substantial restructuring.

MAJOR REVISIONS
