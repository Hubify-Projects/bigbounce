(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:

[MAJOR] Section III B / Section IV C, definition of the primary sample: the p
eq
	​

>0.6 cut is not convincingly preregistered or independent of the outcome. A Git commit that simultaneously defines the estimator and the cut is not a prospective registration, and the manuscript explicitly motivates 0.6 as the threshold at which the z≃4.0−4.3 signal disappears while discarding roughly 70% of classified spirals. The primary inference therefore has a serious post-selection problem; the authors must either demonstrate a genuinely frozen, pre-unblinding protocol or account statistically for the full confidence-cut scan and validate the cut on independent data. 

ext_P4_M14

[MAJOR] Abstract / Sections V A and VI B / Conclusions, detectability of a Shamir-scale physical dipole: the claim that a genuine 1.7% dipole would have been detected contradicts the manuscript’s own classifier-dilution estimate g≃0.398. A true 1.7% signal would map to only ≃0.68% in the observed hard-label field, below the stated A
50
	​

≃0.75% and well below A
95
	​

∈(1.0%,1.5%]. The paper may compare 1.7% directly only if it is explicitly an observed-label amplitude for this classifier, not an underlying physical chirality amplitude.

[MAJOR] Sections IV C, IV D, and VI B, interpretation of injection–recovery: A
50
	​

 and A
95
	​

 are detection-efficiency thresholds, not confidence limits on the measured dipole. Nevertheless, the manuscript repeatedly treats them as ceilings, bounds on an inherited signal, and criteria for dismissing the unexplained harmonic residual. A non-detection with p=0.31 establishes only failure to reject the null; the paper needs a likelihood or posterior for the three dipole components and a confidence/credible upper limit with stated coverage, including orientation dependence and nuisance marginalization.

[MAJOR] Appendix D, “z≃−7.6” block-bootstrap template disfavor: computing (A
best
	​

−A
ref
	​

)/σ
boot
	​

 from a bootstrap distribution centered on the observed estimate is not a calibrated test under A
ref
	​

=0.017. The amplitude is a positive-definite norm, its direction is unspecified, the full-sample field is known to contain coherent systematics, and 7
∘
 bootstrap blocks do not demonstrably capture the covariance of an ℓ=1 mode. This quantity cannot be designated a primary cosmological exclusion without signal-injected simulations under A
ref
	​

, or a proper spatial likelihood whose coverage is validated.

[MAJOR] Section IV C, primary null distribution and estimator: randomly permuting pixel asymmetries assumes exchangeable pixels, whereas their variances depend strongly on N
spiral
	​

(p), depth, confidence selection, morphology, and survey leg. Uniform-pixel least squares likewise ignores this heteroscedasticity. The per-galaxy shuffle is a better conditional check but still does not propagate classifier uncertainty, spatially varying confusion, or intrinsic spin correlations. The primary result should be obtained from an object-level or per-pixel binomial likelihood with the survey selection function and spatial covariance included.

[MAJOR] Sections II and VI A / Appendix B, classifier validation: 66.5% of the training labels are pseudo-labels, the externally measured chirality accuracy is only 69.91%, the probabilities are strongly miscalibrated, and the catalog retains a 9.5σ global handedness offset. The GZ1 confusion analysis is restricted to a nonrepresentative, high-confidence overlap and its science-cut differential-error interval is still of order 0.6 percentage points, comparable to the claimed sub-percent sensitivity. A two-leg split does not exclude RA-, depth-, PSF-, or morphology-dependent differential errors, and a single global dilution factor g is not an adequate physical transfer model.

[MAJOR] Section VI A, model-independent cross-check: the GZ1-human-only test has an admitted sensitivity of A
50
	​

∼3.4% and A
95
	​

∼4.5−6.8%. It therefore cannot validate the sub-percent null claimed for the learned catalog or exclude pseudo-label-inherited structure at the relevant amplitude; it is only a coarse consistency check and should not be presented as establishing independence of the headline result.

[MAJOR] Sections IV D and Appendix D, treatment of the harmonic residual: the data contain highly significant low-ℓ structure under several stated nulls, while approximately 47% of the ℓ=1 amplitude remains unexplained. Declaring this channel “diagnostic” does not make it statistically irrelevant because it is built from the same labels and footprint. The cited discriminators are not decisive: splitting into quality quartiles greatly reduces sensitivity, ℓ=2>ℓ=1 significance is not by itself incompatible with a cut-sky dipole, and the depth cross-spectrum is based on only 200 null realizations. A joint signal-plus-systematics model is required before attributing the residual cosmologically or instrumentally.

[MAJOR] Section IV C, full-sample result: the unthresholded catalog gives a z≃4.2−4.4 real-space dipole, and the manuscript’s own full-sample injections place its 0.57% amplitude between the corresponding A
50
	​

 and A
95
	​

. Calling this result a systematic solely because it disappears after the selected confidence cut is circular unless the depth-dependent misclassification mechanism is independently measured and shown quantitatively to reproduce the dipole vector.

[MAJOR] Section VI B, claimed image-level “end-to-end injection”: mirroring every image and recovering T
eq
	​

≃1 principally verifies the algebraic equivariance imposed by Eq. (2); it does not inject a sky-dependent physical chirality dipole through the image distribution, not-spiral triage, confidence cut, and spatially varying confusion matrix. A valid end-to-end test would alter a controlled, direction-dependent subset of images or use realistic simulated galaxies with known chirality, then rerun the complete catalog construction and estimator.

[MAJOR] Section III A / Table V / Appendix A, nonunique “canonical” harmonic statistic: the manuscript reports +3.64σ and +7.93σ for nominally canonical unapodized ℓ=1 analyses, but with different fields, monopole subtractions, weights, and null conventions, and then declares them noncomparable. The factor-of-two field rescaling cannot itself change z; the change is therefore driven by substantive analysis choices. One frozen field definition, mask, weighting, subtraction, and null must be selected before interpreting the harmonic result.

[MAJOR] Sections V and VII, comparison with Shamir: the samples differ in footprint, redshift and morphology selection, classifier transfer, contamination, and estimator, and no matched-footprint Ganalyzer analysis is performed. The manuscript acknowledges this but still advertises a factor 3.7−8.8 tension and near-certain recovery of the lower 1.7% value. Those statements should be removed or limited to a clearly labeled observed-label, pipeline-specific comparison after correcting the dilution inconsistency.

[MAJOR] Section VI A, amplitude units: the statement that A
95
	​

≲1.5% is in “f
CW
	​

 units” and corresponds to ≲3×10
−2
 in A
p
	​

 units conflicts with Eq. (3), Table VIII, and Table XV, where A
95
	​

 is already the full-amplitude A=A
p
	​

. This factor-of-two inconsistency directly affects the claimed inherited-signal ceiling and must be corrected throughout.

[MINOR] Section VI C, theoretical interpretation: without a redshift-resolved sample or a transfer function from primordial parity-violating physics to projected arm winding, the manuscript cannot claim constraints on cosmic birefringence, Chern–Simons gravity, or other primordial sectors. These paragraphs should be framed strictly as motivation, not as constraints.

[MINOR] Section II, survey selection: the exact construction of the third-party parent catalog, duplicate rejection, coordinate-match multiplicities, star/artifact contamination, and the magnitude, size, morphology, and redshift distributions of both the full and p
eq
	​

>0.6 samples are insufficiently documented. These distributions are needed to assess domain shift and the representativeness of the selected 30%.

[MINOR] Data Availability: a live main branch, future DOI language, and missing final commit hashes do not constitute an immutable reproducibility record. The submitted version must point to a frozen archive containing the catalog, code, configuration, null arrays, and checksums used for every quoted result.

[MINOR] Presentation: the manuscript is highly repetitive, repeatedly restates the same caveats and GZ1 test, and embeds repository paths throughout the scientific narrative. It should be substantially shortened, with provenance details and artifact inventories moved to a supplement and one concise table defining each estimator, sample, null, and inferential meaning.

(3) No—the manuscript currently supports only a non-detection in a post-selected observed-label subset, not the broader physical chirality null or the claimed exclusion of a genuine 1.7% dipole.
