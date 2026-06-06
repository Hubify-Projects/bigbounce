# P1A auto-2026-06-05_1817pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (8013 chars)
**Wall time**: 336.6s

---

Referee report for Physical Review D (methods-focused review)

Manuscript: “Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter”
Pages: 21

Overall scope of this review
- This is a methods/statistical rigor and derivations audit. I checked equations for dimensional consistency, recomputed quoted ratios and significances, and audited table/figure numbers. I also verified that every load-bearing scalar in the abstract and conclusions has a traceable derivation in the body. I flagged reliance on unpublished “companion” works. I did not assess novelty/importance except where it intersects methodology sufficiency for PRD.

Findings

ESSENTIAL (must be fixed before PRD can consider publication)

P1A-E1 (Abstract; pp.1–3; Table I p.4; multiple sections) — Reliance on unpublished/“in preparation” companion results for core numerical claims
- Text: Multiple instances: “Companion paper—ΛCDM+ΔNeff MCMC verification … 309,189 frozen accepted samples… Paper I(b) [6].”; “Paper II forecast [2]”; “Paper IV [23]”; “Paper III [46]”; “NaMaster pipeline validation … in companion Paper I(b) [6].”
- Problem: Load-bearing numerical values and procedural claims (H0 = 67.68 ± 1.06; ΔNeff ≈ 0; SPHEREx σ(fNL) ≈ 0.7; galaxy-spin null; PTA γ result) are not documented in this manuscript nor in public preprints. PRD cannot accept key results that depend on unpublished analyses.
- Required fix: Either (a) remove all claims that rely on “in preparation” works and restrict the paper to what is fully derived here, or (b) include complete, self-contained methods, data descriptions, priors, convergence diagnostics, and numerical results for every quantity used in the text (MCMC chains, galaxy-spin classifier performance/bias audits, forecast details). Do not cite “frozen accepted samples” without full reproducible context in this manuscript. Numbers imported from companion works must be either re-derived here or replaced with community-standard published values (e.g., Planck 2018) and used only illustratively.

P1A-E2 (Sec. IV.B, Eq. 15; pp.9–10) — Dimensional and numerical inconsistency in the R2 one-loop closure estimate; 27+ orders-of-magnitude ambiguity
- Text: “∆θone-loop/∆θobs ∼ (αem/4π) (H0/MPl) · M/MPl · α · βobs … numerically ∼ 10−58 to 10−60 … an alternative ordering yields ∼ 10−33.”
- Problem: The presented ratio is not derived from a clearly defined EFT operator with unambiguous normalization. The appearance of both MPl·(α/M) and M/MPl·α in different lines signals double counting/inconsistent parameterization. The paper acknowledges a 10^27 discrepancy depending on “ordering,” which invalidates the channel-closure argument. A quantitative no-go at the amplitude level demands a single, dimensionally consistent derivation from a specified operator with explicit time integration and redshift factors.
- Required fix: Provide a consistent EFT starting point for R2 with a well-defined Lagrangian density (coefficients, dimensions, fields). Derive ∆θ from recombination to today with proper units, show the time integral, and express the result as a single dimensionless number. Remove the alternative “ordering” and present one consistent calculation. If an upper bound is intended, state and justify it rigorously.

P1A-E3 (Sec. II.A.1 Eq. 1; Sec. II.A.2; Sec. IV.A, Eq. 13; throughout) — Inconsistent treatment of torsion-squared term and torsion elimination (double counting risk)
- Text: Eq. (1) includes “+ 1/4 TabcTabc” while also stating it is a “shorthand for the four-fermion contact interaction obtained after integrating out the non-propagating torsion; it is not an independently specified kinetic term.” Later, torsion is “integrated out” to produce Eq. (13).
- Problem: Writing an explicit T^2 term in the starting action and then also performing torsion elimination to generate a four-fermion term risks double counting unless the variational procedure is specified precisely (first-order formalism with Lagrange multipliers vs. inserting the on-shell torsion back into S). As written, it is ambiguous whether Eq. (1) is a starting action to be varied or an already-reduced effective action.
- Required fix: Present the first-order Einstein–Cartan–Holst action without an a priori T^2 term, vary to obtain the Cartan equation, solve algebraically for torsion in terms of spin density, and then insert back to obtain the four-fermion term. Alternatively, if Eq. (1) is the already-reduced effective action, remove the “integrate out torsion” step to avoid double counting and state explicitly that T is not an independent variable in the variation.

P1A-E4 (Sec. X; pp.14–15) — “Perturbation-transparency theorem” insufficiently derived for PRD as a theorem
- Text: Five-line outline: “scalar has zero spin density ⇒ torsion = 0 ⇒ Levi-Civita ⇒ Holst term = Pontryagin (total derivative) ⇒ no EOM.” Then claim “at all perturbation orders.”
- Problem: For a theorem-level claim in PRD, the derivation must: (i) start from the full ECH action; (ii) demonstrate explicitly that δSHolst[ΓLC] is a boundary term under FRW + perturbations including boundary conditions; (iii) show no contribution to the quadratic and cubic actions for scalar and tensor perturbations; (iv) discuss gauge issues and any residual surface terms relevant to cosmological correlators. The current sketch is not sufficient to support an “all orders” theorem claim.
- Required fix: Provide a complete derivation: write the action in terms of Levi-Civita variables when spin density vanishes, expand to second and third order in cosmological perturbations, and show the Holst (Pontryagin) term contributes only as a total derivative that does not affect the equations of motion nor correlation functions under standard boundary conditions. Cite and, if necessary, reproduce the standard variational identities. Remove the “all orders” claim unless you present a general proof beyond cubic order.

P1A-E5 (Appendix B; Eq. B2; Sec. II.C.2; Sec. XII.A; multiple places) — Persistent dimensional inconsistency between Λ and ρΛ and use of an off-shell dimension-1 operator to infer a dimension-4 density
- Text: Eq. (B2): “ρbounceΛ ∼ (α/M) M5Pl ∼ 10−2 M4Pl.” Sec. II.C: “Λeff = Ξ M2Pl + cω ω^2 … ρΛ = Ξ M4Pl elsewhere.”
- Problem: Λ and ρΛ are interchanged with inconsistent powers of MPl across the paper. Eq. (B2) sets a dimension-4 quantity equal to a coefficient with net +1 mass dimension times M^5Pl and then equates it to 10−2 M4Pl, which is dimensionally inconsistent unless MPl=1 is tacitly assumed (it is not, since explicit MPl factors are carried elsewhere). The authors acknowledge the operator in Eq. (6) has off-shell mass dimension +1, but they nonetheless use it in quantitative closure arguments.
- Required fix: Choose a consistent convention: either work entirely in reduced Planck units (MPl = 1) and clearly state this at the beginning, or carry all MPl factors consistently. Distinguish Λ (mass^2) from ρΛ (mass^4) throughout. If Eq. (6) is not a valid dimension-4 local operator, do not use it to set or “map” amplitudes; remove all amplitude-level conclusions that rely on it, or replace with a correct dimension-4 operator and redo the analysis.

P1A-E6 (Sec. IV.D, Eq. 17; pp.10–11) — R4 derivation must specify the birefringence normalization and units
- Text: “β = (α/M) ∆θ ≈ (α/M) sqrt(2 ρθ / m^2θ) … fits ρΛ for mθ ≈ H0 at α/M = 10−21 GeV−1.”
- Problem: The birefringence mapping depends on the operator normalization. In common conventions for L ⊃ −(gϕγ/4) ϕ F F~, the rotation angle is β = ½ gϕγ ∆ϕ. The manuscript uses β = (α/M) ∆θ without justifying the factor of 2. Since this feeds directly into the ρθ estimate, the factor-of-two ambiguity changes the required ρθ by a factor of 4.
- Required fix: State the operator normalization explicitly (e.g., L ⊃ −(α/4M) θ F F̃) and derive the exact β–θ relation. Then recompute ρθ. Provide units for α/M in the calculation (convert GeV−1 to eV−1), show the numeric substitution leading to ρθ ≈ 2.8 × 10−11 eV^4, and quote the numerical uncertainty from the normalization choice. The qualitative “naturalness” conclusion remains, but the quantitative mapping must be correct.

P1A-E7 (Multiple sections; pp.1, 3, 5, 16–18, 19–20) — Version-history and internal bookkeeping language appears in the manuscript
- Text: “earlier drafts,” “supersedes the earlier synthetic-Gaussian-likelihood value,” “hUBIFY-2026-002,” “companion technical note, available upon request,” “frozen accepted samples,” “Paper I(b) Table IV row … (new),” “GPU MCMC.”
- Problem: PRD forbids version-history chatter and internal project tags in the scientific record.
- Required fix: Remove all version-history language, internal codes, chain-running statuses, and references to “earlier drafts.” Replace “available upon request” with proper citations or material included in the manuscript or as Supplemental Material.

P1A-E8 (Sec. IX; Table II; pp.12–14) — “14 mechanism-class barriers” are mostly asserted without derivations or quantitative limits
- Text: Barriers 1–14 include substantial claims (e.g., mass-coupling lock geff ∼ H0/MPl ∼ 10−61; Liouville conservation; Decoupling universality; Vacuum amplification ceiling Eq. 20) with minimal or no derivations.
- Problem: Many of these are not self-evident. For PRD, each barrier must be either (a) a theorem/proposition with a proof, or (b) a quantitative bound/citation to a published proof. Presently, several are statements of philosophy or hand-waving.
- Required fix: For each barrier on which a route-closure depends, provide a derivation or a precise literature reference and reproduce the intermediate steps needed for your use-case. In particular: derive Eq. (20), justify Barrier 9 (Liouville conservation) in this cosmological context, and quantify Barrier 11 (Decoupling universality) with explicit coupling-size bounds.

P1A-E9 (Sec. II.C; Eq. 10; pp.6–7) — Mixed use of Λeff and ρΛ without a consistent conversion
- Text: “Λeff = Ξ M2Pl + cω ω^2 … The dark energy scale is set by Ξ ∼ 10−123.” Elsewhere, ρΛ = Ξ M4Pl.
- Problem: Λ and ρΛ are used interchangeably without defining the conversion (e.g., ρΛ = Λeff M2Pl/8π or in reduced Planck units). This bleeds into later discussions.
- Required fix: Define Λeff and ρΛ precisely at first use and maintain consistent usage. If the paper chooses to discuss ρΛ exclusively, convert all Λeff appearances accordingly.

P1A-E10 (Sec. III.B; Sec. V; pp.8, 11) — Galaxy spin “confirmed null” claim without in-paper methods
- Text: “Independent ViT-Small chirality classifier … confirms the null … full bias-audit … Paper IV [23].”
- Problem: A key observational conclusion is asserted without any methods, validation metrics, or data selection in this manuscript, and reliant on “in preparation.”
- Required fix: Either remove the claim entirely or supply a complete methodology section (classifier architecture, training data, test accuracy, domain-shift audits, label-noise handling, dipole estimator definition, null tests, look-elsewhere corrections) and data availability sufficient for PRD replication.

MAJOR (significant revision required)

P1A-M1 (Sec. IV.A; Eq. 13; p.9) — Route-1 amplitude bound needs a quantitative density-level comparison to ρΛ
- Text: “ρNJL ∼ κ n^2ψ ∼ n^2ψ/M^2Pl … many orders below ρΛ.”
- Problem: This conclusion needs numbers. At recombination or today, use conservative upper limits on fermion number densities for electrons, baryons, neutrinos and show the resulting energy density (with the Holst γ correction if claimed) vs. ρΛ ≈ 2.8 × 10−11 eV^4. Quote the margin quantitatively.
- Required fix: Provide an explicit bound with numbers and units, and note any assumptions (charge neutrality, degeneracy, polarization).

P1A-M2 (Sec. IV.C; Eq. 16; p.10) — Route-3 “running of γ” uses an ad hoc β-function
- Text: “we adopt the one-loop running ansatz dγ/d ln μ = (1/12π^2)(NLF − NRF) γ + O(γ^2) … used solely for amplitude budget.”
- Problem: This is not taken from the cited work (Date–Kaul–Sengupta or Benedetti–Speziale) and is presented as an “upper-bound EFT ansatz.” PRD requires either using the published β-function or deriving one.
- Required fix: Use the actual result from Benedetti & Speziale (with four-fermion terms) or provide your own derivation starting from a specified matter content and regularization scheme. Then recompute the implied amplitude bound.

P1A-M3 (Sec. II.C.1; “Reheating thermal-reset barrier”; pp.6–7) — Qualitative washout argument lacks rate estimates
- Text: “C/P-violating scattering rates exceed the Hubble rate at Treh … coherent axial-current background is rapidly washed out.”
- Problem: This is plausible but unquantified. The paper leans on this as an independent “closure” of torsion-memory channels.
- Required fix: Provide a numerical comparison: estimate the relevant axial-charge randomization rate Γ5(T) vs. H(T) at T ∼ Treh for SM interactions, and show Γ5/H ≫ 1. Quantify the residual ⟨J5μ⟩T or its variance and the time scale for washout.

P1A-M4 (Sec. II.C.2; p.7) — “Underpredicts galaxy spin asymmetry by >100 orders of magnitude” without calculation
- Text: “The parity-odd operator coupling α/M ∼ 10−21 GeV−1 underpredicts any plausible spin asymmetry by > 100 orders of magnitude.”
- Problem: No estimate or model is provided to support this numerical statement.
- Required fix: Either remove the claim or give a back-of-envelope model that maps α/M to an expected spiral spin asymmetry amplitude (including redshift scaling, galaxy-scale fields, and polarization fractions), then compute the order-of-magnitude deficit.

P1A-M5 (Sec. IX.L; Eq. 20; p.13) — ΩGW ceiling lacks derivation and cosmological evolution discussion
- Text: “ΩECHGW|bounce ≲ (ρcrit/ρPl)^2 ≃ 0.07–0.17 … total bounce-epoch GW energy-density fraction … not directly comparable to PTA.”
- Problem: No derivation is provided for why the square of ρcrit/ρPl bounds the GW energy fraction at the bounce. The physical meaning of this “ceiling” is unclear without a spectrum and a transfer function.
- Required fix: Provide a derivation or remove. If it is a heuristic bound, state it as such and do not use it as a quantitative barrier.

P1A-M6 (Abstract; Sec. I; Sec. IV.E; throughout) — “Channel-level closure” overclaim relative to what is actually proven
- Text: “channel-level amplitude closure of the four enumerated minimal-ECH dark-energy routes” while repeatedly noting omitted operators (gravitational Chern–Simons, parity-odd 4-fermion partner).
- Problem: Given the unresolved dimensional issues (E2, E5), reliance on ansätze for running (M2), and lack of full derivations for several “barriers,” the term “closure” is too strong for PRD.
- Required fix: Rephrase to “we find strong evidence against these routes under stated assumptions” and ensure the abstract and conclusions accurately reflect what is demonstrated rigorously in the text.

P1A-M7 (Sec. II.A.2; Eq. 7; p.6) — Undefined symbols and unclear origin
- Text: “α/M ∼ (g^2/32π^2) γ/M ln(Λ^2UV/μ^2) + δNY.”
- Problem: The coupling g is not defined (gauge, gravitational?), δNY is not specified, and no derivation is given.
- Required fix: Define all symbols, specify the loop diagram and theory space, or remove the equation if it cannot be justified.

P1A-M8 (Sec. X.C; Eq. 21; p.14) — Tensor equation-of-motion claim would benefit from an explicit action expansion
- Text: “h′′ij + 2Hh′ij + k^2 hij = 0; no parity dependence.”
- Problem: While likely correct if torsion vanishes, the paper should show the second-order action in tensor modes in the presence of the Holst term evaluated on ΓLC to verify no parity-odd corrections survive.
- Required fix: Include the quadratic action for tensor modes and demonstrate explicitly that SHolst[ΓLC] contributes only a boundary term.

MINOR (address but not publication-blocking)

P1A-m1 (Throughout; e.g., Abstract p.1; Sec. X p.14) — Notation “RRe” vs. RR̃
- Problem: The Pontryagin density should be written R ∧ R̃ or ½ ε R R. “RRe” is non-standard and confusing.
- Fix: Use a consistent, standard notation: R ∧ R̃, or Rμνρσ ˜Rμνρσ.

P1A-m2 (Sec. II.A.1; p.5) — Clarify Planck mass convention (reduced vs unreduced)
- Problem: MPl sometimes appears without stating whether it is reduced (2.435×10^18 GeV) or unreduced (1.22×10^19 GeV).
- Fix: Declare the convention once and use it consistently; adjust all numerical ratios (e.g., H0/MPl) if needed.

P1A-m3 (Sec. I.A; Sec. XII.B; Sec. XIII; Sec. XV) — Condense extensive meta-discussion
- Problem: Many programmatic asides (NANOGrav re-analysis values, chain-status notes, “this value supersedes…”) distract from the central derivations.
- Fix: Remove or move such asides to Supplementary Material. PRD prefers concise manuscripts focused on the presented derivations.

P1A-m4 (Sec. II.B; pp.6) — Reference precision on ρcrit window
- Problem: The text states a 0.27–0.41 ρPl window as “an internal extrapolation across counting schemes.” This should be carefully worded to avoid implying Ashtekar–Singh quote both endpoints.
- Fix: Present the standard ρcrit ≃ 0.41 ρPl with γ ≈ 0.2375 and separately note the implied change with γ ≈ 0.274, clearly labeling the latter as your inferred value using the same formula.

P1A-m5 (Sec. III.A; Eq. 12; p.7–8) — Birefringence relation presentation
- Problem: The standard small-angle result is CEBℓ ≈ 2β CEEℓ if CBB ≪ CEE. The “− CBBℓ” term is fine but should be accompanied by a comment that it is negligible for current limits.
- Fix: Add a sentence clarifying the approximation and the regime of validity.

NIT (cosmetic/editorial)

P1A-n1 (Throughout) — Typos and spacing
- Examples: “R∧Re” (missing tilde), “Domaga la” spacing, “Poincar´e” accent artefact, “programme” vs “program” inconsistency, occasional hyphenation artifacts.
- Fix: Copyedit.

P1A-n2 (Acknowledgments; p.18) — Brand mention of AI tool
- Problem: “Acknowledges the use of Claude (Anthropic) as an AI research assistant.” Not wrong, but atypical for PRD.
- Fix: Consider rephrasing generically (“AI-assisted editing was used; all scientific content is the author’s responsibility”) to avoid brand endorsement.

Length and scope
- The paper is long relative to the hard derivational content currently included. Much of the space is spent on programmatic commentary, companion-paper cross-references, and qualitative “barrier” statements. After removing companion-paper dependencies and adding the required derivations for the key claims (E2–E5, M2, M5, M8), the paper can be focused and likely reduced to ~12–14 pages.

Audit of key numbers and equations
- ρcrit formula (Eq. 9) numerically reproduces 0.41 (γ=0.2375) and 0.27 (γ=0.274): OK.
- H0/MPl ~ 10−61 using H0 ≈ 1.5 × 10−33 eV and MPl ≈ 1.22 × 10^28 eV: OK.
- β difference 0.342° − 0.27° = 0.072°; combined σ ≈ sqrt(0.03^2 + 0.094^2)=0.0987°; Z ≈ 0.73σ: OK.
- R4 mapping ρθ = m^2θ β^2 / [2 (α/M)^2] with α/M = 10−21 GeV−1 and mθ = H0 gives ρθ ≈ 4.0 × 10−11 eV^4 (close to ρΛ ≈ 2.8 × 10−11 eV^4): OK if normalization β = (α/M)Δθ is explicitly adopted (see E6).
- Eq. (B2) dimensional mismatch flagged above.

Bibliography checks
- Many citations are plausible; several are “in preparation” and unacceptable as authorities for results used here. Ensure all load-bearing claims cite published or arXiv-posted works with stable identifiers.

## Summary recommendation
REJECT

Given the number of essential methodological deficiencies — reliance on unpublished companion papers for key numerical claims, a central route-closure estimate (R2) that is dimensionally inconsistent and numerically ambiguous by tens of orders of magnitude, an insufficient derivation for the main “perturbation transparency theorem,” and pervasive Λ vs ρΛ dimensional inconsistencies — the manuscript does not currently meet PRD methodological standards. A substantially rewritten, self-contained paper with rigorous derivations and without dependence on unpublished materials could be reconsidered, but the present submission requires changes well beyond a major revision.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes re-audit)

Note: I do not repeat items already listed in my initial report. New issues are labeled continuing the same scheme.

ESSENTIAL

P1A-E11 (Fig. 1 caption and Table III vs. Sec. X.G; stale/conflicting PTA γ values)
- Observation: Fig. 1 and Table III present “PTA γ = 3.0 v.s. data 3.20 ± 0.42 (P3 §6).” In Sec. X.G the text states an updated result “γ = 2.567 ± 0.382 … supersedes the earlier … 3.20 ± 0.42.”
- Problem: Core numbers in figure/caption and table disagree with the updated value in the body. This is not a trivial formatting issue; it creates contradictory quantitative claims.
- Required fix: Update Fig. 1 caption and Table III to use the same PTA result quoted in Sec. X.G, or vice versa. State clearly which dataset/analysis each number comes from and do not mix them within the same manuscript.

P1A-E12 (Arithmetic; ACT vs WMAP+Planck birefringence consistency overstated)
- Text: “ACT DR6 follow-up … β = 0.215° ± 0.074°; … consistent within ∼ 1.4σ” relative to WMAP+Planck β = 0.342° ± 0.094°.
- Recompute: Δβ = 0.127°. σcomb = sqrt(0.094^2 + 0.074^2) = 0.1196°. Z = 0.127/0.1196 = 1.06σ, not 1.4σ.
- Required fix: Correct the stated significance to ≈1.1σ, or show the calculation that yields 1.4σ if a different combination/weighting was intended.

P1A-E13 (Internal contradiction: “no fine-tuning” vs “naturalness objection” for R4)
- Text A (Sec. IV.D): “the spectator-ALP route … only by tuning mθ ∼ H0 … the cosmological constant problem in disguise.” 
- Text B (Sec. XII.B): “A spectator ALP with fa ∼ MPl, m ∼ H0 is … consistent … without fine-tuning.”
- Problem: These are mutually inconsistent conclusions about the same parameter point.
- Required fix: Resolve and state a single, consistent position. If you regard m ∼ H0 as tuned, use that description throughout and quantify the tuning; if not, justify why it is natural in your framework.

P1A-E14 (Eq. 14; undefined dimension/role of θ leads to potential dimensional mismatch)
- Text: Γone-loop ⊃ −(1/16π^2) β(γ)/MPl ∫√−g ∂μθ J5μ.
- Problem: The mass dimension of θ is never specified. If θ is dimensionless (common for angles), ∂μθ has dimension 1; with J5μ (dim 3) and 1/MPl (dim −1), the Lagrangian density has dim 3, not 4. If θ has dim 1, it’s consistent — but this must be stated and justified (θ as a canonically normalized pseudoscalar with [θ]=1).
- Required fix: Specify [θ] and its normalization (kinetic term, origin as Nieh–Yan pseudoscalar or ALP-like field). Reconfirm dimensional consistency of Eq. (14) under that choice.

P1A-E15 (Eqs. 5–6; undefined F IJ[K, Γ̊] construction)
- Text: Seff ∝ eI ∧ eJ ∧ FIJ[K, Γ̊].
- Problem: FIJ[K, Γ̊] is never defined. Is F the curvature of the full connection? A mixed functional of contorsion K and Levi-Civita Γ̊? The notation suggests a hybrid object, which is nonstandard and leaves the operator ill-defined.
- Required fix: Define precisely the curvature used (full curvature of Γ = Γ̊ + K, its decomposition, and which piece enters). Without this, the subsequent dimensional discussion and any amplitude mapping from Eqs. (5–6) are not well-posed.

MAJOR

P1A-M9 (Ntot inconsistency between main text and Appendix B)
- Text: Main text repeatedly uses Ntot ≈ 92 as the controlling value; Appendix B derives Ntot ≈ 94 for the MPl-to-ρΛ hierarchy, attributing the ~2% offset to ansatz choices.
- Problem: The manuscript mixes these values without a single, explicit convention. This propagates to structural-tension statements and fine-tuning reparameterizations.
- Required fix: Choose and consistently use one value (with an uncertainty band) or present both but tie each to a specific, traceable assumption. Flag all downstream uses as carrying that uncertainty.

P1A-M10 (Sec. II.C.1; “thermal-reset barrier” scaling is dimensionally unclear)
- Text: r.m.s. residual “∼ √nψ/T1/2reh” and statements like “the cube of the fermion bilinear scales as the cube of the fermion number density.”
- Problems: 
  - √nψ/T1/2reh has mismatched units unless a dimensionless normalization is specified; as written, it cannot represent a mean axial current or a directly observable fraction. 
  - The “cube of the fermion bilinear” phrase is conceptually muddled; torsion ∝ J5 (a bilinear), and any quadratic torsion energy density scales like J5^2, not “cube.”
- Required fix: Provide a consistent thermal-field-theory derivation of axial-charge washout: define the observable (e.g., mean polarization fraction), specify its dimensionless scaling, and show Γ5(Treh)/H(Treh) ≫ 1 with numbers. Remove ambiguous “cube” language.

P1A-M11 (Sec. II.A.3; parent black-hole mass threshold Mcrit ≈ 10−3 M⊙ stated without derivation/citation)
- Text: “The parent black hole mass must exceed Mcrit ≈ 10−3 M⊙ ….”
- Problem: No derivation or reference is provided; the value is non-obvious and used to support “easily satisfied” naturalness.
- Required fix: Cite the source or derive Mcrit (e.g., from bounce-density conditions, torsion-induced pressure, or collapse threshold) with the necessary assumptions.

P1A-M12 (Sec. II.B; use of γSU(2)=0.274 in the LQC ρcrit formula without a consistent LQC derivation)
- Text: ρcrit is quoted as 0.41 ρPl for γ ≈ 0.2375 and then “internal extrapolation” to 0.27 ρPl using γSU(2) ≈ 0.274.
- Problem: LQC’s ρcrit depends on the area-gap and quantization choices; directly swapping in the BH-entropy γSU(2) is not a standard LQC result and could be misleading without a consistent LQC derivation for that γ.
- Required fix: Either stick to the standard LQC value (with its quantization choice) or supply a consistent derivation/argument justifying the substitution. Clearly segregate “standard LQC” numbers from “author’s extrapolation.”

MINOR

P1A-m6 (Notation clash: Kμ used for both electromagnetic and gravitational Chern–Simons currents)
- Text: In Sec. IV.D, Kμ is the electromagnetic Chern–Simons current; in Sec. X.D/Eq. (23), Kμ denotes the gravitational Chern–Simons current.
- Fix: Use distinct symbols (e.g., Kemμ vs Kgravμ) to avoid confusion.

P1A-m7 (Undefined angle-bracket notation in Eq. 24)
- Text: Ξ ≡ ⟨(α/M) MPl⟩ Dinf.
- Problem: The meaning of ⟨…⟩ is not defined (time/ensemble/UV average?).
- Fix: Define the averaging operation or remove the brackets.

P1A-m8 (Fig. 1 “PTA γ = 3.0 v.s. data …” phrasing)
- Problem: “v.s.” suggests a model-vs-data tension graphic, but γ = 3.0 appears as a model line while the body now centers on 2.567 ± 0.382. The caption should state explicitly what is being compared (a class prediction vs a specific measurement) and avoid implying agreement with a superseded number.
- Fix: Rephrase to avoid ambiguity; align with updated numbers per E11.

P1A-m9 (EB small-angle relation context)
- Text (Eq. 12/caption): CEBℓ ≈ 2β(CEEℓ − CBBℓ).
- Suggestion: Add a sentence that for current limits CBBℓ ≪ CEEℓ so CEBℓ ≈ 2β CEEℓ, and note when the subtraction matters.

P1A-m10 (Symbol “RRe”)
- Problem: Continued nonstandard notation for the Pontryagin density (“RRe”).
- Fix: Replace by standard RR̃ or ½ εμνρσ Rμνab Rρσab throughout.

RATIONALE FOR “FRESH EYES”
- I focused on cross-checking numbers embedded in captions vs body, redoing quick significance calculations that were not previously recomputed, scanning for undefined symbols in new operators, and reconciling statements that appear in different sections about the same physical point (ALP tuning; PTA spectral index). These are common failure modes in late-stage drafts and were not fully covered in my initial pass.

Summary: The new issues include (i) contradictory/stale numbers between figure/table and body (PTA γ), (ii) a concrete arithmetic error (1.06σ vs claimed 1.4σ), (iii) an internal contradiction on “fine-tuning” for R4, (iv) undefined/dimensionally ambiguous fields in a key operator, (v) an ill-defined hybrid curvature in the parity-odd ansatz, and (vi) dimensionally unclear thermal-washout scalings. Addressing these is prerequisite to a coherent, self-consistent manuscript.