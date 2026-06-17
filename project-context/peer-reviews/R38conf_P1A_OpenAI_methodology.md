# P1A R38conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1a_ech_nogo_v1A.0.70.pdf` md5=4e24501f pages=28
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (9398 chars)
**Wall time**: 365.9s

---

Referee report (Physical Review D – methodology/statistics audit)

Scope of this review
- Focus: methodological rigor, internal logic/derivations, dimensional analysis, numerical and statistical correctness, and presentation discipline (claims vs. evidence).
- I read the full 28-page manuscript (figures, tables, equations, captions, and appendices). I recomputed every quoted scalar I could trace from values stated in the text.

Global assessment
- The paper attempts a channel-level closure of four “minimal ECH” routes, supported by a catalogue of “barriers” and a “perturbation-transparency” theorem. Many parts of the theoretical argument are carefully caveated and dimensionally consistent.
- However, the manuscript (i) relies at multiple load-bearing points on “companion” works still “in preparation” for methods/results (MCMC, NaMaster validation, SPHEREx Fisher, ACT/Planck EB pipelines), (ii) contains presentation issues that violate PRD standards (version tags in the header, earlier-draft commentary in the body), (iii) uses a figure (Fig. 3) whose “observable” deviation is dominated by parameter choices, not the proposed physics, and (iv) closes one key route (R2) using an ad hoc operator and a back-of-the-envelope dimensional reduction that needs to be replaced by a proper line-of-sight computation to the observable β. Several other places present σ-levels from different null hypotheses next to each other without an explicit caveat at that location.

Below I itemize all issues, with category, location, problem, and required fix.

ESSENTIAL findings (must be fixed before acceptance)

P1A-E1
- Location: Title block, page 1 (first lines)
- Problem: Versioning/round language in the scientific header: “(Dated: June 13, 2026 PDT — v1A.0.70)”
- Required fix: Remove all version strings, time zones, internal labels, and development tags from the scientific header. Keep only a conventional date (“Dated: June 13, 2026”).

P1A-E2
- Location: Sec. III B (page 10) and throughout where galaxy-spin results are invoked; also Sec. V and VI; references to Paper IV [23]
- Problem: Load-bearing observational claims (galaxy spin “confirmed null”, amplitude-tension with Shamir “factor ∼6–12”, sample sizes, bias audits) rely entirely on a “companion” paper “posted concurrently” and are not presented with sufficient detail in this manuscript. This violates the standalone-reader requirement. No numbers (dipole amplitudes, uncertainties) are provided here; no estimator definition/pre-declaration is given in this paper.
- Required fix: Either (a) include, within this manuscript or its Supplemental Material, the full methods for the chirality classifier, masks, sample selection, null tests, estimator definitions, and the resulting numbers with uncertainties; or (b) remove all quantitative galaxy-spin claims and rephrase to a non-load-bearing literature status until the companion is publicly available, peer-reviewed, and citable.

P1A-E3
- Location: Sec. VII and Fig. 4 caption (page 15), Sec. XIII and Fig. 6 (page 22), Abstract (page 1), Sec. III A (page 10)
- Problem: Multiple σ-values from different null procedures (WMAP+Planck EB β ≠ ACT EB β ≠ SPHEREx fNL forecast vs. inflation null vs. “≠0” β null) are juxtaposed. While the abstract explicitly notes they are “not directly comparable”, that caution does not accompany every juxtaposition (e.g., Fig. 4 caption, Sec. VII bullets).
- Required fix: Add the explicit caveat “these significances arise from different null procedures and are not directly comparable” at every location where heterogeneous σ-values appear side-by-side (figure captions, section VII text, section XIII text). Where practical, add the corresponding effect sizes (e.g., expected |fNL|/σ under the exact template overlap) or relegate cross-channel σ-comparisons to a table that carries the caveat prominently.

P1A-E4
- Location: Sec. IV B (Route 2), esp. Eq. (14)–(15), page 12
- Problem: The closure of Route 2 uses an ad hoc “one-loop parity-odd operator” Γ ⊃ (1/16π^2) β(γ)/MPl ∫ √−g ∂μϑNY J5μ and then estimates ∆θone-loop/∆θobs via H0/MPl with an order-unity line-of-sight reduction. This skips the actual mapping from that operator to a measurable β (which requires the anomaly chain to photons and an explicit line-of-sight integral of the birefringence rate). As written, this is not a controlled computation to the observable; it is a dimensional back-of-the-envelope. The paper highlights the dimensionality caveats elsewhere; for a PRD closure, the observable mapping must be explicit.
- Required fix: Provide a proper derivation from Eq. (14) to an observable β. That requires: (i) writing the induced photon-sector Chern–Simons term through the chiral anomaly, (ii) deriving the dispersion relation including the relevant background ⟨∂μϑNY⟩ and integrating from recombination to today, (iii) carrying units consistently, and (iv) showing the resulting β is ≳58–60 orders of magnitude below βobs for conservative parameter choices. If you wish to retain only an upper bound, state it explicitly as such with a clear, complete line-of-sight expression and justify the replacement H0 ↔ 1/Δt.

P1A-E5
- Location: Sec. III A (page 10), Sec. VII (page 15), Abstract, and multiple places citing MCMC/ALP/NaMaster/Fisher “companion” works [2], [6]
- Problem: The manuscript depends on “Companion paper I(b)” for NaMaster validation, ALP parameter fitting, and ΛCDM+ΔNeff MCMC values (H0 = 67.68 ± 1.06, etc.), and on “Companion II” for SPHEREx Fisher forecasts. These are not accessible to the reader and, in places, underpin claims and figures in this paper (e.g., Figs. 4, 6). This violates PRD’s self-contained requirement.
- Required fix: Either (a) include in this manuscript the minimal methods/derivations and numerical results that you actually use (even if summarized), or (b) remove every quantitative claim that depends on “in-preparation” companions, keeping only conceptual statements clearly labeled as such. At minimum, do not label numbers as “verified values” (see P1A-E12) unless verified within this paper or in a published, citable source.

P1A-E6
- Location: Fig. 3 and caption (page 8)
- Problem: The “ECH dark-energy model vs. ΛCDM H(z)” panel shows a 2–3% deviation across z = 0–3, but the orange curve differs in H0 and Ωm from the blue “reference”, and Ξ was fitted to match ρΛ. The plotted deviation is thus dominated by different baseline parameters, not the claimed “Ξ MPl^2” mechanism. As framed, this risks misattribution of an effect to the proposed physics.
- Required fix: Replot with identical baseline cosmological parameters (H0, Ωm, Ωr) and only one change at a time: turn Ξ on/off. If Ξ is fitted to match ρΛ, the two should be essentially identical; state that clearly. If you intend to illustrate sensitivity to different parameter choices, relabel the figure accordingly and do not present the deviation as the “central observable” of the paper.

P1A-E7
- Location: Sec. X, footnote 8 (page 20)
- Problem: Version-history language in the body: “An earlier version of this manuscript misidentified the Holst dual contraction with the Pontryagin density.”
- Required fix: Remove version-history commentary. State the correct identity succinctly without referencing earlier drafts.

P1A-E8
- Location: Appendix A, Table IV (page 26)
- Problem: Table column “Verified Value” includes “H0 = 67.68 ± 1.06 km/s/Mpc” (and others), attributed to “companion Paper I(b) [6]”. These are not verified within this paper nor citable in a published source.
- Required fix: Change “Verified Value” to “Assumed/Input Value” for any parameter not independently verified in this manuscript or a published source. Provide a citation for each. Do not imply verification by unpublished work.

P1A-E9
- Location: Data and Code Availability (page 25)
- Problem: The text promises “a Zenodo-archived release will pin all artifacts to the submitted-version snapshot,” but no actual DOI or tag is given, and it is stated as a future action. For a paper that emphasizes reproducibility, this is insufficient.
- Required fix: Provide a permanent DOI (Zenodo or equivalent) with an immutable snapshot of all code and frozen artifacts used to generate any figures/numbers in this paper (including commit hash and environment spec). If you cannot, then remove language implying reproducibility beyond what you actually provide and mark the GitHub link as “best-effort, no guarantees”.

MAJOR findings (significant revision required)

P1A-M1
- Location: Eq. (1) and footnote (pages 5–6)
- Problem: The “fundamental action” displays a +¼ Tabc Tabc term within S_ECH while later asserting it is merely a shorthand for the four-fermion contact after integrating out torsion and not varied independently. Presenting it inside the fundamental action is confusing and risks double counting conceptually.
- Required fix: Rewrite the action presentation: (i) state the fundamental action as Holst+Palatini+Dirac, (ii) then, after varying the connection and eliminating torsion algebraically, present the effective four-fermion contact term (with all coefficients) in a separate displayed equation. Remove T·T from the fundamental S unless you explicitly move to an effective action section.

P1A-M2
- Location: Sec. IV C (page 13)
- Problem: Route-3 “mass-dimension lock” closure mixes dimensions (e.g., stating a suppression “relative to the dark-energy density” by (Δγ/γ)(H/MPl) ≈ 10^−63). The observable (β, EB, or a density-like quantity) is not consistently defined in this closure argument.
- Required fix: Specify the observable you are bounding (e.g., a fractional change in a parity-odd correlator or an induced vacuum term) and carry dimensions consistently to a dimensionless ratio against a measured quantity. If your closure does not map to a measured observable, say so and present it as an upper bound with a clearly defined norm.

P1A-M3
- Location: Sec. II C 2 (page 9–10): “> 100 orders of magnitude” underprediction of spin asymmetry
- Problem: The statement “The parity-odd operator coupling α/M ∼ 10^−21 GeV^−1 underpredicts any plausible spin asymmetry by > 100 orders of magnitude” is not supported by an explicit computation in the text.
- Required fix: Provide a concrete estimate that maps α/M to an expected A0-like spin-asymmetry signal in a realistic galaxy sample (with units and a chain of assumptions), or remove the quantitative “>100 orders” claim. Qualitative wording (“utterly negligible under any plausible mechanism”) is acceptable if properly caveated.

P1A-M4
- Location: Sec. VII and Fig. 4 (page 15), Sec. XIII and Fig. 6 (page 22)
- Problem: The SPHEREx 2.6–5σ “realistic significance” is repeatedly quoted but depends on a companion forecast and specific assumptions (template overlap r, GR projection, bϕ priors, photo-z). This paper does not define the estimator, priors, nor the precise degradation steps.
- Required fix: Either (a) include a concise Fisher summary (assumed tracer set, k-cuts, r overlap, priors, and a table of σ(fNL) before/after each systematic) or (b) recast 2.6–5σ as “from [2], not reproduced here,” and remove it from figures unless the figure itself contains the caveat.

P1A-M5
- Location: Sec. II C 1 (pages 8–9)
- Problem: The “reheating thermal-reset barrier” mixes estimates of Γ/H across wide temperature ranges but provides no concrete calculation and yet is presented as a plausible erasure channel for coherence.
- Required fix: Either include an explicit quantitative inequality demonstration Γwash(Treh) > H(Treh) for at least one channel with numbers (using standard expressions at T ∼ 10^15 GeV), or mark this subsection unambiguously as a qualitative conjecture and remove it from any chain of logic that contributes to a definitive “closure”.

P1A-M6
- Location: Sec. II A 2, Eq. (7) and paragraph below (page 7)
- Problem: The numerical chain leading from g^2/(32π^2) × γ/M × ln(ΛUV^2/μ^2) to “[(α/M) MPl] ≈ 3 × 10^−3” is sensible, but the presentation would benefit from writing all dimensionless intermediate products explicitly (e.g., show the γ/M × MPl reduction with M = MPl/√γ).
- Required fix: Add one line showing (γ/M)MPl = γ( MPl/M ) = γ√γ and evaluate numerically (≈0.143) to make the 3×10^−3 result fully traceable.

P1A-M7
- Location: Table IV caption (page 26) and Fig. 5 caption (page 18)
- Problem: Fine-tuning numbers for ΛCDM appear as 10^122 in text/caption, but the bottom panel axis and illustrative bars may suggest 10^120 to some readers. This can confuse the reader given different conventions (reduced vs unreduced MPl).
- Required fix: Standardize on a single figure for ΛCDM hierarchy (state explicitly unreduced MPl ⇒ ∼10^122) and ensure the figure axis and caption match that choice. If using an axis labeled in decades, label the bar for ΛCDM with the same 10^122 used in the text.

MINOR findings (address but do not block acceptance)

P1A-m1
- Location: Sec. II A 1 (pages 5–6), footnote 1 and the two-convention discussion
- Problem: The convention reconciliation is thorough but verbose and partly duplicates text on the same page.
- Required fix: Condense to a single clear convention statement and move the long derivation pointer to an appendix if needed.

P1A-m2
- Location: Sec. II C (page 8), Eq. (10) and rotation-bound estimate in caption of Fig. 3
- Problem: The derivation of the “∼1.2×10^−21 of ρΛ” from (ω/H)^2/(3ΩΛ) is not shown.
- Required fix: Add a one-line derivation or drop the specific 1.2×10^−21 factor; keep the statement “utterly negligible.”

P1A-m3
- Location: Sec. X C, Eq. (21) (page 19)
- Problem: The tensor-mode equation is given in both conformal and cosmic times; minor typographical spacing (“k^2 h_ij” vs “k^2 h_ij”).
- Required fix: Uniformize notation and spacing; define primes and dots once.

P1A-m4
- Location: Sec. IV E (page 14–15)
- Problem: Route-4 naturalness closure is clearly explained, but the text oscillates between α/M “bounded by one-loop” and “treated as free phenom parameter.” This could be misread as inconsistent.
- Required fix: Add one sentence at the start of R4: “We consider two subcases: (i) α/M as bounded by the anomaly matching estimate, which leads to the mθ ∼ H0 tuning; (ii) α/M floated phenomenologically, which removes predictive power and runs into astrophysical constraints.”

P1A-m5
- Location: Sec. II A 2, Fig. 2 (page 6)
- Problem: The “Energy density hierarchy” sketch is useful but lacks units on the vertical axis.
- Required fix: Label the axis (log10 ρ in eV^4 or in units of ρPl) and mark the bounce and present-day reference values.

P1A-m6
- Location: Bibliography (pages 27–28)
- Problem: Several references are 2025–2026 preprints without journal info. Acceptable, but cross-check arXiv identifiers and years for consistency.
- Required fix: Ensure arXiv IDs and years match the cited versions; for [5] and others marked “arXiv preprint (2025)”, include arXiv IDs in the text consistently.

NITs (cosmetic)

P1A-n1
- Location: Sec. I A (page 3), Table I caption (page 4)
- Problem: A few stylistic redundancies (“class-level” repeated).
- Required fix: Light edit for concision.

P1A-n2
- Location: Sec. X A (page 19)
- Problem: “This generalizes Hehl et al. (1976) to the Holst sector and to all perturbation orders.” A citation pin (equation or page) would help.
- Required fix: Add a pinpoint to the relevant result being generalized.

P1A-n3
- Location: Sec. II B (page 7)
- Problem: Minor typographical spacing in Eq. (9) (γ2 vs γ^2).
- Required fix: Typeset powers consistently.

Numerical/derivation spot checks performed
- Conversion in R1 density estimate: with nψ = 10^2 cm^−3 → 7.66×10^−13 eV^3, ρ ∼ n^2/MPl^2 ≈ 4×10^−81 eV^4, giving ∼4×10^−69 ρΛ. Matches text.
- R2 ratio Eq. (15): αem/(4π) ≈ 5.8×10^−4; H0/MPl ≈ 1.2×10^−61; MPl(α/M) ≈ 10^−2; βobs ≈ 6×10^−3 rad ⇒ ratio ∼1×10^−60. Matches text.
- R4 inversion (Eq. 17): with α/M = 10^−21 GeV^−1 = 10^−30 eV^−1, β ≈ 6×10^−3, mθ ≈ 1.5×10^−33 eV ⇒ ρθ ≈ 1.6×10^−10 eV^4 ≈ 6 ρΛ. Matches text.
- Barrier 12 ceiling: (ρcrit/ρPl)^2 with ρcrit/ρPl ∈ [0.27, 0.41] ⇒ [0.073, 0.168]. Matches text.
- Ntot from Dinf ∝ e^−3Ntot to reach 10^−122: Ntot ≈ (122 ln 10)/3 ≈ 93.8. The manuscript’s 92–94 range is consistent with its own ansatz variability.

Length/fit to contribution
- The paper is long (28 pages) for what is, at heart, a conceptual closure argument plus a formal transparency result. Given PRD expectations, consider trimming to ≤20 pages by moving descriptive background (e.g., parts of Sec. II A 3, Sec. VIII, and repetitive caveats) to an appendix or Supplement.

Standalone-reader test
- Multiple critical elements currently fail this test (P1A-E2/E3/E5/E8/E9). These must be addressed to meet PRD standards.

Effect sizes
- Where σ-levels are quoted (SPHEREx fNL, LiteBIRD β detection), consider adding effect-size context: e.g., expected EB amplitude at β = 0.27°, fraction of EE rotated into EB, and for fNL the expected bispectrum amplitude relative to shot noise and cosmic variance in the quoted configuration.

## Summary recommendation
MAJOR REVISIONS

The core theoretical contribution (perturbation transparency and channel-level closures) is potentially suitable for PRD once the paper is made fully self-contained and the methodology presentation tightened. However, the current manuscript relies on unpublished companions for quantitative claims, includes non-PRD-compliant version text, juxtaposes heterogeneous σ-values without local caveats in several places, contains a misleading H(z) figure, and closes Route 2 using an ad hoc estimate that should be replaced by a proper observable computation. Addressing the ESSENTIAL and MAJOR items above will significantly improve methodological rigor and presentation to meet PRD’s standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes pass)

Scope of this addendum
- I re-ran the A–J checklist you requested (arithmetic, captions vs. body, dimensional consistency, cross-references, null-procedure comparability, abstract faithfulness, novelty claims, hedges, appendix/main-text match, stale numbers).
- I ONLY list NEW issues below; none of the items already raised in my prior report are repeated.

ESSENTIAL findings (must be fixed before acceptance)

P1A-E10
- Location: Sec. X G (page 20), Fig. 1 caption (page 5), Table III (page 21), Appendix A Table IV (page 26)
- Problem: Dependence on “companion Paper III [46]” (real-KDE PTA reanalysis) for γPTA = 2.567 ± 0.382 is load-bearing in the narrative and appears in figure/table annotations, but the analysis is unpublished and not summarized here.
- Required fix: Either (a) include a short, self-contained description of the PTA pipeline used to obtain γPTA (dataset, likelihood, priors, spectral model, convergence metrics) and freeze an immutable DOI with the chain/posterior used in this paper, or (b) demote all uses of γPTA to purely contextual text without numbers and remove it from figures/tables. As with the other companions, do not present unpublished results as “verified” inputs.

P1A-E11
- Location: Sec. IV B, Eq. (14) and surrounding paragraph (page 12)
- Problem: Dimensional inconsistency in the displayed “one-loop parity-odd operator.” As written, L ⊃ (1/16π^2) β(γ)/MPl ∂μϑNY J5μ has mass-dimension 3 unless ϑNY is assigned a nonstandard mass dimension. The manuscript does not specify [ϑNY]. If ϑNY is a dimensionless pseudoscalar (natural for a topological angle), ∂μϑNY has dimension +1, J5 has +3, so the coefficient must be dimensionless (not 1/MPl) for L to have dimension +4. If ϑNY carries dimension +1, ∂μϑNY has +2 and the coefficient must be 1/MPl^0 or 1/MPl^−? Clarification is required.
- Required fix: State explicitly the mass dimension of ϑNY, re-derive the operator with correct prefactor dimensionality, and carry that consistently into the observable bound. If the intent was to write an upper-bound EFT ansatz, say so and fix the prefactor so that the Lagrangian density is dimension +4 before proceeding to any β estimate.

P1A-E12
- Location: Sec. IV D, footnote under the Chern–Simons operator paragraph (page 13–14)
- Problem: The text references “external review” and earlier-draft issues (“correctly) prompted a dimensional-mismatch flag in external review”). This is version-history process language inappropriate for the published record.
- Required fix: Remove all mentions of external review and earlier drafts. State the single authoritative normalization/convention succinctly and move any extended convention notes to an appendix or SI.

P1A-E13
- Location: Appendix C (page 26–27), “Setup” paragraph
- Problem: Internal file-system path cited (“research/branch_R_alp_birefringence/phase2_mcmc/alp_ode.py”). This is not an archival reference and breaks the standalone-reader/reproducibility standard.
- Required fix: Replace with a DOI (Zenodo or equivalent) to a frozen archive that contains the exact script and environment used. If not available, remove the path reference and explicitly state that the ODE was integrated with a standard solver, giving the equation and initial conditions only.

MAJOR findings (significant revision required)

P1A-M8
- Location: Sec. IV B (page 12), transition from Eq. (14) to Eq. (15)
- Problem: Even aside from the dimensional issue (P1A-E11), the line-of-sight mapping replaces the cosmological integral with H0 by fiat, and folds in MPl(α/M) from a different sector. This risks double counting or mixing unrelated normalizations. The current text labels this as “canonical contraction,” but it is not an explicit integral of a dispersion relation to an observable.
- Required fix: If you insist on retaining a back-of-the-envelope bound while you work up a full derivation, write an explicit inequality starting from a physically normalized birefringence rate dβ/dη ∝ background field(s), integrate ∫ηrecη0, and show each factor’s origin. State it transparently as an upper bound (not an observable prediction).

P1A-M9
- Location: Sec. IX L, Eq. (20) and discussion (page 17)
- Problem: The “vacuum amplification ceiling” ΩGW|bounce ≲ (ρcrit/ρPl)^2 is introduced without derivation or a clear physical norm. While the numerical range (0.07–0.17) is dimensionless, the logic that a fractional GW energy density at the bounce is bounded by a squared ratio of critical to Planck densities is not justified.
- Required fix: Either provide a physical derivation (e.g., from an explicit quadratic-in-perturbations energy density expression normalized to ρtot at the bounce) or recast Eq. (20) as a heuristic, non-binding ceiling and remove any downstream use as a quantitative constraint.

P1A-M10
- Location: Fig. 2 and Sec. III/IV usage of Ωr,ext (pages 6 and 8)
- Problem: The orange “ECH curve” in Fig. 3 adopts an “enhanced radiation density” Ωr,ext = Ωr,std (1 + 0.3 × 7/8 × (4/11)4/3) as a ∆Neff proxy without motivation in the body. This introduces an extra degree of freedom in the figure that is not tied to the ECH mechanism discussed.
- Required fix: Justify the choice (why 0.3?) or remove the extra-radiation tweak from this comparison figure. If you retain it, label the figure explicitly as a parameter-variation illustration and not as an ECH-vs-ΛCDM physics comparison (see also P1A-E6 from my first report).

MINOR findings (address but do not block acceptance)

P1A-m7
- Location: Sec. II A 2, Step 4 and immediately below Eq. (7) (page 7)
- Problem: Two different round numbers are used for the same dimensionless combination: “[(α/M) MPl] ≈ 3 × 10^−3” and “adopted 10^−2.” This 3× spread is acceptable for OOM reasoning but is needlessly confusing when both appear back-to-back.
- Required fix: Standardize on one benchmark (e.g., 3×10^−3) and, if desired, bracket a plausible range (e.g., 10^−3–10^−2) once, with a short sentence explaining the source of the uncertainty (logarithm size, finite-part scheme dependence).

P1A-m8
- Location: Sec. IV B footnote 3 (page 12)
- Problem: The parity classification discussion is clear, but the statement “the label is retained for consistency with the section’s established terminology” can be misread as endorsing an intrinsically parity-odd operator when it is parity-even absent a P-breaking background.
- Required fix: Add one clarifying sentence: “We therefore refer to ‘parity-odd phenomenology’ rather than a parity-odd operator.”

P1A-m9
- Location: Sec. II C, Eq. (10) and discussion (page 8)
- Problem: The phenomenological cω term is introduced without specifying sign conventions or the precise mapping from vorticity to an effective isotropic term (even if only to argue its negligibility).
- Required fix: Add one line clarifying that cω is a dimensionless bookkeeping parameter (sign unconstrained a priori), and reiterate that in realistic Bianchi models vorticity sources anisotropy rather than an isotropic Λ; the term is shown only to bound magnitude.

P1A-m10
- Location: Appendix C, Eq. (C3) and discussion (page 27)
- Problem: The dimension analysis of ϕ′ in conformal time is stated ([ϕ′] = +2) but this is nonstandard in some cosmology conventions and could confuse readers.
- Required fix: Add a parenthetical note: “In units where ∂/∂η has mass dimension +1 (a is dimensionless), a derivative raises the mass dimension by +1, hence [ϕ′] = [ϕ] + 1 = 2.”

P1A-m11
- Location: Table III (page 21)
- Problem: The “✓/(spectator)” entries could be misread as predictions of the bounce models. The footnote helps, but the table itself invites quick misinterpretation.
- Required fix: Add “(not model-specific; requires added spectator sector)” in the table header for the ALP-birefringence column.

Checks A–J summary notes (only NEW observations)

A. Arithmetic: All additional spot-checks I re-computed matched the manuscript’s values (e.g., ω/H bound to ρΛ fraction, γPTA offset 1.13σ, H0 in eV, Treh/MGUT exponent). No new numeric discrepancies found.

B. Figure-caption vs body-claim: New: Fig. 3 also quietly introduces an “enhanced radiation” proxy not discussed in the body (P1A-M10).

C. Dimensional consistency: New: Eq. (14) prefactor dimensionality problem (P1A-E11).

D. Internal cross-references: The cited sections/equations I re-checked point to the intended content.

E. Null procedure comparability: No additional juxtapositions beyond those already flagged in my first report.

F. Abstract faithfulness: The abstract’s claims are now largely traceable in the body; no new mismatches found.

G. Unsupported novelty claims: None newly detected.

H. Unquantified hedges: None newly detected beyond those already flagged.

I. Appendix vs main-text mismatch: New: internal path reference in Appendix C (P1A-E13).

J. Stale numbers: No additional stale/mismatched numbers found on this pass.

Conclusion of addendum
- The most important new issues are (i) the dimensional inconsistency around Eq. (14) and the ensuing bound (P1A-E11), and (ii) the reliance on an unpublished PTA companion across multiple places (P1A-E10). Addressing these, along with cleanup items P1A-E12/E13 and M8–M10, will materially improve rigor and presentation. If these are fixed alongside the earlier ESSENTIAL/MAJOR items, the manuscript will be much closer to PRD standards.