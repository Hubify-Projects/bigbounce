# P1A auto-2026-06-08_1424pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (9239 chars)
**Wall time**: 362.4s

---

Referee report on P1A (Physical Review D – methods/statistics rigor)

Scope of review
I audited every equation, scalar, table, and figure for dimensional consistency, numerical soundness, and statistical-method rigor. I recomputed quoted significances and checked that every quantitative claim in the abstract/conclusions is traceable to the body. I also checked for use of unpublished “companion” results, internal version-history language, and non-reproducible elements.

Overall assessment
The central qualitative statement (perturbation transparency for canonical scalar matter in minimal EC–Holst) is plausible and, as stated, largely follows from standard facts: vanishing spin density implies vanishing torsion; the Holst dual reduces to the Pontryagin density on a torsion-free connection and contributes only a boundary term. However, multiple critical methodology and consistency problems prevent acceptance in its current form. Chief among them are (i) a dimensional inconsistency in the Route-2 one-loop operator used to argue a many-orders suppression (Eq. 14), compounded by an order-of-magnitude arithmetic error in Eq. (15); (ii) insertion of a nonstandard “T^2” term in the gravitational action (Eq. 1) described as “shorthand,” which is misleading at best; (iii) undefined symbols and missing derivation steps (e.g., “N” in Eq. 4; unspecified F[K, R˚] in Eq. 5); (iv) pervasive reliance on unpublished, “in preparation” companion works for core numbers, plots, and pipeline/validation claims; and (v) internal version-history language and ongoing-chain status reports that are incompatible with PRD standards.

Detailed findings and required actions
ESSENTIAL (paper cannot be accepted without these fixes)

P1A-E1
- Location: Sec. IV.B, p. 9–10, Eq. (14)
- Problem: Dimensional inconsistency in the proposed one-loop parity-odd operator: Γ_parity-odd_one-loop = −(1/16π^2) β(γ)/MPl ∫ d^4x √−g ∂μθ J5^μ. With θ dimensionless (Nieh–Yan pseudoscalar), ∂μθ has mass dimension 1 and J5^μ has mass dimension 3; the product has mass dimension 4, so the coefficient must be dimensionless. The 1/MPl factor lowers the Lagrangian density to dimension 3, which is inconsistent.
- Required fix: Either (a) remove 1/MPl and present a dimensionless coefficient with a correct one-loop derivation or citation, or (b) define θ to carry mass dimension −1 explicitly (and justify), showing how the Planck suppression enters. Then recompute all downstream amplitude estimates. Provide a traceable derivation or cite a published computation that matches the precise normalization adopted.

P1A-E2
- Location: Sec. IV.B, p. 10, Eq. (15) and surrounding text
- Problem: Numerical inconsistency by ≈ 8–10 orders of magnitude in the dimensionless ratio Δθ_one-loop/Δθ_obs. Using the paper’s numbers, α_em/(4π) ≈ 6×10^−4, H0/MPl ≈ 6×10^−61, MPl(α/M) ≈ 10^−2, β_obs ≈ 6×10^−3, the product is ≈ 2×10^−68, not 10^−58–10^−60 as stated. The “alternative ordering” yielding ∼10^−33 also lacks a defensible dimensional chain.
- Required fix: Present a step-by-step, unit-consistent computation of Δθ_one-loop/Δθ_obs with clearly stated conventions for MPl (reduced or unreduced), H0 units, and α/M units. Correct the quoted magnitude and update all narrative conclusions that refer to the erroneous range.

P1A-E3
- Location: Sec. II.A.2, p. 5, Eq. (4)
- Problem: The prefactor “3π G N/2” contains an undefined N. The standard Hehl–Datta result is L ∼ −(3κ/16)(ψ̄γ_aγ5ψ)(ψ̄γ^aγ5ψ) for minimal EC; with Holst, a γ^2/(γ^2+1) factor is known, but the appearance of “N” is unexplained.
- Required fix: Define N unambiguously or remove it. Provide a derivation or a precise citation that matches your normalization, including the Holst γ dependence.

P1A-E4
- Location: Multiple (Abstract, Sec. I, III, VI, VII, XIII, XIV, Table I, Table IV)
- Problem: Dependence on unpublished “companion” works for critical quantitative claims (MCMC posteriors; NaMaster validation; EB/ALP fits; galaxy spin null results; PTA γ; SPHEREx forecasts; running chains). PRD requires self-contained, reproducible results or references to published literature. Phrases like “documented internally rather than as externally citable arXiv-posted numbers” are unacceptable.
- Required fix: Remove or replace all analysis claims that rely on in-preparation companions. Either provide the full methods and results within this paper (including data, code, and diagnostics) or cite peer-reviewed or publicly posted works containing these results. Do not report running-chain statuses or “frozen accepted samples” without making the chains and complete configuration publicly accessible and fully documented in this submission.

P1A-E5
- Location: Multiple (Sec. V–VII, X.G, XII–XV, footnotes and narrative)
- Problem: Internal version-history/production language appears (“supersedes the earlier synthetic-Gaussian-likelihood value… used in pre-real-KDE drafts,” “chain is running,” “we deliberately do not commit to a specific calendar date”). This is incompatible with PRD norms.
- Required fix: Remove all process/production commentary, earlier-draft references, and running-chain status reports. Present a clean and final scientific narrative with only published, reproducible results.

P1A-E6
- Location: Sec. II.A.1, p. 5, Eq. (1)
- Problem: The action includes “+ (1/4) T_abc T^abc” and is described as a shorthand for the four-fermion term after integrating out torsion. In standard first-order EC (+Holst), there is no explicit torsion kinetic term; torsion is eliminated algebraically to yield a matter-sector four-fermion interaction. As written, Eq. (1) is misleading and dimensionally ambiguous.
- Required fix: Replace Eq. (1) with the standard first-order EC–Holst action (no explicit T^2 term), then explicitly show (or cite) the algebraic elimination of torsion leading to the four-fermion current–current operator in the matter sector.

P1A-E7
- Location: Sec. IX.L, p. 13–14, Eq. (20)
- Problem: The bound Ω_GW^ECH|bounce ≲ (ρ_crit/ρ_Pl)^2 ≃ 0.07–0.17 is stated without derivation or citation. As written, it is unclear why a squared density ratio bounds a dimensionless GW energy fraction.
- Required fix: Provide a derivation (including definitions of Ω_GW and the mapping from bounce-era stress-energy to GW energy density) or cite a peer-reviewed source deriving this bound. Otherwise, remove or restate the claim as a heuristic with clear caveats.

P1A-E8
- Location: Fig. 1 caption and Table I, p. 4; Table IV, p. 20
- Problem: Figure/Table text and entries rely on in-preparation works (“Paper II forecast,” “Paper I(b) MCMC,” “Paper III real-KDE”), and list numerical posteriors not supported in this paper.
- Required fix: Replace with self-contained content or published references. Remove companion-only numbers and forecasts, or include the full methodology and results in this submission.

P1A-E9
- Location: Sec. II.B, p. 6, Eq. (9) and surrounding text
- Problem: ρ_crit expression depends on γ through ∆ and leads to the 0.27–0.41 ρ_Pl window by substituting different γ values from black-hole counting schemes. In LQC the standard quoted value ρ_c ≈ 0.41 ρ_Pl is tied to a specific area-gap choice; importing black-hole entropy γ into LQC’s ∆ is nonstandard and called an “internal extrapolation.”
- Required fix: Clearly separate standard LQC assumptions from your extrapolation. Provide a precise derivation (with ∆(γ)) or cite literature where this γ dependence is established in LQC. If none, present ρ_c = 0.41 ρ_Pl as the baseline and move the γ-dependent 0.27 ρ_Pl to a speculative appendix.

P1A-E10
- Location: Sec. II.A.2–3, p. 5–6, Eqs. (5)–(6)
- Problem: Notation FIJ[K, R˚] and its dependence on contorsion K and Levi–Civita curvature R˚ is not defined; the “leading contribution” in components is asserted without an explicit intermediate.
- Required fix: Define all symbols explicitly and show one concrete contraction leading from the 3-form e ∧ e ∧ F to Eq. (6), or provide a precise reference where this operator is constructed with the same normalization.

MAJOR (significant revision required)

P1A-M1
- Location: Sec. II.A.2, p. 6–7; Sec. XII.A; Appendix B
- Problem: The order-of-magnitude [(α/M) MPl] is quoted as ∼10^−2 without a transparent numerical input (g^2 value, ln factor, M definition). A plausible estimate gives ∼10^−3. This choice feeds into N_tot and several order-of-magnitude arguments.
- Required fix: Provide a concrete numerical estimate with inputs and uncertainties (g, log, γ, M definition). Quote a range (e.g., 10^−3–10^−2) and propagate it through to N_tot and related figures.

P1A-M2
- Location: Sec. II.A.3, p. 6
- Problem: “The parent black hole mass must exceed M_crit ≈ 10^−3 M⊙” is asserted without derivation or citation.
- Required fix: Add a derivation or a peer-reviewed citation; otherwise remove the statement.

P1A-M3
- Location: Sec. II.C.1, p. 6–7, Eq. (11) and discussion
- Problem: The prefactor (T_reh/M_GUT)^{3/2} is described as a phase-space ansatz, not derived; yet it enters the tuning budget. The scaling of the “r.m.s. residual ∝ √nψ/T_reh^{1/2}” lacks a clear derivation and unit check.
- Required fix: Provide a principled derivation from a thermal partition function or kinetic-theory calculation with units consistent; quantify its uncertainty and propagate to N_tot. If not possible, remove the prefactor and reframe D_inf purely as an illustrative exponential.

P1A-M4
- Location: Sec. IX (Barriers), p. 12–14, esp. Eq. (18)
- Problem: Multiple barriers rely on undefined quantities or unproven assertions (e.g., “t3” in Eq. 18; “topological-shift duality”; scalar–tensor universality on FRW). As stated, these are not operationally testable or derived.
- Required fix: Define all symbols, provide concise derivations or precise citations for each barrier, and distinguish conjectural/philosophical points from quantitative constraints.

P1A-M5
- Location: Notation throughout
- Problem: Mixed notation “RRe,” “∗R R,” “Pontryagin density ∝ RRe.” This is inconsistent and potentially confusing.
- Required fix: Adopt standard notation throughout (e.g., R∧R˜, or Rμνρσ ˜R^{μνρσ}), define once, and use consistently.

P1A-M6
- Location: Sec. III.A, IV.D, Eq. (17), and surrounding text
- Problem: The ALP birefringence analysis uses the generic Chern–Simons coupling α/M θ F F˜. This is fine, but its relation (or non-relation) to the Holst-sector one-loop coupling must be clearly separated. Currently the text conflates "R4-fitted α/M" with “one-loop motivated α/M” without a clean bridge.
- Required fix: Clearly separate: (i) the generic ALP–photon α/M fitted to β, and (ii) any α/M emerging from EC–Holst loops. Do not use the same symbol unless they are tied by a derivation (and then, show it).

P1A-M7
- Location: Table I; Sec. VII and XIII
- Problem: SPHEREx σ(fNL) claims are presented as “surviving predictions” but rely on external forecasts; no computation is made here.
- Required fix: Rephrase as external forecasts with citations and remove any implication that these are results of this work. Alternatively, include your own Fisher calculation and systematic budget.

P1A-M8
- Location: Sec. III.B; V; VI; XIII
- Problem: Galaxy spin “confirmed null” relies on [23] in preparation. No data, classifier metrics, or bias audit are provided here.
- Required fix: Either cite a published null result or remove the claim. If you wish to include your own result, provide the full methodology, catalog construction, bias audits, and statistics in this paper.

P1A-M9
- Location: Multiple (Eqs. 7, 10, 15, Appendix B)
- Problem: Planck mass convention (reduced vs unreduced) not specified; numerical conversions (e.g., H0/MPl, MPl(α/M)) depend on this choice.
- Required fix: State the convention explicitly and apply consistently. Provide a one-line conversion reminder where used.

P1A-M10
- Location: Sec. X.G, p. 15
- Problem: “This figure supersedes … earlier synthetic-Gaussian-likelihood value…” is version-history language; also presents a PTA γ posterior from an in-preparation work.
- Required fix: Remove version-history prose and any quantitative claims not supported by a published analysis or a self-contained section here.

MINOR (address but paper can proceed)

P1A-m1
- Location: Bibliography and throughout
- Problem: Author names and diacritics: Poplawski (“Pop lawski”), Domagała, Gödel, etc.
- Required fix: Correct names and accents.

P1A-m2
- Location: Sec. X.D, Eq. (23)
- Problem: Typo “Re(˚Γ)” for R_e or similar; ensure consistent notation for the Holst dual and Pontryagin density.
- Required fix: Correct typesetting.

P1A-m3
- Location: Sec. II.A.2, p. 6
- Problem: “In components, the leading contribution reduces to … Eq. (6).” No intermediate is shown.
- Required fix: Add a one-line expansion showing how ε μνρσ e^I_μ e^J_ν F_{IJ ρσ} arises from e ∧ e ∧ F.

P1A-m4
- Location: Sec. X.B–D, p. 14
- Problem: Add a standard reference that the Pontryagin density is a total derivative and does not affect local EOM (e.g., standard GR/topology texts).
- Required fix: Insert citation(s).

P1A-m5
- Location: Throughout
- Problem: British/American spelling inconsistencies (“programme”/“program”).
- Required fix: Standardize per PRD style.

P1A-m6
- Location: Fig. 2 (p. 5)
- Problem: Axes/units not fully specified in the text; ensure clarity in the figure itself.
- Required fix: Add axis labels and units (log scale, energy density normalization) and ensure the caption states that it illustrates an ansatz.

P1A-m7
- Location: Sec. XII.A; Appendix B
- Problem: Statements like “O(0.01–0.1)” for prefactors without impact quantification.
- Required fix: Provide an uncertainty propagation or move to a footnote indicating negligible impact on the main qualitative conclusion.

NIT (cosmetic)

P1A-n1
- Location: Acknowledgments, p. 18–19
- Problem: Declaration of AI assistance (“use of Claude …”) is atypical for PRD and unnecessary.
- Required fix: Remove to conform to standard PRD acknowledgments.

P1A-n2
- Location: Throughout
- Problem: Minor encoding artifacts (e.g., “G¨odel,” “Domaga la,” “Pop lawski”).
- Required fix: Clean typesetting.

P1A-n3
- Location: Throughout
- Problem: Mixed phrasing (“Holst sector” vs “Holst term”).
- Required fix: Standardize to “Holst term” unless a broader sector is explicitly defined.

P1A-n4
- Location: Sec. I–XV
- Problem: Occasional verbose meta-remarks (“we emphasize,” “the role of this paper…”).
- Required fix: Tighten prose; remove promotional language.

Additional length/comment
The paper is long relative to the core methodological contribution (the perturbation-transparency statement). A focused version (≤ 14 pages excluding references/appendices) that (i) cleanly proves perturbation transparency, (ii) corrects the Route-2 dimensional analysis, and (iii) removes all reliance on unpublished companions would be more suitable for PRD. Consider moving the barrier catalog and phenomenological programmatic remarks to a companion review or appendix.

Traceability of abstract/conclusion scalars
- βobs = 0.342° ± 0.094° and 0.215° ± 0.074°: Numerically consistent; OK.
- Ntot ≈ 92 vs Appendix B ≈ 94: You acknowledge a ∼2% offset; acceptable once tied to explicit parameter choices and uncertainties.
- [(α/M) MPl] ∼ 10^−2: Needs a concrete numerical derivation and range (see P1A-M1).
- Δθ_one-loop/Δθ_obs suppression: Current 10^−58–10^−60 claim is not supported; recalc needed (P1A-E2).
- Ω_GW ceiling 0.07–0.17: Numerically consistent as the square of 0.27–0.41, but lacks derivation (P1A-E7).
- LiteBIRD differential significance 0.73σ: Your calculation 0.072°/√(0.03^2+0.094^2) ≈ 0.73 is correct.

## Summary recommendation
MAJOR REVISIONS

The core perturbation-transparency result is potentially publishable, but the manuscript has critical dimensional and arithmetic inconsistencies (especially in the one-loop Route-2 sector), undefined symbols and nonstandard action terms, and it relies heavily on unpublished “companion” papers for key quantitative claims. All essential items above must be addressed: correct the dimensions and recompute the Route-2 amplitude; rewrite the action and derivations cleanly; remove dependence on in-preparation works; and excise internal version-history language. Once these are fixed and the paper is made self-contained and methodologically rigorous, the revised manuscript can be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (new issues only)

P1A-E11
- Location: Sec. II.A.2, p. 6–7, Eq. (7)
- Problem: Dimensional inconsistency and undefined symbols. The relation α/M ∼ (g^2/32π^2) γ/M ln(Λ^2/μ^2) + δNY mixes a term of mass dimension −1 (∝ 1/M) with an additive counterterm δNY written as dimensionless. If δNY denotes a finite renormalization of the same operator, it must carry the same mass dimension (i.e., δNY → δNY/M). The coupling g is also undefined (which interaction, which normalization), so the numerical estimate is not reproducible.
- Required fix: Define g and its value/range; ensure every term on the RHS has mass dimension −1. If δNY is a finite piece, write δNY/M and justify its size and sign. Provide a published derivation (or a careful EFT estimate) with the same normalization.

P1A-E12
- Location: Sec. IV.B, p. 9–10 (Route 2 narrative, esp. Eq. (14) → Eq. (15))
- Problem: Unjustified mapping from a parity-odd fermionic operator to CMB birefringence. The one-loop ansatz Γ ⊃ −(1/16π^2) β(γ)/MPl ∫√−g ∂μθ J5μ couples the Nieh–Yan pseudoscalar to the axial fermion current. No derivation is given that this operator generates a uniform rotation of photon polarization (β) or how it feeds into EB. The subsequent comparison Δθone−loop/Δθobs assumes such a mapping without establishing the photon-sector coupling or Maxwell-equation modification.
- Required fix: Either derive the photon-rotation rate from this operator (showing the chain from ∂μθ J5μ to modified electromagnetism and EB) or explicitly separate Route 2 from birefringence and remove Eq. (15)’s comparison to βobs.

P1A-E13
- Location: Sec. X.B (step 4), Sec. X.D, Eq. (23)
- Problem: Misidentification of the Holst term with the Pontryagin density. The text asserts that “the Holst dual contraction reduces on the Levi-Civita connection to the Pontryagin density ∝ RR˜” and then writes Re(˚Γ) = (1/2) εμνρσ Rμνρσ(˚Γ) = (1/2) ∗R R ≡ ∂μKμ. This conflates three distinct objects:
  - The Holst density is linear in curvature: e ∧ e ∧ R (equivalently e ∧ e ∧ ∗R in internal indices), not quadratic.
  - The Pontryagin density is quadratic in curvature: R ∧ R˜ ≡ (1/2) εμνρσ Rμν
αβ Rρσ
αβ, a total derivative (∂μKμ).
  - The scalar contraction εμνρσ Rμνρσ (with all four spacetime indices) vanishes identically on a torsion-free connection by pair symmetry (Rμνρσ = Rρσμν).
- Required fix: Correct the identities. State clearly: (i) on torsion-free backgrounds the Holst term does not alter the classical equations of motion (but is not the Pontryagin density); (ii) Pontryagin is R∧R˜ (quadratic), not εμνρσ Rμνρσ. Remove or replace Eq. (23) and the related sentences with accurate statements (with citations).

P1A-E14
- Location: Sec. X.D, Eq. (23)
- Problem: The equality “(1/2) εμνρσ Rμνρσ(˚Γ) = ∂μKμ” is false. The RHS is the Pontryagin density; the LHS is a linear-in-R scalar that vanishes identically for Levi–Civita by the exchange symmetry of Riemann. This error invalidates the “explicit verification” as written.
- Required fix: Remove this equality and provide the correct topological identity (Pontryagin = ∂μKμ with R∧R˜), and reframe the perturbation-transparency argument accordingly (e.g., by standard first-order variation showing the Holst term’s non-contribution to EOM for torsion-free matter).

P1A-M11
- Location: Sec. IV.D, Eq. (17)
- Problem: Missing factor of 1/2 in the birefringence angle. For L ⊃ −(g/4) φ F F˜, the uniform-rotation angle is β = (g/2)[φ(to) − φ(trec)]. The text uses β = (α/M) Δθ without the 1/2. This biases the inferred α/M by a factor of ∼2.
- Required fix: Use β = (α/2M) Δφ (or define α/M ≡ 2g if preferred), recompute the numerical examples, and adjust all quoted α/M bounds accordingly.

P1A-M12
- Location: Fig. 1 (caption/text bubble), Sec. X.G, Table III
- Problem: Stale/discordant PTA spectral-index numbers. Fig. 1 text shows “PTA γ = 3.0 v.s. data 3.20 ± 0.42 (P3 §6)” while the body later states “2.567 ± 0.382 (real-KDE).” This is an internal inconsistency.
- Required fix: Update Fig. 1 and all instances to a single, supported value (preferably a published one) or remove all PTA numbers from this paper if supported only by “in preparation” work.

P1A-M13
- Location: Sec. II.A.2, Eqs. (5)–(6); Appendix B
- Problem: Internal inconsistency between the effective operator and its on-shell use. The “leading contribution in components” is written as ∝ εμνρσ eIμ eJν FIJρσ. For a torsionless Levi–Civita connection this reduces to εμνρσ Rμνρσ, which vanishes identically; yet Appendix B maps this operator, evaluated “on-shell at the bounce,” to a non-zero ρΛ ∼ (α/M) M5
Pl. The torsion dependence is not kept consistently between the two statements.
- Required fix: Clarify whether FIJ[K, R˚] retains torsion contributions in the on-shell mapping (and then do not reduce it to R(˚Γ) in components), or explicitly state that the Levi–Civita reduction is zero and that the non-zero bounce-scale mapping uses torsionful contributions. Provide one explicit torsionful contraction to justify the scaling.

P1A-M14
- Location: Sec. XII.A, Eq. (24)
- Problem: Angle-bracket notation 〈(α/M) MPl〉 is undefined (RG average? thermal average? ensemble?). This obscures what is being averaged and how uncertainties propagate.
- Required fix: Define the averaging operation or remove the brackets and specify a concrete numerical value/range used in estimates.

P1A-M15
- Location: Sec. IX.D (Barrier 4)
- Problem: Planck-suppression arithmetic. The text asserts O(10^−122) generically for factors like (mϕ/MPl)^2 at mϕ ∼ H0. With the stated conventions, (H0/MPl)^2 ≈ (6×10^−61)^2 ≈ 3.6×10^−121. The order quoted (10^−122) is not consistent with the other places in the paper that use H0/MPl ≈ 10^−61.
- Required fix: State the Planck-mass convention explicitly and use a single rounded value (e.g., 10^−121) consistently, or provide a range and propagate it.

P1A-m8
- Location: Table I, row “H0/σ8 tension resolution?”
- Problem: Misleading wording. “Recovers ΛCDM” is not a “resolution” of any tension; it merely states consistency with the baseline model (and relies on an unpublished companion).
- Required fix: Rephrase to “consistent with ΛCDM baselines (no additional resolution claimed here)” and remove dependence on unpublished chains.

P1A-m9
- Location: Sec. X.C, Eq. (21)
- Problem: Notation inconsistency. Prime denotes conformal-time derivative, but the friction term is written with H (used elsewhere for cosmic-time Hubble). Standard is ℋ = a′/a in conformal time.
- Required fix: Replace H with ℋ or state explicitly that H in Eq. (21) is the conformal Hubble rate and distinguish it from the cosmic-time H used elsewhere.

P1A-m10
- Location: Sec. II.A.2, Eq. (7)
- Problem: The coupling g is never defined (gauge? gravitational? numerical value/range). This prevents reproducing the 10^−2 OOM claim downstream.
- Required fix: Define g and specify its magnitude (and uncertainty) used in all numerical estimates.

P1A-m11
- Location: Throughout (Sec. II preamble)
- Problem: Missing explicit unit conventions. The text appears to use natural units (c = ℏ = 1) and often the reduced Planck mass, but this is not stated once and consistently.
- Required fix: Add a single-sentence convention statement (units; reduced vs unreduced MPl) and enforce it wherever ratios like H0/MPl or MPl(α/M) appear.

P1A-m12
- Location: Secs. III.A, XII, Table IV
- Problem: Mixed use of the “benchmark” β ≈ 0.27°–0.30° alongside the measured 0.342° ± 0.094° and 0.215° ± 0.074°. The term “midpoint” is used without definition.
- Required fix: Define what 0.27° represents (a chosen benchmark for a GR+ALP toy point), and avoid implying it is an average of the two measurements. Keep measured numbers separate from benchmarks.

P1A-m13
- Location: Throughout
- Problem: Mixed notation γ vs γBI for the Barbero–Immirzi parameter.
- Required fix: Choose a single symbol and define it once; if multiple schemes are discussed, use subscripts consistently (γSU(2), γU(1), etc.).

P1A-m14
- Location: Sec. III.A, Eq. (12)
- Problem: No citation for the uniform-rotation EB formula CℓEB ≈ 2β (CℓEE − CℓBB).
- Required fix: Add a standard reference (e.g., Lue, Wang & Kamionkowski 1999; or a modern CMB polarization text) for the small-angle limit.

P1A-m15
- Location: Sec. II.C.1 and XII.A
- Problem: Coexistence of two mutually exclusive narratives (a−3 dilution of coherent torsion vs. “thermal reset” erasure at reheating) without a clear timing hierarchy may confuse readers.
- Required fix: Add a one-sentence clarification that the a−3 scaling is only an illustrative pre-reheating parametrization and that the thermal reset dominates at/after reheating, nullifying any surviving coherent torsion.

Explanation
These issues emerged on a targeted second pass focused on arithmetic cross-checks, figure/body consistency, dimensional analysis, and internal logic. The Holst–Pontryagin conflation (E13–E14), the unjustified use of a fermion operator to infer photon birefringence (E12), and the dimensional inconsistency in Eq. (7) (E11) are particularly critical and were not captured in the initial review. Addressing them will materially change parts of the derivation and several narrative conclusions.