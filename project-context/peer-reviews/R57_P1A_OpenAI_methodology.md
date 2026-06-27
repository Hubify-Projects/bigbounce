# P1A R57 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/private/tmp/R57_P1A/paper1a_ech_nogo.pdf` md5=9a9dd83f pages=29
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (8465 chars)
**Wall time**: 275.2s

---

Referee report for Physical Review D (Methods, Cosmology)

Manuscript: “Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter”

Overall scope
The manuscript proposes a “channel-level” closure of four routes in minimal Einstein–Cartan–Holst (ECH) gravity to source late-time dark energy and parity-odd cosmological signatures, culminating in a “perturbation-transparency” result for canonical scalar matter. The core technical pieces are: (i) a torsion-elimination/NJL contact argument (R1), (ii) an EFT-motivated one-loop parity-odd operator scaling (R2), (iii) a γ (Barbero–Immirzi) running ansatz (R3), (iv) a spectator-ALP birefringence mapping (R4), and (v) a transparency proof based on the vanishing of torsion for scalar matter and the algebraic Bianchi identity that nulls the Holst dual contraction on the Levi-Civita connection.

While the conceptual program is interesting, the present submission does not meet PRD methodological standards as written. There are foundational issues with dimensional consistency, reliance on unpublished or “in preparation” companion works for load-bearing numbers and figures, use of an off-shell dimension-1 operator as if it were a Lagrangian density, heuristic scalings used to produce numerical benchmarks (e.g., Ntot ≈ 92) without a derivation, and several quantitative claims lacking explicit computations. Below is a detailed, itemized audit.

Findings

ESSENTIAL (paper cannot be accepted without these fixes)

P1A-E1 (Abstract + throughout; pages 1–3, 6–9, 22–27)
Problem: Load-bearing use of a non-EFT, off-shell dimension-1 “parity-odd operator.” Eq. (6) defines Seff ∝ (α/M) ε e e F with off-shell mass dimension +1 (Appendix B, Eq. (B1)), explicitly acknowledged as non-EFT. Yet the text repeatedly uses its on-shell “scaling ansatz” to define the dark-energy normalization Ξ and to compute Ntot ≈ 92 (Eq. (11), Sec. XII A, Appendix B). This operator is not a valid local action density. The core quantitative claims (Ξ ∼ 10−123, the Ntot bookkeeping, and Figures relying on this normalization) rest on this ansatz.
Required fix: Either (i) promote the operator to a dimension-4 EFT operator with an explicit, well-defined coupling (e.g., replace α/M → α M^3_Pl/M or provide a derived, diffeomorphism-invariant operator basis that yields a controlled dimension-4 local density), and propagate all numerical consequences, or (ii) remove all quantitative claims that depend on Eq. (6)/(B2) (Ξ, Ntot ≈ 92, Figure 3 orange curve, etc.), demoting them to qualitative speculation. A PRD article cannot base quantitative conclusions on a non-EFT action density.

P1A-E2 (Stand-alone reproducibility; pages 3–5, 10–11, 15–16, 22–26)
Problem: Heavy reliance on unpublished “companion” works for load-bearing results and figures. Examples: SPHEREx fNL Fisher forecast (2.6–5σ) [2], NaMaster birefringence pipeline and ALP MCMC [6], real-KDE PTA γPTA reanalysis [46], galaxy-chirality catalog [23]. These provide numerical values used in figures/tables/text (e.g., Fig. 4/7 trajectories, Table I notes, Sec. XIII), but are “in preparation” and thus not verifiable.
Required fix: Replace all “in preparation” citations with public arXiv preprints or include the full derivations, datasets, and code sufficient to reproduce every number and figure in this manuscript within the present paper or its Supplemental Material. Remove or clearly bracket any results that cannot be independently verified at acceptance time.

P1A-E3 (Action definition; page 5, Eq. (1))
Problem: The displayed “Einstein–Cartan–Holst action” includes a 1/4 TabcTabc term under the overall 1/(16πG) prefactor, while the text states this is “on-shell shorthand” for the four-fermion term and is “not varied independently.” As written, Eq. (1) is a functional to be varied; including T^2 there and then declaring it “not varied” is inconsistent and risks double-counting and confusion.
Required fix: Replace Eq. (1) by the standard Einstein–Cartan–Holst+Dirac action without the T^2 term; then derive and display the Hehl–Datta effective four-fermion Lagrangian after eliminating torsion. Alternatively clearly separate “off-shell action” from “on-shell effective action” in distinct equations, and ensure later derivations (Eqs. (3–4, 13)) follow from the off-shell action only.

P1A-E4 (Data/code availability; page 26)
Problem: The Data and Code Availability section promises a future Zenodo DOI and references a GitHub repo but does not provide a frozen release or commit hash for the exact version that produces the manuscript’s figures/tables. Given the heavy reliance on custom pipelines, a PRD methods paper requires immediately usable artifacts.
Required fix: Provide a Zenodo DOI for a frozen snapshot containing all scripts, configuration files, fixed random seeds, and input data subsets needed to regenerate every figure/table in this manuscript without the companions. Include the exact commit hash(s) in the paper.

P1A-E5 (Unpublished numerical inputs in figures; pages 8, 16, 23; Figs. 3, 4, 7; Table I)
Problem: Figures 3, 4, 7 and Table I/Appendix entries draw specific numbers from unpublished internal analyses (e.g., H0 = 69.2 vs 67.36; SPHEREx σ(fNL); joint “significance” tracks; β forecast overlays) and then mix them with published values. The captions caveat partially, but the numbers are not traceable.
Required fix: Either remove the numeric curves/points derived from unpublished analyses or replace with published values (with citations) and/or analytic placeholders. For any retained curve, explicitly state the data source, algorithm, and reproducibility pointer (file path in the archived code).

P1A-E6 (Abstract and conclusions – scope inflation; page 1, 25)
Problem: The abstract states “channel-level closure” of four routes at “amplitude-budget granularity” and presents two “surviving predictions.” However, several closures (R2, R3) depend on explicit ansätze, and key numerical pieces (Ξ, Ntot ≈ 92) rest on a non-EFT operator. The two “surviving” predictions are explicitly not ECH-specific, and one depends on an unpublished forecast. The abstract’s certainty exceeds what is rigorously derived in the body.
Required fix: Reword the abstract and conclusions to align with what is strictly proven without the nonlocal ansatz or unpublished companions. Clearly state “conditional on the stated EFT/scaling ansätze” where appropriate. Remove the quantitative Ntot ≈ 92 and similar numbers unless derived from a controlled EFT operator or fully justified.

P1A-E7 (Standalone-reader test for all symbols/constants; multiple sections)
Problem: Several quantities appear without self-contained derivations: the one-loop coefficient in Eq. (7) (and its mapping to [(α/M) MPl] ~ 10−2), the (Treh/MGUT)3/2 factor in Eq. (11), the ΩGW ceiling Eq. (20), and geff ∼ H0/MPl in Eq. (18). These are admitted as ansätze, yet they feed directly into numerical or qualitative “closure” claims.
Required fix: For each of these four places, either provide a compact, self-contained derivation (including dimensional analysis and assumptions) or move the statements to a clearly marked “speculative outlook” subsection and remove any closure claims that rely on them.

P1A-E8 (Galaxy-chirality amplitude claim without computation; pages 9–10, 15)
Problem: The paper asserts that the α/M ∼ 10−21 GeV−1 coupling “underpredicts any plausible spin asymmetry by > 100 orders of magnitude,” but no calculation is shown. This is used to support the “confirmed null” narrative and to discount galaxy-spins as a test channel in this framework.
Required fix: Provide an explicit calculation linking the torsion/ALP coupling to a predicted spin-dipole amplitude (even order-of-magnitude), with all assumptions stated, or remove/soften this numerical statement.

MAJOR (significant revision required)

P1A-M1 (Sigma mixing hygiene; pages 1, 10–11, 16, 23, 25)
Problem: The manuscript juxtaposes multiple σ-level statements from different null procedures: WMAP+Planck β (∼3.6σ), ACT DR6 (∼2.9σ), SPHEREx fNL forecast (2.6–5σ), and a “∼9σ” LiteBIRD detection of β≠0. While several places add caveats, there remain instances where these are presented together without per-instance “not directly comparable” notes (e.g., Fig. 4/7 curves labeled “Detection Significance (σ)” without a per-curve null-hypothesis definition).
Required fix: For every σ value shown or quoted, specify the null hypothesis and the test statistic. In any place where values from different null procedures appear on the same axis/figure/caption, include a local, explicit “not directly comparable across datasets/procedures” disclaimer and, where possible, add an effect-size axis (e.g., fractional rotation angle, forecast σ(fNL)).

P1A-M2 (Eq. (15) one-loop ratio derivation; page 12)
Problem: The dimensionless ratio Δθone-loop/Δθobs is presented with a compact contraction of scales. While the back-of-the-envelope evaluation gives ~10−60, the route from Eq. (14) to Eq. (15) is not fully spelled out, and the insertion of βobs and MPl factors may obscure units to some readers.
Required fix: Add a short derivation starting from Eq. (14), specify the mapping from ∂μJ5μ to FF̃ via the anomaly with all coefficients, track units consistently (GeV/eV), and show explicitly how H0/MPl enters. Include a numeric line showing the intermediate values (αem/4π ≈ 5.8×10−4, H0 ≈ 1.5×10−33 eV, MPl ≈ 1.22×10^28 eV, (α/M)MPl ≈ 10−2) to make the 10−60 conclusion transparent.

P1A-M3 (Barrier 12 ceiling; page 19–20, Eq. (20))
Problem: The “vacuum amplification ceiling” ΩGW|bounce ≲ (ρcrit/ρPl)^2 ≃ 0.07–0.17 is used as a barrier but is explicitly stated to be an “order-of-magnitude ceiling ansatz,” with no derivation or reference. It is then tied to current PTA amplitudes by suggestion.
Required fix: Either provide a derivation or literature reference justifying the quadratic scaling and the numeric window, or delete this barrier as a quantitative constraint. If retained qualitatively, state clearly that it is not used in any exclusion and remove any suggestive quantitative implications.

P1A-M4 (Dinf prefactor and Ntot sensitivity; pages 8–9, 22–24)
Problem: Eq. (11)’s Dinf = e−3Ntot (Treh/MGUT)3/2 is a key ingredient for Ntot ≈ 92. The exponent 3/2 is justified by a heuristic “parity-odd density-of-states” argument, not by a calculation. The paper concedes this but still uses specific e-fold numbers in several discussions and figures.
Required fix: Either (i) provide a calculation of the prefactor starting from a thermal partition function or a controlled kinetic argument, or (ii) remove specific Ntot numbers and replace by inequalities or scaling relations (e.g., “Ntot must be O(10^2) within ±O(1) e-folds”) and eliminate any claims that hinge on the exact central value.

P1A-M5 (Fig. 3 and associated text; page 8)
Problem: The “ECH dark-energy model vs ΛCDM H(z)” plot uses an illustrative parameter set tied to Ξ via the non-EFT operator and an H0 that is not from a published chain. The lower panel claims “∼2–3%” deviations across z=0–3. No uncertainty bands or systematic budget are shown; the parameter provenance is not standalone-verifiable.
Required fix: Either remove Fig. 3 or regenerate it using a publicly documented model anchored in a valid EFT operator or standard ΛCDM + phenomenological Λeff with uncertainties. Explicitly label it as schematic if it is not a data-driven inference, and remove the percent-deviation claims or qualify them as illustrative only.

P1A-M6 (PTA “γPTA = 2.567 ± 0.382” usage; pages 5, 21)
Problem: The quoted PTA spectral index result is from a companion “real-KDE GPU MCMC” [46], not yet public. It is used to position the matter-bounce prediction relative to data.
Required fix: Replace this with a published PTA spectral index posterior (e.g., NANOGrav 15-yr results) or remove the quantitative comparison. If retained, provide the exact analysis description and reproducibility pointers within this paper or Supplemental Material.

P1A-M7 (Operator parity classification; pages 12–13, footnote)
Problem: The operator ∂μϑNY J5μ is called “parity-odd phenomenology,” but the Lagrangian term is parity-even, with parity violation arising from a P-breaking background. This is explained in a footnote and can confuse readers when cross-referenced to “parity-odd” routes.
Required fix: Harmonize the terminology: refer to “parity-violating phenomenology induced by a P-breaking background” consistently, and reserve “parity-odd operator” for operators that transform oddly under P. Add a one-sentence reminder wherever this route is summarized.

P1A-M8 (Clarity and length; full manuscript)
Problem: The manuscript is 29 pages with extensive programmatic narrative and repeated caveats. The core technical contributions (torsion-elimination NJL recap, amplitude suppression estimates, perturbation-transparency argument) could be presented more concisely with clearer separation of derived results vs. speculative framework.
Required fix: Reduce to ≤20 pages by moving descriptive program elements and speculative diagnostics (e.g., the 14-barrier catalog that are not quantitatively derived here) to Supplemental Material, while tightening the main derivations and quantitative tests in the main text.

MINOR (address but paper can proceed)

P1A-m1 (Arithmetic checks; multiple)
- Eq. (15) numeric contraction yields ~10−60; consistent.
- NJL energy density estimate on p. 11–12: ρNJL ≈ 4×10−81 eV^4 is consistent from inputs.
- ρΛ ≈ (2.3 meV)^4 ≈ 2.8×10−11 eV^4; OK.
- β differences and σ-combination (0.127/0.120 ≈ 1.06σ) and the LiteBIRD-vs-Planck combined uncertainty 0.072/0.0987 ≈ 0.73σ; OK.
- ρcrit/ρPl from Eq. (9) evaluated at γ=0.2375 (≈0.41) and 0.274 (≈0.27) matches the stated range; OK.
Required fix: None; retain numerical lines in-text for readability.

P1A-m2 (Equation (3) conventions; page 6)
Problem: Two different torsion-weight conventions are mixed in the text/footnote. While the footnote resolves it, readers can be confused.
Required fix: Add a compact convention table in an appendix or at first use, stating explicitly the mapping between Tλμν = Γλ[μν] vs 2Γλ[μν].

P1A-m3 (Figure axis annotations; Figs. 4, 7)
Problem: “Detection Significance (σ)” y-axes do not state the null hypothesis per curve.
Required fix: Annotate in the caption or legend the null being tested for each curve (β=0 uniform rotation; fNL=0 local-type; etc.).

P1A-m4 (Terminology: “spectator-ALP β ≈ 0.27° prediction”; pages 1, 23–26)
Problem: The manuscript sometimes calls β ≈ 0.27° a “prediction” while elsewhere it is “a benchmark consistency point.” The latter is correct in this context (α/M is fitted).
Required fix: Replace all occurrences of “prediction” for β with “benchmark consistency point” or “fit-matched benchmark.”

P1A-m5 (Bibliography consistency)
Problem: Some references have future years (2025/2026) and rely on arXiv preprints; ensure citation formats match PRD style (journal, volume, page, arXiv ID).
Required fix: Standardize to PRD bib style; ensure all arXiv IDs correspond to the cited claim (e.g., LiteBIRD forecast σ(β) source).

NIT (cosmetic)

P1A-n1 (Hyphenation and accents)
Minor typos such as “ans¨atze” and broken hyphenation across lines appear a few times (pages 1–4).
Required fix: Run a typographical cleanup.

P1A-n2 (Footnote formatting)
Some long footnotes break the reading flow (pages 6, 12–13, 21). Consider moving technical asides to an appendix.

P1A-n3 (Figure aesthetics)
Fig. 5 lower panel “fine-tuning score” bars would benefit from stating explicitly that these are orders-of-magnitude and are not derived within this paper (already stated in caption, but could be emphasized).

Abstract-last drift sweep (pattern-045)
- “We assess four enumerated minimal-ECH ... and find that each is constrained...” This matches the main text only if all ansatz caveats are pulled up front. As written, the abstract acknowledges assumptions for R2–R3 and the naturalness closure for R4; OK if strengthened per P1A-E6.
- “Central result is a perturbation-transparency result...” The body provides a compact argument; OK.
- “Two predictions surviving ... are not predictions of ECH itself ...” This is stated; OK.
- All quoted numbers (βobs, ACT β, SPHEREx 2.6–5σ) are consistent with body statements and carry at least one disclaimer. OK.

Provenance surfaces (patterns 046/047)
- The GitHub link is provided but without a frozen DOI or commit hash. See P1A-E4.
- The text implies data and chains exist (“frozen accepted samples”) but they are not integrated into this paper. Either remove or publish links with hashes.

Uncomputed quantitative claims (pattern-048)
- Galaxy spin “>100 orders of magnitude” underprediction (P1A-E8).
- Barrier 12 ceiling (P1A-M3).
- Eq. (18) “geff ∼ H0/MPl” scaling (P1A-E7).

Effect sizes
- Where σ are presented, add effect sizes (e.g., β in degrees; fNL values) consistently alongside σ, especially in Figs. 4 and 7 (P1A-M3, P1A-m3).

Recommended maximum page count
Given the methodological contribution, a ≤20-page main text would be appropriate, with lengthy programmatic narrative and catalogs moved to Supplemental Material.

## Summary recommendation
MAJOR REVISIONS

The manuscript presents an interesting and potentially useful “perturbation-transparency” observation and a structured audit of several ECH routes. However, the present version relies on a non-EFT operator to produce quantitative normalizations, draws heavily on unpublished companion works for key figures and numbers, and includes several heuristic scalings used to make numerical claims without derivations. To meet PRD standards, the authors must either supply controlled EFT derivations (or remove dependent quantitative claims), replace unpublished inputs with publicly verifiable ones, freeze and archive all code/data artifacts, and tighten sigma-reporting hygiene and length. Once these issues are addressed, the core transparency result and amplitude-level closures could be evaluated on their own merits.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes audit)

P1A-E9 (Eq. (14) dimensional inconsistency; page 12)
Problem: The one-loop operator is written with an explicit factor of MPl in the numerator,
Γone-loop ⊃ −(1/16π^2) β(γ) MPl ∫√−g ∂μϑNY J5μ,
but the text immediately below states the coefficient is “multiplied by the Planck mass to a single negative power.” Dimensional counting confirms the mismatch: [∂ϑ] = +2, [J5] = +3, so the integrand is +5 and needs a coefficient of mass dimension −1 (i.e., 1/MPl), not +1. As written the Lagrangian density is not dimension-4.
Required fix: Correct Eq. (14) to carry 1/MPl (or an explicit mass M−1) and propagate the change into Eq. (15) and any numerical ratios. Clarify the mass-dimension assignment for ϑNY and the anomaly mapping used.

P1A-E10 (Stand-alone referencing breach in Appendix C; page 28)
Problem: Appendix C’s normalization chain explicitly refers to “the convention block of the companion’s §VI8,” which is not part of the present submission and cannot be verified by readers.
Required fix: Remove all references to companion-section numbering and reproduce the full normalization (including the gaγ mapping, sign conventions, and any 2π/4π factors) in this paper or in its Supplemental Material.

P1A-M9 (Inconsistent H0 values across the manuscript; pages 8, 15, 26)
Problem: Three different H0 values are used without justification: 69.2 km/s/Mpc (Fig. 3 orange curve), 67.68 ± 1.06 (companion MCMC, abstract/§III), and 67.36 (Planck-VI reference in Fig. 3 caption). These inconsistencies can change percent deviations and any figure overlays.
Required fix: Adopt a single baseline (with uncertainty and citation) throughout, or clearly label which value is used where and why. If Fig. 3 is schematic, state so prominently and remove quantitative percent claims tied to mixed H0 inputs.

P1A-M10 (Inconsistent anchoring for α/M across sections/figures; pages 6–7, 13–14, 18, 27)
Problem: The one-loop estimate yields [(α/M) MPl] ≈ 3×10−3 (Eq. (7) evaluation), while other places adopt 10−2 for the same product and figures are anchored at α/M ≈ 10−21 GeV−1. The paper calls this “within a factor of a few,” but no unified uncertainty or propagation is shown. In addition, the figure “RG running of α/M” is anchored at the 10−21 GeV−1 benchmark without showing how the running law is obtained from Eq. (7).
Required fix: Provide a single, consistent anchor for [(α/M) MPl] with an explicit uncertainty (from the log, γ, and δNY), show how it maps to α/M at the reference scale used in figures, and propagate the range wherever α/M enters quantitative statements. If α/M is purely phenomenological, label all anchored curves as such.

P1A-M11 (Opaque normalization for the rotation-energy fraction; page 8, Fig. 3 caption)
Problem: The conversion from the bound (ω/H)0 < 5×10−11 to a contribution “≲ 10−21 ρobsΛ” uses the step “dividing by 3ΩΛ ≈ 2.1,” but the derivation is not shown and the intermediate units are unclear (Λeff term vs energy density).
Required fix: Provide a two-line derivation showing how cω ω^2 in Eq. (10) translates to a fraction of ρΛ, including any factors of 3M2
Pl H2 and ΩΛ. Otherwise, remove the quantitative “≲ 10−21 ρobsΛ” claim.

P1A-M12 (Notation collision for curvature/EM field strengths; pages 6 and 13)
Problem: The manuscript uses F for the gravitational curvature two-form in Eqs. (5–6) and Fμν for electromagnetism (Sec. IV D). Although a sentence notes this, Eq. (6) reverts to FIJ without calligraphic/curly notation, creating avoidable confusion in a paper that discusses both sectors side-by-side.
Required fix: Use distinct symbols throughout (e.g., ℛIJ for gravitational curvature and Fμν for electromagnetism), and revise Eq. (6) accordingly.

P1A-M13 (Ambiguity in the mass dimension of the Nieh–Yan pseudoscalar; pages 12–13)
Problem: The text asserts ϑNY has mass-dimension +1, but in many treatments the “axion-like” angle is dimensionless and the canonical field carries the mass dimension via fa. The present paper uses both dimension-1 ϕ and dimensionless θ in different contexts; the Nieh–Yan ϑNY is introduced without a construction that fixes its mass dimension.
Required fix: Define ϑNY explicitly (e.g., as a dimensionless angle with an associated decay constant, or as a canonically normalized field) and ensure Eq. (14)’s dimensions follow from this definition. Align the dimensional choice with Appendix C’s θ/ϕ conventions.

P1A-J2 (Conflation risk: identifying α/M from the Holst/Nieh–Yan sector with the photon Chern–Simons coupling; pages 13–14, Appendix C)
Problem: The text sometimes equates α/M with gaγ, while earlier α/M was motivated by gravitational-sector renormalization with M set by the area-gap scale (Marea-gap ≈ MPl/√γ). Equating these couplings assumes a UV completion linking the two sectors, which is not derived here.
Required fix: Either provide a model that enforces α/M = gaγ, or treat them as independent parameters and adjust the β–ρΛ mapping and constraints accordingly. At minimum, add a clear “assumption” box where this identification is used.

P1A-B1 (Figure-caption vs body mismatch: Appendix C normalization)
Problem: The caption-level statement “this mapping is what Eq. (17) and the Route-2 estimates of Sec. IV use” relies on a convention chain that is not reproduced in the body and points to a companion. This contradicts the “standalone derivation” expectation for a Methods paper.
Required fix: Inline the full mapping with all constants (1/2, 2π vs 4π, fa normalization) in the main text where β is used, or in a self-contained appendix section without external references.

P1A-J3 (Symbol reuse: γ as both Barbero–Immirzi parameter and PTA spectral index; pages 5, 21)
Problem: Although the manuscript states the distinction, the reuse of γ for two unrelated quantities still invites confusion, especially in figures/tables where the context is minimal.
Required fix: Use a different symbol for the PTA spectral index (e.g., nGW or γPTA → nPTA) in both text and figures.

P1A-J4 (Stale/cross-paper pointer in Appendix C; page 28)
Problem: The line “this reproduces the companion pipeline’s β = (αem Caγ/4π) (Δϕ/fa) … the companion’s §VI8” is a stale, cross-paper internal pointer that will not be interpretable post-publication.
Required fix: Replace with a self-contained derivation and a literature citation for the dispersion relation and rotation mapping; remove the companion pointer.

P1A-m6 (Define ρPl explicitly; page 7, Eq. (9))
Problem: ρPl is used without explicit definition in the main text (Planck density based on unreduced vs reduced MPl can differ by (8π)2 in some conventions).
Required fix: Add the definition of ρPl consistent with the unreduced MPl convention adopted in the paper.

P1A-m7 (Minor figure-caption hygiene; Figs. 4 and 7)
Problem: The “Detection Significance (σ)” axes include “Combined (ρ=...)” curves; the caption notes cross-correlation but does not specify the combination rule or null. This is especially important because β and fNL sigmas come from different null procedures.
Required fix: In each caption, state the null per curve and the combination rule used (e.g., inverse-variance sum with assumed correlation ρ), plus an explicit “not directly comparable across procedures” note on the y-axis legend.

P1A-m8 (Arithmetic spot-check: α/M product variability)
Observation: Using Eq. (7) with γ = 0.274, g2 = 4παem, and ln(Λ2/μ2) ≈ 74 produces [(α/M) MPl] ≈ 3×10−3 as stated; the paper elsewhere uses 10−2. This is within “factor-of-few,” but impacts Ntot bookkeeping when combined with Dinf. No required fix beyond P1A-M10 if the variability is explicitly bracketed.

P1A-m9 (Equation label/cross-ref clarity; multiple)
Problem: Several places refer to “Sec. X G; 2027–early-2030s,” mixing section cross-references with timeline annotations inline. This reads like a marginal note that survived editing.
Required fix: Remove timeline annotations from cross-refs; keep section references clean.

NO OTHER ARITHMETIC MISMATCHES FOUND
- Recomputed ratios and conversions quoted in the manuscript (β in radians, Δθone-loop/Δθobs ~ 10−60 with the stated inputs, NJL ρ estimate, ρcrit/ρPl range, β-difference significance, Dinf ≈ 10−121 for Ntot ≈ 92 with the stated prefactor) are numerically consistent as back-of-the-envelope checks. The principal issues are dimensional consistency, symbol/parameter consistency, and standalone reproducibility, as itemized above.