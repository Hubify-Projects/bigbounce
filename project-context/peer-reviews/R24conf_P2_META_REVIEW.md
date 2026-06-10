# P2 R24conf — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 309.6s

---

P2 META-REFEREE REPORT — Issues not caught by any of the 5 prior reviews

P2-META-E1
- Severity: ESSENTIAL
- Location: Abstract (pp. 1–2; “Caveat: if the Li & Brandenberger (c = 1) normalization convention is adopted… the detection significance halves”), Appendix A.2 (p. 22; “the detection significance |fNL|/σ(fNL) is convention‑independent… σ scales as 1/c while fNL scales with c… the ratio is invariant under a consistent change of c”)
- Why missed: Each prior referee focused on whether c=1 vs c=2 was disclosed, not on the internal logical consistency between the abstract and the appendix.
- Problem: The abstract attributes a halving of detection significance to switching the Komatsu–Spergel constant (c=2→1), but Appendix A states the opposite: the ratio |fNL|/σ(fNL) is invariant under a pure normalization change c. The body later explains the factor-of-two difference comes from missing time ordering, not a c-rescaling. These statements are contradictory as written.
- Required fix: Resolve the contradiction unambiguously and consistently across abstract, body, and appendix. State clearly: (i) a pure c-rescaling leaves |fNL|/σ(fNL) invariant; (ii) the halving arises from using a single-time-ordering (not from c), and therefore changes the physical amplitude entering the estimator. Rewrite the abstract’s caveat accordingly, and add an explicit cross-reference to Appendix A clarifying this point.

P2-META-M1
- Severity: MAJOR
- Location: Sec. II A (pp. 3–4; paragraphs on the 6-coefficient polynomial, benchmarks, null space: “The resulting null space is therefore a genuine theory‑modeling ambiguity…”), Abstract (p. 1; “null-space amplitude scatter ±0.13 absolute in r … from the underdetermined c1–c6 benchmark”)
- Why missed: Others asked for stability checks of r under the null space but did not question whether the “null space” is physical at all.
- Problem: The claimed three-dimensional “null space” (6 monomials, 3 benchmark constraints) is an identifiability artifact of fitting six coefficients to three points, not a physical ambiguity. Cai et al. provide a full shape (their Eq. 37) that fixes the coefficients uniquely in their basis; there is no fundamental underdetermination in the physics. Propagating a ±0.13 spread in r and 0.55–1.14 ranges from this underconstrained fit bakes a self-inflicted modeling uncertainty into the forecast.
- Required fix: Either (a) compute r directly from the full, published Cai et al. shape (no coefficient fitting), or (b) use sufficient constraints (many more triangle configurations) to uniquely fix the coefficients in your chosen basis. Remove the “null-space amplitude scatter” from the systematic budget unless you can show it reflects genuine physical freedom rather than underfitting.

P2-META-M2
- Severity: MAJOR
- Location: Sec. II A (p. 4; “a log-weighted grid with enhanced squeezed sampling gives r = 0.88 (vs. r = 0.87 on the uniform grid) …”), Sec. III B (p. 7; “The squeezed-limit cutoff is completely insensitive: varying x3,min from 0.001 to 0.200 changes r by < 0.0002”)
- Why missed: Reviewers flagged the <2×10−4 claim as implausibly precise, but none noticed it contradicts the earlier 0.01 shift attributed to squeezed sampling.
- Problem: The paper simultaneously claims that (i) upweighting squeezed triangles changes r by ~0.01 and (ii) varying a squeezed-limit cutoff over two decades changes r by <0.0002. These are inconsistent unless the procedures and weightings are carefully distinguished—which they are not in the current text.
- Required fix: Provide a single, consistent sensitivity analysis: specify weighting, grid resolution, and measure for both tests. Either reconcile the numbers (e.g., different weightings/measures) or correct them. Report reproducible inputs so both results can be independently verified.

P2-META-M3
- Severity: MAJOR
- Location: Sec. VI C (pp. 10–12; bullets describing σtheory), Table II caption (p. 12; “σtheory = 1.0 (recommended headline) … encompassing both the Cai et al. and Li & Brandenberger values plus the full ϵ-correction range”)
- Why missed: Other reviewers checked Bayes-factor arithmetic but not the logical claim about prior coverage.
- Problem: A Gaussian bounce prior with σtheory = 1.0 centered at −4.375 spans [−5.375, −3.375] at 1σ and does not include the Li & Brandenberger value −2.1875 (which is 2.19σ away). The manuscript repeatedly claims that σtheory = 1.0 “encompasses both literature values,” which is false.
- Required fix: Correct all statements asserting that σtheory = 1.0 encompasses the Li & Brandenberger value. If inclusion of both literature values is needed, state that σtheory ≳ 2.0 is required and adjust the Bayes-factor narrative accordingly.

P2-META-M4
- Severity: MINOR
- Location: Sec. II D (p. 6; “r ≈ 10−4 (from LQC quantum-geometry tensor suppression)”), Sec. III B and throughout (r used for template amplitude recovery)
- Why missed: Each reviewer focused on the template-overlap r but not on symbol reuse.
- Problem: The letter r is used both for the tensor-to-scalar ratio and for the amplitude recovery factor (template overlap). This symbol collision is easy to misread and risks confusion when scanning equations and figures.
- Required fix: Use distinct symbols (e.g., rt for tensor-to-scalar ratio, ρ for template-overlap recovery factor), and edit the manuscript to disambiguate all occurrences.

P2-META-M5
- Severity: MINOR
- Location: Sec. II (end of p. 4 to p. 5; injection–recovery test and fsky discussion)
- Why missed: Others noted that the test is not an LSS pipeline, but not the specific fsky scaling assumption.
- Problem: The flat-sky KSW-style injection/recovery uses a 2D CMB-like estimator and then applies an fsky scaling (1/√fsky) to discuss partial-sky effects. For a 3D galaxy bispectrum with photometric-z, this scaling is not appropriate and can be misleading.
- Required fix: Remove the 1/√fsky statement or qualify it explicitly as a CMB-estimator heuristic that does not apply to 3D LSS bispectrum analyses. Do not use this scaling in any quantitative forecast.

P2-META-M6
- Severity: MINOR
- Location: Sec. VI.C.b (p. 12; “at this [QSFI] endpoint the bounce‑vs‑QSFI shape mismatch vanishes and the Bayes factor against the bounce hypothesis collapses to BF → 1.”)
- Why missed: Reviewers caught the QSFI endpoint inversion, but not the Bayes-factor conclusion.
- Problem: Even if the QSFI shape approaches local in the squeezed limit, BF need not → 1 unless the amplitude prior predictive distributions are identical. Shape degeneracy alone does not force BF to unity; it removes one discriminator but leaves amplitude priors and nuisance structures.
- Required fix: Soften to “shape-based discrimination weakens substantially near the local-like QSFI limit; BF depends on the amplitude prior and nuisance modeling.” Remove the unconditional “BF → 1” claim.

P2-META-m7
- Severity: MINOR
- Location: Abstract (p. 1; “range 0.55–1.14 in the body of §II C”), Sec. II (actual null-space discussion lives in II A/B)
- Why missed: Others focused on content, not on subsection cross-references.
- Problem: The abstract points to Sec. II C (Assumptions) for the 0.55–1.14 r range, but that content actually appears earlier in Sec. II A/B. This mis-citation makes the paper harder to navigate.
- Required fix: Correct the cross-reference to the exact subsection where the null-space scan and r-range are presented (Sec. II A/B).

P2-META-m8
- Severity: MINOR
- Location: Sec. III B (p. 7; definition of shape cosine and overlap), Sec. III B/C (weightings)
- Why missed: Reviewers verified numbers but not metric definition.
- Problem: The manuscript reports rcos values but does not define the inner-product measure used for the shape cosine (e.g., k-space weighting, scale-invariant measure, or Fisher weighting). Without this, the reported rcos > 0.97 cannot be independently interpreted or reproduced.
- Required fix: Provide the explicit inner-product definition for rcos, including the measure and weighting (e.g., scale-invariant integral with 1/(k1 k2 k3) weighting, or a Fisher-weighted inner product). Include binning and convergence details sufficient for replication.

## Meta-review recommendation
MAJOR REVISIONS

Given the union of all six reviews, there are multiple blockers: (i) an internal contradiction between the abstract and appendix on normalization/significance invariance; (ii) a central methodological misstep treating a coefficient-fitting underdetermination as a physical “null-space” systematic; (iii) unresolved inconsistencies in squeezed-limit sensitivity; and (iv) several presentation/consistency issues (symbol collision, mis-citations, and over-strong QSFI BF claims). Correcting these, alongside the substantial issues already identified by the five referees (Bayes-factor arithmetic, AT/BNL definition, QSFI endpoint, systematics propagation, internal artifacts, and professional tone), is required.

With these addressed, the paper’s core contributions (template-overlap quantification, SPHEREx recast, and careful normalization discussion) could be solid. My confidence that the paper would survive external peer review after a thorough revision is moderate: the analysis can be made rigorous, but the current version mixes assumptions, internal artifacts, and inconsistent statements that must be cleaned and, in places, reworked quantitatively.