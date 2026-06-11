# P1B R29 — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 429.3s

---

META-REVIEW (new issues none of the 5 prior referees caught)

P1B-META-E1 — ALP sign restriction silently removes half the physical parameter space
- Severity: ESSENTIAL
- Section + page: Sec. VI (pp. 10–13), Appendix C (p. 15)
- Why others missed it: Reviewers focused on fine-tuning and prior ranges, but not on sign symmetry of the coupling/product.
- Specific problem: The ALP fits sample Caγ only over positive intervals (e.g., “Caγ: uniform prior on [4, 60] …” Appendix C) and θi ∈ [0.01, π], so Caγ(Δϕ/fa) is constrained to be positive and β must be positive by construction. In QED-axion models Caγ can be ±O(1) depending on UV details, and Δϕ can change sign; the observable is sensitive only to the product CaγΔϕ/fa.
- Required fix: Re-run the ALP chains with a sign-symmetric prior (e.g., Caγ ∈ [−60, +60] and θi ∈ [−π, +π], or equivalently allow Δϕ to be signed). Report how allowing β < 0 affects the posterior (it should be nearly symmetric around zero given a purely amplitude-constraining likelihood). State explicitly that the observed positive β does not fix the sign convention uniquely.

P1B-META-E2 — Hidden BBN-consistency/validity assumption for ΔNeff < 0 not checked
- Severity: ESSENTIAL
- Section + page: Sec. III (pp. 2–5)
- Why others missed it: Prior reviewers discussed one-sided limits and neutrino mass degeneracy, but not the BBN Yp mapping domain for negative ΔNeff.
- Specific problem: The run uses “YHe follows the CAMB BBN-consistent default (no explicit override)” while adopting a flat prior that permits ΔNeff down to −1. The standard BBN fits embedded in Boltzmann solvers are calibrated over a limited range around Neff ≈ 3; pushing to Neff ≈ 2 can step outside validated coverage and bias the CMB inferences through Yp(Ωbh^2, Neff).
- Required fix: Either (a) document the Yp(Neff, Ωbh^2) validity range used by CAMB and confirm that the posterior weight at Neff < 3 lies within it, or (b) add a robustness run fixing Yp (or adopting the PArthENoPE/PRIMAT Yp table over a validated domain) and show ΔNeff/H0 are unchanged within errors. If not, restrict the ΔNeff prior to the BBN-validated interval and recompute one-sided limits.

P1B-META-M1 — Missing TB-channel validation for the rotation pipeline
- Severity: MAJOR
- Section + page: Sec. IV (pp. 6–9)
- Why others missed it: They concentrated on EB estimator weighting and binning, not on the companion TB observable.
- Specific problem: Uniform rotation generates both EB and TB: CEB ∝ ½ sin(4β)(CEE − CBB) and CTB ∝ ½ sin(4β)CTE. The paper validates EB only; TB is never tested, even though T×E carries different S/N and mode-coupling structure and is used in several published analyses as a cross-check.
- Required fix: Add a TB template-fit validation (same MC skies) and report recovered β and bias. At minimum, show EB- and TB-based estimates agree within the 0.040° pipeline floor and that combining them does not change the conclusion.

P1B-META-M2 — Periodicity/multimodality of the β likelihood is untested for the estimator used
- Severity: MAJOR
- Section + page: Sec. IV (pp. 6–9)
- Why others missed it: They noted wrapping only for the ALP summary likelihood, not for the pipeline estimator.
- Specific problem: The text notes “the uniform-rotation observable is periodic, β ≡ β + n × 90°” only in the ALP-likelihood context. For the NaMaster pipeline, the β estimator is a grid search against sin(2β)cos(2β)CEE; no demonstration is provided that the likelihood over β in [−90°, +90°] is unimodal or that the grid does not misidentify a secondary lobe (e.g., near 45° − β).
- Required fix: Plot the χ2(β) or SNR(β) curve over the full period [−90°, +90°] for a representative realization and show the global maximum lies at the injected β with no competing maxima above the fit grid tolerance. State the β-grid boundaries and step size in the main text.

P1B-META-M3 — Instrumental-miscalibration α not co-injected; degeneracy behavior untested
- Severity: MAJOR
- Section + page: Sec. IV (pp. 6–9)
- Why others missed it: They accepted the scope note about β–α degeneracy but did not ask for a stress test.
- Specific problem: The validation injects only β. A realistic EB/TB pipeline must contend with joint (β, α) rotations (sky vs. instrument). With no galactic foregrounds in the MC, the β–α degeneracy is exact; this is precisely where one should test whether the estimator is identifiable (or not) and how nuisance α would bias β recovery if left free or fixed incorrectly.
- Required fix: Add a two-parameter injection test with (β, α) and demonstrate: (i) β is unrecoverable without an external α prior (as expected), and (ii) with a realistic α prior (e.g., Planck Tau A), the recovered β remains within the quoted bias floor. Make clear in the main text which nuisance constraints would be required on real data.

P1B-META-M4 — The ΔP convention (per Q/U vs per polarization pair) is used to set σpix but never tied to the ACT-like number actually adopted
- Severity: MAJOR
- Section + page: Sec. IV, “Noise model and injections” (pp. 6–8)
- Why others missed it: One reviewer flagged the √2 ambiguity in general, but not its alignment with “ACT-like” in this paper.
- Specific problem: The paper takes ΔP = 10 μK·arcmin as “ACT-like” and sets σpix = ΔP/√Ωpix “with no √2 factor.” ACT noise levels in the literature are sometimes quoted per Stokes (Q or U), sometimes per combined P; which convention is 10 μK·arcmin here? Without matching conventions, the injected noise level can be off by √2.
- Required fix: Cite the specific ACT DR6 polarization noise convention the 10 μK·arcmin number refers to and confirm that your σpix mapping matches that convention. If not, correct the conversion and re-quote the recovered bias and SNR.

P1B-META-m1 — AI assistant acknowledgment in the Acknowledgments is not PRD-standard and may trigger policy issues
- Severity: MINOR
- Section + page: Acknowledgments (p. 14)
- Why others missed it: They focused on scientific content, not journal policy.
- Specific problem: “The author acknowledges the use of Claude (Anthropic) as an AI research assistant …” PRD style typically discourages tool marketing and may require disclosure in a different form (e.g., “large-language model assistance was used for drafting; all scientific content was verified by the author”).
- Required fix: Replace the product-specific mention with a generic statement that conforms to APS/PRD policy or remove it.

P1B-META-m2 — Equation-of-motion benchmarking range in Sec. VI inconsistent with “natural box” framing without a single, consolidated table
- Severity: MINOR
- Section + page: Sec. VI (pp. 10–13)
- Why others missed it: They noted fine-tuning and “envelope scans,” but not the presentational gap.
- Specific problem: The text alternates among “natural parameter range m/H0 ∈ [1,3], θi ∈ [0.5,2],” “posterior prefers m ∼ 10–10^2 H0,” and “continuous prior log10(ma/eV) ∈ [−35, −30] (m/H0 ≈ 7×10−3 to 7×10^2).” These are consistent but scattered, making it hard to see at a glance how the benchmarks, priors, and posteriors relate.
- Required fix: Add a one-row summary table listing: (a) benchmark “natural box,” (b) sampled prior range (continuous run), and (c) posterior-preferred ranges for m/H0, θi, and Caγ. This will prevent accidental misreadings of “natural” vs “preferred.”

P1B-META-m3 — No explicit statement that the EB template used in fits is exactly ½ sin(4β) times the measured, masked CEE bandpowers (or otherwise)
- Severity: MINOR
- Section + page: Sec. IV (pp. 6–9)
- Why others missed it: They did ask about pixel windows and ℓ-range, but not the exact form used in code.
- Specific problem: The text alternates between “fit of decoupled CEBb to sin(2β)cos(2β)CEEℓ” and “matched extension with (CEE − CBB),” but never explicitly states whether CEEb is the measured, decoupled, non-deconvolved bandpower from the same masked realization or a theory spectrum forward-filtered. The “beam/pixel-window cancel” claim hinges on this.
- Required fix: State unambiguously that the template uses the measured, decoupled CEEb (or a forward-filtered theory CEE), and confirm the same filtering (mask coupling, pixel window) is applied to template and data. If not, quantify the induced multiplicative mismatch.

P1B-META-N1 — Minor typographical/notation clarity in Eq. (3) pre-factor
- Severity: NIT
- Section + page: Sec. VI (p. 11)
- Why others missed it: They focused on the arithmetic (which is correct).
- Specific problem: “β ≈ αEM × 8 / 4π × 1.06 …” could be read as (αEM × 8)/(4π) × 1.06, but writing “(αEM/4π) Caγ (Δϕ/fa)” once as the displayed expression avoids ambiguity.
- Required fix: Replace the inline “αEM × 8 / 4π” by the explicit product form and include the one-line dimensional statement Δϕ/fa is dimensionless.

Meta-review recommendation
MAJOR REVISIONS

Given the union of all six reviews, there are multiple essential and major blockers: (i) ALP sign-prior restriction and ΔNeff–BBN validity (new here), (ii) SN double-counting in the w0wa stack, (iii) Planck likelihood pairing/lensing inconsistency, (iv) incomplete NaMaster robustness (binning/ℓ-range) and missing TB/β–α tests, (v) provenance/versioning, and (vi) presentation issues (overstated marginal-tail “σ,” internal-artifact prose, and figure/legend fixes). My confidence that the paper would survive external (non-series) PRD peer review without these fixes is low; with the requested changes, especially the SN/cosmology-stack hygiene, Planck pairing check, and ALP prior symmetry, it could be rehabilitated.