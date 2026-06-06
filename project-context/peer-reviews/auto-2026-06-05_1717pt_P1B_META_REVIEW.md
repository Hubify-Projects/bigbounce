# P1B auto-2026-06-05_1717pt — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 407.2s

---

META-REVIEW (focus: blind spots none of the 5 referees caught)

P1B-META-E1
- Severity: ESSENTIAL
- Section + page: Sec. III, “MB–H0 joint-posterior offset check” (p. 4)
- Why others missed it: Reviewers checked the arithmetic but not the statistical conditioning behind the relation used.
- Specific problem (quote + issue): The text asserts “sn.pantheonplus enforces a soft constraint on the combination MB − 5 log10(H0) ≈ const along the SN distance-modulus degeneracy,” and then computes −28.571 from the SH0ES anchor as “the Pantheon+ constraint axis.” This is conceptually wrong: Pantheon+ by itself is insensitive to H0 and does not fix the constant MB − 5 log10(H0); that constant is set only once an external absolute-calibration prior (e.g., SH0ES) is applied. Using the SH0ES-derived value as “the Pantheon+ constraint axis” to diagnose YAML aliasing is therefore a misinterpretation of the SN degeneracy.
- Required fix: Recast the MB–H0 diagnostic correctly. Explicitly state that Pantheon+ alone leaves MB unconstrained (degenerate with H0), and that the constant is set by the SH0ES prior. If the goal is to verify the SH0ES prior is actually active and coupled, show (i) the posterior correlation coefficient corr(MB, log10 H0); (ii) a 2D posterior contour MB vs H0 with and without the SH0ES prior; and (iii) the explicit form of the Pantheon+ likelihood as used (distance-modulus residuals independent of H0). Remove language implying Pantheon+ fixes the constant −28.571.

P1B-META-E2
- Severity: ESSENTIAL
- Section + page: Sec. III/Table I (pp. 3–5)
- Why others missed it: Prior reviews focused on dataset versions and evidence metrics; none examined ΔNeff modeling assumptions that dominate the constraint.
- Specific problem (quote + issue): The paper repeatedly quotes ΔNeff posteriors from “stock CAMB” but never states the helium treatment or neutrino-mass prior: whether Yp is set by BBN consistency as a function of (ωb, ΔNeff) and whether Σmν is fixed (and to what value). These choices materially change ΔNeff constraints (and H0 posteriors) at the quoted precision.
- Required fix: State explicitly (i) whether BBN consistency was enforced (and which fitting formula/library and version), or if Yp was fixed; (ii) the Σmν prior (fixed to 0.06 eV vs. free with prior), number of massive species, and mass splitting convention; and (iii) whether Nν,eff in the neutrino hierarchy is tied to radiation density only or allowed to vary independently. Provide a short sensitivity test (one chain or Fisher) showing how ΔNeff and H0 shift under alternative standard choices (BBN on/off; Σmν fixed/free).

P1B-META-M1
- Severity: MAJOR
- Section + page: Sec. III/Table I; likelihood settings (pp. 3–6)
- Why others missed it: Focus remained on CamSpec/NPIPE naming; not on internal Planck nuisance/extended parameters.
- Specific problem (quote + issue): The treatment of the CMB lensing-amplitude parameter AL is not stated. AL (free vs fixed at 1) can correlate with ΔNeff, ns, and σ8 and alter derived constraints, especially with CamSpec TTTEEE+lensing. Without disclosing AL, reproducibility and interpretation of ΔNeff and σ8 are ambiguous.
- Required fix: State whether AL was fixed to 1 or sampled; if sampled, report its posterior and R̂; if fixed, justify. Add a short note on the impact (ΔNeff, H0) of toggling AL in this stack.

P1B-META-M2
- Severity: MAJOR
- Section + page: Table I footnote (p. 3)
- Why others missed it: They checked counts and R̂ but not the taxonomy of nuisance blocks.
- Specific problem (quote + issue): The footnote lists “10 Planck likelihood nuisance: Aplanck, amp143, amp217, amp143×217, n143, n217, n143×217, calTE, calEE, Mb...” but MB is not a Planck-likelihood nuisance; it is a supernova-nuisance parameter. This misclassification undermines clarity about which likelihoods constrain which parameters and complicates convergence interpretation per block.
- Required fix: Correct the parameter taxonomy: present a clean table splitting cosmological vs each-likelihood’s nuisances (Planck high-ℓ; low-ℓ; lensing; BAO; Pantheon+; SH0ES; DES S8). Report R̂ and min ESS per block.

P1B-META-M3
- Severity: MAJOR
- Section + page: Sec. IV (pp. 5–6)
- Why others missed it: They focused on beam and purification; not on the β-injection protocol relative to instrument angle systematics.
- Specific problem (quote + issue): “The β injections rotate Q+iU via e^{2iβ}(Q+iU) before adding noise.” This models cosmic birefringence only. However, the paper’s stated scope is to “validate deconvolution under MASTER mode coupling,” which is equally sensitive to spurious EB from a uniform instrument angle error α. An instrument miscalibration rotates both signal and instrument-noise polarization. The present MC rotates the sky-only and leaves noise unrotated; there is no MC branch that tests α-like rotations where noise is rotated with the signal.
- Required fix: Add a second MC branch that applies a uniform rotation to both the map and the noise realization (instrument-miscalibration surrogate) and report β̂ biases/variances there. This cleanly distinguishes the β-vs-α response in the pipeline and tests robustness to angle systematics at the algorithmic level (even if sky-foreground information is not included).

P1B-META-M4
- Severity: MAJOR
- Section + page: Sec. III vs. Sec. V/Table II (pp. 3–6)
- Why others missed it: They flagged dataset-version confusion, but not the label re-use with incompatible results.
- Specific problem (quote + issue): The label “Planck+BAO+SN” is used in two different contexts with incompatible posteriors: Table I reports H0 = 67.79 ± 1.09 (Planck+BAO+SN), whereas Table II (labeled “DESI DR2 w0wa … + Pantheon+”) reports H0 = 67.185 ± 0.455. The paper never disambiguates that one “Planck+BAO+SN” includes a w0wa extension and a different BAO stack and that the other is ΛCDM+ΔNeff; readers can easily misinterpret these as the same combination.
- Required fix: Standardize dataset labels across the paper to include both model and data version (e.g., “ΛCDM+ΔNeff: Planck PR4 lowℓ + CamSpec TTTEEE + lensing + BAO (set X) + Pantheon+”; “w0wa: Planck PR4 lowℓ + CamSpec + lensing + DESI [version] BAO + DES-Y5 + Pantheon+”). Add a one-line legend under each table specifying the model and exact data stack.

P1B-META-M5
- Severity: MAJOR
- Section + page: Sec. VI (pp. 6–7)
- Why others missed it: They checked the CaγΔφ/fa arithmetic but not the implied coupling scale versus fa ~ MPl.
- Specific problem (quote + issue): The paper argues Caγ ∈ [~9, ~51] is “accommodated in extended models,” while fixing fa ∼ MPl. For fa ~ MPl, the implied photon coupling g_{aγ} = α C_{aγ}/(2π f_a) is O(10^−21 – 10^−20) GeV^−1, which is far below typical laboratory/astrophysical sensitivities but also in tension with achieving β ≈ few × 10^−3 rad unless Δφ/fa is near the top of the quoted range. The manuscript does not check consistency against bounds on ultra-light axion-like fields with fa ≳ GUT–Planck and CMB/stellar-cooling constraints on Caγ at those fa. The “accommodated” statement is too strong without referencing these global constraints.
- Required fix: Add a constraints panel or paragraph comparing the required (C_{aγ}, f_a=MPl) to known limits (e.g., stellar cooling and CMB birefringence bounds framed as g_{aγ}; plus limits on ultra-light ALPs from black-hole superradiance if applicable). If substantial tension exists for Caγ ≳ O(10), qualify the claim accordingly or adjust the favored parameter window.

P1B-META-M6
- Severity: MAJOR
- Section + page: Sec. IV (p. 5)
- Why others missed it: They flagged beam and noise, but not low-ℓ filtering.
- Specific problem (quote + issue): The pipeline uses ℓmin = 30 without documenting any large-scale mode filtering or mapmaking transfer function for the Commander product at Nside=512. EB-based β estimation is especially sensitive to residual striping/large-scale systematics at ℓ < 50. No test is shown that the chosen ℓmin = 30 is above any unsafe transfer-function regime post-degradation.
- Required fix: Justify ℓmin = 30 with a transfer-function test: (i) compute β̂ on MC skies with a conservative low-ℓ cut sweep (e.g., ℓmin = 20, 30, 50); (ii) demonstrate stability of the mean and variance; or (iii) adopt a safer ℓmin if needed. Report any change in the systematic bias figure.

P1B-META-m1
- Severity: MINOR
- Section + page: Sec. VI, Eq. (2) and surrounding text (pp. 6–7)
- Why others missed it: They checked numbers, not dimensional clarity of variables.
- Specific problem (quote + issue): Symbols {ϕ, fa, m, θi} are used with mixed dimensional conventions (ϕ as a field with mass dimension vs. normalized angle θ ≡ ϕ/fa). The text moves between Δϕ/fa and θi without an explicit definition block near Eq. (2), risking confusion about whether “Δϕ/fa ≈ 0.65” is an angle or a normalized displacement.
- Required fix: Add a one-line definitions box at the start of Sec. VI: “We define θ ≡ ϕ/fa; Δθ ≡ Δϕ/fa; m in units of H0; Caγ dimensionless; β = [αEM/(4π)] Caγ Δθ.” Use θ consistently thereafter.

P1B-META-m2
- Severity: MINOR
- Section + page: Sec. IV (p. 5)
- Why others missed it: Focus stayed on the presence/absence of foregrounds, not on the Commander product used.
- Specific problem (quote + issue): “The Planck Commander Q/U maps are provided at Nside = 2048 … we degrade to Nside = 512 …” It is not specified whether the map is the full-sky Commander CMB solution or a polarization-only product, nor whether the mask excludes regions where the Commander CMB solution is poorly constrained in polarization. This matters for the claimed fsky = 0.32 and the leakage bias at the chosen apodization scale.
- Required fix: Identify the exact Commander polarization product used (file name/version) and show the unmasked sky fraction pre- and post-apodization. Provide the number of unmasked pixels at Nside=512. If necessary, adjust fsky and re-quote the bias figures.

P1B-META-m3
- Severity: MINOR
- Section + page: Sec. III/Table I (p. 3)
- Why others missed it: They focused on numbers, not definition.
- Specific problem (quote + issue): The paper reports S8 posteriors but never defines S8. While widely used, PRD expects definitions for derived parameters used centrally.
- Required fix: Add the explicit definition S8 ≡ σ8 (Ωm/0.3)^{1/2} once (e.g., in the Table I caption or Sec. III text).

P1B-META-N1
- Severity: NIT
- Section + page: Footnote 2 (p. 3)
- Why others missed it: Outside core cosmology; easy to overlook.
- Specific problem (quote + issue): “Λstrong ∼ MPl/√γBI set by the inverse Barbero–Immirzi parameter γBI” is asserted without reference. The scale dependence on γ is model-specific and not standardly quoted with a square root. As written, it reads like an unsupported heuristic.
- Required fix: Either remove the formula or add a precise reference deriving the γ-dependence of the torsion strong-coupling scale in the Holst+fermions EFT; if uncertain, state it qualitatively (Λstrong ∼ O(MPl)) without a γBI scaling.

Meta-review recommendation
REJECT

Given the union of all six reviews, the blocker count is high. Beyond the already substantial issues flagged by the other referees (non-public/future-dated datasets and citations; missing estimator/likelihood details; internal-process prose; Commander beam; SN double counting; downgrade/noise modeling; evidence deferral), this meta-review adds further essential problems in the statistical conditioning of the SN degeneracy argument (E1), incomplete specification of ΔNeff modeling assumptions (E2), and missing disclosure of the AL lensing amplitude (M1), any of which alone would preclude acceptance. My confidence that the paper would survive independent external peer review is low until all public-data/citation problems are fixed, the β-estimator and EB likelihood are fully specified, and the additional issues above are corrected.