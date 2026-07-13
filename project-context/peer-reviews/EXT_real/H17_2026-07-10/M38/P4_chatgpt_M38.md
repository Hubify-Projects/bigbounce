(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:

[MAJOR] Abstract, Secs. V A and VI B—physical amplitude versus observed-label amplitude. The injection study inserts a dipole only after classification, triage, and the p
eq
	​

>0.6 selection, so A
50
	​

 and A
95
	​

 apply to the observed hard-label field, not to an underlying physical chirality dipole. Nevertheless, the manuscript compares Shamir’s 1.7% amplitude directly with these thresholds and states that such a physical signal would necessarily have been detected. Using the manuscript’s own conservative transfer factor g≃0.398, a 1.7% physical dipole would appear at only ≃0.68%, below the quoted A
50
	​

≃0.75%; the corresponding physical A
95
	​

 would be approximately 2.5–3.8%, before additional transfer uncertainty. If 1.7% is instead interpreted merely as the output amplitude of Shamir’s different classifier, no cross-pipeline z=−7.6 cosmological exclusion is justified. 

ext_P4_M38

[MAJOR] Sec. IV C—claimed pre-specification of the p
eq
	​

>0.6 primary sample. A source-code commit containing the cut is not an adequate pre-registration, particularly when the manuscript explicitly motivates 0.6 as the lowest threshold at which the observed z≃4 excess disappears and acknowledges that no frozen tag or independent pre-unblinding record exists. Because the unthresholded sample is significantly non-null, selection of the threshold is outcome-relevant; the confidence-cut sweep does not remove this selection issue. The primary result must either be demonstrated from an independently frozen/blinded analysis or be reported with the appropriate selection and multiplicity qualifications.

[MAJOR] Secs. IV C–D and Appendix D—unresolved conflict between the selected-sample null and the non-null full-catalog observables. The full catalog gives a 4.2–4.4σ real-space excess, multiple 7σ-level harmonic statistics, and a look-elsewhere-corrected hemisphere rejection, while approximately 47% of the harmonic residual amplitude remains unexplained. Confidence dependence, an ℓ=2>ℓ=1 pattern, and correlations with survey templates are suggestive of systematics but do not uniquely establish that interpretation; a real effect could depend on redshift, surface brightness, or morphology and therefore preferentially occupy the low-confidence population. Declaring these measurements “diagnostic” rather than “primary” does not statistically resolve them.

[MAJOR] Sec. IV C—validity of the permutation and label-shuffle nulls. Permuting pixel ratios is not exchangeable when their variances depend strongly on per-pixel galaxy counts, while global label shuffles erase spatially varying confusion rates and dependencies on imaging depth, PSF, morphology, redshift, and survey leg. Both procedures also remove any intrinsic short-range spin correlations that should contribute to the covariance of a large-scale dipole estimator. The per-galaxy shuffle is a useful code-level comparison, but it is not a sufficient cosmological null; a conditional randomization scheme or spatial likelihood that retains the relevant nuisance dependence is required.

[MAJOR] Sec. III D, Appendix B, and Sec. VI B—equivariance is being conflated with unbiased physical classification. Equation (2), the unit flip-swap correlation, and the reported T
eq
	​

=0.9997 mirror recovery follow algebraically from the TTA construction and therefore cannot validate the response to a physical chirality signal. They do not probe image-dependent selection, the not-spiral decision, or spatially varying CW↔CCW errors. The 21.4% Z2-to-D4 argmax instability, the catalog-pass mismatch affecting 2.9% of rows, and the approximately 70% independent GZ1 chirality accuracy show that a survey-matched, spatially and morphologically conditioned confusion model is still needed.

[MAJOR] Secs. IV D and VI A–B—misuse of recovery thresholds as upper limits. The manuscript repeatedly states that A
50
	​

 and A
95
	​

 are detection-efficiency thresholds rather than confidence limits, but then uses them to assert that the unexplained residual or any inherited cosmological contribution “must” lie below those values. A 50% or 95% recovery probability is not an upper confidence bound on the amplitude present in the observed realization. A likelihood or confidence construction with demonstrated coverage is required before placing an upper limit or describing the residual’s cosmological content as bounded.

[MAJOR] Appendix D(g), Table XV, and Fig. 10—interpretation of the z≃−7.6 WLS statistic. The quoted number is obtained by subtracting a reference amplitude from the observed best-fit positive-definite amplitude and dividing by a block-bootstrap width centered on the observed data; it is not a null distribution generated under A
ref
	​

=0.017. It also includes optimization over dipole direction, an incompletely modeled spatial covariance, and nuisance templates that can absorb part of a true dipole on the cut sky. The authors acknowledge that it is uncalibrated, yet designate it a primary cosmological exclusion. The reference signal must be injected through the complete regression and selection pipeline, with the same nuisance fitting and test statistic, to obtain a valid rejection probability.

[MAJOR] Secs. VI A and Appendix D—claim that unmodeled bias makes the null conservative. A coherent systematic is a vector field and can either add to or cancel a cosmological dipole; it does not necessarily increase the fitted amplitude. Consequently, the statement that inherited or survey-correlated structure can only bias the result away from zero, except for uniform dilution, is false. Given the explicitly unexplained residual and incomplete nuisance basis, cancellation of a real dipole has not been excluded.

[MAJOR] Secs. VI A–B and Tables VIII/XV—amplitude-unit and transfer-function inconsistencies. Section VI A describes A
95
	​

≲1.5% as an f
CW
	​

-unit quantity corresponding to A
p
	​

≲3%, whereas elsewhere A
95
	​

, the injected full amplitude A, and the A
p
	​

 dipole amplitude are stated to be numerically identical. The global g=0.398 transfer factor is also inconsistent with the much higher accuracy quoted for the selected science-cut GZ1 subset, demonstrating that the relevant transfer function has not been established for the actual primary sample. These inconsistencies directly affect the sensitivity and literature-comparison claims.

[MAJOR] Sec. IV C—absence of a proper dipole constraint. A null-result paper should report the fitted Cartesian dipole components and their full covariance, or an equivalent likelihood/posterior and a 68%/95% confidence region after nuisance marginalization. A positive-amplitude moment z, an empirical rank, and a direction stated to be unconstrained do not provide a statistically interpretable upper limit. An unbinned Bernoulli or hierarchical model would also avoid arbitrary dependence on HEALPix resolution, minimum pixel count, and uniform pixel weighting.

[MINOR] Data Availability and presentation. The claimed reproducibility package is still tied to a mutable live branch, with the immutable tag, checksums, and Zenodo DOI left as placeholders; these must exist and be independently reproducible before acceptance. The manuscript is also excessively repetitive and contains mutually inconsistent estimator descriptions, internal artifact paths, and referee-response-style defenses that should be consolidated into a substantially shorter main text and a clearly versioned supplement.

(3) No—the selected high-confidence hard-label catalog is consistent with a zero dipole, but the stronger central claim of a sub-percent cosmological null and exclusion of a 1.7% physical dipole is not supported.
