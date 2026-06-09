# P1A auto-2026-06-09_1042pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (8536 chars)
**Wall time**: 486.5s

---

Referee report on “Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter”

Scope of review
I assessed methodology rigor: derivation chains, dimensional analysis, internal arithmetic and unit consistency, statistical claims, estimator declarations, and reproducibility. I audited all equations, figures, tables, and every load-bearing scalar stated in the abstract and conclusions against the body text.

Findings

ESSENTIAL (paper cannot be accepted without this fix)

P1A-E1 (Abstract; Sec. I, pp. 1–5; multiple throughout). Reliance on unpublished “companion” papers and in‑preparation material for core results.
Quote/examples:
- “Companion paper.—ΛCDM+ΔNeff MCMC verification… are reported in Paper I(b) [6]. … documented internally rather than as externally citable arXiv-posted numbers…” (p. 5)
- “Paper II forecast [2]” for the 3–5σ SPHEREx detection claim; “Paper III [46]” for PTA γ; “Paper IV [23]” for galaxy-spin null; all are “in preparation.”
Problem: Key numerical claims (H0, ΔNeff, NaMaster validation, ALP fits, SPHEREx Fisher forecast, PTA reanalysis, 8.47M galaxy chirality null) are not substantiated within this manuscript nor cited to public, peer-accessible sources. PRD requires the submission to be self-contained or to rely on publicly available, citable results.
Required fix: Remove all results that depend on unpublished/in‑preparation work or replace them with full, self-contained derivations, data products, and methods in this paper, or cite publicly available preprints with complete methodological detail. If those are central to the work’s conclusions (they are), the paper must be resubmitted only when those companion works are publicly available and formally cited.

P1A-E2 (Sec. II A 2; Appendix B, pp. 5–7, 21). Dimensionally inconsistent parity-odd operator used as a load-bearing element.
Quote: Eq. (6): “Seff = ∫ d4x √−g (α/M) εμνρσ eIμ eJν FIJρσ,” acknowledged to have naive mass dimension +1 (Appendix B, Eq. B1).
Problem: A dimension-1 Lagrangian term cannot be used to derive quantitative mappings to ρΛ without specifying a valid dimension-4 EFT completion. The manuscript repeatedly uses the on-shell scaling ansatz ρΛ ∼ [(α/M) MPl] M4
Pl as a basis for Ntot ≈ 92 and other conclusions.
Required fix: Provide a consistent, diffeomorphism-invariant, dimension-4 operator (with all necessary MPl powers in the coefficient) derived from a controlled EFT or path-integral elimination of torsion, and redo all quantitative mappings with that operator. Alternatively, remove every claim that depends on the dimension-1 operator (including the Ntot ≈ 92 “suppression” accounting) and restrict the discussion to rigorously derived, dimensionally consistent results.

P1A-E3 (Sec. IV B, pp. 9–10). Route 2 (one-loop) operator and amplitude ratio are ad hoc and lack a derivation; the numerical suppression estimate (Eq. 15) is ambiguous.
Quote: Eq. (14) is introduced as an “upper-bound EFT ansatz” not derived from the cited literature; Eq. (15) contains an order-of-magnitude chain mixing H0/MPl and an unexplained factor “MPl(α/M).”
Problem: Without a firm one-loop computation (or citation with explicit coefficient and scheme), the comparison to observed birefringence amplitude is not methodologically valid. The dimensionless reduction in Eq. (15) is also unclear: the placement of M/MPl and MPl(α/M) needs an explicit, reproducible derivation.
Required fix: Either (i) present a proper one-loop calculation (including regularization scheme, counterterms for the Nieh–Yan divergence, and the finite part) that yields the exact operator and its normalization, then recompute the expected β; or (ii) explicitly demote Route-2 to qualitative only and remove all quantitative amplitude-ratio statements.

P1A-E4 (Sec. IX L, Eq. 20, p. 15). “Vacuum amplification ceiling” ΩGW|bounce ≲ (ρcrit/ρPl)^2 lacks derivation.
Problem: No calculation is given to justify that the total GW energy density fraction at the bounce is bounded by the square of ρcrit/ρPl; the expression has no provenance and is not even dimensionally motivated for an energy-density fraction. It is subsequently used as a “barrier.”
Required fix: Provide a full derivation or a precise citation where this bound is derived; otherwise remove Eq. (20) and the associated barrier claim.

P1A-E5 (p. 2 footnote; multiple places). Version-history and draft-language appear in the body.
Quote: “Earlier versions of this manuscript erroneously identified the two; the correction preserves the headline conclusion…” (p. 2, footnote). Also extensive status/progress reporting on chains: “we deliberately do not commit to a specific calendar date for convergence…” (Table III footnote, p. 17).
Problem: PRD does not permit version-history commentary or internal status logs in the final manuscript body.
Required fix: Remove all version-history remarks, internal chain-status logs, and draft commentary. If a correction is needed, state the correct identity once in a neutral way with a literature citation.

P1A-E6 (Abstract; Secs. I, III, XIII, XV). Juxtaposition of σ values from different null procedures without “not directly comparable” caveats.
Quote: “WMAP+Planck … 3.6σ … and ACT DR6 … 2.9σ.” These appear side-by-side multiple times without an explicit statement that they are not directly comparable due to differing data, pipelines, and null procedures.
Required fix: At each juxtaposition, add an explicit statement that the significances are not directly comparable and depend on experiment-specific likelihoods and systematics.

P1A-E7 (Sec. II C 1, pp. 7–8). “Reheating thermal-reset barrier” asserts washout of axial current with a schematic fluctuation scaling ~√nψ/T1/2
reh but provides no thermal field theory derivation or rate comparison.
Problem: The barrier is presented as a decisive closure mechanism yet rests on a non-derived scaling and unquantified rate arguments (no explicit comparison of C/P-violating scattering rates to H). This is not methodologically sufficient for a closure claim.
Required fix: Provide a quantitative thermal-field-theory calculation: specify the relevant axial-current damping channels, compute Γwashout(Treh) and compare to H(Treh), and show that coherent ⟨J5⟩ → 0 on cosmological timescales. Otherwise, state this as a conjecture and remove it from the set of formal barriers.

P1A-E8 (Sec. IV A, p. 9 vs. Sec. II A 2, p. 6). Inconsistency regarding γ-dependence of the torsion-induced four-fermion operator.
Quote: Eq. (4) introduces a γ-dependent axial–axial coefficient ∝ γ^2/(γ^2+1), but Sec. IV A asserts “torsion-elimination map is independent of γ at the classical level.”
Problem: These two statements conflict. The literature (e.g., Freidel–Minic–Takeuchi; Mercuri) shows γ-dependence for minimally coupled fermions; special non-minimal couplings can remove it.
Required fix: Clarify precisely which coupling scheme is assumed. If minimal, maintain the γ^2/(1+γ^2) dependence and show why it does not affect the amplitude bound; if a specific non-minimal coupling is assumed (e.g., Nieh–Yan completion), state it explicitly and adjust all formulas consistently.

P1A-E9 (Figures 2–3 and 5–6). Figure axis labeling/units and caption–body consistency.
Problems:
- Fig. 2 has no axes, tick marks, or units; it is not possible to assess the quantitative mapping it purports to illustrate.
- Fig. 3 lower panel “ΔH(z)/H0 (%)” is shown, but the caption/body do not specify the model difference definition nor the exact parameters used.
- Fig. 5 “Naturalness landscape” shows orders-of-magnitude bars (10^40, 10^60, 10^120) with no derivation or references; this looks like an infographic rather than a quantitative result.
- Fig. 6 “Detection significance forecast” shows σ-level growth vs year with no axis units on the y-axis (presumably σ), no legend normalization, and relies on as‑yet unpublished forecasts.
Required fix: For each figure, add well-defined axes with units, specify all model parameters used, and either supply the derivations/citations for plotted values in the main text or remove the figure.

P1A-E10 (Abstract; Sec. II C; Sec. XIV A; Appendix B). Mapping from the parity-odd sector to ρΛ and Ntot ≈ 92 is non-derivative yet repeatedly used as a central quantitative result.
Problem: Even though the authors label it an ansatz, they still anchor multiple conclusions (e.g., “structural tension” with fNL, Dinf bookkeeping, required e-folds) on this mapping.
Required fix: Either (a) provide a fully consistent EFT derivation that yields a dimension-4 operator and a controlled mapping to dark-energy density; or (b) remove all quantitative claims (Ntot ≈ 92, “reduction from 10^122 to 10^5”, etc.) and clearly segregate these speculations from the formal results.

P1A-E11 (Sec. III B, p. 8; Sec. XIV B, p. 19). Galaxy spin “confirmed null” is asserted without providing the classifier, selection, systematics, or statistical tests in this paper.
Problem: The null result and its statistical significance are central to dismiss “galaxy spin asymmetry” as an observable, yet the methods and data are deferred to “Paper IV [23] (in preparation).”
Required fix: Include a self-contained methods section with the dataset, classifier architecture, training/validation splits, bias audits, sky maps, null tests, and the statistical estimator used (pre-declared), or remove the claim and its interpretive consequences.

MAJOR (significant revision required)

P1A-M1 (Throughout; 23 pages). The manuscript mixes a rigorous structural result (perturbation transparency for canonical scalars) with a large number of speculative “barriers,” forecasts, and in-prep program notes, leading to an overlong, diffuse paper for the claimed contribution.
Required fix: Refocus and shorten. A tight paper proving the perturbation-transparency theorem (with a clean, self-contained derivation and implications) would likely fit in ≤15 pages. Move the speculative route-closures and programmatic material to a separate, fully substantiated paper.

P1A-M2 (Sec. X, p. 15–16). Holst dual contraction identity is asserted; a short, explicit derivation would improve rigor.
Required fix: Add a brief appendix or inline derivation showing εμνρσ Rμνρσ(Γ̊)=0 from the algebraic Bianchi identity on torsion-free connections, ideally also in differential-forms notation using the Nieh–Yan identity e∧e∧R = −NY + T∧T.

P1A-M3 (Sec. IX, multiple barriers). Several “barriers” (e.g., Mass-Coupling Lock Eq. 18; Topological-Shift Duality; Scalar-Tensor Universality; Liouville Conservation; Gravitational Democracy) are stated without concrete derivations or precise theorems.
Required fix: For each barrier kept in the paper, provide a rigorous statement and proof (or a citation to a proof) with explicit assumptions. Otherwise demote them to discussion points and remove them from the numbered “constraint” catalog.

P1A-M4 (Sec. IV D, pp. 10–11). ALP birefringence normalization and mapping to ρΛ.
Problem: The relation β = (α/M) √(2ρθ/m^2) is used; units and the precise definition of α/M versus the canonical gaγ are relegated to a footnote with informal equivalences.
Required fix: Present the mapping cleanly in a standard ALP basis (gaγ, fa), with explicit unit consistency and numerical conversion. Then recompute ρθ for the quoted parameters with clear unit tracking.

P1A-M5 (Sec. II B, p. 6). Use of ρcrit(γSU(2)) = 0.27 ρPl is presented as an “internal extrapolation.”
Required fix: Either cite a source that explicitly quotes ρcrit for the SU(2) entropy-counting γ value or move this to a clearly marked internal estimate and avoid using it as an externally citable input in the main text.

P1A-M6 (Abstract; Sec. I A, Table I, Fig. 1). Claims of “channel-level closure” versus “operator-level closure” blur the line between what is proven and what is conjectured.
Required fix: Sharpen the claims in the abstract and conclusions to match exactly what is proven in the paper: closure of four specifically enumerated channels under stated, non-exhaustive assumptions, not a general no‑go. Remove or rephrase any language that could be read as an operator-basis no-go.

P1A-M7 (Sec. I C; Sec. XIV D). “Structural tension” between Ntot ≈ 92 and SPHEREx-detectable fNL is framed as a key outcome but rests on the speculative Dinf ansatz.
Required fix: Qualify this section accordingly, or provide a self-contained, model-independent mapping of bounce-to-inflation scale relationships that does not rely on the ad hoc operator mapping.

MINOR (address but paper can proceed)

P1A-N1 (Notation; multiple). “R ∧ R̃e” and “R ∧ Re” appear; Pontryagin density notation is inconsistent/incorrect.
Required fix: Use standard notation R ∧ R̃ or 1/2 εμνρσ Rμν
αβ Rρσ
αβ and reserve “Holst dual contraction” exclusively for e ∧ e ∧ R or ε·R with one curvature.

P1A-N2 (Typographic formatting; multiple). 10^122 is rendered as “10122” in text; γ5 vs. γ
5; ψγ¯ μγ5ψ unusual ordering; “Pop lawski” spelling.
Required fix: Standardize scientific notation (10^122), Dirac adjoint notation (ψ̄γμγ5ψ), and correct spellings (Popławski).

P1A-N3 (Sec. III A, p. 8). Add explicit caveat that EB/TB rotation in different experiments is derived under different estimator and systematics treatments (already hinted elsewhere, but add once here).

P1A-N4 (Acknowledgments, p. 21). “We acknowledge the use of Claude (Anthropic) as an AI research assistant…” is unusual but not methodologically problematic; check PRD policy. If required by journal policy, remove or move to a general tools acknowledgment.

P1A-N5 (Sec. II C 1, p. 7). The range “O(0.01–0.1)” for (Treh/MGUT)3/2 is too narrow if Treh varies by a full order of magnitude below MGUT; at Treh = 10^14 GeV the factor is ≈ 3×10^−3. Adjust the stated range or specify the Treh interval assumed.

NITS (cosmetic)

P1A-NT1 (Throughout). Occasional UK spelling (“programme”); acceptable but consider consistency.

P1A-NT2 (Tables II–IV). Ensure column headers specify units where applicable and that footnotes do not contain running “status” commentary.

Arithmetic and dimensional checks performed

- ρcrit(γ=0.2375) ≃ 0.41 ρPl and ρcrit(γ=0.274) ≃ 0.27 ρPl follow from Eq. (9); correct.
- βobs significances: 0.342°/0.094° ≈ 3.64σ; 0.215°/0.074° ≈ 2.90σ; correct.
- Differential significance LiteBIRD vs WMAP+Planck: |0.342−0.27| / sqrt(0.03^2+0.094^2) ≈ 0.73σ; correct.
- R4 ρθ with α/M = 10^−21 GeV^−1, β ≈ 6×10^−3, mθ = H0 ≈ 1.5×10^−33 eV gives ρθ ≈ 4×10^−11 eV^4, same order as (2.3 meV)^4 ≈ 2.8×10^−11 eV^4; consistent with text.
- H0/MPl ≈ 10^−61; consistent.
- kphys scaling with eNtot−Nexit and e32 at Ntot−Nexit ≈ 32; correct.

Core theoretical claim: perturbation transparency
The scalar-matter transparency argument (Sec. X) is sound in outline: intrinsic spin density S=0 ⇒ torsion vanishes algebraically ⇒ Levi-Civita connection ⇒ Holst dual contraction vanishes by the (algebraic) Bianchi identity ⇒ no perturbative EOM contribution. However, for PRD-level rigor, a short, explicit derivation (see P1A-M2) should be included, and the boundary-term subtleties (Nieh–Yan) must be stated cleanly in standard notation.

Length
Given the current blend of rigorous and speculative content, the paper is overlong. A focused manuscript proving the perturbation-transparency result with carefully bounded claims would likely be ≤15 pages. The route-closure program should only be included if fully derived and self-contained; otherwise, it should be drastically shortened or moved elsewhere.

## Summary recommendation
REJECT

The submission contains a potentially interesting structural result (perturbation transparency for canonical scalars), but the manuscript as submitted does not meet PRD methodological standards. It relies heavily on unpublished “companion” papers for essential numerical and statistical claims; uses a dimensionally inconsistent operator as a load-bearing element; introduces ad hoc one-loop operators without derivation; and includes multiple “barriers” and quantitative assertions that lack rigorous proofs. There is also version-history text and internal workflow commentary embedded in the manuscript. Substantial restructuring, removal of speculative/unsupported content, provision of self-contained methods and derivations, and resolution of the dimensional-analysis issues are required. I encourage the authors to submit a shorter, self-contained paper centered on the proven perturbation-transparency theorem, with all speculative elements and unpublished dependencies removed or fully substantiated.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS AFTER SECOND-PASS AUDIT

I re-ran the checklist A–J with a cold read and found several new issues that were missed in my first report. I list only new items below, using the same taxonomy. Items already covered in my initial review (E1–E11, M1–M7, N1–N5, NT1–NT2) are not repeated.

ESSENTIAL (paper cannot be accepted without this fix)

P1A-E12 (Sec. IV B, Eq. 14). Dimensional inconsistency in the proposed one‑loop operator.
- Stated operator: Γone-loop ⊃ −(1/16π^2) [β(γ)/MPl] ∫ d^4x √−g (∂μθ) J5μ.
- If θ is a standard axion/Nieh–Yan angle (dimensionless), then (∂μθ) has mass dimension +1 and J5μ has +3, so the local density has +4; the coefficient must be dimensionless. The explicit 1/MPl makes the density +3, i.e., dimensionally wrong.
Required fix: Either (a) provide a derivation yielding a dimensionless coefficient (and redo the amplitude estimate), or (b) redefine θ with its mass dimension and demonstrate that the overall coefficient renders the density dimension +4. As written, Eq. (14) is not a valid EFT operator.

P1A-E13 (Sec. II A 1, Eq. 1). Non-standard and internally inconsistent appearance of a T^2 term in the “fundamental” ECH action.
- The action includes +(1/4) TabcTabc inside the 1/(16πG) bracket while also stating “T^2 is a shorthand for the four-fermion contact after integrating out torsion.”
- In minimal EC/Holst, there is no independent T^2 term at the classical level; integrating out the algebraic torsion generates a four-fermion term in the matter sector with coefficient ∝ κ, not a bare T^2 kinetic piece inside the gravitational action. Placing T^2 in Eq. (1) risks double counting and obscures normalizations.
Required fix: Present the standard EC/Holst action without an ad hoc T^2 term, and then derive the four-fermion term by eliminating torsion. If a T^2 term is intentionally added (PGT-like), state the theory change explicitly, fix coefficients, and propagate it consistently through the paper.

P1A-E14 (Sec. II A 2; Fig. 2). Figure 2 displays a dimensionally inconsistent “mapping” ρvac ∼ [(α/M) MPl] M4Pl.
- [(α/M) MPl] has mass dimension +0 (if α/M has −1). Multiplying by M4Pl yields mass^4 only if [(α/M) MPl] is dimensionless; but the same text elsewhere (Appendix B) acknowledges that the parity-odd operator has net +1 and the on-shell mapping ρΛ ∼ (α/M) M5Pl is not an EFT result.
Required fix: Remove or correct Fig. 2 so it does not promote a dimensionally inconsistent relation. If you keep a schematic, label it explicitly as a non-EFT ansatz and avoid equations that look like derived equalities.

P1A-E15 (Sec. II A 2 vs. Step 1 Eq. 3). Cartan equation presented without the Holst-induced γ dependence, but γ is used immediately afterward in the four-fermion coefficient.
- Eq. (3) uses Tabc = 8πG Sabc (pure EC), while Eq. (4) inserts the γ^2/(1+γ^2) factor that arises only when the Holst term and minimal fermions are included.
Required fix: Write and use the correct torsion–spin relation in the Holst + fermion theory (with the explicit γ dependence) before integrating out torsion. As written, Step 1 and Step 2 are not a single consistent derivation.

P1A-E16 (Fig. 3). Axis mislabel and undefined comparison on the Hubble panel.
- The top panel y-axis is labeled “H0 (km s−1 Mpc−1)” as a function of redshift z; this must be H(z), not H0. The bottom panel shows “ΔH(z)/H0 (%)” but does not define Δ relative to what model or list the parameters used.
Required fix: Correct the axis label to H(z), define Δ precisely (Spin–Torsion minus ΛCDM? which parameters?), and provide the exact parameter set used to draw the curves (or remove the figure).

MAJOR (significant revision required)

P1A-M8 (Sec. X B, steps 4–5). Internal inconsistency: “identically zero” vs. “total derivative.”
- Step 4 states the Holst dual contraction vanishes identically by the algebraic Bianchi identity on Γ̊. Step 5 then says “A total derivative contributes nothing to variational equations.” These are logically different statements; if the object is identically zero, there is no need to invoke a boundary term.
Required fix: Keep the Bianchi-identity zero statement and remove the total-derivative remark (or relegate the Nieh–Yan identity to a parenthetical aside clearly separated from the Pontryagin discussion).

P1A-M9 (Eqs. 5, 10, 18). Undefined symbols and coefficients in load-bearing equations.
- Eq. (5): FIJ[K, R̊] is undefined (what precise functional combination is used?).
- Eq. (10): cω is not defined (units, magnitude).
- Eq. (18): t3 is not defined or given units (needed to judge geff).
Required fix: Define every symbol when first used, including dimensions and physical meaning, and provide references or derivations for any nonstandard constants.

P1A-M10 (Sec. IV C, Eq. 16 and surrounding text). Unsupported numerical claim Δγ/γ ∼ 10−2.
- After presenting an ad hoc running equation for γ, the text states Δγ/γ ∼ 10−2 over GUT→IR without an explicit calculation or a reference with the same normalization and matter content.
Required fix: Show the running integral (with NL, NR specified for the SM) and compute Δγ/γ, or cite a paper that computes the finite part with the same definitions. Otherwise demote the 10−2 number to a conjectural OOM.

P1A-M11 (Sec. II C; Fig. 3 caption). “Distance-impact of rotation” and Λeff = cω ω^2 statements lack a quantitative derivation and unit accounting.
- The text asserts the rotation contribution is ≲10−22 ρΛobs without showing how cω and ω/H map to an energy-density fraction. The figure caption mentions “distance-impact” but the panel shows H(z), not distance.
Required fix: Provide a short derivation mapping ω/H bounds to a fractional dark-energy contribution with explicit units and assumptions, and align the caption with the plotted quantity; otherwise, remove this figure/claim.

P1A-M12 (Symbol overloading). γ used both for the Barbero–Immirzi parameter and (elsewhere) for the PTA spectral index.
- Table III and surrounding text denote the PTA spectral index as “γPTA,” while the rest of the paper uses γ for the Immirzi parameter.
Required fix: Use disjoint symbols (e.g., γBI for Immirzi, γPTA or nPTA for PTA) consistently to avoid confusion.

MINOR (address but paper can proceed)

P1A-N6 (Units consistency for β). Degrees vs radians are mixed without explicit conversions in some places (e.g., Eq. 15 uses βobs in radians; elsewhere values are quoted in degrees).
Required fix: State once that β is converted to radians for equations, keep units in equations explicit, and ensure all numbers match the stated units.

P1A-N7 (Notation clarity). The symbol “Re(Γ̊)” in Eq. (23) can be mistaken for “real part”; elsewhere “R ∧ R̃e” appears with a stray “e”.
Required fix: Adopt standard notation throughout: Pontryagin density P ≡ (1/2) εμνρσ Rμν αβ Rρσ αβ; Holst dual contraction H ≡ (1/2) εμνρσ Rμνρσ(Γ); Nieh–Yan NY ≡ d(eI ∧ TI). Avoid overloading R e or “Re”.

P1A-N8 (Assumed unit system). The paper intermixes SI-like and natural units (e.g., H0 in km s−1 Mpc−1 and in eV). A brief “Units and conventions” paragraph would help.
Required fix: State c=ℏ=1, MPl convention (reduced or not), and the conversion used for H0 when inserted into EFT estimates.

P1A-N9 (Figure 2 caption). If kept as a schematic, add “schematic, not a derived equality” and remove explicit equations that look quantitative.

Explanation of coverage overlap with initial report
- Earlier findings already flagged: unpublished dependencies (E1), dimension-1 operator reliance (E2), ad hoc one-loop amplitude ratio (E3), GW “ceiling” with no derivation (E4), version-history text in body (E5), σ comparability caveat (E6), thermal-reset barrier lacking rates (E7), γ-dependence inconsistency claim (E8), broad figure-axis/units issues (E9), Ntot ≈ 92 reliance (E10), galaxy-spin null unsupported (E11), plus majors on focus/scope and barrier rigor (M1–M7), and minor notation/typography points (N1–N5).
- The new items above target additional lapses that were not previously called out: Eq. (14) dimensionality, the nonstandard T^2 term in the fundamental action and potential double counting, a concrete figure-axis mislabel (H0 vs H(z)), the “identically zero vs total derivative” inconsistency, several undefined symbols in core equations, an unsupported γ-running numerical claim, symbol overloading, and unit/notation housekeeping.

Overall, these additional issues reinforce the prior recommendation: the manuscript requires substantial reconstruction before it can meet PRD standards.