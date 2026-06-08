# P2 auto-2026-06-08_1520pt — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 466.9s

---

Meta-review (new issues none of the five referees flagged)

P2-META-E1
- Severity: ESSENTIAL
- Section/page: Sec. 3.3 (priors), p. 3; Sec. 3.4 (Bayes factor prior), p. 3
- Why others missed it: Reviewers noted the one‑sided β prior in the Bayes factor, but not that the ALP parameter priors themselves force β > 0.
- Problem: Hidden sign conditioning. The ALP priors θi ∈ [0.01, π] and Caγ ∈ [1, 30] combined with gaγ = C/fa imply gaγ > 0 and θi > 0, hence β ∝ gaγ Δφ/2 is a priori non‑negative. This makes negative rotation angles impossible under the ALP prior, then the Bayes factor is also computed with β ∈ [0°,1°], compounding a one‑sided assumption. This bakes the observed positive sign into both the model and the evidence computation and artificially inflates support for β > 0.
- Required fix: Use sign‑symmetric priors: θi ∈ [−π, π], allow Caγ (or the effective sign of the photon coupling) to take either sign, and adopt a β prior symmetric about zero for Bayes factors. Recompute all posteriors and ln B.

P2-META-E2
- Severity: ESSENTIAL
- Section/page: Abstract (p. 1), Sec. 2.2 (p. 2), throughout
- Why others missed it: Coupling normalization issues were noted, but not the Planck-mass convention ambiguity that propagates to g and ρ.
- Problem: Unstated Planck-mass convention. The paper repeatedly writes fa ∼ MPl but never specifies whether MPl denotes the reduced (≈ 2.435×10^18 GeV) or unreduced (≈ 1.22×10^19 GeV) Planck mass. This factor ≈ 5 ambiguity propagates directly into the coupling g ∝ 1/fa, the energy density scale m^2 f_a^2, and the “naturalness” statements. Given the already marginal consistency of the energy budget and couplings, this missing convention materially affects the quantitative claims.
- Required fix: State explicitly which Planck mass is used and propagate that choice consistently through all equations, numbers, and “order‑unity” claims (including the energy-density discussion, even if moved to an appendix).

P2-META-E3
- Severity: ESSENTIAL
- Section/page: Model/Results as a whole; omitted from Secs. 2–4
- Why others missed it: Focused on isotropic β and dataset issues; anisotropic predictions were not discussed.
- Problem: Missing anisotropic-birefringence test. A rolling ALP with m ~ H0 generically produces spatial fluctuations in the rotation angle (α(n̂)) from field perturbations. Planck and other experiments have placed limits on anisotropic birefringence (C_L^α). The manuscript does not compute the predicted anisotropy nor check consistency with existing C_L^α limits, which can be more constraining than the isotropic average for some models.
- Required fix: Provide an estimate of the expected C_L^α for the stated parameter choices (including assumptions on initial ALP perturbations) and verify consistency with current constraints. If necessary, restrict the parameter space accordingly.

P2-META-M1
- Severity: MAJOR
- Section/page: Sec. 2.2 (p. 2) and Sec. 3.2–3.3 (pp. 2–3)
- Why others missed it: Degeneracies were noted, but not that quoting Caγ × θi alone is not meaningful without conditioning on m.
- Problem: Ill‑posed “coupling–misalignment product.” The reported constraint Caγ × θi = 3.4 ± 1.1 (Eq. 8) is presented as if it were mass‑independent, yet Δφ/fa and hence β depend strongly on m/H0. With the mass posterior pressing against the prior ceiling, the product Caγ × θi has a broad, m‑dependent degeneracy. Quoting it without conditioning on m (or marginalizing over a demonstrably uninformative prior) is not a well‑defined, reproducible constraint.
- Required fix: Report the joint posterior p(Caγ × θi, m) and/or condition the product on narrow slices of m/H0. Alternatively, present constraints directly in terms of g_aγ and m, which are the physical parameters entering β.

P2-META-M2
- Severity: MAJOR
- Section/page: Sec. 3.2 (p. 2); Fig. 2 caption (p. 5)
- Why others missed it: EB focus was taken as given; the complementary TB channel was not discussed.
- Problem: No TB/EB consistency check. A constant cosmological rotation produces identical β in EB and TB (up to sign conventions). The analysis and combinations are based on EB only (“fits the full EB cross‑spectrum”); there is no mention of the TB channel or published TB-based β estimates. Ignoring TB forfeits an internal null/consistency test that could expose residual systematics or frequency‑dependent effects.
- Required fix: Include TB‑based constraints (or cite them) and demonstrate consistency between TB‑ and EB‑inferred β within each dataset used, or justify why TB was excluded.

P2-META-M3
- Severity: MAJOR
- Section/page: Sec. 2.2, Sec. 4 (pp. 2–4)
- Why others missed it: The constant‑β assumption was critiqued qualitatively but not tied to the time dependence relevant to reionization vs. recombination.
- Problem: Time‑dependent rotation ignored. For m ~ H0 the field evolves mainly at late times. The measured “single β” from EB/TB is effectively a weighted average over photon last‑scattering epochs (reionization bump vs recombination), which have different optical‑depth weightings. If β(t) is not constant, a single‑angle estimator is biased. The paper assumes a constant β without checking whether the model’s β(t) variation across z ≈ 10 → 1100 is negligible.
- Required fix: Compute the predicted β(z) and demonstrate that its variation across the visibility function induces sub‑percent biases in the single‑β estimator for the favored m/H0 range; otherwise, incorporate this in the likelihood or add a model‑uncertainty term.

P2-META-M4
- Severity: MAJOR
- Section/page: Sec. 3.3 (priors), p. 3
- Why others missed it: Priors were criticized as “informative,” but not their physical structure.
- Problem: Physically implausible prior on anomaly coefficient. The prior “Caγ flat on [1, 30]” treats what is typically a discrete UV‑model‑dependent anomaly coefficient (E/N‑like integer ratios) as a continuous linear variable with a broad ad hoc range, while absorbing or omitting α/2π. This prior has no clear physical basis and directly drives posteriors in Run 2.
- Required fix: Either (i) parametrize the analysis in terms of g_aγ with a physically motivated (e.g., log‑flat) prior and remove Caγ, or (ii) justify a discrete set of Caγ values from UV models and perform a model‑averaged analysis over that discrete set.

P2-META-M5
- Severity: MAJOR
- Section/page: Sec. 3.2 (p. 2–3); Sec. 6 (p. 5)
- Why others missed it: Systematics were mentioned for CMB only; extra‑CMB constraints were not.
- Problem: No cross‑check against non‑CMB birefringence constraints. A late‑time, achromatic rotation should also affect polarized light from distant radio galaxies/quasars. Several studies bound isotropic cosmic polarization rotation at the ~degree level over Gpc baselines. The paper neither cites nor checks compatibility of β ≈ 0.27° with these non‑CMB constraints.
- Required fix: Summarize contemporary extra‑CMB bounds on isotropic rotation and verify that β ≈ 0.27° is consistent. If any tensions exist, discuss how model specifics (e.g., redshift dependence) resolve them.

P2-META-m1
- Severity: MINOR
- Section/page: Sec. 2.1–2.2 (pp. 1–2)
- Why others missed it: Focus was on the inconsistency between Eq. (1) and the 10−2 claim; a smaller but telling issue remains.
- Problem: Inconsistent small‑angle vs full‑cosine language. The potential is written as 1 − cos(ϕ/fa), but the narrative implicitly toggles between small‑angle and large‑angle regimes without stating when the harmonic approximation is used (e.g., when mapping Δϕ/fa to “O(1)” or “∼10−2”). Given θi values up to O(1 rad), clarity is needed because the harmonic and full‑cosine dynamics differ materially in the late‑time rolling regime emphasized here.
- Required fix: State explicitly whether the harmonic approximation is ever used in analytics or forecasting; if so, specify the θi domain where it is applied and validate it against the full potential by numerical comparison.

P2-META-n1
- Severity: NIT
- Section/page: Throughout
- Why others missed it: Overshadowed by larger statistical issues.
- Problem: Units and symbol hygiene for angles. Angles appear in degrees in figures, in radians in equations, and in unspecified units in priors (e.g., θi flat on [0.01, π] but β priors in degrees). This complicates reproducibility and makes prior unit‑dependence easy to miss.
- Required fix: Adopt a single internal unit (radians) for all Bayesian priors/likelihoods and reserve degrees for final quoted numbers only. State this convention once and ensure all priors and Bayes‑factor ranges are expressed in radians.

Meta-review recommendation
REJECT

Given the union of all six reviews, there are multiple essential errors and omissions: inconsistent or undefined coupling normalization; a contradictory/unsupported derivation of Δϕ; use of uncitable or misattributed datasets; under‑converged MCMC; prior‑dependent and unit‑dependent Bayes factors; a physically inconsistent “spectator” energy budget; and, additionally from this meta‑review, hidden sign conditioning in the priors, an unstated Planck‑mass convention, and missing anisotropic and non‑CMB birefringence tests. Blockers exceed a dozen substantive items. Confidence that the paper would survive external peer review without a comprehensive rewrite is very low.