# P1B auto-2026-06-08_1424pt — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 447.5s

---

Meta-referee report (new issues not raised by the five prior reviewers)

P1B-META-E1
- Severity: ESSENTIAL
- Section + page: Sec. VI (Cosmic Birefringence), p. 7; Appendix C, p. 9
- Why others missed it: Reviewers checked scaling and priors qualitatively but did not test internal consistency of the ALP priors with the reported βALP number.
- Specific problem (quote): “βALP = 0.336° ± 0.107° (Caγ = 8 fixed), … The field-displacement range Δϕ/fa ∈ [0.2, 1.1] …”
  Using the paper’s own formula β = [αEM/(4π)] Caγ (Δϕ/fa), the maximum β attainable with Caγ = 8 and Δϕ/fa ≤ 1.1 is:
  βmax ≈ (5.8×10−4) × 8 × 1.1 rad ≈ 0.00510 rad ≈ 0.292°. The reported mean βALP = 0.336° exceeds this physical maximum. Equivalently, β = 0.336° implies Δϕ/fa ≈ β/[αEM Caγ/(4π)] ≈ 0.005867/(8×5.8×10−4) ≈ 12.6, far outside the stated [0.2, 1.1] envelope.
- Required fix: Reconcile the inconsistency by (a) showing that Δϕ/fa explored in the ALP-MCMC can in fact exceed 1.1 (and updating the stated envelope accordingly), or (b) correcting βALP (or the fixed Caγ) to be consistent with the allowed Δϕ/fa range. Explicitly report the formula used inside the ALP-MCMC and a table of (m/H0, θi) → Δϕ/fa to demonstrate the reachable β range for each fixed Caγ.

P1B-META-E2
- Severity: ESSENTIAL
- Section + page: Table II “Goodness-of-fit decomposition” and footnote c, p. 4
- Why others missed it: Prior reviews focused on a 0.1-unit rounding mismatch, not on the statistical meaning of the reported quantity.
- Specific problem (quote): “χ2total 14037.4 ± 5.6 … The mean-of-total χ2 here is GetDist’s weighted-sample average over the full posterior…”
  A posterior-weighted mean χ2 with an attached “±” spread is not a recognized GOF statistic for model checking; it conflates parameter-volume effects with fit quality and has no straightforward null distribution without specifying degrees of freedom. Presenting “± 5.6” risks being read as an uncertainty on χ2, which it is not.
- Required fix: Report GOF using standard metrics: best-fit (or maximum-posterior) χ2 with the number of data points and degrees of freedom, and a PTE (probability to exceed). If you also wish to show posterior summaries of χ2, present them separately and label them explicitly as posterior moments, not as GOF “uncertainties.”

P1B-META-M1
- Severity: MAJOR
- Section + page: Sec. IV (NaMaster), p. 5–6
- Why others missed it: Reviewers noted beam underspecification but not the attribution of bias.
- Specific problem (quote): “The bias is 0.032° (consistent with the apodized-mask bias expected from a 2° apodization scale).”
  The paper attributes the recovered β bias entirely to the mask/apodization without any control demonstrating that beam mis-modelling (using a “5 arcmin FWHM at 143 GHz” beam for a Commander CMB product with its own effective transfer function) is not the primary source. Since the estimator scales with EB/EE and the deconvolution uses bℓ, an incorrect bℓ can produce an amplitude bias that mimics an apodization effect.
- Required fix: Add robustness tests that (i) swap in the documented Commander effective beam (or an empirically measured transfer), (ii) vary the apodization scale, and (iii) toggle purify_b/purify_e. Show the recovered bias under each setting to justify attributing the 0.032–0.040° offset to the mask rather than to beam mis-modelling or purification.

P1B-META-M2
- Severity: MAJOR
- Section + page: Sec. IV (NaMaster), p. 5–6
- Why others missed it: Reviewers focused on missing estimator details; they did not probe missing robustness checks specific to purification/apodization choices.
- Specific problem (quote): “We use NaMaster’s spin-2 B-mode purification (purify b=True, purify e=False)… The bias … 0.032–0.040°.”
  B-mode purification can suppress part of the rotation-induced EB signal under a mask. No sensitivity study is shown to quantify how β̂ changes with purify_b on/off, purify_e on/off, or with different apodization radii. Without these tests, the sign and size of the reported bias cannot be attributed or bounded.
- Required fix: Report β̂ means and MC scatters for at least a 2×2 grid of (purify_b on/off) × (purify_e on/off) and for at least two apodization radii (e.g., 1° and 3°). State which choice is used in the headline “systematic floor,” and justify it with these comparisons.

P1B-META-M3
- Severity: MAJOR
- Section + page: Sec. III–IV, p. 3–6
- Why others missed it: The “auxiliary floor” language slipped by because the SNR definitional issue dominated.
- Specific problem (quote): “we carry forward [0.040°] as the NaMaster systematic floor; this is a methodology cross-check, not a competitive sky measurement.”
  The 0.040° “systematic floor” is derived from a bespoke NaMaster test on a degraded Commander map with ACT-like noise and a specific mask/apodization, but it is never propagated into the EB-likelihood fits used to quote βALP and βfree, which rely on a different analysis stack (“Planck PR4 + ACT DR6 EB-spectrum likelihoods”). Treating the NaMaster bias as a general floor yet not applying it where you report β posteriors is inconsistent.
- Required fix: Either (i) propagate the 0.040° as an additive systematic into βALP and βfree uncertainties and state the combined error, or (ii) explicitly decouple the NaMaster bias from the EB-likelihood results and refrain from calling it a general “systematic floor.”

P1B-META-M4
- Severity: MAJOR
- Section + page: Sec. III “MB–H0 joint-posterior offset check,” p. 4–5
- Why others missed it: One reviewer flagged dimensionless logging but not the hidden conditioning.
- Specific problem (quote): “sn.pantheonplus enforces a soft constraint on the combination MB − 5 log10(H0) ≈ const… This offset is ~3.2σ relative to the chain’s σMB = 0.049 marginal width and corresponds exactly to the canonical 3.6σ Hubble tension…”
  The 3.2σ mapping compares a 1D offset along an oversimplified SN degeneracy (omitting SALT2 and host-mass-nuisance directions and the proper use of h ≡ H0/100) with σMB, not with the actual curvature along the SN degeneracy. This is a hidden conditioning: it presumes the SN constraint is strictly 1D in MB−5log10 h and uses the marginal σMB as the scale, which overstates the comparability to the canonical H0 tension.
- Required fix: Re-express the Pantheon+ degeneracy using h (dimensionless) and include the relevant nuisance directions (or show they are negligible). If you wish to map the offset to a σ, project the joint Pantheon+ covariance onto the (MB − 5 log10 h) axis and use its 1D variance, not σMB, to compute the offset in σ units. Remove “corresponds exactly to the canonical 3.6σ” unless you quantitatively demonstrate it with the correct covariance.

P1B-META-M5
- Severity: MAJOR
- Section + page: Sec. III, Table I footnote a, p. 3
- Why others missed it: Prior reviews questioned counts/labels but not the nuisance-parameter set itself.
- Specific problem (quote): “10 Planck likelihood nuisance: Aplanck, amp143, amp217, amp143×217, n143, n217, n143×217, calTE, calEE, Mb…”
  The listed set mixes CamSpec cross-spectrum amplitudes/slopes with calibration parameters and includes Mb (a supernova nuisance) inside the count of “Planck likelihood nuisance.” This conflation makes it unclear which parameters are active in which likelihoods and risks double-counting or mis-assigning priors. It also suggests both amplitude (Aplanck) and individual cross-spectrum amplitude terms are simultaneously free, which is non-standard for CamSpec and can distort cosmological parameters through degeneracies.
- Required fix: Provide a per-likelihood nuisance table: list nuisance parameters, priors, and which likelihood(s) each belongs to. Clarify whether Aplanck and the band-specific amplitude terms are both active, and justify that choice with references to the CamSpec configuration used.

P1B-META-m1
- Severity: MINOR
- Section + page: Abstract and Sec. III, p. 1–3
- Why others missed it: Focus was on broader framing and dataset issues.
- Specific problem: Abstract states “H0 consistent with standard ΛCDM … at 0.3σ,” but no reference value or calculation is shown anywhere to substantiate “0.3σ.”
- Required fix: Quote the specific Planck baseline H0 (value and σ) used for the comparison and show the one-line calculation leading to “0.3σ.” If you mean relative to your Planck+BAO+SN chain, say so explicitly.

P1B-META-m2
- Severity: MINOR
- Section + page: Sec. VI Eq. (3), p. 7
- Why others missed it: They flagged missing explicit formula but not the definition mismatch.
- Specific problem (quote): “β ≈ αEM × 8/(4π) × 1.07 ≈ 0.29°.”
  The 1.07 factor is from Δϕ/fa but the equation does not show the general form β = [αEM/(4π)] Caγ (Δϕ/fa); as written, it looks like a special-case numerical recipe and obscures that Δϕ/fa is the only model-dependent part in the prefactor.
- Required fix: Replace Eq. (3) with the general formula β = [αEM/(4π)] Caγ (Δϕ/fa) and then evaluate it at the stated benchmark, explicitly identifying Δϕ/fa = 1.07 as coming from the ODE solution at the chosen (m/H0, θi).

P1B-META-n1
- Severity: NIT
- Section + page: Sec. IV and Conclusions, p. 5–8
- Why others missed it: The numeric content overshadowed stylistic precision.
- Specific problem: The paper calls the 0.040° bias a “systematic floor” but never states whether the “floor” is absolute (bias) or relative (fractional), nor how it would combine with statistical errors in future forecasts (e.g., LiteBIRD’s σ(β) ≈ 0.03°).
- Required fix: Define “systematic floor” precisely (absolute angle in degrees), and if you retain it, show how it would combine in quadrature (or not) with a statistical σ when projecting detection significances.

Meta-review recommendation
REJECT

Rationale: In addition to the extensive issues already identified by the five reviewers (non-existent/future-dated references; inconsistent dataset/likelihood labeling; under-specified estimators; incorrect pivot-covariance math; off-topic w0–wa table; mis-framed significance; internal review-log artifacts), there is a fundamental internal inconsistency in the ALP section (P1B-META-E1) showing that the reported βALP cannot be produced by the stated ALP priors with Caγ fixed = 8. The goodness-of-fit reporting is methodologically inappropriate (P1B-META-E2). The NaMaster bias attribution is unsubstantiated and not propagated consistently (P1B-META-M1/M3). The SN “degeneracy” σ mapping is based on hidden conditioning (P1B-META-M4). These are not cosmetic; they cut to the correctness and interpretability of the main numerical claims.

Given the union of all six reviews, the blocker count is high: at least 10–15 essential/major corrections (including fabricated citations, dataset/likelihood inconsistencies, ALP inconsistency, estimator specification/robustness, model-comparison omissions, and structural/narrative problems). My confidence that the paper would survive external, independent peer review in its current form is very low. Even with substantial revision, several sections would need to be re-run, re-documented, and re-framed before the manuscript could be considered for PRD.