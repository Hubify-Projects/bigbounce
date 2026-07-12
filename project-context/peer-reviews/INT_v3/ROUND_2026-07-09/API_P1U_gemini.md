# INT API Review — P1U v1U.0.17 — gemini (gemini-3.1-pro-preview)
paper: P1U  version: v1U.0.17  model: gemini-3.1-pro-preview
modality: native-PDF (inline_data base64)
UTC: 2026-07-12T10:46:52.749408Z  |  latency: 31.3s  |  attempt: 1
usage: {"promptTokenCount": 32854, "candidatesTokenCount": 533, "totalTokenCount": 35416, "promptTokensDetails": [{"modality": "TEXT", "tokenCount": 94}, {"modality": "IMAGE", "tokenCount": 32760}], "thoughtsTokenCount": 2029, "serviceTier": "standard"}
PARSED VERDICT: MINOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

VERDICT: MINOR REVISIONS

ISSUES:
1. [MAJOR] Abstract and Overall Verbosity: The abstract is excessively long (over 500 words) and reads more like a rebuttal to anticipated criticism than a concise summary of physical results. Furthermore, throughout the manuscript (e.g., Section I "What this paper does and does not establish" box; Section IV "Scope" paragraph), the author repeatedly and defensively restates the exact limitations, caveats, and evidentiary tiers of the work. These meta-discussions must be heavily consolidated and streamlined to align with the standard, objective stylistic norms of *Physical Review D*.
2. [MAJOR] Section IX Constraint Catalog: The categorization of exactly 14 "mechanism-class constraints" artificially inflates the structural findings of the paper. As the author acknowledges, many of these (e.g., Barriers 5, 6, 10, 11) are generic naturalness, scale-separation, or initial-condition arguments applicable to almost any quintessence or modified gravity model, rather than novel ECH-specific calculations. This section should be condensed to focus primarily on the mathematically rigorous ECH-specific constraints (such as the NJL gap equation limits and the perturbation transparency).
3. [MINOR] Section X (Perturbation Transparency): The core algebraic mechanism—that the Holst term vanishes identically on a torsion-free Levi-Civita connection due to the first Bianchi identity—is a well-known property of the classical action. While expanding this explicitly to all orders of scalar/tensor perturbations to shut down dark-energy/birefringence routes is a useful synthesis, the text should more carefully delineate the well-known classical background identity from the author's specific perturbative application. 
4. [MINOR] Appendix F (MCMC Proxy Analysis): The MCMC analysis utilizes stock CAMB to fit $\Lambda$CDM + $\Delta N_{\text{eff}}$ as an "upper bound envelope check," explicitly acknowledging that the code contains no bespoke torsion physics. Because this is essentially a standard cosmological parameter estimation whose null result is entirely expected for the standard model, devoting such extensive space (Tables VIII, IX; Figs. 8, 9) to it is disproportionate. The MCMC reporting should be drastically shortened to a brief summary of the upper bound.

The central claim that minimal Einstein-Cartan-Holst gravity cannot naturally source late-time dark energy or parity-violating perturbations without invoking severe fine-tuning or non-minimal extensions is rigorously supported by sound effective field theory power-counting and exact geometric identities.