# EXT Review — P2 × ChatGPT
- paper: P2
- version: v1.7.92
- reviewer: ChatGPT
- model: Pro Extended (Pro thinking)
- timestamp: 2026-07-06T18:51:50Z
- chat_url: https://chatgpt.com/c/6a4bf780-e5e0-83e8-8e68-4e06a5b47766
- pdf: /tmp/round_P2.pdf

## Raw verbatim response

(1) VERDICT: REJECT.

(2) ISSUES:

[MAJOR] Appendix A / claimed Cai–Li factor-of-two resolution: the decisive algebra is internally inconsistent. With the manuscript’s own normalization f
NL
	​

=10A/(3∑
i
	​

k
i
3
	​

), an added +(99/128)∑
i
	​

k
i
3
	​

 term changes f
NL
	​

 by +(10/3)(99/128)=+165/64, not by the −35/16 required to move −35/16 to −35/8; if the “exact vertex sum” were −35/16, the printed polynomial described here would give +25/64, not −35/8. This invalidates the paper’s central arithmetic explanation. 

round_P2

[MAJOR] Appendix A.1 / “vertex-by-vertex certification”: the manuscript says the archived notebook implements only operator structures and permutation factors and does not evaluate the conformal-time integrals, yet the claimed correction requires the actual four-vertex in-in integrals and their squeezed limits. This is not a derivation of the numerical amplitude. 

round_P2

[MAJOR] Sec. II / bispectrum polynomial and null space: the paper first claims to use the Cai et al. bispectrum shape, then says Cai’s printed coefficients cannot be transplanted into the author’s basis and instead fixes six coefficients from only three benchmark triangles, leaving a three-dimensional null space. A cubic-action calculation should fix the polynomial coefficients; treating the resulting underdetermination as a basis-dependent “systematic” means the actual shape, and hence the quoted overlap r, has not been derived. 

round_P2

[MAJOR] Sec. II C and Sec. IX E / cubic transmission through the bounce: the manuscript upgrades a linear-order result into “transmission =1±O((kη
bounce
	​

)
2
)” at cubic order by degree-of-freedom counting and single-clock arguments. This is not sufficient for a nonsingular bounce with nontrivial constraint evolution, possible LQC correction terms, gauge/boundary contributions, and a contracting phase in which ζ is explicitly said to grow on superhorizon scales; a second-/third-order perturbation calculation through the bounce is still required. 

round_P2

[MAJOR] Secs. III B–IV / SPHEREx significance forecast: the headline 2.6–2.75σ and 1.3–2.75σ results are not an independent forecast but a scalar rescaling of a single external local-template Fisher error, with no bounce-fiducial multi-tracer bispectrum Fisher matrix, no derivative of the galaxy bispectrum with respect to the bounce template, and no survey covariance for the non-local tails. The manuscript itself acknowledges this limitation, so the result should not be presented as a PRD-level quantitative forecast. 

round_P2

[MAJOR] Sec. III B / template-overlap factor r: the recovery factor is obtained from ad hoc shape weights, a Euclidean triangle-grid cosine, CMB-like ℓ-space checks, and a two-dimensional KSW-style injection test, none of which is the SPHEREx three-dimensional multi-tracer galaxy-bispectrum estimator with realistic redshift bins, window functions, bias covariance, and shot noise. A scalar r=0.84 cannot substitute for the actual cross-Fisher matrix. 

round_P2

[MAJOR] Sec. VII / systematic budget: the post-systematic range is built by additive quadrature of heterogeneous effects and by importing a power-spectrum/SDB correlation coefficient as a proxy for bispectrum GR marginalization. This is not a joint nuisance-marginalized bispectrum forecast, and the paper gives no calculation showing that the adopted b
ϕ
	​

, GR, photo-z, and nonlinear-bias degradations are valid for the Heinrich et al. bispectrum covariance. 

round_P2

[MAJOR] Sec. VI / Bayesian comparison: the quoted Bayes factors are dominated by arbitrary prior-volume choices in a point-prediction-versus-uniform-prior exercise; the Monte Carlo ensembles only validate a closed-form likelihood integral and do not supply independent evidence. The comparison to “tuned multifield” models is therefore not a robust model-selection calculation and should not be part of the central claim. 

round_P2

[MAJOR] Secs. VII–IX and Figs. 4–5 / unresolved internal inconsistencies: large parts of the manuscript still use the discarded −35/8 amplitude and the corresponding 5.2–5.5σ or 2.6–5.5σ ranges, while the abstract and Table VI say the corrected headline is 2.6–2.75σ before systematics and 1.3–2.75σ after systematics. These are not harmless typographical errors; they occur in figures, captions, Sec. VII.B, Sec. IX.A, and Sec. IX.D. 

round_P2

 

round_P2

 

round_P2

[MAJOR] Sec. IX.D / SDB forecast hierarchy: the manuscript states that the SDB running Fisher is subordinate, but then says the paper’s headline remains the “bispectrum-only 5.2–5.5σ” result, contradicting the corrected-amplitude headline. This makes the stated channel hierarchy and numerical conclusions unreliable. 

round_P2

[MINOR] Sec. V / MegaMapper outlook: the MegaMapper discussion applies SPHEREx-like systematics and quotes broad significance envelopes for an unfunded, not-finalized concept without an instrument-specific covariance, selection function, or relativistic-projection treatment. This should be reduced to a qualitative outlook, not a forecast. 

round_P2

[MINOR] Secs. I, VI, and X / gauge-frame versus CFC-frame language: the manuscript partly corrects itself by saying the estimator measures gauge-frame local f
NL
	​

, but still uses physical-frame squeezed-limit language as a discriminator. The CFC statement is not an observable forecast for SPHEREx and should be removed or confined to a short theoretical comment. 

round_P2

[MINOR] Sec. IX.E / extraneous material: the cosmic-birefringence paragraph, anomaly-selected tracer discussion, and broad model-building remarks are not used in the calculation and introduce unsupported distractions into an already overlong manuscript. 

round_P2

[MINOR] Data and code availability: central numerical claims rely on named scripts and JSON artifacts, but the manuscript leaves the Zenodo DOI as “inserted at submission” and does not make the referee-facing record self-contained. For a result hinging on algebraic correction and custom Fisher/bookkeeping scripts, the exact code archive must be fixed and citable at submission. 

round_P2

(3) The central claim is not supported by the evidence presented because the corrected amplitude derivation is algebraically inconsistent, the cubic bounce transmission is not actually computed, and the SPHEREx sensitivity is only a heuristic rescaling of an external local-template forecast rather than a bounce-template Fisher analysis.
