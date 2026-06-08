# P2 auto-2026-06-08_1520pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7586 chars)
**Wall time**: 415.5s

---

Referee report for Physical Review D (methods-focused)

Manuscript: “Cosmic Birefringence from a Planck-Scale Axion-Like Particle: Predictions, Constraints, and LiteBIRD Forecasts”
Length: 6 pages, 2 figures, 1 table

General assessment
- The paper aims to (i) present a “natural” prediction β ≈ 0.27° for cosmic birefringence from an ALP with fa ~ MPl and m ~ H0, (ii) combine Planck NPIPE and ACT DR6 birefringence estimates via a Gaussian summary-likelihood, (iii) perform small MCMC runs to compare an ALP model with a model-independent β, (iv) give a Bayes factor for nonzero β, and (v) provide a LiteBIRD forecast.
- Methodologically, there are multiple internal inconsistencies in the derivation of the predicted rotation, unclear and inconsistent coupling definitions and notation, a Bayes factor computation that is not unit-invariant and uses a boundary prior without explicit justification, mixing of different data summaries across sections, and insufficient MCMC details with very small effective sample sizes relative to the claims.
- Several load-bearing numerical claims in the abstract and conclusions cannot be traced to well-defined, dimensionally consistent equations in the body, and one of the key equations (Eq. 1) is mathematically inconsistent with the narrative and with the claimed 0.27° prediction.

Below I list detailed findings, each with a severity classification and required fixes.

Findings

P2-E1 (ESSENTIAL)
- Section 2.1, page 1–2, Eq. (1)
  Offending text: “Δϕ ≈ fa θi (1 − J0(m/H0)/J0(0)) ≈ fa θi × O(1). For m/H0 ∼ 1, 1 − J0(1) ≈ 0.24…”
  Problem: This implies Δϕ/fa ≈ θi × O(1) ≈ O(0.2–1) for θi ~ 1, which would yield β ≈ (C0/2) × O(0.2–1) ≳ O(0.1) rad ≳ several degrees, in direct contradiction with the “natural” β ≈ 0.27° claim. Later (Sec. 2.2) the text asserts “Δϕ/fa ∼ 10−2,” which is incompatible with Eq. (1).
  Required fix: Provide a correct and traceable derivation (or numerical integration) of Δϕ/fa for m ≈ H0 in a ΛCDM background, with explicit assumptions on θi and initial conditions. Remove the spurious J0(m/H0)/J0(0) form (J0(0)=1 makes the ratio trivial, and the Bessel form is not justified for an expanding ΛCDM background with varying H). State the actual cosmological integral and show how it yields Δϕ/fa ≈ 10−2 if that is the intended result, including the redshift range over which rolling occurs. Update all dependent scalars (β prediction, Figs., discussion).

P2-E2 (ESSENTIAL)
- Section 2.2, page 2 (and throughout)
  Offending text: “β = gaγ/2 Δϕ = C0/(2 fa) Δϕ … C0 is an order-unity coefficient from the ABJ anomaly.”
  Problem: The standard ALP–photon coupling is g_aγ = (α/2π f_a) C_aγ for QED couplings. Here the α/2π factor is omitted, yet C0 is called the ABJ anomaly coefficient “of order unity.” With fa ~ MPl this omission boosts g by ~8.6×10^2, which drives the claimed “natural” β. Without clarity on whether C0 already absorbs α/2π (then it is not of order unity), the parameter mapping to the literature is incorrect, and comparisons (e.g. “C=8 fixed”, priors on “Caγ”, etc.) become meaningless.
  Required fix: Define g_aγ unambiguously. If using g_aγ = C/f_a, state that C includes α/2π times the anomaly coefficient and give the numerical mapping to the conventional C_aγ. Alternatively, use the standard g_aγ = (α/2π f_a) C_aγ and adjust all priors, figures, and numerical claims accordingly. Ensure all quoted “order-unity” statements are consistent with this definition.

P2-E3 (ESSENTIAL)
- Section 3.2, page 2–3, Eq. (5) and abstract
  Offending text: “The effective photon coupling parameter: fphoton × C0 = 1.73 ± 0.44 (order-unity…).”
  Problem: “fphoton” is never defined; dimensionality is unclear; the relation to Eq. (2) and to the Run 2 posterior “Caγ × θi = 3.4 ± 1.1” (Eq. 8) is opaque. The reader cannot reproduce 1.73 ± 0.44 from the stated inputs.
  Required fix: Define fphoton explicitly, with units, and derive Eq. (5) step-by-step from Eq. (2) or the full model. Show the algebra linking the summary-likelihood βcombined to fphoton × C0 (or, if that is a different construct, rename and define it properly). Ensure consistency with Eq. (8); explain the factor-of-two and any deg↔rad conversions.

P2-E4 (ESSENTIAL)
- Section 3.4, page 3, Eq. (9) and related text
  Offending text: “ln B = 5.17 (indicative) computed via the Savage-Dickey density ratio with a flat prior β ∈ [0°, 1°].”
  Problems:
  - A uniform prior on a dimensionful parameter stated in degrees is not unit-invariant; Bayes factors then depend on unit choice (deg vs rad), which is unacceptable without careful definition.
  - The prior is one-sided with β ≥ 0. The null (β = 0) lies at the boundary of support, violating the standard Savage–Dickey conditions unless a truncated posterior normalization is handled explicitly. This is not explained.
  - No justification is given for restricting β to ≥ 0; birefringence is in principle signed.
  Required fix: Define the prior in radians and justify symmetry or intentional asymmetry. If using a truncated prior/posterior at β ≥ 0, show the exact SD expression used and its normalization. Provide a sensitivity analysis over reasonable symmetric priors (e.g. uniform on β ∈ [−βmax, βmax]) and state the unit-invariant results. Alternatively, provide a cross-check via Laplace approximation or nested sampling to confirm ln B robustness.

P2-E5 (ESSENTIAL)
- Section 3.3 and Table 1, page 2–3
  Offending text: “We acknowledge that these sample sizes (720–6,840 accepted samples)… The Gelman-Rubin … R̂ − 1 < 0.01… small effective sample sizes (Neff ∼ 1,000).”
  Problem: For Run 3 with 720 accepted samples, Neff cannot exceed 720. Neff should be reported per parameter and per run. R̂ alone is insufficient to claim convergence, especially with such short chains; the reported uncertainties in Eqs. (6–7) are of the same order as the input measurement errors and could mask poor mixing. The methodology section lacks basic details: sampler used, number of chains, warm-up/burn-in, thinning, proposal/adaptation, priors on all parameters including f_a or C variants, and likelihood specification (EB spectrum vs summary β Gaussian) for each run.
  Required fix: Provide full MCMC details, per-run Neff for β and for other parameters, number of chains and lengths, burn-in, acceptance rates, and diagnostics beyond R̂ (e.g. rank plots, energy-BFMI). Increase chain lengths to achieve Neff ≳ 5,000 per parameter (or justify why fewer suffice for the reported precisions). If the MCMC-based results are purely illustrative, state so explicitly and do not rely on them for quantitative claims (e.g. Bayes factor).

P2-E6 (ESSENTIAL)
- Sections 3.1–3.3, pages 2–3
  Offending text: Use of two distinct data summaries without consistent treatment.
  Problem: The summary-likelihood combines Planck NPIPE (0.30 ± 0.11°) and ACT DR6 (0.215 ± 0.074°) assuming independence to obtain βcombined = 0.242 ± 0.061°. But the MCMC analyses then use the Eskilt et al. joint value (0.342 ± 0.094°). Mixing these different summaries without a principled joint likelihood or a clear rationale confounds interpretation and traceability. Independence of Planck and ACT estimates for isotropic β is asserted but not demonstrated (shared sky, possible foreground/systematic correlations).
  Required fix: Choose and justify a single likelihood strategy: either use the joint EB-spectrum likelihood (as in Eskilt et al.) for all analyses, or construct a well-justified joint summary likelihood that accounts for any cross-covariance between experiments. If assuming independence, provide a quantitative justification or an upper bound on possible correlations and their impact on βcombined and ln B.

P2-M1 (MAJOR)
- Section 2.1, page 1–2
  Problem: The Bessel-function template for Δϕ is not derived for ΛCDM with time-dependent H. As written it suggests an ad hoc “O(1)” factor, later contradicted by Δϕ/fa ~ 10−2. The main physics result (the “natural” β ≈ 0.27°) depends critically on Δϕ/fa.
  Required fix: Replace the heuristic with a clear ODE solution or numerical integral for the ALP background in ΛCDM, showing Δϕ(a) from recombination to today as a function of m/H0 and θi. Provide a plot of Δϕ/fa vs m/H0 for θi ∈ [0, π], and quote the number used in the β prediction.

P2-M2 (MAJOR)
- Section 3.2, page 2–3, Eq. (3)
  Problem: The independence assumption for Planck and ACT EB-based β estimators is untested. Given a common sky and possibly common foreground modeling systematics, this assumption can bias the combined σ downward.
  Required fix: Provide an estimate (even conservative) of possible cross-correlation. E.g., propagate an assumed correlation coefficient ρ ∈ [0,0.3] to show impact on βcombined and σ. Alternatively, cite published estimates of independence or reweight to be robust to plausible ρ.

P2-M3 (MAJOR)
- Section 3.3, page 3; Table 1 caption and Fig. 2 caption
  Problem: Inconsistent naming “Run 1/2/3” vs “Model 2, 2b, 0” (Fig. 2). Also, “C = 8 fixed” appears without prior definition or physical motivation.
  Required fix: Unify run/model labels across text, table, and figures. Define “C” rigorously (see P2-E2) and justify the specific value C=8 (e.g. theoretical motivation, mapping to C_aγ, and inclusion of α/2π). If arbitrary, state that it is illustrative and show sensitivity to C.

P2-M4 (MAJOR)
- Abstract and Section 4, page 1 and 3–4
  Offending text: “LiteBIRD… will test this prediction at 9σ—either confirming the signal or ruling out the ALP explanation decisively.”
  Problem: Overclaim. A null LiteBIRD β would rule out the specific parameter choice (fa ~ MPl, m ~ H0, O(1) misalignment and coupling as defined here), not the “ALP explanation” generally, which includes many parameterizations producing negligible isotropic rotation.
  Required fix: Rephrase to “ruling out this specific Planck-scale ALP scenario (with m ~ H0 and O(1) misalignment)” or similar.

P2-M5 (MAJOR)
- Section 3.3, page 3
  Offending text: Priors: “θi flat on [0.01, π]; log10(m/eV) flat on [−35, −30]; Caγ flat on [1, 30] (Run 2 only).”
  Problem: No justification for these bounds; the lower cutoff at 0.01 excludes a non-negligible prior mass near small misalignment; the Caγ prior range is unexplained and, under standard definitions, physically suspect. The fa prior is effectively a delta-function at MPl; this strong assumption is central to the “naturalness” claim but not tested.
  Required fix: Justify each prior physically or theoretically. Explore robustness to wider priors (e.g. θi ∈ [0, π], Caγ spanning values consistent with conventional C_aγ and including α/2π factors if appropriate). Show how the posterior on β and on the coupling–misalignment product changes across priors.

P2-M6 (MAJOR)
- Section 6, page 5
  Problem: The statement “The prediction matches the combined Planck + ACT measurement at 1σ” depends on the unresolved inconsistency in Δϕ/fa and undefined coupling normalization (P2-E1, P2-E2, P2-E3). As it stands, the claim is not supported.
  Required fix: After fixing P2-E1–E3, reassess the degree-level match and quantify it rigorously (e.g., difference in means divided by the combined σ, clearly stating which data set/likelihood is used).

P2-m1 (MINOR)
- Section 3.2, page 3
  Check: Weighted combination of β1 = 0.30 ± 0.11° and β2 = 0.215 ± 0.074° gives βcombined ≈ 0.2416° and σ ≈ 0.0614°, i.e., 3.97σ. The text reports 0.242 ± 0.061° (3.9σ). Acceptable rounding, but consider reporting 4.0σ or 3.97σ for precision.

P2-m2 (MINOR)
- Section 2.1, page 2
  Offending text: “J0(m/H0)/J0(0)”
  Problem: J0(0) = 1; this ratio is gratuitous and suggests a derivation that is not shown.
  Required fix: Remove J0(0) denominator; if retaining any special-function expression, provide the underlying ODE solution and approximations.

P2-m3 (MINOR)
- Figures, pages 4–5
  Problem: Fig. 2 labels “Model 2: ALP (C = 8 fixed)” vs Table 1 “Run 1: ALP (C = 8 fixed).” Minor naming inconsistency.
  Required fix: Harmonize labels.

P2-m4 (MINOR)
- Units
  Problem: Frequent mixing of radians and degrees in narrative. Eq. (2) assumes radians; some text converts without always stating units.
  Required fix: State a clear convention (default radians in equations); convert to degrees only in final numerical summaries. Ensure all priors and densities used in Bayesian computations are in radians to maintain unit invariance.

P2-m5 (MINOR)
- References, page 6
  Problem: “Namikawa, Murai & Naokawa (2025)” — verify spelling of third author and bibliographic details when available; “in preparation” is acceptable in draft but must be updated to a citable form at acceptance.
  Required fix: Audit and correct reference metadata and years; confirm that quoted statistics elsewhere (e.g., Minami & Komatsu 2020) are consistent with the cited abstracts.

P2-n1 (NIT)
- Language consistency
  Problem: Alternating between “order-unity” and “O(1)” and informal phrasing like “no fine-tuning” without quantitative criteria.
  Required fix: Define what “no fine-tuning” means quantitatively (e.g., priors and posteriors not requiring extreme parameter values) or soften the language.

P2-n2 (NIT)
- Abstract and body
  Problem: “We forecast that LiteBIRD, with σ(β) ≈ 0.03°, will test this prediction at 9σ.” This is just 0.27/0.03; trivial arithmetic could be stated once without repetition.
  Required fix: Keep the statement but avoid overstating; ensure it is clearly conditional on the specific model and parameters.

Length
- The paper is concise (6 pages). However, given the number of required clarifications (derivation of Δϕ/fa, coupling normalization, Bayesian details, and MCMC methodology), it will likely expand. That is appropriate for PRD-level rigor.

Additional arithmetic and consistency checks
- 0.342/0.094 = 3.64σ (stated “3.6σ” — acceptable).
- 0.35/0.14 = 2.5σ (correct).
- 0.215/0.074 = 2.91σ (stated 2.9σ — acceptable).
- 1 − J0(1) = 1 − 0.76520… = 0.2348… (rounded as 0.24 — acceptable).
- The reported ln B values (5.17, 4.48, 5.86) are approximately consistent with a one-sided, truncated-posterior Savage–Dickey computation, but must be made unit-invariant and justified per P2-E4.

Summary recommendation
MAJOR REVISIONS

Justification: The manuscript has several core methodological and definitional issues that prevent acceptance in its current form. Chief among them are (i) an inconsistent and insufficient derivation for the key quantity Δϕ/fa leading to the headline β ≈ 0.27° prediction, (ii) ambiguous and nonstandard definitions of the ALP–photon coupling that undermine the interpretation of all coupling-related results, (iii) a Bayes factor calculation that is not unit-invariant and uses a boundary prior without adequate justification, and (iv) inadequate MCMC methodology and reporting. These are fixable but require substantial revision, clearer derivations, and reproducible statistical methodology.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS (second-pass audit)

P2-E7 (ESSENTIAL)
- Figure 1 numerical inconsistency (caption vs plotted marginal stats)
  Offending content: Fig. 1 caption claims “posterior on the coupling-misalignment product Caγ × θi is centered at 3.4 ± 1.1.” However, the text overlays on the figure show θi ≈ 1.33 and Caγ ≈ 13.4, which multiply to ≈ 17.8, not 3.4. The β marginal on the figure also reads β = 0.324 ± 0.099° for the same run.
  Problem: The figure’s displayed one-parameter marginals contradict the captioned (and text) value for Caγ × θi by about a factor of 5, creating a direct reproducibility failure from the published graphic alone. This also creates confusion about whether Caγ is normalized as in Eq. (2) (C0) or in a different convention.
  Required fix: Regenerate Fig. 1 with internally consistent parameter definitions and overlays, and report Caγ × θi computed from the same samples used to draw the contours. If the plotted Caγ already absorbs α/2π or other factors, state this in the caption and in Sec. 2.2, and update the numerical product accordingly. If the 3.4 ± 1.1 value is correct, the figure overlays for Caγ and/or θi are stale and must be updated.

P2-E8 (ESSENTIAL)
- Abstract misattribution of the 0.342 ± 0.094° result
  Offending text: “βobs = 0.342 ± 0.094° from the Eskilt et al. joint Planck + ACT analysis.”
  Problem: The widely quoted 0.342 ± 0.094° is from Eskilt & Komatsu (2022) using WMAP + Planck polarization, not a “joint Planck + ACT” analysis. This misstates the dataset composition in the abstract, while Sec. 3.1 correctly discusses Planck and ACT separately.
  Required fix: Correct the abstract to attribute the 0.342 ± 0.094° value to WMAP+Planck (Eskilt & Komatsu 2022). If a true joint Planck+ACT value exists and is used elsewhere, cite it precisely and reconcile all places where βobs is referenced.

P2-E9 (ESSENTIAL)
- Bayes factor computed for the wrong model class
  Offending text: “Comparing the ALP model (β ≠ 0) against the null hypothesis (β = 0): ln B = 5.17 computed via the Savage–Dickey density ratio with a flat prior β ∈ [0°,1°].”
  Problem: The SD ratio shown applies to a free-β constant-rotation model nested within the β=0 null. It does not compute the marginal likelihood for the ALP model with its induced prior on β (coming from priors on θi, m, coupling). Reporting ln B from a free-β model as “comparing the ALP model against the null” is incorrect. This is a model-mismatch error, independent of the unit/prior issues already flagged in P2-E4.
  Required fix: Either (1) present ln B for “free-β vs β=0” and label it as such (not “ALP vs null”), or (2) compute the ALP model evidence by integrating the likelihood over the ALP parameter priors to obtain p(data|ALP), and then form B = p(data|ALP)/p(data|null). Provide a cross-check (e.g., nested sampling) and a sensitivity analysis to the ALP priors on θi, m, and coupling.

P2-M7 (MAJOR)
- “m ~ H0” claim vs posterior mass location
  Offending content: Fig. 1 overlays report log10(m/eV) ≈ −31.4. Using H0 ≈ 1.44 × 10^−33 eV (log10 ≈ −32.84), the plotted posterior mean corresponds to m/H0 ≈ 28, not “∼ 1.”
  Problem: The headline narrative emphasizes m ∼ H0 to ensure “rolling today,” but the shown posterior is an order of magnitude larger, implying rolling substantially before z ∼ 1. This materially affects Δϕ/fa and the β prediction window, and conflicts with the “m ∼ H0” positioning in the abstract and conclusions.
  Required fix: Quantify the posterior for m/H0 and update text to reflect where the posterior actually lies. Show Δϕ/fa vs m/H0 (addressed in P2-M1) and demonstrate that the β prediction remains in the quoted range for m/H0 ≈ 10–30 if that is indeed where the posterior peaks. Otherwise, tighten priors or reanalyze to support the stated “m ∼ H0” claim.

P2-M8 (MAJOR)
- Symbol collision and inconsistent coupling notation beyond normalization
  Offending content: Mixed usage of C0, Caγ, C (including “C = 8 fixed”), gaγ, and the undefined fphoton across Eqs. (2), (5), Table 1, Fig. 1, and Fig. 2.
  Problem: Beyond the normalization issue flagged earlier (P2-E2), the manuscript uses multiple C-like symbols with different meanings without a definitive mapping. This impedes any cross-comparison among Eq. (2), Eq. (5), “Caγ × θi” (Eq. 8), “C = 8 fixed” (Table 1/Fig. 2), and the figure overlays. It is impossible to tell which C includes α/2π, which is an anomaly coefficient, and how these map to the literature-standard g_aγ.
  Required fix: Provide a one-page symbol table defining gaγ, fa, C0, Caγ, C (if retained), and any “effective” couplings (e.g., fphoton) with units and their relations, including where α/2π enters. Enforce one consistent notation in figures, tables, equations, and text, and re-express all results (including priors) in those terms.

P2-M9 (MAJOR)
- Gaussianity assumption for per-experiment β estimators is untested
  Offending text: Sec. 3.2 assumes a Gaussian summary-likelihood L(β) from the quoted β ± σ for Planck NPIPE and ACT DR6.
  Problem: EB-based birefringence estimators can have non-Gaussian posteriors due to self-calibration degeneracies, residual systematics, and bounded-angle effects. Assuming Gaussianity without verification risks biasing both βcombined and its uncertainty, and therefore the quoted “3.9σ” and derived ln B.
  Required fix: Cite or reproduce the likelihood shape for each experiment (e.g., from released posteriors), or validate Gaussianity by a second-order Taylor or simulation-based check. If non-Gaussian, either use the published likelihood curves in the combination or adopt a robust combination method (e.g., importance resampling) and re-evaluate βcombined and ln B.

P2-m6 (MINOR)
- Arithmetic/rounding in β ≈ 5 × 10^−3 rad ≈ 0.27°
  Offending text: Sec. 2.2: “β ≈ C0 θi × 5 × 10^−3 rad ≈ 0.27°.”
  Problem: 5 × 10^−3 rad ≈ 0.286°, not 0.27°. The 6% difference is small, but in a paper where O(1) factors are central to the argument, this should be tightened or consistently rounded.
  Required fix: Use consistent conversions (e.g., 4.7 × 10^−3 rad = 0.27°) or state ranges explicitly.

P2-m7 (MINOR)
- Abstract/body mismatch on dataset description for βobs besides misattribution
  Offending content: Abstract implies a “joint Planck + ACT” origin for 0.342 ± 0.094°, while Sec. 3.1 uses that number to represent a full EB-spectrum fit distinct from the Planck/ACT point-estimate combination.
  Problem: Even after fixing P2-E8, the manuscript should clearly segregate the two likelihoods: “full EB-spectrum (WMAP+Planck)” vs “summary combination (Planck NPIPE + ACT DR6).” The current wording risks readers believing a Planck+ACT joint EB analysis produced 0.342 ± 0.094°.
  Required fix: Standardize naming in abstract and body: e.g., “EB-spectrum (WMAP+Planck)” and “summary combination (Planck NPIPE + ACT DR6).” State explicitly that no Planck+ACT joint EB-spectrum value is used in this paper.

P2-m8 (MINOR)
- Omitted reporting of Run 2 β summary in text
  Offending content: Fig. 1 shows β = 0.324 ± 0.099° for the C-free run, but the text only quotes Run 1 and Run 3 β summaries (Eqs. 6–7).
  Problem: Readers seeking to cross-validate Fig. 1 against the text lack the Run 2 β statistic.
  Required fix: Add the Run 2 β mean and uncertainty to Sec. 3.3 or the Fig. 2 caption, and ensure the three runs’ β summaries are all reported in one place.

These issues were not covered in the initial review and, in several cases (notably P2-E7, P2-E8, and P2-E9), materially affect the paper’s internal consistency and evidentiary claims.