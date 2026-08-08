(1) VERDICT: REJECT

(2) ISSUES:

[MAJOR] Section II.A and Appendix A—internally inconsistent bispectrum polynomial. The coefficient vector actually used for the shape analysis, (2,7,3,−12,−69,19), does not reproduce the “corrected” benchmarks under the manuscript’s explicitly stated ordered-sum convention. Direct substitution into Eqs. (1)–(2) gives B
NL
equil
	​

=−255/64, B
NL
squeezed
	​

=−35/8, and B
NL
folded
	​

=−9/4: precisely the uncorrected values, not Table I’s halved values. Conversely, Eq. (A4) fixes a unique corrected polynomial, corresponding in the main-text six-orbit basis to (3,1,−9,5,−33,9), because the ordered (5,2,2) orbit double-counts its three distinct monomials. Thus the claimed three-dimensional coefficient null space is artificial, and the null-space scan, Fig. 1 shape, template overlaps, injections, and all downstream r-dependent significances are based on the wrong or manually rescaled shape. 

ext_P2_M4

[MAJOR] Appendix A—“four independent certifications” and time-ordering interpretation are not established. The vertex sum, the ϵ-grouped sum, and benchmark matching are algebraically dependent checks, not independent certifications. Moreover, the assertion in Appendix A.1(d) that Cai et al.’s Eqs. (34)–(36) are undoubled single-time-ordering expressions is unsupported and conflicts with both the source calculation, which starts from the full in-in commutator, and this manuscript’s earlier use of those equations as the complete vertex sum. Li et al.’s Eq. (4.19) at c
s
	​

=1 already supplies the unique corrected full shape and Eq. (5.1) gives −35/16; the defensible result is therefore an algebraic correction of Cai et al.’s final collapse, not the manuscript’s commutator-doubling narrative. 
arXiv
+3
arXiv
+3
arXiv
+3

[MAJOR] Section II.C—faithful cubic transmission through the bounce is not proved. “Single clock” means one scalar degree of freedom; it does not imply 
ζ
˙
	​

=0, an attractor background, or conservation of nonlinear correlators. The matter-contraction solution is explicitly non-attractor, with a growing super-Hubble ζ mode, and Wilson-Ewing’s linear calculation exhibits bounce-induced mode mixing rather than unit transfer. Even a scale-independent linear transfer ζ
out
	​

=Tζ
in
	​

 changes the normalized non-Gaussian amplitude unless T=1, while genuinely cubic LQC interactions can add further contributions. No cubic LQC action, nonlinear transfer matrix, or in-in evolution through the bounce is calculated, so the claimed bound δf
NL
	​

≲10
−3
 and the asserted UV-completion independence do not follow. 
arXiv
+1

[MAJOR] Sections II.C–II.D—incorrect identification of the LQC perturbation prescription. The manuscript states that Wilson-Ewing uses a dressed-metric/hybrid prescription with Lorentzian c
s
2
	​

=1, relegating c
s
2
	​

=1−2ρ/ρ
c
	​

<0 to an alternative scheme. The cited Wilson-Ewing calculation instead explicitly uses the holonomy-corrected Mukhanov–Sasaki equation with gradient coefficient 1−2ρ/ρ
c
	​

, which changes sign near the bounce. The proposed cubic-conservation “closure” is therefore conditioned on a different perturbation prescription from the model used to motivate the observable prediction. The same reference also requires ρ
c
	​

∼10
−9
ρ
Pl
	​

 to normalize the scalar spectrum and notes the tension with the usual LQC critical density, contrary to the claim that the model has no known observational or theoretical tension. 
arXiv
+1

[MAJOR] Section III.B—r=0.84 is not the response of the SPHEREx estimator. For local template L, bounce template B, and covariance C, the local-estimator response is

α=
L
T
C
−1
L
L
T
C
−1
B
	​

,

and the matched-template information is B
T
C
−1
B. A Euclidean grid average, a k
n
-weighted average, or an unweighted shape cosine is not interchangeable with either quantity. The manuscript’s own in-house Fisher gives r
eff
	​

≃0.99, demonstrating that the adopted 0.84 is not the survey response. Calling an arbitrary non-survey metric “conservative” does not turn it into a statistically defined forecast. The headline significance must be recomputed with the exact corrected polynomial and one consistently specified SPHEREx covariance. 
arXiv
+1

[MAJOR] Section IV—independent Fisher calculation does not validate the recast as presented. The claimed σ(f
NL
	​

)=0.42–0.45 redshift-space result is substantially stronger than the published 0.7, while the calculation fixes b
2
	​

 and b
s
2
	​

, uses only the leading diagonal Gaussian covariance, omits non-Poisson stochastic terms and non-Gaussian covariance, and treats FoG and other survey effects incompletely. These approximations generally increase the information. Reproducing one scalar error bar to 2–11% is insufficient validation of the off-diagonal template response or nuisance correlations, particularly when the input bounce shape is itself inconsistent. The full Fisher equations, binning, derivatives, covariance normalization, nuisance set, and convergence tests must appear in the manuscript rather than being delegated to mutable scripts.

[MAJOR] Section VII and Table V—systematic “budget” is not a valid marginalization. Relativistic projection terms are model templates that cause parameter bias if omitted and parameter degeneracy if fitted; they are not an independent Gaussian error σ
GR
	​

 that can simply be added in quadrature. Likewise, replacing 0.7 by 0.9 or 1.0 for b
ϕ
	​

 is not derived from a joint likelihood. The formula σ
marg
	​

=σ
base
	​

/
1−ρ
2
	​

 applies only when the conditional error and correlation come from the same Fisher matrix with the same data vector and nuisance normalization. Combining Heinrich’s bispectrum error with a correlation imported from a different power-spectrum SDB calculation—or with an unweighted shape cosine—is invalid. Heinrich et al. assume the universal-mass-function bias relations and vary the linear biases; they do not supply the manuscript’s 20–50% b
ϕ
	​

 degradation model. Consequently, the 0.8, 1.3, 1.5, and 2.3σ endpoints do not bracket a controlled uncertainty, and the advertised “realistic 1.3–2.75σ” range has no defined statistical interpretation. 
arXiv

[MAJOR] Section VI—Bayes factors do not constitute a model comparison. A uniform prior directly on f
NL
	​

∈[−5,5] or [−15,15] is not a prior-predictive distribution for curvaton, quasi-single-field, or generic multifield inflation; it ignores their fundamental parameters, correlations with other observables, and model-dependent shape predictions. Placing the mock datum exactly at the bounce mean and comparing a narrow or delta-function bounce prior with a broad uniform competitor produces the Occam factor W/σ by construction. The Monte Carlo realizations merely reevaluate the same assumed likelihood and do not independently validate the evidence. In addition, the r-“rebooking” is coordinate dependent: under f
bounce
	​

=f
local
	​

/r, likelihoods, prior widths, and Jacobians must all be transformed consistently. Inflating σ while retaining an untransformed competitor prior creates an artificial change in evidence. The headline BF≃9–14 should be removed.

[MAJOR] Sections II.C and VIII—quasi-dust correction and f
NL
	​

–n
s
	​

 relation are speculative. The range κ
ϵ
	​

=2.8–40 is not a calculated bound: its upper endpoint is introduced through a schematic factor of approximately 14, without evaluating the mode functions or four cubic integrals. There is therefore no derivation of the claimed 0.6–8% correction, its sign, or its correlated effect on the shape. Equation (13) is not currently a model consistency relation but an ansatz with an order-of-magnitude coefficient. It cannot support the stated theory prior or the Bayesian conclusions.

[MAJOR] Section VI.A and Table II—incorrect identification of the survey observable in single-field inflation. The manuscript labels Maldacena’s comoving-gauge f
NL
	​

≃(5/12)(1−n
s
	​

) as the “gauge-frame survey observable.” The cited conformal-Fermi analyses show instead that the leading single-field squeezed contribution is a coordinate effect and produces no primordial scale-dependent halo bias or observable squeezed correlation apart from projection effects. Thus the quoted factor of 146 is not an observable-to-observable SPHEREx comparison, and the separation between a “survey gauge frame” and a “physical theoretical frame” is conceptually wrong. The qualitative statement that an observed physical local signal of order −2 would disfavor standard single-field slow roll may remain, but Table II and the associated argument must be reformulated. 
arXiv
+1

[MAJOR] Section V—MegaMapper numerical outlook is uncalibrated by construction. Only the idealized σ(f
NL
	​

)≃0.5 input is externally anchored; the GR, magnification, b
ϕ
	​

, tracer, and design degradations are transferred from SPHEREx or chosen as placeholders despite the very different z=2–5 regime. A range assembled from qualitatively unrelated scenarios is not a forecast and should not appear in the abstract, conclusion, or detection plot. Either perform a dedicated high-redshift Fisher analysis or restrict this section to a qualitative outlook.

[MINOR] Scope, presentation, and reproducibility. The potentially publishable content is a concise correction of the canonical matter-contraction bispectrum polynomial. The Einstein–Cartan–Holst and fermion discussion, anomaly-selected tracers, cosmic-birefringence appendix, repeated mission-status material, and extensive restatement of caveats obscure that result. A revised work would need a frozen archival code release at submission, a compact analytic derivation of the unique corrected shape, and a separate, consistently formulated forecast analysis.

(3) No: the manuscript plausibly supports a corrected pre-bounce canonical-GR squeezed-limit value f
NL
	​

=−35/16, but it does not establish that this value survives the bounce or that SPHEREx or MegaMapper has the quoted sensitivity to it.
