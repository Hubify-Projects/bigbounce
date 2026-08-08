(1) VERDICT: REJECT.

(2) ISSUES:

[MAJOR] Section II A and Appendix A—polynomial reconstruction and claimed null-space uncertainty. Appendix A, Eq. (A4), supplies the complete vertex-summed polynomial and therefore fixes its coefficients uniquely. In the six-ordered-permutation basis defined in Section II, Eq. (A4) corresponds to (c
1
	​

,…,c
6
	​

)=(3,1,−9,5,−33,9), not the adopted (2,7,3,−12,−69,19). Consequently, the three-dimensional “physical null space,” its r=0.85±0.13 distribution, and the associated uncertainty budget are artificial: once the vertex calculation is accepted, three benchmark values are not the only information available. More seriously, the released null-space code constrains the coefficients to the superseded amplitudes −35/8,−255/64,−9/4, while the Fisher code uses the same old-shape coefficients and treats the correction as an overall factor of 1/2. This contradicts the manuscript’s own claim that the error is an additive local-shaped polynomial term rather than a global rescaling. All shape plots, overlaps, non-local-template projections, Fisher calculations, and significance numbers must be recomputed from the actual vertex-summed polynomial. 

ext_P2_M23

[MAJOR] Sections III B–IV, Eq. (5)—invalid hybrid template recast. The relation σ
bounce
	​

=σ
local
	​

/r is justified only when r is the cross-Fisher response F
local,bounce
	​

/F
local,local
	​

, evaluated with precisely the covariance and nuisance marginalization that produced σ
local
	​

. The quoted r=0.84 is instead obtained from a collection of uniform, CMB-like, scale-dependent-bias, and heuristic survey weights, none of which is the Heinrich et al. multi-tracer bispectrum covariance. Pairing this r with the externally imported σ
local
	​

=0.7 is therefore not a controlled Fisher projection. The later result r
eff
	​

≃0.99 in the manuscript’s own surrogate covariance confirms that 0.84 is not the SPHEREx estimator response. Calling the smaller number “conservative” does not convert it into a statistically defined forecast; the quoted 2.6–2.75σ baseline is consequently unsupported. Heinrich et al. provide the local-template σ(f
NL
	​

)≃0.7, but not the cross-template contraction needed for this recast. 
arXiv

[MAJOR] Section IV—“independent Fisher validation.” The in-house calculation is not sufficiently equivalent to the Heinrich analysis to validate the imported covariance or its nuisance marginalization. The released implementation uses one global logarithmic bias-amplitude nuisance, rather than independent tracer- and redshift-dependent bias parameters, and omits the b
2
	​

, b
s
2
	​

, non-Gaussian covariance, and other nuisance directions that determine a bispectrum forecast. Agreement of one scalar error bar at the 2–11% level can therefore be accidental and does not validate off-diagonal Fisher elements. The computation also uses the incorrect reconstructed bounce shape identified in Issue 1. The absolute 3.2–5.2σ results and r
eff
	​

≃0.99 cannot be presented as independent confirmation without a like-for-like nuisance model, convergence tests under those nuisances, and the corrected vertex shape.

[MAJOR] Section VII and Table V—GR and b
ϕ
	​

 “marginalized floor.” The correlation ρ=−0.868 is transferred from an f
NL
	​

–n
f
NL
	​

	​

 scale-dependent-bias power-spectrum Fisher calculation and then used as though it were the correlation between f
NL
	​

 and a relativistic galaxy-bispectrum template. There is no statistical or physical theorem supporting that substitution. Likewise, a geometry-only shape cosine ∣ρ∣≃0.95 cannot be inserted into σ
marg
	​

=σ
0
	​

/
1−ρ
2
	​

 unless it is computed in the same covariance, with a specified nuisance normalization and prior. The resulting 0.8–1.3σ values are not upper and lower bounds; they are unrelated scenarios. The manuscript’s channel-native surrogate instead gives a materially different correlation and significance, demonstrating rather than resolving the ambiguity. The abstract’s 1.3–2.75σ “post-systematics” interval must be removed or replaced by a single joint Fisher analysis with explicit GR, bias, selection, and photo-z responses.

[MAJOR] Section II C and the Conclusion—claimed cubic-order transmission bound. The assertion that one scalar degree of freedom guarantees nonlinear conservation of ζ, and hence bounds bounce-induced changes to δf
NL
	​

≲10
−3
, is not established. Single-field systems need not be attractors; matter contraction itself possesses a growing superhorizon curvature mode. Nonlinear conservation requires the relevant adiabatic/attractor and regularity conditions, not merely degree-of-freedom counting. The assumed kη
bounce
	​

∼10
−2
 is also not derived for the observable modes from a specified background solution. Existing linear transfer results do not determine the cubic transfer kernel, and LQC bounce dynamics can generate nontrivial non-Gaussianity. 
arXiv
+1
 Until a third-order calculation is supplied, faithful transmission must remain an unquantified model assumption; it cannot be described as “closed,” “derived,” or “bounded.”

[MAJOR] Appendix A.1(d)—incorrect interpretation of Cai et al.’s ϵ-grouped expressions. The standard in-in identity converting a commutator into twice an imaginary part is correct, but the manuscript’s claim that Cai et al.’s Eqs. (34)–(36) are undoubled single-time-ordering quantities is not. Cai et al. introduce the full in-in commutator and then explicitly describe Eqs. (34)–(36) as the summed contributions grouped by powers of ϵ, which are subsequently combined into their final polynomial. 
arXiv
 Thus Appendix A.1(d) does not provide an independent factor-of-two certification and should be removed. Moreover, the vertex sum, its ϵ-grouped rewrite, and benchmark evaluations are algebraically dependent checks, not three independent derivations; only the comparison with the independent general-c
s
	​

 calculation is genuinely external.

[MAJOR] Section II D—conflation of distinct bounce models. The manuscript describes a “Wilson-Ewing ΛCDM quasi-dust model” whose small tensor amplitude is attributed jointly to LQC tensor suppression and c
s
	​

≪1. Wilson-Ewing’s construction is a scalar-field LQC matter bounce and quotes r
t
	​

∼9×10
−4
, whereas the small-sound-speed ΛCDM bounce is a separate escape route discussed in the no-go literature. 
arXiv
+1
 This distinction is essential because the adopted −35/16 result is the c
s
	​

=1 limit of the general formula; inserting c
s
	​

≪1 changes f
NL
	​

 substantially. The manuscript must identify one consistent background, perturbation action, sound speed, quantization prescription, and tensor prediction rather than combining favorable properties of different models.

[MAJOR] Sections II C and VIII—quasi-dust correction and “consistency relation.” The range κ
ϵ
	​

=2.8–40 is not obtained from a calculation. Its upper endpoint is described as a schematic 14× enhancement of the prefactor contribution, with no mode-function integral, controlled expansion, or error analysis. It therefore cannot support a quoted 0.6–8% theoretical uncertainty, the interval f
NL
	​

∈[−2.175,−2.01], or the Gaussian theory priors used later. The four cubic vertices must be evaluated for the actual w=−0.003 background, including the changed mode functions and cancellations, or the finite-w correction must be reported as unknown. Equation (13) is presently a parametrization with an assumed coefficient range, not a derived matter-bounce consistency relation.

[MAJOR] Section VI—Bayes-factor headline. The reported BF≃9–14 is primarily an arbitrary prior-volume ratio. In the manuscript’s own broad-prior limit it reduces essentially to W/
2π
	​

σ
eff
	​

, so widening the competitor interval mechanically increases the claimed support for the bounce. The “tuned multifield” model is represented by a uniform prior directly on f
NL
	​

, rather than by physical model parameters and their induced prior-predictive distribution, while the mock observation is centered on the bounce prediction. The Monte Carlo exercises only reproduce this chosen analytic integral; they do not validate the model priors. These quantities may be retained as an explicitly labeled prior-volume illustration, but they do not constitute model-selection evidence and should not appear as a principal abstract or conclusion result.

[MINOR] Section VI A and Table II—gauge-frame terminology. A galaxy-survey observable is gauge invariant after the light-cone and relativistic projection terms are included; it is misleading to label the comoving-coordinate consistency-relation value as the “gauge-frame survey observable” and the conformal-Fermi result as merely theoretical. The paper should instead specify the conventional primordial f
NL
local
	​

 normalization used by the estimator and consistently map it into the observable galaxy statistics, including projection effects.

[MINOR] Overall scope and reproducibility. The manuscript is substantially longer than warranted by the supported result and repeatedly mixes the central arithmetic correction with tangential discussions of Einstein–Cartan torsion, anomaly-selected tracers, dark energy, cosmic birefringence, and speculative MegaMapper scenarios. A publishable resubmission should be reorganized around the exact vertex calculation and one correctly defined survey Fisher problem. Because many claims depend on named JSON outputs and mutable scripts, an immutable tagged archive containing the precise source, input tables, configuration files, and outputs used for the submitted PDF is also required rather than a future Zenodo DOI.

(3) No—the exact-dust algebra supporting f
NL
local
	​

=−35/16 is credible, but the central observational claim that SPHEREx can test a robustly transmitted matter-bounce prediction at the quoted significance is not supported.
