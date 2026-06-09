# P2 auto-2026-06-09_1042pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6257 chars)
**Wall time**: 279.3s

---

Referee report on “Cosmic Birefringence from a Planck-Scale Axion-Like Particle: Predictions, Constraints, and LiteBIRD Forecasts”

Scope of review: methodology rigor (statistics, derivations, dimensional checks, internal arithmetic consistency, figure/table audit).

Overall assessment: The draft contains multiple methodological and internal-consistency problems that preclude acceptance in PRD in its current form. Several central quantitative claims are either unsupported, computed from inconsistent datasets, or internally contradictory. Numerous placeholder citations “[?]” appear throughout. Below I itemize all findings.

Findings

ESSENTIAL

P2-E1 (Sec. 3.4, pp. 3–4): Dataset inconsistency in Bayes factor
- Text: “ln B = 5.17 … computed via the Savage-Dickey density ratio with a flat prior β ∈ [0°, 1°].”
- Problem: The reported ln B = 5.17 numerically matches using βobs = 0.342 ± 0.094° (Eskilt et al.), not the combined constraint given in Eq. (4) (β = 0.242 ± 0.061°). For Eq. (4), a correct SDDR gives ln B ≈ 5.99 for prior [0°, 1°]. The two subsequent prior variations (4.48 for [0°, 2°], 5.86 for [0°, 0.5°]) also correspond to the Eskilt value, not the combined likelihood.
- Required fix: State unambiguously which likelihood/posterior is used for the SDDR and recompute ln B consistently for that choice. If presenting multiple datasets/estimators, compute and report ln B separately for each, with clear labels. Provide numerical steps or an ancillary notebook to reproduce the densities at β = 0.

P2-E2 (Sec. 5, p. 5): Incorrect claim that β is unaffected by imposing the spectator-energy-density condition via small θi
- Text: “We adopt option (a) (θi ∼ 0.22 …) as the headline parameter point, in which case the β ∼ 0.27° prediction continues to hold by the cancellation above; …”
- Problem: The fa-cancellation only removes explicit fa-dependence; β ∝ (Caγ θi) F(m/H0). Reducing θi from ∼1 to 0.22 reduces β by ≈4.5× unless Caγ (or F via m/H0) is increased accordingly. With the fiducial example (Caγ = 8, F ≈ 1.07), β scales to ≈0.064°, far below the observed ≈0.34°. The text’s assertion is mathematically incorrect.
- Required fix: Recompute β for the spectator regime and specify what changes to Caγ and/or m/H0 (and hence F) are needed to recover β ≈ 0.27–0.34°. Update all figures/tables and conclusions accordingly, or clearly state that the “strict spectator” regime predicts a much smaller β unless Caγ is substantially larger.

P2-E3 (Sec. 3.2, p. 2): Undefined parameter in Eq. (5)
- Text: “The effective photon coupling parameter: fphoton × C0 = 1.73 ± 0.44.”
- Problem: fphoton is not defined anywhere (dimensions, functional dependence on θi, m/H0, αEM, etc.). This number cannot be interpreted or reproduced.
- Required fix: Define fphoton explicitly (including units) and show how it maps to β via Eq. (2). Provide a derivation or reference and enough detail to reproduce the 1.73 ± 0.44 value from the inputs.

P2-E4 (Multiple places, all pages): Missing citations (“[?]” placeholders)
- Examples: Abstract, Sec. 1 (Planck/ACT results), Sec. 3.1 (Planck NPIPE, ACT DR6), Sec. 4 (LiteBIRD), Sec. 6–7 (ECH gravity, bounce cosmology, Fujita et al., Namikawa et al.), “companion Paper I(a)”.
- Problem: PRD requires complete, accurate references. Placeholders are not acceptable.
- Required fix: Replace all “[?]” with full references (authors, year, journal/arXiv). Verify that quoted statistics match those sources.

P2-E5 (Sec. 3.4, p. 3): One-sided prior used for Bayes factor without justification
- Text: prior β ∈ [0°, 1°].
- Problem: The parity-violating birefringence angle can have either sign. Restricting to β ≥ 0 places the nested null at the boundary and artificially inflates ln B by ln 2 relative to a symmetric prior. No justification is given.
- Required fix: Recompute SDDR using a symmetric prior (e.g., β ∈ [−1°, 1°]) or explicitly justify a one-sided physical prior. If using a one-sided prior, discuss boundary issues for SDDR and their impact on the evidence.

P2-E6 (Sec. 3.2, p. 2): Independence assumption in the summary-likelihood combination
- Text: “combining the measurements under the assumption of independent errors.”
- Problem: Planck and ACT birefringence estimates share overlapping sky and use conceptually similar self-calibration; correlations and common systematics are plausible. Treating them as independent may overstate the combined significance.
- Required fix: Provide a correlation assessment or a conservative combination that brackets plausible correlations (e.g., include a correlation coefficient ρ and show sensitivity). At minimum, justify independence or propagate an uncertainty band on σ(βcombined).

P2-E7 (Abstract p. 1 and Sec. 5 p. 5): Misleading claim on fa “required” by spectator constraint
- Text (Abstract): “the ‘fa ∼ MPl’ choice is required … by the spectator-condition energy-density constraint Ωϕ ≪ 1.”
- Problem: Eq. (11) shows Ωϕ ∝ (fa/MPl)^2; decreasing fa helps the spectator condition. The text later acknowledges that lowering fa achieves the same effect (option b). The “required” wording is therefore false/misleading.
- Required fix: Correct the abstract and conclusions to state that the spectator condition can be met either by small θi and/or by smaller fa; fa ∼ MPl is a model choice, not required by the spectator constraint.

P2-E8 (Sec. 3.3, p. 3; Fig. 1, p. 4): Inconsistency between Caγ × θi posterior and the β amplitude
- Text: “Caγ × θi = 3.4 ± 1.1.”
- Problem: Using β = (αEM/4π) (Caγ θi F), and F ≈ 0.65–1.1 (Sec. 2.1), Caγ θi ≈ 3.4 implies β ≈ 0.07–0.13°, not 0.34°. This indicates a normalization/definition mismatch with Eq. (2) or with how Caγ × θi is reported.
- Required fix: Audit the normalization used in the MCMC and in Eq. (2); ensure consistent units (radians vs degrees) and definitions. Report the posterior of the physically relevant combination Caγ θi F(m/H0), and verify that it reproduces the β posteriors shown. If there was a missing factor (e.g., 2, π, degree-to-radian), correct all numbers accordingly.

P2-E9 (Figs. 1–2, pp. 4–5 vs. Sec. 3.3, p. 3): Figure-text inconsistencies and missing provenance
- Text vs. Fig.: Sec. 3.3 states βALP = 0.336 ± 0.107° and βfree = 0.344 ± 0.096°, but Fig. 1 bottom-right shows “β [deg] = 0.324 ± 0.099”. Fig. 2 caption indicates “All three are consistent,” but run provenance is not specified.
- Required fix: For each figure, specify which run/dataset it corresponds to, ensure numbers match text, and update captions to be fully self-consistent.

MAJOR

P2-M1 (Sec. 3.3, p. 3; Table 1, p. 3): Insufficient MCMC sample sizes for the claims made
- Text: runs with 720–6840 accepted samples; R̂ − 1 < 0.01; Neff ∼ 1,000.
- Problem: For the dimensionality considered, 720–6840 total samples are inadequate for stable tail probabilities, Bayes factors, and precise posteriors. Quoting ln B to two decimals and tight posterior means with such small chains is not robust. Neff cannot exceed total accepted samples; the text is confusing or incorrect.
- Required fix: Increase chain lengths substantially (multiple chains totaling ≳50k–100k effective samples per configuration), report per-parameter Neff and R̂, and provide autocorrelation times. Recompute all posterior summary statistics and ln B with the longer runs.

P2-M2 (Sec. 3.3, p. 3): Prior choices insufficiently justified and sensitivity not explored
- Text: θi ∈ [0.01, π] flat; Caγ ∈ [1, 30] flat; log10 m uniform in [−35, −30].
- Problem: The θi prior excludes 0; Caγ upper bound fixes conclusions about “order unity”; no prior sensitivity tests are shown.
- Required fix: Justify each prior with references/physical reasoning and perform prior-robustness checks (vary bounds, log vs linear) to demonstrate stability of key inferences (β, Caγ θi).

P2-M3 (Sec. 2.1–2.2, pp. 2): Insufficient detail for reproducibility of Δϕ/fa and F(m/H0)
- Problem: Δϕ/fa values are quoted from a “numerical integration” without providing equations in dimensionless form, initial conditions, the cosmology used, or code. F(m/H0) is referenced but never tabulated/plotted.
- Required fix: Provide the dimensionless EOM, initial conditions, numerical scheme, and a figure/table of F(m/H0) over the stated mass range. Include code or a reproducibility appendix/ancillary file.

P2-M4 (Throughout, esp. Abstract, Sec. 1, Sec. 3): Mixing σ-levels from different estimators without qualification
- Problem: The manuscript juxtaposes σ-levels from Planck-only, ACT-only, a simple inverse-variance combination, and a joint EB spectral fit (Eskilt) without consistently flagging that these are not directly comparable estimators/likelihoods.
- Required fix: In every place where different σ-levels appear side-by-side, explicitly state that they are not directly comparable and indicate which estimator/likelihood each refers to.

P2-M5 (Sec. 2.2, p. 2): “Natural DFSZ-type value Caγ = 8” claim without support
- Problem: The anomaly coefficient range and “naturalness” claim for a generic ALP require a model or citation; DFSZ pertains to the QCD axion.
- Required fix: Provide appropriate citations/model context or remove the “DFSZ-type” naturalness language for an unrelated ALP.

MINOR

P2-m1 (Sec. 5, p. 5): Numerical inconsistency for “∼25× fine-tuning”
- Text: “suppressing θi to ∼√0.05 θnat ≈ 0.22 (a ∼25× fine-tuning…)”
- Problem: √0.05 ≈ 0.2236; the energy density reduces by a factor ≈ 20, not 25. The misalignment amplitude is reduced by ≈ 4.47×, not 25×.
- Required fix: Correct the factor(s) and clarify whether the “×” refers to energy density or angle.

P2-m2 (Sec. 1, p. 1): Typo
- Text: “the mθ ∼ H0 ultralight-mass tuning…”
- Required fix: Replace with “m ∼ H0 ultralight-mass tuning”.

P2-m3 (Sec. 2.1, p. 2): Redundant sentence
- Text: The sentence about Hubble friction freezing the field and rolling at z ∼ O(1) appears twice.
- Required fix: Remove duplication.

P2-m4 (Sec. 2.2, p. 2): Units of β
- Problem: Eq. (2) yields β in radians; subsequent text lists degrees without explicit conversion note.
- Required fix: State explicitly that numerical values are quoted in degrees and apply the 180/π factor when comparing with data.

P2-m5 (Throughout): Inconsistent notation for anomaly coefficient
- Problem: The paper alternates between C0, Caγ, Cav.
- Required fix: Choose a single symbol (e.g., Caγ) and use it consistently.

P2-m6 (Sec. 2.1, p. 2): Planck 2018 cosmological parameters cited without reference
- Required fix: Add the Planck 2018 reference.

P2-m7 (Throughout): “Order-unity” language used loosely (sometimes meaning 1–3, elsewhere up to 10–12).
- Required fix: Clarify the intended range and use “O(10)” where appropriate.

P2-m8 (Figs. 1–2): Ensure all axes have units and consistent labels (e.g., Caγ vs “Cav”).
- Required fix: Correct axis labels and include units where applicable.

NIT

P2-n1 (Throughout): Typesetting artifacts (hyphenation/spacing around “◦ , consis­ tent”; “βobs” formatting).
- Fix typography.

P2-n2 (Acknowledgments, p. 7): “consumer hardware” and “AI research assistants” are not standard for PRD acknowledgments.
- Suggest removing or rephrasing succinctly.

P2-n3 (Sec. 6, p. 5–6): Bounce-cosmology discussion is tangential for a birefringence methods paper.
- Suggest compressing to one sentence or moving to an appendix.

P2-n4 (Notation): Use a consistent style for αEM.

Arithmetic/Dimensional spot-checks performed

- Eq. (2) numerical example: With αEM ≈ 1/137, Caγ = 8, Δϕ/fa = 1.07, β ≈ (αEM × 8/4π) × 1.07 rad = 0.00498 rad = 0.285°, consistent with the text.
- Combined constraint (Eq. 4): From 0.30 ± 0.11° and 0.215 ± 0.074°, inverse-variance combination yields 0.241 ± 0.061°, consistent with 0.242 ± 0.061°; significance ≈ 3.97σ.
- SDDR check: Using 0.342 ± 0.094° and prior [0°, 1°], ln B ≈ 5.17 (matches text); using Eq. (4), ln B ≈ 5.99 (does not match text), confirming P2-E1.
- Spectator Ωϕ (Eq. 11): For fa = MPl, m = H0, θi = 1, Ωϕ = 1/6 ≈ 0.167 (matches text).
- Effect of θi = 0.22 on β (with Caγ and F unchanged): scale β down by ≈ 0.22; conflicts with text’s claim (P2-E2).

Length and scope
At 7 pages the paper is short for the multiple analyses claimed, but substantial methodological content is missing. A thorough revision with full derivations, references, clarified likelihoods, and robust MCMC would likely expand the paper; that is appropriate.

## Summary recommendation
REJECT

The manuscript in its current form fails PRD methodological standards: it contains multiple essential inconsistencies (notably the erroneous claim that β remains unchanged under the spectator misalignment reduction; dataset inconsistency in the Bayes factor; undefined parameters; one-sided priors without justification), and numerous placeholder citations. The MCMC evidence claims are not robust given the very small chains. A fundamentally revised submission addressing all ESSENTIAL and MAJOR items, with complete references, corrected derivations, reproducible computations, and consistent figures, could be reconsidered, but the present draft is not suitable for publication.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (second-pass audit)

ESSENTIAL

P2-E10 (Abstract, p. 1): Missing αEM/(4π) factor in the “fa-cancellation” formula
- Text: “β = (gaγ/2) ∆ϕ ≈ (C0 θi/2) F(m/H0) is independent of fa”
- Problem: This omits the required αEM/(2π) factor from gaγ. From Eq. (2): β = (αEM C0/4π) θi F(m/H0). The abstract’s formula is dimensionally and numerically wrong (would overpredict β by ≈1/(αEM/2π) ≈ O(10^3) if taken literally).
- Required fix: Replace with β ≈ (αEM/4π) C0 θi F(m/H0). Ensure this corrected normalization is used consistently wherever the “cancellation” is discussed.

P2-E11 (Sec. 2.2, p. 2): Inconsistent predicted β span vs stated “natural” parameter ranges
- Text: “prediction spans β ≈ 0.17–0.43° across m/H0 ∈ [1, 3], θi ∈ [0.5, 2], Caγ ∈ [4, 12].”
- Problem: Using β = (αEM/4π) Caγ θi F and F ≈ 0.65–1.1 for m/H0 ∈ [1,3], the actual span is ≈0.043° (Caγ=4, θi=0.5, F=0.65) up to ≈0.88° (Caγ=12, θi=2, F=1.1). The quoted 0.17–0.43° band excludes much of the parameter space described.
- Required fix: Recompute and report the correct β range (state the exact F(m/H0) used). If additional cuts were applied, state them explicitly.

P2-E12 (Sec. 3.4, p. 3): SDDR unit dependence not specified (degrees vs radians)
- Problem: Densities used in the Savage–Dickey ratio depend on the variable’s units. The manuscript uses β in degrees in several places (including the prior bounds), but this is never stated for the SDDR. A change of variable (deg ↔ rad) rescales both prior and posterior densities by 57.3 and shifts ln B by ln(57.3) ≈ 4.05 if not handled consistently.
- Required fix: State explicitly whether the prior/posterior entering SDDR are defined per degree or per radian, and ensure both use the same units. Provide reproduction steps accordingly.

P2-E13 (Secs. 2.2 vs 3.3): Mass-range inconsistency between “prediction” and inference priors
- Text: Prediction discussion uses m/H0 ∈ [1,3]; MCMC prior is log10(m/eV) ∈ [−35, −30], i.e., m/H0 ≈ 0.016–50.
- Problem: The predictive statements and plots are framed for m/H0 ∈ [1,3], but inference explores—and is informed by—a much broader mass range. This undermines comparability of the quoted “natural” β span with the posteriors.
- Required fix: Align the prior to the stated “natural” range or present predictions and β spans across the full prior, with F(m/H0) tabulated over that domain.

P2-E14 (Sec. 3.3, Fig. 1): Treating an “integer” anomaly coefficient as continuous
- Text: Caγ is repeatedly described as an integer anomaly coefficient but is sampled as a continuous parameter (prior flat on [1,30]; continuous axis in Fig. 1).
- Problem: Methodological inconsistency; inferences depend on the assumed measure. If Caγ is discrete, the prior should reflect that, and posteriors should be reported for integer support.
- Required fix: Either (a) adopt a discrete prior over integers and recompute posteriors, or (b) justify why a continuous effective coupling is appropriate and drop the “integer” language.

MAJOR

P2-M6 (Abstract, Secs. 1, 7): Unjustified claim that “fa ∼ MPl is required by EFT consistency”
- Problem: There is no derivation or citation that a gravitationally coupled pseudoscalar must have fa ∼ MPl. Many ALP EFTs admit fa well below MPl. This assertion materially affects the paper’s framing.
- Required fix: Provide a rigorous argument/citation for this requirement or soften to “can be motivated,” clearly separating it from the spectator-density argument (which, in any case, does not require large fa).

P2-M7 (Sec. 4, p. 4): Forecast ignores model uncertainty; uses a single-point β
- Text: 9σ forecast uses β = 0.27° as fixed.
- Problem: β depends on Caγ, θi, and m/H0. A proper forecast should present the posterior predictive distribution for β (given priors/posteriors on these parameters) and an expected detection significance or expected Bayes factor distribution for LiteBIRD.
- Required fix: Provide a posterior-predictive forecast (and sensitivity to priors), not just a single-number significance.

P2-M8 (Sec. 5, p. 5): Unsupported cosmology claim about Ωϕ ≈ 0.17 being “allowed … at the ∼10% level”
- Problem: No citation or quantitative fit is provided. Moreover, 0.17 of critical density today is larger than “∼10%.” This statement needs evidence or removal.
- Required fix: Cite constraints on additional smooth components at z ≈ 0 and show that Ωϕ ≈ 0.17 is viable (or retract/qualify the claim).

P2-M9 (Abstract/Secs. 3.2–3.3 vs Fig. 2): Dataset baseline inconsistency across the manuscript
- Problem: Abstract and Sec. 3.2 emphasize the “combined Planck + ACT” summary-likelihood (β = 0.242 ± 0.061°), while Sec. 3.3 and Fig. 2 center the analysis on the Eskilt joint EB fit (βobs = 0.342 ± 0.094°). The manuscript alternates baselines without a unifying structure, complicating interpretability.
- Required fix: Choose a primary baseline (or clearly separate presentations), and consistently label every figure/result with the corresponding dataset/likelihood.

MINOR

P2-m9 (Throughout, esp. Secs. 2.2, 3.2–3.4, Figs. 1–2): Unit convention not stated uniformly
- Problem: Some quantities are in degrees (β plots), some equations give β in radians (Eq. 2). The likelihoods and priors are applied in degrees, but this is not stated globally.
- Required fix: Add a short subsection stating the global unit convention (likelihoods, priors, posterior densities per degree), and annotate axes accordingly.

P2-m10 (Sec. 7, p. 6): “Degeneracy … does not affect the birefringence prediction” is asserted, not shown
- Problem: While β depends on Caγ θi, the impact of the Caγ–θi degeneracy on predictive uncertainty is not quantified.
- Required fix: Show the posterior for the product Caγ θi F(m/H0) and the induced β posterior, and discuss how parameter degeneracies propagate to β and to particle-model interpretations.

NO OTHER OVERLAPS
I have not repeated items from the first report (P2-E1…E9, P2-M1…M5, P2-m1…m8, P2-n1…n4). The new findings above originate from additional arithmetic checks (β span), abstract/body normalization audit (missing αEM/(4π)), SDDR unit sensitivity, prior-domain consistency, discrete-parameter treatment, unsupported EFT requirement, forecast methodology, and unsupported cosmology claim.