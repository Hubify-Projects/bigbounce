# P1A auto-2026-06-06_0021pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (9306 chars)
**Wall time**: 308.0s

---

Referee report on “Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter”

Scope of review
- Focus: methodology rigor, derivations, dimensional analysis, internal arithmetic, significance claims, estimator declaration, reproducibility.
- I audited every equation, table, and all load-bearing numbers in the abstract and conclusions for internal consistency and traceability to the body text.

Overall assessment
The manuscript presents an ambitious “channel-level closure” of four minimal ECH routes to dark energy and states a “perturbation-transparency” result. However, the analysis as written does not meet Physical Review D methodological standards. Central quantitative inputs depend on unpublished companion works “in preparation,” the key parity-odd operator used to connect ECH to dark energy is explicitly acknowledged to be non-EFT (dimensionally inconsistent off shell), several central claims (ALP tuning, observed β) are internally inconsistent across sections, and multiple barriers are asserted without derivations. The text also includes internal project codes (“hUBIFY-…,” “this volume”) and real-time chain-status notes inappropriate for a PRD article.

Below I list specific findings with severity, location, citation, and required remedy.

ESSENTIAL findings (acceptance blocked until addressed)

P1A-E1
- Section: Abstract (p.1), throughout (e.g., pp.4–5, 8, 11, 15–16, 18–20)
- Problem: Reliance on unpublished “companion” papers for primary numerical inputs and validation (e.g., ΛCDM+ΔNeff MCMC posteriors, NaMaster validation, ALP fits, SPHEREx forecast, galaxy spin catalog) with statements like “companion work in preparation [2, 6]” and internal codes (“hUBIFY-2026-001B”).
- Required fix: Make the manuscript fully self-contained or cite posted, citable arXiv preprints with the complete methods, data, and results used here. Remove all dependence on unpublished/“in preparation” analyses from claims, tables, and figures. If results depend on those, either include full methods and results here or defer claims until those works are public and citable.

P1A-E2
- Section: II.A.2 (pp.5–6), Appendix B (p.19)
- Problem: Central parity-odd operator Eq. (6) is explicitly non-EFT: off-shell mass dimension +1 rather than +4; mapping to ρΛ uses an on-shell scaling ansatz [(α/M) MPl] MPl^4 without a controlled derivation. Yet this operator underpins amplitude budgets, Ntot estimates, and several “closures.”
- Required fix: Provide a consistent, local, diffeomorphism-invariant, dimension-4 operator-level construction (including all needed powers of MPl in the coupling) and re-derive all amplitude budgets from that EFT; or surgically remove all claims and numerical inferences that rely on Eq. (6)/Appendix B and recast them as clearly speculative, without quantitative closure statements.

P1A-E3
- Section: IV.A vs II.A.2 (pp.8–9 vs. p.5)
- Problem: Inconsistent four-fermion coupling. Eq. (4) includes a Holst-dependent factor γ^2/(γ^2+1); Eq. (13) does not. The text later claims “torsion-elimination map is independent of γ at the classical level,” contradicting Eq. (4)’s γ-dependence.
- Required fix: Use a consistent derivation (with citations) for the axial–axial contact term in the Holst-extended EC theory. Either include the γ-factor everywhere or justify precisely the limit/assumptions under which it drops out. Recompute any amplitude budgets that depend on this coefficient.

P1A-E4
- Section: X (p.14), Abstract (p.1)
- Problem: The “perturbation-transparency theorem” is asserted but not rigorously derived. The scalar case is sketched; the tensor case is asserted via bullet points without a full variation-of-action demonstration including boundary terms and gauge subtleties. The extension “to all perturbation orders” is claimed without proof.
- Required fix: Provide a complete derivation (or cite a rigorous published proof) showing that, for canonical scalars, torsion vanishes identically, the Holst sector reduces to Pontryagin, and contributes only a boundary term at any perturbative order—explicitly demonstrating that no parity-violating terms enter the quadratic and cubic actions for scalar and tensor perturbations. Include discussion of boundary conditions and possible residuals.

P1A-E5
- Section: II.C Eq. (10) (p.6)
- Problem: Dimensional inconsistency and definition mismatch. “Λeff = Ξ M^2_Pl + cω ω^2” is dimension-2 if Λ denotes the cosmological constant, but the manuscript repeatedly equates Ξ with the dimensionless energy-density ratio ρΛ/M^4_Pl. Connection between Λeff and ρΛ is not defined, yet Ξ is used as “dark energy scale.”
- Required fix: Define conventions unambiguously: whether Λ is a curvature-scale (mass^2) or ρΛ is an energy density (mass^4), and how Ξ enters. Ensure all equations are dimensionally consistent and that usage of Λ vs ρΛ is coherent across the text. Revisit any numerical statements predicated on Eq. (10).

P1A-E6
- Section: XII.B (p.16) vs. IV.D (pp.10–11)
- Problem: Contradictory statements about ALP fine-tuning. Sec. IV.D argues reproducing ρΛ with the birefringence-fitted coupling requires mθ ≈ H0, calling it “precisely the cosmological constant problem in disguise.” Sec. XII.B states, “A spectator ALP with fa ∼ MPl, m ∼ H0 is consistent … without fine-tuning.”
- Required fix: Resolve the contradiction. Either acknowledge the tuning explicitly throughout or justify why mθ ∼ H0 is not a fine-tuning. Align the discussion in IV.D, XII.B, and the Conclusions.

P1A-E7
- Section: Abstract (p.1), III.A (p.8), VI (p.11), XV (p.18)
- Problem: Sigma values from different analyses are juxtaposed without the explicit “not directly comparable” qualifier mandated by the journal’s statistical reporting standards. Examples: “βobs = 0.342° ± 0.094° (~3.6σ) … comparable to ACT DR6 … 0.215° ± 0.074° (~2.9σ).”
- Required fix: Wherever significance values from different pipelines/instruments are placed side-by-side, explicitly mark them as not directly comparable and state the null hypotheses and analysis differences. Provide a consistent framework if you combine them; otherwise, avoid comparative language.

P1A-E8
- Section: Table III and its footnote (p.16)
- Problem: Real-time status of an ongoing MCMC chain (“chain … reports R̂−1 ≈ 3×10−2 … we deliberately do not commit to a specific calendar date”) appears inside the manuscript, as does the statement that no free-w0wa samples exist in frozen chains.
- Required fix: Remove all real-time and lab-notebook content. Only include results from completed, converged analyses with full methods, diagnostics, and posted data. If no w0wa chains exist, delete claims contingent on them.

P1A-E9
- Section: II.A.2 Fig. 2 caption and body (pp.5–6), XIV.A (p.17), Appendix B (p.19)
- Problem: Two inconsistent headline values for Ntot to match ρΛ: Ntot ≈ 92 in the main text vs ≈ 94 in Appendix B. The manuscript attempts to rationalize a 2% “ansatz dependence,” but the headline number is used repeatedly as a firm target (e.g., in the tension with SPHEREx).
- Required fix: Present a single, consistent estimate with an uncertainty band reflecting all sources (ansatz, area-gap scheme, reheating T uncertainty). Propagate that uncertainty to any downstream “tension” claims. Preferably quote an interval (e.g., Ntot = 93 ± 2) and adjust the discussion accordingly.

P1A-E10
- Section: III.B (p.8), V (p.11), XIV.B (p.17), Acknowledgments (p.18)
- Problem: Galaxy spin “confirmed null” and pLEE < 10−4 result are claimed but all methods and numbers are deferred to “Paper IV [23] (in preparation).”
- Required fix: Either remove the galaxy-spin claims from this manuscript, or include the full dataset description, classifier architecture, bias audits, sample sizes, sky masks, estimators, null tests, and uncertainty accounting sufficient for independent reproduction.

P1A-E11
- Section: Throughout (e.g., pp.4–5, 15–16, 18–20)
- Problem: Internal project codes/phrases inappropriate for a journal article: “hUBIFY-2026-002,” “this volume,” “companion technical note, available upon request,” etc.
- Required fix: Remove all internal codes and “this volume” language. Replace with standard citations to published or posted works, or integrate necessary content here.

P1A-E12
- Section: II.C “Parameter naturalness” (p.6)
- Problem: “The parent black hole mass must exceed Mcrit ≈ 10−3 M⊙” is asserted without derivation or citation. This is a load-bearing numerical threshold for the scenario.
- Required fix: Provide a derivation and/or cite a peer-reviewed source. Quantify any dependence on assumptions (spin, EoS, collapse model, torsion strength).

MAJOR findings

P1A-M1
- Section: II.A.2 (p.6), IV.D (pp.10–11), XII (p.15), XIII (p.16)
- Problem: Observed birefringence central value is repeatedly conflated with a “benchmark” 0.27°; at one point (p.8) the text states “observed isotropic birefringence at β ≈ 0.27°–0.30°,” inconsistent with the quoted WMAP+Planck βobs = 0.342° ± 0.094°.
- Required fix: Correct the description: 0.27° is your chosen benchmark, not the observed central value. Ensure all references to “observed” use the quoted βobs = 0.342° ± 0.094°, and clearly separate benchmarks from measurements.

P1A-M2
- Section: IV.B Eq. (15) (p.9)
- Problem: The one-loop bound is presented as a “canonical” estimate but critical assumptions are not enumerated (e.g., precise operator normalization, identification of θ, smoothness assumptions, time dependence of ∂μθ).
- Required fix: List all assumptions explicitly and, where possible, bound their impact. Present the calculation in a dimensionally transparent way (e.g., with all numerical constants and units) and show the numerical evaluation to reach the 10−58–10−60 range.

P1A-M3
- Section: IX.A Eq. (18) (p.12)
- Problem: Undefined symbol t3 appears in geff ∼ 1/(MPl √|t3|) ∼ H0/MPl without definition or derivation. The step to H0/MPl is not justified.
- Required fix: Define t3 and derive Eq. (18) or remove the equation. If geff scaling is asserted, provide a model and steps leading to H0/MPl.

P1A-M4
- Section: IX.L Eq. (20) (p.13)
- Problem: Claim that ΩGW|bounce ≲ (ρcrit/ρPl)^2 without derivation. No clear link from bounce energy density to GW energy density fraction is given.
- Required fix: Provide a derivation (or a clearly labeled conservative bound) connecting torsion/holonomy corrections at the bounce to a bound on ΩGW, with assumptions and transfer-function evolution to today. Otherwise, delete Eq. (20).

P1A-M5
- Section: II.A.1 Eq. (1) (p.5)
- Problem: Action includes a Tabc Tabc term “as shorthand” inside the overall 1/(16πG) prefactor. This risks double counting and blurs the distinction between fundamental and induced terms. The dimensions also become ambiguous.
- Required fix: Write the fundamental EC-Holst action without an ad hoc T^2 term. If you wish to include the four-fermion effective interaction, do so after integrating out torsion, in a separate, clearly normalized effective Lagrangian, with the correct coefficients.

P1A-M6
- Section: XII.A (p.15), Appendix B (p.19)
- Problem: Internal arithmetic on the CC hierarchy: some places speak of “reduction from 10^120 to 10^5,” others of the “genuine M^4_Pl/ρΛ ≈ 10^122.” The presentation is confusing.
- Required fix: Use a single consistent figure for the CC hierarchy (≈10^122), state assumptions (unit conventions), and clarify precisely what is being “reparameterized” (sensitivity to Ntot), avoiding any suggestion that the hierarchy is reduced.

P1A-M7
- Section: Bibliography (pp.19–21)
- Problem: Several citations are to “in preparation,” “companion technical note available upon request,” and internal URLs; PRD requires stable, public citations.
- Required fix: Replace with arXiv identifiers or published references, or remove claims dependent on non-public sources.

MINOR findings

P1A-m1
- Section: II.B Eq. (9) (p.6)
- Problem: The ρcrit formula matches the standard LQC expression; however, you should show the intermediate step (ρcrit = 3/(8πG γ^2 Δ) with Δ = 4√3 π γ ℓP^2) for clarity, since you use it to justify the 0.27–0.41 ρPl range.
- Required fix: Add the intermediate expression and one-line derivation for readers to verify the numerical range.

P1A-m2
- Section: I.A (p.3), VIII (p.12), Bibliography (pp.19–21)
- Problem: Name formatting/diacritics: “Pop lawski” appears with a space; standard usage is “Popławski” (or “Poplawski” without diacritics). “Domaga la” has stray space/diacritic issues.
- Required fix: Standardize author names and ensure consistency with cited works.

P1A-m3
- Section: Table I (p.4) and associated footnotes
- Problem: Formatting glitches in footnote markers (e.g., “b
3–5σ realistic…”), unclear superscripts, and cluttered prose in a summary table.
- Required fix: Clean formatting, move extended caveats from the table to the main text, and keep the table compact.

P1A-m4
- Section: III.A (p.8)
- Problem: Eq. (12) Cℓ^EB ≈ 2β (Cℓ^EE − Cℓ^BB) is valid for small, spatially uniform rotations; specify the small-angle approximation explicitly and cite a standard derivation.
- Required fix: Add a citation and state the small-angle assumption.

P1A-m5
- Section: Acknowledgments (p.18)
- Problem: Statement about using an AI assistant may conflict with some journals’ disclosure norms and could raise questions about authorship contributions.
- Required fix: Ensure compliance with PRD’s authorship and AI-use policies; adjust or remove if non-compliant.

NITs

P1A-n1
- Section: Throughout
- Problem: Numerous hyphenation artifacts from PDF typesetting (e.g., “con­traction,” “over­predicts”).
- Required fix: Clean final typeset.

P1A-n2
- Section: PACS numbers (p.1)
- Problem: PACS are deprecated; APS now uses Physics Subject Headings (PhySH).
- Required fix: Update to current APS classification if required by PRD.

P1A-n3
- Section: Figure 1 caption (p.4)
- Problem: Schematic figure is helpful but lacks axes/units by design; ensure all figures are essential. If kept, state clearly that it is schematic.
- Required fix: Clarify as schematic or consider moving to Supplemental Material.

Additional observations on length and focus
- At 21 pages, the paper is long relative to the validated contribution. If the authors focus the paper on the perturbation-transparency result with a rigorous derivation and remove dependencies on unpublished companions, it could be substantially shortened (recommended: ≤12 pages), with purely phenomenological speculations (Ntot bookkeeping, galaxy spins, PTA γ) excised or moved to an appendix.

Arithmetic and dimensional spot checks
- R2 bound (Eq. 15): Using αem/(4π) ≈ 5.8×10−4, H0/MPl ≈ 1.2×10−61, MPl(α/M) ≈ 10−2 (for α/M ≈ 10−21 GeV−1), βobs ≈ 6×10−3 rad, gives Δθone-loop/Δθobs ≈ 1–2×10−60. The stated 10−58–10−60 range is acceptable given O(1) ambiguities noted.
- R4 inversion for ρθ: With mθ = H0 ≈ 1.5×10−33 eV, α/M = 10−21 GeV−1, β ≈ 6×10−3 rad yields ρθ ≈ 4×10−11 eV^4, consistent within factors of unity with ρΛ ≈ (2.3 meV)^4 ≈ 2.8×10−11 eV^4.
- LQC ρcrit (Eq. 9): Numerically reproduces 0.41 ρPl at γ = 0.2375 and 0.27 ρPl at γ ≈ 0.274; fine.

However, these checks do not mitigate the central methodological issues listed above.

## Summary recommendation
REJECT

The manuscript, in its current form, does not meet PRD methodological standards. Central quantitative claims depend on an explicitly non-EFT operator and on multiple unpublished companion papers; the key “perturbation-transparency” theorem is asserted without a rigorous derivation; there are internal inconsistencies (ALP fine-tuning, observed β), dimensional ambiguities (Λ vs ρΛ), unreferenced thresholds, and laboratory-style content (ongoing chain status) in the body. A substantially revised, self-contained paper that (i) rigorously proves the perturbation-transparency result, (ii) removes speculative dark-energy mappings based on nonlocal/on-shell ansätze, and (iii) excises all dependence on unpublished companions could be reconsidered, but that would constitute a different, much shorter submission.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (new issues only)

P1A-E13
- Section: IV.B Eq. (14), surrounding text (p.9)
- Problem: Dimensional inconsistency in the one-loop parity-odd operator. As written, Γone-loop ⊃ −(1/16π^2)(β(γ)/MPl)∫√−g ∂μθ J5μ. If θ is a standard angle-like pseudoscalar (dimension 0), then [∂μθ]=1 and [J5μ]=3, so [∂μθ J5μ]=4 and dividing by MPl yields a dimension-3 density. If θ instead has mass dimension 1 (axion-like), then [∂μθ]=2, giving [∂μθ J5μ]=5, and 1/MPl restores dimension 4 only if θ is dimension 1 and the suppression is 1/f with [f]=1, not necessarily MPl. The manuscript does not state the mass dimension of θ, yet uses 1/MPl. This renders Eq. (14) dimensionally ambiguous and undermines the subsequent amplitude bound (Eq. 15).
- Required fix: Specify θ’s mass dimension and the EFT normalization unambiguously. If θ is dimensionless (Nieh–Yan angle), remove 1/MPl and supply the correct loop-induced dimensionless coefficient; if θ is a dynamical pseudoscalar with [θ]=1, write the operator as (c/f)∂μθ J5μ with f carrying mass dimension 1 and justify f≈MPl (or not). Then redo the R2 amplitude estimate with the corrected normalization.

P1A-E14
- Section: Abstract (p.1) vs. Sec. IV.D/E (pp.10–11)
- Problem: Abstract states all four routes “fail at the amplitude level,” but the body explicitly says Route 4 (parity-odd CMB coupling) is not closed by amplitude but by a “naturalness objection” (mθ∼H0 tuning). This is an internal contradiction in how R4 is characterized.
- Required fix: Make the abstract consistent with the body. Either revise the abstract to say R4 is closed by a tuning/naturalness argument (not amplitude), or reframe R4 throughout as an amplitude-level exclusion and provide the missing amplitude derivation (which currently is not there).

P1A-E15
- Section: Data and Code Availability (p.18), multiple cross-references to companion Paper I(b)
- Problem: Reproducibility gap. The manuscript claims “All materials necessary to reproduce ... are publicly available” at the GitHub repository, but also states that “MCMC chains and convergence diagnostics are in companion Paper I(b) [6],” which is “in preparation.” If chains, diagnostics, and key numerical inputs (posteriors, ALP fits, NaMaster validation) are not publicly posted, the work is not currently reproducible.
- Required fix: Post all chains, diagnostics, and analysis scripts referenced in the text in a stable public location (arXiv/Supplemental Material/Zenodo link) and update citations accordingly, or remove all claims that depend on non-public artifacts.

P1A-E16
- Section: II.C.1 “Reheating thermal-reset barrier” (pp.6–7)
- Problem: Unsupported and dimensionally inconsistent scaling. The text asserts that the thermal expectation’s rms residual “scales as ∼√nψ/T1/2
reh,” which has mass dimension 1 rather than the 3 expected for J5μ (or 0 for a mean polarization fraction). No derivation or citation is provided, and the step is used to bolster a “thermodynamic closure.”
- Required fix: Provide a derivation (or peer-reviewed citation) for the thermal washout of ⟨J5μ⟩, including a dimensionally consistent expression and the dynamical rates vs Hubble. If unavailable, remove the quantitative scaling and recast the argument qualitatively, clearly separating it from any quantitative closure claims.

P1A-E17
- Section: Abstract (p.1), Sec. XIII–XV (pp.16–18)
- Problem: LiteBIRD “∼9σ” claim for β detection is presented without the null-procedure caveats that are essential for birefringence (e.g., angle-calibration degeneracy, self-calibration, method dependence on EB/TB estimators). Elsewhere the manuscript correctly cautions about comparability for WMAP+Planck vs ACT, but the same caution is missing for the LiteBIRD projection used as an anchor claim.
- Required fix: State the null hypothesis and estimator assumptions underpinning the 9σ projection, and explicitly note that this is contingent on an analysis that breaks angle-calibration degeneracy (e.g., Minami–Komatsu self-calibration). Otherwise, avoid precision-sigma language.

P1A-M8
- Section: II.A.2 Eq. (7) and paragraph below (p.6)
- Problem: The leap from Eq. (7) to “[(α/M) MPl] ∼ 10−2” is not demonstrated. With g2/(32π2)∼10−3–10−2, γ∼0.27, ln(ΛUV/μ)∼O(1–10), and M≈MPl, [(α/M) MPl] generically comes out 10−4–10−3 absent a finely tuned δNY. The text neither provides the numerical inputs nor the role of δNY needed to land at 10−2.
- Required fix: Show the numerical evaluation leading to 10−2 (with explicit choices of g, log, δNY), or quote a range reflecting the uncertainty (e.g., 10−4–10−2) and propagate that range wherever [(α/M)MPl] is used.

P1A-M9
- Section: IV.C (p.10)
- Problem: The statement “In the Standard Model ... Δγ/γ ∼ 10−2 over the running from the GUT scale to the IR” is asserted without derivation, reference, or specification of the β-function actually used. This value controls the R3 closure but is unsupported.
- Required fix: Provide a derivation or cite a calculation that yields Δγ/γ∼10−2 for the SM field content, including the RG interval and scheme. If such a result is not established, present the R3 conclusion as conditional on an assumed running and bracket the impact with a range.

P1A-M10
- Section: XIV.D (p.17), Abstract (p.1)
- Problem: “Definitively erased” matter-bounce fNL claim. The argument that Ntot≳60 “definitively” erases fNL at SPHEREx scales is asserted using a back-of-envelope e-fold mapping without a transfer of the bispectrum through inflation or a quantitative assessment of residual contamination vs survey sensitivity.
- Required fix: Either (i) provide a quantitative calculation of the contraction-origin bispectrum’s transfer and suppression to SPHEREx bands given Ntot and Nexit (including a shape-overlap with inflationary vacuum contributions), or (ii) soften the claim to a qualitative expectation and remove the word “definitively.”

P1A-M11
- Section: IV.E, XII.B, and Conclusions (pp.11, 16, 18)
- Problem: “Condensate mechanism yields a vacuum energy parametrically too large” is stated without any derivation, operator content, or numerical estimate. Since this is used to “close” a route, the absence of a calculation is problematic.
- Required fix: Either supply a concise derivation (or cite one) showing why the NJL-like condensate channel is parametrically too large in the present setup (with explicit γ dependence), or remove/relocate the claim as an unquantified aside.

P1A-M12
- Section: III.B (p.8), V (p.11), XIV.B (p.17)
- Problem: Claims of “refutes Shamir’s 3% asymmetry at high significance” are made alongside a “pLEE<10−4” without defining pLEE, its null procedure, or comparability to Shamir’s pipeline. These are different test statistics and nulls.
- Required fix: Define pLEE, its look-elsewhere correction procedure, and the test statistic. Explicitly state that this is not directly comparable to Shamir’s reported significance unless you reanalyze his data with your estimator; otherwise, avoid cross-pipeline significance language.

P1A-m6
- Section: Throughout (e.g., Table IV, Sec. II.A.1, Sec. X.G)
- Problem: Overloaded symbol γ: used for the Barbero–Immirzi parameter and for the PTA spectral index (γPTA). While γPTA is specified in Table IV, the text elsewhere uses “γ=3.0” (matter-bounce PTA) near discussions of γ=0.274 (Immirzi), inviting confusion.
- Required fix: Use distinct symbols throughout (e.g., γBI for Immirzi, γPTA for the spectral index), and avoid bare “γ” in contexts where ambiguity can arise.

P1A-m7
- Section: II.A.2 Eqs. (5)–(6) (p.6)
- Problem: Notation ambiguity: FIJ[K,Γ̊] is introduced without definition (is it the curvature of the total connection or a mixed functional?). Since operator counting hinges on which curvature enters, this should be clarified.
- Required fix: Define FIJ[K,Γ̊] precisely and state whether the contraction is taken on the Levi-Civita connection after eliminating torsion or on the full connection before integration-out.

P1A-m8
- Section: Figure 2 caption vs. Eq. (24) (pp.5, 15)
- Problem: In Fig. 2, ρvac is written as [(α/M) MPl] MPl^4 (a notationally unusual but dimensionally OK factoring), while Eq. (24) defines Ξ≡⟨(α/M)MPl⟩Dinf. The body alternates between treating [(α/M)MPl] as an O(10−2) number and as an average ⟨...⟩. The notation invites confusion about whether this factor is fixed or averaged.
- Required fix: Use a single notation for the dimensionless factor (e.g., codd≡(α/M)MPl) and state clearly whether it is treated as a fixed number, a nuisance parameter with a prior, or an average over high-scale microphysics.

P1A-m9
- Section: III.A (p.8)
- Problem: The small-angle EB formula is applied without mentioning lensing B-mode contamination, which determines whether the −CBB term can be neglected (often EB≈2β CEE in practice). The body text later uses EB heuristics.
- Required fix: Add a one-line note clarifying that in the lensing-dominated regime CBB≪CEE so CEB≈2β CEE is typically used, and cite a standard reference.

Explanation
These items are in addition to, and do not duplicate, the issues listed in my initial report. They focus on fresh checks of arithmetic/dimensions, abstract-to-body fidelity, notation clarity, reproducibility assertions, and missing derivations that were not previously flagged.