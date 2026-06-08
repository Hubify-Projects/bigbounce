# P1A auto-2026-06-08_1632pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (8083 chars)
**Wall time**: 445.6s

---

Referee report for: “Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter”

Overall assessment
The paper advances a channel-level “no-go” program for dark-energy generation within minimal Einstein–Cartan–Holst (ECH) gravity and presents a “perturbation-transparency” statement for canonical scalar matter. While the topic is timely and the structural perspective is potentially valuable, the manuscript in its present form does not meet Physical Review D standards for methodological rigor and completeness.

The submission repeatedly relies on unpublished “companion” papers for essential numerical results, derivations, pipelines, and even basic data summaries; it contains version-history/disclaimer prose inappropriate for a journal article; several key equations introduce undefined symbols or dimensionally ambiguous forms; and multiple central claims are asserted as barriers without formal derivations or citations. The perturbation-transparency statement, although plausible, is not presented with sufficient rigor for an “all-orders” theorem. Numerous load-bearing scalars and significances are reported without traceable, self-contained methods.

Below I enumerate specific issues classified by severity.

ESSENTIAL issues (paper cannot be accepted without these)
P1A-E1 (Abstract; p.1, and throughout: Sec. I, III, V, VI, XIII, XIV; Tables I/III)
Problem: Heavy reliance on unpublished “companion” papers for key inputs (MCMC posteriors, NaMaster validation, galaxy-spin catalog, SPHEREx Fisher forecast, PTA spectral index, ALP fits). Examples:
- “Companion work in preparation [6]” provides H0, ΔNeff, σ8, MCMC chain sizes; “Paper II [2]” contains the actual SPHEREx fNL forecast; “Paper IV [23]” contains the galaxy-spin null; “Paper III [46]” contains the PTA γ result; [47] is an “available upon request” technical note.
Required fix: Either (a) include all necessary methods, data selections, estimators, diagnostics, and numerical results in this paper in a self-contained way, or (b) restrict the manuscript to claims that do not depend on unpublished results (remove those claims entirely), or (c) defer submission until the companion papers are publicly available and citable, and then quote only what is demonstrably needed with exact, verifiable numbers and uncertainties.

P1A-E2 (p.2 footnote; p.15 footnote 2; Appendix B)
Problem: Version-history language inside the scientific narrative, e.g., “Earlier versions of this manuscript erroneously identified the two...” and “the migration is documented in Paper III § 6” and “the ∼ 35 misstated in earlier drafts.”
Required fix: Remove all version-history and draft-log language. Replace with a neutral, final-form presentation. If a correction to prior literature is being made, cite the prior publication and state the correction succinctly and formally.

P1A-E3 (Eq. (4), p.6; Eq. (7), p.6; Eq. (18), p.12)
Problem: Undefined symbols and coefficients in load-bearing equations.
- Eq. (4) Lint includes “GN” and a prefactor with γ^2/(γ^2+1), but “N” is not defined (is it number of species?). The coefficient is not derived or referenced precisely.
- Eq. (7) uses “g” (coupling) and “δNY,” but neither is defined; dimensional analysis is implied but not shown.
- Eq. (18) introduces “t3” in geff ∼ 1/(MPl sqrt|t3|) with no definition or units; the step to H0/MPl ∼ 10−61 is not derived.
Required fix: Define all symbols at first use and provide a precise derivation or an explicit literature reference for each coefficient. For Eq. (18), define t3 and show the steps leading to geff ∼ H0/MPl (or remove the claim if no rigorous derivation is available).

P1A-E4 (Eq. (6), p.6)
Problem: Component expression for the parity-odd operator mixes densities and tensors in a way that is likely not tensorially consistent: “∫ d^4x sqrt(-g) (α/M) εμνρσ eIμ eJν FIJρσ.” Using both sqrt(-g) and the coordinate εμνρσ (not the tensor density) alongside tetrads is nonstandard; dimensional/tensor-density status is unclear.
Required fix: Present the component expression carefully:
- Either (i) remain in differential-form notation, which is unambiguous, or
- (ii) write the tensorial form in components using the Levi-Civita tensor Eμνρσ = √−g εμνρσ and clarify index positions and contractions so the Lagrangian density has mass-dimension +4 and is coordinate-invariant.
Explicitly confirm the mass dimensions of all building blocks and the coupling.

P1A-E5 (Inconsistent use of Λ vs ρΛ; Eq. (10), p.6 vs text elsewhere)
Problem: The manuscript alternates between Λeff = Ξ MPl^2 + cω ω^2 (dimension two) and ρΛ = Ξ MPl^4 (dimension four). The mapping Ξ ≡ ⟨(α/M) MPl⟩ Dinf is used in both contexts without clarifying whether Ξ multiplies Λ or ρ, leading to dimensionally ambiguous claims.
Required fix: Choose one convention and stick to it throughout. If discussing energy density ρΛ, write ρΛ = Ξ MPl^4; if discussing Λ itself, write Λ = 8πG ρΛ = (Ξ MPl^2). State explicitly in Sec. II C which object is being parameterized and enforce dimensional consistency everywhere (including Tables and the abstract).

P1A-E6 (Table III footnote; p.16)
Problem: Live status of an MCMC chain, run details (“MPI pod... OMP threads... R̂−1≈3×10−2...”), and promises of future convergence are inappropriate for a published article and not relevant to this paper’s claimed results.
Required fix: Remove the entire footnote and any discussion of running chains. Only include fully converged, published results that are actually used in this paper. If the DESI w0wa analysis is not completed here, do not reference it beyond a brief forward-looking sentence.

P1A-E7 (Barrier 12; Eq. (20), p.13–14)
Problem: ΩGW^ECH|bounce ≲ (ρcrit/ρPl)^2 ≃ 0.07–0.17 is asserted as a “global energy-density-fraction ceiling” without derivation. Squaring the critical-density ratio is not justified; dimensions and the physical meaning are unclear.
Required fix: Provide a derivation (starting from a concrete GW energy-density production mechanism and budget) or remove Eq. (20) entirely. If it is only a heuristic scaling, label it explicitly as such and do not use it as a quantitative constraint.

P1A-E8 (Sec. IV.B, Eq. (14) and Eq. (15), p.9–10)
Problem: A one-loop parity-odd operator is posited with a specific structure and coefficient. While the author acknowledges it is an ansatz, the subsequent amplitude ratio relies on it. The dimensional bookkeeping in Eq. (15) is ad hoc and mixes a dimensionful rotation rate proxy with a dimensionless angle without a full path from the effective action to an observable rotation.
Required fix: Either (a) provide a complete derivation of the birefringence angle from the stated operator, including normalization, units, and assumptions; or (b) clearly label the ratio as an order-of-magnitude upper bound with defined assumptions, and propagate realistic uncertainties (e.g., αem/(4π), choice of ∂μθ, redshift integration) to the final suppression factor. Ensure dimensionless ratios are constructed transparently.

P1A-E9 (Sec. X, “all orders” perturbation-transparency claim; p.14–15)
Problem: The theorem is asserted to hold “at all perturbation orders,” but the proof is largely a one-line identity. The step “Holst term vanishes by Bianchi: 1/2 εμνρσ Rμνρσ(Γ̊) = 0” is plausible for torsion-free connections, but a complete all-orders, cosmological-perturbation proof (including lapse/shift sector and gauge fixing) is not provided. The statement that it decouples from the cubic action and the bispectrum requires more than the identity.
Required fix: Provide a rigorous derivation (or citation) that, when expanding the full action for scalar/tensor perturbations about FRW with T=0 and canonical scalar matter, the Holst contribution vanishes identically at quadratic and cubic order. Show the steps or reference a peer-reviewed derivation. Explicitly state which assumptions (boundary conditions, topology, regularity) are required. If only the background-level and linear identity are proven here, soften “all orders” to what is actually shown and remove bispectrum-level claims unless explicitly derived.

P1A-E10 (Sec. V, p.11; Sec. III.B, p.8)
Problem: Galaxy-spin results are presented as a “confirmed null” and leveraged to support claims, but all details (catalog construction, classifier performance, biases, significance) are deferred to Paper IV [23] (unpublished).
Required fix: Either include the essential methodology and results (sample definition, classifier architecture, calibration, null tests, error model, dipole estimator, sky masks, robustness checks) in this paper, or remove all galaxy-spin claims and their implications.

P1A-E11 (Multiple locations; Abstract p.1; Sec. I p.3; Sec. XIII p.17; Tables I/III)
Problem: Reported significances and forecasts are presented side-by-side from different procedures without explicit “not directly comparable” warnings at the point of juxtaposition. Example: “LiteBIRD will detect β at ∼9σ” vs “differential against the prior central value” 0.73σ; “3–5σ realistic” SPHEREx forecast vs “σ(fNL)≈0.7 Fisher-ideal ⇒ 6.25σ raw.”
Required fix: Each time two sigma values from incommensurate null hypotheses or error budgets are presented together, state explicitly that they are not directly comparable and explain the basis for each. For SPHEREx, confine the paper to quoting published, externally citable Fisher numbers unless you present your own forecast with a declared estimator and full systematics budget.

P1A-E12 (Sec. I.B, p.5; Sec. II.A.1, Eq. (1), p.5–6)
Problem: The gravitational action (1) includes “+ 1/4 Tabc Tabc” with a comment that it is shorthand for the four-fermion contact after integrating out torsion. That term is not part of the classical first-order EC–Holst action and its inclusion inside S before integration is conceptually misleading.
Required fix: Remove the Tabc Tabc term from the fundamental action. Instead, present the standard EC–Holst action, then integrate out torsion to obtain the four-fermion contact in the effective matter action, with a correct coefficient and clear parity properties (and references).

P1A-E13 (Sec. IX, multiple “barriers,” p.12–14)
Problem: Several “barriers” (e.g., Liouville conservation; UV→IR specificity; attractor-sensitivity dilemma; parameter immunity) are asserted as general theorems without derivations or citations. These read as rhetorical rather than methodological results.
Required fix: For each barrier that is essential to the closure claim, either provide a formal derivation/proof (with equations and assumptions) or supply peer-reviewed citations to an established theorem. Otherwise, move them to a Discussion subsection as qualitative observations and remove them from the numbered “constraints” list.

MAJOR issues (significant revision required)
P1A-M1 (Sec. II.A.2 “Derivation of the Parity-Odd Term,” p.6–7)
Problem: The multi-step “derivation” culminates in an operator with the wrong off-shell mass dimension (+1) and then adopts an on-shell scaling ansatz at the bounce to fix dimensions. While the manuscript admits this, subsequent sections still use the ansatz to motivate quantitative statements (e.g., Ntot≈92).
Required fix: Prominently flag, at every place where the on-shell scaling is used to produce numbers (e.g., Ntot), that this is not an EFT derivation. Provide a clear separation between formal results and heuristic parameterizations. If the main no-go does not depend on the ansatz, remove all numerical inferences (Ntot, etc.) that derive from it.

P1A-M2 (Sec. II.C Eq. (10), p.6–7)
Problem: The rotation term cω ω^2 is introduced without specifying cω or how ω is defined (vorticity of what congruence? units? observational bound translation). The later claim that “rotation is negligible” uses (ω/H)0 < 5×10−11 but does not connect it to cω ω^2 quantitatively.
Required fix: Define ω and cω precisely and propagate the observational bound to a quantitative constraint on Λeff in Eq. (10), or remove the ω-term.

P1A-M3 (Sec. IV.A, p.9)
Problem: The coefficient and parity classification of the Hehl–Datta term require care. The equation given for LNJLtor lacks a reference to the exact coefficient and omits the dependence on non-minimal couplings that control the γ dependence when the Holst term is present.
Required fix: Quote a standard reference for the precise four-fermion operator (and its parity properties) in EC–Holst with minimal coupling and, if relevant, with non-minimal axial couplings. State clearly whether the γ dependence survives after integrating out torsion (classically it drops out under minimal coupling).

P1A-M4 (Fig. 2, p.5; Appendix B, p.19–20)
Problem: The “energy density hierarchy” figure and the Appendix B dimensional discussion are inconsistent with the insistence on operator-level rigor. The figure labels and arrows suggest a derivational path that the text explicitly disclaims.
Required fix: Either rewrite Fig. 2 to depict only dimensionally consistent, on-shell scaling narratives clearly marked as “ansatz,” or remove the figure. In Appendix B, confine to a rigorous dimensional check and remove narrative that could be interpreted as a derivation.

P1A-M5 (Sec. III.A, p.8)
Problem: The EB relation CℓEB ≈ 2β (CEEℓ − CBBℓ) is given without specifying conventions (signs, small-angle limit, units). The paper also transitions to a claim of “qualitative consistency” with β≈0.27° though no ECH photon coupling is derived.
Required fix: Add a one-paragraph primer stating the rotation conventions and approximations (small β, uniform rotation), and remove any implication that ECH predicts β unless a concrete photon-torsion or ALP–photon coupling is derived within ECH.

P1A-M6 (Sec. X.D/E, p.14–15)
Problem: The claim “the cubic action for ζ receives zero contribution from the Holst term” is asserted without showing the cubic action. The “What would break transparency” list is helpful but should be tied to explicit terms in an action.
Required fix: Provide at least the schematic cubic action for ζ and indicate where the Holst contribution would enter and why it vanishes. Cite a standard cosmological perturbation reference to anchor notation and steps.

MINOR issues (address but paper can proceed after major/essential fixes)
P1A-m1 (Sec. II.B, p.6; Eq. (9))
Check: ρcrit/ρPl numbers for γ=0.274 and γ=0.2375 are correct (≈0.27 and ≈0.41). Please add a brief sentence clarifying that this follows from Δ = 4√3 π γ ℓP^2 and ℓP^2=G (ℏ=c=1 units), for traceability.

P1A-m2 (Sec. IV.D, p.10–11)
Check: ρ inversion from β with α/M = 10−21 GeV−1 and mθ = H0 yields ρθ ≈ few ×10−11 eV^4; the reported 2.8×10−11 eV^4 is within a factor ~1.5 of a back-of-the-envelope recomputation. Please show the one-line numeric to avoid confusion (state explicitly the H0 value used).

P1A-m3 (Tables I/III, p.4 and p.16)
Problem: The phrase “3–5σ realistic” is used; Table I footnote also mentions “3–5σ realistic after full systematic budget” while referencing σ(fNL)≈0.7 (which by itself would imply ~6.25σ for |fNL|=4.375).
Required fix: Harmonize the language across text and tables: state clearly “Fisher-ideal σ(fNL)≈0.7 (⇒ 6.25σ raw); including GR projection, bϕ uncertainty, and photo-z marginalization degrades to σ(fNL)≈1.0 (⇒ 4.4σ).” Provide a citation or a calculation to justify the degradation.

P1A-m4 (Sec. II.A.1, p.5–6)
Problem: γ values and counting-scheme discussion are correct but please cite exact equations or pages from [16–18] to make it easy for readers to verify 0.127, 0.274, 0.2375.

P1A-m5 (Sec. II.C.1, “Reheating thermal-reset barrier,” p.7)
Problem: The thermal washout argument is qualitatively correct but mixes expectation values and r.m.s. residuals with no quantitative rate estimates.
Required fix: Add a sentence with a reference for axial-current equilibration timescales at T≈Treh compared with Hubble expansion (e.g., standard model scattering rates) to justify the “rapidly washed out” assertion.

NITs (cosmetic)
P1A-n1 (Formatting; throughout)
Replace “programme”/“program” inconsistencies with a single US style per PRD style guide, and remove footnote markers like “a.” in running text that appear to be remnants of drafting.

P1A-n2 (PACS numbers; p.1)
PACS numbers are deprecated; remove per PRD style.

P1A-n3 (Acknowledgments; p.19)
The “use of Claude (Anthropic)” sentence is unusual for PRD and unnecessary; consider removing or softening to “We used AI-assisted tools for manuscript preparation; all scientific content was verified by the author.”

P1A-n4 (Typographic)
Ensure consistent use of ε vs ϵ and F̃μνFμν notation; currently typesetting alternates.

Length and focus
The manuscript is long (21 pages) relative to the core contribution actually demonstrated here (the torsion-free Bianchi identity implication for the Holst term; the four route-level amplitude arguments). With the removal of unpublished-companion dependencies, live-chain footnotes, and speculative barrier prose, the paper could be tightened to 12–15 pages focusing on:
- A rigorous, self-contained perturbation-transparency theorem and proof (background, quadratic, cubic orders).
- Clean, dimensionally consistent closures of R1–R4 with explicit coefficients and references.
- A brief, clearly labeled discussion of the phenomenological on-shell scaling ansatz and why it cannot solve the CC problem.

## Summary recommendation
REJECT

The manuscript in its current form relies on multiple unpublished “companion” works for essential inputs, contains version-history text, employs undefined symbols and dimensionally ambiguous expressions in key equations, and asserts several “barriers” without formal proof or citations. The central “all-orders” perturbation-transparency claim is plausible but not demonstrated with sufficient rigor for PRD. Substantial restructuring is required: remove or replace all unpublished dependencies, supply rigorous derivations (or citations) for the main claims, enforce dimensional and notational consistency, and confine the narrative to results actually proven in this paper. I encourage the author to prepare a focused, self-contained submission centered on a rigorous perturbation-transparency theorem and carefully supported route closures.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS AFTER SECOND-PASS AUDIT (A–J checklist applied)

P1A-E14 (Dimensional reconstruction inconsistency; Fig. 2, Sec. IV “Three technical aspects…”, Appendix B)
Problem: The manuscript alternates among three mutually inconsistent dimensional “reconstructions” for mapping the off-shell +1 operator to a vacuum energy:
- Fig. 2 and Appendix B Eq. (B2): ρΛ ∼ [(α/M) MPl] MPl^4 ≡ (α/M) MPl^5.
- Sec. IV (three-technical-aspects paragraph): references “(α/M) MPl^3 (dimension +2) and the equivalent rewriting [(α/M) MPl] MPl^4 (dimension +4).”
The two forms are not “equivalent reconstructions”: (α/M) MPl^3 has mass-dimension +2, whereas (α/M) MPl^5 has +4. This is not a change of presentation; it inserts two extra powers of MPl by fiat. Because Ntot estimates and several order-of-magnitude narratives lean on this mapping, the paper must settle on a single, explicit scaling (or remove derived numbers like Ntot≈92 that rely on it).

P1A-E15 (Dimensional inconsistency in “thermal-reset” r.m.s. scaling; Sec. II.C.1, “Reheating thermal-reset barrier”)
Problem: The text states that the post-reheating coherent mean of the axial current is washed out and that the r.m.s. residual “scales as ∼ √nψ / T1/2
reh.” The axial current density J5 has mass-dimension 3, whereas √nψ/T1/2 has dimension (3/2 − 1/2) = 1. Without specifying a coarse-graining volume/time or a fluctuation spectrum, this scaling is dimensionally inconsistent. If used as physical support for a closure argument, it needs a correct, dimensionally consistent expression with rates and averaging volume made explicit (or be removed).

P1A-E16 (Incorrect cross-reference in abstract)
Problem: The abstract claims “we acknowledge missing operators … explicitly in Sec. IV and Sec. XI.” Sec. XI concerns a “hybrid dark-energy loophole,” not operator enumeration. The omitted operators are only discussed in Sec. IV’s Scope paragraph. Fix the abstract cross-reference.

P1A-E17 (Undefined curvature object in the parity-odd ansatz; Sec. II.A.2, Eq. (5))
Problem: Seff = (α/M) ∫ eI ∧ eJ ∧ FIJ[K, R̊] introduces FIJ[K, R̊] without a definition. Standard notation would use the curvature two-form RIJ(ω) with ω = ω̊ + K (Levi-Civita + contorsion). As written, FIJ[K,R̊] is undefined, mixes formalisms, and leaves unclear which geometric object is being used. Define the connection and curvature unambiguously and rewrite the operator in standard differential-form notation.

P1A-E18 (Figure/body inconsistency: PTA spectral index value; Fig. 1 caption vs Sec. X.G)
Problem: Fig. 1 text states “PTA γ v.s. data 3.20 ± 0.42 (P3 §6).” The body (Sec. X.G) gives γ = 2.567 ± 0.382 (real-KDE). These are materially different posteriors. Reconcile and ensure a single, citable value appears consistently in figure and text, with a public reference.

P1A-M7 (Heuristic “Treh/MGUT” prefactor conflated with inflationary dilution; Sec. II.C.1, Eq. (11))
Problem: Dinf is written as exp(−3Ntot) × (Treh/MGUT)3/2, but only the first factor encodes cosmological dilution; the second is presented as a phase-space or matching coefficient. Folding them together under “inflationary dilution” obscures their very different physical origins. If retained, explicitly split the terms, justify the 3/2 power with a concrete thermal integral, and keep it separate from e-fold dilution.

P1A-M8 (Nieh–Yan “pseudoscalar θ” treated as a dynamical field; Sec. IV.B, Eq. (14))
Problem: The operator Γone−loop ⊃ (∂μθ) J5μ assumes a propagating pseudoscalar θ associated with the Nieh–Yan invariant. In minimal EC–Holst gravity without an independent axion-like field, the Nieh–Yan density is a topological density (or boundary term) and θ is not a dynamical field. Using ∂μθ in a local operator requires explicitly introducing and justifying a new dynamical pseudoscalar degree of freedom. Otherwise the term must vanish for T=0 and cannot generate birefringence. Clarify the field content or remove the operator as a minimal-ECH route.

P1A-M9 (Unsupported numerical threshold for parent black-hole mass; Sec. II.A.3)
Problem: “The parent black hole mass must exceed Mcrit ≈ 10−3 M⊙” is quoted without derivation or citation. Provide a reference or a derivation tied to the EC bounce condition and the assumed microphysics, or remove the number.

P1A-M10 (Galaxy-spin p-value claim lacks definition; Sec. V; Sec. III.B)
Problem: The statement “hemisphere null at pLEE < 10−4” is made without defining the test statistic, trials factor, masks, or how the look-elsewhere effect (LEE) was computed. This is a standalone statistical claim; it requires a self-contained description or removal from this paper.

P1A-m6 (Notation swap in tensor sector; Sec. X.C)
Problem: The text switches from hij to vR, vL without defining v (Mukhanov–Sasaki-like variable for tensors?). Either keep hij throughout or define v and its normalization.

P1A-m7 (Symbol overloading for γ; Table IV; multiple sections)
Problem: γ denotes both the Barbero–Immirzi parameter and the PTA spectral index (Table IV: “γPTA”). This invites confusion. Use different symbols (e.g., γBI and γPTA) consistently.

P1A-m8 (Symbol overloading for β; Sec. IV.B, Eq. (14) vs. birefringence angle β)
Problem: β(γ) appears as an RG β-function in Eq. (14) while β elsewhere denotes the rotation angle. Use distinct symbols (e.g., βRG for the β-function; ϑ or αCB for rotation) to avoid ambiguity.

P1A-m9 (Mixed rationale for Holst-term irrelevance; Sec. X.B–D)
Problem: The text alternates between “identically zero by Bianchi on Γ̊” and “a total derivative contributes nothing,” which are distinct statements. Settle on a single, correct rationale for the Holst dual on a torsion-free connection (Bianchi identity implies the contraction vanishes pointwise), and use it consistently.

P1A-m10 (Arithmetic check of ALP energy density inversion; Sec. IV.D)
Observation: Using β = 6×10−3 rad, mθ = 1.5×10−33 eV, and α/M = 10−21 GeV−1 = 10−30 eV−1, ρθ = m2
θ β2/[2(α/M)2] ≈ 4.0 × 10−11 eV4, not 2.8 × 10−11 eV4. The two are within a factor ~1.4; please show the one-line numeric and state precisely which H0 value and unit conversions were used at this step to prevent confusion.

P1A-m11 (Units of β in EB formula; Sec. III.A, Eq. (12))
Observation: Eq. (12) requires β in radians in the small-angle expansion. The text sometimes quotes β in degrees. Add a one-sentence reminder that β in Eq. (12) is in radians and that the uniform-rotation, small-β limit is assumed.

P1A-m12 (Spin-density notation typos; Sec. II.A.2, Step 1, Eq. (3) text)
Problem: Sabc is written with “ψγ¯ [aγ bc]ψ” (garbled bar/indices). Use standard notation Sλμν ∝ ψ̄ γ[λ γμ γν] ψ and define all index positions once to avoid ambiguity.

P1A-m13 (Figure 1 stale number vs text; cross-reference clarity)
Problem: Beyond the absolute mismatch in γPTA noted above, Fig. 1 text uses “P3 §6” to justify the 3.20 ± 0.42 value, but Sec. X.G explicitly supersedes it. Update the figure and adjust the caption to point to the single, final source. If both appear in the literature, state which dataset/analysis corresponds to which value.

P1A-m14 (Arithmetic consistency: “e32” factor; multiple places)
Observation: The inflationary differential Ntot − Nexit = 32 implies a physical-wavenumber rescaling by e32 ≈ 7.9 × 10^13, consistent with the text. Consider adding this numeric to anchor the “deep inside the inflationary subhorizon” claim quantitatively at SPHEREx k.

Rationale for additions
- Items E14–E18 address new issues in dimensional consistency, undefined geometric objects, cross-reference mistakes, and stale/mismatched numbers not covered in the initial review.
- Items M7–M10 cover new conceptual/statistical/assertion gaps (conflation of dilution and thermal matching, Nieh–Yan-as-field, unsupported Mcrit, undefined pLEE) that materially affect claims.
- Items m6–m14 are newly identified notational, unit, and arithmetic hygiene issues that will matter to PRD readers and reviewers.

If the authors choose to resubmit, please address these in addition to the previously listed Essential/Major issues.