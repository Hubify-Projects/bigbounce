# P4 EXT18 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p2_chirality/chirality_catalog_paper.pdf` md5=c47abc18 pages=23
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (9894 chars)
**Wall time**: 451.4s

---

Referee report (PRD methodology review)

Manuscript: “Survey-Scale Galaxy Chirality with Equivariant TTA: A Null Real-Space Chirality Dipole, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)”

General assessment
The manuscript presents a very large chirality-labeled catalog and a careful hierarchy of estimators with extensive null and systematics diagnostics. The authors are scrupulous about distinguishing null procedures and frequently warn that σ values are not comparable across channels. However, several issues must be addressed before this is suitable for PRD:

- One core methodological inconsistency: the training/augmentation bookkeeping does not add up.
- Multiple instances of internal version-history language and editorial revision commentary in the body of the paper.
- Reproducibility references rely heavily on internal artifact paths in the main text; these should be confined to properly curated supplemental material with a frozen DOI.
- Some unit usage for amplitudes is confusing and must be standardized.
- A few claims and p-values are quoted with precision exceeding the MC resolution used; language should reflect the finite resolution of the null ensembles.

Below I itemize all findings.

ESSENTIAL

P4-E1 — Sec. II.B (p. 3): Training/augmentation arithmetic inconsistency
Quoted text: “The combined training set contains 6,637 + 17,153 + 2,000 = 25,790 source images; after flip augmentation of the training split the combined pool is 26,616 images (80/20 split: ntrain = 21,293, nval = 5,323; the 826-image difference … arises entirely from horizontal-flip augmentation applied to the training split only — the validation split … is never augmented).”
Problem: If horizontal-flip augmentation is applied by duplicating the training split, one expects an increase of O(ntrain), not 826 images. If augmentation is on-the-fly (no dataset-size change), the pool should remain 25,790. As written, the numbers are mutually inconsistent and leave the training protocol ambiguous.
Required fix: Precisely and consistently specify the augmentation protocol. If flips are applied on-the-fly, state that explicitly and remove the 826 extra images. If flips created additional stored samples, provide the exact counts per class before/after augmentation and explain why only 826 extra items were created. Align ntrain, nval and total-pool numbers accordingly. This is a load-bearing provenance item and must be internally consistent.

P4-E2 — Multiple locations (pp. 4, 15, 21): Internal version-history and revision commentary in body text
Instances:
- Sec. III.B (p. 4): “was declared in early versions of this analysis and predates the provenance audit…”
- Appendix D, footnote (p. 19–20): “computed post-R29…”
- Appendix E (p. 21): “An earlier version of this paragraph overstated the stability… Now recomputed…”
Problem: PRD articles must not contain internal version-history, review-log, or earlier-draft commentary in the main text.
Required fix: Remove all references to “early versions,” “post-R29,” “earlier version of this paragraph,” “restamps,” etc., from the body. If needed, restrict such notes to a changelog in a Supplement, but they should not appear in the article proper.

P4-E3 — Sec. V.A (p. 12): Units confusion for amplitudes
Quoted text: “our maximum WLS template amplitude in the full-footprint regional fit is 0.32% (in Ap units…)”
Problem: Ap is dimensionless; elsewhere you report Ap amplitudes as decimals (e.g., 4.55 × 10−3) and note Ap = 2(fCW − 1/2). Saying “0.32% in Ap units” is internally inconsistent and risks confusion with fCW-deviation-in-percent.
Required fix: Adopt a single, explicit unit convention throughout. Either report Ap as a pure number with “Ap units” (e.g., 0.0032) and, when helpful, give the corresponding fCW deviation (0.16%) in parentheses, or report all amplitudes as fCW-deviation percentages. Correct this sentence and audit the paper for similar wording.

P4-E4 — Data Availability (p. 22): Missing frozen DOI and citable snapshot for code/data
Quoted text: “A persistent archival DOI (Zenodo deposit of the versioned release) has not yet been minted; until it is, the versioned release tag above is the citable artifact.”
Problem: For PRD, the reproducibility record should point to frozen, immutable artifacts (data, code, and configuration) with DOIs at acceptance.
Required fix: Before publication, mint DOIs (e.g., Zenodo) for: (i) the catalog release used in this paper, (ii) code snapshot sufficient to reproduce the analyses, and (iii) the “canonical-provenance artifacts” referenced in the text. Replace provisional language with DOI links in the manuscript.

MAJOR

P4-M1 — Throughout (many pages): Heavy use of internal artifact paths and JSON filenames in the main text
Examples: “artifact pipelines/p2_chirality/outputs/canonical_provenance/c11_meta_m4_slab_stats.json”… appears dozens of times.
Problem: While commendable for reproducibility, this level of low-level path detail clutters the narrative and is not standard PRD style.
Required fix: Move these file-level references to a properly curated Supplemental Material (with a frozen DOI). In the body, keep brief pointers (e.g., “see Supplemental Material, Sec. S3, Artifact A1”) rather than raw paths/filenames.

P4-M2 — Sec. IV.D/Table IV (pp. 10–11): Reporting of significance with small null ensembles
Instances: canonical-mask direct-MC values quoted with N = 500 null realizations (e.g., “+3.64σ (pMC = 0.030)”), and hemisphere “pLEE ≤ 10−4” with N = 10,000.
Problem: When NMC is small, tail estimates are coarse. Using inequalities is correct, but some σ values carry a precision that exceeds the null resolution.
Required fix: Where NMC is small, consistently accompany σ with the empirical rank p and its finite-resolution bounds. For pLEE, explicitly state pLEE = 1/(N+1) as the minimum resolvable value with N = 10,000, and avoid “≤” unless there is an analytic bound; use “≤ 1.0 × 10−4 (resolution-limited)” or similar. Consider standardizing diagnostic σ values to the higher-precision 10^4-permutation runs or move low-NMC diagnostic numbers to Supplemental.

P4-M3 — Sec. VI.A (p. 13): Injection axis-draw convention
Quoted text: “each injection draws an independent random dipole axis (polar angle θ ∼ U(0, π)… uniform in polar angle, which mildly over-weights near-polar axes relative to an area-uniform draw)” with a later area-uniform spot check.
Problem: Using θ-uniform instead of area-uniform can bias axis-averaged completeness; you mitigate this with a spot check.
Required fix: Either (i) adopt area-uniform axis draws (cos θ ∼ U[−1,1]) for the main recovery curve and update the numbers, or (ii) keep θ-uniform but elevate the area-uniform re-run from a spot check to a full reproduction of the table, and state prominently that both conventions give indistinguishable thresholds within MC error. As written, the conclusions likely hold, but PRD readers should not have to reconcile axis conventions midstream.

P4-M4 — Sec. IV.C, V.A (pp. 7, 12): Effect-size reporting consistency
- You quote the HC real-space dipole amplitude (Adip = 4.4 × 10−3) and various template-fit amplitudes (0.32% Ap, 0.46–0.56% regional maxima), but not always with a unified unit convention or uncertainties.
Required fix: Provide all dipole-amplitude effect sizes in the same unit system alongside uncertainties (or state “point estimate without uncertainty” where applicable) and, where amplitudes are from different estimators or selections, clearly label them. Consider a single summary table of amplitudes for the main estimators with units and selections.

P4-M5 — Sec. IV.C (pp. 7–8): Reporting axis for an insignificant dipole
Quoted text: “amplitude 4.4 × 10−3 toward (l, b) = (293°, 12°) with significance 0.41σ… at this significance the dipole axis is unconstrained…”
Problem: Quoting a direction for a null-level dipole can mislead.
Required fix: Either omit the direction in the main text or move it to Supplemental with an explicit caveat that, under the null, the recovered direction is random; retain the note that the axis is unconstrained.

MINOR

P4-m1 — Abstract and Sec. I (pp. 1–2): “largest chirality-labeled galaxy catalog to date”
Claim appears plausible (3.2M spirals vs 1.95M in CE-ResNet) but should be carefully phrased because a substantial fraction of labels derive from CE-ResNet pseudo-labels and Galaxy Zoo.
Required fix: Rephrase to “to our knowledge, the largest chirality-labeled catalog analyzed with an equivariant pipeline (3.2M spirals),” or similar, and note that a portion of training labels derive from prior catalogs.

P4-m2 — Table III caption (p. 11): Minimum rank p
Quoted: “minimum reportable p is 1/(N+1) ≈ 1.0 × 10−4.”
Required fix: Report exactly 1/10001 ≈ 9.999 × 10−5 to avoid implying greater precision; ensure consistent use across manuscript.

P4-m3 — Sec. III.D (p. 4): Overstated certainty “flip-swap correlation = 1.000 by construction”
While correct in floating-point arithmetic, storage quantization and pipeline mismatches are discussed later.
Required fix: Add “within floating-point precision; see QC in Appendix B” or harmonize with the later QC paragraph.

P4-m4 — Typos and style
- Several minor hyphenation/spacing artifacts (e.g., “V iT − Small,” “apodized-footprint,” inconsistent capitalization of “MASTER”).
Required fix: Copy edit for consistent typography and capitalization.

P4-m5 — Appendix E, footnote marker “4” (p. 21)
Footnote “4” references an estimator variant; ensure footnote numbering and references are consistent and clear.

NIT

P4-n1 — Bibliography consistency
Spot-checking a few entries looks fine; ensure all DOIs and arXiv IDs match cited years (e.g., [7] ApJ 943 (2023), [9] MNRAS 526 (2023) — both correct). No action unless a full sweep finds mismatches.

P4-n2 — Length and structure
The manuscript is dense (23 pages). The main story could be streamlined by moving much of the artifact-path detail and some diagnostic panels to Supplemental Material. Recommended but not mandatory for PRD regular articles.

Abstract-last drift audit
- Abstract’s key numbers (+0.41σ; p = 0.31; z = 0.70 alternate null; N ≈ 9.5 × 10^5 spirals; +3.64σ canonical, +7.28σ apodized; WLS block-bootstrap z ≈ −18 at Aref = 1.7%; A50 ≈ 0.75%, A95 bracket 1.0–1.5%) are all traceable to the body (Secs. IV.C, IV.D, Appendix D, VI.A; Tables I, III, IV, V, X). The abstract repeatedly cautions that σ from distinct nulls are not directly comparable — consistent with the body. No overclaim detected in the main significance narrative. Retain this discipline in the revised version.

Effect sizes
- The real-space effect size Adip = 4.4 × 10−3 is reported (good). Please standardize units in V.A (see P4-E3/P4-M4).

Stand-alone reader test
- The paper is largely self-contained; ensure that any reliance on external CE-ResNet pseudo-labels is adequately caveated (already done), and that all load-bearing results do not require consulting an unpublished companion.

## Summary recommendation
MAJOR REVISIONS

The scientific core appears solid and carefully caveated, with commendable attention to null procedures and systematics. However, there is a critical inconsistency in the training/augmentation accounting that must be corrected, and substantial editorial clean-up is needed (removal of internal version-history language from the main text, consolidation of artifact paths into Supplemental Material, and unit-standardization for amplitudes). With these addressed and DOIs minted for the reproducibility artifacts, the paper would be suitable for PRD.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS (fresh-eyes audit)

A. ARITHMETIC/CALCULATION CHECKS

P4-m6 — Table II (Catalog B row): Missing Nspiral and σ consistency
- Issue: The Catalog B row quotes fCW = 0.504 ± 0.0003 with “Dev. +14.6σ,” but Nspiral for B is not given (only NA and NC are listed). If σ = 0.0003 is used, 0.004/0.0003 ≈ 13.3σ, not 14.6σ. The printed +14.6σ matches σ ≈ 0.000274 (i.e., the A-tier σ), but then the quoted ±0.0003 is inconsistent.
- Required fix: State NB
spiral explicitly and compute σB = sqrt[f(1−f)/NB
spiral] from that N. Ensure the “±” uncertainty and the “Dev. (σ)” use the same σB. If Catalog B uses NA
spiral, say so.

P4-M8 — Section V.A vs Appendix D (effect-size mismatch across estimators)
- Issue: Sec. V.A cites a “maximum WLS template amplitude … 0.32% (in Ap units…)” for a full-footprint regional fit, whereas the joint nuisance-marginalized WLS on the canonical mask (Table X) gives Abest
dipole = 4.55 × 10−3 = 0.455% (Ap units). The text does not clearly reconcile these two amplitudes across selections/fit designs.
- Required fix: Add a single summary table of all quoted dipole-amplitude point estimates, each labeled by estimator, mask/selection, and nuisance basis, with a unified unit convention and (where available) uncertainties. Explicitly explain why the 0.32% and 0.455% differ (different region partition, nuisance templates, or weighting).

B. NULLS, RESOLUTION, AND REPRODUCIBILITY

P4-E5 — Unthresholded-sample A50 reported below tested grid (extrapolation called “interpolation”)
- Location: Sec. IV.C, unthresholded full-sample injection. 
- Issue: A50 ≈ 0.36% is reported even though the smallest amplitude with ≥50% recovery that was actually tested is 0.5%; the manuscript calls this “log-interpolated,” but with no bracketing point below 0.5% this is an extrapolation.
- Required fix: Either (i) extend the injected grid below 0.5% to bracket the 50% crossing and report the bracketed A50 with MC errors, or (ii) state clearly that 0.36% is an extrapolation and present a conservative bound (e.g., A50 ≤ 0.5% on tested grid), moving the extrapolated number to Supplemental.

P4-M6 — Figure/diagnostic consistency: mixed-NMC significance across body and figures
- Location: Fig. 8 caption uses a 200-MC “multi-null battery,” Table III uses 10^4 permutations for the same channel.
- Issue: Displaying low-NMC and high-NMC results for the same diagnostic in different places invites confusion and over-interpretation of low-NMC tails.
- Required fix: Standardize the displayed diagnostic σ/p-values to the higher-precision 10^4-permutation runs where available (or explicitly mark figure panels as low-NMC previews and move them to Supplemental). In the body, prefer the 10^4 results.

P4-E6 — Ambiguity/inconsistency in “per-galaxy label-shuffle” vs. “per-pixel/binomial” nulls
- Locations: Sec. IV.C (per-galaxy label-shuffle null), Sec. VI.A/Table V (explicitly binomial per-pixel draws).
- Issue: The manuscript sometimes calls the null “per-galaxy” but elsewhere defines/implements it as per-pixel binomial re-draws nCW(p) ~ Binomial(Nspiral(p), pglobal
CW). These are not the same object if “per-galaxy shuffle” means shuffling labels at the galaxy level globally.
- Required fix: Unify terminology and give exact algorithm(s) in one place (pseudocode): (i) pixel-permutation null; (ii) per-pixel binomial draw; (iii) any true per-galaxy shuffles. Then, in each result, name which exact null was used.

P4-M11 — Primary estimator uses pixel-permutation (“isotropic bootstrap”) null; heteroscedasticity justification is buried
- Location: Sec. IV.C primary dipole uses pixel permutation; only later is a per-pixel-count-preserving null checked.
- Issue: On a highly non-uniform footprint, the choice of pixel-permutation (destroying Nspiral(p)-dependent noise geometry) vs. per-pixel binomial matters conceptually. You do present a robustness check, but the text still elevates the pixel-permutation null as the “primary.”
- Required fix: Either adopt the per-pixel-count-preserving null as the primary for the dipole (and keep pixel-permutation as a cross-check), or add a short, explicit justification in the main text for preferring pixel-permutation as the canonical choice, with the per-pixel-preserving result quoted alongside.

P4-E7 — Alternate-null z-value in abstract vs body (0.70 vs 0.58) lacks a single canonical choice
- Locations: Abstract (“z = 0.70 … per-galaxy label-shuffle null”), Sec. IV.C (0.58σ from the same generator; a separate implementation gives 0.70σ).
- Issue: The abstract promotes the 0.70σ value from a secondary implementation while the body’s first-listed result for the same null is 0.58σ. This looks like cherry-picking even if both are within MC fluctuation.
- Required fix: Choose one canonical implementation for alternate nulls (preferably the one co-located with all other primary computations) and report that consistently in both abstract and body. If you wish to cite the independent cross-check, keep it secondary and labeled as such.

C. FIGURE CAPTION VS BODY CLAIMS

P4-M7 — Hemisphere LEE narrative mixes incompatible post-LEE summaries
- Location: Appendix C (3.05σ raw, direct-MC pLEE ≤ 10−4, Bonferroni “< 1σ”).
- Issue: The direct-MC LEE p-value (resolution-limited) and the Gaussian Bonferroni heuristic lead to qualitatively different post-LEE statements. You note the dependence/independence caveat, but the juxtaposition reads as contradictory evidence without a clear take-away.
- Required fix: Collapse to a single, principled post-LEE statement (the direct-MC max-statistic null) in the body; move the Bonferroni heuristic to Supplemental with a clear note that it is known to be conservative and inapplicable under strong correlations.

D. EQUATIONS AND DEFINITIONS

P4-m7 — Undefined “flip-swap error” metric and surprising magnitude
- Location: Appendix B (T7 calibration proxy).
- Issue: The “mean flip-swap error” is quoted (e.g., 0.267 vs 0.383; 0.698 vs 0.464 on spirals only), but the metric is not defined (L1? L2? range?). Values > 0.5 suggest a scale not obvious for a probability-difference measure.
- Required fix: Define the flip-swap error precisely, including its range and interpretation. If reported on different subsets (all classes vs spirals-only), state why those means can exceed 0.5 and what that implies for calibration.

E. CROSS-REFERENCES AND TERMINOLOGY

P4-m8 — Null-procedure glossary needed
- Locations: Throughout (isotropic bootstrap; pixel permutation; per-galaxy shuffle; per-pixel binomial; density-stratified; depth-stratified).
- Issue: Many distinct nulls are introduced with similar names. Even with local caveats, it’s easy for readers to lose track.
- Required fix: Add a short “Null procedures at a glance” box (or Supplemental table) listing each null by a unique handle, with a one-line definition and the sections/figures where it is applied.

F. ABSTRACT FAITHFULNESS

P4-M9 — Shamir amplitude comparison lacks a single, clearly defined in-paper comparator
- Location: Abstract and Sec. V.A (“factor of ∼6–12” vs Shamir 1.7–4.0%).
- Issue: The factor-of-6–12 uses the 0.32% comparator from a “full-footprint regional fit,” but Table X’s best-fit on the canonical mask is 0.455%, changing the factor materially (to ≈3.7–8.8). The abstract does not explain which comparator it uses and why.
- Required fix: In the body and abstract, choose one internally consistent comparator for your amplitude-level statement against Shamir and justify the choice (selection, mask, nuisance model). Alternatively, report a range with both in-paper comparators explicitly named.

G. APPENDIX VS MAIN-TEXT ALIGNMENT

P4-M10 — Bias-hardening T6 threshold is far looser than analysis sensitivity and is underspecified
- Location: Appendix B (T6: “< 10% CW difference between hemispheres” with a reported < 0.4%).
- Issue: A 10% pass threshold is not meaningful in a study targeting sub-percent sensitivity, and the hemisphere definition (Galactic? Equatorial? Ecliptic?) is not specified here.
- Required fix: Specify the hemisphere frame used and tighten the acceptance threshold to be commensurate with the study’s sensitivity (e.g., < 0.5% or a z-threshold versus binomial expectation). Otherwise, clarify T6’s limited role as a coarse sanity check only.

H. STALE/INCONSISTENT NUMBERS

P4-M12 — Mixed naming for the same primary null
- Locations: Table I uses “iso. boot.,” Sec. IV.C calls it “pixel-permutation null,” elsewhere “isotropic permutation.”
- Issue: Same procedure, multiple names.
- Required fix: Standardize the name (e.g., “pixel-permutation isotropic bootstrap”) and use it consistently.

I. MINOR/NITS

P4-n3 — Seed/reporting consistency for MC ensembles
- Issue: Some places state seed=42 and NMC; others don’t. Readers attempting reproduction may struggle to match panel-level numbers if seeds differ.
- Required fix: For every body-quoted NMC result that is not superseded by a higher-NMC recomputation, list NMC and whether a fixed seed was used. Otherwise, move low-NMC seeded previews to Supplemental and keep only high-NMC canonical numbers in the body.

P4-n4 — Clarify “monopole-preserving” estimator variant in Appendix E
- Issue: The footnoted “monopole-preserving” single-mode pseudo-Cℓ variant that yields +4.31σ is easy to confuse with the canonical post-subtraction, post-MASTER channels.
- Required fix: In the first sentence referencing this variant, add a parenthetical that this is pre-subtraction, pre-MASTER, single-mode pseudo-Cℓ, and is not a cosmological estimator (diagnostic only), with a pointer to Sec. IV.D for leakage context.

NO OVERLAP STATEMENT
The items above are new and non-duplicative of the issues in my initial report. They arose from re-checking arithmetic, unit consistency, null-definition clarity, abstract/body alignment, and the comparability of diagnostics under different MC resolutions.