# P1A R40conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/paper1a_ech_nogo.pdf` md5=fd4707e3 pages=28
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (4323 chars)
**Wall time**: 283.2s

---

Referee report on “Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter” (28 pages)

Overall assessment
The manuscript presents a channel-level “no-go” audit for four putative dark-energy routes in minimal Einstein–Cartan–Holst (ECH) gravity and a “perturbation-transparency” statement. Much of the argumentation is qualitative or rests on phenomenological ansätze the authors acknowledge. From a PRD methodology standpoint, there are several essential issues: heavy reliance on “companion” papers in preparation for load-bearing numerical claims and pipelines; version-history prose in the body; multiple places where units/dimensions are left ambiguous; a key quantitative “structural tension” result depends on an ad hoc phase-space prefactor; and the central one-loop amplitude comparison (Route 2) is not derived in a single, unit-consistent way. Numerous figures/tables present numbers without sufficient methodological detail to be reproducible from this paper alone.

Below I list findings by severity, with IDs, page/section, the problem, and the concrete required fix.

ESSENTIAL

P1A-E1 — Throughout (e.g., Abstract, pp. 3–5, 10, 15, 21, 24–25): Non-standalone dependence on “companion” papers in preparation
- Problem: Load-bearing statements (ΛCDM+ΔNeff MCMC values and diagnostics; NaMaster validation; ALP parameter fits; SPHEREx Fisher methodology; PTA KDE MCMC; galaxy chirality pipeline) are repeatedly deferred to “Paper I(b) [6]”, “Paper II [2]”, “Paper III [46]”, “Paper IV [23]”, all “in preparation” or “posted concurrently.” This violates the standalone-reader requirement for PRD methodology work and prevents verification of quoted numbers (e.g., H0 = 67.68 ± 1.06; σ(fNL) ranges; γPTA posterior; galaxy spin null).
- Required fix: Make the present paper fully self-contained. Either (i) remove all companion-dependent quantitative claims and rephrase to purely qualitative context, or (ii) include full methods, datasets, priors, likelihoods, convergence diagnostics, and numerical results in this manuscript. At a minimum, delete internal posterior values (H0, ΔNeff, σ8) and all claims that depend on not-yet-public pipelines. Do not cite “companion, in preparation” as evidence for numerical claims.

P1A-E2 — p. 20, Sec. X D, footnote: Version-history prose in the body
- Quote: “An earlier version of this manuscript misidentified the Holst dual contraction with the Pontryagin density. The correction …”
- Problem: Version-history language must not appear in a PRD paper.
- Required fix: Remove all version-history language; state the corrected identity succinctly with a reference or an explicit proof.

P1A-E3 — p. 25, Data and Code Availability: No pinned, immutable artifact identifiers
- Problem: Only a mutable GitHub URL is provided; the text promises “a Zenodo-archived release will pin all artifacts” in the future. No release tag/commit hash is specified. Reproducibility requirements (provenance surfaces) are not met.
- Required fix: Provide an archived, immutable release with DOI (e.g., Zenodo), list the exact commit hashes, release tags, and checksums corresponding to the paper’s results. The bundle must include all scripts and exact configurations to reproduce every figure and table in this paper (not just in “companions”).

P1A-E4 — pp. 12–13, Sec. IV B (Route 2): Ambiguous, unit-inconsistent amplitude budget; two contradictory order-of-magnitude results
- Problem: The central one-loop amplitude comparison for birefringence alternates between a “canonical” ~10^−60 ratio and an “alternative ordering” giving ~10^−33, with no single, fully dimensionally consistent derivation from a clearly defined operator and field dimensions. The dimension of ϑNY is not specified; the factor of MPl is moved between numerator/denominator without a single explicit chain.
- Required fix: Present one unambiguous derivation. State the operator with a fixed normalization; define the engineering dimensions of ϑNY and J5µ; track units through to a dimensionless ∆θone−loop/∆θobs estimate. Remove the second alternative. If a range remains, quantify it with explicit assumptions and bounds.

P1A-E5 — p. 17, Sec. IX L, Eq. (20): Unsupported GW energy-density ceiling
- Quote: “ΩECH_GW|bounce ≲ (ρcrit/ρPl)^2 ≃ 0.07–0.17,” labeled as an “ansatz.”
- Problem: This formula is used as a “global ceiling” but has no derivation, units audit, or reference. As written it compares an epoch-integrated fractional energy density to a dimensionless squared ratio without showing how it enters the present-day spectrum or respects cosmological redshifting. This is not acceptable as a quantitative bound in PRD.
- Required fix: Either (i) derive Eq. (20) from first principles (including how the ceiling maps to present-day ΩGW(f) via transfer functions) or (ii) remove the equation and all dependent text, keeping only a qualitative statement that bounce-generated GW backgrounds are limited by the bounce’s total energy density.

P1A-E6 — Abstract; pp. 1, 4, 8–9, 21–24: “Structural tension” anchored to an ad hoc (Treh/MGUT)3/2 prefactor
- Problem: The headline Ntot ≈ 92 (and subsequent “structural tension” with fNL at SPHEREx scales) depends on an explicitly ad hoc phase-space prefactor (Treh/MGUT)3/2 and on a phenomenological on-shell scaling (Appendix B). Yet the abstract and conclusions present the tension as a headline result. The paper itself says this prefactor is “dimensional-analysis-aesthetic” and not derived.
- Required fix: Demote the Ntot ≈ 92–94 and the associated “structural tension” from the abstract and conclusions unless you provide a first-principles derivation of the prefactor and a quantitative suppression transfer function across the bounce→inflation→reheating epochs. If retained as a hypothesis, label it explicitly and provide uncertainty propagation that shows the tension is robust to O(1)–O(few) changes in the prefactor.

P1A-E7 — pp. 13–14, Sec. IV D; Appendix C: Inconsistent ALP–photon coupling conventions (α/M vs gaγ)
- Problem: The paper alternates between the nonstandard α/M normalization and the canonical gaγ = (αem cγ)/(2π fa). Footnote 5 states α/M is “not” gaγ, requiring cγ ~ O(10) or fa ~ MPl/10 to match 10^−21 GeV^−1; Appendix C then identifies α/M ≡ Caγ αem/(2π fa). This is internally inconsistent and confuses the mapping used to compute β.
- Required fix: Add a “Conventions” subsection early (Sec. II or IV.D) defining all couplings precisely. Choose one normalization, provide the exact conversion to the other, and propagate it consistently through Eq. (17) and Appendix C. Numerically reconcile α/M = 10^−21 GeV^−1 with specific (fa, cγ) values used for all quantitative examples.

P1A-E8 — p. 12, Eq. (14): Dimension of the Nieh–Yan pseudoscalar ϑNY undefined
- Problem: The dimensional consistency of Eq. (14) depends on whether ϑNY is dimensionless or dimension +1. The text never specifies this, yet uses 1/MPl as a prefactor.
- Required fix: Explicitly state [ϑNY] and verify that the integrand has mass dimension +4. If ϑNY is dimensionless, the 1/MPl prefactor must be reconsidered. If ϑNY is dimension +1, show the field normalization and origin.

P1A-E9 — p. 10–11, Sec. III B and companion references: Quoted MCMC posteriors without methods
- Problem: Numerical posteriors (e.g., H0 = 67.68 ± 1.06, ΔNeff ≈ 0) are quoted from a “companion internal MCMC” that is not accessible. This is not acceptable in PRD.
- Required fix: Either (i) remove all such posterior numbers, or (ii) include full MCMC methods and results here: datasets, masks, priors, likelihoods, Boltzmann code versions, sampler settings, sample sizes, R̂ diagnostics, burn-in, thinning, and chain files.

P1A-E10 — p. 18, Fig. 5 (top): “RG running of α/M” plotted without β-function or inputs
- Problem: The figure shows an evolving α/M vs μ up to MPl with no displayed β-function, scheme, particle content, or threshold matching. The caption calls it a “diagnostic,” but without an equation it is not reproducible or verifiable.
- Required fix: Provide the explicit β-function used, its derivation or citation, threshold matching assumptions, and the integration that yields the curve. Otherwise remove the panel.

P1A-E11 — Multiple places (e.g., Abstract p. 1; Fig. 4 p. 15; Fig. 6 p. 22; Conclusions p. 25): Mixing σ values from different null procedures
- Problem: The paper juxtaposes significances from distinct null hypotheses/procedures (e.g., “~9σ detection” of β≠0 from 0.27°/0.03° versus Planck’s 0.342° ± 0.094°), SPHEREx Fisher forecasts with/without GR-projection, and ACT/Planck EB estimates. Some panels include caveats, but not all juxtaposed mentions carry the “not directly comparable” qualifier at the point of comparison.
- Required fix: Ensure that every instance where σ-values from different null procedures appear side-by-side includes an explicit, local statement that they are not directly comparable, and clearly states each null hypothesis. Where a single-number “σ” is given (e.g., “∼9σ”), specify the null (β = 0), and avoid implying comparability to Planck/ACT constraints unless reanalyzed in a common pipeline.

MAJOR

P1A-M1 — p. 5, Eq. (1): Action includes +¼ Tabc Tabc “as shorthand” while also varying the torsionful connection
- Problem: Writing a T^2 term inside the gravitational Lagrangian but stating it is “not an independently specified kinetic term” is nonstandard and risks double-counting or confusing the variational setup.
- Required fix: Rewrite the formalism cleanly: start from the Einstein–Cartan–Holst + Dirac action without an explicit T^2 term, vary, then integrate out torsion to show the induced four-fermion operator and its coefficient. If you keep Eq. (1), move the explanation into the main text with a precise derivation to prevent misinterpretation.

P1A-M2 — p. 11, Sec. IV A (Route 1): Single-density estimate only; no systematic envelope
- Problem: The amplitude bound uses a post-recombination baryon density nψ ∼ 10^2 cm^−3. No scaling across plausible cosmological densities (IGM, cluster cores, stellar interiors) is provided to show robustness.
- Required fix: Provide a general bound ρNJL ∼ κ nψ^2 over the observed cosmic density range, with numerical values at several benchmarks (IGM, ISM, cluster, stellar) to demonstrate that even the largest densities remain far below ρΛ and that no coherent w = −1 component appears.

P1A-M3 — p. 12–13, Sec. IV B (parity classification and anomaly chain): Clarify operator provenance
- Problem: The operator ∂µϑNY J5µ is called “parity-odd phenomenology,” but intrinsically parity-even; then a reference to the chiral anomaly is used to motivate a link to F F̃. This is too schematic for PRD.
- Required fix: Either provide (or cite) a clear EFT derivation that connects the Nieh–Yan pseudoscalar sector to an observable photon-sector parity-odd correlation, including any required additional couplings, or explicitly limit the claim to an upper-bound amplitude budget and remove language that implies a derived photon coupling.

P1A-M4 — pp. 19–20, Sec. X (perturbation transparency): Proof sketch lacks a formal statement and reference for Holst dual vanishing
- Problem: The argument is plausible (scalar matter ⇒ S=0 ⇒ T=0 ⇒ Γ=ΓLC ⇒ εR=0 by the first Bianchi identity), but the paper should either provide a short, explicit tensor proof or cite a standard reference.
- Required fix: Add a concise proof (two lines using the Riemann symmetries suffice) or cite a standard text/paper where εμνρσ Rμνρσ(ΓLC) = 0 is established.

P1A-M5 — pp. 8–9, Sec. II C 1: “Reheating thermal-reset barrier” needs quantitative rates
- Problem: The argument that Yukawa and sphaleron rates exceed H relies on order-of-magnitude “expectations.” For a methodology paper, numbers should be explicit.
- Required fix: Provide numerical estimates: Γt/H at Treh with yt ~ 1; Γsph/H as a function of T with αW; show explicitly where Γ/H > 1 holds and for which temperature ranges, and note any model-dependence (e.g., right-handed neutrinos).

P1A-M6 — p. 16–17, Table II and surrounding text: “13 logically-independent barriers”
- Problem: The paper asserts logical independence among barriers but does not provide criteria or a proof (e.g., B8 is acknowledged to be subsumed by B14).
- Required fix: Either (i) provide a clear definition and demonstration of independence (e.g., each barrier closes a distinct mechanism class under non-overlapping assumptions), or (ii) remove the “logically independent” phrasing and keep the catalog as a qualitative taxonomy.

P1A-M7 — pp. 13–14, Sec. IV D: External-constraint claims for “free-coupling” ALP scenario are unsupported
- Problem: The text asserts that couplings required at ultralight masses are “in strong tension with helioscope and stellar-cooling constraints,” but provides no numbers or references.
- Required fix: Cite concrete bounds (e.g., CAST, HB-stars, RGB) with the relevant gaγ limits in the ultralight regime and compare numerically to the required coupling.

MINOR

P1A-m1 — pp. 5–6, Sec. II A 1–2: Notation collisions (F as curvature two-form vs Fµν Maxwell)
- Required fix: Consolidate the “calligraphic F” vs “Fµν” disclaimer once in a Conventions paragraph and ensure symbols are consistently distinct in all equations.

P1A-m2 — pp. 7–8, Fig. 3: H(z) comparison based on parameters partly from “companion”
- Required fix: Either remove the quantitative comparison or provide the exact parameter values used and a statement that this is illustrative only, not a derived prediction (the caption already leans this way; tighten the language).

P1A-m3 — pp. 1–2, Abstract vs body: Ensure every abstract numerical claim is backed in-body
- Check: βobs values and significances are backed (p. 10, Sec. III A); Ntot numbers are discussed (Sec. XII A, App. B) but derived only under ansätze; Route closures are discussed. Required fix: At minimum, add “under stated ansätze” to the abstract’s lines that hinge on the on-shell scaling or (Treh/MGUT)3/2 prefactor.

P1A-m4 — pp. 7–8: Units for ω/H bound translation to fractional ρΛ
- Required fix: Leave the quick calculation but add one intermediate line relating Λeff MPl^2 to 3H^2 MPl^2 for clarity.

P1A-m5 — p. 26, Table IV: “Reference values” labeled as from a companion internal MCMC
- Required fix: Add an asterisk at the table header reiterating that these are not used in any closure result and are not part of this paper’s evidence; or remove the table.

NIT

P1A-n1 — Typos/formatting: “Sec. X G” → “Sec. X.G”; ensure consistent hyphenation (Barbero–Immirzi, Nieh–Yan).
P1A-n2 — Clarify that γPTA is unrelated to the Barbero–Immirzi parameter each time it appears on figures (already done once; mirror that in the caption of Fig. 1).

Length recommendation
Given the scope (a largely qualitative channel-level closure with one formal identity), 28 pages is long. If the companion-dependent material is removed and the derivations are tightened, this paper could be reduced to ~18–20 pages without loss: keep the four-route analysis, the perturbation-transparency proof, and the clearly derived/algebraic parts; move speculative forecasts and internal MCMC figures to an appendix or to the appropriate companion when published.

## Summary recommendation
MAJOR REVISIONS

The manuscript addresses an interesting question, but as submitted it does not meet PRD methodology standards. Load-bearing results depend on unpublished “companion” papers; a key one-loop amplitude comparison is not derived in a single, unit-consistent way; a headline “structural tension” relies on an ad hoc prefactor; an unproven GW ceiling is presented as a quantitative bound; code/data are not pinned to immutable artifacts; and version-history prose appears in the body. If the authors make the paper fully self-contained, fix the derivations and dimensional bookkeeping, remove or rigorously justify speculative numerical claims, and provide proper reproducibility artifacts, the work could be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes pass)

ESSENTIAL

P1A-E12 — Nieh–Yan identity misstated (Sec. I footnote a; Sec. X D)
- Problem: The differential-form identity is written as eI ∧ eJ ∧ RIJ = −NY + T I ∧ TI. The standard Nieh–Yan 4-form is NY = d(eI ∧ TI) − eI ∧ eJ ∧ RIJ + TI ∧ TI, implying eI ∧ eJ ∧ RIJ = d(eI ∧ TI) + TI ∧ TI − NY. The d(e ∧ T) term is missing in the paper’s formula.
- Impact: While both d(e ∧ T) and T ∧ T vanish when T = 0 (so the main transparency conclusion is unaffected), the identity as printed is incorrect and could mislead readers.
- Required fix: Correct the identity everywhere it appears and state explicitly that at T = 0 all three terms vanish (NY = d(e ∧ T) − e ∧ e ∧ R + T ∧ T ⇒ e ∧ e ∧ R = d(e ∧ T) + T ∧ T − NY).

P1A-E13 — Additional version-history prose (p. 14, footnote 4)
- Problem: Footnote 4 references “earlier drafts displayed … which … prompted a dimensional-mismatch flag in external review.”
- Required fix: Remove all version-history language here as well (your prior fix P1A-E2 addressed a different spot); retain only the final, self-contained conventions.

P1A-E14 — Arithmetic mismatch in Route 1 amplitude ratio (p. 11, Sec. IV A)
- Problem: Using the paper’s own numbers, ρNJL ≈ 3.9 × 10−81 eV4 and ρΛ ≈ 2.8 × 10−11 eV4 gives ρNJL/ρΛ ≈ 1.4 × 10−70 (70 orders below ρΛ), but the text states “∼69 orders below ρΛ.”
- Required fix: Correct the quoted order-of-magnitude ratio to 10−70 (or “≈ 70 orders of magnitude below ρΛ”).

P1A-E15 — Inconsistent cosmological-constant hierarchy (Fig. 5 bottom vs. Appendix B)
- Problem: Fig. 5 bottom quotes ΛCDM fine-tuning score as 10120, but Appendix B states the “genuine” M4
Pl/ρΛ hierarchy is ∼10122 (and elsewhere 10122 or 10121 are used to set Ntot). 
- Required fix: Use one value consistently across the paper (pick 10122 if that underpins Ntot) and explain any convention differences (reduced vs unreduced MPl) so figure and text agree.

P1A-E16 — Holst-dual normalization inconsistency (Sec. X D)
- Problem: In several places the “Holst dual contraction” is written as εμνρσ Rμνρσ, while Eq. (23) defines RH(Γ̊) ≡ 1/2 εμνρσ Rμνρσ. The extra factor 1/2 is not tracked consistently.
- Required fix: Choose one normalization for the dual contraction and apply it uniformly in text, equations, and any later references to RH.

MAJOR

P1A-M8 — Template-overlap degradation used without method or citation (p. 22, Sec. XIII; footnote 6)
- Problem: The SPHEREx significance is reduced from |fNL|/σ ≈ 6.25 to “∼5–5.5σ optimistic after template-overlap correction r ≈ 0.84,” but no method, calculation, or reference for r is provided.
- Required fix: Provide the overlap definition, basis, and computation (or a citation with the same value and setup) and show how it maps to the quoted degradation. Otherwise remove the r-based adjustment.

MINOR

P1A-m6 — CMB EB small-angle relation presentation (p. 10, Eq. 12)
- Observation: The paper writes CEB
ℓ ≈ 2β (CEE
ℓ − CBB
ℓ). Since most analyses use CEB
ℓ ≈ 2β CEE
ℓ when primordial BB is negligible and lensing BB is treated carefully, consider adding one line clarifying which terms are retained/neglected in practical estimators (to avoid readers inferring a mismatch with standard pipelines).

P1A-m7 — γPTA notation disclaimer missing in Fig. 6 (p. 22)
- Problem: Fig. 1 caption clarifies that γPTA is unrelated to the Barbero–Immirzi γ, but Fig. 6 caption does not repeat this and could confuse readers.
- Required fix: Add the same clarification to Fig. 6 caption.

NIT

P1A-n3 — Minor arithmetic re-checks that do match (for transparency)
- The differential β tension |0.342° − 0.215°|/√(0.094°2 + 0.074°2) ≈ 1.06σ is correct; the βobs significances 0.342°/0.094° ≈ 3.64σ and 0.215°/0.074° ≈ 2.91σ are consistent with the text.
- The ALP energy-density back-calculation ρθ = 2 m2
θ β2/(α/M)2 at mθ = 1.5 × 10−33 eV, β ≈ 6 × 10−3, α/M = 10−21 GeV−1 yields ρθ ≈ 1.6 × 10−10 eV4 as stated.

Explanation
This fresh-eyes pass focused on arithmetic, caption/body consistency, dimensional identities, and internal normalization/coherence. The items above are new and do not duplicate the earlier report. The most consequential new issues are the incorrect Nieh–Yan identity (E12), the inconsistent Holst-dual normalization (E16), and numerical/consistency mismatches (E14, E15).