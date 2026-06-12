# P1A R35conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1a_ech_nogo_v1A.0.64.pdf` md5=03392974 pages=28
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7608 chars)
**Wall time**: 528.6s

---

Referee report for Physical Review D (methods/statistics rigor)

I have read the manuscript in full, including all figures, tables, equations, appendices, and footnotes. Below I list all issues found, classified by severity. For each item I provide an ID, the section and page reference, the specific problem (with a quote where possible), and the required fix.

ESSENTIAL (must be fixed before the paper can be considered further)

P1A-E1 — Sec. IV A, p. 11: Unit conversion and ρNJL estimate are wrong by ~60 orders of magnitude
- Offending text: “A naive order-of-magnitude estimate using post‑recombination baryon densities nψ ∼ O(10^2) cm−3, converted to natural units via ℏc = 1.973 × 10−5 eV·cm (1 cm−3 = (1.973×10−5 eV)^3 ≈ 7.66×10−15 eV^3), … gives ρNJL ∼ nψ^2/MPl^2 ≈ 4 × 10−81 eV^4, i.e. roughly 4 × 10−69 ρΛ.”
- Problem: The conversion 1 cm^-3 = (1.973×10^-5 eV)^3 is incorrect. Using ℏc = 1.97327×10^-5 eV·cm, one has 1 cm^-1 = 1/(ℏc) ≈ 5.0677×10^4 eV, hence 1 cm^-3 = (5.0677×10^4 eV)^3 ≈ 1.30×10^15 eV^3, not 7.66×10^-15 eV^3. Recomputing with nψ = 10^2 cm^-3 gives nψ ≈ 1.30×10^17 eV^3, nψ^2 ≈ 1.69×10^34 eV^6, MPl^2 ≈ 1.49×10^56 eV^2, so ρNJL ≈ 1.1×10^-22 eV^4. Compared to ρΛ ≈ (2.3 meV)^4 ≈ 2.8×10^-11 eV^4, the ratio is ~4×10^-12, not 4×10^-69.
- Required fix: Correct the unit conversion and recompute ρNJL and the ratio ρNJL/ρΛ. If you wish to use a cosmologically relevant mean baryon density (e.g., n_b ~ 2×10^-7 cm^-3 today), recompute that case as well; even then, the conclusion “negligible compared to ρΛ” holds, but the quantitative margin must be correct. Update any subsequent text that quotes or relies on the incorrect 10^-69 figure.

P1A-E2 — Fig. 3 caption and Sec. II C, p. 7–8: Inconsistent “2–3%” H(z) deviation despite Xi tuned to match ρΛ
- Offending text (Fig. 3 caption): “The orange ECH curve uses Ξ set to reproduce ρΛ (i.e. Ξ = ρΛ/M4_Pl = Λeff/M2_Pl ≈ 10−123) … the ∆H/HΛCDM deviation is ∼2–3% across z = 0–3.”
- Problem: If Ξ is set so that the ECH vacuum term exactly equals ρΛ at z=0 and if this term behaves as a constant w = −1 (as claimed), then H(z) should match ΛCDM identically for the same Ωm, ΩΛ, H0. A persistent 2–3% deviation across 0<z<3 is inconsistent with “Ξ set to reproduce ρΛ”. Either there is an additional z-dependence in the ECH energy density (not stated) or the plot/caption is inconsistent with the stated setup.
- Required fix: Either (a) demonstrate analytically why H(z) differs at the percent level despite Ξ reproducing a constant ρΛ (provide the explicit modified Friedmann equation used to generate the orange curve and identify which term produces the deviation), or (b) correct the figure/caption to reflect that H(z) is identical to ΛCDM when Ξ is tuned to ρΛ and cωω^2 is negligible. If numerical artifacts produced the 2–3% difference, remove the claim.

P1A-E3 — Eq. (1), p. 5: Action includes an on-shell T^2 term that the text says is not to be varied
- Offending text: “SECH = (1/16πG) ∫ d^4x e [ e^μ_a e^ν_b R^{ab}_{μν} + (1/γ) ε_{abcd} e^μ_a e^ν_b R^{cd}_{μν} + (1/4) T_{abc}T^{abc} ] + S_matter … The TabcTabc term … is a shorthand … not an independent kinetic term and is not varied independently … so no double counting arises.”
- Problem: Writing SECH with an explicit +¼ T^2 term inside the gravitational bracket while stating it is not varied is methodologically confusing and risks mis-normalization. The standard procedure is to write the EC-Holst + Dirac action without an explicit T^2 term, vary with respect to the connection, solve the Cartan equation algebraically, and only then substitute back to obtain the induced four-fermion contact in the effective action.
- Required fix: Rewrite the action to exclude the on‑shell T^2 term from the varied action. Present the torsion-eliminated effective Lagrangian (four-fermion contact) after varying and integrating out torsion, with clear normalization (e.g., −3κ/16 (J5)^2 modified by γ^2/(γ^2+1) in the Holst case). This removes ambiguity and aligns with EC/Hehl–Datta practice.

P1A-E4 — Versioning and draft-history language in the body
- Offending text:
  - Title block: “(Dated: June 12, 2026 PDT — v1A.0.64)”
  - Sec. X D footnote (p. 19–20): “An earlier version of this manuscript misidentified …”
- Problem: PRD requires a clean scholarly presentation; version tags and draft-history commentary must not appear in the body.
- Required fix: Remove all version identifiers and draft-history prose from the manuscript text, including footnotes; confine any such information to cover letters.

P1A-E5 — Provenance placeholders in Data & Code Availability, p. 24–25
- Offending text: “a Zenodo-archived release (DOI to be inserted at submission) will pin all artifacts …”
- Problem: This is a placeholder; PRD requires reproducibility surfaces to be complete at submission. The current statement fails the provenance test.
- Required fix: Provide the permanent DOI for the archived code/data snapshot that reproduces the exact version submitted, or remove the Zenodo claim and provide a tagged Git commit hash with a date and a guarantee of long-term availability.

P1A-E6 — Dependence on non-public “companion” works for loaded numerical claims
- Offending text (multiple locations): numerical posteriors (H0, ∆Neff), SPHEREx fNL significance, PTA γPTA = 2.567 ± 0.382, NaMaster validation, and MCMC diagnostics are all said to be in “companion works in preparation” or “posted concurrently.”
- Problem: This manuscript must stand alone. Any quantitative claim used to support the argument should be reproducible from content in this paper or from published sources. As written, several load-bearing numbers (e.g., the SPHEREx 2.6–5σ significance) and even a figure annotation (Fig. 1, γPTA) cannot be verified without the companions.
- Required fix: Either (a) remove those quantitative claims from this paper (leave only qualitative statements and references to the literature), or (b) provide sufficient methodological detail (inputs, priors, estimator definitions, masks, binning, covariance models) and numerical artifacts (chains, diagnostics) within this paper to reproduce them independently. For figure annotations (e.g., γPTA in Fig. 1), either replace with a citation to published results or remove.

P1A-E7 — Ambiguous notation in Eq. (4), p. 6
- Offending text: “Lint = − (3πGN/2) × γ^2/(γ^2 + 1) × J5μ J5^μ”
- Problem: The symbol “GN” appears only here; elsewhere the paper uses G for Newton’s constant. It’s unclear whether “GN” is G_N (Newton’s constant) or G×N (with N undefined). In Sec. IV A, the coefficient is given as −3κ/16, consistent with −3πG/2, i.e., no extra factor.
- Required fix: Standardize the Newton’s constant symbol throughout (e.g., G_N) and clarify that Eq. (4) reads −(3π G_N/2) × γ^2/(γ^2 + 1) × J5·J5. Remove any ambiguity about an extra “N” factor.

MAJOR (significant revisions needed)

P1A-M1 — Mixed dimensionless ratios in Route-2 estimate, Sec. IV B, p. 11–12
- Offending text: “We adopt this contraction as the canonical Route‑2 estimate … we conservatively allow up to two orders of magnitude … an alternative ordering … yields a numerically distinct ∼ 10−33 ratio. The canonical-bound conclusion … is robust to this choice.”
- Problem: Presenting two different normalizations (10^-60 vs 10^-33) without a clear, explicit dimensional reduction path risks confusion and undermines reproducibility. Only a single, consistent, dimensionless mapping should be presented.
- Required fix: Provide one explicit, fully dimensionally consistent derivation of the dimensionless ratio ∆θ_one-loop/∆θ_obs, specifying all factors (including H0/MPl, α/M in GeV^-1→eV^-1, etc.). Remove the “alternative ordering” unless it is shown to be algebraically equivalent.

P1A-M2 — Fig. 5 (top) “Renormalization Group Running of α/M” is schematic without a stated β-function
- Offending text: “Renormalization-group running of the parity-odd coupling α/M … anchored at the primordial benchmark …”
- Problem: The figure appears quantitative but no β-function or integration path is given; the y-axis units/scale are unspecified beyond α/M (GeV^-1). This risks being misleading.
- Required fix: Either (a) provide the explicit β-function used, the initial condition, and the integration details to generate the curve, or (b) clearly label the panel as “schematic,” remove the numerical axes (or provide uncertainty bands), and ensure it is not read as a quantitative prediction.

P1A-M3 — Forecast claims without sufficient declared methodology, Sec. VII and Fig. 4/Fig. 6
- Offending text: “SPHEREx … will test fNL = −35/8 at 2.6–5σ realistic significance (footnote 6) … GR-projection, bφ uncertainty, photo-z marginalization …”
- Problem: A detection-significance claim in this paper requires pre-declared estimator(s), survey area, n(z), bias models, covariance, binning, and systematic model — or it must be removed and deferred to the cited forecast. The current footnote is not sufficient for a PRD methods standard.
- Required fix: Either (a) remove the 2.6–5σ claim and retain only a qualitative statement with a reference to Heinrich et al. (2024) and your companion forecast, or (b) provide the full Fisher setup sufficient for an independent reader to reproduce σ(fNL), including assumed target redshift bins, number densities, biases, shot noise, and all degradation factors.

P1A-M4 — Inconsistent summary of SPHEREx σ(fNL) across the paper
- Offending text: Table I notes “σ(fNL)≈0.7 — detailed Fisher forecast in companion work,” elsewhere you state “σ(fNL) ≈ 1.0 after GR-projection and photo-z marginalization,” and Fig. 6/footnote 6 combine these differently.
- Problem: These numerical statements need to be made consistent, tied to a single set of assumptions, or clearly labeled as coming from different steps and not directly comparable.
- Required fix: Consolidate to one consistent forecast figure with clear assumptions, or relegate all numerical values to the dedicated forecast paper and keep only a qualitative statement here.

P1A-M5 — Use of γPTA = 2.567 ± 0.382 (Fig. 1 caption, Sec. X G) without an external, citable source
- Problem: You annotate a key plot with a numerical result that is not documented in this manuscript or a peer‑reviewed source; the “companion Paper III” is not available to a reader.
- Required fix: Either remove the γPTA annotation from Fig. 1 or replace it with a number and citation from a published analysis. If you retain your value, provide a concise methods appendix sufficient to reproduce it (data selection, priors, likelihood, sampler settings, convergence).

P1A-M6 — Clarity on the coefficient in Eq. (7), Sec. II A 2, p. 6–7
- Offending text: “the one-loop estimate is α/M ∼ g^2/(32π^2) γ/M ln(ΛUV^2/µ^2) + δNY, motivating … [(α/M) MPl] ∼ 10^-2.”
- Problem: The finite part δNY is left completely unspecified, yet later numerical benchmarks use [(α/M)MPl]~10^-2. For PRD-level rigor, an uncertainty range reflecting scheme dependence should be shown, or subsequent usages should be cast explicitly as benchmark fits rather than predictions.
- Required fix: State an uncertainty band for [(α/M)MPl] implied by plausible δNY ranges (or explicitly state it is a fitted parameter throughout and not used in any prediction). Ensure later quantitative statements reflect this.

MINOR (address but does not block publication)

P1A-n1 — Typographical/orthographic issues
- Instances: “Domaga la–Lewandowski” (with an extra space), “R ∧ Re” sometimes written with/without tilde for the dual, mixed use of cal F vs F for curvature and electromagnetic field strength.
- Required fix: Standardize names and notation; use R ∧ R̃ for Pontryagin consistently; reserve calligraphic F for gravitational curvature and Fμν for electromagnetism, and state this clearly at first use.

P1A-n2 — Clarify cωω^2 bookkeeping (Fig. 3 caption), p. 7
- Offending text: “dividing by 3ΩΛ ≈ 2.1 gives ∼1.2×10−21 of ρobsΛ”
- Problem: The mapping from a vorticity bound (ω/H)_0 to a contribution to ρΛ is non-obvious and mixes Λ-units (mass^2) and energy density (mass^4). The present text compresses several steps.
- Required fix: Add a one-line derivation showing how the dimensionless (ω/H)_0^2 bound limits an effective Λ contribution and how that translates to a fraction of ρΛ, explicitly noting units.

P1A-n3 — Overuse of “earlier drafts” and “we emphasize” wording
- Required fix: Remove remaining meta-comments and streamline prose to declarative, impersonal style.

NIT (cosmetic)

P1A-N1 — PACS numbers (p. 2) are not needed by PRD (no action required, but consider removing per journal style).
P1A-N2 — Repeated explanatory parentheticals could be tightened for length.

Additional targeted checks requested in the round metadata

- NJL passage: Although the qualitative closure (amplitude negligible; parity‑even) is fine, the quantitative estimate is dimensionally incorrect (see P1A-E1). This must be corrected.
- Fig. 3 caption: The identification “Ξ = ρΛ/M^4_Pl = Λeff/M^2_Pl ≈ 10^-123” is physically correct. However, the co-appearing “2–3%” H(z) deviation is inconsistent if Ξ really reproduces ρΛ and cωω^2 is negligible (see P1A-E2); fix or explain.

Other numerical/dimensional spot-checks (pass)

- Eq. (9): ρcrit formula and 0.27–0.41 ρPl values are numerically consistent with γ = 0.274 vs 0.2375.
- Route-2 amplitude ratio, Eq. (15): Using αem/(4π) ≈ 5.8×10^-4, H0/MPl ~ 1×10^-61, MPl (α/M) ≈ 10^-2, βobs ≈ 6×10^-3, yields ~10^-60, as quoted.
- Route-4 energy density from β (Eq. 17): With α/M = 10^-21 GeV^-1 = 10^-30 eV^-1, mθ ≈ 1.5×10^-33 eV, β ≈ 6×10^-3, one gets ρθ ≈ 1.6×10^-10 eV^4 ≈ 6 ρΛ; matches the text.
- Appendix C rotation formula β = (α/2M) ∆ϕ is dimensionally and derivationally consistent.

Stand‑alone reader test

The central “channel‑level closure” arguments for R1–R4 can, in principle, stand without the companions (once the NJL unit error is fixed). However, all quantitative forecast/detection claims (SPHEREx, LiteBIRD significance graphics, PTA γPTA) currently rely on non-public companions; please either remove or fully document these elements in this manuscript to meet PRD’s stand‑alone standard.

Length

At 28 pages, the paper is long for the net new contribution (a structured no‑go, with many caveats/ansätze). If the authors remove the forecast/companion-dependent material and draft‑history commentary and tighten the prose around the core closures and the perturbation‑transparency result, the paper could be reduced to ~18–20 pages without loss of content.

## Summary recommendation
MAJOR REVISIONS

The manuscript makes a careful channel-level no-go assessment with many explicit caveats; the perturbation-transparency result is clearly stated. However, there are critical methodological issues: a severe unit-conversion error in the NJL energy-density estimate; an internal inconsistency in Fig. 3’s captioned H(z) deviation; inclusion of an on-shell T^2 term in the varied action; reliance on non-public companion works for quantitative annotations; and draft-history/version tags in the text. Once these essential and major issues are corrected — with clean, dimensionally consistent calculations and a fully stand-alone presentation — the paper can be reassessed.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS AFTER SECOND PASS (A–J audit)

P1A-E8 — Sec. IV B, p. 12 (Eq. 14): Dimensional inconsistency in the one-loop operator
- Offending text: “Γparity-oddone-loop = − (1/16π^2) β(γ)/MPl ∫√−g ∂μϑNY J5μ”
- Problem: If ϑNY is a pseudoscalar angle (dimension 0), then [∂μϑNY] = +1 and [J5μ] = +3, so [∂μϑNY J5μ] = +4. The coefficient must therefore be dimensionless. The explicit 1/MPl factor makes the Lagrangian density dimension +3. If instead ϑNY is a canonical dimension-1 field, this must be stated and carried consistently through Eq. (15). As written the normalization is dimensionally inconsistent.
- Required fix: Choose one consistent convention and propagate it: (a) take ϑNY dimensionless and drop 1/MPl (recompute Eq. 15), or (b) define ϑNY canonically with [ϑNY] = +1 and keep 1/MPl, stating this explicitly and adjusting subsequent mappings accordingly. In either case, give one fully consistent path to the dimensionless ratio in Eq. (15) and update the numerical value if it changes.

P1A-E9 — Sec. II A 1 (p. 6–7) and Table IV (p. 26): Incorrect “∼0.020” scheme spread for γ
- Offending text: “the ∼0.020 figure … is the spread between counting prescriptions” and Table IV “γ … (scheme range ∼0.020)”.
- Problem: Using the numbers given, γSU(2) ≈ 0.274 and γDLM ≈ 0.2375 differ by 0.0365, not ∼0.020. The U(1) counting quoted (≈0.127) implies an even larger spread.
- Required fix: Correct the stated scheme spread (e.g., “∼0.037 between SU(2) and DLM”; “∼0.147 between SU(2) and U(1)”), or present a justified narrower interval if you are restricting to a specific pair of schemes. Update Table IV accordingly.

P1A-E10 — Sec. XII A, p. 20–21: Sign error in the “residual 10^5” sensitivity statement
- Offending text: “the residual 10^5 tracks the exponential e−3ΔNtot for ΔNtot ≈ 4 e-folds”
- Problem: e−3ΔN with ΔN ≈ 4 is ≈ 6×10−6, not 10^5. The claimed 10^5 sensitivity corresponds to e+3ΔN.
- Required fix: Replace “e−3ΔN” with “e+3ΔN” (or explicitly say “a ±ΔN ≈ 4 shift rescales the amplitude by e±3ΔN ≈ 10^±5”). Ensure consistency anywhere else this sensitivity is cited.

P1A-M7 — Figs. 4 and 6 captions vs body: Unintroduced correlation parameter ρ and missing curves
- Offending text (Fig. 6 caption): “the significance tracks duplicate the ρ = 0 combination of Fig. 4; … Fig. 4 additionally shows the correlated (ρ = 0.3, 0.5) combinations…”
- Problem: The main text never defines ρ (correlation between which estimators/datasets?), and Fig. 4 as reproduced does not visibly annotate ρ-curves or a legend explaining them.
- Required fix: Define ρ explicitly in the main text and both captions, show the ρ = 0.3 and 0.5 curves/markers in Fig. 4 with a legend, or remove these statements if such curves are not actually plotted.

P1A-M8 — Sec. II C 1, p. 8–9: Incorrect phrasing about “cube of the fermion bilinear”
- Offending text: “the cube of the fermion bilinear scales as the cube of the fermion number density …”
- Problem: The axial current J5μ is a fermion bilinear whose coherent mean scales ∝ nψ, not “the cube of the bilinear.” The a−3 factor follows from number density dilution, not from any cubic of a bilinear.
- Required fix: Rewrite to state plainly that ⟨J5μ⟩ ∝ nψ and therefore dilutes as a−3 during expansion. Remove references to “cube of the bilinear.”

P1A-M9 — Sec. V (p. 14–15) and Sec. III B (p. 10): Undeclared meaning and construction of “pLEE”
- Offending text: “hemisphere null at pLEE < 10−4”
- Problem: “LEE” (look-elsewhere effect) is not defined, and the null-procedure used to obtain pLEE (trial factor, search domain, resampling scheme) is not documented in this manuscript.
- Required fix: Define pLEE, specify the search over which the LEE correction was applied, and describe the null generation used (randomizations, masks, number of trials). Alternatively, remove the p-value and defer to the companion with only a qualitative null statement here.

P1A-M10 — Sec. IV B footnote 3 (p. 12) and Eq. (15): Unspecified anomaly-bridge details in Route-2 β estimate
- Offending text: “mapping … uses the standard chiral-anomaly ∂μJ5μ ⊃ (αem/4π) F F̃ chain at the EFT level. We treat the resulting β estimate strictly as an amplitude-budget bound…”
- Problem: Eq. (15) depends on how ∂μJ5μ is integrated along the line of sight (background evolution, boundary terms), yet no explicit mapping or approximations are given. As presented, this is an unquantified chain.
- Required fix: Add a short derivation or cite a standard reference that shows how the anomaly term feeds into a net β with the exact normalization used (or remove the quantitative use of this chain here and keep only the qualitative “loop- and MPl-suppressed” conclusion).

P1A-n4 — Notation collisions for β and γ
- Offending text: β used for birefringence angle and RG β-function; γ used for Barbero–Immirzi parameter and PTA spectral index γPTA.
- Problem: Although you note some distinctions in-text, multiple collisions remain and can confuse readers.
- Required fix: Adopt unambiguous symbols globally (e.g., βCB for birefringence, βRG for RG; γBI for Barbero–Immirzi, γPTA retained with explicit subscript) and enforce consistently across figures, captions, and text.

P1A-n5 — Sec. II A 2, Eq. (7), p. 6–7: δNY dimensionality and range unspecified
- Offending text: “+ δNY” with no units or magnitude range
- Problem: α/M has dimension (mass)−1, so δNY must carry the same; the text reads as if δNY were a dimensionless finite part. This ambiguity propagates to the benchmark [(α/M)MPl] ≈ 10−2 uses.
- Required fix: State the units of δNY, its expected magnitude/range under known regularization schemes, and how it propagates into the numerical benchmark used later; or rephrase to treat α/M strictly as a fitted parameter wherever it appears in quantitative estimates.

P1A-n6 — Appendix C, p. 25–26: Inconsistent normalization of Kμ vs its divergence
- Offending text: “Kμ ≡ εμνρσ Aν Fρσ … ∂μKμ = 1/2 F F̃”
- Problem: With Kμ ≡ εμνρσ Aν Fρσ, one indeed gets ∂·K = 1/2 F F̃. Many readers expect a 1/2 in the definition. The mismatch between common conventions and yours may confuse.
- Required fix: Either define Kμ with the 1/2 and keep ∂·K = F F̃, or retain your current Kμ and explicitly show the identity ∂μ(εA F) = 1/2 F F̃ in a one-line calculation or footnote.

P1A-n7 — Table IV (p. 26): “γ scheme range ∼0.020”
- Problem: Duplicates P1A-E9 at the table level; please correct the numeric value(s) or annotate the restricted scheme pair to which the “∼0.020” refers.

P1A-n8 — Figs. 4 and 6 captions: Undefined ρ parameter
- Offending text: “ρ = 0 combination” and “correlated (ρ = 0.3, 0.5)”
- Problem: ρ is not defined anywhere in the main text or captions.
- Required fix: Define ρ clearly (e.g., cross-correlation coefficient between probes assumed in the joint detection forecast) and, if used, give the assumed values in the body text; otherwise remove ρ from the captions.

P1A-n9 — Abstract vs body: “13 logically-independent constraints” not made testable
- Offending text (Abstract and Sec. IX): “13 logically‑independent mechanism‑class constraints”
- Problem: The body lists the barriers but does not provide a dependency matrix or other device that lets a reader verify logical independence (beyond the statement that B8 is subsumed by B14).
- Required fix: Add a small table or DAG indicating which assumptions each barrier depends on and where they overlap, or soften to “catalogue of 14 constraints, 13 of which are treated as independent here.”

NO repeats of previously flagged issues appear above; these are additional to P1A-E1…M6, n1…n3.