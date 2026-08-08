# INT API Review — P2 v1.7.118 — openai (gpt-5-2025-08-07)
paper: P2  version: v1.7.118  model: gpt-5-2025-08-07
provenance: commit=9089d65c64752e3a2c69778b72d97ef7c45b4443  pdf=research/focused_paper_source_integration/02_full_draft.pdf  sha256=01107b3d731b945b2aa9ea04ce4e8188282770a87b495c4a1f7ad5b71a4db71a
modality: native-PDF (Files API input_file)
UTC: 2026-07-14T09:49:22.977299Z  |  latency: 124.2s  |  attempt: 1
usage: {"input_tokens": 15213, "input_tokens_details": {"cache_write_tokens": 0, "cached_tokens": 0}, "output_tokens": 5271, "output_tokens_details": {"reasoning_tokens": 3968}, "total_tokens": 20484}
PARSED VERDICT: MAJOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:
1. [MAJOR] Appendix A/Table IV (vertex resummation and notation): The per-vertex contributions are written with ambiguous summation symbols (e.g., Σijk, Σijlk) and overloaded “k” notation, making the algebra non-auditable; provide unambiguous, fully symmetrized expressions (with explicit definitions of all sums), quote the precise interaction Hamiltonian and mode functions used, and show the intermediate time integrals (or a compact derivation) so that the −35/16 result can be reproduced without relying on code.
2. [MAJOR] Appendix A (discrepancy with Cai et al.): The claimed −(99/128) Σi k_i^3 difference between Cai’s printed AT and the exact vertex sum is asserted via code; reproduce Cai et al.’s A_T explicitly (with equation numbers from Ref. [7]) in your notation and show the algebraic subtraction on paper to demonstrate the discrepancy is not due to conventions (gauge, normalization, integration by parts, or field redefinition treatment).
3. [MAJOR] Sec. II A and Eq. (3) (ordered-basis coefficients): The “ordered symmetric degree-nine basis” and coefficient vector (3, 1, −9, 5, −33, 9) are unusual and easy to misinterpret; map Eq. (A4) to Eq. (3) step-by-step, also presenting the polynomial in a standard symmetric basis (e.g., labeled by partitions or in terms of elementary symmetric polynomials), and provide a machine-readable expression to ensure community reuse.
4. [MAJOR] Initial-state and contour prescription (assumptions a–c, Appendix A.1): Using Bunch–Davies initial conditions and the iε prescription in a contracting background requires justification; discuss possible subtleties (e.g., excited states, far-past adiabaticity) and demonstrate the chosen prescription does not shift the squeezed amplitude.
5. [MAJOR] Quantification of quasi-dust corrections (Sec. II C/VIII): The manuscript repeatedly notes that w ≠ 0 induces percent-level corrections but gives no quantitative estimate; provide at least a controlled leading-order estimate or a bound (with assumptions stated) to bracket the robustness of −35/16 in the quasi-dust model cited.
6. [MAJOR] Shape-overlap pipeline (Sec. II A/B): The “fixed 23,098-triangle ratio grid,” weighting, k-range, binning, and normalization used to compute r and rcos are insufficiently specified; document the triangle set, weight definition, k-cuts, and show stability of r under reasonable variations so that the 0.8354 value is independently reproducible.
7. [MAJOR] In-house Fisher calculations (Sec. IV): The “channel-native” and redshift-space Fisher results lack the necessary survey specifications (tracer populations, n(z), b1(z), shot noise, redshift bins, volumes, k and μ cuts, multipole set, cosmology, and nuisance priors); supply a complete parameter table and inputs so the quoted 3.47σ→0.42σ ladder can be replicated.
8. [MAJOR] Presentation of observational claims (Abstract/Sec. IV/IX–X): The 2.63σ “headline” relies on adopting σ(fNL)=0.7 from Ref. [1] and strong assumption (d); move all sigma-level statements to a clearly labeled “conditional sensitivity” subsection and reiterate the dependence on cubic transfer and per-triangle covariance to avoid overstatement in the abstract and conclusion.
9. [MAJOR] Field redefinition term and conventions (Appendix A/Table V): Provide the explicit form of the field redefinition and confirm that the fNL normalization matches Refs. [7,8] (including factors of 10/3 and Σi k_i^3) to preclude a covert convention mismatch as the source of the factor-of-two discrepancy.
10. [MAJOR] Relativistic-projection surrogate (Sec. IV/VII): Define AGR precisely (which relativistic terms it rescales), cite the underlying expressions, and justify the adopted marginalization/prior choices; otherwise the nuisance-driven significance range (3.47σ→0.42σ) is not interpretable.
11. [MINOR] Notation cleanup (Sec. II A, Appendix A): Avoid using “k” both as an index and as magnitude; define Σi≠j and Σi≠j≠l once and use consistently; replace “Σijk”/“Σijlk” with explicit ordered-pair/triple sums or standard symmetric-sum notation.
12. [MINOR] Distinguish BNL from fNL clearly (Sec. II A): Reserve fNL for the squeezed-limit amplitude and use a standard symbol for the reduced bispectrum to minimize confusion.
13. [MINOR] Significant figures (Sec. II A/B, IV): Reduce excessive precision (e.g., r = 0.83542294) to 3–4 significant digits in the main text; place machine-precision values in ancillary material.
14. [MINOR] Literature context (Sec. VI/VII): Add citations on relativistic light-cone and projection effects in LSS bispectra and on calibration of bϕ beyond scale-dependent bias basics; clarify how your AGR prior relates to that literature.
15. [MINOR] Code availability (Data and Code): Provide a permanent DOI for the exact commit used (not “will be minted”), and ensure scripts reproduce all tables/figures from a clean environment.
16. [MINOR] Typos/formatting: Multiple minor typesetting issues (e.g., misrendered sums, inconsistent hyphenation) require a careful copyedit; ensure all equations and table captions are self-contained and unambiguous.

(3) The central claim is partly supported: the −35/16 amplitude is convincingly backed by the vertex-level calculation and an independent general-cs check, whereas the SPHEREx sensitivity mapping is only conditionally supported and under-specified pending full survey covariance and nuisance treatment.