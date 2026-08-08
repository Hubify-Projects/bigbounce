# P1A R53 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/private/tmp/R53_P1A/paper1a_ech_nogo.pdf` md5=1996d408 pages=29
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (8283 chars)
**Wall time**: 444.5s

---

Referee report for: “Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter”

Scope of review
- Methodology rigor: derivation chains, dimensional analysis, internal arithmetic consistency, statistical validity, error propagation, and reproducibility.
- I read all 29 pages, tables, figures, equations, footnotes, and appendices provided in the PDF text above and recomputed/checked the stated numerical results where possible.

General assessment
The manuscript advances a “channel-level” no-go for four minimal ECH dark-energy routes and presents a “perturbation transparency” statement (Holst sector inert for scalar/tensor perturbations). While many caveats are explicitly stated, a number of load-bearing elements (data-based claims, forecasts, MCMC numbers, and PTA re-analyses) rely on “in preparation” companion papers, and several quantitative conclusions rest on ad hoc scaling ansätze that are not derived within the manuscript. As it stands, the paper is not self-contained to PRD standards. Below I enumerate issues in the required format.

Findings

ESSENTIAL

P1A-E1 (Abstract; pp. 1–3; Secs. III, V, VI, X G; Table I; Table IV; Figs. 1, 4, 7)
Problem: Load-bearing results depend on “in preparation” companion papers and are not reproducible or fully specified here. Examples:
- Galaxy-spin “confirmed null” and dipole significance rely on Paper IV [23] (Sec. III B; Sec. V), with no quantitative summary (catalog size, sky mask, dipole amplitude, p-values, control tests) provided in this manuscript.
- ΛCDM+ΔNeff MCMC values (e.g., H0 = 67.68 ± 1.06, ΔNeff ≈ 0; Table I, Appendix A, Sec. III B) taken from Paper I(b) “in preparation”; the methods and dataset combinations are not detailed here.
- PTA real-KDE GPU-MCMC “γPTA = 2.567 ± 0.382” (Sec. X G; Fig. 1 annotation; Table IV) relies on Paper III [46], with no analysis in this paper.
- SPHEREx Fisher forecast (2.6–5σ) and multi-tracer details are deferred to Paper II [2] yet used in Figs. 4 and 7 captions and Table I footnote b.
Required fix: Make the paper fully standalone. Either:
(a) remove all results, claims, and figures that depend on the unpublished companions (including galaxy-spin null, MCMC posteriors, γPTA result, and the SPHEREx/LiteBIRD forecast curves and joint-significance lines), or
(b) incorporate full methods, data descriptions, estimators, covariances, masks, pipeline validation, and numerical results for these elements directly in this manuscript (including reproducible details and uncertainties), with code/data archived by DOI (see P1A-E3).

P1A-E2 (Sec. IV B, Eq. (15), p. 12–13)
Problem: Route-2 one-loop “amplitude budget” for birefringence mixes parameters from a different route (uses the R4-fitted α/M and βobs in a ratio for the R2-induced rotation), without a clean derivation from the displayed operator Γone-loop ∝ (β(γ)/MPl) ∫√−g ∂μϑNY J5μ. The reduction to a dimensionless ∆θone−loop/∆θobs formula is not shown step-by-step; as written it is not obvious that the units are consistent, and the appearance of MPl(α/M)βobs in the denominator is not transparent from Eq. (14). This ratio underpins the claim of ~10^−60 suppression closing Route 2.
Required fix: Provide a complete derivation of the expected birefringence angle induced by Eq. (14) (including the anomaly chain ∂μJ5μ ⊃ (αem/4π) F F̃, the cosmological background for ϑNY, time integral, and all prefactors) leading to a manifestly dimensionless expression. State explicitly all assumptions and numerical inputs (H0, ∂ηϑNY scale, redshift range, etc.), and show the units at each step. Alternatively, if you intend only to provide a parametric bound, remove Eq. (15) and restate the closure as an inequality with clearly justified constants; do not mix R4’s α/M and βobs into the R2 estimate unless the logical chain is explicitly derived.

P1A-E3 (Data and Code Availability; p. 26)
Problem: Reproducibility is stated via a GitHub “main” link with a future intention to archive on Zenodo. There is no frozen DOI, version tag, or commit hash documented for the artifacts backing the present manuscript. Companion-paper artifacts are referred to but not archived here.
Required fix: Provide a permanent, citable archived release (e.g., Zenodo DOI) that pins the exact code, configurations, and data artifacts used for this submission. Include the exact commit hash, environment (compiler, package versions), and a step-by-step reproduction guide. If “frozen MCMC chains” are included, give their file names, provenance, and checksums. This is required for verification at PRD.

P1A-E4 (Figs. 4 and 7 captions and corresponding text; pp. 16, 23)
Problem: Forecast detection significances (2.6–5σ for SPHEREx, ~9σ for LiteBIRD) and the “combined” joint-significance curves with an assumed inter-estimator correlation ρ are presented without a declared estimator, covariance, binning, or Fisher setup in this manuscript. They rely on an unpublished companion forecast. This fails the pre-declaration and standalone-reader tests.
Required fix: Either remove these forecast significance curves and the explicit 2.6–5σ and 9σ numbers from this paper, or include the full Fisher/likelihood setup, templates (including template overlap calculations), survey specifications (fsky, redshift bins, number densities), all degradation factors (GR-projection, bφ uncertainty, photo-z), and the formulae used to combine significance across probes with correlation ρ, plus a validation example.

P1A-E5 (Sec. III B; Sec. V; p. 10, 15)
Problem: “Galaxy spin asymmetry: A confirmed null” is asserted, but this paper provides no quantitative result beyond “N ≈ 9.5 × 10^5 high-confidence spirals,” no measured dipole amplitude, masks, classifier performance metrics, selection function controls, or p-values. The claim rests entirely on Paper IV [23].
Required fix: Either (a) remove the “confirmed null” claim from this paper and defer to the separate publication, or (b) provide a self-contained quantitative summary here: catalog construction, train/val/test performance, sky mask, dipole estimator, null simulations, bias audits, measured dipole amplitude and its uncertainty, and the look-elsewhere corrected p-value.

P1A-E6 (Table I, Appendix A; Sec. III; throughout)
Problem: MCMC cosmological parameters (e.g., H0, σ8, ΔNeff) are quoted from an internal analysis “in preparation” [6]. They are used to support statements like “recovers ΛCDM” and appear in Fig. 3 choices. This is not verifiable in this paper.
Required fix: Remove these parameter results from the present manuscript unless you include a full description of the MCMC setup (data sets, priors, likelihoods, CAMB settings, chain lengths, convergence diagnostics, and posterior tables) here. If retained, archive the chains with a DOI and document the exact inputs.

P1A-E7 (Sec. IV D; Eq. (17); p. 13–14)
Problem: The conversion from βobs to an inferred ρθ (leading to “ρθ ≈ 1.6×10^−10 eV^4 ≈ 6 ρΛ when mθ = H0”) is shown as a single number. There is no propagation of observational uncertainty (β = 0.342° ± 0.094°) nor of mθ uncertainty, nor any systematic on α/M. This is used to argue a “naturalness” closure of Route 4.
Required fix: Provide the error propagation: give ρθ(β, mθ, α/M) with uncertainties, and show the range implied by βobs ± σ and by the assumed mθ prior (e.g., mθ ~ H0 vs natural ALP band). Present the numerical band (and state the unit conversions explicitly: 10^−21 GeV^−1 = 10^−30 eV^−1, etc.). The central estimate 6 ρΛ is correct by my recomputation, but the uncertainty band must be shown if used to close a route on “explanatory deficit.”

P1A-E8 (Abstract; p. 1–2; Sec. IV E)
Problem: The abstract states that 14 constraints “collectively constrain the enumerated channels,” and later “the central result is a perturbation-transparency result.” Several barriers (e.g., B9 “Liouville conservation,” B12 “Vacuum amplification ceiling”) are explicitly heuristic/ansatz-level in the body, yet the abstract reads as if all 14 are established on equal footing. This is stronger than the body’s caveats.
Required fix: Calibrate the abstract language to match the body. Explicitly mark which closures are theorem-level (perturbation-transparency for canonical scalar matter) vs. ansatz-level amplitude budgets vs. heuristic scenario constraints. Provide a one-line pointer (e.g., “Route-2 and -3 closures are amplitude-level under the stated EFT scaling ansätze”) in the abstract.

P1A-E9 (Eq. (1) and surrounding footnote; p. 5–6)
Problem: The displayed action includes a + 1/4 TabcTabc term under the overall 1/(16πG) prefactor, with a long footnote explaining it is a “Hehl–Datta shorthand” and not independently varied. As written, the action is mathematically inconsistent: adding T^2 and then varying the connection typically double-counts unless the term is removed prior to variation.
Required fix: Rewrite the action to avoid inconsistency. Present the standard EC/Holst+Dirac action without an explicit T^2 term, perform the variation, and then show the resulting four-fermion contact term (Eq. (4)) upon algebraic elimination. Alternatively, present an on-shell effective action after elimination, but do not mix the two in the same functional.

MAJOR

P1A-M1 (Figs. 4 and 7; pp. 16, 23)
Problem: The SPHEREx “2.6–5σ realistic” headline combines multiple degradation factors (template-overlap r ≈ 0.84, GR-projection, bϕ, photo-z), but the arithmetic is not shown. For example, |fNL|/σ = 4.375 if σ = 1.0; a 20% amplitude degradation would give ~3.5σ; achieving 2.6σ requires additional quantified factors. This violates transparency of the combination.
Required fix: Provide a simple tabulation of the multiplicative degradations and the resulting final σ (or remove the explicit 2.6–5σ range from this paper and defer to the companion).

P1A-M2 (Sec. II C; Fig. 3 caption; p. 8)
Problem: The lower panel shows ∆H/HΛCDM ≈ 2–3% across z = 0–3. This appears driven by different parameter choices (H0 = 69.2 vs 67.36 km/s/Mpc; Ωm differences), not by the ECH mechanism per se (Ξ was tuned to match ρΛ). The caption risks implying the ECH model predicts a 2–3% deviation.
Required fix: Clarify in the caption/body that the plotted ∆H/H arises from the chosen parameter pair, not a model-driven deviation once Ξ is set to ρΛ. Provide a same-parameter overlay to show the pure Ξ-term equivalence (i.e., identical background expansion when Λeff is matched).

P1A-M3 (Sec. IX M; Eq. (20); p. 19)
Problem: Barrier 12 “Vacuum Amplification Ceiling” states ΩGW|bounce ≲ (ρcrit/ρPl)^2 ≃ 0.07–0.17 as a ceiling “ansatz,” used to close a mechanism class. No derivation or reference is provided.
Required fix: Either provide a derivation or literature reference for the stated scaling, or demote this to a non-load-bearing observation. If it is not used to close any channel independently (as claimed later), remove the number or label it explicitly as a heuristic placeholder without quantitative force.

P1A-M4 (Throughout; e.g., Sec. IV D footnote 5; Appendix C; p. 14, 27–28)
Problem: Conventions and normalizations for the ALP–photon coupling switch between α/M and gaγ with nonstandard normalizations (−1/4 vs 1/(2π), etc.). While you include an extensive footnote, the mapping is still opaque to a reader who wants to reproduce β numerically.
Required fix: Add a short, self-contained convention block near Eq. (17): explicitly define gaγ, fa, cγ, and show α/M ↔ gaγ conversion and units. Provide one worked numerical example of β from ∆θ using your exact operators and conventions.

P1A-M5 (Sec. II A 2; Eq. (7); p. 6–7)
Problem: The one-loop estimate (α/M) numerics are stated qualitatively. The recomputation is consistent ([(α/M)MPl] ≈ 3×10^−3), but the intermediate constants (32π^2, ln(Λ^2/µ^2), M = MPl/√γ) should be presented more explicitly for verification.
Required fix: Show the numeric steps explicitly (values for g^2/(32π^2), γ, M, ln…), and state the renormalization-scheme dependence of δNY. This can be an inline computation or a short appendix line.

P1A-M6 (Sec. X B–D; p. 20–21)
Problem: The “perturbation-transparency” result is stated as a general theorem for canonical scalar matter with a sketch using the algebraic Bianchi identity. This is fine, but you should include a one-line proof of εμνρσ Rμνρσ(ΓLC) = 0 from Rμ[νρσ] = 0 (explicitly showing the 3-index antisymmetrization contraction) to make the “pointwise zero” claim watertight.
Required fix: Add the explicit contraction argument (or a reference) confirming εμνρσ Rμνρσ = 0 for torsionless connections, to support the “pointwise” statement (not merely a total derivative).

P1A-M7 (Sec. II A 2; p. 7)
Problem: Definition of M = Marea-gap ∼ MPl/√γ is used repeatedly. The constant of proportionality (from ∆ = 4√3 π γ ℓP^2) is omitted. Since M enters α/M numerics, the constant matters at the factor-of-few level.
Required fix: Give the exact mapping M ≡ 1/√∆ with ∆ = 4√3 π γ ℓP^2 (or whichever convention you use) and state the resulting numerical M in GeV for γ = 0.274. Propagate this into the order-of-magnitude for (α/M)MPl.

P1A-M8 (Various; e.g., Sec. II C; Sec. XII A; p. 8–9, 21–22)
Problem: Several “order-of-magnitude” constructs (e.g., Dinf prefactor (Treh/MGUT)3/2) are acknowledged as ansätze. However, they are then used to obtain a specific value Ntot ≈ 92. The ~2% offset to 94 is later discussed, but the status of the 92 vs 94 number remains ambiguous.
Required fix: Add a single consolidated paragraph in Sec. XII A that lists the assumed inputs and the range they imply for Ntot (e.g., α/M uncertainty, Treh/MGUT band), and state clearly that 92 is an O(1) e-fold estimate with ±2 e-fold systematic. Remove any language that might be read as a precision prediction.

MINOR

P1A-m1 (Sec. IV A; p. 11–12)
Problem: The “mean-field amplitude” estimate for the NJL term uses nψ ≈ 10^2 cm^−3 as a “post-recombination baryon density,” which substantially exceeds the cosmic mean today (~2×10^−7 cm^−3). It does not affect the suppression conclusion (it strengthens it), but it is a misleading reference point.
Required fix: Replace the example with a realistic mean baryon number density and optionally add a high-density ISM example to emphasize the suppression end-to-end.

P1A-m2 (Fig. 1 & caption; p. 5)
Problem: The figure annotates “PTA γPTA = 2.567 ± 0.382 (Sec. X G)” but, as noted in P1A-E1, this is not derived here.
Required fix: Remove this annotation from Fig. 1 or mark it clearly as “external (Paper III, in preparation)” and non-load-bearing.

P1A-m3 (Throughout)
Problem: Mixed use of γ and γBI; use of “Domaga la” with a space; inconsistent hyphenation; minor grammatical duplications in long footnotes (e.g., “explicitly, the displayed … is not an independent kinetic term but … shorthand” repeated).
Required fix: Standardize γ → γBI where needed, correct author names to standard spellings, and streamline repeated sentences in footnotes.

P1A-m4 (PACS numbers; p. 2)
Problem: PACS numbers are deprecated in PRD formatting.
Required fix: Remove PACS or replace with current keywords as per PRD guidelines.

P1A-m5 (Sec. II C; p. 8)
Problem: The rotation-energy cω ω^2 term: the “≤ 10^−21 ρΛ” estimate is stated without showing the conversion.
Required fix: Provide the conversion used to go from (ω/H)^2 < 2.5×10^−21 to a bound on ρrotation/ρΛ (one line is sufficient).

NIT

P1A-n1 (Table I footnote b; p. 4)
Problem: Refers to “footnote at the abstract-level 2.6–5σ quote,” i.e., internal cross-reference to the abstract.
Required fix: Reword footnote b to be self-contained; avoid referring to “abstract-level” notes.

P1A-n2 (Typography)
Problem: Some long em-dash constructions and formula punctuation make sentences hard to parse.
Required fix: Light copy-edit for readability.

Arithmetic and dimensional cross-checks performed
- [(α/M)MPl] ~ 10^−2 used repeatedly: numerically consistent with Eq. (7) upper-bound estimate when using MPl unreduced and ln(ΛUV/µ) ≈ 74.
- Dinf ~ e^−3Ntot × (Treh/MGUT)3/2: with Treh = 10^15 GeV, MGUT = 10^16 GeV, the prefactor is 0.0316; matching Ξ ≈ 10^−123 gives Ntot ≈ 92, consistent with the manuscript’s number.
- R4 “overshoot” check: ρθ = 2 mθ^2 β^2/(α/M)^2 with α/M = 10^−21 GeV^−1 = 10^−30 eV^−1, mθ = 1.5×10^−33 eV, β = 0.342° = 5.97×10^−3 rad gives ρθ ≈ 1.6×10^−10 eV^4 ≈ 6 ρΛ; arithmetic consistent.
- e^(Ntot−Nexit) with Ntot − Nexit ≈ 32 ⇒ e^32 ≈ 7.9×10^13: consistent with text.
- Holst-dual vanishing on T = 0 via algebraic Bianchi: correct (but include an explicit contraction line as requested).
- LQC ρcrit(γSU(2)=0.274) ≈ 0.27 ρPl derived from the quoted scaling ρcrit ∝ 1/γ^3: consistent.

Overclaim/scope alignment check
- The abstract generally carries caveats (e.g., “channel-level assessment”). However, see P1A-E8: ensure the non-theorem barriers are not presented as on par with the perturbation-transparency result.

Length/productivity
- The paper is long (29 pages) relative to the core proven contribution (the perturbation transparency theorem plus qualitative channel closures). A leaner manuscript focusing on the theorem, with a concise, fully self-contained channel-closure discussion (and removal of companion-dependent material), could be ~18–22 pages. See P1A-E1/E4 for content to remove or relocate.

## Summary recommendation
MAJOR REVISIONS

The manuscript contains potentially valuable theoretical clarifications (especially the perturbation-transparency result), but it currently fails PRD’s methodological and reproducibility standards due to reliance on unpublished companion works for load-bearing claims, an incomplete/opaque derivation for the Route-2 amplitude suppression, and inclusion of forecast significance figures without declared estimators or covariances. The essential fixes above must be addressed to make the paper self-contained, with transparent derivations and archived artifacts. Once these are met and the overreach in the abstract is calibrated, the manuscript could be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh pass)

ESSENTIAL

P1A-E10 (Appendix C; final paragraph and footnote 8)
Problem: Appendix C’s convention closure explicitly references an external “companion’s §VI8” to justify the β mapping normalization. A self-contained derivation is required in this manuscript. Cross-referencing an unpublished companion section leaves the normalization unverifiable here.
Required fix: Remove the external cross-reference and provide a self-contained convention block and worked example (see also P1A-M4 in your first report). State the exact mapping from your −1/4 (α/M) ϕ FF̃ operator to gaγ, with units, and reproduce β = (α/2M)Δϕ numerically for one parameter point inside this paper.

P1A-E11 (Abstract; Sec. XIV D)
Problem: The abstract says the matter-bounce fNL signal is “definitively erased” by Ntot ≈ 92 e-folds. The body provides only a scale-tracking argument (kphys,bounce ∼ eNtot−Nexit kphys,obs) without a quantitative transfer-function suppression or bispectrum amplitude calculation. “Definitive” overstates what is shown.
Required fix: Calibrate the abstract (and Sec. XIV D) to “expected to be erased under standard assumptions” or provide an explicit suppression factor calculation (or a rigorous bound) through the four-epoch transfer function demonstrating a decisive depletion at SPHEREx scales.

MAJOR

P1A-M9 (Fig. 5, top panel; caption p. 18; Sec. II A 2)
Problem: “Renormalization Group Running of α/M” is plotted as a smooth monotonic curve from “Present” to MPl, but no β-function for α/M is given in the text, and no scheme or thresholds are specified. As drawn, it looks like a computed result rather than a schematic. This risks implying a derived running that is not provided.
Required fix: Either replace the panel with a clearly labeled schematic (no axes ticks or values; “illustrative only”), or supply the explicit RG equation, thresholds, and inputs used to generate the curve (or remove the plot).

P1A-M10 (Barrier C: “Scalar-Tensor Universality”; Sec. IX C)
Problem: The claim that “torsion fluctuation couples to curvature invariants in the same manner as any other scalar, with no additional ECH-specific observable” is asserted without a derivation or citation in the FRW background. This is load-bearing for dismissing distinct ECH observables near the bounce.
Required fix: Provide a derivation (or formal reference) showing the most general diffeo-invariant quadratic action for scalar and torsion perturbations on FRW reduces to the standard scalar-tensor form (with torsion eliminated or recast), or rephrase as a conjecture/ansatz rather than a barrier-level statement.

P1A-M11 (F vs F: curvature vs electromagnetism; Eq. (6), Sec. II A 2; Sec. IV D)
Problem: The manuscript alternates between calligraphic F (curvature two-form) and plain F for both gravitational curvature and the electromagnetic field strength. In Eq. (6) FIJρσ denotes gravitational curvature, while later Fµν is EM. This is easy to confuse.
Required fix: Use R for gravitational curvature throughout and reserve Fµν exclusively for electromagnetism (or vice versa). Fix Eq. (5)–(6) and surrounding prose accordingly.

P1A-M12 (Fig. 4 and Fig. 7 “combined” joint-significance; captions pp. 16, 23)
Problem: The curves assume a cross-estimator correlation ρ between SPHEREx fNL and CMB EB birefringence measurements. No physical or statistical rationale is provided for ρ ≠ 0 across these disparate probes, nor is a covariance model specified.
Required fix: Either set ρ = 0 and remove the ρ > 0 curves, or provide a justified covariance model for joint-estimator correlations (including which shared systematics or sky cuts induce a nonzero ρ) and the formula used to combine significances.

P1A-M13 (Sec. IV D; Eq. (17) use; Appendix C)
Problem: The inversion ρθ = 2 mθ^2 β^2/(α/M)^2 relies on the estimate Δϕ ≈ √(2ρθ)/mθ (monotonic slow roll or frozen field). This equivalence is asserted but not derived or cited; it is not valid for all regimes (e.g., mθ ≪ H0 with negligible rolling, oscillatory mθ ≫ H0).
Required fix: Derive the Δϕ–ρθ relation under the stated background evolution (frozen/slow-roll with mθ ≲ H0), or cite a standard reference, and clearly delimit the regime of validity. Provide a sentence noting that for mθ ≫ H0 the present-day β is further suppressed (oscillatory dilution), strengthening the “overshoot” point.

P1A-M14 (Sec. II C 1; “Reheating thermal-reset barrier”)
Problem: While a useful heuristic, the washout argument hinges on Γwash/H estimates. You show Γy/H ∼ y^2 MPl/T ≫ 1 for yt ∼ 1 at Treh ∼ 10^15 GeV, but Γsph/H ∼ αW^5 MPl/T is only ≫ 1 at lower T (you note this). The logic is sound, but the conclusion “instantaneously inherited post-reheating mean torsion ≃ 0” is stronger than the inputs shown (since it depends on detailed thermal history).
Required fix: Rephrase to “expected rapid washout” and list the precise temperature ranges for each channel with a concrete numerical example (e.g., Γy/H ≈ 10^4 at T = 10^15 GeV). Clarify that a full Boltzmann computation is required for a quantitative bound.

MINOR

P1A-m6 (Appendix C; WKB condition statement)
Problem: The WKB validity check uses “cosmological-tuning mθ ∼ H0 sets ˙θ ∼ H0,” but for mθ ≪ H0 the field is even more frozen and the inequality k ≫ (α/M)ϕ′ is even better satisfied. The present text could be misread as requiring mθ ∼ H0 for WKB.
Required fix: Add a clause noting that for mθ ≪ H0 the WKB condition holds even more strongly; the bound used is conservative.

P1A-m7 (Eq. labeling and symbol hygiene)
Problem: In Sec. II A 2 Step 3, FIJ[K, R˚] is introduced and immediately the component expression Eq. (6) uses FIJρσ with a note about calligraphic vs roman F. This can trip readers.
Required fix: Rename FIJ → RIJ consistently (with a sentence “we now write the curvature two-form as RIJ to avoid confusion with the electromagnetic Fµν”). Adjust the text around Eq. (5)–(6).

P1A-m8 (Abstract vs body phrasing: barrier hierarchy)
Problem: The abstract lists “14 constraints” without labelling which are theorem-level vs. ansatz-level vs. heuristic. While you do this carefully in the body (Sec. IX, XII), the abstract could mislead a skim reader.
Required fix: Add one phrase in the abstract such as “These include a theorem-level perturbation-transparency proof (scalar matter) and amplitude/heuristic constraints under stated ansätze for the remaining routes.”

P1A-m9 (Table/figure cross-reference redundancy; Fig. 7 caption)
Problem: The caption says the significance “duplicates the ρ = 0 combination of Fig. 4,” which is a circular cross-reference and unhelpful for a standalone figure.
Required fix: Remove the duplication phrasing and simply state the assumptions (ρ = 0, survey specs) in this caption.

P1A-m10 (Typographic/notation)
Problem: Inconsistent use of ε vs ϵ, occasional spacing in author names (e.g., “Pop lawski,” “Domaga la”), and mixed γ, γBI in a few places.
Required fix: Normalize symbols and names uniformly (e.g., γBI for Barbero–Immirzi, “Popławski,” “Domagała”). Ensure ε-style uniformity.

P1A-m11 (Barrier labeling clarity; Table II vs text)
Problem: Barrier labels in Table II are concise; some corresponding sections (e.g., B3, B10) do not provide a precise statement (lemma/theorem/ansatz).
Required fix: Add a parenthetical in each barrier’s text with its status (theorem/ansatz/heuristic) to align with Table II and the abstract calibration.

J. ARITHMETIC/CHECKS PASSED (no changes required)
- All reported simple ratios/significances cross-check: βobs/σ (3.64σ), ACT (2.90σ), Δβ significance (1.06σ), γPTA offset (1.13σ), e32 ≈ 7.9×10^13, [(α/M)MPl] ≈ 3×10^−3, ρθ(βobs, mθ = H0) ≈ 1.6×10^−10 eV^4.
- LQC ρcrit/ρPl scaling at γ = 0.274 and 0.2375 recomputes to 0.27 and 0.41, respectively.

Conclusion
These additional issues focus on (i) self-containment of key normalizations (Appendix C), (ii) over-assertive language about fNL erasure absent a quantitative suppression, (iii) a plot that looks like a derived RG result without an equation, (iv) clarity on an ECH “universality” claim, and (v) avoiding implied cross-probe correlations without a covariance model. Addressing them—together with the essential fixes in the initial review—will materially improve rigor and readability.