# P1A INT-M2 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/arxiv/paper1a_ech_nogo.pdf` md5=a80102d5 pages=32
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6534 chars)
**Wall time**: 337.8s

---

Referee report for Physical Review D (cosmology methods)

Overall assessment
The manuscript presents a “channel-level closure” analysis of four minimal Einstein–Cartan–Holst (ECH) parity-odd/dark-energy routes and a perturbation-transparency theorem for canonical scalar matter. The logical scoping is carefully delimited (ansatz vs derivation; load-bearing vs illustrative numbers), and many common pitfalls (mixing σ from different null procedures) are explicitly caveated. However, several issues prevent publication in PRD in its current form:

- A dimension-carrying error/typo in the one-loop parity-odd operator (Eq. 14) that renders the expression dimensionally inconsistent as written.
- Excessive dependence on “in preparation” companion papers for quantitative values that appear in the main text, tables and figures (MCMC posteriors, SPHEREx Fisher forecast numbers, EB pipeline validation, galaxy-spin results), undermining the standalone-reader criterion.
- Data/code availability lacks a stable, citable, frozen DOI; the repository is referenced, but the Zenodo-archived snapshot is promised rather than present.
- Some derivation chains and dimensional reductions (notably Eq. 15) are opaque and should be cleaned up for unambiguous reproducibility.
- The gravitational action as written (Eq. 1) includes a T·T term that the text simultaneously declares shorthand for an on-shell elimination; this is likely to confuse readers and should be rewritten in a standard ECH+Dirac form with torsion eliminated afterward.

Below I list detailed findings.

Detailed findings

ESSENTIAL

P1A-E1
- Location: Sec. IV.B, page 13, Eq. (14)
- Problem: The one-loop parity-odd operator is written with a coefficient “− 1 16π^2 β(γ) MPl ∫ …” which, as typeset, multiplies by MPl rather than divides by it. The surrounding text states “dimensionless coefficient is O(αem/4π) multiplied by the Planck mass to a single negative power,” so the intended coefficient is β(γ)/MPl. As written, the mass dimension is wrong.
- Required fix: Correct Eq. (14) to include an explicit division by MPl, i.e., −(1/16π^2)[β(γ)/MPl] ∫ d^4x √−g ∂μϑNY J5μ, and check the propagation of this factor into Eq. (15). State the coefficient’s mass dimension explicitly under the corrected equation.

P1A-E2
- Location: Table II (page 7), Sec. III.B (page 10), multiple places across the manuscript where companion results are imported (e.g., Table I footnotes, Sec. V, Sec. X.G, Figs. 4, 7 captions)
- Problem: The paper repeatedly cites quantitative results (MCMC posteriors, NaMaster EB validation, SPHEREx Fisher forecast, galaxy-spin dipole null, PTA reanalysis) from companions “in preparation” and “posted concurrently.” PRD requires the article to be auditably standalone; these results are not reproducible from the current manuscript or stable public sources. Some are embedded as numbers in this manuscript (e.g., H0 = 67.68 ± 1.06; 309,189 samples), potentially implying endorsement.
- Required fix: Either (a) remove all numerical values and figures that depend on non-public, in-prep companions, or (b) include, within this manuscript or its Supplemental Material, the minimum reproducible methods and artifacts to back every imported number (dataset versions, priors, likelihoods, code/commit, chain summaries, convergence diagnostics). Alternatively, replace with citations to already-public peer-reviewed sources. At minimum, Table II must be excised or converted to citations to published sources.

P1A-E3
- Location: Data and Code Availability (page 25), and references throughout to a GitHub repository
- Problem: The reproducibility statement promises a future Zenodo snapshot (“will pin all artifacts to the submitted-version snapshot”) but provides neither a DOI nor a tag/commit hash that ties this submission to an immutable artifact. For PRD methods, a permanent record is required.
- Required fix: Provide a permanent DOI (e.g., Zenodo) and the exact commit/tag used for this submission. Ensure that the archived bundle contains the “frozen chains” referenced in text, plus all scripts to regenerate key figures and calculations used within the present paper, or remove claims relying on those artifacts.

P1A-E4
- Location: Eq. (15), page 13
- Problem: The dimensionless reduction for Δθone-loop/Δθobs is not written transparently; the displayed expression uses a product/quotient “MPl (α/M) βobs” without explicit parentheses, and the role of H0/MPl vs. MPl(α/M) is easy to misread. Although the numerical estimate that follows is plausible, the algebra as presented is ambiguous.
- Required fix: Rewrite Eq. (15) with explicit parentheses and units, e.g., Δθone-loop/Δθobs ≈ [αem/(4π)] [H0/MPl] / [(α/M) MPl βobs]. State numerical substitutions step-by-step, including units (eV, GeV), to make the 10^−60 estimate re-checkable.

P1A-E5
- Location: Sec. II.A.1, Eq. (1), page 5, and footnotes around Eq. (3)
- Problem: The action (1) includes an explicit Tabc Tabc/4 term but the text then explains this is an on-shell shorthand obtained after integrating out torsion from the Einstein–Cartan–Holst+Dirac action. Presenting it in the original action while also stating it is not independently varied is inconsistent and can mislead readers into double counting.
- Required fix: Present the standard ECH+Dirac action without an explicit T·T term. Then, in a separate subsection, derive and write the effective four-fermion contact term obtained after algebraically eliminating torsion (with the correct coefficient, cf. Eq. 13). Alternatively, if you insist on including T·T as shorthand, add a boxed statement immediately after Eq. (1) that this is a not-to-be-varied on-shell mnemonic and provide both the original and the effective forms side-by-side.

MAJOR

P1A-M1
- Location: Entire manuscript; especially Abstract (pages 1–2), Sec. III, Sec. XIII, Figs. 4 and 7
- Problem: Forecast claims (SPHEREx 2.6–5σ; LiteBIRD ~9σ nonzero β) and galaxy-spin “confirmed null” rely on non-public in-prep works. While you repeatedly state these are not load-bearing, the paper still foregrounds specific σ values and figures that a PRD reader cannot audit.
- Required fix: Either (i) replace companions with citations to public, peer-reviewed sources and keep only qualitative statements in the current paper, or (ii) move all forecast numbers and spin-dipole results to an Appendix clearly marked “illustrative, non-load-bearing” or remove them entirely. Everywhere a σ is quoted from a different null procedure, keep the “not directly comparable” disclaimer adjacent, not only in the abstract.

P1A-M2
- Location: Sec. IV.D, pages 14–15; Appendix C, pages 26–27
- Problem: The R4 derivation for β vs ρθ and the statement “θtoday − θrec” mapping are sound, but the choice Δϕrec→today ≈ √(2ρθ)/mθ is justified heuristically. For a rolling or oscillating homogeneous ALP, the mapping depends on regime (frozen vs. oscillatory). The text conflates the endpoint-excursion picture and the oscillatory dilution floor.
- Required fix: Add a short derivation outlining the two regimes explicitly: (a) mθ ≲ H0 (monotonic slow-roll/frozen field), where Δϕ ≈ O(ϕ0) and ρθ ≈ (1/2)m^2 ϕ0^2; (b) mθ ≫ H0 (oscillatory), where the amplitude dilutes as a−3/2 and ρθ ∝ a−3. Clarify which regime is used in each inequality (overshoot) and ensure the numerical example (ρθ ≈ 1.6×10^−10 eV^4 at mθ=H0) is tagged to regime (a). This will pre-empt misreadings.

P1A-M3
- Location: Sec. II.A.2 and Appendix B (pages 7–8 and 25–26)
- Problem: The operator in Eq. (6) is acknowledged to have off-shell mass dimension +1; the paper treats the on-shell M^5_Pl scaling ansatz as bookkeeping. This is fine if clearly separated from any claims that depend on it. However, some later sections (e.g., Ntot ~ 92 vs. 94 discussion) intermix this ansatz with “genuine” Planck-to-ρΛ counting.
- Required fix: Consolidate all uses of Eq. (6) and the on-shell scaling into a single subsection with a boldface “Ansatz” label. In the body text (e.g., Sec. XII.A and Appendix B), consistently refer back to that label and avoid language that could be construed as a derivation. Ensure every place Ntot is used distinguishes the 92 vs. 94 counts as explicitly ansatz-dependent.

P1A-M4
- Location: Sec. X.B–D (pages 19–20)
- Problem: The perturbation-transparency theorem’s proof is concise but omits one standard caveat: the algebraic Bianchi identity ensures εμνρσRμνρσ=0 for T=0, but some readers will want an explicit index-symmetry reduction to verify that the Levi-Civita curvature’s slot symmetries force the dual contraction to zero.
- Required fix: Add a two-line sketch showing Rμνρσ = Rρσμν and Rμ[νρσ]=0 ⇒ εμνρσRμνρσ = 0, or give a reference (textbook or review) where this contraction is shown to vanish for torsionless connections. This strengthens the “theorem” status.

P1A-M5
- Location: Fig. 3 caption (page 29)
- Problem: The caption uses benchmark parameters that differ from values quoted elsewhere (e.g., H0=69.2 vs 67.68 ± 1.06 in Table V) and discusses ΔNeff proxies. While you caveat that the deviation is dominated by H0 choice, the figure risks being misread as an ECH prediction plot.
- Required fix: Either remove Fig. 3 or add a conspicuous label on the panel (“Illustrative only; not an ECH prediction”) and include an H0-matched overlay to demonstrate the “sub-percent” statement quantitatively. Alternatively, move to Appendix.

MINOR

P1A-m1
- Location: Sec. IV.A, page 12
- Problem: Density estimate for the NJL contact term uses “dense ISM-like” nψ ∼ 10^2 cm^−3, giving ρNJL ≈ 4×10^−81 eV^4. The conversion is correct (1 cm^−3 ≈ 7.66×10^−15 eV^3), but the choice of density is arbitrary.
- Required fix: Add a parenthetical note that using cosmic mean baryon density n_b ~ 2×10^−7 cm^−3 strengthens the bound by ~18 orders of magnitude, but the conclusion (≪ρΛ, parity-even) is unchanged.

P1A-m2
- Location: Sec. II.B, Eq. (9), page 8
- Problem: You note that ρcrit=0.27ρPl at γ=0.274 is an internal cross-scheme extrapolation. Good. Please add an explicit citation for the exact formula ρcrit = √3/(32π^2 γ^3) ρPl.
- Required fix: Add a reference (e.g., Ashtekar & Singh (2011) Eq. number) or briefly re-derive from Δ=4√3 π γ ℓP^2 to fix conventions.

P1A-m3
- Location: Sec. II.C.1, page 9
- Problem: The (Treh/MGUT)^(3/2) prefactor is labeled a “phenomenological phase-space ansatz,” but the exact exponent 3/2 appears ad hoc.
- Required fix: Add a one-sentence rationale for the half-integer power (e.g., parity-odd density-of-states suppression) and a pointer to a future or past calculation. Label a plausible range (e.g., O(1) power) to show robustness of the Ntot conclusion.

P1A-m4
- Location: Sec. XIV.D, pages 23–24
- Problem: The erasure-by-e-folds argument is sound but would benefit from a single equation showing kphys,bounce = kobs e^(Ntot−Nexit).
- Required fix: Add the explicit mapping kphys,bounce = k/a|bounce = kobs e^(Ntot−Nexit) and define Nexit clearly in the same equation block.

P1A-m5
- Location: Bibliography
- Problem: Several references list years that would be “future” relative to today (e.g., 2025 arXiv entries for ACT DR6; 2026 companions). That may be correct, but PRD requires that cited works be available at acceptance.
- Required fix: For works “in preparation” or not yet on arXiv, either replace with a stable citation or clearly mark them as “to be posted concurrently” and remove all load-bearing dependence (see E2/M1).

NITS (cosmetic/editorial)

P1A-n1
- Location: Multiple places
- Problem: Typographic spacing and diacritics: “Pop lawski” (space), “Domaga la,” “Poincar´e,” mixed hyphens/dashes.
- Required fix: Normalize to “Popławski,” “Domagała,” “Poincaré,” and use en dashes consistently.

P1A-n2
- Location: Footnote marks and in-text cross-references
- Problem: Some footnotes are lettered (a, b) in the abstract and Table I, which can confuse with equation labels.
- Required fix: Use numeric footnotes consistently or convert these as endnotes.

P1A-n3
- Location: Eq. (12), page 10
- Problem: You note “small-angle, spatially uniform-rotation limit.” Good; for completeness, cite a standard derivation (e.g., Lue, Wang & Kamionkowski 1999 or Minami & Komatsu 2020).
- Required fix: Add a brief citation after Eq. (12).

P1A-n4
- Location: Throughout
- Problem: Repeated long parentheticals in-line interrupt the flow.
- Required fix: Consider moving some of the long caveats to footnotes or an Assumptions box for readability.

Audit of scalars and ratios

- βobs difference significance: |0.342° − 0.215°| = 0.127°. Combined σ = sqrt(0.094²+0.074²) ≈ 0.120°. Ratio ≈ 1.06σ. Matches text.
- LiteBIRD differential test: 0.072°/sqrt(0.03²+0.094²) ≈ 0.730σ. Matches text (0.73σ).
- NJL estimate: nψ = 10^2 cm^−3 ⇒ 7.66×10^−13 eV^3 → ρ ≈ (nψ)^2/MPl^2 ≈ 4×10^−81 eV^4 ≈ 1.4×10^−70 ρΛ. Matches text.
- Eq. (7) loop prefactor: [(α/M)MPl] ≈ 3×10^−3 computed from g^2/(32π^2)·γ·ln(Λ^2/μ^2)·√γ ≈ 0.0031. Matches text (~3×10^−3).
- R4 energy density at mθ=H0: ρθ = 2 m^2 β^2 / (α/M)^2. Taking m=1.5×10^−33 eV, β=6×10^−3, α/M=10^−21 GeV^−1=10^−30 eV^−1 yields 1.62×10^−10 eV^4 ≈ 6ρΛ. Matches text.
- ρcrit scaling: γ=0.274 vs 0.2375 gives (0.2375/0.274)^3 × 0.41 ≈ 0.266. Matches text’s ~0.27.
- ΩGW ceiling: (0.27–0.41)^2 ≈ 0.073–0.168. Matches text.

Abstract-last drift sweep

- Claims about perturbation-transparency: supported and proved (Sec. X).
- Closure of each of the four routes: R1 amplitude-suppressed; R2/R3 ansatz-level amplitude suppression; R4 naturalness rather than amplitude: the body supports these claims; the ansatz-caveats are repeated.
- “Not a complete operator basis” caveat: stated in abstract and repeated in body.
- β measurements and comparability note: stated in abstract with “not directly comparable,” consistent with body. Good.
- Surviving predictions (fNL and β): The paper is careful to say they are ECH-independent; consistent.

Length and focus

At 32 pages, the paper is long for the net methodological innovation (a short Bianchi-identity-based theorem and a set of amplitude/naturalness arguments). A focused version could likely fit within ~20–24 pages by moving illustrative figures relying on companion results (Figs. 3–7; Table II) to an Appendix or removing them.

## Summary recommendation
MAJOR REVISIONS

The paper’s core theoretical point (perturbation transparency for canonical scalar matter) is sound and clearly useful, and the route-closure narrative is generally careful about assumptions. However, the coefficient error in Eq. (14), heavy reliance on non-public companion results for quantitative claims embedded in this manuscript (Table II, figures, and several quoted σ values), and the incomplete reproducibility provisioning (no DOI for the code/data snapshot) require substantial revision before this can meet PRD’s methodological standards. Once Eq. (14) is corrected, all companion-dependent numerics are either removed or supported within this manuscript/Supplemental Material, and a stable archived artifact is provided, I would be enthusiastic to re-review.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS AFTER FRESH-AUDIT (A–J checklist)

ESSENTIAL

P1A-E6
- Location: Sec. II.C, Eq. (10) and surrounding text
- Problem: Relation between Λ and ρΛ is missing the 1/(8π) factor when using the unreduced Planck mass. In Einstein’s equations Gμν + Λ gμν = 8πG Tμν, the vacuum-energy density is ρΛ = Λ/(8πG) = Λ MPl^2/(8π) with MPl ≡ G−1/2. The manuscript states “ρΛ = Λeff MPl^2,” which is off by a factor of 8π.
- Required fix: Use the reduced Planck mass M̄Pl^2 ≡ 1/(8πG) and write ρΛ = Λeff M̄Pl^2, or keep the unreduced MPl and include the explicit 1/(8π) factor everywhere this mapping is used (text, tables, and figure captions).

P1A-E7
- Location: Fig. 3 caption (radiation-density rescaling), also consistency with Sec. III/Appendix A
- Problem: The ΔNeff mapping in the caption omits the standard 7/8 factor. The caption uses Ωr → Ωr std(1 + 0.378 (4/11)4/3), which yields a 0.098 boost. The standard mapping is Δρr/ργ = (7/8)(4/11)4/3 ΔNeff; for ΔNeff=0.378 this is 0.2271×0.378 ≈ 0.0859, not 0.098. In addition, this positive ΔNeff contradicts the body’s “ΔNeff ≈ 0, recovers ΛCDM” narrative (Table V).
- Required fix: Correct the formula to include (7/8) and reconcile with the main-text claim (either set ΔNeff=0 in the figure or clearly mark the panel as purely illustrative with the correct normalization shown).

P1A-E8
- Location: Appendix C, last paragraph
- Problem: Broken cross-reference to “the companion’s §VI8.” This section label is not standard and cannot be resolved by a reader (even if the companion existed).
- Required fix: Remove the cross-reference to an unavailable/ambiguous subsection or replace it with a precise, public citation. Do not rely on companion sub-subsection numbering.

MAJOR

P1A-M6
- Location: Sec. II.C.1 (“Reheating thermal-reset barrier”), sphaleron rate estimate
- Problem: The stated crossover “electroweak sphalerons only exceed H at T ≲ few × 10^10 GeV” is too high by roughly an order of magnitude. Using Γsph ∼ αW^5 T and H ≃ 1.66√g* T^2/MPl with αW ≃ 0.033 and g* ≃ 100 gives Γsph/H ≃ 2.5×10−10 (MPl/T). Setting Γsph/H = 1 implies T ∼ a few × 10^9 GeV, not 10^10 GeV.
- Required fix: Update the numerical threshold and supporting arithmetic. If a different normalization is intended, show the explicit factors used and the resulting T-cross.

P1A-M7
- Location: Sec. IV.B, Eq. (14) narrative (definition of ϑNY)
- Problem: The mass-dimension and normalization of the “Nieh–Yan pseudoscalar” ϑNY are nonstandard/unclear. You declare [ϑNY]=+1 to make ∂μϑNY J5μ/MPl dimension-4, but ϑNY is not defined by reference to a conventional action term (e.g., ϑNY·NY) or canonical field normalization. As written, it is ambiguous whether ϑNY is a dimension-1 canonical field, a dimensionless axion-like angle multiplied by a decay constant, or a composite functional of torsion.
- Required fix: Define ϑNY precisely, including its normalization, mass dimension, and relation to a conventional Lagrangian term (e.g., L ⊃ ϑNY NY). State how this choice maps to Eq. (14) and to any chiral-anomaly chain used to reach photons. Without this, dimensional accounting in R2 remains ambiguous even after correcting the 1/MPl factor (P1A-E1).

P1A-M8
- Location: Fig. 3 vs body (Sec. III and Table V)
- Problem: Body text and tables stress “recovers ΛCDM; ΔNeff ≈ 0,” but Fig. 3 injects a nonzero ΔNeff proxy and a deliberately high H0=69.2 km/s/Mpc, which risks being read as a prediction or a best-fit example. This creates a body–figure inconsistency.
- Required fix: Either remove Fig. 3, or (i) overlay an H0-matched ΛCDM curve, (ii) correct the ΔNeff normalization (P1A-E7), and (iii) stamp the panel “Illustrative only; not an ECH prediction,” as well as state the exact ΔNeff used and why it differs from Table V.

P1A-M9
- Location: Sec. X.C (tensor equation) and immediately following sentence
- Problem: Notational ambiguity: H is used both as the conformal Hubble rate (H ≡ a′/a in h′′ + 2H h′ + k^2 h = 0) and, one sentence later, as the cosmic Hubble parameter in h¨ + 3H h˙ + (k^2/a^2) h = 0. This is easy to misread as the same H.
- Required fix: Use ℋ ≡ a′/a for conformal time and H ≡ a˙/a for cosmic time consistently in equations and text.

MINOR

P1A-m5
- Location: Sec. II.A.2, Step 1 and the ensuing footnote (Sabc relation)
- Problem: The identity Sabc = (1/4) ψ̄ γ[a γbc] ψ = (1/4) εabcd J5d generally depends on gamma-matrix conventions and may carry an extra factor of i in some sign conventions. As written, it may confuse readers attempting to reproduce the contraction.
- Required fix: State the precise gamma-matrix and ε0123 conventions used and whether an i factor is absorbed. A one-line note or reference will eliminate ambiguity.

P1A-m6
- Location: Sec. II.C (Planck-mass conventions)
- Problem: The manuscript mixes unreduced MPl in prose with reduced-MPl conventions implicitly used in some cosmology mappings (e.g., ρΛ). You do note this qualitatively, but an explicit conversion equation is missing near first use.
- Required fix: Add a one-line “convention bridge” near Eq. (10): M̄Pl^2 ≡ 1/(8πG) and ρΛ = Λ M̄Pl^2 = Λ MPl^2/(8π). Refer back to this whenever ρ–Λ mappings appear.

NITS (cosmetic/editorial)

P1A-n5
- Location: Throughout (Fig. 1 caption, Sec. X.G)
- Problem: The symbol γ is used for both the Barbero–Immirzi parameter and the PTA spectral index (γPTA). While you add caveats, reusing γ is still error-prone.
- Required fix: Adopt a different letter for the PTA index (e.g., nGWB) or keep γPTA but add a global notation table early in the text.

P1A-n6
- Location: Figs. 4 and 7 captions
- Problem: Axis-unit clarity. The y-axes are “Detection Significance (σ)” but some points amalgamate heterogeneous null procedures (you note this in text elsewhere).
- Required fix: Add a note on each caption that σ values derive from different null procedures and are not directly comparable; specify the underlying null per curve (EB uniform-β vs bispectrum fNL).

BRIEF RATIONALE

I focused only on additional issues that were not in my initial review. The fresh audit surfaced:
- one normalization error (ρΛ–Λ mapping, P1A-E6),
- a concrete arithmetic/normalization mistake in the ΔNeff rescaling used in Fig. 3 (P1A-E7),
- an order-of-magnitude slip in the sphaleron vs Hubble crossover (P1A-M6),
- and notational/dimensional ambiguities (ϑNY in R2, conformal-vs-cosmic H).

All other earlier issues (wrong MPl placement in Eq. 14, companion-dependence, missing DOI, opaque Eq. 15, T·T placement, etc.) stand and are not repeated here.