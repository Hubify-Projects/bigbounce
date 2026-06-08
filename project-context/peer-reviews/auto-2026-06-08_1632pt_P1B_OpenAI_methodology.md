# P1B auto-2026-06-08_1632pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6689 chars)
**Wall time**: 709.9s

---

Referee report for PRD submission: “Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model”

Scope of review
- Focus: methodology rigor (statistical validity, derivation chains, dimensional analysis, internal arithmetic consistency, error propagation).
- I audited all load-bearing scalars in the abstract and conclusions against the body, recomputed quoted σ and combinations, and checked internal consistency of tables/figures.

Overall assessment
- The submission assembles three largely independent technical checks. The basic posterior numbers in Table I are self-consistent, and many arithmetic cross-checks (e.g., inverse-variance combinations, conversion of β to Caγ Δφ/fa) are correct.
- However, there are several essential methodological and sourcing issues that must be addressed before the paper can be considered at PRD standards. Chief among them: inconsistent dataset definitions across sections/tables, an incorrect and mixed citation/attribution for “Planck 2018 NPIPE,” lack of an explicit β estimator in the NaMaster pipeline validation, missing uncertainties and robustness tests for the quoted 0.032–0.040° “systematic floor,” and presence of version-history language. Some claims (e.g., “independent cross-validation” with Liu et al.) lack the quantitative backing needed to verify the stated σ-level agreements.

Findings and required actions

ESSENTIAL

P1B-E1 (Section V.A, p. 6; Table II, p. 4; Fig. 1 caption, p. 5; Abstract, p. 1)
Problem: Dataset inconsistency and ambiguity. Section V.A lists four combinations including “DESI 2024 DR1 BAO” and “DES Y3 S8,” while Table II uses “DESI DR2 BAO + DES-Y5 + Pantheon+,” and the Fig. 1 caption refers to “Planck+BAO+SN+H0+S8” without naming which S8. The abstract references two “frozen dataset combinations” but does not define them precisely.
Required fix: Provide an unambiguous, table-level mapping between each named dataset combination and every reported result:
- Define “Full-tension” explicitly (e.g., Planck PR4/NPIPE high-ℓ TTTEEE + low-ℓ TT/EE + lensing + DESI DR2 BAO + Pantheon+ + SH0ES + DES Y3 S8; adjust to what was actually used).
- Ensure that the dataset labels in Section V.A, Table I, Table II, Fig. 1, and text all match. If some runs used DR1 and others DR2 or DES Y3 vs Y5, separate the results explicitly by stack. Recompute any numbers if the stack was misstated.

P1B-E2 (Section V.A, p. 6; Ref. [17], p. 10)
Problem: Mis-citation and mixing of Planck releases. The paper repeatedly says “Planck 2018 NPIPE,” but NPIPE is the PR4 (2020/2021) data release. Ref. [17] points to Planck 2018 “VI. Cosmological parameters” (PR3), not PR4/NPIPE. The text also mixes “NPIPE” with “CamSpec TTTEEE” (CamSpec PR3 vs PR4 usage must be clarified).
Required fix: Correct all references and labels to Planck releases:
- If NPIPE (PR4) data/products were used, cite the correct PR4/NPIPE releases and likelihoods, and state explicitly which high-ℓ likelihood (CamSpec, Plik, or CamSpec-NPIPE) and versions were used. If CamSpec from PR3 was used with NPIPE maps, justify and cite the appropriate likelihood paper or note any non-standard pairing and its implications.

P1B-E3 (Section IV, pp. 5–6)
Problem: The β estimator is not specified. The NaMaster section describes pseudo-Cℓ deconvolution and MC signal injection but does not define the β estimator (e.g., EB spectrum-based quadratic estimator or full-likelihood fit), the multipole weighting, or the exact ℓ-range used for the estimator (beyond binning).
Required fix: Provide the explicit form of the β estimator used in the MC (e.g., β̂ = argmin L(EB|β), or a weighted least-squares match of EB to sin(2β)E templates), with:
- The ℓ-range actually used in the estimator (not just the spectra computation range).
- The weighting scheme (noise/beam corrected, covariance model).
- A reference implementation (function name in your code repo) or a formula sufficient for reproduction.

P1B-E4 (Section IV, p. 6)
Problem: The reported “pipeline-recovery bias 0.032–0.040°” and SNR values lack uncertainties and robustness diagnostics. With 500 MC realizations, one can quote standard errors on the mean recovered β and quantify sensitivity to mask apodization and purification settings. Declaring 0.040° a “systematic floor” is too strong without these diagnostics.
Required fix:
- Define SNR precisely (e.g., β_inj / σ[β̂] per MC realization, or mean[β̂]/std[β̂], and at what ℓ-range).
- Report mean ± standard error on the recovered β for each injection (e.g., β̂ = 0.238° ± SE from 500 MC).
- Show robustness checks: vary apodization scale (e.g., 1°, 2°, 3°), with/without purify_b, and quantify the impact on the bias and variance. Recast “systematic floor” as “observed bias in this configuration” unless shown robust across settings.

P1B-E5 (Section III, p. 3–4)
Problem: Version-history/internal-review language. Example: “An earlier count erroneously quoted ‘98.6% quintom-B’ weight... promised a Savage-Dickey ratio...” PRD policy: remove version-log language and prior-draft discussion from the paper body.
Required fix: Remove all references to earlier counts, promises, or review-process language. State only the final, verified results and their limitations.

P1B-E6 (Appendix C, p. 9; Section VI, pp. 6–8)
Problem: The ALP MCMC uses “Planck PR4 + ACT DR6 EB-spectrum likelihoods combined with shared calibration covariance” but the construction of the “shared calibration covariance” is not described or cited, and no artifact is linked.
Required fix: Provide a precise description and citation for the joint EB likelihood and the shared calibration covariance model (or place the exact covariance matrix and likelihood specification in the repo, with a stable link and filename). Without this, the βALP and βfree posteriors are not independently reproducible.

P1B-E7 (Section III end, p. 5)
Problem: “Independent cross-validation.—Liu et al. [11] ... preferred by AIC ... Our MCMC agrees at 0.5σ in H0 and 0.4σ in σ8.” No concrete numbers from [11] are provided to reproduce or confirm the 0.5σ and 0.4σ statements, and the models differ.
Required fix: Provide the comparison table with the specific values and uncertainties from [11] and from your runs used to compute the σ-level agreements, or remove the σ-quantified “agreement” claim. If the models differ, state that only a qualitative parameter-level consistency check was made.

P1B-E8 (Section IV, p. 5)
Problem: Beam model for Commander polarization map. The text uses “Planck-2018 effective Gaussian beam (5 arcmin FWHM at 143 GHz),” but the Commander CMB Q/U product is a multifrequency component-separated map with an effective beam that is not simply the 143 GHz beam.
Required fix: Use the correct effective beam window function supplied for the Commander product you analyzed, or justify quantitatively that adopting a 5′ Gaussian at 143 GHz yields negligible error in β recovery. If you used a specific effective beam provided by Planck PR4, state and cite it explicitly.

P1B-E9 (Section V.A, p. 6; Table II, p. 4)
Problem: Inconsistent naming and use of DES samples (DES Y3 S8 vs DES-Y5 and DES-SN5YR). Table II cites DES-Y5 and Pantheon+; Section V.A cites “DES Y3 S8” as part of a dataset combination; the text elsewhere mentions DES-SN5YR. This muddles which DES data were used in which results.
Required fix: Unify DES dataset naming and ensure every quoted result lists the exact DES datasets used (e.g., DES-Y3 3×2pt, DES-SN5YR, DES-Y5 SN, etc.), with consistent references ([14] is DES-SN5YR; add/update a DES-Y5 SN paper reference if used). If you did not include DES Y3 3×2pt in the chains behind Table II, remove it from the Section V.A dataset list.

P1B-E10 (Section VII, p. 8; Abstract, p. 1)
Problem: “CMB-S4 (σ(Neff) ∼ 0.03) will provide the first precision test.” No citation provided.
Required fix: Add a standard CMB-S4 science book forecast citation (or equivalent Stage-4 forecasts) that supports σ(Neff) ≈ 0.03.

MAJOR

P1B-M1 (Abstract, p. 1; Section III, pp. 2–3; Table I, p. 3)
Problem: Prominence of raw accepted sample counts (e.g., “309,189 frozen samples”) is not a standard convergence or precision metric. While you do report R̂ − 1 and minimum ESS in Table I, the headline emphasis on raw sample counts is misleading.
Required fix: De-emphasize raw sample counts in the abstract and body. Report effective sample sizes per parameter (or minimum/median ESS) alongside R̂ − 1 as the primary convergence indicators.

P1B-M2 (Section IV, pp. 5–6)
Problem: Inhomogeneous noise and mask treatment not described. You adopt a single “ACT-noise level ΔP = 10 μK·arcmin” and fsky = 0.32 for Commander, but Commander polarization has strongly inhomogeneous noise, and the EB estimator’s bias/variance are sensitive to weighting. Declaring a configuration-level “systematic floor” without testing noise inhomogeneity is not robust.
Required fix: Describe the noise model and weighting used in the pseudo-Cℓ computation and β estimator. Provide a sensitivity test (e.g., uniform vs hit-count-weighted noise, or using a simple inhomogeneous noise model) and quantify the effect on the recovered bias.

P1B-M3 (Fig. 1 caption, p. 5)
Problem: The dataset stack behind “full-tension” in Fig. 1 is given in prose (“Planck+BAO+SN+H0+S8”) but not explicitly mapped to the YAML config. This complicates reproducibility.
Required fix: Add a pointer to the exact YAML filename in the repo and list the active likelihood blocks (Planck high-ℓ, low-ℓ, lensing, DESI BAO, Pantheon+, SH0ES, DES-Y3 S8 or equivalent). Ensure the figure caption and Section V.A are consistent.

P1B-M4 (Section VI, p. 7; Eq. (3), p. 7)
Problem: Values of Δφ/fa used in Eq. (3) (e.g., “1.07 at m ≈ 2H0”) are not substantiated with a plot or table. They are central to the β prediction.
Required fix: Provide a small figure or table showing Δφ/fa as a function of m/H0 and θi over the prior box used, or at least list the numerically obtained values at the representative points cited (m/H0 = 1, 1.8, 2, 3; θi = 0.5, 1, 2), with the ODE integration setup described (initial conditions, starting redshift, recombination redshift).

P1B-M5 (Section VI, pp. 6–8; Appendix C, p. 9)
Problem: Combining Planck PR4 and ACT DR6 EB spectra “with shared calibration covariance” is nontrivial and central to βALP and βfree. Without enough detail/citation, it is hard to assess.
Required fix: Add details on how the shared calibration nuisance parameters and covariance were modeled (e.g., a joint Gaussian prior with correlation coefficient X between experiments), and cite prior work (e.g., Eskilt & Komatsu for Planck/WMAP joint modeling, and ACT DR6 papers). If this is your own construction, document it in the repo and summarize it in the appendix.

P1B-M6 (Section II, p. 2; Table I, p. 3)
Problem: S8 constraints in Table I (“0.814 ± 0.008” with “full-tension” including S8 and H0 priors) are plausible but sit between Planck+BAO+SN (~0.83) and DES-Y3 (~0.776). If DES Y3 3×2pt was included, a naïve Gaussian combination would yield ≈0.802 ± 0.012 (rough benchmark). Your tighter ±0.008 suggests other high-weight inputs or different S8 definition.
Required fix: Specify precisely the S8 likelihood used (which Y3/Y5 product, priors, and definition) and provide a brief explanation of why the posterior width is ±0.008 (e.g., additional constraining power from lensing or correlations from the full parameter fit) to dispel the impression of double counting or mismodeling.

P1B-M7 (Section III, p. 3; footnote 2)
Problem: The statement “Λstrong ∼ MPl/√γBI” as the torsion-resolution scale for the Holst sector is nonstandard and not justified by a citation that derives this scaling.
Required fix: Provide a derivation or a credible citation establishing this scaling, or remove the formula and keep the qualitative statement that a higher-scale UV completion is required where the contact operator breaks down.

MINOR

P1B-n1 (Throughout)
Problem: Inconsistent notation and formatting: MPl appears with varying typography; “M−2 Pl” vs “MPl−2”; pseudo-Cℓ vs pseudo-C_l; units spacing.
Required fix: Normalize notation (MPl, MPl−2; pseudo-Cℓ consistently), and ensure consistent unit formatting (km s−1 Mpc−1, μK·arcmin).

P1B-n2 (Section III, p. 4)
Problem: τ constraint language. You state τ is a free parameter “constrained by low-ℓ EE + TT likelihoods” but do not list the exact likelihood names/versions in the chain that yielded Table I.
Required fix: Specify the exact Planck low-ℓ likelihoods used (e.g., lowl.EE, lowl.TT names and PR3/PR4 provenance).

P1B-n3 (Section IV, pp. 5–6)
Problem: The phrase “carry forward as the NaMaster systematic floor” overstates generality for one configuration.
Required fix: Rephrase to “the observed bias in this MC configuration was ≤0.040°; we do not claim a universal floor without further configuration scans.”

P1B-n4 (Section VI, p. 7)
Problem: The ALP birefringence relation is used but not written explicitly.
Required fix: Write the relation β = (αEM/4π) Caγ [φ0 − φrec]/fa before Eq. (3) to make the dimensional inputs clear.

P1B-n5 (Acknowledgments, p. 8)
Problem: Use of AI tools in Acknowledgments may require specific wording under APS policy.
Required fix: Ensure compliance with current PRD/APS policy for AI tool acknowledgments (if needed, revise language).

P1B-n6 (References)
Problem: Some references are “in preparation” or “this volume”. PRD prefers publicly available references for load-bearing claims. Here they mostly provide context, but ensure every claim in this paper is supported by publicly accessible sources or by the paper’s own results.
Required fix: Where a claim depends on an in-prep ref, either remove the dependency or add a publicly available citation.

NIT

P1B-N1 (p. 5)
Problem: Minor typography in the corner-plot caption (spacing and punctuation).
Required fix: Clean up formatting; ensure axes and units are fully labeled where applicable.

P1B-N2 (Throughout)
Problem: Very long parentheticals reduce readability.
Required fix: Shorten or move to footnotes.

Arithmetic checks performed (selected)
- Inverse-variance combination (Planck 0.30 ± 0.11 and ACT 0.215 ± 0.074) gives 0.241 ± 0.061 (3.95σ). Matches Eq. (4) claim “0.241° ± 0.061° (3.9σ)”.
- Conversion βobs = 0.342° = 5.97×10−3 rad; α/(4π) ≈ 5.8×10−4 ⇒ Caγ Δφ/fa ≈ 10.3. Matches text.
- w0 deviation: (−0.8122 + 1)/0.0436 = 4.31σ; wa deviation: −0.6666/0.1864 = −3.58σ. Matches “+4.3σ” and “−3.6σ” within rounding.
- SN-degeneracy constant: MB − 5 log10 H0 = −28.571 (Riess anchor) and −28.416 (chain mean), difference 0.155 mag; 0.155/0.049 ≈ 3.16σ. Matches text.

Length guidance
- At 11 pages the manuscript is acceptable in length for PRD provided the essential clarifications and estimator details are added. No reduction needed if the above changes are incorporated; otherwise, consider trimming background prose once methods are clarified.

Summary recommendation
MAJOR REVISIONS

The paper’s numerical values are largely self-consistent, and the scope limitations are appropriately stated. However, core methodological and sourcing issues must be fixed for PRD standards: unify and correctly cite dataset stacks (Planck PR4/NPIPE vs PR3, DES Y3 vs Y5), define the β estimator and its weighting precisely, quantify uncertainties and robustness for the reported NaMaster bias, remove version-history language, and document the joint Planck–ACT calibration covariance used in the ALP MCMC. These are fixable but essential to ensure rigor and reproducibility.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (new issues only)

ESSENTIAL

P1B-E11 (Table II, p. 4; wpivot paragraph)
Problem: Incorrect decorrelation formula and propagated uncertainty for wpivot. The text defines ap = 1 − Cov(w0, wa)/Var(wa) and then uses σ^2(wpivot) = σ^2(w0) + (1 − ap)^2 σ^2(wa), claiming it reproduces 0.0301. That expression omits the 2(1 − ap) Cov(w0, wa) term and cannot reduce the variance below σ(w0); numerically, with 1 − ap = 0.332, σ(w0) = 0.0436, σ(wa) = 0.1864, it gives √[0.0436^2 + (0.332·0.1864)^2] ≈ 0.0757, not 0.0301. The correct decorrelation requires ap = 1 + Cov/Var and σ^2(wpivot) = σ^2(w0) − Cov^2/Var(wa).
Required fix: Replace the ap definition with ap = 1 + Cov(w0, wa)/Var(wa) and give the correct variance formula including the covariance term. Provide the actual covariance numbers used and recompute wpivot and its ±σ. If the quoted 0.0301 came from GetDist directly, say so and remove the incorrect back-of-envelope derivation.

P1B-E12 (Section III fn. 1, p. 3; Section VII, p. 8; Table I, p. 3)
Problem: Broken internal cross-reference. The text twice says the “Planck-only” run is “reported separately in Table I,” but Table I has only two columns (Full-tension, Planck+BAO+SN) and no Planck-only column.
Required fix: Either add the Planck-only results as a third column in Table I or delete the claim that it is “reported in Table I.” If reported elsewhere, give the exact table/figure label or repo filename.

P1B-E13 (Section VI, p. 7; Appendix C, p. 9)
Problem: Inconsistency in βfree configuration counting. The main text states “βfree … 9,720 accepted samples across the 3 ALP-MCMC configurations … Caγ = 4, 8, 12,” but Caγ is irrelevant when β is sampled as a free amplitude. Reporting three configurations for βfree is confusing and inflates the sample-count narrative.
Required fix: For the model-independent βfree fit, report a single configuration (no Caγ) and its accepted-sample count; if you actually ran three redundant chains, clarify that they are statistically identical and merged only for numerical stability, or collapse to one. Update counts accordingly.

MAJOR

P1B-M8 (Section IV, pp. 5–6; Methods)
Problem: Map downgrade/beam/noise inconsistency and potential aliasing. You degrade Commander Q/U from Nside=2048 to 512 and apply only the pixel window, while assuming a 5′ Gaussian beam and adding uniform “ACT-level” noise (10 μK·arcmin). This mixes a Planck-resolution beam with ACT-like noise and omits pre-smoothing before downgrading, risking aliasing and bias in EB. Declaring the result a “conservative worst-case bias check” is not substantiated.
Required fix: Pre-smooth to ≳2× the Nside=512 Nyquist scale before downgrading, use the proper Commander effective beam (or justify quantitatively the 5′ choice), and test a realistic inhomogeneous noise/hit-count weighting. Quantify the impact on β̂ bias/variance under these fixes.

P1B-M9 (Section V, p. 6; Abstract)
Problem: Mixed Cobaya versions without clear provenance. You state “v3.5 original; v3.6.1 verification” but do not tie which version produced the headline posteriors (Table I/II) and Fig. 1.
Required fix: State explicitly which Cobaya version and CAMB tag were used for each reported result (Table I, Table II, Fig. 1), and confirm no material differences between versions for those stacks.

MINOR

P1B-m7 (Table I footnote a, p. 3)
Problem: Misclassification of Mb as a “Planck likelihood nuisance.” The list says “10 Planck likelihood nuisance: … calEE, Mb,” but Mb belongs to the SN likelihood.
Required fix: Relabel Mb correctly as an SN nuisance parameter; adjust the “Planck nuisance” count accordingly.

P1B-m8 (Table I footnote a, p. 3)
Problem: Inequality vs rounding mismatch. You state “all … satisfy R̂ − 1 < 3×10−3,” yet the Planck+BAO+SN column reports 0.003. If this is rounded, the strict “<” is misleading.
Required fix: Replace by “≤ 3×10−3” or give unrounded maxima.

P1B-m9 (Table II, p. 4; likelihood listing)
Problem: Ambiguous likelihood label “lensing.native.”
Required fix: Provide the exact Planck lensing likelihood name/version (e.g., Planck 2018 lensing likelihood, NPIPE lensing if applicable) to avoid ambiguity.

P1B-m10 (Section VII, p. 8; Methods style)
Problem: Run-date/process chatter (“production 500-realization run, April 2026”; “16-rank mpirun process terminated…”) is not standard PRD style.
Required fix: Move such operational details to the repo README or an online note; keep the paper methods time-agnostic.

NIT

P1B-N3 (Section IV, p. 6)
Problem: “∼ 12% amplitude-dependent component” for the bias is unclear/mismatched. The bias shifts from 0.032° to 0.040° (a 25% change in the bias itself) or ~3% relative to the injected 0.27° signal, not 12%.
Required fix: Specify the denominator and correct the percentage (e.g., “a 25% change in the bias” or “a 3% change relative to the injected signal”), or drop the percent.

P1B-N4 (Ref. [15], p. 10)
Problem: Likely mis-attribution and extraneous cross-paper note. The PR4/NPIPE Planck birefringence PRL is commonly associated with Minami et al.; your [15] includes a non-standard author list and references “value used at L256/L416 of P1B,” which is out of scope here.
Required fix: Verify the correct bibliographic entry for the Planck PR4 birefringence result and remove cross-references to “P1B” line numbers.

Rationale for additions
- A (Arithmetic): The wpivot decorrelation/variance derivation is mathematically inconsistent and numerically wrong; the claimed ±0.0301 cannot follow from the stated formula and numbers.
- B (Figure-caption vs body): The Planck-only/Table I cross-ref is an internal inconsistency between body text and the displayed table.
- C (Dimensional): No new dimensional errors found beyond the wpivot statistical formula issue.
- D (Cross-refs): The Planck-only/Table I mis-reference and βfree/three-config mismatch are new internal-reference problems.
- E (Null comparability): No new juxtaposition issues beyond those already flagged previously; your caveats are adequate where given.
- F (Abstract faithfulness): The abstract’s claims are broadly reflected in the body; the wpivot variance problem affects Table II interpretation, not the abstract directly.
- H (Hedges): The “conservative worst-case” claim for the NaMaster bias lacks quantitative backing given the map/beam/noise mismatch; now flagged under M8.
- I (Appendix vs main): The βfree/three-config inconsistency arises between Sec. VI and Appendix C; now flagged.
- J (Stale numbers): The wpivot σ and “reported in Table I” Planck-only note appear to be stale/copy artifacts; now flagged.

Please address these in addition to the issues listed in the initial review.