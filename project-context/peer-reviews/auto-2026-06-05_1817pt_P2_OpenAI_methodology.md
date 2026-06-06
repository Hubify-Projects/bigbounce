# P2 auto-2026-06-05_1817pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (5431 chars)
**Wall time**: 437.1s

---

Referee report on “Cosmic Birefringence from a Planck-Scale Axion-Like Particle: Predictions, Constraints, and LiteBIRD Forecasts”

Scope of review
I audited the methodology, statistical procedures, derivations, dimensional consistency, internal arithmetic, and the traceability of every scalar appearing in the abstract and conclusions to explicit content in the body. I also checked figure/tables for internal consistency and axes/units, and I recomputed all reported significances and ratios that could be recomputed from the quoted inputs.

Overall assessment
The paper tackles a timely topic and uses a summary-likelihood combination of publicly reported birefringence measurements alongside a simplified ALP model and small MCMC explorations. However, there are several methodology-critical inconsistencies and undefined quantities. In particular, the field-displacement expression in Eq. (1) is incompatible by over an order of magnitude with the later scaling used to derive the β ≈ 0.27° “natural” prediction; the Bayes factor reported in Sec. 3.4/abstract is numerically inconsistent with the summary-likelihood numbers given in Sec. 3.2 and appears to have been computed with a different dataset without disclosure; the “effective photon coupling” fphoton × C0 is not defined anywhere in the text and cannot be reconstructed from the presented model; and Figure 1’s quoted marginal summaries are inconsistent with the stated posterior for the product Caγ × θi. The MCMC sample sizes and convergence claims are also not methodologically adequate for the inferential claims made.

Below I list all issues found, classified per journal standards.

Findings

ESSENTIAL

P2-E1 (Sec. 2.1, p. 1–2): Inconsistent and unsubstantiated field displacement
- Text/equation: “Δϕ ≈ fa θi (1 − J0(m/H0)/J0(0)) ≈ fa θi × O(1) (1)” and “For m/H0 ∼ 1, 1 − J0(1) ≈ 0.24 …” followed in Sec. 2.2 by “the cosmological field evolution gives Δϕ/fa ∼ 10−2 … yielding β ≈ C0 θi × 5×10−3 rad ≈ 0.27°.”
- Problem: Eq. (1) implies Δϕ/fa ≈ 0.24 θi (O(10−1)), which plugged into β = (C0/2)(Δϕ/fa) gives β ≈ 0.12 C0 θi rad ≈ 7° for C0 θi ∼ 1—grossly inconsistent with the 0.27° “natural” prediction. Conversely, Δϕ/fa ∼ 10−2 used in Sec. 2.2 contradicts Eq. (1). No derivation is provided for Eq. (1) or for Δϕ/fa ∼ 10−2.
- Required fix: Provide a correct, fully derived expression for Δϕ/fa between recombination and today, starting from the background EOM in an expanding universe and explicitly integrating over the cosmological history actually assumed. Remove the Bessel-Ansatz unless derived, and reconcile the amplitude used to predict β = 0.27°. All numbers in Sec. 2.2 must follow from the derived expression with explicit parameter choices. If an O(10−2) factor is intended, show the integral or numerical evolution producing it.

P2-E2 (Sec. 3.4, p. 3; Abstract p. 1): Bayes factor dataset inconsistency and transparency
- Text: “ln B = 5.17 … computed via the Savage-Dickey density ratio with a flat prior β ∈ [0°,1°].” Abstract repeats ln B = 5.17.
- Problem: Using the explicit summary-likelihood combination provided in Eq. (4), β = 0.242 ± 0.061°, the Savage–Dickey Bayes factor for a uniform prior on [0°,1°] gives ln B ≈ 5.99, not 5.17. The numbers ln B = 5.17/4.48/5.86 match a Gaussian with μ = 0.342°, σ = 0.094° (Eskilt et al. joint analysis), not the combined constraint in Eq. (4). The dataset used for the Bayes factor is therefore not the one introduced in Sec. 3.2, and this is not stated.
- Required fix: State explicitly which dataset/likelihood is used for each Bayes factor. If Sec. 3.4 uses the Eskilt joint-analysis numbers, say so and justify. Also provide ln B computed from the combined summary-likelihood in Eq. (4), and discuss the difference. All numbers in the abstract must match the dataset choice made in the body.

P2-E3 (Sec. 3.2, Eq. 5, p. 2; Abstract p. 1): Undefined “effective photon coupling” and non-derivability
- Text: “The effective photon coupling parameter: fphoton × C0 = 1.73 ± 0.44 (5).”
- Problem: fphoton is never defined in the paper; dimensionality is unclear; the mapping from βcombined to this parameter is not given. The value 1.73 cannot be reproduced from the stated relations β = (C0/2fa) Δϕ with any clear definition of fphoton. The number 1.73 also suspiciously equals 0.242/0.14, which suggests it may be a ratio of unrelated scalars (βcombined divided by an older Planck error bar) rather than a physical coupling.
- Required fix: Precisely define fphoton and show, step by step, how Eq. (5) is computed from Eqs. (1)–(2) and the data in Eq. (4), including units. If fphoton × C0 is intended to be Caγ × θi or any other meaningful function of model parameters, use consistent notation and provide the algebra. Remove Eq. (5) if it does not have a clear physical definition and derivation.

P2-E4 (Fig. 1 caption and panels vs. Sec. 3.3 text, p. 4 and p. 3): Posterior inconsistency for Caγ × θi
- Text: Sec. 3.3 states “Caγ × θi = 3.4 ± 1.1.” Fig. 1 panels show central values roughly θi ≈ 1.33 and Caγ ≈ 13.4, which multiply to ≈ 17.8, not 3.4.
- Problem: The figure annotations and the stated product are inconsistent by a factor ∼5. This undermines the MCMC result’s credibility and suggests either mislabeling, a hidden rescaling, or a plotting/annotation error.
- Required fix: Audit the Run 2 posteriors and regenerate Fig. 1 with consistent parameter definitions. Provide a table with posterior medians and 68% credible intervals for θi, Caγ, log10(m/eV), β, and their product, and verify internal consistency numerically.

P2-E5 (Table 1 and Sec. 3.3, p. 3): Inadequate MCMC sampling and inconsistent Neff claims
- Text: Table lists 720–6,840 “Samples” with R̂ − 1 < 0.01; text says “effective sample sizes (Neff ∼ 1,000).”
- Problem: With total accepted samples as low as 720 (Run 3), Neff cannot exceed the total draws; R̂ is not a reliable convergence diagnostic at these lengths. There is no information on the number of chains, warm-up length, thinning, or acceptance rates. Claims relying on tail behavior (e.g., Bayes factors via Savage–Dickey or product posteriors) are not supported by these tiny samples.
- Required fix: Report full MCMC configuration (sampler, number of chains, warm-up, total draws per chain, acceptance rates, thinning), and provide per-parameter Neff and R̂. Increase sampling to standard practice (e.g., O(10^5) post-warmup draws and Neff ≳ O(10^4) per parameter) or adopt analytic propagation for the 1D Gaussian summary likelihood where appropriate. Recompute posteriors and all derived quantities after adequate sampling.

P2-E6 (Methodological clarity across Secs. 3.2–3.4, pp. 2–3): Primary estimator and comparability
- Text: Paper alternates between using (i) a two-point summary-likelihood combination (Eq. 4) and (ii) the Eskilt et al. joint-analysis EB likelihood summarized as βobs = 0.342 ± 0.094° for MCMC and Bayes factors, without declaring a single primary estimator and without warning that the significances are not directly comparable.
- Problem: Different likelihood inputs and null-procedures are interleaved without consistent labeling. This violates good practice for reporting significance and evidence.
- Required fix: Declare a primary likelihood/estimator for the analysis and use it consistently in all headline numbers (posteriors, Bayes factors). When quoting alternative numbers from a different estimator, explicitly state “not directly comparable” at each juxtaposition and isolate them in a separate subsection.

MAJOR

P2-M1 (Notation coherence; throughout): Confusing and inconsistent symbols
- Issue: The text uses C0, C, Caγ, gaγ, and “fphoton × C0” seemingly interchangeably. Table 1 references “C = 8 fixed” while Sec. 2.2 defines gaγ = C0/fa. Sec. 3.3 reports “Caγ × θi = 3.4 ± 1.1.”
- Required fix: Adopt a single, consistent notation: e.g., gaγ = Cγ/fa with Cγ dimensionless anomaly coefficient; define all symbols in one place; ensure figures/tables use the same symbols; remove “fphoton” unless it is explicitly defined and used consistently.

P2-M2 (Choice and justification of C = 8 fixed; Table 1 p. 3, Sec. 3.3 p. 3): Parameter choice not motivated
- Issue: Run 1 fixes C = 8 with no microphysical or phenomenological justification, while elsewhere the text emphasizes O(1) coefficients near unity.
- Required fix: Justify C = 8 from a specific UV completion or known anomaly coefficient normalization. If it is merely a nuisance scaling, remove the run or recast results in terms of the product C × θi, avoiding arbitrary fixed values.

P2-M3 (Assumption of independent errors; Sec. 3.2 p. 2): Independence of Planck and ACT constraints not justified
- Issue: The summary-likelihood combination assumes independent errors. Calibration and sky/systematics correlations can couple Planck and ACT EB-based β estimates.
- Required fix: Provide a justification for independence (e.g., different optics and independent self-calibration pipelines) or, minimally, perform a sensitivity analysis to a modest correlation coefficient (e.g., ρ = 0.2–0.5) and show how βcombined and σ change.

P2-M4 (Savage–Dickey at a boundary; Sec. 3.4 p. 3): Technical caveat missing
- Issue: With a prior restricted to β ≥ 0, the nested point β = 0 lies at a boundary, where Savage–Dickey has subtle conditions.
- Required fix: State explicitly how truncation is handled. Either use an untruncated Gaussian likelihood for the Bayes factor computation (and explain why this is acceptable) or give the corrected expression for a half-Gaussian posterior. For μ/σ ≈ 3–4 the effect is small, but the method must be stated.

P2-M5 (Forecast claim strength; Sec. 4 p. 3; Conclusions p. 6): Over-stated decisiveness
- Issue: “LiteBIRD … will test this prediction at 9σ significance—either confirming the signal or ruling out the ALP explanation decisively.” This ignores calibration systematics floors and that a null β would constrain only this minimal parameter point, not the entire ALP class.
- Required fix: Soften to: “Under σ(β) ≈ 0.03° statistical precision and controlled systematics, the benchmark β ≈ 0.27° would correspond to ≈9σ; a null result would strongly disfavor this minimal parameter choice.” Cite forecast systematic budgets.

P2-M6 (Model-to-observable mapping; Sec. 2, pp. 1–2; Sec. 3.3 p. 3): Missing explicit mapping from (m, fa, θi, Cγ) to β
- Issue: Beyond Eq. (2), there is no explicit formula or numeric mapping used in the MCMC to propagate parameter priors to β. Given the confusion around Δϕ/fa, this is critical.
- Required fix: Provide the explicit computational pipeline used to compute β(m, fa, θi, Cγ), including the cosmological background assumed, numerical integrator, and any approximations. Include a validation plot of β vs m/H0 for a few θi values.

P2-M7 (Sign of β and priors; Sec. 3.3 p. 3): Truncation to β ≥ 0 not justified
- Issue: Birefringence estimators yield signed β; the paper effectively imposes θi ≥ 0 and β ≥ 0.
- Required fix: Justify the restriction or allow θi ∈ [−π, π] with a symmetric prior, and propagate to signed β. Clarify consequences for Bayes factors and posteriors.

P2-M8 (Use of “order-unity” while adopting broad priors; Sec. 3.3 p. 3; Fig. 1 p. 4): Scope of “order unity”
- Issue: Prior Caγ ∈ [1, 30] and posterior near ~13 are not “O(1)” in the narrow sense used elsewhere in the text to motivate naturalness.
- Required fix: Calibrate language or narrow priors to match the “order-one” claim, or argue from the underlying model why values up to 30 are natural.

MINOR

P2-m1 (Arithmetic verification; Sec. 3.2 p. 2): Combined constraint
- Check: Combining 0.30 ± 0.11 and 0.215 ± 0.074 as independent Gaussians gives β = 0.2416 ± 0.0614°, i.e., 0.242 ± 0.061° (3.97σ). Your Eq. (4) is consistent. Please add the explicit weighted-average formula and the assumption that quoted uncertainties are 1σ Gaussian.

P2-m2 (Units clarity; Sec. 2.2 p. 2): Radians vs degrees
- Issue: The line “β ≈ C0 θi × 5×10−3 rad ≈ 0.27°” is correct numerically but readers may miss the unit conversion.
- Fix: Insert “(1 rad = 57.2958°)” or show 0.005 rad × (180/π) = 0.286°.

P2-m3 (Redundant denominator; Sec. 2.1 p. 2): J0(0)
- Issue: Dividing by J0(0) = 1 in Eq. (1) is unnecessary and potentially misleading.
- Fix: Remove J0(0) from the denominator or explain why it is written that way.

P2-m4 (Figure 2 caption vs text; p. 5): Dataset clarity
- Issue: Fig. 2 shows posteriors centered near 0.33°, which correspond to the Eskilt joint-analysis likelihood, not the summary-likelihood in Eq. (4).
- Fix: State explicitly in the caption which likelihood is used to produce each curve.

P2-m5 (Bibliography completeness; p. 6): “In preparation” citation
- Issue: “Namikawa et al., 2025. In preparation” is not citable for results comparison in PRD style.
- Fix: Replace with an arXiv identifier/preprint or remove claims that rely on it.

NITS

P2-n1 (Language): Several instances of “order-unity, no fine-tuning” repeat close together. Consider tightening phrasing.

P2-n2 (Acknowledgments): “AI research assistants” acknowledgement is acceptable but consider specifying which tools or versions for reproducibility compliance.

P2-n3 (Typos/formatting): Ensure all parameter symbols are consistently italicized and that tildes in F F̃ are typeset clearly.

Length and scope
For the actual methodological content delivered (summary-likelihood combination and a simple parameter-level MCMC), six pages is acceptable, but once the essential fixes (especially the derivation and consistent notation) are implemented, I recommend keeping the manuscript concise, around 6–8 pages including figures.

Summary recommendation
MAJOR REVISIONS

Justification: The manuscript contains multiple methodology-critical inconsistencies: the central predictive scaling for Δϕ/fa contradicts itself by over an order of magnitude; the Bayes factor reported in the abstract/body is computed from a different dataset than the combined constraint presented and is not properly documented; a key “effective coupling” parameter is undefined; and the MCMC posterior summaries are internally inconsistent with figure annotations and are based on sample sizes that are not adequate for the stated inferences. These issues must be corrected and clarified before the work can meet PRD standards. The core idea may remain publishable after substantial revision, but the current version is not acceptable.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (second-pass audit)

P2-E7 (Sec. 2.2, notation/normalization): Axion–photon coupling missing α/(2π) normalization
- Text: “gaγ = C0/fa is the ALP-photon coupling and C0 is an order-unity coefficient from the ABJ anomaly.”
- Problem: In the standard normalization, gaγ = α Cγ/(2π fa). Dropping α/(2π) ≈ 1.16×10−3 and folding it into “C0” without stating so changes amplitudes by ~10^3. With the standard normalization and the paper’s stated Δϕ/fa ∼ 10−2, the predicted rotation is β ≈ (α Cγ/4π)(Δϕ/fa) ≈ 5.8×10−6 Cγ rad ≈ 0.00033 Cγ deg, which is ≳800× smaller than 0.27° for Cγ = O(1). The paper’s “C0 ∼ O(1)” therefore contradicts the stated “natural” β ≈ 0.27° unless C0 implicitly includes α/(2π)−1. This affects the interpretation of C = 8 in Table 1 and the prior Caγ ∈ [1, 30].
- Required fix: State the exact normalization used for gaγ, including whether α/(2π) is absorbed into C0. If you adopt the standard gaγ = α Cγ/(2π fa), recompute all β predictions and posteriors; if not, define C0 ≡ (2π/α)Cγ explicitly and reconcile with literature values.

P2-E8 (Sec. 2.2 and Abstract): β prediction is independent of fa in the presented setup
- Text: “A spectator ALP with Planck-scale decay constant … naturally accommodates β ≈ 0.27° …” and “gaγ = C0/fa,” “Δϕ ≈ fa θi × O(1).”
- Problem: With Δϕ ∝ fa and β = (C0/2fa)Δϕ, fa cancels; the prediction for β depends on C0, θi, and the cosmological O(1) factor, not on fa. Thus fa ∼ MPl is not required to obtain β ≈ 0.27° in this model as written. Emphasizing fa ∼ MPl as central to the birefringence prediction is therefore misleading.
- Required fix: Clarify that β is independent of fa under the stated assumptions, and shift the “naturalness” argument accordingly (e.g., to energy density, isocurvature, or UV motivation) or modify the modeling so fa enters β nontrivially.

P2-E9 (Fig. 1 vs Sec. 3.3): Mismatch in β posterior summaries for the same run
- Text: Sec. 3.3 reports for Run 2 (C free) “βALP = 0.336 ± 0.107°” (Run 1) and “βfree = 0.344 ± 0.096°” (Run 3). Fig. 1’s 1D marginal for β displays “β [deg] = 0.324 ± 0.099.”
- Problem: The figure’s β summary (0.324 ± 0.099) does not match any of the textual posteriors reported for the corresponding MCMC configurations. This is a separate inconsistency from the already noted Caγ × θi product issue.
- Required fix: Recompute and synchronize the figure annotations with the text. Provide a table listing medians and 68% credible intervals for each run and confirm that the plotted corner summaries reproduce those numbers.

P2-M9 (Sec. 3.3, priors): Physically unjustified prior measure for θi
- Text: “Priors: θi flat on [0.01, π].”
- Problem: For a shift-symmetric angular field, the natural prior is uniform on θi ∈ [−π, π] (or symmetric about zero). Truncating to positive angles both forbids negative β in the model mapping and doubles the prior mass near large |θi|, biasing evidence/Bayes factors and posteriors. This is distinct from the previously noted signed-β point: the prior measure itself is not physically motivated.
- Required fix: Use a symmetric prior θi ∈ [−π, π] (or justify an asymmetric choice from microphysics), and recompute posteriors and Bayes factors. Explicitly state how this impacts β’s sign and evidence.

P2-m6 (Sec. 2.1): Onset-of-rolling criterion missing the standard factor of 3
- Text: “begins rolling at z ∼ O(1) when H(z) ∼ m.”
- Problem: The usual criterion for linearized oscillations is 3H ≈ m. Using H ≈ m shifts the inferred onset redshift by an O(1) factor and affects Δϕ estimates across the integrand window.
- Fix: Replace with 3H(zroll) ≈ m (or justify the deviation) and propagate any resulting change to Δϕ/fa and β.

P2-m7 (Sec. 6, “Consistency with data”): Unquantified hedge; provide explicit deviation
- Text: “The prediction matches the combined Planck + ACT measurement at 1σ.”
- Problem: The benchmark 0.27° differs from the Eq. (4) combined mean by 0.028° = 0.46σ and from the Eskilt joint-analysis mean by 0.072° = 0.77σ. The current text does not quantify this.
- Fix: Add the explicit Δ/σ values relative to both likelihood choices and state which comparison you consider primary.

P2-m8 (Fig. 2 caption vs x-axis units used in statistics): Units consistency across likelihoods
- Text: Bayes-factor computations in Sec. 3.4 use degrees (explicitly w in degrees). Eq. (2) and much of Sec. 2 use radians.
- Problem: While internally consistent within each subsection, the manuscript never states the working units when moving between model-space (radians) and likelihood-space (degrees). This can easily lead to silent factor mistakes in evidence calculations.
- Fix: Add a one-line note in Sec. 3 that all likelihood-level computations use degrees, and show one explicit conversion example when mapping model predictions (in radians) to data space.

P2-m9 (Sec. 2.2): Double use of undefined O(1) factors
- Text: “β ≈ C0 θi/2 × O(1)” after Eq. (2), while Eq. (1) already introduced an O(1) in Δϕ/fa.
- Problem: The two O(1) placeholders obscure where the numerical factor comes from and risk double-counting. This is separate from the amplitude inconsistency already flagged.
- Fix: Collapse O(1) placeholders into a single, explicitly defined cosmological transfer factor F(m/H0, background), quote its value, and use it consistently.

These items are in addition to, and do not duplicate, the issues identified in my initial review.