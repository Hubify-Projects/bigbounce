# P4 R54 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/private/tmp/R54_P4/chirality_catalog_paper.pdf` md5=bda86fa1 pages=23
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (8701 chars)
**Wall time**: 410.4s

---

Referee report (methodology/statistics), Physical Review D

I have read the paper carefully, including all figures, tables, equations, appendices, and the abstract/conclusions. Below I list all methodological/statistical and internal-consistency issues I found. For each finding I give an ID, page/section reference, a precise description, and a required fix. Severity categories: ESSENTIAL, MAJOR, MINOR, NIT.

ESSENTIAL FINDINGS

P4-E1 (Sec. II.B, p. 3): Training augmentation arithmetic is inconsistent and not reproducible
- Offending text: “The combined training set contains 6,637 + 17,153 + 2,000 = 25,790 source images; after flip augmentation of the training split the combined pool is 26,616 images (pre-augmentation 79.4/20.6 source-image split: ntrain = 21,293 post-augmentation, nval = 5,323 never augmented; the 826-image difference between the source manifest (25,790) and the combined pool (26,616) arises entirely from horizontal-flip augmentation applied to the training split only…).”
- Problem: With a 79.4% train split of 25,790, pre-augmentation training images are ~20,476. “Flip augmentation of the training split” would naively add ~20,476 images if applied uniformly, not 826. The text implies only ~4% of training items received saved augmentations, but the protocol is not explained. The stated ntrain (21,293) implies 826 augmented samples (21,293 – 20,467 ≈ 826), matching the delta to the pool total, but contradicts the phrase “flip augmentation of the training split” without any restriction. As written, a reader cannot reconstruct the exact augmentation policy.
- Required fix: Precisely specify the augmentation policy and reconcile the counts. Provide a compact table listing (i) pre-augmentation train/val counts per label source; (ii) which subsets were augmented and why; (iii) the exact number of augmented instances added; (iv) the random seed/sampling rule used. If augmentation was selective (e.g., class rebalancing), describe the selection rule explicitly. Ensure the numbers in text sum exactly and match the released manifest.

P4-E2 (Abstract p. 1; Sec. IV.C/D pp. 7–12; Table III p. 11; Conclusions p. 15): Two different σ values for the same canonical ℓ=1 channel are reported in parallel
- Offending text: Abstract reports “+3.64σ … canonical mask” and “+7.28σ, apodized footprint,” and elsewhere “the 10^4-permutation canonical unapodized row … gives +7.93σ,” with caveats that they are not comparable. Similar mixing appears in Sec. IV.D and Conclusions (p. 15).
- Problem: PRD requires a single canonical analysis configuration per reported channel. Here, for the same canonical unapodized ℓ=1 MASTER-deconvolved statistic, two σ values are presented (3.64 with 500-MC, 7.93 with 10^4 permutations; slight field-normalization differences are also mentioned). Even with caveats, this undermines clarity and invites cherry-pick perception.
- Required fix: Choose one canonical null/estimator configuration (recommend the 10^4-permutation configuration in Table III) and report only that σ in Abstract, body, and Conclusions. Move the alternative run (500-MC) to Supplementary/Appendix with a brief note that it is superseded. Ensure all σ quoted for this channel use the same estimator, weight map, field normalization, and null size.

P4-E3 (Appendix E.a, p. 21): Edge-on contamination figure (65.7%) lacks a reproducible derivation
- Offending text: “In our catalog, 65.7% of visually identified edge-on systems (b/a<0.3) receive CW or CCW classifications rather than not spiral.” Then: “This estimate is qualitative pending the axis-ratio cross-match…”
- Problem: The stated 65.7% percentage implies a completed axis-ratio cross-match, yet the text says it is pending. No sample size, catalog used for b/a, or cross-match criteria are provided.
- Required fix: Either (a) provide the exact cross-match source (e.g., Legacy Surveys catalog name/table), sample size, selection cuts, and the computed proportion with binomial uncertainty; or (b) remove the 65.7% number and explicitly defer this to future work. As written, it is not reproducible.

P4-E4 (Abstract p. 1; Sec. VI.A/Table V p. 13–14): “Falsification criterion” phrasing overstates coverage and precision
- Offending text: “Falsification criterion: a future ≥ 5σ real-space dipole detection … at amplitude A ≳ A95, where injection–recovery brackets A95 between 1.0% and 1.5% (A50 ≈ 0.75%) … would be in tension with the present null.”
- Problem: A95 is bracketed, not measured; detection probabilities are axis-averaged under a particular null/scorer; the mapping to “falsification” lacks a formal coverage statement. PRD requires precise statistical language for claims of “falsification.”
- Required fix: Rephrase to “tension” and clearly state that A95 is an axis-averaged, estimator- and null-specific bracket without strict frequentist coverage. Do not label this a “falsification criterion” unless you provide a coverage-calibrated threshold (with uncertainty) and a pre-registered test definition. Update abstract and conclusions accordingly.

MAJOR FINDINGS

P4-M1 (Sec. III.A, multiple pages; Figures and Tables captions): Mixed MC sizes and precision throughout
- Problem: Several primary or diagnostic σ values are computed with NMC=500 (e.g., +3.64σ canonical direct-MC) while others use NMC=10,000 (Table III). For sub-sigma differences and precise rank-p reporting, 500 realizations can be marginal. You also quote σ to two decimals in places where null-moment uncertainty from finite MC is non-negligible.
- Required fix: For all headline σ/p values (abstract, Table I rows, main figures), recompute nulls with ≥10,000 realizations or provide analytic variances where possible. Where 500-MC results are retained as diagnostics, quantify the Monte Carlo uncertainty on z (e.g., via bootstrap on null moments) and round σ accordingly.

P4-M2 (Sec. IV.B, p. 6): Ambiguous “0.39σ shift in the standard error of the difference” statement
- Offending text: “means 1.957 × 10−3 vs. 1.935 × 10−3, a 0.39σ shift in the standard error of the difference; N=500 each…”
- Problem: The phrasing is unclear: σ of what? The SE of the difference of means? The numeric SE is not given. Readers cannot verify the 0.39σ claim.
- Required fix: Provide the numeric SE of the difference, the test statistic used, and the corresponding p-value or z. Alternatively, show the two empirical mean ± SE values explicitly.

P4-M3 (Sec. V.A, p. 12; Appendix D.g, p. 20): Inconsistent WLS amplitudes and terminology
- Offending text: “maximum WLS template amplitude in the full-footprint regional fit is 0.32% … equal-area slab maxima reach 0.46–0.56%.” In Appendix D.g, the joint WLS fit returns Adipole = 4.55×10−3 (0.455%).
- Problem: The term “full-footprint regional fit” is ambiguous and can be confused with the global template fit in Appendix D.g. The 0.32% vs 0.455% amplitudes are not reconciled.
- Required fix: Define “regional fit” precisely (e.g., per-region localized fits) and explain how its amplitude relates to the global 9-template fit. Report both with identical units and confidence intervals, and clarify that the 0.32% is a per-region maximum under a different partitioning.

P4-M4 (Sec. III.B, p. 4; Sec. IV.C, p. 7–8): Pre-declaration of the HC threshold vs post-hoc sweep
- Problem: You declare the HC peq>0.6 cut as primary (generator used “throughout”), yet later present a confidence-cut sweep that appears to motivate the 0.6 threshold by where z collapses. To avoid post-selection bias, the pre-registration of the primary threshold must be unambiguous.
- Required fix: State explicitly when and how the peq>0.6 threshold was fixed relative to all downstream analyses. If it was fixed before inspecting sky maps and nulls, say so; if not, adjust the language to reflect post-hoc choice and present sensitivity to nearby thresholds (e.g., 0.5–0.7) in the primary section, not only in diagnostics.

P4-M5 (Global, multiple pages): Excessive inclusion of ephemeral “artifact” file paths in body text
- Problem: Strings like “pipelines/p2_chirality/outputs/…json” appear across the main text. These are fragile internal paths and distract from scientific narrative.
- Required fix: Move all artifact-path references to a dedicated Reproducibility Checklist or Supplementary Note. In the body, cite a stable DOI/Zenodo bundle with a short handle (e.g., “Artifact A1, DOI: …, file: …”) and include only the minimal handle in-line.

P4-M6 (Data Availability, p. 22): No archived DOI for released catalog/code; commit hash only
- Problem: PRD reproducibility expectations are not met by a mutable GitHub/HuggingFace tag alone. The abstract heavily relies on public release.
- Required fix: Mint archival DOIs (e.g., Zenodo) for: (i) the catalog release used for the paper; (ii) the exact code snapshot (including training/inference scripts); and (iii) the analysis artifacts used to produce the numbers in the paper. Replace “will be deposited” with live DOIs before acceptance.

MINOR FINDINGS

P4-m1 (Abstract p. 1; Sec. III.A pp. 3–4; Table I p. 5; multiple): σ from different nulls shown adjacently—mostly caveated, but one instance lacks explicit caveat
- Example: Table VI (p. 14–15) juxtaposes harmonic-channel injected z and the observed +7.28σ in the same row label. While this section includes a general caveat, make sure every figure/table that juxtaposes σ from different nulls/stats carries an explicit “not directly comparable” note in the caption itself (you did this in most places; standardize it here too).
- Required fix: Add the explicit comparability caveat in any remaining captions/tables where it is missing (e.g., Table VI).

P4-m2 (Appendix A.d, p. 17): “Depth-stratified null leaves the excess essentially unchanged” – quantify “essentially”
- Problem: The text gives +7.13σ vs +7.28σ (good), but “unchanged” is qualitative.
- Required fix: Add the absolute and relative differences in σ (e.g., Δz = −0.15; ~2% change) and the corresponding change in C1 to make the statement quantitative.

P4-m3 (Appendix D.d, p. 19): Leg-template collinearity
- Problem: You note exact rank deficiency (sum to zero) and a huge condition number (4.5×10^16). You state SVD-pseudoinverse and alternatives all recover the same dipole amplitude.
- Required fix: Provide the numerical stability tolerance used and the SVD truncation criterion. Include a short table showing the recovered Adipole under (i) SVD pinv, (ii) dropping one leg, (iii) Gram–Schmidt, with differences at machine precision.

P4-m4 (Sec. IV.D/Table IV, p. 10–11): Report uncertainty on the “99.32%” reproduction fraction consistently
- Problem: You later note the standard error on the mean fraction (~0.018 pp), but the headline percentage is shown without uncertainty.
- Required fix: Present “99.32% ± 0.02% (SE on mean)” or similar, and state N=500 explicitly next to it.

P4-m5 (Appendix B.d, p. 18): T5 (metadata leakage) is acknowledged as limited but still listed as a pass in Table VIII
- Problem: You correctly flag RA circularity in the prose, but Table VIII presents T5 as a clean pass which could be misread.
- Required fix: Add a footnote to Table VIII stating T5 is a weak proxy (RA circularity) and is not counted as an independent directional-leakage test; directional coupling is probed via spherical-harmonic regression elsewhere.

P4-m6 (Sec. VI.A, p. 13): Mapping from label accuracy to amplitude dilution
- Problem: The mapping g = 2a − 1 is given; good, but no uncertainty on a=0.6991 is provided.
- Required fix: Quote the binomial SE for the 69.91% estimate (and κ if desired), and propagate to an uncertainty on g to frame the 1.88% “true-amplitude” estimate as approximate with bounds.

P4-m7 (Appendix C.c, p. 19): Hemisphere LEE direct-MC
- Problem: pLEE ≤ 10−4 is quoted without NMC. Later you imply N=10,000.
- Required fix: State NMC explicitly in that sentence and, if p hits the minimum resolvable, note it (“one-sided, min p = 1/(N+1)”).

P4-m8 (Global): Significant digits/rounding
- Problem: σ are sometimes reported to two decimals when MC errors/finite-sample effects likely support only one decimal (e.g., +7.31σ).
- Required fix: Standardize to one decimal for σ unless analytic variances justify two. Apply consistently.

NITPICKS

P4-n1 (Typos/hyphenation, multiple pages): Spurious hyphenations due to line breaks (e.g., “ap￾pendix”, “com￾puted”). 
- Fix: Clean up hyphenation artifacts in final typeset.

P4-n2 (Notation, p. 7): Clarify that Adipole in Ap units equals the full-amplitude A under your injection definition right where Adip is first defined (you do this later; a short parenthetical on first use would help).

P4-n3 (Figure captions): Ensure all color bars have labeled units consistently (Fig. 7 uses fCW in the caption; the color bar itself is unlabeled in the provided snapshot—confirm the final figure has the label).

P4-n4 (References): Spot-check done; please ensure consistent DOI formatting (e.g., [7], [23]) and that all arXiv IDs resolve; minor consistency cleanup.

ABSTRACT-LAST DRIFT SWEEP (pattern-045)

- All headline numbers in the abstract (+0.41σ, p=0.31; z=0.70 label-shuffle; +3.64σ canonical; +7.28σ apodized; 99.32% leakage reproduction; A50≈0.75%, A95∈(1.0%,1.5%]; harmonic completeness ≥0.999 at 0.75%) are traceable in the body and consistent numerically. 
- However, the abstract currently mixes the two canonical ℓ=1 σ values (+3.64 and +7.93 via Table III footnote). This must be standardized per P4-E2.
- The “Falsification criterion” phrasing must be softened and coverage caveats added per P4-E4.

PROVENANCE SURFACES (patterns 046/047)

- Data Availability (p. 22): commit hash present; catalog link present; no immutable DOI at the time of writing. This must be fixed (P4-M6). Also, many artifact filenames are sprinkled through the text; move to a consolidated reproducibility checklist (P4-M5).

UNCOMPUTED QUANTITATIVE CLAIMS (pattern-048)

- Most qualitative claims are backed by numbers. A few require quantification (P4-M2, P4-m2).

STANDALONE-READER TEST

- The methodology is largely self-contained. The overuse of internal artifact paths harms readability (P4-M5) but does not block comprehension.

EFFECT SIZES

- Effect sizes are generally provided (amplitudes in Ap units). For the hemisphere maximum, please add the corresponding amplitude alongside σ in the main text (you provide 3.484×10−3 in Table IV; mirror it in Appendix C text for transparency).

## Summary recommendation
MAJOR REVISIONS

The paper presents a careful and extensive methodological study with many robustness checks, but several issues must be addressed before meeting PRD standards: reconcile and document the training augmentation counts (reproducibility blocker), standardize to a single canonical σ per diagnostic channel (avoid mixing 500- vs 10k-MC σ in abstract/body), provide an archival DOI for all released artifacts, clarify the edge-on contamination statistic, and tighten a few quantitative statements. Once these are resolved and the presentation streamlined (especially removal of ephemeral file paths from the main text), the paper will be much clearer and methodologically solid.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes pass)

ESSENTIAL FINDINGS

P4-E5 (Appendix D.g p. 20 vs. Table X p. 20; Sec. III.B p. 4): Inconsistent block-bootstrap exclusion z for the same NSIDE=8 setup
- Offending text: Main text repeatedly cites “z ≈ −18.1” (e.g., Table X bottom row; Sec. III.B). Footnote 3 in Appendix D.g reports “z = −18.4 (NSIDE = 8)” for the same block scale. Both are presented as the “primary” NSIDE=8 result.
- Problem: The paper presents two different z values for the NSIDE=8 block-bootstrap exclusion without a clear provenance difference beyond Nboot and seed changes implied only in the footnote. Because this number anchors a key exclusion claim, a single canonical configuration and result must be reported consistently across Abstract/body/Conclusions, with any alternative runs clearly demoted.
- Required fix: Choose and declare one canonical NSIDE, Nboot, seed, and design matrix for the block-bootstrap WLS analysis (recommend NSIDE=8 with Nboot ≥ 1000). Report only that z in Abstract/body/Conclusions. Move any alternate runs (e.g., Nboot=500) to Appendix with an explanation of expected run-to-run variability. Provide the exact configuration (Nboot, seed, block definition, design matrix) and uncertainty on z due to bootstrap Monte Carlo noise.

MAJOR FINDINGS

P4-M7 (Sec. VII.a, Fig. 9 p. 15; Table VI p. 14–15): Harmonic-channel completeness averaged over only three fixed axes
- Offending text: “axis-averaged P(≥3σ) vs Ap … over {x, y, z}” with headline statements such as “P(≥3σ) = 0.92 at Ap = 0.5%” and “≥ 0.999 at Ap ≥ 0.75%.”
- Problem: Averaging completeness over three cardinal axes is not representative of a sphere-average and may materially over/underestimate detection probability for generic axes relative to the analysis footprint. The text elsewhere correctly emphasizes axis dependence, but the headline completeness values are easy to over-interpret.
- Required fix: Either (a) recompute completeness using a dense, area-uniform set of axes (e.g., HEALPix NSIDEdir ≥ 8) and report sphere-averaged P(≥3σ) with uncertainty; or (b) explicitly relabel all completeness results as “cardinal-axis only,” and add a quantitative comparison to a random-axis (area-uniform) average at one or two amplitudes to show the bias from using {x, y, z}. Update Table VI and Fig. 9 captions accordingly.

P4-M8 (Appendix B.a p. 17; Sec. II.B p. 3): Validation accuracy (93.7%) mixes CE-ResNet pseudo-labels and human labels
- Offending text: “The reported 93.7% accuracy is the best-epoch three-class validation accuracy on the un-augmented held-out random 80/20 split…” with the caveat that 66.5% of labels come from CE-ResNet.
- Problem: Quoting a single validation accuracy on a mixed-label source can be misleading; most of that metric reflects agreement with CE-ResNet rather than independent truth. While you later provide an independent GZ1 cross-match (69.91%), the paper never reports validation accuracy disaggregated by label source on the held-out split.
- Required fix: Report per-source validation metrics on the held-out split: (i) against GZ1-only items, (ii) against CE-ResNet-only items, and (iii) against synthetic negatives, with confidence intervals. Make clear in the text that 93.7% reflects mixture agreement and that 69.91% (κ=0.40) is the conservative accuracy against independent human labels. Consider moving 93.7% out of any performance-sounding context to avoid misinterpretation.

P4-M9 (Global, Monte Carlo): Missing seeds/config summaries for all nulls/injections
- Problem: Some runs list seeds (e.g., seed 42) and NMC, others do not. For reproducibility and to interpret small z deltas (e.g., +7.28 vs +7.31), every Monte Carlo/permutation/injection result must have its seed(s), NMC, and configuration captured in one place.
- Required fix: Add a consolidated Monte Carlo registry (table or Supplement), listing for each headline σ/p/injection curve: the null type, NMC, seed(s), mask/weight/field definition, and scorer. Reference this registry from the main text instead of ad hoc mentions.

MINOR FINDINGS

P4-m9 (Sec. VI.A p. 13): “Uniform in polar angle” described as “mildly over-weights” poles
- Offending text: “uniform in polar angle, which mildly over-weights near-polar axes relative to an area-uniform draw”
- Problem: A θ-uniform draw strongly, not mildly, over-weights near-polar directions relative to an area-uniform distribution (density ∝ 1 vs. sin θ). You later provide a useful cross-check showing negligible practical impact here, but the description is inaccurate.
- Required fix: Rephrase to “non–area-uniform (over-weights near-polar axes)” and keep the quantitative cross-check. Optionally adopt area-uniform draws as the default for injection sweeps to avoid confusion.

P4-m10 (Appendix C.b p. 19): σiso symbol not defined
- Offending text: “NGP (b > 0) gives σiso = +0.47…”
- Problem: σiso appears without definition (e.g., “moment-z against isotropic permutation null”). While inferable, it should be explicit on first use.
- Required fix: Define σiso at first appearance in Appendix C and/or replace with “moment-z against the isotropic permutation null” for clarity.

P4-m11 (Sec. IV.B p. 6): “slab-to-slab scatter … ≲2.7σ per slab” not quantified
- Problem: The text asserts a maximum |z| without listing the exact max, mean, and expected scatter under the global rate. This is easy to quantify and improves transparency.
- Required fix: Add the numeric maximum z, the RMS of slab deviations, and the expected RMS under binomial noise at the global rate. A one-line parenthetical suffices.

P4-m12 (Appendix D.a p. 19): Apodization robustness “essentially unchanged” needs numbers
- Offending text: “C2 2° apodization gives +3.57σ … essentially unchanged from +3.64σ”
- Problem: As with the depth-stratified null you quantified elsewhere, state the absolute Δz and the percent change.
- Required fix: Add “Δz = −0.07 (≈2% change)” or equivalent, and, if available, the corresponding change in C1.

P4-m13 (Appendix C.c p. 19): Hemisphere maximum effect size not echoed in text
- Problem: The Appendix C text cites the σ for the maximum-hemisphere asymmetry but not the amplitude, forcing readers to look up Table IV.
- Required fix: Add the amplitude (3.484 × 10−3 in Ap units) alongside the σ in the Appendix C paragraph for completeness.

P4-m14 (Table III p. 11, caption): Minimum resolvable p-value rounding
- Offending text: “minimum reportable p is 1/(N+1)≈1.0×10−4”
- Problem: For N = 10,000 permutations, 1/(N+1) = 9.999×10−5. Minor, but since you emphasize careful p reporting elsewhere, use the exact value.
- Required fix: Change “≈1.0×10−4” to “= 9.999×10−5” (or keep “≈ 1.0×10−4” but note exact expression in parentheses once).

P4-m15 (Appendix B.d p. 18): QC-flagged rows and T7 summary
- Problem: You note 2.9% rows with recovered flip probabilities outside [0,1] and show the primary estimator is unchanged when excluding flagged rows. It is unclear whether the T7 calibration-proxy comparisons in Table VIII were computed with or without the flagged rows.
- Required fix: State explicitly that all QC-driven reliability summaries (including T7) were recomputed excluding flagged rows, or report both values to show invariance.

P4-m16 (Terminology, multiple): “Band” vs “single-mode” for ℓ = 1 MASTER
- Problem: A few places refer to the ℓ = 1 MASTER point as a “band” (while Appendix A correctly states it is a single-ℓ bin). This can confuse readers.
- Required fix: Ensure all references to ℓ = 1 MASTER use “single-mode” or “single-ℓ bin,” reserving “bandpower” for true multi-ℓ bins.

NITPICKS

P4-n5 (Notation artifacts, multiple): Spurious carets/diacritics
- Example: “x, ˆ y, ˆ zˆ” (Appendix D.g table note) shows a stray diacritic. 
- Fix: Clean notation to standard x, y, z unit vectors (e.g., x̂, ŷ, ẑ) consistently.

P4-n6 (Consistency of apodization label): Use a uniform notation for the apodization kernel (e.g., “C2, 2°” everywhere), matching the NaMaster API name once in Appendix A, and a human-readable shorthand in figures/tables.

Explanation
This fresh-eyes pass focused on recomputing/arithmetic spot-checks, figure-caption vs body consistency, unit/normalization checks, cross-reference fidelity, null comparability, and abstract-to-body traceability. Most headline arithmetic checked out; the primary new issues are (i) inconsistent reporting of the NSIDE=8 block-bootstrap exclusion z, which should be standardized; (ii) completeness curves averaged over only three axes; (iii) clearer separation of validation accuracy by label source; and (iv) consolidated seeds/configs for all Monte Carlo results. Other items are minor presentation clarifications.