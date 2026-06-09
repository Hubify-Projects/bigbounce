# P1A auto-2026-06-08_1737pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (9430 chars)
**Wall time**: 503.4s

---

Referee report (Physical Review D – Methodology)

Scope of review
I evaluated the full 22-page manuscript, including all equations, figures, tables, captions, footnotes, and the abstract/conclusions. I audited dimensional consistency, internal arithmetic, sigma claims, and cross-checked every quoted scalar that appears in the abstract and conclusions for traceable support within the body.

General assessment
The submission aims to “close” four minimal ECH (Einstein–Cartan–Holst) dark-energy channels and to formulate a “perturbation-transparency theorem” for canonical scalar matter. While many high-level statements are directionally plausible, the methodology presentation does not meet PRD standards. Central claims rely on in-preparation companion papers for core statistical analyses, parameter inferences, and even dataset descriptions. Several load-bearing equations are explicitly presented as phenomenological ansätze rather than derived results, yet downstream conclusions in the abstract and conclusions are framed as if proven. Multiple statements essential to the purported closure (especially the 13–14 “barriers”) are qualitative with no quantitative derivations or bounds. There are dimensional inconsistencies (Λ vs ρΛ normalization), version-history language in the body, non-standard notations, and figures/tables containing non-reproducible or non-traceable numbers. Forecast-based significance claims are not computed in this paper.

Below I list specific findings. Severities: ESSENTIAL (must fix); MAJOR (significant revision); MINOR; NIT.

Findings

ESSENTIAL

P1A-E1
- Location: Abstract (p.1), and throughout (e.g., Sec. I B, p.5; Table I p.4; Sec. III B p.8; Data & Code Availability p.20; Table IV p.21)
- Issue: Reliance on non-public, in-preparation companions for all quantitative results that are presented as “verified” or “confirmed” (ΛCDM+ΔNeff MCMC verification; NaMaster pipeline validation; galaxy-spin null; ALP parameter fits; PTA reanalysis). Example quotes: “ΛCDM+ΔNeff MCMC verification … are documented separately in companion work in preparation [6].” Table IV labels “Verified Value” for H0, σ8, Ωm from that companion.
- Required fix: Either (i) include all of these analyses, data choices, priors, samplers, convergence diagnostics, and results in the present manuscript with full reproducibility, or (ii) remove every claim that depends on them and reframe the paper as purely theoretical. PRD cannot accept reliance on unpublished/inaccessible “companion” results for key claims.

P1A-E2
- Location: Abstract (p.1), Sec. X (pp.15–16)
- Issue: The “perturbation-transparency theorem” is stated as a central result but the proof is schematic. The core step “ϵμνρσ Rμνρσ(Γ̊) = 0 by the first Bianchi identity” is asserted, but there is no explicit variational demonstration that the Holst term contributes nothing to the quadratic or cubic perturbation action, nor a careful treatment of boundary terms or gauge. The extension to tensor sector is a single sentence.
- Required fix: Provide a complete derivation. At minimum: (a) write the Holst term in differential forms, show explicitly e∧e∧R = −NY + T∧T; (b) evaluate on FRW + scalar perturbations to second order, demonstrating that the variation w.r.t. metric perturbations vanishes; (c) show no residual boundary terms affect the perturbation EOM; (d) include a transparent statement of assumptions (matter content, boundary conditions). Alternatively, cite and follow a standard, detailed derivation with equations shown in-text.

P1A-E3
- Location: Eq. (10) (p.6) vs. Appendix B (p.20)
- Issue: Dimensional inconsistency between Λ and ρΛ normalizations. Main text: “Λeff = Ξ M^2Pl” with Ξ defined as dimensionless. Appendix B and the rest of the paper use ρΛ = Ξ M^4Pl (e.g., Eq. B2, Eq. 24). These are not the same normalization, and the abstract/conclusion statements about the vacuum-energy matching use ρΛ.
- Required fix: Choose a single consistent normalization for Λ and ρΛ throughout the paper. If the object controlled by Ξ is ρΛ, present Λ–ρΛ conversion (ρΛ = M^2Pl Λ/8π in conventions used) and use consistent units in all formulae, tables, and narrative. Audit and correct every occurrence.

P1A-E4
- Location: Sec. II A 2 (pp.5–6), Step 3–4; Appendix B (p.20)
- Issue: Central operator used in the “dark-energy mapping” is explicitly not a valid dim-4 EFT term off shell: Lodd ∼ (α/M) ε e e F has mass dimension +1 by the authors’ own counting. Yet the abstract/conclusions carry amplitude-level closure claims that leverage this operator and its induced scaling. PRD cannot accept a load‑bearing result derived from a self-acknowledged non-EFT operator.
- Required fix: Reformulate the analysis using a consistent, diffeomorphism-invariant, dimension‑4 operator basis (e.g., explicit Nieh–Yan with a coupling, gravitational Chern–Simons R∧R̃, and consistent four-fermion terms), or unambiguously demote all claims that rely on Eq. (6) to “speculative ansatz, not used to draw conclusions.” If the paper’s core closure depends on this operator, it is not acceptable in current form.

P1A-E5
- Location: Entire “barrier catalog” Sec. IX (pp.12–15)
- Issue: The 13 (14 listed) barriers are formulated as qualitative statements. Many are heuristic with no derivations, quantitative inequalities, or references that compute the claimed suppression or impossibility. Examples: Barrier 1 (Eq. 18 introduces t3 with no definition; the H0/MPl scaling is asserted), Barrier 5 (“No such mechanism exists within minimal ECH” without proof), Barrier 9 (Liouville conservation) stated without a concrete Hamiltonian flow or measure argument.
- Required fix: For each barrier, provide a precise statement, assumptions, and a derivation or a pointer to a published, quantitative result; include actual bounds where “suppressed” is claimed. Otherwise, reframe as “open conjectures” and remove them from the set of “logically independent constraints.”

P1A-E6
- Location: Table I (p.4), Sec. III B (p.8), Sec. V (p.11), Table IV (p.21)
- Issue: Galaxy spin “confirmed null” and quantitative statements (e.g., “hemisphere null,” “refutes Shamir’s 3% at high significance”) are asserted but all methods/results are deferred to an in-preparation Paper IV. No classifier architecture details, training sets, selection functions, null tests, or p-value computations are in this paper.
- Required fix: Remove the galaxy-spin results or include full methodology and results here (classifier description, training/validation, selection biases, sky cuts, null tests, p-value computation with trials factors). PRD will not accept claims anchored only to a non-public companion.

P1A-E7
- Location: Figures 3–4 and associated text (pp.13, 18); Table III (p.17)
- Issue: Forecast significance claims for SPHEREx fNL (3–5σ) and LiteBIRD β (∼9σ vs zero) are shown in plots and table entries, but the forecasts are not computed in this paper. The SPHEREx result is attributed to “companion work in preparation [2],” and LiteBIRD σ(β) is simply read off from design numbers without a pipeline model.
- Required fix: Either remove these figures and claims or include a self-contained forecast section (specification of survey, tracer populations, Fisher setup, shot noise, GR projection effects, photo‑z, multi-tracer combination, priors, and resulting σ’s). At minimum, remove detection-significance y-axes if you do not compute them.

P1A-E8
- Location: Footnote on p.2 and Sec. X n.2 (p.16)
- Issue: Version-history language in body: “Earlier versions of this manuscript erroneously identified …” PRD policy discourages version-history commentary in the main text.
- Required fix: Remove all version-history remarks from the main text/footnotes; present the corrected statement cleanly.

P1A-E9
- Location: Sec. IV B, Eq. (15) (pp.8–10)
- Issue: The ratio Δθone-loop/Δθobs expression mixes notations and contains an unexplained “MPl (α/M) βobs” in the denominator while also treating MPl·(α/M) as a standalone number. The steps are not clearly dimensionally reduced and the chosen ordering is declared “canonical,” then alternative orderings are mentioned.
- Required fix: Present a clean, unit-consistent derivation of the rotation angle induced by the one-loop operator, with a single, unambiguous dimensionless ratio, all factors defined (including what M is), and an explicit numerical evaluation using the stated inputs. Remove the “alternative ordering” prose.

P1A-E10
- Location: Table IV (p.21)
- Issue: Table presents “Verified Value” entries for cosmological parameters (H0, σ8, Ωm) with no methods/results in this paper. The label “Verified” is misleading given the text itself says the companion chains are not yet publicly posted.
- Required fix: Remove “Verified Value” column or replace with “Adopted value from [citation]” where the citation is a peer-reviewed, publicly available source. If your own analysis is required, include it here.

MAJOR

P1A-M1
- Location: Sec. II C (p.6), Eq. (10) and surrounding discussion; Sec. XII A (p.16); Appendix B (p.20)
- Issue: Inconsistent and shifting counts for the required e-folds (Ntot ≈ 92 vs ≈ 94) and the prefactor structure in Dinf = e^(-3Ntot) (Treh/MGUT)^(3/2). The prefactor is admitted as an ansatz, yet quantitative conclusions are drawn from it and used in the abstract/conclusions.
- Required fix: Choose one consistent normalization (ρΛ mapping to Ξ M^4Pl), derive Ntot from that choice once, and quarantine any further numbers as order-of-magnitude estimates. Make the ansatz status prominent in the abstract and conclusions, or remove quantitative reliance on it.

P1A-M2
- Location: Sec. II A 2, Step 4 (p.6), Eq. (7)
- Issue: The one-loop estimate for α/M is written with a δNY and a logarithm; the conclusion “[(α/M) MPl] ∼ 10^-2” is asserted without a concrete choice for g, ΛUV/μ, or δNY. A simple estimate with g ~ 1 and M ~ MPl/√γ would give ~ 5×10^-3 unless the log is very large.
- Required fix: Show the actual numerical inputs you use to reach 10^-2, or qualify this as a range with a plot versus log(ΛUV/μ). Alternatively, remove the specific 10^-2 claim and keep only the order-of-magnitude inequality.

P1A-M3
- Location: Sec. IV A (p.9)
- Issue: Route 1 (NJL) closure claims “many orders of magnitude” suppression without an explicit bound. ρNJL ∼ κ n^2ψ is asserted, but no numbers for nψ at recombination or later are provided to quantify the mismatch with ρΛ ~ (2.3 meV)^4.
- Required fix: Provide a concrete numerical bound (e.g., using n_baryon(z) with standard cosmology) and show that ρNJL/ρΛ ≪ 1 with all units explicit.

P1A-M4
- Location: Sec. IV C (p.10)
- Issue: Running of the Immirzi parameter: you present a schematic β-function [Eq. (16)] not taken from a published calculation and then assert Δγ/γ ∼ 10^-2 between MGUT and IR. No derivation or reference supports the magnitude used in the subsequent suppression estimate.
- Required fix: Either adopt the actual RG equation from Benedetti & Speziale (Ref. [27]) and compute Δγ/γ with the Standard Model content, or qualify this as an upper bound and do not use a numerical 10^-2 in your amplitude estimate without support.

P1A-M5
- Location: Sec. II C 1 (pp.6–7), “Reheating thermal-reset barrier”
- Issue: The claim that ⟨J5μ⟩ → 0 during reheating because C/P-violating scattering exceeds H is plausible, but no rates are shown. It is presented as a key closure supporting Barrier 14.
- Required fix: Provide an order-of-magnitude rate calculation comparing the relevant axial-current damping rate Γ5(Treh) with H(Treh), or cite a standard result. Without it, this remains a qualitative assertion.

P1A-M6
- Location: Sec. II C (p.6)
- Issue: “Parent black hole mass must exceed Mcrit ≈ 10^-3 M⊙” – no derivation or citation is given for this threshold.
- Required fix: Provide a derivation or a peer-reviewed reference for this criterion (and why it is relevant to your model).

P1A-M7
- Location: Sec. IV D (pp.10–11), Eq. (17)
- Issue: The relation β = (α/M) Δθ ≃ (α/M) √(2ρθ/m^2θ) is used to back out ρθ ≈ ρΛ for mθ ≃ H0. This assumes a homogeneous rolling/pseudo-static field with specific initial conditions. The derivation is not shown.
- Required fix: Derive Eq. (17) (e.g., from ϑ dynamics and the birefringence integral dβ/dη ∝ (α/M) ϑ′) and state the assumptions. Alternatively, add an explicit citation that derives this formula.

P1A-M8
- Location: Sec. X D (p.15)
- Issue: Notation “R e” and “R Re” for the Pontryagin density is nonstandard and risks confusion with the dualized one-curvature contraction Re(Γ̊).
- Required fix: Use standard notation R ∧ R̃ or R⋅R* for the Pontryagin density, and reserve Re only for the one-curvature dual contraction you analyze. Fix consistently in text and footnotes.

P1A-M9
- Location: Figures 2–4 and Table III (pp.5, 18, 17)
- Issue: Figures are largely schematic or forecast-based with no underlying computation here; captions do not fully specify axes units (Fig. 2 is qualitative), and Fig. 4 presents “detection significance” curves not derived in the paper.
- Required fix: Either remove these figures or replace with computed, reproducible content. Ensure all axes have units and the caption states the full computational setup.

P1A-M10
- Location: Sec. I A 1 (p.3)
- Issue: Claim of “14 mechanism-class structural constraints” with B8 “retained for historical completeness.” The independence and completeness of these constraints is not demonstrated.
- Required fix: Provide a dependency graph or argument showing logical independence, or tone this down to “a catalog of constraints we examined,” without independence claims.

MINOR

P1A-m1
- Location: Sec. II A 2 (p.6), Step 2
- Issue: Coefficient of the axial–axial contact term: “−(3/16) κ (ψ̄γaγ5ψ)^2 × γ^2/(γ^2+1)” appears consistent with the literature; however, a reference to a standard derivation with conventions would help.
- Required fix: Add a citation (e.g., Hehl–Datta, or a modern review) with matching conventions.

P1A-m2
- Location: Sec. IV B (pp.9–10)
- Issue: “αem/(4π) ≈ 5×10^-4” – more precisely ~5.8×10^-4. The text notes OOM robustness but the figure could be fixed.
- Required fix: Use the precise value or round consistently; state αem at the scale used.

P1A-m3
- Location: Sec. XII B (p.17)
- Issue: “Spectator-ALP birefringence … consistent with WMAP+Planck … at fa ∼ MPl, m ∼ H0 and θi ∼ O(1)” – this is plausible but please give or cite an explicit numeric example of fa, m, θi that reproduces βobs within uncertainties.
- Required fix: Provide one concrete parameter triplet and the resulting β, or cite a paper that does.

P1A-m4
- Location: Sec. IV E (p.11)
- Issue: The “fractional width Δmθ/mθ ∼ 10^-1” estimate around mθ ∼ H0 is stated without derivation.
- Required fix: Show the lines leading from β and ρΛ relations to this fractional width.

P1A-m5
- Location: Nomenclature throughout
- Issue: Mixed use of units (eV vs GeV) within the same paragraph (e.g., Sec. IV D). Although you remark on the conversion, it is clearer to pick one unit system per calculation.
- Required fix: Standardize units in each subsection.

P1A-m6
- Location: References (pp.21–22)
- Issue: Several citations are “in preparation” or arXiv placeholders with future years. While not fatal, any critical dependence on them must be removed (see ESSENTIAL items). Also, check diacritics (Godel → Gödel).
- Required fix: Update to published references where possible; ensure no critical claims depend on unpublished work.

NIT

P1A-n1
- Location: Footnotes and scattered places (pp.2, 16, 21)
- Issue: Version-history commentary and informal language (“earlier drafts,” “synthetic-Gaussian-likelihood”).
- Required fix: Remove; maintain formal tone.

P1A-n2
- Location: Typographical
- Issue: Occasional spacing/formatting inconsistencies (e.g., “Re” vs “R e”, missing tildes).
- Required fix: Copyedit for consistency.

P1A-n3
- Location: Table III (p.17)
- Issue: Footnote about a new DESI chain “running” with convergence R̂ − 1 ~ 3×10^-2 belongs in an internal note, not a PRD article.
- Required fix: Remove this operational status note.

P1A-n4
- Location: Sec. I A 2 (p.3)
- Issue: Redundant explanatory aside about comoving vs physical k appears multiple times.
- Required fix: Keep once; remove duplicates.

Length and scope
Given that many quantitative results are deferred to companions and several sections are schematic, the paper is too long for its present, primarily conceptual contribution. If pared down to a rigorous, self-contained derivation of the perturbation-transparency result (with a short, quantitative no-go for the other channels) and without the companion-dependent sections, the manuscript could likely be reduced to 12–14 pages.

## Summary recommendation
REJECT

The manuscript relies heavily on non-public companion papers for core results and quantitative claims; uses a central operator that is explicitly not a valid dimension-4 EFT term off shell; presents key “barriers” largely as qualitative assertions without derivations; contains dimensional inconsistencies (Λ vs ρΛ); and includes version-history language and forecast figures not computed here. The stated “perturbation-transparency theorem” is plausible but insufficiently derived in the text. To be suitable for PRD, the authors would need to (i) remove reliance on unpublished companions or include all analyses in this paper, (ii) reformulate with a proper EFT operator basis, (iii) present rigorous derivations with quantitative bounds for each no-go claim, and (iv) correct dimensional/notation inconsistencies. These changes are substantial and foundational rather than incremental.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes audit)

ESSENTIAL

P1A-E11
- Location: Sec. IV B, Eq. (14) and surrounding text
- Issue: Dimensional inconsistency in the one-loop operator. With ϑ dimensionless (standard in axion EFT), ∂μϑ has mass dimension 1 and J5μ has 3, so ∂μϑ J5μ has mass dimension 4. The coefficient must therefore be dimensionless O(αem/4π). The manuscript writes “−(1/16π^2) β(γ) MPl ∫√−g ∂μθ J5μ” and then treats it as “suppressed by M−1Pl,” which renders the Lagrangian density dimension 5. This mismatch propagates into Eq. (15)’s ratio.
- Required fix: Correct Eq. (14) to a dimensionless coefficient (or explicitly define θ with mass dimension −1 and re-derive all scalings). Provide a clean, unit-consistent derivation of the induced rotation with the corrected normalization.

P1A-E12
- Location: Sec. II A 1, Eq. (1)
- Issue: Nonstandard and internally inconsistent gravitational action. The action includes an explicit +¼ Tabc Tabc term while also stating it is “a shorthand for the four-fermion contact interaction obtained after integrating out torsion.” Writing an explicit T^2 term and also planning to integrate torsion out from the Palatini-Holst sector double-counts unless the full PGT kinetic structure and independent torsion variational equations are provided. The fixed 1/4 coefficient is neither derived nor referenced.
- Required fix: Start from the standard Hilbert–Palatini+Holst+Dirac action without an ad hoc T^2 term and perform the torsion elimination to obtain the four-fermion term with its correct coefficient; or, if you intend a Poincaré gauge theory with independent torsion dynamics, state the full torsion Lagrangian and field equations. Remove the “shorthand” TabcTabc from the bare action.

P1A-E13
- Location: Sec. II A 2, Eq. (4)
- Issue: Undefined symbol N in the prefactor “−(3π G N/2) × γ^2/(γ^2+1) × J5·J5”. N is never defined (number of fermion species? a normalization?). This directly affects amplitude estimates and any numerical bounds.
- Required fix: Define N precisely (and whether it is summed with charges/couplings), or remove N and adopt a standard, referenced normalization for the axial–axial contact.

P1A-E14
- Location: Throughout (Sec. II A 2 Steps 3–4; Sec. IV D Eq. 17; Eq. 15; Eq. 24)
- Issue: Symbol collision for M. M is used both as (i) the “area-gap mass scale” MΔ ∼ MPl/√γ in the Holst/LQG context, and (ii) the ALP-photon Chern–Simons scale in the birefringence section. This conflation propagates into mixed expressions such as MPl(α/M) and the β relation. It is unclear which M is used where and how the two are related.
- Required fix: Use disjoint symbols (e.g., MΔ for the LQG area-gap scale; Maf for the ALP-photon scale). Audit and correct every formula and numerical estimate that uses α/M.

P1A-E15
- Location: Data and Code Availability (p.20)
- Issue: Misleading availability statement. The paper asserts “All materials necessary to reproduce the cosmological and galaxy spin results are publicly available,” yet key claims (ΛCDM+ΔNeff verification, NaMaster validation, galaxy-spin null, ALP fits) depend on unpublished, in-preparation companions and non-posted chains/pipelines.
- Required fix: Amend the statement to reflect what is actually reproducible from the repository and remove claims tied to non-public companions; or include the full analyses in this paper with posted artifacts.

P1A-E16
- Location: Sec. XII B (p.17), last sentence
- Issue: Critical claim relies on an unavailable internal note. “The parity assessment finds no photon coupling in the minimal framework [47].” Reference [47] is a “companion technical note, available upon request.” PRD cannot accept load-bearing claims supported only by non-public notes.
- Required fix: Either remove the claim or replace it with a published derivation/citation; ideally, include the derivation in this manuscript.

P1A-E17
- Location: Sec. IV A (p.9) vs. Sec. II A 2 (Eq. 4)
- Issue: Internal inconsistency on γ-dependence. Eq. (4) explicitly includes the γ^2/(γ^2+1) factor in the four-fermion term, but Sec. IV A states “the torsion-elimination map is independent of γ at the classical level.” These cannot both be true in the same minimal coupling setup.
- Required fix: Reconcile by adopting the correct, referenced expression for the axial–axial operator in Einstein–Cartan–Holst with minimal (or specified non-minimal) fermion coupling, and make the narrative consistent.

P1A-E18
- Location: Sec. III A, Eq. (12)
- Issue: EB rotation formula mismatched to standard linear result. For a uniform small rotation and negligible primordial B, the leading relation is CℓEB ≈ 2β CℓEE (no subtraction of CℓBB). The manuscript writes CℓEB ≈ 2β (CℓEE − CℓBB) without derivation or caveat.
- Required fix: Provide a derivation or correct to the standard form with a clear statement of assumptions (primordial BB, lensing BB, delensing treatment).

P1A-E19
- Location: Sec. X C, Eq. (21)
- Issue: Ambiguous H definition in conformal-time equation. Primes denote derivatives w.r.t. conformal time η, but the friction term is written 2H h′ij. In conformal time the coefficient is 2 a′/a, not 2H unless H is redefined as a′/a. No definition is given, and elsewhere H denotes the physical Hubble rate.
- Required fix: Define H(η) explicitly (H ≡ a′/a or ℋ), or replace with 2(a′/a). Ensure dimensional consistency throughout perturbation equations.

P1A-E20
- Location: Sec. II A 2, Step 3 (Eq. 5) and prose
- Issue: Fij[K, R̊] undefined. The object FIJ[K, R̊] is introduced without definition (is it the curvature 2-form of the full connection with contorsion? a mixed functional?); this makes Eq. (5) ill-posed and undermines subsequent dimensional arguments.
- Required fix: Define FIJ precisely (full curvature of ω = ω̊ + K, or a specific contraction), and write the operator in standard differential-form notation with explicit indices/contractions.

MAJOR

P1A-M11
- Location: Sec. IV D, Eq. (17) and subsequent uses
- Issue: Units mixed silently. β = (α/M) √(2ρθ/m^2θ) combines α/M in GeV−1 with ρθ, mθ given in eV without an explicit conversion. While later text notes GeV–eV conversion in a different context (Eq. 15), no such clarification is provided here and the numerical examples assume base-eV inputs implicitly.
- Required fix: State a consistent unit system for α/M, ρθ, and mθ in this subsection and include the explicit 1 GeV = 10^9 eV conversion when evaluating β numerically.

P1A-M12
- Location: Sec. I A 1 (“Foundations A–G”) and Table II headers
- Issue: “Foundations A–G” are invoked as prior studies but are not actually specified or derived in this paper (no subsections, methods, or results corresponding to them). Readers cannot trace what each “Foundation” comprises beyond the barrier labels.
- Required fix: Either provide explicit subsections (or an appendix) detailing each Foundation’s setup and result, or remove the “Foundations” framing and present the barriers as author-proposed constraints with appropriate caveats.

P1A-M13
- Location: Sec. X D, Eq. (23) and surrounding text
- Issue: Over-assertive identity without boundary discussion. The text moves from the algebraic Bianchi identity to “Re(Γ̊) = 0 (identically),” but does not reconcile this with the standard e∧e∧R = −NY + T∧T identity’s boundary term structure (NY = d(e∧T) − e∧e∧R + T∧T). While T = 0 implies e∧e∧R = −NY, this only guarantees local vanishing if NY is shown to vanish as well; the text assumes, rather than demonstrates, that no boundary term contributes in the perturbation action.
- Required fix: Add an explicit boundary-term analysis (falloff conditions, gauge choice) demonstrating that the second-order (and cubic) perturbation action receives no surface contribution from the Holst sector.

MINOR

P1A-m7
- Location: Sec. IV B and Sec. XIII
- Issue: Same symbol β used for birefringence angle and for β-function β(γ) in Eq. (14). Although context differs, this invites confusion.
- Required fix: Rename the RG β-function as b(γ) or similar.

P1A-m8
- Location: Sec. II A 2, Eq. (24)
- Issue: Angle-bracket notation “⟨α/M MPl⟩” is introduced without definition (average over what?). If it merely denotes a number, brackets are unnecessary and confusing.
- Required fix: Remove angle brackets or define the averaging operation.

P1A-m9
- Location: Sec. X G, last paragraph
- Issue: Versioned numbers appear in the body (“supersedes the earlier synthetic-Gaussian-likelihood value…”). While you already removed version-history statements elsewhere, this one remains and mixes historical and current values in the science text.
- Required fix: Keep only the current value and move any historical comparison to a brief methods note or remove entirely.

P1A-m10
- Location: Sec. III A and captions
- Issue: EB formula/caption do not specify whether CℓBB includes lensing B or if delensing is assumed; this affects the presence/size of the “−CℓBB” term you wrote.
- Required fix: State explicitly the treatment of lensing BB and whether delensing is assumed in the EB relation shown.

Explanation
These items were not covered in the initial review. In particular, the dimensional inconsistency in Eq. (14), the nonstandard action in Eq. (1) (double counting torsion), undefined symbols, symbol collisions, the EB formula mismatch, and reliance on an unpublished technical note are newly identified and materially affect the manuscript’s correctness and clarity.