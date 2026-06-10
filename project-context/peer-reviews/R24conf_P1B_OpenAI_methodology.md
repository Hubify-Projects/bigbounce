# P1B R24conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1b_mcmc_companion_v1B.0.52.pdf` md5=4047dfe1 pages=15
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6644 chars)
**Wall time**: 321.2s

---

Referee report for PRD submission: “Technical Verification Companion to the ECH Spin‑Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator‑ALP Model”

Summary of scope as presented
- Three separate technical checks are reported: (1) stock‑CAMB ΛCDM+ΔNeff MCMC proxy runs (no torsion physics), (2) a NaMaster pseudo‑Cℓ Monte‑Carlo validation of an EB‑based birefringence estimator on synthetic ΛCDM polarization maps, and (3) a consistency check showing that a spectator ALP with fa ~ MPl and m ~ H0 can reproduce the published β ≈ 0.3° isotropic CMB birefringence.
- The manuscript is careful to scope each analysis and to avoid conflating internal pipeline SNRs with sky‑measurement significances. Many numbers in the abstract and conclusions are traceable and arithmetically consistent.

I audited all quoted scalars and key claims against the body text, tables, and figures; recomputed reported σ’s and ratios; checked basic dimensional consistency of formulae; and examined estimator declarations in the NaMaster section.

Findings

ESSENTIAL (must be fixed for PRD)

P1B‑E1 (Sec. VI p. 9; Appendix C p. 13): Version‑history/revision‑log language in the body of the paper
- Problem: Multiple places include “Correction note: an earlier draft … corrected here” and similar revision‑log prose in the main text (e.g., Sec. VI, p. 9; Appendix C, p. 13). PRD articles must not carry internal version history in the scientific narrative.
- Required fix: Remove all references to “earlier draft,” “correction note,” “replaced with the committed truth,” etc. If corrections must be documented for reproducibility, move them to a neutral, non‑historical sentence in Appendix A (reproducibility) or to a formal erratum after acceptance. The main text must read as a self‑contained, final analysis.

P1B‑E2 (Sec. IV p. 6–8; Fig. 3 caption): Primary EB‑rotation estimator is not formally pre‑declared and contains internal inconsistencies
- Problem: The text alternates between an “unweighted χ² template fit” and an inverse‑variance‑weighted fit in the robustness battery. Simultaneously, the paper states that bins above the map band limit ℓ=1024 “carry zero template weight,” which is incompatible with an unweighted χ² unless the template is explicitly set to zero for those bins (not stated). It is also unclear whether the template C^EE entering the fit is theory Cℓ, the decoupled C^EE from the same realization, or a hybrid. These choices materially impact the measured bias.
- Required fix:
  - Pre‑declare a single primary estimator (weighted or unweighted), give its exact formula, and specify its β grid and ℓ‑range.
  - State unambiguously whether C^EE_b used in the template is theoretical (CAMB), realization‑estimated (decoupled), or otherwise, and what is used above ℓ=1024.
  - Reconcile “unweighted” with “zero template weight above ℓmax.” If bins >1024 were included, either show that the template is zero there, or restrict the baseline fit to ℓ≤1024 and report the change. Adopt one baseline choice and carry that consistently through all reported numbers.
  - Keep the inverse‑variance estimator either as the new baseline (it removes ~80% of the bias) or explicitly label it as a cross‑check and justify why the less efficient estimator remains baseline.

P1B‑E3 (Data availability and persistence; Appendix A pp. 12–13; Sec. IV pp. 6–8; Sec. VI pp. 9–11): Long‑term archival access and in‑text file‑path noise
- Problem: The paper relies on GitHub/HuggingFace links and embeds numerous file‑system paths (e.g., “reproducibility/p1_namaster_500mc/results/…”), which are not archival. PRD requires durable, citable data/code deposition (DOI), and the main text should not contain repository path clutter.
- Required fix:
  - Deposit all analysis code, the exact masks, and key artifacts (MC summary CSVs, configuration YAMLs used to produce the reported numbers, and, where practicable, thinned chains) in an archival repository with DOI (e.g., Zenodo), and cite the DOI(s) in the paper. HuggingFace without DOI is insufficient.
  - Move file‑path listings out of the main text into Appendix A or the Supplemental Material. In the main text, refer only to the DOI and dataset names.

P1B‑E4 (Sec. V.A p. 8; Table I p. 3; Sec. III pp. 2–5): Explicit numerical definition and verification of the DES‑Y3 S8 Gaussian prior
- Problem: The “full‑tension” chain is said to include a “DES‑Y3 S8 Gaussian” prior, but the paper does not state the exact central value and σ fed to Cobaya nor show a simple posterior pull check (as was done for SH0ES via MB). Given S8’s role in the conclusions (it remains high), readers must be able to verify the prior is active and correctly implemented.
- Required fix: State the exact Gaussian prior used (central value, σ) and how S8 is defined in the code (mapping to sampled parameters). Add a short posterior‑pull diagnostic (e.g., 1D S8 posterior with and without the prior) or a sentence analogous to the MB check demonstrating it is indeed active.

P1B‑E5 (Table III p. 9; Sec. V.A pp. 8–9): Inconsistent use of Planck lensing likelihoods across chains (.clik vs .native)
- Problem: Table III indicates the iter2 w0wa chain uses planck_2018_lensing.native while the ΛCDM+ΔNeff chains use planck_2018_lensing.clik. This inconsistency can bias model‑comparison impressions and complicate cross‑chain interpretation.
- Required fix: Either (a) re‑run the iter2 chain with the same lensing likelihood flavor used in the ΔNeff chains and update the numbers, or (b) include a short reproducible test showing that swapping .native/.clik causes negligible shifts (<0.2σ) in the headline parameters quoted (w0, wa, H0, σ8, S8). State which flavor is baseline and why.

MAJOR (significant revision required)

P1B‑M1 (Sec. IV pp. 6–8; Fig. 3): ℓ‑binning to 1536 with Nside=512 and lmax=1024
- Problem: The MC uses synfast with ℓmax=1024 but adopts 20 bins up to ℓ=1536. The text asserts these bins carry “noise only,” yet the rotation template depends on C^EE_b which is non‑zero at those ℓ unless explicitly truncated. This matters for the reported 12% multiplicative bias under an unweighted fit.
- Required fix: Clarify precisely how C^EE_b is set for ℓ>1024 in the fit, and repeat the baseline recovery explicitly restricting to ℓ≤1024, reporting any difference with error bars. If no change, explain why (e.g., template truncated at ℓmax). Keep one consistent ℓ‑range choice thereafter.

P1B‑M2 (Sec. V, Table II p. 4): Provide a compact prior/likelihood summary for the iter2 w0wa chain
- Problem: Table II presents w0wa posteriors and χ² breakdown, but the prior definitions (e.g., flat ranges on w0, wa, τ, Σmν assumption, etc.) and DESI DR2 BAO data vector details are only implicit.
- Required fix: Add a concise appendix table listing sampled parameters and priors for the iter2 chain (analogous to Appendix C for ALP), and explicitly state Σmν assumptions and any external priors (e.g., τ).

P1B‑M3 (Sec. III p. 5; Sec. VII p. 12): CMB‑S4 σ(Neff) ≈ 0.03 claim is uncited
- Problem: The statement “CMB‑S4 (σ(Neff) ∼ 0.03)” lacks a citation.
- Required fix: Cite a standard CMB‑S4 sensitivity reference (e.g., CMB‑S4 Science Book or updated design sensitivity paper) and ensure the figure is consistent with the cited configuration.

P1B‑M4 (Sec. VI pp. 9–11; Fig. 4 p. 11; Appendix C p. 13): Prior‑driven nature of ALP parameter posteriors not sufficiently quantified
- Problem: The ALP MCMC uses a single Gaussian summary likelihood on βobs and reports medians for m and C_aγ over very broad priors. Although the text notes prior‑dependence, the presentation risks over‑interpretation.
- Required fix: Overlay 1D prior curves on the posterior marginals (θi, log10 ma, C_aγ) or provide a Kullback–Leibler divergence (prior→posterior) to quantify information gain. Strengthen language that m and C_aγ constraints are largely prior‑driven given a single amplitude datum.

P1B‑M5 (Sec. IV pp. 6–8): “Consistent with ACT‑noise floor” claim is qualitative
- Problem: The phrase “template‑fit SNR consistent with the ACT‑noise floor” is qualitative and not backed by a quantitative mapping.
- Required fix: Either remove that comparison or add a quantitative sentence linking ΔP=10 μK·arcmin to an expected σβ per realization and showing agreement with the measured σβ values, including their fsky scaling.

P1B‑M6 (Sec. II p. 2; Sec. III p. 3): Explicit Σmν assumption should be carried into all summary tables
- Problem: The ΛCDM+ΔNeff chains fix Σmν = 0.06 eV (one massive eigenstate). This materially affects σ8/S8. It appears in the text but not in a visible summary table.
- Required fix: Add a one‑line note to Table I stating Σmν = 0.06 eV, N_massive=1, and BBN consistency for YHe, to avoid ambiguity.

MINOR (address, but does not block acceptance)

P1B‑m1 (Throughout; especially Sec. IV and Appendix A): File‑path “artifact” references clutter the main text
- Problem: Numerous internal paths (e.g., “reproducibility/p1_namaster_500mc/results/c10_…”) distract from the methods narrative.
- Required fix: Move such path references to Appendix A or Supplemental Material; keep the main text clean.

P1B‑m2 (Table I p. 3): State explicitly that the S8 Gaussian prior appears only in the full‑tension chain and give its numerical values
- Required fix: Add a parenthetical in the caption, e.g., “DES‑Y3 S8 Gaussian prior S8=0.776±0.017 applied only in the full‑tension chain.”

P1B‑m3 (Sec. IV p. 6): Clarify ΔP convention
- Problem: It is not stated whether ΔP=10 μK·arcmin is per Stokes map or an effective polarization sensitivity; the note “no √2 factor” could confuse readers given varying conventions.
- Required fix: Add a sentence stating your convention (per Stokes Q and U) and a reference.

P1B‑m4 (Eq. (3) p. 9): State the numerical αEM used
- Required fix: Add “using αEM=1/137.036 and 4π=12.566…” to fix conventions, or cite a standards source.

P1B‑m5 (Fig. 1–3): Verify all axes include units where appropriate
- Required fix: Ensure β is labeled in degrees and all parameter axes are clearly labeled.

P1B‑m6 (Sec. VI p. 9): Cite a source for fa ~ MPl motivation from the Holst sector or move this motivation to the companion paper and simply treat fa as a phenomenological scale here.

P1B‑m7 (Sec. V Table II p. 4): Replace “an unremarkable goodness of fit” with a quantified p‑value or remove the qualitative adjective.

P1B‑m8 (Sec. III p. 5): “getdist‑thinned” should specify the thinning factor or criterion used (ESS‑based, autocorrelation time, etc.).

NIT (cosmetic)

P1B‑n1 (Sec. IV p. 7 footnote 3): Harmonize notation for per‑realization scatter (σβ vs σ_β̂) and avoid mixing.
P1B‑n2 (Sec. IV p. 8): Replace “pod anchor” with neutral phrasing (“baseline run”).
P1B‑n3 (Throughout): Normalize hyphenation and joiners (e.g., “post‑burn‑in” vs “post‑burnin”), ensure consistent use of en/em dashes.
P1B‑n4 (Acknowledgments p. 12): Check PRD policy on acknowledgement of AI tools; if required by the journal, move to a Competing Interests or Author Contributions statement.
P1B‑n5 (Length): Consider moving some long parenthetical clauses to footnotes for readability. The paper could be shortened by ~2–3 pages by relocating implementation details to Appendix/Supplemental without loss of scientific content.

Arithmetic and methodological cross‑checks (selected)
- ΔNeff posteriors in abstract match Table I: −0.020±0.169 (full‑tension) and +0.065±0.17 (Planck+BAO+SN).
- H0 tension: |67.68−73.04|/sqrt(1.06²+1.04²)=3.62σ (stated “3.6σ”).
- S8 tension (Table II vs DES‑Y3): (0.8245−0.776)/sqrt(0.0089²+0.017²)=2.53σ (stated “2.5σ”).
- w0 departure: (−0.8122+1)/0.0436=+4.31σ; wa departure: −0.6666/0.1864=−3.58σ (stated +4.3σ and −3.6σ). wpivot departure: (−0.952+1)/0.019=+2.53σ.
- Pivot decorrelation math checks out: 1−ap=−Cov/Var(wa)=0.210; ap=0.790; zp≈0.27; σ(wpivot)=0.0193.
- MB–H0 degeneracy constant: −18.571 (Riess anchor) vs −18.415 (chain mean); offset 0.156 mag ≈3.18σMB, as stated (~3.2σ).
- NaMaster bias fraction: 0.238/0.27=0.881 (≈12% under‑recovery); 0.302/0.342=0.883 (same).
- Weighted combination of Planck NPIPE and ACT DR6 β yields 0.241±0.061°, 3.95σ; manuscript states 3.9σ and correctly flags correlation caveat.
- ALP rotation: β=(αEM/(4π)) Caγ Δφ/fa; using αEM/(4π)=5.8×10^−4, Caγ=8, Δφ/fa=1.06 gives β=0.00493 rad=0.282°, as stated ≈0.28°.
- Product Caγ Δφ/fa from βobs=0.342°: 0.342°→5.97×10^−3 rad; divide by 5.8×10^−4 gives ≈10.3; consistent with text.
- H0→eV conversion: H0=67.7 km s^−1 Mpc^−1 ≈1.44×10^−33 eV is standard; suggest adding a short footnote/citation (see P1B‑M5).

Overall methodological soundness
- The ΔNeff proxy MCMC and its caveats are appropriate and conservatively framed.
- The EB pseudo‑Cℓ MC is useful as a pipeline check, but the estimator definition needs to be made fully explicit and internally consistent (P1B‑E2, P1B‑M1).
- The ALP “consistency check” is correctly framed as non‑diagnostic for ECH and as prior‑dominated; strengthen quantification of prior‑dependence (P1B‑M4).

## Summary recommendation
MAJOR REVISIONS

The core analyses appear numerically consistent and appropriately scoped, but several methodological and presentation issues prevent acceptance in their current form. Chief among them are the lack of a single, precisely defined primary EB‑rotation estimator (with an inconsistency about high‑ℓ bin treatment), the inclusion of revision‑log language in the main text, the need for DOI‑archived data/code and removal of in‑text file‑path noise, explicit documentation of the DES‑Y3 S8 prior, and harmonization or justification of Planck lensing likelihood choices across chains. Addressing the Essential and Major items above should bring the paper to PRD methodological standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh‑eyes pass)

ESSENTIAL (must be fixed for PRD)

P1B‑E6 (Sec. VI p. 11; Fig. 4/Appendix C): Posterior mass fraction arithmetic error
- Problem: The text states that the strict θi ≤ 0.1 sliver “carries only 0.33% of the posterior mass (42 of the 8,955 raw samples).” The fraction 42/8,955 = 0.469% (≈0.47%), not 0.33%.
- Required fix: Correct the percentage (0.47%) and verify that any derived statements (e.g., “too few for a stable marginal”) remain accurate with the corrected value.

P1B‑E7 (Sec. IV p. 7 fn. 3): Inconsistent β/σβ ratios vs quoted σβ
- Problem: The footnote quotes per‑realization scatters σβ = 0.029° (fsky=0.85) and 0.033° (fsky=0.65) and simultaneously states β/σβ = 8.1 and 7.2, respectively. For β=0.27°, the implied ratios are 0.27/0.029=9.31 and 0.27/0.033=8.18, not 8.1 and 7.2.
- Required fix: Recompute and correct either the σβ values or the β/σβ ratios (and propagate to any text/figures that reference them). Also confirm unit consistency (degrees vs radians) in the internal calculation.

P1B‑E8 (Table I p. 3 footnote; Sec. III p. 3): R̂ − 1 threshold stated with the wrong inequality
- Problem: The footnote claims “all sampled parameters across both frozen combinations satisfy R̂ − 1 < 3 × 10^−3,” while Table I reports a worst value of 0.003 for the Planck+BAO+SN chain (equal to, not below, the bound).
- Required fix: Change to “≤ 3 × 10^−3” or update the reported value with additional sampling if the true worst R̂ − 1 is < 0.003.

MAJOR (significant revision required)

P1B‑M7 (Sec. III p. 5, “Independent cross‑validation”): Ambiguous/incorrect significance formulas
- Problem: The standardized‑difference expressions read “|67.79−68.41|/sqrt(1.092 + 0.322)” and “|0.831−0.812|/sqrt(0.0182 + 0.0062)”, which, as written, omit the squares on the uncertainties and are dimensionally wrong. Even if typesetting intended “σ^2,” this must be explicit.
- Required fix: Correct to sqrt(1.09^2 + 0.32^2) and sqrt(0.018^2 + 0.006^2) in LaTeX, and ensure every such calculation in the manuscript shows the proper squared‑σ form.

P1B‑M8 (Sec. IV p. 8, “Robustness battery and bias attribution”): Unsupported “analytic −CBB template‑mismatch estimate”
- Problem: The text asserts that replacing CBB=0.05CEE with CAMB lensed CBB reduces the bias by “≈5 percentage points of the 12%,” calling this “consistent with the analytic −CBB template‑mismatch estimate above.” No such analytic estimate is actually shown.
- Required fix: Provide a brief derivation (or a one‑paragraph toy model) quantifying the expected multiplicative bias from omitting the −CBB term, or remove/soften the “analytic estimate” claim and present only the empirical robustness result.

P1B‑M9 (Sec. IV p. 7–8): “Unbiased at the |Δβ̂| ≤ 0.040° level” phrasing is self‑contradictory
- Problem: The pipeline is explicitly biased by −0.032° to −0.040°. Calling this “unbiased” is misleading.
- Required fix: Rephrase to “biased at ≤0.040°” or “systematic limited to ≤0.040°,” and keep this wording consistent across the section and figure captions.

P1B‑M10 (Throughout Sec. V/Table II/Refs.): Inconsistent naming of the DES supernova dataset
- Problem: The manuscript alternates between “DES‑Y5,” “DES‑SN5YR,” and the Cobaya block “sn.desy5.” This risks confusion about what SN dataset actually enters Table II.
- Required fix: Standardize the naming (e.g., “DES‑SN5YR (DES‑Y5 SNe)”) at first use, tie it explicitly to the Cobaya likelihood block name, and use one consistent label thereafter.

P1B‑M11 (Sec. IV p. 6–7): SNR template definition omits treatment of bin–bin covariance
- Problem: SNRtmpl ≡ [∑b (C^th_EB,b/σb)^2]^{1/2} is defined with diagonal σb from per‑bin MC scatter. If the decoupled bandpowers are significantly correlated (common in pseudo‑Cℓ pipelines), this SNR is not optimal and can be misinterpreted.
- Required fix: State explicitly that bin–bin covariance is neglected in SNRtmpl, justify the approximation (e.g., show that the off‑diagonal correlations are small in this setup), or switch to a covariance‑aware quadratic form.

MINOR (address, but does not block acceptance)

P1B‑m9 (Sec. V.A p. 8; Likelihoods): Missing citation for the PR4/NPIPE CamSpec high‑ℓ likelihood
- Problem: Ref. [19] is Planck 2018; it is not the PR4/NPIPE CamSpec likelihood reference.
- Required fix: Add the appropriate PR4/NPIPE (CamSpec) likelihood/method reference(s).

P1B‑m10 (Footnote labeling; Sec. VI pp. 9–11; Appendix C p. 13): Re‑used/ambiguous footnote marker “fn. a”
- Problem: “fn. a” is used earlier for an Eskilt–Komatsu dataset clarification and later referenced in a different context, which can confuse readers.
- Required fix: Ensure unique, unambiguous footnote numbering in the final LaTeX (no letter re‑use), and make cross‑references explicit.

P1B‑m11 (Sec. III p. 5; MB–H0 constant): Tiny rounding mismatch
- Problem: −19.263 − 5 log10(0.6768) = −18.417 (to three decimals), not −18.415.
- Required fix: Either recompute with consistent precision (same digits retained as at the Riess anchor) or state the rounding convention; update the printed value if needed.

P1B‑m12 (Conclusions p. 12): “CMB‑S4 will provide the first precision test”
- Problem: The word “first” is over‑strong and ambiguous (Simons Observatory and other Stage‑3/4 forecasts exist).
- Required fix: Replace with a neutral, cited statement (e.g., “CMB‑S4 is forecast to improve σ(Neff) to ≈0.03,” with a proper CMB‑S4 design/sensitivity citation; see also your earlier to‑be‑added citation in P1B‑M3 of the initial review).

NIT (cosmetic)

P1B‑n6 (Table I footnote; Sec. III p. 3): Harmonize the R̂ inequality language
- Problem: See P1B‑E8. Even if the numerical value is retained, use “≤” not “<” for internal consistency.

P1B‑n7 (Sec. III p. 5): Make squared‑σ notation unambiguous
- Problem: “0.0182 + 0.0062” could be misread as decimals rather than σ^2 terms.
- Required fix: Typeset as 0.018^2 + 0.006^2 (LaTeX) or write explicitly “(0.018)^2 + (0.006)^2”.

P1B‑n8 (Sec. IV p. 7): Clarify that SNRtmpl comparison lines (e.g., 33.12 vs 32.98) are percent‑level checks
- Problem: The current prose could be read as exact equality.
- Required fix: Add “within 0.5%” directly in the sentence for immediate clarity.

Explanation
These issues were not covered in the initial review and arose from re‑checking arithmetic, consistency between quoted ratios and variances, precise notation in significance calculations, clarity of footnotes and references, and wording that could mislead readers about bias and comparability. Addressing them will further tighten numerical and procedural rigor to PRD standards.