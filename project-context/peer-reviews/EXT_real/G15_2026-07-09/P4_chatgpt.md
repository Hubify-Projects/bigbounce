# P4 ChatGPT EXT review — G15 2026-07-09

- Paper: P4 v1.0.229 (34pp), g_P4.pdf
- Reviewer: ChatGPT Pro (Extended Thinking)
- URL: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a504a1d-37d8-83e8-9e27-ac8622819895
- Verdict: **MAJOR REVISIONS** (F14 baseline: MAJOR)

## Raw response

Referee report

Manuscript: A Null Chirality Dipole in 8.5 Million DESI Galaxies from Equivariant Deep Learning 

g_P4

Overall assessment

The catalog could become a valuable community product, and the manuscript contains several commendable practices: explicit disclosure of pseudo-label dependence, comparison of pixel-permutation and galaxy-label-shuffle nulls, confidence-threshold sweeps, mask/weight checks, and unusually detailed reporting of known failures. At the level of the selected hard-label field, the result p=0.31 for the high-confidence sample is a legitimate statement that this particular estimator finds no evidence for a dipole.

The central cosmological conclusions, however, are substantially stronger than the analysis supports. In particular, the paper does not provide a confidence interval or upper limit on a physical dipole; its injection tests do not propagate a signal through the classifier or spatially varying selection; the advertised z≃−18 template result mishandles classifier attenuation and may also contain a factor-of-two error in the reference amplitude; and the substantial harmonic residual remains only partially explained. These are not matters of presentation. They affect the abstract, title, principal results, comparison with previous work, and claimed falsification thresholds.

Major concerns
1. MAJOR — A detection-efficiency threshold is repeatedly used as though it were an upper bound

Sections IV C and VI B report a non-rejection, p=0.31, and power thresholds A
50
	​

 and A
95
	​

. The manuscript correctly states in several places that A
95
	​

 is not a frequentist confidence upper limit. Nevertheless, the abstract, Sec. IV D, Sec. VI A, and the conclusions repeatedly infer that an unresolved component is “bounded” because it is below A
95
	​

, or that it therefore “does not affect” the dipole constraints. 

g_P4

 

g_P4

That inference is invalid. A power statement,

P(detection∣A=A
95
	​

)=0.95,

does not imply

P(A<A
95
	​

∣non-detection)=0.95.

Indeed, signals below A
95
	​

 are precisely signals that the estimator can fail to detect. The same problem affects the proposed “ceiling” on pseudo-label-inherited structure and the assertion that the unexplained harmonic residual cannot contain a cosmological contribution.

For a null-result paper, the authors must provide a statistically calibrated constraint on the dipole vector or amplitude: for example, a likelihood or simulation-based Neyman construction with correct coverage, or a clearly specified posterior with nuisance parameters and priors. The positive-definite amplitude and unknown direction must be treated explicitly. Until such a constraint is supplied, the defensible conclusion is only “no evidence in this estimator,” not an upper bound or exclusion.

2. MAJOR — The injection-recovery study is not end-to-end and does not calibrate physical sensitivity

The paragraph “What the injection-recovery chain does and does not traverse” in Sec. VI B explicitly states that the injections are introduced into the already classified hard-label field. They do not pass through the images, ViT classifier, not spiral triage, confidence cut, or depth-, PSF-, morphology-, and imaging-leg-dependent confusion. 

g_P4

 

g_P4

This limitation is fundamental because those omitted stages are exactly where the manuscript finds its dominant systematics. A real physical dipole would first alter the distribution of true morphologies; it would then be transformed by a position-dependent selection and confusion operator. A single global dilution factor cannot represent this generally. Schematically,

A
obs
	​

(
n
^
)=b(
n
^
)+g(
n
^
)A
true
	​

(
n
^
),

where both the additive term b and response g may vary over the footprint. Such variation can attenuate, rotate, add to, or cancel a dipole. It is not guaranteed merely to dilute it.

The simulated backgrounds also appear to be independent binomial/label-shuffle realizations rather than realizations preserving the observed brick-, imaging-leg-, and low-ℓ-correlated residuals. Therefore the quoted A
50
	​

 and A
95
	​

 can be optimistic even as thresholds for the observed-label estimator.

A publication-grade sensitivity analysis requires one of the following:

Image-level injection followed by the entire production classifier, triage, confidence selection, map construction, and estimator; or

A validated spatially conditional confusion/selection model, calibrated by imaging leg, depth, PSF, magnitude, size, morphology, and preferably redshift, followed by forward simulations through the complete catalog construction.

Absent that work, every A
50
	​

, A
95
	​

, “falsification,” and comparison to a physical literature amplitude must be explicitly restricted to an artificial dipole inserted into this catalog’s observed hard labels.

3. MAJOR — The “3σ” and “5σ” recovery criteria are not calibrated significances

Section III A emphasizes that the moment-z statistic does not map to a Gaussian p-value. Table V demonstrates this dramatically: values described as z≃7−8 have empirical ranks of order 10
−4
−10
−3
, not Gaussian 7−8σ tail probabilities.

Despite this, Table VIII defines recovery through z
moment
	​

>3, and the abstract defines future falsification through a “5σ” moment-z. These are merely thresholds measured in null standard deviations; they are not conventional 3σ or 5σ false-alarm levels. With only N
MC,null
	​

=1000, a genuine one-sided 3σ tail would in any case contain only approximately one expected null realization, so it cannot be calibrated reliably by empirical rank.

The recovery curves must instead use a predeclared false-positive probability under the same null employed for the data, with enough simulations to resolve that probability or with a validated tail model. The false-positive rate should be verified explicitly. The abstract and conclusions must not use “3σ” or “5σ” terminology for an uncalibrated moment ratio.

4. MAJOR — The z≃−18 WLS result ignores the classifier transfer and therefore does not exclude a physical reference dipole

Appendix D.g and Table XIV compare the observed hard-label amplitude

A
best
	​

=4.55×10
−3

directly with A
ref
	​

=0.034, using σ
boot
	​

=1.63×10
−3
. Yet Sec. VI B states that the classifier response is approximately g=0.398. If A
ref
	​

 is a physical underlying amplitude, the expected hard-label amplitude is not A
ref
	​

 but approximately gA
ref
	​

, with further corrections for triage, contamination, confidence selection, and spatial dependence.

Even using the manuscript’s global g only as an illustration,

gA
ref
	​

=0.398(0.034)=0.0135,

which would change the quoted statistic from about −18.1 to

0.00163
0.00455−0.0135
	​

≃−5.5.

If the appropriate reference is actually A
ref
	​

=0.017, as discussed in the next concern, the same illustrative calculation gives z≃−1.4. The exact answer requires the missing end-to-end transfer model, but the direction of the error is unambiguous: ignoring attenuation makes exclusion of an underlying physical signal stronger, not more conservative.

The manuscript’s statement in Appendix D that omission of classifier uncertainty makes the result conservative is therefore incorrect. Classification affects the expected mean signal as well as its variance.

There are additional problems with this result:

Figure 10 shows a block-bootstrap sampling distribution around the observed field, not a null distribution generated under A=A
ref
	​

.

The amplitude is nonlinear and positive-definite; a Gaussian standard-error ratio is not automatically a calibrated test.

Table XIV’s nine-template “nuisance-marginalized” fit contains dipole components, imaging-leg fractions, density, density squared, and a constant. It does not contain the explicit depth, PSF, extinction, and morphology templates that the surrounding text claims have been jointly marginalized.

Section III B alternately calls this fit “primary” and a “diagnostic cross-check,” which must be resolved.

A formal forward likelihood or signal-injection test under the reference hypothesis is required. The present z≃−18 result should be removed from the abstract and from the primary-estimator hierarchy.

5. MAJOR — The conversion of the Shamir reference amplitude appears to contain a factor-of-two error

The manuscript defines

A
p
	​

=
N
CW
	​

+N
CCW
	​

N
CW
	​

−N
CCW
	​

	​

=2(f
CW
	​

−
2
1
	​

)

in Eq. (3). It then states that Shamir’s reported 1.7%−4.0% asymmetry must be doubled to 3.4%−8.0% in A
p
	​

 units.

However, Ref. [3] explicitly defines its asymmetry as

A=
N
CW
	​

+N
CCW
	​

N
CW
	​

−N
CCW
	​

	​

,

which is already identical to Eq. (3), not to f
CW
	​

−1/2. 
arXiv
+1

Unless the manuscript’s 1.7%−4.0% range is taken from some separately defined quantity, the factor of two is erroneous. The authors must cite the exact table, equation, and column from each comparison paper and reproduce the convention conversion transparently. This issue propagates into:

The abstract’s A
ref
	​

=0.034;

Sections V A and VI C;

Table XIV and Figure 10;

The claimed 7−18× amplitude tension;

The claimed z≃−18 template result;

The conclusions.

Using 1.7% directly in Eq. (3) units would already reduce the unattenuated block-bootstrap ratio to approximately −7.6, before addressing the more serious transfer-function problem above.

6. MAJOR — Classifier validation is inadequate for a sub-percent spatial measurement

The classifier’s internal validation statistics cannot support the claimed precision:

Section II B and Table XI state that 66.5% of the labels are CE-ResNet pseudo-labels.

The only explicitly listed not spiral training source is 2,000 synthetic hard negatives. Unless additional real non-spirals exist but are not described, the reported 99.4% internal not spiral validation accuracy is principally a same-domain synthetic validation, not a test on real ellipticals, mergers, and edge-on disks.

The independent GZ1 comparison gives only 58.7% three-class accuracy and 69.91% conditional chirality accuracy, with κ=0.40.

Appendix E finds that 15.8% of objects classified as spirals have b/a<0.3.

The catalog exhibits a 0.26% global handedness artifact and significant confidence- and imaging-leg-dependent spatial structure. 

g_P4

For a sub-percent angular dipole test, a global confusion matrix is insufficient. The required quantity is the spatially conditional transfer matrix after all selection cuts. At minimum, the paper needs validation stratified jointly by:

Imaging campaign;

Depth and seeing/PSF;

Magnitude and angular size;

Axis ratio and morphology;

Galactic extinction;

Confidence;

Sky region;

Redshift or a suitable photometric-redshift proxy.

Those tests must be performed specifically on the p
eq
	​

>0.6 primary sample. A global g=0.398 does not demonstrate that g(
n
^
) is constant.

The GZ1-human-only test does not close this gap. The manuscript itself estimates A
95
	​

≃4.5%−6.8% for that test, so it cannot validate the sub-percent regime. Statements that it “establishes” that the headline null is not inherited from pseudo-labels must be weakened to the much narrower statement that no several-percent dipole is seen in that small, differently selected sample.

7. MAJOR — Rotation dependence remains a potentially dangerous uncorrected systematic

Equation (2) guarantees covariance under a horizontal reflection. It does not guarantee invariance under in-plane rotations, even though image rotation should leave chirality unchanged. Section III D and Appendix B report that 21.4% of per-galaxy argmax labels change between Z
2
	​

 and D
4
	​

 TTA in the tested samples. The paper dismisses this as a borderline-object effect, but those borderline objects enter the full-catalog WLS and harmonic analyses, and no production-scale spatial audit of this instability is shown.

Rotation sensitivity can couple to galaxy position angle, PSF anisotropy, camera orientation, resampling artifacts, and survey-dependent image construction. Stability of the mean p
CW
	​

 on two samples of approximately 2,000 objects does not demonstrate stability of a sky dipole formed from millions of hard labels.

The authors should either:

Produce a D
4
	​

-averaged or architecturally rotation-equivariant production catalog and repeat the analysis; or

Demonstrate, on a sufficiently large sample, that Z
2
	​

→D
4
	​

 label changes have no dipolar or low-ℓ dependence after conditioning on imaging leg, depth, PSF, morphology, and position angle.

The corresponding test must be reported separately for the high-confidence primary sample and the full sample.

8. MAJOR — The primary confidence cut is scientifically consequential and not adequately justified as pre-specified

The full Catalog C sample gives a z≃4.2−4.4 real-space excess, while the result becomes null after imposing p
eq
	​

>0.6, retaining only about 30% of the classified spirals. Section IV C explicitly motivates 0.6 as the threshold where the excess disappears. A code commit in a live repository, with no frozen tag or independent preregistration record, is not sufficient to establish that this choice was made before examining relevant outcomes. 

g_P4

The stability of the results at 0.6, 0.7, and 0.8 is useful, but it does not address the larger selection decision between the full sample, which is non-null, and the high-confidence subset, which is null.

Moreover, confidence is confounded with source brightness, size, morphology, redshift, depth, and imaging leg. A genuine signal whose amplitude or sampled population varies with these quantities could be preferentially present in the low-confidence sample. Confidence dependence is evidence for a classifier systematic, but it is not by itself proof.

The authors need to do one of the following:

Define the cut solely from an external validation criterion fixed without consulting any sky statistic, and show the corresponding conditional selection function;

Treat confidence continuously in a joint likelihood;

Correct for the analysis-selection procedure; or

Restrict the headline conclusion to the 949,584-object high-confidence subset, without claiming a null “in 8.5 million galaxies.”

The assertion that 0.5 is “the argmax boundary” should also be corrected: in a three-class classifier, an argmax probability can lie anywhere above 1/3; 0.5 is not an argmax boundary.

9. MAJOR — The harmonic residual is unresolved, not securely “systematics-attributed”

The manuscript reports significant low-ℓ residuals under several diagnostic constructions, while the imaging-plus-morphology forward model reproduces only about 53% of the ℓ=1 amplitude. The remaining approximately 47% is explicitly unresolved. 

g_P4

 

g_P4

The “eight-anchor” battery is suggestive, but it is not a calibrated comparison of a signal model against a systematic model:

Apodization and boundary tests rule out particular numerical artifacts; they do not distinguish cosmological signal from a smooth survey systematic.

Density-stratified persistence shows that density alone is insufficient; it does not establish what the residual is.

The ℓ=2 cross-spectrum result is based on 200 realizations and is one statistic among multiple inspected multipoles/templates.

The assertion that ℓ=2>ℓ=1 is incompatible with a clean dipole should be demonstrated by injecting pure dipoles through the exact mask, weighting, mean subtraction, and MASTER pipeline and examining the joint (C
1
	​

,C
2
	​

,…) distribution.

The reported 53% explained fraction is an in-sample fit to the same map. Its uncertainty and chance-alignment distribution are not given, and no cross-validation is presented.

There is also a questionable field construction in Appendix A: pixels with N
spiral
	​

=0 on the N
all
	​

≥1 footprint are assigned A
p
	​

=0 while retaining nonzero N
all
	​

 weight. Since A
p
	​

 is undefined where there are no spirals, these pixels should ordinarily have zero mask weight. Treating “no chirality information” as a measured zero can itself couple the non-spiral selection function into low-ℓ power.

The residual should be described as an unresolved diagnostic residual with evidence favoring survey systematics, not as definitively attributed. The abstract and conclusions should not claim that its possible cosmological content has been bounded by A
95
	​

.

10. MAJOR — The physical and early-universe interpretation is not supported by the analysis

The data analysis is a two-dimensional angular test on an imaging-selected sample. The manuscript provides neither a measured redshift distribution for the selected high-confidence sample nor redshift-binned results. It also explicitly lacks a transfer function from primordial parity-violating physics through galaxy formation and image selection to projected apparent arm winding.

Nevertheless, Sec. VI C states that cosmic-birefringence and gravitational Chern-Simons scenarios would generically produce a morphology-channel dipole and that the reported sensitivity “bounds” such scenarios. No such implication is derived. Cosmic birefringence acts on photon polarization; a relation to projected spiral-arm handedness is not generic without an explicit model. Similarly, parity-violating gravitational-wave propagation does not by itself establish a predicted galaxy-morphology dipole of known amplitude.

The parity classification of the ℓ=1 pseudoscalar mode as parity-even is reasonable. The subsequent model claims are not. Section VI C should either derive an actual transfer calculation and predicted observable, including the sample’s redshift kernel, or be reduced to a brief statement that the result is a phenomenological angular isotropy test with no current translation into fundamental-theory parameters.

11. MAJOR — The reproducibility record is not presently archival or immutable

The Data Availability section says that the exact DOI, commit hashes, and frozen release will be inserted later. At present, the artifacts resolve against a live main branch. This is particularly problematic because:

The claimed pre-specification of the primary cut rests on repository history;

Numerous central numbers are available only through named JSON artifacts rather than reproducible tables in the manuscript;

Several nominally similar harmonic calculations use different field, mask, weighting, and mean-subtraction conventions;

The released catalog retains rows affected by a raw/equivariant pipeline mismatch, including reconstructed probabilities outside [0,1].

Before the scientific claims can be audited, the authors must provide a frozen archive containing the exact catalog, model weights, masks, null arrays, source tables, environment specification, scripts, random seeds, and one-command reproduction workflow for every primary table and figure. The invalid or mismatched probability columns should preferably be regenerated rather than merely flagged.

Minor concerns
12. MINOR — The ECE lower-bound calculation uses quantities from different samples

Appendix B.g subtracts the catalog-wide mean confidence, 0.951, from accuracy measured on the GZ1 cross-match. The Jensen inequality cited there only provides an ECE lower bound when confidence and accuracy are evaluated on the same sample and weighting. Recompute the mean confidence on the exact GZ1 evaluation subset before quoting this bound.

13. MINOR — GZ1 disagreement is not automatically a lower bound on intrinsic accuracy

Appendix B states that noisy human labels make the measured accuracy a lower bound on classifier accuracy. That conclusion requires a model of the human-label errors and their independence from classifier errors. Correlated or systematic human biases can make the observed agreement either higher or lower than agreement with latent truth. Call this an agreement rate unless a noise model is supplied.

14. MINOR — Mask and field terminology is unnecessarily inconsistent

Section IV C defines the “canonical mask” as N
spiral
	​

≥10, whereas Appendix A.d calls N
all
	​

≥1 the “canonical analysis-footprint declaration.” Table V then uses different field scalings and mean-subtraction weights on the two footprints. These distinctions are real but the terminology is confusing. Assign unique names to each footprint and field convention and use them consistently in all tables and captions.

15. MINOR — Figure 10 is mislabeled as a null distribution

A nonparametric block-bootstrap distribution obtained by resampling the observed data is a sampling distribution around the observed estimate, not a null distribution unless the data were first transformed under a specified null. The figure title, caption, and surrounding text should be corrected.

16. MINOR — The “two-sided p=0.62” for a positive-definite amplitude is not well motivated

The primary statistic is an amplitude with a natural upper-tail test. Doubling its upper-tail rank does not generally produce a meaningful two-sided test, particularly when the observed value is above the null mean. Report the one-sided amplitude p-value and, separately, component-wise tests if signs are scientifically relevant.

17. MINOR — Monte Carlo uncertainty should be propagated consistently

For the 500-realization direct run, the manuscript reports 15/500=0.030, while elsewhere it uses the recommended (k+1)/(N+1) rank convention. Apply one convention consistently. Table VIII should include binomial confidence intervals on every recovery probability; with 100 injections, “1.00” does not mean exact unity. The log-interpolated A
95
	​

=1.20% should not be emphasized given the coarse grid and Monte Carlo uncertainty.

18. MINOR — The harmonic “axis average” is not an isotropic axis average

Figure 9 and Table IX average over only the Cartesian x,y,z axes. On a highly anisotropic footprint, these three directions do not constitute an isotropic orientation average. Use many uniformly distributed axes or label the result a three-axis diagnostic.

19. MINOR — The monopole-mask result is overstated as an explanation of prior work

The 99.32% result demonstrates expected cut-sky mode coupling for this manuscript’s own biased classifier, field definition, and mask. It does not establish that earlier Ganalyzer or hemisphere analyses were caused by the same mechanism. The manuscript acknowledges that a matched reanalysis is needed, but several sentences nevertheless attribute prior claims to this channel. Those statements should be removed. The phenomenon itself is standard mask-induced multipole mixing; the useful contribution is its quantitative size in this pipeline.

20. MINOR — Local monopole renormalization is not a universally safe prescription

Section IV B and Data Availability recommend per-region monopole subtraction for future parity analyses. Depending on the chosen regions, that procedure can project out genuine low-order modes and induce complicated transfer functions. The recommendation should specify a forward-modeled estimator and its mode-response matrix rather than prescribe ad hoc local subtraction.

21. MINOR — Cross-match and catalog-construction details should be self-contained

Section II A should state the coordinate-match radius, treatment of multiple matches, duplicate-object policy, and distribution of the 157 failed quality-control objects. The exact construction of the synthetic hard negatives also needs to be described, not only referenced through repository artifacts.

22. MINOR — The manuscript needs substantial compression and removal of repetition

The same caveats concerning incompatible σ conventions, the GZ1-only test, the 47% residual, and the distinction between observed-label and physical sensitivity are repeated many times. Several figure captions are effectively additional discussion sections. A shorter paper with one definitive estimator table, one definitive mask/field table, and a clear separation among measurement, systematics, and interpretation would be considerably easier to audit.

The potentially publishable core is a narrower one: a large public classifier catalog, a null result for a clearly specified high-confidence observed-label sample, and a detailed demonstration that low-confidence and harmonic analyses are contaminated by survey/classifier systematics. Establishing a physical sub-percent bound or a formal exclusion of previously reported amplitudes requires the additional analyses identified above.

Recommendation: MAJOR REVISIONS
