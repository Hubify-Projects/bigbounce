# INT API Review — P1A v1A.0.119 — openai (gpt-5.5)
paper: P1A  version: v1A.0.119  model: gpt-5.5
provenance: commit=142d9d54  pdf=arxiv/paper1a_ech_nogo.pdf  sha256=dfe2a47a3221888477dfa47adb9cddf7ebbe25acc96185c3af9e58a1e7c065d0
modality: native-PDF (Files API input_file)
UTC: 2026-07-14T17:29:21.351316Z  |  latency: 66.9s  |  attempt: 1
usage: {"input_tokens": 8793, "input_tokens_details": {"cache_write_tokens": 0, "cached_tokens": 0}, "output_tokens": 3042, "output_tokens_details": {"reasoning_tokens": 2070}, "total_tokens": 11835}
PARSED VERDICT: MAJOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:

1. [MAJOR] Sec. III A / Abstract / Conclusions: the “finite-density bound” is not actually derived as a bound from the action; the manuscript assumes \(|\langle J_5^I J_{5I}\rangle|\lesssim n_\psi^2\), but number density alone does not bound the composite axial-current correlator without specifying the state, spin polarization, relativistic normalization, species content, and renormalization/contact prescription. Recast this as a dimensional homogeneous benchmark unless a real inequality is proven.

2. [MAJOR] Sec. III A: the comparison to \(\rho_\Lambda\) is numerically correct for the chosen \(n_\psi=100\,{\rm cm}^{-3}\), but the physical meaning of that density is unclear. Since it is neither the cosmic baryon density nor a specified relic fermion density with spin state, the manuscript should not call the result a late-time cosmological “bound” without defining the ensemble and explaining why this benchmark is conservative for the intended application.

3. [MAJOR] Secs. II–III / Appendix A: the sign of the scalar Fierz projection is central to the NJL conclusion, but the manuscript relies on a convention-dependent direct-channel rearrangement. The paper should state the metric, gamma-matrix, \(\gamma^5\), \(\epsilon^{IJKL}\), and four-fermion sign conventions in one place and explicitly connect the Fierz ordering in Appendix A to the NJL interaction convention \(G_s(\bar\psi\psi)^2\). Otherwise the claim “repulsive scalar channel” is not independently auditable.

4. [MAJOR] Sec. V A–C: the “all orders” scalar/tensor transparency statement is basically correct on the torsion-free branch, but the proof should use the full Holst-modified Cartan equation, not the schematic \(T^\lambda{}_{\mu\nu}=8\pi G S^\lambda{}_{\mu\nu}+\cdots\). Show explicitly that for real finite \(\gamma\) the algebraic operator is invertible and \(S=0\) implies \(T=0\), while excluding the self-dual singular values \(\gamma=\pm i\).

5. [MINOR] Sec. V C: the displayed tensor equation \(h''_{ij}+2{\cal H}h'_{ij}+k^2h_{ij}=0\) is the source-free linear GR equation on an FRW background. Since the text claims all-order equality of tensor perturbation dynamics, clarify that this equation is only an illustrative linear result and that the all-order statement concerns equality of the action/equations to GR, not this specific linear equation.

6. [MINOR] Sec. V F: the phrase “Nonperturbative parity channels … model-dependent tests of \(\gamma_{\rm BI}\)” is potentially misleading in a paper whose theorem says constant-\(\gamma\) minimal ECH gives no scalar/tensor parity signal. Make explicit that such channels require additional non-minimal, dynamical-Immirzi, axionlike, fermionic, or propagating-torsion ingredients not present here.

7. [MINOR] Sec. V B–D: Step 5 says “A total derivative contributes nothing,” but the stronger statement used here is pointwise vanishing of \(e^I\wedge e^J\wedge R_{IJ}\) at \(T=0\). The total-derivative discussion of Nieh–Yan should be separated from the torsion-free Bianchi identity to avoid suggesting that the Holst density is merely a boundary term in the Levi-Civita sector.

8. [MINOR] Sec. IV: the discussion of Shapiro–Teixeira and Benedetti–Speziale is acceptable as context, but the manuscript should avoid implying that those papers attempted to provide a dark-energy observable map; state only that such a map is not supplied by those RG calculations.

9. [MINOR] Data and Code Availability: code is helpful, but the analytic claims should not depend on unpublished companion material or repository-specific scripts. Ensure all factors used in the finite-density and NJL calculations are reproducible from equations in the paper alone.

(3) The central claim is supported in its narrow form—minimal ECH gives a Planck-suppressed axial contact term and a constant Holst term is classically inert for canonical scalar/tensor perturbations on the torsion-free branch—but several statements currently overstate benchmark estimates as bounds and require tighter convention-level justification.