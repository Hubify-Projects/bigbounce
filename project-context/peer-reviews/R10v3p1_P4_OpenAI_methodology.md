# P4 R10v3p1 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (9027 chars)
**Wall time**: 386.6s

---

Referee report for “Survey-Scale Galaxy Chirality with Equivariant TTA: A −0.122σ Subsample-Mask ℓ=1 Null, …”

Overall assessment
The paper presents a large-scale, machine-learning-based chirality catalog (8.47M galaxies; 3.20M spirals) and a set of dipole/isotropy tests, with the headline claim that the ℓ=1 chirality dipole is consistent with null under a MASTER-deconvolved estimator on a “subsample mask,” and a +0.43σ real-space cross-check. The work includes extensive diagnostics of survey-mask and classifier systematics and an (imperfect) quantification of monopole–mask leakage.

However, there are multiple methodological and numerical inconsistencies that must be corrected for PRD. Chief issues include: an incorrect table cross-reference in the abstract that obscures the null-procedure mapping; internal numerical inconsistencies in the reported global CW fractions and “suppression factor”; inconsistent or insufficiently justified significance and p-values (especially across different nulls using limited MC); ambiguous definitions (e.g., the “subsample mask” and n=5,547,858); and several places where the text uses version-history language inappropriate for a published paper. Some table entries (Table III bandpower significances) appear arithmetically inconsistent with the displayed numbers. The “Fisher floor” and the propagation to a “true-underlying threshold” are not coherently derived. These are essential to address in a methodology-focused PRD submission.

Detailed findings

ESSENTIAL

P4-E1
- Location: Abstract (page 1), last sentence of first paragraph
- Problem: “see Table II for the mapping of each result to its null.” Table II is the “Global CW fraction across catalog tiers,” not the null mapping. The mapping of estimator→mask→null is in Table I.
- Required fix: Correct the cross-reference to Table I (or provide a dedicated table that maps each estimator to its null, and refer to that). This error obscures how σ values are defined and violates the paper’s own admonition to keep nulls distinct.

P4-E2
- Location: Sec. IV.B “Global CW Fraction” (page 4)
- Problem: Inconsistent numbers for the raw/equivariant monopoles and suppression factor: “3.86× asymmetry-suppression factor from raw +2.05% to equivariant −0.53%.” Table II reports Tier A = 0.5079 (i.e., +0.79%), Tier C = 0.4974 (i.e., −0.26%). The stated +2.05% and −0.53% do not match Table II. The quoted suppression factor 3.86× is also inconsistent (0.79%/0.26% ≈ 3.04, not 3.86).
- Required fix: Replace +2.05% and −0.53% with values consistent with Table II (or correct Table II). Recompute the suppression factor and ensure all related text uses a single, clearly stated convention (Ap units vs fCW−0.5). If −0.53% refers to Ap (twice fCW−0.5), make that explicit and ensure Tier A is given in the same units.

P4-E3
- Location: Table II (page 4) and Sec. IV.B (page 4)
- Problem: The “Dev. (σ)” column is numerically inconsistent with the quoted values and the listed uncertainties. Using σbinom = 0.000279:
  - Tier A: (0.5079−0.5)/0.000279 = 28.32σ (table shows 28.8σ).
  - Tier B: (0.504−0.5)/0.000279 = 14.34σ (table shows 14.6σ).
  - Tier C: (0.4974−0.5)/0.000279 = 9.33σ (table shows 9.5σ; Sec. IV.B text also says “9.5σ”).
- Required fix: Recompute and correct the “Dev. (σ)” values or, if a different σ was used (e.g., σ = sqrt(p(1−p)/N) with p ≠ 0.5), state the exact σ used for each tier and show the calculation. Ensure consistency between text and table.

P4-E4
- Location: Abstract (page 1); Sec. IV.C and Appendix A (pages 4–7)
- Problem: Ambiguity in “strict-superset subsample mask (n = 5,547,858, fsky = 0.659).” The variable n here is used as if it were the sample size, but Appendix A defines Nmap,weighted = ΣWp = 5,547,858, where Wp counts all galaxies (including non-spirals) per pixel. This is not the number of spirals used to construct Ap. This is potentially misleading in a headline result.
- Required fix: Replace “n = 5,547,858” in the abstract and elsewhere with an unambiguous label (e.g., Nmap,weighted = 5,547,858) and explicitly state in the abstract/body that the dipole estimator for chirality is constructed from spirals (Nspiral = 3,201,160) but weighted by total counts for depth (giving Nmap,weighted). Clarify the construction of the subsample mask and how it differs from the canonical mask.

P4-E5
- Location: Sec. IV.D and Appendix A (pages 4–7)
- Problem: The narrative surrounding monopole subtraction, MASTER deconvolution, and significance is confusing/internally inconsistent. Appendix A states: “Monopole subtraction reduces decoupled C1 … from 2.30×10−5 to 1.51×10−5 (~34%) and increases σ from +1.85 to +3.64 (the canonical-mask number).” Increasing significance despite decreasing C1 requires clear justification (null σ changes), but this contradicts the earlier statement “MASTER decoupling removes the canonical-mask pseudo-Cℓ leakage.” The canonical-mask residual is still quoted as +3.64σ post-MASTER, whereas the “headline” −0.122σ uses a different (subsample) mask. The logic chain is opaque.
- Required fix: Rewrite Sec. IV.D/Appendix A to: (i) clearly separate pre-MASTER vs post-MASTER, (ii) clearly separate canonical mask vs subsample mask, (iii) explicitly report the corresponding null means and σnull for both cases, (iv) explain why σ increases despite reduced C1 after monopole subtraction, and (v) justify how this supports the claim that “MASTER removes leakage” in one configuration but leaves a +3.64σ residual in another. A small schematic flow diagram of fields/masks/nulls would help.

P4-E6
- Location: Sec. VI.A (page 6)
- Problem: The derivation of the Fisher/Poisson “3σ sensitivity floor” and its connection to the empirical injection-recovery threshold is not internally consistent.
  - The text states: “Fisher Poisson floor at 3σ is ∼0.29% (from σ(A/2) ≈ 0.048% at Nspiral = 3,201,160, fsky = 0.46).” No derivation is shown; fsky=0.46 contradicts earlier fsky values (0.49005 or 0.659). The computation leading to 0.048% is not reproducible from given numbers.
  - The empirical threshold A=0.75% is quoted for the HC subset (N=471,049). The text attributes the excess above 0.29% “due to classification noise (GZ1-dilution factor ≈0.63, giving a true-underlying threshold ∼1.19%).” This mixes effects: sample-size reduction (3.20M→471k) and classification dilution. If you propagate both, the scaling should be explicit (e.g., 0.29% × sqrt(3.20M/0.471M) / 0.63 ≈ 1.20%), which does not match the 0.75% empirical value. Currently the explanation is self-contradictory and confounds map-based vs object-based Fisher estimates.
- Required fix: Provide a transparent derivation for the Fisher floor (clearly stating whether it is object-count limited or map-based with fsky and pixel thresholds), use a consistent fsky, and cleanly separate the effects of: (a) HC sample-size reduction, (b) classification dilution (0.6991 accuracy), and (c) any other penalties (edge-on contamination, etc.). Show that the 0.75% empirical threshold is consistent with this decomposition (or revise accordingly).

P4-E7
- Location: Table III (page 5)
- Problem: The bandpower “Significance (σ)” values appear arithmetically inconsistent with the displayed Cℓ and σnull (null means not shown). For example:
  - ℓeff=4: 3.210/0.804 ≈ 3.99, but table lists +6.097. 
  - ℓeff=9: −0.248/0.574 ≈ −0.43 in naive units; table lists +2.232. 
  - Similar issues for ℓeff=14,19,24. Without the null means, one cannot reconstruct the Δ/σnull values. The signs are also puzzling (negative Cℓ but positive “σ”).
- Required fix: Add the null means for each bandpower and explicitly define z = (Cmeas−⟨Cnull⟩)/σnull for each row. Ensure all listed significances numerically match that definition. If you are quoting |z| with a sign convention, state it and apply uniformly.

P4-E8
- Location: Multiple (pages 4–7, 8)
- Problem: Version-history/internal-draft phrasing appears in the body, e.g., Sec. IV.D: “were interpreted in earlier paper versions as …”. PRD policy requires removal of draft/version-history language in the final text.
- Required fix: Remove all version-history/internal-process language and write in a final, self-contained form.

MAJOR

P4-M1
- Location: Sec. III.A (page 3), Sec. IV (page 3–6)
- Problem: Although an “Analysis Hierarchy” is declared, the “subsample mask” that underpins the headline MASTER result is never formally defined in the Data/Methods section. The canonical vs subsample masks are inconsistently described and used throughout, with different fsky values and thresholds unevenly documented.
- Required fix: Add a subsection in Methods defining all masks (canonical, subsample, any apodization), their construction (pixel count thresholds, sky cuts), their fsky, and their intended use for each estimator. Ensure this definition is consistent across all occurrences.

P4-M2
- Location: Sec. IV.C “Simple dipole” (page 4)
- Problem: You quote +0.43σ with p = 0.30 (bootstrap NMC=10,000). A Gaussian 0.43σ corresponds to two-sided p ≈ 0.67. The bootstrap p = 0.30 implies a different mapping. Without reporting the test statistic and null distribution shape, the relation between σ and p is opaque.
- Required fix: Report the exact definition of the “σ” proxy used here (e.g., z from bootstrap mean/stdev) and present the empirical p-value alongside, stating that Gaussian p is not used. Alternatively, quote only the bootstrap p-value for this estimator to avoid confusion.

P4-M3
- Location: Sec. IV.D (page 4–5), Table IV (page 5)
- Problem: Table IV “Pre-MASTER pseudo-C(ℓ=1)ℓ” significance is given as +1.68σ from Data 1.696×10−2 and Null (1.685±0.007)×10−2. Δ = 0.011×10−2; σnull = 0.007×10−2; z ≈ 1.57, not 1.68. While small, these discrepancies recur (also in Table II).
- Required fix: Recompute and correct the z-values, including proper rounding. Provide numerical precision consistently.

P4-M4
- Location: Sec. VI.A (page 6), Appendix E (page 9)
- Problem: Edge-on contamination and classification dilution are acknowledged but only roughly quantified. The “10–15%” effective sample-size loss and “5–8% sensitivity penalty” need a reproducible calculation given to support the injection-recovery interpretation.
- Required fix: Provide the calculation or a short derivation linking the measured edge-on rates and classification behavior to the effective sample-size loss and sensitivity penalty, or else move these to a qualitative statement and avoid numerical claims that cannot be reproduced.

P4-M5
- Location: Sec. V.A (page 5), VII (page 6–7)
- Problem: The statement “inconsistent in amplitude with Shamir’s claimed ∼3% signal by a factor of ∼6–12 under the present pipeline” is undocumented. The paper’s empirical 50%-recovery-at-3σ is 0.75%; the factor vs 3% would be ≈4. If you intend to compare to an inferred amplitude from your real-space estimator, that amplitude is not reported.
- Required fix: Either (i) remove the “6–12” factor or (ii) show the amplitude basis and computation that yields this factor (with uncertainties). As written, it is unsupported.

P4-M6
- Location: Sec. IV.E and Appendix D (pages 5, 8–9)
- Problem: The canonical-mask residual (+3.64σ) is attributed to systematics with several diagnostics. However, the description mixes different nulls (permutation, density-stratified), weighs evidence qualitatively, and uses a small number of MC (often N=500), limiting the precision of σ/p. Some diagnostics (e.g., leg-proxy partial closure) would benefit from numeric error bars and null distributions.
- Required fix: For each diagnostic (cross-spectrum rℓ, density-stratified null, boundary-distance variance, WLS fit), report the null distribution and p-value/error bars, or provide a figure with uncertainty bands. This will make the systematic case quantitatively compelling.

P4-M7
- Location: Throughout (pages 1–7)
- Problem: The paper frequently juxtaposes σ from different null procedures (e.g., +0.43σ vs −0.122σ) without restating they are not directly comparable at each juxtaposition. You do include such a caveat in the abstract and at the start of Sec. IV, but later side-by-side mentions reappear without the reminder.
- Required fix: Whenever σ from distinct nulls are compared in the same sentence/paragraph, add a short parenthetical “(distinct nulls; not directly comparable)” or, better, lean on p-values or amplitude estimates to avoid misleading comparisons.

MINOR

P4-n1
- Location: Sec. IV.C (page 4)
- Problem: “pre-MASTER pseudo-Cℓ in the lowest bandpower—both entirely artifacts…” It would help to show a figure of the pseudo-Cℓ vs MASTER-deconvolved Cℓ to visually support this statement.
- Required fix: Add a small figure panel with pseudo- vs MASTER Cℓ for Catalog A/C to illustrate the collapse.

P4-n2
- Location: Appendix A (page 7)
- Problem: Notation “C 2 2° apodization” is unclear.
- Required fix: Specify the exact NaMaster apodization call/parameters (e.g., apodization type and FWHM in degrees) in standard notation.

P4-n3
- Location: Sec. II.B and Appendix B (pages 2–3,7)
- Problem: 67.6% of training labels are from CE-ResNet pseudo-labels. The split of CW/CCW/NS in training and any class rebalancing are not documented.
- Required fix: Provide class counts or weights used during training (and any rebalancing) to interpret the learned priors and the raw monopole in Catalog A.

P4-n4
- Location: Sec. III.C (page 3)
- Problem: The D4-TTA check is informative but cryptic (“argmax labels flip in 21.4%... sign-flip … confirms sample-noise…”).
- Required fix: Provide an explicit metric (e.g., per-galaxy mean |ΔpCW| over D4, or an inter-rotation consistency score) to quantify rotational equivariance stability.

P4-n5
- Location: Sec. IV.C (page 4)
- Problem: “Nside = 64 … ∼0.84 deg2 per pixel.” Good, but the cut “>10 spirals per pixel” should be justified against the noise floor and potential bias introduced by variable pixel selection.
- Required fix: Provide a short rationale (and perhaps a sensitivity test) for the >10 threshold; Appendix E.d suggests robustness, but a sentence in the main text would help.

P4-n6
- Location: Sec. I (page 2)
- Problem: The statement “We emphasize … ℓ=1 observable is parity-EVEN” is correct, but the paper sometimes refers to “parity analyses” for CW/CCW fractions without reiterating parity-even/odd distinctions.
- Required fix: Add a short clarifying sentence in Sec. VI.B to prevent misinterpretation (some readers equate chirality with parity-violation tests).

NITS

P4-N1
- Location: Page 1, line “471 049 high-confidence per-spiral after peq CW >0.9”
- Problem: Spacing/format: use thin space or comma formatting consistently (e.g., 471,049).
- Required fix: Standardize number formatting throughout.

P4-N2
- Location: Sec. V.B (page 5)
- Problem: “two pipelines are complementary” reads as borderline promotional.
- Required fix: Tone down to neutral comparison language.

P4-N3
- Location: Data availability (page 9)
- Problem: URLs broken across lines; ensure clickable links in final PDF or include DOIs where available.
- Required fix: Follow PRD style for links/DOIs.

P4-N4
- Location: Bibliography (pages 9–10)
- Problem: Check that all arXiv IDs and DOIs correspond to the cited year/journal (e.g., [3], [7], [9] formatting).
- Required fix: Verify and correct any mismatches per PRD style.

Additional comments on length and scope
- At 10 pages, the manuscript is not overly long for PRD. However, several sections (IV.D, Appendix A/D) should be reorganized for clarity (mask definitions, null choices, and step-by-step estimator logic). A schematic of the pipeline (fields → masks → estimators → nulls) would materially improve methodological transparency.

## Summary recommendation
MAJOR REVISIONS

The core scientific conclusion (no significant ℓ=1 chirality dipole on the broader subsample mask; real-space cross-check consistent with null; canonical-mask residual attributable to systematics) is potentially sound and interesting. However, the manuscript contains multiple essential methodological and numerical inconsistencies that must be corrected before PRD publication: wrong table cross-referencing in the abstract, inconsistent global fraction numbers/suppression factors, internal arithmetic issues in tables (especially Table III), ambiguous definitions of masks and “n,” and an unclear derivation connecting Fisher limits and injection-recovery. With these addressed and the systematic-case diagnostics reported with proper nulls and uncertainties, the paper could meet PRD methodology standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS

ESSENTIAL

P4-E9
- Location: Sec. IV.C (Eq. 3) vs Appendix A(a), “Field: scalar (spin-0) asymmetry map”
- Problem: In Sec. IV.C, Ap is defined as (NCW − NCCW)/(NCW + NCCW) using spirals only. In Appendix A, Ap is stated as (NCW − NCCW)/Ntotal, where Ntotal is implied to include NS (non-spirals). These are not equivalent and lead to different amplitudes, noise levels, and null variances. This is a fundamental inconsistency in the definition of the key field used in MASTER.
- Required fix: Use a single, explicit definition of Ap throughout (and state exactly which counts enter numerator and denominator). If the denominator differs between configurations, document both clearly and report how this changes ⟨Cnull⟩ and σnull. Recompute any affected results.

P4-E10
- Location: Abstract; Sec. IV.D; Appendix A
- Problem: The same canonical-mask post-MASTER residual is reported as “+3.64σ (z = Δ/σnull)” while the empirical rank pMC = 0.030 (≈ 1.9σ Gaussian-equivalent). Reporting both 3.64σ and 1.9σ for the same test without a clear explanation is contradictory. The abstract also calls the null a “binomial per-pixel-shuffle null,” conflating two distinct nulls used elsewhere (binomial generative vs permutation/label-shuffle).
- Required fix: State unambiguously which null defines z and which defines pMC for this exact result. If z is computed under a Gaussian proxy from the same null, report the corresponding p; if pMC is from a different null, say so explicitly and avoid calling both “σ” without qualification. Replace “binomial per-pixel-shuffle null” with the precise null procedure actually used for this residual.

P4-E11
- Location: Appendix A(a), “galaxy-weighted mask-mean subtraction ⟨A⟩mask,gw = −0.005294”
- Problem: ⟨A⟩mask,gw = −0.005294 implies 2(fCW − 0.5) ≈ −0.00529 → fCW ≈ 0.49735, which is close to Table II’s 0.4974, but the 2× scaling is never stated here. Combined with the Ap denominator conflict (P4-E9), this leaves it unclear whether the monopole subtraction is in Ap-units or in fCW-units, and whether NS are in the denominator.
- Required fix: State explicitly the unit of A used for monopole subtraction (Ap vs fCW − 0.5). If Ap is used, explain the factor-of-two mapping and why ⟨A⟩mask,gw matches the catalog’s global fraction despite different weights/denominators. Ensure Section IV and Appendix A use the same convention.

P4-E12
- Location: Sec. II.B (page 2) vs Data Availability (page 9)
- Problem: The GZ1 cross-match sample size is stated as 234,282 (Sec. II.B) and 240,919 (Data Availability), both with “69.91%” agreement. This is a stale-number inconsistency.
- Required fix: Report the correct cross-match N consistently in both places and verify any statistics that depend on it.

P4-E13
- Location: Sec. VI.A (page 6)
- Problem: The “GZ1-dilution factor ≈ 0.63” is inconsistent with the stated independent GZ1 agreement of 69.91%. Under symmetric mislabeling, the amplitude-dilution factor is g = 2a − 1, where a is accuracy; with a = 0.6991, g ≈ 0.398, not 0.63. Using 0.398 changes the “true-underlying threshold” from ~1.19% to ~1.9% when propagating sample-size and dilution (0.29% × sqrt[3.20M/0.471M] / 0.398 ≈ 1.9%).
- Required fix: Correct the dilution factor and re-derive the mapping from the empirical 0.75% observed threshold to the implied true-underlying amplitude. Update any text comparing to prior claims that uses the 1.19% number.

MAJOR

P4-M8
- Location: Table III (page 5) vs Appendix A(b,c)
- Problem: Binning inconsistency. Appendix A states single-ℓ bins (nlb=1), but Table III reports bandpowers over ranges (e.g., ℓ∈[2,6], [7,11], …). The joint χ2/dof is reported for 38 bandpowers, but only 5 are shown, and no binning configuration for those 38 is documented.
- Required fix: Document the exact binning used for Table III (and for the 38-bandpower χ2), including nlb and ℓ ranges, and ensure Appendix A records the configuration actually used for the bandpowers as presented.

P4-M9
- Location: Appendix A(c) vs Appendix D(a)
- Problem: Apodization inconsistency. Appendix A says no apodization on the canonical mask and C2 2° apodization on the subsample mask. Appendix D(a) then presents a “C2 2° apodization” test for the canonical mask, but the exact NaMaster parameters (type, scale) are not shown and appear to contradict Appendix A.
- Required fix: Specify the NaMaster apodization call and parameters for all masks tested (including the canonical-mask apodization test in Appendix D). Reconcile any conflicts with Appendix A and state which results correspond to which apodization settings.

P4-M10
- Location: Sec. III.C; Appendix B(d), T7 (Bias-hardening suite)
- Problem: Test T7 “confidence calibration (qualitative, < 50% at confidence > 0.9)” is unclear/misleading as a pass/fail criterion and is not a recognized calibration metric. Without a formal calibration curve or ECE/Brier score, the claim “PASS” is not interpretable.
- Required fix: Replace T7 with a standard calibration metric (e.g., ECE with binning scheme; reliability diagram) and report numerical values. If you intend a simple cap on the mass above a particular probability, define that metric precisely and justify the 50% threshold.

P4-M11
- Location: Sec. IV.C (page 4), “pre-MASTER pseudo-Cℓ in the lowest bandpower”
- Problem: “Lowest bandpower” is referenced for the raw Catalog A +6.48σ claim, but no binning/ℓ-range is specified, and there is no figure/table showing this pre- vs post-MASTER collapse. The absence of a precise ℓ-range and null makes the 6.48σ claim opaque.
- Required fix: Specify the exact ℓ-bin used for this “lowest bandpower” and the null procedure, or include a figure showing pseudo- vs MASTER Cℓ with uncertainties for Catalog A and C, as already suggested (P4-n1). Provide the corresponding p-value under the stated null.

MINOR

P4-n7
- Location: Abstract; Sec. IV.D; Table I (row iii)
- Problem: The language “binomial per-pixel-shuffle null” appears in the abstract, but Table I row (iii) lists “per-pixel-shuffle” as the null, while Sec. IV.D discusses a separate “monopole-only binomial generative null.” These are different nulls and should not be conflated.
- Required fix: Standardize terminology: “permutation (label-shuffle) null” vs “binomial generative null,” and apply consistently in text, tables, and abstract.

P4-n8
- Location: Sec. II.B and Appendix B(a)
- Problem: Training/validation metrics are reported, but class distributions (CW/CCW/NS) and any loss reweighting are still absent. Given that 67.6% of training labels come from pseudo-labels, readers need class counts/weights to interpret priors and the origin of the raw Catalog A monopole.
- Required fix: Add a small table (or sentence) with class counts in the training/validation sets and any class weights used in the loss.

P4-n9
- Location: Appendix C(d)
- Problem: The two-point correlation outlier at θ ≈ 0.5° (-2.41σ) is attributed to “brick-boundary” artifacts, but no quantitative check or uncertainty on the “brick-interior subsample” result (−0.03σ) is provided.
- Required fix: Provide the uncertainty on the brick-interior value and the corresponding null test to substantiate the claim that the outlier vanishes when removing boundary regions.

P4-n10
- Location: Sec. VII(b), item b; Sec. IV juxtaposition
- Problem: The text asserts that two estimators are “null” (0.43σ real-space; −0.122σ MASTER) alongside a “+3.64σ” canonical residual without restating that these σ’s come from distinct nulls and different masks, inviting misinterpretation.
- Required fix: When presenting these side-by-side, add a brief parenthetical reminder that these σ values derive from distinct null procedures and masks (and are not directly comparable), or present p-values consistently.

NITS

P4-N5
- Location: Appendix D(c)
- Problem: “The summed leg-induced ℓ = 1 amplitude is ∼25% of the observed canonical-mask ℓ = 1 amplitude” is stated without numbers or an uncertainty. As a nit, the qualitative point is fine, but a single numeric line (with error) would help.
- Required fix: Add the numerical amplitudes and an uncertainty estimate (and the null/MC used to get them).

P4-N6
- Location: Data Availability, Appendix B headers
- Problem: Minor typos and spacing (e.g., “dataset s/…”, “galaxy- chirality- catalog”, inconsistent en-dash/hyphen usage).
- Required fix: Clean up link spacing and hyphenation per PRD style so URLs are clickable and text is consistent.

Explanation
I focused on new issues not covered in the initial report. The most consequential are (i) the internal inconsistency in the Ap definition between the main text and Appendix A, (ii) the contradictory significance reporting for the canonical residual (3.64σ vs pMC=0.030), and (iii) the incorrect classification-dilution factor (0.63 vs 2a−1 ≈ 0.398). I also flagged binning/apodization configuration mismatches, a stale cross-match N, and several clarity/calibration gaps. These collectively affect methodological rigor and reproducibility.