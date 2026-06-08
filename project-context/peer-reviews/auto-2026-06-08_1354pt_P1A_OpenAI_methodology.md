# P1A auto-2026-06-08_1354pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (8691 chars)
**Wall time**: 211.0s

---

Referee report on P1A (Physical Review D, methods/statistics rigor)

Scope of review
I audited the full 21-page manuscript, including the abstract, figures, tables, equations, and bibliography, for methodological rigor: statistical validity, derivation chains, dimensional analysis, internal arithmetic consistency, and traceability of all quoted scalars to calculations in the body. Below are all issues found, classified by severity.

ESSENTIAL issues (must be fixed before further consideration)

P1A-E1
- Location: Abstract and throughout (e.g., p.1–2; p.4–5; Table I p.4; “Companion paper” paragraph p.5; §III.B p.8; §VI p.11; Table III footnote p.16; Acknowledgments p.18; Ref. [6], [23], [46], [47])
- Problem: Load-bearing results (ΛCDM+ΔNeff posteriors, H0 value, galaxy-spin “confirmed null,” birefringence pipeline validation, ALP parameter fits, PTA analysis) rely on “companion works in preparation” and unpublished internal chains. The paper explicitly states numbers “should be read as internal-analysis inputs” and that chains are “frozen accepted samples” not publicly posted. PRD cannot accept claims that depend on unpublished analyses.
- Required fix: Remove all reliance on unpublished or in-preparation results, or include the complete methods and results in this manuscript (data, priors, likelihoods, chains, convergence diagnostics, robustness checks). Alternatively, cite published, peer-reviewed sources and use only those values in this paper’s arguments. Rephrase any conclusions that hinge on non-public material.

P1A-E2
- Location: §II.C Eq. (10) p.6; §XII Eq. (24) p.15; Appendix B Eq. (B2) p.19; multiple places where ρΛ and Λ are interchanged
- Problem: Dimensional inconsistency between Λ and ρΛ. Eq. (10) defines Λeff = Ξ MPl^2 + cω ω^2 (mass-dimension 2), while elsewhere the dark-energy mapping is written as ρΛ = Ξ MPl^4 (mass-dimension 4). The manuscript alternates between Λ and ρΛ without a consistent convention or the 8πG relation.
- Required fix: Adopt a single convention and define it explicitly (reduced vs unreduced MPl). State the relation ρΛ = Λ MPl^2/2 (or appropriate 8π factors) and use Λ consistently (dimension 2) or ρΛ consistently (dimension 4) everywhere. Correct all equations, text, and tables accordingly.

P1A-E3
- Location: §II.A.2–§II.C, Fig. 2 p.5, Eq. (6) p.5–6; Appendix B p.19–20; §XIV.D p.17 (Ntot ≈ 92)
- Problem: The leading parity-odd operator in Eq. (6) is declared dimension +1 (off-shell) and the paper explicitly labels the mapping to ρΛ as a phenomenological “on-shell scaling ansatz,” yet the manuscript repeatedly treats quantitative outputs (e.g., Ntot ≈ 92, structural tension) as numerically meaningful. The “Treh/MGUT” prefactor carries only dimensional/aesthetic justification, not a derivation, and the residual sensitivity to ∆Ntot is used as if robust.
- Required fix: Demote all quantitative inferences that depend on Eq. (6)/Appendix B to qualitative, order-of-magnitude statements. Provide transparent uncertainty propagation that reflects: (i) the operator-dimension deficit, (ii) the absence of a first-principles derivation for the (Treh/MGUT)3/2 factor, and (iii) scheme dependence in MPl(α/M). If you wish to retain Ntot numbers, give a rigorous derivation or clearly bracket them with conservative, justified bounds and emphasize they are heuristic.

P1A-E4
- Location: §IV.B, Eq. (14)–(15) p.9
- Problem: The one-loop “Route 2” birefringence bound is presented via a dimensionless ratio (Eq. 15), but the derivation is not shown. The normalization of θ, the mapping from Γparity-odd to a cumulative rotation angle, and the time integral are omitted. The appearance of βobs in the denominator of Eq. (15) is unexplained. A conflicting statement appears that an “alternative ordering” yields ~10−33, which undermines the claimed robustness.
- Required fix: Provide a complete derivation from the operator in Eq. (14) to the integrated birefringence angle, including: field normalization conventions; the time integral between recombination and today; explicit dependence on H0, MPl, αem; and the role of MPl(α/M). Remove the ambiguous “alternative ordering” remark or reconcile it analytically. Present a single, reproducible bound with stated assumptions.

P1A-E5
- Location: §IX.L, Eq. (20) p.13
- Problem: “Vacuum Amplification Ceiling” states ΩECHGW|bounce ≲ (ρcrit/ρPl)^2 ≃ 0.07–0.17 with no derivation. Squaring the density ratio to bound a GW energy fraction is not justified, and the numerical band appears pulled from the ρcrit range without a physical calculation.
- Required fix: Either (a) supply a derivation for Eq. (20), starting from a concrete GW production mechanism and energy budget, or (b) remove the equation and replace with a clearly labeled conjecture or order-of-magnitude bound with references. If retained, connect to a transfer function and today’s spectrum to show relevance.

P1A-E6
- Location: §IX.A, Eq. (18) p.12
- Problem: “Mass-Coupling Lock” gives geff ∼ 1/(MPl√|t3|) ∼ H0/MPl without defining t3 or the underlying Poincaré gauge Lagrangian, and without a derivation from the propagator or mixing matrix. The numerical conclusion (∼10−61) is asserted without the intermediate steps.
- Required fix: Define the model (kinetic and mass terms for torsion), the parameter t3, and derive geff at low energies. Show how mT ∼ H0 leads to geff ∼ H0/MPl. Provide references or a self-contained derivation.

P1A-E7
- Location: §II.C.1 “Reheating thermal-reset barrier” p.6–7
- Problem: The claim that C/P-violating scattering rates at Treh exceed H and erase ⟨J5μ⟩ lacks quantitative estimates or citations. This is used as an independent “closure.”
- Required fix: Provide explicit rate estimates (or references) for the dominant axial-current randomization processes at Treh, compare to H(Treh), and quantify the residual ⟨J5μ⟩ and its scaling. Otherwise, remove this as an independent closure argument.

P1A-E8
- Location: §IV.A p.8–9 vs §II.A.2 p.5–6
- Problem: Internal inconsistency regarding γ dependence. Eq. (4) includes the Holst-induced factor γ^2/(γ^2+1), but later (§IV.A) the text says “torsion-elimination map is independent of γ at the classical level.” These statements conflict unless one specifies minimal vs non-minimal fermion couplings (Mercuri cancellations, Nieh–Yan, etc.).
- Required fix: State clearly which fermion coupling prescription is used. If minimal coupling yields γ-dependent axial–axial contact, say so and use it consistently. If non-minimal couplings/Nieh–Yan render γ unobservable classically, adjust Eq. (4) and the discussion. Provide precise citations for the adopted scheme.

P1A-E9
- Location: §X p.14–15; Abstract p.1
- Problem: “Perturbation-transparency theorem” is asserted “at all orders,” but only a sketch is given. There is no explicit variation of the action showing that the Holst term reduces to a boundary term for FRW + scalar perturbations up to cubic order, nor a careful argument that boundary terms do not affect the perturbation action or bispectrum.
- Required fix: Provide a formal proof or at minimum an explicit second- and third-order perturbative calculation showing: (i) torsion vanishes for scalar matter, (ii) the Holst term reduces to the Pontryagin density on the Levi-Civita connection, and (iii) its contribution to the quadratic and cubic actions is a total derivative that does not modify equations of motion or the bispectrum. State and justify boundary conditions.

P1A-E10
- Location: §III.B p.8; §V p.11; §VI p.11; abstract p.1
- Problem: “Galaxy Spin Asymmetry: A Confirmed Null” is claimed based on Paper IV [23] “in preparation” with no reproducible details in this manuscript. The “>100 orders of magnitude” underprediction claim is also unquantified in-text.
- Required fix: Remove the “confirmed null” claim unless full methods, data, and error budgets are included here or in a published paper. If you wish to retain the “underpredicts by >100 OOM” statement, present the computation (coupling value, astrophysical scaling, predicted asymmetry) that leads to that number.

P1A-E11
- Location: Table I p.4; “Companion paper” paragraph p.5; Table IV p.20
- Problem: H0, ΔNeff, σ8 and related numbers are listed as “verified values” from non-public MCMC runs. This fails PRD reproducibility and traceability standards.
- Required fix: Replace with published values (e.g., Planck 2018) or include full MCMC details and chains in this paper. Otherwise, remove these rows from the tables and from the narrative.

P1A-E12
- Location: Table III footnote p.16; multiple places with “in preparation,” “this volume,” “running chain” language
- Problem: Version-history/internal-lab status language appears in the body (explicitly disallowed by the instructions and PRD style). E.g., “At the time of this writing ... we deliberately do not commit to a specific calendar date ... Paper I(b) ... running on a dedicated MPI pod ...”.
- Required fix: Remove all internal-status prose, “this volume” labels, and “in preparation” qualifiers from the body. Only cite public, citable sources. If essential, move such notes to a non-scientific cover letter.

P1A-E13
- Location: §II.A.2 Eq. (7) p.6; §IV.D p.10
- Problem: The statement “MPl·(α/M) ∼ 10−2” and the implied α/M ∼ 10−21 GeV−1 are used repeatedly, but Eq. (7) does not yield a number without specifying g, ΛUV/μ, δNY. No numeric inputs are given.
- Required fix: Provide an explicit numerical estimate for Eq. (7) (values for g, ΛUV, μ, δNY) that justifies MPl(α/M) ~ 10−2, or make clear that α/M is phenomenologically fitted from birefringence and not derived from Eq. (7). Keep these uses separate.

P1A-E14
- Location: §XIII p.16–17; §X p.15; Fig. 1 caption p.4; refs [5], [46], [47]
- Problem: Multiple claims reference non-public analyses (ACT DR6 birefringence “follow-up,” “real-KDE GPU MCMC” for PTA with new spectral index) that are not available to the reader.
- Required fix: Remove or replace with published sources. Do not present numbers that are not traceable to public datasets/papers.

MAJOR issues (significant revision required)

P1A-M1
- Location: §II.A.1, Eq. (1) p.5
- Problem: The action includes “+ 1/4 TabcTabc” and then states “is a shorthand for the four-fermion contact ... after integrating out torsion; it is not an independently specified kinetic term.” Including it in the bare action and simultaneously treating it as a proxy for an integrated-out contact term is conceptually inconsistent and risks double counting.
- Required fix: Either (i) present the first-order (Palatini/tetrad + independent connection) action and integrate out torsion explicitly to obtain the four-fermion term, or (ii) omit the T^2 term from the starting action and introduce the induced four-fermion interaction after torsion elimination. Clarify which path is used.

P1A-M2
- Location: §III.A Eq. (12) p.7
- Problem: The small-rotation formula CℓEB ≈ 2β(CEEℓ − CBBℓ) is quoted without specifying conventions (E/B sign, polarization basis, whether the 2β approximation includes lensing B-modes, etc.). Not fatal, but the formula underpins later qualitative arguments.
- Required fix: State the assumptions and conventions (flat-sky vs full-sky, small-angle limit, treatment of lensing B-modes). Provide a reference.

P1A-M3
- Location: §IV.D Eq. (17) p.10
- Problem: The ALP birefringence mapping β = (α/M) √(2ρθ)/mθ presumes Δθ ≈ √(2ρθ)/mθ with unit excursion, but the factor-of-2 and time evolution are not justified (β ∝ gϕΔϕ/2 in much of the literature; Δϕ depends on dynamics). You later use this to argue mass tuning mθ ~ H0.
- Required fix: Derive β from the ALP Lagrangian with ϕF F̃, specify normalization (with/without 1/2), and clarify whether Δϕ is an excursion between recombination and today or a present-day amplitude. Provide the time integral as appropriate.

P1A-M4
- Location: §X p.14–15 (tensor sector)
- Problem: The claim “No GW birefringence, no tensor chirality ... from the ECH mechanism” is correct for scalar matter and torsionless backgrounds, but the text does not quantify whether boundary terms could induce parity-odd correlators in nontrivial topologies or with time-dependent θ-like backgrounds. You assert “no equations of motion” but do not address observables constructed from boundary terms.
- Required fix: Add a brief discussion (with references) on when Chern–Pontryagin boundary terms can or cannot affect cosmological correlators. State the assumptions (topologically trivial FRW, fixed boundary conditions) under which your conclusion holds.

P1A-M5
- Location: §II.B Eq. (9) p.6; Fig. 2 p.5
- Problem: The LQC ρcrit expression is used with γ values from black-hole entropy counting schemes. You acknowledge this is an internal extrapolation. However, Fig. 2 and later numerics treat ρcrit ∈ [0.27, 0.41] ρPl as an input. The mapping between black-hole entropy γ and cosmological holonomy corrections is not justified here.
- Required fix: Either justify the cross-scheme use of γ with references that connect the entropy-counting γ to cosmological holonomy scale, or fix γ to the standard LQC choice and propagate the implied uncertainty consistently.

P1A-M6
- Location: §IV.A p.8–9
- Problem: Route-1 closure states the induced NJL term is parity-even (correct) and “amplitude-suppressed,” but no quantitative bound is given (e.g., upper limit at recombination or today using an explicit nψ). The closure is qualitative only.
- Required fix: Provide an explicit upper bound using reasonable fermion densities and show ρNJL ≪ ρΛ numerically. Include all factors (γ dependence if retained).

P1A-M7
- Location: §XIII p.16–17; §VII p.11
- Problem: Forecast for SPHEREx fNL significance relies on Heinrich et al. (2024) but mixes Fisher-ideal and post-systematic numbers without a clear, conservative final figure. The text switches between 6.25σ (ideal) and “3–5σ realistic,” with several degradations (template overlap, GR projection, photo-z) not explicitly compounded.
- Required fix: Present a single, conservative forecast number with all degradations compounded, or separate clearly as two scenarios with full accounting. Avoid mixing the two in the same sentence.

P1A-M8
- Location: Multiple (e.g., §XIII, §XIV.D)
- Problem: Comparisons of “σ” significances from different null hypotheses (e.g., LiteBIRD nonzero β vs. differential against current central value) appear side-by-side. You correctly distinguish them in §XV, but earlier text risks conflation.
- Required fix: At every juxtaposition of σ from different nulls, explicitly state they are not directly comparable (you do this once in §XV; do so consistently elsewhere).

MINOR issues (address, but do not block)

P1A-m1
- Location: §II.A.2 Eq. (3) p.5
- Problem: Notation Sabc = 1/4 ψγ̄[aγbc]ψ is nonstandard; “γbc” should be clarified (is this the antisymmetrized product of Dirac matrices?).
- Required fix: Define precisely (e.g., γ[aγbγc] or σab) and index conventions.

P1A-m2
- Location: §IV.A Eq. (13) p.8–9
- Problem: “κ” is introduced without definition immediately above; later you equate κ=8πG. Make it explicit where used.
- Required fix: Define κ at first use and keep consistent.

P1A-m3
- Location: §III.A p.7
- Problem: The small-angle EB relation would normally include a note about lensing B-mode dominance at ℓ ≳ few hundred. Add a brief qualifier.
- Required fix: Add one sentence clarifying regime of validity.

P1A-m4
- Location: §II.A.3 p.6
- Problem: “The parent black hole mass must exceed Mcrit ≈ 10−3 M⊙” is asserted without citation.
- Required fix: Provide a reference or derivation.

P1A-m5
- Location: Throughout
- Problem: MPl is used without stating reduced vs unreduced. You use numbers consistent with unreduced MPl in Eq. (15), but it should be explicit.
- Required fix: State at first use and keep consistent.

P1A-m6
- Location: §X D Eq. (23) p.14
- Problem: “Re(˚Γ) = 1/2 ε R R (˚Γ)” uses “Re” for Pontryagin density; notation is confusing (Re could be “real part”).
- Required fix: Use a standard symbol (e.g., ∗RR or 1/2 εR R) and avoid “Re.”

NITS (cosmetic/editorial)

P1A-n1
- Location: Bibliography and text (e.g., [13], [14], [39])
- Problem: Spelling “Pop lawski” with a space; journal style requires consistent author names.
- Required fix: Ensure consistent spelling “Popławski” (with or without diacritics per journal style) across text and refs.

P1A-n2
- Location: Acknowledgments p.18
- Problem: “The author acknowledges the use of Claude ... as an AI research assistant.” Journal policies may discourage tool branding in acknowledgments.
- Required fix: Replace with a neutral acknowledgment (“AI-assisted drafting tools were used to organize notes; all scientific claims were verified by the author.”) or remove per PRD policy.

P1A-n3
- Location: Fig. 1 caption p.4
- Problem: The caption is long and mixes interpretation and claims of “closure.”
- Required fix: Shorten to describe the figure content; move interpretive text to the body.

P1A-n4
- Location: Throughout
- Problem: Repeated phrases (“generically non-zero pointwise but a total derivative”) appear verbatim several times.
- Required fix: Consolidate to one clear statement; avoid repetition.

P1A-n5
- Location: Units
- Problem: Mixed use of GeV and eV in some inline conversions without explicit unit conversions can confuse (e.g., §IV.D discussion near Eq. (17)).
- Required fix: Whenever switching units, show the conversion step or keep one unit system.

Length and scope
The manuscript is long (21 pages) relative to the provable core contribution (channel-level amplitude arguments and the perturbation-transparency observation). Given the extensive reliance on unpublished companions and phenomenological ansätze, I recommend trimming to ≤14 pages by:
- Removing all observational claims that depend on in-prep works (galaxy spins, internal MCMC, PTA re-analyses).
- Focusing on the theoretical closure arguments and providing the missing derivations called for above.
- Moving programmatic roadmaps and multi-paper cross-references to a brief outlook section.

## Summary recommendation
MAJOR REVISIONS

Justification
The paper raises interesting points about the (non)role of the Holst sector in scalar/tensor perturbations and assembles several amplitude-level arguments against specific minimal ECH dark-energy routes. However, it currently fails PRD methodological standards in multiple essential ways: dependence on unpublished “companion” results; dimensional inconsistencies between Λ and ρΛ; incomplete or missing derivations in key load-bearing equations (one-loop birefringence bound, GW ceiling, PGT coupling); internal inconsistencies regarding γ dependence; and inclusion of internal status language. These issues are correctable. A substantially revised, self-contained manuscript that removes reliance on non-public results, fixes dimensional bookkeeping, and supplies the missing derivations could be suitable for reconsideration.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW ADDITIONAL FINDINGS (second-pass audit)

P1A-E15
- Location: §IV.B Eq. (14)
- Problem: Dimensional inconsistency of the one-loop parity-odd operator. With the normalization used, ∂μθ has mass-dimension 1 (θ dimensionless), J5μ has mass-dimension 3, and d^4x√−g contributes −4, so the operator ∫ d^4x√−g (1/MPl) ∂μθ J5μ yields an action with net mass-dimension −1 (not 0). The 1/MPl prefactor is insufficient to make Γ dimensionless; an additional inverse mass is needed (or a differently normalized θ). This undermines the subsequent birefringence bound unless the normalization is fixed and stated.
- Required fix: Specify field normalizations and mass-dimension assignments and adjust the operator coefficient (e.g., 1/MPl^2, or normalized θ with mass-dimension 1) so that the action is dimensionless. Then re-derive the birefringence bound.

P1A-E16
- Location: Abstract p.1; §I.A.1 p.3; Table II p.13; §XV p.18
- Problem: The claim of “13 logically-independent” barriers is not demonstrated. No dependency graph, orthogonality proof, or counterexample analysis is provided; several barriers appear potentially overlapping (e.g., B4 Planck suppression, B11 decoupling universality, B10 UV→IR specificity) but independence is asserted.
- Required fix: Either (a) provide a formal independence argument (e.g., “removing barrier X leaves mechanism Y viable; removing X and Z together is still insufficient…”) or (b) soften to “13 distinct barriers” and remove claims of logical independence.

P1A-E17
- Location: §IV.B Eq. (15) p.9
- Problem: Arithmetic mismatch in the “canonical Route-2” ratio. Using the manuscript’s own numbers: αem/(4π) ≈ 5×10−4, H0/MPl ≈ 10−61, MPl·(α/M) ≈ 10−2, βobs ≈ 6×10−3 rad gives ∆θone−loop/∆θobs ≈ (5×10−4 × 10−61)/(10−2 × 6×10−3) ≈ 8×10−61, not 10−58–10−60. The stated “58–60 orders” band is not reproduced from the inputs provided.
- Required fix: Recompute the bound carefully and report a single number (with a justified uncertainty band) consistent with the stated inputs, or adjust the inputs explicitly to yield the claimed range.

P1A-E18
- Location: §II.C.1 “Reheating thermal-reset barrier” p.6–7
- Problem: The stated residual scaling for the thermal expectation of the axial current, “r.m.s. residual scales as ∼ √nψ/T1/2reh,” is dimensionally inconsistent for ⟨J5μ⟩ (mass-dimension 3). No citation is provided. As written, √n/T1/2 has mass-dimension 1, not 3.
- Required fix: Provide a dimensionally consistent estimate for ⟨J5μ⟩T and its variance (with references) or remove the formula. If the point is purely qualitative (fast equilibration drives ⟨J5μ⟩ → 0), state it without an incorrect parametric form.

P1A-E19
- Location: §IV.E “Closure summary” p.11
- Problem: Misplaced cross-reference. The sentence “The condensate mechanism yields a vacuum energy that is parametrically too large … documented in Sec. X as a quantitative closure” is incorrect: Sec. X treats perturbation transparency, not a condensate calculation.
- Required fix: Point to the correct location (likely §IV.A or a dedicated subsection where the condensate route is quantitatively closed), or add the missing derivation where claimed.

P1A-E20
- Location: §III.A p.7 vs Fig. 1 caption p.4 and body text
- Problem: Figure-caption vs body mismatch. The Fig. 1 caption advertises “ΔNeff null: −0.020 ± 0.169,” but the body repeatedly states that these values come from non-public companion runs “in preparation.” The caption reads like a standalone result, while the body hedges its status.
- Required fix: Either (a) remove numerical posteriors from figure captions unless they are supported by public, reproducible analyses in this manuscript, or (b) include the full MCMC details and data within this paper (see P1A-E1/E11).

P1A-E21
- Location: §III.A p.7; §XII “Spectator-ALP birefringence” p.16
- Problem: Inconsistent central values for β. The text alternates between “β ≈ 0.27–0.30°” and βobs = 0.342° ± 0.094°, and then labels 0.27° as a “midpoint.” The midpoint of 0.342° and 0.215° is 0.2785°, not 0.270°. These inconsistencies are small numerically but symptomatic of stale or hand-waved numbers in places that claim precision.
- Required fix: Choose and stick to a single reference value (with uncertainty), clarify when “benchmark” values are chosen for illustration, and correct the “midpoint” arithmetic if retained.

P1A-M9
- Location: §II.A.1 Eq. (1) p.5
- Problem: Nonstandard torsion-squared structure and coefficient. The bare action includes “+ 1/4 TabcTabc” with no decomposition into irreducible torsion pieces (vector, axial, tensor), and no justification that this specific quadratic form yields the standard Hehl–Datta result upon elimination. In EC theory the minimal action is linear in curvature; torsion-squared pieces represent extra couplings and change the algebraic elimination and the induced four-fermion coefficient.
- Required fix: Specify the torsion-squared sector (full quadratic basis and coefficients) or remove the T^2 term from the starting action and perform torsion elimination from the standard Einstein–Cartan–Holst action. Show that the standard axial–axial four-fermion term (with its coefficient) is recovered.

P1A-M10
- Location: §IX.I “Liouville Conservation (Branch J)” p.13
- Problem: Over-generalized closure. The assertion that phase-space volume conservation “closes” vacuum selection at the bounce is made without a Hamiltonian proof in the specific ECH/LQC setting or a discussion of time-asymmetric ingredients (e.g., reheating, particle production) that could break simple Liouville arguments in the cosmological coarse-grained system.
- Required fix: Provide a precise statement (and citation) of Liouville conservation in the relevant minisuperspace or perturbative phase space used here, including assumptions (no dissipation, unitary evolution, choice of variables), or downgrade this to a heuristic comment rather than a formal barrier.

P1A-M11
- Location: §IV.D p.10 (last paragraph, tuning discussion)
- Problem: The claimed fractional tuning window “∆mθ/mθ ∼ 10−1” for simultaneously fitting β and ρΛ (with α/M fixed) is not derived. The width depends on the propagated uncertainties in βobs and in the mapping ρθ ∝ m2θ (and on the model for Δθ evolution), none of which are quantified.
- Required fix: Derive ∆mθ/mθ from error propagation using the stated βobs uncertainty and any model priors (or remove the numerical value and state only that the matching is tuned to mθ ≈ H0).

P1A-m7
- Location: §II.A.2 Eq. (5)–(6) p.5–6
- Problem: Undefined symbol F[I J] and ambiguous construction. The object FIJ[K, R̊] (and its component F IJρσ) is introduced without definition; is it the curvature 2-form R IJ, the contorsion field strength, or a specific combination? This ambiguity propagates into Eq. (6) and the subsequent dimensional argument.
- Required fix: Define FIJ explicitly and state whether it is the curvature of the independent connection, the Levi-Civita curvature, or a mixed object.

P1A-m8
- Location: §II.A.2 (paragraph after Eq. (5)) p.5–6; §II.B Eq. (9) p.6
- Problem: Missing numerical constants in the “area-gap mass scale.” Marea-gap ∼ MPl/√γ is quoted without the overall numerical factor derived from ∆ = 4√3 π γ ℓ^2P. This leads to ambiguity when used quantitatively (e.g., in Fig. 2 scaling discussions).
- Required fix: Provide the full expression (including constants) for the mass scale associated with the LQG area gap and use it consistently in any numerical estimates.

P1A-m9
- Location: §III.A p.7
- Problem: Stale/ambiguous phrasing: “parity-odd structure is qualitatively consistent with β ≈ 0.27–0.30°.” The cited WMAP+Planck result is 0.342° ± 0.094°; 0.30° is not the central value, and the range appears ad hoc.
- Required fix: Replace with the cited quantitative result and uncertainty; if 0.27° is used as a benchmark for later forecasts, label it clearly as such.

Explanation
This second-pass audit focused on arithmetic checks, caption/body coherence, dimensional consistency of every displayed operator, internal cross-references, null-procedure comparability, abstract-vs-body fidelity, unsupported novelty, hedged claims, appendix/main-text alignment, and stale numbers. The additional issues above are new and do not duplicate items in the initial report. They primarily concern (i) a dimensionally inconsistent one-loop operator used for birefringence; (ii) unsupported claims of logical independence; (iii) arithmetic and cross-reference mismatches; and (iv) missing definitions/normalizations that block reproducibility. Addressing these, in addition to the essential and major issues from the first review, is necessary to meet PRD standards.