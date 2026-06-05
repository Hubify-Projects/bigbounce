# P1B R10v3p1 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (3793 chars)
**Wall time**: 357.9s

---

Referee report (methods/statistics) on “Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model”

Overall scope
The manuscript presents three technical exercises intended as verification/consistency checks: (i) a stock-CAMB ΛCDM+ΔNeff Metropolis-Hastings MCMC over several data combinations; (ii) a NaMaster pseudo-Cℓ pipeline Monte Carlo recovery test for a birefringence angle injected on the Planck Commander polarization map; (iii) a spectator-ALP (m ~ H0, fa ~ MPl) consistency check against published cosmic-birefringence measurements. The author is careful to position these as methodological validations rather than new sky detections or distinctive ECH predictions.

That said, a number of methodological, reproducibility, and internal-consistency issues must be addressed for PRD standards. Below I audit the numerical claims, internal consistency, and statistical methodology, and I list required corrections.

Findings and required actions

ESSENTIAL

P1B-E1 (Sec. VII, p. 8): Table cross-reference is incorrect; missing Planck-only column in Table I
- Offending text: “an additional 114,992-sample Planck-only run is still accumulating at Rˆ − 1 ∼ 0.05 and is reported separately in Table I, not aggregated into the frozen headline”
- Problem: Table I (p. 3) presents only two dataset combinations (“Full-tension” and “Planck+BAO+SN”) and no “Planck-only” column. The text asserts that the Planck-only run is “reported separately in Table I,” which is false.
- Required fix: Either add a third “Planck-only” column to Table I with the quoted 114,992-sample status metrics (R̂−1, etc.) or remove the claim that it is “reported in Table I” and state clearly that the Planck-only chain is ongoing and not tabulated.

P1B-E2 (Secs. V.A p. 6; Table II p. 4; Conclusions p. 8): Inconsistent dataset versions and naming across sections (DR1 vs DR2; DES-Y3 vs DES-Y5; Planck 2018 vs PR4/NPIPE)
- Offending text examples:
  - Sec. V.A (p. 6): “We analyze four dataset combinations: (1) Planck 2018 NPIPE; (2) +DESI 2024 DR1 BAO; (3) +Pantheon+; (4) +SH0ES H0 prior + DES Y3 S8.”
  - Table II caption (p. 4): “DESI DR2 BAO + ... + DES-Y5 + Pantheon+.”
  - Sec. VII Forward paragraph (p. 8): “DESI DR2 + Planck NPIPE + Pantheon+ + DES-SN5YR.”
- Problem: The dataset labels and versions are inconsistent across the paper. “Planck 2018” is PR3 (A&A 641 A6, 2020), whereas “NPIPE/PR4” is the 2022 reprocessing; “Planck 2018 NPIPE” is not a standard name. BAO references alternate between DESI DR1 (2024) and DR2 (2025). SNe discussions switch between DES-Y3 and DES-Y5, and there is also DES-SN5YR. This prevents unambiguous reproducibility and clouds the provenance of the Table II w0wa chain.
- Required fix: Standardize all dataset names and versions consistently throughout the manuscript and tables, and ensure references match. For Planck, specify PR3 vs PR4 unambiguously and the exact likelihood variants (e.g., “Planck PR4/NPIPE low-ℓ (EE/TT), CamSpec high-ℓ TTTEEE (version …), lensing.native”). For BAO, state “DESI DR1” or “DR2” consistently and cite the correct paper. For SNe, use “DES-Y3” or “DES-Y5” consistently, and likewise specify Pantheon+ and DES-SN5YR consistently. If Table II uses DR2/DES-Y5 while Table I uses DR1/DES-Y3, make this explicit and segregate the results by dataset family to avoid confusion.

P1B-E3 (Sec. III, p. 4): Inclusion of reviewer-discussion/meta-review language in the body text
- Offending text: “This addresses earlier reviewer concerns that the reported 67.68 was inconsistent with active SH0ES likelihood…”
- Problem: PRD articles must not contain meta-review narrative. This is internal process language and must be removed.
- Required fix: Remove all references to reviewer concerns or prior-round discussions. Replace with a neutral, self-contained exposition of the SH0ES prior handling and the resulting posterior behavior.

P1B-E4 (References, p. 10): Internal line/round identifiers embedded in bibliography entry
- Offending text in Ref. [15]: “… reports beta = 0.30 +/- 0.11 deg from Planck NPIPE (PR4); the value used at L256/L416 of P1B …”
- Problem: The citation contains internal cross-document line references (“L256/L416 of P1B”) and an internal code (“P1B”), which are not part of standard bibliography formatting and violate PRD style.
- Required fix: Replace Ref. [15] with a standard bibliographic entry (authors, title, journal, volume, page, year, arXiv) without internal project identifiers or line numbers. If you need to say which value you adopted, do so in the body text, not in the reference note.

P1B-E5 (Sec. IV, p. 5–6): β estimator is not specified; pseudo-Cℓ pipeline output lacks a declared estimator definition and uncertainty construction
- Offending text: The section describes masks, binning, beam, purification, and that “βˆNaMaster = 0.238° (pipeline-recovery SNR = 20.32)” is recovered, but no explicit estimator for β is given (e.g., TB/EB cross-spectra based linear estimator; form of MASTER deconvolution; handling of noise bias; bandpower covariance).
- Problem: For methodological validation in PRD, the estimator must be specified. How is β estimated from pseudo-Cℓ bandpowers? Is it the standard minimum-variance linear EB estimator, a likelihood fit in β rotating the spectra, or something else? How is the covariance built (analytic MASTER/Knox, MC-derived)? Without this, the SNR=20.32 and the bias figures (0.032°–0.040°) are not reproducible from the description alone.
- Required fix: Provide the explicit β estimator definition (equations), including how pseudo-Cℓ bandpowers and their covariance enter, what multipole range and binning are used for the fit, how E/B purification modifies the estimator normalization, and how uncertainties are computed (analytic vs MC). If you use an existing public likelihood, cite it and state precisely how you call it. Otherwise, include equations and sufficient algorithmic detail to allow reproduction.

P1B-E6 (Sec. VI and Appendix C, p. 6–7, 9): Reproducibility gap for the ALP MCMC EB-likelihood
- Offending text: Sec. VI claims “Dedicated MCMC sampling of the ALP parameter space … uses the Planck PR4 + ACT DR6 EB-spectrum likelihoods … Cobaya v3.6.1 … R̂ − 1 < 0.01 … 9,720 accepted samples.” Appendix A, however, states: “No CMB polarization map analysis code is provided beyond the NaMaster driver script; all published birefringence values are literature citations.”
- Problem: There is a contradiction. If you have run your own MCMC on an EB-spectrum likelihood combining Planck PR4 and ACT DR6, then either that likelihood code (or a pointer to an existing public implementation including the calibration-covariance matrix you used) must be provided, or you must clarify that you did not re-fit EB spectra and instead used literature posteriors. As written, the analysis is not reproducible.
- Required fix: Either (i) deposit the exact EB-spectrum likelihood implementation (or link to a public one) along with the calibration-covariance matrix and multipole ranges used, and provide run scripts, or (ii) remove claims of having run a bespoke EB-spectrum MCMC and clearly state that you adopted literature constraints for β and only ran the simple ALP-parametric mapping (Caγ, m/H0, θi) → β as a forward model without re-fitting EB spectra. If (i), also add enough detail in Appendix C (ℓ ranges, splits, covariance construction) to enable reproduction.

P1B-E7 (Abstract p. 1; Sec. IV p. 5–6; Sec. VI p. 6–7): Multiple σ-levels from different procedures presented closely; ensure explicit “not directly comparable” qualification at each juxtaposition
- Instances:
  - Abstract: “The primary sky detection significance is the published Planck/ACT DR6 2.4–2.9σ [2, 3]; the pipeline SNR figures refer to recovery of injected MC signals…” (good disclaimer here).
  - Sec. VI: juxtaposes 3.6σ (WMAP+Planck joint) with the author’s pipeline SNR values earlier.
- Problem: The manuscript largely does the right thing, but given the journal’s strict standards, any place where your pipeline SNR appears near an observational σ should again carry the explicit caveat “not directly comparable” to avoid misinterpretation.
- Required fix: Audit the manuscript and, in every location where a pipeline SNR is presented within one paragraph of an observational σ significance (e.g., 2.4–2.9σ or 3.6σ), add the explicit “not directly comparable” disclaimer (statistic definition and data differ).

MAJOR

P1B-M1 (Sec. V.A p. 6; throughout): Ambiguous Planck likelihood nomenclature (“Planck 2018 NPIPE” and “NPIPE CamSpec”)
- Problem: “Planck 2018” (PR3) and “NPIPE” (PR4) are distinct releases. “CamSpec” also has PR3 and PR4 variants. The paper mixes these labels (e.g., “Planck 2018 NPIPE CamSpec TTTEEE”), creating ambiguity.
- Required fix: State precisely which release and likelihood version was used in each run (e.g., “PR4/NPIPE low-ℓ EE/TT; PR4 CamSpec TTTEEE, vX.Y; lensing.native PR4”), with citations and version numbers where applicable.

P1B-M2 (Sec. III, Table I p. 3): Chain-quality reporting is incomplete for 17-parameter space
- Problem: Only worst R̂−1 and min ESS across parameters are reported. Given 17 parameters (7 cosmological + 10 nuisance), additional diagnostics (acceptance fraction per chain, autocorrelation time, per-parameter ESS counts) would help justify that e.g. ΔNeff, H0, τ, and nuisance parameters are well mixed.
- Required fix: Provide an extended chain-diagnostic summary in the Appendix or SM (per-parameter R̂−1 and ESS, acceptance rates). Alternatively, deposit getdist diagnostics in the repo and reference them explicitly.

P1B-M3 (Sec. III p. 4–5): MB–H0 degeneracy check wording overstates “exact” correspondence
- Offending text: “This offset is ∼3.2σ … corresponds exactly to the canonical 3.6σ Hubble tension manifesting in the MB axis…”
- Problem: Your own calculation yields ~3.16σ in MB given σ(MB)=0.049. Calling this “exactly” the canonical 3.6σ is imprecise and may confuse readers.
- Required fix: Rephrase to “is consistent with the canonical ~3.6σ H0 tension when expressed in MB” and, if helpful, show the simple tension calculation in H0-space: (73.04 − 67.69)/sqrt(1.04^2+1.06^2) ≈ 3.6.

P1B-M4 (Sec. IV p. 5–6): “Conservative worst-case bias check” characterization of ACT-like noise is misleading
- Offending text: “The 500 Monte Carlo realizations are drawn at ACT-noise level ΔP = 10 μK·arcmin (a conservative worst-case bias check).”
- Problem: A lower noise level generally increases SNR and can reduce sensitivity to leakage biases; calling a deeper (lower-noise) setting “worst-case” for bias is counterintuitive unless you justify that the bias mechanism you test scales in the opposite way (e.g., mask-induced leakage dominating over noise). As written, it reads as a non sequitur.
- Required fix: Clarify why ΔP = 10 μK·arcmin constitutes a conservative or worst-case choice for the bias being probed, or correct the phrasing to simply report the assumed noise and note its relation to Planck vs ACT depths.

P1B-M5 (Sec. VI p. 6–7): ALP parameter-space and “spectator” status need a clearer, quantitative energy-density bound
- Problem: You correctly note ρa ~ H0^2 MPl^2 θi^2 and that θi ≪ 1 is required for true spectator behavior, but the allowed bound is never quantified. Given that your natural prior covers θi ∈ [0.5, 2], readers need a specific numerical spectator bound (e.g., Ωa < 0.01 or 0.05) to understand what fraction of your prior/parameter space truly qualifies as “spectator.”
- Required fix: State an explicit quantitative bound for “spectator” (e.g., Ωa < 0.01) and show how it maps onto θi, m/H0, and fa. Indicate how this reduces the acceptable parameter space and how it affects the required Caγ to match β.

P1B-M6 (Sec. VI p. 6–7): EB-likelihood calibration covariance is mentioned but unspecified
- Problem: You mention “shared calibration covariance” when combining Planck PR4 and ACT DR6 in the EB-spectrum likelihood. The specific form and numerical values of this covariance are crucial to any joint constraint on β.
- Required fix: Specify the calibration parameters and their covariance matrix, with a citation or a data file in the repository. At minimum, detail which calibration nuisance parameters are marginalized, their priors, and how they propagate into β.

MINOR

P1B-n1 (Abstract p. 1): “2.4–2.9σ” attribution
- Problem: The 2.4–2.9σ range is ascribed to “Planck/ACT DR6” collectively, but your main text then highlights 3.6σ for WMAP+Planck joint and ~2.9σ for ACT. The attribution in the abstract is vague.
- Required fix: Attribute explicitly in the abstract (e.g., “ACT DR6 reports ~2.9σ; WMAP+Planck joint ~3.6σ; Planck-only ~2.7σ”). Or restrict to one cited value with a clear source.

P1B-n2 (Sec. IV p. 5–6): Bandpower and ℓ-range details are terse
- Problem: You state Δℓ = 20 bins from ℓ = 30 to 1024 and fsky = 0.32, but do not report which bins dominate the β fit or whether low-ℓ cuts were tested.
- Required fix: Add a sentence summarizing the ℓ-range sensitivity (e.g., “β constraints are dominated by ℓ ≈ 100–800; raising ℓmin to 70 changes β̂ by X and σβ by Y”).

P1B-n3 (Sec. III, Table I p. 3): Parameter list for Planck nuisance terms is partial/ambiguous
- Problem: The footnote lists Aplanck, several amplitude/noise terms, and calTE, calEE, etc., but it is not clear whether this matches the exact CamSpec PR4 nuisance set.
- Required fix: Provide the full nuisance parameter set and priors used (pointer to YAML is fine), and confirm alignment with the chosen CamSpec version.

P1B-n4 (Sec. VI p. 7): Caγ benchmarks vs KSVZ/DFSZ
- Problem: The statement “the entire required range therefore lies outside minimal ALP benchmarks” is fine, but a citation or a one-sentence quantitative reminder of typical KSVZ/DFSZ Caγ magnitudes would help readers.
- Required fix: Add a citation and a numerical ballpark for KSVZ/DFSZ photon couplings.

P1B-n5 (Appendix A p. 8): Reproducibility run-time statement
- Problem: “~4–12 h per configuration on 4 CPU cores” is useful, but consider adding the tested CPU model(s) to calibrate expectations.
- Required fix: Add a hardware note (e.g., CPU model, RAM) for the stated run-time.

NIT

P1B-N1 (Sec. V.A p. 6): “v3.5 original; v3.6.1 verification”
- Suggestion: Replace with “We used Cobaya v3.6.1; earlier exploratory runs used v3.5.” This avoids implying two sets of results.

P1B-N2 (Throughout): Hyphenation and typography
- Examples: inconsistent use of “high-l” vs “high-ℓ”, “E → B” vs “E→B”; “E-B” vs “E–B”.
- Fix: Standardize notation (ℓ for multipole; E/B with en-dashes where appropriate).

P1B-N3 (Sec. IV p. 5): “C2 apodization at 2° scale”
- Suggestion: Briefly define “C2 apodization” for readers who do not use NaMaster (or cite Alonso et al. for the scheme).

P1B-N4 (Sec. VI p. 6): Units/notation in Eq. (3)
- Suggestion: State explicitly that β is in radians inside the formula, and convert to degrees at the end.

Arithmetic and dimensional checks (spot-audits)

- Table I abstract numbers match the table (H0 and ΔNeff values consistent). Units are consistent (km s−1 Mpc−1).
- Burn-in/sample counts in footnote 1: 176,240 × 0.7 = 123,368; 132,949 × 0.7 = 93,064; total 216,432 — consistent with the text. The 119,617 post-burn-in count after thinning is plausible; the difference is appropriately attributed to thinning.
- MB–H0 degeneracy constant: −19.253 − 5 log10(73.04) ≈ −28.569; −19.263 − 5 log10(67.69) ≈ −28.4155; difference ≈ 0.154–0.155 mag; 0.155 / 0.049 ≈ 3.16σ — correctly reported as ~3.2σ (but do not call it “exactly” the canonical 3.6σ).
- Eq. (3) birefringence normalization: αEM/(4π) ≈ 5.8×10−4; with Caγ=8 and Δϕ/fa≈1.07 ⇒ β ≈ 0.00497 rad ≈ 0.285°; consistent with “≈ 0.29°”.
- βobs = 0.342° ⇒ 5.97×10−3 rad; divided by 5.8×10−4 ⇒ Caγ Δϕ/fa ≈ 10.3; consistent.
- Inverse-variance combination (Planck 0.30±0.11 and ACT 0.215±0.074): β = 0.2415°, σ = 0.0614°; matches Eq. (4).
- Table II σ-distances: (−0.8122 − (−1))/0.0436 ≈ +4.31σ; (−0.6666 − 0)/0.1864 ≈ −3.58σ; (−1.0344 + 1)/0.0301 ≈ −1.14σ. Internally consistent. χ2 sum arithmetic note is correct.

Comments on length and scope
For the claimed contribution (verification companion with three technical checks), 10 pages is acceptable. However, the paper currently mixes multiple dataset generations and contains meta-review language and internal project tags. Once standardized and cleaned, the text should be slightly tightened (removing process narrative and cross-round commentary) but does not obviously require large cuts.

## Summary recommendation
MAJOR REVISIONS

The manuscript contains solid methodological intentions and careful caveats, but several issues prevent acceptance in its present form: inconsistent dataset labeling and references (DR1/DR2, PR3/PR4, DES-Y3/Y5), an incorrect table cross-reference for the “Planck-only” run, inclusion of reviewer/meta-process language, an undefined β estimator in the NaMaster section, and a significant reproducibility gap regarding the claimed Planck+ACT EB-spectrum likelihood MCMC. Addressing the ESSENTIAL and MAJOR items above—standardizing datasets/likelihoods and references, removing meta-review language, explicitly defining the β estimator and supplying or citing the EB-likelihood implementation, and fixing the table cross-reference—should bring the manuscript to PRD methodological standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh pass)

ESSENTIAL

P1B-E8 (Fig. 1 axis labeling and ΔNeff vs Neff inconsistency)
- Issue: The corner plot’s second axis is labeled “Neff” but its tick range is 0.03–0.07, which matches τ, not Neff or ΔNeff. Elsewhere the paper reports and interprets ΔNeff (mean ~ −0.02). The figure thus mixes labels and tick ranges (σ8 appears as “8”; Ωm as “m”), creating ambiguity about what was actually plotted and whether the parameter is Neff or ΔNeff.
- Why it matters: This confuses the central cosmology extension under study and compromises figure interpretability/reproducibility.
- Required fix: Regenerate the corner plot with correct parameter names and tick ranges (use ΔNeff with a range straddling zero; τ with 0.03–0.08; σ8 labeled as “σ8”; Ωm labeled “Ωm”). Ensure the figure matches the text and the YAML variable naming.

P1B-E9 (Broken internal cross-references)
- Instances:
  - Table II footnote (a) refers to “§ Headline-result discussion,” which does not exist.
  - Conclusions (NaMaster paragraph) says “see §VI body text” for the 0.040° bias, but the NaMaster injection–recovery details are in §IV, not §VI.
- Required fix: Replace “§ Headline-result discussion” with a valid section (likely §V, Model-comparison statistics paragraph), and change “§VI body text” to “§IV.”

MAJOR

P1B-M7 (Ambiguity in whether Neff or ΔNeff is sampled and what prior is used)
- Issue: The text repeatedly states the run is “ΛCDM+ΔNeff,” and Table I reports ΔNeff posteriors. Yet Fig. 1 labels an axis “Neff,” and there is no explicit statement of the prior used (flat prior on ΔNeff or on Neff? prior bounds?).
- Why it matters: The choice of sampling Neff vs ΔNeff and the prior bounds can affect posteriors and comparability to other works.
- Required fix: State explicitly which parameter was sampled (Neff or ΔNeff), with exact prior type and bounds. If ΔNeff was a derived parameter (e.g., ΔNeff = Neff − 3.046), say so and show both the sampled and derived quantities in the figure and tables consistently.

MINOR

P1B-n6 (Misclassification of nuisance parameter categories in Table I footnote)
- Issue: The footnote describes “10 Planck likelihood nuisance” parameters but includes Mb (the SN Ia absolute magnitude), which is not a Planck nuisance.
- Required fix: Correct the description to “9 Planck likelihood nuisance + 1 SN nuisance (Mb), totaling 10 non-cosmological nuisance parameters,” or list the full nuisance sets per likelihood explicitly.

P1B-n7 (Corner-plot typography)
- Issue: Axis labels in Fig. 1 are truncated or non-standard (e.g., “8” for σ8, “m” for Ωm).
- Required fix: Use standard symbols (σ8, Ωm) and confirm legibility. This also helps avoid confusion with units and ranges.

P1B-n8 (Abstract footnote content)
- Issue: The abstract contains a long technical footnote (Eskilt & Komatsu dataset disambiguation) with repository-level details. PRD typically discourages extended footnotes in the abstract.
- Required fix: Move the dataset-disambiguation footnote to the main text (e.g., at the start of §VI) and keep the abstract concise.

NO OTHER NEW ARITHMETIC MISMATCHES DETECTED
- Re-computation of all explicitly stated σ-distances, weighted averages, unit conversions, and sample-count arithmetic matches the body text. The only arithmetic-adjacent issue newly flagged here is the corner-plot axis mismatch (E8), which is a labeling/variable-identity problem rather than a numeric inconsistency.

Rationale for “fresh eyes” completeness
- This pass specifically targeted figure labeling vs. body claims (B), cross-references (D), and parameter-definition/prior clarity (A/C/H/I). The newly found issues (E8–E9, M7, n6–n8) were not covered in the initial review and materially improve clarity, reproducibility, and interpretability.