# P2 R40 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/research/focused_paper_source_integration/02_full_draft.pdf` md5=dbcc5834 pages=29
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7156 chars)
**Wall time**: 226.4s

---

Referee report on “Testing the Matter Bounce with Primordial Non‑Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook”

Scope of review
- Focus: methodology rigor (statistics, derivations, dimensional analysis, arithmetic consistency), estimator declarations, error propagation, reproducibility surfaces.
- I audited every scalar used in the abstract/conclusions, recomputed σ/significance ratios and Bayes‑factor numbers from what is shown in the body, and checked figure/table consistency.

Overall assessment
- The paper is a sensitivity recast, not a new Fisher forecast. Many caveats are explicitly stated. Most headline ratios/significances in the abstract numerically match the detailed calculations in the body once the authors’ bookkeeping is followed.
- However, several core load‑bearing steps remain under‑determined or insufficiently justified for PRD methods standards, notably the reconstruction of the bounce bispectrum shape from only three benchmark configurations to a 6‑coefficient symmetrized polynomial (which directly feeds the central overlap factor r), the use of a 2D CMB‑style injection test to “validate” a 3D galaxy‑bispectrum overlap, and the absence of a frozen, citable code/data DOI. Some numerical degradations introduced in the systematic budget (e.g., PNG‑bias priors) are not reproducibly linked to a Fisher computation.

Detailed findings

ESSENTIAL

P2‑E1 (Data and Code Availability; p.24–25)
- Problem: “archived at Zenodo (DOI inserted at submission)” is a placeholder; no immutable DOI or release/tag/commit hash is given. Numerous load‑bearing artifacts (e.g., “phase3 fisher overlap.json”, “c9g bf table recompute.py”, “null space analysis.py”) are referenced but cannot be verified without a frozen release.
- Required fix: Provide a permanent DOI and a version tag/commit hash corresponding exactly to the manuscript version. Ensure all named artifacts are included and paths match the text. PRD requires reproducibility with a stable archive.

P2‑E2 (Sec. II.A–B; pp.3–5)
- Problem: The 6‑coefficient degree‑9 symmetric polynomial P(k1,k2,k3) used to evaluate the bounce shape and to compute the central template‑overlap r is fit from only three benchmark configurations (squeezed/equilateral/folded), leaving a 3‑dimensional null space. The resulting r = 0.84 ± 0.02 (noise‑weighted) and the quoted central recast significance 5.2–5.5σ hinge on this representation. While a 10,000‑sample null‑space scan is reported, the sampling measure and basis choice are acknowledged as arbitrary, and the injection‑recovery and ℓ‑space Fisher validations both feed back the same internal polynomial family.
- Required fix: Replace the under‑determined reconstruction with either (a) a direct evaluation of the bounce bispectrum from the vertex‑level expressions (Cai et al.) across a sufficiently dense triangle grid, or (b) provide the explicit linear map from the Cai et al. integrand to your 6‑orbit basis (including per‑orbit Wick‑factor corrections) and demonstrate (with numbers, not just statements) that the computed r is invariant at the ≤1–2% level under basis changes and null‑space parametrizations. Alternatively, re‑compute the SPHEREx Fisher overlap using the analytic shape from Cai/Li (without re‑fitting coefficients). This is critical because r directly sets every quoted detection significance.

P2‑E3 (Sec. II.A end and Sec. III.B; pp.5, 8–9)
- Problem: “Injection/recovery test … KSW‑type optimal linear estimator … rmeasured = 0.90 ± 0.01.” This is a 2D flat‑sky, CMB‑style test with isotropic Gaussian noise applied to photometric‑z power spectra, explicitly not a 3D galaxy‑bispectrum estimator. It is presented as a confirmation of r but is not methodologically comparable to the SPHEREx multi‑tracer 3D bispectrum pipeline.
- Required fix: Remove this as a validation of the 3D r, or relegate it to a non‑binding sanity check. If retained as validation, provide a 3D galaxy‑bispectrum Fisher or mock‑analysis using the SPHEREx binning and survey window to demonstrate that the same r applies within quoted uncertainties.

P2‑E4 (Sec. III.B Eq. (5) and surrounding prose; p.8–9)
- Problem: Definition clarity. BNL and AT are used in Eqs. (1)–(2) with ambiguous parenthesization in “BNL = 10/3 P/AT i k^3_i”. The current typography makes it unclear whether Σi k_i^3 multiplies AT or divides the full fraction. This expression also underpins dimensional reasoning for BNL.
- Required fix: Rewrite Eqs. (1)–(2) with explicit parentheses and a clear definition of BNL and AT, and verify the degree counting step‑by‑step. Provide a brief derivation or a reference where exactly this normalization is introduced.

P2‑E5 (Sec. VII.B; pp.16–17; Fig. 5)
- Problem: Quantitative claims for σ(fNL) vs. bϕ prior width (e.g., “at 20% prior, MegaMapper SDB gives σ(fNL) ≈ 1.0; at 50%, σ ≈ 2.2”) are not reproducibly connected to a Fisher computation in the paper or to a citable table. Fig. 5 has no axis units or survey parameter table to reconstruct the curves.
- Required fix: Either (a) provide the Fisher setup (tracers, redshift bins, number densities, shot noise, k‑ranges, bias priors) and a table of σ(fNL) values vs. σ(bϕ)/bϕ that reproduces Fig. 5 with units, or (b) remove the specific numbers and replace them with a qualitative statement, clearly separated from the SPHEREx bispectrum channel (which is your primary headline).

P2‑E6 (Sec. IV and Table IV; pp.10, 20)
- Problem: The step from a “20–50%” bϕ prior to the adopted σ(fNL) values 0.9 and 1.0 used in the “All combined” rows is not derived. These numbers significantly affect the advertised 2.6–2.8σ floor.
- Required fix: Show the explicit mapping (via a Fisher recomputation or by citing a table in Heinrich et al. or Barreira) that justifies σ(fNL) → 0.9 (30%) and 1.0 (50%) for the SPHEREx multi‑tracer bispectrum. If these are scoping choices, label them explicitly as such and provide the sensitivity of the final significance to these inputs.

P2‑E7 (Sec. VII.C and Table III; p.18)
- Problem: P(BF>3) values are reported from a 2×10^5 Monte‑Carlo ensemble. Given the closed‑form likelihoods already presented, these probabilities can be computed analytically (function of σeff). Reporting MC‑based probabilities without the corresponding closed‑form makes verification cumbersome.
- Required fix: Add the closed‑form expression for P(BF>3) under your Gaussian assumptions and give the analytical values in Table III (keep the MC as a cross‑check if desired). Provide the exact σeff used in each row.

MAJOR

P2‑M1 (Sec. II.C and Sec. VIII; pp.6–7, 21)
- Problem: The ϵ‑correction coefficient κϵ is quoted as ranging from 5.6 to 80, leading to a 0.6–8% correction in fNL. The lower bound is attributed to the explicit prefactor scaling AT ∝ 1/ϵ^3; the upper bound is a “schematic scaling” from mode‑function growth. No derivation or worked example is provided.
- Required fix: Provide a concrete derivation or numerical estimate leading to 5.6 and 80 (even if in an appendix): show the derivative of the cubic prefactor at ϵ=3/2 and the separate contribution from the mode‑function amplitude scaling that yields the “×14” factor. If this cannot be supported, reduce the claim to a qualitative bound without numbers and remove the 0.6–8% headline.

P2‑M2 (Sec. III.B; pp.8–9)
- Problem: The paper states “10 physically motivated weighting schemes” for r and reports four values (CMB Fisher 0.876; SDB 0.829; SPHEREx‑like 0.830; flat 0.835) and a spread ±0.02. The remaining schemes, exact formulae for weights, and the survey inputs behind “SPHEREx‑like” are not specified.
- Required fix: Provide a table listing each weighting scheme, its explicit weight w(k1,k2,k3) (or ℓ‑space equivalent), triangle domain, k‑cuts, and the resulting r with uncertainty from numerical integration. Identify the exact inputs for “SPHEREx‑like.”

P2‑M3 (Sec. III.B; p.9)
- Problem: The claim that changing the squeezed cutoff x3,min from 0.001 to 0.2 modifies r by <2×10^-4 is surprising given the asserted importance of squeezed configurations for local shapes.
- Required fix: Provide a short table or figure showing r vs. x3,min for one or two representative weightings (with numerical precision), and state the triangle sampling used in each case.

P2‑M4 (Figures 4–5; pp.16–17)
- Problem: Axis labels/units and survey parameters are insufficient. Fig. 4 left lacks axes units for kmin; Fig. 5 left lacks units and a legend entry for the SPHEREx bispectrum (dashed line). The underlying survey assumptions (n(z), b1(z), fsky, k‑ranges) are not documented alongside the figures.
- Required fix: Add units and full captions that list the survey assumptions needed to reproduce the curves, or move these plots to an appendix and mark them as schematic.

P2‑M5 (Appendix A; pp.25–27)
- Problem: The text claims a “symbolic verification” of i⟨[ζ^3,L]⟩ = −2 Im⟨ζ^3 L⟩ and that the permutation/Wick counting resolves the Cai/Li factor‑of‑two. However, the explicit permutation map and symmetry factors Sv used to go from Eqs. (A5) to (A7) are not given, and the verification relies on the unreleased code artifacts.
- Required fix: Include the explicit list of symmetry factors and, at minimum, a compact worked example for one vertex that shows how the single ordering doubles to the commutator result. Tie this to a released, DOI‑backed notebook so the claim is verifiable.

MINOR

P2‑N1 (Eqs. (1)–(2); p.3)
- Problem: Notation clarity. The role of AT vs. BNL and the normalization via Σi k_i^3 are hard to parse. The degree counting explanation is terse.
- Required fix: Add one explanatory sentence and fix parentheses as per P2‑E4; optionally include a pointer to where this normalization is standard.

P2‑N2 (Sec. II.A footnote and related text; pp.3–4)
- Problem: The monomial‑basis mapping and orbit counting are central but described in a long paragraph with informal references to JSON artifacts. This is difficult to follow in print.
- Required fix: Move the mapping to an appendix with a short, numbered recipe and retain only the key conclusion in the main text.

P2‑N3 (Sec. VIII; p.21)
- Problem: The linear relation fNL(ns) ≈ −35/8 − c′(ns − 1) is stated with c′ ∈ [0.7, 10] but no illustrative plot/table is shown.
- Required fix: Provide a one‑line worked example at ns = 0.9649 showing both bounds in fNL, as you do in prose, or a tiny table.

P2‑N4 (Fig. 2 caption; p.11)
- Problem: The caption is long and blends methodological caveats with plot description.
- Required fix: Split into two sentences: what is plotted, and how to interpret. Keep the “not used in any headline” note, which is useful.

NITS

P2‑T1 (Throughout)
- Minor typos and style: “nonneg” → “non‑negative”; occasional double spaces; em‑dashes used inconsistently.
- Fix: Copy‑edit.

P2‑T2 (Figures)
- Add units to axes where applicable (k in h Mpc^-1), and ensure all legends identify lines (e.g., “SPHEREx bispectrum (σ=0.7)” in Fig. 5).

P2‑T3 (Acronyms)
- Expand PNG, SDB, CFC, QSFI at first use in the main text and abstract.

P2‑T4 (Acknowledgments; p.27)
- The explicit mention of “AI‑assisted software tooling (Anthropic Claude)” may be acceptable, but some journals prefer a neutral phrasing. Check PRD policy; adjust if needed.

Arithmetic and consistency checks (selected)
- finf_NL = (5/12)(1 − ns) at ns=0.9649 → 0.0146; ratio 4.375/0.0146 ≈ 299; authors round to 290 in abstract and 290 in text; acceptable given 2 s.f.
- Template‑corrected significance: 4.375×0.84/0.7 = 5.25σ; the reported 5.2–5.5σ range across r ∈ [0.829,0.876] is consistent (5.19–5.48σ).
- GR quadrature: σeff = √(0.7^2+1^2)=1.221 → 3.675/1.221 = 3.01σ; matches “∼3.0σ”.
- All‑combined 30% bϕ prior + GR 1.0: σeff=√(0.9^2+1^2)=1.345 → 3.675/1.345=2.73σ; matches text.
- Planck PR4 recast: σ′ = 5.0/0.876 = 5.71; Δ/σ′ ≈ 0.75σ; consistent.
- Bayes factors: delta prior, W=30, σ=0.7: 30/(√(2π)σ)=17.1; narrow W=10 exact integral 6.99; Gaussian bounce prior σtheory=1.0 → 30/(√(2π)√(σ^2+σtheory^2)) ≈ 9.81; all consistent with Table II and prose.
- SDB joint Fisher degeneracy: σunmarg(fNL)=1.53, ρ=−0.87 → σmarg=1.53/√(1−ρ^2)=3.10; reported 3.08; within rounding.

Length and scope
- For a sensitivity recast (not a full Fisher re‑derivation), 29 pages is long. Condense background/discussion tangents (ECH/Holst decoupling, anomaly‑tracer aside, cosmic birefringence note) and move basis‑mapping details/JSON references to appendices. Recommended maximum main‑text length: ~18–20 pages, with technical material in appendices.

Abstract‑last drift check
- Abstract claims are generally mirrored in the body with appropriate caveats. The only place where the body is more tentative than the abstract is the template‑overlap validation (abstract says “validated via ℓ‑space Fisher overlap, 200 injection‑recovery realizations”); per P2‑E3 this must be softened or replaced by a 3D validation. Also, the Bayes‑factor envelope in the abstract should explicitly state that the headline BF ≈ 9–14 already includes the r‑rebooking; the body explains this but the abstract compresses it into parentheticals.

Provenance surfaces
- Replace the DOI placeholder (P2‑E1). Ensure all artifact filenames in the text exist in the archive. Include a manifest mapping each figure/table number to the generating script and inputs.

Standalone‑reader test
- Most symbols are defined in place. Clarify Eq. (1)–(2) (P2‑E4) and add first‑use acronym expansions (P2‑T3).

Effect sizes
- The paper does report effect sizes in the form of |fNL| r/σ and BF magnitudes; acceptable.

## Summary recommendation
MAJOR REVISIONS

The numerical claims largely check out, but several core methodological steps that underpin the central sensitivity (the r overlap and its “validation,” the bϕ‑prior degradation used in the 2.6–2.8σ floor, and the absence of a frozen DOI for code/data) must be addressed before PRD can consider publication. Tighten the reconstruction of the bounce shape or replace it with a direct evaluation; remove or replace the 2D injection test with a 3D validation; provide a reproducible mapping from bϕ priors to σ(fNL); and supply a permanent code/data archive. With these changes and minor clarity/format fixes, the paper could be suitable as a careful sensitivity recast.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes pass)

ESSENTIAL

P2-E8 (Fig. 4 right; Sec. VII.A; null-procedure comparability and r usage)
- Problem: The right panel shows “detection significance for fNL = −35/8” for the SDB channel while the caption also overlays a “SPHEREx bispectrum (σ=0.7, dotted)” reference curve. It is not stated whether the SDB significance includes the template-overlap factor r (it should not), whereas the bispectrum significance elsewhere in the paper is always quoted after r-correction. This mixes two different null procedures on the same axis without an explicit “not directly comparable” qualifier.
- Required fix: State explicitly in the caption and body that SDB significances are |fNL|/σSDB (no r), while bispectrum significances are |fNL| r/σbis. Either remove the dotted bispectrum line from this SDB plot or add a clear “different estimator; not directly comparable” label. If the dotted line is kept, decide whether it shows 6.25σ (naive) or 5.25σ (template-corrected) and say so.

P2-E9 (Eq. (4) units; dimensional bookkeeping across text)
- Problem: The paper says “wavenumbers k are comoving and quoted in h Mpc−1 throughout” (Sec. III.A) but Eq. (4) uses H0 and Ωm in SI/c=1 units implicitly. Without stating the unit system for H0 (h vs km s−1 Mpc−1 vs s−1) and whether c=1 is assumed, M(k, z) can be misread dimensionally.
- Required fix: State the unit convention explicitly (e.g., c=1, H0 = 100 h km s−1 Mpc−1, k in h Mpc−1) and confirm that M(k, z) is dimensionless under that convention. Add a one-line dimensional check so readers don’t have to infer hidden h/c factors.

P2-E10 (Fig./table provenance manifest)
- Problem: Several figures and tables are not mapped to specific scripts/commits in the manuscript itself (only in the generic “Data and Code Availability” paragraph with a placeholder DOI). For PRD reproducibility, readers must be able to go from Figure/Table number to the exact generator and inputs.
- Required fix: Add a short manifest (table or appendix) that maps each Figure and Table to the exact script name, inputs, and commit/tag (once the Zenodo DOI is provided per P2‑E1 in your first-round report). This is necessary for independent regeneration.

MAJOR

P2-M6 (bϕ treatment inconsistency; Sec. IV vs Sec. VII.B)
- Problem: Sec. IV states Heinrich et al. “treats the PNG bias parameter bϕ with a fixed universality relation” and warns that marginalizing bϕ would widen σ(fNL). Sec. VII.B then says Heinrich et al. “marginalize over bϕ … assuming the universal-mass-function relation,” which reads as both “marginalized” and “fixed by relation.” These are not the same operation.
- Required fix: Align the description with the actual Heinrich et al. treatment and cite the exact equations/pages. If bϕ is fixed by UMF (i.e., not a free parameter), say “fixed by UMF, not marginalized.” If it is a free parameter with a UMF prior, give the prior. This matters for justifying the σ(fNL) baselines used in Table IV.

P2-M7 (Shape-mismatch variance not propagated; Sec. III.B, Eq. (5))
- Problem: The significance budget treats only the amplitude loss r (σ → σ/r in bounce space). The extra variance from template mismatch (“projection noise”) is only heuristically bounded via 1 − rcos^2 ≲ 0.03–0.06 and then ignored in σeff. Under survey weights, that residual can inflate σ beyond σ/r.
- Required fix: Provide a quantitative Fisher cross-shape estimate (under SPHEREx weights) of the variance inflation due to using a local template on a bounce-shaped signal, or give a rigorous upper bound translated into Δσ/σ. If negligible, show the number; if non-negligible, include it in σeff.

P2-M8 (Fig. 4 right numerical construction; channel consistency)
- Problem: The right panel’s “detection significance” vs kmin is not documented: which σ(kmin) curve is used (SDB only), and whether r or any GR/bϕ degradations are included. The panel is then compared to a fixed bispectrum dotted line. This risks misinterpretation as like-for-like.
- Required fix: Specify precisely how the right-panel curve is computed (channel, weights, r usage, degradations). If r is not used (appropriate for SDB), add an explicit note in the caption and text to avoid conflating it with the bispectrum baseline.

P2-M9 (Non-Gaussian covariance justification; Sec. IV, Eq. (7))
- Problem: The decision to reuse σ(fNL)=0.7 at the bounce fiducial rests on a ζ-field scaling estimate (Eq. (7)), which the text labels “heuristic” and “not a galaxy-covariance derivation.” Yet this step underpins the core use of 0.7 at fNL = −4.375.
- Required fix: Either (a) provide a galaxy-field covariance check (even a back-of-envelope using tree-level six-point terms under SPHEREx n(z), b1, shot noise) showing the fractional change in σ(fNL) remains ≪1%, or (b) cite a published result demonstrating that the fNL=O(1–5) shift at SPHEREx depth does not materially change the bispectrum covariance. Otherwise, label the 0.7 reuse as an assumption and quantify sensitivity if σ widened by, e.g., 5–10%.

MINOR

P2-N5 (BF vs SSFSR closed form; Sec. VII.C/Table III)
- Problem: Very large Bayes factors vs SSFSR (e.g., 3.5×10^8) are quoted without the simple 2-point Gaussian likelihood ratio formula shown.
- Required fix: Add the one-line closed-form BF(point vs point) = exp[(Δθ)^2/(2σeff^2)] with Δθ = −35/8 − 0.015 at σeff specified for each row. This makes Table III immediately checkable.

P2-N6 (Fig. 4 caption and units)
- Problem: Fig. 4 left axis lacks k units and the kmax used for the calculation; right panel lacks an explicit note that it is SDB-only (no r).
- Required fix: Add units (k in h Mpc−1), state kmax, fsky, tracer selection and whether shot noise is included, and label the right panel as SDB-only.

P2-N7 (Minor rounding drift in the inflation contrast)
- Problem: The ratio 4.375/[(5/12)(1−0.9649)] = 299 is rounded to “≈ 290” in multiple places. That’s fine as 2 s.f., but the text mixes 290/299 in different sections.
- Fix: Pick one rounding for consistency (e.g., “≈ 3.0×10^2” or “≈ 300”).

NITS

P2-T5 (Terminology consistency)
- Problem: The four-fermion term is “Hehl–Datta,” not “Hehl‑Datta–Mercuri” (Mercuri clarified Holst/topological aspects; Hehl–Datta is the axial-axial induced term). Current phrasing is a bit awkward.
- Fix: Use “Hehl–Datta four-fermion term; see Mercuri/Freidel et al. for Holst/topological context” or similar.

P2-T6 (Fig. 5 legend completeness)
- Problem: The dashed “SPHEREx bispectrum (σ=0.7)” line is not labeled in the legend; the caption mentions it textually only.
- Fix: Add a legend entry for the dashed line and its meaning (bispectrum baseline; no dependence on bϕ).

Brief rationale for why these are new
- These items focus on cross-figure comparability (especially Fig. 4), unit conventions in M(k, z), an explicit check of point-vs-point Bayes factors, internal consistency of the bϕ treatment, and the omission of shape-mismatch variance in σeff. They were not covered in the initial review’s essential/major items, which concentrated on the underdetermined polynomial reconstruction, the 2D injection test, the missing DOI, and the bϕ-prior-to-σ mapping.