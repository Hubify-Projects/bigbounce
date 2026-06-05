# P1A auto-2026-06-05_1517pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (9933 chars)
**Wall time**: 267.1s

---

Referee report for: “Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter”

Scope of review
I evaluated the full manuscript for methodological rigor: derivation chains, dimensional analysis, internal arithmetic consistency, statistical claims, error propagation, and traceability of every load-bearing scalar in the abstract and conclusions to the body of the paper. I also audited tables, equations, and figure captions for consistency.

Overall assessment
The paper’s central physical point (torsion decouples from scalar/tensor perturbations in minimal ECH; the Holst term reduces to a boundary term on the Levi-Civita connection) is correct and well known. However, the manuscript relies heavily on unpublished “companion” works for essential numerical inputs and claimed observational results; several key closures are based on dimensionally inconsistent operators or on power-counting ansätze rather than controlled EFT derivations; and there is pervasive internal/provenance language inappropriate for a PRD article. As written, the paper does not meet PRD standards for methodological rigor and self-contained presentation.

Findings

ESSENTIAL

P1A-E1
Section I (pages 3–5), throughout (Table I, Fig. 1 caption, Sec. III B, Sec. VI, Sec. VII, Sec. XIII, Table IV)
Problem: Reliance on unpublished “companion” papers for core inputs and claims. Examples:
- “Companion paper.— ΛCDM+ΔNeff MCMC verification … documented internally … should be read as internal-analysis inputs … until Paper I(b) is publicly posted.”
- Galaxy spin null result is asserted but deferred to “Paper IV [23] (in preparation).”
- SPHEREx fNL forecast and PTA reanalysis numbers are deferred to “Paper II [2]” and “Paper III [46],” both “in preparation.”
- Table IV quotes posterior cosmological parameters (H0, ΔNeff, σ8, Ωm) from Paper I(b) [6], which is in preparation.
Required fix: All load-bearing numerical results used to support conclusions must be either (i) reproduced in this manuscript with sufficient methodological detail, data description, and diagnostics to be independently assessed; or (ii) replaced by citations to peer-reviewed, publicly available sources. Remove internal/in-preparation references as sources of quantitative claims or relegate them to non-essential context.

P1A-E2
Sec. IV.B (page 9–10), Eq. (14)–(15)
Problem: Dimensional inconsistency and notational confusion in the one-loop parity-odd operator and amplitude bound.
- Eq. (14): “Γ_parity-odd_one-loop = −(1/16π^2) β(γ)/MPl ∫√−g ∂μθ J5μ” is dimensionally inconsistent if θ is dimensionless (as implied for a topological/Nieh–Yan field): ∂θ has mass dimension 1, J5 has 3; product 4; coefficient must be dimensionless. The extra 1/MPl gives dimension 3, not 4.
- Eq. (15): The ratio mixes αem and a separate coupling “α” introduced earlier; the final expression contains “· M/MPl · α · βobs” with unclear provenance. Two orderings are said to give wildly different answers (~10^−58 vs ~10^−33), indicating an uncontrolled estimate.
Required fix: Provide a dimensionally consistent EFT operator with a clearly defined normalization and symbols (distinct from the fine-structure constant), and derive a single, unambiguous amplitude bound. If only an order-of-magnitude bound is possible, show the explicit steps and assumptions yielding the final dimensionless ratio, keeping track of units. Use distinct symbols for EM fine-structure (αem) and any new coupling (e.g., gθγ).

P1A-E3
Sec. II.A.2, Eq. (6); Appendix B (pages 5–6, 19)
Problem: The central parity-odd operator used to motivate the DE scaling, Lodd ∝ (α/M) ε e e F, is explicitly dimension +1, not +4. While the text acknowledges this and labels the mapping as an ansatz, the operator continues to be used to support e-fold bookkeeping and “structural tension” conclusions later in the paper.
Required fix: Either (a) replace Eq. (6) with a consistent dimension-4 operator and propagate the consequences through the amplitude and e-fold analysis; or (b) reframe every downstream use of the operator (Ntot requirements, suppression factors, “structural tension”) as purely hypothetical/illustrative, explicitly segregated from any claimed closure, and remove quantitative claims that rely on the dimensionally inconsistent term.

P1A-E4
Sec. IX.A, Eq. (18) (page 12)
Problem: “Barrier 1” uses undefined symbol t3 and asserts geff ∼ 1/(MPl sqrt(|t3|)) ∼ H0/MPl ∼ 10^−61 with no derivation, context, or definition of t3.
Required fix: Define all symbols and provide a derivation (or a citation to a standard, peer-reviewed derivation) that leads from a specified Poincaré gauge theory Lagrangian to this effective coupling scaling. If the result depends on model choices (e.g., particular torsion kinetic terms), state them explicitly.

P1A-E5
Sec. II.C.1 “Reheating thermal-reset barrier” (pages 6–7)
Problem: The claim that C/P-violating scattering “exceeds the Hubble rate at T ∼ Treh” and thus “rapidly washes out” ⟨J5μ⟩ is asserted without any rate calculation, cross sections, or references to standard-model processes at GUT-scale reheating. This argument is subsequently used as an independent closure of an ECH DE route.
Required fix: Provide an explicit estimate comparing the relevant axial current equilibration rate Γ5(T) to H(T) at T ∼ Treh, including the dominant SM processes and couplings, and show Γ5/H ≫ 1 over the required temperature interval. Otherwise, present the “thermal reset” solely as a qualitative hypothesis and not as a quantitative closure.

P1A-E6
Sec. IV “Route 2 closure” (pages 9–10) and Sec. XII.A / Appendix B
Problem: Inconsistent treatment of Ntot and the dilution factor Dinf across the paper: Ntot ≈ 92 is used repeatedly, while Appendix B recomputes the Planck-to-ρΛ gap as requiring Ntot ≈ 94. The paper then uses that Ntot value to argue a structural tension with SPHEREx-accessible k-modes.
Required fix: Choose a single, internally consistent Dinf/Ntot derivation (based on a dimensionally consistent operator) and propagate that value throughout. If the conclusion truly depends only on order-of-magnitude, avoid anchoring on a specific “92” and present a robust inequality with an error budget.

P1A-E7
Throughout: internal version-history and provenance language (e.g., Sec. X.G page 15; Sec. I, Sec. V–VII; Table III notes)
Problem: The manuscript contains internal versioning/provenance statements inappropriate for a PRD paper:
- “supersedes the earlier synthetic-Gaussian-likelihood value … used in pre-realKDE drafts”
- “hUBIFY-2026-00X; companion paper, this volume”
- “GPU MCMC”
- “frozen accepted samples”
This language signals draft-stage bookkeeping and undermines the archival character of the paper.
Required fix: Remove all version-history and internal-bookkeeping statements. Replace with standard, citable references; provide succinct method summaries where needed.

P1A-E8
Sec. V (page 11), Sec. III.B (page 8)
Problem: Galaxy spin null result is asserted as an empirical conclusion of this work but fully deferred to an unpublished “Paper IV [23].” No data description, selection criteria, classifier performance metrics, or systematics are provided here.
Required fix: Either (i) remove the galaxy-spin result from this paper (it is not essential to the ECH closure claims), or (ii) include a concise but complete methods/results section with sufficient detail to independently assess the finding (sample size, sky coverage, classifier accuracy, calibration, null tests, error bars).

MAJOR

P1A-M1
Sec. IV.D (page 10–11), Eq. (17)
Problem: Notational collision between α (fine-structure constant) and α (ALP–photon Chern–Simons coupling) across the manuscript. Eq. (17) and surrounding text use “α/M” to denote gθγ with dimensions GeV^−1, while elsewhere αem/(4π) appears. Eq. (15) even contains “… α/MPl · M/MPl · α · βobs …” intermixing them.
Required fix: Use distinct symbols: e.g., αem for fine-structure constant; gθγ ≡ α/M for the ALP–photon coupling; avoid “α” alone for new couplings. Update all equations and text accordingly.

P1A-M2
Sec. IX (pages 12–14), Table II
Problem: The catalog of 14 “barriers” contains several statements that are assertions without derivation or citation (e.g., Barrier 2 “Topological-Shift Duality,” Barrier 3 “Scalar-Tensor Universality,” Barrier 11 “Decoupling Universality”). While the perturbation-transparency theorem is adequately argued for scalars, many other barriers require proof or should be reframed as working hypotheses.
Required fix: For each barrier that is used to “close” a route, either provide a concrete derivation (or rigorous literature citation) or reframe it as a conjecture/working assumption not carrying the force of a closure. Mark clearly which closures rely on theorem-level arguments vs. power counting vs. phenomenological priors.

P1A-M3
Sec. IX.L, Eq. (20) (page 13)
Problem: “Vacuum Amplification Ceiling” ΩGW|bounce ≲ (ρcrit/ρPl)^2 ≃ 0.07–0.17 is asserted with no derivation and unclear physical basis. The square of the density ratio is not obviously the GW energy fraction ceiling.
Required fix: Provide a derivation from the stress–energy budget at the bounce (or from a well-defined effective theory of GW production near ρcrit), showing why the GW energy density fraction is bounded by this quantity. If this is only an order-of-magnitude heuristic, state it clearly and remove the numerical range.

P1A-M4
Sec. III.A (page 7–8), Sec. XII.B / XIII (pages 15–16)
Problem: Statements that the parity-odd structure is “qualitatively consistent with the observed isotropic birefringence” risk implying an explanation, despite the explicit admission that no photon–torsion coupling is derived. The paper later presents a spectator ALP as the mechanism. The juxtaposition could be misleading.
Required fix: Clarify that minimal ECH, as treated here, does not predict a CMB birefringence signal without additional non-minimal couplings; any β discussed arises from a spectator ALP that is not derived from ECH. Remove any phrasing that suggests ECH-explains-β.

P1A-M5
Sec. VII (page 11) and Table I (page 4)
Problem: fNL forecast significance “3–5σ realistic” is attributed to Heinrich et al. (2024) Fisher σ(fNL) ≈ 0.7, but the final significance band also folds in additional degradations (GR projection, bφ, photo-z) without showing the explicit combination. The paper states the detailed Fisher computation is “in preparation.”
Required fix: Either remove the numerical 3–5σ band from this manuscript or provide the explicit error-propagation steps (including GR projection and bias priors) that connect σ(fNL) ≈ 0.7 to the 3–5σ range.

P1A-M6
Sec. II.A.2 Step 4 (page 6)
Problem: The estimate “[(α/M) MPl] ∼ 10^−2” is asserted based on a schematic one-loop structure with a log and δNY counterterm, without specifying the UV completion, regulator, or renormalization scheme dependence that can strongly affect finite parts in torsionful theories. Shapiro & Teixeira [20] is cited but does not fix the finite part used here.
Required fix: Either provide a concrete example calculation (with regulator and subtraction scheme) showing how [(α/M) MPl] ~ 10^−2 arises, or relegate this to a purely phenomenological parameter with a prior range, avoiding the impression of a loop-derived estimate.

P1A-M7
Sec. XIV.D (page 17)
Problem: The “structural tension” between Ntot ≈ 92 and matter-bounce fNL uses a specific e^{32} scaling example and SPHEREx k-range. While the scaling is plausible, the argument should quantify the scale window of fNL survival more carefully (e.g., bounds on Ntot for which any SPHEREx k-modes remain superhorizon at exit).
Required fix: Either provide a short quantitative analysis showing the Ntot range for which the SPHEREx wavenumber band maps outside the inflationary subhorizon at bounce, or present this tension as qualitative.

MINOR

P1A-m1
Sec. II.A.1 (page 5), Eq. (1) and surrounding text
Problem: The TabcTabc/4 term is introduced “as a shorthand” after integrating out torsion. As written, in an action it looks like a bare kinetic/mass term for torsion; the sign and normalization are nonstandard in that context.
Required fix: Replace Eq. (1) with a strictly first-order (Cartan) form without a T^2 bare term, and then show the effective four-fermion action after eliminating torsion. Alternatively, explicitly label TabcTabc as “effective” and never as a part of the fundamental action.

P1A-m2
Notation (multiple pages)
Problem: Inconsistent use of R∧R̃, RR̃, “RRe,” and “Re(Γ)” for Pontryagin density; also J5μ alternates with J5
μ.
Required fix: Normalize notation: use RR̃ consistently for Pontryagin density; use J5μ uniformly.

P1A-m3
Sec. XII.A (page 15–16)
Problem: The phrase “the ε-correction-driven prefactor adjustment” appears without defining ε.
Required fix: Define ε or replace with a clear description (e.g., “order-one numerical factor from pre-exponential matching”).

NIT

P1A-n1
Typos and grammar (multiple pages)
- “Domaga la” -> “Domagała” (accents optional but use consistently).
- “RRe” -> “RR̃” (if intended).
- Several repeated phrases; tighten prose.

P1A-n2
Length vs. contribution
The paper is 21 pages and mixes a short, known perturbation-transparency theorem with an extensive, largely qualitative “barrier catalog” and programmatic discussion. After removing unpublished dependencies and reframing speculative barriers, the core could be presented more concisely.
Recommendation: ≤12 pages for the main paper. Move applied-program elements, catalogs, and non-essential discussions to appendices or a separate, published companion.

Traceability audit of abstract and conclusions scalars

- ρcrit/ρPl ≃ 0.27–0.41: Consistent with Eq. (9) and the stated γ values; numerically correct.
- fNL = −35/8: Standard matter-bounce result; appropriately cited [1].
- e^(Ntot−Nexit) at Ntot ≈ 92, Nexit ≈ 60 → e^32: Numerically correct (e^32 ≈ 7.9×10^13).
- βobs = 0.342° ± 0.094° and ACT 0.215° ± 0.074°: Numbers are consistent with cited works.
- “[(α/M) MPl] ∼ 10^−2”: Only heuristically motivated; no controlled derivation provided (see P1A-M6).
- H0 = 67.68 ± 1.06, ΔNeff ≈ 0: Traceability fails — these are internal, unpublished numbers (P1A-E1/E6).
- LiteBIRD “~9σ” detection vs. “0.73σ” difference to current central value: The paper correctly distinguishes different nulls (β ≠ 0 vs. model discrimination), which is good practice.

Bibliography spot-check
Key citations are generally appropriate. However, several items are arXiv-only “in preparation” and cannot be used as sources for quantitative claims (see P1A-E1). Ensure arXiv IDs, years, and journals are correct when those works are published.

## Summary recommendation
REJECT

Given the extensive reliance on unpublished companion analyses for core numerical claims; the presence of dimensionally inconsistent operators underpinning Route-2 and the DE-scaling ansatz; the lack of derivations for several “barriers” presented as closures; and pervasive draft-stage/internal-provenance language throughout, the manuscript does not meet PRD’s standards for methodological rigor and self-contained presentation. A substantially reworked submission would need to (i) remove or replace all unpublished dependencies, (ii) present dimensionally consistent EFT operators and unique amplitude bounds, (iii) supply full derivations or recast speculative “barriers” as hypotheses, and (iv) streamline to a concise, self-contained paper.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW ADDITIONAL FINDINGS AFTER SECOND-PASS AUDIT (A–J checklist)

ESSENTIAL

P1A-E9
Planck vs. reduced-Planck mass ambiguity and Λ–ρ mapping inconsistencies
Where: Sec. II.C (Eq. 10), Appendix B, throughout “MPl”
Issue: The paper mixes Λ and ρΛ without fixing whether MPl denotes the unreduced Planck mass (G−1/2) or the reduced Planck mass M̄Pl = (8πG)−1/2. In natural units ρΛ = Λ M̄Pl^2, not Λ MPl^2. Multiple places assert ρΛ = Ξ MPl^4 (Appendix B, Sec. II.C) and also write Λeff = Ξ MPl^2 (Eq. 10) with no 8π reconciliation. This affects every place the “Ξ MPl^4” scaling is used, the Ntot bookkeeping, and Fig. 2’s vertical normalization.
Required fix: Define once and for all M̄Pl and MPl, state which one you use in each formula, and re-derive the Λ–ρΛ relations with correct 8π factors. Propagate the choice consistently through Eq. (10), Appendix B, Fig. 2, and any Ntot numbers that depend on ρΛ normalization.

P1A-E10
Numerical inconsistency in the one-loop prefactor estimate
Where: Sec. II.A.2 Step 4, Eq. (7), and the statement “[(α/M) MPl] ∼ 10−2”
Issue: With g^2/(32π^2) × γ × ln(Λ^2/μ^2) as written, even taking g ≈ e (e^2 ≈ 0.092), γ ≈ 0.27, and a generous ln ≲ O(10), one finds (α/M)MPl ≲ few × 10−4, not 10−2. Hitting 10−2 would require an implausibly large log O(10^2–10^3) or a different coupling. The δNY term is introduced but its finite part and dimensionality are not specified (see P1A-m6).
Required fix: Either provide a worked example (regularization, subtraction scheme, scales) that yields O(10−2) stably, or retract this as a loop estimate and treat (α/M) as a free phenomenological parameter with a clearly stated prior range.

P1A-E11
Contradictory γ-dependence of the axial–axial four-fermion term
Where: Sec. II.A.2 Eq. (4) vs. Sec. IV.A paragraph “Adding the Holst term … torsion-elimination map is independent of γ at the classical level”
Issue: Eq. (4) includes a γ^2/(γ^2+1) factor multiplying J5·J5, while the Route-1 closure later asserts the torsion-elimination map is independent of γ at the classical level. Moreover, in the standard minimal Holst+Dirac case the coefficient is typically ∝ 1/(1+γ^2) (with additional vector–axial pieces), not γ^2/(1+γ^2).
Required fix: Pick one consistent classical result, cite it, and use it everywhere. If you keep γ^2/(γ^2+1), provide the explicit derivation (or a citation) in the convention used in Eq. (1).

P1A-E12
Internal contradiction on ALP mass “naturalness”
Where: Sec. IV.D (pages 10–11) vs. Sec. XII.B (page 16)
Issue: Route-4 argues matching both βobs and ρΛ “requires tuning mθ ∼ H0,” i.e., reimporting the CC problem. Later, Sec. XII.B states “A spectator ALP with fa ∼ MPl, m ∼ H0 is consistent … without fine-tuning.” These statements are in direct tension.
Required fix: Unify the stance. If m ∼ H0 is considered tuned, say so consistently and explain in what sense the later ALP point is “consistent without fine-tuning,” or else qualify the latter as “phenomenologically consistent but not explained.”

P1A-E13
Symbol reuse for “M” creates cross-channel ambiguity
Where: Sec. II.A.2 (M = “LQG area-gap mass”), Sec. IV.D (gθγ ≡ α/M), and elsewhere
Issue: The same symbol M denotes (i) an LQG-derived “area-gap mass scale” and (ii) a generic heavy scale in the photon–ALP coupling gθγ. These are unrelated and conflated in several places.
Required fix: Use distinct symbols: e.g., MΔ for the area-gap mass, and MCS (or fθ ≡ 1/gθγ) for the Chern–Simons/ALP scale. Update all equations and text to end the ambiguity.

P1A-E14
Figure–text mismatch on “surviving prediction”
Where: Table I “Executive summary” and Fig. 1 caption vs. Sec. XIII/Sec. XV
Issue: Table I labels “Testable prediction? fNL = −35/8 (Paper II forecast). Yes, class-level.” The body later clarifies this is a matter-bounce-class prediction, not specific to ECH. Presenting it as the paper’s “surviving testable prediction” in the executive summary/figure overstates the ECH-specific content.
Required fix: In captions and summary tables, label fNL = −35/8 explicitly as “matter-bounce class; not ECH-specific” to match the body’s caveats.

MAJOR

P1A-M8
Nieh–Yan vs. Pontryagin and “θ” field confusion in Eq. (14)
Where: Sec. IV.B, Eq. (14) and surrounding text
Issue: The operator −(1/16π^2)(β(γ)/MPl) ∫√−g ∂μθ J5μ is introduced with “θ(x) is the Nieh–Yan pseudoscalar.” The Nieh–Yan density is a topological density built from torsion and tetrads; introducing a propagating “θ” field that is “Nieh–Yan” requires a specific topological extension and kinetic sector. None is given, and dimensional consistency (see E2 from your first report) was already problematic.
Required fix: Either (i) formulate a consistent EFT with a well-defined pseudoscalar θ (its origin, kinetic term, and normalization) and derive the operator with correct dimensions, or (ii) drop the “Nieh–Yan pseudoscalar” wording and treat θ as a generic axion-like field, with a clean mapping to known axion–fermion operators.

P1A-M9
Barrier 9 (“Liouville conservation”) asserted without a Hamiltonian proof
Where: Sec. IX.I
Issue: The claim that the bounce cannot select a late-time vacuum because “phase-space volume conservation prevents irreversible selection” requires a statement about the Hamiltonian structure of the effective LQC/ECH system and its measure through the bounce. No derivation or citation is provided.
Required fix: Provide a formal statement (and ref) of Liouville’s theorem in the effective LQC/ECH phase space used, including the time symmetry of the bounce map, or demote Barrier 9 to a hypothesis rather than a closure.

P1A-M10
Figure 2 conveys a dimensionally inconsistent “DE scaling” as if established
Where: Fig. 2 and caption; Appendix B
Issue: Fig. 2 annotates a “parity-odd vacuum energy (on-shell loop, Holst term)” path feeding ρvac ∼ [(α/M) MPl] MPl^4, despite Appendix B conceding the underlying operator is dimension +1 and not a controlled EFT term. The graphical presentation suggests a concrete derivation rather than a heuristic.
Required fix: Re-caption Fig. 2 to label this branch explicitly as a dimensional ansatz/illustration, not an EFT derivation. Alternatively, remove the figure or replace the middle branch with a dimension-4 operator and re-derive.

MINOR

P1A-m4
Inconsistent “scheme range ~ 0.020” for γ
Where: Sec. II.A.1, Eq. (2) paragraph; Table IV “(scheme range ∼0.020)”
Issue: The stated SU(2) and DLM values (0.274 vs. 0.2375) differ by ≈ 0.0365, not ≈ 0.020. If the “range” is meant as a half-spread, specify clearly; otherwise correct the number.
Required fix: State the actual spread (≈ 0.0365) or define precisely how “∼ 0.020” is computed (e.g., stdev across schemes, half-range, etc.).

P1A-m5
ALP birefringence normalization off by a factor-of-two and undefined coupling convention
Where: Sec. IV.D, Eq. (17)
Issue: For L ⊃ −(gθγ/4) θ F F̃, the small-angle rotation is β ≈ (gθγ/2) Δθ. Using ρθ ≈ ½ m^2 θ0^2 gives β ≈ gθγ √(ρθ/2)/m. The text’s β ≈ (α/M) √(2 ρθ/m^2) corresponds to β ≈ gθγ √(2ρθ)/m (missing a 1/2 in the standard convention). Since you fit order-of-unity numbers, this likely doesn’t change qualitative claims, but the convention must be explicit.
Required fix: Define gθγ and your β–θ relation; carry (or explicitly drop) the factor 1/2 consistently.

P1A-m6
Dimensional ambiguity of δNY in Eq. (7)
Where: Sec. II.A.2, Eq. (7)
Issue: δNY is added to a term with dimensions of 1/M. As written it looks dimensionless. If it is a finite, scheme-dependent counterterm, it should carry the same mass dimension as α/M.
Required fix: Clarify the dimensionality of δNY and write it as δNY/M or equivalent, with a brief note on its scheme dependence.

P1A-m7
Undefined symbols/units in Eq. (10)
Where: Sec. II.C, Eq. (10)
Issue: ω is introduced without defining its precise meaning (vorticity? rotation scalar?) and units; cω is not given units. Since Λeff has mass^2, cω must be dimensionless if ω is a rate.
Required fix: Define ω (e.g., cosmic vorticity scalar with units of H), specify cω’s units, and cite the observational bound used.

P1A-m8
Missing definition of prime notation in Eq. (21)
Where: Sec. X.C, Eq. (21)
Issue: h′′ij + 2H h′ij + k^2 hij = 0 uses primes without defining the time variable (η vs t). Given mixed use of H (conformal vs physical), this should be explicit.
Required fix: State “prime denotes derivative w.r.t. conformal time η; H = a′/a.”

NIT

P1A-n3
Unlabeled change of notation for RR̃
Where: Sec. X.D Eq. (23) and multiple places
Issue: The paper alternates between RR̃, R∧R̃, “RRe,” and “Re(Γ)” for the same topological density. While you flagged this once (P1A-m2), additional instances remain (e.g., Eq. 23 “Re(Γ)”).
Required fix: Standardize to RR̃ (Pontryagin density) everywhere; avoid “RRe” and “Re(Γ).”

P1A-n4
Uncited “Mcrit ≈ 10−3 M⊙” threshold
Where: Sec. II.A.3 “Parameter Naturalness”
Issue: This specific number is asserted without derivation or citation.
Required fix: Provide a reference/derivation or remove the sentence.

P1A-n5
Caption/body phrasing that could mislead on β
Where: Sec. III.A, Fig. 1 right column box “ALP β 0.27° spectator”
Issue: The body correctly says minimal ECH does not provide a photon–torsion coupling and β arises from a spectator ALP. The figure label should make “spectator, not ECH-derived” explicit to avoid misinterpretation.
Required fix: Change the box to “Spectator ALP β ≈ 0.27° (not ECH-derived).”

Explanation for why these are new
The items above focus on arithmetic re-checks (E10 loop prefactor size; E14 caption vs body), dimensional and normalization consistency (E9, m5–m7), figure/body alignment (M10, n5), cross-reference consistency within the Holst/EC sector (E11), and comparability/interpretation mismatches (E12, M9) that were not explicitly covered in the first review. They materially affect the paper’s internal consistency, quantitative claims, or clarity, and would be expected by PRD’s rigor standards.