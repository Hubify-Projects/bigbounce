(1) VERDICT: REJECT

(2) ISSUES:

[MAJOR] Appendix A, claimed resolution of the Cai–Li discrepancy: The value −35/16 may be correct, but the manuscript does not establish its claimed provenance in a convention-stable way. Section II defines ∑
i

=j

=l
	​

 as six ordered permutations, whereas Eq. (A4) introduces a three-monomial Σ
dist
(5,2,2); the alleged −(99/128)∑
i
	​

k
i
3
	​

 discrepancy is numerically tied to this multiplicity change and therefore requires a single explicit monomial-by-monomial comparison in one fixed basis. More seriously, Appendix A.1(d) claims that Cai et al.’s Eqs. (34)–(36) are single-time-ordered expressions awaiting an additional commutator doubling, although Cai et al. already include the complex-conjugate contribution and state that Eqs. (34)–(36) add directly to Eq. (37); this also contradicts the manuscript’s repeated statement that time ordering is not the source of the discrepancy. 

ext_P2_CN1

 
arXiv
+2
arXiv
+2

[MAJOR] Section II A, polynomial “null-space uncertainty”: Once the four cubic vertices have been summed, the full momentum polynomial is fixed; there is no physical three-dimensional null space. In the six-ordered-orbit basis defined in Section II, Eq. (A4) corresponds to coefficients proportional to (3,1,−9,5,−33,9), not the fitted vector (2,7,3,−12,−69,19). Sampling arbitrary coefficient vectors that reproduce only the squeezed, equilateral, and folded values generates shapes not derived from any cubic action, so the reported r=0.85±0.13, its percentile floors, and the claimed basis-independent robustness do not represent theoretical uncertainty. All overlap calculations must instead use the unique vertex-derived polynomial.

[MAJOR] Sections II–III, treatment of the corrected shape: The identified correction is an additive local-shaped term, not an overall multiplicative factor. Consequently, taking “the Cai shape normalized to exactly one-half” of the published amplitude, as done in Fig. 1 and the benchmark discussion, is not justified by Eq. (A2). Agreement at three configurations does not prove that the entire corrected shape is one-half of the previously plotted shape. The full vertex-summed function must be evaluated on every triangle before any template overlap is quoted.

[MAJOR] Sections III B and IV, SPHEREx template recast: Multiplying the published σ(f
NL
	​

)=0.7 by a primordial-shape recovery factor 1/r is not a valid recast of the Heinrich et al. galaxy-bispectrum Fisher matrix. That forecast includes the primordial bispectrum, PNG-induced bias operators, redshift-space kernels, tracer-dependent photometric-redshift damping, second-order bias, and the full multi-tracer covariance; much of its f
NL
	​

 information is therefore not weighted by the primordial shape inner product used to obtain r=0.84. A correct response is the survey-specific cross-Fisher F
local,bounce
	​

/F
local,local
	​

, not an average under heuristic weights such as 1, k
2
, or 1/k
2
. Heinrich et al.’s published setup and baseline are explicitly redshift-space, multi-tracer, and photo-z dependent. 
arXiv

[MAJOR] Section IV, contradiction between r=0.84 and r
eff
	​

≃0.99: The manuscript’s own purported survey Fisher gives r
eff
	​

≃0.99, demonstrating that the headline r=0.84 is not the response of the SPHEREx estimator. Calling the latter “deliberately conservative” does not turn it into a forecast quantity, and the resulting 2.6–2.75σ significance has no well-defined likelihood interpretation. The manuscript must either use a validated full cross-Fisher result or present no quantitative template-corrected significance.

[MAJOR] Section IV, claimed independent-Fisher validation: The validation is not like-for-like. The real-space calculation happens to return 0.63–0.69, whereas the manuscript’s redshift-space extension returns 0.42–0.45, substantially tighter than the already-redshift-space published result 0.7. At the same time, b
2
	​

 and b
s
2
	​

 are fixed, the covariance is Gaussian and diagonal in triangle space, and the text does not demonstrate parity with Heinrich et al.’s sample-dependent photo-z damping, stochastic terms, nuisance set, and orientation binning. Reproducing one final number after changing the observable and nuisance assumptions is not a validation; intermediate Fisher blocks and identical-assumption benchmarks are required.

[MAJOR] Section II C, “closure” of cubic-order transmission: The inference “single scalar degree of freedom ⇒
ζ
˙
	​

=0 ⇒ bispectrum conserved to O(k
2
)” is false in the background under study. The manuscript itself relies on the non-attractor growing solution ζ∝∣η∣
−3
, which evolves at k=0 despite the system being single-field. Degree-of-freedom counting therefore does not eliminate the second adiabatic mode or establish nonlinear conservation through the bounce. Linear transfer does not bound the cubic transfer coefficient, and the claimed δf
NL
	​

≲10
−3
 requires an explicit second-/third-order LQC calculation rather than a separate-universe assertion.

[MAJOR] Sections II C–D, misidentification of the Wilson–Ewing model: Reference [2] is not the “dressed-metric/hybrid, Lorentzian c
s
2
	​

=1, low-CDM-sound-speed ΛCDM bounce” described in the manuscript. It uses a holonomy-corrected Mukhanov–Sasaki equation with gradient coefficient 1−2ρ/ρ
c
	​

, discusses the associated near-bounce difficulties, and reports r≃9×10
−4
, not 10
−4
; it does not contain the claimed low-c
s
	​

 CDM mechanism. Thus the model supplying the linear transfer and tensor suppression is not the model for which the canonical c
s
	​

=1 cubic action is evaluated. If a genuinely small scalar sound speed is invoked, the cited general-c
s
	​

 formula itself predicts a large, generally positive non-Gaussianity rather than −35/16. 
arXiv
+3
arXiv
+3
arXiv
+3

[MAJOR] Sections II C and VIII, quasi-dust correction: The quoted 0.6–8% correction and κ
ϵ
	​

∈[2.8,40] are not calculated uncertainties. The upper endpoint is introduced through an unsupported schematic factor of approximately 14, and neither the sign nor the correlated shape change is derived. Since the advertised viable model has w=−0.003, the exact-w=0 result cannot be promoted to a precision prediction for that model until the four vertices are recomputed with the quasi-dust mode functions.

[MAJOR] Section VII and Table V, systematic-error construction: The 1.3–2.75σ envelope mixes incompatible statistical objects. The formula σ
marg
	​

=σ
fixed
	​

/
1−ρ
2
	​

 is valid only when ρ and σ
fixed
	​

 come from the same Fisher matrix, yet the manuscript combines a power-spectrum SDB correlation ρ=−0.868 with a bispectrum error 0.7. GR light-cone effects are also not a single redshift-independent template amplitude that can be added in quadrature. After obtaining a channel-native result with ρ≃−0.001 and a 2.5σ significance, the manuscript nevertheless retains the unrelated 1.3σ proxy as its headline floor, while the conclusion simultaneously states that no full joint bispectrum Fisher was performed. This is not a conservative confidence interval; it is a collection of noncommensurate scenarios.

[MAJOR] Section VI, Bayes factors: The reported BF≃9–14 is almost entirely an imposed prior-volume ratio. The mock observation is placed exactly at the bounce prediction, the competitor is assigned an arbitrary uniform interval, and in the broad-prior limit the result reduces to W/(
2π
	​

σ), independent of where the detection occurs. The Monte Carlo ensembles merely reproduce this analytic construction and do not constitute independent model validation. A meaningful comparison requires evidences induced by explicit inflationary and bounce model parameters, shared nuisance parameters, the bispectrum shape, n
s
	​

, and survey selection effects; otherwise the Bayes-factor headline should be removed.

[MAJOR] Section V, MegaMapper outlook: Every post-systematic MegaMapper number is obtained by transferring an explicitly uncalibrated SPHEREx budget to a qualitatively different z=2–5 survey, and the quoted 1.5–3.5σ envelope even includes an ad hoc midpoint of the ideal and degraded cases. Since MegaMapper appears in the title, either a dedicated high-redshift Fisher analysis including Doppler, potential, lensing-magnification, evolution-bias, window, and b
ϕ
	​

 nuisance terms is required, or all quantitative MegaMapper significance claims must be removed.

[MINOR] Appendix A.1, Eqs. (A7)–(A12): Equation (A7) contains −i⟨[Q,H
int
	​

]⟩, Eq. (A8) evaluates +i⟨[Q,H
int
	​

]⟩, and Eq. (A12) then adopts a −2Im convention without consistently tracking the sign from H
int
	​

=−L
int
	​

. The operator identity should be rewritten with one convention throughout.

[MINOR] Organization and reproducibility: The manuscript repeatedly alternates among r=0.84, r
eff
	​

=0.99, and r
cos
	​

=0.985, and among 0.8σ, 1.3σ, 2.5σ, and 3.5–5.2σ sensitivities, while presenting each in overlapping “headline” language. The numerical work also lacks an immutable archive, exact commit identifier, and DOI at submission. A publishable version should separate the potentially useful algebraic correction into a concise derivation and place any independently validated survey forecast in a distinct analysis.

(3) No—the manuscript gives credible evidence that the idealized canonical w=0, c
s
	​

=1 squeezed-limit algebra yields f
NL
	​

=−35/16, but it does not support the stronger claim that this is a robust prediction of the stated LQC model or that SPHEREx/MegaMapper will test it at the quoted significances and Bayes factors.
