# INT API Review — P1U v1U.0.16 — gemini (gemini-3.1-pro-preview)
paper: P1U  version: v1U.0.16  model: gemini-3.1-pro-preview
modality: native-PDF (inline_data base64)
UTC: 2026-07-12T09:39:34.273846Z  |  latency: 37.8s  |  attempt: 1
usage: {"promptTokenCount": 32854, "candidatesTokenCount": 745, "totalTokenCount": 35753, "promptTokensDetails": [{"modality": "TEXT", "tokenCount": 94}, {"modality": "IMAGE", "tokenCount": 32760}], "thoughtsTokenCount": 2154, "serviceTier": "standard"}
PARSED VERDICT: MAJOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

VERDICT: MAJOR REVISIONS

ISSUES:
1. [MAJOR] General / Formatting and Tone: The manuscript is excessively defensive, pedagogical, and heavily littered with meta-commentary (e.g., "What this paper does and does not establish," "Scope statement," "Caveats"). This non-standard stylistic choice must be stripped out. A PRD paper should present the scientific arguments and derivations directly rather than preemptively debating hypothetical referees in the main text.
2. [MAJOR] Section X (Perturbation Transparency): The "theorem" that the Holst term $\epsilon^{\mu\nu\rho\sigma} R_{\mu\nu\rho\sigma}$ vanishes identically on a Levi-Civita (torsion-free) connection due to the algebraic Bianchi identity is a foundational, widely known property of the Holst action (e.g., Holst 1996; Perez 2003). Presenting this as a novel, central "proof" or "theorem" significantly overstates the theoretical contribution. The section must be heavily condensed into a brief review of this known property and its direct consequence for perturbation theory.
3. [MAJOR] Section IX (14-Barrier Catalog): The catalog of 13/14 distinct "barriers" is artificially inflated, repetitive, and reads like a presentation slide deck. Several barriers (e.g., Barrier 4: Planck Suppression, Barrier 1: Mass-Coupling Lock, Barrier 5: Scale Separation) are simply variations of standard Effective Field Theory (EFT) Naive Dimensional Analysis. This section should be collapsed into a single, concise theoretical discussion of EFT power-counting and naturalness in the minimal ECH framework.
4. [MAJOR] Appendices F-I / Observational Scope Mismatch: The inclusion of extensive stock CAMB MCMC parameter estimation, NaMaster pseudo-$C_\ell$ pipeline validations, and spectator-ALP fits creates a severe scope mismatch. Because the main text successfully establishes that ECH theory predicts vanishingly small amplitudes for these effects, dedicating roughly half the manuscript to standard observational bounds on *generic* ALPs or generic $\Delta N_{\rm eff}$ is superfluous. These appendices should be removed and, if necessary, relocated to an observation-focused companion paper.
5. [MINOR] Section IV.A / Appendix D: The NJL gap equation analysis for the torsion-induced four-fermion term is physically sound, but the fact that the scalar channel is repulsive (and thus fails to condense) under minimal coupling has been explored in prior literature (e.g., Freidel et al. 2005; Perez & Rovelli 2006). The text should clearly delineate what is newly derived here versus what is a confirmation of established ECH fermionic properties.
6. [MINOR] Section II.C (Eq. 13): The exponential dilution tracking $e^{-3N_{\rm tot}}$ for the torsion contribution relies on treating the background axial current as a coherent, cold-relic-like state. The author's subsequent thermodynamic erasure argument (that post-bounce reheating thermalizes the coherent state to zero) is physically much stronger and actually renders the highly parameterized e-fold fine-tuning bookkeeping largely moot; the text should prioritize the thermal reset argument. 

The central claim that minimal Einstein-Cartan-Holst gravity cannot naturally source late-time dark energy or observable cosmic birefringence without re-introducing severe fine-tuning is theoretically supported, but the manuscript requires drastic structural condensation and the removal of extraneous observational pipeline details to meet the standards of a focused PRD article.