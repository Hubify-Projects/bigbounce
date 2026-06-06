# P5 auto-2026-06-06_0004pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6748 chars)
**Wall time**: 298.3s

---

Referee report on “Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with V-Web Cross-Check Across 791,635 DR1 Matched Spirals”

General scope
I reviewed all 20 pages, figures, equations, tables, and the abstract. Below I list all methodological/statistical issues found, with recomputations of quoted statistics where possible. I classify each item per the requested scale.

ESSENTIAL findings (must be fixed before PRD publication)

P5-E1
- Location: §VII, page 9–10, Phase 2 sensitivity sweep (paragraph beginning “The largest single-cell |σfrom half| across the entire sweep is 11.32 … n = 3,696,152”)
- Problem: Inconsistent sample size and statistic definition. You report |σfrom half| = 11.32 “(filament … n = 3,696,152)”. The chirality-labeled sample never exceeds 791,635. A σfrom half requires CW/CCW labels; the 3,696,152 figure must be from the DR1 parent (unlabeled) sample. The sentence also flips between “observed” and “predicted” language, making it unclear whether 11.32 was computed from data or from the monopole formula.
- Required fix: Remove any “observed” σfrom half claims that use N beyond the chirality-labeled sample. If the 11.32 value is a pure prediction (σpred = 2ΔfCW√N), state it explicitly as a prediction and compute it with the correct N for the chirality-labeled subset in that cell. Alternatively, if presenting a sanity check on the parent DR1 sample, rephrase to note that σ is undefined without labels and do not call it σfrom half. Provide corrected numbers and a clear separation between measured σ and predicted σ.

P5-E2
- Location: §XI, page 17, “Systematics and null tests” (last sentence of paragraph)
- Problem: Internal contradiction with earlier results. You state: “target-class split (BGS vs. LRG-ELG-QSO) with BGS-only CW fraction within ±0.001 of LRG-ELG-QSO.” Earlier (§VI D, p. 7) you report bright vs dark fCW = 0.4970 vs 0.5051 on n = 775,760 vs 14,782, a difference of ≈ 0.0081, i.e., 8.1× larger than 0.001.
- Required fix: Reconcile this contradiction. If §XI intended to describe a different split or a monopole-subtracted comparison, specify precisely and provide the corresponding values (and whether monopole-subtracted or not). Otherwise, correct §XI to reflect the measured 0.0081 difference and update any conclusions predicated on the ±0.001 assertion.

P5-E3
- Location: §VIII B, page 11, DESIVAST-anchored void classifier (KDTree step)
- Problem: Potentially unsafe point-in-sphere membership algorithm and inconsistent “maximum hole radius.” You perform a k = 20 nearest-neighbour KDTree query against VoidFinder hole centers, asserting it is “sufficient given the 24 Mpc/h maximum hole radius.” Elsewhere you quote maximal effective radii of 10–32 Mpc/h for “maximal voids” (§VIII E) and up to 55.9 Mpc/h for V2-VIDE (§VIII C). Using a fixed-k nearest-neighbour query is not equivalent to a guaranteed ball search of radius Rmax; it can miss covering spheres if the 21st (or later) nearest center lies just beyond the 20th distance but has a large radius that still covers the point. The stated “24 Mpc/h maximum hole radius” conflicts with other reported maxima.
- Required fix: Replace the k-NN approximation with a provably complete query for all hole centers within the true maximum effective radius for the algorithm in question (VoidFinder, V2-REVOLVER, V2-VIDE separately). Implement a radius (ball) query using Rmax equal to the catalog’s actual max effective radius and confirm by a brute-force subset check. Report the actual Rmax used for each algorithm, cite the source in the DESIVAST release, and re-run the void membership and Table VII/VIII if any memberships change. State the fraction of galaxies whose membership flips under the corrected method.

P5-E4
- Location: §V B, page 5, “Multiplicity bookkeeping” (Bonferroni threshold)
- Problem: Miscomputed Bonferroni threshold. You write: “Treating the five DESIVAST estimators as a Bonferroni-5 family at α = 0.05, the per-test threshold is |σ|Bonf ≈ 2.81.” For a family-wise α = 0.05 and K = 5 independent tests, the two-sided per-test α is 0.01, giving the Gaussian threshold z ≈ 2.576, not 2.81. Your own Eq. (2) would yield |σ|Bonf = √2 erfc−1(α/K) = √2 erfc−1(0.01) ≈ 2.576.
- Required fix: Correct the threshold to 2.576 (or, if you intended a different family-wise α or a max-statistic threshold rather than per-test threshold, state that explicitly and compute accordingly). Revisit any statements about “no DESIVAST estimator crosses it.”

MAJOR findings (significant revision required)

P5-M1
- Location: Abstract and throughout (primary/secondary analysis designation), §V B, page 5
- Problem: Primary estimator declared post hoc; garden-of-forking-paths risk. You acknowledge no pre-registered plan and designate the DESIVAST-based analysis post hoc as “primary.” While you discuss multiplicity within DESIVAST (five effective primary-class statistics), you explicitly exclude the other environment classifiers and stratifications from the “headline” family, despite extensive on-the-fly choices and diagnostics.
- Required fix: Provide a transparent multiplicity control that includes all environment-classifier choices relevant to the headline claim, or strictly limit headline claims to the DESIVAST analyses with a clear statement that all other analyses are exploratory/diagnostic and not used to support the main conclusion. Alternatively, predefine and justify a hierarchical testing plan that controls the FWER/FDR for the entire analysis tree. Make the statistical decision rule explicit.

P5-M2
- Location: §VIII B vs §VIII E, pages 11–12
- Problem: Inconsistent statements about “maximum hole radius.” In §VIII B you assert a 24 Mpc/h maximum hole radius for the DESIVAST VoidFinder holes; in §VIII E you report maximal-void effective radii spanning 10–32 Mpc/h; in §VIII C you report V2-VIDE maxima of 55.9 Mpc/h. These numbers are not reconciled by algorithm, and the 24 Mpc/h figure conflicts with the later 32 Mpc/h statement.
- Required fix: Provide the exact maximum effective radius per algorithm (VoidFinder, V2-REVOLVER, V2-VIDE) from the DESIVAST release and use those values consistently in all algorithmic steps (KDTree/ball search). Correct the text and any downstream computations if needed.

P5-M3
- Location: Data/code availability, Appendix B, p. 19; multiple places reference “companion data repository”
- Problem: Reproducibility not verifiable from manuscript. The paper repeatedly refers to a “companion data repository” and analysis drivers/configs, but no URL/DOI is provided. PRD requires that load-bearing computations be reproducible.
- Required fix: Provide persistent DOIs/URLs (Zenodo/GitHub tag/OSF or journal’s SDC) for the repository with exact scripts, configuration files, and the inputs used to generate every figure/table/number quoted. Include the exact commit hash or tag in the manuscript.

P5-M4
- Location: §VI A, page 5, “σpred(filament)≈ −3.16”
- Problem: Numerical inconsistency in predicted σ from the Paper IV monopole. For filament N = 408,187 and Δf = −0.0026, σpred = 2Δf√N = −0.0052 × √408,187 ≈ −3.32, not −3.16. Cluster’s −3.28 is correct.
- Required fix: Correct σpred(filament) to ≈ −3.32 (or state the exact Δf used if it differs from −0.0026 and recompute both predictions consistently).

P5-M5
- Location: §VI B, page 6, “logistic regression” sentence
- Problem: Insufficient reporting for the regression result (“a z-coefficient of 0.0059 with no significant intercept (0.000652)”). No standard errors or p-values are given; variables are not standardized; the interpretation is ambiguous.
- Required fix: Report coefficient estimates with standard errors, z/t statistics, and p-values; specify whether features were standardized; clarify the link function and whether clustering/robust errors were used given sky correlations. Otherwise, remove the regression claim and rely on the permutation result (p = 0.372).

MINOR findings (address, paper can proceed)

P5-m1
- Location: §VI C and Table III, page 6–7
- Problem: Wording could better distinguish the observed σ from the “Paper IV-monopole prediction” σpred to avoid implying they come from the same null. The figure caption already helps, but the text blends them.
- Required fix: Add an explicit sentence that σobs (binomial deviation) and σpred (catalog-monopole expectation) are different benchmarks and not from the same null distribution; the comparison is purely to assess consistency with the known catalog monopole.

P5-m2
- Location: §V A, Eq. (2), page 4
- Problem: The Bonferroni formula as written is acceptable, but where you later use “parametric Bonferroni” thresholds for maximum-absolute-σ statistics (e.g., in Table V context), it would be clearer to distinguish per-test z-thresholds from max-stat thresholds.
- Required fix: Insert a clarifying sentence in §V A that your Eq. (2) is applied as a per-bin two-sided Gaussian threshold (not a max-stat threshold), and that you also compute an empirical max-statistic LEE p-value via permutations as the primary control.

P5-m3
- Location: §VIII A, page 10–11
- Problem: The “0/6” V-Web-void inside DESIVAST holes check is extremely underpowered and could be misread as a rate estimate.
- Required fix: Add a sentence explicitly noting that n = 6 is too small to estimate a concordance rate and that this check is purely illustrative, not inferential.

P5-m4
- Location: §IX A, page 13–16 (Tempel cross-validation)
- Problem: The mapping “isolated→void”, “small group→wall”, etc., is a heuristic. You note this, but the text implies concordance at 0.026 pp only at filament/filament-like.
- Required fix: Retain the mapping caveat prominently in the caption (Fig. 7) to avoid overinterpretation of lower-N class differences.

NITs (cosmetic/editorial)

P5-n1
- Location: Throughout, e.g., Fig. 1 caption, text
- Problem: Superscripts like “2563” should be typeset as 256^3; several instances use plain text.
- Required fix: Typeset exponents properly.

P5-n2
- Location: Several places
- Problem: Occasional typography (“σfrom half”) appears without math formatting.
- Required fix: Use math mode consistently.

P5-n3
- Location: §VIII E, p. 12
- Problem: Phrase “−4.75σ … is consistent with the imaging-leg systematic … at the ∼1σ level” could be misread.
- Required fix: Clarify that “the residual after subtracting the catalog monopole is −1.55σ,” to make the logic explicit.

P5-n4
- Location: §IX B, p. 15
- Problem: “p < 10−1000” is rhetorically extreme.
- Required fix: Report as “p < 10−300” or simply “p ≪ 10−10” to avoid implying numerical precision beyond double precision.

Arithmetic and internal-consistency spot checks (selected)
- Table I sums check: CW + CCW + NS = 2,232,212; SPECTYPE sums and imaging-leg sums also match. OK.
- Table II σ recomputations: void −0.68, wall +0.56, filament ≈ −2.55 (reported −2.61), cluster −4.67. Within rounding (except filament σpred discrepancy flagged above).
- Density quintiles: N = 158,327 per bin; predicted |σpred| = 2×0.0026×√158,327 ≈ 2.07; observed max |σ| = 3.94; residual 1.87 as stated. OK.
- HEALPix Table V: NSIDE=16/32/64 p-values 0.607/0.135/0.413 consistent with figure captions. OK.
- DESIVAST void vs non-void (Table VII): ΔfCW = 0.0007 as stated; σ scale difference between classes matches sample size ratio. OK.
- DESIVAST three-algorithm (Table VIII): V2-REVOLVER and VIDE values internally consistent; catalog-native zone memberships reduce |σ| as claimed (spheres to catalog-native deltas ≈ 16–17k). OK.
- P5 monopole: for n = 791,635 and f = 0.4972, σ ≈ −4.99 as reported. OK.
- Two-sample bright/dark (filament class) z ≈ 3.39 computed from provided Ns and σ signs; consistent with “≈ 3.4σ.” OK.

Length/contribution
The manuscript is long (20 pages) for a null-result methodological test. The core contribution (DESIVAST-anchored void/non-void ΔfCW ≈ 7×10−4 with three void finders; V-Web sensitivity sweep shows ≤ 0.22 pp inter-class range) could be presented in a shorter paper. I recommend condensing to 12–14 pages by moving secondary diagnostics (e.g., some sky maps and descriptive HEALPix scans) and the toy EFT appendix to the Supplementary Material.

## Summary recommendation
MAJOR REVISIONS

The paper presents a carefully designed set of null tests and cross-validations, and most headline scalars are arithmetically consistent. However, there are several critical methodological issues that must be corrected for PRD standards: an internally inconsistent and likely incorrect Phase 2 “largest σ” claim using an unlabeled N; a contradiction in target-class split results; an unsafe void-membership algorithm with inconsistent maximum radii; and a miscomputed Bonferroni threshold. In addition, reproducibility requires a concrete, citable code/data repository. Once these are addressed, the remaining issues are mostly clarifications and minor numerical fixes.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS AFTER SECOND-PASS AUDIT

P5-E5
- Location: Abstract; §VI D (c), page 7
- Problem: Impossible dark-sample count. You state “filament class: bright −2.80 vs dark +2.85 … where the dark sample n = 21,203 is large enough to test.” Earlier in the same section you report the full matched-spiral dark sample size as n = 14,782 (and bright n = 775,760), and the four-program totals sum exactly to 791,635. It is not possible for the filament-class dark subsample to exceed the catalog-wide dark total.
- Required fix: Correct the filament-class dark n (and any derived statistics that used it) and scrub the abstract/body for this number. Recompute the bright-vs-dark two-sample z where needed and update any text that invokes the “n = 21,203” statement.

P5-M5
- Location: §VIII F, §VI C, Table III; generally wherever σobs is compared to σpred
- Problem: Monopole uncertainty not propagated. Comparisons of σobs to σpred treat σpred = 2Δf√N as fixed, but Paper IV quotes fCW = 0.4974 ± 0.000279, implying σ(Δf) ≈ 2.79×10−4. This contributes non-negligible extra variance to σpred: e.g., for N ≈ 1.58×10^5 (density quintiles), σ(σpred) = 2√N·σ(Δf) ≈ 0.22; for N ≈ 4×10^5, ≈ 0.35. All “|σobs − σpred|” tests implicitly assume Var(σpred)=0.
- Required fix: Propagate σ(Δf) into the null for σobs − σpred (use Var = 1 + [2√N·σ(Δf)]^2 under the monopole-only model), and update the residual significances and any Bonferroni/LEE statements that relied on the uncorrected residuals.

P5-M6
- Location: §IV A (steps 8–11), §VII (Phase 2 sweep)
- Problem: Missing normalization/units for tidal-tensor eigenvalues while using nonzero λth. You set Φ(k) = −δk/k^2 and Tij(k) = kikjΦ(k) but do not state the normalization convention (e.g., ∇^2Φ = δ vs ∇^2Φ = 4πG a^2 ρ̄ δ). With λth swept over {0, 0.1, 0.3}, the physical meaning of a fixed threshold depends on the chosen normalization. As written, the eigenvalues’ units are ambiguous, so λth ≠ 0 thresholds are not interpretable or comparable across Rs.
- Required fix: Specify the exact normalization (Poisson convention, factors of a, H0, 4πG, and grid/window normalization) so λ has defined units. Confirm that λth values are meaningful in those units and that cross-Rs comparisons are valid, or restrict conclusions to λth = 0 where only signs matter.

P5-M7
- Location: §IV A step 12 vs §VI D/Table IV
- Problem: Density variable inconsistency. Step 12 says you interpolate “smoothed log density” to galaxies. In §VI D/Table IV, the density quartiles are reported in terms of “ȓ” with values ≈ 0.9–2.21, which looks like ρ/ρ̄ (linear density), not log density.
- Required fix: Clarify exactly what scalar was used for the density-based stratifications (log-density vs ρ/ρ̄), ensure terminology is consistent across the paper, and relabel Table IV accordingly.

P5-m5
- Location: Table I (p. 3)
- Problem: Implausible median match separation. p50 separation is reported as 0.0066 arcsec (6.6 mas), which is unrealistically small for Legacy–DESI cross-matches; the p99 is 0.30 arcsec. A 0.0066–arcsec median is likely a decimal slip (0.066" is plausible).
- Required fix: Recompute and correct the separation statistics (median and percentiles) and confirm units. If values are in degrees or radians internally, state the conversion explicitly.

P5-m6
- Location: §V (nulls), §VI B–E, Table V
- Problem: Two nulls advertised, one reported. You say you run both label-shuffle and position-shuffle permutation nulls, but all reported p-values use label-shuffle only.
- Required fix: Either report the position-shuffle results alongside the label-shuffle ones (noting expected similarities/differences) or remove the claim that both were run.

P5-m7
- Location: §V (intervals) vs Fig. 2 and others
- Problem: Interval terminology inconsistency. Methods say “exact binomial 95% credible interval,” while figure captions specify “95% Jeffreys binomial credible intervals.” Jeffreys is not “exact” in the Clopper-Pearson sense.
- Required fix: Standardize to “Jeffreys 95% binomial credible interval” throughout (or switch to Clopper-Pearson and update captions accordingly).

P5-m8
- Location: §VIII F, per-pixel counts
- Problem: Pixel-count thresholds not specified consistently. You report NSIDE=32 per-pixel σvs monopole statistics over “1,821 valid pixels” on the matched-spiral catalog, while Fig. 6 bottom uses “1,496 valid pixels” for the z ≤ 0.24 subset with ≥200 spirals/pixel. The threshold for the 1,821-pixel analysis is not stated.
- Required fix: State the minimum-spiral threshold used for the 1,821-pixel statistic and make clear that these two pixel populations are different (full matched-spiral vs low-z subset).

P5-m9
- Location: §VIII E, p. 12; Fig. 6 caption
- Problem: Ambiguous phrasing around residual significance. The text says “−4.75σ … is consistent with … at the ∼1σ level,” which mixes the raw deviation with the residual after subtracting the monopole.
- Required fix: Make explicit in the sentence that the “−1.55σ residual after monopole subtraction” is what is being judged against systematics (as you already compute numerically).

P5-n5
- Location: §VI D (d), p. 8
- Problem: Overall bright fraction reference ambiguous. You compare per-class bright/(bright+dark) to “the overall matched-spiral ratio 0.978,” but the earlier program totals on the chirality-relevant sample imply bright/(bright+dark) ≈ 0.981. If 0.978 comes from the 811,609 env-labeled bright+dark superset, say so explicitly.
- Required fix: Specify which population defines the “overall” reference and keep it consistent whenever used.

P5-n6
- Location: Throughout
- Problem: “P5” shorthand is used for the present paper without prior definition; “P4” is defined by context as Paper IV.
- Required fix: Define “P5” at first use or avoid the shorthand.

P5-n7
- Location: Eq. (8–10) and surrounding text (Poisson/tidal steps)
- Problem: Dimensional clarity. Even if λth=0 is sign-only, it would help to state explicitly that variables are nondimensionalized (or in which units) to avoid confusion.
- Required fix: Add a one-sentence note on nondimensionalization or adopted units in the Poisson/tidal pipeline description.

Why these are new
- These issues were not raised in my initial report. The most critical new catch is the impossible filament-class dark sample size (P5-E5), which appears verbatim in the abstract and the body and must be corrected. The failure to propagate monopole uncertainty (P5-M5) affects several significance claims. The tidal-tensor normalization gap (P5-M6) directly bears on the interpretability of the λth ≠ 0 sweep. Additional consistency and clarity problems (P5-M7, P5-m5–m9, P5-n5–n7) tighten the statistical and methodological reporting to PRD standards.