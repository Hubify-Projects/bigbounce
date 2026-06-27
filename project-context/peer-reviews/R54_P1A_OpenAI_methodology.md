# P1A R54 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/private/tmp/R54_P1A/paper1a_ech_nogo.pdf` md5=439212bf pages=29
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (11671 chars)
**Wall time**: 427.4s

---

Referee report on “Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter”

Scope of review
- Focus: methodology rigor, derivations, dimensional analysis, arithmetic consistency, statistical validity, and reproducibility.
- I audited every equation, numerical substitution, sigma claim, figure/table caption and axis labeling in the submitted 29-page manuscript.

Overall assessment
The manuscript assembles a set of amplitude-level “no-go” arguments for four enumerated channels within minimal ECH, together with a formal “perturbation-transparency” statement. While many caveats are explicitly stated, the paper, as submitted, relies heavily on non-public companion papers for key numerical inputs, mixes phenomenological ansätze with quantitative conclusions without fully isolating them methodologically, and includes estimates that are not derived from a closed EFT or a reproducible pipeline. Several quantitative claims (notably the Route-2 one-loop amplitude bound and the Hubble-parameter comparison) are heuristic rather than derived; the data/code availability is not yet archival; and some numerical ratios use inconsistent benchmarks.

I list detailed findings below, each with an ID, location, issue, and required fix.

Findings

ESSENTIAL

P1A-E1 — Standalone-Reader failure: reliance on non-public “companion” papers for load-bearing numbers
- Location: pp. 3–5 (end of Section I B and the “Companion paper” paragraph), Table IV p. 27, Fig. 1 caption p. 5, Sec. III B p. 10, Sec. XIII pp. 23–24, Data/code availability p. 26.
- Problem: Multiple numerical statements are imported from “Paper I(b) [6] (in preparation)”, “Paper II [2] (in preparation)”, and “Paper III [46] (posted concurrently/on arXiv)” without methods, priors, masks, or chain diagnostics in this manuscript. Examples include:
  - H0 = 67.68 ± 1.06, ∆Neff ≈ 0 (Table IV; Sec. I B); 309,189 “frozen accepted samples.”
  - γPTA = 2.567 ± 0.382 (Fig. 1 caption; Sec. X G) from a “real-KDE GPU MCMC reanalysis.”
  - SPHEREx σ(fNL) projections and “2.6–5σ realistic significance” tied to Paper II.
  - NaMaster pipeline validation and ALP parameter fits claimed but deferred.
  Authors explicitly say these are “not independently peer-reviewable values until Paper I(b) is publicly posted,” yet they appear in tables/figures of the present paper.
- Required fix: Make the manuscript self-contained. Either:
  (a) remove all quantitative results that depend on non-public companion work (Table IV values, γPTA posterior, Fisher ranges, etc.) and rephrase any statements that rely on them so they become citations to external, already-published work; or
  (b) fully include in this manuscript the methods, datasets, priors, masks, likelihood definitions, chain configurations, burn-in, convergence diagnostics (R̂, ESS), and links to frozen chains such that a referee can reproduce the quoted numbers without opening any companion paper.

P1A-E2 — Data/code availability not archival; missing immutable identifiers
- Location: Data and Code Availability, p. 26.
- Problem: Only a GitHub link is provided; the text promises a future Zenodo release “will pin all artifacts.” No tag/commit hash is specified for the version corresponding to this submission; no DOI is provided; no guarantee of future immutability.
- Required fix: Provide an immutable archival release for all artifacts referenced in the paper (code, configs, frozen chains, catalog snapshots) with a DOI (e.g., Zenodo) and cite that DOI in the paper. Include the exact Git tag/commit hash used to produce each figure/table; ensure the repository contains the frozen chains and configuration files as described.

P1A-E3 — Route-2 amplitude (one-loop Holst-sector) quantitative bound lacks a controlled derivation
- Location: Sec. IV B, pp. 12–13, Eq. (14) and Eq. (15).
- Problem: The dimensionless ratio ∆θone-loop/∆θobs is formed using a chain of heuristic identifications that are not derived from a specific EFT linking ∂μϑNY J5μ to a photon FF̃ term; the 10−60 suppression claim depends on mixing an H0/MPl factor with an R4-fitted α/M obtained from an unrelated spectator-ALP operator. While the text calls it an “amplitude-budget bound,” PRD requires that quantitative claims be supported by a controlled derivation or that the numbers be removed or explicitly marked qualitative.
- Required fix: Provide a concrete calculation for Route-2 starting from a specified EFT that yields a photon coupling (or an unambiguous projection through the chiral anomaly with clear intermediate steps and renormalization scheme), propagate it to a rotation angle with dimensional clarity, and show how the 10−60 bound follows; or else remove the numerical 10−60 bound and replace with a qualitative statement (e.g., “far below present sensitivity”) and eliminate Eq. (15) altogether.

P1A-E4 — Use of a dimension-1 operator as load-bearing input for quantitative “Ntot ≈ 92” statements
- Location: Sec. II A.2–A.3 pp. 6–8; Eq. (6); Appendix B p. 26–27; Sec. XII A p. 22; Sec. XIV D p. 24.
- Problem: The central parity-odd operator used in mapping to a dark-energy scale, Eq. (6), is explicitly acknowledged to have off-shell mass-dimension +1. Yet the manuscript repeatedly uses its on-shell scaling ansatz (Appendix B) to produce quantitative statements (notably the Ntot ≈ 92 figure and the “structural tension” with fNL), which are then woven into the narrative as key conclusions. The caveats are present but insufficient: PRD methodology standards require that any quantitative headline arising from a non-EFT operator be either (a) recast as a clearly segregated, non-load-bearing phenomenological exercise, or (b) replaced with a result from a consistent dimension-4 operator (e.g., by promoting the coupling to α MPl^3/M as noted).
- Required fix: Either provide the analysis using a proper dimension-4 local operator (with the three missing mass-dimensions in the coupling, including a discussion on naturalness and renormalization), or fully demote all quantitative inferences that depend on Eq. (6)/Appendix B (Ntot values, structural-tension plot text) to a non-load-bearing appendix and remove them from the abstract/conclusions.

P1A-E5 — Table IV reports “companion internal MCMC” posteriors with uncertainties; not reproducible here
- Location: Table IV, p. 27; also p. 4–5.
- Problem: The table mixes “fundamental theory parameters” with MCMC-derived cosmological parameters carrying ± errors from a non-public analysis. The paper says explicitly these are not peer-reviewable yet. Including them in a PRD submission table is not acceptable.
- Required fix: Remove the MCMC posterior rows (H0, ∆Neff, σ8, Ωm) from Table IV unless the full likelihood analysis is provided and the chains are archived as per E2. If retained, include full methodology in this manuscript.

P1A-E6 — Figures present companion-only numbers without methods (γPTA; SPHEREx fNL forecast)
- Location: Fig. 1 (caption), p. 5; Fig. 4 (caption), p. 16; Fig. 7 (caption), p. 23.
- Problem: γPTA = 2.567 ± 0.382 is shown as a panel annotation (“real-KDE reanalysis; GPU MCMC”), but no method is provided. The SPHEREx 2.6–5σ “realistic” range is asserted, tied to a non-public forecast.
- Required fix: Either remove these numerical overlays from figures or include the full analysis and data pointers in this manuscript. At minimum, if retained as citations, the figure captions must state explicitly that these numbers are external (with a citable DOI/arXiv link already posted) and not derived in this paper.

P1A-E7 — Abstract/Conclusions contain numerical/falsification timelines that rely on non-public analyses
- Location: Abstract pp. 1–2 (SPHEREx forecast significance; LiteBIRD discrimination phrasing), Conclusions p. 25.
- Problem: Several quantitative projections (“2.6–5σ,” “∼9σ,” “0.73σ separation”) appear in the abstract/conclusion. Some are demonstrative arithmetic, but they are interleaved with numbers imported from non-public forecasts. Mixing these in the Abstract without consistently flagging provenance violates journal standards for abstracts to summarize what is shown/proven in the paper.
- Required fix: Restrict the Abstract to statements proven or fully derived herein. Move all forecast numbers to the body with explicit provenance and remove any companion-dependent claims from the Abstract.

MAJOR

P1A-M1 — Inconsistent ρΛ benchmark used in the NJL ratio estimate
- Location: Sec. IV A, p. 11 (end of item (i)).
- Problem: The ratio ρNJL/ρΛ is quoted as “roughly 4 × 10−69 ρΛ” using ρΛ ∼ (10−3 eV)^4 = 10−12 eV^4. Elsewhere the paper consistently uses ρΛ ≈ (2.3 meV)^4 ≈ 2.8 × 10−11 eV^4. Using the latter gives ρNJL/ρΛ ≈ 4 × 10−81/2.8 × 10−11 ≈ 1.4 × 10−70, i.e., a factor ~30 smaller than reported. The order-of-magnitude conclusion stands, but the inconsistency must be corrected.
- Required fix: Use a single consistent ρΛ benchmark throughout. Re-compute and report the ratio with the adopted benchmark. If using 2.3 meV, state the number (≈1 × 10−70).

P1A-M2 — Route-2 operator parity/renormalization chain needs a precise reference and scheme
- Location: Sec. IV B, p. 12 (Eq. 14 and footnote 3).
- Problem: The operator ∂μϑNY J5μ is called a “parity-odd operator” in the section header but is acknowledged parity-even in the footnote; then its phenomenology is labeled parity-breaking via a background. This is conceptually fine, but the normalization (−1/16π^2 β(γ)/MPl) and its running need a precise citation with the adopted regularization for γ5 and the Nieh–Yan subtraction, otherwise the finite part is scheme-dependent (as the authors mention elsewhere).
- Required fix: Provide an explicit reference and, if possible, a brief derivation or an equation number from the cited source that justifies both the normalization and the running used in Eq. (14), including the treatment of the NY counterterm. Alternatively, label Eq. (14) as an upper-bound ansatz prominently in the section header and remove any implication that it is a direct consequence of the cited works.

P1A-M3 — Naturalness comparison bar chart lacks sources and definitions
- Location: Fig. 5 (bottom panel) and its caption, p. 18.
- Problem: The “fine-tuning score” entries for ΛCDM (10^122), quintessence (10^60), f(R) (10^40), and “spin-torsion (this work)” (10^5) are stated without definitions (what exactly is being tuned and how the score is computed) or references to calculations underpinning the 10^60 and 10^40 numbers. As presented, this is non-reproducible.
- Required fix: Define the fine-tuning metric used (e.g., log10 of ratio of UV to IR scales for a particular parameter), provide references or a short derivation for each bar, and include uncertainties. If such derivations are not available, remove the bar chart or move it to a qualitative discussion without numerical values.

P1A-M4 — Thermal washout argument needs at least one explicit rate-vs-H calculation
- Location: Sec. II C.1, pp. 8–9 (“Reheating thermal-reset barrier” paragraph).
- Problem: The argument that Γwash > H at Treh is plausible and likely correct for the top Yukawa, but as stated it is qualitative. One explicit numerical ratio Γ/H at the chosen Treh (with y_t, g*, MPl) should be shown to substantiate the key inequality; likewise, a clear statement for the sphaleron regime (provide numeric threshold) should be given.
- Required fix: Add a line computing Γ_t/H numerically at Treh ≈ 10^15 GeV (and quote the g* used) to show the margin, and provide the corresponding estimate for sphalerons at T ≈ few × 10^10 GeV. This keeps the argument quantitative and checkable.

P1A-M5 — Fig. 1 (left-to-right mapping) and Fig. 3 (H(z)) captions must clearly state “illustrative only”
- Location: Fig. 1 caption p. 5; Fig. 3 caption p. 8.
- Problem: Fig. 1 includes a numerical overlay for γPTA and dashed closings; Fig. 3’s orange curve is computed with specific parameter values (H0 = 69.2, Ωm = 0.310, Ωext_r scaling) without showing their source in this paper. The caption partly explains, but a reader could misinterpret these as derived or preferred fits.
- Required fix: Add a clear sentence to both captions: “All numbers in this figure are illustrative and not derived in this paper; no fit is performed here.” For Fig. 3, state explicitly that the parameter choices are illustrative benchmarks and that no inference is made.

MINOR

P1A-m1 — Clarify Λeff anatomy vs anisotropy
- Location: Sec. II C, p. 7–8, Eq. (10) and Fig. 3 caption p. 8.
- Problem: Λeff is written as Ξ MPl^2 + cω ω^2. Since vorticity sources anisotropic stress, not an isotropic vacuum term, the inclusion as “Λeff” could confuse readers.
- Required fix: Add a sentence in the main text near Eq. (10) clarifying that cω ω^2 is not an isotropic vacuum energy contribution but a bookkeeping bound on the possible size of rotational contributions to background kinematics; state that it is not used elsewhere.

P1A-m2 — Uniform convention for ALP–photon coupling normalization
- Location: Sec. IV D p. 13–14 and Appendix C p. 27–28.
- Problem: The paper alternates between −(α/4M) ϕ FF̃ and the canonical gaγ a FF̃/(4) conventions and notes a 1/(4π) vs 1/(2π) normalization issue in footnote 5. This is potentially confusing.
- Required fix: Choose one convention (e.g., gaγ) throughout, provide the conversion once, and then stick to it in all subsequent formulas and numerical estimates.

P1A-m3 — EB small-angle formula usage note
- Location: Sec. III A, p. 10, Eq. (12).
- Problem: The caveat “CBBℓ is not neglected in the published estimators” is stated; add a short parenthetical that lensing B dominates at current sensitivities, which is why full estimators include it.
- Required fix: One sentence addition after Eq. (12).

P1A-m4 — Spacing/typography nits
- Location: Throughout.
- Problems: Inconsistent spacing around numbers and units (e.g., “km/s/Mpc”), mixed hyphenation of names (Domaga la), and a few typeset artifacts “R R˜︁”.
- Required fix: Standardize unit spacing (e.g., km s−1 Mpc−1), fix author-name diacritics/hyphenation, and ensure consistent typesetting of duals/tilde symbols.

NIT

P1A-n1 — Acknowledgment of AI tool
- Location: Acknowledgments, p. 26.
- Problem: “The author acknowledges the use of Claude (Anthropic) ...” This is acceptable but unusual in PRD style.
- Fix: Optional — check PRD policy; if requested by editors, move to a footnote or remove.

P1A-n2 — Length relative to contribution
- Location: Whole manuscript (29 pages).
- Problem: For a “channel-level closure” methodology note, 29 pages is long; many caveats and companion-paper cross-references inflate the length without adding derivations.
- Fix: Consider reducing to ≤20 pages by removing companion-paper summaries, illustrative parameter tables, and non-load-bearing forecasts. Concentrate on the four closures (with derivations) and the perturbation-transparency proof.

Abstract-last drift sweep

- The abstract contains several numbers and qualifiers. Many are appropriately caveated (e.g., “not directly comparable” for the σ’s), but:
  - The SPHEREx “2.6–5σ” and LiteBIRD “9σ” statements belong to forecasts not derived here; they should not appear in the abstract unless fully derived in this paper. Move to body or remove (see E7).
  - Claims like “ΛCDM+∆Neff MCMC verification ... documented separately” should not appear in an abstract for a standalone PRD paper; remove.

Provenance surfaces

- The Data Availability statement promises a future archival pin; this must be resolved before acceptance (E2).
- Any reference to “frozen chains” must include a DOI and a hash.

Uncomputed quantitative claims

- Sec. XII A: “residual 10^5 fine-tuning” is tied to Ntot sensitivity; include the explicit mapping (already given) and note uncertainty bounds; move the bar chart to an appendix or justify.

Effect sizes

- Where σ appears (β ≈ 0.342° ± 0.094°, ACT DR6 0.215° ± 0.074°), the effect size is the absolute angle (deg), which is fine. For the fNL forecast, either provide the fractional amplitude context (e.g., expected ∆Cℓ/Cℓ) or remove from this paper.

Consistency checks

- Eq. (9) reproduces the quoted ρcrit/ρPl values for the two γ choices; arithmetic OK.
- Eq. (17) inversion gives ρθ consistent with 6 ρΛ once the GeV→eV conversion for α/M is correctly applied (10−21 GeV−1 = 10−30 eV−1); arithmetic OK.
- EB difference significance between WMAP+Planck and ACT DR6 computed as ~1.06σ (p. 14) is correct.

## Summary recommendation
REJECT

The manuscript, in its current form, does not meet PRD’s methodological and reproducibility standards. Core numerical statements rely on non-public companion papers; the data/code availability is not archival; a key quantitative bound (Route 2) lacks a controlled derivation; and a load-bearing energy-density mapping is built on a dimension-1 operator acknowledged to be an ansatz. The perturbation-transparency statement itself may be publishable once isolated and proved cleanly, but the present submission intermixes speculative/phenomenological elements, non-reproducible numerical overlays, and companion-only results. I encourage the authors to resubmit a substantially reduced, self-contained paper that (i) focuses on the perturbation-transparency theorem with full proofs, and (ii) treats the channel closures with controlled EFT derivations or clearly demotes them to non-quantitative statements, while eliminating all dependence on unpublished companion work and providing archival artifacts.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (new issues only; do not duplicate items from the initial report)

ESSENTIAL

P1A-E8 — “13 logically-independent barriers”: independence claim is asserted but not demonstrated
- Location: Abstract pp. 1–2; Sec. I A (items 1–3) pp. 3–4; Sec. IX and Table II p. 17; Conclusions p. 25.
- Problem: The manuscript repeatedly claims “13 logically-independent barriers (with B8 subsumed by B14).” No proof of logical independence is given (e.g., no dependency graph, no explicit minimality proof, no demonstration that assumptions used in B9/B10/B11 are not shared with B1–B7 in a way that would make them derivative). Several barriers share common assumptions (e.g., minimal ECH, torsion non-propagation, Planck suppression), suggesting potential overlaps.
- Required fix: Either (a) provide a concrete independence analysis (explicit assumption sets, a dependency DAG, and a short proof that each barrier is not a corollary of others under the same hypothesis set), or (b) rephrase to “13 barriers catalogued (with B8 subsumed by B14)” and drop the independence claim throughout.

P1A-E9 — Broken/ambiguous cross-references to companion material; inconsistent status labeling
- Location: Appendix C, final paragraph p. 28 (“companion pipeline’s §VI8”); Sec. X G p. 21 (Paper III §6 [46]); multiple “in preparation/posted concurrently” labels across [2], [6], [46].
- Problem: The citation “§VI8” is not a valid section label in this manuscript and is opaque for a reader; it likely refers to a section in a companion paper. Across the text, the same companion documents are alternately labeled “in preparation” and “posted concurrently,” making provenance unclear.
- Required fix: Remove all intra-companion section cross-references from this paper, or point to a publicly posted arXiv/DOI with precise section numbers. Make the status of each companion reference consistent in all locations (either posted with identifiers, or removed from load-bearing claims in this manuscript).

P1A-E10 — Action in Eq. (1) presents TabcTabc under 1/(16πG) as if fundamental, while the text says it is an on-shell shorthand
- Location: Sec. II A.1, Eq. (1), pp. 5–6 and the adjoining footnote.
- Problem: The displayed action includes +(1/4)TabcTabc multiplied by 1/(16πG) as if it were a term to be varied, then the prose says it is only an on-shell “shorthand” after eliminating non-propagating torsion and “is not varied independently.” Presenting it inside the gravitational action as written is misleading and dimensionally ambiguous prior to elimination.
- Required fix: Replace Eq. (1) by the true fundamental action to be varied (Einstein–Cartan–Holst + Dirac, without T^2), and move the four-fermion contact piece to a subsequent “effective action after torsion elimination” equation with its correct coefficient. Explicitly separate pre- and post-elimination Lagrangians.

MAJOR

P1A-M6 — Route-3 (Immirzi running) RG equation used (Eq. 16) is an ad hoc ansatz inconsistent with the literature; numeric ∆γ/γ ~ 10−2 lacks derivation
- Location: Sec. IV C, Eq. (16) and following paragraph p. 13.
- Problem: The adopted β-function dγ/dlnµ = (1/12π^2)(NLF − NRF)γ + O(γ^2) is not taken from a cited derivation. The most relevant computation (Benedetti & Speziale, JHEP 06 (2011) 107) shows a more complicated γ-running (sign and magnitude depend on |γ| and induced four-fermion terms), not a simple chiral-count proportionality. The subsequent numerical statement “∆γ/γ ∼ 10−2 over the running from the GUT scale to the IR” is not supported.
- Required fix: Replace Eq. (16) and the ∆γ/γ ≈ 10−2 estimate with either (a) the actual β-function and integrated running from a cited calculation (specify matter content, renormalization scheme, and energy interval), or (b) label Eq. (16) as a purely illustrative upper-bound toy model and remove any numerical conclusion (including the 10−63 suppression).

P1A-M7 — Fig. 5 (top): RG running of α/M lacks a β-function, integration limits, or boundary conditions; inconsistent anchoring
- Location: Fig. 5 top panel and caption p. 18; Sec. II A.2 Eq. (7).
- Problem: The plotted straight-line “renormalization-group running of α/M” from “Present” to “MPl” is shown without stating the β-function used, the renormalization scheme, scale steps, or the chosen boundary condition. Moreover, the text earlier treats α/M as a one-loop coefficient motivated at high scale; the figure appears to anchor α/M at the Planck scale and then “runs” to today, but the numbers (4×10−22 → 10−21 GeV−1) are unexplained and not reproducible.
- Required fix: Provide the explicit β-function used for α/M, the integration (µ0 → µ), and the boundary value at one end (with uncertainties), or remove the panel. If purely illustrative, label it as such and remove the numeric y-axis ticks.

P1A-M8 — Barrier 3 (Scalar-Tensor Universality) makes an unproven claim specific to the bounce point
- Location: Sec. IX C p. 17.
- Problem: It states “Torsion decouples from the FRW background precisely at the bounce density, yielding no distinctive perturbation signal.” No derivation or reference is given for a special decoupling “precisely at the bounce density.” The perturbation-transparency proof in Sec. X is general for canonical scalars and does not single out the bounce density.
- Required fix: Either supply a derivation (showing why the FRW background coupling vanishes “at ρ = ρcrit” but not generically), or revise the text to a general statement that follows from Sec. X (torsion vanishes for canonical scalars at all densities).

P1A-M9 — “>100 orders of magnitude” underprediction of galaxy spin asymmetry is asserted without a calculation
- Location: Sec. II C.2, p. 10; Sec. VI p. 15.
- Problem: The claim that the α/M ∼ 10−21 GeV−1 coupling “underpredicts any plausible spin asymmetry by > 100 orders of magnitude” is not backed by an explicit mapping from the operator to an observable A0 (or any proxy). No scaling or reference is provided.
- Required fix: Provide a back-of-the-envelope estimate linking the operator to a predicted dipole/quadrupole in galaxy spin (including redshift scaling and selection), or remove the quantitative “> 100 OOM” claim and keep the qualitative “consistent with null” statement.

P1A-M10 — “∼50 e-folds dilute rotation” lacks a quantitative demonstration or citation
- Location: Sec. II A.3 p. 7.
- Problem: The statement “Required dilution of inherited rotation is naturally achieved through ∼50 e-folds of inflation” is plausible but unsupported. The decay rate of vorticity in anisotropic (Bianchi) backgrounds requires a model and scaling (often ω ∝ a−1 or faster under inflation).
- Required fix: Provide a brief derivation or a citation quantifying the suppression of a representative vorticity measure to below the Saadeh et al. bound after N ≈ 50, or delete the numerical “∼50” and keep a qualitative remark.

P1A-M11 — Nieh–Yan pseudoscalar mass dimension and normalization not sourced
- Location: Sec. IV B, Eq. (14) and footnote 3 p. 12; Appendix B p. 26.
- Problem: The field ϑNY is taken to have mass-dimension +1 without citing a convention or a Lagrangian that normalizes it. Different treatments regard the Immirzi/Nieh–Yan field as a dimensionless angle; this choice affects the normalization of Eq. (14).
- Required fix: Specify the Lagrangian for ϑNY (kinetic term and coupling), give a reference for the chosen normalization/dimension, and ensure dimensional consistency across Eqs. (14)–(15).

P1A-M12 — Alternate “local-operator-promotion” route in Appendix B is asserted equivalent at OOM but not demonstrated
- Location: Appendix B p. 26–27 (paragraph “Either reading is a phenomenological dimensional assignment” and “Sharper dependency statement”).
- Problem: The text claims the on-shell MPl^5 vs local-operator-promotion α MPl^3/M routes yield the same Ntot at order of magnitude but provides no calculation or uncertainty budget. Given the three missing mass dimensions are central to the dilution bookkeeping, this needs to be shown.
- Required fix: Show the explicit Ntot values under both dimensional assignments (including the prefactors) and quantify the difference; otherwise, demote the “equivalence” claim and remove its use in any headline statements.

MINOR

P1A-m5 — Inconsistent H0 values across the manuscript without an explicit reconciliation
- Location: Fig. 3 caption p. 8 (H0 = 69.2 km s−1 Mpc−1 for orange; 67.36 for blue), Table IV p. 27 (H0 = 67.68 ± 1.06).
- Problem: Multiple H0 values are used in nearby contexts without a one-line note clarifying that distinct benchmarks are being used (Planck-VI best-fit vs internal companion posterior vs illustrative curve).
- Required fix: Add a short parenthetical in Fig. 3 caption and in Table IV noting the different provenances and that no joint fit is attempted here.

P1A-m6 — Notation collisions: β is both birefringence angle and an RG β-function; γ is both Barbero–Immirzi and PTA spectral index
- Location: Sec. IV B (β(γ) vs β ≡ rotation angle); Fig. 1 caption p. 5 and Sec. X G p. 21 (γPTA vs γBI).
- Problem: Although some disambiguation is present, the dual use is easy to confuse in quick reading.
- Required fix: Enforce notation disambiguation every time these symbols appear together in a section (e.g., write βCBR(θ) for cosmic birefringence angle; use γBI vs γPTA consistently in every occurrence, including figure insets).

P1A-m7 — Parity-violation σ juxtaposition lacks a “not directly comparable” disclaimer in Sec. IV D
- Location: Sec. IV D p. 14 (comparison of WMAP+Planck and ACT DR6 angles and 1.06σ difference).
- Problem: Elsewhere the manuscript correctly warns that σ’s from different pipelines are not directly comparable; here, the 1.06σ comparison is presented without that caveat.
- Required fix: Add a parenthetical here as done in the abstract and Sec. III A.

P1A-m8 — “Cubic action for ζ receives zero contribution from the Holst term” is stated but not demonstrated
- Location: Sec. X D p. 20.
- Problem: While the Bianchi argument shows the Holst contraction vanishes pointwise at T = 0, the statement about the cubic ζ action would benefit from a brief outline (e.g., show the 3+1 decomposition term that could contribute and why it cancels).
- Required fix: Add a one-paragraph sketch or a reference to a worked-out perturbative expansion where the ζ^3 term from Holst vanishes.

P1A-m9 — Figure 1 and Figure 3 captions need explicit “illustrative only” language (beyond what is in the body)
- Location: Fig. 1 p. 5; Fig. 3 p. 8.
- Problem: The captions could still be read as showing preferred numerical fits.
- Required fix: Add the sentence: “All numbers in this figure are illustrative and not derived in this paper; no fit is performed here.”

P1A-m10 — Cross-ref style and typography
- Location: multiple (e.g., “Domaga la,” “R R˜︁,” unit spacing like km/s/Mpc).
- Problem: Typographic artifacts remain.
- Required fix: Standardize names/diacritics and unit spacing (e.g., km s−1 Mpc−1) and ensure consistent typesetting of duals/tilde symbols.

NO FURTHER ARITHMETIC DISCREPANCIES FOUND BEYOND THOSE ALREADY REPORTED
- I recomputed all explicitly stated ratios and significances not covered in the initial report. The following checked out numerically: Eq. (7) [(α/M)MPl] ≈ 3×10−3; Eq. (9) ρcrit/ρPl at γ = 0.2375 and 0.274; Eq. (11) prefactor (Treh/MGUT)3/2 ≈ 0.032; Eq. (17) inversion to ρθ ≈ 1.6×10−10 eV^4 for mθ = H0; ΩGW ceiling in Eq. (20); β-difference significance 0.73σ in Fig. 7; γPTA offset 1.13σ. The only new arithmetic inconsistency I found was already captured in P1A-M1 of the initial report (ρΛ benchmark mismatch in Sec. IV A).