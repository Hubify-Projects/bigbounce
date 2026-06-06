# P1A auto-2026-06-06_0004pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (8088 chars)
**Wall time**: 312.6s

---

Referee report on “Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter”

Scope of review
- Methodology rigor: statistics, derivation chains, dimensional analysis, internal arithmetic consistency, error propagation.
- I audited every equation, stated σ and p-value, and all load-bearing scalars in the abstract and conclusions for traceability to the body text.
- I verified dimensional consistency where possible and recomputed numerical estimates quoted in the text.

Overall assessment
The manuscript contains interesting conceptual material, but as a PRD methods paper it falls short on multiple essential fronts: core numerical claims rely on non-public “companion” works; key derivations (especially for Route-2 one-loop and the parity-odd operator) are internally inconsistent dimensionally; the abstract overstates what is shown; and there are numerous procedural/“version history” artifacts inappropriate for a PRD article. The central “perturbation-transparency” statement (torsion vanishes for canonical scalars and the Holst sector reduces to a Pontryagin boundary term) is standard in Einstein–Cartan/Holst and is not rigorously proven here beyond brief bullets. The paper should be refocused substantially and must be made self-contained.

Findings

ESSENTIAL

P1A-E1
- Location: Abstract (p. 1), Sec. IV.D (pp. 10–11), Sec. IV.E (p. 11)
- Problem: Contradictory claim about closure mechanism for Route 4. Abstract: “find that each fails at the amplitude level under stated assumptions.” Body text: “Route 4 … naturalness objection rather than amplitude no-go” and “closed … at the level of an explanatory deficit, not an amplitude exclusion.”
- Required fix: Make the abstract and conclusions consistent with the body. Either (a) demonstrate an amplitude-level no-go for R4 with a clear, reproducible bound, or (b) revise the abstract and all summary statements to state explicitly that R4 is not amplitude-closed, but is disfavored by a naturalness/tuning argument. Do not claim amplitude-level closure for all four routes.

P1A-E2
- Location: Throughout; e.g., Abstract (p. 1), Sec. I (pp. 3–5), Fig. 1 caption (p. 4), Secs. III, VI–VII, XII–XIII, Table IV (p. 20)
- Problem: Load-bearing numerical results, validation, and forecasts rely on non-public “companion” papers in preparation ([2], [6], [23], [46]). Examples include: MCMC posteriors (H0, ΔNeff, σ8), NaMaster validation, ALP parameter fits, galaxy-chirality nulls, SPHEREx fNL forecast significance, and PTA reanalysis. These values appear in the abstract, main text, and tables, but are not reproducible from the present manuscript or public data.
- Required fix: Remove all numerical results and validation claims that depend on non-public companion works, or incorporate full methods and results (including data, likelihoods, priors, convergence diagnostics, and code/chain availability) into this manuscript. Every scalar quoted in the abstract and conclusions must be computable from methods and data presented here or from published, citable sources.

P1A-E3
- Location: Sec. II.A.2 (pp. 5–6, Eq. 4), Sec. IV.A (p. 8–9, Eq. 13)
- Problem: Internal inconsistency regarding γ-dependence of the EC four-fermion contact term. Eq. (4) includes a Holst-dependent factor γ^2/(γ^2+1), while Sec. IV.A uses the standard γ-independent Hehl–Datta term and asserts Holst independence “at the classical level.”
- Required fix: State clearly the fermion coupling choice (minimal vs non-minimal). Provide a single, consistent derivation/citation for the four-fermion contact term used in Route 1, and use it consistently. If Eq. (4) is retained, justify its γ-dependence (with Mercuri or equivalent) and then propagate that form consistently into the Route-1 closure. If the standard Holst-independence applies (Nieh–Yan), remove the γ-dependent Eq. (4).

P1A-E4
- Location: Sec. IV.B (pp. 9–10), Eqs. (14)–(15)
- Problem: Route-2 one-loop operator and amplitude estimate are dimensionally and algebraically inconsistent. Eq. (14) posits an ad hoc operator with 1/MPl, but the field dimensions of θ and J5 are not specified. In Eq. (15), the algebra changes from a division by MPl(α/M)βobs in the first line to a product with M/MPl α βobs in the second line, reversing the dimensional structure. The derivation of Δθone-loop and its scaling with H0 is not shown, and the final 10−58–10−60 range is not reproducibly derived from a consistent expression.
- Required fix: Provide a consistent EFT operator with field dimensions explicitly stated (is θ dimensionless or canonically normalized?), derive the induced rotation angle Δθ (or β) step by step with correct units (choose reduced MPl consistently), and present a single, unambiguous formula leading to the numerical bound. Remove the contradictory algebra or correct it with a full derivation.

P1A-E5
- Location: Sec. IX.L (p. 13–14), Eq. (20)
- Problem: “Vacuum Amplification Ceiling” ΩGW^ECH|bounce ≲ (ρcrit/ρPl)^2 ≃ 0.07–0.17 is asserted without derivation. ΩGW is the present-day spectral density fraction, while (ρcrit/ρPl)^2 is a dimensionless square of bounce-era densities; the connection is unclear and likely dimensionally incorrect as a bound on the observable ΩGW today.
- Required fix: Either provide a proper derivation linking the bounce-era GW energy fraction to today’s ΩGW (including redshift, transfer functions, and spectral shape) or remove Eq. (20) and the associated barrier claim. As written it is not methodologically sound.

P1A-E6
- Location: Multiple places, e.g., Sec. X.G (p. 15: “supersedes the earlier synthetic-Gaussian-likelihood value … pre-real-KDE drafts”), Table III footnote (p. 16), Sec. V (p. 11), Sec. I (p. 5)
- Problem: Version-history/procedural language (“earlier drafts,” “frozen samples,” “this volume,” GPU pod settings, convergence in progress) appears in the body text. PRD does not permit draft history or operational notes in the scientific narrative.
- Required fix: Remove all version-history and operational/procedural notes from the manuscript text and tables. Replace any such statements with final, citable results or delete them if not essential.

P1A-E7
- Location: Sec. IV.D (pp. 10–11), Eq. (17)
- Problem: The mapping from β to ALP energy density uses β ≈ (α/M) Δθ with Δθ ≈ √(2ρθ)/mθ, implicitly assuming an O(1) field excursion between recombination and today. No derivation is given for this time integral nor for the regime (mass, Hubble friction) in which Δθ equals the amplitude. The overshoot/tuning conclusion for mθ ≠ H0 depends sensitively on this assumption.
- Required fix: Provide a derivation (or a standard reference) for the relation between β and ρθ that includes the time evolution of θ (under/overdamped regimes), and justify the use of Δθ ≈ amplitude in the relevant mass ranges. Otherwise, state the result as conditional on this assumption and remove quantitative overshoot claims.

P1A-E8
- Location: Data and Code Availability (p. 18), Sec. III–VII, Table IV (p. 20)
- Problem: Reproducibility mismatch. The GitHub link is provided, but the manuscript states that MCMC chains, ALP fits, and some validations are “in companion” works. Readers cannot reproduce the quoted numbers from this manuscript and the linked repo alone.
- Required fix: Either host all data and chains underpinning the numbers quoted here in the repository linked in this paper, with a documented run script, or remove those numbers from this manuscript.

P1A-E9
- Location: Sec. X (pp. 14–15), Abstract (p. 1), Conclusions (pp. 18–19)
- Problem: The “perturbation-transparency” result is presented as a theorem “at all orders” with a brief five-step sketch. No explicit perturbative expansion or variation is shown beyond stating S=0 ⇒ T=0. For a methods paper claiming a theorem, this is insufficient.
- Required fix: Provide a formal derivation: vary the full ECH action with canonical scalar matter to quadratic (and, if claiming all-orders, outline the inductive argument or cite a rigorous proof) showing that torsion vanishes and the Holst term reduces to a boundary term in the action, and that no parity-odd terms enter the scalar and tensor perturbation equations. Alternatively, limit the claim to linear/quadratic order and present the explicit calculation.

MAJOR

P1A-M1
- Location: Table III (p. 16), Sec. X.G (p. 15)
- Problem: Notation clash: γ denotes both the Barbero–Immirzi parameter and the PTA spectral index in the same paper. This is confusing.
- Required fix: Rename the PTA spectral index (e.g., γPTA or κ) and state this clearly in the text and tables.

P1A-M2
- Location: Sec. II.A.2–C (pp. 5–7), Appendix B (pp. 19–20)
- Problem: The leading parity-odd operator, Eq. (6), is acknowledged to be dimension-1 off shell; the mapping to ρΛ = Ξ MPl^4 is an on-shell ansatz. Yet much of the Ntot and dilution bookkeeping in Secs. II.C and XII relies on this. As presented, the EFT is inconsistent.
- Required fix: Either (a) present a consistent dimension-4 operator (e.g., supply the missing MPl^3 factor in the coupling and justify it from a controlled EFT) and redo the scaling, or (b) quarantine all Ntot-sensitivity claims explicitly as heuristic and remove any implication that they follow from a valid EFT. The paper should not mix EFT-level claims with an operator acknowledged to be dimensionally inconsistent.

P1A-M3
- Location: Sec. II.C.1 (pp. 6–7), “Reheating thermal-reset barrier”
- Problem: Claim that C/P-violating scattering at Treh drives ⟨J5μ⟩ → 0 faster than H is asserted without references or quantitative estimates (e.g., rates vs Hubble).
- Required fix: Provide references and/or an order-of-magnitude estimate for axial-current relaxation rates at relevant temperatures to support the claim that torsion “memory” is erased at/after reheating.

P1A-M4
- Location: Sec. IX (pp. 12–14), multiple “Barrier” statements
- Problem: Several barriers (e.g., Scale Separation, UV→IR Specificity, Decoupling Universality, Gravitational Democracy) are conceptual assertions with little or no quantitative support or formal statements. As a methods paper, these should be formulated as quantitative bounds or theorems where possible.
- Required fix: For each barrier that is essential to a no-go claim, either provide a quantitative bound with derivation, a theorem with proof, or soften the language and move to a discussion section as heuristic/qualitative insight.

P1A-M5
- Location: Sec. II.C, Eq. (10) (p. 6)
- Problem: Λeff = Ξ MPl^2 + cω ω^2 is introduced without specifying cω’s dimensions or giving a bound. The subsequent text uses only the observational bound on ω/H and declares rotation negligible; the role of cω is unclear.
- Required fix: Define cω (units, expected magnitude), or drop the ω^2 term if it is not used quantitatively.

P1A-M6
- Location: Table IV (p. 20), Sec. I (p. 5)
- Problem: The paper quotes H0 = 67.68 ± 1.06, ΔNeff ≈ 0, etc., as “verified” from an internal Cobaya MCMC but gives no methods or data to reproduce. Appearing in a parameter table gives these the weight of results.
- Required fix: Replace these with published values (e.g., Planck 2018) or include full MCMC methods and make the chains available in the present paper’s repository. Otherwise remove the table entries that are not used elsewhere.

P1A-M7
- Location: Sec. IV.D (pp. 10–11), LiteBIRD forecast statements
- Problem: Statements about LiteBIRD’s ability to distinguish β values and the calculation of 0.73σ are methodologically careful, but elsewhere the text also states a “∼ 9σ” detection in absolute terms. These are different null hypotheses and need to be clearly separated each time they appear.
- Required fix: In every place where a β significance appears, specify the null hypothesis (β = 0 vs β equal to the WMAP+Planck central value) and avoid juxtaposing them without that explicit qualifier.

MINOR

P1A-m1
- Location: Eq. (6) and (5) (p. 6)
- Problem: Notation F IJ[K, R˚] and eI ∧ eJ ∧ FIJ is introduced without definition of K or the precise content of FIJ. This obscures the construction.
- Required fix: Define all symbols the first time they appear, or replace with standard curvature/tetrad notation used in the Holst/Nieh–Yan literature.

P1A-m2
- Location: Throughout
- Problem: MPl vs reduced M̄Pl is not specified; the ratio H0/MPl ≈ 10−61 implicitly assumes reduced MPl. In other places, “MPl” seems to be the unreduced value.
- Required fix: Declare at the start of the paper whether MPl is reduced or unreduced, and use it consistently throughout.

P1A-m3
- Location: Sec. II.B (p. 6)
- Problem: The ρcrit formula is presented with caveats about scheme-dependence. The numerical window 0.27–0.41 ρPl is consistent with the formula; however the text mixes “quoted” and “internal extrapolation” phrasing.
- Required fix: Streamline this paragraph: present the formula once, evaluate at the two schemes to yield the range, and cite Ashtekar & Singh for 0.41. Avoid “internal extrapolation” language.

P1A-m4
- Location: Sec. X.D (p. 14), Eq. (23)
- Problem: Typo/notation: “Re(˚Γ) = (1/2) ε R = 1/2 ∗R R ≡ ∂μKμ.” The first equality as written is unclear (“ε R”).
- Required fix: Replace with a standard, unambiguous expression for the Pontryagin density: P ≡ (1/2) εμνρσ Rμνab Rρσab = ∂μ Kμ.

P1A-m5
- Location: Multiple places
- Problem: Occasional typographical/encoding issues (e.g., Poincar´e, Domaga la, Jackiw–Pi), repeated “RRe,” odd hyphenation.
- Required fix: Run a thorough copy-edit to fix diacritics, hyphenation, and repeated character artifacts.

NIT

P1A-n1
- Location: Table I and Table III (pp. 4, 16)
- Problem: Captions are verbose and mix methodology with future work logistics.
- Required fix: Shorten captions to describe only what is in the table and move programmatic statements to the text.

P1A-n2
- Location: Acknowledgments (p. 18)
- Problem: AI assistant usage is acknowledged. PRD typically allows acknowledgments, but consider ensuring the phrasing aligns with the journal’s policy and avoids implying co-authorship.

Length and scope
The manuscript is overly long for what is actually supported within it (21 pages). If refocused on the perturbation-transparency result and a clean, self-contained closure of Routes 1–3 with rigorous derivations, the paper could be 12–14 pages. All MCMC, galaxy-chirality, and PTA reanalysis material should either be removed or fully incorporated as reproducible analyses. Route 4 should be clearly repositioned as a naturalness argument unless an amplitude no-go is proven.

Bibliography and citations
- Spot-checks of a few citations (e.g., Planck 2018, Holst 1996, LQC review) are consistent. Several references are “in preparation” and not acceptable as supports for quantitative claims made here. Replace with published sources or remove dependent claims.

Arithmetic checks
- ρcrit(γ=0.2375) ≈ 0.41 ρPl and ρcrit(γ=0.274) ≈ 0.27 ρPl are consistent with the stated formula.
- Ntot needed for e−3Ntot ∼ 10−121–10−122 is Ntot ≃ 93–94, consistent with the text.
- β mapping for mθ = H0 and α/M = 10−21 GeV−1 yields ρθ of order 10−11 eV^4, numerically comparable to ρΛ; this check passes as an order-of-magnitude estimate.
- The LiteBIRD differential significance 0.072°/√(0.03^2+0.094^2) ≈ 0.73σ is correct.

However, the Route-2 ratio in Eq. (15) is not reproducible from a single coherent formula, as noted in P1A-E4.

## Summary recommendation
REJECT

The manuscript, as submitted, does not meet PRD methodological standards. Core claims rely on non-public companion works; the Route-2 derivation is internally inconsistent; the abstract overstates the amplitude-level closure (conflicting with the body for Route 4); and the “perturbation-transparency theorem” is not rigorously demonstrated beyond a brief sketch of known results. To be reconsidered, the paper must be made self-contained, remove non-public dependencies, present consistent EFT operators and derivations with correct dimensions, provide a rigorous proof (or scoped claim) for the transparency result, and excise all version-history and operational content. A substantially shorter, tightly focused manuscript could be viable after these essential corrections.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS AFTER FRESH-AUDIT

I focused on the ten “often-missed” classes (A–J). Below are only NEW issues not listed in my initial report.

ESSENTIAL

P1A-E10
- Location: Sec. II.C Eq. (10), Appendix B (pp. 19–20), Fig. 2 label
- Problem: Inconsistent use of Ξ between Λ and ρ. Eq. (10) defines Λeff = Ξ MPl^2 (Ξ dimensionless). Elsewhere the paper maps the vacuum energy density as ρΛ = Ξ MPl^4 with the same Ξ symbol (Appendix B, Fig. 2, Sec. XII). These two uses differ by MPl^2 and cannot both be correct.
- Required fix: Choose one convention and use it consistently. If Ξ parametrizes Λ (mass^2), then ρΛ = (MPl^2/8π) Λ implies a different numerical Ξ. If Ξ parametrizes ρΛ directly, remove Eq. (10) or redefine there.

P1A-E11
- Location: Sec. IV.D (p. 10–11), paragraph defining Kμ
- Problem: Wrong normalization for the Chern–Simons current divergence. The text states ∂μKμ = 1/2 F̃μν Fμν. With the definition Kμ ≡ εμναβ Aν Fαβ, the correct identity is ∂μKμ = F̃μν Fμν (no 1/2). This factor-of-two error propagates into the birefringence mapping.
- Required fix: Fix the normalization consistently: either (i) keep Kμ ≡ εμναβ Aν Fαβ and use ∂μKμ = F̃F, or (ii) define Kμ with a 1/2 and keep ∂μKμ = F̃F.

P1A-E12
- Location: Sec. IV.B (pp. 9–10), Eqs. (14)–(15) and surrounding text
- Problem: Channel mismatch: the Route-2 operator given, ∝ (1/MPl) ∂μθ J5μ, couples a Nieh–Yan pseudoscalar to the axial fermion current; it does not couple to photons. Yet the text proceeds to constrain it using cosmic birefringence β (a photon-sector observable) without an intermediate, derived link to F̃F. As written, the comparison to β is conceptually unsupported.
- Required fix: Either (a) derive the radiative or anomaly-induced mapping from ∂μθ J5μ to an effective θFF̃ with a controlled coefficient and then compute β, or (b) refrain from using β to bound Route 2.

P1A-E13
- Location: Sec. II.A.2 Step 4, Eq. (7)
- Problem: Dimensional inconsistency and undefined symbols. The RHS adds g^2/(32π^2) (γ/M) ln(Λ^2/μ^2) (dimension −1) to δNY (dimensionless), but both terms are added to match α/M (dimension −1). δNY must carry the same mass dimension or be factored accordingly. Also, g, ΛUV, μ, and δNY are not defined.
- Required fix: Specify the EFT matching: define g, ΛUV, μ, and δNY, and write α/M = [dimensionless]×(1/M) consistently. Remove the dimensionless-plus-dimensionful sum.

P1A-E14
- Location: Sec. IV.D (p. 10–11), Eq. (17)
- Problem: Missing factor of 1/2 in the β–axion relation. For L ⊃ −(1/4)(α/M) θ F̃F, the polarization rotation is β = (α/2M) Δθ (standard result). The manuscript uses β = (α/M) Δθ. This factor-of-two error biases the subsequent ρθ estimates.
- Required fix: Correct to β = (α/2M) Δθ and update the numerical statements (overshoot factors are unchanged at the order-of-magnitude level but the exact mapping is wrong).

MAJOR

P1A-M8
- Location: Eq. (1), Sec. II.A.1
- Problem: Possible double counting and sign risk for torsion. The action explicitly includes +(1/4) TabcTabc while also stating that this is “a shorthand for the four-fermion contact interaction obtained after integrating out torsion.” In EC theory, the T^2 structure emerges after eliminating torsion; inserting it ab initio risks double counting and sign inconsistencies relative to the Hehl–Datta effective term.
- Required fix: Present the fundamental first-order action without an explicit T^2 piece, then show the torsion elimination that yields the four-fermion operator; or justify the T^2 term from a well-defined PGT Lagrangian with clear conventions so no double counting occurs.

P1A-M9
- Location: Sec. IX.A (Barrier 1), Eq. (18)
- Problem: Undefined quantity and unsubstantiated scaling. geff ∼ 1/(MPl p|t3|) ∼ H0/MPl is stated without defining p|t3| or deriving the relation. As written, Eq. (18) is opaque.
- Required fix: Define t3 (torsion mass parameter?), derive geff in a propagating torsion model, and justify the H0/MPl scaling numerically.

P1A-M10
- Location: Multiple (citations [6], [23], [46], and [47])
- Problem: Unacceptable reliance on unpublished or unavailable references, including one “available upon request.” This goes beyond my earlier P1A-E2 by noting [47] explicitly offers no public record.
- Required fix: Remove all quantitative claims dependent on these sources or replace them with peer-reviewed, publicly available references; do not cite private notes “upon request” for quantitative support.

MINOR

P1A-m6
- Location: Sec. II.A.2, Eq. (7)
- Problem: Undefined symbols g, ΛUV, μ, δNY used in a load-bearing estimate.
- Required fix: Define each symbol where first used and specify their expected magnitudes/ranges.

P1A-m7
- Location: Secs. XII and Appendix B
- Problem: Stale/inconsistent Ntot values. The body frequently quotes Ntot ≈ 92 while Appendix B’s first-principles CC hierarchy gives Ntot ≈ 94. While the paper notes a ∼2% offset, the two values appear without a single canonical choice.
- Required fix: Choose one representative value and state the systematic associated with the ansatz; use that consistently throughout.

P1A-m8
- Location: Eq. (12) vs text
- Problem: Units inconsistency for β. Eq. (12) requires β in radians while the manuscript elsewhere uses degrees (e.g., 0.27°). This can confuse readers applying Eq. (12).
- Required fix: State explicitly that β in Eq. (12) is in radians and convert consistently when quoting numbers.

P1A-m9
- Location: Sec. X.C–D, Eq. (23)
- Problem: Notation/normalization issues around Pontryagin density and Chern–Simons current. Beyond the earlier typo (addressed in my first review), Kμ normalization is not fixed consistently with ∂μKμ.
- Required fix: Present a single, standard definition P ≡ (1/2) εμνρσ Rμνab Rρσab = ∂μKμ and define Kμ once with the matching normalization.

P1A-m10
- Location: Sec. XII, Eq. (24)
- Problem: Angle brackets in Ξ ≡ ⟨(α/M) MPl⟩ Dinf are not defined (ensemble average? running average?).
- Required fix: Define the averaging operation or drop the brackets.

P1A-m11
- Location: Sec. II.A.3
- Problem: Unsupported threshold claim “parent black hole mass must exceed Mcrit ≈ 10−3 M⊙.” No citation or derivation provided.
- Required fix: Add a reference and one-line derivation, or remove the threshold statement.

P1A-m12
- Location: Sec. II.C.1 (“contorsion dilutes as a−3” paragraph)
- Problem: Confusing phrasing “the cube of the fermion bilinear scales as the cube of the fermion number density.” The source is a bilinear; no cubic dependence is relevant at this stage.
- Required fix: Rephrase to “the axial current J5 ∝ nψ scales as a−3” to avoid implying higher powers.

P1A-m13
- Location: Eq. (21)
- Problem: Primes not defined (conformal vs cosmic time).
- Required fix: State explicitly that primes denote derivatives with respect to conformal time.

P1A-m14
- Location: Sec. II.C.1 first paragraph (inflationary suppression)
- Problem: “∼50 e-folds of inflation” cited for rotation dilution sits alongside Ntot ≈ 92 elsewhere; the two are used for different purposes but this can read as inconsistent.
- Required fix: Clarify that the 50 e-fold figure pertains only to diluting any inherited macroscopic rotation, not to the dark-energy scaling argument.

NIT

P1A-n3
- Location: Sec. IV.D (p. 10–11)
- Problem: Parenthetical “all indices are fully contracted” is superfluous, while the actual normalization error on ∂μKμ is not addressed there.
- Required fix: Remove the aside and correct the normalization (see P1A-E11).

Explanation
I recomputed all explicit ratios, checked unit normalizations in every displayed equation tied to an observable, and compared symbol usage across sections and appendices. The biggest additional issues are (i) the inconsistent use of Ξ for Λ vs ρ (P1A-E10), (ii) the conceptual mismatch of using a θ–J5 operator to constrain birefringence (P1A-E12), and (iii) normalization/dimensional problems in the Chern–Simons and axion–photon sector (P1A-E11, P1A-E14, P1A-E13). These materially affect claims and must be fixed alongside the essential problems noted in my initial review.