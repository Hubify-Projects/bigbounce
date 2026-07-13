(1) VERDICT: REJECT

(2) ISSUES:

[MAJOR] Abstract; Secs. II and VI B; Tables VIII and XV — the stated physical sensitivity is inconsistent with the manuscript’s own classifier transfer function. The injection–recovery experiment injects a dipole into the already classified hard-label field; it does not pass the signal through image classification, the not spiral decision, or the p
eq
	​

>0.6 selection. Under the manuscript’s own conservative g
eff
	​

=0.398, a true A=1.7% dipole would appear with A
obs
	​

≃0.68%, below the quoted A
50
	​

=0.75% and well below A
95
	​

>1.0%. The corresponding physical A
95
	​

 would be roughly 2.5%−3.8%, not sub-percent. The all-image mirror test verifies algebraic flip-equivariance, not recovery of a weak, sky-dependent population signal. Consequently, the claims that a genuine Shamir-scale dipole “would have been detected” and is disfavored at z≃−7.6 are unsupported. 

ext_P4_M19

[MAJOR] Sec. IV C — the primary p
eq
	​

>0.6 sample is outcome-dependent and cannot support a catalog-wide null. The reported significance changes from z≃4.0−4.3 at cuts 0−0.5 to z=0.41 at 0.6, exactly where the primary threshold is placed. A commit containing the cut, without an externally timestamped protocol, frozen release, or blinded outcome, is not a convincing preregistration. Moreover, the cut discards about 70% of classified spirals. The manuscript has not demonstrated that a physical dipole must be independent of confidence, magnitude, redshift, morphology, or survey depth, so a null in this selected subset cannot be generalized to the parent population.

[MAJOR] Sec. II B and Appendix B — external classifier validation is inadequate for the claimed precision. Two thirds of the training labels are CE-ResNet pseudo-labels, while the genuinely independent GZ1 comparison gives only 69.91% chirality accuracy and κ=0.40. The GZ1-human-only dipole test contains only 4.6×10
4
 objects and, by the manuscript’s own estimate, has A
95
	​

∼4.5%−6.8%; it therefore cannot validate the sub-percent behavior of the headline sample. A representative, spatially stratified, independently labeled validation set is required.

[MAJOR] Appendix B, Tables XIII–XIV — the error model incorrectly omits three-class selection effects. The claim that only CW↔CCW error asymmetry can bias A
p
	​

 is false. Differential CW/CCW rejection into not spiral, asymmetric contamination of the chirality classes by true nonspirals, and chirality-dependent passage through the confidence cut all alter the numerator and denominator of A
p
	​

. Table XIII shows low CW/CCW precision, about 0.53, and asymmetric nonspiral leakage into CW and CCW; this is especially consequential because nonspirals constitute about 62% of the parent catalog. Table XIV conditions on true GZ1 spirals and removes objects classified as nonspiral, so it cannot test these channels. A full spatially conditioned 3×3 confusion-and-selection model must be propagated.

[MAJOR] Sec. IV C and Sec. VI B — the permutation nulls do not provide the required covariance model. Permuting pixel asymmetries assumes exchangeability despite large variations in N
spiral
	​

(p), morphology, depth, and classification reliability. The per-galaxy shuffle preserves counts but erases spatially coherent classification errors and physical spin correlations. The manuscript’s own block-bootstrap analysis finds a 14.7-fold increase over the naive WLS uncertainty, demonstrating that spatial coherence can be large, yet no analogous block/mocked-sky covariance is used for the primary estimator or its injection–recovery thresholds. The quoted p-value and especially A
50
	​

/A
95
	​

 therefore lack a validated sampling distribution.

[MAJOR] Sec. III B and Appendix D, Table XV/Fig. 10 — z≃−7.6 is not a valid primary exclusion statistic. The block bootstrap is centered on the observed field, not generated under A
ref
	​

=0.017; the tested quantity is a positive-definite three-vector amplitude with unknown direction; and the nuisance templates and dipole components are correlated on the cut sky. A scalar (A
best
	​

−A
ref
	​

)/σ
boot
	​

 is not a calibrated test of the composite hypothesis ∣A∣=0.017. The authors explicitly acknowledge this, yet still designate the result as a primary cosmological estimator. A profile likelihood or signal-injection test under A
ref
	​

, using the same science sample and complete nuisance model, is required.

[MAJOR] Secs. IV C–D and Appendix D — the statistically significant anisotropy in the unthresholded catalog is not resolved. The full sample gives a real-space excess near 4.2σ, while the harmonic and hemisphere channels reject their respective random-label nulls; only approximately 53% of the harmonic residual amplitude is forward-modeled, leaving about 47% explicitly unexplained. Declaring these channels “diagnostic” does not make the discrepancy disappear. Nor does the fact that a residual lies below A
50
	​

 identify it as systematic: below-threshold means the analysis lacks reliable discrimination. The null claim requires a joint reconciliation of the selected and unselected samples.

[MAJOR] Sec. VI A and Appendix D — the argument that unknown systematics can only add power or dilute a signal is incorrect. A spatially coherent differential classification or selection bias can anti-align with a real dipole and partially cancel it. Likewise, regression against survey templates can absorb a genuine sky mode when the templates and dipole basis are correlated on a restricted footprint. The claim that the resulting bounds are automatically conservative is therefore unjustified; nuisance effects must be marginalized with unrestricted signs and covariances.

[MAJOR] Sec. III D and Appendix B — flip-equivariance is not sufficient rotational control. Chirality is invariant under arbitrary in-plane rotations, but production inference averages only the identity and one reflection. The limited D4 test reports 21.4% argmax changes, which is substantial, and stability of the global mean probability does not bound a spatial dipole. Rotation-dependent network behavior can couple to survey PSF orientation, image resampling, and the fixed sky orientation of the cutouts. The science analysis should be rerun with a genuinely rotation-equivariant model or full D4 inference.

[MAJOR] Secs. V and VI C — comparisons with previous work and parity-violating theories are overinterpreted. The Shamir analyses use different selections, redshift distributions, footprints, and classifiers, and the manuscript has not established a common physical transfer function. The claimed factor-of-3.7−8.8 tension is therefore not a robust physical comparison. Similarly, no transfer function from cosmic birefringence or Chern–Simons gravity to projected galaxy morphology is derived, so the data cannot presently constrain those sectors. These claims should be removed or replaced by a matched-pipeline analysis and an explicit theoretical mapping.

[MAJOR] Data Availability and Appendix B — the reproducibility package is not submission-ready. The manuscript refers to a future Zenodo deposit and a live main branch rather than an immutable DOI-tagged archive. In addition, 2.9% of catalog rows have reconstructed probabilities outside [0,1], indicating a raw/equivariant pass mismatch. Flagging these rows is not an adequate substitute for regenerating a self-consistent catalog and demonstrating row-level alignment, checksums, and exact reproducibility before publication.

[MINOR] Title and Abstract — the advertised sample size is misleading. The parent catalog contains 8.47 million objects, but only 3.20 million are classified as spirals and the primary measurement uses 949,584 high-confidence spirals. The title and headline statements should identify the actual science sample.

[MINOR] Sec. III A and Tables V–VI — “σ” is used misleadingly for moment ratios. For example, moment values around 7−8 correspond to empirical rank probabilities of 3−6×10
−4
, not Gaussian 7−8σ significances; the +3.64 moment value corresponds to p=0.030. Results should be reported primarily by empirical p-value, with Gaussian-equivalent significance only when appropriate.

[MINOR] Throughout — the manuscript is excessively repetitive and uses inconsistent estimator terminology. “Canonical mask” alternates between N
spiral
	​

≥10 and the N
all
	​

≥1 footprint, while several +3.64, +7.28, and +7.93 results use different fields, subtractions, weights, and nulls. The analysis should be reduced to one clearly specified primary estimator, with secondary diagnostics presented once and with unambiguous notation.

(3) The central claim is not supported: the manuscript establishes at most a null in one post-selected observed-label field, not a null physical galaxy-chirality dipole at the claimed sub-percent sensitivity.
