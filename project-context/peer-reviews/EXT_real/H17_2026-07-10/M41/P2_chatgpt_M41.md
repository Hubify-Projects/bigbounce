VERDICT: REJECT

ISSUES:

[MAJOR] Appendix A, “Resolution of the Cai–Li Factor of Two”: The direct four-vertex sum appears to support f
NL
local
	​

=−35/16, but the manuscript’s account of Li et al. is algebraically incorrect. Setting c
s
	​

=1 in Li et al. Eq. (4.19) gives the corrected vertex-sum polynomial: its explicit −99/128∑
i
	​

k
i
3
	​

 term supplies precisely the contribution missing from Cai et al.’s printed combined expression. It therefore does not agree coefficient-for-coefficient with Cai et al.’s erroneous polynomial and does not reduce to −305/64, contrary to repeated statements in the manuscript. The text is also internally contradictory in calling Cai Eq. (37) “the only object that yields −35/8” while correctly observing elsewhere that the printed coefficients instead yield −305/64. The historical and algebraic narrative must be rewritten around the actual relation among Cai’s vertex sum, Cai’s printed polynomial, Cai’s separately quoted benchmark values, and Li’s result. 

ext_P2_M41

 
arXiv
+2
arXiv
+2

[MAJOR] Section II A, polynomial reconstruction and “null-space uncertainty”: Appendix A already supplies the exact summed polynomial, so its coefficients are fixed by the four cubic vertices and are not to be inferred from three benchmark configurations. In the six-ordered-orbit convention, the vertex-sum coefficient vector is proportional to (9,3,−27,15,−99,27); equivalently, Eq. (A4) has coefficient −198 on the three distinct (5,2,2) monomials. The adopted vector (2,7,3,−12,−69,19) is merely one interpolation through three values and is not demonstrated to be a basis transformation of the physical vertex sum. Consequently, the three-dimensional “physical null space,” the 10,000-vector scan, the r=0.85±0.13 distribution, and the claimed basis-independent shape stability do not represent theoretical uncertainty in the matter-bounce bispectrum and must be removed or recomputed from the unique vertex-derived shape. 
GitHub

[MAJOR] Section III B, template-recovery factor r=0.84±0.02: The relevant amplitude response is F
local,bounce
	​

/F
local,local
	​

, evaluated with the actual survey transfer functions, triangle measure, tracer covariance, redshift dependence, and the exact physical bounce template. Uniform shape averages and weights such as powers of k are not substitutes for that Fisher projection, and the cited analysis code inserts several “noise-weighted” numerical values rather than deriving them from a SPHEREx multi-tracer covariance. There is also no theorem making the resulting flat/intermediate-triangle-weighted value a conservative lower bound. Thus Eq. (5) is formally reasonable, but the value of r used in every headline significance is not established. 
GitHub
+1

[MAJOR] Section IV, “independent bispectrum Fisher validation”: The released Fisher code uses the same non-vertex-derived coefficient vector (2,7,3,−12,−69,19), normalizes its squeezed value by hand, and therefore does not validate the corrected physical template. It also uses a comparatively coarse internally generated triangle grid and a simplified tree-level Gaussian covariance, while holding important nonlinear-bias parameters fixed and omitting several components of the Heinrich et al. analysis. Reproducing one scalar uncertainty, σ(f
NL
	​

)≃0.7, within 2–11% does not validate the off-diagonal covariance, template response, or nuisance marginalization. The claimed r
eff
	​

≃0.99 therefore cannot be used to certify the r=0.84 recast. 
GitHub
+1

[MAJOR] Sections II C–D, consistency of the “viable Wilson–Ewing model”: The paper imports the canonical c
s
	​

=1 cubic-action result while also invoking c
s
	​

≪1 matter as an essential ingredient of the viable low-tensor bounce/escape route. These are not interchangeable models. Li et al. find

f
NL
local
	​

=−
16
165
	​

+
8c
s
2
	​

65
	​

,

so the small-c
s
	​

 regime produces an enormous, generally positive non-Gaussianity and underlies their extended no-go result. The manuscript must specify a single action and matter clock that generate the scalar perturbations, and compute the scalar bispectrum and tensor suppression consistently in that same model; it cannot combine the c
s
	​

=1 bispectrum with a low-c
s
	​

 viability argument. 
arXiv
+1

[MAJOR] Section II C, claimed cubic-order transmission bound δf
NL
	​

≲10
−3
: A single scalar degree of freedom does not by itself imply 
ζ
˙
	​

→0 or nonlinear conservation of ζ; an attractor solution is additionally required. Indeed, the matter-contraction mechanism used here relies on the dominant super-Hubble mode of ζ growing rather than being conserved. Linear propagation of the power spectrum through an effective LQC bounce does not establish conservation of the three-point function, nor does degree-of-freedom counting determine the coefficient of nonlinear gradient corrections through the quantum-gravity regime. The stated 10
−4
 transmission error and 10
−3
 bound on f
NL
	​

 are therefore assertions, not derived bounds. A nonlinear calculation in the specified dressed-metric theory is required, or faithful cubic transfer must remain an unquantified model assumption. 
arXiv
+1

[MAJOR] Sections II C and VIII B, quasi-dust correction: The quoted 0.6–8% correction and κ
ϵ
	​

∈[2.8,40] are not obtained from a controlled expansion. The upper endpoint is introduced through a schematic 14× enhancement of one contribution, without evaluating the four in-in integrals or their cancellations. These numbers cannot be presented as a theoretical error interval, propagated into the forecast, or used to justify the Gaussian theory prior in the Bayesian analysis. The calculation must be performed for w=−0.003, or the correction should be reported as unknown.

[MAJOR] Section VII, GR-projection marginalization: The adopted GR template is not a relativistic observed-galaxy bispectrum kernel. In the released implementation, the purported squeezed enhancement is represented by (k
min
	​

/k
max
	​

)P
a
	​

P
b
	​

, which tends to zero in the squeezed limit—the opposite of the enhancement described in the text—and it contains no line-of-sight, redshift, evolution-bias, magnification-bias, or wide-angle dependence. Correlations of 0.95, the 0.8σ lower edge, and the subsequent “channel-native” Fisher result derived from this template therefore have no physical interpretation. Transferring ρ=−0.868 from a power-spectrum running analysis to a bispectrum GR nuisance is likewise unjustified. 
GitHub
+1

[MAJOR] Section VII E and Table V, combined 1.3–2.75σ range: The table mixes multiplicative signal losses, assumed replacements of the baseline error, additive Gaussian noise terms, inverse-Fisher correlations, and endpoints obtained under different null procedures. It is not a cumulative likelihood or a joint marginalized forecast, and the assumed changes σ(f
NL
	​

):0.7→0.9 or 1.0 under b
ϕ
	​

 relaxation are not derived from the stated bispectrum Fisher matrix. Consequently, 1.3–2.75σ is not a statistical confidence range and should not be quoted as the realistic SPHEREx sensitivity. Heinrich et al. explicitly leave full GR, wide-angle, window-function, and non-Gaussian-covariance treatments to future work, so those effects cannot be converted into numerical SPHEREx errors by the present quadrature prescription. 
arXiv
+2
arXiv
+2

[MAJOR] Section VI C, Bayesian model comparison: The reported Bayes factors are not evidences for the matter bounce versus defined inflationary models. They compare a point or phenomenological Gaussian prior on f
NL
	​

 with an arbitrarily chosen uniform interval labelled “multifield inflation”; in the broad-prior limit the result is essentially the prior-volume factor W/(
2π
	​

σ). Generating mock measurements at exactly the bounce prediction and reproducing the same closed-form integral by Monte Carlo validates numerical integration, not model discrimination. Actual curvaton and quasi-single-field models require priors on their Lagrangian parameters and a joint likelihood for all relevant observables and shapes. The BF≃9–14 claim should be removed from the abstract and conclusions unless such an analysis is supplied.

[MAJOR] Section IV, Eq. (7), and Section VII D, unmodelled covariance and photo-z claims: The estimate δC/C∼f
NL
2
	​

Δ
ζ
2
	​

/N
modes
	​

 is not a derivation of the galaxy-bispectrum covariance and cannot support the numerical assertion that shifting the Fisher fiducial to f
NL
	​

=−2.1875 changes the error by at most 5×10
−4
. The connected galaxy six-point function contains bias, gravitational, shot-noise, binning, and window contributions absent from this expression. Similarly, the claimed 5% degradation from a 10% catastrophic-outlier fraction and the 10–20% gain from anomaly-selected tracers are not produced by a documented survey Fisher calculation. Heinrich et al. themselves note that non-Gaussian covariance could alter the f
NL
	​

 constraint. 
arXiv

[MINOR] Section V and the abstract, MegaMapper outlook: The manuscript explicitly acknowledges that its MegaMapper systematic budget is transferred from SPHEREx without a high-redshift GR kernel, finalized survey design, or calibrated tracer model. Numerical post-systematic ranges such as 1.5–3.5σ should therefore not appear as forecast results; only the externally anchored idealized sensitivity may be quoted, clearly as a design study.

[MINOR] Sections VI A, IX, Appendix B, and overall presentation: The identification of a coordinate “gauge-frame” primordial amplitude as the direct on-sky observable is too simplistic because galaxy surveys measure gauge-invariant observed number counts including relativistic projection terms. More generally, the 37-page manuscript is highly repetitive and contains substantial material unrelated to the stated recast—Einstein–Cartan torsion, anomaly-selected galaxies, cosmic birefringence, repeated scope statements, and AI-pipeline documentation. A publishable version would need to be reorganized as a focused paper on the −35/16 algebraic correction, with the survey forecast included only after the physical template and covariance analysis are redone.

CENTRAL CLAIM: No—the canonical c
s
	​

=1 contracting-phase vertex sum supports f
NL
local
	​

=−35/16, but the claimed bounce-wide robustness, SPHEREx significance, and Bayes factors do not follow from the analysis presented.
