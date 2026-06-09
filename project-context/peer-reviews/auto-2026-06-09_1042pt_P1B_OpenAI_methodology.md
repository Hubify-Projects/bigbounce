# P1B auto-2026-06-09_1042pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (8447 chars)
**Wall time**: 349.8s

---

Referee report on “Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model”

Overall scope
The manuscript documents three technical components: (i) a stock-CAMB ΛCDM+ΔNeff MCMC “proxy,” (ii) a NaMaster pseudo-Cl pipeline validation for EB-based birefringence recovery via MC signal injection, and (iii) a spectator-ALP consistency check against existing birefringence measurements. The authors repeatedly emphasize scope limitations, which is appropriate.

I assessed (a) statistical and numerical consistency, (b) internal arithmetic and dimensional checks, (c) estimator and likelihood specification sufficiency, and (d) figure/table coherence. Below I list all issues found, classified by severity.

ESSENTIAL (must be fixed prior to publication)
P1B-E1 — Sec. V/Table II (page 4): Incorrect wpivot decorrelation formula, inconsistent a_p, z_p, and σ(wpivot)
- Problem: The text states “wpivot ≡ w0 + (1 − ap) wa with ap chosen so that w0 and wa are decorrelated in the posterior covariance: ap = 1 − Cov(w0, wa)/Var(wa). On the converged iter2 chain ap = 0.6680, giving zp = 1/ap − 1 = 0.497; ... With w0 and wa formally decorrelated at zp, σ^2_wpivot = σ^2_w0 + (1 − ap)^2 σ^2_wa = (0.0301)^2.”
- Issues:
  1) The pivoting decorrelates wpivot and wa, not w0 and wa. The text misstates the decorrelation condition.
  2) The variance relation Var(wp) = Var(w0) + (1 − ap)^2 Var(wa) is incomplete; the cross term 2(1 − ap)Cov(w0,wa) must be included. At the correct pivot (where Cov(wp,wa)=0), Var(wp) = Var(w0) − Cov(w0,wa)^2/Var(wa).
  3) Using the given σ(w0)=0.0436 and σ(wa)=0.1864 with ap=0.6680 is inconsistent: it implies Cov large enough that Var(wp) would be negative if one enforces the pivot condition. Independently recomputing with the correct condition shows that the reported ap=0.6680, zp=0.497, and σ(wp)=0.0301 cannot be simultaneously true given the stated σ’s.
- Required fix: Provide the actual posterior covariance Cov(w0,wa), re-derive ap from the correct condition Cov(wp,wa)=0, and recompute zp and σ(wp) using the correct variance formula. Replace the sentence “so that w0 and wa are decorrelated” with “so that wpivot and wa are decorrelated.” Ensure the stated mean wpivot and its error bar are consistent with the supplied σ’s and covariance.

P1B-E2 — Sec. IV vs Fig. 3 (pages 5–6): Inconsistent map product and mislabeling of external result
- Problem:
  - Text says “Planck Commander Q/U maps ... degrade to Nside=512...” (page 5), while Fig. 3 title/legend reads “NaMaster, Planck SMICA.” These are different component-separated maps with different systematics. The methods must unambiguously state which product was used.
  - Fig. 3 legend appears to label 0.34±0.09° as a “Planck NPIPE central” value, but in the text the 0.34±0.094° figure is the WMAP+Planck joint result (Eskilt & Komatsu 2022), whereas Planck NPIPE-only is 0.30±0.11°. This is a mislabel that could mislead readers.
- Required fix: State exactly which Planck map was used (Commander or SMICA), at which data release (PR3 vs PR4/NPIPE), and ensure that all figure captions and legends reflect the same product. Correct the legend to label 0.34±0.094° as “WMAP+Planck joint,” and 0.30±0.11° as “Planck NPIPE-only,” if both are shown.

P1B-E3 — Sec. IV (page 5–6): Missing formal definition of the birefringence estimator and likelihood
- Problem: The paper claims a NaMaster pseudo-Cl pipeline validates EB-based β recovery via MC injection, but never writes down the β estimator used (e.g., the TB/EB rotation estimator, or slope fit on EB with mode-coupling corrections), nor the exact bandpower likelihood or covariance treatment. A methods paper must specify the estimator mathematically and state the binning, coupling-matrix inversion, and how β was extracted from the bandpowers.
- Required fix: Provide the explicit form of the β estimator used (e.g., relation between EB bandpowers and β after E→B leakage purification and MASTER coupling correction), the χ^2 or likelihood used to obtain β̂ and its uncertainty per realization, and the binning scheme and ℓ-range used. Include how purification (purify_b=True) modifies the mode-coupling model for EB.

P1B-E4 — Sec. III fn. 1 and Sec. VII (pages 2, 8): Nonexistent “third Planck-only chain” in Table I
- Problem: The text repeatedly states the Planck-only chain (114,992 raw samples; R̂−1≈0.05) is “reported separately in Table I,” but Table I only shows two columns (full-tension and Planck+BAO+SN). The Planck-only chain is not present in the table.
- Required fix: Either add a third column with the Planck-only chain metrics or remove the claim that it is reported in Table I. Also make clear that the “309,189 frozen samples” headline corresponds strictly to the two frozen dataset combinations, and that the Planck-only chain is excluded from all reported aggregate statistics.

P1B-E5 — Sec. III, V.A, Table I (pages 2, 6, 3): Incomplete MCMC configuration: BBN consistency, Σmν, and S8 prior value not specified
- Problem: For ΔNeff runs, whether Yp follows BBN consistency (and what BBN code/options) is crucial; Σmν prior (e.g., fixed 0.06 eV vs free Σmν) also materially affects posteriors. The full-tension stack includes an S8 prior but no numerical value/uncertainty is given.
- Required fix: State explicitly in the main text: (i) whether Yp is set by BBN consistency as a function of ωb and ΔNeff (and which BBN recipe), or fixed; (ii) whether Σmν is fixed (and to what value) or sampled (with what prior); (iii) the exact S8 prior mean and σ and the source likelihood used. These are load-bearing for reproducibility and interpretation.

P1B-E6 — Fig. 2 (page 5): Misleading label “SM ( Neff = 0 )” on a ΔNeff axis; unexplained “WP4” bands
- Problem: The x-axis is ΔNeff (as implied by zero-centered distributions), but the figure annotates “SM ( Neff = 0 ).” This is incorrect: the SM reference on a ΔNeff axis is ΔNeff=0. The “WP4 reheating/decay” colored bands are not explained or cited in the caption/body.
- Required fix: Change the label to “SM (ΔNeff = 0).” Add a caption note explaining what “WP4” bands represent and cite the source, or remove them.

P1B-E7 — Sec. IV (page 5): Beam model inconsistency for component-separated maps
- Problem: The text applies a single “Planck-2018 effective Gaussian beam (5′ FWHM at 143 GHz)” to a component-separated CMB map (Commander/SMICA). Those maps are delivered at a common resolution, but it is not simply the 143 GHz beam; the effective transfer function is map-specific. Using a single 5′ Gaussian without justification is an uncontrolled approximation for polarization EB analyses.
- Required fix: Specify the actual effective beam/pixel window used for the chosen component-separated product (e.g., use the provided map-specific transfer function). If approximating with a 5′ Gaussian, justify insensitivity (e.g., demonstrate that deviations change β̂ by < X deg).

P1B-E8 — Table I footnote (page 3): Misclassification of Mb as a “Planck likelihood nuisance”
- Problem: The footnote lists “10 Planck likelihood nuisance: Aplanck, amp143, ... calEE, Mb for the SNIa absolute magnitude.” Mb is not a Planck nuisance; it is a SN nuisance.
- Required fix: Correct wording to “10 likelihood nuisance parameters (Planck nuisances: ...; and the SN Ia absolute magnitude Mb).” Also, provide the full nuisance list actually sampled for CamSpec/lowl/lensing; the current list appears incomplete for CamSpec TTTEEE.

MAJOR (significant revision)
P1B-M1 — Sec. III (page 5 end) “Independent cross-validation” with Liu et al. [11] lacks quantitative support
- Problem: The text states “Our MCMC agrees at 0.5σ in H0 and 0.4σ in σ8.” No explicit numbers from [11] nor a calculation are shown.
- Required fix: Quote the [11] posterior means and σ, and compute the normalized differences explicitly in the text or a footnote.

P1B-M2 — Sec. IV (pages 5–6): Mask-bias statement lacks quantitative support
- Problem: The claim “bias ... consistent with the apodized-mask bias expected from a 2° apodization scale” is asserted without a model/derivation or reference, and no uncertainty on the 0.032–0.040° bias is given.
- Required fix: Provide a reference or a brief analytic/MC justification for the expected bias scaling with apodization, and report the uncertainty on the measured bias from the 500 realizations.

P1B-M3 — Sec. IV (page 5): Estimator SNR definitions are nonstandard and need context
- Problem: SNRSE = β̂/SE(β̂) is reported (20.32, 25.71) and later converted to per-realization SNR. While the caveat exists, the paper should present the per-realization SNR as the primary detectability metric and place the estimator-calibration SNR in an appendix.
- Required fix: Move SNRSE discussion to methods/appendix, and foreground SNR per realization in the main text to avoid confusion.

P1B-M4 — Sec. V.A vs Table II vs citations (pages 6, 4, refs): Dataset-version and naming inconsistencies
- Problem: The manuscript alternates between “DESI 2024 DR1 BAO” in Sec. V.A and “DESI DR2 BAO” in Table II and elsewhere; it also mixes “Planck 2018 NPIPE” (PR3 year with PR4/NPIPE label). This confuses reproducibility.
- Required fix: Standardize dataset naming and versioning throughout (e.g., “Planck PR4/NPIPE CamSpec TTTEEE + ...”, “DESI DR2 BAO”, etc.) and ensure references [17], [12], [18] match the datasets actually used.

P1B-M5 — Fig. 2 right panel (page 5): Illegible/undefined axis label
- Problem: The right panel’s x-axis label “(x xfull_tension) / full_tension” is unclear and undefined in the text.
- Required fix: Replace with a clear, defined quantity or remove the panel.

P1B-M6 — Sec. IV (page 5): ℓ-range and binning specifics for β estimation
- Problem: Although Δℓ=20, ℓmin=30, ℓmax=1024 are mentioned, the text does not state which ℓ-bands enter the β fit (e.g., ℓ-cuts to avoid residual foregrounds or beam uncertainties) nor how bandpower covariance is estimated.
- Required fix: State the exact ℓ-range used in the β fit, justification for ℓ cuts, and the method of estimating bandpower covariance (analytic vs MC).

P1B-M7 — Sec. VIII/Acknowledgments (page 9): Use of internal filepaths and run-log details in the body
- Problem: Strings like “pipelines/h200_results/pod1_namaster_umap_2026-04-29/” and references to “two consecutive flushes” read like internal run logs.
- Required fix: Move such operational details to the Data and Code Availability or an appendix. Keep the main text focused on scientific content.

MINOR (address but not blocking)
P1B-m1 — Acknowledgments (page 9): Mention of using “Claude (Anthropic) as an AI research assistant”
- Comment: Journal policy may or may not welcome such acknowledgments; consider removing or confirming with the editor.

P1B-m2 — Sec. IV (page 5): Capitalization/notation consistency (Nside vs N_side)
- Required fix: Standardize notation.

P1B-m3 — Fig. 2 (page 5): Consistent symbol use ΔNeff vs Neff
- Required fix: Ensure all axis labels and annotations use ΔNeff consistently if that is the plotted quantity.

P1B-m4 — Table I (page 3): Significant-figure consistency
- Required fix: Harmonize uncertainties (e.g., ΔNeff ±0.169 vs ±0.17). Adopt a consistent rounding convention.

P1B-m5 — Sec. III fn. 2 (page 2): Statement “Λstrong ∼ MPl/√γBI set by the inverse Barbero–Immirzi parameter”
- Problem: This scaling is nonstandard and γ is dimensionless; the proposed dependence requires a proper derivation or citation.
- Required fix: Provide a correct, referenced expression for the relevant strong-coupling scale in Holst/Immirzi theories, or remove.

P1B-m6 — Language tone (multiple pages): Terms like “canonical 3.6σ,” “headline result,” “canonical quintom signature”
- Required fix: Replace with neutral, technical phrasing.

P1B-m7 — Sec. IV (page 5): Degree symbol and units consistency (° vs deg)
- Required fix: Use a single convention throughout.

P1B-m8 — Table III (page 10): For β̂NaMaster = 0.238° add uncertainty on the MC mean
- Required fix: Report SE(β̂) to quantify the calibration precision from 500 realizations.

P1B-m9 — Sec. III (pages 2–5): Planck likelihood modules and nuisances
- Required fix: Specify exact Planck likelihood versions (e.g., CamSpec 12.5, PR4 low-ℓ names) and full list of sampled nuisances in an appendix or table for reproducibility.

NITS
P1B-n1 — Unit formatting: keep “km s−1 Mpc−1” consistent.
P1B-n2 — Remove stray em-dashes where commas/semicolons suffice.
P1B-n3 — Several long footnotes interrupt flow; consider moving to appendices.

Arithmetic and consistency spot-checks (passed)
- Table I ΔNeff and H0 values match the abstract and conclusions.
- H0 tension with Riess et al. 73.04±1.04 vs 67.69±1.06 gives 3.6σ; computed 3.59σ.
- SN degeneracy check: −19.253 − 5 log10(73.04) = −28.571; −19.263 − 5 log10(67.69) = −28.416; offset 0.155 mag ~ 3.2σ of σMB=0.049; arithmetic matches.
- S8 computed from Table I numbers is consistent within rounding.
- Birefringence scaling: β ≈ (αEM/4π) Caγ (Δϕ/fa): for Caγ=8 and Δϕ/fa=1.07 gives 0.0050 rad ≈ 0.285°, consistent with 0.29°.
- Product Caγ Δϕ/fa from βobs=0.342°: 0.342°=5.97×10−3 rad; dividing by αEM/(4π)=5.8×10−4 gives ~10.3; consistent.
- Inverse-variance combination of 0.30±0.11 and 0.215±0.074 gives 0.241±0.061 (3.95σ); matches text.

Length and scope
The paper is 11 pages. For a methods companion, this is acceptable provided the ESSENTIAL estimator/likelihood definitions and dataset-version clarifications are added. If the authors decide not to expand the derivations, the page count could be kept similar by moving run-log prose to appendices and tightening narrative repetition.

## Summary recommendation
MAJOR REVISIONS

The manuscript contains several essential methodological and internal-consistency issues that must be corrected for PRD standards: (i) the wpivot decorrelation mathematics and numbers are inconsistent and use the wrong variance/decorrelation statements; (ii) inconsistent dataset/map labeling (Commander vs SMICA vs NPIPE; DESI DR1 vs DR2) and a mislabel in Fig. 3; (iii) lack of an explicit β estimator and likelihood specification for the NaMaster pipeline; (iv) missing key MCMC configuration details (BBN consistency, Σmν, S8 prior). Once these are addressed and the smaller issues corrected, the paper could be suitable as a technical companion.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (second-pass review)

ESSENTIAL

P1B-E9 — Broken/ambiguous internal references: “Eq. 1–3” and “§ Headline-result discussion”
- Problem: On p. 6 the text says “this is the NaMaster systematic floor adopted in Eq. 1–3,” but Eqs. (1)–(3) mix an MC estimate of β̂ (Eq. 1) with an ALP prediction formula (Eq. 3); no equation actually “adopts” a systematic floor. In Table II fn. a, “see § Headline-result discussion” points to a non-existent section.
- Required fix: Replace “adopted in Eq. 1–3” with a precise statement of where the 0.032–0.040° systematic is applied (e.g., “we add 0.040° in quadrature to β̂ uncertainties when quoting pipeline calibration systematics”). Remove or correct the “§ Headline-result discussion” pointer; cite the exact subsection containing that discussion.

P1B-E10 — Nside inconsistency between methods and Fig. 3
- Problem: Methods state the analysis degrades Commander to Nside=512, but Fig. 3 is explicitly “β vs HEALPix Nside” with points spanning Nside beyond 512 (256, 1024, 2048 shown). It is unclear at which Nside the headline MC numbers (β̂=0.238°, bias 0.032°) are obtained, and whether the mask/beam/noise are redefined consistently for each Nside in the sweep.
- Required fix: State the Nside used for the reported β̂ values (and for the quoted 0.032–0.040° bias). If a resolution sweep was performed, describe the exact configuration changes with Nside (mask apodization kernel in pixels vs degrees, beam/pixel windows, ℓmax scaling) and provide a table or caption note tying each plotted point to a configuration.

P1B-E11 — Mischaracterization of noise level in the MC as “conservative worst-case”
- Problem: The MC uses ΔP=10 μK·arcmin (“ACT-level”) and calls this “a conservative worst-case bias check.” For a Commander/Planck map, 10 μK·arcmin is lower than Planck polarization noise and is not a worst case; it is a best-case or optimistic noise level. This can inflate per-realization SNR and under-represent noise-driven leakage/bias.
- Required fix: Either justify why lower noise gives a worst-case bias for this estimator (with a reference or MC scaling study), or re-run/augment the MC with Planck-like noise appropriate to the chosen component-separated map and quote both sets of results. Clarify in the text that “SNRSE” is a calibration precision across 500 realizations and not a detectability claim.

P1B-E12 — Sample-count and convergence statement inconsistencies
- Problem:
  - Fig. 2 legend lists “Full tension (175 545 samples)” while Table I gives 176,240 raw samples for the same combination; neither number is labeled as raw vs post-burnin vs thinned. Fig. 1 caption gives “119,617 post-burnin samples” while fn. 1 quotes 123,129 post-burnin for that subset. These numbers should reconcile.
  - Table I footnote claims “all 17 sampled parameters … satisfy R̂−1 < 3×10−3,” but the Planck+BAO+SN column reports “Worst R̂−1 = 0.003,” i.e., equal to 3×10−3, not strictly less.
- Required fix: Standardize and label sample counts (raw accepted, post-burnin, and any thinning) consistently across text, figure captions, and legends. Change the convergence statement to “≤ 3×10−3” or report the exact worst value(s). Provide a short table in the appendix with per-chain raw, burn-in fraction, post-burnin, and effective sample size.

P1B-E13 — ALP joint-likelihood “shared calibration covariance” under-specified
- Problem: Appendix C says the Planck PR4 + ACT DR6 EB-spectrum likelihoods are “combined with shared calibration covariance” but gives no explicit form, nuisance list, or reference (e.g., the Tau A angle treatment, cross-covariance terms, priors). Since the combined constraint βfree = 0.344° ± 0.096° is central to the ALP consistency check, the construction of this covariance is load-bearing.
- Required fix: Provide the explicit calibration/angle nuisance model used (parameters, priors, and where it enters the covariance), or cite a public likelihood implementation with version tag. If custom, include the covariance blocks or a reference file in the reproducibility materials and summarize them in an appendix.

MAJOR

P1B-M8 — Fig. 3 contains an unlabeled “Prediction: β = 0.27°” reference line not described in the text
- Problem: The legend shows a prediction line, but the methods and caption do not explain whether this is an ALP prediction, an injected value, or a benchmark. This invites confusion with the MC injection values and external measurements.
- Required fix: Clarify in the caption and text what the prediction line represents and how it is computed; if it is simply the injected β for the MC test, label it as “Injection β.”

P1B-M9 — Dataset naming and releases for DES “Y5” vs “DES-SN5YR” and Planck low-ℓ likelihoods remain ambiguous
- Problem: The body references “DES-Y5” generically in Table II, while the references and Sec. V list DES-SN5YR and DES Y3 S8 separately. Likewise, low-ℓ likelihoods are referred to as “planck 2018 lowl.EE + lowl.TT” in places while the narrative emphasizes PR4/NPIPE elsewhere.
- Required fix: Unify dataset names to the exact data products used in each chain, including DES-SN5YR vs DES-Y5 (SN vs WL/BAO), and specify which low-ℓ Planck likelihood files (PR3 vs PR4) were active in each chain. Cross-check the references to ensure the cited papers match the releases used.

P1B-M10 — Mask provenance and definition not documented in the main text
- Problem: The fsky=0.32 mask is central to the EB analysis, but its origin (e.g., which Galactic + point-source mask, component-separated product, and apodization kernel) is not described beyond “C2 apodization at 2°” and an internal path in the reproducibility section.
- Required fix: Briefly describe the mask inputs (base mask, point source cuts, inpainting if any), apodization type/scale in degrees and pixels, and provide a DOI or direct link to the exact FITS file used.

MINOR

P1B-m10 — Small S8 inconsistency in Table I (Planck+BAO+SN)
- Problem: Using the table’s Ωm=0.312 and σ8=0.812 gives S8 ≈ 0.828, while the table lists 0.831 ± 0.018. This is within rounding/systematic differences but should be acknowledged.
- Required fix: Note in the caption that S8 is computed from full posterior samples (not from rounded means), or adjust the displayed digits for internal consistency.

P1B-m11 — Units and separators consistency
- Problem: Mixed usage of “km/s/Mpc” (table) vs “km s−1 Mpc−1” (text); sample counts written as “175 545” vs “176,240.”
- Required fix: Standardize units to “km s−1 Mpc−1” and number formatting with consistent thousands separators.

P1B-m12 — Unexplained horizontal annotations in Fig. 2 (left panel)
- Problem: The overplotted lines “BBN 2 upper (0.41)” and “ACT DR6 central (0.40)” are not defined or cited in the caption/body.
- Required fix: Add a caption note with citations and clarify whether these are Neff or ΔNeff references and how they relate to the plotted posteriors.

P1B-m13 — Ambiguous phrasing around “Eq. (1)-adjacent disclaimer” (p. 7, fn. 5)
- Problem: The footnote refers to an “Eq. (1)-adjacent disclaimer,” which is not a standard reference and is unclear.
- Required fix: Replace with a clear reference to the exact sentence or subsection where the spectator-status caveat is stated.

P1B-m14 — Instrument model self-consistency
- Problem: The combination of a single 5′ Gaussian beam with Commander/SMICA and ACT-level noise is not a realistic joint instrument model for any single experiment.
- Required fix: Add a sentence noting that the MC is a methods check and not an instrument-level simulation; if possible, show that modest beam mis-specification at this level does not bias β̂ beyond the quoted 0.032–0.040° floor.

P1B-m15 — Reference coverage for PR4/NPIPE high-ℓ likelihoods
- Problem: Ref. [17] is Planck 2018 PR3 parameters; the manuscript uses “PR4/NPIPE CamSpec TTTEEE + low-ℓ + lensing.” A PR4/NPIPE reference for the high-ℓ likelihood should be cited in addition to the PR3 parameters paper.
- Required fix: Add the appropriate PR4/NPIPE high-ℓ likelihood and processing references.

Explanation
This second-pass focused on new issues across arithmetic, caption/body alignment, internal references, null-procedure comparability, and abstract faithfulness. The items above are non-duplicative with the original report and target places where the current manuscript may mislead readers or hinder reproducibility despite otherwise careful scoping language.