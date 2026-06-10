# EXT1 P2 — Gemini 3.5 Thinking referee report
**Provider**: gemini.google.com web app · model **3.5 Thinking**
**Chat**: https://gemini.google.com/app/c01bc000d0305271
**PDF**: paper2_fnl_forecast_v1.7.48.pdf (md5 4cb0963e) · **Harvested**: 2026-06-10T17:05 PDT

---

Gemini said
Referee Report

Manuscript Title: Testing the Matter Bounce with Primordial Non-Gaussianity: SPHEREx Forecasts, with a MegaMapper Outlook   
PDF

Author: Houston Golden (Independent Researcher)   
PDF

Journal Target: Physical Review D / JCAP

1. Recommendation

MINOR REVISIONS. This manuscript presents a highly thorough sensitivity recast of next-generation Large-Scale Structure (LSS) surveys (specifically SPHEREx and MegaMapper) to constrain the primordial non-Gaussianity (f
NL
	​

) signature of the quasi-dust matter bounce scenario. The paper succeeds in resolving a long-standing factor-of-two normalization discrepancy in the literature between historical derivations. It also provides the first rigorous quantification of the template mismatch between the true matter-bounce bispectrum and the standard local template.  
PDF
+ 4

The paper is exceptionally transparent regarding its assumptions and structural dependencies . However, a few methodological assumptions regarding Fisher matrix shift-invariance and the physical boundary of the null-space exploration must be clarified before publication.  
PDF

2. BLOCKERS (Must fix before publication)
Fisher Shift-Invariance Near Large Non-Zero Fiducial Values

Section/Line: Section IV,   
PDF

Issue: The analysis adopts the baseline error projection σ(f
NL
	​

)≈0.7 from Heinrich et al. 2024, which was computed around a Gaussian fiducial model of f
NL
	​

=0. The author notes that shifting this to the bounce fiducial of f
NL
	​

=−4.375 relies on the assumption that the Fisher matrix is approximately invariant under fiducial shifts.  
PDF

Proposed Fix: While standard, this assumption is structurally non-trivial for local-type non-Gaussianity because a non-zero f
NL
	​

 introduces substantial scale-dependent corrections directly into the galaxy power spectrum and bispectrum covariances via higher-order loops and trispectrum terms. The author must include a quantitative scaling argument or a bounding expression proving that the multi-tracer covariance matrix does not degrade significantly when evaluated at f
NL
	​

∼−4.4.

Basis-Dependence of the Null-Space Coefficient Scan

Section/Line: Section II.A,   
PDF
+ 2

Issue: To evaluate the impact of the 3-dimensional polynomial underdetermination, the author uniformly samples 10,000 valid coefficient sets within a ball of radius 50 in null-space coordinates centered on the reference solution. As explicitly conceded in the text, this uniform Euclidean measure is entirely basis-dependent and not invariant under linear reparameterizations.  
PDF
+ 2

Proposed Fix: To elevate this from an indicative convention check to a physically robust constraint, the author should bound the scan volume using microphysical constraints. Specifically, the range of the polynomial coefficients c
1
	​

 through c
6
	​

 should be bounded by the theoretical limits of the matching conditions or action vertices from the underlying contracting phase action, rather than an arbitrary geometric radius.

3. MAJORS (Should fix)
Quantifying the Fermion Suppression Bound

Section/Line: Section II.C,   
PDF
+ 2

Issue: Assumption (f) notes that the fermion energy density during contraction must be negligible to suppress the Hehl-Datta-Mercuri four-fermion contact term ⟨
ψ
	​

γ
5
γ
a
ψ⟩
2
, which would otherwise source torsion and reactivate the Barbero-Immirzi parameter in the scalar cubic action. The text states that models with significant fermion sectors require an explicit bound on this operator.  
PDF
+ 3

Proposed Fix: Provide at least a schematic or order-of-magnitude analytical bound for ρ
fermion
	​

/ρ
scalar
	​

 during the contracting phase that is required to keep the resulting f
NL
	​

 corrections below the 8% extreme systematic floor of the e-correction budget.  
PDF
+ 1

Light-Cone and Magnification Degradation at High Redshift

Section/Line: Section V & VII.D,   
PDF
+ 1

Issue: For the MegaMapper outlook, relativistic projection effects and lensing magnification bias become severe at z>2, creating a spurious 1/k
2
 signal that mimics local f
NL
	​

. The systematic budget groups these under an estimated O(10−30%) degradation factor.  
PDF
+ 2

Proposed Fix: Expand the discussion in Section V to explicitly detail the expected degradation on the scale-dependent bias (SDB) channel versus the bispectrum channel for the Lyman-break galaxy sample. Because SDB is a 2-point statistic, it is far more vulnerable to lensing magnification than the 3-point galaxy bispectrum. This distinction needs to be mathematically emphasized.  
PDF
+ 3

4. MINORS (Polish)
Monomial Basis Conversion Clarity

Section/Line: Section II.A,   
PDF

Issue: The author notes that the original coefficients printed in Cai et al. (2009)—(3,1,−9,5,−66,9)—cannot be directly transplanted into the symmetrized basis used here due to differing Wick-permutation normalizations .  
PDF

Proposed Fix: Add a brief footnote or appendix equation showing the exact linear transformation matrix or definition mapping the Cai et al. monomial normalization convention onto the author's reference solution (2,7,3,−12,−69,19) to facilitate future symbolic cross-checking.  
PDF

Parameter Notation Mapping

Section/Line: Section VIII.B,   
PDF
+ 2

Issue: Equation (9) introduces the parameters c
′
 and κ
ϵ
	​

 to map the spectral index tilt onto the non-Gaussianity running: c
′
≡κ
ϵ
	​

/8.  
PDF
+ 2

Proposed Fix: Ensure that c
′
 is clearly distinguished from the monomial coefficients c
1
	​

…c
6
	​

 in Section II.A. A simple explicit note stating that c
′
 is a scale-dependence parameter unrelated to the spatial configuration polynomial coefficients will resolve potential reader confusion.  
PDF
+ 1

5. Strengths

Definitive Normalization Audit: The symbolic and numerical resolution of the factor-of-two discrepancy between the Cai et al. doubled in-in commutator result and the Li et al. single time-ordering calculation provides a necessary and elegant service to the primordial cosmology community .  
PDF
+ 1

Realistic Template Mismatch Modeling: Rather than relying on simple equilateral or local approximations, the calculation of the amplitude recovery factor (r≈0.83−0.84) across 10 distinct physical noise-weighting schemes provides a highly realistic foundation for LSS recasting.  
PDF
+ 3

Rigorous Systematics Budgeting: The transition from an optimistic baseline (∼5.2−5.5σ) to a robust post-systematic budget (∼3−5σ) properly accounts for the complex degeneracies introduced by b
ϕ
	​

 marginalization, photometric redshift failure modes, and general relativistic corrections.  
PDF
+ 1

6. Specific Scrutiny
Evaluation of the f
NL
	​

=−35/8=−4.375 Prediction

The manuscript accurately frames this prediction as minimally parameterized rather than strictly parameter-free. By tracing the O(ϵ) corrections stemming from a quasi-dust equation of state (w=−0.003), the text establishes a tightly constrained theoretical variance (f
NL
	​

∈[−4.35,−4.02] at the Planck best-fit tilt). The explicit acknowledgment that the spatial polynomial P is underdetermined when constrained only by the three cardinal kinematic configurations (equilateral, folded, squeezed) is handled honestly. It correctly separates the stable shape cosine (r
cos
	​

>0.97) from the amplitude recovery scatter.  
PDF
+ 4

Externalization of Heinrich et al. (2024)

The paper is carefully scoped as a sensitivity recast rather than a ground-up Fisher matrix calculation. By mapping the template projection factor r directly onto the external multi-tracer galaxy bispectrum errors (σ(f
NL
local
	​

)≈0.7), the author prevents double-counting of cosmic variance cancellation benefits. The caveat flagged regarding the assumption of b
ϕ
	​

 universality in the original Heinrich et al. pipeline is highly astute ; relaxing this universality condition per tracer bin widens the forecast margins appropriately.  
PDF
+ 4

Detection Significance (3–5$\sigma$ Post-Systematic-Budget)

The headline conclusion that SPHEREx can achieve a template-corrected significance of ∼3−5σ is structurally sound. The step-down analysis from the uncorrected naive limit (∼6.25σ) through the noise-weighted shape projection floor (∼5.2σ) is mathematically transparent.  
PDF
+ 3

  Naive Ideal Limit (~6.25σ)
             │
             ▼  [Template Mismatch Projection: r ≈ 0.83-0.84]
  Optimistic Noise-Weighted Floor (~5.2-5.5σ)
             │
             ▼  [GR Corrections, Photo-z, b_φ Marginalization]
  Realistic Post-Budget Envelope (~3.0-5.0σ)


Even when evaluated at the 16th percentile of the null-space polynomial deformation scan, the significance stays safely above the 3σ standard evidence threshold.  
PDF
+ 1

DBI Category-Error Closure at Section VIII.D

The author skillfully bypasses a common category error when evaluating alternative models under the joint Scale-Dependent Bias (SDB) running index (n
f
NL
	​

	​

) framework. The text correctly clarifies that Non-canonical single-field models (such as DBI inflation) are fundamentally distinguished from local shapes by their equilateral configuration geometry and vanishing squeezed-limit amplitudes, rather than their scale running. Consequently, a local SDB running check is a subordinate tool for distinguishing the bounce from the curvaton or QSFI continuum, but completely inapplicable to DBI, which requires the full bispectrum-shape channel. This explicit categorization demonstrates strong theoretical command of the non-Gaussian landscape.  
PDF
+ 4




Thinking

