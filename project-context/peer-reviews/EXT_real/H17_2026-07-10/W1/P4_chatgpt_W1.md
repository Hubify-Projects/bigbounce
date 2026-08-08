(1) VERDICT: REJECT

(2) ISSUES:

[MAJOR] Abstract, Secs. III B and VI B, and Appendix D(g)—the claimed z≃−7.6 disfavoring of a 1.7% cosmological dipole is inconsistent with the manuscript’s own classifier-transfer model. The WLS fit compares the observed-label amplitude A
best
	​

=0.00455 directly with A
ref
	​

=0.017. Yet the paper adopts g=2a−1=0.398; a physical dipole of 0.017 would therefore yield only gA
ref
	​

≃0.00677 in the observed hard-label field. With σ
boot
	​

=0.00163, the discrepancy is then only about −1.36σ, not −7.6σ. If 0.017 is instead intended to denote Shamir’s pipeline-dependent measured output rather than a physical dipole, comparing it directly with this classifier’s output is not a cosmological exclusion. This error invalidates one of the two declared “primary” results. 

ext_P4_W1

[MAJOR] Sec. VI B and Table VIII—the injection–recovery calculation is not end-to-end and cannot establish the quoted physical sensitivity or falsification boundary. Signals are injected only after classification, not-spiral triage, and the p
eq
	​

>0.6 selection. Consequently, A
50
	​

 and A
95
	​

 characterize the already-observed hard-label map, not the underlying galaxy-chirality field. Under the paper’s own g=0.398, A
50
	​

=0.75% corresponds to a physical amplitude of about 1.88%, while A
95
	​

=1.0%−1.5% corresponds to approximately 2.5%–3.8%. This directly contradicts the claim that a genuine 1.7% physical dipole would be recovered with probability approaching unity. Image-level injection, or a validated spatially conditional three-class transfer function, is required.

[MAJOR] Sec. IV C—the primary pixel-permutation null is not a valid cosmological null for this survey and classifier. Randomly permuting A
p
	​

 across pixels destroys the strong relation between pixel variance, galaxy count, depth, imaging leg, morphology, and confidence. The per-galaxy label shuffle preserves pixel totals but still assumes spatial exchangeability of CW and CCW labels and erases precisely the survey-correlated classifier structure that is the dominant concern. These tests establish inconsistency with random relabeling, not unbiasedness with respect to a cosmological dipole. A binomial or multinomial spatial likelihood, or survey mocks preserving depth-, PSF-, morphology-, and confidence-dependent confusion, is needed.

[MAJOR] Secs. III B and IV C—the declared primary sample is post-selected and is not the “8.5 million galaxy” sample advertised in the title. The headline estimator uses 949,584 high-confidence spirals, about 30% of the classified spirals and about 11% of the parent catalog, while the unthresholded catalog gives a z≃4.0−4.3 dipole-like excess. The claimed preregistration of the 0.6 threshold is not independently established by an immutable timestamped analysis plan: there is no frozen tag, the repository is described as a live branch, and the manuscript’s rationale explicitly depends on where the observed confidence-cut transition occurs. The result must be presented as conditional on this selection, with selection uncertainty and any cut optimization accounted for.

[MAJOR] Appendix B(h), Table XIV, and Sec. VI B—the confusion analysis omits a dipole-biasing selection channel. The stratified analysis conditions on galaxies that the classifier retained as CW or CCW and then studies only CW↔CCW swaps. Spatially varying differential probabilities for true CW and true CCW galaxies to be assigned “not spiral” also bias the CW fraction among retained objects. The 5,030 confident GZ1 spirals assigned to “not spiral” are excluded rather than included in a full three-class transfer analysis. The binary formula g=s
CW
	​

+s
CCW
	​

−1 is therefore insufficient unless chirality-neutral triage is demonstrated in every relevant sky/depth/confidence stratum.

[MAJOR] Appendix B(h)—the external validation does not constrain spatial differential errors tightly enough for a sub-percent measurement. The quoted confidence intervals permit differential error asymmetries of roughly 0.6 percentage points in the science-cut sample and up to about 1.4 percentage points in an imaging leg, comparable to or larger than the claimed dipole sensitivity. A two-leg declination split also cannot exclude RA-dependent or smaller-scale differential errors. The validation therefore does not justify a cosmological bound at the stated precision.

[MAJOR] Appendix D(g) and Fig. 10—the block-bootstrap “z≃−7.6” is not a calibrated test of A
ref
	​

. The plotted distribution is a bootstrap distribution centered on the observed data, not a sampling distribution generated under a 1.7% dipole. The fitted amplitude is a positive-definite norm of three correlated coefficients, so subtracting A
ref
	​

 and dividing by a bootstrap standard deviation does not produce a normally distributed test statistic. The direction is also not profiled or marginalized under the reference hypothesis. A likelihood-ratio construction or signal-injection test under each amplitude and direction is required.

[MAJOR] Appendix D(g)—the WLS fit cannot serve as a second primary cosmological estimator. It uses the full, low-confidence-contaminated catalog that the manuscript itself shows has a significant systematic dipole, whereas the first primary estimator uses only p
eq
	​

>0.6. Its nine-template design contains imaging-leg fractions and density terms but not the full depth, PSF, extinction, morphology, and conditional-classifier-response basis later invoked to explain the residual. Moreover, A
best
	​

/σ
boot
	​

≃2.8 relative to zero is never given a properly calibrated null probability. This fit is a diagnostic on a systematics-dominated sample, not independent confirmation of a null.

[MAJOR] Secs. VI B and VII—the recovery threshold is repeatedly used as though it were an exclusion limit. A 95%-detection-efficiency amplitude is not a confidence upper limit on the signal conditional on the observed data. It cannot establish that amplitudes above A
95
	​

 are excluded, nor that a future result above A
95
	​

 “falsifies” the present measurement. The authors must invert a family of tests or construct a likelihood/posterior for amplitude and direction, including nuisance uncertainty and axis-dependent sensitivity.

[MAJOR] Sec. IV C, Table V, and the Conclusions—the harmonic-channel significance reporting is statistically misleading. For the apodized ℓ=1 result, the empirical rank p=6.0×10
−4
 corresponds to about 3.2 Gaussian standard deviations one-sided, not 7.3. The manuscript acknowledges heavy tails but nevertheless repeatedly advertises “+7.28σ.” Likewise, the “canonical” values +3.64σ and +7.93σ arise from altered field, subtraction, coupling, and null conventions; increasing the Monte Carlo count alone cannot explain such a shift. One fixed estimator and an empirically calibrated p-value should be reported.

[MAJOR] Sec. VII and Fig. 9—the harmonic injection completeness is calibrated against an uncalibrated moment-z threshold. Because the low-ℓ null is explicitly heavy-tailed, “z≥3” does not correspond to a fixed false-positive probability. Recovery should instead be defined using an empirical critical value from the null distribution, with the same field and estimator convention used for the data.

[MAJOR] Sec. IV D—the unresolved approximately 47% harmonic residual cannot be declared irrelevant merely because its amplitude lies below A
50
	​

. A systematic below a detection-efficiency threshold can still bias an estimator, broaden an interval, or partially cancel a cosmological dipole. The claim that survey systematics necessarily add low-ℓ power and therefore bias only away from null is false for a vector dipole: an unknown systematic vector can align or anti-align with the signal. A simultaneous nuisance model is required before making exclusion statements.

[MAJOR] Sec. IV B and Sec. IV D—the “99.32% monopole–mask leakage reproduction” is overinterpreted. The calculation uses an uncentered field containing a nonzero constant on a cut sky; obtaining low-ℓ pseudo-power from the mask transform of that constant is expected by construction. It does not establish the origin of the global 9.5-standard-deviation monopole, does not explain the post-subtraction residual, and cannot be generalized to prior real-space Ganalyzer claims. The manuscript should present this as a bookkeeping demonstration of pseudo-C
ℓ
	​

 mode mixing, not as evidence against other dipole measurements.

[MAJOR] Sec. III D and Appendices B and E—flip equivariance is conflated with unbiased chirality classification. The Z
2
	​

 averaging guarantees covariance under horizontal reflection, but it does not guarantee rotational invariance, spatially uniform confusion, or unbiased hard argmax labels. A reported 21.4% change in argmax labels between Z
2
	​

 and D
4
	​

 processing is substantial because hard labels are the actual science observable. Production D
4
	​

 averaging, or at least a full-sample and high-confidence spatial audit of rotational instability, is required.

[MAJOR] Data Availability and the preregistration claims—the analysis is not yet reproducible to publication standard. The manuscript states that the archival DOI, frozen tag, and exact commit hashes “will” be supplied, while current references resolve against a mutable live main branch. These materials must exist during review, including immutable versions of the catalog, model, scripts, null arrays, masks, and all provenance artifacts. A mutable commit history is not a preregistration record.

[MINOR] Appendix B(g)—the stated ECE lower bounds are not valid as computed. The catalog-wide mean confidence of 0.951 is compared with accuracy on a distinct GZ1 cross-match sample. Jensen’s inequality gives the proposed lower bound only when confidence and correctness are averaged over the same population. Calibration must be recomputed on the matched sample using explicit reliability bins.

[MINOR] Appendix C—the statement that Bonferroni correction assumes independent tests is incorrect. Bonferroni controls the family-wise error rate under arbitrary dependence. Any disagreement between the Bonferroni estimate and the Monte Carlo max-statistic must instead be traced to the local p-value calibration, non-Gaussian tails, or the use of an approximate Gaussian conversion.

[MINOR] Sec. VI C—the links to cosmic birefringence and gravitational Chern–Simons gravity are too speculative. No transfer function from those sectors to projected spiral-arm chirality is derived, and the statement that such mechanisms would generically produce or align a galaxy-morphology dipole is unsupported. These claims should be removed or clearly identified as conjecture.

[MINOR] Presentation throughout—the manuscript is excessively repetitive and obscures the statistical logic. It repeatedly calls noncommensurable moment ratios “σ,” describes correlated analyses of the same catalog as “independent,” and restates caveats many times without resolving them. The revised paper should use one primary estimator, one calibrated significance convention, a formal interval on amplitude, and a title that states the actual 949,584-object primary sample.

(3) No—the manuscript supports only a conditional non-detection in a post-selected hard-label catalog, not the claimed cosmological null or the stated exclusion of a 1.7% physical dipole.
