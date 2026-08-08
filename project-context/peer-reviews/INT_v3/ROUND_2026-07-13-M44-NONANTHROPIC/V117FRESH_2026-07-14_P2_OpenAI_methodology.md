# P2 V117FRESH_2026-07-14 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/research/focused_paper_source_integration/02_full_draft.pdf` md5=a6bf211f pages=10
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6854 chars)
**Wall time**: 510.1s

---

Verdict-first: MAJOR REVISIONS

This manuscript presents (i) an exact four-vertex derivation for the matter-bounce cubic bispectrum giving fNL = −35/16 and the ordered-basis coefficients (3, 1, −9, 5, −33, 9), and (ii) a conditional sensitivity recast to SPHEREx. The algebraic component is carefully argued and largely self-contained, with useful internal checks and benchmark limits. The observational recast is explicitly labeled conditional and separated from a full survey likelihood, which is appropriate.

However, several methodology essentials need correction or clarification before this can meet PRD standards. Chief among them are: an undefined nuisance parameter (AGR), an undeclared definition of the recovery metric reff, and an unsubstantiated CMB recovery factor r = 0.876 used in Sec. VIII. The Data/Code Availability section does not yet provide a frozen release (DOI or tag/commit), which is required for reproducibility. A handful of additional clarity and style issues should also be addressed.

Below I list all findings with required fixes.

Findings

P2-E1 (ESSENTIAL)
- Location: Sec. IV (p. 4), Sec. VII (p. 6–7), Table III (p. 7)
- Problem: Undefined nuisance parameter “AGR.”
  • Examples: “A channel-native (fNL, bϕ, AGR) surrogate Fisher…” (p. 4); “ρ(fNL, AGR) = −0.4264 …” (p. 6)
- Required fix: Define AGR at first use: what physical effect it captures, its normalization, prior, and how it enters the Fisher model (e.g., an amplitude of relativistic projection terms or similar). Provide its explicit appearance in the modeled bispectrum or power-spectrum response.

P2-E2 (ESSENTIAL)
- Location: Sec. IV (p. 4)
- Problem: reff is used as a central diagnostic (“gives reff as a benchmark statistic… reff = 0.9929…”) but is never explicitly defined mathematically.
- Required fix: Provide a precise definition (e.g., reff ≡ σlocal/σbounce under the stated survey covariance and nuisance treatment), including the exact inner product and weighting used. If reff depends on marginalization choices, state that explicitly with the formula.

P2-E3 (ESSENTIAL)
- Location: Sec. VIII (p. 6)
- Problem: Use of CMB-weighted recovery r = 0.876 to compare to Planck PR4/NPIPE is not sourced or derived in this paper.
  • Quote: “using the CMB-weighted recovery r = 0.876 gives f bounce NL = −0.11 ± 5.71…”
- Required fix: Either (a) derive and document r = 0.876 in this paper (definition of the CMB inner product, triangle domain, weighting, and numerical grid), or (b) provide a precise citation that reports this number with compatible conventions, or (c) remove this conversion and simply compare the Planck constraint to the model value without remapping.

P2-E4 (ESSENTIAL)
- Location: Data and Code Availability (p. 7)
- Problem: No frozen, citable software/data release. The text promises a future archive (“will be minted from the camera-ready state”) and references transient file paths (scripts/…).
- Required fix: Provide a permanent, versioned release with DOI (e.g., Zenodo) and a specific tag/commit hash corresponding to the exact results in the manuscript. Ensure all artifacts needed to reproduce Eq. (3), the vertex-sum checks (Appendix A), the overlap r and rcos on the stated 23,098-triangle grid, and the C13/C14/C15 Fisher outputs are included. Update the manuscript to point to those immutable artifacts.

P2-E5 (ESSENTIAL)
- Location: Abstract (p. 1); Sec. IV (p. 4)
- Problem: Multiple σ-values from different procedures (published SPHEREx baseline recast vs. in-house Fisher vs. surrogate model ladder) are juxtaposed. Although the text cautions they use different covariances, the summary presentation can still invite conflation.
- Required fix: At every place where σ from different procedures appear side-by-side, append a parenthetical reminding the reader “not directly comparable; different covariance/assumptions.” This is especially important in the abstract and at the start of Sec. IV.

P2-E6 (ESSENTIAL)
- Location: Appendix A (p. 7–9)
- Problem: The central claim about the transcribed Cai et al. polynomial differing from the exact vertex sum by −(99/128)∑i k_i^3 is important and nontrivial.
- Required fix: For full auditability, include in the appendix (or as a short supplementary text file linked via the DOI release) the exact coefficient list of the Cai et al. printed polynomial you compare against (cs = 1), and display explicitly the algebraic difference leading to Eq. (A2). This need not be exhaustive but must be sufficient for a reader to verify the claimed discrepancy without running external code.

P2-M1 (MAJOR)
- Location: Throughout (e.g., p. 2–4)
- Problem: C13/C14/C15 labels are used as shorthand for internal pipelines without prior definition.
- Required fix: Define these labels once (e.g., “C13 = independent real-space Fisher; C14 = redshift-space multipoles; C15 = channel-native surrogate Fisher”) or avoid the labels entirely in the manuscript body.

P2-M2 (MAJOR)
- Location: Sec. IV (p. 4–5)
- Problem: Redshift-space modeling mentions “tree-level Kaiser and Z2 kernels” without formulae or references for the exact conventions used (e.g., symmetrization, bias model).
- Required fix: Add explicit references and/or short defining equations for the redshift-space kernels used (including normalization and bias conventions), and state the cosmological parameters assumed if any number depends on them. If numbers are cosmology-independent to the order used, state that as well.

P2-M3 (MAJOR)
- Location: Reference [14] (p. 10)
- Problem: Reference entry includes commentary (“standard separable local/equilateral/orthogonal bispectrum template basis”), which is non-standard citation style.
- Required fix: Remove commentary from the bibliographic entry and place clarifying prose in the main text where the reference is cited.

P2-M4 (MAJOR)
- Location: Sec. III.B (p. 3–4)
- Problem: The adopted r = 0.84 ± 0.02 “weighting-scheme envelope” is invoked but the two endpoints are not both derived here. The “signal-only endpoint 0.876” is referenced without derivation or citation.
- Required fix: Either (a) briefly tabulate the weighting choices and the resulting r values used to define the ±0.02 envelope (with a sentence defining “signal-only endpoint”), or (b) remove the ±0.02 language and stick to the explicitly derived flat-grid value 0.8354 for this paper’s recast.

P2-Min1 (MINOR)
- Location: Title block (p. 1)
- Problem: Version string “v1.7.117” appears in the manuscript.
- Required fix: Remove version strings and other internal versioning from the camera-ready PRD manuscript.

P2-Min2 (MINOR)
- Location: Fig. 1 caption/figure (p. 2)
- Problem: Axis labeling not explicitly stated in caption. “Squeeze ratio” is ambiguous without indicating kL/kS and the ordinate being BNL.
- Required fix: Ensure the figure has axis labels “kL/kS” (horizontal) and “BNL” (vertical), or state explicitly in the caption.

P2-Min3 (MINOR)
- Location: Fig. 2 (p. 5)
- Problem: Caption does not state axis labels; reader must infer fNL axis and which models are plotted.
- Required fix: Add explicit axis labels in the figure/caption (e.g., “horizontal: local fNL”; vertical: categorical model axis or remove vertical axis if categorical).

P2-Min4 (MINOR)
- Location: Table I header (p. 2)
- Problem: Folded configuration label “(k1=2k2=2k3)” is potentially confusing (reads like chained equalities).
- Required fix: Replace with a clear statement: “Folded: limit k1 → 2k, k2 = k3 = k (k1 = k2 + k3).”

P2-Min5 (MINOR)
- Location: Sec. III.A (p. 3)
- Problem: Unit statement “express H0 in h Mpc−1” is uncommon and could confuse readers.
- Required fix: Clarify the unit convention (e.g., “we set c = 1 and express H0 in Mpc−1 by absorbing km s−1 via c; factors of h follow the choice of k in h Mpc−1 so that M(k, z) is dimensionless”).

P2-Min6 (MINOR)
- Location: Sec. IV (p. 4–5) and Sec. VII (p. 6)
- Problem: Use of internal file names in narrative (e.g., scripts/c13_independent_bounce_fisher.py) is unusual for the body text.
- Required fix: Move such details to the Data/Code Availability section, keeping the main text free of path names.

P2-Min7 (MINOR)
- Location: Sec. IV (p. 4–5)
- Problem: The 30% Gaussian theory prior on bϕ is presented without rationale.
- Required fix: Add 1–2 sentences motivating this choice (e.g., range of theoretical uncertainty expected for bϕ calibration) or explicitly state it is a purely illustrative prior width.

P2-Min8 (MINOR)
- Location: Sec. VII (p. 6–7), Table III (p. 7)
- Problem: bϕ is not defined where first used.
- Required fix: Define bϕ at first use as the coefficient of the local-PNG scale-dependent bias response (or the exact surrogate parameterization employed).

P2-N1 (NIT)
- Location: Sec. II.A (p. 2)
- Problem: Minor typographical spacing (e.g., “three-argument P denotes this polynomial only; power spectra always carry a field subscript…” runs long).
- Required fix: None strictly required; consider minor copyediting for readability.

Arithmetic and internal consistency checks

- fNL = −35/16 = −2.1875: correct.
- Equilateral: −255/128 = −1.9921875: correct (rounded to −1.9922).
- Folded: −9/8 = −1.125: correct.
- Recast significance: with r = 0.84 and σlocal = 0.7 → |fNL| r / σ = 2.1875×0.84/0.7 ≈ 2.6268 → 2.63σ: consistent.
- With r = 0.8354 → 2.1875×0.8354/0.7 ≈ 2.611: consistent with “2.61σ.”
- Real-space Fisher: σlocal = 0.626 vs. σbounce = 0.631 → reff ≈ 0.626/0.631 = 0.9929: consistent. After marginalization: 0.687/0.688 = 0.9986: consistent.
- Surrogate ladder uncertainties implied by quoted σ: 2.1875/0.631 = 3.47; 2.1875/0.697 = 3.14; 2.1875/0.941 = 2.32; 2.1875/5.173 = 0.42: all consistent.

Dimensional checks

- Δb(k, z) = 2 fNL (b1−1) δc / M(k, z) with M(k, z) = 2k^2 T(k)D(z)/(3Ωm H0^2): standard, dimensionless Δb if units are chosen consistently. Suggest clarifying unit convention per P2-Min5.

Abstract-last drift sweep

- The abstract’s claims (coefficients, r = 0.8354 and rcos = 0.9817, 2.63σ recast; surrogate ladder 3.47σ → 0.42σ; conditional framing) are supported in the body. However, per P2-E5, add an explicit “not directly comparable” parenthetical when listing σ from different procedures together in the abstract.

Provenance surfaces

- Current code link lacks a frozen release. Required per P2-E4.

Stand-alone reader test

- AGR and bϕ lack definitions at first use; reff is undefined mathematically; CMB r = 0.876 lacks provenance. Addressing P2-E1, P2-E2, P2-E3, P2-Min8 resolves this.

Recommended maximum page count

- At 10 pages, the length is appropriate for the scope (algebraic derivation plus conditional recast).

Summary recommendation: MAJOR REVISIONS

The algebraic derivation is strong and the conditional nature of the observational recast is appropriately marked. To meet PRD methodological standards, the authors must (i) define AGR, bϕ, and reff precisely; (ii) either derive or cite the CMB recovery factor used; and (iii) provide a frozen, citable code/data release. Minor presentation and reference-style fixes are also required. With these addressed, the paper would be suitable for publication.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS AFTER SECOND-PASS AUDIT

P2-E7 (ESSENTIAL)
- Location: Sec. II.A (p. 2), Sec. III.B (p. 3–4), Abstract (p. 1)
- Problem: r and rcos are reported from a “fixed 23,098-triangle ratio grid,” but the triangle domain, discretization, and inner product are not defined. Without the k-domain bounds, binning in (k1, k2, k3) or in ratio coordinates, and the exact weighting (e.g., flat in shape space, measure on the momentum simplex, symmetry factors), the quoted r = 0.83542294 and rcos = 0.98167825 are not reproducible from the paper alone.
- Required fix: Specify precisely:
  • The triangle domain and parameterization (e.g., x ≡ k2/k3 ∈ [1, …], y ≡ k1/k3 ∈ [0, …]; k-ordering conventions).  
  • The grid resolution and counting that leads to 23,098 triangles.  
  • The inner product used for r and rcos, including weights and any symmetrization.  
  • If the grid adheres to a standard basis (e.g., Fergusson–Shellard tetrahedral domain), state so and cite it.

P2-E8 (ESSENTIAL)
- Location: Appendix A (p. 7–9)
- Problem: The vertex-level verification relies on parsing the arXiv source of Cai et al. [7] but does not identify the exact arXiv version used (arXiv supports multiple versions, sometimes with source changes).
- Required fix: State the exact arXiv identifier with version (e.g., arXiv:0903.0631vX) whose TEX source was parsed. If the source was retrieved on a given date, include that date. This is needed for auditability of Table IV and the coefficient comparison leading to Eq. (A2).

P2-E9 (ESSENTIAL)
- Location: Sec. IV (p. 4–5)
- Problem: The in-house Fisher results (real-space and redshift-space) are not reproducible from text because essential survey and analysis specifications are missing.
- Required fix: Provide a compact specification sufficient to reproduce σ = 0.626, 0.687, 0.417, 0.449 and reff values:
  • Tracer set(s), redshift bins, sky fraction/volume per bin.  
  • Number densities and linear biases b1(z) (and any b2, bs if used).  
  • k-range, k-bin widths, triangle selection, and any cuts (e.g., kmax, fundamental mode).  
  • Covariance model (Gaussian-only), shot-noise model, and whether cross-triangle covariance is neglected.  
  • For the redshift-space calculation, multipole content used, AP treatment (if any), damping model (stated as omitted), and µ-integration limits and quadrature.  
  • Cosmological parameters (or a statement of cosmology-independence to the reported order if applicable).

P2-E10 (ESSENTIAL)
- Location: Sec. II.A and Sec. III.B (p. 2–4)
- Problem: The “shape cosine” rcos is repeatedly used without a mathematical definition. Different communities use slightly different cosines (e.g., weightings by 1/(P1 P2 P3), by survey covariance, or by flat shape-domain measures).
- Required fix: Provide the exact formula for rcos, including the integration measure and normalization. If it is the flat-grid analogue of a Fisher cosine, state that and show the equation.

P2-E11 (ESSENTIAL)
- Location: Appendix A, Table IV (p. 9)
- Problem: The Σ-notation in Table IV is ambiguous (e.g., Σijk, Σijlk) and differs from the explicit “ordered pairs” and “all-distinct triples” definitions elsewhere. As written, a reader cannot unambiguously reconstruct the polynomials without running the code.
- Required fix: Rewrite Table IV using unambiguous sums or explicit symmetric-polynomial notation and define every sum symbol in-line (e.g., Σi≠j k7
i k2
j, Σi≠j≠l k5
i k2
j k2
l, etc.). Alternatively, list the coefficient vectors explicitly (cs = 1) for each vertex in the ordered basis used in Eq. (3), and include those vectors in the DOI-archived supplement.

P2-M5 (MAJOR)
- Location: Sec. IV (p. 4–5)
- Problem: The stated “approximately 34.7% gain over the real-space calculation” is ambiguous about which pair of numbers is compared (0.687→0.449 gives 34.7%; 0.626→0.417 gives 33.4%).
- Required fix: Specify which comparison is meant (marginalized case: 0.687→0.449), give the exact percentage, and note that the alternative (fixed-bias case) yields 33.4%.

P2-M6 (MAJOR)
- Location: Intro (p. 1) and throughout
- Problem: rt (tensor-to-scalar ratio) is defined in the notation list but never used elsewhere.
- Required fix: Remove rt from the notation list or use it meaningfully; otherwise it is distracting.

P2-M7 (MAJOR)
- Location: Sec. II.B title and opening paragraph (p. 3)
- Problem: The section title “UV-Completion Independence” overstates the claim given the text immediately stresses that cubic-order transmission is an additional assumption verified only at linear order.
- Required fix: Retitle to “Conditional UV-Completion Independence” (or equivalent) and reiterate the dependency on assumption (d) in the section header or first sentence to avoid over-claim.

P2-M8 (MAJOR)
- Location: Sec. III.A (p. 3)
- Problem: The standard scale-dependent bias formula is written in terms of fNL for local PNG. For the bounce case where the shape is not exactly local away from the squeezed limit, the mapping to Δb(k) requires the squeezed-limit amplitude only, and this assumption should be stated explicitly.
- Required fix: Add 1–2 sentences clarifying that Eq. (5) applies with fNL understood as the squeezed-limit amplitude of the primordial bispectrum (the local-shape coefficient), and cite a reference that justifies that the leading k−2 SDB response is controlled solely by the squeezed limit.

P2-Min9 (MINOR)
- Location: Sec. IV (p. 4–5)
- Problem: The phrase “full-run primordial-transfer-only comparison gives reff = 0.9981” is confusing (a “full-run” that is “primordial-only”).
- Required fix: Rephrase to clearly distinguish the two calculations: (i) primordial-only, and (ii) primordial plus standard density-bispectrum terms; state which reff belongs to which.

P2-Min10 (MINOR)
- Location: Sec. VI.B (p. 5)
- Problem: The sentence “drives a natural Bayesian preference for the bounce” reads as a model-selection claim without a calculation (later you emphasize prior sensitivity).
- Required fix: Soften to descriptive language that does not imply a computed preference (e.g., “suggests a potential Bayesian advantage under suitably chosen priors”).

P2-Min11 (MINOR)
- Location: Table II (p. 5)
- Problem: The entry “physical (conformal-Fermi) … + ≫ 146” is cryptic.
- Required fix: Replace with clear text (e.g., “formally infinite” or “parametrically larger than the gauge-frame ratio, since fNL → 0 in this frame for single-field slow roll”).

Explanation
These findings focus on reproducibility and auditability gaps that remained after the first pass: explicit definitions and domains for r and rcos; full specification of the internal Fisher setup; unambiguous appendix algebra; versioning of the Cai et al. source; and several clarity issues that could confuse a PRD reader attempting to verify results from the manuscript alone.