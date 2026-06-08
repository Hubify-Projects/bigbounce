# P1A auto-2026-06-08_1520pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7498 chars)
**Wall time**: 236.6s

---

Referee report on “Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter”

Overall assessment
The manuscript proposes a “channel-level” no-go for four specific dark-energy routes in minimal Einstein–Cartan–Holst (ECH) gravity and states a “perturbation-transparency” result for canonical scalars. While several qualitative points are plausible (e.g., axial–axial four-fermion being parity-even; Holst term reducing to a boundary term on a torsion-free connection), the paper does not meet Physical Review D standards for methodological rigor or self-contained verifiability. Core numerical claims and multiple load-bearing assertions rely on “companion papers” in preparation; several equations contain dimensional inconsistencies; one key numerical comparison is incorrect by ~30%; and version-history/internal-run content appears in the text. Many “barriers” are stated without derivations or quantitative bounds. The submission must be substantially revised.

Below I itemize findings with severity levels and required fixes.

ESSENTIAL findings

P1A-E1
- Location: Sec. II A 2, Eq. (5) and (6), page 6
- Problem: Undefined and inconsistent operator. The phenomenological parity-odd term Seff = (α/M) ∫ eI∧eJ∧FIJ[K, R̊] is introduced without precise definition of FIJ[K, R̊] (which field strength, what is K, what is R̊, how are indices contracted, what is the background structure?).
- Required fix: Provide a precise, covariant definition of the operator, with indices and differential forms fully specified, including whether F is a curvature 2-form built from the contorsion K or the Levi-Civita curvature R̊, and the exact contraction used (e.g., εIJKL eI∧eJ∧F KL). State its symmetry and mass-dimension unambiguously, including the convention for α/M. If it is an ansatz, make this an explicit “Definition/Assumption” box with a consistent dimensional count.

P1A-E2
- Location: Sec. IV B, Eq. (14), page 9–10
- Problem: Dimensional inconsistency in the one-loop parity-odd effective action. The operator Γone-loop ⊃ −(1/16π^2) β(γ) MPl ∫ √−g ∂μθ J5μ has incorrect mass dimension: ∂θ has dimension 1, J5 has dimension 3, giving 4 in the integrand; multiplying by MPl makes the coefficient dimensionful, which is not consistent with a local dimension-4 operator in the action density. Later text claims suppression by M−1
Pl, contradicting Eq. (14).
- Required fix: Correct the coefficient so that the total integrand has mass dimension 4. If θ is dimensionless (typical for a pseudoscalar angle), the coefficient must be dimensionless. If θ has mass dimension 1, adjust and justify. Then re-derive Eq. (15) consistently and remove the “alternative ordering” that yields ∼10−33 (see P1A-E3).

P1A-E3
- Location: Sec. IV B, Eq. (15), page 9–10
- Problem: Ambiguous dimensional bookkeeping leading to two wildly different answers. The text presents ∆θone-loop/∆θobs ∼ 10−58–10−60 but also says “an alternative ordering … yields a numerically distinct ∼ 10−33 ratio.” These cannot both be valid if the coefficient is fixed dimensionally.
- Required fix: After fixing Eq. (14), derive a single, dimensionally consistent expression for ∆θone-loop/∆θobs, showing all steps. Remove the “alternative ordering” and present one consistent value with clear unit conversions. If you retain order-of-magnitude only, quantify assumptions explicitly.

P1A-E4
- Location: Sec. IV D, page 10
- Problem: Incorrect “consistency within ~1.4σ” between WMAP+Planck β = 0.342° ± 0.094° and ACT DR6 β = 0.215° ± 0.074°. The difference is 0.127°. Combined σ = sqrt(0.094^2 + 0.074^2) = 0.1196°. The tension is 0.127/0.1196 ≈ 1.06σ, not ~1.4σ.
- Required fix: Correct the tension to 1.06σ (or 1.1σ), and ensure all such cross-experiment comparisons are recomputed and consistent throughout.

P1A-E5
- Location: Throughout (Abstract; Sec. I, III, V–VII, XIII–XV, Tables I, III, IV)
- Problem: Reliance on “companion papers” and unpublished analyses (in preparation) for load-bearing claims: MCMC posteriors (H0, ΔNeff, σ8), Galaxy spin null results, Fisher forecasts (σ(fNL)), NaMaster validation, PTA KDE analysis, and more. The present paper cannot be verified independently, and PRD generally does not accept reliance on unpublished “in preparation” for core results.
- Required fix: Either (a) remove all conclusions that depend on companion/in-preparation works and present only what is fully derived in this manuscript, or (b) fully include the necessary methodological components, datasets, priors, chains, diagnostics, and code within this submission (or stable repositories) so that results are reproducible without the companion manuscripts. At minimum, any quoted posterior numbers must be traceable to methods and data described here.

P1A-E6
- Location: Appendix B, last paragraph, page 19
- Problem: Version-history/internal-draft language in the paper body: “not the ∼ 35 misstated in earlier drafts.” Similar “supersedes earlier synthetic-Gaussian-likelihood value …” in Sec. X G (page 15–16) and progress/status text in Table III footnote.
- Required fix: Remove all version-history and internal status language from the paper. PRD does not allow draft-history commentary in the body.

P1A-E7
- Location: Sec. II A 1, Eq. (1), page 5
- Problem: Action includes + (1/4) Tabc Tabc term inside the same 1/(16πG) overall factor, labeled later as “a shorthand” for the four-fermion contact after integrating out torsion. As written, it is not a faithful starting action and risks double-counting, and its normalization/dimension is unclear (T^2 has mass-dimension 2; the overall 1/G prefactor gives dimension 4, but then the separate non-minimal matter term is still mentioned).
- Required fix: Replace Eq. (1) with the standard first-order Palatini–Cartan–Holst action, clearly stating that torsion is non-propagating and will be integrated out; then derive the four-fermion operator and its coefficient. If a T^2 term is retained, provide a rigorous derivation and show it is not double-counting the induced contact term; otherwise remove it.

P1A-E8
- Location: “Barriers” (Sec. IX, Table II), pages 12–14
- Problem: Several barriers are asserted without derivation or quantitative statements (e.g., Barrier 1 “Mass-Coupling Lock,” Barrier 2 “Topological-Shift Duality,” Barrier 6 “Attractor-Sensitivity Dilemma,” Barrier 9 “Liouville Conservation,” Barrier 10–11). The paper’s main claim (“closure by 14 constraints”) requires that each barrier be well-defined, with hypotheses, derivation or theorem statements, and clear applicability conditions.
- Required fix: For each barrier, provide either a formal derivation (with equations and references), a theorem-style statement with proof, or soften the claim to a “conjecture/heuristic” with appropriate caveats. For Barrier 1, define t3 and show how geff ∼ H0/MPl follows. For Barrier 2, state the duality precisely and prove it or cite a specific derivation. For Barrier 6 and 9, provide dynamical-system or Liouville-theorem arguments linked to the specific ECH system.

P1A-E9
- Location: Sec. III B and V, pages 8 and 11
- Problem: “Galaxy spin asymmetry: a confirmed null” relies entirely on Paper IV [23] “in preparation” and not demonstrated here. Yet statements like “refutes Shamir’s claimed 3% asymmetry at high significance” are not reproducible.
- Required fix: Either remove these claims or provide the full dataset description, classifier architecture, validation tests, bias audits, and statistical pipeline in this paper (or as an appendix/Supplement), including dipole estimators, masks, and look-elsewhere corrections.

P1A-E10
- Location: Sec. III A and IV D (Eq. 17), pages 8 and 10
- Problem: The mapping between the ALP–photon coupling normalization and the rotation angle β is not fixed. In Eq. (12) small-angle EB relation is quoted, but Eq. (17) β ≈ (α/M) Δθrec→today ∼ (α/M) √(2ρθ/mθ^2) is used without clarifying whether the conventional factor 1/2 is present for L ⊃ −(gϕγ/4) ϕ F F̃. This normalization controls the fitted α/M ≈ 10−21 GeV−1.
- Required fix: Specify the exact photon–ALP Chern–Simons normalization and derive the line-of-sight rotation angle with all factors, then recompute the implied α/M from βobs. Quote one convention and stick to it; otherwise the inferred α/M is ambiguous by O(2), affecting several conclusions.

MAJOR findings

P1A-M1
- Location: Abstract, Sec. I, XII A, Appendix B, pages 1–3, 15–16, 19
- Problem: The “Ntot ≈ 92” e-fold requirement is repeatedly quoted but depends on an explicit on-shell scaling ansatz for a dimensionally inconsistent operator (Appendix B admits [Lodd]=+1). While the text acknowledges this as an ansatz, the quantitative headline “92” is presented without displaying the exact algebra from Ξ ≈ 10−123 and the assumed [(α/M) MPl] ≈ 10−2.
- Required fix: Provide an explicit one-line calculation showing Dinf ≈ 10−121 and Ntot ≈ (ln 10) × 121 / 3 ≈ 93.1, and explain the difference between 92 and 94 that appears later. State numerical inputs and uncertainties clearly (e.g., α/M choice, Treh/MGUT exponent, etc.).

P1A-M2
- Location: Sec. II C 1 (“Reheating thermal reset”), pages 6–7
- Problem: The claim that C/P-violating scattering rates at reheating erase coherent axial currents “exceed the Hubble rate” is plausible but entirely qualitative. No rates, cross sections, or references are given.
- Required fix: Provide an order-of-magnitude calculation or literature citation for the relevant SM (or BSM) processes that relax axial charge, including ΓCP(Treh) and compare to H(Treh), to substantiate the erasure argument.

P1A-M3
- Location: Sec. X (“Perturbation-Transparency Result”), pages 14–15
- Problem: While the scalar-sector argument is standard (S=0 ⇒ T=0 ⇒ Holst term becomes Pontryagin density, a boundary term), the statement “at all perturbation orders” is correct only for the decoupling from the EOM, but boundary contributions can be non-vanishing on nontrivial topologies. The text is casual about this subtlety.
- Required fix: Add a short paragraph acknowledging that while the Pontryagin density is a total derivative and does not affect local equations of motion, it can contribute boundary/topological terms; clarify the boundary conditions/topology assumed in the cosmological application.

P1A-M4
- Location: Sec. IV A, Eq. (13), page 8–9
- Problem: Parity classification of the axial–axial term is stated but not demonstrated. While correct (pseudovector squared is parity even), given the centrality, show a one-line parity check or cite a standard source.
- Required fix: Add a footnote or appendix line explicitly showing that J5μ J5μ is parity even.

P1A-M5
- Location: Sec. II C, Eq. (10), page 6
- Problem: Λeff = Ξ MPl^2 + cω ω^2 is introduced; however, Ξ is defined via a bracket average ⟨(α/M) MPl⟩ Dinf without specifying the averaging procedure. It is unclear how stochasticity, time evolution, or renormalization affects Ξ.
- Required fix: Either remove the bracket or define what is averaged (e.g., spacetime average at reheating, ensemble average), and explain why this is legitimate in a late-time cosmological constant term.

P1A-M6
- Location: Sec. IX L (Barrier 12), Eq. (20), page 13
- Problem: The bound ΩGW|bounce ≲ (ρcrit/ρPl)^2 is quoted without a derivation. While numerically consistent (0.27^2–0.41^2), the physical reasoning for a squared fraction cap on GW energy density from the bounce epoch is not shown.
- Required fix: Provide a clear derivation or a cited reference justifying this bound, or rephrase as a heuristic estimate.

P1A-M7
- Location: Bibliography and in-text citations throughout
- Problem: Several citations are to “in preparation” works by the author [2, 6, 23, 46, 47] and one 2025+ ACT DR6 preprint [5] with a future-stamped arXiv ID. PRD allows arXiv citations but not “in preparation” for central results.
- Required fix: Replace “in preparation” references by arXiv-posted manuscripts or remove claims that depend on them.

MINOR findings

P1A-m1
- Location: Sec. II B, Eq. (9), page 6
- Problem: The formula for ρcrit with Δ = 4√3 π γ ℓP^2 is correct and reproduces 0.41 (γ=0.2375) and 0.27 (γ=0.274). However, the text suggests using γSU(2) in a formula originally quoted for γDLM; clarify that this is a scheme-dependent extrapolation, not a published LQC result for that γ.
- Required fix: Add a sentence clarifying that inserting γSU(2) into the standard LQC expression is an internal extrapolation, as you partly note.

P1A-m2
- Location: Sec. II C 2, page 7
- Problem: “Parent black hole mass must exceed Mcrit ≈ 10−3 M⊙” is stated without citation or derivation.
- Required fix: Provide a reference or derivation, or remove.

P1A-m3
- Location: Sec. IV D, Eq. (17), page 10
- Problem: Units and normalization of α/M as “GeV−1” are used; ensure that elsewhere you do not switch to other conventions (e.g., gϕγ) without mapping.
- Required fix: Add a brief mapping between α/M and the conventional axion–photon coupling gϕγ and confirm the numerical translation.

P1A-m4
- Location: Table I (page 4), Table III (page 16), Table IV (page 20)
- Problem: Tables include claims outside the scope of the present paper (e.g., “SPHEREx forecast,” “PTA KDE,” MCMC posterior values). These are not reproducible here.
- Required fix: Either remove these entries or clearly label them as external context not used in any inference here, and avoid presenting numerical values (posteriors, σ) not derived in the paper.

NIT findings

P1A-n1
- Location: Acknowledgments, page 18
- Problem: “We acknowledge the use of Claude (Anthropic) as an AI research assistant…” is unusual for PRD.
- Required fix: Consider removing or moving to a short neutral acknowledgment (e.g., “LLM-assisted drafting was used; all results were independently verified by the author”).

P1A-n2
- Location: General
- Problem: Repetitive “channel-level closure” phrasing and overlong narrative. The manuscript could be more concise.
- Required fix: Consider condensing to ≤ 12–14 pages by moving catalog/roadmap prose to appendices and focusing on the core derivations (torsion elimination, Holst boundary term, each route’s quantitative amplitude cap).

P1A-n3
- Location: Sec. X C–D, page 14
- Problem: The notation vR, vL, ∆v defined but not used further.
- Required fix: Either remove or add a sentence explaining that ∆v=0 implies no GW chirality or TB/EB.

Audit of abstract/conclusions scalars
- “ρcrit ≃ 0.27–0.41 ρPl”: traceable to Eq. (9). OK.
- “Ntot ≈ 92”: only as ansatz-dependent; must show explicit algebra (P1A-M1).
- “fNL = −35/8”: cited as class-level from Cai et al. (2009). OK, but not derived here.
- “βobs = 0.342° ± 0.094°; ACT 0.215° ± 0.074°”: values OK, but 1.4σ consistency is wrong (P1A-E4).
- “[(α/M) MPl] ∼ 10−2”: relies on α/M fitted to β; requires normalization clarity (P1A-E10).
- “ΩGW bound 0.07–0.17”: numerically consistent with (ρcrit/ρPl)^2 but needs derivation (P1A-M6).

Figure/table audit
- Fig. 1 is schematic; acceptable.
- Table I mixes results, forecasts, and “phenomenology” with footnotes pointing to in-prep works; must be harmonized or trimmed (P1A-m4).
- Table II (barriers) is fine as a roadmap but needs each entry to be supported by formal arguments (P1A-E8).
- Table III and IV contain non-reproducible numbers here; see P1A-m4.

Bibliography audit
- Many standard references are correct. However, several core claims depend on [2, 6, 23, 46, 47], which are “in preparation.” Replace by stable arXiv postings or excise dependent claims (P1A-M7).
- The ACT DR6 reference [5] uses a future year and arXiv number; acceptable if on arXiv at submission, but not load-bearing.

Recommended maximum length
The current 21-page manuscript is verbose given the actual derivations presented. After removing companion-paper content and focusing on rigorous derivations, a 12–14 page manuscript should suffice.

Summary recommendation
REJECT

The manuscript contains multiple essential methodological issues: undefined/incorrectly dimensioned operators, conflicting magnitude estimates for the same observable, a miscomputed cross-experiment consistency, heavy reliance on unpublished “companion” works for load-bearing claims, and inclusion of version-history/internal status text. While the central qualitative “perturbation-transparency” statement is plausible and potentially publishable, the paper in its current form does not meet PRD’s standards for self-contained rigor and reproducibility. I encourage the author to produce a shorter, fully self-contained paper that (i) rigorously defines the operators; (ii) proves the transparency result carefully; (iii) presents each closure route with consistent dimensional analysis and single-valued amplitude estimates; and (iv) removes all reliance on in-preparation work.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (second-pass audit)

Below are new issues not listed in my initial report, organized with the same severity tags and numbering continued from the prior review.

ESSENTIAL

P1A-E11
- Location: Sec. II C Eq. (10), Fig. 2 caption, Appendix B, and multiple passages using ρΛ versus Λ
- Problem: Inconsistent Λ–ρΛ mapping and missing 8π factors. The paper alternates between Λeff = Ξ MPl^2 (Eq. 10) and ρΛ = Ξ MPl^4 (Fig. 2 caption, Appendix B, and elsewhere) as if Ξ controls both with the same normalization. In GR, ρΛ = Λ MPl^2/(8π) (up to convention). Treating Ξ ≈ 10−123 as simultaneously setting Λ/MPl^2 and ρΛ/MPl^4 without an 8π (or stated convention) is inconsistent.
- Required fix: Choose a convention and stick to it. Explicitly state whether Ξ parameterizes Λ (dimension 2) or ρΛ (dimension 4). If Λeff = Ξ MPl^2, then ρΛ = Ξ MPl^4/(8π) in that convention. Propagate this consistently through Fig. 2, Sec. XII A, and Appendix B.

P1A-E12
- Location: Sec. II A 2 (Eq. 4) vs. Sec. IV A (Eq. 13) and discussion around Route 1
- Problem: Conflicting γ-dependence of the torsion-induced axial–axial four-fermion term. Eq. (4) includes the Holst factor γ^2/(γ^2+1), but Eq. (13) (and the discussion closing Route 1) uses the γ-independent Hehl–Datta coefficient −3κ/16 J5·J5 and asserts that “the torsion-elimination map is independent of γ at the classical level.” Both can’t hold simultaneously under the same coupling assumptions.
- Required fix: State precisely which fermion coupling is assumed (minimal vs. the standard Holst-extended Dirac action) and derive the four-fermion term once. If γ^2/(γ^2+1) appears, carry it consistently into Route 1. If one argues for γ-independence, remove the factor from Eq. (4) and cite the result used.

P1A-E13
- Location: Sec. II C 1 (“Reheating thermal-reset barrier”), page 7
- Problem: Dimensional inconsistency in the stated r.m.s. scaling for the axial current: “r.m.s. residual scales as ∼ √nψ/T1/2
reh.” The axial current J5 has mass-dimension 3, whereas √nψ/T1/2 has dimension 1 in natural units, so this cannot be an estimate for ⟨J5⟩rms. This undermines the quantitative erasure claim.
- Required fix: Replace with a dimensionally consistent estimate for ⟨J5⟩rms (and its relaxation rate) or remove the formula. If the point is qualitative (ΓCP ≫ H), provide a rate calculation (see also P1A-M2 in the first report).

P1A-E14
- Location: Sec. II A 2, Eqs. (5)–(6)
- Problem: Parity structure and index contraction mismatch. The form eI∧eJ∧FIJ without an internal εIJKL is parity-even (Palatini-like). The component rewrite in Eq. (6) uses the spacetime εµνρσ with eI
µ eJ
ν FIJ
ρσ, which does not reproduce the standard Holst pseudo-scalar εIJKL eI∧eJ∧FKL. As written, the “parity-odd” claim is unsupported and contractions are inconsistent with the Holst parity-odd structure.
- Required fix: If the intent is the Holst/Nieh–Yan parity-odd interaction, write it with εIJKL explicitly, or provide a covariant differential-form definition that unambiguously yields a pseudo-scalar 4-form. Then re-do the dimensional analysis and any downstream inferences with the corrected operator.

MAJOR

P1A-M8
- Location: Sec. IV D, Eq. (17), and surrounding text
- Problem: Over-simplified mapping from ALP energy density to birefringence angle. The paper assumes β ≈ (α/M) Δθ with Δθ ∼ √(2ρθ)/mθ, which corresponds to taking θ as a single-harmonic oscillator with amplitude fixed by ρθ ≃ mθ^2 θ^2/2 and Δθ equal to that amplitude. For mθ ∼ H0, the field is slow-rolling, not coherently oscillating, and Δθrec→today equals an integral of θ̇, not √(2ρ)/m. The mapping used is model-dependent and can change the inferred α/M by O(1)–O(few).
- Required fix: Specify the θ dynamics (oscillating vs. slow-roll), derive Δθrec→today accordingly, and update the α/M inference consistently with the chosen regime and normalization (see also P1A-E10 in the first report).

P1A-M9
- Location: Sec. II C 1 (“Inflationary Suppression” paragraph 1), page 6–7
- Problem: Incorrect statement about “the cube of the fermion bilinear.” Torsion tracks the axial current J5 (a fermion bilinear). If the number density nψ ∝ a−3, then J5 ∝ a−3 (up to polarization factors), not “the cube of the fermion bilinear.” The present wording is physically confusing and suggests a^−9 scaling.
- Required fix: Clarify that in minimal EC the (algebraic) torsion source scales as J5 ∝ a−3 for a dilute non-relativistic fermion gas (or provide the appropriate scaling for the actual regime considered).

P1A-M10
- Location: Footnote 1 to Sec. VII and Table I, “SPHEREx forecast” discussion
- Problem: S/N degradation by a template-overlap factor r ≈ 0.84 is quoted as a linear multiplier (from 6.25σ to ~5.25σ). That translation is not generally valid without specifying the estimator and covariance; in many cases mismatch enters via Fisher projections with r^2 weights, not r, and can couple to binning and noise.
- Required fix: Either provide a short derivation (or citation) showing why the linear-in-r degradation holds for the specific bispectrum estimator assumed, or remove the numerical adjustment.

P1A-M11
- Location: Sec. II B, end of first paragraph under Eq. (9)
- Problem: “No free parameters” claim for the bounce is overstated. ρcrit depends on Δ ∝ γ and the area-gap choice; the text elsewhere emphasizes scheme dependence (γSU(2) vs γDLM). Calling the bounce “with no free parameters” is inconsistent with this scheme dependence.
- Required fix: Rephrase to “once a counting scheme (and hence Δ) is fixed, ρcrit is fixed.” Do not claim parameterlessness.

MINOR

P1A-m5
- Location: Sec. X D/E and Sec. XIII “LiteBIRD” paragraph
- Problem: Notation drift and missing definitions. Primes in Eq. (21) are used (conformal time derivatives) without stating the time variable at first use in Sec. X; vR, vL, Δv are introduced but not defined until later prose.
- Required fix: Define η (conformal time), primes, and the polarization mode functions where first used; if Δv is not used further, remove or tie it directly to TB/EB non-generation in one sentence.

P1A-m6
- Location: Throughout
- Problem: Several typographical/encoding artifacts (e.g., “Poincar´e,” “Domaga la”) and inconsistent MPl vs. M_Pl notation.
- Required fix: Normalize typography and notation.

NIT

P1A-n4
- Location: Fig. 2 caption and related text
- Problem: The caption’s formula ρvac ∼ [(α/M) MPl] M4
Pl is not explicitly linked to the Λeff parameterization of Eq. (10). While algebraically equivalent if one defines Ξ ≡ (α/M) MPl Dinf and then ρΛ ≡ Ξ M4
Pl/(8π), the missing connective tissue may confuse readers.
- Required fix: Add a brief sentence cross-linking Eq. (10) and Fig. 2 with the chosen convention for mapping Λ to ρΛ, including any 8π factors.

P1A-n5
- Location: Sec. III A, Eq. (12)
- Problem: The small-angle EB expression CEB
ℓ ≈ 2β (CEE
ℓ − CBB
ℓ) is correct to first order but the text does not note the exact form (½ sin 4β)(CEE
ℓ − CBB
ℓ). This is harmless, but a parenthetical “small-angle limit of (½) sin 4β” would avoid confusion.
- Required fix: Add a parenthetical note about the exact form.

Explanation
This second-pass focused on unit consistency (Λ vs ρΛ), parity and index structure of the purported parity-odd operator, the γ-dependence of the torsion-induced contact term, and hidden assumptions in the ALP-to-β mapping and SPHEREx S/N degradation — issues commonly missed on a first read. I did not repeat items from the original report.