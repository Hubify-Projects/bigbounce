# P2 auto-2026-06-06_0021pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7869 chars)
**Wall time**: 496.6s

---

Referee report on “Cosmic Birefringence from a Planck-Scale Axion-Like Particle: Predictions, Constraints, and LiteBIRD Forecasts” (6 pp)

Scope of this report: methodological rigor, statistical/likelihood procedures, derivations, dimensional analysis, arithmetic consistency, figure/table audits. I read all 6 pages, equations, captions, and references and recomputed the quoted numbers.

Findings

ESSENTIAL

P2-E1 (Sec. 2.1–2.2; pp. 1–2): Internal inconsistency in the predicted field displacement Δϕ/fa
- Offending text/equations:
  • Eq. (1): “Δϕ ≈ fa θi (1 − J0(m/H0)/J0(0)) ≈ fa θi × O(1). For m/H0 ∼ 1, 1 − J0(1) ≈ 0.24.”
  • Sec. 2.2: “the cosmological field evolution gives Δϕ/fa ∼ 10−2 … yielding β ≈ C0 θi × 5 × 10−3 rad ≈ 0.27°.”
- Problem: Eq. (1) implies Δϕ/fa ≈ 0.24 θi for m/H0 ≈ 1. Together with β = (C0/2)(Δϕ/fa), this gives β ≈ 0.12 C0 θi rad. With C0, θi = O(1), β would be O(0.1 rad) ≈ 7°, not 0.27°. The narrative later assumes Δϕ/fa ∼ 10−2, contradicting Eq. (1) by a factor ≈ 24. This discrepancy controls the central “naturalness” claim (C0 O(1) vs C0 ≪ 1).
- Required fix: Provide a correct, traceable derivation or validated numerical integration of the homogeneous ALP equation of motion in the ΛCDM background yielding the displacement between recombination and today, Δϕ/fa = F(m/H0, Ωm, ΩΛ) θi. Report F explicitly (with uncertainty). Remove the ad hoc J0 expression unless derived and justified; J0(0)=1 makes the Eq. (1) form particularly suspect for a time-varying H(t). All subsequent numerical claims (β ≈ 0.27°, “no fine-tuning,” posteriors for C0 θi) must be recomputed self-consistently with the corrected F.

P2-E2 (Sec. 3.2; p. 2): Undefined parameter “fphoton × C0 = 1.73 ± 0.44”
- Offending text: “The effective photon coupling parameter: fphoton × C0 = 1.73 ± 0.44 (5).”
- Problem: fphoton is not defined anywhere. The product’s units are not stated; dimensional analysis is impossible. The quoted value (1.73 ± 0.44) is not traceable to any equation in the paper.
- Required fix: Define fphoton precisely in the Lagrangian normalization used (e.g., gaγ ≡ C0/fa or gaγ ≡ αC0/(2πfa), etc.). Show how Eq. (5) is obtained from the likelihood and report it with correct units. If the intent was to constrain C0 θi F/2 from β, write that explicitly and do not introduce new, undefined symbols.

P2-E3 (Sec. 3.4; p. 3): Bayes factor arithmetic inconsistent with the reported likelihood
- Offending text: “ln B = 5.17 … for β ∈ [0°, 1°]; ln B = 4.48 for β ∈ [0°, 2°] and ln B = 5.86 for β ∈ [0°, 0.5°].”
- Audit: Using the combined Gaussian constraint in Eq. (4): β = 0.242 ± 0.061° (σ from zero ≈ 0.242/0.061 = 3.97), the posterior density at 0° is fpost(0) = [1/(√(2π)σ)] exp(−μ^2/(2σ^2)) = 0.00248 deg^−1. For a uniform prior on [0°, 1°], fprior(0) = 1 deg^−1. Savage–Dickey gives B01 = fpost(0)/fprior(0) = 0.00248, so ln B10 = −ln B01 = 6.00, not 5.17. For [0°, 2°], ln B10 = 5.30; for [0°, 0.5°], ln B10 = 6.69. Your numbers are systematically ≈0.7–0.8 too small.
- Required fix: Recompute and report Bayes factors with correct units and explicit formulae. State clearly whether β is in degrees or radians in both prior and posterior densities; SDDR is unit-sensitive. Provide the exact numerical inputs used.

P2-E4 (Abstract, Sec. 3.1, Fig. 2 caption; pp. 1–2, 5): Missing/unclear citation for “Eskilt et al. joint Planck + ACT analysis”
- Offending text: Abstract and Sec. 3.1 use “βobs = 0.342 ± 0.094° from the Eskilt et al. joint Planck + ACT analysis,” and Fig. 2 calls this the “Observed” band.
- Problem: No corresponding reference is listed in the bibliography for a joint Planck+ACT analysis by Eskilt et al. The cited Eskilt & Komatsu (2022) is Planck/WMAP only. The ACT DR6 result is listed as Diego-Palazuelos & Komatsu (2025), but not a joint analysis.
- Required fix: Provide a traceable, citable reference (published or arXiv) for the 0.342 ± 0.094° value, or remove it. If this is your own reanalysis, it must be described with full methodological detail and added as a separate section. As written, the MCMC likelihood is not reproducible.

P2-E5 (Sec. 3.3; Table 1 and throughout; pp. 2–3, 4–5): Notation inconsistency for the anomaly/coupling coefficient
- Offending text: C0 (Sec. 2), C (Table 1: “C=8 fixed”), Caγ (Sec. 3.3, Fig. 1 axes) are used apparently interchangeably.
- Problem: These symbols are not defined consistently. It is unclear whether “C”, “C0”, and “Caγ” are the same quantity or different normalizations. The prior “Caγ flat on [1,30]” (Run 2) conflicts with the claim “C0 ∼ O(1)” and with Fig. 1 numbers (see P2-E6).
- Required fix: Unify notation and define once in Sec. 2. Use the same symbol everywhere, with units and physical meaning (pure anomaly coefficient vs gaγfa normalization). Update figures/tables accordingly.

P2-E6 (Fig. 1 vs Sec. 3.3; pp. 4–5 vs p. 3): Numerical inconsistency between figure and text
- Offending content: Fig. 1 corner plot shows (reading from axes/labels) Caγ ≈ 13.4+15.6−3.1 and θi ≈ 1.33+1.12−0.31; this implies Caγ × θi ≈ 18 (order-of-magnitude), yet the text states “Caγ × θi = 3.4 ± 1.1 (8).”
- Problem: Direct numerical contradiction between the figure and the quoted product. This undermines confidence in the MCMC reporting.
- Required fix: Recompute and report a consistent set of marginalized summaries. Provide a small table with posterior means/medians and 68% CIs for all plotted parameters and key products. Ensure figures and text match.

P2-E7 (Abstract, Secs. 3.1–3.3, Fig. 2; pp. 1–3, 5): Mixing significances from different estimators without explicit “not directly comparable” caveats
- Offending text: The paper juxtaposes the combined-summary result (0.242 ± 0.061°, “3.9σ”) and a separate “βobs = 0.342 ± 0.094° (3.6σ)” value adopted for MCMC, and overlays them in Fig. 2 as “Observed.”
- Problem: These are different estimators/likelihood constructions (summary-combined vs a specific EB fit). By the journal’s standards, every juxtaposition must explicitly label them as methodologically distinct and not directly comparable. As written, readers can misinterpret cross-method σ-levels.
- Required fix: Choose and declare a primary estimator in Sec. 3.1. When quoting or plotting alternative estimates, explicitly label them as methodologically distinct and “not directly comparable” at each juxtaposition (text and figure captions), or move them to an appendix.

P2-E8 (Sec. 3.3; pp. 2–3): Missing forward model from {m, fa, θi, C0} to β in the MCMC
- Offending text: The MCMC uses βobs but does not specify how β is computed from (m, θi, Caγ/C0) inside the sampler beyond vague references to O(1) factors.
- Problem: Without a defined mapping β(θi, m, C0; background) (analytic or numerical), the MCMC cannot be replicated or reviewed. Given the inconsistency in Sec. 2.1 (P2-E1), this is critical.
- Required fix: Provide the explicit forward model used in the chains. If using an analytic approximation, give the formula and its domain of validity; otherwise, describe the numerical integration, cosmological parameters used, and computational tolerances. Validate the approximation against the numerical solution.

MAJOR

P2-M1 (Sec. 2.1; p. 1): Derivation of Eq. (1) using Bessel functions is unmotivated
- Offending text: “Δϕ ≈ fa θi (1 − J0(m/H0)/J0(0)).”
- Problem: For a scalar in a ΛCDM background with H(t) varying through radiation/matter/Λ, a closed form in terms of J0(m/H0) is not standard. No derivation or citation is provided. It appears to treat H as constant.
- Required fix: Either derive Eq. (1) rigorously (including assumptions and approximations) or replace it with a demonstrably accurate approximation/numerical result. Provide a plot/table of F(m/H0) = Δϕ/(fa θi) across the prior range with uncertainties.

P2-M2 (Sec. 3.2; p. 2): Independence assumption in the summary-likelihood combination
- Offending text: “We combine the measurements under the assumption of independent errors.”
- Problem: Planck and ACT EB self-calibration analyses may share sky, foreground models, and method systematics; independence is not guaranteed. Combining as independent can overstate significance and shrink errors.
- Required fix: Justify independence quantitatively (e.g., by citing covariance estimates or non-overlapping focal-plane systematics), or present a conservative combination (e.g., add a correlation coefficient ρ and show sensitivity for ρ ∈ [0, 0.5]). At minimum, add a caveat and an error inflation test.

P2-M3 (Sec. 3.3; Table 1; pp. 2–3): MCMC configuration inadequate for reported inferences
- Offending content: Only 720–6,840 accepted samples, unspecified number of chains, and R̂ − 1 < 0.01 reported without chain counts or effective sample sizes for each parameter. Yet Bayes factors and tail probabilities are discussed.
- Problem: These sample sizes are not sufficient for robust estimation of posterior tails or SD ratios; R̂ is not meaningful without multiple chains. The text acknowledges limitations but still draws quantitative conclusions.
- Required fix: Either (a) replace MCMC with analytic posterior propagation where possible (β is Gaussian; posteriors for simple products can be computed semi-analytically), or (b) run multiple independent chains and increase post–burn-in samples to ≥ 50k per run, report per-parameter ESS, trace plots, and rank statistics.

P2-M4 (Sec. 3.3; pp. 2–3): Justification for “C = 8 fixed” run
- Offending text: “Run 1 ALP (C = 8 fixed).”
- Problem: No motivation is given for fixing C to 8 (and what C is). If C denotes an anomaly coefficient, values depend on UV completion and are model-specific; 8 is not generic.
- Required fix: Provide a model-based rationale for the fixed value and relate C to standard anomaly normalizations, or drop this run and keep only the parameterized run with a physically justified prior.

P2-M5 (Sec. 4; p. 3): Over-strong claim of decisiveness in the LiteBIRD forecast
- Offending text: “If LiteBIRD measures β = 0 ± 0.03°, the ALP explanation is excluded at 9σ.”
- Problem: A null β at 0.03° excludes the specific parameter combination producing β ≈ 0.27°, but not the entire ALP model class (e.g., smaller C0 θi F). “Excluded at 9σ” overstates the model-level conclusion.
- Required fix: Rephrase to clarify that LiteBIRD would falsify the specific numerical prediction β ≈ 0.27° at ≈9σ, not the general ALP birefringence framework. Quantify the resulting bound on C0 θi F/2.

P2-M6 (Fig. 1 caption and Sec. 3.3; pp. 4–5): Missing numerical summaries corresponding to the plotted posteriors
- Offending content: The corner plot shows numbers that do not appear (consistently) in the text; the product reported in text contradicts the figure (P2-E6).
- Required fix: Provide a table with posterior summaries (mean/median and 68% CI) for θi, Caγ (or C0), log10(m/eV), β, and their key products. Ensure figure annotations match.

P2-M7 (References; p. 6): “In preparation” citations and unverifiable results
- Offending refs: “Namikawa et al., 2025. In preparation.” Used for comparison of mass constraints.
- Problem: PRD discourages relying on “in preparation” for quantitative claims. Readers cannot verify.
- Required fix: Replace with published/arXiv sources or remove the comparison.

P2-M8 (Sec. 3.3; p. 2): Prior choice on θi excludes negative values
- Offending text: “θi flat on [0.01, π].”
- Problem: For a periodic potential, θi ∈ (−π, π]. Restricting to positive angles implicitly folds in a sign assumption that affects β if C0 is signed. Even if β depends on Δϕ magnitude, the prior should be justified.
- Required fix: Justify the restriction or adopt a symmetric prior and state how sign degeneracies are treated.

MINOR

P2-m1 (Sec. 3.2, Eq. 4; p. 2): Reported “3.9σ from zero” is actually ≈ 4.0σ
- Audit: 0.242/0.061 = 3.97.
- Required fix: Either quote 4.0σ or add a note about rounding.

P2-m2 (Table 1; p. 3): Ambiguity in “Samples”
- Offending content: “Samples” column lists “accepted samples” but the number of chains and total draws/burn-in are not given.
- Required fix: Report number of chains, total draws, burn-in fraction, acceptance rates, and per-parameter effective sample sizes.

P2-m3 (Sec. 3.1; p. 2): Dataset labels and figure model labels inconsistent
- Offending content: Runs are “Run 1/2/3” in text; Fig. 2 legend uses “Model 2,” “Model 2b,” “Model 0.”
- Required fix: Unify naming across text, table, and figures.

P2-m4 (Sec. 2.2; p. 2): Unit conversion
- Offending text: “5 × 10−3 rad ≈ 0.27°.”
- Audit: 5 × 10−3 rad = 0.286°. 
- Required fix: Correct the conversion or round consistently.

P2-m5 (Sec. 6; p. 5): Novelty and attribution
- Offending text: “Our contribution is not the model itself, but rather the specific parameter identification (fa ∼ MPl, m ∼ H0) …”
- Comment: Fujita et al. (2021) already emphasized Planck-scale ALP yielding β ∼ 0.3°. The manuscript should carefully delimit the precise incremental methodological contribution.
- Required fix: Calibrate the novelty statement and add precise citations to prior work demonstrating fa ∼ MPl, m ∼ H0 predictions.

NIT

P2-n1 (Throughout): Recurrent undefined or shifting symbols (C, C0, Caγ, fphoton).
- Fix: Harmonize symbols and add a notation table.

P2-n2 (Various): Minor typographical/formatting issues (e.g., “FF˜”, hyphenation, spacing).
- Fix: Proofread.

P2-n3 (Sec. 1; p. 1): “3.6σ isotropic birefringence signal” should be tied to an explicit, citable source with the exact estimator used.
- Fix: Add explicit citation and method qualifier.

Arithmetic/consistency checks performed

- Combined constraint (Eq. 4): From β1 = 0.30 ± 0.11°, β2 = 0.215 ± 0.074°, the inverse-variance weighted mean is 0.2416° with σ = 0.0614°, in agreement with 0.242 ± 0.061°. Significance is ≈ 3.97σ (not 3.9σ).
- Bayes factor via SDDR: Using Eq. (4), ln B10 ≈ 6.00 for a flat prior on [0°, 1°]; your quoted 5.17 is inconsistent (see P2-E3).
- LiteBIRD forecast: 0.27°/0.03° = 9.0σ as stated; but the model-level exclusion claim is overstated (see P2-M5).

Page-length assessment

- At 6 pages, the length is appropriate, but the current draft lacks the essential derivations and methodological details. Additional space will be needed to fix P2-E1, P2-E4, and P2-E8. Recommend a target length of 7–9 pages after adding the necessary derivations, likelihood details, and corrected results.

## Summary recommendation
MAJOR REVISIONS

The manuscript contains multiple essential methodological inconsistencies. Chief among them is a fundamental contradiction between the stated field displacement (Eq. 1 implies Δϕ/fa ≈ 0.24 θi) and the value implicitly used to obtain β ≈ 0.27° (Δϕ/fa ∼ 10−2). The Bayes factor arithmetic is inconsistent with the supplied likelihood, and a key dataset used in the MCMC (“Eskilt et al. joint Planck + ACT”) is uncited and therefore non-traceable. Notation is inconsistent, and figure/text numbers disagree. These issues must be resolved with explicit derivations or validated numerics, unified notation, corrected calculations, and fully traceable data sources before the paper can meet PRD standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eye pass)

ESSENTIAL

P2-E9 (Fig. 1 vs stated priors; pp. 4–5 vs p. 2): Posterior credible interval exceeds the stated prior bound
- Evidence: Text says prior log10(m/eV) ∈ [−35, −30]. Fig. 1 annotation shows log10(m/eV) = −31.4+1.5−1.2, whose 68% upper edge is −29.9, i.e., outside the stated prior maximum (−30).
- Problem: A posterior C.I. cannot extend beyond the prior’s support. Either the plotted run used a different prior or the figure annotation is incorrect.
- Required fix: Clarify the actual prior used in the plotted run, correct the figure annotation, or rerun with the stated prior. Provide a table with the exact priors used for each plotted posterior.

P2-E10 (Sec. 3.4; p. 3): Bayes factor definition ambiguity likely explains the systematic ~0.7–0.8 shortfall found earlier
- Evidence: You write “Comparing the ALP model (β ≠ 0) against the null (β = 0): ln B = 5.17,” but never define whether B ≡ B10 or B01. The earlier arithmetic discrepancy (your ln B10 smaller than the recomputed value by ≈0.7–0.8) is numerically close to ln 2.
- Problem: This is consistent with a boundary/one-sided prior mishandling (e.g., using a one-sided uniform prior on β ≥ 0 but evaluating the SDDR with an untruncated two-sided Gaussian posterior, or mixing one-sided and two-sided priors/posteriors). Without an explicit statement of truncation and model indexing, the SDDR result is not reproducible.
- Required fix: Specify B10 ≡ P(data|M1)/P(data|M0); state explicitly whether the β prior and posterior used in SDDR were one-sided [0, U] or two-sided [−U, U], and ensure consistency. Recompute ln B10 with those choices. Report the normalization constants for any truncation.

P2-E11 (Fig. 1 vs Sec. 3.3; pp. 4–5 vs p. 3): β posterior from the “extended ALP” run is not reported in text and appears inconsistent with the listed runs
- Evidence: Fig. 1 (Run 2, “C free”) shows β[deg] = 0.324 ± 0.099. In Sec. 3.3 the only β summaries provided are for Run 1 (0.336 ± 0.107°) and Run 3 (0.344 ± 0.096°). The “C free” run β is neither quoted nor compared.
- Problem: Readers cannot reconcile the figure with the text; the set of reported β posteriors is incomplete and naming of runs/models is inconsistent (compounds P2-m3 from the first report).
- Required fix: Add the β summary for the “C free” run in Sec. 3.3 and align run labels with Fig. 1/2.

MAJOR

P2-M9 (Sec. 2 and throughout): Cosmological parameter values are not specified for any computation depending on H(z)
- Problem: All claims about Δϕ/fa, the onset of rolling at z ~ O(1), and any numerical integration for F(m/H0, Ωm, ΩΛ) are cosmology dependent. No values for H0, Ωm, ΩΛ (and radiation parameters if used) are stated.
- Required fix: State the cosmological parameters used (e.g., Planck 2018 baseline or your chosen set) and their values. If any derived numbers (e.g., your putative F) are sensitive to these inputs, provide that sensitivity.

P2-M10 (Sec. 3.3; pp. 2–3): Posterior near or at prior boundary implies prior-dominated inference; robustness not assessed
- Evidence: Fig. 1 shows log10(m/eV) peaking close to the prior’s upper edge (and even exceeding it per P2-E9). This is a classic indicator that the posterior is prior-limited.
- Problem: Inferences about m (and any derived β dependence on m) may be biased by the hard bound. No alternative prior ranges or robustness checks are shown.
- Required fix: Expand the prior range for log10(m/eV) and report whether the posterior continues to press against a boundary. Provide a robustness table/plot showing stability of posterior summaries under wider priors.

P2-M11 (Sec. 3.4; p. 3): SDDR at a boundary requires care; conditions for validity not discussed
- Problem: With a one-sided prior β ∈ [0, U], the null β=0 lies at the boundary. The classic SDDR derivation assumes the nested parameter point is in the interior where prior density is well-defined and the same under the larger model. Boundary SDDR can still be used, but only with explicit attention to truncation and normalization.
- Required fix: Cite and follow a boundary-aware SDDR treatment, or avoid SDDR and compute the evidence ratio via direct numerical integration (e.g., bridge sampling) using the same likelihood and priors used to generate Eq. (4).

P2-M12 (Abstract vs Sec. 3; pp. 1–3): “Order-unity, no fine-tuning” claim for coupling relies on an undefined mapping and a product parameter (fphoton × C0) that is nowhere derived
- Problem: Beyond the undefined symbol flagged earlier (P2-E2), the abstract’s inference about “no fine-tuning” depends on how β maps to microscopic parameters and on the size of F(m/H0, Ωm, ΩΛ), which is not provided or validated. This is a methods issue, not just a notation issue.
- Required fix: Provide the explicit β(θi, m, C0; cosmology) used in inference, quantify F, and then demonstrate via a posterior on C0 and θi that “order-unity” holds once the corrected mapping is applied.

MINOR

P2-m6 (Fig. 2 vs Sec. 3; pp. 5 vs 2–3): Model/run naming mismatch persists and now obscures which curve corresponds to which run
- Evidence: Fig. 2 legend uses “Model 2,” “Model 2b,” and “Model 0,” while Sec. 3 and Table 1 use “Run 1/2/3.” There is no explicit mapping.
- Required fix: Use a single run ID across text, tables, and figures; add a legend/table mapping if necessary.

P2-m7 (Throughout): Ambiguity over Planck mass convention (reduced vs unreduced)
- Problem: You write “fa ∼ MPl” without stating whether MPl is the reduced (2.435×10^18 GeV) or unreduced (1.22×10^19 GeV) Planck mass. This affects numerical statements about “order-unity” couplings and dimensional analysis in Sec. 2.2.
- Required fix: State explicitly which convention is used and use a single symbol; adjust any numerical back-of-the-envelope conversions accordingly.

P2-m8 (References; p. 6): Author name likely misspelled/inconsistent
- Evidence: “Namikawa, Murai, and Sho Naokawa.” The third author’s surname appears nonstandard; also the in-text “Namikawa, Murai & Naokawa [Namikawa et al., 2025]” differs from typical spellings in this subfield.
- Required fix: Verify and correct author names and ensure consistency between text and bibliography.

P2-m9 (Sec. 1 vs Sec. 3; pp. 1–2): Stale significance statement
- Evidence: Introduction: “Combined, the evidence exceeds 3.5σ.” Sec. 3.2 reports 3.97σ from the stated combination.
- Problem: Readers see two different combined significances without qualification.
- Required fix: Harmonize to a single combined significance (with method noted), or clearly label the introductory statement as a literature summary distinct from your recomputed value.

P2-m10 (Sec. 3.2, Eq. 3; p. 2): Units for β in the likelihood not stated
- Problem: Eq. (3) defines L(β) with σi but never states explicitly whether β is in degrees or radians inside the likelihood. Given later use of SDDR and unit sensitivity, this should be explicit.
- Required fix: State the angular unit used in Eq. (3) and maintain it consistently through all downstream calculations.

NIT

P2-n4 (Sec. 2.1, Eq. 1; p. 1): Redundant/odd notation “J0(m/H0)/J0(0)”
- Problem: Since J0(0)=1, writing a ratio invites confusion about hidden normalizations.
- Fix: If the expression remains, simplify to 1 − J0(m/H0) and justify its derivation; otherwise remove per P2-M1.

P2-n5 (Sec. 6; p. 5): fNL value dropped without context
- Problem: “fNL = −35/8” is asserted as a “complementary test” with only a pointer to a companion paper. As a standalone statement it is abrupt and unexplained.
- Fix: Add one sentence clarifying that this is unrelated to birefringence and depends on a different framework, or move to an appendix/citation-only remark.

If these are addressed alongside the previously listed essentials, the paper’s methodological transparency and numerical consistency would improve substantially.