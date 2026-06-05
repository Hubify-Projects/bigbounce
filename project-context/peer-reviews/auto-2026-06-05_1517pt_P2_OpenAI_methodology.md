# P2 auto-2026-06-05_1517pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6454 chars)
**Wall time**: 486.5s

---

Referee report on “Cosmic Birefringence from a Planck-Scale Axion-Like Particle: Predictions, Constraints, and LiteBIRD Forecasts”

Overall assessment
The topic is timely and potentially important. However, the current manuscript contains multiple methodological and statistical inconsistencies that prevent verification of the central quantitative claims. Core derivations for the predicted rotation and the coupling normalization are incomplete or internally inconsistent; the Bayes factor calculation is mislabeled and prior handling is problematic; the MCMC analyses are far too small to support the stated precision; and several key quantities are undefined or ambiguously defined. The paper, as written, does not meet Physical Review D standards for methodological rigor.

Below I enumerate detailed issues. For each, I provide an identifier, location, the problem, and the required fix.

ESSENTIAL

P2-E1
- Location: Sec. 2.1–2.2, pp. 1–2, Eq. (1) and subsequent text
- Problem: Internal inconsistency in the field displacement used to predict β. Eq. (1) gives Δφ/fa ≈ θi[1 − J0(m/H0)/J0(0)] ≈ 0.24 θi for m/H0 ≈ 1 (since J0(1) ≈ 0.765). But Sec. 2.2 then asserts “Δφ/fa ∼ 10−2” and uses this to obtain β ≈ C0 θi × 5×10−3 rad ≈ 0.27°. These two statements are incompatible by over an order of magnitude (0.24 vs 0.01). No derivation is provided for the J0 expression, and it appears ad hoc for ΛCDM evolution between recombination and today.
- Required fix: Provide a self-consistent derivation or validated numerical integration of the axion equation of motion in a ΛCDM background that yields Δφ between z ≈ 1100 and today for m ~ H0. Explicitly compute Δφ/fa(θi, m/H0) and propagate to β = (gaγ/2)Δφ. Remove the Bessel J0 formula unless rigorously derived; if derived, show the steps and domain of validity. All numerical predictions (e.g., β ≈ 0.27°) must follow from this derivation.

P2-E2
- Location: Sec. 2.2, Eq. (2), and throughout; Abstract; Sec. 3.2–3.3; Fig. 1; Table 1
- Problem: Coupling normalization is not standard and is internally inconsistent. The manuscript takes gaγ = C0/fa with C0 “order unity,” and uses C = 8 in MCMC. In QED-normalized axion models one typically has gaγ = (α/2πfa)(E/N − 1.92), i.e., the α/π factor is not optional. If C0 is meant to absorb α/2π and model-dependent coefficients, this must be stated unambiguously. As written, results and statements about “naturalness” of fa ∼ MPl are not interpretable.
- Required fix: Define precisely the coupling convention used (state whether C0 includes α/2π and anomaly factors). Give units for gaγ, and connect all symbols consistently: C0, Caγ, C, and gaγ must be mapped to one another. Justify the choice C = 8, and perform a sensitivity analysis over a physically motivated range. If you intend a fully effective coupling gaγ with no reference to α, then drop “ABJ anomaly” language and treat C0 as a dimensionless phenomenological constant.

P2-E3
- Location: Sec. 3.2, p. 2, Eq. (5); Abstract
- Problem: “The effective photon coupling parameter: fphoton × C0 = 1.73 ± 0.44.” The quantity fphoton is undefined anywhere in the paper, and the route from the combined β constraint to this number is not shown.
- Required fix: Define fphoton explicitly and show the algebra that maps the combined β measurement to the stated value. Provide its units (or demonstrate it is dimensionless). If this is a reparameterization of gaγ θi or C0 θi, state so clearly and ensure consistency with Sec. 3.3 where Caγ × θi = 3.4 ± 1.1 is quoted.

P2-E4
- Location: Sec. 3.4, p. 3
- Problem: Bayes factor inconsistencies. You report ln B = 5.17 for a prior β ∈ [0°,1°], ln B = 4.48 for [0°,2°], and ln B = 5.86 for [0°,0.5°]. For a Gaussian likelihood with μ = 0.242°, σ = 0.061°, the Savage–Dickey ratio with a symmetric prior β ∈ [−L, L] gives ln B10 ≈ 5.17 for L = 1°, ≈ 4.48 for L = 2°, and ≈ 5.87 for L = 0.5°. Your numbers match the symmetric-prior results but are labeled as one-sided priors. Additionally, using a one-sided prior for a signed quantity is unjustified and artificially boosts evidence relative to a symmetric prior by ln 2.
- Required fix: Recompute and report Bayes factors with properly specified priors and units (degrees vs radians), and state explicitly whether the prior is symmetric. Use a symmetric prior unless you justify a physical reason for β ≥ 0. Provide the formula used and the posterior density at β = 0 to allow reproduction.

P2-E5
- Location: Sec. 3.2, p. 2
- Problem: Independence assumption for Planck and ACT birefringence errors is not justified. Both analyses rely on variants of the Minami–Komatsu self-calibration and may share similar systematic error budgets (e.g., dust modeling assumptions). Treating them as independent likely overstates the combined significance (3.94σ).
- Required fix: Provide a quantitative assessment of possible correlations or a conservative combination that brackets plausible correlation coefficients (e.g., ρ = 0–0.5), and report how βcombined and σ(β) change. Alternatively, restrict to a single measurement for inference and reduce claims accordingly.

P2-E6
- Location: Sec. 3.3 and Table 1, p. 3; Fig. 1
- Problem: MCMC sample sizes (720–6,840 accepted samples) are orders of magnitude too small for robust parameter estimation or evidence statements. R̂ − 1 < 0.01 is not meaningful with such short chains; the stated “Neff ∼ 1,000” contradicts Run 3 having only 720 samples. You present tail-sensitive quantities (Bayes factors, posteriors under broad priors) without adequate sampling.
- Required fix: Re-run MCMC with multiple chains and effective sample sizes ≥ 5×10^4 for all reported posteriors. Report chain counts, burn-in, acceptance rates, autocorrelation lengths, and effective sample sizes. Remove any quantitative conclusions (including Eq. (8)) that rely on current runs, or clearly mark them as exploratory and not used for the main claims.

P2-E7
- Location: Abstract; Sec. 3.1–3.3; Fig. 2
- Problem: Dataset inconsistency and mixed use of different estimates. The paper quotes and uses both (i) βobs = 0.342 ± 0.094° (Eskilt et al. joint analysis) and (ii) a combined “summary-likelihood” value β = 0.242 ± 0.061° derived from two separate point estimates. These are not based on identical pipelines and are not directly comparable; yet they are used side-by-side to support conclusions.
- Required fix: Choose a single primary estimator/likelihood (pre-declare it) for the main inference, and move the other to a cross-check section with explicit “not directly comparable” caveats wherever numbers are juxtaposed. If you keep the summary-likelihood, justify its construction (including possible correlations; see P2-E5).

P2-E8
- Location: Sec. 2.2, p. 2; Conclusions, p. 6
- Problem: Overclaim on falsifiability. “If LiteBIRD measures β = 0 ± 0.03°, the ALP explanation is excluded at 9σ.” The model has free parameters (θi, C0, and even m) that can make β arbitrarily small. A null β would exclude only the particular parameter region that predicts β ≈ 0.27°, not the model class.
- Required fix: Rephrase to “would exclude the specific parameter region (e.g., C0 θi × transfer factor) that yields β ≈ 0.27° at ≈ 9σ,” and quantify the predicted distribution (with priors) to state what fraction of parameter space would be disfavored.

P2-E9
- Location: Sec. 3.3, p. 3; Fig. 1
- Problem: Prior on Caγ is ad hoc and biased: flat on [1, 30] excludes Caγ < 1 and enforces large couplings; this directly affects the posterior on Caγ × θi. No physical motivation is given.
- Required fix: Justify this prior physically or adopt a less informative prior (e.g., log-flat over a wide range that includes < 1). Provide prior-sensitivity tests showing how Eq. (8) and Fig. 1 change.

P2-E10
- Location: Sec. 2.1, Eq. (1), p. 2
- Problem: Dimensional/notation ambiguity: θi is used without units; later Fig. 1 seems to plot θi over ~0–3.2, suggesting radians. Eq. (2) and surrounding text mix radians and degrees without always specifying units.
- Required fix: State explicitly that θi is in radians and use consistent units for all angles. When converting to degrees (e.g., β ≈ 0.27°), show the conversion from radians.

MAJOR

P2-M1
- Location: Sec. 3.1–3.2, pp. 2–3
- Problem: The summary-likelihood combination assumes Gaussianity for each estimate and neglects any non-Gaussian systematics reported in the original analyses. No check of robustness to modest non-Gaussianity is provided.
- Required fix: Perform a robustness test (e.g., t-distribution likelihoods with ν = 5–10, or inflate σ by the reported systematic budgets) and report the impact on βcombined and ln B.

P2-M2
- Location: Fig. 1 caption and axes, p. 4
- Problem: Axes lack units for θi (rad?) and Caγ (dimensionless?). The caption does not specify priors used in this run (“C free”) nor the likelihood input (which β likelihood was used).
- Required fix: Add units to each axis; state priors, likelihood choice (0.242 ± 0.061° vs 0.342 ± 0.094°), and whether angles are in degrees or radians.

P2-M3
- Location: Table 1, p. 3
- Problem: “Samples” is ambiguous (total post–burn-in draws? per chain? accepted after thinning?). R̂ alone is insufficient; the table should report the number of chains, total draws per chain, burn-in, and effective samples for each parameter.
- Required fix: Expand Table 1 to include these details and report effective sample sizes per key parameter.

P2-M4
- Location: Sec. 2.2, p. 2
- Problem: The statement “the cosmological field evolution gives Δφ/fa ∼ 10−2 (from the ratio of field displacement to decay constant over the Hubble time)” is qualitative and unsupported; it appears to insert the desired small number without derivation.
- Required fix: Replace with a calculation tied to Eq. (1)’s corrected expression (see P2-E1) or a numerical integration in ΛCDM showing Δφ/fa over z ∈ [1100, 0] for m ∼ H0. Quote a number with uncertainty and show its dependence on m/H0 and θi.

P2-M5
- Location: Sec. 6, p. 5
- Problem: “The prediction matches the combined Planck + ACT measurement at 1σ.” This depends on the ad hoc Δφ/fa ∼ 10−2 (see P2-E1, P2-M4). Without a defensible transfer factor, this comparison is not established.
- Required fix: After fixing P2-E1/M4, recompute the predicted β and state the quantitative comparison to the chosen dataset with uncertainties.

P2-M6
- Location: Citations, p. 6
- Problem: Reference to “Namikawa, Murai & Naokawa, 2025. In preparation” and “Diego-Palazuelos and Komatsu, 2025. arXiv preprint” are used as quantitative inputs/comparisons. Reliance on unpublished/in-preparation sources for key numbers is discouraged.
- Required fix: Verify all quoted statistics against published sources where possible, or explicitly caveat the provisional status. If arXiv is the only source, include arXiv identifiers and verify that the quoted numbers match the preprint.

MINOR

P2-m1
- Location: Sec. 1, p. 1
- Problem: “Combined, the evidence exceeds 3.5σ.” This is vague and mixes analyses with different pipelines. 
- Required fix: Specify which combination and how σ is computed, or rephrase to avoid implying a single joint pipeline.

P2-m2
- Location: Eq. (1), p. 2
- Problem: Dividing by J0(0) is trivial since J0(0) = 1 and may confuse readers.
- Required fix: Remove J0(0) from the denominator unless there is a nontrivial normalization to justify it.

P2-m3
- Location: Sec. 5, p. 4
- Problem: The speculative connection to the Holst action/Barbero–Immirzi parameter is qualitative and not used in the analysis.
- Required fix: Either provide a concrete mapping to the coupling normalization used in Sec. 2.2, or delimit this as speculation and ensure it does not affect the main claims.

P2-m4
- Location: Fig. 2, p. 5
- Problem: The vertical band labeled “Observed βobs = 0.342 ± 0.094°” is plotted alongside posteriors derived from a different effective likelihood (0.242 ± 0.061°) without caveat.
- Required fix: Add a note in the caption that these are not directly comparable because they come from different procedures; or show two bands corresponding to both likelihood choices.

P2-m5
- Location: Throughout
- Problem: Inconsistent use of symbols C, C0, and Caγ; and of φ vs ϕ.
- Required fix: Consolidate notation; define all symbols once and use them consistently.

NITS

P2-n1
- Location: Abstract and Sec. 4, pp. 1, 3
- Problem: “9σ significance” computed as 0.27/0.03 = 9; fine, but report it as approximate (9.0) and note dependence on the final LiteBIRD systematic floor.
- Required fix: Add a qualifier “assuming systematics are below the statistical floor and σ(β) = 0.03°.”

P2-n2
- Location: Acknowledgments, p. 6
- Problem: “The author acknowledges the use of AI research assistants...” Journal policies vary on such statements.
- Required fix: Ensure compliance with PRD’s authorship and tools policies; if required, move to a Data/Code Availability or Author Contributions statement per journal guidelines.

P2-n3
- Location: Typos/formatting
- Problem: Occasional hyphenation artifacts (e.g., “birefringence rota­tion angle”) and spacing in equations.
- Required fix: Clean up typesetting artifacts.

Checks of numbers quoted in the paper
- Weighted mean of (0.30 ± 0.11) and (0.215 ± 0.074) gives 0.2416 ± 0.0614°, i.e., 3.94σ from zero. Your Eq. (4) matches this.
- 3.6σ significance for 0.342 ± 0.094° is consistent (0.342/0.094 = 3.64).
- 5×10−3 rad = 0.2865°, close to 0.27°, but this rests on the unsupported Δφ/fa ∼ 10−2 and additional θi factor; see P2-E1/E3.
- Bayes factors: For μ = 0.242°, σ = 0.061°, the SDDR with symmetric prior β ∈ [−L, L] yields ln B10 ≈ 5.17 (L = 1°), 4.48 (L = 2°), 5.87 (L = 0.5°). Your labels suggest one-sided priors; see P2-E4.

Scope and length
Given the current scope (a simple summary-likelihood combination and a highly schematic ALP prediction), the manuscript is relatively dense but still includes speculative material (Sec. 5) that is not essential to the core method. After addressing the essential issues, consider focusing the paper to ≤ 6 pages by trimming speculative connections and moving extended discussion of bounce cosmology to an appendix or separate work.

Summary recommendation
MAJOR REVISIONS

The central quantitative prediction for β is internally inconsistent and not derivable from the equations as written; the coupling normalization is ambiguous; the Bayes factor numbers are mislabeled with respect to the stated priors; the MCMC setup is inadequate to support the quoted posteriors; and a few key parameters are undefined. These issues are fixable but require substantial revision: a correct and transparent derivation (or validated numerical integration) for Δφ/fa; a consistent and standard coupling normalization; rigorous and reproducible Bayes factor computation with justified priors; and adequately sampled MCMC with clear priors and likelihoods. Addressing the independence assumption for the combined datasets is also necessary. Only after these corrections can the claims meet PRD methodological standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes pass)

ESSENTIAL

P2-E11
- Location: Sec. 3.3, Eq. (8) and Fig. 1 (triangle plot)
- Problem: Arithmetic inconsistency between the text’s quoted product and the figure’s marginals. The caption states “Caγ × θi = 3.4 ± 1.1,” but the 1D marginals printed on the diagonals show approximately Caγ = 13.4+5.6
−3.1 and θi = 1.33+1.12
−1.11. The central-value product is ≈ 17.8, over 5× larger than 3.4. Either (i) the Caγ axis is mis-scaled/mis-labeled, (ii) a different run produced Eq. (8), or (iii) the plotted numbers are in different units/parameterizations than stated.
- Required fix: Reconcile Fig. 1 with Eq. (8). State explicitly which run, parameterization, units, and likelihood were used for Fig. 1; if Caγ was transformed (e.g., rescaled by α/2π or by fa), write it on the axis and in the caption. If Eq. (8) is from a different run, label it as such and present the corresponding triangle plot for that run.

P2-E12
- Location: Fig. 1 (β [deg] panel) vs Sec. 3.3 text
- Problem: Figure shows a 1D posterior β = 0.324 ± 0.099°, but Sec. 3.3 reports βALP = 0.336 ± 0.107° (Run 1) and βfree = 0.344 ± 0.096° (Run 3). No β value is reported for Run 2 (“C free”), yet Fig. 1 is explicitly “Run 2, C free.” The number in Fig. 1 is not discussed in the text and is not matched to any quoted run/likelihood choice.
- Required fix: Report the Run 2 β posterior in Sec. 3.3 with its uncertainties, stating the exact likelihood used (0.242 ± 0.061° or 0.342 ± 0.094°). Ensure the β number shown in Fig. 1 appears in the text with the same inputs and priors.

P2-E13
- Location: Sec. 3.3 (Priors)
- Problem: Prior on θi is flat on [0.01, π], explicitly excluding θi ≈ 0. This places zero prior weight on small-misalignment solutions and mechanically suppresses small-β realizations. Given that β ∝ (C0 θi) × transfer factor in your setup, this prior choice biases both posterior and Bayes factor in favor of β ≠ 0.
- Required fix: Include θi = 0 in the support (e.g., flat on [0, π] or a symmetric prior around 0 if applicable) and report prior-sensitivity of the β posterior and ln B. Quantify how much ln B changes when allowing θi near zero.

P2-E14
- Location: Sec. 3.3 and Fig. 1 (log10(m/eV) panel); Sec. 2.1–2.2
- Problem: With the implemented likelihood (a single β measurement with no time-evolution modeling), β depends only on the product of coupling and misalignment; m does not enter. Yet Fig. 1 shows a seemingly informative posterior for log10(m/eV) = −31.4
+1.4
−1.6, narrower than the stated prior [−35, −30]. This suggests either (i) an unreported mapping from (m, θi) to Δφ/fa was applied in the likelihood (contradicting the “O(1)” treatment in Sec. 2.2), or (ii) a coding/diagnostic error is producing spurious information about m.
- Required fix: Clarify exactly how m enters the likelihood. If no Δφ(θi, m) integration is used, acknowledge that m is unconstrained and that its posterior equals the prior. If an integration was used, document the equation solved, cosmology assumed, and numerical validation; then show the induced dependence of β on m and re-run the inference.

P2-E15
- Location: Fig. 1 (log10(m/eV) = −31.4…); Sec. 2.1–2.2
- Problem: The Fig. 1 posterior mode corresponds to m/H0 ≈ 20–40 (H0 ≈ 1.5×10−33 eV), not m ∼ H0. If m ≫ H0, the field would begin rolling earlier than z ∼ 1 and likely oscillate, changing the transfer factor Δφ/fa used to predict β. The text’s analytic “O(1)” factor (and the specific J0(1) illustration) assumes m/H0 ∼ 1 and does not cover m/H0 ≫ 1.
- Required fix: Either constrain m/H0 to the regime used for the analytic argument or, preferably, compute Δφ/fa(θi, m/H0) numerically in ΛCDM across the posterior support and propagate to β. Discuss how the predicted β changes for m/H0 ≫ 1, and whether Fig. 1’s preferred masses are still compatible with the claimed β prediction.

MAJOR

P2-M7
- Location: Fig. 1 caption/body cross-reference (Run identification and inputs)
- Problem: The figure caption states “Run 2, C free,” but the body never gives the corresponding β posterior for Run 2, nor does it specify which β likelihood (0.242 ± 0.061° vs 0.342 ± 0.094°) feeds this run. This prevents readers from reproducing the β = 0.324 ± 0.099° shown in the figure.
- Required fix: In Sec. 3.3, add the Run 2 β result using the exact same likelihood as Fig. 1, and state the likelihood choice in the figure caption.

P2-M8
- Location: Sec. 3.4 (Bayes factor) and Sec. 3.2 (summary likelihood)
- Problem: The reported ln B values are computed from the combined summary-likelihood that assumes Planck and ACT errors are independent. Any positive correlation (shared systematics, calibration method, or dust modeling) reduces effective significance and therefore ln B. This dependency is not acknowledged for ln B (only for βcombined in P2-E5 of the previous report).
- Required fix: Recompute ln B under correlated Gaussian summaries with ρ in a plausible range (e.g., 0–0.5), or report ln B using a single dataset. Provide a table/figure showing ln B(ρ) for the chosen symmetric prior(s).

MINOR

P2-m6
- Location: Sec. 2.2, p. 2
- Problem: Numerical conversion: “5 × 10−3 rad ≈ 0.27°.” Precisely, 5 × 10−3 rad = 0.2865°. If this number anchors the claimed 0.27°, the discrepancy should be acknowledged or the prefactor adjusted.
- Required fix: Either round consistently (e.g., 0.29°) or show the exact multiplicative factors used to obtain 0.27° (e.g., if adopting C0 θi ≈ 0.94).

P2-m7
- Location: Fig. 2 vs body text
- Problem: Fig. 2 overlays posteriors from different model parameterizations (C fixed vs C free) but the caption’s “All three are consistent” claim is qualitative. No quantitative comparison (e.g., KL divergence or a simple Δμ/σ metric) is provided, and the underlying likelihoods/prior choices for each curve are not restated in the caption.
- Required fix: Add a brief caption note summarizing which likelihood and priors each curve uses, and quantify the level of agreement (e.g., difference of means in units of combined σ).

Explanation
These items are new relative to the initial review. The most serious new issues are (i) the internal inconsistency between the reported Caγ × θi product and the figure’s plotted marginals, and (ii) the appearance of an informative posterior on m despite a likelihood that (as described) contains no m dependence. Both directly impact the credibility and reproducibility of the inference results.