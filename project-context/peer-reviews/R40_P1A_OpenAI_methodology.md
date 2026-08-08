# P1A R40 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/arxiv/paper1a_ech_nogo.pdf` md5=f1eab008 pages=29
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7111 chars)
**Wall time**: 362.6s

---

Referee report for PRD (methods/statistics focus)

General assessment
The manuscript makes a channel-level “no-go” argument for four minimal Einstein–Cartan–Holst (ECH) dark-energy routes and presents a “perturbation transparency” statement for canonical scalar matter. The paper is long (29 pages) and mixes conceptual arguments with phenomenological bookkeeping, forecasts, and results deferred to multiple “in preparation” companion papers. Many conclusions are qualified as ansatz-level, which is appropriate, but a number of methodology and reproducibility issues do not meet PRD standards.

Below I list all concrete issues found (dimensional analysis, arithmetic checks, statistical statements, reproducibility/provenance, version-history language, figure/table consistency). Each entry includes classification, ID, location, issue, and required fix.

ESSENTIAL findings

P1A-E1
- Location: p. 14, Sec. IV D, footnote immediately below operator definition; text: “Earlier drafts displayed … which (correctly) prompted a dimensional-mismatch flag in external review; the present footnote fixes that gap…”
- Problem: Version-history/editorial-review language appears in the body. This violates PRD style and introduces non-scientific meta-prose.
- Required fix: Remove all references to “earlier drafts,” “external review,” or version history throughout the paper. State the single authoritative convention concisely without referencing prior versions.

P1A-E2
- Location: p. 20, Sec. X D, paragraph starting “An earlier version of this manuscript misidentified …”
- Problem: Same issue: explicit reference to earlier version and a “correction” narrative.
- Required fix: Remove all version-history sentences. Retain the corrected statement only (Holst dual contraction vanishes by algebraic Bianchi at T = 0; Pontryagin is a different invariant).

P1A-E3
- Location: p. 15, Fig. 4 caption; also body text around Sec. VII and XIII
- Problem: Detection “σ” values from different null procedures (Planck/WMAP β ≠ ACT β procedure; SPHEREx fNL Fisher forecasts) are juxtaposed graphically without an explicit, local “not directly comparable” disclaimer. The abstract and some other places include such a caveat, but PRD standards (and the journal’s reproducibility bar) require the qualification at every juxtaposition.
- Required fix: Amend Fig. 4 caption to state explicitly that the displayed significances arise from different null procedures and are not directly comparable; avoid plotting a “combined” σ curve unless a rigorously defined joint estimator and covariance are provided. If a “combined” curve is retained, supply the estimator definition, covariance treatment, and a numerical reproducibility appendix or remove the curve.

P1A-E4
- Location: Throughout (multiple places): reliance on “companion” papers “in preparation” [2], [6], [23], [46]; e.g., p. 4 “Companion paper—… 309,189 frozen accepted samples…”, p. 15 Fig. 4 timeline, p. 19 Sec. X G (PTA γPTA = 2.567 ± 0.382 from a real-KDE GPU MCMC, “in preparation” [46]), Appendix A table (companion internal MCMC), various forecasts.
- Problem: Load-bearing numerical claims and figure annotations rely on unpublished and unavailable analyses. The manuscript is not self-contained for a reader who cannot access those works; key quantities (MCMC posteriors, Fisher forecasts) cannot be verified.
- Required fix: Either (i) remove all numerical claims and figure annotations that depend on unpublished companions, or (ii) move them to a short “Outlook” paragraph without numbers, or (iii) include in this paper a self-contained minimal methods appendix with the precise estimator definitions, data combinations, priors, code versions, burn-in/cut thresholds, and the chains (or a DOI) so a referee can reproduce the quoted numbers. At minimum, remove PTA γPTA and SPHEREx forecast curves unless the full procedure and artifacts are supplied here.

P1A-E5
- Location: p. 25, “Data and Code Availability”
- Problem: Reproducibility not at PRD level. GitHub URL given with no frozen release DOI or commit hash pinned to the submitted version; “a Zenodo-archived release will pin” is future tense. Several artifacts are said to be “in the bundle,” but no hash/DOI is provided.
- Required fix: Provide a persistent DOI (Zenodo/OSF) with an immutable snapshot of all code and data used in this submission, including the exact commit hash, environment files, and instructions to regenerate every figure in this paper. If companion chains are required for any figure appearing here, include them or remove those figures.

MAJOR findings

P1A-M1
- Location: p. 19, Sec. X B (Proof) and Sec. X D
- Problem: The “perturbation transparency” statement is central. The current outline proof is correct in spirit (T = 0 for scalar matter ⇒ Holst dual contraction vanishes by algebraic Bianchi ⇒ no contribution), but it is presented as a sequence of assertions without an explicit variation-of-action step showing T = 0 at each perturbative order for canonical scalar matter and without an explicit tensor-mode check beyond the schematic form. For a PRD-level result, this needs a self-contained derivation.
- Required fix: Add a compact appendix that carries out: (i) the variation with respect to the connection in the ECH+scalar action to show T = 0 holds order-by-order for scalar perturbations; (ii) the explicit demonstration that εμνρσ Rμνρσ(Γ̊) = 0 at T = 0 using index symmetries (one line is sufficient, but show it), (iii) the explicit second-order scalar and tensor actions indicating the Holst term’s null contribution. This can be short but must be explicit.

P1A-M2
- Location: p. 18, Fig. 5 (Parameter-naturalness diagnostics); p. 10–13 Sec. IV (R2/R3 amplitude budgets); p. 21–22 Sec. XII A
- Problem: The one-loop and running arguments (R2/R3) are described as conservative upper bounds “by ansatz.” That is fine, but the current text sometimes treats the resulting many-orders-of-magnitude shortfall as definitive without enclosing it in a clearly demarcated assumption box. Also, Fig. 5 “fine-tuning score” compares different frameworks (ΛCDM/quintessence/f(R)/spin–torsion) on non-uniform definitions of tuning (e.g., Ntot sensitivity vs potential flatness), which risks overinterpretation.
- Required fix: Clearly box or gray-background the exact assumptions used in the R2/R3 amplitude budgets (e.g., which β(γ), which scales, which log). In Fig. 5, add a caption sentence stating explicitly that “fine-tuning scores use different definitions/not directly comparable across models; this panel is heuristic.” Alternatively, move the figure to Supplementary Material.

P1A-M3
- Location: p. 19, Table II (Barriers), entry “Barrier 12: Vacuum Amplification Ceiling” and p. 18–19 discussion
- Problem: The ceiling ΩGW^ECH|bounce ≲ (ρcrit/ρPl)^2 ≃ 0.07–0.17 is introduced as an “ansatz ceiling” without derivation or a literature pointer. As written, it risks being cited as a quasi-bound.
- Required fix: Provide a short derivation or a cited reference where this specific quadratic ceiling arises. If none exists, rephrase as a dimensional estimate with an explicit “back-of-the-envelope” label and remove the numeric 0.07–0.17 band; or move to an appendix making the dimensional path explicit.

P1A-M4
- Location: p. 8, Fig. 3 caption and body text, parameters H0 = 69.2 km/s/Mpc, Ωm = 0.310, “Ξ set to reproduce ρΛ”
- Problem: The figure uses parameters from an internal analysis not documented in this paper. The percent deviations (2–3% across z = 0–3) are stated but not reproducible from the text.
- Required fix: Provide the exact background equations used to generate the orange curve (including how Ξ MPl^2 enters H(z)), and the numerical values of all parameters; or remove the panel as it is illustrative only and not necessary for the core claim.

P1A-M5
- Location: p. 10, Eq. (12) and the surrounding text in Sec. III A
- Problem: The EB relation Cℓ^EB ≈ 2β (Cℓ^EE − Cℓ^BB) is correct for small-angle, uniform β. The text says the paper does not perform a β extraction, yet the equation is presented inline as if used. For methodological clarity, the estimator definition and whether lensing B’s are included must be explicit any time EB is used numerically.
- Required fix: Add one sentence making clear that no EB estimator is implemented in this paper and that Eq. (12) is quoted for orientation only, with lensing B included in published β estimators.

P1A-M6
- Location: p. 11, Sec. IV A, paragraph containing the nψ conversion and ρΛ normalization
- Problem: Two different normalizations for ρΛ are used in different places: (i) (2.3 meV)^4 ≈ 2.8×10^-11 eV^4 (elsewhere), and (ii) “(10^-3 eV)^4” = 10^-12 eV^4 used in the Route-1 ratio paragraph. The OOM conclusion is unaffected, but methodological consistency requires a single normalization carried through.
- Required fix: Choose one normalization for ρΛ (preferably (2.3 meV)^4) and recompute the displayed ratio to that normalization (∼1.4×10^-70 in that case); or explicitly state that the estimate uses the fiducial 10^-12 eV^4 scale. Keep consistency across the text.

P1A-M7
- Location: p. 16–17, Table II and Sec. IX narrative (“Known results,” “Heuristic closure under assumptions”)
- Problem: Several “barriers” (e.g., Liouville conservation; attractor-sensitivity dilemma) are qualitative and assumption-dependent. Presently they are interleaved with quantitative amplitude closures, which risks conflating heuristic arguments with hard bounds.
- Required fix: Visually separate the purely qualitative mechanism-closure entries from quantitative amplitude closures (e.g., subheadings “Heuristic/structural” vs “Amplitude-based”). For heuristic barriers, list assumptions explicitly in a sub-bullet under each entry.

MINOR findings

P1A-m1
- Location: p. 7, Eq. (7) and discussion
- Problem: Numerical estimate [(α/M) MPl] ≈ 3×10^-3 uses specific choices (g^2 = 4παem, γ ≈ 0.274, log ≈ 74) that are not all justified in-line.
- Required fix: Add a one-line parenthetical explaining the log size used (Planck-to-TeV) and that δNY is an unknown scheme-dependent finite piece.

P1A-m2
- Location: p. 9–10, “Reheating thermal-reset barrier” paragraph
- Problem: The washout argument is plausible, but the top-Yukawa rate estimate and the Hubble comparison are given only as narrative.
- Required fix: Add a compact back-of-the-envelope line: Γt/H ∼ y_t^2 MPl/T with T ≈ 10^15 GeV ⇒ Γt/H ≫ 1, and cite a standard review (e.g., Kolb & Turner) for the parametric dependence.

P1A-m3
- Location: p. 16, footnote 6 and Sec. VII
- Problem: The SPHEREx 2.6–5σ wording is careful, but the exact degradation factors (template overlap r ≈ 0.84, GR projection, photo-z) are not specified numerically here.
- Required fix: Either supply a short table of the multiplicative degradations used for the 2.6–5σ band, or change the phrasing to “2.6–5σ depending on template overlap and survey systematics; see Ref. [36] for baseline σ(fNL) ≈ 0.7 Fisher sensitivity.”

P1A-m4
- Location: p. 14–15, footnote 5 (basis conversion α/M vs gaγ)
- Problem: The identification of the numerical mismatch (∼10×) is helpful, but a clear definition of gaγ as used in the ALP literature would help avoid confusion.
- Required fix: Add the explicit definition gaγ ≡ αem cγ/(2π fa) and state clearly that the convention here is −(1/4)(α/M) ϕ F F̃, so α/M ↔ gaγ holds only after matching conventions.

P1A-m5
- Location: p. 5, Eq. (1)
- Problem: The displayed TabcTabc/4 in the gravitational bracket is unusual and could be read as a standalone kinetic term.
- Required fix: Move the clarifying footnote into the main text line immediately below Eq. (1): “The T·T piece is a mnemonic for the on-shell four-fermion contact after eliminating torsion; it is not independently varied.”

NITs (cosmetic/editorial)

P1A-n1
- Location: Abstract and several places: “ans¨atze” with diaeresis
- Problem: Typographical artifact (“ansätze”).
- Required fix: Replace with “ansätze” (UTF-8) or “ansatze”.

P1A-n2
- Location: p. 7, footnote 2, repeated parentheticals
- Problem: Overlong footnote with multiple clauses reduces readability.
- Required fix: Split into two compact sentences or move extended convention discussion to an appendix.

P1A-n3
- Location: Acknowledgments, p. 25: “The author acknowledges the use of Claude (Anthropic) as an AI research assistant …”
- Problem: Nonstandard for PRD; not prohibited, but atypical and unnecessary.
- Required fix: Consider removing or softening to a generic “We used language-model tools for editing; the author is solely responsible for all content.”

Arithmetic, dimensional, and consistency checks performed

- Dimensional status Eq. (6): Verified [α/M] = −1, εe e F has mass dimension +2 in components (with √−g outside), so Lodd has +1. The paper correctly flags the off-shell dimensional shortfall and frames the bounce-scale mapping as an on-shell ansatz.

- One-loop Holst-sector parity coupling (Route 2) amplitude ratio: Using αem/(4π) ≈ 5.8×10^-4, H0/MPl ≈ 1.2×10^-61, MPl(α/M) ≈ 10^-2 (with α/M = 10^-21 GeV^-1), βobs ≈ 6×10^-3 rad, yields ∆θone-loop/∆θobs ≈ 1.2×10^-60. The text’s ∼10^-60 statement is correct.

- Route 1 NJL contact energy density: Using nψ ≈ 10^2 cm^-3 ⇒ nψ ≈ 7.66×10^-13 eV^3, n^2/MPl^2 ≈ 3.9×10^-81 eV^4. Ratio to ρΛ = (2.3 meV)^4 ≈ 2.8×10^-11 eV^4 is ∼1.4×10^-70. The paper quotes ∼4×10^-69 relative to (10^-3 eV)^4; numerically consistent given the chosen normalization; please harmonize as per P1A-M6.

- Route 4 birefringence–density relation: With β = (α/2M) Δϕ and Δϕ ≈ √(2ρθ)/mθ, inversion ρθ = 2 mθ^2 β^2 / (α/M)^2 is correct. Inserting α/M = 10^-21 GeV^-1 (10^-30 eV^-1), mθ = 1.5×10^-33 eV, β = 6×10^-3 gives ρθ ≈ 1.6×10^-10 eV^4 ≈ 5.7 ρΛ. Numbers in text check.

- Inflationary dilution bookkeeping: Ξ = [(α/M) MPl] Dinfl with [(α/M) MPl] ∼ 10^-2 and Dinfl ∼ e^-3Ntot (Treh/MGUT)^{3/2}. Taking Ntot ≈ 92 and prefactor O(0.01–0.1) yields Ξ ∼ 10^-123. Consistent.

- Holst dual vanishing: The assertion εμνρσ Rμνρσ(Γ̊) = 0 at T = 0 follows from Rμ[νρσ] = 0; correct.

- Eq. (9): ρcrit(γ ≈ 0.2375) ≃ 0.41 ρPl and ρcrit(γ ≈ 0.274) ≃ 0.27 ρPl from ρcrit ∝ 1/γ^3; numerically consistent.

- β difference Planck vs ACT: (0.342−0.215)/√(0.094^2+0.074^2) ≈ 1.06σ; correct.

- Rotation negligibility estimate: (ω/H)_0 < 5×10^-11 ⇒ (ω/H)^2 < 2.5×10^-21; dividing by 3ΩΛ ≈ 2.1 gives ≈1.2×10^-21; consistent with text.

Scope/length
The paper is long for the core contribution (a dimensional-analysis-based no-go plus a short perturbation-transparency statement). A focused presentation limited to: (i) precise operator/dimensional arguments, (ii) a clean, explicit transparency derivation, (iii) removal of all companion-paper-dependent figures, could fit in 18–20 pages. Please consider trimming by consolidating repeated caveats and moving heuristic “barriers” to an appendix with a compact bullet list.

Standalone-reader test
As written, the manuscript cannot be fully assessed without the unavailable companions. All load-bearing numerical displays depending on those should be removed or documented here with reproducible artifacts.

Effect sizes
Where σ or “detection” is discussed (β, SPHEREx), you generally include appropriate qualifiers. Please add an explicit effect-size statement whenever a σ is quoted (e.g., for β, the rotation angle magnitude in degrees is already present; for fNL, provide the fractional impact on the low-k bispectrum amplitude or percent-level galaxy bispectrum modulation).

## Summary recommendation
MAJOR REVISIONS

The central conceptual claims (channel-level closures under explicit ansätze; the scalar-matter perturbation transparency) are sound in spirit, and most arithmetic/dimensional checks pass. However, the manuscript contains version-history language (must be removed), depends on multiple unpublished companions (must be excised or made self-contained), lacks a compact explicit derivation for the key “transparency” statement (should be added), mixes heuristic and quantitative “barriers” (should be cleanly separated), and needs stronger reproducibility (frozen DOI). Addressing the ESSENTIAL and MAJOR points above is required for PRD.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes pass)

Only new issues are listed below. IDs continue the prior numbering. I do not repeat any items from the initial report.

ESSENTIAL

P1A-E6
- Location: p. 12–13, Eq. (14) and surrounding text (Route 2)
- Problem: Dimensional inconsistency. The operator written as Γone-loop ⊃ −(1/16π^2) β(γ)/MPl ∫√−g ∂µϑNY J5µ has unclear mass dimension unless ϑNY is assigned a nonstandard dimension. With the common EFT choice ϑNY dimensionless (as for axion-like couplings), ∂µϑNY has mass dimension +1 and J5 has +3, so the integrand is already dimension +4 and the extra 1/MPl makes the Lagrangian density dimension +3. If instead ϑNY is taken to have dimension +1 (or +2), this must be stated and justified.
- Required fix: State explicitly the mass dimension of ϑNY and re-derive Eq. (14) to ensure the integrand has mass dimension +4. If the 1/MPl prefactor is retained, provide the operator-basis argument that demands it; otherwise remove 1/MPl or replace it by the correct dimensionful factor.

P1A-E7
- Location: Appendix B (B1–B2), Sec. II C 1 (Dinf discussion), Sec. XII A; abstract/conclusions where the CC hierarchy is quoted
- Problem: Inconsistent cosmological-constant hierarchy exponents and conventions. The text alternates between 10^121, 10^122, and 10^123 for MPl^4/ρΛ depending on whether unreduced vs reduced MPl and ρΛ ≈ (2.3 meV)^4 vs (10−3 eV)^4 are used. Elsewhere you explicitly state “unreduced MPl throughout,” which would push the ratio toward ~10^123 with ρΛ = (2.3 meV)^4.
- Required fix: Choose one convention (state reduced vs unreduced MPl and the ρΛ normalization) and carry a single number consistently across the paper (and update the Dinf and Ntot figures accordingly). If you keep order-of-magnitude only, explicitly say “we adopt 10^123 (unreduced MPl, ρΛ = (2.3 meV)^4)” and harmonize all occurrences.

P1A-E8
- Location: Sec. II A 2, Eq. (5)–(6) and notation paragraph
- Problem: Notation clash. You state calligraphic F is reserved for gravitational curvature and Fµν for electromagnetism, but Eq. (6) uses plain F IJ
ρσ for the gravitational curvature in components. This conflicts with later use of Fµν for EM.
- Required fix: Use a distinct symbol for the gravitational curvature in components (e.g., RIJ
µν or calligraphic F everywhere), and reserve Fµν exclusively for EM. Fix in Eq. (6) and any other occurrences.

MAJOR

P1A-M8
- Location: Sec. IX (Table II and narrative), abstract (“13 logically-independent barriers”)
- Problem: “Logically independent” is not supported. At least one barrier (B8) is explicitly subsumed by B14; several others are labeled “heuristic” and assumption-dependent. As written, the independence claim is overstated.
- Required fix: Soften to “13 catalogued barriers (one subsumed by B14; several heuristic under explicit assumptions).” Provide a dependency note (e.g., which entries are consequences of B14; which rely on washout, attractors, or Liouville assumptions).

P1A-M9
- Location: Appendix C, line with “(the convention block of the companion’s §VI9)”
- Problem: Cross-reference to an external companion for a basic normalization in a core derivation. This makes the present paper non–self-contained.
- Required fix: Remove the reference to the companion’s section and include the needed convention (gaγ definition, normalization factors) locally in this appendix.

P1A-M10
- Location: Fig. 3 caption (“H0 = 69.2 km/s/Mpc, Ωm = 0.310”) vs Appendix A table (H†0 = 67.68 ± 1.06, Ωm = 0.308 ± 0.005)
- Problem: Stale/inconsistent numbers. The figure uses H0 = 69.2 while the body/appendix quote 67.68 ± 1.06.
- Required fix: Recompute the orange curve with the same parameter set listed in Appendix A or state explicitly that Fig. 3 uses an illustrative, non-MCMC parameter choice. If illustrative, consider moving to Supplementary or add a boxed disclaimer in the caption.

P1A-M11
- Location: Sec. II C and Fig. 3 (Λeff = Ξ MPl^2 term entering H(z))
- Problem: Background normalization not explicit. Given “unreduced MPl throughout,” the FRW normalization involves 8πG factors and can easily lead to numerical slips when plotting H(z). The current paper does not write the exact background equation that was integrated to make Fig. 3.
- Required fix: Write the explicit H(z) equation used, including the normalization that injects Ξ MPl^2 into ρΛ and into H^2 via 8πG/3. This can be one line but is needed for reproducibility and to avoid 8π mismatches.

MINOR

P1A-m6
- Location: Throughout α/M unit usage (e.g., p. 7 and p. 13–14)
- Problem: Mixed units for α/M (GeV−1 and eV−1) with conversions sometimes implicit.
- Required fix: Adopt a primary unit (GeV−1), and when switching to eV−1 include the explicit 10^9 conversion in-line the first time it appears (e.g., “α/M = 10−21 GeV−1 = 10−30 eV−1”).

P1A-m7
- Location: Fig. 1 caption and Sec. X G (γPTA)
- Problem: Figure cites γPTA = 2.567 ± 0.382 from an unpublished analysis, but the caption does not say “unpublished; shown illustratively” (the body does).
- Required fix: Add “illustrative, from an unpublished analysis; no claim is made here” to the Fig. 1 caption, or remove the number from the figure.

P1A-m8
- Location: Footnote 3 near Eq. (14) (“parity-odd phenomenology”)
- Problem: Potential confusion: the operator written is parity-even, while the text calls the route “parity-odd” due to backgrounds. This is fine, but a one-line clarifier would help readers skimming.
- Required fix: Add “We label the route ‘parity-odd’ because a time-dependent background ∂µϑNY breaks P and T; the operator itself is P-even.”

P1A-m9
- Location: Appendix B, first paragraph (B1) and later text
- Problem: The dimensional statement “[ε e e F] = +2” uses component notation; a quick reminder that √−g is outside in Eq. (6) and that you are counting in component form would avoid confusion.
- Required fix: Add a parenthetical “(component counting; √−g outside)” after Eq. (B1).

P1A-m10
- Location: Abstract footnote “a” and footnote “a” label in the main text
- Problem: Footnote marker “a” appears in the abstract, which is atypical for PRD style and can confuse cross-referencing.
- Required fix: Move the abstract’s footnote content into the main text (e.g., to Sec. X D) and remove footnote markers from the abstract.

P1A-m11
- Location: Sec. II C (cω ω^2 term)
- Problem: You correctly note this is anisotropic in rotating Bianchi models and keep it only as a bookkeeping bound, but the equation Λeff = Ξ MPl^2 + cω ω^2 may mislead casual readers to read ω^2 as an isotropic vacuum term.
- Required fix: Add “This term is strictly anisotropic; we do not treat it as an isotropic Λ contribution. It is shown only to bound its negligibility.”

WHY THESE ARE NEW
- The core new issues are the dimension of Eq. (14) (E6), the inconsistent global CC hierarchy exponents and conventions (E7), and inconsistencies between figure parameters and appendix values (M10). These were not addressed previously and materially affect rigor and reproducibility. I also add notation and cross-reference fixes that impede a self-contained PRD submission.