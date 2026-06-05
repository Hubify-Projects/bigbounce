# P1B auto-2026-06-05_1418pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7671 chars)
**Wall time**: 421.8s

---

Referee report on “Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model”

Scope of review
- Focus: methodology rigor, statistical validity, derivation chains, dimensional consistency, internal arithmetic, and claim-to-evidence traceability.
- I audited all scalars quoted in the abstract and conclusions against the body. I recomputed the quoted significances and simple combinations, and checked consistency across tables/sections.

Overall assessment
The manuscript is a methods companion documenting three technical components: (i) a stock-CAMB ΛCDM+ΔNeff proxy MCMC; (ii) a NaMaster pseudo-Cl pipeline validation for birefringence recovery with injected signals; and (iii) an ALP-based cosmic-birefringence consistency check. The intent and many scoping caveats are commendably explicit. However, several critical issues prevent acceptance in PRD in its present form:

- Inconsistent dataset attributions (PR3 vs PR4/NPIPE; DESI DR1 vs DR2), one outright contradiction (a “Planck-only” chain “reported in Table I” while Table I has only two columns), and scattered internal/reviewer-process language embedded in the text and even in a reference entry.
- The NaMaster pipeline section does not specify the primary estimator for β (nor its weighting, ℓ-range, or covariance estimation), yet reports recovered angles, biases, and “SNR”; this is not reproducible as written.
- The w0–wa chain is presented as a “headline” dark-energy result while the authors explicitly defer Bayes factors and even Δχ2 model-comparison metrics; several passages conflate (or at least co-display) different kinds of significances without a side-by-side comparability warning.
- Multiple minor but nontrivial inconsistencies (R̂ − 1 threshold claim vs. table value; terminology and units mismatches) need correction.

Below is a structured list of findings.

Findings

ESSENTIAL (must be fixed for PRD)

P1B-E1 (Sec. III, p. 3; Table I, p. 3)
Problem: Footnote 1 states: “The third (Planck-only) dataset combination … is reported separately in Table I,” but Table I contains only two columns (“Full-tension” and “Planck+BAO+SN”) and no Planck-only column. This is an internal contradiction.
Required fix: Either add the Planck-only column with its diagnostics to Table I or delete the statement that it is reported in Table I. If you keep it, ensure the Planck-only chain’s configuration (likelihoods, priors), R̂ − 1, ESS, and posteriors are shown.

P1B-E2 (Sec. V.A, p. 6; Table II header/caption p. 4; multiple pages)
Problem: Dataset labeling inconsistencies:
- Sec. V.A: “Planck 2018 NPIPE [17]” (NPIPE is PR4; ref. [17] is PR3 parameters).
- Sec. III/Table II caption: “Planck 2018 NPIPE lowl.EE+TT + highl.CamSpec.TTTEEE + lensing.native.”
- Body text alternates between DESI 2024 DR1 BAO [18] and DESI DR2 (Table II explicitly says DR2).
Required fix: Unify all dataset attributions. Explicitly name the exact likelihoods used (PR3 vs PR4/NPIPE; which CamSpec high-ℓ version; which low-ℓ set; DESI DR1 vs DR2; DES(-Y3/-Y5) and Pantheon+/DES-SN5YR versions). The paper—not a repository README—must be authoritative and internally consistent.

P1B-E3 (Sec. III “Physics interpretation”, p. 3–4; Sec. III “MB–H0 joint-posterior check”, p. 4; Ref. [15], p. 10; Abstract footnote a, p. 1)
Problem: Internal versioning/reviewer-process language inside the scientific narrative, e.g.:
- “An earlier count erroneously quoted ‘98.6%...’”
- “This addresses earlier reviewer concerns… NOT a YAML omission.”
- “prior caveat promised a Savage-Dickey ratio…”
- Ref. [15] includes “the value used at L256/L416 of P1B”
- Abstract footnote a: “The repository README is the authoritative source…”
Required fix: Remove all internal versioning/reviewer-process statements and internal line-number references. Replace with neutral, self-contained scientific prose. The paper must itself be the authoritative source.

P1B-E4 (Sec. IV, p. 5–6)
Problem: The NaMaster pipeline does not define the β estimator (mathematical form, ℓ-range, bandpower weights, and covariance estimator). Yet the paper reports β̂, a “pipeline-recovery bias” (0.032–0.040°), and an “SNR=20.32; 25.71.”
Required fix: Predeclare the β estimator precisely (e.g., EB-based estimator formula; exact ℓ-bin edges; weighting; whether you fit a constant β via CℓEB ∝ 2β CℓEE with purification; how uncertainties are obtained). Report:
- The per-realization scatter σ(β̂) from the 500 MCs and the standard error on the mean (SEM).
- The exact SNR definition (mean/SD across MCs, or other).
- The dependence of the bias on mask apodization scale, purification flags, and ℓ-range. If you adopt 0.040° as a “systematic floor,” justify it by showing stability across these choices or restate it as configuration-dependent.

P1B-E5 (Sec. III/Table II, p. 3–4; Sec. V, p. 6–7)
Problem: The w0–wa chain is used to make a “headline result” (w0 departs +4.3σ; wa departs −3.6σ; w0+wa = −1.48±0.15), but (i) the exact likelihood stack and priors vary across the paper, and (ii) model comparison against ΛCDM (Δχ2, Bayes factors) is explicitly deferred. Statements about “disfavoring” ΛCDM are not accompanied by proper model-selection metrics and the LCDM point lies in the posterior tails of an MH chain that did not sample it.
Required fix: Either (a) provide a controlled Δχ2 and/or a robust Bayes factor using nested sampling for the exact likelihood stack you report, or (b) strictly confine the w0–wa discussion to parameter estimates only and remove any language implying model preference/exclusion. Also provide the exact YAML-like configuration used for Table II (likelihood names/versions, priors) in the text or an appendix.

P1B-E6 (Table I footnote a, p. 3)
Problem: Footnote asserts “all 17 sampled parameters … satisfy R̂ − 1 < 3 × 10−3” but the table lists “Worst R̂ −1 = 0.003” (Planck+BAO+SN). 0.003 equals the threshold, not strictly less than.
Required fix: Change to “≤ 3 × 10−3” or recompute R̂ to below the stated threshold.

P1B-E7 (Abstract and Sec. VI, p. 1 and p. 6–7)
Problem: The paper relies on β = 0.342° ± 0.094° as the “headline” WMAP+Planck joint constraint while also mentioning PR4/NPIPE code updates. The abstract’s footnote a defers to a repository README for dataset attribution.
Required fix: State unambiguously in the paper which CMB release(s) and likelihoods your ALP MCMC actually use (e.g., PR3+WMAP9 for the headline; PR4/NPIPE for reproductions), and keep these consistent across the abstract/body. Remove the statement that the repository README is authoritative.

MAJOR

P1B-M1 (Sec. III, p. 5)
Problem: “Independent cross-validation.—Liu et al. [11] … Our MCMC agrees at 0.5σ in H0 and 0.4σ in σ8.” No numbers from [11] are shown and your reported values are for a different model class (ΛCDM+ΔNeff proxy vs. the torsion model of [11]).
Required fix: Quote the comparison numbers from [11] and compute the differences explicitly, specifying the models and datasets so the comparison is apples-to-apples. Otherwise, remove the cross-validation claim.

P1B-M2 (Footnote 2, p. 3)
Problem: “Λstrong ∼ MPl/√γBI set by the inverse Barbero–Immirzi parameter γBI” is stated without derivation/citation detail. Dimensional consistency is fine, but the √γBI dependence requires support.
Required fix: Provide a precise reference and brief derivation/argument, or neutralize the claim (e.g., “parametrically near MPl up to order-unity factors depending on γBI,” with citation).

P1B-M3 (Sec. III, p. 4)
Problem: SH0ES prior handling: you correctly discuss MB vs H0 tension, but you must explicitly state the SH0ES likelihood version and how covariance with Pantheon+ is handled. The present text references “H0.riess2020Mb” but does not document the covariance treatment between MB and Pantheon+ calibration.
Required fix: Specify the SH0ES prior implementation (mean, σ, nuisance parameters), how it couples to Pantheon+ (shared MB), and confirm no double counting. Include YAML-style names or an explicit list.

P1B-M4 (Sec. VI, p. 7)
Problem: “LiteBIRD is projected to achieve σ(β) ≈ 0.03° [23]” is plausible but needs a traceable pointer within [23] (figure/table/page) to the birefringence sensitivity, not inflationary r.
Required fix: Cite the specific section/figure in [23] (or an updated LiteBIRD birefringence forecast reference) from which σ(β) ≈ 0.03° is taken.

P1B-M5 (Sec. IV, p. 5–6)
Problem: The noise choice for the MC (ΔP = 10 µK·arcmin) is called “a conservative worst-case bias check,” but 10 µK·arcmin is lower noise than Planck polarization and closer to ACT. Bias from E→B leakage typically depends on mask geometry and purification more than on white-noise level.
Required fix: Rephrase to “optimistic” or justify with a test showing that bias magnitude weakly depends on ΔP in this pipeline, or else drop the “worst-case” characterization.

P1B-M6 (Sec. VI and App. C, p. 6–9)
Problem: ALP MCMC setup lacks key likelihood details: ℓ-ranges, binning, and EB-spectrum covariance. You also state “shared calibration covariance” but do not specify how it is modeled.
Required fix: Provide the β-likelihood construction details: the EB data vector definition, ℓ-bins, covariance construction (analytic vs. simulation-based), and how calibration uncertainties are included.

MINOR

P1B-m1 (Sec. V, p. 6–7)
Problem: You defer ln B/AIC/BIC but still call the w0–wa result a “headline” and say it “disfavors ΛCDM (in the marginal-tail sense).”
Required fix: Add a clear clause wherever such results are presented that posterior tail distances are not comparable to Bayes factors or frequentist exclusion, and avoid language like “disfavors” unless accompanied by Δχ2 or ln B.

P1B-m2 (Table I, p. 3)
Problem: Units formatting is inconsistent (“km/s/Mpc” vs. “km s−1 Mpc−1”).
Required fix: Standardize to “km s−1 Mpc−1”.

P1B-m3 (Sec. IV, p. 5)
Problem: “C2 apodization” presumably means cosine-squared apodization.
Required fix: Spell out “cosine-squared (C2) apodization.”

P1B-m4 (Sec. IV, p. 5–6)
Problem: The mask (fsky = 0.32) is not characterized beyond an apodization length.
Required fix: Briefly describe the sky region or provide a small figure in the appendix to document the mask.

P1B-m5 (Sec. VI, p. 7)
Problem: The statement “Both ends are larger than standard KSVZ/DFSZ benchmark range, which predicts |Caγ| ∼ O(1)” is correct, but you could add a canonical numeric range and citation.
Required fix: Add a citation and a typical numeric span for KSVZ/DFSZ Caγ to make the comparison precise.

NIT

P1B-N1 (Abstract, p. 1)
Problem: Stray footnote marker layout “2.4– 2.9σ [2, 3];a the pipeline …”
Required fix: Tighten typography; ensure the footnote marker is placed cleanly and consistently.

P1B-N2 (Multiple)
Problem: Hyphenation/typographic consistency (e.g., “ALP-MCMC re-runs”, “post-burnin”, “Cℓ” vs “Cl”).
Required fix: Standardize style per PRD guidelines.

P1B-N3 (Ref. list, p. 10)
Problem: Ref. [3] likely has many co-authors; using “and E. Komatsu” only may be fine for an arXiv preprint but check journal style for multiple-author arXiv entries.
Required fix: Conform to PRD reference style (et al. as appropriate).

Arithmetic and consistency checks performed

- Table I numbers match the abstract: H0 = 67.68 ± 1.06 and 67.79 ± 1.09; ΔNeff = −0.020 ± 0.169 and +0.065 ± 0.17. σ8 and S8 values are consistent across table and text.
- R̂ − 1 values are consistent with table entries, but the strict “< 3 × 10−3” claim conflicts with “0.003” in the Planck+BAO+SN column (see P1B-E6).
- Footnote 1 sample-count arithmetic checks out (burn-in removal yields ~216,432 post-burn-in samples across both frozen chains; the figure’s 119,617 reflects additional thinning).
- MB–H0 arithmetic: MB − 5 log10(73.04) = −28.571; MB − 5 log10(67.69) = −28.416; difference 0.155 mag (~3.16σ with σMB = 0.049) consistent with the stated ~3.2σ and canonical H0 3.6σ tension.
- Table II “vs LCDM” tail distances: (−0.8122 + 1)/0.0436 = +4.31σ; −0.6666/0.1864 = −3.58σ. wpivot = −1.0344 ± 0.0301 gives 1.14σ from −1. Internals are consistent.
- Inverse-variance combination of β (0.30 ± 0.11) and (0.215 ± 0.074) gives β = 0.241 ± 0.061 with SNR ≈ 3.95σ, consistent with the reported 0.241° ± 0.061° (3.9σ).
- ALP birefringence magnitude check: β = (αEM/4π) Caγ Δφ/fa. For β = 0.342° = 5.965×10−3 rad and αEM/(4π) ≈ 5.8×10−4, Caγ Δφ/fa ≈ 10.3 (as stated).
- Eq. (3) check: αEM ≈ 1/137; (αEM/4π)×8×1.07 ≈ 4.97×10−3 rad = 0.285°; matches ~0.29°.

Additional methodological requests

- Explicitly state the ΔNeff prior (range/form) and whether Neff was allowed to be negative in sampling (it appears so). Clarify early in Sec. III.
- For the MCMC diagnostics, add the number of post-burn-in effective samples per key cosmological parameter (ESS by parameter) and acceptance rates for transparency.
- For the NaMaster test, report null-injection results quantitatively (mean β̂ and its SD) rather than just “consistent with zero.”

Page-length
- 10 pages is reasonable for the claimed contribution once the above clarifications are made.

## Summary recommendation
MAJOR REVISIONS

The paper contains substantive methodological contributions but requires major revisions to meet PRD standards: (i) resolve dataset attribution inconsistencies and remove all internal/reviewer-process language; (ii) fully specify the NaMaster β estimator and uncertainty/SNR definitions; (iii) correct the table contradiction and R̂ threshold statement; and (iv) make the w0–wa “headline” claims methodologically neutral unless supported by proper model-comparison metrics. With these addressed, the paper could be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-pass audit)

P1B-E8 (Sec. IV, p. 5)
Problem: Rotation operator written as “e2iβ(Q + iU)” is mathematically incorrect/ambiguous. The standard operation is (Q + iU) → e2iβ (Q + iU), i.e., Q+iU multiplied by a phase, not placed inside the exponent.
Required fix: Correct the formula and unambiguously state the applied rotation: (Q+iU)rot = e2iβ (Q+iU).

P1B-E9 (Conclusions, p. 8)
Problem: Misplaced internal cross-reference: “see §VI body text” for the NaMaster bias. The NaMaster pipeline and bias are in §IV, not §VI.
Required fix: Change the section reference to §IV.

P1B-E10 (Table I footnote a, p. 3)
Problem: Footnote says “references to ‘k = 7’ elsewhere in this paper…” but no other instance of “k = 7” appears. This is a dangling, incorrect self-reference.
Required fix: Remove or provide the actual location and context for “k = 7”. As written it confuses the reader.

P1B-E11 (Sec. IV, p. 5–6)
Problem: The 500-MC “SNR” is derived by varying noise realizations on a single fixed-sky Commander map. This suppresses sky variance and can grossly inflate SNR; the result is not a meaningful detection significance or even a robust pipeline performance metric.
Required fix: Either (a) build the covariance from sky+noise MCs (e.g., ΛCDM realizations convolved with the mask, with and without rotation) and report SNR under that null, or (b) drop SNR entirely and report only bias and per-realization σ(β̂) under clearly stated assumptions.

P1B-E12 (Sec. IV, p. 5)
Problem: Map downgrading lacks a required pre-smoothing step. Degrading Nside=2048 → 512 without low-pass smoothing (e.g., Gaussian smoothing to a safe common beam before repixelization) risks harmonic aliasing and mis-modeled beams.
Required fix: Specify the pre-degrade smoothing kernel (FWHM and beam transfer function), and verify that the effective beam used in NaMaster matches the post-degrade effective beam. Otherwise, reported β-biases may be contaminated by aliasing.

P1B-E13 (Sec. VI, p. 7; App. C, p. 9)
Problem: Logical inconsistency in ALP/βfree runs. The text says the model-independent βfree fit has “9,720 accepted samples across the 3 ALP-MCMC configurations … Caγ = 4, 8, 12 with β as a free parameter.” But βfree has no dependence on Caγ; pooling or triplicating runs only labeled by Caγ is unjustified and risks double counting.
Required fix: Clarify that βfree was run once (independent of Caγ) and report that sample size. If you actually ran three identical βfree chains, do not combine them as independent evidence; instead present a single βfree posterior.

MAJOR

P1B-M7 (Abstract, Sec. III, p. 1–3)
Problem: “H0 consistent with Planck ΛCDM (… at 0.3σ)” is stated without showing the specific Planck baseline value/σ used for that 0.3σ computation.
Required fix: Quote the Planck reference (value and 1σ) and show the arithmetic for the 0.3σ consistency, or drop the quantified 0.3σ statement.

P1B-M8 (Sec. VIII/Conclusions, p. 8)
Problem: “CMB-S4 (σ(Neff) ∼ 0.03) will provide the first precision test” lacks a citation and specification (forecast assumptions, dataset combination).
Required fix: Add a precise CMB-S4 forecast citation (e.g., CMB-S4 Science Book) and context for σ(Neff) ≈ 0.03 (channels, ℓ-range, external priors).

P1B-M9 (Sec. VI, p. 7)
Problem: Statement “∆ϕ/fa ∝ θi along the underdamped trajectory” is used to scale Caγ but is neither derived nor cited.
Required fix: Provide a short derivation or cite a reference demonstrating the proportionality in the m ~ H0, small-angle regime. Otherwise rephrase as an approximate empirical trend observed in your ODE integrations, with a figure or table.

P1B-M10 (Sec. IV, p. 6)
Problem: Claim that the measured β-bias is “consistent with the apodized-mask bias expected from a 2° apodization scale” is unsupported by a quantitative study.
Required fix: Show β-bias vs. mask apodization length and purification flag (at least 2–3 points) to justify this expectation, or qualify the statement as a configuration-dependent observation rather than an “expected” behavior.

P1B-M11 (Sec. IV, p. 5)
Problem: Commander CMB solution beam handling. You adopt a “Planck-2018 effective Gaussian beam (5′ FWHM at 143 GHz)” for a Commander CMB map. Commander’s effective beam is not simply a 143 GHz Gaussian; it is a component-separated product with its own transfer function.
Required fix: Document the effective beam of the specific Commander product you use (cite Planck PR4/NPIPE Commander documentation), and use the correct beam window in NaMaster. If you approximated it as 5′, quantify the resulting β-bias.

P1B-M12 (Sec. IV, p. 6)
Problem: Time-stamp language in the scientific body (“production 500-realization run, April 2026”) is process/provenance prose rather than scientific content.
Required fix: Remove date-stamp phrasing from the main text (can remain in a reproducibility note or README).

P1B-M13 (Sec. VI, p. 7)
Problem: Reference [3] appears as a future-dated arXiv placeholder (“arXiv:2509.13654 (2025)”). This is not a stable citation.
Required fix: Update to the actual, citable arXiv ID/version (or journal) used for the ACT DR6 β measurement.

MINOR

P1B-m6 (Table II, p. 4; Sec. III, p. 3–4)
Problem: wpivot is quoted without defining the pivot redshift zp (or scale factor ap).
Required fix: State the definition (CPL pivot) and give zp (or ap) used by your chain/likelihood.

P1B-m7 (Sec. III, Table I, p. 3)
Problem: The ΔNeff prior (range and whether negative values are permitted) is not specified, yet negative posterior means imply Neff was allowed to be < 0.
Required fix: Report the exact ΔNeff prior (type and bounds) in the text or an appendix.

P1B-m8 (Sec. IV, p. 6)
Problem: Null-injection results are only described qualitatively (“consistent with zero”).
Required fix: Provide the mean and standard deviation of β̂ for β=0 injections across the 500 MCs.

P1B-m9 (Sec. III, Table I, p. 3)
Problem: ESS/acceptance transparency. Only “Min ESS” is given; acceptance rates are not reported.
Required fix: Add sampler acceptance rates and per-parameter ESS for the main cosmological parameters.

P1B-m10 (Sec. IV, Eq./text units)
Problem: β is sometimes in degrees in narrative while formulas imply radians. This risks unit slips.
Required fix: State the unit convention explicitly where formulas are presented and show the conversion when reporting degree values derived from radian formulas.

P1B-m11 (Sec. IV, p. 5)
Problem: fsky = 0.32 is given without defining how it is computed (HEALPix pixel count after apodization threshold?).
Required fix: Specify the fsky definition and measurement procedure.

NIT

P1B-N4 (Appendix A, p. 8)
Problem: Pathnames with spaces (“pipelines/h200 results/pod1 namaster umap 2026-04-29/”) are error-prone and non-portable.
Required fix: Quote such paths or present them in a code block; consider sanitizing spaces in repository paths.

P1B-N5 (Sec. IV, p. 6)
Problem: Excessive significant figures for SNR (“20.32”, “25.71”) given that the definition and covariance are not finalized.
Required fix: Round to two significant figures (e.g., 20, 26) once the SNR definition is clarified.

Explanation
The fresh-pass focused on hidden arithmetic, cross-references, dimensional/operational correctness, and reproducibility-critical details commonly missed on first read. Most new issues are in the birefringence pipeline (mathematical form of the rotation, sky-only/noise-only MC design inflating SNR, unsound beam/downgrade handling) and in the ALP βfree/Caγ configuration logic. These are separable from the previously noted dataset-label and model-comparison issues and need to be addressed for PRD-level rigor.