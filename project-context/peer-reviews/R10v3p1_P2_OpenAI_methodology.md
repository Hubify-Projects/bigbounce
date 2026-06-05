# P2 R10v3p1 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (8355 chars)
**Wall time**: 339.3s

---

Referee report on “Cosmic Birefringence from a Planck-Scale Axion-Like Particle: Predictions, Constraints, and LiteBIRD Forecasts”

Overall assessment
The paper aims to connect a minimal ALP model (fa ~ MPl, m ~ H0, θi ~ O(1)) to the reported isotropic cosmic birefringence signal, and to provide a summary-likelihood combination of Planck and ACT measurements, simple MCMC fits, and a LiteBIRD forecast. The topic is timely. However, there are serious methodological and internal-consistency issues:

- The central theoretical prediction for the field displacement and hence β is internally inconsistent (Eq. 1 vs. Sec. 2.2 narrative).
- A Bayes factor is numerically inconsistent with the data reported, and uses a one-sided prior at the parameter boundary without justification; the dependence on prior width is miscomputed.
- A key “effective photon coupling” quantity reported in the abstract and main text is undefined and dimensionally unclear.
- The choice C=8 in Run 1 contradicts the “order-unity” premise and is not justified.
- The summary-likelihood combination assumes independence without an explicit discussion of cross-experiment correlations relevant to birefringence estimators.
- The MCMC sample sizes are too small for the breadth of claims (evidence, posterior tail properties), and effective sample sizes/chains are not documented.
- Several places juxtapose “σ” significances from different procedures (summary-likelihood vs. full-spectrum fits) without an explicit “not directly comparable” disclaimer at each juxtaposition.

I list detailed findings below.

ESSENTIAL ISSUES

P2-E1 (Sec. 2.1–2.2, pp. 1–2): Inconsistent displacement and β prediction
- Offending text/equations:
  - Eq. (1), p. 2: “∆ϕ ≈ fa θi (1 − J0(m/H0)/J0(0)) ≈ fa θi × O(1). For m/H0 ∼ 1, 1 − J0(1) ≈ 0.24”
  - Sec. 2.2, p. 2: “the cosmological field evolution gives ∆ϕ/fa ∼ 10−2 ... yielding β ≈ C0 θi × 5×10−3 rad ≈ 0.27°.”
- Problem: Eq. (1) implies ∆ϕ/fa ≈ 0.24 θi (i.e., O(10−1)), but Sec. 2.2 asserts ∆ϕ/fa ∼ 10−2 without derivation. The resulting β differs by a factor ~24. The key prediction (β ≈ 0.27°) hinges on the latter. No derivation or reference is provided to reconcile these.
- Required fix: Provide a correct, fully worked derivation of ∆ϕ/fa between recombination and today for m ~ H0 in ΛCDM (or cite and reproduce the main steps), including the role of the slow-roll/oscillatory regime and the time dependence of H(a). If Eq. (1) is an approximation, demonstrate when it holds and why the numerical factor is ~10−2 rather than ~0.24. Update all ensuing numerical predictions consistently. If the prediction is instead driven by near-harmonic evolution with small excursions, show explicitly why ∆ϕ/fa is suppressed.

P2-E2 (Sec. 3.4, p. 3): Bayes factor numerical inconsistency and improper prior handling at boundary
- Offending text: “ln B = 5.17 ... computed via the Savage-Dickey density ratio with a flat prior β ∈ [0°, 1°]. ... ln B = 4.48 for β ∈ [0°, 2°] and ln B = 5.86 for β ∈ [0°, 0.5°].”
- Problem:
  - Using the combined summary-likelihood β = 0.242 ± 0.061° (Eq. 4), the Savage–Dickey ratio for H0: β=0 versus H1: β free with a uniform prior on [0°,1°] yields posterior density at β=0: f(0) = (1/(σ√2π)) exp(−µ^2/(2σ^2)) ≈ 0.00248 deg−1. With prior density 1 deg−1, B10 = prior/posterior = 1/0.00248 ≈ 403 → ln B10 ≈ 6.0, not 5.17. For [0°,2°], ln B10 ≈ 5.31; for [0°,0.5°], ln B10 ≈ 6.69. All differ from the values quoted.
  - The prior support is one-sided with the null value at the boundary. This requires explicit treatment of truncation effects or, more simply, adopting a symmetric prior around zero, since β can in principle be negative. The boundary choice inflates evidence in favor of H1 relative to a symmetric prior.
- Required fix: Recompute ln B using a symmetric prior (e.g., β ∈ [−1°, 1°]) and report both B01 and B10 with clear definitions. Provide the exact calculation (not just SDDR shorthand), including the effect of truncation if a one-sided prior is retained. Update all quoted ln B values and their prior dependence.

P2-E3 (Abstract p. 1; Sec. 3.2 p. 2): Undefined “effective photon coupling” fphoton × C0 = 1.73 ± 0.44
- Offending text: “The effective photon coupling fphoton × C0 = 1.73 ± 0.44 (order-unity, no fine-tuning).”
- Problem: This parameter is not defined anywhere. It has unclear dimensions (the standard coupling is gaγ = C0/fa with mass dimension −1). No equation links it to β, the data, or model parameters. As written it is not reproducible.
- Required fix: Define fphoton precisely, including dimensions and its appearance in the birefringence formula. Derive the mapping from the combined β measurement (Eq. 4) to this parameter and show the propagation of uncertainty. If this is a placeholder for an “O(1)” cosmological transfer factor, rename it to avoid confusion with a coupling and quantify it from a proper integral.

P2-E4 (Sec. 3.3, Table 1 p. 3; text pp. 3–4): Unjustified choice C=8 and inconsistency with “order unity”
- Offending text: Table 1 and Sec. 3.3: “Run 1 ALP (C = 8 fixed).” Elsewhere C0 is said to be order unity from the ABJ anomaly.
- Problem: C=8 is not motivated or referenced. It contradicts the statement that “no fine-tuning” is required and that the anomaly coefficient is O(1). The impact of fixing C=8 on β and on the inferred θi and m is non-negligible.
- Required fix: Provide a microphysical justification (e.g., specific UV model) or literature reference for C=8. Alternatively, do not fix it ad hoc; keep it a parameter with a motivated prior (e.g., centered near 1 with support up to O(10)), and update Run 1 accordingly.

P2-E5 (Sec. 3.2 p. 2; throughout): Mixed and juxtaposed significances from different procedures without explicit non-comparability
- Offending text: Abstract and Secs. 1–3 cite 2.5σ, 2.7σ, 2.9σ, 3.6σ, and 3.9σ from different analyses (planar self-calibration, EB-spectrum fit, and summary-likelihood combination) with statements like “Combined, the evidence exceeds 3.5σ” and side-by-side comparisons to βobs = 0.342 ± 0.094°.
- Problem: These σ values arise from distinct estimators and analysis choices and are not directly comparable. The paper does not consistently flag this at each juxtaposition, risking overstatement of the cumulative evidence.
- Required fix: Every time different σ results are juxtaposed, add an explicit statement that they are not directly comparable and explain the methodological differences (e.g., full-spectrum EB fit vs. point-estimate combination). Limit integrative claims (e.g., “exceeds 3.5σ”) to a single, well-defined estimator or provide a meta-analysis framework.

MAJOR ISSUES

P2-M1 (Sec. 3.2 p. 2): Independence assumption for Planck and ACT errors not justified
- Offending text: “combining the measurements under the assumption of independent errors”
- Problem: While instrumental systematics are independent, both experiments observe the same sky. For isotropic birefringence β estimated via EB, cosmic-variance correlations are typically subdominant but not zero; calibration degeneracies and foreground modeling could induce correlated biases. No quantitative argument is given.
- Required fix: Provide a justification (e.g., show that the covariance from shared-sky EB is negligible relative to noise/systematic floors, or cite a study demonstrating negligible cross-correlation) or include a correlation coefficient in the combination and assess sensitivity to plausible ρ values (e.g., 0–0.3).

P2-M2 (Sec. 3.3 p. 3–4; Table 1): MCMC size, chains, and effective sample sizes insufficiently documented for reported claims
- Offending text: “sample sizes (720–6,840 accepted samples) ... R̂−1 < 0.01 ... small effective sample sizes (Neff ∼ 1,000) limit...”
- Problem: The number of chains, warm-up, proposal, and computation of Neff are not reported. A Bayes factor claim and tail behavior require reliable Neff in the tails and convergence diagnostics across multiple chains. 720 posterior draws (Run 3) is marginal for robust credible intervals.
- Required fix: Report number of chains, warm-up, total draws, and thinning. Provide autocorrelation times and computed Neff per parameter (not just a single approximate number). Target Neff ≥ 5,000 per scalar parameter for the Bayes factor and tail inferences, or drop the Bayes factor from MCMC and compute it analytically from the Gaussian summary-likelihood.

P2-M3 (Sec. 2.1, p. 1–2): Bessel J0 form and “O(1)” factor need derivation or reference
- Offending text: Eq. (1) with J0(m/H0) and the statement “the precise value depends on the cosmological integration through the matter and dark-energy eras.”
- Problem: No derivation or reference connects the ALP equation of motion in an expanding universe to this Bessel expression. As written it suggests a toy-model background with constant H or special function approximations. This is central to the claimed “naturalness.”
- Required fix: Derive Eq. (1) from the EOM with the appropriate background H(a), or replace with a standard slow-roll/oscillatory integral (with a cited result) and provide a numerical integration demonstrating the quoted factor for ΛCDM.

P2-M4 (Abstract p. 1; Sec. 4 p. 3): Over-strong exclusion phrasing in LiteBIRD forecast
- Offending text: “If LiteBIRD measures β = 0 ± 0.03°, the ALP explanation is excluded at 9σ.”
- Problem: The ALP model has free parameters (C0, θi) that can produce arbitrarily small β. A null β would exclude the specific point prediction (C0θi times the chosen cosmological factor), not the entire ALP model class. The text later notes prior dependence, but the strong “excluded at 9σ” is overstated.
- Required fix: Rephrase to: “would exclude the specific O(1) amplitude prediction (for fa ~ MPl, m ~ H0, and θi, C0 ~ O(1)) at ~9σ,” and clarify which parameter ranges would remain viable.

P2-M5 (Sec. 3.3 p. 3–4; Fig. 1): Priors and parameterization need clearer justification
- Offending text: Priors “θi ∈ [0.01, π], log10(m/eV) ∈ [−35, −30], Caγ ∈ [1, 30]”
- Problem: The lower cutoff at θi=0.01 excludes small misalignment that could produce β~0. The Caγ prior lower bound at 1 conflicts with “order unity including sub-unity” and biases amplitudes upward; the upper bound at 30 is very wide relative to ABJ expectations. No sensitivity test is shown.
- Required fix: Justify these bounds from theory or perform prior-sensitivity tests. Include priors allowing θi→0 and Caγ<1 (e.g., log-uniform over [0.1, 30]) and report how posteriors and β change.

MINOR ISSUES

P2-m1 (Sec. 2.2 p. 2): Numerical conversion and factor-of-2 clarity
- Offending text: “β ≈ C0 θi × 5×10−3 rad ≈ 0.27°.”
- Problem: 5×10−3 rad = 0.286°; also Eq. (2) has a factor of 1/2 that must be carried through consistently.
- Required fix: State the exact factor (carry the 1/2) and give the correct conversion 0.286° (or update the underlying factor to match 0.27° if warranted by the corrected displacement).

P2-m2 (Sec. 1 p. 1): “Combined, the evidence exceeds 3.5σ.”
- Problem: This sentence conflates different data sets and analyses; see P2-E5.
- Required fix: Either remove or qualify as per P2-E5.

P2-m3 (Sec. 3.2 p. 2): Units
- Offending text: “βcombined = 0.242 ± 0.061° (3.9σ from zero)”
- Problem: Fine numerically; consider also quoting in radians for theoretical context and adding the weight calculation to ensure reproducibility.
- Required fix: Add one line showing the weight computation.

P2-m4 (Sec. 3.4 p. 3): Notation B vs. B10/B01
- Problem: It is unclear whether B is p(D|H1)/p(D|H0) or the inverse. This ambiguity likely contributed to the numerical inconsistencies.
- Required fix: Define B10 ≡ p(D|H1)/p(D|H0) at first use and maintain this convention.

P2-m5 (Sec. 6 p. 5): Novelty claim
- Offending text: “Our contribution is not the model itself, but rather the specific parameter identification (fa ∼ MPl, m ∼ H0) ... and the inference framework...”
- Problem: This is acceptable but would benefit from a more precise contrast with Fujita et al. (2021) and subsequent work, ideally with a table or brief quantitative comparison.
- Required fix: Add a short paragraph explicitly contrasting your priors/assumptions and what is new beyond earlier “Planck-scale ALP” analyses.

NITS

P2-n1 (Abstract and Sec. 6): Hyphenation/grammar
- Examples: “birefringence rotation angle” → “birefringence angle,” “order-unity inputs” → “order-unity inputs,” minor punctuation around em dashes.
- Fix: Proofread and standardize.

P2-n2 (Figures pp. 4–5): Axis labels/units
- Ensure β axis has “[deg]” consistently and any mass axis clearly notes “log10(m/eV).”

P2-n3 (References p. 6): “In preparation” citation
- Problem: “Namikawa et al., 2025. In preparation” provides no stable reference for comparisons.
- Fix: Either replace with an available preprint/journal reference or remove from quantitative comparisons.

P2-n4 (Sec. 5 p. 4): ECH gravity mention
- Problem: As acknowledged, speculative and not used. For a methods paper, this can be trimmed.
- Fix: Condense to one sentence or move to a brief outlook.

Page count
The main methodological content (summary-likelihood, MCMC, Bayes factor, forecast) could be presented in 4–5 pages. The current 6 pages are acceptable, but please remove speculative material (ECH gravity motivation) and replace with derivations/sanity checks (addressing P2-E1, P2-M3).

Audit of quoted numbers
- Planck NPIPE 0.30 ± 0.11° → 2.73σ: OK.
- ACT DR6 0.215 ± 0.074° → 2.91σ: OK.
- Combined β = 0.242 ± 0.061°: recomputed via inverse-variance weighting: OK. 3.94σ: OK.
- Eskilt joint 0.342 ± 0.094° → 3.64σ: OK.
- LiteBIRD forecast 0.27/0.03 = 9σ: arithmetic OK; scope/interpretation needs softening (P2-M4).
- Bayes factor: Not OK (see P2-E2).
- “C0 θi × 5×10−3 rad ≈ 0.27°”: conversion off by ~6% and inconsistent with Eq. (2) factor; see P2-m1.

## Summary recommendation
MAJOR REVISIONS

The paper contains a central theoretical inconsistency in the field-displacement prediction that directly affects the claimed “natural” value of β; an incorrectly computed Bayes factor with problematic prior handling; and an undefined “effective photon coupling” used as a key quantitative result. These are essential to fix. Additional major concerns include justification of independence in the data combination, clarification and justification of priors/parameter choices (especially C=8), and improved reporting of MCMC diagnostics. With these corrected and the claims recalibrated, the paper could be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes audit)

P2-E6 (Sec. 3.3; Table 1): Neff and sample-count inconsistency
- Offending text: “sample sizes (720–6,840 accepted samples)… small effective sample sizes (Neff ∼ 1,000)”
- Problem: Run 3 reports only 720 accepted samples yet the text asserts Neff ∼ 1,000 “per run” in aggregate terms. It is impossible for Neff to exceed the number of posterior draws for that run. This indicates either a misreported Neff, miscounted draws, or mixing data from different runs.
- Required fix: Report Neff per parameter and per run, and ensure Neff ≤ number of post-warmup draws. If Neff ∼ 1,000 is from Run 2 only, say so explicitly and give the Run-3 Neff.

P2-E7 (Abstract; Sec. 1; Refs): Misattributed dataset description for βobs
- Offending text: “βobs = 0.342 ± 0.094° from the Eskilt et al. joint Planck + ACT analysis.”
- Problem: The references list Eskilt & Komatsu (2022) (WMAP+Planck polarization), and Diego-Palazuelos & Komatsu (ACT DR6, 2025) separately. There is no cited paper that is a “joint Planck + ACT analysis by Eskilt et al.” The abstract’s attribution is inconsistent with the bibliography and with Sec. 3.1’s dataset description.
- Required fix: Correct the attribution for βobs and cite the precise paper that reports 0.342 ± 0.094°. If it is not a joint Planck+ACT analysis, change the wording in the abstract and body accordingly.

P2-E8 (Sec. 2.1): Onset-of-rolling criterion inconsistent with m ∼ H0 claim
- Offending text: “the field… begins rolling at z ∼ O(1) when H(z) ∼ m.”
- Problem: For the equation of motion 3Hϕ̇ + m^2ϕ ≈ 0, the usual criterion for the onset of rolling is m ≈ 3H, not m ≈ H. If m ≈ H0 today, then 3H0 > m, implying the field is still overdamped today and the onset would occur in the future (H/H0 ≈ m/3H0 ≈ 1/3), not at z ∼ 1 where H/H0 ≈ 1.7–2. This materially affects the predicted displacement ∆ϕ between recombination and today.
- Required fix: State and use a consistent onset criterion (e.g., m = 3H), show the redshift of onset for m ∼ H0, and recompute ∆ϕ accordingly.

P2-E9 (Secs. 2.2, 3.3): Photon coupling normalization missing α/(2π)
- Offending text: “gaγ = C0/fa is the ALP-photon coupling and C0 is an order-unity coefficient from the ABJ anomaly.”
- Problem: The standard normalization is gaγ = (α/2πfa)(E/N − 1.92), where (E/N − 1.92) is O(1) and α/2π ≈ 1.16×10−3. Writing gaγ = C0/fa with C0 ∼ O(1) implicitly drops the α/(2π) factor and inflates the coupling by ~10^3, which cascades into β predictions and the interpretation of “order-unity” anomaly coefficients. This also tangles the meaning of your “C” prior and of “C=8”.
- Required fix: Restore the α/(2π) factor explicitly, define C0 ≡ (E/N − 1.92), and propagate this normalization through all equations, priors, figures, and numeric claims. Reassess whether β ≈ 0.27° remains “natural” under correct normalization.

P2-M6 (Notation; throughout Secs. 2–3; Table 1; Fig. 1): Inconsistent use of C0, C, and Caγ
- Offending text: gaγ = C0/fa; Run 1 fixes “C = 8”; priors use “Caγ ∈ [1, 30]”; Sec. 3.3 reports “Caγ × θi = 3.4 ± 1.1.”
- Problem: Three near-identical symbols (C0, C, Caγ) are used for the same conceptual quantity without a clear definition, and at least one of them (gaγ) is dimensionful. It is unclear whether Caγ is the anomaly factor, a rescaled coupling, or absorbs α/(2π). This impedes reproducibility.
- Required fix: Consolidate to a single symbol for the dimensionless anomaly factor (e.g., C ≡ E/N − 1.92), keep gaγ dimensionful, and update all tables/figures/prior statements accordingly.

P2-M7 (Fig. 1 vs text; Fig. 2): Numerical mismatches and missing cross-reference
- Offending items:
  - Fig. 1 annotates β[deg] = 0.324 ± 0.099 for Run 2, but Sec. 3.3 never reports a β summary for Run 2; only the product Caγ × θi is quoted. 
  - Fig. 2 caption claims all three β posteriors are consistent with βobs = 0.342 ± 0.094°, but no quantitative comparison (e.g., differences in means/σ) is given in the text.
- Problem: The body text does not reproduce the Run-2 β number visible in Fig. 1, and the consistency claim in Fig. 2 is qualitative only.
- Required fix: Report the Run-2 β posterior mean and σ in Sec. 3.3 and provide a brief quantitative check (e.g., |µmodel − µobs|/σ) for each model shown in Fig. 2.

P2-M8 (Sec. 3.2; Eq. 4): Rounding and reproducibility details for the combined result
- Offending text: “βcombined = 0.242 ± 0.061°”
- Problem: Inverse-variance weighting of the stated inputs yields β = 0.2433° and σ = 0.0614°. The quoted mean (0.242°) appears rounded beyond what the inputs justify. No weights are shown, and the units of σ in Eq. 3 are implicit (deg).
- Required fix: Show the weights wi = 1/σi^2 explicitly, quote the combined mean to consistent precision (0.243 ± 0.061°), and note that the likelihood is in degrees (or convert all to radians).

P2-M9 (Sec. 2.1–2.2): “O(1)” cosmological factor left undefined yet used numerically
- Offending text: “∆ϕ/fa ≈ θi × O(1)” (Eq. 1), and later “∆ϕ/fa ∼ 10−2… yielding β ≈ C0 θi × 5×10−3 rad.”
- Problem: Beyond the inconsistency already flagged in your first review, the symbol “O(1)” is used as a placeholder for a number that is then numerically taken to be ~10−2 with no derivation. This is a separate documentation issue: the paper never defines, computes, or tabulates this factor for ΛCDM.
- Required fix: Replace “O(1)” with a named transfer integral (e.g., TΛCDM), define it precisely, and compute it numerically for the stated mass range, reporting TΛCDM with uncertainties.

P2-m6 (Sec. 3.3; Fig. 1): Mass posterior summary lacks central tendency type
- Offending text: Fig. 1 shows “log10(m/eV) = −31.4+1.5 −1.1” (from the figure annotation), but the text never states whether these are posterior means with 68% equal-tailed intervals or medians with HPD intervals.
- Required fix: Specify for all summary numbers whether they are means ± σ, medians with equal-tailed intervals, or HPD intervals.

P2-m7 (Sec. 6): “Matches the combined Planck + ACT measurement at 1σ” is vague
- Offending text: “The prediction matches the combined Planck + ACT measurement at 1σ.”
- Problem: “At 1σ” could mean within 1σ or exactly 1σ. The actual offset is |0.27 − 0.243|/0.061 ≈ 0.46σ. 
- Required fix: Rephrase to “within 0.5σ” (or say “within 1σ”) and provide the numerical offset.

P2-m8 (Sec. 3.1): Consistency of σ-values for quoted significances
- Offending text: 2.7σ (0.30 ± 0.11°), 2.9σ (0.215 ± 0.074°).
- Problem: These recompute to 2.73σ and 2.91σ, respectively. Elsewhere 3.9σ is quoted for 0.242 ± 0.061°, which recomputes to 3.97σ. The mixed rounding makes side-by-side comparison visually inconsistent.
- Required fix: Adopt a uniform rounding convention for significances (e.g., two decimals) and apply it consistently.

P2-m9 (Sec. 2.2): Notational ambiguity for units in Eq. (2)
- Offending text: “β = gaγ/2 ∆ϕ” with quantities implicitly in natural units, followed by numeric statements in degrees.
- Problem: The switch from natural units to degrees without stating the conversion (rad→deg) within the same subsection adds friction for reproducibility.
- Required fix: State explicitly when β is in radians vs. degrees and include the conversion in the first numerical estimate.

P2-N5 (References): “In preparation” and missing persistent identifiers
- Offending text: “Namikawa et al., 2025. In preparation” and “Companion paper, submitted simultaneously.”
- Problem: For quantitative comparisons these are not citable. If the β value or mass constraints hinge on these, the claims are not verifiable.
- Required fix: Replace with arXiv identifiers (if available) or remove quantitative comparisons pending a public preprint.

P2-N6 (Eq. numbering): Redundant J0(0) in Eq. (1)
- Offending text: “∆ϕ ≈ fa θi (1 − J0(m/H0)/J0(0))”
- Problem: J0(0) = 1; dividing by it is superfluous and makes the expression look like a special-function identity rather than a derived result.
- Required fix: Simplify to 1 − J0(m/H0) and add a footnote/derivation reference.

Rationale
These issues were not covered in the initial review and emerged from a second-pass audit focused on arithmetic consistency, figure-body alignment, equation normalization, dataset attribution, and notation. Several of them (P2-E6–E9) materially affect the paper’s core quantitative claims and reproducibility.