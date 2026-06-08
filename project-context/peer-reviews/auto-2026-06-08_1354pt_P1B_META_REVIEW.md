# P1B auto-2026-06-08_1354pt — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 399.5s

---

Meta-referee report for “Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model”

New findings (not raised by any of the 5 prior referees)

P1B-META-E1
- Severity: ESSENTIAL
- Location: Sec. IV, p. 5–6 (Eq. (1) paragraph and “Independent verification” block)
- Why missed: Prior reviewers asked for an SNR definition but did not diagnose the specific inflation mechanism.
- Problem: The quoted “pipeline-recovery SNR = 20.32 (500 MC)” is almost certainly computed on the MC mean (i.e., μ/SE[μ] = √N μ/σ), not the per-realization detection significance μ/σ. With N = 500, SNR(mean) = 20.3 corresponds to a per-realization SNR ≈ 20.3/√500 ≈ 0.9, explaining the large numerical disparity with Planck/ACT sky errors. As written, readers can misinterpret an SNR-on-the-mean as a per-map detectability metric; the paper never states which is used.
- Required fix: Define SNR unambiguously and report both μ/σ (per-realization detectability) and μ/SE(μ) (estimator calibration precision). Replace the headline SNR with the per-realization SNR when contrasting to sky measurements. Provide the numerical σ(β̂) across realizations and SE(μ) = σ/√N.

P1B-META-M2
- Severity: MAJOR
- Location: Sec. IV, p. 5 (“Pipeline configuration,” “Beam and pixel window,” “degrade to Nside = 512”)
- Why missed: Others flagged beam modeling and noise choices, but not the aliasing risk from map degradation.
- Problem: The manuscript degrades the Commander Q/U map from Nside=2048 to 512 and applies only the pixel window (bℓwℓpix). Absent explicit pre-smoothing to an ℓcut < 2 Nside, harmonic aliasing and E/B mixing can be introduced when down-sampling, biasing EB-derived β estimates even after pseudo-Cℓ deconvolution.
- Required fix: Pre-smooth prior to degrading (e.g., Gaussian smoothing to an ℓcut ≲ 2 Nside,512 − 1) and document the transfer function applied. Demonstrate that β recovery and its bias are stable (within quoted uncertainties) with and without the recommended anti-alias smoothing.

P1B-META-M3
- Severity: MAJOR
- Location: Sec. IV, p. 5–6 (“Independent verification” paragraph)
- Why missed: Reviewers questioned noise levels but not the choice of using the real sky as the signal template in MC.
- Problem: The MC “signal” is the actual Commander CMB map, then globally rotated and noise-added. This entangles the validation with one specific sky realization (including its residual systematics) and with the existing, unknown Commander noise, which is then further augmented by injected ACT-like noise. This design undermines the clean separation of algorithmic bias from realization noise and systematics.
- Required fix: Add a simulation suite that uses synthetic CMB realizations drawn from a fiducial Cℓ, rotated by β, masked/apodized identically, and noise-added at the stated level. Show that the recovered bias and dispersion match the Commander-based test within errors. Alternatively, explicitly subtract the Commander noise or validate that “double-noising” does not change bias within uncertainties.

P1B-META-M4
- Severity: MAJOR
- Location: Sec. III, p. 4–5 (“MB–H0 joint-posterior offset check”)
- Why missed: Prior reviewers flagged “exactly” language and σ mismatch but not the unit conditioning.
- Problem: The paper states “sn.pantheonplus enforces a soft constraint on the combination MB − 5 log10(H0) ≈ const.” The SN Ia degeneracy is defined with the dimensionless h ≡ H0/(100 km s−1 Mpc−1), i.e., MB − 5 log10 h = const. Using H0 directly hides a required additive constant 5 log10 100 and renders the displayed “constant” numerically unit-dependent.
- Required fix: Rewrite the degeneracy explicitly in terms of h (MB − 5 log10 h) and show the corresponding constants. If H0 is used for exposition, add the fixed 5 log10 100 term, and state units to avoid dimensional ambiguity. Recompute the two constants with consistent units and report the tension in a unit-robust way.

P1B-META-M5
- Severity: MAJOR
- Location: Sec. IV, p. 5 (“E/B leakage and purification”)
- Why missed: Others noted purification existence but not its possible impact on EB-based rotation recovery.
- Problem: The configuration uses purify_b=True and purify_e=False. For a uniform β that converts E→B on a cut sky, EB-based estimators can be sensitive to residual ambiguous-mode E contamination if E is not purified. This can bias or re-scale the EB slope used to infer β, especially with fsky=0.32 and 2° apodization.
- Required fix: Repeat the MC with purify_e=True and quantify the change in recovered β (bias and dispersion). If results differ beyond the stated systematic floor, either adopt symmetric purification (both E and B) or justify the chosen setting with a demonstrable invariance of β recovery.

P1B-META-M6
- Severity: MAJOR
- Location: Sec. VI, p. 6–7 (Eq. (2)–(3) and surrounding text)
- Why missed: Prior reviews flagged missing Δφ/fa in Eq. (3); none examined regime-of-validity.
- Problem: The birefringence expression β ≈ (αEM/4π) Caγ (Δφ/fa) assumes the linearized axion-photon coupling in the small-angle limit. Yet the text uses Δφ/fa ≈ 1.0 (“midpoint”) and ∈ [0.2, 1.1], pushing beyond the strict small-displacement regime of the harmonic approximation of V(φ). A single fudge factor “1.07” is introduced without derivation, but no demonstration is given that linearization errors remain ≪ total uncertainty across the quoted parameter range.
- Required fix: Provide a derivation or numerical cross-check showing the fractional error incurred by using the linear β ∝ Δφ/fa formula for Δφ/fa ≈ O(1) under the full cosine potential, across the sampled (m/H0, θi) range. If nonlinearity exceeds a few percent, propagate it into the β uncertainty (or adopt the exact integral form in the inference).

P1B-META-M7
- Severity: MAJOR
- Location: Sec. VI and Appendix C, p. 6–7, 9
- Why missed: Others noted underspecified likelihoods; none flagged aggregation across discrete Caγ as a single “sample size.”
- Problem: The ALP MCMC totals “9,720 accepted samples across 3 configurations” but each configuration fixes a different discrete coupling Caγ ∈ {4, 8, 12}. Later text quotes a single result “βALP = 0.336° ± 0.107° (Caγ = 8 fixed)” while still presenting the 9,720 total as if it backed that number. Mixing sample counts across discrete, non-sampled Caγ values is misleading and does not describe a single posterior.
- Required fix: Report per-configuration sample sizes and results separately (3 × 3,240). If a combined inference over Caγ is intended, introduce Caγ as a sampled parameter with a prior, or perform a discrete model average with explicit weights and quote the aggregated posterior accordingly. Do not pool sample counts from fixed-Caγ runs to support a single-point Caγ result.

P1B-META-m1
- Severity: MINOR
- Location: Table I footnote, p. 3
- Why missed: Others focused on dataset labeling and R̂ thresholds; this is a cross-reference-only glitch.
- Problem: The note reads “references to ‘k = 7’ elsewhere in this paper refer to the cosmological-parameter count only,” but there are no occurrences of “k = 7” elsewhere in the manuscript. This is a dead cross-reference indicating residual template text.
- Required fix: Remove this sentence or replace it with an actual, correct cross-reference if intended.

P1B-META-m2
- Severity: MINOR
- Location: Sec. VI, p. 7 (discussion after Eq. (3))
- Why missed: Prior reviews checked envelope arithmetic; none examined periodicity constraints.
- Problem: β is an angle defined modulo 90° (because polarization rotates as 2β). The βfree prior is [−2°, 2°], but the manuscript does not state the treatment of periodicity or verify that the posterior is insensitive to prior edges and the chosen principal branch. This matters when comparing “βfree” to literature that often reports angles in a specific branch.
- Required fix: State the β periodicity convention and confirm that the posterior mass is well within the [−2°, 2°] prior, not influenced by edges or principal-branch choices.

P1B-META-m3
- Severity: MINOR
- Location: Sec. IV, p. 5 (“Independent verification” paragraph)
- Why missed: Others flagged lack of estimator details; not this integral-step definition.
- Problem: The EB-based β estimation depends critically on ℓ-weighting. The text specifies only Δℓ=20 binning and ℓmin/max but does not state the weighting scheme used to convert EB bandpowers to a single β (e.g., inverse-variance weighting by Var[EBℓ], analytic Fisher weighting proportional to (∂CℓEB/∂β)/Var[EBℓ], etc.). Without this, the quoted bias and SNR are not reproducible or auditable end-to-end.
- Required fix: Provide the explicit estimator formula for β from bandpowers, including weights per ℓ-bin and any nuisance marginalization (e.g., α-like calibration modes). Report the Fisher normalization (if used) or the regression recipe.

P1B-META-m4
- Severity: MINOR
- Location: Sec. VI, p. 7 (shared calibration covariance for Planck+ACT EB likelihood)
- Why missed: Others flagged underspecification; not the specific risk of double-counting.
- Problem: You add a “shared calibration covariance” while using published EB bandpowers/likelihoods that may already include their own calibration priors. Without an explicit description, there is a real risk of double-counting calibration uncertainties or imposing inconsistent priors across experiments.
- Required fix: Describe how the joint calibration model is constructed (parameters, priors, and covariance), how existing per-experiment calibration priors are modified or removed, and show that the combined covariance is positive definite and not double-counted.

P1B-META-N1
- Severity: NIT
- Location: Sec. IV, p. 5 (mask description)
- Why missed: Others asked for mask provenance but not this small quantitative check.
- Problem: fsky = 0.32 is quoted after “C2 apodization at 2°,” but it is not stated whether fsky refers to the unapodized binary mask fraction, the apodized effective fsky (sum of mask weights / 4π), or an ℓ-weighted effective sky fraction. Different definitions differ by O(5–10%) and affect Fisher forecasts and SNRs.
- Required fix: Specify which fsky definition is used (binary vs apodized effective) and give both values, so readers can relate the SNR and Fisher expectations to the correct mask metric.

Meta-review recommendation
REJECT

Union-of-reviews summary and survivability
Across the five prior reports and this meta-review, I count multiple essential and major blockers: (i) misuse/mismatch of datasets (PR3 vs PR4, DESI DR1 vs DR2, DES-Y5 vs DES-SN5YR), (ii) a serious internal inconsistency in the w0–wa covariance/pivot algebra (including a sign error and a Cauchy–Schwarz violation), (iii) ambiguous or misleading SNR definitions for the NaMaster validation (and likely SNR-on-the-mean inflation), (iv) insufficient specification and potential bias in the pseudo-Cℓ pipeline (degradation aliasing, purification asymmetry, MC built on the real sky), (v) conflation of three different σ-concepts without airtight separations, (vi) framing the paper as “ECH verification” while none of the analyses actually test torsion, and (vii) reliance on unpublished companion papers for scientific context. Given these, my confidence that the paper would survive independent, external peer review (outside the author’s project sphere) is low. Even after major revisions, the work would likely need to be reframed as a short, stand-alone methods note, with cleaned dataset attributions, corrected w0–wa covariance math, and fully specified EB estimators and MC procedures.