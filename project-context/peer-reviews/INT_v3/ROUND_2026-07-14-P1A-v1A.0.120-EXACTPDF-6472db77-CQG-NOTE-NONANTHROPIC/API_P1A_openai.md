# INT API Review — P1A v1A.0.120 — openai (gpt-5.5)
paper: P1A  version: v1A.0.120  model: gpt-5.5
provenance: commit=438ce8ec  pdf=arxiv/paper1a_ech_nogo.pdf  sha256=6472db7741deebd4100fe3191d5ef23a9b0b7960c4284cf53e9e4761f62f535b
modality: native-PDF (Files API input_file)
UTC: 2026-07-14T18:06:11.366911Z  |  latency: 78.0s  |  attempt: 1
usage: {"input_tokens": 9840, "input_tokens_details": {"cache_write_tokens": 0, "cached_tokens": 0}, "output_tokens": 4117, "output_tokens_details": {"reasoning_tokens": 3312}, "total_tokens": 13957}
PARSED VERDICT: MAJOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MAJOR REVISIONS.

(2) ISSUES:

1. [MAJOR] Overall/CQG Note suitability: the manuscript contains two largely independent Notes-level points—four-fermion contact benchmarking and Holst-sector scalar/tensor transparency—plus NJL appendices, running-literature discussion, code references, and companion-paper disclaimers; it should be substantially shortened and focused around one clear Note-worthy clarification.

2. [MAJOR] Novelty and positioning: the main ingredients—algebraic torsion elimination, the induced axial–axial contact term, zero scalar spin current, and vanishing of the torsion-free Holst contraction by the first Bianchi identity—are standard; the manuscript must state more sharply what the new useful clarification is, rather than presenting known facts with extensive caveats.

3. [MAJOR] Section V.A–F, “classical scalar-sector transparency”: the local classical statement is basically correct, but claims such as “all perturbation observables,” “bispectrum identical,” and “no CMB parity violation” are too broad unless boundary conditions, global/topological sectors, initial-state assumptions, and the absence of loop/anomaly effects are explicitly excluded at the point of the claim.

4. [MAJOR] Section II/V proof of the Cartan constraint: the central algebraic step is asserted rather than shown; for a self-contained Note the authors should write the Holst-modified connection equation explicitly and demonstrate that, for invertible tetrad and real nonsingular γ, zero spin source implies \(e^{[I}\wedge T^{J]}=0\) and hence \(T^{I}=0\).

5. [MAJOR] Section III.A finite-density benchmark: the comparison \(\kappa n_\psi^2/\rho_\Lambda\) is a dimensional scale estimate, not a physical energy density, bound, or expectation value; the manuscript says this repeatedly, but the abstract/conclusion still risk implying physical relevance to dark energy, and the arbitrary choice \(n_\psi=100\,{\rm cm}^{-3}\) needs either motivation or relegation to a simple illustrative example.

6. [MAJOR] Section III.B and Appendix B, NJL check: the “no scalar gap” conclusion is valid only for the declared Fierz projection, direct-channel mean-field ansatz, regulator, and sign convention; because mean-field NJL treatments are Fierz-ambiguous and the stress-test cutoff is at or above \(M_{\rm Pl}\), this material should be presented as a narrow consistency check, not as an independent robustness result.

7. [MINOR] Appendix A notation: expressions such as \(G_s(\psi\bar\psi)^2\) are unconventional and potentially confusing; use \(G_s(\bar\psi\psi)^2\) consistently, while separately explaining the operator ordering used in the Fierz rearrangement.

8. [MINOR] Section V.D Nieh–Yan/Pontryagin discussion: the distinction is useful but overlong for a Note and contains notation that appears garbled, e.g. “\(R\,R e\)”; this section should be shortened and cleaned because the operative argument is simply the algebraic Bianchi identity on the torsion-free branch.

9. [MINOR] References to Paper I(b), stock-CAMB, NaMaster, spectator-ALP studies, and extensive GitHub/code discussion are peripheral to the claimed ECH results and should be removed or reduced to one sentence if this is to function as a concise CQG Note.

(3) Yes, the narrow central claim—that minimal constant-\(\gamma\) ECH gives the standard Planck-suppressed axial contact term and is classically transparent to canonical scalar/tensor perturbations on the torsion-free branch—is supported, but the manuscript must be narrowed and its broader observational/EFT implications softened.