(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:

[MAJOR] Abstract; Secs. V, VI B, and VII — physical sensitivity is contradicted by the manuscript’s own classifier-dilution calculation. The injection–recovery exercise injects a dipole only into the already classified hard-label field, after the classifier, not spiral triage, and confidence selection. Using the manuscript’s adopted transfer factor g
eff
	​

=0.398, a genuine physical dipole of 1.7% would appear at only 0.017×0.398≃0.68% in the observed-label field, below the reported A
50
	​

≃0.75% and well below A
95
	​

=1.0%−1.5%. Thus the repeated claim that a genuine Shamir-scale 1.7% dipole “would have been detected” is not supported; under the stated dilution, the physical A
95
	​

 scale would instead be approximately 2.5%−3.8%. The full-catalog mirror test checks equivariance, not recovery of a sky-dependent physical dipole through classification and selection. 

ext_P4_M7

[MAJOR] Sec. IV C — the primary p
eq
	​

>0.6 selection is not demonstrably pre-registered and coincides exactly with the disappearance of the signal. The reported moment-z changes from approximately 4.0 at cuts 0,0.4,0.5 to 0.41 at 0.6. A repository commit without an independently timestamped frozen release is not a statistical preregistration and does not demonstrate that the threshold was fixed before examining the dipole or related systematics. The primary probability must therefore include the confidence-cut selection procedure, or the result must be validated on an untouched sample.

[MAJOR] Sec. IV C — neither primary randomization null is valid for the demonstrated spatially varying classifier and survey response. Permuting pixel asymmetries assumes exchangeability despite large variations in galaxy count, depth, PSF, morphology, confidence, and label reliability. The global per-galaxy label shuffle preserves pixel counts but destroys spatially varying confusion rates and conditional CW fractions—the very effects invoked to explain the full-sample excess. A valid test must condition on these variables, for example through an individual-galaxy likelihood or a spatially stratified/hierarchical null with calibrated, position-dependent confusion.

[MAJOR] Appendix D — the quoted z≃−7.6 is not a calibrated exclusion of a 1.7% dipole. It is computed as (
A
−A
ref
	​

)/σ
boot
	​

, where the bootstrap distribution is centered on the observed, positive-definite dipole amplitude rather than generated under A=A
ref
	​

. The dipole direction is unknown, the amplitude distribution is non-Gaussian, the fit uses a different full-catalog sample from the declared high-confidence primary, and classifier signal attenuation is absent. A likelihood-ratio or injection-based test under A
ref
	​

, with direction and nuisance parameters treated explicitly and coverage demonstrated, is required.

[MAJOR] Secs. III A and VI B; Tables V, VIII, and IX — “σ” is used for an uncalibrated moment ratio and then treated as a detection threshold. The manuscript itself shows that z=7.31 corresponds to an empirical rank p=6×10
−4
, only about 3.2σ on a Gaussian one-sided scale. Likewise, the z
inj
	​

>3 rule used to define A
50
	​

 and A
95
	​

 has no specified false-alarm probability; nearly null, very-low-amplitude injections cross it about 1% of the time in Table VIII. All recovery curves and “3σ” statements must be recomputed using an empirical critical value at a declared α, or a calibrated likelihood statistic.

[MAJOR] Sec. IV D — the statistically significant harmonic and hemisphere results remain unresolved; designating them “diagnostic” does not establish that they are systematic. The manuscript reports low-ℓ rank probabilities of order 10
−3
 and a hemisphere max-statistic p
LEE
	​

≤10
−4
, while the forward model accounts for only part of the signal. Moreover, the stated “47% remaining amplitude” is mathematically incorrect: with ∣a
sys
	​

∣/∣a
obs
	​

∣=3.75/6.95≃0.54 and cosθ≃0.84, vector subtraction leaves approximately 0.62∣a
obs
	​

∣, or A
p
	​

≃0.43%, not 0.32%. A real-space non-detection also does not imply that the cosmological part of this residual must be below A
50
	​

; a joint signal-plus-systematics analysis is needed.

[MAJOR] Sec. III D and Appendix B — rotational non-invariance is insufficiently controlled. Rotations preserve chirality, so the finding that 21.4% of argmax labels change between Z
2
	​

 and D
4
	​

 processing is substantial for an analysis using hard labels at sub-percent precision. Stability of the mean soft score on two samples of roughly 2,000 objects is not enough to exclude coupling between image orientation, anisotropic PSF or scan patterns, and sky position. Full-catalog D
4
	​

 averaging, or an equivalent full-sky rotation-bias test demonstrating stability of the dipole, is required.

[MAJOR] Secs. II and VI A; Appendices B and E — external classifier validation does not establish sub-percent spatial parity symmetry. The independent performance is only 58.7% for three classes and 69.91% for spiral chirality, while 15.8% of classified spirals are reported to be edge-on. Galaxy Zoo 1 labels and footprint are not representative of the complete DESI footprint, and the two-leg confidence intervals still permit differential CW/CCW errors comparable to the claimed sensitivity. The N≃4.6×10
4
 human-only test has an estimated A
50
	​

∼3.4%, so it cannot validate the sub-percent null or rule out pseudo-label inheritance at the relevant scale; statements that it “establishes” independence should be weakened.

[MAJOR] Secs. VI B and VII — no confidence interval or upper limit on the dipole amplitude is provided. A recovery probability is a property of an estimator and detection rule, not an upper bound on the signal given the observed data. The manuscript consequently cannot support quantitative “tension factors,” exclusions, or future-falsification boundaries. A frequentist interval with demonstrated coverage or a posterior for the three dipole components and amplitude, including survey and classifier nuisance parameters, is necessary.

[MAJOR] Primary covariance estimation neglects allowed isotropic spatial correlations. Both label shuffling and independent binomial simulations erase intrinsic spin correlations, environmental correlations, and correlated classifier errors. Statistical isotropy does not imply independent Bernoulli chirality labels. The two-point test on a 50,000-object subsample is not sufficient to establish that this contribution is negligible. Survey mocks, an empirically validated spatial covariance, or a block/jackknife analysis performed directly on the high-confidence primary sample is needed.

[MAJOR] Appendix D — the “joint nuisance-marginalized” characterization overstates what is actually fitted. The nine-template WLS design contains dipole components, imaging-leg fractions, density, density squared, and a constant; it does not contain the stated depth, PSF, extinction, or measured morphology fields. The 24-template extension adds leg-by-confidence proxies, not a physical depth/PSF/morphology model. Those variables are considered later in a separate forward model that leaves most of the vector residual unexplained. The claimed clean-dipole disfavor therefore is not marginalized over the principal nuisance channels identified by the paper.

[MINOR] Several internal numerical and convention inconsistencies must be resolved. Examples include the in-mask count of 3,200,420 in Sec. IV C versus 3,201,160 in Table XVI; the Sec. VI A conversion that calls A
95
	​

 an f
CW
	​

-unit quantity and doubles it despite Tables VIII and XV defining it in A
p
	​

 units; the coexistence of +3.64 and +7.93 “canonical” MASTER results under different field and mean-subtraction conventions; and inconsistent descriptions of whether the primary injection axes are θ-uniform or area-uniform.

[MINOR] Sec. VI C — the early-universe interpretation is too strong without a transfer calculation. The manuscript has not shown that cosmic birefringence or gravitational Chern–Simons models generically generate a projected galaxy-morphology dipole of the form measured here. Until a galaxy-formation and observational transfer function is derived, the result should be presented only as a constraint on the observed late-time morphology field, not on those theoretical sectors.

[MINOR] Data Availability and presentation — the analysis is not yet frozen in a publication-grade reproducibility archive. The manuscript relies extensively on repository-local artifact paths while stating that the DOI and immutable release will be created later and that the live main branch is authoritative. The exact catalog, model, scripts, random seeds, environments, and result arrays must be archived under an immutable DOI and commit before acceptance; the paper should also be substantially shortened and reorganized around one primary estimator and one coherent statistical convention.

(3) The narrow statement that the selected high-confidence hard-label sample is consistent with zero under the authors’ chosen permutation null is supported, but the manuscript’s central physical claim of a robust sub-percent DESI chirality null and exclusion of Shamir-scale dipoles is not.
