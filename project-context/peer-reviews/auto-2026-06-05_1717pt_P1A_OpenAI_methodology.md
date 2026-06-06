# P1A auto-2026-06-05_1717pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (9363 chars)
**Wall time**: 385.4s

---

Referee report on “Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter” (21 pages)

Scope of review
- Role per editor’s instruction: methodology rigor (derivations, dimensional analysis, internal arithmetic consistency, statistics, estimator declaration, error propagation).
- I read all 21 pages, tables, figure, equations, abstracts/conclusions, and bibliography as rendered.

Overall assessment
The manuscript makes broad, largely qualitative claims about “channel-level” closures of dark-energy routes in minimal Einstein–Cartan–Holst (ECH) gravity and states a “perturbation-transparency theorem.” However, many load‑bearing statements are not derived in the paper; critical numbers are taken from “companion” works that are in preparation and not publicly available; several key equations have dimensional or normalization inconsistencies; and the central claims rely on phenomenological ansätze acknowledged by the author as not controlled EFT derivations. For PRD standards, the paper is not yet methodologically rigorous or self‑contained.

Below I itemize findings with required fixes. I classify each as ESSENTIAL (must fix for PRD), MAJOR, MINOR, or NIT.

ESSENTIAL FINDINGS

P1A-E1 (Sec. I, p. 5; Sec. III B, p. 8; Sec. VI, p. 11; “Companion paper” block p. 5; Table I p. 4; Table IV p. 20)
Reliance on unpublished/in-preparation companion works for load-bearing results
- Offending text: “Companion paper—ΛCDM+ΔNeff MCMC verification… (Paper I(b) [6], in preparation)… values referenced… are documented internally… should be read as internal-analysis inputs…”; Table I and Table IV list posterior values; Sec. III B cites a galaxy-spin null from “Paper IV [23], in preparation”; Sec. VI: “NaMaster pipeline validation… in companion Paper I(b) [6].”
- Problem: PRD requires the manuscript to be self‑contained. Load‑bearing numerical claims (H0, ΔNeff, galaxy-spin null significance, ALP MCMC fits, pipeline validation) cannot rest on unpublished, inaccessible work. The GitHub link provided does not include the MCMC chains and diagnostics; those are said to be “in companion Paper I(b).”
- Required fix: Either (a) remove all results and claims that depend on [2], [6], [23], [46], [47], or (b) fully include in this paper the corresponding methods, data, chains, diagnostics, and results sufficient for independent reproduction, with public links to data and code archived and versioned, and move all “in preparation” content into this submission or cite published, peer‑reviewed sources.

P1A-E2 (Sec. II A.1, Eq. (1), p. 5)
Incorrect/gratuitous inclusion of torsion-squared term in the starting action
- Offending text: Eq. (1) includes “+ 1/4 Tabc Tabc” and states “is a shorthand for the four-fermion contact interaction obtained after integrating out the non-propagating torsion; it is not an independently specified kinetic term.”
- Problem: The Einstein–Cartan–Holst action does not contain an explicit TabcTabc term at the fundamental level; the four-fermion term arises only after integrating out the algebraic torsion from the Dirac + (Hilbert–Palatini + Holst) action. Including T^2 at the outset double‑counts and conflicts with the later torsion elimination. The coefficient (1/4) is also not justified and is not the standard coefficient arising from variation.
- Required fix: Start from the standard first-order EC(+Holst)+Dirac action without an ad hoc TabcTabc term, present the Cartan equation, then integrate out torsion to recover the induced four‑fermion operators with correct coefficients. Remove the 1/4 T^2 term and adjust subsequent derivations consistently.

P1A-E3 (Sec. II A.2 Eq. (4) p. 5 vs. Sec. IV A Eq. (13) p. 8)
Inconsistent four-fermion coefficients and γ‑dependence
- Offending texts: Eq. (4) gives Lint ∝ −(3πGN/2)·(γ^2/(γ^2+1)) J5·J5 (Holst‑extended), while Eq. (13) gives LNJLtor = −(3/16) κ (ψ̄γaγ5ψ)^2 and asserts “torsion-elimination map is independent of γ at the classical level.”
- Problem: These are contradictory statements. The Holst term does modify the relative weights of axial–axial vs. vector–axial contact terms and introduces γ‑dependence in the contact term coefficients in the minimally coupled Dirac case; see standard treatments (e.g., Freidel–Minic–Takeuchi 2005; Mercuri 2006/2009). The manuscript must reconcile the two expressions, justify the numerical coefficients and signs, and explain clearly in what limit γ‑dependence cancels (e.g., upon imposing the Nieh–Yan reconstruction with non‑minimal coupling) rather than asserting both.
- Required fix: Provide a single, consistent derivation of the induced four‑fermion terms from the chosen matter coupling (minimal or non‑minimal), track γ‑dependence, give explicit coefficients, and correct the closure arguments accordingly.

P1A-E4 (Sec. II C Eq. (10) p. 6 and throughout; Appendix B p. 19)
Λ vs ρΛ dimensional inconsistency and unclear conventions for MPl vs M̄Pl
- Offending text: “Λeff = Ξ M2Pl + cω ω2, Ξ ≡ ⟨(α/M) MPl⟩ Dinf”; elsewhere ρΛ = Ξ M4Pl; Eq. (B2) ρbounceΛ ∼ (α/M) M5Pl ∼ 10−2 M4Pl.
- Problem: Λ has mass dimension 2, while ρΛ has dimension 4; the paper switches between Λ and ρΛ with the same symbol Ξ without a consistent definition of whether MPl is the reduced or unreduced Planck mass. Eq. (B2) is dimensionally inconsistent unless conventions are stated and justified. This propagates into the Dinf → Ntot mapping and quoted e‑fold counts.
- Required fix: Declare units/conventions (ℏ=c=1), specify whether MPl is reduced (2.435×10^18 GeV) or unreduced (1.22×10^19 GeV) everywhere, define Λ and ρΛ distinctly, and repair all equations (10), (B1)–(B2) so that dimensions match off shell. Recompute Ntot with consistent conventions.

P1A-E5 (Sec. IV B Eq. (15), p. 9–10)
Ambiguous, non-reproducible one-loop birefringence amplitude estimate
- Offending text: Eq. (15) yields ∆θone-loop/∆θobs ~ 10−58–10−60; the text admits “an alternative ordering… yields ∼10−33.”
- Problem: A 25–27 order-of-magnitude ambiguity indicates the calculation is not fixed. The mapping from the postulated operator to an integrated rotation angle must be derived unambiguously, with proper normalization, choice of MPl vs M̄Pl, H0 to GeV conversion, and line‑of‑sight integral. As written, the estimate is not auditable.
- Required fix: Derive β from the stated effective action with explicit steps: write the modified Maxwell equations, obtain the dispersion relation or Stokes rotation equation, integrate over conformal time, and present a final expression with all constants and unit conversions shown, using a specified cosmology. Quote a single robust number with an uncertainty range reflecting only controlled approximations.

P1A-E6 (Sec. IV D Eq. (17), p. 10)
Rotation-angle normalization and ALP energy-density relation not derived
- Offending text: “β = (α/M) Δθrec→today ∼ (α/M) √(2ρθ/m2θ).”
- Problem: With L ⊃ −(1/4)(α/M) θ F F̃, the standard small-angle result is Δβ = (1/2)(α/M)Δθ (up to convention). The field excursion Δθ and its relation to ρθ depend on the mass regime (oscillatory vs. slow-roll). The factor-of‑2 and the use of ρθ = m2θ β2/[2(α/M)2] must be derived from the action; otherwise the overshoot argument is numerically under‑ or over‑stated.
- Required fix: Provide a first‑principles derivation of β(η) from the axion‑photon action (define the normalization of α/M relative to gφγ), derive Δθ between recombination and today for the mass regimes considered, and then derive ρθ(β, mθ, α/M) with correct factors. Recompute the “22–36 OOM” overshoot using the corrected normalization.

P1A-E7 (Sec. X, p. 14–15)
“Perturbation-transparency theorem” is only sketched, lacks variation and boundary analysis
- Offending text: Five-step outline; no explicit variation; no discussion of boundary terms/topology; no gauge-invariant perturbation expansion beyond asserting Pontryagin is a total derivative.
- Problem: For a central theorem, PRD requires a rigorous proof in the stated scope: spell out the action with Holst term on a torsion-free connection, vary to second (or all) order in metric perturbations for scalars and tensors, and show that the variation of the Pontryagin term vanishes under the assumed boundary conditions. Otherwise “theorem” is overstated.
- Required fix: Provide a full derivation: (i) show SHolst|T=0 reduces to the Chern–Pontryagin term; (ii) compute its metric variation δSHolst to second order around FRW and demonstrate it is a boundary term under the stated boundary conditions; (iii) present explicit scalar/tensor perturbation EOM confirming no γ‑dependent terms. If boundary/topological sectors are excluded, state precise conditions (compact spatial slices or falloff).

P1A-E8 (Throughout; p. 3–5, 8, 11–18; Refs [2],[6],[23],[46],[47])
Versioning/logbook language and internal report codes in body/bibliography
- Offending text: “hUBIFY-2026-001B,” “frozen accepted samples,” “this volume,” “companion work in preparation,” “companion technical note, available upon request from the author.”
- Problem: PRD style does not allow internal report codes and version-history/logbook language in the body. Reliance on “available upon request” is not acceptable.
- Required fix: Remove all such language and either (a) publish those results in this paper, or (b) cite peer‑reviewed publications. Otherwise excise claims that depend on them.

P1A-E9 (Appendix B Eq. (B1)–(B2), p. 19)
Mass-dimension counting not anchored to a declared convention
- Offending text: “[α/M] = −1, [εμνρσ eIμ eJν FIJρσ] = +2 ⇒ [Lodd] = +1.”
- Problem: The dimension of eIμ and FIJ depends on conventions; without declaring them, the counting is ambiguous. This underpins the central “dimension +1 not +4” claim and the on‑shell ansatz used to set Ntot.
- Required fix: State conventions explicitly (dimensions of eIμ, spin connection, and curvature two-form), then redo the counting and ensure consistency across Eqs. (5)–(6), (10), (B1)–(B2).

P1A-E10 (Sec. II A.2 Eq. (7), p. 6; Sec. IV B, p. 9–10)
Numerical claim [(α/M) MPl] ~ 10−2 lacks parameter choices and is inconsistent with later usage
- Offending text: “motivating the order of magnitude [(α/M) MPl] ∼ 10−2.”
- Problem: With M ≈ MPl/√γ and a one‑loop prefactor g^2/(32π^2) ln(Λ^2/μ^2), the value depends sensitively on g, the log, and γ. No parameters are specified, yet this number is repeatedly used (e.g., Eq. (15)). Using reduced vs unreduced MPl changes it by ~5×. This must be grounded.
- Required fix: Choose explicit values (g, Λ/μ, γ) or quote a range with justification; propagate uncertainties consistently into all amplitude estimates.

MAJOR FINDINGS

P1A-M1 (Sec. II C.1 “Reheating thermal-reset barrier,” p. 6–7)
Unquantified claim that reheating erases axial current faster than H
- Problem: The argument depends on C/P-violating scattering rates vs Hubble at Treh. No calculation or citation is provided; scaling of ⟨J5μ⟩ and its variance is asserted without kinetic theory support.
- Required fix: Provide an order-of-magnitude calculation of the axial charge equilibration rate at Treh with references, compare to H(Treh), and show how this feeds into torsion via the Cartan equation.

P1A-M2 (Sec. IX L, Eq. (20), p. 13)
“Vacuum amplification ceiling” ΩGW|bounce ≲ (ρcrit/ρPl)^2 presented without derivation
- Problem: It is unclear why the GW energy fraction scales as the square of the bounce critical‑density ratio; no derivation or reference is given.
- Required fix: Derive or cite a bound on ΩGW at the bounce and how it scales with ρcrit; clarify definition (total energy fraction vs. today’s spectral density) and show steps.

P1A-M3 (Sec. II A.3, p. 6)
Uncited “parent black hole mass must exceed Mcrit ≈ 10−3 M⊙”
- Problem: No source or derivation. This looks like a model-dependent claim; it cannot be asserted without justification.
- Required fix: Provide a derivation or remove.

P1A-M4 (Sec. III A, p. 7–8)
CMB EB formula given, but the paper lacks the photon–torsion (or gravity–induced) coupling that would connect ECH to β
- Problem: The paper concedes it does not derive the required coupling; yet it discusses EB expectation for ECH. This section must either become purely phenomenological (explicitly detached from ECH) or include a derivation from the stated action.
- Required fix: Either provide the explicit coupling derived from the gravitational sector and compute β, or clearly separate all CMB birefringence discussion as ALP‑only phenomenology not attributable to minimal ECH.

P1A-M5 (Sec. IX, pp. 12–14; Table II p. 13)
Barrier catalog items presented without derivations
- Problem: Many “barriers” (e.g., Topological-Shift Duality, Scalar–Tensor Universality, Parameter Immunity, Liouville Conservation) are asserted in prose without proofs or references. For PRD, such mechanism-class closures must be shown.
- Required fix: For each barrier that is used to close a route, provide a derivation or a precise citation where the result is proved, and explain applicability conditions. Otherwise, demote to conjectures and remove them from the closure argument.

P1A-M6 (Sec. XII A and Appendix B, pp. 15, 19)
Inconsistent Ntot figures (92 vs 94) from different bookkeeping; lack of a single, controlled mapping from Dinf to ρΛ
- Problem: The text oscillates between Ntot≈92 and ≈94 and acknowledges dependence on an ad hoc prefactor (Treh/MGUT)3/2. This is a central scalar in abstract/conclusions.
- Required fix: Choose a single, fully derived mapping (or remove the claim), use consistent Λ vs ρΛ conventions and a declared MPl, and give a single Ntot with uncertainty. If it is only a phenomenological reparameterization, reduce prominence accordingly.

P1A-M7 (Sec. II A.2 Eq. (5) and (6), p. 6)
Undefined F[K,R˚] and unclear operator content
- Problem: The symbol FIJ[K,R˚] is undefined; it is not clear what degrees of freedom enter and how. Without a definition, subsequent dimensional analysis is moot.
- Required fix: Define FIJ[K,R˚] precisely or eliminate the K notation and write the explicit curvature objects used.

P1A-M8 (Throughout)
Reduced vs unreduced Planck mass ambiguity
- Problem: Sometimes MPl=10^19 GeV is used (e.g., to get MPl·α/M~10−2), other places standard practice would use reduced M̄Pl=2.43×10^18 GeV. This leads to 4–5× inconsistencies in numeric estimates.
- Required fix: Declare and use one Planck mass consistently everywhere; recompute all affected numbers.

MINOR FINDINGS

P1A-m1 (Acknowledgments, p. 18)
Acknowledgment of AI assistant “Claude” for research assistance
- Comment: This is nonstandard in PRD. If retained, clarify that all scientific content is the author’s responsibility and that no proprietary tools were used to generate or verify proofs.
- Recommended fix: Remove or condense to a standard acknowledgment per journal policy.

P1A-m2 (Notation and typos, various pages)
- “R∧Re,” “RRe,” “Pontryagin density ∝ RRe” used inconsistently; write as R∧R̃ or εμνρσRμνab Rρσab with consistent normalization.
- “Pop lawski” appears with an internal space; standard is “Popławski” or “Poplawski” consistently.
- Fix these minor typos for clarity.

P1A-m3 (Units/axes for Fig. 2, p. 5)
- The figure caption does not state units on the vertical axis (hierarchy depiction). If a schematic, label as “schematic (not to scale)” or add quantitative scales.

P1A-m4 (Table footnotes, p. 4 and p. 16)
- Footnotes in Table I and Table III include unpublished chain status and computational details inappropriate for a final paper. Either move to methods appendix or remove.

P1A-m5 (Bibliography formatting, pp. 19–21)
- Several entries are “in preparation” with internal report numbers. PRD discourages such citations if they are load‑bearing. Where possible, replace with arXiv/preprints; otherwise, remove claims predicated on them.

NIT FINDINGS

P1A-n1 (PACS numbers, p. 1)
- PACS is deprecated. PRD no longer requires PACS; remove unless requested by editors.

P1A-n2 (Repeated phrasing, multiple pages)
- The phrase “B8 is subsumed by B14” appears multiple times; consolidate once where the catalog is introduced.

Audit of scalars in abstract and conclusions
- “ρcrit ≃ 0.27–0.41 ρPl” — consistent with Eq. (9) given γ=0.274 and γ=0.2375; OK.
- “Ntot ≈ 92” — inconsistent with Appendix B’s ≈94; must be unified (see E4/M6).
- “fNL = −35/8” — standard matter-bounce value; acceptable as external citation.
- “βobs = 0.342° ± 0.094° (~3.6σ from 0)” — 0.342/0.094 = 3.64; OK.
- “ACT DR6 0.215° ± 0.074° (~2.9σ)” — 0.215/0.074 ≈ 2.9; OK.
- “ΩECHGW|bounce ≲ 0.07–0.17” — matches (ρcrit/ρPl)^2 if ρcrit/ρPl in [0.27,0.41]; but the underlying formula lacks derivation (see M2).
- “[(α/M) MPl] ~ 10−2” — not justified numerically (see E10).

Statistical claims and estimator declarations
- EB estimator formula CℓEB ≈ 2β(CEE−CBB) is standard for a uniform β; fine as a background equation.
- No primary estimator is declared for the galaxy-spin measurement (which is deferred to a companion paper). Since the spin result is load‑bearing in the narrative, this is not acceptable (see E1).
- Multiple σ-values from different analyses (Planck+WMAP vs ACT) are presented; the manuscript does note independence qualitatively. The LiteBIRD 9σ “detection” is immediately qualified as against zero, not as model discrimination; acceptable.
- MCMC sample size statements (309,189 accepted samples) are not documented in this paper; no R̂ values shown; no priors listed beyond Table IV stubs. Remove or include full MCMC details (see E1).

Derivation chains and dimensional analysis
- The core “dimension +1 rather than +4” point rests on undeclared conventions (E9).
- The ALP birefringence normalization is not derived (E6).
- The one-loop parity-odd effective action (Eq. 14) is posited but not derived; the coefficient structure is asserted to be “natural EFT operator” without a derivation or a precise source (E5).

Length relative to contribution
- At 21 pages, the manuscript is long for what is, at present, a largely qualitative argument with many results deferred to companion works. If resubmitted as a self-contained, rigorous work, length can be justified by full derivations; otherwise, reduce to ≤12–14 pages focusing on rigorously proved statements and remove companion-dependent content.

## Summary recommendation
REJECT

The manuscript in its present form does not meet PRD methodological standards. It relies heavily on unpublished companion works for key numerical and methodological claims, contains internal inconsistencies in the action and four‑fermion sector, mixes Λ and ρΛ dimensions, leaves the central “perturbation-transparency theorem” only sketched rather than proved, and presents ambiguous, non‑reproducible amplitude estimates. A substantially revised, self‑contained submission addressing all ESSENTIAL and MAJOR items, with rigorous derivations and removal (or full inclusion) of companion‑paper dependencies, could be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS AFTER SECOND-PASS (fresh-eyes) AUDIT

ESSENTIAL FINDINGS

P1A-E11 (Abstract; Sec. X A–D, esp. “Explicit Verification,” Eq. (23))
Holst ≠ Pontryagin on torsion-free backgrounds; internal vs spacetime duals conflated
- Offending text: “the Holst dual contraction εμνρσRμνρσ reduces on the Levi-Civita connection to the Pontryagin density ∝ R R̃…and therefore contributes only a boundary term…”
- Problem: The Holst density is e^a∧e^b∧R_ab (internal dual in the usual form (1/γ) e∧e∧*R), not the spacetime Pontryagin density R∧R̃ ≡ (1/2)εμνρσRμνab Rρσab. On a torsion-free connection, the Nieh–Yan 4-form identity gives T^a∧T_a − e^a∧e^b∧R_ab = d(e^a∧T_a); setting T=0 implies e^a∧e^b∧R_ab = 0, not “Pontryagin.” The classical irrelevance of the Holst term follows because it does not affect the torsion-free Einstein equations (its variation vanishes on shell), not because it reduces to R∧R̃. The manuscript’s argument is thus conceptually wrong even if the conclusion (no effect on EOM for torsionless scalar matter) is standard.
- Required fix: Correct the identity and provide a rigorous variation: (i) derive SHolst = (1/γ)∫e∧e∧R_ab and show it vanishes for T=0 (or, equivalently, contributes no terms to the torsionless EOM), (ii) separate clearly the Pontryagin density R∧R̃ (Jackiw–Pi) from the Holst term, and (iii) remove the erroneous “Holst→Pontryagin” claim.

P1A-E12 (Sec. II A.2 Eq. (7), p. 6; Sec. IV B, p. 9–10)
Inconsistent coupling choice in one-loop estimates (g^2 vs αem)
- Offending text: Eq. (7) uses a generic g^2/(32π^2) log; Sec. IV B frames the coefficient as O(αem/4π). 
- Problem: The one-loop operator and its coefficient depend on the specific field content and loop (gravitational vs gauge vs chiral anomaly). Mixing a generic g with αem blurs which diagram is being estimated and prevents reproducibility. The number [(α/M)MPl]~10−2 is repeatedly used downstream without a consistent coupling choice.
- Required fix: Specify the actual loop (matter/graviton/EM), fix the coupling constant accordingly, and propagate a single, consistent coefficient (with uncertainties) through all amplitude estimates.

P1A-E13 (Sec. II C.1 “Inflationary Suppression,” p. 6–7)
Unjustified Dinf ∝ e−3Ntot scaling for the quantity that sources Λ
- Offending text: “The contorsion dilutes as a−3 during inflation… Dinf = e−3Ntot × (Treh/MGUT)3/2,” justified by “the cube of the fermion bilinear…”
- Problem: Torsion in EC is algebraically proportional to the axial current (a bilinear scaling ∝ nψ), and the induced four-fermion energy density scales ∝ n^2 (i.e., a−6). The manuscript asserts an a−3 scaling for the effective quantity that later maps to Λ without deriving what object is being diluted. The “cube of the fermion bilinear” phrase is physically opaque and dimensionally incongruent for the stated mechanism.
- Required fix: Derive from first principles which operator contributes to Λeff and its scale-factor dependence between bounce and reheating. If the relevant energy density is NJL-like, show a−6; if a different effective operator is used, derive its scaling explicitly. Recompute Dinf and the implied Ntot accordingly.

P1A-E14 (Sec. IV B Eq. (14), p. 9)
Undefined “Nieh–Yan pseudoscalar θ(x)” treated as a dynamical field
- Offending text: Γone-loop ⊃ −(1/16π^2) β(γ)/MPl ∫√−g ∂μθ J5μ with θ labeled “Nieh–Yan pseudoscalar.”
- Problem: The Nieh–Yan density is a topological 4-form, not a propagating scalar field. Introducing ∂μθ J5μ presumes θ is a bona fide field (e.g., a dynamical Immirzi axion), which is neither defined nor derived here. As written, Eq. (14) lacks a well-defined dynamical origin for θ.
- Required fix: Either (a) explicitly introduce and normalize a dynamical pseudoscalar field (e.g., BI-axion) with an action and justify the operator, or (b) refrain from using θ(x) in a way that implies dynamics. In either case, provide or cite a derivation of the operator and its coefficient.

P1A-E15 (Abstract vs Sec. IV D)
Abstract misstates that all four channels are closed at the amplitude level
- Offending text: Abstract: “find that each fails at the amplitude level”; body: Sec. IV D states Route 4 closes by “naturalness objection rather than amplitude no-go.”
- Problem: This is a direct inconsistency between abstract and body.
- Required fix: Make the abstract faithful to the body: state explicitly that R4 is not amplitude-excluded but fails on naturalness/explanatory grounds under the paper’s assumptions.

P1A-E16 (Sec. II A.2 Eq. (7) with M = Marea-gap ≈ MPl/√γ; multiple uses downstream)
Numerical inconsistency in [(α/M)MPl] ~ 10−2 given stated M
- Offending text: Repeated claim [(α/M)MPl] ~ 10−2 anchored to Eq. (7) with M ≈ MPl/√γ.
- Problem: With MPl/M ≈ √γ ≈ 0.52 (γ=0.274), and a one-loop factor g^2/(32π^2) ~ 10−3 for g~O(1), the product [(α/M)MPl] ~ O(10−4)×ln(Λ/μ). Bringing this to 10−2 requires an unrealistically large log (∼25–50) and/or g≫1. The paper neither specifies these choices nor propagates uncertainties.
- Required fix: Provide explicit parameter choices (g, log, γ) and recompute. If the plausible range is 10−4–10−3, update all amplitude budgets that used 10−2.

MAJOR FINDINGS

P1A-M9 (Sec. IX A, Eq. (18))
Undefined symbol and unmotivated relation in “Mass-Coupling Lock”
- Offending text: geff ∼ 1/(MPl√|t3|) ∼ H0/MPl.
- Problem: t3 is undefined; the identification of geff with H0/MPl is asserted without derivation. As written, the barrier relies on an unintroduced parameter.
- Required fix: Define t3 and derive geff from a specific propagating-torsion Lagrangian, or remove the formula.

P1A-M10 (Sec. II C.2, p. 7; Sec. III B, p. 8)
“>100 OOM underprediction” of galaxy-spin asymmetry asserted without calculation
- Problem: No derivation links the stated parity-odd operator with a predicted spin-dipole amplitude to justify the “>100 orders” figure. This claim is central to dismissing the spin channel.
- Required fix: Provide the chain from the operator to a predicted A0 (or dipole) with all normalizations, or soften/remove the quantitative “>100 OOM” statement.

P1A-M11 (Citations throughout to 2025–2026 works; examples: Ref. [5] arXiv:2509.13654; [46], [47])
Unverifiable citations and placeholders
- Problem: Several references point to future-dated arXiv IDs or in-prep internal notes. PRD requires citable, accessible sources for load-bearing claims.
- Required fix: Replace with existing arXiv/preprints or published papers; otherwise remove dependent claims.

P1A-M12 (Sec. X D “Explicit Verification,” p. 14)
Section title misleads; no explicit perturbative calculation is presented
- Problem: The subsection title promises an explicit perturbative verification, but only restates that Pontryagin is a total derivative (itself misassigned; see E11). No scalar/tensor quadratic action or variation is shown.
- Required fix: Either show the promised expansions/variations or retitle and remove claims that an explicit check was performed.

MINOR FINDINGS

P1A-m6 (Sec. IV B Eq. (14))
β(γ) introduced without definition or range
- Problem: The β-function of γ is invoked but not defined or referenced; its magnitude drives the amplitude budget.
- Recommended fix: Define β(γ), cite a computation, and adopt a value/range in estimates.

P1A-m7 (Sec. II A.2 Eq. (7))
δNY introduced but never defined
- Problem: The counterterm/finite part labeled δNY is unexplained.
- Recommended fix: Define δNY, its scheme dependence, and expected size.

P1A-m8 (Sec. IV D Eq. (17))
Chern–Simons normalization and “by parts” equivalence missing factors
- Problem: The equivalence between (α/M)θ F F̃ and (α/M)∂μθ Kμ usually carries a 1/2 factor depending on conventions. The manuscript mixes both forms without fixing normalization.
- Recommended fix: Declare a single convention and track the factor throughout β and ρθ relations.

P1A-m9 (Sec. X C, Eq. (21))
Notation: primes and H not defined
- Problem: h″+2Hh′+k^2h=0 uses primes and H; the time variable (η vs t) and Hubble definition are not stated.
- Recommended fix: Define prime ≡ d/dη and H ≡ a′/a.

P1A-m10 (Fig. 2 caption vs body, p. 5)
Caption calls the plot “illustrating the phenomenological scaling,” but body text occasionally treats it as quantitative
- Recommended fix: Mark the figure as schematic and not to scale; ensure body statements do not ascribe quantitative content to it.

NIT FINDINGS

P1A-n3 (Terminology)
“Holst dual” and “dual contraction” used ambiguously
- Problem: Ambiguous language contributes to the Holst/Pontryagin confusion.
- Recommended fix: Reserve “dual” for internal Hodge in Holst and “spacetime dual” for Pontryagin; write them explicitly.

P1A-n4 (Consistency)
“ε-correction perturbative-order scaling alone” phrase is unclear; consider rephrasing for readability.

Explanation
This second-pass focused on deep structural consistency checks that frequently slip first reviews. The main new issues are (i) a fundamental conflation of the Holst term with the spacetime Pontryagin density (E11), (ii) an internally inconsistent and likely overstated one-loop normalization (E12, E16), and (iii) an unproven scaling Dinf ∝ a−3 attached to a quantity later mapped to Λ (E13). Together with undefined constructs (E14; M9) and a non-faithful abstract (E15), these undermine central claims independently of the companion-paper dependencies flagged earlier.