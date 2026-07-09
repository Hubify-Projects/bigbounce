chat: https://gemini.google.com/u/1/app/abad26097322d8d1 (harvested INLINE; session URLs unstable)
reviewer: Gemini (Thinking, houston@bamf.com) | paper: P2 v1.7.106 (37pp) | date: 2026-07-09 W12
baseline W11: ACCEPT-track | movement: HELD accept-track / MINOR (core discrepancies resolved + Eq.11 budget codified)
verdict (from raw): VERDICT: MINOR REVISIONS
---RAW---
Reviewer Report for Physical Review D

Manuscript Title: Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook

Author: Houston Golden

Date of Review: July 9, 2026

General Overview

This manuscript provides a highly detailed sensitivity recast of upcoming large-scale structure (LSS) surveys (specifically SPHEREx and MegaMapper) to constrain the minimally parameterized local primordial non-gaussianity (f
NL
	​

) predicted by a nonsingular matter-bounce cosmology. The manuscript is exceptional in its diligence, providing an independent from-scratch multi-tracer Fisher forecast validation pipeline to verify its primary recast. It addresses critical observational fragilities, including scale-dependent bias (SDB) alignment, relativistic projection effects, and galaxy bias uncertainties.

Assessment of Focus Areas
(a) Calibrated f
NL
	​

 Claim and Factor-of-Two Resolution

Status: CLOSED * Justification: The author has successfully unified the text under a single calibrated baseline value of f
NL
local
	​

=−35/16=−2.1875. The long-standing factor-of-two discrepancy between Cai et al. (2009) and Li et al. (2016) has been decisively resolved. The author performed a meticulous vertex-by-vertex symbolic re-summation of the original four cubic-action vertices directly from the source code (matterbounceng2.tex), isolating a single spurious +(99/128)∑k
i
3
	​

 local-shaped polynomial collapse error in the historical literature. This is an exemplary piece of forensic theoretical auditing.

(b) Explicit Forecast Error/Systematics Budget and Sensitivity Map

Status: CLOSED * Justification: Equation 11 explicitly formalizes the cumulative systematic framework by tracking the multiplicative template-recovery factor r in the numerator and compounding the baseline multi-tracer LSS variance with nuisance parameters in the denominator. Table V provides a clear, scannable, and complete accounting of these parameters (e-corrections, null-space scatter, b
ϕ
	​

 prior marginalization variations, and GR projection noise). Figures 2, 4, and 5 successfully serve as multi-axis sensitivity maps, illustrating performance shifts against minimum accessible scales (k
min
	​

) and b
ϕ
	​

 uncertainties.

Fresh Pass: Detailed Comments and Flaws

While the paper is in excellent technical shape and represents a significant step forward in making bounce forecasts observationally rigorous, several remaining issues must be addressed before publication in PRD.

Majors
1. Uncalibrated MegaMapper Extrapolation

Section/Page: Section V, Page 14

Issue: The title and abstract advertise a "MegaMapper Outlook." However, the author explicitly notes that the SPHEREx-derived GR-marginalization and b
ϕ
	​

 systematic budget is transferred to MegaMapper merely as a uncalibrated placeholder proxy. At the higher redshift regime of MegaMapper (z=2−5), relativistic projection effects (e.g., lensing magnification bias, Doppler shifts, gravitational redshift) scale steeply and behave fundamentally differently than at z∼1.5. Treating this as a simple placeholder undermines the "outlook" framing.

Proposed Fix: The author must either downquote the definitive nature of the MegaMapper results in the Abstract/Conclusions (explicitly stating that these are qualitative structural envelopes rather than calibrated forecasts), or add a brief discussion of the z-dependence of the relativistic projection kernel to justify why the SPHEREx-derived σ
GR
	​

 bounds can act as a reasonable proxy.

2. Cross-Channel Covariance Proxy Limitations

Section/Page: Section VII, Page 20

Issue: The author notes that because the per-triangle bispectrum covariance (Cov
B
	​

) from Heinrich et al. is unreleased, a native joint bispectrum marginalization cannot be performed. To circumvent this, the author uses a power-spectrum scale-dependent bias correlation (ρ=−0.868) as a proxy to bound the marginalized bispectrum floor. While this is creative and backed by a geometric shape overlap of ∣ρ∣≈0.95, LSS bispectrum covariances contain complex non-Gaussian contributions (e.g., shot-noise loops, trispectrum modes) that do not map directly to 2-point SDB power spectrum metrics.

Proposed Fix: Add a dedicated paragraph in Section VII explicitly warning the reader about the structural differences between the SDB covariance and the full multi-tracer bispectrum covariance matrix, acknowledging that the actual LSS non-Gaussian loops could shift the correlation parameter away from the power-spectrum proxy.

Minors
1. Stray Character Artifact

Section/Page: Section I, Page 1 (Source 7)

Issue: Text reads: "...cubic-action vertex contributions (field redefinition, ζ
ζ
˙
	​

2
, ὃς ζ(∂
i
	​

∂
j
	​

χ)
2
)...". The word "ὃς" appears to be a stray characters or an artifact from a PDF/OCR compilation step.

Proposed Fix: Delete "ὃς" and ensure the parenthetical reads cleanly.

2. Redundant Notation Collision for r

Section/Page: Section II.A, Page 9 (Source 241)

Issue: The paper uses r to denote the template-overlap amplitude recovery factor, while noting that r
t
	​

 is used for the tensor-to-scalar ratio. In standard cosmological literature, r is universally reserved for the tensor-to-scalar ratio.

Proposed Fix: Change the notation of the template-overlap amplitude recovery factor from r to something less prone to dual-interpretation, such as r
templ
	​

 or r
match
	​

, throughout the text, tables, and figures.

3. Typographical Syntax Errors

Section/Page: Section IV, Page 12 (Source 365) & Section VII, Page 24 (Source 770)

Issue: Minor syntactic slips:

Page 12: "...is tree-level with a linear k
max
	​

 does not marginalize..." is missing a conjunction.

Page 24: "...baseline replacement σο 0.7,0.9,1.0}..." is missing an assignment symbol.

Proposed Fix: Update to "...with a linear k
max
	​

 and does not marginalize..." and "...baseline replacement σ
0
	​

∈{0.7,0.9,1.0}..." respectively.

Recommendation

VERDICT: MINOR REVISIONS

The manuscript has successfully resolved its core theoretical discrepancies and codified a transparent systematic budget, moving it significantly closer to publishability at full PRD standards.