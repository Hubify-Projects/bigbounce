# P1A P1EXACT91ad88e3 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/project-context/peer-reviews/INT_v3/ROUND_2026-07-14-P1-EXACTPDF-91ad88e3-NONANTHROPIC/P1A/frozen/arxiv/paper1a_ech_nogo.pdf` md5=633205d8 pages=6
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (4370 chars)
**Wall time**: 408.7s

---

Referee report on “Algebraic Torsion in Minimal Einstein–Cartan–Holst Gravity: Four-Fermion Contact Bounds and Classical Scalar-Sector Transparency”

Scope of review: methodology rigor, derivation chains, dimensional analysis, internal arithmetic consistency, and reproducibility of quantitative claims. I read the full manuscript, equations, appendices, and references, and recomputed all quoted numbers that appear in the text.

Overall assessment: The paper makes two focused claims: (i) the minimal Einstein–Cartan–Holst (ECH) axial–axial contact term is negligible at late-time densities and remains subcritical in a standard mean-field NJL check; (ii) for canonical scalars, the Holst term is classically inert to all orders about the torsion-free branch. The classical transparency result is well framed and follows from standard identities once hypotheses are fixed. The late-time amplitude estimate is dimensionally consistent and numerically correct for the worked example.

However, there are several essential issues that must be resolved before publication in PRD: (a) the subcriticality headline numbers 0.156 (scalar) and 0.31 (axial) are not reproducible from the paper as written because the inputs to Eq. (B4) are not specified; (b) multiple “repository artifact” placeholders appear in the Data and Code Availability section instead of frozen links or hashes; (c) an ambiguous typesetting of the NJL critical coupling Gcrit leaves the main comparison potentially unclear; (d) a promised “convention footnote” at Eq. (2) is missing; (e) the Immirzi-dependent four-fermion coefficient is stated without a fully pinned convention or equation reference. There are also several presentation issues (Nieh–Yan identity sign/convention, Fierz map documentation, minor notation/forward-reference cleanups).

Findings

ESSENTIAL

P1A-E1 (Abstract and Sec. III B; pp. 1 and 3)
- Problem: The headline subcriticality numbers “largest scalar-channel ratio 0.156; the larger axial-channel ratio remains 0.31” are not reproducible from the text. Equation (B4) gives |Gscalar|/Gcrit = (3 Nf Nc / (64 π^2)) (Λ^2/MPl^2). The paper states “single-species” earlier (suggesting Nf Nc = 1) and mentions a scan including Λ = MPl and Λ = MPl/√γ but does not specify the γ values scanned or the Nf, Nc used to obtain 0.156. For Nf Nc = 1 and Λ = MPl, the ratio is ≈ 0.00475, not 0.156.
- Required fix: State explicitly in the body (not just “repository artifact”) the exact inputs used to obtain 0.156 and 0.31: the values of Nf, Nc, the cutoff(s) Λ used, and the specific γ chosen at the “formal above-Planck cutoff-sensitivity point.” Include a one-line numerical evaluation from Eq. (B4). If a scan was performed, describe the ranges and the maximizing point in-text or add a small table. Ensure the abstract values match these declared inputs.

P1A-E2 (Data and Code Availability; p. 5)
- Problem: The section contains placeholders (“repository artifact” repeated) instead of concrete, frozen references. The GitHub link given (https://github.com/Hubify-Projects/bigbounce) is not pinned to a specific commit, tag, or Zenodo DOI. PRD requires reproducibility.
- Required fix: Replace all placeholders with working, permanent links or DOIs and provide exact commit hashes/tags for every artifact used to validate: (i) the Fierz matrix check and involution F^2 = 1; (ii) the regulated NJL gap-equation code and scan; (iii) any scripts producing the 0.156/0.31 values. Include a minimal README stating environment, compiler/interpreter versions, and how to reproduce the numbers.

P1A-E3 (Appendix B, Eq. (B3); p. 6)
- Problem: The typesetting of the critical coupling is ambiguous. As printed, “Gcrit =
π
2
NfNcΛ2” could be read as π^2/(Nf Nc Λ^2) or π/(2 Nf Nc Λ^2). The distinction is essential to the ratios.
- Required fix: Rewrite Eqs. (B2)–(B4) to remove ambiguity and provide a two-line derivation of Gcrit from (B2) in the M→0 limit, with parentheses that make the factors of π explicit (e.g., Gcrit = π^2/(Nf Nc Λ^2) in your normalization). Cross-check that the numerical examples in the text use the same normalization.

P1A-E4 (Sec. III A; p. 2)
- Problem: The text says “see the convention footnote at Eq. (2))” but there is no footnote there. This leaves the torsion normalization and mapping claim unsupported in place.
- Required fix: Either supply the missing footnote at Eq. (2), explicitly laying out the torsion convention(s) used (e.g., Tλ μν = Γλ[μν] vs 2Γλ[μν]) and the precise mapping of Sabc normalization, or remove the reference and expand the sentence to give the mapping inline with a citation to a standard reference.

P1A-E5 (Sec. II, Eq. (3); p. 2)
- Problem: The Immirzi-dependent four-fermion coefficient is presented as L4ψ = −(3κ/16) [γ^2/(1+γ^2)] (J5·J5) without an explicit derivation in the paper and without a convention-locked citation (equation number and convention match) from the literature. Given the well-known convention sensitivities in this sector (metric signature, γ definition, minimal vs non-minimal coupling), this needs to be pinned down for readers to verify the factor of γ^2/(1+γ^2).
- Required fix: Add a short derivation in a footnote or an appendix (two lines suffice) showing how the Holst term modifies the algebraic Cartan equation for a purely axial spin current and leads to the stated γ-dependent prefactor, or cite an equation from [3] or [7] that matches your conventions (state metric signature, ε0123 normalization, and minimal coupling choice) so readers can confirm the factor and sign.

MAJOR

P1A-M1 (Sec. V D and footnote 1; p. 4)
- Problem: The Nieh–Yan identity is stated as “eI ∧ eJ ∧ R IJ(Γ) = − d(eI ∧ TI) + TI ∧ TI, i.e. e ∧ e ∧ R = −NY + T ∧ T, where NY ≡ d(eI ∧ TI).” In the standard convention (torsion two-form TI = Dei), the exact Nieh–Yan 4-form is NNY ≡ d(eI ∧ TI) = eI ∧ eJ ∧ R IJ − TI ∧ TI. This yields e ∧ e ∧ R = NNY + T ∧ T, not −NY + T ∧ T, when NY is defined as d(e ∧ T). Signs vary with conventions, but the present text defines NY as d(e ∧ T) and simultaneously uses a minus sign, which is inconsistent.
- Required fix: State your conventions explicitly and correct the identity so that the algebra is self-consistent. If you define NY ≡ d(e ∧ T), then write e ∧ e ∧ R = NY + T ∧ T (up to convention-dependent signs clearly explained). The T = 0 conclusion remains unchanged, but the identity should be corrected.

P1A-M2 (Appendix A; p. 5)
- Problem: The Fierz transformation used to project A·A onto S,V,T,A,P channels is given with a 5×5 matrix and the statement that the tensor channel coefficient is zero in the A·A→… rearrangement you use. In many textbook presentations a tensor channel appears for general four-fermion products unless field ordering/identification suppresses it. Since the sign of the scalar projection underpins the “repulsive” statement, this step should be fully documented.
- Required fix: Provide a precise reference (equation number) from [9] or [10] that matches your ordering conventions and shows that for the identical-spinor/direct-channel rearrangement the tensor coefficient indeed vanishes. Alternatively, add a short derivation (two lines using completeness and trace identities) to document the specific Fierz map used and clarify the field ordering and contraction conventions. Confirm explicitly that the scalar coefficient is +1/4 of A·A in your convention, so that Gscalar = (−3κ/16)×(1/4) = −3κ/64.

MINOR

P1A-m1 (Sec. V F; p. 5)
- Problem: The symbol “γBI” is introduced without definition (“tests of γBI…”).
- Required fix: Define γBI at first use as the Barbero–Immirzi parameter.

P1A-m2 (Sec. III heading and III A; p. 2–3)
- Problem: The text says “The contact operator in Eq. (5) …” before Eq. (5) is introduced (it appears a few lines later in III A). Also, essentially the same operator appears as Eq. (4) in Sec. II.
- Required fix: Avoid forward referencing by either moving the definition earlier or referring back to Eq. (4) consistently. Consider defining the operator only once and reusing the same equation number when cited later.

P1A-m3 (Sec. V C–D; p. 4)
- Problem: Notation for the Pontryagin density is informal (“∝ R Re”). 
- Required fix: Replace with a standard expression (e.g., (1/4) εμνρσ Rμνab Rρσab or Tr(R ∧ R)) and cite a standard reference.

P1A-m4 (Throughout)
- Problem: The metric signature and ε0123 normalization are not stated.
- Required fix: State signature and Levi-Civita tensor conventions near Eq. (1), since several signs depend on them.

P1A-m5 (Sec. III A; p. 3)
- Problem: The statement “the cosmic-mean baryon density … would make the bound stronger still” is qualitative; a number would be trivial to provide.
- Required fix: Add the cosmic-mean nψ and the resulting ρNJL/ρΛ number to quantify “stronger.”

NIT

P1A-N1 (Sec. II; p. 2)
- Problem: Minor phrasing/spacing artifacts (e.g., “J γ ¯ a γ5”).
- Required fix: Clean up typographical spacing in bilinears (use standard ψ̄γaγ5ψ).

P1A-N2 (Sec. V C; p. 4)
- Problem: The GW equation switches between k^2 (conformal time) and k^2/a^2 (cosmic time) without explicitly stating the change in the independent variable mid-line.
- Required fix: Keep the two forms on separate lines with explicit “in conformal time”/“in cosmic time” statements, as you already indicate in words.

P1A-N3 (Bibliography)
- Problem: Minor style consistency (ensure all references include consistent arXiv category brackets and journal formatting).
- Required fix: Harmonize formatting (e.g., [5] already uses arXiv:1111.0884 [hep-th]; apply the same style consistently).

Arithmetic and dimensional checks performed

- Late-time density bound: For nψ = 100 cm−3, 1 cm−3 = (1.973×10−5 eV)^3 ≈ 7.66×10−15 eV^3 gives nψ ≈ 7.66×10−13 eV^3. With MPl = 1.22×10^28 eV (MPl^2 ≈ 1.49×10^56 eV^2), ρNJL ≈ nψ^2/MPl^2 ≈ (7.66×10−13)^2 / (1.49×10^56) eV^4 ≈ 4.0×10−81 eV^4. The ratio to ρΛ ≈ 2.8×10−11 eV^4 is ≈ 1.4×10−70. This matches the paper.
- Dimensional analysis: κ has mass dimension −2; J5 has +3; κ(J5)^2 has +4; OK.
- NJL critical coupling: From the stated gap equation, at M→0 the standard hard-cutoff result yields Gcrit = π^2/(Nf Nc Λ^2) in this normalization; confirm and disambiguate as in P1A-E3.
- Ratios 0.156 and 0.31: Consistent with Eq. (B4) only if the paper used Λ > MPl and/or Nf Nc > 1 (e.g., Λ = MPl/√γ with γ ≈ 0.03 and Nf Nc = 1 would give ≈0.158). But these inputs are not stated and must be supplied (P1A-E1).

Novelty and claims
- The paper avoids overclaiming and is careful about scope. The abstract correctly states what is proved except for the unreproducible numerical ratios (P1A-E1).

Length
- Six pages are appropriate for the scope; no shortening required.

## Summary recommendation
MAJOR REVISIONS

The core classical transparency result is correct given the stated hypotheses, and the late-time contact-term bound is consistent. However, essential reproducibility items must be fixed: provide explicit inputs for the 0.156/0.31 ratios, correct the ambiguous NJL critical-coupling equation, replace all “repository artifact” placeholders with frozen links/hashes, supply the missing torsion-convention footnote (or inline mapping), and pin the Immirzi-dependent contact coefficient to a derivation or convention-matched citation. Additional presentation fixes (Nieh–Yan identity convention, Fierz documentation, minor notation) are also required. Once these issues are addressed, the paper could be suitable for PRD.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS (fresh-eyes pass)

ESSENTIAL

P1A-E6 (κ–Planck-mass normalization inconsistency; Secs. II and III A)
- Problem: Eq. (1) defines κ = 8πG, but Sec. III A uses “κ = 1/MPl^2” with MPl = 1.22×10^19 GeV in the numerical estimate. For the unreduced Planck mass this is inconsistent by a factor 8π. If you instead mean the reduced Planck mass M̄Pl ≡ 1/√(8πG) ≈ 2.435×10^18 GeV, then κ = 1/M̄Pl^2, not 1/MPl^2. This affects Eq. (B4) and all κ→MPl substitutions.
- Required fix: State unambiguously whether you use the reduced or unreduced Planck mass and enforce it consistently: either (i) keep κ = 8πG = 1/M̄Pl^2 with M̄Pl ≈ 2.435×10^18 GeV, or (ii) keep MPl ≈ 1.22×10^19 GeV and write κ = 8π/MPl^2. Propagate the choice through Sec. III A and Appendix B (including the numerical prefactors in B4 and the density estimate). If you keep the current numbers, replace MPl by M̄Pl everywhere a κ→1/M^2 substitution is made.

MAJOR

P1A-M3 (Cutoff phrase “above-Planck” is γ-dependent and potentially false as written; Appendix B and Abstract)
- Problem: You write “a formal above-Planck cutoff-sensitivity point Λ = MPl/√γ.” Whether Λ is above MPl depends on γ (Λ > MPl only if 0 < γ < 1). Without specifying the γ range, the “above-Planck” label can be incorrect.
- Required fix: State explicitly the γ interval explored and clarify when Λ exceeds MPl. If the maximizing point for the 0.156/0.31 ratios uses γ < 1, say so in-text.

P1A-M4 (Bridge from internal-index Holst form to spacetime ε·R identity; Sec. V B–D)
- Problem: The argument uses “the Holst term evaluated with the Levi-Civita connection gives (1/2) εμνρσ Rμνρσ,” but the paper does not show (or cite) the internal-to-spacetime conversion: ϵIJKL eI ∧ eJ ∧ RKL ↔ (1/2) ε · R. Without explicit conventions (vierbein determinant e, εIJKL eIμ eJν eKρ eLσ = e εμνρσ, etc.), the Bianchi-based vanishing rests on an unstated bridge.
- Required fix: Add a one-line derivation or a precise citation showing the conversion with your conventions (metric signature, ε0123 normalization, and e ≡ det eIμ), e.g., ϵIJKL eI ∧ eJ ∧ RKL = e d^4x (1/2) εμνρσ Rμνρσ for T = 0. This also ties into P1A-m10 below.

MINOR

P1A-m6 (Undefined symbols vR, vL; Sec. V C, Eq. (7))
- Problem: vR and vL are not defined. The letter v is often used for the canonical Mukhanov variable, so the meaning here (phase/group velocity vs amplitude) is unclear.
- Required fix: Define vR, vL explicitly (e.g., phase velocities, dispersion relations ωR/L(k)) or rewrite Eq. (7) in terms of the tensor mode functions hR/L with “identical dispersion” wording.

P1A-m7 (Scope of γ-inequality; Sec. II, Eq. (3))
- Problem: The statement “γ^2/(1+γ^2) < 1” is correct for real γ. If imaginary/self-dual γ were considered, the factor could behave differently.
- Required fix: Add “for real γ” (the working assumption of the paper) to avoid ambiguity.

P1A-m8 (ζ introduced without definition; Sec. V D)
- Problem: The curvature perturbation ζ is mentioned (“cubic action for ζ ... bispectrum”) without definition or prior use.
- Required fix: Define ζ on first mention or remove the sentence if ζ is not otherwise used in the paper.

P1A-m9 (Define J5·J5 contraction; Secs. II–III)
- Problem: J5·J5 appears without an explicit definition of the contraction (sign depends on ηIJ).
- Required fix: State J5·J5 ≡ ηIJ J5I J5J and give your metric signature, tying into P1A-m4 from the initial review.

P1A-m10 (Internal-to-spacetime epsilon relation; near Eq. (1))
- Problem: The text uses both ϵIJKL (internal) and εμνρσ (spacetime) epsilons but does not state the relation ϵIJKL eIμ eJν eKρ eLσ = e εμνρσ (with your ε0123 normalization).
- Required fix: Add this relation and your ε0123 sign convention near Eq. (1). This also supports the Holst-to-spacetime identity invoked in V B–D.

NO OTHERS

- No additional arithmetic mismatches were found beyond the κ/MPl normalization issue noted in P1A-E6. The late-time density estimate still checks out up to the 8π factor convention (which does not affect the “70 orders” conclusion once the convention is fixed).
- There are no figures, so B (figure-caption vs body-claim) does not apply.
- Null-procedure comparability (E) is not directly implicated, as there are no σ-level comparisons.
- The abstract is otherwise faithful to the body except for items already flagged in the initial review (E1, E3).