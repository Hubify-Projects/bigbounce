VERDICT: REJECT 

ext_P2_FR1b

ISSUES:

[MAJOR] Section II.A and Appendix A—artificial polynomial “null space.” The manuscript cannot simultaneously claim an exact vertex-level derivation and treat the bispectrum polynomial as underdetermined by three benchmark configurations. Its own Eq. (A4) uniquely fixes the six coefficients: in the main text’s six-ordered-term convention they are (3,1,−9,5,−33,9), equivalently c
5
	​

=−66 when the three distinct (5,2,2) monomials are counted only once. The adopted set (2,7,3,−12,−69,19) is instead an arbitrary solution fitted to three triangles. A full-rank change of monomial basis cannot create a physical three-dimensional null space. Consequently, the 10,000-sample coefficient scan, the quoted r=0.85±0.13 distribution, the claimed null-space uncertainty, and every shape calculation based on those arbitrary coefficients must be discarded and recomputed from the exact vertex sum.

[MAJOR] Appendix A—factor-of-two resolution is internally contradictory and misidentifies the relevant algebraic step. Page 31 states that the shared printed polynomial reduces to −305/64, whereas page 33 states that the same polynomial reduces to −35/8. Appendix A.1(d) further asserts that Cai et al.’s Eqs. (34)–(36) are undoubled, single-time-ordering expressions, although the original paper presents them as contributions to the full shape that are subsequently summed. Li et al.’s independent final formula does give −35/16 at c
s
	​

=1, so the numerical correction is plausible, but the manuscript has not supplied a coherent account of which printed equation is erroneous, how the permutation convention is mapped, or how the alleged −(99/128)∑
i
	​

k
i
3
	​

 discrepancy relates to Cai et al.’s stated −35/8. The appendix must be rewritten as one self-contained derivation in a single convention, preferably accompanied by confirmation from the original authors. 
arXiv
+1

[MAJOR] Sections II.C–II.D—no internally consistent “viable model” is specified. The paper combines the canonical c
s
	​

=1 prediction f
NL
	​

=−35/16 with assertions that the Wilson–Ewing model uses c
s
	​

≪1, dressed-metric quantization, and r
t
	​

≃10
−4
. Wilson–Ewing’s calculation instead uses effective/lattice LQC dynamics and reports r
t
	​

 of order 9×10
−4
; the manuscript does not demonstrate that its dressed-metric model is the same theory. More importantly, Li et al.’s quoted result f
NL
local
	​

=−165/16+65/(8c
s
2
	​

) shows that adopting c
s
	​

≪1 radically changes the non-Gaussianity and is incompatible with retaining −35/16. The author must define one action, matter sector, sound speed, and LQC perturbation prescription, and derive all of n
s
	​

, r
t
	​

, and f
NL
	​

 within that same model. 
arXiv
+2
arXiv
+2

[MAJOR] Sections II.C, IX.E, and X—cubic transmission through the bounce is not bounded by δf
NL
	​

≲10
−3
. “Single clock” is a degree-of-freedom statement, not proof that 
ζ
˙
	​

=0; the contracting phase used here is explicitly non-attractor-like, with a growing super-Hubble curvature mode. Linear conservation or transfer does not establish second- or third-order transfer through a modified-gravity bounce, and the separate-universe argument requires dynamical adiabaticity conditions that are not demonstrated. Likewise, (kη
bounce
	​

)
2
 supplies only a formal gradient scaling, not a numerical bound without deriving the coefficient, mode matching, and the asserted kη
bounce
	​

≃10
−2
. The cubic transfer must either be calculated explicitly or retained as an uncontrolled model-dependent assumption; it cannot support the claims of UV-completion independence or a certified 10
−3
 systematic.

[MAJOR] Section III.B, Eq. (5)—the template-mismatch map is not the response of the SPHEREx estimator. For local and bounce templates T
L
	​

,T
B
	​

 with covariance C, the response of a local estimator is F
LB
	​

/F
LL
	​

, while the optimal bounce error is F
BB
−1/2
	​

, with F
ij
	​

=T
i
T
	​

C
−1
T
j
	​

. The manuscript instead uses an average of B
NL
	​

 under ad hoc weights such as 1, k
2
, and 1/k
2
. This quantity is neither estimator response nor forecasted uncertainty. The mutually different numbers r=0.84, r
cos
	​

≃0.985, and r
eff
	​

≃0.99 cannot be interchanged by calling one “conservative.” Without the channel-native multi-tracer covariance, the degradation from 3.13σ to 2.6–2.75σ is not derived.

[MAJOR] Section IV— the “independent Fisher validation” is not a like-for-like reproduction of Heinrich et al. Heinrich et al.’s published result is already a redshift-space, multi-tracer galaxy-bispectrum forecast with its own nuisance-parameter treatment. The manuscript obtains 0.63–0.69 from a real-space calculation and compares that to the published ≃0.7, but its purportedly corresponding redshift-space calculation gives 0.42–0.45, approximately 35–42% tighter than the published result. Thus the claimed 2–11% validation is produced by comparing different observables. Holding b
2
	​

 and b
s
2
	​

 fixed, using only diagonal Gaussian covariance, omitting non-Gaussian covariance and fingers-of-God effects, and adopting a different marginalization set further prevent validation. The published local-template Fisher result must first be reproduced with the same redshift-space kernels, triangle cuts, covariance, tracer definitions, and nuisance parameters before the bounce template is substituted. 
arXiv
+1

[MAJOR] Section VII and Table V—the quoted 1.3σ and 0.8σ systematic floors have no statistical basis. The value ρ=−0.868 is transferred from an f
NL
	​

–n
f
NL
	​

	​

 correlation in a scale-dependent-bias power-spectrum Fisher matrix to an unrelated f
NL
	​

–GR-amplitude pair in the bispectrum. The alternative ∣ρ∣≃0.95 is a geometry-only template overlap without the bispectrum covariance. Neither is an upper or lower bound on the channel-native Fisher correlation. Similarly, adding GR “errors” in quadrature and replacing σ
0
	​

 by guessed b
ϕ
	​

-degraded values of 0.9 or 1.0 is not nuisance marginalization; Heinrich et al.’s baseline imposes bias relations rather than the manuscript’s asserted 20%, 30%, and 50% prior sequence. Until a joint observed-bispectrum Fisher calculation is performed, the advertised 1.3–2.75σ envelope should not appear as a quantitative forecast. 
arXiv

[MAJOR] Section VI and Tables III–IV—the Bayes factors are prior-volume constructions, not evidence against physical inflationary models. The calculation compares a point or narrow Gaussian bounce prior with an arbitrary uniform interval in the single phenomenological parameter f
NL
	​

, while placing the mock observation exactly at the bounce prediction. In the broad-prior limit the result is essentially W/
2π(σ
eff
2
	​

+σ
theory
2
	​

)
	​

, so the claimed preference increases linearly with the freely selected competitor width W. No curvaton, multifield, or quasi-single-field parameter likelihood is evaluated, and no inflationary prior predictive distribution is derived. The Monte Carlo exercises merely reproduce the same analytic prior-volume factor. The BF≃9–14 claim must be removed from the abstract and conclusions or relabeled strictly as a toy prior-sensitivity illustration.

[MAJOR] Sections II.C and VIII.B—the quasi-dust correction and f
NL
	​

–n
s
	​

 consistency relation are not derived. The range κ
ϵ
	​

=2.8–40 rests on an asserted “approximately 14×” mode-function enhancement, with no evaluation of the four in-in integrals and no controlled error estimate. It therefore does not establish a 0.6–8% uncertainty, the interval f
NL
	​

∈[−2.175,−2.01], or Eq. (13). These quantities are subsequently used to characterize the prediction as precise and to choose the Bayesian theory prior. They must be computed from the quasi-dust mode functions and cubic action or removed.

[MINOR] Section VI.A and Table II—observer-frame interpretation is misleading. SPHEREx measures a gauge-invariant observed galaxy correlation including light-cone and projection terms, not a bare “gauge-frame f
NL
	​

.” The conformal-Fermi-coordinate discussion cannot be separated into “survey observable” and “physical theoretical” rows as written. The comparison with single-field consistency relations should be reformulated directly at the level of the observed galaxy bispectrum; the qualitative statement that an order-unity negative local signal would be incompatible with ordinary single-field slow-roll inflation can remain.

The isolated algebraic correction f
NL
	​

=−35/16 is plausible, but the central claim that it is a robust prediction of a specified viable bounce model testable by SPHEREx at 1.3–2.75σ with Bayes factor 9–14 is not supported.
