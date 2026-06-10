# P1A R26conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1a_ech_nogo_v1A.0.53.pdf` md5=878edf0c pages=25
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (9841 chars)
**Wall time**: 300.6s

---

Referee report for: “Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter”

Scope of review
I assessed the full 25-page manuscript (figures, tables, equations, footnotes, appendices, references) for methodology rigor: dimensional analysis, derivation chains, statistical claims, numeric/arithmetic consistency, estimator clarity, and internal coherence. All load-bearing scalars in the abstract and conclusions were traced back to the body and recomputed where possible.

Overall assessment
The paper’s central technical statement (Holst dual contraction vanishes identically on the Levi-Civita connection and hence decouples from scalar/tensor perturbations for canonical scalar matter) is correct and important. However, the submission does not meet PRD standards in its current form. It relies pervasively on unpublished “companion” materials for results and even for numerical inputs; includes version-history and draft-correction prose inside the scientific text; introduces a nonstandard action with an unexplained T^2 term; advances a quantitative one-loop birefringence bound built on an operator ansatz that is not derived; and presents several load‑bearing quantitative figures (e.g. “115 orders of magnitude improvement”) whose interpretation is at odds with the text’s own caveats. These are all fixable, but the fixes are substantial.

Findings and required actions

ESSENTIAL

P1A-E1
Section II (p. 5), Sec. V–VII (pp. 12–13), multiple other locations; also Table I (p. 4), Fig. 4 caption (p. 13), and “Companion paper” paragraph (p. 5)
Problem: Core numerical claims and even baseline cosmological parameter values (e.g., H0 = 67.68 ± 1.06, ΔNeff ≈ 0; “309,189 frozen accepted samples”; NaMaster validation; ALP parameter fitting; SPHEREx fNL forecast significance; PTA γ reanalysis) are sourced to “companion works in preparation/posted concurrently” with no stable, citable results in this manuscript. The text repeatedly tells the reader to treat numbers as “internal-analysis inputs … rather than peer-reviewable values.”
Required fix: Make the paper self-contained. Either (i) remove all claims depending on unpublished/“internal” results (including H0/ΔNeff posteriors, “confirmed null” galaxy-spin inference, SPHEREx Fisher numbers, PTA γ reanalysis), or (ii) include full methods and results needed to substantiate these claims in this manuscript (data cuts, estimators, pipelines, convergence diagnostics, posteriors). Relying on “in preparation” work is not acceptable for load-bearing numbers.

P1A-E2
Footnote on p. 2 (first occurrence) and again in Sec. X footnote 3 (p. 17) and Appendix B (p. 22–23)
Problem: Version-history/draft-correction prose appears in the scientific text: “Earlier versions of this manuscript erroneously identified the two; the correction preserves the headline conclusion…”, “not the ∼ 35 misstated in earlier drafts…”. PRD does not permit manuscript version history commentary in the body.
Required fix: Remove all references to earlier drafts, corrections, or version history from the body and footnotes. State the correct identity succinctly and cite an external reference if needed.

P1A-E3
Eq. (1), p. 5
Problem: The “Einstein–Cartan–Holst Action” is written with a + (1/4) Tabc Tabs term as if it were a bare action term. The text then says this is “a shorthand for the four-fermion contact interaction obtained after integrating out the non-propagating torsion; it is not an independently specified kinetic term.” Including it at the level of the fundamental action is misleading and dimensionally ambiguous unless the torsion elimination is shown explicitly (with correct coefficients and signs).
Required fix: Present the standard EC+Holst action without an explicit T^2 term, then derive the four-fermion contact by integrating out torsion (give the exact steps and coefficients), or move the T^2 term out of Eq. (1) and into a derived effective Lagrangian with a clear reference derivation. Provide a consistent convention for κ, sign, and the γ dependence.

P1A-E4
Sec. IV.B, Eq. (14)–(15) (pp. 10–11)
Problem: The one-loop “Route 2” amplitude bound for birefringence is based on a phenomenological operator ansatz Γone-loop ∝ MPl−1 ∫ ∂μϑNY J5μ that is not derived from a controlled computation. Yet a hard quantitative exclusion (“≈ 60 orders of magnitude below the observed signal”) is drawn from it. Appendix C derives β = (α/2M)Δθ for the Maxwell–Chern–Simons operator, but there is no derivation linking Eq. (14) to a uniform CMB rotation angle with the stated normalization.
Required fix: Either (a) provide a controlled derivation (or a precise literature reference) that maps Eq. (14) to a birefringence angle with all prefactors, and then recompute Eq. (15) with all units and constants explicit; or (b) explicitly downgrade the Route-2 statement to a qualitative scaling bound (Planck + one-loop αem/(4π) + H0 suppression) without a numeric “~10^−60” claim. In either case, remove the arbitrary “up to two orders of magnitude allowance” and provide a defensible uncertainty estimate tied to stated assumptions.

P1A-E5
Throughout; esp. Table I (p. 4), Sec. XII.A and Fig. 5 (p. 15), Appendix B (pp. 22–23)
Problem: The figure and text repeatedly describe “115 orders of magnitude improvement” in fine-tuning due to the Ntot reparameterization, while also acknowledging that this is merely a reparameterization (not a solution) of the cosmological constant problem. The current figure and labels can mislead readers into inferring genuine alleviation.
Required fix: Replace “improvement” by “reparameterization” everywhere it appears (including in Fig. 5’s burned-in annotation and caption). Add a clear statement in the caption that the “fine‑tuning score” is a diagnostic of sensitivity to Ntot, not a reduction of the cosmological constant hierarchy. Alternatively, remove the bar-chart completely.

P1A-E6
Multiple places; e.g., Table III footnote (p. 19)
Problem: The manuscript includes live-run status of MCMC chains (“chain has … R̂ − 1 ≈ 3×10−2… we deliberately do not commit to a specific calendar date for convergence”). This is not publishable material and cannot support any scientific claims in this paper.
Required fix: Remove all pipeline status updates and any claims that depend on such unfinished results.

MAJOR

P1A-M1
Sec. II.C.1, “Reheating thermal-reset barrier” paragraph (pp. 7–8)
Problem: The claim that “C/P-violating scattering rates … exceed the Hubble rate at T ∼ Treh” and erase any coherent axial background is plausible but unsupported by calculation or references (rates, species content, temperature ranges).
Required fix: Provide at least an order-of-magnitude estimate (species, typical weak/strong/electroweak rates vs. H at Treh) or cite literature quantifying the thermalization of axial charge and washout of ⟨J5μ⟩ near reheating. Clarify assumptions (degree of chemical equilibrium, lepton/baryon asymmetry, sphaleron effects).

P1A-M2
Sec. II.A.2, Eq. (7) and surrounding text (pp. 6–7)
Problem: The one-loop estimate [(α/M)MPl] ≈ 3×10−3 uses a specific large logarithm (ln(ΛUV/μ) ≈ 74) and an unquantified δNY. The narrative fairly says this is an ansatz, but the quantitative claims downstream (e.g. Dinf budget) use this number as if it were tight.
Required fix: Present a transparent error budget: bracket ΛUV, μ, and g^2 choices, and show the range of [(α/M)MPl] that follows. State explicitly how large δNY would need to be to match the 10−2 “target” and whether that is plausible. Label all downstream uses as sensitivity studies, not determinations.

P1A-M3
Sec. IV.A, NJL bound (p. 9–10)
Problem: The number-density conversion n ≈ 330 cm−3 ≈ 2.5×10−12 eV^3 and ρNJL ≈ 4×10−80 eV^4 checks out. However, the text states NB that the operator is parity‑even, then later uses it to close an EB-type channel (partly via B14). The logical separation is clear in places, but the NJL closure paragraph should explicitly say “closes parity-odd imprint as well.”
Required fix: Add one explicit sentence at the end of Sec. IV.A noting that this operator cannot source parity-odd EB or TB at any order in the minimal setup.

P1A-M4
Sec. IV.D (pp. 11–12)
Problem: The ALP birefringence mapping β = (α/2M)Δθ and the inversion ρθ = 2 m^2 θ β^2 / (α/M)^2 are correct, and the numeric example ρθ ≈ 1.6×10−10 eV^4 at mθ = H0 reproduces my recomputation. However, the text conflates two couplings (the paper’s α/M vs. the canonical gaγ) only in a footnote, leaving ambiguity for readers who will try to compare against helioscope/stellar-cooling bounds.
Required fix: Move the basis-conversion discussion from footnote to the main text of Sec. IV.D, and include an explicit mapping to gaγ = (αem cγ)/(2π fa) so readers can compare directly to standard ALP constraints. State clearly what value of gaγ your α/M = 10−21 GeV−1 corresponds to.

P1A-M5
Sec. X (pp. 16–18)
Problem: The “perturbation transparency” result is mostly well presented, but the proof references the algebraic Bianchi identity in words. Given the confusion in the literature about Holst vs. Nieh–Yan vs. Pontryagin, a short, explicit index‑level proof (three lines) or a precise literature reference would improve rigor.
Required fix: Add a short derivation showing εμνρσ Rμνρσ(Γ̊) = 0 using Rμ[νρσ] = 0, or cite a standard reference with equation number where this contraction is proven to vanish for Levi‑Civita.

P1A-M6
Figures 1, 4, 6 and Table I (pp. 4–5, 13, 20)
Problem: Several figures and Table I are tightly coupled to “companion” forecasts and catalogs (SPHEREx σ(fNL), galaxy spin null, LiteBIRD β forecast); captions and arrows imply results established here.
Required fix: Redraw figures/captions to (a) remove dependence on unpublished results, or (b) explicitly label all such entries as “external to this paper—illustrative only.” Do not present forecast numbers or “confirmed null” claims unless supported within this manuscript or by peer‑reviewed/citable literature.

MINOR

P1A-n1
Sec. II.C, Eq. (10) and Fig. 3 (pp. 6–7)
Problem: The rotation contribution accounting (“dividing by 3 ΩΛ ≈ 2.1”) is plausible but unreferenced.
Required fix: Add one sentence or citation justifying the mapping from ω^2 to a fractional contribution to ρΛ or H^2 in Bianchi‑type cosmologies, or clearly label it as a back‑of‑envelope bound.

P1A-n2
Sec. III.A, Eq. (12) (p. 8)
Problem: The small-angle uniform-rotation approximation CℓEB ≈ 2β(CEEℓ − CBBℓ) is standard, but a reference would help (and specify that current β estimators use full likelihoods, not this approximation).
Required fix: Add a canonical reference and explicitly say this equation is used only for intuition (as you already partly note).

P1A-n3
Sec. XIV.C–E and Table III (pp. 20–21)
Problem: Several places compare σ-significances from different analyses (WMAP+Planck vs. ACT DR6) and also quote a “∼ 9σ” LiteBIRD detection of nonzero β by 0.27°/0.03°. The caveat about different null hypotheses is good, but it should be reiterated next to each juxtaposition to avoid misinterpretation.
Required fix: At each juxtaposition of significances from different null tests, add “not directly comparable; different null hypotheses and pipelines” (or rephrase to avoid numerical side-by-side comparisons).

NITS

P1A-N1
Throughout
Problem: The manuscript uses “programme,” “burned-in,” “posted concurrently,” and other informal phrasings atypical for PRD style.
Required fix: Standardize to PRD style (e.g., “program,” remove informal figure-caption remarks like “burned-in”).

P1A-N2
References [5], [41]–[45], [46], [47] etc.
Problem: Several citations are to 2025–2026 arXiv preprints; check that the citation metadata (year/IDs/authors) are correct. Reference [5] is a 2025 arXiv ID; confirm title/author match.
Required fix: Verify and correct bibliography entries; where possible, add journal references or clearly label as “arXiv preprint (YYYY).”

Arithmetic and dimensional spot-checks performed

- Eq. (9): ρcrit/ρPl = √3/(32π^2 γ^3) reproduces 0.41 for γ = 0.2375 and ~0.27 for γ = 0.274 (OK).
- Eq. (7) numeric: [(α/M) MPl] ≈ 3×10−3 using g^2=0.092, ln(Λ^2/μ^2)=74, γ^3/2 factor via M=MPl/√γ (OK).
- NJL bound: n ≈ 330 cm−3 → 2.5×10−12 eV^3; ρNJL ~ n^2/MPl^2 ≈ 4×10−80 eV^4 (OK; ~10^−69 ρΛ).
- R2 amplitude ratio Eq. (15): Using αem/4π ≈ 5.8×10−4, H0/MPl ~ 10^−61, MPl(α/M) ≈ 10^−2, βobs ≈ 6×10−3 → ~10^−60 (OK, under stated ansatz).
- R4 inversion: ρθ = 2 m^2 β^2/(α/M)^2 at m=H0=1.5×10^−33 eV, α/M=10^−30 eV−1, β=6×10^−3 → 1.6×10^−10 eV^4 ≈ 6 ρΛ (OK).
- Appendix B: Ntot: e−3N ≈ 10−122 → N ≈ 94; with [(α/M)MPl] ≈ 10−2 shifts to ~93 (OK; text gives 92–94).
- Appendix C: β = (α/2M)Δθ derivation from helicity dispersion (OK).

Length
The manuscript is long (25 pages) for a primarily theoretical closure/consistency paper. Given the required removals (all “companion”‑dependent material) and tightening of the central proofs, the paper could be shortened to ~15–18 pages without loss.

## Summary recommendation
MAJOR REVISIONS

The central “perturbation transparency” result is sound and interesting, and several amplitude-level closures are plausible. However, the manuscript does not meet PRD’s standards in its current form due to (i) heavy reliance on unpublished/“in preparation” companion materials for quantitative claims and even basic parameter values; (ii) inclusion of version-history commentary in the scientific text; (iii) a nonstandard action presentation that conflates fundamental and effective terms; and (iv) a quantitative one-loop birefringence bound built on an undemonstrated operator ansatz. Addressing the ESSENTIAL and MAJOR points above would make the paper self-contained, methodologically rigorous, and suitable for PRD consideration.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS (second-pass audit)

P1A-E7
Location: Sec. II.A.2, Eq. (4) and Sec. IV.A, Eq. (13)
Issue: Undefined “N” and coefficient mismatch in the four-fermion term. Eq. (4) introduces an extra factor N (apparently “number of fermion species”?) that is never defined, and the overall coefficient then does not match the standard Hehl–Datta result shown later in Eq. (13). With κ = 8πG, Eq. (13) has −(3/16)κ(J5)^2, i.e. −(3πG/2)(J5)^2. Eq. (4) reads −(3πGN/2)(γ^2/(γ^2+1))(J5)^2. The “N” is absent from Eq. (13), and the γ-factor should be justified by an explicit torsion-elimination step with Holst. As written the two equations are inconsistent.
Required fix: Define N explicitly or remove it; present a single, self-consistent derivation (including the Holst-induced γ^2/(γ^2+1) factor) and carry that coefficient through consistently everywhere.

P1A-E8
Location: Sec. IV.B, Eq. (14)
Issue: Dimensional inconsistency in the Route-2 one‑loop operator. The proposed Γone-loop ∝ MPl−1 ∫ d^4x √−g ∂μϑNY J5μ is dimensionally problematic unless ϑNY carries an unconventional mass dimension. In 4D, J5 has mass-dimension 3; ∂μϑNY has dimension 1 if ϑNY is dimensionless; the integrand then has dimension 4 and does not need a 1/MPl. With 1/MPl it has dimension 3 and the action is not dimensionless. If instead ϑNY has mass-dimension 0 and the coupling is dimensionless, that must be stated. As written, the operator’s mass dimensions are not consistent with a well-defined action.
Required fix: Specify the mass dimension of ϑNY and re-normalize the operator so that the Lagrangian density has dimension 4 (natural units). If a 1/MPl appears, show explicitly how the remaining factors raise the density back to 4. Recompute any downstream amplitude estimates with the corrected normalization.

P1A-E9
Location: Appendix C (Eq. C1–C4), Sec. IV.D (Eq. 17), and surrounding text
Issue: Inconsistent normalization and field dimension for the ALP/CS sector. The Lagrangian is written as L ⊃ −1/4 F^2 − 1/4 (α/M) θ F F̃ with “θ a homogeneous pseudoscalar,” then β = (α/2M) Δθ is used. If θ is dimensionless (axion angle), (α/M) must have mass-dimension +0 for L to have dimension 4; if (α/M) has mass-dimension −1 (as used elsewhere), then θ must be canonically normalized with mass dimension +1 (i.e., the field a), not a dimensionless angle. The text later maps to gaγ via θ = a/fa, but the intermediate formulas mix notations, creating dimension mismatches (e.g., β = (α/2M) Δθ is only dimensionally correct if Δθ has mass-dimension 1).
Required fix: Choose one consistent convention:
- Canonical: L = −(gaγ/4) a F F̃; β = (gaγ/2) Δa, with [gaγ] = M−1, [a] = M.
- Angle: L = −(αem C/8π) θ F F̃ (no 1/M); β = (αem C/4π) Δθ.
Then show the exact mapping between (α/M, θ) and (gaγ, a) and keep it fixed throughout. Recompute any numerical examples if the normalization changes.

P1A-B1
Location: Fig. 3 annotation vs. main-text bound in Sec. II.C, p. 7
Issue: Mismatch in the rotation bound. The figure (burned-in annotation) quotes |ω^2/H^2| < 10−20, while the body uses (ω/H)0 < 5×10−11 ⇒ (ω/H)^2 < 2.5×10−21. The caption/body explanation that they are “the same rotation term in different units” is incorrect; both are the same dimensionless ratio. The numbers differ by a factor ≈ 4.
Required fix: Make the bound numerically consistent between figure and text (and state the source/reference once).

P1A-E10
Location: Sec. IV.D (galaxy-spin paragraph on p. 8 and reiterated p. 12)
Issue: “> 100 orders of magnitude” underprediction claim for galaxy spin asymmetry is unsupported. The manuscript asserts that α/M ∼ 10−21 GeV−1 underpredicts “any plausible spin asymmetry” by >100 OOM, but no model equation linking α/M to an observable A0 (or any spin-dipole amplitude) is given, nor any back-of-envelope with numbers.
Required fix: Provide a quantitative mapping from the parity-odd operator to a galaxy-scale spin-asymmetry observable (with scale/hierarchy estimates) or remove the claim.

P1A-M7
Location: Sec. II.A.2, Eq. (7) and text
Issue: Unmotivated linear γ factor in the one-loop estimate. The estimate [(α/M)MPl] ∼ (g^2/32π^2) γ ln(ΛUV^2/μ^2) + δNY includes a factor of γ without an explicit derivation or citation supporting that precise dependence. Given the paper’s emphasis on operator-level rigor, this insertion needs justification; otherwise, it compounds the already-acknowledged ansatz status with a specific, unproven γ-scaling.
Required fix: Cite a calculation that yields exactly this γ-dependence (not just “motivation”) or present the intermediate steps; else remove γ from Eq. (7) and restrict the claim to an order-of-magnitude loop/log estimate.

P1A-M8
Location: Multiple sections (Sec. II.A.2, IV.D, Fig. 5 top)
Issue: Inconsistent baseline for α/M. The text alternates between [(α/M)MPl] ≈ 10−2 (i.e., α/M ≈ 8×10−22 GeV−1) and α/M ≈ 10−21 GeV−1 as the “adopted” value. Fig. 5 (top) is anchored at 10−21 GeV−1, while Appendix B and Sec. II.A.2 often imply 8×10−22 GeV−1. This affects all quadratic-in-coupling inferences (e.g., ρθ ∝ 1/(α/M)^2).
Required fix: Pick one baseline value (with a defensible uncertainty band from Eq. 7’s inputs) and use it consistently. Where a different value is needed (e.g., for an illustrative ALP point), label it explicitly as such and discuss the quantitative impact on key results (e.g., the ρθ overshoot).

P1A-M9
Location: Sec. II.B, Eqs. (8)–(9) and surrounding text
Issue: Cross-scheme extrapolation for ρcrit. The manuscript plugs the SU(2) black-hole-entropy value γ = 0.274 into the LQC ρcrit formula to quote ρcrit ≃ 0.27 ρPl, while acknowledging this is an “internal extrapolation” across schemes. Because ρcrit is central in LQC, using a nonstandard γ choice should be justified quantitatively (how much this matters for any bound) or treated purely as a sensitivity test.
Required fix: Either revert to the canonical LQC value (γ = 0.2375 ⇒ ρcrit ≃ 0.41 ρPl) for all numerics, or keep both values in a bracketed sensitivity statement and ensure no later quantitative claim depends on the scheme choice.

P1A-M10
Location: Throughout (e.g., Sec. II.C Eq. (10), Sec. XII.A Eq. (24))
Issue: Planck-mass convention drift. The paper states it uses the unreduced Planck mass MPl = G−1/2, but many EFT normalizations and several community-standard formulas are conventionally written with the reduced mass M̄Pl. Since products like MPl(α/M) and Λeff MPl^2 are used repeatedly, a factor of 8π drift can move some of your “order-of-magnitude” numbers by an e-fold at the Ntot level.
Required fix: Explicitly restate the convention near every place such products appear (or convert everything to M̄Pl). Where MPl(α/M) is used as a dimensionless “baseline,” show the corresponding number with M̄Pl so readers can compare.

P1A-M11
Location: Sec. XIII, paragraph beginning “This value holds within the scalar-only w = 0 matter-bounce class under Assumption (f) of Paper II [2]…”
Issue: Reliance on an external, unpublished assumption for a core “surviving” prediction. Even after removing numerical dependence on companion papers, tying the validity range of fNL = −35/8 to an “Assumption (f)” in another manuscript makes the present paper non-self-contained.
Required fix: State the assumption explicitly here (content and mathematical form) and show how it enters the derivation or the class definition. Otherwise, rephrase to a purely qualitative, literature-cited statement.

P1A-n4
Location: Throughout (e.g., Table IV, Sec. X.G)
Issue: Ambiguous reuse of γ. The same symbol γ denotes the Barbero–Immirzi parameter and the PTA spectral index in different sections. Although “PTA γ” is sometimes written, several instances still use “γ” alone.
Required fix: Disambiguate with subscripts everywhere (γBI for Barbero–Immirzi, γPTA for the spectral index).

P1A-n5
Location: Sec. II.C Eq. (10) and Sec. XII.A Eq. (24)
Issue: Angle bracket notation ⟨(α/M) MPl⟩ is undefined. It reads like an average; over what (time? species? loops?) is not stated.
Required fix: Define the bracket or drop it. If it signifies “reference value,” write it plainly.

P1A-n6
Location: Sec. IV.C and surrounding text
Issue: “Mass-dimension lock” claim is asserted, not shown. The statement that any parity-odd operator “forces a single power of M−1
Pl in the prefactor” needs a short dimension-counting argument (or a reference) to avoid appearing ad hoc.
Required fix: Add a 1–2 sentence dimension count for the relevant operator basis, or cite a standard EFT reference demonstrating the restriction.

P1A-n7
Location: Multiple
Issue: Cross-procedure σ juxtapositions beyond the birefringence case. In addition to the β discussion (already caveated once), the text places σ(fNL) Fisher forecasts and galaxy-spin dipole “null” side-by-side in figures/tables. These come from different null procedures and pipelines.
Required fix: Add a “not directly comparable; different null hypotheses/pipelines” qualifier at each such juxtaposition, not just for β.

P1A-n8
Location: Notation (e.g., Eq. (6))
Issue: Mixed index conventions. Expressions like εμνρσ eI
μ eJ
ν FIJ
ρσ intermix curved and internal indices without a stated convention for contractions and signature. This is standard but should be stated once to avoid ambiguity.
Required fix: Add a brief notation block (metric signature, index placement conventions, how eI
μ contracts FIJ
ρσ, etc.).

Explanation
These are issues that were not covered in my first report. Most are dimensional-normalization inconsistencies in the parity-odd/ALP sector (E8–E9), an undefined factor in the four-fermion term (E7), a figure/body numeric mismatch (B1), and additional self-containedness/notation problems (M11, n4–n8). The earlier report’s essential items still stand; the new items above are in addition to, and do not duplicate, those prior findings.