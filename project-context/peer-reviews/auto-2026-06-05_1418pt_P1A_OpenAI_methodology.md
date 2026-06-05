# P1A auto-2026-06-05_1418pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7834 chars)
**Wall time**: 267.0s

---

Referee report on “Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter”

Overall scope of review
I evaluated the full manuscript (21 pages) with a focus on methodological rigor: derivation chains, dimensional consistency, internal arithmetic, statistical claims, estimator specification, reproducibility, and figure/table consistency. I recomputed all quoted σ-levels and order-of-magnitude relations that are numerically checkable from the text. Below is a comprehensive list of findings with severity levels and required fixes.

ESSENTIAL findings (must be fixed for PRD)

P1A-E1 (Sec. IV B, p. 9–10): Dimensionally inconsistent one-loop operator (Route 2)
- Issue: Eq. (14) is written as Γ_parity-odd_one-loop = −(1/16π^2) β(γ) MPl ∫ d^4x √−g ∂μθ J5μ. The narrative then states “dimensionless coefficient ... multiplied by the Planck mass to a single negative power,” but Eq. (14) multiplies by MPl (positive power), not 1/MPl. The subsequent ratio (Eq. 15) tries to “restore” an H0/MPl factor by hand, admitting alternative orderings. This is internally inconsistent and renders the closure argument for Route 2 non-auditable.
- Required fix: Provide a consistent derivation of the one-loop parity-odd operator with correct mass dimension throughout. Either:
  - Derive Eq. (14) from a published calculation, including the precise MPl scaling, or
  - Present a fully self-consistent EFT ansatz with explicit dimensional bookkeeping leading to Eq. (15), and then recompute the amplitude ratio. State clearly whether the coefficient is ∝1/MPl or ∝MPl and propagate consistently. Update numerical estimates accordingly.
  - Remove hand-waving about “alternative orderings” and present a single, dimensionally correct chain.

P1A-E2 (Sec. X, p. 14–15): “All-orders” perturbation-transparency theorem is asserted, not proven
- Issue: The central “perturbation-transparency” claim is stated for “all perturbation orders,” yet only a short sketch is provided. There is no explicit variation of the action showing that all scalar/tensor perturbation terms vanish once torsion is set to zero and the Holst term reduces to the Pontryagin density. Boundary term subtleties and gauge issues are not addressed; “all orders” requires more than a linearized demonstration.
- Required fix: Supply a rigorous proof or at least a complete second-order calculation for both scalar and tensor sectors that explicitly shows (i) the vanishing torsion solution for canonical scalars in the perturbed action, (ii) the Holst term reducing to a boundary term with no contribution to the equations of motion, and (iii) that no parity-odd residual appears in the cubic action (bispectrum). Address boundary conditions in cosmology and gauge choices. If “all orders” cannot be rigorously proven here, limit the claim to the order you compute and restate the result accordingly.

P1A-E3 (Multiple locations): Reliance on unpublished or “in preparation” companion works for core inputs
- Issue: The paper repeatedly cites non-public “companion works” (Paper I(b) [6], Paper II [2], Paper III [46], Paper IV [23], [47]) for key numbers (H0 = 67.68 ± 1.06, ΔNeff posterior, ALP MCMC fits, NaMaster validation, galaxy spin null, PTA reanalysis, etc.). PRD requires that all load-bearing results be documented in the submitted manuscript or in publicly available, citable literature.
- Required fix: Remove all reliance on unpublished companions for any conclusion in this paper, or include sufficient methods, data, and results within this manuscript to substantiate the claims (MCMC settings and priors, diagnostics, estimator definitions, dataset lists, numerical values, uncertainties). Alternatively, replace these with public, citable sources (e.g., quoted Planck 2018 values) and do not import any internal/companion-only numbers.

P1A-E4 (Sec. IV D, p. 10–11; Sec. XII B, p. 16): Conflicting and under-specified inference of α/M from βobs
- Issue: The text infers α/M ~ 10−21 GeV−1 from βobs without an explicit model for Δθ (or, equivalently, ρθ and mθ). Eq. (17) shows β = (α/M) √(2ρθ/mθ^2), but unless ρθ and mθ are fixed independently, β does not determine α/M. Elsewhere, the same O(10−21) comes from a one-loop estimate [(α/M) MPl] ~ 10−2. These are not equivalent inference routes and should not be conflated.
- Required fix: Separate clearly:
  - One-loop motivated estimate for α/M (with full dimensional derivation; see P1A-E1), and
  - Fits to βobs, which require a specified ρθ and mθ model.
  If you keep Eq. (17), state explicitly the assumed ρθ and mθ when quoting α/M; otherwise remove any claim that βobs alone fixes α/M. Recompute any downstream amplitude budgets accordingly.

P1A-E5 (Sec. IX L, p. 13–14): Unjustified bound ΩGW|bounce ≲ (ρcrit/ρPl)^2
- Issue: Barrier 12 introduces an inequality ΩGW|bounce ≲ (ρcrit/ρPl)^2 ≃ 0.07–0.17 without derivation. No definition of ΩGW at the bounce epoch is provided, no transfer to today is calculated, and no argument is given for the quadratic dependence.
- Required fix: Provide a derivation of this bound starting from the stress-energy of gravitational waves or a robust energy-budget argument, with assumptions explicitly stated. If this cannot be justified, remove Barrier 12 as a quantitative constraint and recast it qualitatively.

P1A-E6 (Throughout; Table III, p. 16): Symbol collision for γ
- Issue: The symbol γ is used for both the Barbero–Immirzi parameter and the “PTA spectral index γ,” and γ = 3.0 is called a “bounce” value in Table III, while γ = 0.274 denotes the Immirzi parameter elsewhere. This is unacceptable ambiguity.
- Required fix: Use distinct, standard symbols (e.g., γBI for Barbero–Immirzi, and γPTA or n_t for a spectral slope) and revise all tables/sections accordingly.

P1A-E7 (Appendix B, p. 19–20): Version-history language in the paper body
- Issue: “... not the ~35 misstated in earlier drafts” appears in Appendix B. Version-history statements are forbidden in the paper.
- Required fix: Remove all version-history prose (e.g., “earlier drafts,” “supersedes,” “this volume,” “hUBIFY-2026-00x”) from the main text, tables, and references.

P1A-E8 (Sec. II C.1, p. 6–7; Sec. XII A, p. 15): Ad hoc thermal factor and use of Ntot ≈ 92 as a load-bearing scalar
- Issue: The dilution factor Dinf ≡ e−3Ntot (Treh/MGUT)3/2 is explicitly acknowledged as an ansatz, with the extra 1/2 power justified only by “parity-odd density-of-states aesthetics,” not by a calculation. Yet Ntot ≈ 92 is used repeatedly as a structural headline number and in the abstract. Later, a “reheating thermal reset” argument claims any memory is erased, undermining the very use of Dinf.
- Required fix: Move all Ntot-based quantitative claims to a clearly labeled heuristic appendix, or (preferably) remove Ntot ≈ 92 from the abstract and conclusions. If retained, provide a first-principles derivation for the (Treh/MGUT)3/2 factor or drop it entirely; otherwise, treat Ntot only as an illustrative parameter with no quantitative weight in constraints.

P1A-E9 (Sec. III B, p. 8; Sec. V, p. 11): Galaxy spin “confirmed null” relies on non-public analysis
- Issue: The claimed all-sky dipole null and refutation of a 3% asymmetry are sourced to “Paper IV [23] (in preparation).” No methodology, sample definition, classifier calibration, bias tests, or numbers are given here.
- Required fix: Either include the full analysis in this manuscript (methods, datasets, masks, classifier performance, null tests, uncertainties) or remove the claim. Citing an unpublished, unavailable work is insufficient for PRD.

P1A-E10 (Sec. III A, p. 7–8; Sec. VI, p. 11): Side-by-side σ values without “not directly comparable” disclaimer
- Issue: The manuscript juxtaposes the WMAP+Planck birefringence significance (3.6σ) and the ACT DR6 significance (2.9σ) without explicitly stating that different datasets and pipelines yield non-comparable σ values.
- Required fix: At every juxtaposition of σ values from different experiments or null procedures, add a clear statement that they are not directly comparable (as required in the review instructions). Do the same wherever SPHEREx forecast σ(fNL) is set against other pipelines.

P1A-E11 (Sec. IV E, p. 11): Route-4 “naturalness closure” still uses a non-derived α/M and ad hoc β relation
- Issue: The closure argument for Route 4 hangs on tuning mθ ~ H0 and a fixed α/M ~ 10−21 GeV−1. But α/M is not actually derived in this paper (see P1A-E1/E4), and the birefringence formula lacks the standard factor-of-1/2 and time-evolution assumptions.
- Required fix: Provide the standard birefringence rotation formula (e.g., Δβ = (gφγ/2) [φ(rec)−φ(today)] with gφγ ≡ α/M), justify the quasi-static/slow-roll limit used to convert to Eq. (17), include the 1/2 factor if appropriate, and state the assumed φ dynamics. Then recompute the ρθ relation and the tuning statement. Otherwise, recast Route 4 as an agnostic phenomenology statement without claiming closure.

MAJOR findings

P1A-M1 (Sec. II A.3, p. 6; Table IV, p. 20): Planck vs reduced-Planck conventions, and ρPl definition
- Issue: The manuscript alternates between MPl (∼10^19 GeV) and reduced M̄Pl (2.435×10^18 GeV) conventions without ever stating which is used. ρPl is used with LQC formulas that assume ℓP^2 = G; please state whether MPl or M̄Pl is used everywhere, and ensure all numerical conversions (e.g., H0/MPl) are consistent.
- Required fix: Declare conventions (natural units, which MPl, how ρPl is defined) at the start of Sec. II. Replace all mixed uses with consistent notation; recompute any order-of-magnitude products (e.g., (α/M)MPl ~ 10−2) accordingly.

P1A-M2 (Sec. II A.1, p. 5): Non-standard shorthand “+ (1/4) TabcTabc” in the action
- Issue: Writing + (1/4) T^2 as a shorthand for the four-fermion contact can mislead readers into thinking a propagating torsion kinetic term is assumed. In EC, after eliminating torsion, the induced four-fermion term arises with specific signs from the curvature decomposition, not an arbitrary +1/4 T^2 insertion.
- Required fix: Remove this term from the fundamental action and instead show explicitly the algebraic torsion elimination from the Palatini–Holst action with fermions, leading to the Hehl–Datta term. Keep kinetic torsion terms out unless Poincaré gauge theory is truly intended.

P1A-M3 (Sec. IV A, p. 8–9): Four-fermion coefficient and parity claim need a precise citation/derivation
- Issue: The coefficient −(3/16) κ(ψγ¯aγ5ψ)^2 with the stated γ^2/(1+γ^2) scaling is presented without a precise derivation-chain citation (the factor depends on conventions and non-minimal couplings).
- Required fix: Cite a precise derivation with the same conventions (e.g., Mercuri 2006/2009 or standard EC references) and show how your Eq. (13) follows from your action. Clarify parity: J5 is a pseudovector; (J5)^2 is a scalar (parity-even). This is correct, but include a brief, explicit parity argument to avoid confusion.

P1A-M4 (Sec. II A.2, p. 5–6; Appendix B, p. 19): Off-shell operator of mass dimension +1 used in the body text before confining to an appendix
- Issue: The parity-odd operator in Eq. (6) has dimension +1 and is explicitly acknowledged as a non-EFT operator requiring on-shell scaling. Nonetheless, it is threaded through the narrative in Secs. II–IV.
- Required fix: Confine all use of this operator to a dedicated appendix labeled “Phenomenological ansatz,” and clearly separate any results that depend on it from the main, operator-level claims. Do not mix ansatz-dependent scalings into sections that claim model-independent closures.

P1A-M5 (Sec. XII B, p. 16; Sec. X, p. 14–15): Claim “no photon coupling in the minimal framework” sourced to [47], a non-public technical note
- Issue: A core statement (“no photon coupling in the minimal framework”) is attributed to an unavailable technical note.
- Required fix: Either provide a brief derivation in this paper or cite a peer-reviewed/publicly available source for this statement. Otherwise, rephrase as a conjecture or remove.

P1A-M6 (Sec. XIII, p. 16–17): SPHEREx σ(fNL) quote and realism claims
- Issue: You quote σ(fNL) ≈ 0.7 (Fisher-ideal) from Heinrich et al. (2024), then degrade to 3–5σ “realistic” based on GR projection effects, bφ uncertainty, and photo-z degradation without performing any computation in this paper.
- Required fix: Either (i) provide a short, reproducible calculation showing how each degradation enters and how 6.25σ (ideal) decreases to 3–5σ, or (ii) state clearly that this is a qualitative extrapolation from Heinrich et al. and remove σ-level claims beyond what is in the cited paper.

P1A-M7 (Table III, p. 16): “PTA γ (real-KDE)” uses unpublished analysis and nonstandard estimator
- Issue: A “real-KDE GPU MCMC” yielding γ = 2.567 ± 0.382 is not standard, and the work is not public. The meaning of “γ” is nonstandard (see P1A-E6).
- Required fix: Remove this row or replace it with a result from a peer-reviewed/public source with standard estimators. Clarify the parameter and estimator definition if you insist on keeping any PTA comparison.

P1A-M8 (References, p. 19–21): Placeholder/future arXiv identifiers, “this volume” language
- Issue: Multiple references list future years or arXiv identifiers that do not exist as of submission (e.g., [5], [41]–[45], [47]), and “this volume,” “in preparation,” and project codes (“hUBIFY-2026-00x”) are sprinkled throughout.
- Required fix: Replace every such reference with a published journal or freely available arXiv entry that exists now, or remove the citation and any associated claims. Remove all “this volume,” “in preparation,” and internal codes from references.

MINOR findings

P1A-m1 (Sec. III A, p. 7): EB rotation formula
- Issue: The small-angle rotation formula Cℓ^EB ≈ 2β (Cℓ^EE − Cℓ^BB) is stated without the usual reminder that this assumes frequency independence and uniform rotation, and that BB is typically subdominant.
- Required fix: State the small-angle, uniform-β assumption and that the formula is frequency-independent in this limit.

P1A-m2 (Sec. II B, p. 6; Eq. 9): LQC ρcrit window attribution
- Issue: You correctly compute that inserting γSU(2)=0.274 into the standard LQC formula yields ρcrit ≈ 0.27 ρPl, but you should emphasize again (briefly) that Ashtekar–Singh quote 0.41 ρPl for γ = 0.2375, and your 0.27 is an extrapolation across schemes.
- Required fix: Tighten the language to avoid implying that 0.27–0.41 ρPl is a published LQC range; it is a scheme-dependent extrapolation.

P1A-m3 (Sec. IV D, p. 10–11): Factor-of-2 in birefringence rotation
- Issue: The standard birefringence rotation convention is Δβ = (gφγ/2) Δφ in many conventions. Your Eq. (17) omits this 1/2 without clarifying conventions.
- Required fix: State your convention explicitly and adjust the normalization if needed. Recompute the numeric example if a factor-of-2 applies.

P1A-m4 (Sec. II A.1, p. 5): Notation Re(˚Γ), ∗RR
- Issue: The expression “Re(˚Γ) = 1/2 ε R = 1/2 ∗R R ≡ ∂μKμ” is not standard notation and risks confusing Re with “R wedge R-tilde.”
- Required fix: Use a standard Pontryagin density notation P ≡ (1/2) εαβμν Rαβρσ Rμν ρσ = ∂μKμ, and avoid overloading “Re.”

P1A-m5 (Sec. I, Abstract p. 1; Sec. XII B, p. 16): “Without fine-tuning” claim for ALP β
- Issue: The text says a spectator ALP with fa ∼ MPl, m ∼ H0 is “consistent ... without fine-tuning,” which is at odds with the earlier statement that mθ ∼ H0 is exactly the cosmological constant tuning (when simultaneously fitting ρΛ). This could mislead.
- Required fix: Clarify explicitly: “Matching β alone does not require fine-tuning; simultaneously matching β and ρΛ requires m ∼ H0, which is the cosmological constant tuning.”

P1A-m6 (Typos and names)
- Issue: Several author names have spurious spaces or diacritics (e.g., “Pop lawski,” “Domaga la,” “G¨odel” formatted inconsistently).
- Required fix: Correct to standard spellings: Popławski, Domagała, Gödel, etc.

NITs

P1A-n1 (Length)
- Issue: The manuscript is long (21 pages) relative to its core, largely conceptual contribution.
- Recommendation: After removing unpublished dependencies and consolidating the derivations, the paper can likely be reduced to ≲14 pages without loss of content.

P1A-n2 (Acknowledgment of AI use)
- Issue: The acknowledgment of an AI assistant is unusual but not prohibited. Consider moving to the end of Acknowledgments or omitting the tool’s brand name.

Arithmetic and consistency checks (spot-audited)
- ρcrit formula (Eq. 9): Using γ = 0.2375 gives ≈0.41 ρPl; γ = 0.274 gives ≈0.27 ρPl. Correct.
- One-loop ratio (Eq. 15) with consistent dimensions (if coefficient is 1/MPl): αem/4π ≈ 5.8×10−4, H0/MPl ≈ 10−61, (α/M) MPl ≈ 10−2, βobs ≈ 6×10−3 rad → ratio ~ O(10−60). Magnitude plausible but contingent on fixing P1A-E1.
- Route 4 ρθ example: With α/M = 10−21 GeV−1 = 10−30 eV−1, β = 6×10−3, mθ = 1.5×10−33 eV ⇒ ρθ ≈ 4.05×10−11 eV^4, comparable to (2.3 meV)^4 ≈ 2.8×10−11 eV^4. Numerically consistent (subject to factor-of-2 convention).
- β significance: 0.342°/0.094° ≈ 3.64σ; 0.215°/0.074° ≈ 2.91σ. Correct.
- LiteBIRD differential significance vs current central: |0.342−0.27|/√(0.03^2+0.094^2) ≈ 0.73σ. Correct.
- fNL ratio: 4.375/0.7 = 6.25σ. Correct as Fisher-ideal; subsequent degradations are qualitative.

Bibliography audit
- Several entries list years/arXiv IDs that appear speculative (e.g., [5], [41]–[45], [47]). PRD will not accept placeholders. Replace with extant references or remove.

Figures and tables
- Fig. 1: Qualitative flow diagram; fine as a schematic.
- Table I: Numbers attributed to “companion” must be either removed or replaced with public values. The footnote conflates different σ sources; add “not directly comparable” where needed.
- Table II: Barriers list is fine; explicitly mark B8 as subsumed by B14 (you do so).
- Table III: Remove the unpublished PTA row; rename γ to avoid collision.
- Table IV: Clarify Planck-mass convention and the source for each “Verified Value” (replace companion-paper dependence).

## Summary recommendation
REJECT

The manuscript contains multiple foundational methodological issues: a dimensionally inconsistent one-loop operator (and dependent amplitude estimates), an asserted but not demonstrated “all-orders” transparency theorem, heavy reliance on unpublished “companion” works for core claims, ambiguous inference of α/M from βobs, an unproven GW bound, and symbol collisions that create confusion. It also includes version-history language and numerous placeholder citations. While the high-level idea (channel-level closure within minimal ECH and the observation that Holst decouples for scalar perturbations) is potentially publishable, bringing this work to PRD standards would require substantial re-derivation, removal of unpublished dependencies, and a thorough rewrite. I therefore recommend rejection at this time. If the authors can address all ESSENTIAL and MAJOR items with a fully self-contained, dimensionally consistent manuscript and public citations, a new submission could be considered.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW ADDITIONAL FINDINGS AFTER SECOND-PASS AUDIT

P1A-E12 (Sec. I, Abstract; Sec. X B–D, p. 14–15): Holst term misidentified as Pontryagin; incorrect Eq. (23) and dualizations
- Issue: The manuscript repeatedly conflates the Holst term eI ∧ eJ ∧ FIJ (internal dual in Holst uses ∗ on Lorentz indices) with the spacetime Pontryagin density P ≡ 1/2 εαβμν Rαβρσ Rμν ρσ. Equation (23) asserts “Re(˚Γ) = 1/2 εμνρσ Rμνρσ(˚Γ) = 1/2 ∗R R ≡ ∂μKμ,” which is not correct: (i) εμνρσ Rμνρσ carries mass-dimension 2 and is not a topological invariant; (ii) Pontryagin requires the product of two curvature tensors R ∧ R˜; (iii) the Nieh–Yan identity relates e ∧ e ∧ R to T ∧ T − d(e ∧ T), not to Pontryagin. This misidentification undermines the central “Holst reduces to a boundary term” narrative as written.
- Required fix: Replace Eq. (23) with the correct identities and clearly distinguish: (a) Palatini term εIJKL eI ∧ eJ ∧ RKL; (b) Holst term eI ∧ eJ ∧ ∗RIJ; (c) Nieh–Yan density NY = d(eI ∧ TI) = TI ∧ TI − eI ∧ eJ ∧ RIJ; (d) Pontryagin P = R ∧ R˜. Then explicitly show that, for torsionless Levi-Civita connection, variation of the Holst term does not affect the equations of motion, without equating it to Pontryagin.

P1A-E13 (Sec. II C, Eq. 10; Sec. II A.2, Fig. 2; Appendix B): Λ vs ρ mixing and missing 8πG convention
- Issue: The text alternates between Λeff = Ξ MPl^2 + cω ω^2 and ρΛ = Ξ MPl^4, without stating the conversion convention (Λ = 8πG ρ or Λ = ρ/M̄Pl^2, etc.). Factors of 8π are never fixed, and it is unclear whether MPl or M̄Pl is used in these mappings.
- Required fix: State conventions at the start of Sec. II (natural units; whether MPl or M̄Pl is used, how ρPl and Λ relate), and propagate them consistently. Provide the explicit conversion between Λeff and ρΛ used in Fig. 2 and Appendix B; recompute any relations that depend on these mappings.

P1A-E14 (Sec. II A.2, Eqs. 5–6): Undefined curvature object FIJ[K, ˚R] and index/duality ambiguities
- Issue: Seff = (α/M) ∫ eI ∧ eJ ∧ FIJ[K, ˚R] and its component reduction (Eq. 6) are never defined beyond the bracket [K, ˚R]. It is unclear whether F is the internal-dualized Lorentz curvature, how contorsion K enters, and which dual (internal vs spacetime) is applied. The epsilon tensor in Eq. (6) is over spacetime indices while FIJ carries Lorentz indices; the contraction rules are not specified, and the parity properties are thus not auditable.
- Required fix: Precisely define FIJ[K, ˚R], the dualization convention, and the index contractions. Show the form of the 4-form whose integral is written in Eq. (6), with explicit wedge products and differential forms, and confirm its parity and mass dimension unambiguously.

P1A-M9 (Sec. II A.2, Step 1; Eq. 3 vs Eq. 4): Torsion source stated in EC form while Holst dependence appears later
- Issue: Step 1 states Tabc = 8πG Sabc (pure EC), but Step 2 immediately introduces a γ-dependent four-fermion coefficient ∝ γ^2/(1+γ^2) without showing how the Holst term modifies the Cartan equation. This is internally inconsistent as presented.
- Required fix: Either (i) keep Step 1 in pure EC and then add Holst in a transparent second step deriving the γ-dependent torsion solution, or (ii) present the coupled EC+Holst Cartan equation directly with γ-dependence and show how Eq. (13) follows.

P1A-M10 (Fig. 2 vs Appendix B; Sec. II A.2): Two incompatible-looking scalings for ρvac appear without crosswalk
- Issue: Fig. 2 shows ρvac ∼ [(α/M) MPl] MPl^4, while Appendix B uses ρΛ ∼ (α/M) MPl^5 ≃ 10−2 MPl^4. The text (p. 8) also references a “reconstruction between (α/M) MPl^3 and [(α/M) MPl] MPl^4.” Although these can be made mutually consistent under an on-shell ansatz, the manuscript uses them interchangeably without a single, explicit mapping.
- Required fix: Choose one canonical scaling and derive the others from it in an appendix (with a single equation showing the exact identity and assumptions). Use only one in figures and in the main text.

P1A-M11 (Sec. IX I, Barrier 9): “Liouville conservation” barrier asserted without derivation in the LQC/bounce context
- Issue: The claim that phase-space volume conservation prevents irreversible state selection across the bounce is made without citations or a demonstration that Liouville’s theorem applies through the quantum/gravity-modified bounce dynamics used here.
- Required fix: Provide a derivation or authoritative citation showing how Liouville’s theorem applies in the effective LQC/ECH setting across the bounce. Otherwise, downgrade Barrier 9 to a qualitative remark, not a quantitative or formal constraint.

P1A-M12 (Sec. IX C, Barrier 3): Unproven “torsion decouples from FRW at the bounce density” statement
- Issue: Barrier 3 asserts torsion “decouples from the FRW background precisely at the bounce density,” but no derivation is shown. This is distinct from (and not covered by) the perturbation-transparency claim.
- Required fix: Provide an explicit background-level derivation (or a citation) showing that torsion vanishes at the bounce density in the minimal ECH effective equations used, or soften the claim.

P1A-M13 (Sec. II C, Eq. 10): Undeclared normalization of cω and its bound
- Issue: The rotational contribution Λeff ⊃ cω ω^2 is introduced without defining cω (dimension, sign, origin). Without normalization, the constraint from (ω/H)0 < 5×10−11 cannot be propagated to Λeff.
- Required fix: Define cω and either compute or bound it (with references), or remove the rotational term from Eq. (10).

P1A-M14 (Sec. II A.3, p. 6): Critical black-hole mass Mcrit ≈ 10−3 M⊙ asserted without source/derivation
- Issue: The threshold mass is stated as fact but no reference or derivation is provided.
- Required fix: Add a published citation or supply a derivation; otherwise remove the claim.

P1A-m7 (Sec. II A.2, Eq. 4): Notation ambiguity in coefficient and species sum
- Issue: “3πGN/2” likely means 3π G_N/2. It is also unclear whether J5µ is summed over fermion species (and how Nf enters).
- Required fix: Fix the notation and state the species sum explicitly.

P1A-m8 (Sec. III A, Eq. 12): Units of β not stated
- Issue: The small-angle EB rotation formula requires β in radians.
- Required fix: State explicitly that β is in radians in Eq. (12).

P1A-m9 (Sec. X C–D, Eq. 21): Ambiguous H notation in conformal-time tensor equation
- Issue: The equation h''ij + 2H h'ij + k^2 hij = 0 appears to use H for a'/a (conformal Hubble), but H is elsewhere used for the physical Hubble. This risks dimensional confusion.
- Required fix: Use the standard script ℋ ≡ a'/a in conformal time, and reserve H for cosmic-time Hubble.

P1A-E16 (Sec. IV E, p. 11): Incorrect cross-reference for the “condensate mechanism” discussion
- Issue: The text says “The condensate mechanism … is documented in Sec. X as a quantitative closure,” but Sec. X is the perturbation-transparency section; it does not analyze a condensate route.
- Required fix: Correct the reference (likely to Sec. IV A or Sec. IX) or revise the sentence.

Explanation for why these were missed initially
The first-pass review focused heavily on the one-loop operator’s dimensional consistency, the “all-orders” transparency proof status, unpublished dependencies, and amplitude budgets. A deeper, second-pass scrutiny of the Holst/Pontryagin identities, Λ vs ρ conventions, and index/duality structure in Eqs. (5)–(6) surfaced additional foundational issues (P1A-E12, E13, E14) that materially affect the central claims. Several barriers (9 and 3) also lacked explicit derivations, which was not fully appreciated on the initial pass. Minor clarity and cross-reference problems (m7–m9, E16) further hinder reproducibility and precision.

These new findings are independent of those already listed and require resolution for the manuscript to meet PRD standards.