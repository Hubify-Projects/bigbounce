# P1B auto-2026-06-06_0021pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6950 chars)
**Wall time**: 306.1s

---

Referee report on “Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+∆Neff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model” (tag: P1B)

Overall scope and standard
This is a methods-focused companion paper reporting three technical components: (i) a stock-CAMB ΛCDM+∆Neff MCMC proxy; (ii) a NaMaster pseudo-Cl pipeline validation via MC bias injection for β recovery; (iii) a spectator-ALP birefringence consistency check. The authors repeatedly and clearly scope what is and is not claimed. However, there are several essential methodological gaps, internal inconsistencies, and presentation issues that prevent acceptance in PRD in its current form. Below I itemize all issues with required fixes.

Findings

ESSENTIAL

P1B-E1
- Location: Sec. IV (pp. 5–6), Eq. (1) and surrounding text
- Problem: The birefringence estimator used to recover β from pseudo-Cl EB spectra is not specified. The paper reports β̂ values and SNRs (e.g., “β̂NaMaster = 0.238° (pipeline-recovery SNR = 20.32)”) but does not declare the estimator, fitting procedure, or weighting used. It is not clear if the standard small-angle relation CℓEB ≈ 2β CℓEE was used, whether a maximum-likelihood or regression estimator was applied, how bandpower covariance was estimated, whether E/B purification modifies the response, or how the uncertainty σ(β̂) was computed. Without the explicit estimator and error model, the SNR numbers are not auditable or reproducible.
- Required fix: Add a dedicated subsection: define the β estimator explicitly (formula connecting CℓEB, CℓEE, mask/beam coupling, and β), state the bandpower covariance model, the weighting used in the fit, the treatment of E/B purification in the response, and how σ(β̂) and SNR were computed across the 500 MC realizations. Provide the recovered distribution’s mean and standard deviation for each injection (β = 0, 0.27°, 0.342°). Include (or cite) the exact joint-likelihood when combining Planck PR4 and ACT DR6 EB spectra for the ALP fits.

P1B-E2
- Location: Dataset and likelihood naming throughout; Sec. V.A (p. 6), Table II (p. 4), Sec. III (pp. 2–4), Sec. VII (p. 8)
- Problem: Inconsistent and contradictory dataset/likelihood attributions:
  - Sec. V.A lists “Planck 2018 NPIPE [17]” but Ref. [17] is Planck 2018 PR3 cosmological parameters (Aghanim et al. 2020) and is not NPIPE PR4. The text elsewhere mixes PR3 (CamSpec high-ℓ) with PR4/NPIPE claims.
  - Sec. V.A lists DESI 2024 DR1 BAO; Table II is labeled “DESI DR2 BAO”; Sec. VII mentions “DESI DR2 + ... + DES-SN5YR” while Table II caption says “DES-Y5” and the reference [14] is DES-SN five-year. These are distinct datasets.
  - Sec. III states a third “Planck-only” chain is “reported separately in Table I,” but Table I has only two columns (Full-tension, Planck+BAO+SN). The Planck-only chain is not shown.
  - Sec. VII Conclusion refers to a bias value location “see §VI body text” for the NaMaster pipeline, but the pipeline study is §IV.
- Required fix: Harmonize all dataset/likelihood labels and references:
  - Clearly and consistently specify whether PR3 or PR4/NPIPE products are used, and for which likelihood components (low-ℓ TT/EE, high-ℓ CamSpec, lensing). Cite the correct Planck likelihood papers for the specific versions used.
  - Resolve DR1 vs DR2 BAO and DES Y5 vs DES-SN5YR inconsistencies. Use a single consistent set in text, tables, and references. If multiple were used in different sections, state that explicitly and keep the labels accurate in each place.
  - Either add the Planck-only column to Table I or correct the text to state it is not reported in the table.
  - Fix the cross-reference in Conclusions to point to §IV (not §VI) for the NaMaster bias values.

P1B-E3
- Location: Sec. IV (p. 6), paragraph discussing amplitude-dependent bias
- Problem: Numerical inconsistency. The text states the bias changes from 0.032° (βinj = 0.27°) to 0.040° (βinj = 0.342°), calling this a “relative ∼12% amplitude-dependent component.” The relative increase is (0.040−0.032)/0.032 = 0.25 = 25%, not 12%.
- Required fix: Correct the 12% to 25% (or present the precise number and its uncertainty from the 500 MC).

P1B-E4
- Location: Sec. VI (p. 7), Eq. (3)
- Problem: Unit/angle conversion is not stated. The expression “β ≈ αEM × 8/(4π) × 1.07 ≈ 0.29°” is dimensionally a value in radians on the LHS; the RHS is presented in degrees without indicating the rad→deg conversion factor. This is a presentation error that can confuse readers and precludes independent checking at a glance.
- Required fix: State clearly that β[radians] = (αEM/(4π)) Caγ (∆ϕ/fa). Then either keep everything in radians or explicitly multiply by (180/π) to report degrees. Show the intermediate numeric step (e.g., β ≈ 0.00499 rad = 0.286°).

P1B-E5
- Location: Sec. IV (pp. 5–6), “Beam and pixel window” paragraph
- Problem: The effective beam used for the Planck Commander CMB polarization map is stated as “Planck-2018 effective Gaussian beam (5 arcmin FWHM at 143 GHz)” with a degradation to Nside=512. Commander CMB maps are component-separated products with non-trivial effective beams, not single-frequency 143 GHz beams. Using a 5′ Gaussian 143-GHz beam for a Commander map is not justified here and can bias the response unless demonstrated negligible at Nside=512 and ℓmax=1024.
- Required fix: Justify the beam choice with a citation to Planck PR3/PR4 Commander beam documentation, or change to the appropriate Commander effective beam. Alternatively, demonstrate (e.g., by a short test or citation) that at Nside=512 and the specified binning, the beam mismatch induces negligible bias in β recovery compared to the reported 0.032–0.040° systematic floor.

P1B-E6
- Location: Throughout (e.g., Sec. III, p. 3; Sec. IV, p. 5; Sec. VII, p. 8), and References [15], [22]
- Problem: Internal-process and version-history language inappropriate for a PRD article:
  - Reference [15] contains “the value used at L256/L416 of P1B,” which appears to be internal line-number bookkeeping.
  - Sec. III contains “an earlier count erroneously quoted ‘98.6% quintom-B’ weight...” — version history that should not appear in the final text.
  - Sec. III includes “This addresses earlier reviewer concerns...” — references to the review process are not appropriate in the manuscript.
  - Reference [22] includes editorial commentary about how it is used in P1A; references must be neutral bibliographic entries.
- Required fix: Remove all internal line-number notes, version-history comments, and references to reviewer concerns. Clean the bibliography to standard references without commentary about usage in other manuscripts.

P1B-E7
- Location: Sec. III (p. 4), Table I footnote a
- Problem: Mislabeling of nuisance parameters. The footnote says “10 Planck likelihood nuisance: Aplanck, amp143, amp217, amp143×217, n143, n217, n143×217, calTE, calEE, Mb for the SNIa absolute magnitude” — but Mb is not a Planck nuisance parameter; it is a SN nuisance parameter.
- Required fix: Correct the description to “9 Planck likelihood nuisance parameters plus Mb (SN absolute magnitude), totaling 10 nuisance parameters,” or list them in two groups.

MAJOR

P1B-M1
- Location: Sec. IV (pp. 5–6), “Independent verification” paragraph and Eq. (1)
- Problem: SNRs are quoted (20.32, 25.71) without explicitly giving the recovered σ(β̂) from the 500-MC ensemble. Readers cannot verify the SNR calculation or propagate uncertainties.
- Required fix: Report the β̂ mean ± standard deviation for each injection, and show how SNR was computed (mean divided by ensemble σ). Include a brief check that 500 MC ensures ≤10% relative error on σ(β̂) [~√(2/(N−1))].

P1B-M2
- Location: Sec. VI (pp. 6–7), “shared calibration covariance” and ALP fits; Appendix C (p. 9)
- Problem: The “shared calibration covariance” used to combine Planck PR4 and ACT DR6 EB-spectrum likelihoods is mentioned but not defined or cited. Without an explicit likelihood expression or a clear reference to a reproducible implementation, the ALP MCMC setup remains underspecified.
- Required fix: Provide the explicit form of the joint likelihood (or cite a standard reference/code) and list the calibration parameters and their priors included in the shared-covariance treatment. Clarify whether instrument polarization-angle priors are used and how degeneracies with β are handled.

P1B-M3
- Location: Sec. III (p. 5), “MB–H0 joint-posterior offset check”
- Problem: The text claims the 0.155 mag offset “corresponds exactly to the canonical 3.6σ Hubble tension manifesting in the MB axis.” From the numbers given, 0.155/0.049 ≈ 3.16σ, not 3.6σ; “exactly” is overstated and numerically off.
- Required fix: Replace “exactly” with a quantitatively correct statement (e.g., “~3.2σ along the MB axis, consistent with the well-known ~3.6σ H0 tension when expressed in H0 units”) and, if desired, show the corresponding transformation to H0 to support the comparison.

P1B-M4
- Location: Sec. IV (p. 5), “Foreground and noise model”
- Problem: The noise model adopts ACT-like polarization noise (ΔP = 10 μK·arcmin) for MC on a Planck Commander CMB map and calls it a “conservative worst-case bias check.” Lower noise is not a worst-case for detection SNR or for bias visibility; it can artificially inflate SNR. The choice may be fine for a methods test, but the rationale is misstated and the consequences for SNR should be acknowledged.
- Required fix: Rephrase to accurately describe the motivation (e.g., “we use low noise to probe algorithmic bias independent of noise variance; this inflates SNR relative to Planck but does not affect the mean bias”) and, if possible, include a brief sensitivity check (e.g., one higher-noise MC setting) to show the bias is insensitive to the noise level at the reported scale.

P1B-M5
- Location: Sec. VI (p. 6), headline observational constraint paragraph and Eq. (4)
- Problem: Mixing significance figures from different procedures is generally handled carefully in the text, but where multiple σ-values are juxtaposed (e.g., the 3.6σ WMAP+Planck joint result and the 3.9σ inverse-variance combine), the caveat appears only once. For PRD standards, every such juxtaposition should explicitly flag non-comparability (different systematic treatments).
- Required fix: Ensure that whenever two significances from different null procedures are quoted side-by-side, there is an explicit note that they are not directly comparable because of differing systematic/error treatments (you already do this once—please replicate the caveat at each juxtaposition).

P1B-M6
- Location: Sec. III (p. 5), “Independent cross-validation”
- Problem: The statement “Our MCMC agrees at 0.5σ in H0 and 0.4σ in σ8” references Liu et al. [11] but provides no numbers for Liu et al. or for the exact comparisons. This is not traceable.
- Required fix: Quote the specific H0 and σ8 values (±σ) from Liu et al. and from your chains, and show the numerical differences in σ-units. If the datasets differ significantly between the two works, state this explicitly and qualify the comparison accordingly.

MINOR

P1B-m1
- Location: Sec. IV (p. 6), end of pipeline paragraph
- Problem: “The deconvolution is therefore unbiased at the 0.04° level...” This uses “unbiased” while reporting a nonzero bias up to 0.040°.
- Required fix: Reword to “biased below 0.04° (worst case 0.040° at βinj = 0.342°), which we take as the systematic floor of the method.”

P1B-m2
- Location: Figure 1 (p. 5) caption and axes
- Problem: The H0 axis label in the corner plot does not show units in the axes themselves; only the caption mentions units. This is common practice but avoidable ambiguity.
- Required fix: Add units [km s−1 Mpc−1] to the H0 axis labels in the plot if re-rendering figures is feasible; otherwise, ensure the caption clearly states units once (it already does).

P1B-m3
- Location: Sec. V.A (p. 6)
- Problem: The four dataset combinations list includes DES Y3 S8 prior [19]; the “full-tension” figure caption refers to “+H0+S8,” whereas Table I labels the column simply “Full-tension.” The mapping between names and YAMLs in the repo is not spelled out here.
- Required fix: Add a one-sentence mapping in the main text (e.g., “Full-tension corresponds to Planck+BAO+SN+H0+S8”) and ensure all labels are used consistently across text, figure captions, and Table I.

P1B-m4
- Location: Sec. VI (p. 7), paragraph on Caγ range
- Problem: The dependence of required Caγ on θi is described qualitatively; a single illustrative numeric example would help clarity (e.g., show Caγ required for θi = 0.1 vs 0.5 at fixed β).
- Required fix: Add one line with a concrete numeric example to illustrate the scaling Caγ ∝ 1/(∆ϕ/fa) ∝ 1/θi in the underdamped regime.

P1B-m5
- Location: Sec. II–III (pp. 2–4)
- Problem: CMB-S4 σ(Neff) ≈ 0.03 is quoted without citation.
- Required fix: Add a citation to a CMB-S4 forecast paper or collaboration document supporting σ(Neff) ≈ 0.03.

NITS

P1B-n1
- Location: Sec. III (p. 4)
- Problem: Wording “promised a Savage-Dickey ratio...” is informal.
- Required fix: Rephrase as “we initially planned a Savage–Dickey ratio; however, ...”

P1B-n2
- Location: Appendix A (p. 8)
- Problem: “docs/KNOWN GAPS.md—honest disclosure of what cannot currently be reproduced.” The wording is informal for a PRD paper.
- Required fix: Rephrase to “documentation of current reproducibility limitations.”

P1B-n3
- Location: References [1], [4]–[6]
- Problem: Multiple “in preparation” and “this volume” references. While allowed, this should be minimized and clearly segregated from claims that require published evidence.
- Required fix: Keep these only where strictly necessary for context and ensure no load-bearing claim in P1B depends on unpublished work.

Arithmetic audits and consistency checks
- Table I values (H0, ΔNeff, σ8, S8, Ωm, τ, ns) are self-consistent and match the abstract. R̂−1 values and ESS are plausible for the reported chain sizes.
- Footnote 1 chain arithmetic checks out: 176,240×0.7=123,368; 132,949×0.7≈93,064; sum ≈ 216,432 post-burn-in across two frozen combos. The getdist-thinned 119,617 samples for the plot are plausible.
- Table II departures: w0 = −0.8122±0.0436 → |Δ|/σ ≈ 4.31σ; wa = −0.6666±0.1864 → 3.58σ; wpivot = −1.0344±0.0301 → 1.14σ; consistent with text.
- Inverse-variance combine of βPlanck = 0.30±0.11 and βACT = 0.215±0.074 yields β = 0.2415±0.0613 (3.94σ), consistent with Eq. (4); authors correctly caution non-comparability with the 3.6σ WMAP+Planck joint result.
- ALP product Caγ(∆ϕ/fa) ≈ 10.3: β = 0.342° = 5.966×10−3 rad; α/(4π) ≈ 5.8×10−4; 5.966e−3 / 5.8e−4 ≈ 10.3; range Caγ ≈ 9–51 for ∆ϕ/fa ∈ [1.1, 0.2] checks out.
- MB–H0 constant computation: −28.571 vs −28.416 (difference ≈ 0.154 mag) matches within rounding; the “exactly corresponds to 3.6σ” wording is overstated (see P1B-M3).

Length and focus
At 10 pages, the paper is concise for three technical verifications. However, once the essential methodological details (β estimator, likelihood combination) and dataset-label fixes are incorporated, the core content should still fit within ~12 pages. Please remove review-process and version-history commentary to maintain a professional archival tone.

## Summary recommendation
MAJOR REVISIONS

The paper presents useful technical checks and is careful about scope, but several essential issues prevent acceptance. Most critically, the birefringence estimator and joint-likelihood methodology are not sufficiently specified to audit the quoted β̂ and SNR values; dataset/likelihood naming is inconsistent (PR3 vs PR4/NPIPE, DR1 vs DR2, DES-Y5 vs DES-SN5YR); numerical and reference cross-references contain errors; and there is inappropriate version-history/reviewer language in the text and references. These are all fixable. With the requested corrections and clarifications, the manuscript could meet PRD methodological rigor.

---

## PASS 2 — self-critique findings (what initial review missed)

P1B-E8
- Location: Sec. IV (pp. 5–6), “Beam and pixel window” and map downgrade description
- Problem: The Nside=2048 → 512 downgrade procedure is not specified beyond “apply the corresponding pixel window function.” Without an explicit pre-smoothing/low-pass step before ud_grade (or equivalent), harmonic aliasing is expected at ℓ ≳ few×Nside. This can bias E/B separation and EB response at the stated ℓmax=1024. The paper does not describe any anti-alias filter, beam convolution applied prior to degrade, or checks that aliasing is negligible for β recovery.
- Required fix: Document the exact downgrade pipeline (e.g., Gaussian smoothing FWHM X arcmin to bandlimit to ℓcut, then healpy.ud_grade with power=True), and demonstrate that, with this filtering, residual aliasing is negligible for β (e.g., by toggling the pre-smoothing and showing Δβ̂ well below the 0.032–0.040° systematic floor). If no pre-smoothing was used, add it and re-run the 500-MC test.

P1B-E9
- Location: Figure 1 and its caption (p. 5)
- Problem: Axis labeling inconsistency. The corner plot axis is labeled “Neff” but the analysis samples ΔNeff. The plotted posterior is centered near zero and spans negative values, which is consistent with ΔNeff, not Neff. This mislabeling propagates confusion between Neff and ΔNeff in a key figure.
- Required fix: Relabel the axis to “ΔNeff” in the figure, and ensure all text and captions consistently refer to ΔNeff throughout.

P1B-E10
- Location: Table III (p. 10) and surrounding text
- Problem: Table III entry “β̂NaMaster = 0.238° (500-MC) — Pipeline; MC bias table” implies the existence of an MC bias table, but no such table appears in the manuscript or appendices, and no figure/tabulated distribution of β̂ across realizations is provided.
- Required fix: Include the referenced MC bias table (means, standard deviations, and biases for βinj = 0, 0.27°, 0.342°), or remove/rename the reference in Table III and add the statistics in text per P1B-M1.

P1B-M7
- Location: Sec. V.A (p. 6), Secs. II–III, Table II (p. 4), and References [17], [15]
- Problem: Beyond inconsistent labeling (flagged in P1B-E2), the methodology appears to hybridize Planck releases without justification: PR4/NPIPE elements are described for low-ℓ and for birefringence, while CamSpec high-ℓ TTTEEE is a PR3-era likelihood. Mixing PR4 low-ℓ with PR3 high-ℓ products is non-standard and can lead to subtle inconsistencies unless the hybridization is explicitly validated (many collaborations avoid cross-release hybrids).
- Required fix: State clearly which Planck likelihood versions are used (PR3 vs PR4/NPIPE) for each component and justify the cross-release combination (or switch to a self-consistent single-release stack). Cite the specific likelihood papers/versions. If a hybrid is retained, add a brief validation that parameter shifts are negligible relative to quoted uncertainties for the ΛCDM+ΔNeff chain.

P1B-M8
- Location: Sec. IV (pp. 5–6), “Independent verification” and estimator SNR discussion
- Problem: The 500-MC ensemble appears to vary only the noise on a single fixed CMB sky (the Commander map). Thus, the reported σ(β̂) and SNR exclude sky (cosmic-variance) and EB sampling covariance contributions from the stochastic CMB E field. For an EB∝β EE estimator, cosmic variance of EE contributes to the error budget, so a fixed-sky/noise-only ensemble underestimates σ(β̂) and inflates SNR.
- Required fix: Clarify whether the CMB sky was fixed or resampled. If fixed, either (a) re-run the MC with CMB realizations consistent with the EE spectrum to include sky variance, or (b) explicitly state that σ(β̂) reflects noise-only variance and is not an SNR for any sky-like ensemble, and refrain from quoting “SNR” without this qualifier. Provide an error budget indicating the size of the missing sky term relative to the quoted σ(β̂).

P1B-M9
- Location: Sec. VI (pp. 6–7) and Conclusions (p. 8)
- Problem: The paper quotes Caγ ≈ 9–51 based on Δϕ/fa ∈ [0.2, 1.1] from θi ∈ [0.5, 2], then acknowledges that true spectator status requires θi ∼ 0.1, which would reduce Δϕ/fa and increase the required Caγ beyond the 9–51 range. However, the Conclusions still present “Caγ between ∼9 and ∼51” as the operative range for the spectator-ALP interpretation.
- Required fix: Provide the explicit Caγ range required in the spectator-consistent corner (e.g., θi ≈ 0.1), at fixed β, using your Δϕ/fa(m/H0, θi) trajectories. Update the Conclusions to report both ranges (natural prior vs spectator-consistent) and clarify which one underpins the “spectator-ALP consistency” claim.

P1B-m6
- Location: Abstract (p. 1), Sec. IV (p. 5)
- Problem: The “published Planck/ACT DR6 2.4–2.9σ” bracket is not supported by the quoted values: Planck PR4/NPIPE β = 0.30 ± 0.11 implies 2.7σ; ACT DR6 β = 0.215 ± 0.074 implies 2.9σ. The lower bound 2.4σ is not traceable to [2,3] as cited.
- Required fix: Either adjust the range to 2.7–2.9σ or provide a citation and value supporting the 2.4σ endpoint (and ensure both numbers refer to the same release-level definitions and null procedures).

P1B-m7
- Location: Sec. III (p. 4), “MB–H0 joint-posterior offset check” and preceding paragraph
- Problem: σ-difference reporting is asymmetric. The text states the chain’s MB agrees with the Riess prior at “0.2σ,” using the chain’s σMB = 0.049 (0.010/0.049 ≈ 0.2σ). Standard practice is to compare using the combined uncertainty or at least the tighter prior’s uncertainty; relative to the Riess σ=0.027, the difference is ≈0.37σ, and relative to the combined error it is ≈0.33σ.
- Required fix: State explicitly which σ is used for the comparison and report the combined-uncertainty significance; avoid asymmetric σ-normalizations.

P1B-m8
- Location: Sec. IV (p. 5), mask/sky-fraction statement
- Problem: fsky = 0.32 is quoted without specifying whether this is computed before or after apodization, and whether it is the NaMaster-effective fsky used in the coupling-matrix normalization. This affects the response and covariance normalization.
- Required fix: Specify whether fsky refers to the unapodized or apodized mask and confirm that the same mask is used to build the mode-coupling matrix and weights. If different effective fsky definitions are used, clarify how normalization is handled.

P1B-n4
- Location: Throughout
- Problem: Inconsistent ΛCDM/LCDM capitalization (e.g., Table II caption and Sec. V use “LCDM,” elsewhere “ΛCDM”).
- Required fix: Standardize to a single convention throughout.

P1B-n5
- Location: Sec. V (p. 6) and elsewhere
- Problem: Inconsistent capitalization of “GetDist/getdist.”
- Required fix: Standardize to “GetDist” (the package name) throughout.

P1B-n6
- Location: Text, figures, and tables
- Problem: Mixed usage of Neff vs ΔNeff in prose/figure labels (Figure 1 shows “Neff,” Table I and text refer to ΔNeff).
- Required fix: Use ΔNeff consistently across text, tables, and figures to avoid confusion.