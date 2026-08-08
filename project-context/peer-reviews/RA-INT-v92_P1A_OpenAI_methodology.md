# P1A RA-INT-v92 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/arxiv/paper1a_ech_nogo.pdf` md5=7488bd1c pages=36
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6615 chars)
**Wall time**: 299.2s

---

Referee report on “Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter”

Scope of this review
I audited the paper for methodological rigor: derivation chains, dimensional consistency, estimator definitions, statistical claims, arithmetic and unit checks, and figure/table consistency. I recomputed all quoted ratios and significances that can be evaluated from the text, and I assessed whether every abstract/conclusion scalar is traceable in the body. I also applied PRD’s standards for referencing, reproducibility, and independence from in-preparation companion works.

Overall assessment
The manuscript makes two main contributions: (i) a perturbation-transparency statement for the Holst sector in torsionless scalar cosmology, and (ii) a “channel-level” amplitude/no-go survey of four routes by which minimal ECH might feed late-time dark energy or CMB parity-violation, accompanied by a catalog of “barriers”.

The scalar-sector transparency argument is concise and correct within its stated scope: in the torsionless branch the Holst dual ϵR vanishes by the algebraic Bianchi identity, so γBI drops out of scalar/tensor perturbation equations. However, the paper’s other claims rely heavily on ansatz-level amplitude budgets, and much of the contextual numerics and several figure captions depend on “in-preparation” companion works that are not available to the referee or reader. As a PRD methodology submission, the paper must be fully self-contained and avoid load-bearing dependence on unpublished companions. In addition, there are a few places where the presentation risks confusion (action normalization with an on-shell T^2 term; reuse of the symbol β; mixing of heterogeneous significance conventions in figures; simultaneous use of “M” for both the area-gap scale and the denominator of an ALP-photon coupling), and several claims of “closure” for routes R2–R3 are supported only by explicitly phenomenological scaling ansätze.

Below I itemize required revisions.

Findings and required actions

ESSENTIAL

P1A-E1 (Global; multiple pages: 2, 4–5, 7, 10–11, 16–18, 20–24, 30–34)
Problem: The manuscript cites and uses non-public “in preparation” companions for numerical values, forecasts, pipeline validation, and even axis-annotated figures (e.g., Table II “Companion-imported inputs,” Fig. 1 PTA annotation γPTA = 2.567 ± 0.382 from a “real-KDE” reanalysis, Fig. 4/7 forecast significances, Sec. III.B MCMC results, Sec. X.G PTA summary).
Required fix: For PRD, any value, figure annotation, or pipeline claim that appears in the main text must be reproducible from publicly archived sources. Either (a) post the companions on arXiv at submission and cite them, or (b) remove all non-public numbers/annotations from the main text and figures, and recast any remaining mentions as qualitative background with citations to peer-reviewed or arXiv-posted literature. In particular: delete the PTA γPTA label from Fig. 1, remove Table II from the main text or replace every entry with a public reference, and strip Fig. 4/7 of any forecast curves that rely on unpublished methods or inputs. If you wish to keep forecasts, provide a minimal, self-contained description of the estimator, inputs, and a reproducible notebook/script in an archived release (see E3).

P1A-E2 (Sec. II.A.1, Eq. (1), p. 5–6)
Problem: The gravitational action is written with a +¼ TabcTabc term inside the Einstein–Cartan–Holst bracket, scaled by (16πG)−1, but then declared to be “a shorthand” for the on-shell four-fermion contact obtained after integrating out torsion and “not varied.” This presentation risks double counting and obscures normalization. As written, the integrand’s mass dimensions and the variational content are ambiguous.
Required fix: Present the standard Einstein–Cartan–Holst+Dirac action without an explicit T·T term. Then integrate out torsion in an appendix (or within Sec. IV.A) to derive the Hehl–Datta four-fermion term with a clear, conventional normalization. If you insist on keeping a T·T term in the action display, explicitly mark it as an auxiliary field introduced for convenience, describe precisely which pieces are varied, and move the (16πG)−1 factor to the conventional places so the mass dimensions are transparent. Provide a compact derivation that connects your conventions to the standard −3κ/16 (J5)^2 contact.

P1A-E3 (Sec. II.A.2 and Appendix B; Eqs. (6), (B1)–(B2), pp. 8–9, 27)
Problem: The central parity-odd operator used for the dark-energy scaling, Eq. (6), is acknowledged to have off-shell mass-dimension +1, not the required +4. The “on-shell insertion” to reach Eq. (B2) [ρbounce_Λ ∼ (α/M) MPl^5] is qualitative. Yet the Ntot ≈ 92 result and the “structural tension” discussion use Eq. (B2) as input.
Required fix: Provide one explicit, fully worked local dimension-4 completion for Eq. (6) (e.g., promote the coefficient as α MPl^3/M or give a concrete curvature-dressed manifestation) and show step-by-step that the on-shell bounce evaluation reproduces the same amplitude budget that underlies Ntot ≈ 92. Alternatively, if you keep the current nonlocal/dimensional-ansatz language, move every quantitative consequence that uses Eq. (B2) (including the Ntot figure) into a clearly boxed “Phenomenological ansatz” subsection, and restate in the abstract and conclusions that any Ntot number is an ansatz-dependent order-of-magnitude illustration (not a quantitative result). PRD requires that the single algebraic step connecting the operator to the scale used in all subsequent arithmetic be auditable.

P1A-E4 (Figures 4 and 7; captions pp. 30 and 33; Table I p. 5)
Problem: Heterogeneous σ values and null procedures are juxtaposed in combined-significance plots (EB rotation versus galaxy bispectrum) and in Table I without an explicit “not directly comparable” qualifier at each juxtaposition. PRD requires unambiguous handling of heterogeneous nulls.
Required fix: At every instance where σ values from different null procedures appear side-by-side (Figures 4 and 7, Table I), insert an in-caption sentence that they are not directly comparable and state the nulls explicitly (e.g., “EB: β=0 null, Planck WMAP+Planck pipeline; bispectrum: local-shape fNL=0 null, Fisher ideal/degraded assumptions as stated; plotted σ cannot be combined in quadrature”). If combined curves are shown, remove them unless you provide and justify a concrete cross-covariance model; otherwise keep the channels separate.

P1A-E5 (Sec. IV.B, Eq. (14), p. 13–14; Eq. (15))
Problem: The “one-loop” parity-odd operator is written with a coefficient β(γ)/MPl but then treated as O(αem/4π)/MPl in the subsequent amplitude estimate, and the symbol β is also used for the CMB rotation angle elsewhere. This conflates two β’s and leaves the normalization of Eq. (14) unclear.
Required fix: Rename the RG coefficient in Eq. (14) to avoid collision with the birefringence angle (e.g., bNY(γ)). Either include the explicit αem/(4π) factor in Eq. (14) or state unambiguously that bNY(γ) ≡ c × αem/(4π) with c = O(1). Then update Eq. (15) so that the dimensionless reduction is traceable and unit-consistent from your Eq. (14) as written.

P1A-E6 (Figure 1 caption; Sec. X.G p. 21; Table VI; refs [46])
Problem: The figure and text annotate a PTA spectral index γPTA = 2.567 ± 0.382 from a “real-KDE reanalysis” (GPU MCMC) in an “in preparation” work. This is a load-bearing numeric annotation with no public provenance.
Required fix: Remove the numerical annotation everywhere unless the PTA analysis is public on arXiv with a stable version you can cite. As written, it violates the standalone-reader test.

P1A-E7 (Sec. IV.D, pp. 14–16)
Problem: Notation reuse and basis conversion for the ALP–photon coupling. The paper’s α/M is not the canonical gaγ; the footnote explains a 10× basis-conversion gap and mentions cγ and fa choices. However, the main text continues to use α/M across two physically different roles (gravity-side parameter and photon-side coupling), which risks confusing readers.
Required fix: Provide a single, prominent mapping box early in Sec. IV.D that defines precisely how α/M relates to gaγ, cγ, and fa, with units, and use the canonical gaγ notation thereafter in all birefringence formulas and plots (retain α/M for the gravitational side only). Move the “10× gap” discussion from the footnote into the main text and make clear which normalization is used in every equation.

P1A-E8 (Data and code availability, p. 26; reproducibility)
Problem: The repository link is mutable; there is no archived DOI nor a frozen commit hash corresponding to the submitted version, and it is unclear whether all figure-generation scripts are present and runnable.
Required fix: Deposit a frozen snapshot of all analysis and figure scripts used in this paper to an archival service (e.g., Zenodo) and provide the DOI and the exact commit/tag in the paper. Include a minimal manifest indicating which script reproduces which figure/table, along with versions of any external dependencies.

MAJOR

P1A-M1 (Use of “closure” language for R2–R3; Abstract p. 1; Sec. IV pp. 11–16)
Problem: Routes R2–R3 are said to be “closed” by amplitude suppression, but the derivations are admitted to be ansatz-level upper bounds. Table III classifies them as Tier III, but the abstract and section headers still use decisive “closed by” phrasing.
Required fix: Systematically soften R2–R3 wording to “falls short by ≳X orders under the EFT ansatz of Sec. IV B/C” in the abstract, section headings, and conclusions. Reserve “closed” for cases supported by a derivation (R1) or a theorem (perturbation transparency). PRD readers should not infer an operator-level no-go.

P1A-M2 (Sec. X.B, Eq. (23), p. 21; clarity)
Problem: The proof that ½ ϵμνρσRμνρσ(˚Γ) = 0 for T=0 is asserted; while true, it would benefit from one explicit line of derivation or a precise citation to standard results to avoid any ambiguity about torsionless/nonmetric cases.
Required fix: Add a one- or two-line derivation (e.g., show the cyclic identity contraction explicitly) or cite a standard reference (Holst 1996, or a modern review) showing that the Holst dual vanishes identically for torsionless connections.

P1A-M3 (Figure 3, p. 34)
Problem: The H(z) comparison figure overlays two different H0 baselines and then explains in the caption that the percent-level deviation is dominated by the H0 offset and is “not” a spin–torsion signal. As-is, the figure risks being read as a positive detection-like deviation.
Required fix: Either (a) replace with an H0-matched overlay so that only the genuine dynamical differences are shown, or (b) move the current panel to an appendix and add a boldface note in the caption stating “Illustrative only; not a model prediction; deviation at z=0 is exactly the H0 offset.”

P1A-M4 (Sec. XII.A; “definitive erasure” language; p. 24–25, 32–33)
Problem: The structural-tension claim that fNL = −35/8 is “definitively erased” at Ntot ≈ 92 is based on the ansatz Dinf ∝ e−3Ntot and qualitative scale-tracking. While the e^32 argument is compelling, the words “definitively erased” are stronger than the analysis provided.
Required fix: Soften to “would be pushed deep inside the subhorizon regime, where the observable bispectrum is expected to be dominated by vacuum-inflationary modes; a full transfer-function calculation is required for a quantitative bound.” Keep the e^32 scale argument.

P1A-M5 (Global notation; multiple pages)
Problem: The symbol M is used both for the “area-gap mass” (MPl/√γ) and as the denominator in the ALP–photon coupling α/M. This invites confusion.
Required fix: Use distinct symbols (e.g., MA for Marea-gap and MCS for the Chern–Simons coupling scale) throughout, and add them to a notation table (Appendix A).

P1A-M6 (Table II and Table VI, pp. 7 and 28)
Problem: Table II (companion-imported inputs) and some entries in Table VI include non-public values. While the manuscript states that none of these are load-bearing, placing them in the main text gives them unwarranted evidentiary weight.
Required fix: Move Table II to Supplementary/Ancillary material or remove it; restrict Table VI to parameters defined and used within this manuscript, or replace external values with published ones.

MINOR

P1A-m1 (Sec. II.B, Eq. (9), p. 8)
Problem: When quoting ρcrit, you switch between unreduced and reduced Planck conventions elsewhere (e.g., Hreh ∼ T^2/MPl). Although you note the unreduced convention in Sec. II.C, readers may still be confused.
Required fix: Add a single boxed “Conventions” paragraph early in Sec. II stating explicitly that unreduced MPl = G−1/2 is used everywhere unless noted, and list the two places where reduced M̄Pl would change order-one factors (e.g., Hreh estimates).

P1A-m2 (Sec. IV.A, Eq. (13), p. 12)
Problem: The numerical estimate of ρNJL is correct; however, to aid reproducibility, include the exact conversion used: 1 cm−3 = (1.97327×10−5 eV)^3.
Required fix: Add the explicit conversion constant in the text or in a footnote.

P1A-m3 (Sec. IV.D, Eq. (17), p. 15–16; Appendix C)
Problem: The sign convention for β and the mapping between ∆θ and ∆ϕ are handled in Appendix C. It would help the reader to state in the main text that your Eq. (17) uses the homogeneous-field, small-rotation limit and that β is achromatic.
Required fix: Add one clarifying sentence in Sec. IV.D referencing App. C’s WKB derivation and the sign convention.

P1A-m4 (Typos/orthography; scattered)
Problem: Names occasionally appear with spurious spaces/diacritics (e.g., “Domaga la,” “Pop lawski”), and there are occasional hyphenation artifacts.
Required fix: Run a careful copyedit pass to correct author names and remove stray spaces.

P1A-m5 (Acknowledgments; p. 26–27)
Problem: The explicit brand reference to an AI assistant is not necessary for a PRD paper and may conflict with evolving policies.
Required fix: Replace with a neutral statement if you wish to acknowledge tool assistance (e.g., “The author used AI-assisted editing tools for language polishing; all scientific content is the author’s responsibility.”) or remove entirely.

NIT

P1A-n1 (Sec. IV.E, “evidentiary status” table phrasing)
Problem: The Tier designations are helpful; a short parenthetical in the caption defining each tier would help readers not to hunt for the legend in the text.
Required fix: Add a one-line definition below Table III.

P1A-n2 (References formatting)
Problem: A few references cite “arXiv preprint (2025)” without journal, which is fine, but check that arXiv categories and IDs are correct and that journal metadata (where available) match current records.

Arithmetic and dimensional audits (spot checks)

- Eq. (7): Your estimate [(α/M) MPl] ≈ 3×10−3 using g^2 = 4παem ≈ 0.092, γ ≈ 0.274, M = MPl/√γ, and ln(Λ^2/μ^2) ≈ 74 is correct to two significant figures.

- Eq. (11): With Ntot ≈ 92 and (Treh/MGUT)3/2 ≈ 0.03 (Treh = 10^15 GeV, MGUT = 10^16 GeV), Dinf ≈ e−276 × 0.03 ≈ 8×10−122, consistent with the text.

- Eq. (13) amplitude budget: Using nψ = 100 cm−3 = 7.66×10−13 eV^3 and MPl^2 ≈ 1.49×10^56 eV^2 gives ρNJL ≈ 4×10−81 eV^4 ≈ 1.4×10−70 ρΛ; correct.

- Eq. (15): The dimensionless ratio Δθone-loop/Δθobs ≈ (αem/4π) (H0/MPl)/(MPl(α/M) βobs) evaluates to ~1×10−60 with α/M = 10−21 GeV−1 and βobs ≈ 6×10−3 rad; correct.

- Eq. (17): With mθ = H0 = 1.5×10−33 eV, β = 6×10−3, α/M = 10−21 GeV−1 = 10−30 eV−1, one finds ρθ ≈ 1.6×10−10 eV^4 ≈ 6 ρΛ; correct. The scaling of the overshoot for mθ ≫ H0 is also consistent.

Length and scope
At 36 pages, the paper is long for its core deliverables (a compact theorem and several ansatz-based amplitude arguments). If the authors remove non-public material, standardize notation, and move purely illustrative overlays and the companion-input table to ancillary, the main text could be reduced to ≲25 pages without loss.

## Summary recommendation
MAJOR REVISIONS

The scalar-sector “perturbation transparency” result is sound and valuable, and several arithmetic and dimensional checks pass. However, the manuscript as submitted is not yet suitable for PRD: it relies too heavily on non-public companion papers for numerical content and figure annotations; it presents a non-variational T·T term inside the action in a way that risks confusion; it uses a non-dimension-4 operator for a central scaling claim without an explicit local completion; and it mixes heterogeneous significance measures in figures without sufficiently strong caveats. Addressing the essential items above, standardizing notation, and tightening the presentation will bring the paper to PRD methodological standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh pass)

The items below are new issues not covered in my initial review. I follow the same coding scheme and add new identifiers continuing the sequence.

ESSENTIAL

P1A-E9 (Sec. X.D, Eq. (23) and surrounding text; Nieh–Yan identity)
Problem: The decomposition “e ∧ e ∧ R = −NY + T ∧ T (Nieh–Yan density plus torsion-squared)” is written with NY ≡ d(e ∧ T). This identity is not correct as stated. The standard Nieh–Yan 4-form is NYstd ≡ d(eI ∧ TI) − eI ∧ eJ ∧ RIJ + TI ∧ TI. Solving for e ∧ e ∧ R gives e ∧ e ∧ R = d(e ∧ T) + T ∧ T − NYstd. If you define NY ≡ d(e ∧ T), then the correct relation is e ∧ e ∧ R = NY + T ∧ T − NYstd, not simply −NY + T ∧ T. As written, the text mixes two conventions and drops a boundary term or an extra topological piece.
Required fix: State one convention unambiguously. Either use NYstd and write e ∧ e ∧ R = d(e ∧ T) + T ∧ T − NYstd, or explicitly define NY ≡ d(e ∧ T) − e ∧ e ∧ R + T ∧ T (the usual “Nieh–Yan density”) and keep consistent signs. Then restate the T = 0 specialization clearly (both d(e ∧ T) and T ∧ T vanish). This avoids sign/total-derivative confusion.

P1A-E10 (Appendix C, after Eq. (C4); cross-reference)
Problem: The text refers to “the companion’s §VI8” to justify a normalization used in this paper. This is a non-public, non-reproducible cross-reference embedded in a key mapping (β formula).
Required fix: Remove the companion cross-reference. Provide the normalization and sign convention self‑contained in this appendix, with a public citation if desired (e.g., Carroll–Field–Jackiw 1990; Harari–Sikivie 1992).

P1A-E11 (Sec. II.C, Eq. (10), Sec. XII.A, Appendix B; numerical consistency of Ξ)
Problem: There is a numerical drift among (α/M)MPl ≈ 3×10−3 (from Eq. (7)), Dinf ≈ 10−121…10−122, and the stated Ξ ≈ 10−123. Using the quoted values yields Ξ ≈ 3×10−124 (if Dinf ≈ 10−121) or ≈ 4×10−122×3×10−3 ≈ 1.2×10−124 (if Dinf ≈ 4×10−122; see E14). Multiple places also state Dinf ∼ 10−121 without reconciling with the explicit e−276×0.03 estimate.
Required fix: Pick one consistent set of inputs and propagate them everywhere: (i) fix Dinf numerically from the stated Ntot and Treh/MGUT; (ii) fix [(α/M)MPl] to the value you actually use (3×10−3 vs 10−2); (iii) recompute Ξ and quote a single value (with a one-line uncertainty rationale). Update all places where Ξ and Dinf appear, including captions and the abstract if needed.

P1A-E12 (Sec. II.C, Fig. 3 caption; rotation term and energy density mapping)
Problem: The mapping from the cω ω2 term in Λeff (units of mass2) to a fractional contribution to ρΛ is opaque. The caption divides (ω/H)2 by 3ΩΛ to assert a contribution “∼ 1.2×10−21 of ρobs
Λ,” but the steps from Λeff = ΞM2
Pl + cω ω2 to ρΛ = Λeff M2
Pl and then to a fraction of ρobs
Λ are not made explicit, nor is the origin of the factor 3ΩΛ.
Required fix: Provide a short derivation: start from the FRW Friedmann equation and define precisely how ω enters (and with what coefficient) and how you normalize to ρobs
Λ. Show the units at each step. If you mean the bound is (cω ω2 M2
Pl)/ρobs
Λ ≪ 1, state it explicitly and justify the use of 3ΩΛ in the denominator.

P1A-E13 (Fig. 5, bottom panel; “Fine-tuning score”)
Problem: The quintessence (1060) and f(R) (1040) bars are labeled as “illustrative order-of-magnitude literature-level comparators,” but there are no citations showing how these numbers were obtained.
Required fix: Provide concrete references for the 1060 and 1040 entries, or move the panel to ancillary material and add a clear “illustrative only” label in the caption. PRD requires published provenance for numbers plotted in the main text.

P1A-E14 (Sec. II.C.1; Appendix B; Dinf arithmetic)
Problem: The text states Dinf ≈ e−276 × 0.03 ≈ 8×10−122. Using ln10 = 2.302585, e−276 = 10−276/ln 10 ≈ 10−119.86 ≈ 1.38×10−120, so e−276 × 0.03 ≈ 4.1×10−122, not 8×10−122.
Required fix: Correct the arithmetic and propagate the update wherever this number is used downstream (Ξ, Ntot illustrations).

MAJOR

P1A-M7 (Global; symbol reuse “γ”)
Problem: γ denotes the Barbero–Immirzi parameter and also appears as γPTA (PTA spectral index). While you sometimes write γPTA explicitly, other places use γ without a subscript (e.g., Eq. (2), several narrative mentions). This invites confusion when figures and text are read quickly.
Required fix: Enforce a strict convention throughout: γBI for Barbero–Immirzi, γPTA for the PTA spectral index. Update figure labels, captions, and text to use the disambiguated symbols everywhere.

P1A-M8 (Sec. X; impact statement on cubic action)
Problem: The claim “the cubic action for ζ … receives zero contribution from the Holst term” follows from the torsionless decoupling, but no explicit pointer or sketch is given for the cubic-order cancellation.
Required fix: Add a one‑line argument or citation showing that once T = 0 and RH(˚Γ) = 0, all Holst-dependent cubic vertices vanish. This will prevent any ambiguity for readers focused on non‑Gaussianities.

MINOR

P1A-m6 (Sec. XII.D; scale factor bookkeeping)
Suggestion: When arguing that SPHEREx‑band comoving modes are pushed to “deep subhorizon” at the bounce for Ntot − Nexit ≈ 32, quote e32 ≈ 7.9×1013 explicitly to give the reader a numerical sense of the shift.

P1A-m7 (Sec. III.A, Eq. (12))
Suggestion: Add a standard reference for the small‑angle uniform rotation formula Cℓ
EB ≈ 2β(CEE
ℓ − CBB
ℓ) (e.g., Lue–Wang–Kamionkowski 1999 or a CMB review), and state in-line that this is the homogeneous, small‑β limit.

P1A-m8 (Sec. V; galaxy‑spin p-value)
Problem: The chirality result quotes “hemisphere null at pLEE < 10−4” but defers all methods to an in‑preparation companion. This is a standalone numerical claim without an auditable null description.
Required fix: Either remove the numerical pLEE value or include a 1–2 line description of the null test and the look‑elsewhere correction applied, with a public reference or archived notebook.

NIT

P1A-n3 (Appendix C; units)
Suggestion: When identifying k ≃ 6×10−4 eV for a 150 GHz CMB photon, add “(taking a0 = 1 so that comoving k today equals physical frequency)” to preempt unit‑system confusion.

Explanation for omissions
I did not repeat previously cataloged issues (non‑public dependencies, action normalization/variation, non‑dimension‑4 operator, heterogeneous σ handling, β‑symbol collision, mutable repository, “closure” language, Bianchi‑identity citation, H(z) overlay, “definitive erasure,” M‑symbol reuse, and companion tables in the main text). Those remain valid and should be addressed in parallel with the new points above.