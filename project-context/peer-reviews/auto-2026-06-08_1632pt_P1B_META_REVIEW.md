# P1B auto-2026-06-08_1632pt — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 460.9s

---

Meta-review for PRD submission “Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model”

New findings that none of the five prior reviewers caught

P1B-META-E1
- Severity: ESSENTIAL
- Section + page: V.B/Table II (p. 4) and V.A (p. 6)
- Why others missed it: Prior reviews noted dataset-name inconsistencies but did not analyze overlap/independence of the SN samples.
- Problem: Possible supernova double counting and ambiguous DES labeling. Table II’s likelihood stack includes “DES-Y5 + Pantheon+,” while ref. [14] (DES-SN5YR) is also cited elsewhere. If “DES-Y5” denotes the DES Year-5 SN sample (as opposed to 3×2pt lensing/clustering), combining DES-SN with Pantheon+ without an explicit joint covariance risks double counting overlapping SN data. The paper never specifies whether “DES-Y5” here is SN or 3×2pt, nor whether a joint SN covariance was used.
- Required fix: Explicitly state what “DES-Y5” denotes in Table II (SN vs 3×2pt) and whether DES-SN events overlap with Pantheon+. If both SN samples are used, provide the joint covariance or remove one set. If “DES-Y5” is 3×2pt, update labels and references to eliminate any implication of SN+SN stacking.

P1B-META-E2
- Severity: ESSENTIAL
- Section + page: III (pp. 2–5) and V.A (p. 6), Table I (p. 3)
- Why others missed it: Reviews focused on ΔNeff posteriors and versioning, not on cosmological recombination assumptions in ΔNeff runs.
- Problem: Unspecified BBN treatment with ΔNeff. The ΔNeff constraint depends sensitively on the helium fraction Yp(H, ωb, Neff). The manuscript never states whether Yp was set by BBN consistency (and with which solver, priors, or fitting function) or fixed independently. In stock CAMB, different choices (BBN-based Yp vs fixed Yp) shift ΔNeff posteriors at the level relevant here.
- Required fix: State the exact Yp–BBN treatment used (e.g., PArthENoPE fit or CAMB’s BBN module; whether Yp varies consistently with Neff and ωb; any priors). If fixed Yp was used, justify and quantify the sensitivity of Table I’s ΔNeff to the Yp choice.

P1B-META-E3
- Severity: MAJOR
- Section + page: IV (pp. 5–6)
- Why others missed it: Prior reviews critiqued beam/noise choices and lack of estimator detail, but not the conditioning implicit in the input map’s provenance.
- Problem: Hidden conditioning from injecting β on a component-separated map built under β=0. The Commander CMB Q/U map is produced by a component-separation pipeline that assumes no cosmic rotation in the mixing model and instrument angles. Injecting β ex post facto into that CMB-only product conditions on a β=0 forward model and cannot probe biases introduced by component separation itself under β≠0. This undermines the claimed “pipeline validation” for sky-like systematics, even acknowledging that it is not a sky measurement.
- Required fix: Explicitly state this limitation and, if the goal is to validate recovery in more realistic conditions, repeat the MC on multifrequency simulations with the component-separation step included (or on half-mission splits with per-band rotation) so that β is injected before separation.

P1B-META-E4
- Severity: MAJOR
- Section + page: IV (p. 5–6)
- Why others missed it: Others noted noise/beam mismatch; none flagged the mischaracterization of noise choice as “conservative worst-case.”
- Problem: Mislabeling ACT-level noise as a “conservative worst-case bias check.” The text uses ΔP = 10 μK·arcmin (ACT-like, significantly lower noise than Planck) and calls this a “conservative worst-case bias check.” Lower noise yields higher SNR and is not a worst-case configuration for bias discovery; conversely, mask/purification-induced amplitude biases are largely noise-independent while the perceived detectability is inflated. This conflates sensitivity and bias stress-testing.
- Required fix: Recharacterize this as a best-case/high-SNR configuration. Add tests at Planck-like noise (and inhomogeneous noise) to evaluate whether the measured 0.032–0.040° bias persists across realistic noise levels; otherwise remove the “systematic floor” framing.

P1B-META-E5
- Severity: MAJOR
- Section + page: III (p. 3, “Physics interpretation” paragraph) and Table II (p. 4)
- Why others missed it: Others critiqued σ-claims and wpivot math but not the specific “crossing in the probed redshift range” assertion.
- Problem: Unproven claim that phantom crossing occurs within the data’s redshift range. The paper asserts “w0 + wa = −1.4788 ± 0.1485 requiring phantom crossing in the redshift range probed by DESI DR2 BAO + DES-Y5 + Pantheon+.” Crossing occurs at a_cross = 1 + (w0 + 1)/wa and must be shown to lie in 0 < a < 1 (i.e., some z>0) with uncertainty. No a_cross posterior is reported; wpivot is quoted but does not demonstrate that crossing happens within the survey z-range given the covariance.
- Required fix: Report the posterior for a_cross (or z_cross) with credible intervals and the fraction of samples that cross within the combined dataset’s z-range. If not robust, soften the statement to reflect only that the central values imply crossing but its location is not established.

P1B-META-E6
- Severity: MAJOR
- Section + page: IV (pp. 5–6)
- Why others missed it: Estimator definition critiques did not cover purification-specific normalization.
- Problem: Purification-induced transfer function not calibrated. The pipeline uses NaMaster with purify_b=True, purify_e=False and then quotes an amplitude bias (0.032–0.040°). Purification changes the effective response and requires either analytic normalization or MC calibration of the β transfer function. No such normalization or MC-derived correction factor is described; the observed bias may simply be an uncorrected transfer function.
- Required fix: Calibrate the β response with MC (derive a multiplicative transfer function vs. ℓ and apply it) or provide the analytic normalization appropriate for B-purification. Re-quote the bias after this correction.

P1B-META-E7
- Severity: MINOR
- Section + page: III (pp. 2–3), Abstract (p. 1)
- Why others missed it: Others criticized the emphasis on raw counts but not the additive headline.
- Problem: Summing raw accepted samples across different dataset combinations is statistically meaningless. The abstract and Sec. III headline “309,189 frozen samples across two converged dataset combinations” aggregates samples from independent posterior runs. Raw sample counts are not additive across different likelihoods and have no bearing on convergence or precision.
- Required fix: Remove any aggregate “total samples across combinations.” Report convergence metrics (R̂, ESS) per chain/stack only.

P1B-META-E8
- Severity: MINOR
- Section + page: IV (pp. 5–6)
- Why others missed it: Noise modeling critiques focused on inhomogeneity; not on the TB/EB estimator completeness.
- Problem: Missing TB channel cross-check. A constant β induces both TB and EB. The MC validation uses only EB; TB is not mentioned. Using both improves robustness to spurious EB from leakage and provides a null consistency check. The absence of TB weakens the bias characterization.
- Required fix: Add a TB-based β estimator (or a joint TB+EB fit) to the MC validation and report whether the 0.032–0.040° bias appears in both channels consistently.

P1B-META-M1
- Severity: MAJOR
- Section + page: Table II (p. 4)
- Why others missed it: Prior reviews critiqued the pivot math; none questioned the use of mean-of-χ2 and lack of dof.
- Problem: Goodness-of-fit reported as posterior-mean χ2 without dof or best-fit likelihood. Table II lists “χ2 total 14037.4 ± 5.6” and components as posterior averages. Without degrees of freedom or best-fit −2 ln L, readers cannot assess absolute fit quality or compare models. Posterior-mean χ2 is not a standard goodness-of-fit summary for model comparison.
- Required fix: Provide best-fit (or maximum-posterior) −2 ln L and χ2 per component with dof, and report Δχ2 relative to ΛCDM for the w0wa run. If only posterior means are used, clearly justify and add dof to enable interpretation.

P1B-META-M2
- Severity: MAJOR
- Section + page: III (p. 4–5, “MB–H0 joint-posterior offset check”)
- Why others missed it: Others noted the σ-level mismatch (3.16σ vs 3.6σ) but not the degeneracy–metric mismatch.
- Problem: Hidden-metric conflation on the SN degeneracy axis. The text equates a 0.155 mag offset in MB − 5 log10 H0 (3.16σ in MB) with the “canonical 3.6σ Hubble tension,” but those σ’s live in different parameter projections and likelihood combinations. Without projecting the full joint covariance of (MB, H0, SN), equating these σ’s is misleading.
- Required fix: Either compute the tension consistently in a single parameter space (e.g., use the same covariance to project both) or refrain from calling the two σ’s “the same,” framing instead as qualitatively consistent but numerically different projections.

P1B-META-m1
- Severity: MINOR
- Section + page: IV (p. 5)
- Why others missed it: Beam critique focused on which beam, not on downgrade practice.
- Problem: No mention of pre-smoothing before degrading Nside=2048 to 512. To prevent aliasing, maps should be smoothed to below the Nside=512 Nyquist limit before downgrade. The text mentions applying only the pixel window after downgrading.
- Required fix: State the pre-smoothing kernel and demonstrate that omitting it does not bias EB. If not used, re-run with appropriate pre-smoothing and update the bias estimate.

P1B-META-m2
- Severity: MINOR
- Section + page: V.A (p. 6)
- Why others missed it: They focused on Planck release/citation mismatches, not neutrino-mass priors.
- Problem: Unspecified Σmν prior in ΔNeff and w0wa runs. The joint constraints on Neff, H0, S8, and w(z) depend on whether Σmν is fixed (e.g., 0.06 eV) or allowed to vary. The paper does not state the Σmν treatment.
- Required fix: State the neutrino-mass prior (sum and hierarchy) for all chains; if varied, report the prior and marginal posterior. Quantify sensitivity if relevant.

P1B-META-N1
- Severity: NIT
- Section + page: Throughout (Abstract, Sec. IV, VII)
- Why others missed it: They covered SNR-vs-σ comparability but not unit clarity.
- Problem: β calculations mix degrees in prose with radian-based formulae without an explicit note that conversions are applied at each step. This can lead to reader misapplication.
- Required fix: Add a one-line note where Eq. (3) appears that all computations are in radians and final values are reported in degrees.

Meta-review recommendation
REJECT

Rationale: In addition to the substantial issues already identified by the five referees (incorrect wpivot derivation and covariance, dataset/likelihood provenance mismatches, estimator opacity, misframed ALP “spectator” prior, internal version/history text, etc.), there are further essential/major problems: potential SN sample overlap without joint covariance, unspecified BBN/helium treatment in ΔNeff runs, hidden conditioning from injecting β onto a component-separated map built under β=0, mischaracterization of ACT-level noise as “conservative worst case,” unproven claim that phantom crossing occurs within the probed redshift range, lack of purification-transfer normalization, statistically meaningless aggregation of sample counts across different likelihood stacks, and insufficient goodness-of-fit reporting (posterior-mean χ2 with no dof). Collectively, these indicate that the manuscript is not yet audit-ready for PRD.

Given the union of all six reviews, there are >15 independent blockers spanning arithmetic correctness, dataset provenance, estimator specification, prior–posterior consistency, and claims framing. Confidence that the paper would survive external peer review (outside the author’s program) in its current form is low. A successful resubmission would require consolidating scope with the primary theory paper, correcting mathematical inconsistencies, fully specifying and justifying the likelihood stacks and estimators, and rerunning key analyses with physically consistent priors and data handling.