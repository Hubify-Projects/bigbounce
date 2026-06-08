# P1B auto-2026-06-08_1354pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7807 chars)
**Wall time**: 264.1s

---

Referee report on: “Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model”

Scope of review
- Focus: methods rigor, statistical validity, internal arithmetic, dataset specification, estimator definition, and reproducibility.
- I audited every quoted scalar in the abstract, tables, figure, and conclusions against the body text; recomputed simple significance and ratios; checked dimensional consistency and likelihood composition where described.

Overall assessment
The manuscript does a commendable job separating scope-limited proxy tests from theory claims and repeatedly warns against overinterpreting pipeline-MC SNRs as sky detections. However, there are multiple critical issues that must be addressed before this can meet PRD standards for a methods paper:
- Dataset attributions are inconsistent (DESI DR1 vs DR2; DES-Y5 vs DES-SN5YR; Planck PR3 vs PR4/NPIPE) and in places self-contradictory.
- The NaMaster validation lacks a pre-declared estimator definition and does not report the MC variance or uncertainty on the quoted biases; the SNR numbers have no traceable calculation.
- The ALP “EB-spectrum likelihood” description is too vague to be reproducible (multipole ranges, masks, calibration-covariance construction, and exact likelihood sources are unspecified).
- Several instances of version-history/meta language and repository-README deference are unsuitable for a journal article and must be removed.
- A few classification/citation inaccuracies and small arithmetic clarity issues.

Findings and required fixes

ESSENTIAL

P1B-E1
- Section V.A (p. 6), Table II (p. 4), Conclusions (p. 8)
- Problem: Inconsistent and contradictory dataset attributions:
  • Sec. V.A lists “DESI 2024 DR1 BAO [18]” in the analyzed combinations.
  • Table II and surrounding text repeatedly state “DESI DR2 BAO,” and the table caption/rows use “DESI DR2.”
  • Table II uses “+DES-Y5 + Pantheon+” for the SN component, while elsewhere you reference “DES-SN5YR [14]” (a supernova sample) and “DES Y3 S8 [19]” (weak lensing). “DES-Y5” (cosmic shear/clustering) is not the same as “DES-SN5YR.”
- Required fix: Unambiguously state, in one place and consistently throughout, exactly which dataset releases enter each analysis. For every table/section that reports numbers, provide a definitive, self-contained list of active likelihood components (name, version/release, and citation). If Table II used DESI DR2 and DES-SN5YR supernovae (plus or minus Pantheon+), label it accordingly and correct the “DES-Y5” label. If the ΔNeff runs used DESI DR1 rather than DR2, update the text and references or rerun with the stated datasets and update results as needed. This must be fully consistent across the abstract, body, tables, figure caption, and conclusions.

P1B-E2
- Sec. III (p. 2–3), Sec. IV (p. 5), Sec. V.A (p. 6), References [15], [17]
- Problem: Planck dataset and citation inconsistencies:
  • You use “Planck NPIPE CamSpec TTTEEE + lowl TT/EE + lensing” and call it “Planck 2018 NPIPE” in Sec. V.A. “Planck 2018 results VI” [17] is PR3; NPIPE is PR4 (reprocessed maps/likelihoods).
  • The proper references for CamSpec PR4/NPIPE high-ℓ and the NPIPE maps/low-ℓ likelihoods are not given; [17] is not the correct NPIPE reference.
  • Ref. [15] contains an internal editorial note (“the value used at L256/L416 of P1B”), which is not a proper literature citation.
- Required fix: Replace ambiguous “Planck 2018 NPIPE” with the correct Planck PR4/NPIPE citations, and explicitly cite the CamSpec PR4 high-ℓ likelihood source (Efstathiou/Gratton or the appropriate arXiv/journal), the low-ℓ likelihood versions used, and the lensing likelihood release. Remove any internal editorial comments from the reference list (e.g., “used at L256/L416 of P1B”).

P1B-E3
- Sec. IV (p. 5–6), Abstract (p. 1), Conclusions (p. 8)
- Problem: The NaMaster “pipeline-recovery SNR” values (20.32, 25.71) and quoted biases (0.032°, 0.040°) are not reproducible from the text:
  • The primary estimator for β is not defined (what EB-based quadratic/maximum-likelihood estimator? binning? weighting?).
  • No mean ± standard deviation over the 500 MC realizations is reported for β̂; the SNR definition is not given.
  • Without the sample variance of β̂ (and its standard error on the mean), the quoted bias values (e.g., 0.032°) lack uncertainty and cannot be judged significant.
- Required fix: Pre-declare the β estimator explicitly (formula and implementation details), report the MC distribution (mean ± standard deviation; standard error on the mean) for each injection case, and define SNR precisely (e.g., β_injected / σ(β̂), or mean(β̂)/std(β̂)). Provide the numerical σ(β̂) used to compute 20.32 and 25.71 and the associated uncertainties on the bias estimates.

P1B-E4
- Abstract footnote a (p. 1), Sec. II–III (p. 2–3), Sec. V (p. 6)
- Problem: Unsuitable version-history/meta language and repository-deference:
  • “the repository README is the authoritative source for the dataset attribution in the executed pipeline.”
  • “An earlier count erroneously quoted ‘98.6% quintom-B’ weight…”
  • “…prior caveat promised a Savage-Dickey ratio…”
- Required fix: The paper itself must be self-contained and authoritative; remove all meta/version-history language and any deference to a README for critical dataset attributions. Replace with explicit dataset descriptions in the manuscript. Delete mentions of earlier erroneous counts and “promised” analyses.

P1B-E5
- Appendix C (p. 9), Sec. VI (p. 6–7)
- Problem: ALP EB-spectrum likelihood stack is underspecified and not reproducible:
  • “Planck PR4 + ACT DR6 EB-spectrum likelihoods combined with shared calibration covariance” is too vague for reproduction: which spectra (EE, BB, EB?), which ℓ-ranges and masks, how is the shared calibration covariance constructed/parameterized, and from which published likelihood codes/data?
- Required fix: Specify exactly:
  • the spectra included (EB only? any TE/TT?),
  • multipole ranges and binning,
  • masks/f_sky and apodization,
  • calibration/miscalibration parameters and priors,
  • the source and version of the Planck PR4 and ACT DR6 polarization bandpowers/covariances,
  • how the shared calibration covariance matrix is built and combined.
  Provide enough detail that an independent group can reproduce the β_free and β_ALP chains.

P1B-E6
- Sec. IV (p. 5)
- Problem: “ACT-noise level ΔP = 10 μK·arcmin (a conservative worst-case bias check).” Lower noise can inflate detection SNR but does not obviously maximize mask-induced E→B leakage bias; calling this “worst-case bias” is not justified as stated.
- Required fix: Either justify analytically/empirically that the chosen noise level yields a conservative upper bound on the mask-induced β bias, or rephrase to remove the “worst-case bias” claim and simply report the chosen noise level as an input. If the intent is to show that bias is noise-independent within errors, demonstrate this with an additional noise-level test or cite a result establishing that dependence.

P1B-E7
- Sec. III Table I footnote (p. 3)
- Problem: Misclassification of nuisance parameters: “10 Planck likelihood nuisance: … calEE, Mb for the SNIa absolute magnitude.” Mb is not a Planck nuisance parameter.
- Required fix: Correct the classification: list Planck nuisance parameters separately from the SN Ia absolute magnitude Mb.

P1B-E8
- Sec. III (p. 3–4)
- Problem: The “exactly” phrased mapping of the MB–H0 offset to the “canonical 3.6σ Hubble tension” is too strong given the simple one-parameter check performed (“corresponds exactly to the canonical 3.6σ…”).
- Required fix: Rephrase to “consistent with” the canonical tension and avoid “exactly,” or provide a rigorous derivation demonstrating the quantitative mapping (including covariances) if you wish to keep a stronger statement.

P1B-E9
- Sec. V.A/Table I and Fig. 1 caption (pp. 3, 5–6)
- Problem: The “full-tension” combination is used repeatedly but never given a precise, citable definition in the table/caption itself. The figure caption mentions “Planck+BAO+SN+H0+S8,” but Table I does not enumerate the active likelihoods for each column.
- Required fix: For each dataset combination reported (columns of Table I and any figure captions), provide a parenthetical list of the active likelihoods with references and, where applicable, the exact prior values used (e.g., SH0ES H0 prior mean/σ; DES Y3 S8 prior mean/σ). This must be consistent with E1 after you fix the DR1/DR2 and DES-Y5/SN5YR labeling.

MAJOR

P1B-M1
- Sec. IV (p. 5)
- Problem: Planck “Commander” CMB polarization product and beam model are not precisely identified. Commander outputs have specific effective beams and filtering; you assume a 5′ Gaussian at 143 GHz.
- Required fix: State exactly which Commander product (version/release) is used, and cite the corresponding effective beam model. If you approximate it as a 5′ Gaussian, justify that approximation at the degraded Nside = 512 resolution, including the impact of the Npix window, and clarify whether a frequency-averaged or component-separated effective beam is applied.

P1B-M2
- Sec. IV (p. 5–6)
- Problem: No uncertainty is reported on the estimated NaMaster bias values, and the amplitude-dependence claim (“scales mildly”) is qualitative.
- Required fix: Report mean ± standard deviation for β̂ over the 500 MC for each injection value, the standard error on the mean, and formally test/report whether the bias difference (0.032° vs 0.040°) is significant given MC variance. If you intend to carry forward 0.040° as a “systematic floor,” provide its uncertainty.

P1B-M3
- Sec. III (p. 3–4)
- Problem: ΔNeff prior and sampling ranges are not stated.
- Required fix: Report the ΔNeff prior (type and bounds) used in the Cobaya runs. Include priors for all extended parameters and any notable nuisance-parameter priors beyond defaults.

P1B-M4
- Sec. III/Table I (p. 3), Fig. 1 (p. 5)
- Problem: The S8 quantity is reported without definition; the “full-tension” column likely used a DES Y3 S8 prior (as implied elsewhere) but the exact prior is not specified.
- Required fix: Define S8 explicitly and provide the DES Y3 prior mean/σ (and proper citation) if used. Ensure alignment with P1B-E9.

P1B-M5
- Sec. III (p. 3–4)
- Problem: Cross-validation claim with Liu et al. [11] (“agrees at 0.5σ in H0 and 0.4σ in σ8”) is unsupported in-text (no numbers from [11] are given).
- Required fix: Quote the specific H0 and σ8 values (with uncertainties) from [11] alongside your results and show the computed offsets; otherwise remove the quantitative “0.5σ/0.4σ” claim.

P1B-M6
- Sec. VI (p. 7)
- Problem: The statement “The fiducial value β ≈ 0.27° corresponds to the midpoint m ≈ 1.8 H0, Δφ/fa ≈ 1.0” is plausible, but the mapping from (m/H0, θi) to Δφ/fa is not shown beyond one point and a broad envelope.
- Required fix: Provide a compact table or figure (or at least a parametric expression) illustrating Δφ/fa across the stated prior ranges to substantiate the [0.2, 1.1] envelope and the “midpoint” mapping.

P1B-M7
- Conclusions (p. 8)
- Problem: The concluding paragraph mixes “DESI DR2 + Planck NPIPE + Pantheon+ + DES-SN5YR” with the earlier “DES-Y5” and DR1 references; also “GetDist posteriors on w0wa are available” but details of that specific run and likelihood composition are not fully summarized in the main text.
- Required fix: After fixing E1, harmonize this conclusion statement with the corrected dataset attributions and provide a concise parenthetical summary of the active likelihoods for the quoted w0wa chain.

MINOR

P1B-n1
- Sec. III (p. 3–4)
- Problem: Over-precise language: “corresponds exactly to the canonical 3.6σ…”
- Required fix: Replace “exactly” by “consistently reflects,” unless a formal mapping is provided (see E8).

P1B-n2
- Sec. III footnote 2 (p. 3)
- Problem: Ambiguous phrasing “inverse Barbero–Immirzi parameter γBI” followed by “Λstrong ∼ MPl/√γBI.” If γBI denotes the Barbero–Immirzi parameter, “inverse” is confusing.
- Required fix: Clarify notation: define γBI unambiguously and avoid calling it “inverse” if you then use γBI itself in the expression.

P1B-n3
- Sec. V (p. 6)
- Problem: Missing citation for “CMB-S4 (σ(Neff) ∼ 0.03).”
- Required fix: Add a standard CMB-S4 science book reference or equivalent.

P1B-n4
- Table I (p. 3)
- Problem: It would help readers if the table caption explicitly states the code versions (Cobaya v3.6.1; CAMB v1.6.5) and whether low-ℓ TT/EE are PR4/NPIPE or PR3.
- Required fix: Enhance the caption accordingly.

P1B-n5
- Sec. IV (p. 5)
- Problem: “C2 apodization” nomenclature is unclear without context.
- Required fix: Clarify that “C2” refers to NaMaster’s C^2 apodization scheme and specify the exact arguments passed to the apodization routine.

P1B-n6
- Abstract (p. 1), throughout
- Problem: A few small numerical rounding choices differ minimally from recomputations (e.g., naive inverse-variance combined β ≈ 0.243° vs 0.241° quoted).
- Required fix: Either show the exact computation or harmonize rounding in the text.

P1B-n7
- Appendix A (p. 8)
- Problem: The “acknowledges the use of Claude (Anthropic) as an AI research assistant” note is not a methods shortcoming, but journal style typically does not include tooling usage in acknowledgments unless required.
- Required fix: Consider removing or ensuring compliance with PRD policy.

NIT

P1B-nt1
- Typographical consistency: “μK·arcmin,” “ℓmax,” hyphenation of “post-burnin,” capitalization of “NaMaster,” and equation punctuation—minor uniformity/house-style issues.
- Fix: Standardize formatting.

P1B-nt2
- Figure 1 (p. 5)
- Suggestion: Add units to H0 axis label and define S8 in the caption.

Arithmetic/consistency checks performed
- Abstract ΔNeff, H0, σ8, S8 values match Table I.
- ΔNeff uncertainties and means are consistent across text/tables.
- w0 (+0.1878)/0.0436 = 4.31σ; wa 0.6666/0.1864 = 3.58σ; wpivot offset 0.0344/0.0301 = 1.14σ. All consistent with claims.
- MB anchor constant check: −19.253 − 5 log10(73.04) = −28.573 (your −28.571 OK); chain mean −19.263 − 5 log10(67.69) = −28.417 (your −28.416 OK); difference ≈ 0.156 mag (~3.2σ of 0.049), consistent with your text but “exactly” overstates the relation to the canonical H0 tension.
- Naive inverse-variance combination of Planck (0.30 ± 0.11) and ACT (0.215 ± 0.074): mean ≈ 0.243°, σ ≈ 0.0613°, giving ~3.96σ; your 0.241 ± 0.061 (3.9σ) is acceptable but please state the exact weighting used if not simple IVW.
- ALP birefringence normalization: αEM/(4π) ≈ 5.8e-4; β = 0.342° = 5.97e-3 rad ⇒ Caγ Δφ/fa ≈ 10.3 (matches text). With Δφ/fa ∈ [0.2, 1.1], Caγ ∈ [~9.4, ~51.5] (text “∼ 9 to ∼ 51” acceptable).
- Equation of motion for ALP field is dimensionally consistent for V(φ)=m^2 f_a^2 [1 − cos(φ/f_a)].

Length
- The manuscript is 10 pages. Given the scope (three verification analyses), this is reasonable, provided the essential reproducibility gaps and dataset labeling inconsistencies are corrected.

## Summary recommendation
MAJOR REVISIONS

The submission contains several core methodological and documentation issues that must be resolved for PRD standards: inconsistent/incorrect dataset attributions (DESI DR1 vs DR2; DES-Y5 vs DES-SN5YR; Planck PR3 vs PR4/NPIPE), insufficient specification of the NaMaster β estimator and MC variance behind the quoted SNR/biases, and an underspecified ALP EB-spectrum likelihood that is not yet reproducible. There are also instances of version-history/meta remarks that are not suitable for a journal article. Once these are corrected with precise dataset definitions, estimator declarations, uncertainty reporting, and proper citations, the paper can be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes pass)

ESSENTIAL

P1B-E10
- Location: Table II footnote b (p. 4)
- Problem: Arithmetic error and formula misuse for σ(wpivot). You assert σ^2_wpivot = σ^2_w0 + (1 − ap)^2 σ^2_wa = (0.0301)^2 using w0 = −0.8122 ± 0.0436, wa = −0.6666 ± 0.1864, ap = 0.6680. Numerically, (0.0436)^2 + (0.3320)^2 (0.1864)^2 = 0.00573, so σ_wpivot ≈ 0.0757, not 0.0301. The cross-term 2(1 − ap) Cov(w0, wa) cannot be dropped unless Cov = 0 in the original parameterization, which it is not. In addition, the standard decorrelation condition yields ap = 1 + Cov(w0, wa)/Var(wa), not 1 − Cov/Var(wa).
- Required fix: Provide the posterior Cov(w0, wa) and use the correct variance formula Var(wp) = Var(w0) + (1 − ap)^2 Var(wa) + 2(1 − ap) Cov(w0, wa). Recompute ap (with the correct sign convention), zp, and σ(wpivot). Correct the numeric value 0.0301 or justify it with the full covariance.

P1B-E11
- Location: Sec. III, footnote 1 (pp. 2–3)
- Problem: Internal inconsistency about the “Planck-only” run. The text says the 114,992-sample Planck-only run “is reported separately in Table I,” but Table I contains only two columns (Full-tension; Planck+BAO+SN) and no Planck-only column.
- Required fix: Either add the Planck-only column to Table I with its numbers and diagnostics, or revise the text to state that it is not tabulated here (and point to an appendix or repository artifact if applicable).

P1B-E12
- Location: Table III (“Claims classification,” p. 10)
- Problem: It says “β̂NaMaster = 0.238° (500-MC) … MC bias table,” but no MC bias table appears anywhere in the manuscript.
- Required fix: Include the referenced MC bias table (means, standard deviations, and standard errors for each injection), or remove “MC bias table” from Table III.

MAJOR

P1B-M8
- Location: Table II caption and Sec. V (pp. 4, 6)
- Problem: The lensing likelihood is denoted “lensing.native” without specifying PR3 vs PR4/NPIPE, source, or version. Mixing Planck PR3 and PR4 elements can be inconsistent if not handled carefully.
- Required fix: Specify precisely which CMB lensing likelihood is used (release, version, reference) and confirm that it is consistent with the rest of the Planck stack in that run.

P1B-M9
- Location: Abstract (p. 1), Sec. IV (p. 5)
- Problem: fsky = 0.32 is quoted but the construction is undocumented in the text (apodization, thresholding, and how fsky is measured before/after apodization).
- Required fix: In the methods section, report fsky for the unapodized and apodized mask, specify the mask source/footprint and threshold, and give the mask filename hash/DOI. Do not rely solely on a repo path for this.

P1B-M10
- Location: Table II footnote b (p. 4)
- Problem: Likely sign error in the pivot algebra. You write ap = 1 − Cov(w0, wa)/Var(wa). The standard decorrelation giving Cov(wp, wa) = 0 implies ap = 1 + Cov/Var(wa). Your sign choice should be justified with the actual covariance sign; otherwise ap and zp may be incorrect.
- Required fix: State Cov(w0, wa), confirm the sign, and correct ap and zp if needed.

P1B-M11
- Location: Sec. IV (pp. 5–6)
- Problem: “Scales mildly” claim for amplitude-dependent bias is undefined. The bias changes from 0.032° to 0.040° when the injection changes by 0.072°. Calling that “∼12%” is ambiguous (12% of what? of the signal change? of the baseline bias?).
- Required fix: Define the metric explicitly (e.g., Δbias/Δβinj = 0.008/0.072 ≈ 11.1%, or Δbias/baseline bias = 0.008/0.032 = 25%). Report uncertainties (see also P1B-M2 in your prior review).

P1B-M12
- Location: Sec. IV (p. 5)
- Problem: EB rotation injection procedure is underspecified for partial-sky systematics. You state Q + iU → e2iβ(Q + iU) “before adding noise,” but for cut-sky with E/B purification, the order of mask vs. rotation can matter.
- Required fix: State whether the CMB is rotated on the full sky and then masked/apodized, or rotated after masking; whether the noise is rotated; and test/report the impact on the recovered bias.

P1B-M13
- Location: Sec. VI, Eq. (3) (p. 7)
- Problem: Units are implicit. The expression yields β in radians, but the quoted value is in degrees.
- Required fix: Add an explicit note “β on the RHS in radians; converted to degrees for the quoted number” (or present the radian value alongside the degree conversion).

P1B-M14
- Location: Appendix C (p. 9)
- Problem: β prior units in the “βfree” fit are given in degrees [−2°, 2°], while likelihoods often take β in radians. The internal sampler unit is not stated.
- Required fix: State the internal unit used for β in the sampler and at the likelihood interface, and confirm that conversions are handled consistently.

P1B-M15
- Location: Sec. IV (p. 5)
- Problem: Commander beam modeling approximation. You apply a single 5′ Gaussian (143 GHz) to a component-separated Commander polarization map. Commander’s effective beam is not a single-frequency Gaussian.
- Required fix: Justify this approximation quantitatively at Nside = 512 (show β shifts < X° when replacing the true beam by 5′), or use the appropriate effective beam window for the Commander product and cite it.

P1B-M16
- Location: Sec. IV (p. 5)
- Problem: Noise–data mismatch in the MC. You inject ACT-like noise (ΔP = 10 μK·arcmin) onto a Planck Commander map and then quote SNRs. This can mislead readers about achievable significance and may interact with mask/leakage differently than Planck-like noise.
- Required fix: Provide an additional MC at Planck-like polarization noise and show that the bias is noise-independent within errors; otherwise, avoid quoting SNRs based on the ACT-noise setup and frame the test as a pure methodology check.

MINOR

P1B-m1
- Location: Fig. 1 (p. 5)
- Problem: Axis label says “Neff” while the text discusses ΔNeff as the sampled extension.
- Required fix: Relabel the axis to “ΔNeff” or clarify in the caption that “Neff” denotes ΔNeff in this corner plot.

P1B-m2
- Location: Sec. III (p. 3)
- Problem: Broken internal pointer “see § Headline-result discussion” — no such section heading exists.
- Required fix: Fix the pointer to the correct section/subsection or remove the phrase.

P1B-m3
- Location: Sec. IV (p. 5)
- Problem: Causal statement without support: “bias … expected from a 2° apodization scale.”
- Required fix: Either cite a result that connects apodization scale to the observed bias level in EB rotation recovery, or remove “expected” and present it descriptively.

P1B-m4
- Location: Sec. IV (p. 5), Abstract (p. 1)
- Problem: “Commander map removes the very component that breaks the β–α degeneracy” is asserted without citation.
- Required fix: Add a citation (e.g., Minami–Komatsu method) and specify which component/assumption is removed and why that reintroduces degeneracy in your test configuration.

NIT

P1B-nt3
- Location: Sec. IV (p. 5)
- Problem: API spelling and consistency: NaMaster method is compute_coupling_matrix, not “compute coupling matrix” (space). Minor naming inconsistencies can confuse readers trying to reproduce.
- Fix: Standardize function/method names.

P1B-nt4
- Location: Sec. IV (p. 5), throughout
- Problem: Mixed prose/repo-path/date stamps in main text (e.g., “production 500-realization run, April 2026”; specific repo directories).
- Fix: Move such details to Data/Code Availability or SI and provide a DOI/commit hash.

Explanation
These issues were not covered in the initial review. The most critical new finding is the arithmetic/formula inconsistency for σ(wpivot) and potential sign error in ap, which directly undermines the wpivot uncertainty quoted. Additional cross-reference and reproducibility gaps (Planck-only column claim; missing MC bias table; undefined lensing likelihood; Commander beam approximation; noise–data mismatch) also warrant correction for PRD-level rigor.