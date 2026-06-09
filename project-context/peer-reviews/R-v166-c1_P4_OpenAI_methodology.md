# P4 R-v166-c1 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7873 chars)
**Wall time**: 286.7s

---

Referee report on “Survey-Scale Galaxy Chirality with Equivariant TTA …”

General scope of this review
I focused on methodology rigor, internal arithmetic and statistical consistency, estimator and null definitions, and whether the retraction of a previously reported subsample-mask MASTER null is handled completely and consistently. I audited all load‑bearing scalars in the abstract and conclusions against the body text, recomputed quoted σ, p-values, ratios, and percentages from the numbers shown, and checked figure/table consistency.

Findings

ESSENTIAL

P4-E1
Section: Abstract (page 1)
Problem: Version-history and review-log language appears in the abstract: “Withdrawal note: versions ≤1.0.165 of this paper reported a −0.122σ MASTER ℓ=1 null … it is withdrawn …”
Required fix: Remove version numbers and internal provenance language from the abstract. Replace with a concise, version-neutral statement in the body (e.g., Appendix) noting that an earlier analysis mistakenly used a synthetic footprint and has been corrected, or move the detailed provenance to a data-repository README. PRD papers should not include version identifiers or internal audit logs in the abstract.

P4-E2
Section: Appendix A, item d (page 11)
Problem: More version-history language: “Versions ≤1.0.165 of this paper reported … a June 2026 provenance audit found … Audit artifacts: pipelines/… .json”
Required fix: Remove all version identifiers (“≤1.0.165”), dates of internal audits, and “Artifact:” filesystem paths from the manuscript. Summarize the correction neutrally without internal bookkeeping; deposit full provenance in the code/data repository.

P4-E3
Section: Appendix A, item a (page 11)
Problem: Contradictory definition of the analysis field Ap. First it states “Field: … Ap = (NCW − NCCW)/N(p)total,” but earlier and elsewhere Ap is consistently defined on spirals only: Ap = (NCW − NCCW)/(NCW + NCCW).
Required fix: Make the definition unambiguous and consistent everywhere. If Ap is defined on spirals only, change N(p)total to Nspiral(p) here, and verify that all computations (NaMaster inputs, nulls, monopole subtraction) use the same definition. If a different field was used in any section, state it explicitly and motivate the choice.

P4-E4
Section: Figure 3 and Section IV.A (page 6)
Problem: In-text Catalog C composition states NCW = 1,592,107 (18.78%), NCCW = 1,609,053 (18.99%), NNS = 5,273,371 (62.23%), Ntotal = 8,474,531. However, the pie-chart labels in Fig. 3 appear to show different counts and percentages (e.g., “Not-Spiral 5,152,736 (60.8%)”, “CW 1,687,069 (19.9%)”, “CCW 1,634,726 (19.3%)”).
Required fix: Regenerate Fig. 3 from the stated Catalog C numbers or correct the caption to reflect the dataset actually plotted. All numbers and percentages in the figure must match the text and totals.

P4-E5
Section: Table II and surrounding text (pages 5–6)
Problem: Inconsistency between quoted “excess (%)”/deviations and the numbers in the table:
- Catalog C: cw fraction = 0.4974. Deviation from 0.5 is −0.0026. With σ = 0.000279 (as printed), |z| = 0.0026/0.000279 = 9.32σ, not 9.5σ as reported.
- Tier A: 0.5079 implies +0.0079, z ≈ 28.3σ, not 28.8σ.
- Tier B: 0.504 implies +0.0040, z ≈ 14.3σ, not 14.6σ.
Required fix: Recompute and correct the “Dev. (σ)” entries using the same σ that you print in the table. Also standardize the “Excess (%)” language: make explicit whether “%” means percentage points of the cw fraction (fCW − 0.5)×100 or the Ap mean (2fCW−1)×100. Keep these two distinct consistently across text, figures, and captions.

P4-E6
Section: Figure 2 caption (page 5) and Section IV.B (page 6)
Problem: Repeated use of inconsistent percentages: “global CW-fraction shift from +2.05% (A) to −0.53% (C)”. Table II lists 0.5079 (i.e., +0.79 percentage points) for A and 0.4974 (−0.26 percentage points) for C. An Ap monopole of −0.53% corresponds to fCW − 0.5 = −0.265 percentage points, not −0.53 percentage points. For A, 0.5079 implies Ap monopole of +1.58%, not +2.05%.
Required fix: Audit and correct all places where “2.05%” and “−0.53%” are used. If you intend to quote Ap mean (%) rather than percentage-point deviation in fCW, say so explicitly and ensure raw fraction numbers match the implied Ap values.

P4-E7
Section: Section IV.C, a. Simple dipole (page 6), Abstract (page 1), Conclusions (page 10)
Problem: Inconsistent mapping of “+0.43σ” and “p = 0.30” for the real-space dipole amplitude. A Gaussian two‑tailed p = 0.30 corresponds to |z| ≈ 1.04; one‑tailed p = 0.30 corresponds to z ≈ 0.52; neither matches 0.43. If “σ” is defined via Δ/σnull from a bootstrap, the corresponding empirical tail probability should be consistent.
Required fix: Report a single, self-consistent significance metric for the real-space dipole: either (i) z and two-tailed p from the bootstrap distribution of the amplitude, or (ii) empirical p only. If you also report a Gaussian-equivalent z, compute it from the reported p. Clarify whether the p is one‑ or two‑sided and whether the bootstrap distribution is amplitude-only (non-negative) or signed.

P4-E8
Section: Table I (page 4)
Problem: The primary “real-space dipole” estimator row shows fsky and Mask as “—” / “none,” yet in Sec. IV.C you apply NSIDE=64 with a per-pixel threshold (>10 spirals), which is a mask implying fsky < 1.
Required fix: Specify the actual mask used and its fsky for the real-space dipole estimator in Table I. If weighting was applied, state it (and whether weights enter the fit). The table of headline estimators must be internally complete and consistent.

P4-E9
Section: Table I (page 4) and Appendix C (page 12)
Problem: Hemispheric “max-stat MC pLEE ≤ 10−4” appears in Table I, yet Appendix C states that, after Bonferroni/BH correction over ~650 directions, “post-LEE significance drops below |σ| < 1.” By definition pLEE should be the look-elsewhere corrected p-value, not the raw permutation null without LEE correction.
Required fix: Define pLEE precisely and report the look-elsewhere corrected p-value in Table I. If the ≤10−4 refers to an uncorrected permutation p, rename it accordingly (e.g., “max-stat raw p”). Provide the corrected p in the main text and the table to avoid contradictory conclusions.

P4-E10
Section: Throughout, especially Abstract (page 1) and Sec. IV.D (pages 6–8)
Problem: Two incompatible “σ” figures are juxtaposed for the same object: e.g., “post‑MASTER canonical-mask direct‑MC residual is +3.64σ (z = Δ/σnull) … empirical rank pMC = 0.030, i.e. ≈ 1.9σ Gaussian‑equivalent.” This risks reader confusion.
Required fix: When you report both a standardized residual (Δ/σnull) and an empirical rank p, clearly label the former as a standardized score and convert the empirical rank to a Gaussian z using a stated convention (one- or two‑sided). Do not call both of them “σ” without qualifiers. Prefer reporting Δ/σnull and pMC, and only add a “Gaussian-equivalent” z if you explicitly define the mapping.

MAJOR

P4-M1
Section: Methods III.A and IV.C (pages 3, 6)
Problem: The “real-space dipole” estimator is not specified with sufficient mathematical detail. You define Ap per pixel, but not the fitting procedure for the dipole: objective function, weights, treatment of incomplete sky, and whether the fit is to Y1m coefficients or a directional regression.
Required fix: Provide an explicit estimator definition: e.g., minimize Σp wp [Ap − (Ad n̂·p̂)]^2 with specified weights wp and pixel selection; or equivalently the map-to-harmonics projection and how the amplitude is formed from the a1m. Include details needed to reproduce the 0.43σ result.

P4-M2
Section: IV.C (page 6)
Problem: Isotropic-null bootstrap procedure is insufficiently specified. Only NMC = 10,000 is given.
Required fix: Describe the bootstrap in detail: what is resampled (galaxy labels within pixels, pixel values, or sky rotations), how directional information is randomized, treatment of the mask, and the definition of the bootstrap test statistic. Provide sufficient information for independent reproduction.

P4-M3
Section: VI.A and Abstract/Conclusions (pages 9–10, 1)
Problem: “Falsification criterion A95 ≈ 1.5–2%” and “A50 ≈ 0.75%” are central sensitivity statements but no figure/table shows Pdet(>3σ | A) vs A nor the definition of A95 beyond prose.
Required fix: Add an injection-recovery figure/table showing the detection probability vs injected amplitude under the stated null (with confidence intervals), and define precisely how A50 and A95 are computed (e.g., empirical fraction of runs with σ > 3). Include the impact of classification noise and sample selection on these curves.

P4-M4
Section: Appendix D, item f (pages 12–13); Abstract/Conclusions (pages 1, 10)
Problem: The block-bootstrap WLS template fit is load-bearing for disfavoring a clean 1.7% dipole (quoted z ≈ −18), but methodological details are insufficient: design matrix elements, weighting scheme, block definition for the bootstrap, number of blocks, and how you form the dipole amplitude parameter in the regression.
Required fix: Provide a formal specification of the regression model, list all templates, define the blocks (e.g., NSIDE=8 HEALPix patches), show the posterior/uncertainty for the dipole amplitude both naive and block‑bootstrap, and include a sanity-check (e.g., recovery on injections). A small table or figure would suffice.

P4-M5
Section: Table III and text (page 7)
Problem: Table III lists several negative Cℓ bandpowers with positive “Significance (σ)” values (+2.232, +2.626, +2.229…). If “Significance” is defined as (Cℓ−⟨Cℓ⟩null)/σnull, the sign should be negative when Cℓ < ⟨Cℓ⟩null.
Required fix: Define the sign convention for the reported “Significance (σ)” explicitly. If you are quoting absolute deviations, indicate this (“|z|”). Otherwise, correct the signs.

P4-M6
Section: Bias hardening suite, Appendix B.d and Table V (pages 11–12)
Problem: Several tests are stated qualitatively or with unclear thresholds/metrics (e.g., “T7: Calibration qualitative PASS; T8: CW/CCW balance 50 ± 10% 49.7%”). For T7 in particular, no calibration metric (ECE, Brier, reliability diagram slope) is provided.
Required fix: Quantify the calibration test (e.g., expected calibration error across bins) and report a scalar measure with uncertainty. For T8, specify whether this is global fCW or Ap monopole and clarify how the ±10% tolerance relates to your sub‑percent sensitivity needs.

P4-M7
Section: Training labels (page 3)
Problem: 67.6% of training labels derive from CE‑ResNet predictions. While you include an independent GZ1 cross‑match (234,282 galaxies; 69.91% accuracy), you do not describe the selection of this cross‑match (confidence thresholds, overlap removal) or provide a confusion matrix.
Required fix: Add details on the GZ1 cross‑match procedure, confidence criteria for “ground truth,” and provide a confusion matrix (or at least per‑class precision/recall) to support the stated 69.91% accuracy and κ = 0.40.

P4-M8
Section: Sec. IV.C and Table I (pages 6 and 4)
Problem: Multiple mask variants and thresholds are used (canonical mask Nspiral ≥ 5, apodized footprint Nall ≥ 1, real-space pixel cut > 10 spirals). The mapping of each estimator to its specific pixel threshold/mask is not always explicit in the corresponding result statement.
Required fix: For each estimator in Table I and the text, list the exact pixel threshold and mask used. Consider adding a short subsection or table enumerating mask definitions and thresholds.

MINOR

P4-m1
Section: Appendix A, item a (page 11)
Problem: Monopole subtraction note states it “increases σ from +1.85 to +3.64,” while simultaneously reducing C1. This is presumably because σ refers to (Δ/σnull) with a larger σnull under the no-subtraction null. As written it is confusing.
Required fix: Clarify that the “σ” refers to standardized deviation relative to a different null (with/without monopole subtraction), and thus is not directly comparable. Spell this out.

P4-m2
Section: Use of seeds and file paths (Appendix A and elsewhere)
Problem: Reproducibility is welcome, but in‑paper “numpy.random.seed(42)” and “Artifact: pipelines/…” lines are atypical for PRD.
Required fix: Keep such details in the code repository’s README or a Data Availability supplement; remove from the main text.

P4-m3
Section: Bibliography (page 14–15)
Problem: You still list “PACS numbers,” which PRD no longer uses; PRD typically uses keywords.
Required fix: Replace PACS with appropriate keywords per PRD style or remove.

P4-m4
Section: Figure 2 (page 5)
Problem: The caption labels “Test-time D4 equivariant averaging (TTA)” but the production Catalog C uses 2‑fold (Z2) TTA; the figure itself depicts D4 transforms.
Required fix: Make clear in the caption that D4 is shown for diagnostic validation, while the production classifier uses Z2 flips; avoid implying D4 is used for Catalog C.

P4-m5
Section: Several places (e.g., Sec. VI Discussion, Appendix C)
Problem: Occasional informal phrasing (e.g., “We classify as a documented systematic-floor artifact”) and long footnotes impede clarity.
Required fix: Tighten language to PRD style; move long explanatory notes into main text or supplementary information.

NITS

P4-n1
Section: Minor typographical issues (scattered)
Problem: Occasional spacing issues around symbols (e.g., “C 2 2◦”) and hyphenation inconsistencies (“apodized-footprint MASTER diagnostic” vs “apodized MASTER”).
Required fix: Uniformize formatting (C2 2° or C2 with 2° apodization), check hyphenation.

P4-n2
Section: Page 10
Problem: “We urge all future chirality studies to adopt comparable bias controls.” Advocacy tone is stronger than necessary.
Required fix: Soften to a neutral recommendation.

Completeness of the retraction handling
The paper clearly states that the earlier subsample-mask null was withdrawn and provides a provenance explanation. However, version numbers and internal file-path “Artifact” notes are left in the abstract and Appendix; these must be removed or moved to supplementary material. I saw no remaining scientific claim that depends on the withdrawn number; the main conclusions are anchored on the real-space dipole null and the WLS template-fit result.

Length
Given the methodological focus and the number of diagnostics, 15 pages including appendices is acceptable for PRD. Nevertheless, some material currently in footnotes and provenance notes should be moved to the data/code repository or a succinct supplementary section.

## Summary recommendation
MAJOR REVISIONS

The central scientific conclusion (a null real-space chirality dipole and a quantifiable monopole–mask leakage channel) appears sound and is supported by multiple estimators. However, the manuscript has several essential arithmetic and reporting inconsistencies (conflicting percentages and σ, contradictory definition of Ap in Appendix A), lingering version-history/provenance language inappropriate for PRD, and insufficient methodological detail on the primary real-space estimator, the isotropic-null bootstrap, and the block‑bootstrap template fit that underpins one of the key claims. These issues are fixable but must be addressed comprehensively before the paper can be considered for publication in PRD.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS (fresh-read audit)

ESSENTIAL

P4-E11
Section: Abstract; Sec. VI.A; Fig. 6
Problem: The abstract cites “471,049 high-confidence per-spiral after peq_CW > 0.9.” Elsewhere the HC cuts used for diagnostics are peq > 0.6 (N = 949,584) and peq > 0.8 (N = 624,660), and Fig. 6 does not mark a >0.9 cut. Using a class-specific threshold (peq_CW > 0.9) is asymmetric vs CCW and inconsistent with the later “HC-spiral subsample (N = 471,049)” that lacks a threshold definition.
Required fix: Define the HC subsample used for injection-recovery explicitly and symmetrically: e.g., max(peq_CW, peq_CCW) > 0.9. Add this cut to Fig. 6 and ensure the abstract, Sec. VI.A, and Fig. 6 all quote the same N and criterion.

P4-E12
Section: Sec. IV.D; Table IV; Appendix C
Problem: Hemisphere max-asymmetry significance is inconsistent: main text says 3.05σ; Table IV (monopole+mask null) reports z = +4.42 for the same statistic. The search grid is also described both as “all hemisphere-pairs at 10° increments” and “NSIDEdir = 8,” implying different numbers of tested directions.
Required fix: Specify a single hemisphere scan procedure (axis grid and number of directions), and report one pair of numbers per null (mean, σ, z). Reconcile 3.05σ vs 4.42σ by stating which null each uses (label-shuffle vs monopole-only). If you use a max-statistic permutation null, do not additionally apply Bonferroni/BH.

P4-E13
Section: Fig. 5 caption; Appendix A.c
Problem: Contradictory canonical-mask pixel thresholds: Fig. 5 says the canonical mask requires Nspiral(p) ≥ 5; Appendix A.c says “canonical Catalog C mask (pixels with ≥ 10 spirals).”
Required fix: Choose one threshold for the canonical mask, state it consistently across text, figures, and Appendix A, and update any fsky and results that depend on it.

P4-E14
Section: Appendix A.a–c; throughout where fields are defined
Problem: Field inconsistency and factor-of-two ambiguity. Appendix A.a says the data vector for NaMaster is fCW(n̂) − 0.5; A.c defines the field as Ap = (NCW − NCCW)/Ntotal. Elsewhere Ap is defined on spirals and Ap = 2(fCW − 0.5). Mixing these without an explicit mapping risks factor-of-two and denominator errors when comparing Cℓ and amplitudes.
Required fix: Declare a single canonical field and its denominator. Where an alternate field is used (fCW − 0.5 vs Ap), add the exact conversion (including the factor of 2 and the denominator choice) and ensure all quoted Cℓ and amplitudes are referenced to the same convention.

P4-E15
Section: Table IV
Problem: z for pre-MASTER pseudo-C(ℓ=1)ℓ is listed as +1.68 from Data 1.696×10−2 and Null (1.685 ± 0.007)×10−2. Using the printed values gives z = (1.696 − 1.685)/0.007 ≈ 1.57, not 1.68.
Required fix: Recompute z from the printed mean and σ, or correct the printed σ to match the stated z.

P4-E16
Section: Abstract vs. body (Secs. IV.C–IV.D; Table III)
Problem: The abstract states “MASTER … removes the leakage,” but multiple passages report non‑zero post‑MASTER residuals (+3.64σ canonical; +7.28σ on the apodized footprint).
Required fix: Soften the abstract to “substantially reduces” or similar, and ensure wording is consistent with the body.

P4-E17
Section: Sec. VI.A
Problem: The Fisher/Poisson sensitivity floor derivation uses σ(A/2) ≈ 0.048% leading to a 3σ full-amplitude ≈ 0.29%. This is not reconciled with the earlier binomial σ = 0.000279 (0.0279%) for fCW. Applying a simple fsky factor still does not land at 0.048%.
Required fix: Show the derivation of 0.048% explicitly (including fsky, pixel cuts, weighting, and any map-level factors), or correct the number and dependent 0.29%.

P4-E18
Section: Appendix A.c; Appendix D.a
Problem: Inconsistent apodized sky fractions: Appendix D.a states fsky = 0.482 with C2 2° apodization for the canonical mask; Appendix A.c lists “Effective sky fractions” including 0.488 for “binary, apodized” (and different feff,sky for weighted masks). It’s unclear which figure matches which mask/weight definition.
Required fix: Provide both the geometric fsky and feff,sky for each mask/weight combination in a single table, and reference the correct one wherever used.

P4-E19
Section: Appendix C; Table I
Problem: The reported “family-corrected p-value 0.0086 (≈ 2.4σ)” for the per-leg × confidence-bin scan lacks sidedness and correction-method detail. The sigma-equivalent of p = 0.0086 is ≈2.4σ one‑sided but ≈2.6σ two‑sided; the text also mentions a “15‑cell joint label‑shuffle max-statistic null,” potentially making the subsequent Bonferroni/BH comment redundant.
Required fix: State one- vs two-sided p, specify whether the correction is via max-statistic permutation, Bonferroni, or BH, and avoid double correction. Report the corrected p and corresponding Gaussian-equivalent z consistently.

MAJOR

P4-M9
Section: Throughout; especially Appendix D.f and Conclusions
Problem: The “z” used to disfavor A = 1.7% is nonstandard (z ≈ −264.5 naive; zboot ≈ −18) and its definition is not given. Negative sign and extreme magnitudes are confusing, and no p-value is reported.
Required fix: Define z precisely (e.g., (Abest − Aref)/σ), state sidedness, and provide the corresponding p-value. Consider presenting a more standard test: e.g., the posterior on Adipole with Aref marked, or the fraction of bootstrap fits with Adipole ≥ Aref.

P4-M10
Section: Comparison with previous work, Sec. V.A
Problem: “30× extension” is attributed while citing Iye et al. (∼80,000 spirals). 3.2×10^6 / 8×10^4 ≈ 40×, not 30×. If the baseline is Shamir’s 127k, the factor is ≈ 25×–32× depending on the sample referenced.
Required fix: Correct the multiplier and make explicit which prior dataset is used as the baseline for the claimed extension.

MINOR

P4-m6
Section: Model naming (Sec. III.B; Fig. 1 caption; elsewhere)
Problem: Inconsistent model name renderings: “ViT-Small,” “vit small patch16 224,” and “V iT − Small-Small.”
Required fix: Standardize to a single, precise model name (e.g., “ViT-Small (patch16/224)”) throughout.

P4-m7
Section: Table I, row (iv)
Problem: Two σ values are shown separated by a slash but the row itself doesn’t indicate which null each corresponds to (the explanation is only in the caption/body).
Required fix: Add an inline note in the row or a column label indicating “σ vs global-shuffle / depth‑stratified.”

P4-m8
Section: Appendix A.a captions/labels; Fig. 8 caption
Problem: Mixed use of “CW-deficit map fCW − 0.5” and “Ap” without a reminder of the relation risks factor-of-two confusion.
Required fix: Add a parenthetical once where both are shown: “Ap = 2(fCW − 0.5) on spirals.”

P4-m9
Section: Minor arithmetic/citation phrasing (Sec. V.A)
Problem: Baseline comparison mixes “SDSS-class samples” while quantifying multipliers against Iye et al. Clarify baseline to prevent ambiguity.
Required fix: State explicitly whether the multiplier references Iye et al.’s 80k or Shamir’s 127k, and adjust numbers accordingly.

NITS

P4-n3
Section: Appendix A.a
Problem: ⟨A⟩mask,gw = −0.005294 corresponds to fCW = 0.497353, while text elsewhere rounds to 0.4974; minor rounding drift.
Required fix: Round consistently to the same number of significant figures.

P4-n4
Section: Typographic consistency
Problem: Continued inconsistencies in “C 2 2° / C^2 2°” and em‑dash spacing, plus mixed UK/US style.
Required fix: Standardize notation and style per PRD guidelines.

Explanation
I focused this pass on inconsistencies that were not called out previously: contradictory mask thresholds, hemisphere-statistic definitions and z-values, field/normalization mismatches between fCW − 0.5 and Ap, a likely arithmetic slip in Table IV, abstract overstatement about MASTER removing leakage, the unexplained 0.048% sensitivity component, inconsistent apodized fsky reporting, unclear multiple-testing corrections, and a few residual scale/novelty and naming/style issues.