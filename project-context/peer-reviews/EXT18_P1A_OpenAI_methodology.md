# P1A EXT18 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/arxiv/paper1a_ech_nogo.pdf` md5=f1eab008 pages=29
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (9588 chars)
**Wall time**: 335.2s

---

Referee report on P1A (PRD methodology review)

Scope of review
I assessed the paper’s methodological rigor: derivations, dimensional analysis, estimator definition, significance accounting, internal arithmetic, and reproducibility. I audited scalars in the abstract and conclusions against the body, recomputed quoted ratios and σ-levels where possible, and inspected all figures/tables for consistency.

Findings

ESSENTIAL

P1A-E1 (Abstract; Secs. I, III, XIII, XV; multiple pages)
Problem: Non–self-contained dependencies on “companion papers in preparation” for load‑bearing numerical claims and pipelines. Examples:
- “ΛCDM+ΔNeff MCMC verification, NaMaster pipeline validation, and ALP parameter fitting are documented separately (in preparation [6]).”
- “309,189 frozen accepted samples ... Paper I(b) [6] ... not yet publicly posted.”
- “real-KDE reanalysis γPTA = 2.567 ± 0.382 (Paper III [46])” appears in Fig. 1 and Sec. X G without a public, citable artifact.
- Galaxy chirality null and amplitudes deferred to Paper IV [23].
Required fix: Make the manuscript standalone. Either (a) remove all results that rely on in‑preparation companions (MCMC posteriors, NaMaster validation, ALP fits, PTA real‑KDE reanalysis, galaxy chirality amplitudes/selection) or (b) replace them with published, citable results (including permanent DOIs and complete methodological descriptions), or (c) move all such claims to the companion and submit jointly with cross-references; the present paper must not require access to unpublished materials to evaluate its claims. Any numerical values retained must be reproducible from information contained in this paper alone or from publicly accessible repositories with frozen releases (see E2).

P1A-E2 (Data and Code Availability, p. 25)
Problem: Reproducibility/provenance incomplete. The manuscript points to a mutable GitHub branch and promises a future Zenodo release: “a Zenodo-archived release will pin all artifacts...”. No DOI or frozen commit hash is provided; no tag is specified for the materials corresponding to the submitted version.
Required fix: Provide a permanent DOI (e.g., Zenodo) and the exact git commit hash/tag for all artifacts used in the paper. List the paths to frozen MCMC chains, configuration files, and plotting scripts. Ensure that all numerical results quoted in the paper can be regenerated from this snapshot without reliance on companion manuscripts.

P1A-E3 (Eq. (1), p. 5; text immediately below)
Problem: Inconsistent variational setup. The action explicitly includes “+ 1/4 Tabc Tabc” and then the text states “it is not an independently specified kinetic term and is not varied independently”. Writing a term in the action and then declaring it is not to be varied is methodologically inconsistent and can mislead readers about the equations of motion.
Required fix: Present either (i) the fundamental action before integrating out torsion (Einstein–Cartan–Holst + Dirac), then perform the variation and elimination explicitly, or (ii) present the already-reduced effective action after integrating out torsion, where the four‑fermion term appears. Do not include a term inside the action and simultaneously state it is not part of the variational principle. If you keep a shorthand, move it outside the displayed action and label it as “on‑shell effective contact term after eliminating torsion”, with the derivation reference.

P1A-E4 (Use of σ values from different null procedures; Fig. 4 p. 15; also Abstract p. 1; Sec. VI p. 15; Fig. 6 p. 22; Fig. 5 p. 18)
Problem: Side‑by‑side σ numbers from different null procedures appear multiple times (WMAP+Planck β significance, ACT β significance, SPHEREx Fisher forecasts). Although the abstract and some captions note non-comparability, Fig. 4’s caption juxtaposes “LiteBIRD σ(β)≈0.03°” and “SPHEREx ... 2.6–5σ” without an explicit “not directly comparable” qualifier at that juxtaposition; the figure itself invites cross‑comparison.
Required fix: At every instance where σ-levels from different nulls/experiments/forecasts are displayed together (Abstract, Figs. 1, 4, 5, 6, Secs. VI–VII, XV), add an explicit warning that these significances arise from different null hypotheses and pipelines and are not directly comparable. In figures, add this note directly in the caption and/or legend.

P1A-E5 (Sec. IV B, Eq. (14)–(15), pp. 12–13)
Problem: The route‑2 birefringence bound relies on an EFT operator Γ ∝ (1/16π^2)(β(γ)/MPl) ∫∂μϑNY J5μ that is not derived, and the subsequent mapping to photon birefringence proceeds via an unstated anomaly chain. As written, a reader cannot verify that this specific operator and normalization control the amplitude budget to the extent claimed. The text labels it an “upper‑bound EFT ansatz”, but then uses it for a 60‑order-of-magnitude suppression claim without a transparent mapping chain (ϑNY → J5 → F F̃).
Required fix: Either (a) provide a derivation or citation that explicitly yields Eq. (14) with its normalization and the EM coupling channel used in Eq. (15), including how ϑNY sources ∂μJ5μ ⊃ (αem/4π) F F̃ and what background expectation values are assumed; or (b) reframe the bound as an inequality with all assumptions (including the anomaly step, background value of ∂μϑNY, time integration) stated explicitly, and carry an uncertainty band reflecting operator/normalization ambiguity. In either case, make the dimension‑reduction to the final dimensionless ratio fully explicit.

P1A-E6 (Abstract, Sec. VII, Fig. 4/6; multiple places)
Problem: Forecasted SPHEREx fNL significance (2.6–5σ) and LiteBIRD β “will measure ... and either confirm or rule out...” are presented without a complete in‑paper specification of the estimators, survey assumptions, priors, and systematics that lead to those numbers. The footnotes point to companions not publicly available.
Required fix: Either remove these forecasted σ ranges from this paper, or include a self‑contained methodological summary sufficient to reproduce them (survey volumes, redshift binning, shot noise, bias priors, GR-projection template overlaps, photo‑z modeling, estimator definitions), or cite a published source with matching numbers. Rephrase “will” claims to conditional statements (“if β≈.../if systematics behave as assumed”) to avoid overstatement.

MAJOR

P1A-M1 (Sec. II A 2, Eq. (7), p. 7)
Problem: Use of g^2 = 4π αem to motivate [(α/M) MPl] ~ O(10^−2). The coupling entering a gravitational Holst/Nieh–Yan one‑loop coefficient is not demonstrated to be electromagnetic; mixing sector‑dependent couplings without justification risks miscalibration by orders of magnitude.
Required fix: Justify the choice of gauge coupling entering Eq. (7), or replace g^2 with an explicit effective coefficient Cloop to be constrained, carrying through the numerical uncertainty accordingly. If retaining αem, explain the physical process/channels that make the EM loop the dominant/representative contribution here.

P1A-M2 (Sec. II C 1, “Reheating thermal-reset barrier”, pp. 8–9)
Problem: The washout argument is qualitative, relying on order‑of‑magnitude rates (Γy ∼ y^2 T, Γsph ∼ αW^5 T) versus H(T) without an explicit calculation of Γwash/H across T and without a quantified condition for survival/erasure. Yet this is used to strengthen Barrier 14.
Required fix: Provide a quantitative calculation (or literature‑backed plot) of Γwash/H(T) for the dominant channels across the relevant T range (from Treh down through the EW epoch), with numerical values for yt, αW, degrees of freedom, and clear inequality thresholds, or relegate this to a conjectural remark and remove it from the list of supporting closure mechanisms. Specify the assumed reheating history (instantaneous vs. prolonged), and define precisely what “coherent axial component” means operationally.

P1A-M3 (Sec. IV C, Eq. (16) and following, p. 13)
Problem: The running of γ is postulated with a schematic β‑function not taken from the literature, and the statement “Δγ/γ ∼ 10^−2 over GUT→IR” is asserted without calculation or reference. The “mass‑dimension lock” conclusion depends on the size of Δγ/γ.
Required fix: Cite an explicit calculation (e.g., Benedetti & Speziale 2011) and show, even at back‑of‑envelope level, the size of Δγ/γ over the stated range, or parameterize the result in terms of an explicit unknown coefficient and present the closure as a bound that holds for Δγ/γ ≤ X. Make the dimension counting transparent: list the fields and their mass dimensions and show how the 1/MPl factor emerges.

P1A-M4 (Fig. 3 caption, p. 8; Sec. II C)
Problem: Inconsistency and opacity in the “rotation negligible” estimate. The caption asserts the cω ω^2 term contributes “≲ 10^−21 ρΛ” with a sketch of a division by 3ΩΛ ≈ 2.1. No derivation is given showing how (ω/H)^2 translates into a fractional contribution to ρΛ given your normalization in Eq. (10).
Required fix: Provide the explicit formula linking cω ω^2 to an energy density fraction relative to ρΛ (with all constants), and compute the bound step‑by‑step using (ω/H)0 < 5×10^−11. Clarify the role of 3ΩΛ in that calculation. If cω is treated as O(1), state the assumed value.

P1A-M5 (Fig. 3 caption vs. Sec. III B, Sec. XV; pp. 8, 10, 24–25)
Problem: Mixed use of cosmological parameters. Fig. 3 uses H0 = 69.2 km/s/Mpc, Ωm = 0.310 as a “spin‑torsion benchmark”, while the text elsewhere cites H0 = 67.68 ± 1.06 from a companion MCMC and Planck 2018 best‑fits as the reference. The rationale for the 69.2 choice is not given and may mislead readers into thinking it is a fit result.
Required fix: Either use consistent, published reference parameters throughout, or clearly mark Fig. 3 as a toy illustration with parameters unrelated to any fit and explain the choice. If a benchmark is chosen to illustrate a point, state that no inference is drawn and no fit is claimed.

P1A-M6 (Sec. IV D, Eq. (17), p. 13–14)
Problem: Basis conversion and coupling normalization. The paper’s α/M is later equated to the canonical ALP–photon coupling gaγ only via a long footnote, and the numerical value α/M = 10^−21 GeV^−1 is used heavily. The mapping to fa and cγ is not cleanly presented in the main text, and the tension with standard ALP limits is not discussed when α/M is floated.
Required fix: Bring the basis conversion into the main text: define gaγ and show explicitly how α/M maps onto gaγ for specified fa and cγ, including the factor of 2 or 4π as appropriate. State the parameter choices under which α/M = 10^−21 GeV^−1 corresponds to a viable gaγ in light of stellar‑cooling/helioscope bounds, or state clearly that the value is treated as a phenomenological effective coupling not directly mapped to a UV‑complete ALP.

P1A-M7 (Barrier 12, Eq. (20), p. 19)
Problem: The ceiling ΩGW|bounce ≲ (ρcrit/ρPl)^2 is introduced without derivation or a clear physical argument, yet specific numerical values (0.07–0.17) are quoted.
Required fix: Provide a derivation or at least a short justification for why ΩGW should be bounded by the square of ρcrit/ρPl, or remove the numerical bound and keep only a qualitative statement that a ceiling exists proportional to some function of ρcrit/ρPl. If retained, state clearly that this is an ansatz and not used in any quantitative exclusion.

MINOR

P1A-m1 (Abstract; Sec. I A 1; multiple)
Problem: The paper’s central “closure” results depend on ansatz‑level dimensional assignments (Eq. (6) and Appendix B). While you do label them as ansätze in several places, the abstract still reads as if a general no‑go theorem has been established.
Required fix: In the abstract and conclusions, insert explicit language that the amplitude‑closure statements for R2–R3 depend on stated scaling ansätze and are not operator‑basis theorems, and that R4 is closed on naturalness rather than amplitude grounds. (You partially do this; make it unambiguous.)

P1A-m2 (Sec. II A 2; Fig. 2, p. 6–7)
Problem: The logarithm ln(ΛUV^2/μ^2) ≈ 74 is used; the inputs are not shown explicitly.
Required fix: State the numerical inputs used for ΛUV and μ that yield ≈ 74 (e.g., ΛUV = MPl, μ = 1 TeV), or show the computation.

P1A-m3 (Sec. III A, Eq. (12), p. 10)
Problem: The CEB formula CEBℓ ≈ 2β (CEEℓ − CBBℓ) is given without reminder of the small-β approximation and the isotropy assumption.
Required fix: Add “to first order in small, spatially uniform β” to the equation text, and cite a standard derivation.

P1A-m4 (Sec. X B, p. 19)
Problem: Statement “the algebraic Bianchi identity holds for any torsionless connection; non‑metricity does not invalidate the identity provided T=0” is correct but unusual for GR readers.
Required fix: Add a reference or a brief footnote pointing to a standard text that proves the algebraic Bianchi identity for general torsionless affine connections (e.g., Lovelock & Rund or equivalent).

P1A-m5 (Nomenclature; multiple pages)
Problem: γ is used for the Barbero–Immirzi parameter, while γPTA is a spectral index in figures/captions. Although you note the distinction in places, it is easy to misread.
Required fix: Ensure every figure/caption that mentions γPTA explicitly re‑states that this is not the Barbero–Immirzi γ to prevent confusion.

P1A-m6 (Typos/orthography; p. 6)
Problem: “Domaga la–Lewandowski” appears with a space in “Domaga la”.
Required fix: Correct to “Domagała–Lewandowski” consistently.

P1A-m7 (Acknowledgments, p. 25)
Problem: Acknowledgement of an AI assistant is unusual but acceptable; however, PRD may require disclosure of the extent of AI usage.
Required fix: Confirm PRD policy compliance; if required, state explicitly that all derivations and conclusions were verified by the author and that no generative content was used without verification.

P1A-m8 (Appendix B, p. 26)
Problem: The phrase “promote (α/M)M3Pl to (α/M)M5Pl by inserting Planck‑scale bounce‑curvature factors” is vague.
Required fix: Specify which curvature scalars/tensors you envisage (e.g., R ∼ M2Pl at the bounce) and how they enter the on‑shell scaling.

P1A-m9 (Fig. 1, caption p. 5)
Problem: The annotation “γPTA = 2.567 ± 0.382 (Sec. X G)” is not reproducible from this paper alone.
Required fix: Either remove this number from the figure or add a clear “illustrative value from companion Paper III” label and remove any inference tied to it in this paper.

NIT

P1A-n1 (Formatting; p. 1–29)
Problem: Occasional encoding artifacts (¨, ´) and dangling spaces around hyphenated names.
Required fix: Clean up diacritics and spacing.

P1A-n2 (Units; multiple)
Problem: Switches between eV/GeV are correct but sometimes implicit.
Required fix: When converting (e.g., α/M in GeV−1 to eV−1), add parenthetical conversions once to guide readers.

P1A-n3 (Length)
Problem: The manuscript is long (29 pages) relative to the core technical contribution (channel‑level amplitude closures and a perturbation‑transparency statement).
Recommended cap: 20–22 pages. Consider moving the extended motivation narrative and survey roadmaps to an appendix or the companion papers; keep the present paper focused on the closures/barriers and the perturbation‑transparency derivation.

Arithmetic checks and recomputations

- Eq. (7) numerical estimate: With g^2 = 4π αem ≈ 0.092, γ ≈ 0.274, M = MPl/√γ, and ln(ΛUV^2/μ^2) ≈ 74, [(α/M) MPl] ≈ (0.092/(32π^2)) × γ × √γ × 74 ≈ 3×10^−3, matching the text’s “within a factor of a few of 10^−2” (OK).
- R2 suppression ratio (Eq. (15)): αem/(4π) ≈ 5.8×10^−4; H0/MPl ≈ 1.2×10^−61; MPl(α/M) with α/M = 10^−21 GeV−1 ≈ 0.012; βobs ≈ 6×10^−3; ratio ≈ 10^−60 (OK).
- R4 inversion: ρθ = 2 m^2θ β^2/(α/M)^2, with mθ = 1.5×10^−33 eV, β ≈ 6×10^−3, α/M = 10^−30 eV−1 gives ρθ ≈ 1.6×10^−10 eV^4 ≈ 5.7 ρΛ (ρΛ ≈ 2.8×10^−11 eV^4) (OK).
- Barrier 12 numeric: (0.27–0.41)^2 ≈ 0.073–0.168 (OK).
- γPTA difference: (3.0−2.567)/0.382 ≈ 1.13σ (OK).

Dimensional consistency spot checks

- Eq. (6): [α/M] = −1, [ε eeF] = +2 → Lodd dim +1 (as stated). Mapping to energy density via on‑shell curvature insertions is an ansatz (must remain clearly labeled).
- Eq. (10): [Λeff] = mass^2; cω ω^2 has mass^2; Ξ dimensionless; ρΛ = Λeff M2Pl has mass^4 (OK).
- Eq. (13): κ = 8πG = M−2Pl ; n2ψ/M2Pl has mass^4 (OK).
- Appendix C: Dispersion ω± ≈ k ∓ (α/M) ϕ′/2; β = (α/2M) Δϕ (OK).

Abstract-last drift sweep

- Claims of “channel-level closure” and “perturbation transparency” are supported in the body, with appropriate caveats. However, the abstract repeatedly references results (SPHEREx σ range, LiteBIRD prospects) that are not derived here and depend on unpublished companions; these must be toned down or removed (E6) or made self‑contained.
- The cosmological constant “reparameterization” via Ntot ≈ 92 is labeled an ansatz in the body and should be explicitly called an ansatz in the abstract as well (m1).
- The βobs and ACT numbers are correctly reproduced and sourced.

Bibliography

- Check author names/years: “Domaga la–Lewandowski” should be “Domagała–Lewandowski”. Verify [5] year (2025) and arXiv ID format; others look plausible. Ensure all preprints are cited as arXiv with versions if necessary.

Effect sizes

- Where σ are quoted (β detection, SPHEREx forecast), add effect‑size interpretations (e.g., β amplitude in degrees; fNL absolute value −4.375) are already present; acceptable.

## Summary recommendation
MAJOR REVISIONS

The paper contains interesting structural arguments and a clear perturbation‑transparency result, but it is not yet suitable for PRD in its current form. The most serious issues are the lack of self‑containment (reliance on in‑preparation companions for key numbers and figures), an inconsistent action presentation in Eq. (1), and insufficiently justified operator choices/normalizations in the route‑2/3 amplitude budgets. Address the ESSENTIAL and MAJOR items above, provide frozen reproducibility artifacts, and either remove or fully substantiate all claims that currently depend on unpublished companion work. Once these issues are remedied and the paper is tightened in length and focus, it could be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eye pass)

I focused on the ten checks you requested (A–J) and report only NEW issues not included in my first review. Page/section indicators refer to the provided manuscript text.

ESSENTIAL

P1A-E7 (Fig. 5, caption p. 18; Sec. II A 2, Eq. (7))
Problem: Unsubstantiated “RG running of α/M” figure. The top panel of Fig. 5 shows a monotonic “renormalization-group running of the parity-odd coupling from the present epoch to the Planck scale,” anchored at a “primordial benchmark α/M ∼ 10^−21 GeV^−1.” No β-function for α/M is ever written, no initial condition is specified (the caption says “anchored at the primordial benchmark,” but the curve is plotted “from the present epoch to the Planck scale”), and no normalization is derived. Eq. (7) is a one-loop matching estimate of a finite coefficient, not a differential RG equation. As drawn, the figure is not reproducible from the paper and risks implying a derived running where none is provided.
Required fix: Either (a) remove the “RG running of α/M” panel, or (b) supply an explicit β-function d(α/M)/d ln μ with all constants, the integration, and the anchoring condition consistent with the caption. If the line is merely schematic (logarithmic running inferred from Eq. (7)), label it as such (schematic; not fitted) and quantify the slope.

MAJOR

P1A-M8 (Internal consistency; Sec. II C 1 vs. Sec. II C 1 “Reheating thermal-reset barrier”)
Problem: Inconsistent use of the dilution ansatz after asserting thermal reset. Section II C 1 first motivates Dinf ∝ e^−3Ntot × (Treh/MGUT)^{3/2} by arguing torsion tracks ⟨J5⟩ ∝ a^−3, then immediately argues that reheating interactions drive ⟨J5⟩ → 0 (coherent component erased if Γwash > H). If the coherent axial expectation is thermally reset to zero, the e^−3Ntot dilution of a pre-reheating coherent background ceases to control today’s amplitude. Yet the paper continues to use Dinf to set the amplitude budget (Sec. XII A and elsewhere).
Required fix: Make the logical branches explicit and consistent. If Γwash > H kills the coherent component, drop Dinf from all amplitude budgets (keep the reset as the operative closure). If you wish to keep Dinf as a working parameterization, state and justify conditions under which a coherent component survives reheating (Γwash/H < 1 over the relevant window) and carry a survival factor S ≤ 1 with a clearly defined prior.

P1A-M9 (Figure–text mismatch; Fig. 5 caption vs. body; also Fig. 5 axes)
Problem: Ambiguous anchoring in Fig. 5 top panel (“from the present epoch to the Planck scale” vs. “anchored at the primordial benchmark”). The x-axis is log10(μ/GeV), but the caption text mixes “present epoch” with a high-scale anchor. This invites readers to interpret the line as a real computed trajectory. No corresponding equation in the body yields this line.
Required fix: Clarify the anchor (μ0 and α/M(μ0)), provide the formula that generated the line, and ensure the caption matches. If illustrative, label as “schematic logarithmic dependence inferred from Eq. (7); not a fit.”

P1A-M10 (Galaxy spin asymmetry amplitude claim; Sec. II C 2, p. 10; Sec. III B, p. 10)
Problem: The statement “parity‑odd operator coupling α/M ∼ 10^−21 GeV^−1 underpredicts any plausible spin asymmetry by > 100 orders of magnitude” is not supported by an explicit calculation in the paper. No mapping from α/M to the dipole/hemisphere spin‑asymmetry estimator A0 is shown, and the numerical “> 100 orders” is not derived here (it is also not in any cited published source).
Required fix: Provide a back‑of‑envelope amplitude estimate linking α/M to a chirality asymmetry in galaxy spins (clearly specifying the observable and the astrophysical window) or remove the “> 100 orders” numerical claim and state qualitatively that the effect is negligible.

P1A-M11 (Figure–method mismatch; Fig. 3 caption vs. Sec. II C 1)
Problem: Fig. 3 displays a percent-level ΔH/HΛCDM curve emerging from a ΞM^2_Pl term while asserting that the rotation contribution is ≲ 10^−21 ρΛ. However, the body never actually shows or tabulates the Ξ value used in the orange curve (only that Ξ = ρΛ/M^4_Pl ≈ 10^−123 generically). As plotted, the ΔH/HΛCDM curve appears tied to specific parameter choices (H0 = 69.2, Ωm = 0.310), but the text neither provides the corresponding Ξ nor explains the consistency with the e^−3Ntot bookkeeping.
Required fix: State the exact Ξ used in the orange curve and show that this Ξ reproduces ρΛ today (i.e., Λeff = 3H0^2ΩΛ) with those H0, Ωm. If it is a toy illustration, add that explicitly in the caption and remove any implied inference.

P1A-M12 (Notation clarity; Sec. II C, Eq. (10) and Eq. (24))
Problem: Ξ is defined twice with slightly different notations. Eq. (10): Ξ M^2_Pl enters Λeff; Eq. (24): Ξ ≡ ⟨(α/M) MPl⟩ Dinf. The angle‑bracket ⟨·⟩ is not defined (average over what?) and the relationship between the two definitions is not explicit. This is brittle for readers trying to trace the normalization.
Required fix: Define ⟨·⟩ or remove the angle brackets; present one canonical definition of Ξ used throughout. If Eq. (24) is a heuristic parameterization rather than a definition, label it as such and keep the formal definition in Eq. (10) unique.

P1A-M13 (Schematic “duality” claims without proof; Sec. IX B, “Topological-Shift Duality”)
Problem: The stated duality “Mass protection ⇔ No geometric fingerprint” is presented as a general statement without a derivation, theorem, or literature citation. It is then used to motivate a barrier classification.
Required fix: Either provide a brief derivation/citation supporting this duality in the stated scope (metric‑affine gravity, Nieh–Yan/axion sector), or rephrase as a conjectural organizing heuristic and remove it from the list of established barriers.

MINOR

P1A-m10 (β symbol collision; Sec. IV B, Eq. (14); Sec. IV D, Eq. (17))
Problem: The symbol β denotes both (i) the birefringence angle and (ii) an RG β‑function β(γ). While you disambiguate with an argument β(γ) near Eq. (14), later text occasionally says “the induced β is suppressed” without reconfirming it is the rotation angle. This can confuse readers, especially in a section discussing both.
Required fix: Whenever “β” (angle) appears within a few lines of “β(γ)” (RG function), restate “rotation angle β” vs. “β‑function β(γ)” to avoid ambiguity.

P1A-m11 (Eqs. (21) and surrounding prose; Sec. X C)
Problem: The symbol H is used both for conformal Hubble a′/a (just above Eq. (21)) and for the cosmic‑time Hubble ḋa/a (two lines below) without restating the switch. This is correct but can mislead on a quick read.
Required fix: Add “in conformal time” and “in cosmic time” labels right next to the two equations, and note explicitly that H ≡ a′/a in the first and H ≡ ḋa/a in the second.

P1A-m12 (Appendix C normalization consistency)
Problem: Eq. (C4) uses β = (α/2M) Δϕ and then notes a basis conversion to gaγ with a 2π factor. The body (Sec. IV D) uses the same α/M throughout but only clarifies the basis conversion in a long footnote. Without reading the appendix, a reader may miss that the paper’s α/M is not identical to gaγ.
Required fix: Move a one‑sentence basis‑conversion summary from the footnote/appx into the main text of Sec. IV D immediately after Eq. (17) (define gaγ and show α/M ↔ gaγ with fa, cγ).

P1A-m13 (Arithmetic visibility; Sec. XIV D)
Problem: You refer to the “deep inside the inflationary subhorizon regime” via the factor e^{Ntot−Nexit} ≈ e^{32}. The numerical value (≈ 7.9×10^13) is never shown.
Required fix: Add the explicit value e^{32} ≈ 7.9×10^13 to make the scale jump transparent.

P1A-m14 (Author names; multiple)
Problem: “Pop lawski” appears with a space in several places; standard usage is “Popławski” (without space; diacritic optional). You already have a diacritic fix request for Domagała–Lewandowski; extend to Popławski for consistency.
Required fix: Normalize to “Popławski” (or “Poplawski” if diacritics are removed globally).

P1A-m15 (Definition of ρobsΛ; multiple)
Problem: Various places compare to “ρobsΛ” without ever stating the numerical value used. You compute it implicitly in R4 checks, but a reader has to infer it.
Required fix: State once (e.g., in Sec. IV D or App. C) the value used for ρobsΛ (≈ 2.8×10^−11 eV^4) and the Λ ↔ ρ relation ρΛ = 3 M^2_Pl H^2_0 ΩΛ.

NIT

P1A-n4 (Pontryagin notation; footnote “a” under abstract; Sec. X D)
Problem: You write “∝ R Rẽ” (mixed typography) once; later you use R ∧ R̃. Keep a single notation (R ∧ R̃ or ϵ R R) to avoid confusion.
Required fix: Harmonize Pontryagin‑density notation across the manuscript.

P1A-n5 (Units visibility; multiple)
Problem: α/M is quoted in GeV^−1 in the body and converted to eV^−1 only implicitly in the R4 arithmetic. For quick checking, one parenthetical “1 GeV = 10^9 eV; hence 10^−21 GeV^−1 = 10^−30 eV^−1” would help.
Required fix: Add one explicit unit‑conversion parenthetical where α/M = 10^−21 GeV^−1 is first used in calculations.

EXPLANATION OF COVERAGE

- I did not repeat previously raised issues (E1–E6, M1–M7, m1–m9, n1–n3).
- I rechecked arithmetic in all places where new claims appear above; the only additional arithmetic suggestion is to print e^{32} explicitly (m13). Other checked numbers still match (no new arithmetic mismatches found).
- The largest new substantive issues are the unsupported “RG running of α/M” figure (E7/M9) and the internal inconsistency of continuing to use Dinf after asserting reheating washout (M8). These affect reader confidence in two visible parts of the narrative.