# P1A R39conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/paper1a_ech_nogo.pdf` md5=ea008466 pages=28
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7741 chars)
**Wall time**: 352.6s

---

Referee report on “Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter” (28 pages)

Scope of review
- Role: methodology rigor (statistics, derivations, dimensional analysis, internal consistency, error propagation).
- I audited every equation and all quoted scalars, recomputed ratios and σ’s from the numbers provided, and checked figure/table consistency and notation.

Global assessment
- The paper’s central theoretical claim (a perturbation-transparency result for the Holst sector with canonical scalar matter) is clearly stated and dimensionally consistent at the level presented.
- However, the manuscript contains multiple items incompatible with PRD standards: load-bearing numerical claims and posteriors are imported from unpublished “companion” works, versioning/internal bookkeeping appears in the PDF, repository provenance lacks a frozen DOI/commit, some quantitative assertions lack a computable backbone, and there are notation issues and a few arithmetic/units problems.
- Many results are framed as ansätze (acceptable if clearly ring-fenced), but several are then used downstream in figures/tables as if “verified values,” which is not acceptable without self-contained methods or citable, public sources.

Below I list all required actions, classified by severity.

ESSENTIAL (acceptance blocks)

P1A-E1 (Title page, p.1): Versioning/internal bookkeeping in the PDF
- Offending text: “(Dated: June 13, 2026 PDT — v1A.0.71)”
- Problem: PRD does not allow version metadata in the published PDF.
- Required fix: Remove “— v1A.0.71” and any other internal versioning from the PDF. Keep a standard “Dated:” if desired, but no internal build tags.

P1A-E2 (Throughout; esp. Abstract, pp.1–4; Secs. I, III, V–VII, XIII; Table IV, p.26): Load-bearing results and posteriors sourced to unpublished “companion” papers
- Offending examples: 
  - “ΛCDM+ΔNeff MCMC verification … documented separately in companion work in preparation [6].”
  - Table IV lists “Verified Value” H0 = 67.68 ± 1.06, ΔNeff = −0.020 ± 0.169 from [6].
  - Galaxy spin null claims and sample sizes from Paper IV [23].
  - PTA γPTA = 2.567 ± 0.382 from Paper III [46].
  - SPHEREx fNL forecast significance summarized from Paper II [2].
- Problem: The manuscript is not self-contained (Stand‑alone reader test). PRD cannot evaluate, reproduce, or even verify the methods without access to these papers. Some claims are presented as “verified values” in a parameter table.
- Required fix: Either (i) excise all quantitative results, tables, and figure annotations that depend on unpublished companions, or (ii) fully include the methods and results in this manuscript (data cuts, likelihoods, priors, convergence diagnostics, estimator definitions, masks, null tests, chain lengths/effective samples, etc.), or (iii) provide public arXiv links and DOIs to posted versions with stable identifiers and ensure nothing load-bearing in the present paper requires content not in those public versions. Table IV should not contain any “verified values” that are not reproducible from this paper alone or from a public, citable source.

P1A-E3 (Data and Code Availability, p.25): Missing frozen release DOI/commit and reproducibility pin
- Offending text: “a Zenodo-archived release will pin all artifacts to the submitted-version snapshot.”
- Problem: For PRD, the reproducibility package must be in-place at acceptance; “will pin” is insufficient. Also, no commit hash/tag is given that matches the exact artifact used for this paper.
- Required fix: Provide a live, immutable DOI (e.g., Zenodo) for a snapshot of the exact repository state used in this paper, list the commit hash/tag in the manuscript, and ensure all referenced paths (e.g., research/branch_R_alp_birefringence/phase2_mcmc/alp_ode.py) exist there. State license and system dependencies.

P1A-E4 (Notation consistency, multiple locations): Ambiguous/incorrect notation for Pontryagin/Chern–Simons term
- Offending text: “Jackiw–Pi gravitational Chern–Simons R∧R˜, parity-odd …” elsewhere “R ∧ Re”, “R Re = ϵ R R”.
- Problem: Confusing/incorrect notation (“Re”, “Ree”) for the Pontryagin density R∧Ṝ (or ϵ R R) appears multiple times. This is a standard invariant and must be denoted unambiguously and consistently.
- Required fix: Replace all instances by a single standard notation (e.g., P ≡ 1/2 ε^{μνρσ} R_{μν αβ} R_{ρσ}{}^{αβ} or, in forms, Tr(R∧R̃)). Audit the manuscript for stray “Re/ Ree” and fix.

P1A-E5 (Sec. X, pp.19–20): Core theorem (Holst dual vanishes by first Bianchi for any torsionless connection) needs a precise citation or a succinct rigorous proof
- Offending text: “The Holst term … vanishes identically … by the first (algebraic) Bianchi identity R_{μ[νρσ]}=0 (which holds for any torsionless connection), … non-metricity does not invalidate the identity provided T = 0.”
- Problem: This is a central load-bearing statement. It is correct in standard Riemannian geometry, but the generality “any torsionless (possibly non-metric) connection” and the specific contraction used warrant either a textbook citation with the exact hypothesis or a short, explicit proof in components or forms.
- Required fix: Add a brief proof (two to five lines, with indices) or cite a standard source making explicit the hypotheses (torsion-free, with/without metric compatibility) under which ε^{μνρσ}R_{μνρσ}=0; and explicitly show that the form-identity e∧e∧R = −NY + T∧T reduces to zero pointwise at T=0 (not just a total derivative). Keep the important “distinct from Pontryagin” clarification.

P1A-E6 (Figures/Claims, Fig. 5 top panel, p.18; associated text): RG “running of α/M” is plotted without a specified β-function
- Offending text: “Renormalization-group running of the parity-odd coupling α/M from the present epoch to the Planck scale … anchored at the primordial benchmark α/M ∼ 10^−21 GeV^−1.”
- Problem: The running curve is presented without the RG equation, scheme, or matter content used. As drawn it appears arbitrary and risks misleading readers.
- Required fix: Either remove the panel or provide the explicit β-function, assumptions (particle content, thresholds), integration and initial condition; include units and axes labels with ticks tied to the calculation. Otherwise relegate the notion of “running” to text only.

MAJOR

P1A-M1 (Sec. IV.A, p.11): Numerical ratio uses a too-crude ρΛ and mixes precise and OOM numbers
- Offending text: “ρ_NJL ≈ 4 × 10^−81 eV^4, i.e. roughly 4 × 10^−69 ρ_Λ for ρ_Λ ∼ (10^−3 eV)^4”
- Check: ρ_Λ ≈ (2.3 meV)^4 ≈ 2.8 × 10^−11 eV^4. Then 4 × 10^−81 / 2.8 × 10^−11 ≈ 1.4 × 10^−70 (not 4 × 10^−69). Using (10^−3 eV)^4 = 1 × 10^−12 eV^4 explains the discrepancy, but that is a poor surrogate for today’s ρ_Λ.
- Required fix: Use ρ_Λ = (2.3 meV)^4 (or the value corresponding to ΛCDM with your H0/Ω_Λ), recompute the ratio consistently, and state explicitly if the comparison is OOM-only. This does not affect the qualitative conclusion (negligible), but PRD requires numerical hygiene.

P1A-M2 (Sec. II.C, p.8): Rotation-energy bookkeeping is opaque
- Offending text: “c_ω ω^2 is a distinct and negligible term, confined to ≲ 10^−21 ρ_obs_Λ ((ω/H)_0 < 5 × 10^−11; dividing by 3Ω_Λ ≈ 2.1 gives ∼ 1.2 × 10^−21 of ρ_obs_Λ).”
- Problem: The mapping from the vorticity bound (ω/H)^2 to a fractional vacuum-energy contribution divided by “3Ω_Λ” is not explained. Without a displayed relation (e.g., how c_ω is fixed and what background equation is used), this reads as handwaving.
- Required fix: Provide the explicit formula connecting ω to an effective isotropic energy term and show the algebra that yields the ≲10^−21 fraction (or delete the calculated fraction and state the physical point qualitatively).

P1A-M3 (Sec. II.A.2 Step 4, p.7): One-loop estimate for (α/M)M_Pl used later needs a compact derivation trace
- Offending text: Eq. (7) and the numeric evaluation to “≈ 3 × 10^−3”.
- Comment: Your back-of-the-envelope result checks out numerically if M = M_Pl/√γ is used (I verified: g^2/(32π^2) × γ × (M_Pl/M) × ln(Λ/μ)^2 ≈ 3 × 10^−3 for your inputs). However, because you later use this to set a benchmark and to argue an “order of magnitude,” readers need a one-line dimensional trace (how γ/M promotes to a dimensionless factor via M_Pl).
- Required fix: Show explicitly (α/M)M_Pl ∼ [g^2/(32π^2)] × γ × (M_Pl/M) × ln(Λ^2/μ^2) with M = M_Pl/√γ so that (M_Pl/M) = √γ, giving γ^(3/2). This makes the 3×10^−3 number transparent.

P1A-M4 (Sec. IV.D, pp.13–14; Appendix C): ALP birefringence mapping is correct but units and normalization need one clean, unified convention
- Issue: You carefully track ϕ (dim +1) vs θ (dimensionless) and derive β = (α/2M) Δϕ with Δϕ = √(2ρ)/m. This is fine. But in the body you also discuss the “canonical” gaγ conventions and a 10× basis-conversion gap footnote.
- Required fix: Provide a single, boxed “operator/normalization conventions” paragraph (one place) giving L ⊃ −¼ F^2 − ¼ (α/M) ϕ F F̃, its θ-form, and the relation to gaγ, cγ, and fa, with dimensionalities. Then point Appendix C to that block. This will prevent reader confusion.

P1A-M5 (Sec. VI and III.B, p.15 and p.10): Galaxy spin “confirmed null” statements depend entirely on a companion paper and are not reproducible here
- Offending text: “Independent ViT-Small … full bias-audit … reported in Paper IV [23]”; “null … disfavored … by a factor of ~6–12.”
- Problem: As written, these are non-verifiable. Either remove them as support for the present manuscript (they are not needed for the ECH closure) or provide sufficient methods and results in an appendix to reproduce the dipole test and error budget.
- Required fix: Either (i) excise the detailed numeric claims and retain only a qualitative “independent ongoing analysis finds no significant dipole,” or (ii) add a self-contained methods/results appendix.

P1A-M6 (Sec. VII, p.15; Figs. 4, 6): SPHEREx fNL detection-significance numbers are imported (and caveated), but the specific 2.6–5σ range shown on figures requires an explicit conditions list
- Offending text: “2.6–5σ realistic after full systematic budget … under Heinrich+2024 σ(fNL)≈0.7 … degraded-with-systematics σ(fNL)≈1.0.”
- Problem: You do cite [36], and you include caveats, but the figure lines/labels give precise-looking σ without a clear conditions list (redshift binning, sky fraction, bias priors, GR projection, photo-z model). These need to be reiterated briefly if you will keep the plotted ranges.
- Required fix: Either remove the numerical ranges from the plotted lines (keep qualitative trajectory only) or add a caption note specifying the assumptions that produce σ≈0.7 and σ≈1.0, with a one-line parameterization (f_sky, N_gal, z bins, priors).

P1A-M7 (Sec. II.C.1, pp.8–9): Thermal “washout” inequality Γwash > H is only asserted
- Offending text: “the operative requirement is Γwash(Treh) > H(Treh) … expected ordering … we leave a full Boltzmann calculation to follow-up.”
- Problem: This is used as a conditional closure point. While you mark it “conditional,” a compact numeric check using known rates (top Yukawa, sphalerons) would greatly improve rigor.
- Required fix: Add a one-line back-of-the-envelope with numbers (e.g., Γ_t ≈ y_t^2 T/(8π), Γ_sph ≈ κ α_W^5 T) evaluated at the representative Treh you use to demonstrate numerically Γ/H ≫ 1 (or clearly retain this only as a conditional aside, not an additional closure leg).

MINOR

P1A-m1 (Sec. I Abstract and body, multiple places): Mixed “10^−60 vs 10^−61” for H0/M_Pl
- Offending text: Route-2 “Planck suppression by H0/MPl ∼ 10^−60 …” elsewhere “H0/MPl ∼ 10^−61”.
- Required fix: Standardize to 1.2 × 10^−61 (or 10^−61) and keep it consistent across the manuscript.

P1A-m2 (Sec. II.B, p.7): LQC critical density range attribution
- Offending text: “ρcrit ≃ 0.27–0.41 ρPl … we extrapolate across schemes … not quoted in [11].”
- Required fix: Since you already flag the scheme dependence, also include a short explicit calculation showing how γ = 0.274 gives ~0.27 ρPl from Eq. (9) to make the extrapolation transparent.

P1A-m3 (Fig. 3, p.8): Parameter line for “Ω_ext_r = Ω_std_r (1 + 0.3/7/8 (4/11)^{4/3})” is unclear
- Problem: As written, “0.3/7/8” is ambiguous. If this is meant to be a ΔNeff proxy, use a clean expression.
- Required fix: Rewrite explicitly (e.g., Ω_r = Ω_γ [1 + 0.2271 (N_eff + ΔN_eff)] with ΔN_eff = 0.3).

P1A-m4 (Notation consistency, multiple locations): “Re”, “Ree”, “Re =” etc.
- Required fix: After addressing P1A-E4, scan and normalize all related symbols. Avoid overloading “γ” (Immirzi) and “γ_PTA” in close proximity; you do note the distinction, but consider a different symbol for the PTA spectral index in figures to minimize confusion.

P1A-m5 (Table IV, p.26): Column heading “Verified Value” is misleading for values not verified within this paper
- Required fix: Rename to “Reference value (from [source])” and remove any rows that point to non-public companions, or add public citations.

NITS

P1A-n1 (Copyediting, multiple pages): Spacing/diacritics in names (e.g., “Pop lawski”, “Domaga la”)
- Required fix: Standardize to “Popławski” (or without diacritics “Poplawski”) and “Domagała–Lewandowski” consistently, or follow journal style.

P1A-n2 (Acknowledgments, p.25): “Claude (Anthropic) as an AI research assistant”
- Comment: Journal policies vary. If PRD requires or disallows such acknowledgments, adjust accordingly. Otherwise acceptable.

P1A-n3 (Bibliography, many entries): Ensure years and arXiv IDs match the cited findings, especially [5], [41]–[45], [46] labeled as 2025–2026 works. 
- Required fix: Verify final citation metadata prior to acceptance; ensure arXiv numbers correspond to the exact results you quote (e.g., ACT DR6 birefringence value).

ABSTRACT-LAST DRIFT SWEEP (pattern-045)
- The abstract generally mirrors the caveats in the body (notably that R4 closes by naturalness, R1–R3 by amplitude under ansätze, and that significances are from different null procedures). Good.
- However, the abstract also repeats companion-paper dependencies (“companion works in preparation [2, 6]”). This is not acceptable for PRD unless those are already public and citable. See P1A-E2.

PROVENANCE (patterns 046/047)
- As per P1A-E3, provide a DOI and commit hash for the exact reproducible bundle; replace “will pin” by a concrete link and hash.

UNCOMPUTED QUANTITATIVE CLAIMS (pattern-048)
- Address P1A-M2 (rotation-energy fraction derivation) and P1A-M7 (Γwash/H).

STANDALONE-READER TEST
- Address P1A-E2 and P1A-M5 comprehensively.

EFFECT SIZES
- Where you quote σ-levels (e.g., EB β), you also provide effect sizes (angles), good. For fNL forecasts, include the amplitude |fNL| and note the practical implication (difference from slow-roll ~ O(1) vs O(10^0)). Already present; make sure the figure captions restate assumptions (P1A-M6).

Page-length
- At 28 pages, the manuscript is long for what is, at its core, a structural/theoretical closure plus a single theorem. If you remove companion-dependent materials and non-essential figures (especially forecast plots and the non-rigorous RG running panel), you could reduce to ~20–22 pages without loss. Recommendation: trim figures to those directly supporting the closure and the perturbation-transparency result.

## Summary recommendation
MAJOR REVISIONS

The central theoretical point (Holst-sector perturbation transparency for canonical scalars) is interesting and, with a precise citation/proof, publishable. However, the manuscript in its current form fails PRD methodological standards due to (i) reliance on unpublished companion works for load‑bearing numerical claims and tables, (ii) missing reproducibility artifacts (frozen DOI/commit), (iii) notation issues for standard invariants, and (iv) several quantitative assertions that require clearer derivations. Addressing the ESSENTIAL and MAJOR items above will make the paper self-contained, reproducible, and internally consistent.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS (fresh-eyes pass)

ESSENTIAL (acceptance blocks)

P1A-E7 (Internal cross-reference errors: Appendix labels)
- Issue: Multiple places point readers to the wrong appendix. Example: p.6 (γ range discussion) says “parameter-budget table (Appendix B)” but the parameter summary table is Appendix A. Similar mismatches recur elsewhere.
- Why it matters: Breaks the stand-alone-reader test and undermines reproducibility/navigation.
- Required fix: Audit and correct all appendix and section cross-references (e.g., “Appendix A: Complete Parameter Summary” vs “Appendix B: Dimensional Status”). Provide a final cross-ref sweep.

P1A-E8 (Route-2 operator normalization/dimensions not fixed)
- Location: Sec. IV.B, Eq. (14) and surrounding text.
- Issue: The mass dimension (and normalization) of the “Nieh–Yan pseudoscalar” ϑNY is not specified. With L ⊃ [1/(16π^2)] β(γ) MPl−1 ∂μϑNY J5μ, dimensional consistency depends on [ϑNY]. If [ϑNY]=0 (angle-like), the overall coefficient should be dimensionless; if [ϑNY]=1, the displayed 1/MPl restores dim+4. The manuscript does not define ϑNY’s normalization, leaving the dimensional status ambiguous.
- Required fix: State explicitly the field redefinition and mass dimension of ϑNY, and give the normalized operator (including any MPl factors) so the Lagrangian density is manifestly dim+4. If ϑNY is dimensionless, drop 1/MPl or include the correct additional factor(s); if it is dim+1, justify and keep 1/MPl. Tie this to a cited construction (e.g., Mercuri) or relegate as an explicit EFT ansatz with dimensions shown.

P1A-E9 (Planck-mass convention drift in H ≃ T^2/MPl)
- Location: Sec. II.C.1, “Reheating thermal reset,” Hreh ∼ T^2/MPl ∼ 10^11 GeV.
- Issue: The manuscript states it uses the unreduced Planck mass throughout, but H ≃ 1.66 g∗1/2 T^2/M̄Pl uses M̄Pl (reduced Planck mass). Using unreduced MPl changes numerical factors by √(8π). The given 10^11 GeV estimate implicitly assumes M̄Pl.
- Required fix: Declare and consistently use one convention. If you keep unreduced MPl elsewhere, write H ≃ c T^2/MPl with c adjusted accordingly (or switch to M̄Pl explicitly). Recompute any Γ/H back-of-the-envelope numbers consistently.

MAJOR

P1A-M8 (Claim of “13 logically-independent constraints” is unproven)
- Location: Abstract, Secs. I, IX, XV.
- Issue: “13 logically-independent” is asserted but independence is not demonstrated (except noting B8 is subsumed by B14). Several barriers are conceptual/heuristic and could overlap in the mechanisms they exclude.
- Required fix: Either (i) provide a short independence matrix/argument (which assumptions each barrier uniquely uses and how overlaps are avoided), or (ii) soften to “13 catalogued constraints (with B8 subsumed by B14)” without the independence claim.

P1A-M9 (NJL density estimate uses non-cosmological nψ as “cosmologically relevant”)
- Location: Sec. IV.A, p.11.
- Issue: nψ ∼ O(10^2) cm−3 is not a cosmological mean density post-recombination; it is an ISM-scale upper bound. While your conclusion (negligible) is robust, the label “cosmologically relevant” is misleading.
- Required fix: Rephrase as “even at dense ISM-like nψ ∼ 10^2 cm−3,” and optionally add the cosmic-mean calculation (n̄b,0 ∼ 2×10−7 cm−3) to strengthen the bound.

P1A-M10 (Undefined angle brackets in Ξ definition)
- Location: Eq. (10) and Eq. (24): Ξ ≡ ⟨(α/M) MPl⟩ Dinf.
- Issue: ⟨…⟩ is never defined (time average? RG average? ensemble?).
- Required fix: Define the averaging operator or remove brackets.

P1A-M11 (Figure/σ comparability missing in captions)
- Location: Figs. 4 and 6.
- Issue: The body text rightly warns that σ values for β and fNL arise from different null procedures; figure captions do not explicitly reiterate this. Readers can misread combined timelines as directly comparable.
- Required fix: Add a one-line caption note: “σ values arise from different null procedures and are not directly comparable across panels; see text.”

P1A-M12 (Barrier-12 ceiling numeric range is quoted without a displayed derivation)
- Location: Sec. IX.L (Eq. 20).
- Issue: ΩGW|bounce ≲ (ρcrit/ρPl)^2 ≃ 0.07–0.17 is presented; the range follows from squaring 0.27–0.41, but this is not shown or cited.
- Required fix: Add the one-line derivation or a citation clarifying the provenance of the quadratic scaling and the numeric range.

P1A-M13 (Appendix-C mapping not fully self-contained)
- Location: Appendix C, end.
- Issue: The final mapping references a “companion” for conventions. Since β = (1/2) gaγ ∆ϕ is central, the conventions (gaγ, Caγ, fa) must be fully stated here.
- Required fix: Inline the gaγ ≡ (αem Caγ)/(2π fa) convention and state the β = 1/2 gaγ ∆ϕ equivalence locally (no external pointer).

P1A-M14 (ε vs Levi–Civita tensor vs density conventions unclear)
- Location: Secs. II.A.2, X.B–D, Appendix B.
- Issue: The manuscript alternates between εμνρσ (symbol) and √−g εμνρσ (tensor). For statements like εμνρσ Rμνρσ = 0, the choice (tensor vs density) matters. This also affects the clarity of the “pointwise zero” vs “total derivative” distinction.
- Required fix: Declare once the convention for ε (tensor or symbol) and stick to it. Where needed, write explicitly e εμνρσ for densities or use the form-language with a clear mapping.

MINOR

P1A-m6 (Appendix mislabel)
- Location: p.6 and elsewhere.
- Issue: “parameter-budget table (Appendix B)” should be “parameter summary (Appendix A).”
- Required fix: Correct all such occurrences.

P1A-m7 (Symbol overloading in Fig. 1)
- Issue: γ (Immirzi) and γPTA (PTA spectral index) both appear; although you note the distinction, the shared glyph invites confusion.
- Required fix: Consider changing the PTA index symbol in figures (e.g., nPTA) to avoid overloading.

P1A-m8 (Fig. 3 caption quantitative claim)
- Issue: “∆H/HΛCDM ∼ 2–3% across z = 0–3” is stated; the figure lacks tick marks or a panel inset to verify this.
- Required fix: Either add an inset or state that the deviation is illustrative for the chosen benchmark parameters.

P1A-m9 (Area-gap mass scale)
- Location: Sec. II.A.2, Step 3.
- Issue: “Marea-gap ∼ MPl/√γ” omits the numerical factor from ∆ = 4√3 π γ ℓP^2.
- Required fix: Add “up to 2(3π)1/2 factors from ∆ = 4√3 π γ ℓP^2” or provide the exact expression used.

P1A-m10 (LQC “no free parameters” wording)
- Location: Sec. II.B.
- Issue: The bounce scale ρcrit depends on γ and ∆ (hence the stated 0.27–0.41 window). “No free parameters” is too strong.
- Required fix: Rephrase to “parameters fixed by the LQC area gap and γ (no additional phenomenological freedoms).”

P1A-m11 (Internal artifact in a caption)
- Location: Fig. 3 caption.
- Issue: Mentions “see generate all figures.py,” which is an internal path.
- Required fix: Remove pathnames; if needed, point to the (to-be-provided) frozen DOI/commit per P1A-E3.

NITS

P1A-n4 (Symbol table/notation polish)
- Issue: Mixed use of F vs calligraphic F for different field strengths and curvature in Sec. II.A.2 without a summary.
- Fix: Add a brief symbol table or a one-sentence legend where 𝔽IJ (gravity) vs Fμν (EM) are separated.

P1A-n5 (Stylistic)
- Issue: Frequent use of “bookkeeping” for parametric estimates.
- Fix: Replace by “parametric estimate” or “ansatz” per journal style.

Explanation
These items emerged from recomputing quoted numbers, checking figure/body alignments, auditing dimensions, and scanning cross-references and captions. I did not repeat previously listed issues (P1A-E1…E6, M1…M7, m1…m5, n1…n3). The new essential items (E7–E9) address clarity and dimensional consistency that affect reproducibility and correctness. The majors tighten claims of independence, conventions, and comparability; the minors/nits improve precision and presentation.