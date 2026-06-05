# P1A R10v3p1 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (10053 chars)
**Wall time**: 313.9s

---

REFEREE REPORT (Methodology/consistency audit)

Overall assessment
The manuscript proposes a “channel-level closure” of four enumerated minimal Einstein–Cartan–Holst (ECH) dark-energy routes and presents a “perturbation-transparency” statement. While the goals are interesting, the paper as written does not meet PRD standards of methodological rigor and self-containment. Key derivations are either incorrect (Holst–Pontryagin conflation), incomplete (one-loop route amplitude), or explicitly rest on non-EFT, dimensionally inconsistent ansätze; several core quantitative claims depend on companion works “in preparation” that are not available to referees. Numerous internal meta-tags appear in the text. Below I list specific findings.

Findings

ESSENTIAL

P1A-E1 (Abstract; Sec. I pp. 1–3; Sec. X pp. 14–15; Eq. (23) p. 14)
Problem: Holst term ≠ Pontryagin. The paper repeatedly claims “the Holst dual contraction ϵµνρσ Rµνρσ reduces on the Levi-Civita connection to the Pontryagin density ∝ R R̃ … total derivative” (abstract; Sec. X B–D; Eq. (23)). This is incorrect. The Pontryagin density is P ≡ (1/2) εµνρσ Rαβ µν Rβα ρσ (a curvature-squared invariant). The Holst term is eI ∧ eJ ∧ FIJ; its topological relation is via the Nieh–Yan identity: d(eI ∧ TI) = TI ∧ TI − eI ∧ eJ ∧ FIJ. On torsionless configurations (TI = 0), e ∧ e ∧ F does not become Pontryagin; rather, e ∧ e ∧ F = 0 from the Nieh–Yan identity, and the Holst term is dynamically inert because torsion vanishes. Equation (23) is also dimensionally/structurally wrong: (1/2) ε R with a single curvature tensor is not the Pontryagin density, which is quadratic in R.
Required fix: Correct all occurrences. Replace the Pontryagin claim with the proper Nieh–Yan identity and show carefully that with Sµνλ = 0 (scalar matter) the torsion vanishes and the Holst term makes no contribution (or is a total derivative of e ∧ T, which vanishes if T=0). Provide a correct expression for Pontryagin (if needed) and avoid identifying it with the Holst sector.

P1A-E2 (Sec. II A 2; Eq. (6) p. 6; Appendix B pp. 19–20; Abstract)
Problem: Central dark-energy mapping uses a dimensionally inconsistent operator. The parity-odd operator (Eq. 6) has off-shell mass dimension +1, acknowledged in Appendix B; the paper then maps it to ρΛ via an “on-shell scaling ansatz” ρbounceΛ ∼ (α/M) M5
Pl and builds major numerical claims (e.g., Ntot ≈ 92) on this. This is not acceptable as a basis for quantitative conclusions in PRD. The paper oscillates between treating this as a core quantitative result (Ntot, “fine-tuning reduction to 10^5”) and as a disclaimer.
Required fix: Either (i) replace the ansatz with a consistent EFT operator of mass-dimension 4 (show the operator basis, couplings, and renormalization), or (ii) remove all quantitative conclusions that depend on this mapping (Ntot, “reduction from 10^122 to 10^5”, etc.) and clearly segregate the ansatz as speculative, with no numerical claims attached. If you retain any Ntot number, it must follow from a dimensionally correct Lagrangian.

P1A-E3 (Sec. IV B pp. 9–10; Eq. (14)–(15))
Problem: One-loop route amplitude closure is asserted without a derivation that connects the postulated parity-odd gravity–chiral-current operator to the observed photon birefringence angle. Equation (14) is an ad hoc EFT term; Eq. (15) attempts a dimensionless ratio ∆θone−loop/∆θobs but mixes dimensionful inputs (H0, MPl) and the fitted α/M from a different operator (ALP–photon Chern–Simons). No explicit mapping from Γparity-odd one-loop to a rotation angle β for CMB photons is given. The stated 10^−58–10^−60 suppression depends on algebraic choices that are not grounded in a photon-sector calculation.
Required fix: Provide a first-principles derivation (or a published reference) that starts from a well-defined parity-odd term in the gravitational + fermion sector and derives an explicit contribution to photon polarization rotation with all coefficients. Alternatively, reframe R2 as “no quantitative prediction available” and drop the claimed amplitude-level closure.

P1A-E4 (Sec. IX L p. 13; Eq. (20))
Problem: “Vacuum Amplification Ceiling” bound ΩGW|bounce ≲ (ρcrit/ρPl)^2 ≃ 0.07–0.17 is asserted without derivation. The inequality, the squared dependence, and the numerical window are unexplained. An energy density fraction ceiling cannot be accepted without a clear derivation or citation.
Required fix: Provide a derivation (spectrum, source, transfer to today), not just a schematic bound, or remove Barrier 12 entirely.

P1A-E5 (Throughout; especially pp. 4–8, 11, 15–18, Table I p. 4, Table IV p. 20)
Problem: Heavy reliance on unpublished “companion” works for essential numerical claims. Key numbers (H0 = 67.68 ± 1.06, ∆Neff posterior, NaMaster validation, ALP parameter fits, “309,189 frozen accepted samples”) and conclusions (galaxy spin null, PTA spectral index, SPHEREx forecast) are deferred to “Paper I(b) [6], Paper II [2], Paper III [46], Paper IV [23]—all in preparation.” PRD requires that quantitative claims in the submitted paper be supported by published or fully included analyses.
Required fix: Either (i) make the present paper entirely self-contained (include the relevant MCMC setup, priors, posteriors, diagnostics; the NaMaster pipeline validation; the ALP fit; the galaxy-spin classifier performance and null test), or (ii) strip the paper of all claims depending on these external works and restrict to statements you actually derive here. “Internal documentation” is not acceptable.

P1A-E6 (Abstract p. 1; Sec. I p. 3; Sec. XIII p. 16; Sec. XV p. 18)
Problem: Mixing significances from different experiments/procedures without explicit “not directly comparable” qualifiers at each juxtaposition. The text presents βobs = 0.342° ± 0.094° (∼3.6σ) and ACT DR6 β = 0.215° ± 0.074° (∼2.9σ) side by side in multiple locations. The paper should explicitly state these are independent analyses with different systematics and that the σ values are not directly comparable each time they are juxtaposed.
Required fix: Add an explicit, local qualification “the two σ values are not directly comparable” at every juxtaposition (Abstract; Sec. III A; Sec. IV D; Sec. VI; Sec. XIII; Conclusions).

MAJOR

P1A-M1 (Sec. X pp. 14–15)
Problem: “Perturbation-transparency theorem” is presented as a five-bullet sketch, but for a claim “at all perturbation orders” PRD requires a precise variational statement. The proof as written conflates Holst with Pontryagin (see E1) and does not show the vanishing of all interaction vertices in the scalar and tensor cubic and higher-order actions; it also omits boundary-term handling in cosmological perturbation theory.
Required fix: Provide a formal derivation from the ECH action with scalar matter: vary the full action, integrate out torsion explicitly, show that the resulting metric perturbation action reduces identically to GR to all orders (or at least up to cubic, where observables like fNL live), and treat boundary terms carefully. Cite or reproduce a known theorem if available.

P1A-M2 (Sec. II C 1 pp. 6–7; Eq. (11); “Reheating thermal-reset barrier”)
Problem: The dilution factor Dinf = e−3Ntot × (Treh/MGUT)3/2 is introduced by dimensional arguments, not by a concrete calculation. The half-integer power is justified as “aesthetic phase-space ansatz” and is then used in quantitative Ntot claims and structural tension arguments. The “thermal reset” paragraph asserts washout of ⟨J5µ⟩ with scaling of rms fluctuations as √nψ/T1/2reh without a kinetic calculation.
Required fix: Either derive Dinf from a concrete model (species, cross sections, Boltzmann equations, matching across the bounce and reheating), or remove all quantitative uses of Dinf and Ntot. Similarly, either compute the washout of axial currents (rates vs Hubble) or present this as qualitative speculation and do not use it to “close” routes.

P1A-M3 (Sec. IV A p. 8; Eq. (13))
Problem: The four-fermion NJL term is quoted with a specific coefficient −3κ/16 (parity-even), but the route-closure relies only on hand-waving “at cosmological densities it is too small.” No numbers are shown for realistic nψ at recombination or later, nor is there a quantitative bound.
Required fix: Provide an explicit upper bound: pick the largest plausible nψ (e.g., relativistic or nonrelativistic regimes), compute ρNJL ∼ κ n^2, and compare to ρΛ numerically with units. Include neutrino backgrounds if relevant. This is straightforward and should be shown.

P1A-M4 (Sec. IV C p. 10)
Problem: “Immirzi running” closure by “mass-dimension lock.” The given ansatz dγ/dlnµ ~ (NLF − NRF) γ/(12π^2) is not the calculation of Benedetti & Speziale (2011) and the final suppression estimate ∼ (∆γ/γ)(H/MPl) ≃ 10^−63 is heuristic. No explicit operator is given nor its contribution to an observable.
Required fix: Either use the actual computed β-function (with its γ-dependence) and propagate it into a specific observable with a clean derivation, or drop the quantitative closure.

P1A-M5 (Sec. IV D p. 10; Eq. (17))
Problem: The ALP birefringence mapping β = (α/M) √(2ρθ)/mθ is presented without derivation and then used to argue a “naturalness objection.” While the scaling is plausible (β ≈ (g/2) Δϕ with ρ ≈ m^2ϕ^2/2), the factor-of-two and time evolution from recombination to today are not treated, nor are constraints from limits on EB/TB frequency dependence. If this route is presented as closed by naturalness, the calculation needs to be explicit.
Required fix: Derive β in an FRW background from L ⊃ −(g/4) ϕ F F̃, show Δϕ from zrec to 0, and demonstrate quantitatively that ρθ must match ρΛ only for mθ ≈ H0 with your fitted g, including units. Otherwise, reframe as an observation (“fits exist but require tuning”) with no quantitative closure.

P1A-M6 (Sec. II B p. 6; Eq. (9))
Problem: You use γSU(2) = 0.274 from BH entropy counting to quote ρcrit ≃ 0.27 ρPl “as an internal extrapolation across counting schemes.” This is not a published LQC value and mixing counting-scheme γ into cosmological LQC formulas needs explicit justification. As written it can mislead.
Required fix: Either quote only the standard LQC result (γ = 0.2375 → ρcrit ≃ 0.41 ρPl) with reference, or show that the ρcrit formula holds for arbitrary γ and discuss scheme consistency. Clearly label the 0.27 number as your extrapolation (separately from the published 0.41).

P1A-M7 (Throughout; eg. Table I p. 4; Sec. V p. 11; Sec. XIII p. 16)
Problem: Inclusion of multiple programmatic, result-like statements that are not part of this paper’s contribution (SPHEREx fNL forecast, galaxy-spin ML classifier null, PTA KDE analysis, MCMC chain counts). This blurs scope and undermines verifiability.
Required fix: Trim all non-essential, non-self-contained results. Limit the paper strictly to derivations actually performed here. Move program logistics to a separate white paper or append only after acceptance with archived companion papers.

P1A-M8 (Bibliography; multiple entries)
Problem: Several citations appear to future-dated works with speculative arXiv numbers and no stable DOIs (e.g., [5], [41]–[45], [47]) or to “companion” notes “available upon request.” PRD requires stable references for load-bearing claims.
Required fix: Replace with published/posted references or remove.

MINOR

P1A-m1 (Sec. III A p. 7; Eq. (12))
Problem: The small-angle EB formula CℓEB ≈ 2β (CℓEE − CℓBB) is fine, but later the paper uses this to speak about “qualitative consistency” with observed β without an explicit photon–torsion coupling. This can confuse readers.
Required fix: Add a sentence stating explicitly that no photon–torsion coupling is derived in this paper and β is only discussed in the context of a spectator ALP in standard axion electrodynamics.

P1A-m2 (Sec. I p. 5 “Companion paper” paragraph; Table IV p. 20)
Problem: Inclusion of internal run labels (e.g., “Cobaya v3.6.1, 309,189 frozen accepted samples”, “hUBIFY-2026-001B”).
Required fix: Remove internal identifiers and “frozen samples” language. If MCMC is relevant here, include a standard Methods section; if not, delete.

P1A-m3 (Sec. XII A p. 15–16; Appendix B p. 19–20)
Problem: Mixed claims about “fine-tuning reduction from 10^122 to 10^5” due to Dinf; then later acknowledgement this is only a reparameterization and not an actual solution. This could mislead.
Required fix: Tighten language to avoid implying the hierarchy is “reduced.” State plainly that no progress on the CC problem is achieved; a parameter redefinition is not a solution.

P1A-m4 (Formatting/typography; throughout)
Problem: Various diacritics and spacing issues (e.g., “Poincar´e,” “Domaga la,” “capitilization of ECH”).
Required fix: Standardize names and accents.

NIT

P1A-n1 (Sec. IV Scope p. 8–9)
Problem: Overuse of meta-language (“channel-level enumeration,” “amplitude budget granularity”).
Required fix: Simplify for clarity.

P1A-n2 (Figure 1 p. 4; Table I p. 4)
Problem: Figure and table largely summarize program plans and not results in this paper.
Required fix: Consider moving to Supplementary Material or trimming.

Arithmetic/consistency spot checks

- Eq. (9): ρcrit formula numerically yields 0.41 ρPl at γ = 0.2375 and ≈0.27 ρPl at γ = 0.274 — OK.
- Eq. (13): Ltor = −(3/16) κ (J5)^2 with κ=8πG → coefficient −(3πG)/2 — consistent.
- ALP energetics (Sec. IV D): With α/M = 10^−21 GeV^−1 = 10^−30 eV^−1, β ≈ 6×10^−3, mθ ≈ 1.5×10^−33 eV → ρθ ≈ O(10^−11) eV^4 — within factors of order unity of (2.3 meV)^4, OK as an OOM.
- LiteBIRD differential test (Sec. XV): |0.342−0.27| / sqrt(0.03^2+0.094^2) ≈ 0.72–0.73σ — OK.
- “e^{32}” scaling (Abstract): Ntot − Nexit = 32 → e^{32} ≈ 8.9×10^{13} — OK.

Length/scope
For the claimed contribution, the paper is too long and diffuse (21 pages) with large sections devoted to program management and companion work advertising. If resubmitted, I recommend a maximum of ~12–14 pages focusing strictly on:
- a corrected, rigorous perturbation-transparency derivation;
- clean, self-contained closures of R1–R4 with explicit, dimensionally consistent calculations or clear statements of limits;
- removal of all “in preparation” dependencies.

## Summary recommendation
REJECT

The manuscript contains a fundamental theoretical error (Holst–Pontryagin conflation), relies on a dimensionally inconsistent operator ansatz for its key numerical claims, and depends pervasively on unpublished companion papers for essential results. Several “route closures” are asserted without derivations connecting the postulated operators to observables. Substantial restructuring, corrected derivations, and self-contained analyses would be required for PRD. I encourage the authors to prepare a shorter, rigorous paper focused on the corrected perturbation-transparency theorem (with a proper Nieh–Yan treatment) and on any route closures they can demonstrate from a consistent EFT.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (second-pass audit for arithmetic, consistency, and rigor)

Only new issues are listed below. I do not repeat items from the first report.

ESSENTIAL

P1A-E7 (Sec. II A 1; Eq. (1), dimensional/variational consistency; Class C)
Problem: Action-level inconsistency in the treatment of torsion. Eq. (1) includes a +¼ TabcTabc term within the same 1/(16πG) bracket as the EH+Holst sector, then states this is “a shorthand for the four-fermion contact interaction obtained after integrating out torsion; it is not an independently specified kinetic term.” Including TabcTabc in the starting action while also intending to integrate torsion out double-counts and changes the algebraic torsion equation. As written, variation with respect to the connection sees an explicit T^2 term and does not reproduce the standard EC algebraic elimination.
Required fix: Remove the explicit T^2 self-interaction from the starting action and derive it by integrating out torsion, or else keep it and consistently rederive the Cartan equation and the induced 4-fermion sector. Clarify which path is used and make the variational steps explicit.

P1A-E8 (Sec. II C; Eq. (10) vs. text in Sec. II C and Appendix B; Classes C, A)
Problem: Λeff vs ρΛ mapping is inconsistent and under-specified. Eq. (10) defines Λeff = Ξ MPl^2 + cω ω^2, while elsewhere you use ρΛ = Ξ MPl^4. This is only consistent if ρΛ = Λeff MPl^2 (up to reduced/ unreduced conventions), but those conventions are never fixed and the 8π factors are not tracked. Several numerical claims (e.g., Ξ ≈ 10−123) implicitly assume one convention.
Required fix: State explicitly whether MPl is reduced (2.435×10^18 GeV) or unreduced (1.22×10^19 GeV), give the relation between Λ and ρΛ used throughout, and recompute all occurrences of Ξ, Ntot, and products like (α/M)MPl accordingly. Track factors of 8π consistently.

P1A-E9 (Sec. II C 1, paragraph “Order-of-magnitude matching…”, lines 3–9; Class C)
Problem: Incorrect operator scaling. The text justifies a ∝ a−3 dilution using “the cube of the fermion bilinear scales as the cube of the fermion number density,” referring to “the cubic axial-current operator.” The axial current J5 is a bilinear; torsion in EC is linear in J5, not cubic. The a−3 scaling of a number density does not require nor justify a “cube of the bilinear” argument. This conceptual error undermines the Dinf scaling rationale.
Required fix: Remove references to a “cubic” axial-current operator. If you want Dinf ∝ a−3, derive it from the linear Cartan relation T ∝ J5 and the standard number-density dilution for the specific species that sources J5, or drop Dinf-based numerics.

P1A-E10 (Sec. II A 2; Eq. (7); Class C)
Problem: Dimensional inconsistency in the “one-loop estimate” of α/M. You write α/M ∼ (g^2/32π^2)(γ/M) ln(Λ^2/μ^2) + δNY. The first term has 1/M dimension; δNY is added but not defined dimensionally (Nieh–Yan contributions are power-divergent and require careful regularization). No citation is given that derives this particular combination.
Required fix: Either provide a published derivation with the full coefficient structure (including the treatment of Nieh–Yan power divergences and scheme dependence) or remove Eq. (7). As written, it mixes dimensions and schemes.

P1A-E11 (Sec. II C; “CMB isotropy bounds give (ω/H)0 < 5×10−11 [21]”; Class J)
Problem: Potentially incorrect numerical bound and referencing. Saadeh et al. (2016) give limits that depend on Bianchi model assumptions; the value 5×10−11 is not obviously present in that paper in this exact form. As given, the number appears uncited or mismatched.
Required fix: Quote the exact bound (with confidence level and model assumptions) from [21] or another primary source and reconcile the numerical value in text with the source.

P1A-E12 (Sec. IX A; Eq. (18); Class C)
Problem: Undefined symbols and dimensional mismatch in Barrier 1. geff ∼ 1/(MPl√|t3|) ∼ H0/MPl is asserted, but t3 is never defined and the equality requires √|t3| ≈ 1/H0 without justification. As written, the step from the left expression to H0/MPl is unsupported.
Required fix: Define t3, show the derivation of geff, and check dimensions. If the intended result is geff ∼ H0/MPl, derive it transparently; otherwise remove or restate Barrier 1.

P1A-E13 (Internal cross-reference; Sec. IV E, last paragraph; Class D)
Problem: Misplaced cross-reference. The sentence “The condensate mechanism … is documented in Sec. X as a quantitative closure” is incorrect; Section X treats perturbation transparency, not a condensate calculation.
Required fix: Correct the reference or remove the sentence.

P1A-E14 (Planck-mass convention; multiple loci incl. Eq. (9), Eq. (15), Appendix B; Class C)
Problem: Inconsistent MPl convention. Some numerics use MPl ≈ 10^19 GeV (unreduced), others implicitly assume the reduced Planck mass. This affects products like (α/M)MPl (10−2 vs 2.4×10−3), Ntot back-of-the-envelope, and ρcrit numerics.
Required fix: Declare a single Planck-mass convention up front and recompute all dependent numbers. Where literature values (e.g., LQC ρcrit) assume reduced MPl, state that explicitly.

MAJOR

P1A-M9 (Sec. X B–D; boundary terms; Class C)
Problem: Boundary-term handling is missing in the “transparency” argument. Even if the Holst contribution reduces to a total derivative after torsion elimination, in cosmological perturbation theory surface terms at fixed conformal time can contribute to cubic actions. No boundary analysis is provided (and the Holst–Pontryagin conflation noted previously aggravates this). 
Required fix: Provide a variational derivation through at least cubic order showing that all boundary terms generated by the Holst/Nieh–Yan sector vanish or cancel, or restrict the claim to linear order.

P1A-M10 (Sec. X; Abstract; independence claims; Class G)
Problem: “13 logically-independent” constraints are asserted without a demonstration of independence. Several barriers overlap conceptually (e.g., B8 parity-even interaction and B14 transparency) and others (B5 “scale separation,” B10 “UV→IR specificity”) appear to restate similar points.
Required fix: Either provide a brief dependency graph clarifying which barriers are corollaries of others (and reduce the “logically-independent” count accordingly) or soften the language to “catalog of constraints” without independence claims.

P1A-M11 (Sec. IV E; Table II note; Class E)
Problem: Juxtaposition of non-comparable null procedures. You compare a bespoke PTA “real-KDE γ” with a theoretical matter-bounce γ=3.0 and quote a “+1.13σ” agreement. The σ is from a nonstandard estimator in a companion “in preparation” work; comparability and calibration to standard practice are not established.
Required fix: Either remove this comparison or provide a self-contained description of the KDE likelihood, its null test and calibration, and how σ is defined and validated against standard PTA pipelines.

MINOR

P1A-m5 (Sec. II A 2; Eq. (5)–(6); Class C)
Problem: Ambiguity in F[K, R˚] notation. Eq. (5) writes FIJ[K, R˚] and then simply uses FIJρσ in components. It is unclear whether F is the full curvature 2-form of the torsionful connection, the Levi-Civita R˚, or some hybrid. The mass-dimension count in Appendix B assumes one choice, but the text does not state it.
Required fix: Define F explicitly (which connection?), stick to that choice, and align the dimensional analysis accordingly.

P1A-m6 (Sec. VIII; citations [41]–[43]; Class G)
Problem: Claims that recent works provide “independent support” (e.g., torsion fits S8 tension, torsion condensation) are made without quantitative comparison or caveats about model differences. The cited works (some future-dated) may not match your minimal-ECH assumptions.
Required fix: Qualify these as thematically related rather than direct support, or add a short paragraph explaining model differences and why results are or aren’t transferable.

P1A-m7 (Sec. II B; “parent black hole mass must exceed Mcrit ≈ 10−3 M⊙”; Class G)
Problem: Uncited, underived threshold. No reference or derivation is provided for Mcrit.
Required fix: Add a derivation or citation, or remove.

P1A-m8 (Table II; naming consistency; Class D)
Problem: The caption notes B8 is “not independent” because of B14, yet elsewhere (Sec. IX H and N) these are both listed as distinct barriers without an explicit dependency arrow.
Required fix: Harmonize the presentation: either collapse B8 into B14 or mark it as a corollary wherever both are listed.

NIT

P1A-n3 (Sec. II C 1; phrasing; Class H)
Problem: “r.m.s. residual scales as √nψ/T1/2reh” is a dimensional non sequitur as written and is presented as if derived from fluctuation-dissipation. This invites confusion.
Required fix: Rephrase clearly as a qualitative statement (if you keep it) and avoid giving a misleading scaling unless it is derived.

P1A-n4 (Figure 1 caption vs body; Class B)
Problem: The figure summarizes programmatic pathways and marks ECH as “structurally closed (this paper)”; the body (Sec. IV Scope; Conclusions) repeatedly emphasizes “channel-level, not operator-basis” closure. The figure does not carry that qualifier.
Required fix: Add “channel-level under stated assumptions” directly to the caption or figure label.

P1A-n5 (Notation; throughout; Class C)
Problem: Alternating use of εµνρσ vs ϵµνρσ and mixed index placements (e.g., FIJρσ vs Rabµν) without a conventions section. 
Required fix: Add a short conventions box (signature, ε normalization, reduced vs unreduced MPl, connection and curvature definitions).

Explanation
This second pass focused on arithmetic checks, dimensional consistency, cross-references, and null-procedure comparability. The most consequential new issues are (i) the inconsistent and variationally problematic inclusion of T^2 in the starting action (E7), (ii) Λ–ρ mapping and Planck-mass convention inconsistencies (E8, E14), and (iii) conceptual errors in the Dinf scaling argument (E9). Several additional cross-reference and notation problems also remain.