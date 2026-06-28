# P1A INT-X-P1A — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/arxiv/paper1a_ech_nogo.pdf` md5=6fc7ac8c pages=31
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (9529 chars)
**Wall time**: 244.1s

---

Referee report for: “Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter”

Scope of review
- Journal: Physical Review D (methods rigor)
- Focus: statistical-method validity, derivation chains, dimensional analysis, internal arithmetic consistency, error propagation, figure/table consistency, and whether abstract/conclusions faithfully reflect results shown in the body.
- I read the entire 31-page manuscript, including equations, tables, figures, captions, footnotes, appendices, and references.

Overall assessment
The manuscript proposes a “channel-level” no-go analysis for four minimal ECH routes to dark energy and presents a “perturbation transparency” result for canonical scalar matter. The logic flow is largely qualitative with several quantitative amplitude-budget checks and many explicit caveats. The author has been unusually careful to mark phenomenological ansätze, dimensional caveats, and the non-load-bearing nature of “in preparation” companions. That said, for PRD standards I found a set of essential and major issues that must be corrected for clarity, reproducibility, and methodological rigor.

Below are all findings, categorized as ESSENTIAL, MAJOR, MINOR, and NIT, each with ID, page/section, problem, and required fix.

Findings

ESSENTIAL

P1A-E1 — Significance juxtaposition without local caveats
- Location: p. 13, Sec. IV D; also p. 21, Sec. XIII; p. 23, Sec. XV Conclusions, last paragraph; Fig. 7 caption.
- Problem: The paper juxtaposes σ-levels derived under different null procedures (WMAP+Planck β = 0.342° ± 0.094° at “∼3.6σ from β = 0”, ACT DR6 β = 0.215° ± 0.074° “at ∼2.9σ”) and computes a pairwise “∼1.06σ” difference (p. 13) without an explicit local caveat that these are not from a joint analysis with a known covariance and that the null procedures differ. Although an earlier abstract caveat notes “not directly comparable in a single tension table,” the journal requires that every juxtaposition be annotated locally to prevent misinterpretation.
- Required fix: At each place where two different σ values are presented and/or combined (Sec. IV D; Sec. XIII; Sec. XV; Fig. 7 caption), insert an explicit note: “The quoted σ values are derived under different null procedures/estimators and are not directly comparable; the ‘difference in σ’ is a heuristic using quoted uncertainties, not a joint-analysis result.” Remove or restate the “1.06σ” difference accordingly as a heuristic, non-joint significance.

P1A-E2 — Reproducibility: missing frozen DOI/hash for code/data bundle
- Location: p. 24, Data and Code Availability.
- Problem: The text promises a future Zenodo-archived release to pin artifacts but does not provide a DOI or a frozen commit hash for the present submission. PRD requires reproducibility surfaces to be stable at review/acceptance.
- Required fix: Provide a working public DOI for a frozen release (Zenodo or equivalent) that exactly matches the submitted manuscript’s artifacts, or provide a permanent commit hash/tag and archive link. Explicitly list file paths for the “frozen MCMC chains,” the exact version of any scripts used to produce figures/tables, and the SHA/DOI in the Data Availability text.

P1A-E3 — Forecast figures rely on non-public, “in preparation” results without minimal in-paper derivation
- Location: Fig. 4 (p. 29) and Fig. 7 (p. 31); footnote 6; throughout text referencing “in preparation [2,6,46]”.
- Problem: Detection-significance curves (2.6–5σ for SPHEREx; LiteBIRD σ(β)=0.03° lines) are shown and discussed, but the paper relies on “in preparation” works for the derivation. The author states these are non-load-bearing, but the figures nevertheless communicate quantitative conclusions to readers. PRD requires that any figure with numerical content be reproducible from the paper or from publicly citable sources.
- Required fix: Either (a) remove Fig. 4 and Fig. 7 and all numeric forecast claims that depend on companions, or (b) include a minimal, self-contained derivation in this paper sufficient to reproduce the plotted points (e.g., explicit σ(fNL) mapping from Heinrich et al. 2024 baselines to final 2.6–5σ range with the applied degradations; explicit assumptions for LiteBIRD β forecast curves). In either case, all remaining forecasts must be explicitly labeled “illustrative, not load-bearing; based on published baseline X with assumptions Y,Z.”

P1A-E4 — Misleading wording for number density used in NJL amplitude bound
- Location: p. 11, Sec. IV A.
- Problem: The text calls nψ ∼ O(10^2) cm−3 “post-recombination baryon densities.” The cosmic-mean baryon density is ∼2×10−7 cm−3 today; 10^2 cm−3 corresponds to dense ISM clouds. The use of a high number is conservative for an upper bound, but the phrasing is inaccurate.
- Required fix: Replace “post-recombination baryon densities nψ ∼ O(10^2) cm−3” with “dense ISM-like number densities (nψ ∼ 10^2 cm−3), used here as a conservative high-density upper bound; the cosmic-mean baryon density is ∼2×10−7 cm−3 and makes the bound even stronger.”

P1A-E5 — R3 (running of Immirzi parameter) uses an asserted ∆γ/γ ∼ 10−2 without a derivation or precise citation
- Location: p. 13, Sec. IV C.
- Problem: The estimate “∆γ/γ ∼ 10−2 over the running from the GUT scale to the IR” is stated without derivation in-text and not directly traceable to the cited literature (Date–Kaul–Sengupta; Benedetti–Speziale). For PRD, a quantitative factor central to an amplitude bound must be derived or tied to a precise published equation.
- Required fix: Provide a transparent derivation (one or two lines) or a precise literature equation that yields ∆γ/γ ∼ 10−2 over the stated running range given SM chiral content. If this is a conservative EFT upper bound, say so explicitly and show the numbers (e.g., specify NL_F − NR_F, the log(μ) lever arm used, and how this maps to 10−2). Otherwise, weaken the statement to a symbolic bound and remove the numeric 10−2.

P1A-E6 — Pairwise comparison of WMAP+Planck and ACT β central values without independence caveat
- Location: p. 13, Sec. IV D.
- Problem: The calculation “consistent within ∼1.1σ” treats the two estimators as independent by combining errors in quadrature. This independence is not established and the two pipelines may share systematics/sky. A local caveat is required.
- Required fix: Add “This 1.1σ difference is a heuristic assuming independent Gaussian errors; a proper joint-pipeline analysis is required for a rigorous comparison.”

MAJOR

P1A-M1 — Formal definition of the phenomenological operator in Eqs. (5)–(6)
- Location: p. 6–7, Sec. II A 2, Steps 3–4; Appendix B.
- Problem: The operator Seff = (α/M) ∫ eI ∧ eJ ∧ FIJ[K,R°] (Eq. 5) is introduced as an ansatz; however, the notation FIJ[K,R°] is not unpacked precisely. Equation (6) provides a “leading contribution” but without a concrete off-shell local completion. For a PRD methods paper, the object entering subsequent amplitude budgets must be explicitly defined or clearly constrained as a schematic placeholder.
- Required fix: State explicitly what tensor contraction Eq. (6) represents (write the full component expression, index structure, and how K and R° enter), and whether any omitted terms change power counting. Alternatively, move Eqs. (5)–(6) to Appendix B as a purely schematic ansatz and ensure all amplitude budgets that use it are clearly labeled “conditional on the +1-dimension ansatz” at point of first use (R2–R4, Secs. IV B–D).

P1A-M2 — Forecast range “2.6–5σ realistic” for SPHEREx needs a concrete mapping from σ(fNL)
- Location: p. 15 (Table I, footnote b); p. 21 Sec. XIII; Fig. 7 caption.
- Problem: The range 2.6–5σ appears repeatedly. The text references Heinrich et al. (σlocal≈0.7 ideal) and then a GR/photo-z degradation to σ≈1.0. From these numbers, the nominal |fNL|/σ range is 4.4–6.25σ, not 2.6–5σ; the “2.6σ” lower endpoint is not derivable from the displayed inputs and is left to an (unavailable) companion.
- Required fix: Either (a) remove the “2.6–5σ” range and state only “using σ≈1.0 yields ≈4.4σ,” or (b) show explicitly how additional degradations move σ from 1.0 to ≈1.7 (to reach 2.6σ) with numbers (e.g., template mismatch r, GR projection factor, photo-z prior), and provide a reproducible line-item multiplication.

P1A-M3 — Barrier A (geff ∼ H0/MPl) presented as a scaling without sufficient context
- Location: p. 16, Sec. IX A (Barrier 1).
- Problem: The statement geff ∼ 1/(MPl√|t3|) ∼ H0/MPl is labeled as a scaling ansatz but lacks a brief derivation or standard reference for the PGT mass/coupling relation. As written it risks appearing ad hoc.
- Required fix: Supply a one-line derivation or cite a standard PGT review that explicitly shows how the torsion mass parameter t3 controls mode mass and the coupling normalization to arrive at geff ∼ H0/MPl for ultralight torsion. If not available, rephrase as a clearly labeled heuristic and do not use it beyond qualitative discussion.

P1A-M4 — Reheating “washout” argument: add a minimal numerical check
- Location: p. 8–9, Sec. II C 1 (“Reheating thermal-reset barrier”).
- Problem: The text’s inequality Γwash > H at Treh is asserted for SM channels. This is plausible, but a short numerical check would greatly strengthen the claim (and avoid the appearance of hand-waving).
- Required fix: Add a two-line numerical estimate for at least the top-Yukawa channel: Γy ≈ y^2 T/8π (or similar standard form), H ≈ 1.66√g* T^2/MPl at T ∼ 10^15 GeV, with y_t ≈ 1, g* ∼ 100, showing Γy/H ≫ 1. Keep it compact; the intention is to document the inequality with numbers.

P1A-M5 — Dependency on non-public “in preparation” numerical values (γPTA; MCMC posteriors)
- Location: p. 19–20, Sec. X G (γPTA); p. 4, 10–11, multiple places referencing Paper I(b) MCMC values; Table IV.
- Problem: Although the author repeatedly states these are not load-bearing, concrete numerical values from non-public analyses are quoted (e.g., γPTA = 2.567 ± 0.382; H0 = 67.68 ± 1.06). This is acceptable only if framed as illustrative context, not as results of this paper.
- Required fix: In every place such numbers appear, prefix with “illustrative, from non-peer-reviewed companion; not used in any closure argument.” For H0 etc., prefer quoting Planck 2018 or other published values directly when needed. Alternatively, move all such non-public numbers to an Appendix “context only” paragraph.

MINOR

P1A-m1 — Clarify dimensionality of ϑNY and provide a concrete definition or reference
- Location: p. 12, Eq. (14).
- Problem: The text states “ϑNY(x) is the Nieh–Yan pseudoscalar (mass dimension +1)” without defining it. This is acceptable if a definition or precise citation is provided.
- Required fix: Add a reference where ϑNY is defined and its mass dimension is established, or include a short definition in a footnote.

P1A-m2 — Holst dual vanishing by Bianchi identity: add a precise reference
- Location: p. 18–19, Sec. X B,D; footnote 7.
- Problem: The argument that εμνρσ Rμνρσ(Γ°) = 0 by the first Bianchi identity is correct but should be referenced for readers.
- Required fix: Add a textbook reference (e.g., Wald or a standard differential-geometric GR text) or a short derivation sketch.

P1A-m3 — Minor unit conversions to show steps explicitly
- Location: p. 11, Sec. IV A (nψ conversion cm−3 → eV^3); p. 13–14, Sec. IV D (α/M in GeV−1 used to get ρθ in eV^4).
- Problem: The conversions are correct (I recomputed them) but terse.
- Required fix: Add a brief parenthetical showing the key constants (1 cm = 1/(1.973×10−5 eV−1)) and “1 GeV−1 = 10−9 eV−1” to aid reproducibility.

P1A-m4 — Forecast language
- Location: p. 21–22, Sec. XIII; p. 23, Conclusions.
- Problem: Some future-looking sentences (“will detect at ∼9σ”) could be softened to “targets sensitivity to” to avoid overpromising.
- Required fix: Replace “will detect at ∼9σ” with “targets sensitivity corresponding to ∼9σ for β ≈ 0.27° under nominal assumptions.”

NIT

P1A-n1 — PACS numbers deprecated
- Location: p. 2 (PACS numbers line).
- Fix: Remove PACS numbers per PRD style.

P1A-n2 — Typographic artifacts
- Location: various (e.g., “ans¨atze”, “Poincar´e”).
- Fix: Ensure proper LaTeX accent encoding (“ansätze”, “Poincaré”).

P1A-n3 — Length
- Location: entire manuscript (31 pages).
- Comment: The paper is long relative to the core contribution (channel-level closure plus perturbation-transparency argument). Consider trimming 4–6 pages by moving purely illustrative content (e.g., Fig. 4/7 if kept), repetition of caveats, and extended contextual asides to appendices. Suggested target: ≤25–27 pages.

Arithmetic and dimensional spot-checks (all consistent unless otherwise noted)
- Eq. (13): L_NJL = −(3/16) κ (J5)^2 with κ=8πG ⇒ coefficient 3πG/2; consistent with Eq. (4) in the Holst limit γ→∞.
- nψ conversion: 100 cm−3 → 7.66×10−13 eV^3; ρNJL ∼ n^2/MPl^2 ≈ 4×10−81 eV^4; ratio to ρΛ ≈ 1.4×10−70 (recomputed).
- Eq. (7) one-loop: (α/M) MPl ≈ 3×10−3 with ln(Λ/μ)≈74, γ=0.274, g^2≈0.092; consistent.
- R2 β suppression ratio, Eq. (15): ∼10−60 (recomputed).
- R4 ρθ with mθ=H0, α/M=10−21 GeV−1, β=0.342°: ρθ≈1.6×10−10 eV^4 ≈ 6 ρΛ (recomputed).
- Overshoot factors at mθ=10−22 and 10−15 eV: ∼22 and ∼36 orders of magnitude, respectively (recomputed).
- LQC ρcrit formula and 0.27–0.41 ρPl range: consistent with stated γ scheme dependence.
- Eq. (11) dilution Dinf ∝ e−3Ntot (Treh/MGUT)3/2: dimensionally consistent as a phenomenological scaling; the Ntot≈92 target matches Ξ≈10−123 with the given prefactors.
- Appendix C helicity dispersion and β = (α/2M) ∆ϕ: derivation correct; WKB condition k ≫ (α/M) ϕ′ satisfied by ≳10^31 (recomputed).

Abstract-last drift audit (pattern-045)
- The abstract’s main claims (channel-level closures R1–R4 under specified assumptions; perturbation transparency for canonical scalar matter; limitations/caveats; forecast statements not directly comparable) largely match the body. However, ensure that every place σ-levels are listed side-by-side in the abstract continues to include the “not directly comparable” qualifier (it appears once; acceptable but please keep it when revising other sections per P1A-E1/E6).

Provenance surfaces (pattern-046/047)
- The GitHub link exists; however, for PRD acceptance a stable DOI or permanent tag is required (P1A-E2). The text currently uses future tense (“will pin”); replace with actual DOI and commit hash.

Uncomputed quantitative claims (pattern-048)
- Several “negligible,” “bounded above,” “washed out,” etc. statements have back-of-the-envelope numbers or are clearly labeled heuristic/conditional. The top-Yukawa/Hubble check still needs a minimal numerical anchor (P1A-M4).

Standalone-reader test
- The no-go logic and perturbation-transparency argument are self-contained, provided the above clarifications are made. Forecasts and some contextual numbers rely on “in preparation”; acceptable if clearly delabeled as non-load-bearing and/or removed.

Effect-size notes
- fNL effect size is clear (−35/8). β reported in degrees. Rotational contribution cω ω^2 negligible quantified in Fig. 3 caption; good.

## Summary recommendation
MAJOR REVISIONS

The central theoretical claims (channel-level closures under explicit ansätze and the perturbation-transparency result) are well framed and, with the author’s many caveats, are methodologically sound. However, for PRD standards the manuscript requires (i) stronger local caveats wherever σ values from different nulls are juxtaposed; (ii) stable, citable reproducibility surfaces; (iii) removal or in-paper derivation of forecast figures that presently depend on “in preparation” companions; (iv) precise support for a few quantitative steps (∆γ/γ estimate; washout inequality); and (v) correction of the misleading density wording. Once these are addressed and the reproducibility DOI is provided, the paper would meet PRD’s methodological rigor bar. I also recommend modest length reduction by moving non-essential forecast content to an appendix or companion.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eye audit)

I re-checked the manuscript against the requested classes A–J and found several NEW issues not covered in my initial report. I list only new items below, using the same severity taxonomy and ID scheme. Where arithmetic is involved I show the recomputation or the logic leading to the concern.

ESSENTIAL
— None new beyond those already listed. The most consequential new item below (Barrier-12 ceiling) is marked MAJOR.

MAJOR

P1A-M6 — Barrier 12 ceiling formula lacks physical derivation; numeric 0.07–0.17 is not justified
- Location: p. 18, Sec. IX L (Barrier 12), Eq. (20).
- Problem: The proposed ceiling ΩGW|bounce ≲ (ρcrit/ρPl)^2 ≃ 0.07–0.17 has no clear physical basis. ΩGW is a fraction of the total energy density at the epoch of interest; at the bounce the total is ρtot = ρcrit by construction, which yields the trivial ceiling ΩGW ≤ 1. Introducing ρPl in the denominator and squaring (ρcrit/ρPl)^2 is not standard and does not follow from energy-fraction algebra. While the text labels this an “order-of-magnitude ceiling ansatz,” assigning a specific numeric band (0.07–0.17) invites readers to over-interpret an unsupported number. As written, the quantity is dimensionless but physically opaque; it is also not a bound on today’s ΩGW(fnHz) and could be misconstrued as such.
- Required fix: Either (a) remove the numeric 0.07–0.17 claim and keep only a qualitative statement (“the bounce cannot exceed ΩGW,bounce ≤ 1; a realistic spectrum redshifts down to ΩGW,0 ≪ 1”), or (b) provide a self-contained derivation tying (ρcrit/ρPl)^2 to a GW production efficiency bound (e.g., via a stress-source amplitude and backreaction inequality). In all cases, clearly separate any bounce-epoch bound from today’s PTA-band ΩGW and remove the specific 0.07–0.17 number unless it is derived.

P1A-M7 — Planck-mass convention inconsistency in energy-density ratios
- Location: p. 8, Eq. (10) and surrounding text; p. 28, Fig. 3 caption (paragraph with “dividing by 3ΩΛ ≈ 2.1”).
- Problem: The paper declares the unreduced Planck mass MPl throughout, but several standard cosmological relations (ρc = 3M̄Pl^2 H^2, ρΛ = M̄Pl^2 Λ) use the reduced mass M̄Pl. The Fig. 3 caption’s ratio ρrot/ρΛ ∼ (ω/H)^2/(3ΩΛ) implicitly uses ρc = 3M̄Pl^2H^2. Mixing MPl in Eq. (10) with reduced-MPl formulas in Fig. 3 introduces an 8π factor ambiguity. Although the authors claim such factors are “below order-of-magnitude resolution,” the specific “divide by 3ΩΛ ≈ 2.1” step is a concrete numerical operation that is sensitive to this choice.
- Required fix: State explicitly which Planck mass is used in each energy-density identity when forming ratios, and ensure internal consistency. The cleanest fix is to rewrite the Fig. 3 ratio with M̄Pl (or add the 8π factor explicitly if insisting on unreduced MPl) and say so in the caption. This is a consistency fix; it will not change the “negligible” conclusion.

MINOR

P1A-m5 — “Parity-odd operator” labeling in R2 conflicts with intrinsic parity; tighten wording
- Location: p. 12, Sec. IV B header and first paragraph around Eq. (14).
- Problem: Eq. (14) is intrinsically parity-even (pseudovector ∂μϑNY times pseudovector J5μ). The text notes this in a footnote, but the section label repeatedly calls it “parity-odd.” This creates avoidable confusion.
- Required fix: Rename the section header and first-sentence descriptor to “parity-violating phenomenology via a time-dependent Nieh–Yan background,” and add “the operator itself is P-even; P-violation arises from ⟨∂μϑNY⟩ ≠ 0” inline (not only in a footnote).

P1A-m6 — Axial anomaly normalization used downstream needs citation or correction
- Location: p. 12, Sec. IV B, footnote after Eq. (14) and subsequent use of “∂μJ5μ ⊃ (αem/4π) FF̃”.
- Problem: The standard Adler–Bell–Jackiw anomaly for a single Dirac fermion is ∂μJ5μ = (e^2/2π^2) E·B = (αem/π) FF̃ (up to conventions). The manuscript uses αem/(4π), which differs by O(1) factors depending on normalization. Since this coefficient is used only for amplitude-budget scaling, a precise numerical value may not be load-bearing, but the normalization should be stated and referenced.
- Required fix: Cite a specific equation (with conventions) that yields the αem/(4π) normalization used here, or state explicitly that this is an order-of-magnitude placeholder and does not affect any closure result.

P1A-m7 — Notation collision: gravitational “F” versus electromagnetic Fμν
- Location: p. 6–7, Eqs. (5)–(6).
- Problem: The manuscript says “calligraphic F” is reserved for gravitational curvature, while Fμν denotes electromagnetism, but Eq. (6) then drops the calligraphic font and uses FIJρσ for the gravitational curvature. This invites confusion once the EM sector appears.
- Required fix: Use RIJρσ or a consistently calligraphic symbol in components for the gravitational curvature everywhere, reserving Fμν for electromagnetism.

P1A-m8 — Galaxy-spin “factor of ∼6–12” tension claim lacks the underlying amplitudes
- Location: p. 9–10, Sec. III B.
- Problem: The statement “in amplitude tension … by a factor of ∼6–12” is not backed by the explicit measured dipole amplitude and its uncertainty from the authors’ classifier. Without the numbers, readers cannot verify the factor-of-6–12.
- Required fix: Add the measured monopole/dipole amplitude(s) with errors (or a pointer to a table/figure in the companion, if unavoidable), and show how the 6–12 factor is computed. If the detailed numbers are intentionally in the companion, explicitly label this as an “illustrative comparison; see [23] for amplitudes.”

P1A-m9 — Units for β in Eq. (12) and surrounding text
- Location: p. 9–10, Eq. (12) and paragraph below.
- Problem: Eq. (12) uses the small-angle approximation CℓEB ≈ 2β(CEEℓ − CBBℓ). To avoid any ambiguity in reproduction, β should be stated to be in radians in this formula (degrees are used elsewhere).
- Required fix: Add “β in radians here” in the sentence below Eq. (12).

P1A-m10 — Appendix citation to “companion’s §VI8” is confusing in a stand-alone paper
- Location: p. 26, Appendix C, last sentence of the paragraph below Eq. (C4).
- Problem: The text references a section “§VI8” of a companion for normalization. This looks like a broken section reference in the present paper.
- Required fix: Remove the companion section-number citation here; if a pointer is needed, cite the companion at a high level (“see companion Paper I(b) for pipeline conventions”).

P1A-m11 — Clarify mapping between Λeff and ρΛ under MPl versus M̄Pl
- Location: p. 8, Eq. (10) and discussion.
- Problem: The manuscript states ρΛ = Λeff MPl^2 using unreduced MPl, whereas the standard GR convention is ρΛ = Λeff M̄Pl^2. Readers can follow the logic with either convention, but the divergence from standard practice should be made explicit at the point of use to preempt confusion (especially where “3ΩΛ” appears later).
- Required fix: Add a one-sentence note under Eq. (10) clarifying the convention and its relation to the reduced-MPl form (e.g., “In standard reduced-MPl units this reads ρΛ = Λeff M̄Pl^2; our subsequent ratios use the reduced-MPl critical-density identity.”)

NIT

P1A-n4 — Keep author-chosen “calligraphic F” promise
- Location: p. 6–7.
- Fix: As per P1A-m7, ensure component notation for gravitational curvature does not revert to plain “F” anywhere.

P1A-n5 — Minor hyphenation/diacritics
- Location: misc.
- Fix: “Domaga la” → “Domagała”, “ans¨atze” → “ansätze”, “Poincar´e” → “Poincaré” (as already noted in P1A-n2; include this specific surname as well).

Notes on the A–J checklist coverage for these new items
- A (Arithmetic): I rechecked all quoted ratios/σ/overshoots; no new arithmetic inconsistencies beyond those already flagged.
- B (Figure-caption vs body-claim): Fig. 3’s caption math depends on the MPl convention (P1A-M7). Other figures’ captions match the text but depend on companions (already covered in P1A-E3).
- C (Dimensional consistency): No new mismatches found beyond the well-flagged Eq. (5)–(6) ansatz status (P1A-M1 in initial review).
- D (Cross-references): The Appendix C pointer to a companion section number (P1A-m10) is new.
- E (Null-procedure comparability): No additional unqualified juxtapositions beyond those already flagged (P1A-E1/E6).
- F (Abstract faithfulness): No new drift detected beyond earlier caveats already noted in the first report.
- G (Novelty claims): No new unsupported “first/largest” claims detected.
- H (Unquantified hedges): The galaxy-spin “factor of 6–12” (P1A-m8) is now quantified as needing explicit backing.
- I (Appendix vs main-text): The Planck-mass convention and notation collisions are the only new inconsistencies; equations otherwise match.
- J (Stale numbers): None detected beyond the Planck-mass convention issue.

Summary of why these are new
- The Barrier-12 ceiling and Planck-mass convention inconsistencies emerged only after re-deriving the figure-caption ratio and re-reading the energy-density identities with attention to MPl versus M̄Pl.
- The parity labeling, anomaly normalization, and notation collision surfaced in a second pass focusing on self-consistency of terminology and symbols.
- The spin-dipole “factor of 6–12” lacked explicit amplitudes; this gap was not obvious on first read because of the repeated pointer to a companion.

With these additions, the combined set of findings covers all the typical PRD rigor pitfalls: arithmetic, units, operator definitions, reproducibility, and internal consistency.