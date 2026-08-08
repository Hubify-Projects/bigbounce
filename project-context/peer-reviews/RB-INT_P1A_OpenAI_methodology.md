# P1A RB-INT — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/arxiv/paper1a_ech_nogo.pdf` md5=5223958f pages=32
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (4819 chars)
**Wall time**: 337.9s

---

Referee report for Physical Review D (methodology): “Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter” (32 pages)

Scope of review
- I audited equations, dimensional analysis, conversions, quoted significances, and arithmetic in figures/tables/captions.
- I recomputed all explicit ratios and key numerical examples that appear in the text.
- I assessed stand-alone reproducibility and the extent of dependence on “in preparation” companions.
- I classified each issue per the journal’s methodology standards.

Overall assessment
The central perturbation-transparency result (Holst dual vanishes identically for torsion-free Levi-Civita connections; torsion sources vanish for canonical scalars; hence no scalar/tensor perturbation imprint) is correct and well posed. The Route-1 NJL amplitude estimate is dimensionally and numerically sound. Several other channel-closure statements (Routes 2–3) are framed explicitly as ansatz-level amplitude budgets, which is acceptable if consistently labeled everywhere (including abstract and conclusions). However, the manuscript contains:
- non-archived computational artifacts (“will pin” a Zenodo), 
- heavy reliance on “in preparation” companions for figures, numbers, and pipeline validations that are not essential to the core theorem yet are presented prominently (tables, figures),
- several “barriers” asserted without derivations or references (non-theorem heuristic entries presented as constraints),
- one presentation-level inconsistency in the action (T^2 term placed inside the varied action but later said not to be varied),
- forecast-significance figures without minimal in-paper methodological detail,
- and editorial issues (length relative to core contribution, repeated caveats, internal jargon).

Below I list all issues with required fixes.

ESSENTIAL findings (must be fixed for PRD acceptance)

P1A-E1
- Section: Data and Code Availability (p. 25)
- Problem: “a Zenodo-archived release will pin all artifacts to the submitted-version snapshot” (future tense). No DOI or immutable tag/commit hash is provided; repository link only.
- Required fix: Provide a permanent archived DOI (Zenodo or equivalent) and the exact commit hash/tag corresponding to the submitted version for all code and frozen chains referenced. Ensure the in-text link and the Data Availability section cite the DOI and tag explicitly.

P1A-E2
- Section: Throughout; esp. Table II (p. 7), Sec. III B (p. 10–11), multiple figures/captions
- Problem: Load-bearing numerical values, pipeline validations, and MCMC diagnostics are repeatedly attributed to “companion papers (in preparation)”. Although the manuscript asserts these are not “load-bearing,” they are featured in Table II, several figures, and text in ways a reader cannot verify.
- Required fix: For a stand-alone PRD paper, either (a) replace all “in preparation” numeric content with citations to publicly accessible arXiv preprints (with identifiers) or (b) remove such values and any figure/table that depends on them, and confine mentions to qualitative statements. Table II must be removed or replaced with external, citable sources only. Any figure using companion-only numbers (e.g., γPTA = 2.567 ± 0.382; SPHEREx Fisher curves; NaMaster validation) must be removed or re-plotted with externally citable data/methods.

P1A-E3
- Section: Eq. (1), text around it (pp. 5–6)
- Problem: The displayed “+ 1/4 TabcTabc” is placed inside S_ECH as if part of the action to be varied, but the text then states it is a shorthand for the on-shell contact term after integrating out non-propagating torsion and “is not varied independently.” Presenting it inside the varied action is inconsistent and risks double counting.
- Required fix: Rewrite the action presentation unambiguously. Either (i) present the Einstein–Cartan–Holst+Dirac action without a T·T term, then explicitly perform (or cite) the torsion elimination and show the resulting effective four-fermion contact term (Hehl–Datta/Mercuri coefficient) in a separate effective action; or (ii) present the fully reduced effective action only. Do not include T·T inside the original action if it is not to be varied—this must be corrected for methodological clarity.

P1A-E4
- Section: Abstract (p. 1) and Conclusions (pp. 24–25)
- Problem: The paper states Routes R2–R3 are “amplitude-suppressed under explicitly-labeled scaling ansätze.” This caveat appears in the body but the abstract and conclusions must carry the same “ansatz-level upper bound” qualifier at every mention of those closures to avoid overstating their rigor.
- Required fix: Insert unambiguous qualifiers in both the abstract and conclusions that R2–R3 closures are “ansatz-level amplitude upper bounds,” not derivations, and that they are conditional on the stated dimensional/scaling ansätze.

P1A-E5
- Section: Figures 4 and 7 (pp. 30, 32), Sec. VII (p. 16), Sec. XIII (pp. 22–23)
- Problem: Forecast significances (SPHEREx 2.6–5σ realistic; LiteBIRD σ(β)≈0.03°) are plotted and discussed without in-paper specification of the primary estimator, data vector, covariance, and minimal Fisher setup. They are linked to companions “in preparation.”
- Required fix: Either remove forecast figures/curves from this paper or provide a concise, self-contained methods box: estimator definition, survey model (f_sky, n(z), bias model), redshift binning, templates used and overlap factor r, treatment of GR projection and photo-z, and how the quoted σ ranges are obtained. Keep the “different null procedures are not directly comparable” disclaimer adjacent to every juxtaposition.

MAJOR findings (significant revision required)

P1A-M1
- Section: Barriers catalog (Sec. IX, pp. 16–19; Table III p. 18)
- Problem: Several barriers (e.g., B2 Topological-Shift Duality; B3 Scalar-Tensor Universality; B5 Scale Separation; B6 Attractor-Sensitivity; B7 Parameter Immunity; B10 UV→IR Specificity; B11 Decoupling Universality; B13 Gravitational Democracy) are presented as constraints with minimal or no derivations and scant citation support; some are qualitative heuristics.
- Required fix: For each barrier, add either (a) a concrete derivation/proof or (b) explicit citations to prior peer-reviewed literature that establish the claim, along with a brief derivation sketch. Otherwise, demote them to “heuristic observations” with explicit labels and remove any quantitative or exclusionary language tied to them. Table III should reflect the revised status (theorem vs heuristic).

P1A-M2
- Section: Route 2 (Sec. IV B, pp. 12–13)
- Problem: The effective one-loop parity-violating operator and the β-ratio estimate are framed as an EFT upper bound; however, the dimensional reduction in Eq. (15) is terse and mixes units (MPl, M, H0) in a way that is easy to misread. The final 10^−60 estimate is plausible, but the algebraic chain is not fully transparent.
- Required fix: Provide a step-by-step dimensional derivation from the operator to a dimensionless ∆θ prediction, in a single consistent unit system (eV or GeV), making explicit where the factor MPl·(α/M) ≈ 10^−2 enters. State assumptions on ⟨∂μϑNY⟩ ∼ H0 and the anomaly chain. Keep the parity-even Lagrangian vs parity-violating background distinction explicit.

P1A-M3
- Section: Route 3 (Sec. IV C, p. 13–14)
- Problem: The running ansatz dγ/d lnμ = [(N_L−N_R)/(12π^2)] γ + O(γ^2) is used as an “upper bound” but does not cite a derivation or reconcile with the sign/|γ|-dependence found in Benedetti & Speziale (2011).
- Required fix: Either compute the bound from the published β-function (with clear approximations) or add a transparent argument showing why your chiral-count estimate is safely conservative compared to the full perturbative result. Clarify the link from ∆γ/γ to a parity-odd amplitude with proper mass-dimension counting.

P1A-M4
- Section: Step 3 (Sec. II A 2, Eq. 5–6, pp. 7–8) and Appendix B (pp. 25–26)
- Problem: The choice M ≡ M_area-gap ≈ MPl/√γ is used repeatedly in numerical estimates. This identification is asserted but not derived or referenced precisely (beyond “up to numerical constants”).
- Required fix: Provide a citation and a one-paragraph derivation for the area-gap mass scale used in your estimates (including the precise numerical prefactor if it matters), or restate all numeric results so they are independent of this identification (e.g., report in terms of [(α/M) MPl] without fixing M).

P1A-M5
- Section: Route 4 (Sec. IV D, pp. 14–15; Appendix C pp. 26–27)
- Problem: The ALP “overshoot” argument across mθ ∈ [10^−22, 10^−15] eV holds only if α/M is fixed. You call this “one-loop matching rigidity” but also acknowledge α/M can be floated to fit βobs. The text mixes these two regimes.
- Required fix: Tighten the logic. State clearly that (i) if α/M is fixed by the β measurement, then ρθ ∝ m^2 overshoots ρΛ outside a narrow mθ ∼ H0 window; (ii) if α/M is treated free, β and ρΛ can be co-fit but the model loses predictivity and runs into independent ALP–photon constraints—cite specific stellar-cooling/helioscope bounds and quantify the tension for the example α/M ∼ 10^−10 GeV^−1 at mθ ∼ 10^−22 eV.

P1A-M6
- Section: Forecast/observational content intertwined with theory (Sec. III; Figs. 4, 7)
- Problem: The paper is positioned as a theory/no-go manuscript, but it devotes space to forecast plots and in-prep anomaly results that are not necessary to support the central claims.
- Required fix: Streamline by removing or moving all forecast plots and PTA numbers to an appendix or to the companion. Keep only concise, citation-backed statements in the main text.

MINOR findings (address but can proceed)

P1A-m1
- Section: Eq. (9) and following (p. 8)
- Problem: You infer ρcrit ≈ 0.27 ρPl for γ = 0.274 by extrapolating the Ashtekar–Singh expression beyond the value used in their paper. You state this caveat, which is good, but please add a one-line numerical check: with γ = 0.274, γ^3 ≈ 0.0206, √3/(32π^2γ^3) ≈ 0.266, confirming the quoted 0.27.
- Required fix: Insert the explicit numerical check inline (or in a footnote) to document the arithmetic.

P1A-m2
- Section: NJL density conversion (Sec. IV A, p. 12)
- Problem: You convert 1 cm^−3 to eV^3 using ℏc = 1.973×10^−5 eV·cm and arrive at 7.66×10^−15 eV^3. This is correct (since 1 cm = 5.07×10^4 eV^−1). For absolute clarity, add the intermediate step 1 cm = 1/(1.973×10^−5 eV) = 5.07×10^4 eV^−1 so readers can reproduce the number easily.
- Required fix: Add the explicit intermediate conversion in a footnote.

P1A-m3
- Section: Appendix C (p. 26–27) and Sec. IV D (p. 14–15)
- Problem: Units toggled between GeV and eV. The worked example for ρθ with mθ = H0, α/M = 10^−21 GeV^−1, β = 0.342° is correct; consider adding both the GeV^4 and eV^4 paths to avoid confusion.
- Required fix: Add a short boxed calculation showing both unit systems side-by-side to demonstrate consistency.

P1A-m4
- Section: Fig. 3 caption (p. 29)
- Problem: The “2–3%” deviation is stated as dominated by H0 mismatch; then you compute (69.2−67.36)/67.36 ≈ 2.7%. Good. Please add the explicit numeric 2.7% in the caption where you explain the offset, to close the loop.
- Required fix: Include “2.7%” explicitly.

P1A-m5
- Section: Throughout
- Problem: Minor typographical/formatting issues: “Domaga la” spacing, occasional hyphenation irregularities (e.g., “improve￾ment” line breaks), lingering “PACS numbers.”
- Required fix: Clean typos and hyphenations; remove obsolete PACS line if not required by PRD.

NITs (cosmetic)

P1A-n1
- Section: Footnotes naming convention (“single-convention statement”) appear multiple times.
- Suggestion: Consolidate notational conventions into one early “Conventions” subsection for readability.

P1A-n2
- Section: Repeated caveats in several places about “not an operator-basis closure”
- Suggestion: State once in the Introduction and at the start of Sec. IV, then reference it, to reduce repetition and shrink length.

Arithmetic and dimensional cross-checks performed
- Eq. (9): ρcrit/ρPl = √3/(32 π^2 γ^3): yields 0.41 for γ=0.2375; 0.27 for γ=0.274 (checks).
- Route-1 NJL energy density: with nψ=10^2 cm^−3, ρNJL ≈ 4×10^−81 eV^4 ≈ 1.4×10^−70 ρΛ (checks).
- One-loop R2 suppression: ∆θone-loop/∆θobs ≈ (αem/4π) (H0/MPl) / [(MPl(α/M)) βobs] ≈ 10^−60 (checks with α/M fixed to 10^−21 GeV^−1, βobs ≈ 6×10^−3).
- Route-4 inversion: ρθ = 2 mθ^2 β^2 / (α/M)^2 with mθ = H0 ≈ 1.5×10^−33 eV, α/M = 10^−21 GeV^−1, β ≈ 0.342° ≈ 5.97×10^−3 rad → ρθ ≈ 1.6×10^−10 eV^4 ≈ 6 ρΛ (checks).
- WKB condition in App. C: (α/M) ϕ′ ≈ (10^−30 eV^−1)(MPl)(H0) ≈ 1.5×10^−35 eV vs k_CMB ≈ 6×10^−4 eV → hierarchy ~ 4×10^31 (checks).
- Ntot estimate: MPl^4/ρΛ ≈ 10^122; with [(α/M) MPl]≈10^−2, need Dinf ≈ 10^−121 → Ntot ≈ (ln 10)(121)/3 ≈ 93; the manuscript quotes 92–94 (consistent).

Length and focus
The manuscript is long relative to its core deliverables (perturbation-transparency theorem; R1 amplitude bound; R2–R3 ansatz-level upper bounds; R4 naturalness point). I recommend reducing to ≲ 22–24 pages by:
- moving all forecast figures and the PTA aside to an appendix or companion,
- removing Table II and any “in preparation” dependent material,
- compressing the barrier catalog to derived/cited entries only,
- consolidating repeated caveats and notational footnotes.

Abstract-last drift sweep
- Most abstract claims are mirrored with caveats in the body. However, ensure every mention of R2–R3 closures in the abstract and conclusions explicitly says “ansatz-level amplitude upper bounds.” Add a one-line statement in the abstract that Table II/forecast/companion numbers are illustrative only and not load-bearing (or drop their mention altogether).

Provenance surfaces
- Replace “will pin” with a DOI; ensure repository state matches the submitted version (hash).
- Remove “posted concurrently” language or replace with arXiv numbers.

Effect sizes and null procedures
- Where you juxtapose significances (WMAP+Planck, ACT DR6, SPHEREx, LiteBIRD), you generally note “not directly comparable” and explain the different nulls; keep those disclaimers adjacent to every such juxtaposition (Figs. 4, 7 captions already do; retain in text as well).

## Summary recommendation
MAJOR REVISIONS

Justification
The core technical results (perturbation-transparency theorem; NJL amplitude bound) appear correct, and the numerical examples I checked are internally consistent. However, the paper in its present form does not meet PRD methodology standards due to (i) missing permanent archival provenance for code and chains, (ii) over-reliance on “in preparation” companions for figures and numerical content that a reader cannot verify, (iii) an action-level presentation inconsistency for the T·T term, and (iv) several “barriers” asserted without derivations or citations. Tightening the abstract/conclusions language for R2–R3, removing or making self-contained all forecast/companion-dependent content, and providing a tagged release/DOI will bring the work to PRD standards. A length reduction is also recommended.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes pass)

P1A-E6
- Section: II C (p. 8) and places that use ρΛ = Λeff MPl^2 (e.g., Fig. 3 caption p. 29)
- Problem: With the unreduced Planck mass convention MPl ≡ G−1/2 adopted in the text, the correct relation is ρΛ = Λeff M̄Pl^2 = Λeff MPl^2/(8π). The manuscript repeatedly uses ρΛ = Λeff MPl^2, which is off by a factor 8π.
- Required fix: Either switch to the reduced Planck mass throughout (declare MPl ≡ M̄Pl = 1/√(8πG)) or keep the unreduced MPl and insert the explicit 1/(8π) where needed. Update all dependent equations, sentences, and figure captions (notably Fig. 3) for consistency.

P1A-M7
- Section: Notation across Sec. X C (Eq. 21) and context
- Problem: The same symbol H is used for the conformal Hubble rate (H ≡ a′/a) and for the cosmic-time Hubble rate in the “equivalent” form h¨ij + 3H h˙ij + (k^2/a^2)hij = 0. This is a notational collision.
- Required fix: Use ℋ ≡ a′/a for the conformal Hubble rate and reserve H ≡ ȧ/a for cosmic time. Update Eq. (21) text and nearby sentences accordingly.

P1A-M8
- Section: Appendix C (p. 27), last paragraph
- Problem: Cross-reference “the companion’s §VI8” is malformed and nonstandard; it is unclear what subsection “§VI8” denotes.
- Required fix: Replace with a standard, unambiguous reference (e.g., “Sec. VI” of the companion, with arXiv identifier) or remove the reference.

P1A-M9
- Section: III A (p. 10), XIII (pp. 22–23), and other narrative juxtapositions
- Problem: Several juxtapositions of σ values from different null procedures appear without the explicit “not directly comparable” caveat adjacent to the sentences (e.g., the paragraph in Sec. III A listing βobs from WMAP+Planck and ACT; some sentences in Sec. XIII). The figures/captions include caveats, but the text does not always repeat them.
- Required fix: Add “not directly comparable (different null procedures/masks/estimators)” immediately wherever disparate σ’s are juxtaposed in the body text (e.g., Sec. III A, Sec. XIII), not just in captions.

P1A-M10
- Section: Fig. 3 caption (p. 29) and surrounding discussion
- Problem: The H0 baseline used for the orange curve (69.2 km/s/Mpc) differs from the value adopted elsewhere in the manuscript (67.68 ± 1.06, Table V). Although the caption notes this is illustrative, the mismatch risks confusion, and—combined with P1A-E6—obscures the normalization.
- Required fix: Either (a) harmonize H0 with the rest of the paper (use the same value/uncertainty) or (b) move this figure to an appendix with a short methods box specifying all inputs (H0, Ωm, Ωr, Λ normalization with reduced vs unreduced MPl). Also correct the Λ-to-ρΛ normalization per P1A-E6.

P1A-m6
- Section: Appendix C (p. 27), WKB hierarchy sentence
- Problem: The text states “satisfied by ∼30 orders of magnitude,” while the worked numbers yield k/(α/M ϕ′) ≈ 6×10−4 eV / 1.5×10−35 eV ≈ 4×10^31 (i.e., > 31 orders). The result is correct but imprecisely rounded.
- Suggested fix: State “> 30 orders of magnitude” or give the explicit ratio (~4×10^31) for clarity.

P1A-m7
- Section: II A 2 (p. 7), Step 4 and Fig. 5 (top panel)
- Problem: The paper uses F for both gravitational curvature (F IJ in Eq. (6)) and electromagnetism (Fμν in Sec. IV D), despite noting a calligraphic distinction earlier. In Eq. (6) the calligraphic F is not used, which can confuse the reader.
- Suggested fix: Use a distinct symbol (e.g., calligraphic ℱIJ for gravitational curvature) consistently in Eq. (5)–(6) and retain Fμν for electromagnetism, as promised in the text.

P1A-m8
- Section: II A 2 (p. 7), Step 2
- Problem: G and GN are used interchangeably, but both appear in nearby equations and captions. Although the text states GN is the same as G, the mixed notation is easy to misread.
- Suggested fix: Use a single symbol (G) throughout unless a genuine distinction is required; otherwise, define once and stick to it.

P1A-m9
- Section: Fig. 3 caption (p. 29)
- Problem: The conversion from the vorticity bound to a ρΛ fraction is correct but terse. As written: fraction ≈ (ω/H)^2/(3ΩΛ) ≲ 2.5×10−21/2.1 ≈ 1.2×10−21. The caption does show the intermediate “dividing by 3ΩΛ ≈ 2.1,” but not the full formula.
- Suggested fix: Add the explicit ratio “ρω/ρΛ ≈ cω (ω/H)^2/(3ΩΛ)” for full transparency.

Explanation
The initial review focused on archival provenance, action-level clarity, ansatz labeling, and forecast self-containment. On a fresh arithmetic/consistency pass, the most substantive new issue is the systematic use of ρΛ = Λ MPl^2 while simultaneously defining MPl as the unreduced Planck mass; this normalization is off by 8π and should be corrected (P1A-E6). Additional notational and cross-reference issues (P1A-M7–M10) and minor clarity fixes (P1A-m6–m9) are identified to improve methodological rigor and reader reproducibility.