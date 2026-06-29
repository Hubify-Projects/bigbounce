# P1A RC-INT — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/arxiv/paper1a_ech_nogo.pdf` md5=94ce8f5c pages=32
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7455 chars)
**Wall time**: 314.6s

---

Referee report for PRD (Methodology/rigor audit)

General assessment
The manuscript undertakes an amplitude- and operator-accounting “channel-level” closure of four minimal Einstein–Cartan–Holst (ECH) dark-energy routes and states a perturbation-transparency theorem. The analysis is largely conceptual and dimensional, with explicit caveats where ansätze are used. However, several elements fall short of PRD standards for methodological rigor and reproducibility:

- The action presented mixes on-shell-eliminated terms into the fundamental variational functional, which is formally inconsistent.
- Several central quantitative statements rely on “in preparation/posted concurrently” companion papers; PRD requires that all load-bearing computations and numerical inputs be available and citable at submission time.
- The data/code availability lacks a frozen DOI and versioned artifact; some figures and tables present numbers from unpublished work.
- A few amplitude ceilings and “barriers” are stated without a transparent derivation, and some numerical bars/forecasts are juxtaposed with different null procedures and only sometimes caveated.

Below is a detailed, itemized audit with required fixes.

Findings

ESSENTIAL

P1A-E1
Location: Sec. II A 1, Eq. (1), p. 5
Problem: The action includes a +¼ TabcTabc term inside the 1/(16πG) bracket and later states it is “a shorthand for the four-fermion contact interaction obtained after integrating out the non-propagating torsion; it is not an independently specified kinetic term and is not varied independently”. Writing an on-shell-eliminated contact term into the action being varied is formally inconsistent—either it is part of the fundamental Lagrangian and must be varied, or else it must be introduced only after solving the Cartan equation.
Required fix: Remove the T^2 term from the fundamental action to be varied, and present the torsion-elimination and resulting four-fermion term in a subsequent effective action (after variation). Alternatively, explicitly split S = S_EC+Holst+Dirac and show the variation and elimination step, with the four-fermion piece only entering the post-elimination effective Lagrangian. Make the normalization consistent (κ, half/full-weight conventions) once and carry it through.

P1A-E2
Location: Multiple (abstract p. 1; Sec. I b p. 4; Table II p. 7; Sec. III B p. 11; Sec. XIII p. 22; Figs. 4, 7 captions)
Problem: Heavy reliance on “companion papers (in preparation; posted concurrently)” for MCMC posteriors, pipeline validation, forecasts (SPHEREx fNL), PTA index, and galaxy-spin results. PRD requires the paper to stand alone. Citing “in preparation” is not acceptable for any quantitative statement included in the submitted manuscript.
Required fix: Replace all “in preparation/posted concurrently” references with citable arXiv preprints or journal articles. If those works are not publicly posted, remove the numerical values from this manuscript or move them to a clearly marked non-load-bearing appendix explicitly labeled as illustrative only—and ensure they are not used in any claimed result. All load-bearing quantitative claims must be reproducible within this paper.

P1A-E3
Location: Data and Code Availability, p. 25
Problem: The repository is a mutable GitHub URL without a frozen snapshot, DOI, tag, or commit hash. The text promises a future Zenodo archive but does not provide it.
Required fix: Provide a permanent archived DOI (e.g., Zenodo) for the exact version used to generate all figures/tables, and list the commit hash(s) and instructions to reproduce each figure/table. If certain results come from companions, remove them or include their artifacts here as well.

P1A-E4
Location: Fig. 1 caption, p. 6; Sec. X G, p. 20; Table IV, p. 21; references [46]
Problem: Use of an unpublished “real-KDE reanalysis” yielding γ_PTA = 2.567 ± 0.382 to position bounce models. This is outside the paper’s scope and not citable. Including an unpublished value in a figure that may be interpreted as part of the analysis is not acceptable.
Required fix: Remove this number from the main text/figures or replace it with a published value. If retained as context, move it to a clearly marked non-load-bearing footnote and state explicitly that it is unpublished and not used in any claim.

P1A-E5
Location: Abstract, p. 1; Sec. II A 2, App. B p. 25–26
Problem: The paper’s central “parity-odd operator” has off-shell mass dimension +1 (Eq. 6), and the mapping to ρ_Λ is explicitly an on-shell scaling ansatz. While this is acknowledged in the body, the abstract presents closure statements that read stronger than an ansatz-based no-go might justify.
Required fix: In the abstract and conclusions, prefix every closure that relies on the on-shell scaling with “conditional on the scaling ansatz of Appendix B” and explicitly state that this is not an EFT-level derivation. Tighten language to reflect that R2–R3 closures are amplitude-level under this ansatz, not operator-level theorems.

P1A-E6
Location: Table II, p. 7; Sec. III A, p. 10; Sec. XIII, p. 22; Figs. 4, 7 captions
Problem: σ-values from different null procedures and pipelines (Planck/WMAP β, ACT β, SPHEREx forecast) are repeatedly compared. While some caveats appear, they are not consistently co-located with every juxtaposition.
Required fix: At every instance where σ from different nulls are listed side-by-side (table entries, figure captions, executive summaries), add an explicit sentence: “These significances arise from different null procedures and are not directly comparable.” You already include this in the abstract; replicate this warning everywhere such numbers are juxtaposed (e.g., Table I footnote b is fine; ensure the same in all figure captions and Section XIII).

P1A-E7
Location: Fig. 3 caption, p. 29; Eq. (10), p. 8
Problem: The bound on the rotation term relative to ρ_Λ is stated via a heuristic manipulation “(ω/H)_0^2 < 2.5×10^-21; dividing by 3Ω_Λ ≈ 2.1 gives ~1.2×10^-21 of ρ_Λ” without a clear derivation of how Λ_eff and ρ terms are connected dimensionally in that expression.
Required fix: Provide an explicit derivation for the ratio of the c_ω ω^2 contribution to ρ_Λ, including the exact prefactor chain from Λ_eff to ρ and the normalization conventions used. If the rotation entry is merely illustrative, move it to an appendix and remove the percentage-like statement from the caption.

MAJOR

P1A-M1
Location: Sec. IV B, Eq. (14), p. 12–13
Problem: The “one-loop parity-odd operator” is introduced as an EFT ansatz. The normalization and origin of β(γ) are not linked to a published calculation; the operator is then used to produce the amplitude-suppression estimate. This is acceptable as an upper-bound exercise, but the text needs to be unambiguous about its status and limiting assumptions.
Required fix: Add a short derivation sketch or explicit dimensional check (already partly present) and an explicit statement that Eq. (14) is an upper-bound EFT ansatz, not a direct consequence of Refs. [15,20]. Clarify whether ∂μϑ_NY carries mass dimension +2 and J_5^μ +3 so that the prefactor must be O(M_Pl^-1). Ensure units are consistently tracked in Eq. (15).

P1A-M2
Location: Sec. IV C, p. 13
Problem: Running of the Immirzi parameter: the ansatz dγ/d lnμ ≈ [(N_L^F−N_R^F)/(12π^2)] γ leads, with ln(μ_GUT/μ_IR) ≈ 30, to Δγ/γ ≈ 0.25 for unit chiral excess, not 10^-2–10^-1 as stated. The text later adopts 10^-2 “conservative”, but the simple estimate gives ~0.25.
Required fix: Correct the order-of-magnitude estimate or justify the smaller value (e.g., use Standard Model chiral count net N_L−N_R = 0 at high energies, or specify the actual field content and thresholding). If your closure does not depend on the precise value, state the insensitivity explicitly and provide a corrected numeric example.

P1A-M3
Location: Sec. II C 1 “Reheating thermal-reset barrier”, p. 9–10
Problem: The closure is framed “conditional on Γ_wash > H,” with informal rate estimates. The Yukawa estimate (Γ_y/H ∼ y^2 M_Pl/T) is fine; the sphaleron estimate is also qualitatively correct. However, the argument would benefit from at least one explicit numerical example at T_reh = 10^15 GeV showing Γ_t/H and Γ_sph/H values with chosen α_W, y_t and the implied timescale vs. H, since this is a central “erasure” mechanism.
Required fix: Add a one-paragraph numeric estimate at T=10^15 GeV: compute Γ_t/H and Γ_sph/H using explicit constants (e.g., α_W ≈ 0.03, y_t≈1) to support the conditional statement. Optionally include a brief line on whether right-handed neutrino interactions change the conclusion if they exist at that scale.

P1A-M4
Location: Barrier 12, Sec. IX L, p. 19
Problem: The “vacuum amplification ceiling” Ω_GW^ECH|bounce ≲ (ρ_crit/ρ_Pl)^2 ≃ 0.07–0.17 is stated as an ansatz without derivation. This reads like a quantitative constraint but lacks provenance.
Required fix: Either provide a derivation or a literature reference for the quadratic scaling and the numbers quoted, or relegate it to a qualitative ceiling and remove the 0.07–0.17 numeric range. If retained, clarify that this is not directly comparable to present-day PTA Ω_GW without a transfer computation.

P1A-M5
Location: Sec. II A 2, Eq. (7), p. 8
Problem: The numerical estimate “[(α/M) M_Pl] ≈ 3×10^-3” uses M = M_Pl/√γ. This is fine, but the log ln(Λ_UV^2/μ^2) ≈ 74 corresponds to Λ_UV ≈ M_Pl, μ ≈ TeV. Please add the intermediate step showing M_Pl/M = √γ to make the reader follow the 3×10^-3 result.
Required fix: Show explicitly: g^2/(32π^2) ≈ 2.9×10^-4; × γ ≈ 0.274 → 7.9×10^-5; × ln ≈ 74 → 5.8×10^-3; × (M_Pl/M)=√γ≈0.523 → 3.0×10^-3.

P1A-M6
Location: Sec. IV D, footnote 5, p. 15
Problem: Basis conversion between α/M and g_{aγ} is discussed qualitatively, but the sign and 2 vs. 4π normalization chains are easy to confuse. Since Eq. (C4) fixes the β normalization, the main text should cross-reference it.
Required fix: Add a one-line pointer “see Appendix C, Eq. (C4), for the exact β normalization and the g_{aγ} ↔ α/M mapping.”

P1A-M7
Location: Fig. 3 & Sec. III A, p. 10, p. 29
Problem: The H(z) comparison figure uses different H0 and Ω_m between the ECH-like benchmark and ΛCDM and then discusses 2–3% residuals. Although the caption explains this, the figure risks being misinterpreted.
Required fix: Provide an H0- and Ω_m-matched comparison panel (same baseline cosmology; only the extra terms toggled) or move the figure to appendix as purely illustrative, with a bold note that this does not visualize a measurable ECH signal.

P1A-M8
Location: Table V, Fig. 5 (bottom panel), p. 26, p. 31
Problem: Fine-tuning scores of 10^60 (quintessence) and 10^40 (f(R)) are shown as bars but marked “illustrative” in the caption. This presentation can be misleading without citations.
Required fix: Either (a) provide authoritative references supporting those specific orders of magnitude for the cited classes, or (b) remove the bars and replace them with a qualitative note. Retain only the values derived in this paper (ΛCDM 10^122; spin-torsion N_tot reparameterization 10^5).

P1A-M9
Location: Throughout (e.g., Sec. I b, p. 4; captions of Figs. 4, 7)
Problem: Version-history language (“posted concurrently”, “coordinated submission”) and internal program logistics appear in the body.
Required fix: Remove all version-history/process language from the scientific narrative. If you must mention companion works, cite public arXiv IDs without status notes.

MINOR

P1A-m1
Location: Sec. IV A, Eq. (13), p. 12
Problem: The sign and coefficient of the Hehl–Datta term are quoted as L = −(3/16) κ (ψ γ̄^a γ_5 ψ)^2. This is standard; nonetheless, since earlier footnotes discuss half-/full-weight torsion factors, please give a one-line cross-check reference (e.g., Hehl 1976 eqs.) right below Eq. (13) to settle normalization.
Required fix: Add “see Hehl et al. Rev. Mod. Phys. 48 (1976), Eqs. (3.20)–(3.21) for the normalization used here.”

P1A-m2
Location: Sec. II B, Eqs. (8)–(9), p. 8
Problem: You re-express ρ_crit as √3/(32π^2 γ^3) ρ_Pl; good. Add a small inline numeric check for γ=0.2375 yielding ≈0.41 and for γ=0.274 yielding ≈0.27 to aid the reader.
Required fix: Add the two-line numeric confirmation in-text or footnote.

P1A-m3
Location: Sec. III A, Eq. (12), p. 10
Problem: The “small-angle, uniformly-rotating sky” approximation is used. It’s standard, but add a sentence that your analysis does not itself fit β and that published estimators include lensing B as appropriate.
Required fix: One-line clarification.

P1A-m4
Location: Sec. X B, step 4, p. 19
Problem: Statement that ε^{μνρσ} R_{μνρσ}(Γ̊) ≡ 0 by the first Bianchi identity is correct for torsionless connections. For completeness, note explicitly that non-metricity does not spoil the algebraic Bianchi identity used (you mention this; retain it) and that this is distinct from Pontryagin RR̃.
Required fix: None beyond ensuring the distinction remains clear (it is).

P1A-m5
Location: Sec. IV D, Eq. (17), p. 15; App. C, Eq. (C4), p. 27
Problem: The β normalization is internally consistent (factor 1/2). Good. To improve readability, add a parenthetical “see App. C for derivation.”
Required fix: Add cross-reference.

P1A-m6
Location: Sec. II C, Eq. (11), p. 9
Problem: Dimensional form of the (T_reh/M_GUT)^{3/2} prefactor is explained as a phase-space ansatz. Since it is central to the N_tot bookkeeping, add a sentence that the dependence on this prefactor corresponds to at most O(few) e-fold shifts, not orders of magnitude (you hint at this in App. B).
Required fix: Add the sentence (or cross-reference App. B “sharper dependency statement”).

NIT

P1A-n1
Location: Abstract author footnote a, p. 2
Problem: Parenthetical “not to be confused with Pontryagin” is useful but long; consider moving most of it to the body (you already have it).
Required fix: Editorial.

P1A-n2
Location: Typographical consistency
Problem: Occasional hyphenation artifacts (“enumerated scaling ans¨atze”) likely from PDF extraction; ensure typesetting in final PDF is correct.
Required fix: Proofread final typeset.

Arithmetic/Dimensional spot-checks (passed)
- Eq. (7) numeric: [(α/M) M_Pl] = 3×10^-3 using M=M_Pl/√γ, ln(Λ/μ)≈74 → consistent.
- Eq. (15) dimensionless ratio: ∼10^-60 using α_em/(4π)≈5.8×10^-4, H0/M_Pl≈10^-61, M_Pl·(α/M)≈10^-2, β_obs≈6×10^-3 → consistent.
- Eq. (17) inversion: ρ_θ ≈ 2 m_θ^2 β^2 /(α/M)^2 → for m_θ=1.5×10^-33 eV, α/M=10^-21 GeV^-1=10^-30 eV^-1, β=6×10^-3 rad gives 1.6×10^-10 eV^4 ≈ 6 ρ_Λ → consistent.
- E-fold estimate: D_inf ~ e^{-3 N_tot} × 10^{-1.5} to reach 10^{-123} → N_tot ≈ (123−1.5)/3 ln10 ≈ 93 → consistent with 92–94 stated.

Standalone-reader test
Numerical content from companions recurs in Table II, Fig. 3 (parameter choice), Figs. 4/7 (forecasts), Sec. X G (PTA index), Sec. V (galaxy chirality). While not strictly load-bearing for the ECH closure, their inclusion in the main narrative violates PRD’s standard unless public, citable resources exist. See ESSENTIAL items P1A-E2/E4/E3.

Page length
At 32 pages, the paper devotes significant space to programmatic descriptions and companion-paper logistics that are not necessary for the core claims (four-route closures and perturbation transparency). Recommended maximum length for this contribution: ≲ 18–20 pages (main text), moving programmatic timelines, illustrative H(z) overlays, and unrelated survey context (PTA) to an appendix or removing them.

## Summary recommendation
MAJOR REVISIONS

The conceptual core (perturbation transparency under canonical scalars; amplitude-level closures R1–R4 under stated ansätze) is potentially suitable for PRD if the methodological and reproducibility issues are corrected. Essential fixes include: removing the on-shell T^2 term from the fundamental action or restructuring the derivation; eliminating dependence on unpublished “in preparation” companions (or replacing them by public references and artifacts); providing a frozen code/data DOI; sharpening or relocating numerical context that is not part of the proof. Additional major fixes are needed for clarity of certain ansatz-based bounds and to prevent misinterpretation of figures. With these addressed, the manuscript could meet PRD’s standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes pass)

ESSENTIAL

P1A-E8
Location: Sec. II C, Eq. (10) and surrounding text; Fig. 3 caption
Problem: Λ-to-ρ normalization uses ρΛ = Λeff MPl^2 with unreduced MPl ≡ G−1/2. In standard conventions (Gμν + Λ gμν = 8πG Tμν), the vacuum energy density is ρΛ = Λ/(8πG) = Λ MPl^2/(8π), i.e., an 8π factor is missing relative to the stated mapping. Although the manuscript later says the 8π difference is “below order-of-magnitude resolution,” equations and any percentage statements that depend on the mapping should be internally consistent.
Required fix: Choose one convention and carry it consistently: either use reduced M̄Pl^2 = 1/(8πG) so that ρΛ = Λ M̄Pl^2, or keep unreduced MPl and write ρΛ = Λ MPl^2/(8π). Update Eq. (10), related prose, and any captions (e.g., Fig. 3) where ratios involving Λeff ↔ ρ are stated.

P1A-E9
Location: Abstract (first paragraph, Route 4 discussion)
Problem: The abstract states R4 closes by a fine-tuning/naturalness objection but does not make explicit that this closure depends on treating α/M as fixed by a one-loop matching (Eq. 7). In the body (Sec. IV D) you note that if α/M is floated, both βobs and ρΛ can be fit for arbitrary mθ. This dependency should be stated up front to avoid over-claim.
Required fix: Amend the abstract to read “closed by an explanatory-deficit objection conditional on fixing α/M by the one-loop matching; if α/M is treated as free, a spectator-ALP fit can match both βobs and ρΛ but provides no explanation for mθ ∼ H0 or the fitted coupling.”

MAJOR

P1A-M10
Location: Sec. IV B, Eq. (14) and footnote 3
Problem: Dimensional status of ϑNY is ambiguous. The text assigns [ϑNY]=+1 (so [∂μϑNY]=+2), but in much of the literature the pseudoscalar multiplying a topological density is taken to be dimensionless. The coefficient in Eq. (14) (∝ 1/MPl) is chosen to restore dim-4 given [∂μϑNY J5μ]=+5, but this hinges on the nonstandard [ϑNY]=+1 choice.
Required fix: Define ϑNY precisely (field normalization and dimension) and give a one-line dimensional check of Eq. (14). If ϑNY is taken dimensionless, adjust the prefactor and text accordingly (e.g., explain why 1/MPl is, or is not, still required). Make clear how this choice maps to the “γ-running” literature (Date–Kaul–Sengupta; Shapiro–Teixeira).

P1A-M11
Location: Appendix C, “Helicity dispersion” paragraph (around Eq. C3)
Problem: The WKB condition uses k ≫ (α/M) ϕ′ with ϕ′ ≡ dϕ/dη, while ϕ′ = a(t) ϕ̇. The estimate plugs H0 for ϕ′/fa without discussing the a-factor along the line of sight (the largest |ϕ′| could occur near recombination when a ≪ 1). The final result (β depends on end points) is fine, but the inequality as written should be shown to hold over the entire path.
Required fix: Add a sentence justifying that maxη |(α/M)ϕ′| remains ≪ k across recombination to today (e.g., bound with amax correction or note that the bound is strongest at low z and remains safe by ≳ 25–30 orders even at z∗). Alternatively, rephrase to emphasize that only the endpoint difference matters and the WKB check is illustrative.

P1A-M12
Location: Table I footnote b; Sec. VII; Ref. [36]
Problem: Year/citation mismatch: the text alternately refers to “Heinrich+2023” and “[36] Heinrich et al. 2024”. This looks like a stale pointer carried through editing.
Required fix: Harmonize the year and citation for the SPHEREx σ(fNL) baseline everywhere (table footnote, Sec. VII text, and reference list).

P1A-M13
Location: Fig. 1 caption; Sec. X G
Problem: Potential symbol confusion: “γPTA” is labeled simply as γ in the figure graphic and can be confused with the Barbero–Immirzi parameter γ used throughout. Although the caption says they are distinct, the visual label invites misreading.
Required fix: Change the plotted/legend label to “γPTA” (or nPTA) in the figure graphic itself, and add “not the Barbero–Immirzi γBI” directly in the legend.

P1A-M14
Location: Sec. X F (Implications), last sentence; Sec. I A 1
Problem: The text lists “primordial GWs” among “nonperturbative parity-violating channels,” but the main theorem establishes that minimal ECH (Holst) is perturbation-transparent for tensor modes. This could be read as implying ECH predicts GW chirality, which it does not without adding non-minimal/topological terms (e.g., Jackiw–Pi R∧R̃ or dynamical torsion).
Required fix: Clarify that any primordial-GW chirality would require additional parity-violating operators beyond minimal ECH (e.g., gravitational Chern–Simons), which are explicitly outside the present four-route enumeration.

MINOR

P1A-m7
Location: Sec. XIII, “Surviving tests,” point (2)
Problem: The phrase “LiteBIRD … detects non-zero β at ∼ 9σ (0.27°/0.03°)” is a different null from the differential test vs the current central value discussed immediately after. To avoid mixed-nulls confusion, add the standard comparability disclaimer here as well.
Required fix: Append “This 9σ number uses a ‘β ≠ 0’ null and is not directly comparable to the differential test against the current central value” to that sentence.

P1A-m8
Location: Appendix C, end of Eq. (C4) paragraph
Problem: The parenthetical “(the companion’s §VI8)” appears malformed and likely refers to a section/footnote in the unpublished companion.
Required fix: Remove or correct this cross-reference; do not point to unpublished structure.

P1A-m9
Location: Multiple figures/tables where “γ” is used without subscript (e.g., Table V row label)
Problem: Occasional unqualified “γ” could be misread (BI parameter vs other γ’s). You mostly use γBI elsewhere.
Required fix: Standardize to γBI everywhere in the main text, tables, and figure labels; reserve γPTA explicitly when needed.

P1A-m10
Location: Sec. IV B, Eq. (14) discussion
Problem: δNY is introduced with mass dimension −1 but without an indicative magnitude or reference.
Required fix: Add a parenthetical “δNY is a renormalization-scheme–dependent finite remainder; see [20] for discussion; its expected size is at most O(1/MPl) in this normalization” or similar, or make clear it is left unconstrained.

P1A-m11
Location: Sec. II C, Eq. (11)
Problem: You later explain in App. B that uncertainty in the (Treh/MGUT)3/2 prefactor shifts Ntot by only O(few) e-folds. That mitigation is central to interpreting Eq. (11).
Required fix: Add a direct pointer here: “The sensitivity to this prefactor corresponds to at most O(few) e-fold shifts; see Appendix B (‘Sharper dependency statement’).”

NO FURTHER ARITHMETIC FAILS DETECTED
- Recomputed all explicit numbers called out in the main text (Planck vs ACT β difference ~1.06σ; Eq. (7) 3×10−3; Eq. (15) ~10−60; Eq. (17) inversion ~6 ρΛ; ρcrit/ρPl values; 0.07–0.17 in Eq. (20)) and found them consistent with the inputs given, within the paper’s stated order-of-magnitude treatment.

NO ADDITIONAL FIGURE-CAPTION VS BODY MISMATCH BEYOND THOSE ALREADY FLAGGED
- Aside from the Λ–ρ normalization (P1A-E8) and the symbol confusion (P1A-M13), captions/claims match axes and units.

ABSTRACT FAITHFULNESS
- Apart from the added dependency noted in P1A-E9 (R4 closure relies on fixing α/M) and the scaling-ansatz condition already covered in your prior P1A-E5, the abstract’s other statements are supported by the body (perturbation-transparency theorem, four-route scope caveat, list of barriers).

With these additional corrections (on top of your earlier list), the manuscript will better meet PRD standards for consistency, clarity, and rigor.