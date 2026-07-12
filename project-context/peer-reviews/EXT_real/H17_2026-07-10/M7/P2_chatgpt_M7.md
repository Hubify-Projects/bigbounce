VERDICT: REJECT

ISSUES:

[MAJOR] Section II C and Conclusion—claimed cubic-order transmission through the bounce. The bound δf
NL
	​

≲10
−3
 is asserted rather than derived. The cited Wilson–Ewing model uses a holonomy-corrected scalar equation whose gradient coefficient is 1−2ρ/ρ
c
	​

, becoming negative near the bounce; it is not the dressed-metric c
s
2
	​

=1 system invoked to justify a controlled gradient expansion. Moreover, the cited calculation is linear, and the absence of additional scalar degrees of freedom does not by itself imply 
ζ
˙
	​

=0 or nonlinear conservation: conservation requires an attractor/adiabatic condition, while matter contraction itself is a single-field non-attractor with a growing super-Hubble mode. A second- or third-order calculation in one consistently specified LQC quantization is required. 

ext_P2_M7

 
arXiv
+2
arXiv
+2

[MAJOR] Appendix A—claimed identification of the Cai arithmetic error. Re-summing Cai et al.’s Eqs. (34)–(36) does support −35/16, and Li et al.’s independent formula gives the same value at c
s
	​

=1; however, the manuscript has not established its more specific claim that Cai’s Eq. (37) contains a spurious −(99/128)∑
i
	​

k
i
3
	​

 term. The manuscript’s own Eq. (A4) is algebraically identical to Cai’s Eq. (37) when the (5,2,2) orbit is summed over its three distinct monomials; the alleged extra term appears when the j↔k-identical terms are counted twice under the manuscript’s imposed ordered-tuple convention. Appendix A.1.d is also internally contradictory in calling Cai’s Eqs. (34)–(36) “pre-doubling” expressions after using them elsewhere as the complete physical vertex sum. The paper establishes a literature inconsistency favoring −35/16, but not the claimed transcription-error mechanism. 
arXiv
+3
arXiv
+3
arXiv
+3

[MAJOR] Section II A and the null-space analysis—use of an unphysical, underdetermined bispectrum shape. Once Appendix A supplies the full vertex-sum polynomial in Eq. (A4), there is no physical three-dimensional coefficient null space: every coefficient is fixed. Nevertheless, the forecasts use coefficients (2,7,3,−12,−69,19) inferred from only three benchmark configurations and sample arbitrary null-space directions with a basis-dependent Euclidean prior. The released Fisher code additionally defines the (5,2,2) basis element with an explicit factor of two; in that basis Eq. (A4) would correspond to (3,1,−9,5,−33,9), not the adopted coefficients. Consequently, the reported shape cosines, r-distribution, nonlocal-template projection, and injection tests are not calculations of the corrected vertex-derived bispectrum and must all be redone. 
GitHub
+1

[MAJOR] Section III B, Eqs. (5)–(6)—the r=0.84 SPHEREx template correction is not a survey Fisher response. Equation (5) is valid only when r is the actual cross-response F
local,bounce
	​

/F
local,local
	​

 under the estimator covariance and after nuisance projection. The quoted 0.84 instead comes from a collection of ad hoc geometry and power-law weightings, none of which is Heinrich et al.’s multi-tracer redshift-space covariance. The manuscript’s own surrogate Fisher gives r
eff
	​

≃0.99, demonstrating that 0.84 is not the response of that estimator; describing it as “conservative” does not turn it into a calibrated forecast. The headline 2.6–2.75σ significance therefore lacks a valid statistical derivation.

[MAJOR] Section IV—independent Fisher “validation.” The released implementation is not apples-to-apples with Heinrich et al.: it uses 20 k-shells despite claiming the 23,098-triangle grid; its scale-dependent-bias derivative omits the photometric-redshift window on the differentiated leg; it replaces the required multi-tracer Wick contractions by one Kronecker product times a scalar s
B
	​

; and its “bias-marginalized” result contains one global bias-amplitude nuisance rather than tracer- and redshift-bin-specific biases plus cosmological parameters. Heinrich et al. explicitly note that the scalar s
B
	​

=6,2,1 prescription is invalid for multi-tracer bispectra and employ a much larger nuisance space. The numerical proximity to 0.7 is therefore not a validation, and the later redshift-space result 0.42–0.45, far tighter than the published redshift-space forecast, further exposes the mismatch. 
arXiv
+3
GitHub
+3
GitHub
+3

[MAJOR] Section VII and Table V—GR-marginalization floor. The correlation ρ=−0.868 is transferred from an f
NL
	​

−n
f
NL
	​

	​

 scale-dependent-bias Fisher matrix to a different f
NL
	​

−A
GR
	​

 bispectrum problem without a derivation. A uniform-shape cosine of 0.95 is likewise not a noise-weighted Fisher correlation, and adding a nominal σ
GR
	​

 in quadrature is not generally equivalent to marginalizing a response template with a prior. The manuscript’s channel-native surrogate instead obtains ρ≃−0.42 and a substantially different significance, after which the less favorable transferred proxy is retained merely because it is “conservative.” Thus the 0.8–1.3σ floor and the advertised 1.3–2.75σ envelope are scenario choices, not statistical forecasts.

[MAJOR] Section VII B—b
ϕ
	​

 prior and degradation estimates. Heinrich et al. impose the universal-mass-function relation b
01
	​

=2f
NL
	​

δ
c
	​

(b
10
	​

−1); this is not equivalent to the manuscript’s claimed 20% Gaussian baseline prior on independently variable b
ϕ
	​

. The subsequent 30% and 50% cases, and the asserted 20–50% widening of the bispectrum constraint, are not produced by a per-tracer, per-bin joint Fisher calculation. Those numbers cannot enter a cumulative significance budget until b
ϕ
	​

, the direct primordial-bispectrum term, nonlinear biases, and their cross-correlations are marginalized consistently. 
arXiv

[MAJOR] Section VI and Tables III–IV—Bayesian model comparison. The quoted Bayes factors are essentially prior-volume ratios obtained by placing the mock datum exactly at the bounce prediction and comparing a point or narrow Gaussian prior with an arbitrary uniform f
NL
	​

 interval; they do not represent evidence for concrete multifield-inflation models with physical parameters, bispectrum shapes, and shared nuisance parameters. The Monte Carlo exercises only reproduce this analytic construction. There is also a numerical inconsistency: for σ
eff
	​

=0.7, σ
theory
	​

=1, and a [−5,5] competitor whose CDF tails are negligible, the stated formula gives

BF=
2π
	​

0.7
2
+1
2
	​

10
	​

≃3.27,

not 3.9. The 9–14 Bayes-factor headline should be removed or explicitly relabeled as a toy prior-predictive illustration.

[MAJOR] Sections II C and VIII B—quasi-dust correction and consistency relation. The observationally used model has w=−0.003, whereas the calculated bispectrum is for exact w=0. The interval κ
ϵ
	​

∈[2.8,40], particularly the asserted 14× enhancement defining its upper endpoint, is a schematic estimate rather than a bound from the four cubic integrals. Shape changes are also not calculated. Until the quasi-dust in-in calculation is performed, the claimed 0.6–8% uncertainty and the f
NL
	​

(n
s
	​

) “consistency relation” are ansätze, not predictions.

[MINOR] Section VI A and Table II—observable-frame interpretation. The manuscript incorrectly labels the comoving-gauge Maldacena value f
NL
	​

≃0.015 as the quantity directly measured on the sky by the SPHEREx scale-dependent-bias estimator. In a physical local frame, the leading single-field consistency contribution produces no primordial scale-dependent halo bias; observable squeezed correlations arise from projection effects. The qualitative contrast with an order-unity bounce signal survives, but the quoted gauge-frame ratio of 146 is not the appropriate survey-level comparison. 
arXiv

[MINOR] Section V and the MegaMapper headline. Only the idealized σ(f
NL
	​

)≃0.5 input is externally anchored; the post-systematic numbers are obtained by transferring a SPHEREx-motivated budget to a substantially higher-redshift survey where relativistic, magnification, selection, and tracer-bias effects differ. Since the manuscript itself calls this transfer uncalibrated, numerical ranges such as 1.5–3.5σ should not appear as forecast results without a dedicated MegaMapper Fisher analysis.

[MINOR] Overall scope and presentation. The central calculation is obscured by extensive material on Einstein–Cartan–Holst fermion operators, anomaly-selected tracers, speculative mission timelines, cosmic birefringence, and repeatedly restated caveats. A publishable paper should focus on the factor-of-two audit and a correctly defined survey projection, remove Appendix B and unsupported ancillary forecasts, and substantially reduce the manuscript’s length and repetition.

No—the algebra plausibly supports −35/16 for the pre-bounce exact-dust squeezed limit, but the manuscript does not establish its survival through the specified bounce or the quoted SPHEREx significances and Bayes factors.
