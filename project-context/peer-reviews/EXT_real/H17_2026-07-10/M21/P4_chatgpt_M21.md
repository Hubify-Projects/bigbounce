(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:

[MAJOR] Sections III B and IV C, primary-sample definition: the p
eq
	​

>0.6 cut is not demonstrably preregistered. A code commit made before the reported fit, without a frozen protocol or independent timestamp, does not establish that the cut was chosen before inspecting related outcomes; moreover, the manuscript explicitly motivates 0.6 as the point where the z≃4 excess disappears. The unthresholded 3.2×10
6
-spiral sample gives z≃4.2–4.4, whereas the headline result uses only 949,584 spirals. A blinded holdout, independent footprint, or explicit post-selection correction is required, and the title and abstract must clearly distinguish the 8.47-million parent catalog from the much smaller primary science sample. 

ext_P4_M21

[MAJOR] Abstract, Sections V and VI B, claim that a Shamir-scale physical dipole “would have been detected”: the injection tests act on the already-classified hard-label field and do not propagate a signal through the classifier, not-spiral triage, confidence cut, or spatially varying confusion matrix. Using the manuscript’s own transfer factor g=0.398, a true A=1.7% dipole would appear as only A
obs
	​

≃0.68%, below the quoted A
50
	​

≃0.75% and below A
95
	​

>1.0%. Thus the lower end of the claimed Shamir range would not be reliably detected under the paper’s own conservative mapping. A genuine end-to-end population-level injection, including selection and conditional misclassification, is needed.

[MAJOR] Appendix D, block-bootstrap claim z≃−7.6 against A
ref
	​

=0.017: this is not a valid exclusion statistic. The bootstrap distribution is centered on the observed estimate, not generated under the A
ref
	​

 hypothesis; the fitted amplitude is positive-definite; the alternative has an unspecified direction; and the comparison does not apply the classifier transfer function. With the manuscript’s own g=0.398, the expected observed amplitude from a true 1.7% dipole is approximately 0.0068, close to the reported 0.00455, not 7.6 standard deviations away. The claim requires a calibrated likelihood-ratio or simulation test under the alternative, with direction and nuisance parameters profiled or marginalized.

[MAJOR] Sections IV C, VI B, and VII, absence of a physical upper limit: A
50
	​

 and A
95
	​

 are detection-efficiency thresholds, not confidence limits, as the manuscript itself notes. They therefore cannot be used to state that the unexplained harmonic remainder is “bounded,” that it cannot affect the null conclusion, or that amplitudes below A
95
	​

 are excluded. A null-result paper must report a frequentist confidence interval or Bayesian posterior upper limit on the dipole vector and amplitude after classifier transfer, sample selection, and systematic uncertainties are included.

[MAJOR] Section IV C, primary estimator and null construction: uniformly weighted least squares on per-pixel ratios, followed by permutation of A
p
	​

 between pixels, assumes exchangeability despite large variations in N
spiral
	​

(p), depth, morphology, and classification uncertainty. The per-galaxy label shuffle preserves counts but still assumes spatially invariant label probabilities and misses coherent classifier errors. The primary analysis should use a binomial or per-galaxy likelihood with the monopole, dipole, survey covariates, misclassification matrix, and spatial covariance fitted jointly; spatial mocks or a validated block-resampling null should determine significance.

[MAJOR] Sections IV C–IV E and Appendix D, unresolved anisotropy in the same catalog: the full sample has a z≃4.2–4.4 real-space excess, the MASTER analyses give approximately 7–8σ moment residuals, and roughly 47% of the harmonic amplitude remains unexplained. Calling these channels “diagnostic” does not establish that they are noncosmological. Nor does being below a recovery threshold dispose of them. A joint, same-sample model comparison between cosmological dipole, survey-systematic, and mixed hypotheses is required before a definitive null can be claimed.

[MAJOR] Sections III A, IV C–IV D, Table V, and Conclusion item (c), mutually inconsistent canonical MASTER results: the manuscript reports +3.64σ with p
MC
	​

≃0.03 and +7.93σ with rank p≃3×10
−4
, alternately describing these as the same canonical field and as different conventions. Increasing the null ensemble from 500 to 10
4
 cannot by itself plausibly produce this change. The exact field normalization, mask, weighting, mean subtraction, coupling-matrix construction, binning, and randomization must be reconciled in one frozen implementation.

[MAJOR] Sections II, IV A, and Appendix B, classifier validation: 66.5% of training labels are CE-ResNet pseudo-labels; independent GZ1 chirality accuracy is only 69.91%; the network is strongly overconfident; the not-spiral class appears to rely on only 2,000 synthetic negatives; and 15.8% of classified spirals are empirically edge-on. These facts make selection and contamination central components of the cosmological inference, not secondary catalog caveats. Validation is needed on an independent, expert-labeled set spanning magnitude, size, redshift, morphology, imaging leg, depth, and PSF, with selection-conditioned three-class confusion matrices.

[MAJOR] Sections III D and VI B, equivariance evidence: flip-swap correlation 1.000 and the T
eq
	​

=0.9997 mirror recovery follow algebraically from the test-time averaging and are implementation checks, not evidence that chirality is correctly recognized. Conversely, the raw mirror-transfer rate T
raw
	​

=0.2303 and the 21.4% change of argmax labels under Z
2
	​

 versus D
4
	​

 averaging require substantial explanation. Non-tautological tests on independently labeled original/mirror pairs and explicit rotation- and sky-dependent error studies are necessary.

[MAJOR] Appendix B, Table XIV, spatially varying differential errors: the quoted 95% intervals permit approximately 0.6 percentage-point error asymmetry in the science-cut sample and approximately 1.4 percentage points in one imaging leg, comparable to or larger than the claimed sub-percent sensitivity and the measured 0.455%–0.695% residual amplitudes. A two-leg declination split cannot exclude right-ascension structure or gradients within a leg. The physical null requires a finer conditional confusion model or independent replication in a survey with different observing systematics.

[MAJOR] Section VI A, GZ1-human-only cross-check: the manuscript estimates this test’s own sensitivity as A
50
	​

≃3.4% and A
95
	​

≃4.5%–6.8%. It therefore cannot validate the sub-percent headline result or exclude the lower end of the 1.7%–4.0% comparison range. It may be retained as a low-power qualitative consistency check, but statements that it establishes the absence of pseudo-label-inherited dipole structure must be removed.

[MAJOR] Sections V, VI C, and VII, physical interpretation and comparison with prior work: the samples, redshift distributions, morphology cuts, footprints, classifiers, and estimators differ from those of Shamir, and no transfer function is derived from primordial parity-violating physics to projected galaxy morphology. Consequently, neither a likelihood-level tension with the previous measurements nor constraints on cosmic birefringence or Chern–Simons scenarios are established. These claims should be removed or replaced by a matched-footprint, matched-selection reanalysis and a quantitative theory transfer model.

[MAJOR] Data Availability and Appendix B, reproducibility and catalog integrity: the analysis points to a mutable live branch, while the DOI and immutable commit hashes remain placeholders. In addition, 2.9% of catalog rows—and 6.3% of the headline high-confidence sample—have mutually inconsistent raw and equivariant probability columns because they came from different inference passes. The catalog should be regenerated from one internally consistent pipeline, and the exact catalog, code, masks, null arrays, and provenance artifacts must be frozen with checksums before acceptance.

[MINOR] Sections VI A–VI B and Appendix A, units and terminology: the manuscript states in one place that A
95
	​

≲1.5% in f
CW
	​

 units corresponds to A
p
	​

≲3%, while elsewhere it correctly states that the full dipole amplitude is numerically identical to the A
p
	​

 amplitude. Likewise, “canonical mask” alternates between N
spiral
	​

≥10 and the N
all
	​

≥1 footprint. A single notation-and-estimator table should define every field, mask, amplitude convention, weight, and sample.

[MINOR] Sections IV D, VI B, and Appendices C–D, Monte Carlo precision and multiplicity: 100 injections per amplitude are insufficient for a stable 95%-recovery crossing, several systematic significances use only 50–200 realizations, and many cuts, masks, multipoles, directions, and template variants are examined. Confidence intervals on recovery probabilities, larger simulation ensembles, and either multiplicity control or explicit designation of exploratory tests are required.

[MINOR] Overall presentation: the manuscript repeatedly restates the estimator hierarchy, caveats, and systematics attribution, often in rebuttal-style language, while crucial distinctions remain obscured. It should be substantially shortened, with one primary analysis, one calibrated systematic model, one sensitivity or upper-limit section, and the implementation audit moved to supplementary material.

(3) No: the manuscript supports only that one data-selected high-confidence hard-label estimator is null-consistent, not the broader physical DESI chirality-dipole null at the claimed sub-percent sensitivity or the stated exclusion of Shamir-scale amplitudes.
