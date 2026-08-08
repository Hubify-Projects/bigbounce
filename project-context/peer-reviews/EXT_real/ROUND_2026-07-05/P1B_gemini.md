# EXT Review — P1B × Gemini
- paper: P1B
- version: v1B.0.99
- reviewer: Gemini
- model: 3 Pro (Ultra)
- timestamp: 2026-07-06T19:10:26Z
- chat_url: https://gemini.google.com/u/1/app/1bc86dfa88769f5a
- pdf: /tmp/round_P1B.pdf

## Raw verbatim response

VERDICT: MAJOR REVISIONS

ISSUES:

[MAJOR] Section III (MCMC Proxy Analysis): The ΛCDM+ΔN
eff
	​

 analysis utilizes a stock CAMB solver and does not implement a torsion-modified Boltzmann module. Running a generic proxy test that yields standard results, such as finding ΔN
eff
	​

 consistent with zero, does not constitute a rigorous physical test of the Einstein-Cartan-Holst theory.  
PDF
+ 1

[MAJOR] Section IV (NaMaster Pipeline Validation): The pseudo-C
l
	​

 pipeline validation relies on CMB-only synthetic skies that are entirely devoid of galactic foregrounds. This structural omission prevents the pipeline from addressing the physical separation of the cosmic-rotation angle from the instrumental-miscalibration angle, rendering the validation decoupled from the primary challenges of real-world sky measurements.  
PDF
+ 2

[MAJOR] Section VI (Spectator-ALP Consistency Check): While the spectator-ALP model accommodates the birefringence signal, the manuscript explicitly acknowledges this is not a distinctive ECH prediction because the exact same result arises in standard General Relativity. Furthermore, the accommodation requires significant parameter tuning, specifically a misalignment initial condition of roughly 0.1 and a non-minimal photon coupling of 8 or greater, which severely limits its natural explanatory power.  
PDF
+ 3

[MINOR] Overall Manuscript Scope: The document functions primarily as a technical reproducibility appendix to Paper I(a) rather than a standalone physical investigation. The valuable, first-principles theoretical derivations—such as the calculation of the bespoke ECH-sector ΔN
eff
	​

 envelope yielding a negligible value at BBN—should be integrated directly into Paper I(a) to strengthen its theoretical completeness.  
PDF
+ 2

CENTRAL CLAIM ASSESSMENT:
The central claim that these limited numerical cross-checks demonstrate null-consistency with the ECH spin-torsion framework is technically supported , but only trivially so, because the implemented tests strictly evaluate standard ACDM and standard GR+ALP models rather than the distinct, propagating dynamics of the proposed modified theory.  
PDF
+ 2
