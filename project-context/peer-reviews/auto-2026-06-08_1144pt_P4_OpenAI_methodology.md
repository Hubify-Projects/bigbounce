# P4 auto-2026-06-08_1144pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (9134 chars)
**Wall time**: 366.3s

---

Referee report for “Survey-Scale Galaxy Chirality with Equivariant TTA: A −0.122σ Subsample-Mask ℓ=1 Null, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)”

Overall scope
The paper presents a very large chirality catalog and an angular-dipole analysis using MASTER with multiple null/diagnostic procedures. The stated headline result is a null ℓ=1 chirality dipole on a wider analysis mask and an interpretation of a canonical-mask residual as a survey/systematics effect, not a cosmological signal. The methodological theme—bias hardening and null testing—is appropriate for PRD Methods. However, there are several internal inconsistencies in the definitions of the analyzed fields, inconsistencies between tabulated numbers and their reported significances, and ambiguity about look-elsewhere accounting and sigma/p-value mappings. These must be resolved before this is publishable in PRD.

Findings

ESSENTIAL

P4-E1 (Section IV.C p.4 and Appendix A p.7): Inconsistent definition of the analysis field Ap.
- Problem: Eq. (3) (p.4) defines Ap = (NCW − NCCW)/(NCW + NCCW), i.e., spirals-only denominator. Appendix A (a) repeats this definition (“spirals only”), but Appendix A (c) later defines the field as Ap = (NCW − NCCW)/Ntotal, where Ntotal includes non-spirals (NS). This is a fundamental inconsistency for the reported MASTER results and the monopole subtraction ⟨A⟩mask,gw.
- Required fix: Unify and explicitly state a single, consistent definition of Ap for all MASTER computations. If a change of definition was applied between different analyses (e.g., canonical vs subsample mask), explicitly label where each definition was used, recompute all quoted Cℓ, σ, and p-values accordingly, and update all affected numbers (including ⟨A⟩mask,gw = −0.005294 if it depends on Ntotal). Provide a minimal reproducible snippet (pseudocode) to construct the field and weight maps.

P4-E2 (Table III p.5): Significance values inconsistent with listed Cℓ and σnull.
- Problem: For ℓeff=4, Cℓ×10^6=3.210 and σnull×10^6=0.804, but the reported “Significance (σ)” is +6.097. The straightforward ratio 3.210/0.804 ≈ 3.99, not 6.10. For ℓeff=9, Cℓ is negative (−0.248), σnull=0.574, yet the reported significance is “+2.232”. Without listing the null mean for each band, these “σ” entries cannot be verified and appear inconsistent (also sign conventions are unclear).
- Required fix: For every row in Table III, specify whether significances are computed as (Cmeas − ⟨Cnull⟩)/σnull or |Cmeas − ⟨Cnull⟩|/σnull and report the corresponding ⟨Cnull⟩ for each bin. Correct the numerical values accordingly. Make sign conventions explicit. If the bandpowers are not zero-mean under the null, the null mean must be shown.

P4-E3 (Appendix C p.8 and Section VI p.6): Look-elsewhere effect accounting is self-contradictory.
- Problem: The text states “Testing all hemisphere-pairs... maximum asymmetry 3.05σ. The direct-MC look-elsewhere test (N=10,000 random-label shuffles) gives pLEE ≤ 10^−4 (rejection of the random-label null); the conservative Bonferroni/BH penalty across ∼650 tested directions reduces post-LEE significance to <1σ.” If pLEE already includes look-elsewhere (global) accounting, applying Bonferroni/BH again double-corrects. Moreover, if pLEE ≤ 10^−4 is a post-LEE p-value, multiplying by 650 yields p ≤ 0.065 (≈1.8σ), not “<1σ”. If pLEE is actually a pre-LEE local p-value, then it must be stated so, and the post-LEE p reported separately.
- Required fix: Clarify whether pLEE is pre-LEE (local) or post-LEE (global). Report both local and global p-values unambiguously, and do not apply two LEE corrections. Update the quoted significance accordingly.

P4-E4 (Section IV.B p.4): “Asymmetry-suppression factor” and raw/equivariant monopoles are numerically unsupported/inconsistent with Table II.
- Problem: The paper claims “3.86× asymmetry-suppression factor from raw +2.05% to equivariant −0.53%,” but Table II lists raw excess +0.79% and equivariant −0.26% (spirals-only fraction). The 2.05% and −0.53% values appear to be galaxy-weighted mask means (Appendix A reports ⟨A⟩mask,gw = −0.5294%), but the raw +2.05% number is not shown anywhere, and the switch between weighting/denominators is not declared at the point of comparison.
- Required fix: Explicitly state the precise definitions (spirals-only vs Ntotal denominator; uniform vs galaxy-weighted average) for the raw and equivariant “monopoles” being compared. Add the raw weighted monopole value (2.05%) to the manuscript with its uncertainty/definition. Do not compare metrics with different weighting schemes without stating so.

P4-E5 (Multiple places, e.g., Conclusions b. p.6–7; Abstract p.1; Sections IV.C–D): Side-by-side σ from different nulls without repeated explicit caveat.
- Problem: While the manuscript states globally that σ values from different nulls are not directly comparable, there are several points where disparate σ values are juxtaposed (e.g., +3.64σ canonical vs −0.122σ subsample-mask vs +0.43σ real-space) without reiterating the caveat at that juxtaposition. The instructions in this report require that any side-by-side comparison of σ from different null procedures include an explicit reminder of non-comparability at that point.
- Required fix: At every instance where σ from different nulls appear side-by-side (e.g., Section IV summary, Conclusions b), append an explicit note that these σ derive from different nulls and are not directly comparable.

P4-E6 (Table II p.4 and Section IV.B p.4): Dev. (σ) sign and magnitude for Tier C.
- Problem: For Tier C, cw/(cw+ccw)=0.4974±0.000279. The deviation from 0.5 is (−0.0026)/0.000279 ≈ −9.32σ. Table II lists “Dev. (σ) = 9.5,” omitting the sign and with a magnitude inconsistent with the listed numbers. Elsewhere (Section IV.B), “The Catalog C residual (9.5σ from 0.5000...)” again uses 9.5 but does not indicate sign.
- Required fix: Report the correct signed deviation with correct magnitude (−9.3σ to one decimal) or explicitly define Dev. (σ) as |z| (absolute). Ensure consistency between Table II and the text.

MAJOR

P4-M1 (Section III.A p.3; Section IV.C p.4; Appendix A p.7): Definition and construction of masks (“canonical mask” vs “analysis subsample mask”) are under-specified.
- Problem: The paper uses two masks: a canonical mask (fsky=0.49005) and a “strict-superset subsample mask” (fsky=0.659), but the exact construction rules (pixel thresholding, NSIDE, applied apodization, and whether thresholds are on Nspiral or Ntotal) are not fully and unambiguously specified in the main text. Reproducibility requires exact rules.
- Required fix: Provide a precise definition for each mask: NSIDE; pixel inclusion thresholds; whether thresholds are on Nspiral or Ntotal; any apodization kernels (functional form, angular scale); and a sentence clarifying “strict-superset” relationship. Consider moving these to the Methods section with a reference to Appendix A.

P4-M2 (Section IV.C p.4): Real-space dipole “0.43σ (p=0.30)” mapping is unclear/inconsistent with Gaussian intuition.
- Problem: A “0.43σ” deviation would correspond to a two-sided Gaussian p ≈ 0.67; the paper lists p=0.30 (isotropic-null bootstrap). If “σ” is defined as a standardized score under a non-Gaussian empirical null, the mismatch with p may be fine, but the definitions must be explicit.
- Required fix: Explicitly define how “σ” is computed for the real-space dipole (is it ∆/σnull with σnull from bootstrap?) and how p is estimated (empirical rank, one- or two-sided). State clearly whether p is one- or two-sided. If the “σ” is not a Gaussian z-score, avoid implying Gaussian p–z equivalence or provide the empirical z–p mapping plot/table for clarity.

P4-M3 (Section IV.D p.4–5 and Appendix D p.8–9): Mixing of different nulls for hemisphere maximum statistic and for canonical residual.
- Problem: The text quotes 3.05σ (Appendix C) for the hemisphere maximum and +4.42σ in Table IV for the same-type statistic, but under a different null (monopole-only binomial generative vs label-shuffle permutes). This is confusing without a side-by-side, label-consistent presentation.
- Required fix: Wherever two values of the same statistic under different nulls are compared or both quoted, state the null explicitly at the point of reference. Consider providing a small table in the main text listing the statistic, null type, and σ/p side-by-side to avoid confusion.

P4-M4 (Section VI.B p.6 and Abstract p.1; Conclusions p.6): Overstatement in comparing to Shamir amplitudes (6–12×).
- Problem: The paper variously compares its sensitivity to Shamir’s ∼2–4% amplitudes using the empirical threshold (0.75%) and the Fisher floor (0.29%), yielding very different factors (∼2.7–5.3× and ∼6.9–13.8× respectively). The abstract claims “inconsistent by a factor of ∼6–12,” but that only holds relative to the Fisher floor, not the empirically demonstrated threshold used elsewhere as the falsification boundary.
- Required fix: Use a single, consistent comparator. If the empirical 50%-recovery 3σ threshold (0.75%) is the operative sensitivity, then state the factor relative to 0.75% only. Alternatively, report both factors but clearly label which is relative to the Fisher floor and which to the empirical threshold.

P4-M5 (Appendix A p.7): MASTER terminology: “post-MASTER pseudo-Cℓ.”
- Problem: The text mixes “pseudo-Cℓ” (pre-deconvolution) with “MASTER-deconvolved” quantities. “Pseudo-Cℓ” should be reserved for masked, not deconvolved spectra.
- Required fix: Use “pseudo-Cℓ” exclusively for pre-deconvolution estimates and “deconvolved Cℓ” for MASTER outputs. Audit the manuscript for consistent terminology.

MINOR

P4-m1 (Appendix A p.7): Monopole subtraction and effect on σ wording.
- Problem: “Monopole subtraction reduces decoupled C1 ... and increases σ from +1.85 to +3.64” is counterintuitive without context (noise model changed). While plausible, a short explanation would help the reader.
- Required fix: Add one sentence noting that monopole subtraction reduces leakage variance under the chosen null, thereby increasing the standardized significance of the residual, even as the raw amplitude decreases.

P4-m2 (Section IV.D p.4–5 and Appendix D): Sign of σ for correlation coefficients.
- Problem: The text reports “rℓ=2 = −0.65 (σ = −2.89).” Conventionally, one would report |z| with the sign carried by r. This is minor but potentially confusing.
- Required fix: Either report z as |z| with the sign in r, or define that z carries the sign of r explicitly.

P4-m3 (Section V.A p.5 and throughout): “Earlier paper versions” language.
- Problem: “...were interpreted in earlier paper versions...” is internal revision history.
- Required fix: Remove “earlier paper versions” phrasing. State the interpretation directly as of this submission.

P4-m4 (Appendix A p.7): Apodization notation.
- Problem: “C 2 2° apodization” is unclear (typesetting?). Usually denoted as cosine-squared with 2° scale.
- Required fix: Standardize to “cos^2 apodization with 2° scale” or similar conventional wording.

P4-m5 (Table II p.4): Clarify whether “Dev. (σ)” is signed or absolute.
- Problem: Current presentation omits sign for Tier C and shows a magnitude inconsistent with the listed numbers.
- Required fix: Label column as “|Dev.| (σ)” if absolute, and fix magnitudes; or include signs consistently.

NIT

P4-n1 (Section IV.E p.5): C(Ap×ntotal) notation.
- Problem: Use standard cross-spectrum notation Cℓ(Ap, ntotal).
- Required fix: Replace with standard Cℓ(Ap, ntotal).

P4-n2 (Data Availability p.9): Minor URL hyphenation artifacts (“galaxy- chirality- catalog”).
- Required fix: Remove errant spaces/hyphens in URLs to ensure they resolve.

P4-n3 (Multiple pages): Occasional spacing/formatting artifacts in equations and units (e.g., “Cℓ × 10^6 (sr)”).
- Required fix: Ensure consistent typesetting; keep units attached without extra spaces.

Arithmetic and internal consistency checks (selected)

- Binomial σ for cw fraction (Tier C): With p=0.4974, N=3,201,160, σ ≈ sqrt(p(1-p)/N) ≈ 0.0002795, consistent with ±0.000279.
- Deviation in σ for Tier C: (0.4974−0.5)/0.000279 ≈ −9.3σ. The manuscript’s “9.5σ” should be corrected or justified if using a different weighting.
- Subsample MASTER ℓ=1: (1.494−1.546)/0.429 ≈ −0.122, consistent.
- Table IV “99.3% of observed amplitude”: 1.685/1.696 ≈ 0.9935, consistent.
- Hemisphere max|A| (Table IV): (3.48−1.69)/0.41 ≈ 4.37 (reported 4.42), small rounding discrepancy acceptable if uncertainties are empirical.

Methodological adequacy of Monte Carlo sizes

- For the canonical-mask post-MASTER residual (pMC=0.030 with N=500), MC resolution is coarse but adequate for p≈0.03 (15/500 exceedances). For tail probabilities near 10^−3 (not reported here), larger N would be necessary. No change required, but please state the MC standard error where p-values are close to decision thresholds.

Claims of novelty
- “Largest chirality catalog” (3.20M spirals) vs CE-ResNet ∼1.95M: factor ≈1.64×; plausible.
- Equivariance TTA approach vs CE-ResNet architectural equivariance: complementary, as stated.

Length
- The paper is dense but appropriate for a Methods article. With the required clarifications and table corrections, the 10-page length is acceptable.

## Summary recommendation
MAJOR REVISIONS

The paper presents a potentially valuable, carefully-designed null result and a thorough set of diagnostics, but there are several essential methodological inconsistencies that must be resolved before publication: (1) unify the field definition (spirals-only vs all-galaxy denominator) across the analysis and recompute affected results; (2) correct/clarify the significances in Table III; (3) fix the look-elsewhere accounting; (4) consistently handle side-by-side σ from different nulls with explicit caveats; and (5) reconcile/justify the raw/equivariant monopole percentages cited in the text with Table II. Once these are addressed and numbers updated, the work could be suitable for PRD Methods.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS

P4-E7 (Abstract p.1; Conclusions b. p.6–7; Appendix A p.7): Internal inconsistency between σ and p for the same canonical-mask residual.
- Problem: The canonical-mask post-MASTER residual is reported as “+3.64σ (z = ∆/σnull; empirical rank pMC = 0.030, i.e. ≈1.9σ Gaussian-equivalent).” A z = 3.64 would imply a two-sided Gaussian p ≈ 2.7×10−4, not 0.030. Reporting both 3.64σ and p = 0.030 for the same test statistic is self-contradictory unless you show that the empirical null is so non-Gaussian that z and p are decoupled; that justification is not provided.
- Required fix: For each quoted significance, report either (i) the standardized z and the corresponding empirical p from the same null distribution, with an explicit z–p mapping (e.g., QQ or CDF plot), or (ii) just the empirical p (rank) without converting to a “σ-equivalent.” Do not mix a large z with a much larger empirical p for the same statistic without an explicit explanation.

P4-E8 (Table III p.5; Appendix A p.7): “Joint χ2/dof (38 bandpowers)” is inconsistent with the described binning and with the rows shown.
- Problem: Table III lists 1 single-ℓ bin (ℓ = 1) and 5 low-ℓ bandpowers, but then quotes a joint χ2/dof over 38 bandpowers. Appendix A states nlb = 1 (single-ℓ bins) up to ℓmax = 191 for the configuration; the 5 bandpowers shown are also inconsistent with nlb = 1. The manuscript never specifies the alternative binning that yields “38 bandpowers.”
- Required fix: Specify the exact binning used to compute the “38 bandpowers” χ2 (nbin, nlb, ℓ ranges), and ensure Table III and Appendix A describe the same configuration. Either include the full set of bandpowers used for χ2 or move the χ2 line to the appendix with the corresponding figure/table. Recompute χ2 if numbers change.

P4-E9 (Appendix D f. p.8–9): Arithmetic mismatch in Abest_dipole and its percent conversion; missing uncertainty.
- Problem: The text states “Abest_dipole = 4.55×10−3 (0.23% in fCW units)” and later “4.51×10−3.” But 4.55×10−3 = 0.455%, not 0.23%. No uncertainty on Abest_dipole is given, while extremely large z-values (|z| ≈ 250) are quoted.
- Required fix: Correct the 0.23% vs 0.455% conversion and report σ(Adipole) explicitly for both the naive WLS and the block-bootstrap cases. If |z| values stem from an unrealistically small naive covariance (pixel-independence), state this clearly, and avoid quoting enormous |z| in the main text without context. Provide the numerical posterior mean and 1σ error bars for Abest_dipole in both the 9-template and 24-template fits.

P4-M6 (Abstract p.1; Conclusions d. p.6–7): Falsification criterion mixes a 3σ amplitude threshold with a 5σ detection claim without scaling justification.
- Problem: The abstract states that “a future survey detecting a chirality dipole at σ > 5 with full amplitude ≳ 0.75% … would falsify the present null.” The 0.75% is the empirical 50%-recovery-at-3σ threshold on the HC subsample; a 5σ threshold for the same pipeline and sample geometry would generally require a higher amplitude unless N or fsky increases. The later “≥ 10^7 galaxies” qualifier appears only in Conclusions but the abstract lacks the scaling link.
- Required fix: State the precise scaling underlying the 5σ ≳ 0.75% criterion (e.g., A5σ ≈ A3σ × 5/3 × √(Nref/Ntarget)). Give a concrete example: with N = 10^7 and the measured classification noise, what A is needed for 5σ under the same null? Align the abstract and conclusions.

P4-M7 (Appendix A vs Table III): Binning/method mismatch between “single-ℓ bins” and “bandpowers.”
- Problem: Appendix A(b) declares single-ℓ bins with nlb = 1 across ℓmax = 191. Table III rows 2–5 report bandpowers over [2–6], [7–11], [12–16], [17–21], [22–26]. This alternative binning is not described in Appendix A.
- Required fix: Document the exact NaMaster binning used for Table III bandpowers (function call, nlb, edges). If different from the primary config, label it as a “diagnostic recompute” with its own configuration block.

P4-M8 (Section IV.E p.5 vs Appendix E.b p.9): Conflicting σ for the same peq > 0.6 cut under different “dipole” estimators without clear definitions.
- Problem: Section IV.E says “cutting to peq > 0.6 gives −0.03σ.” Appendix E.b says “Catalog C-full +4.31σ monopole-preserving dipole collapses to +0.62σ (HC-broad-0.6).” The same peq > 0.6 cut yields two different σ with opposite signs under two “dipole” estimators (“simple dipole” vs “monopole-preserving dipole”), but these estimators are not defined side-by-side where the numbers are quoted.
- Required fix: Define both estimators explicitly (functional forms, monopole treatment, weighting) and present a small table listing σ for the same peq cuts under each estimator to avoid confusion. Clarify that the −0.03σ refers to [estimator A] and +0.62σ to [estimator B], and why they differ in sign/magnitude.

P4-m6 (Conclusions a. p.6–7; Section IV.D p.4–5): “99.3% of observed amplitude” statement is not accompanied by the corresponding uncertainty on the ratio.
- Problem: While Table IV supports 1.685/1.696 = 0.9935, the uncertainty on this ratio under finite MC (N = 500) and finite data variance is not quoted. This matters because the conclusion is used qualitatively to argue near-complete reproduction of the observed pre-MASTER pseudo-Cℓ by monopole leakage.
- Required fix: Quote the uncertainty on the 99.3% ratio (e.g., via delta method or bootstrap across MC realizations) or provide a 68% interval on the null mean. A short clause such as “(99.3% ± X%)” would make the argument more rigorous.

P4-m7 (Section III.D p.3; Table II p.4; Appendix B p.7): Probability calibration quality is asserted qualitatively but not quantified.
- Problem: The paper uses calibrated probabilities to stratify by “peq” and to argue about sample-purity ladders, yet provides no standard calibration metrics (e.g., ECE, Brier score) or reliability plots. The stated median confidence of 0.9997 suggests potential overconfidence.
- Required fix: Add at least one quantitative calibration metric (ECE or Brier) and a brief reliability curve for the CW/CCW vs NS probabilities on a held-out set. This is especially relevant since peq cuts drive several diagnostic conclusions.

P4-m8 (Section VI p.6; Appendices C/E): “Maximum regional asymmetry is 0.32%” and several other hedged claims are not numerically backed in the main text.
- Problem: The 0.32% figure is not tied to a specific estimator, mask, or region definition in the main text; neither is an uncertainty provided.
- Required fix: Specify the estimator and region definition for the 0.32% value, and add an uncertainty or null-based p-value. Provide a pointer to the exact table/figure in the repository.

P4-m9 (Appendix A a. p.7): Weighted-mean subtraction claim lacks a minimal proof or reference.
- Problem: The statement “The depth weighting does not introduce a monopole–dipole coupling because the galaxy-weighted mask-mean ⟨A⟩mask,gw is subtracted” is plausible but not justified. With A defined using a spirals-only denominator and weights using all galaxies, some residual coupling could, in principle, remain.
- Required fix: Add a one-sentence justification or reference showing that subtracting the weighted mean of a scalar field before MASTER decouples ℓ = 0 from ℓ = 1 to leading order, even if the weight map and field map use different galaxy subsets; or empirically demonstrate negligible residual coupling in a controlled simulation.

P4-n4 (Throughout): Inconsistent naming of the null procedures increases ambiguity.
- Problem: The manuscript uses multiple near-synonymous labels—“per-pixel random-label permutation,” “per-pixel-shuffle,” “label-shuffle,” and “per-pixel random-label shuffles”—for the same null. Elsewhere “binomial-monopole generative null” is also used, but sometimes appearing next to “direct-MC” without clear distinction.
- Required fix: Standardize the null labels and include a one-line glossary early in Methods (e.g., “Permutation null = …; Binomial-monopole null = …; Isotropic bootstrap = …”). Use the standardized names consistently in text and tables.

P4-n5 (Appendix A p.7; Conclusions b. p.6–7): “moment-ratio” terminology is nonstandard.
- Problem: The phrase “z = ∆/σnull moment-ratio” is uncommon and may confuse readers about whether a Gaussian z-score is intended.
- Required fix: Replace with “standardized score z = (Cmeas − ⟨Cnull⟩)/σnull” or equivalent standard wording.

Explanation
The initial review focused on field-definition inconsistencies, significance-table issues, LEE accounting, mask definitions, terminology, and raw/equivariant monopole comparisons. Upon re-examination, additional arithmetic and consistency problems emerged: the canonical residual’s σ–p mismatch for the same test, the unexplained “38 bandpowers” χ2 line, a clear conversion error for Abest_dipole, ambiguous estimator definitions leading to conflicting σ for the same peq cut, and several clarity gaps in calibration, null naming, and quantitative backing of hedged claims. Addressing these issues will materially improve the paper’s rigor and reproducibility.