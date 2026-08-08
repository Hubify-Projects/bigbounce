(1) VERDICT: REJECT

(2) ISSUES:

[MAJOR] Appendix A, claimed Cai–Li factor-of-two resolution: the derivation contains mutually incompatible statements. The manuscript says Li et al.’s Eq. (4.19) at c
s
	​

=1 shares Cai et al.’s polynomial and gives −305/64, but direct substitution into Li et al.’s Eq. (4.19) gives −35/16, consistently with their Eq. (5.1). It also identifies Cai et al.’s Eqs. (34)–(36) as an undoubled, single-time-ordering result, whereas Cai et al. present them as the ϵ-order regrouping of the already-computed vertex contributions whose stated sum is Eq. (37). Finally, the diagnosis depends on whether the repeated-exponent (5,2,2) orbit is counted as six ordered tuples or three distinct monomials; the manuscript uses both conventions without deriving the necessary conversion from the original Wick contractions. Thus −35/16 may indeed be the correct direct-vertex value, but the claimed reconstruction of the literature error and the advertised “four certifications” are not presently self-consistent. 

ext_P2_W1

 
arXiv
+2
arXiv
+2

[MAJOR] Sec. II A and Appendix A, bispectrum shape reconstruction: Appendix A purports to give the complete corrected vertex-sum polynomial, so its six orbit coefficients must be uniquely fixed once the permutation convention is specified. Replacing that result by six coefficients inferred from only three benchmark triangles, creating an artificial three-dimensional null space, and sampling Euclidean balls in that space does not represent a physical uncertainty. The sampled shapes need not arise from any cubic action, and the resulting distribution is explicitly basis- and normalization-dependent. Moreover, Sec. II states that the overlap calculation uses Cai et al.’s printed shape even though the manuscript claims that shape contains an additive local-shaped error; such an additive term changes the shape overlap and cannot be repaired by rescaling the squeezed amplitude. The null-space uncertainties, r percentiles, and significance bands derived from this construction must therefore be discarded.

[MAJOR] Sec. II C, cubic-order transmission through the bounce: the claimed bound δf
NL
	​

≲10
−3
 is not derived. Having only one scalar degree of freedom does not imply 
ζ
˙
	​

=0 or nonlinear conservation of ζ; the matter-contracting phase used by the paper is itself a single-field non-attractor in which the super-Hubble curvature mode grows. A bounce can mix the growing and constant solutions even at k→0, so its effect is not generically suppressed by (kη
bounce
	​

)
2
. Neither kη
bounce
	​

≃10
−2
 nor the coefficient connecting that quantity to f
NL
	​

 is calculated. A model-specific second- and third-order perturbation evolution through the bounce is required before the contraction-era bispectrum can be identified with the observable post-bounce bispectrum.

[MAJOR] Secs. II C–D, identification and viability of the Wilson–Ewing model: the manuscript states that Wilson–Ewing uses a dressed-metric/hybrid prescription with Lorentzian c
s
2
	​

=1, but the cited work evolves scalar perturbations with the factor 1−2ρ/ρ
c
	​

, including its negative interval near the bounce; this is the deformed-algebra prescription that the manuscript treats as an alternative. Consequently, the proposed dressed-metric “closure” is not a closure of the cited model. The manuscript also invokes c
s
	​

≪1 as part of the same viable construction while importing the c
s
	​

=1 bispectrum; Li et al.’s formula shows that changing c
s
	​

 changes f
NL
	​

 dramatically. In addition, Wilson–Ewing obtains r≃9×10
−4
 and requires ρ
c
	​

∼10
−9
ρ
Pl
	​

 to normalize the scalar spectrum, whereas the manuscript quotes r∼10
−4
, omits the critical-density requirement, and claims no known tension. 
arXiv
+2
arXiv
+2

[MAJOR] Secs. III B and IV, template-response formalism: the response of a local-template estimator to a bounce template is

r
est
	​

=
F
LL
	​

F
LB
	​

	​

,

with F
LB
	​

 the covariance-weighted cross-Fisher element. By contrast, the manuscript’s “independent recovery factor”

r
eff
	​

=
σ
B
	​

σ
L
	​

	​

=
F
LL
	​

F
BB
	​

	​

	​


is only a ratio of template norms and is not an amplitude-recovery factor; the missing correlation is F
LB
	​

/
F
LL
	​

F
BB
	​

	​

. Therefore r
eff
	​

≃0.99 does not validate r=0.84. The ten schematic weights 1,k
2
,1/k
2
,… are also not substitutes for the SPHEREx multi-tracer covariance, and the text repeatedly calls r=0.84 a “cosine” despite separately reporting r
cos
	​

≃0.985. A single, channel-native calculation of F
LL
	​

, F
LB
	​

, and F
BB
	​

, with identical nuisance marginalization, is necessary.

[MAJOR] Sec. IV, claimed independent reproduction of Heinrich et al.: the comparison is not like-for-like. Heinrich et al.’s σ(f
NL
	​

)≃0.73 is already a full redshift-space Fourier-bispectrum forecast with triangle-orientation bins, sample-dependent photometric-redshift damping, and marginalization over cosmological parameters and linear biases. Their analysis also shows that photometric-redshift damping transfers information into higher and odd multipoles. The manuscript instead obtains 0.63–0.69 in a simpler real-space calculation with important bias and covariance terms held fixed, and then obtains 0.42–0.45 after adding RSD. The latter result is substantially tighter than the redshift-space result it is supposed to reproduce and is evidence that the pipelines are non-equivalent, not validation to “2–11%.” The associated r
eff
	​

 cannot be used until the same data vector, damping, parameter set, covariance, and marginalization as Heinrich et al. are implemented. 
arXiv
+3
arXiv
+3
arXiv
+3

[MAJOR] Sec. VII and Table V, systematic-error construction: the lower significance endpoints have no valid statistical derivation. The value ρ=−0.868 is taken from an f
NL
	​

–n
f
NL
	​

	​

 power-spectrum Fisher calculation and then reused as an f
NL
	​

–GR-projection correlation in a bispectrum calculation; these are different parameters, observables, kernels, and covariances. Likewise, an unweighted or k
2
-weighted shape cosine of 0.95 is not the marginalized Fisher correlation of the SPHEREx galaxy bispectrum. The formula σ
marg
	​

=σ
conditional
	​

/
1−ρ
2
	​

 is applicable only when both quantities come from the same Fisher matrix, including any nuisance prior. Consequently, neither the 1.3σ proxy floor nor the 0.8σ edge is supported, and adding GR, b
ϕ
	​

, photo-z, and other effects in quadrature does not produce a joint-covariance forecast.

[MAJOR] Secs. V and VIII, misuse of the bispectrum overlap in other channels: the factor r=0.84 is defined from a bispectrum-template projection, yet it is also applied to MegaMapper and DESI scale-dependent-bias constraints. Scale-dependent bias probes the squeezed response directly; for a template normalized by its squeezed f
NL
	​

, its response is not reduced by an intermediate- and folded-triangle bispectrum overlap. Planck likewise requires its own transfer-function and CMB-covariance inner product. The MegaMapper section additionally transfers an explicitly uncalibrated SPHEREx GR/b
ϕ
	​

 budget to z=2–5 and nevertheless quotes numerical detection ranges in the abstract and conclusions. Dedicated channel-specific forecasts are required.

[MAJOR] Secs. II C and VIII B, quasi-dust correction and proposed f
NL
	​

–n
s
	​

 relation: the range κ
ϵ
	​

=2.8–40 is not a calculation or a bound. Its upper endpoint is introduced through a schematic factor of approximately 14 multiplying the prefactor-only estimate, without evaluating the mode-function derivatives or the cancellations among the four vertices. Therefore the quoted 0.6–8% uncertainty, f
NL
	​

∈[−2.175,−2.01], and c
′
∈[0.35,5] consistency curve are unsupported. Since the cited viable background has w

=0, the four in-in integrals with the corresponding mode functions must be evaluated before the model can be said to predict a narrow f
NL
	​

 interval.

[MAJOR] Sec. VI, Bayesian model comparison: the reported Bayes factors are primarily the prior-volume expression W/
2π
	​

σ evaluated for mock data placed exactly at the bounce prediction. A uniform interval in the phenomenological parameter f
NL
	​

 is not a prior derived from a curvaton, QSFI, or generic multifield-inflation model, and the calculation omits those models’ actual parameters, correlations, other observables, and selection effects. Replacing σ by σ/r while retaining competitor priors in a different amplitude parametrization further makes the result prior-coordinate dependent. The Monte Carlo realizations only reproduce this assumed one-dimensional calculation; they do not validate physical model evidence. The abstract-level claim BF≃9–14 should be removed or explicitly labeled as a toy prior-volume illustration.

[MINOR] Headline numerical consistency: the stated 2.6–2.75σ range does not include the manuscript’s own full 8% quasi-dust correction. Using its quoted lower amplitude 2.01, lower overlap 0.829, and σ=0.7 gives approximately 2.38σ, not 2.6σ. The upper endpoint also uses a CMB-motivated weighting for an LSS survey. Table V alternately treats theoretical amplitude uncertainty as a numerator shift, a distributional scatter, and a quadrature error. All headline numbers require a single, consistently defined likelihood.

[MINOR] Organization and presentation: the manuscript reads as several response letters and audit logs merged into the article, with extensive repetition and phrases such as “honest,” “reviewers’ expectation,” and “at referee-report granularity.” The Einstein–Cartan–Holst discussion, anomaly-selected tracers, cosmic birefringence, speculative MegaMapper systematics, and AI-pipeline description are not needed to establish the stated result. Once the unsupported forecast and model-selection material are removed, the remaining potentially publishable contribution would be a much shorter, notation-clean derivation of the canonical matter-contraction bispectrum and its relation to the two earlier papers.

(3) No—the contracting-phase algebra is compatible with f
NL
	​

=−35/16, but the manuscript does not establish that this value survives the specified bounce or supports the quoted SPHEREx and MegaMapper sensitivities.
