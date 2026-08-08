# P1A EXT20 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/arxiv/paper1a_ech_nogo.pdf` md5=198cb994 pages=29
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7212 chars)
**Wall time**: 425.3s

---

Referee report for Physical Review D (methods-focused)

Manuscript: “Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter”

Overall assessment
The manuscript aims to provide a “channel-level closure” of four proposed minimal Einstein–Cartan–Holst (ECH) routes to dark energy and to prove a perturbation-transparency result for scalar matter. The scalar/tensor perturbation transparency (Holst dual vanishes on a torsionless connection by the algebraic Bianchi identity) is standard and clearly presented. However, the rest of the paper relies heavily on non-derivative phenomenological ansätze, unpublished “companion” analyses, internally generated numbers that are not citable, and figures/tables that depend on those companions. For a PRD methods paper, the work is not self-contained; several load-bearing quantitative elements are not reproducible from the submission, and multiple equations and scalings are asserted rather than derived. Below I provide a detailed methodological audit with actionable fixes.

Findings

ESSENTIAL

P1A-E1 (Scope, pp. 2–4; Sec. I “Companion paper” paragraph; Table IV; Secs. III, V–VII; Figs. 1, 4–6)
Problem: Pervasive dependence on unpublished “companion” works (in preparation [2, 6, 23, 46]) for MCMC posteriors (H0, ΔNeff, σ8), EB pipeline validation, ACT/WMAP–Planck birefringence handling, SPHEREx Fisher forecasts, and a NANOGrav reanalysis. These are used in the text, Table IV, and Figs. 1, 4–6. The manuscript is not self-contained and cannot be methodologically audited without those artifacts.
Required fix: Remove every load-bearing use of “in preparation” results, or replace with published, citable sources that reproduce the exact numbers used. If these results are essential, delay submission until the companion(s) are on arXiv/peer-reviewed and revise to a self-contained paper that includes all analysis details or provides stable, citable DOIs.

P1A-E2 (Data and Code Availability, p. 25)
Problem: The repository link is given without a frozen release. It promises a future Zenodo archive but provides no DOI, immutable tag, or commit hash for the exact version used. “Frozen MCMC chains” are mentioned but not paired with a DOI. For PRD standards, reproducibility requires fixed, public artifacts.
Required fix: Create a Zenodo or equivalent archival DOI for the exact code and data used in the paper. Cite the DOI in the Data Availability section, include commit hashes for the code, and provide a manifest listing the exact versions used for each figure/table. If “frozen chains” are claimed, they must be included in the archive.

P1A-E3 (Figures 1, 4, 5, 6; captions and text on pp. 5, 15, 18, 22)
Problem: Figures portray forecasted significances and a PTA spectral index γPTA = 2.567 ± 0.382 drawn from an unpublished “real-KDE GPU MCMC” analysis [46]. The RG “running” of α/M in Fig. 5 is plotted without an explicit β-function or parameters used. These are not reproducible from the manuscript.
Required fix: Either (i) remove Figs. 1, 4–6 (and any text dependent on them) or (ii) supply full derivations, inputs, and links to archived artifacts to allow reproduction. For Fig. 5 top panel, provide the explicit β-function, initial conditions, and parameter values used to generate the curve.

P1A-E4 (Appendix C, last paragraph; p. 27)
Problem: Broken internal reference: “the companion’s §VI8” is not a valid section label and points to an unpublished companion.
Required fix: Remove or correct the reference. All normalization chains between Lagrangian and β must be derivable within this paper or via a published, citable resource.

P1A-E5 (Table IV; pp. 26–27; Sec. II B; Fig. 3)
Problem: Table IV lists numerical posteriors (e.g., H0 = 67.68 ± 1.06, ΔNeff = −0.020 ± 0.169), and Fig. 3 uses “spin-torsion benchmark cosmology” parameters that originate from the unpublished companion. These values are presented without independent derivation in this paper or citable provenance.
Required fix: Remove all unpublished posterior values from Table IV and figures, or replace them with published values. If the values are not used to support any proof, delete them. For Fig. 3, either show a purely illustrative comparison with standard Planck ΛCDM values (and label it explicitly as illustrative without using internal posteriors) or remove the figure.

P1A-E6 (Sec. IV A; p. 11–12)
Problem: Arithmetic inconsistency in the NJL amplitude ratio. The text estimates ρNJL ≈ 4 × 10−81 eV4 and claims this is “roughly 4 × 10−69 ρΛ.” With ρΛ ≈ (2.3 meV)^4 ≈ 3 × 10−11 eV^4, the ratio is ≈ 1.3 × 10−70, i.e., 1–2 orders of magnitude smaller than claimed.
Required fix: Recompute and correct the ratio. Provide all conversion steps (nψ in cm−3 to eV^3, MPl in eV), and ensure the final ratio is numerically accurate.

P1A-E7 (Abstract; Sec. IV B; Eq. (15); pp. 1, 12–13)
Problem: The Route-2 one-loop estimate uses a bespoke dimensional reduction to a dimensionless ratio (∆θone-loop/∆θobs). While the final scale (∼10−60) is plausible, the chain mixes H0 (energy), MPl, βobs (angle), and MPl(α/M) without a fully explicit derivation of the observable β from the operator in Eq. (14). This is presented as a bound but plays a key role in the closure claim.
Required fix: Provide an explicit derivation from Eq. (14) to an observable rotation angle integrated along the line of sight (analogous to Appendix C), including all factors of scale factor and units, then show step-by-step how the dimensionless ratio in Eq. (15) is obtained. If only an order-of-magnitude upper bound is intended, write it as such, with a clearly stated inequality and all assumptions.

P1A-E8 (Abstract and throughout the text; pp. 1–4, 13–14, 21–25)
Problem: Heavy use of unpublished ACT DR6, WMAP+Planck re-analyses, SPHEREx forecasts, and internal PTA re-analyses are juxtaposed with significance values from different null procedures. Although several caveats are present (e.g., Abstract, Fig. 4/6 captions), this mixing still appears in multiple places without a nearby, explicit reminder.
Required fix: At every point where σ values from different null procedures are compared or listed together (Abstract; Figs. 4 and 6; Secs. III, VII, XII, XV), append an explicit statement: “These σ values arise from different null hypotheses and estimators and are not directly comparable.” Retain this warning in each location.

P1A-E9 (Appendix B; Sec. II A.2 and II C; pp. 6–8, 26)
Problem: The mapping from the parity-odd operator with off-shell mass dimension +1 to a vacuum-energy density relies on an on-shell scaling ansatz (Eq. (B2)), not a controlled EFT. Yet the paper repeatedly uses this ansatz in equations and figures that appear quantitative.
Required fix: Constrain all uses of the M5Pl/M4Pl mapping strictly to qualitative discussion, clearly label every occurrence as “phenomenological ansatz,” and remove any figure/table that visually implies a derived, quantitative prediction (e.g., Fig. 3’s ΔH/H% curve attributed to Ξ unless it’s purely illustrative and labeled as such). Alternatively, supply a proper EFT operator of mass-dimension +4 with its coefficient and show the inference within a controlled framework.

MAJOR

P1A-M1 (Fig. 1; p. 5; Sec. X G; Ref. [46])
Problem: The plotted PTA “γPTA = 2.567 ± 0.382 (real-KDE reanalysis)” has no methodological details in this manuscript and hinges entirely on an unpublished analysis. It may bias readers by visually suggesting ECH-linked compatibility where none is established here.
Required fix: Remove the γPTA annotation from Fig. 1, or add a methods subsection describing the KDE prior, likelihood, sampler configuration, dataset, masking, convergence diagnostics, and a public link to the exact chains and code. Better: drop the PTA part entirely from this paper.

P1A-M2 (Sec. IV D; Eq. (17); pp. 13–14; Appendix C)
Problem: The ALP birefringence discussion mixes conventions (α/M vs gaγ) and mentions a ∼10× basis-conversion gap that depends on fa and cγ, but no quantitative bounds or consistent parameter scan are shown. The naturalness objection depends sensitively on these conversions.
Required fix: Provide a clean map between α/M and gaγ with explicit numerical constants and a table of representative choices (fa, cγ) that realize α/M ~ 10−21 GeV−1. State clearly which parameterizations are used in the naturalness argument and, where relevant, cite stellar-cooling/helioscope bounds that would exclude the required couplings for given masses.

P1A-M3 (Sec. II C.1; Eq. (11); pp. 8–9; Sec. XII A)
Problem: The dilution factor Dinf = e−3Ntot × (Treh/MGUT)3/2 is admitted to be an ansatz. Even as a bookkeeping device, it drives the headline Ntot ≈ 92 claim in multiple places and is central to the “structural-tension” argument with fNL.
Required fix: Either (i) derive Eq. (11) from a concrete model including the parity-odd density-of-states integral and reheating microphysics with rates Γwash(T) vs H(T), or (ii) relegate the Ntot ≈ 92–94 numbers to a qualitative sidebar and remove them from the headline conclusions and figures. If retained, add a sensitivity plot showing how Ntot shifts with different reasonable values of the prefactor and Treh.

P1A-M4 (Sec. IV B/C; Eqs. (14)–(16); p. 12–13)
Problem: Route 2 and Route 3 closures depend on order-of-magnitude β-functions and running ansätze not derived here. The mass-dimension “lock” is qualitatively sound, but readers cannot reproduce the quoted “≳ 60 orders of magnitude” suppression without transparent steps.
Required fix: Provide a worked example with explicit numbers in a short subsection: (i) write down the operator(s) with all factors; (ii) show the scaling of the induced observable; (iii) tabulate the numerical inputs; (iv) show the final suppression value (with units). Emphasize assumptions and provide an uncertainty band.

P1A-M5 (Sec. X; pp. 19–20)
Problem: The perturbation-transparency proof is correct for canonical scalar matter but slides quickly over possible non-metricity and boundary terms. The statement “non-metricity does not invalidate the identity provided T = 0” needs a reference or a short proof.
Required fix: Add a citation or short derivation clarifying that the first algebraic Bianchi identity Rμ[νρσ] = 0 holds for torsionless connections irrespective of non-metricity, and that the Nieh–Yan boundary term vanishes pointwise for T = 0.

P1A-M6 (Sec. III A; Eq. (12); p. 10)
Problem: The small-angle EB formula CEBℓ ≈ 2β (CEEℓ − CBBℓ) is stated without specifying conventions (e.g., sign, lensing B contribution). Later you note that published β estimators do not neglect CBBℓ, but the equation as given can mislead.
Required fix: Include the full rotation mapping for uniform β including TB/EB with sign conventions, and state explicitly that lensing B is included in the standard estimators. Cite the exact estimator definition used in [3, 4, 5].

P1A-M7 (Sec. IX L; Eq. (20); p. 19)
Problem: “Vacuum Amplification Ceiling” ΩGW|bounce ≲ (ρcrit/ρPl)^2 is labeled an ansatz but presented with precise numbers (0.07–0.17), unrelated to a spectral prediction and with unclear physical status.
Required fix: Either (i) move this to a brief aside with an explicit “not used in any closure” remark, or (ii) provide a derivation or reference for the quadratic scaling. As written it risks being taken as a quantitative bound.

MINOR

P1A-m1 (Symbol reuse; p. 12 Eq. (14) and throughout)
Problem: β is used for both the birefringence angle and the RG β-function β(γ).
Required fix: Change the RG β-function notation to βRG(γ) or b(γ) to avoid confusion.

P1A-m2 (Units and conventions; pp. 7–8)
Problem: The use of unreduced MPl is stated, but some places mix “M” (area-gap scale) and MPl without immediately reminding the reader of M = MPl/√γ.
Required fix: Add a one-line reminder wherever M and MPl are multiplied (e.g., in Step 4, Sec. II A.2).

P1A-m3 (Table I footnote b; p. 4)
Problem: Refers to “footnote at the abstract-level 2.6–5σ quote,” which does not exist as a proper numbered footnote.
Required fix: Remove this language or point to an actual section/footnote.

P1A-m4 (Typographical/consistency; multiple pages)
Problem: Inconsistent hyphenation and spacing (“Domaga la,” “Holst–sector,” “pseudo-density”). Occasional double spaces and hyphen artifacts likely from PDF-to-text.
Required fix: Clean the typography; ensure names and compound terms are consistently formatted.

P1A-m5 (Claims of novelty; Sec. I A, Sec. IX; pp. 3–4, 16–19)
Problem: Statements like “no prior work assembles these into a single quantitative framework with systematic barrier testing” are broad.
Required fix: Soften to “to our knowledge” and ensure the literature survey (e.g., on EC torsion cosmology constraints) is comprehensive.

NIT

P1A-n1 (Acknowledgments; p. 25)
Problem: The explicit reference to using an AI assistant is unusual for PRD and may not be needed.
Required fix: Consider removing or rephrasing to “We used automated tools for text organization; all scientific content remains the responsibility of the author.”

P1A-n2 (Figure utility)
Problem: Fig. 5 top (RG running of α/M) provides a schematic without methods detail.
Required fix: Either annotate as schematic/illustrative or remove.

P1A-n3 (Section labeling)
Problem: “Foundations” vs “Branches” vs “Barriers” could be streamlined for clarity.
Required fix: Add a brief legend at the start of Sec. IX clarifying the taxonomy.

Additional arithmetic/dimensional spot checks

- LQC critical density (Eq. (9)): For γ = 0.2375, ρcrit/ρPl ≈ 0.41; for γ = 0.274, ≈ 0.27. Correct.

- One-loop coefficient (Sec. II A.2 Step 4): With g^2 = 4παem ≈ 0.092, ln(Λ^2/µ^2) ≈ 74, γ ≈ 0.274, M = MPl/√γ, the estimate [(α/M) MPl] ≈ 3 × 10−3 is consistent.

- Route-2 suppression (Eq. (15)): With αem/(4π) ≈ 5.8×10−4, H0/MPl ~ 10−61, MPl(α/M) ~ 10−2, βobs ≈ 6×10−3, the ratio ≈ 10−60. Acceptable as an OOM bound once the derivation to β is supplied.

- R4 overshoot: ρθ = 2 m^2θ β^2/(α/M)^2 with mθ = 1.5×10−33 eV, β ≈ 6×10−3, α/M = 10−21 GeV−1 (= 10−30 eV−1) gives ρθ ≈ 1.6×10−10 eV^4 ≈ 5–6 ρΛ. Correct.

- Rotation bound contribution: (ω/H)^2/(3ΩΛ) with (ω/H)0 < 5×10−11 and ΩΛ ~ 0.7 gives ≈1.2×10−21 of ρΛ. Correct.

Length and focus
At 29 pages, the paper is long relative to what is ultimately proven with rigor in this submission (the perturbation-transparency theorem and several scaling arguments). Given the required removals/rewrites, I recommend a streamlined revision (~18–20 pages) focusing on:
- The rigorous perturbation-transparency result and its scope/limits.
- Clean, fully derived amplitude-closure arguments for R1–R3 with explicit numerical steps.
- A carefully bounded naturalness discussion for R4 with clear parameter maps.
- Removal of all unpublished companion-dependent content, forecasts, and internal posteriors.

Standalone-reader test
As submitted, the paper fails the standalone-reader test due to reliance on unpublished companions for multiple core figures, numbers, and validation claims. PRD requires a self-contained methodological chain. This must be corrected.

Effect sizes and null-procedure caveats
You have taken care in several places to note that σ-values arise from different nulls; ensure this appears wherever the numbers are juxtaposed (Abstract, Figs. 4/6, Sec. VII, Conclusions). Where you quote σ, also state the corresponding effect size (e.g., angle in degrees, fractional ΔH/H), which you mostly do.

## Summary recommendation
REJECT

The manuscript contains a sound and clearly stated perturbation-transparency result, but the broader “channel-level closure” claims rely heavily on non-derivative ansätze and on unpublished companion analyses for key figures, tables, and numerical values. For a PRD methods paper, the work must be self-contained and reproducible; currently it is not. I encourage a resubmission after: (i) removing all dependence on unpublished companions (or publishing them and integrating stable citations); (ii) supplying explicit, reproducible derivations and numerical steps for all amplitude-closure estimates; (iii) archiving code/data with a DOI; and (iv) pruning illustrative but unsupported figures. Once these essential issues are addressed, a shorter, tightly focused paper may be suitable for consideration.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes audit)

The items below are new and do not duplicate the issues in my initial report. I follow the same tag format.

ESSENTIAL

P1A-E10 (Dimensional consistency of Eq. (14); Sec. IV B)
Problem: The one-loop “parity-odd” EFT operator is written as
Γone-loop ⊃ −(1/16π^2) [β(γ)/MPl] ∫ d^4x √−g ∂μϑNY J5μ.
With ϑNY treated as a dimensionless pseudoscalar (as implied by the text), [∂μϑNY] = +1 and [J5μ] = +3, so the integrand has mass dimension +4. Multiplying by 1/MPl (−1) makes the Lagrangian density dimension +3, not +4. As written, Eq. (14) is dimensionally inconsistent unless either (i) ϑNY carries mass dimension +1, or (ii) the coefficient has one more inverse mass (i.e., ∝ 1/M^2), or (iii) an additional heavy scale is present to restore dimension +4.
Required fix: Specify the mass dimension of ϑNY unambiguously and make Eq. (14) dimensionally consistent. If ϑNY is dimensionless, change the coefficient to 1/M^2 with a clearly defined heavy scale (and propagate this consistently through Eq. (15)). If ϑNY has dimension +1, state and reference this choice, and adjust the discussion accordingly. Provide a short derivation or cite a source where this operator (with its coefficient and field dimensions) is obtained.

MAJOR

P1A-M8 (Starting action double-counting/ambiguity; Eq. (1); Sec. II A.1 and footnotes)
Problem: The fundamental action Eq. (1) includes a +¼ TabcTabc term inside the 1/(16πG) prefactor, but the text simultaneously states this is “an on-shell Hehl–Datta shorthand” not varied independently. Presenting it inside the fundamental action while also varying only the EC+Holst+Dirac piece is confusing and risks double counting in readers’ reconstructions.
Required fix: Remove the T·T term from the “fundamental” action and present it only in the derived effective action after integrating out torsion, or add an explicit two-line derivation showing the variation is performed without double counting and that the displayed T·T term is merely a mnemonic, not part of the varied Lagrangian.

P1A-M9 (Unproven mass–coupling scaling in Poincaré gauge barrier; Eq. (18); Sec. IX A)
Problem: The barrier formula geff ∼ 1/(MPl√|t3|) ∼ H0/MPl assumes √|t3| ∼ m−1
T and directly identifies mT with H0, but no PGT Lagrangian or mode decomposition is shown. As written, this is an unproven scaling ansatz that drives a sharp “10−61” conclusion.
Required fix: Either provide a concrete PGT Lagrangian with torsion-mode mass mT and show how geff scales as mT/MPl (with t3 defined and units checked), or explicitly label Eq. (18) as an ansatz and remove its use from any quantitative conclusion.

P1A-M10 (Self-contained assumption for surviving fNL claim; Sec. XIII)
Problem: The statement that fNL = −35/8 holds “under Assumption (f) of [2]” relies on an unpublished companion for a load-bearing assumption. A reader cannot verify what Assumption (f) is.
Required fix: Restate Assumption (f) verbatim in this paper (one or two sentences), so the surviving-class claim is self-contained.

MINOR

P1A-m6 (Notation collision and clarity for curvature “F”; Sec. II A.2, Eqs. (5)–(6))
Problem: The text says “calligraphic F” is reserved for gravitational curvature, while electromagnetic Fμν is used later, but Eq. (6) is written with plain F IJ
ρσ (not calligraphic), risking confusion with the EM F. 
Required fix: Use a distinct symbol consistently (e.g., calligraphic R or ℛIJ
ρσ for curvature two-form) and keep EM Fμν for electromagnetism. Add a one-line reminder at Eq. (6).

P1A-m7 (Typographical clarity in radiation-density proxy; Fig. 3 caption)
Problem: The factor is written as Ωext
r = Ωstd
r (1 + 0.3 7/8 (4/11)4/3), which is ambiguous (missing multiplication symbols).
Required fix: Write explicitly Ωext
r = Ωstd
r [1 + 0.3 × (7/8) × (4/11)4/3] and, if used anywhere, define ΔNeff ≡ 0.3 in the caption or body.

P1A-m8 (Define ε tensor vs. symbol; Sec. X B–D; Eq. (23))
Problem: The symbol εμνρσ is used without stating whether it is the Levi-Civita tensor or the tensor density (and with what metric/sign conventions). This matters for identities like e ∧ e ∧ R = −NY + T ∧ T and for the “Bianchi-vanishing” argument.
Required fix: Add a one-sentence convention statement (tensor vs. density, ϵ0123 = +1, metric signature, and how √−g is handled) where ε appears.

P1A-m9 (Figure 5 bottom-panel numeric claims without citations; Sec. XII; Fig. 5)
Problem: The “fine-tuning score” bars for ΛCDM (10^122), quintessence (10^60), f(R) (10^40), and “spin–torsion (10^5)” are shown as precise orders without references in the caption or text.
Required fix: Cite sources for each bar or annotate the panel “schematic/illustrative only” and remove the specific numeric labels.

P1A-m10 (Consistency of “calligraphic” vs. plain symbols for duals; multiple places)
Problem: The manuscript alternates between F̃ and “Fe” (likely intending F F̃) and between R∧R̃ and R∧Re. This is confusing.
Required fix: Standardize to Fμν F̃μν and R ∧ R̃ throughout.

P1A-m11 (Abstract claim linkage and explicit location)
Problem: The abstract highlights “13 distinct barriers (14 historical entries),” but a reader benefits from a precise pointer. While Sec. IX has Table II, this should be referenced explicitly in the abstract for traceability.
Required fix: Add “(see Table II)” after the first mention of “13 distinct barriers” in the abstract.

CROSS-CHECKS AND ARITHMETIC (new)

- Small-angle separation significance (Conclusions, LiteBIRD vs current βobs): The calculation 0.072° / sqrt(0.03^2 + 0.094^2) ≈ 0.73σ is correct.

- WKB condition for Appendix C: With α/M = 10−30 eV−1, fa ≃ MPl ≃ 1.22×10^28 eV, and a H0 ≃ H0 ≃ 1.5×10−33 eV, (α/M) ϕ′ ~ 10−35 eV vs k150 GHz ≃ 6×10−4 eV gives a ratio ~3×10^31, so the stated “~30 orders of magnitude” is arithmetically sound.

- Radiation fraction bound from rotation (Sec. II C, Fig. 3 caption): ρrot/ρΛ = cω (ω/H)^2 / (3ΩΛ). With (ω/H)0 < 5×10−11 and ΩΛ ≈ 0.7, this yields < 2.5×10−21 / 2.1 ≈ 1.2×10−21 (for cω = 1), consistent.

- Log factor in Eq. (7): Using M = MPl/√γ and g^2 = 4π αem, the estimate (α/M) MPl ≈ (g^2/32π^2) γ (MPl/M) ln(...) = (g^2/32π^2) γ3/2 ln(...) numerically gives ≈ 3×10−3, consistent.

ABSTRACT FAITHFULNESS AND BODY SUPPORT (new)

P1A-E11 (Abstract phrase “we derive a parity-odd effective action through four steps,” Sec. II A.2)
Problem: Steps 3–4 introduce a phenomenological ansatz and a one-loop-motivated scale, not a derivation of a controlled, dimension-4 local operator (Appendix B admits this). Yet the abstract wording reads as if a derivation is supplied.
Required fix: Reword the abstract to state explicitly that (i) the on-shell scaling is an ansatz, and (ii) the one-loop “effective action” used for R2 is an EFT upper-bound ansatz with unresolved dimensional normalization (pending the fix to Eq. (14)).

I believe these additional issues materially affect the paper’s rigor and self-consistency. The most urgent technical correction is the dimensional inconsistency in Eq. (14); the clearest structural clarifications are to avoid double counting in the starting action and to restate any load-bearing assumptions from unpublished companions directly in this manuscript.