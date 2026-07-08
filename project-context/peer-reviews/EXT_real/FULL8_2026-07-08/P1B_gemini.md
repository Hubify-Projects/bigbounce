# P1B (v1B.0.103) — Gemini Ultra — EXT FULL8 2026-07-08

Verdict (verbatim): VERDICT: MAJOR REVISIONS

## RAW

VERDICT: MAJOR REVISIONS

ISSUES:

[MAJOR] Sec. IV (Data Methods: CMB E-B Analysis): The pseudo-C
l
	​

 pipeline validation relies on synthetic polarization skies that are entirely free of galactic foregrounds. Because real-sky cosmic birefringence measurements are fundamentally limited by the degeneracy between the cosmic rotation angle β and the instrumental miscalibration angle α—a degeneracy broken only by unrotated foreground components —a pure CMB algebraic mode-coupling test is structurally incomplete to fully validate a pipeline's systematic readiness for realistic sky measurements.  
PDF
+ 1

[MAJOR] Sec. VI (Cosmic Birefringence: Spectator ALP Consistency Check): The MCMC parameter estimation utilizes a Gaussian summary likelihood centered on the published Eskilt-Komatsu datum (β
obs
	​

=0.342
∘
±0.094
∘
) rather than evaluating the actual EB bandpowers or a joint likelihood. While the manuscript transparently acknowledges this approximation and its impact on the posterior tails , omitting the explicit EB bandpower covariance and calibration systematics renders the derived parameter constraints and posterior mass fractions heuristic. A full joint-EB refit should be performed.  
PDF
+ 3

[MINOR] Sec. III.A (Bespoke ECH-sector ΔN
eff
	​

): The derivation of the coherent spin-torsion energy density relies on a parametric scaling estimate, ⟨(
ψ
	​

γ
5
γ
μ
ψ)
2
⟩
T
	​

∼n
f
2
	​

∼(g
∗
	​

T
3
)
2
, explicitly dropping O(1) coefficients instead of performing a rigorous finite-temperature Nambu-Jona-Lasinio computation. Although the resulting bound (ΔN
eff
(ECH)
	​

∼10
−44
 at BBN) makes these prefactors observationally moot, a formal theoretical derivation in PRD should supply the exact numerical coefficient.  
PDF
+ 2

[MINOR] Prose and Structure: The manuscript is excessively laden with repetitive defensive disclaimers, localized "Scope" definitions, and explicitly bulleted "What is NOT in this paper" boundaries scattered throughout the text. These should be consolidated into a single, cohesive scope-and-limitations section in the introduction to improve readability.  
PDF
+ 3

The central claim—that these numerical models are technically reproducible and yield null or non-distinctive envelope limits consistent with standard cosmology—is structurally supported by the provided artifacts, though the explicit methodological simplifications weaken the physical applicability of the independent tests.  
PDF
+ 1
