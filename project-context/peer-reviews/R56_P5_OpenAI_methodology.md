# P5 R56 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/private/tmp/R56_P5/p5_desi_chirality.pdf` md5=c3295c1f pages=33
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (5898 chars)
**Wall time**: 344.1s

---

Referee report on “Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test …”

Scope of review
- Focus: statistical-method validity, derivation chains, dimensional analysis, internal arithmetic consistency, error propagation, and whether headline claims are precisely supported by the body.
- I audited the numbers and σ/p claims that can be recomputed from the tables/figures/equations in the PDF and checked consistency between abstract, body, tables, and conclusions.

Overall assessment
The paper assembles a large matched sample and conducts a careful set of null tests. Many internal arithmetic checks (fCW, σfrom half values, omnibus χ², Bonferroni thresholds, sample-size scaling) I recomputed match the text. However, there are several essential issues that must be corrected before this can meet PRD standards: (i) inconsistent p-values for quoted σ in the Paper IV dipole reference; (ii) conflicting redshift-quantile permutation p-values (0.372 vs 0.80–0.81) in the same section; (iii) extensive use of internal “artifact [A#]” and version-history language throughout the main text; (iv) the primary estimator/analysis path is designated post hoc; (v) data/code availability lacks a concrete DOI; and (vi) one variance model (ASTRA entropy-weighted) is presented with an approximation that understates dependence and needs either a proper uncertainty treatment or removal. I detail these, plus additional major/minor items, below.

Findings

ESSENTIAL

P5-E1. Sec. II, p. 3: Inconsistent σ-to-p mapping for Paper IV dipole
- Problem: “Paper IV’s current headline is a real-space full-sky dipole null at +0.43σ (p = 0.30)” and earlier “+0.41σ (p = 0.31).” A two-sided p-value for |z| ≈ 0.41–0.43 is ≈ 0.66–0.68; a one-sided p is ≈ 0.33–0.34. The quoted p ≈ 0.30–0.31 is inconsistent with either mapping.
- Required fix: Either (a) correct the p-values to match the stated σ (state explicitly whether one-sided or two-sided), or (b) omit the numerical p and retain only the σ, or (c) quote the precise numbers from Paper IV with the same tail convention used there. Since this paper’s conclusions do not need Paper IV’s p numerics, removing them is acceptable; but if retained, they must be consistent.

P5-E2. Sec. VI.B, p. 9–10: Conflicting redshift-bin permutation p-values
- Problem: The section first states “label-shuffle permutation … returns p = 0.372,” then two sentences later states that a stratified shuffle yields “p = 0.81 stratified vs 0.80 free-shuffle,” i.e., a different free-shuffle p than 0.372 for the same test. The body/text do not explain a change of binning, statistic, or parent set that would reconcile 0.372 vs 0.80.
- Required fix: Unify and document a single redshift-scan test result. If multiple tests were run, label them distinctly (e.g., “five equal-count redshift quintiles,” “different binning,” “different parent”) and report each with its exact configuration so the p-values are not contradictory. If only one test is intended, correct the numbers and keep one pair (free + stratified) with MC uncertainty.

P5-E3. Throughout main text (e.g., Abstract p. 1; Sec. IV–XI, multiple pages): Version-history/internal-artifact language in body
- Problem: The manuscript repeatedly references internal artifacts and versioning in the main text (examples: “[A3], [A4], …,” “earlier preprint versions used the ‘V-Web’ label loosely…,” “an earlier preprint version cited… preliminary values,” “deterministic-seeded NumPy default rng,” “committed artifacts do not carry…,” “manuscript tag v0.1.85-2026-06-26”). PRD requires a clean scientific narrative; such provenance belongs in a Data/Code Availability appendix, not in-line in methods/results prose.
- Required fix: Move all [A#] artifact pointers, RNG/seed statements, repository paths, and version-history commentary out of the main text and into a Reproducibility Appendix (already present) and the Data Availability section. The in-text scientific claims must be understandable without following repository pointers. Keep standard bibliographic citations only in the body.

P5-E4. Sec. V, Eq. (1), Secs. VI, VIII.F, and Fig./Table captions: Mixed use of Paper IV monopole vs matched-sample monopole
- Problem: σpred is defined from Paper IV’s ∆fCW = −0.0026, while Table XII subtracts the matched-sample monopole fP5CW = 0.4972 (∆ ≈ −0.0028). Several results (e.g., Fig. 5, Table IV vs Table XII) intermix references without always restating which monopole is used, and some narrative compares σfrom half to different σpred definitions within the same section.
- Required fix: Choose a single primary reference for monopole-subtracted residuals (either the internal matched-sample fP5CW or Paper IV’s catalog-wide ∆fCW) and consistently use it in all monopole-referenced residuals in the body and figures/tables. If both are reported, clearly label them everywhere they appear and avoid mixing within a section. Propagate the reference uncertainty uniformly in residual statements.

P5-E5. Sec. X, p. 26–27: ASTRA entropy-weighted uncertainty model underestimates dependence
- Problem: The entropy-weighted per-class σ uses an independence assumption across objects and ignores within-object negative correlation among class weights. You note a Monte Carlo shows per-class SDs agree within 1.2% and report class-sum correlations up to +0.42, but the final reported σ-values and intervals in Table XIV still reflect the independence approximation.
- Required fix: Replace the approximate analytic variances with the Monte Carlo standard errors you already computed (report the MC-based SEs or σ-values explicitly), or provide a correct analytic variance that includes the within-object covariance (e.g., from a multinomial/Dirichlet-multinomial weighting formulation). Alternatively, drop the entropy-weighted row from Table XIV and retain only the argmax and T-Web overlap, to avoid understating uncertainty.

P5-E6. Appendix C (Data/Code availability), p. 31–32, and Abstract/Conclusions: Missing citable DOI for the frozen release
- Problem: The manuscript states “A DOI-minted archival snapshot of this directory accompanies journal submission” but does not provide the DOI string. PRD requires a resolvable DOI or long-term archive link for reproducibility.
- Required fix: Provide the exact DOI for the archived code/data snapshot used for the results in this paper and ensure it matches the manuscript tag cited. Confirm that all pointers in Appendix D match that DOI snapshot. If the DOI is not yet minted, this must be completed before acceptance.

P5-E7. Sec. V.B, p. 7–8 (“pre-registration caveat”): Primary analysis designated post hoc
- Problem: The “primary analysis path” is declared post hoc. While you attempt to address garden-of-forking-paths via Bonferroni families and explicit declaration, PRD expects a clearly pre-declared primary estimand and analysis workflow in the paper as submitted.
- Required fix: Recast the manuscript so that the DESIVAST void vs non-void contrast (and precisely which variant: sphere-PIS with k-unbounded exact membership, or catalog-native GALZONE) is stated as the prespecified primary estimand at first introduction of methods (end of Sec. III or start of Sec. IV), with all other analyses unambiguously labeled as secondary diagnostics. Move “pre-registration caveat” language to the Discussion or supplement, keeping the main narrative free of exploratory phrasing.

MAJOR

P5-M1. Sec. X, Table XIV, caption and text: Report effect sizes and confidence intervals for class differences explicitly
- Problem: You present max |σ| versus 1/2 per class but do not give explicit 95% CIs on the class differences (argmax and T-Web overlap). This weakens the quantitative bound comparison claims.
- Required fix: For each class with n ≥ 100, report the 95% two-sided CI for fCW (Jeffreys) and for the difference against parity and, if relevant, for T-Web-vs-ASTRA argmax per-class differences on the overlap. State the maximum permitted class offset at 95% CL to make “no class clears threshold” numerically explicit.

P5-M2. Sec. VII, Table VII: Include only resolved (Rs ≥ cell size) rows in the main table
- Problem: The presence of grid-unresolved Rs = 10 Mpc/h rows in the main robustness table invites misinterpretation despite your caveat.
- Required fix: Move the Rs = 10 rows to an appendix or supplemental table and keep only Rs ∈ {25, 50} in Table VII. In the text, retain the sentence noting that the under-resolved runs were checked but are excluded from claims.

P5-M3. Sec. IV.A, step 4–9, p. 5–6: CIC window not deconvolved; quantify potential impact
- Problem: You state the CIC mass-assignment window is not deconvolved before taking second derivatives. Although you argue only eigenvalue ordering vs λth matters, the CIC suppression at high k can bias small-scale gradients and hence eigenvalue counts near boundaries.
- Required fix: Provide a quantitative check that deconvolving the CIC window (or using Triangular-Shaped Cloud with deconvolution) does not change class volume fractions or per-class fCW beyond quoted tolerances (e.g., re-run on a subvolume or with a coarser/finer grid and report per-class agreement). Alternately, justify with a reference plus a numerical bound.

P5-M4. Sec. IX.C, p. 25–26 (comparison to Ref. [11]): Clarify interpretive limits
- Problem: You compare volume fractions to an 800 Mpc cube analysis with different tracers and footprints and attribute discrepancies to the survey-shell geometry. This is plausible but remains qualitative.
- Required fix: Add a short quantitative bound (e.g., show that mask dilation and Rs choices move void/knot fractions by up to X pp in your pipeline; give the observed difference to Ref. [11] and state whether it is within that bound), or move the comparison to a brief footnote to avoid over-interpreting.

P5-M5. Sec. XI, Table XV: Bright vs dark catalog-level difference
- Problem: You report a 0.81 pp bright–dark difference (|z| = 1.95) but do not provide a multiple-comparison context or an effect-size interpretation here.
- Required fix: Add a brief sentence stating the family of comparisons this belongs to (systematics splits) and that 1.95σ is not significant after accounting for multiple testing; optionally report Cramér’s V for the bright/dark vs class contingency (already done elsewhere) and reference it here for consistency.

P5-M6. Length and scope
- Problem: The manuscript is 33 pages for a null-detection analysis whose primary estimand is a two-sample difference in proportions. While thoroughness is commendable, the density of internal artifact references and multiple diagnostic paths could be consolidated without loss of scientific content.
- Required fix: Consider a target of ≤ 18–20 pages for the main text plus appendices for reproducibility details, with the primary DESIVAST analysis, the T-Web cross-check, and the key systematics retained. Move the extended provenance, detailed per-NSIDE maps, and exploratory diagnostics to appendices or supplementary material.

MINOR

P5-n1. Sec. IV.A, footnote on h-units, p. 5: Clarify notation once
- Problem: The multiply-by-h convention is correct here, but the “alternative convention” language could confuse readers.
- Required fix: Replace “alternative convention” with “common confusion” and explicitly define the numeric relationship once: D[h−1 Mpc] = h × D[Mpc], so values are smaller for h < 1.

P5-n2. Sec. VIII.B, Table VIII: Add two-sided CI for ∆fCW
- Problem: You report z∆ and p∆, and the 95% CI is present in the text; include it in the table for completeness across all three algorithms (Table X already does this; mirror that style in Table VIII).
- Required fix: Add the 95% CI for ∆fCW to Table VIII (presently only given in text for the VoidFinder row).

P5-n3. Fig. 6 caption, p. 14; Table VI: State explicitly two-sided nature of pLEE
- Problem: You report “look-elsewhere p = 0.135” but do not repeat whether the max-|σ| statistic was two-sided (it is).
- Required fix: Add “two-sided max-|σ| statistic” to captions or text for each pLEE instance.

P5-n4. Minor typographical issues
- Problem: A few hyphenation and spacing inconsistencies (e.g., “σfrom half” sometimes with/without space), and occasional duplicated descriptor phrases.
- Required fix: Standardize σfrom-half notation and perform a careful proofread.

NIT

P5-nt1. Sec. VIII.A, p. 17: “This 0/6 disagreement … is consistent with the survey-shell systematic…”
- Suggestion: Add “95% one-sided CP upper bound on purity is 39%” directly in the main sentence (you compute it later), to make the statistical content explicit.

P5-nt2. Abstract, p. 1: Parentheses and abbreviations
- Suggestion: Define “pp” (percentage points) once in the abstract and avoid overloading with internal sample labels there (P5, T-Web); reserve details for the body.

Audit of key numbers in abstract and conclusions
- DESI DR1 post-cut rows 16.36 × 10^6 (Table I: 16,361,731) — consistent.
- Matched catalog 2,232,212 unique; chirality-relevant 791,635 — consistent (Table I).
- T-Web env-labeled rows 812,793; duplicates 28,973 (3.56%) — consistent (Sec. VI.A).
- Per-class fCW and σfrom-half in abstract match Table III and recompute correctly.
- Omnibus χ² = 3.55, p = 0.31 — matches Table XVI context and text.
- Phase-2 pLEE range 0.13–0.56; max residual ≤ 1.64σ (resolved cells) — consistent with Table VII.
- DESIVAST void vs non-void ∆fCW = +0.0007, z = +0.31, p = 0.76, 95% CI [−0.0036, +0.0050] — consistent (Table VIII/text).
- HEALPix p-values (0.607/0.135/0.413) — matches Table VI.
- Maximal-void correlation r = +0.006 (p = 0.88) — consistent (Sec. VIII.F/Fig. 8).
- “Selection-function-conditioned imaging-leg systematics” bright vs dark values and Cramér’s V — calculations check out.
The only abstract/body mismatch I found is the σ→p inconsistency for the Paper IV dipole (P5-E1).

Dimensional consistency and equations
- Eq. (1) σpred = 2 ∆fCW √N dimensionless — consistent. Bonferroni thresholds computed correctly for K = 4/5/9; numbers check.
- Grid/cell size: L/256 = 6,634/256 ≈ 25.9 h−1 Mpc — consistent.

Standalone-reader test
- The analysis depends on an external chirality catalog (Paper IV) “in preparation,” but the matched-sample monopole is re-estimated internally and the catalog is claimed to be publicly mirrored. This is acceptable if the catalog is version-frozen and citable; ensure a DOI is supplied (P5-E6). Do not rely on unpublished Paper IV σ/p numbers for any load-bearing claim (P5-E1).

Effect size reporting
- For large χ² (class × program), Cramér’s V is reported (0.078) — good.
- Where claiming nulls on multi-bin scans, you provide Bonferroni thresholds and MC max-stat p-values — good. Add CIs for per-class fCW where helpful (P5-M1/P5-n2).

## Summary recommendation
MAJOR REVISIONS

The numerical core is careful and largely consistent, and the main conclusions (no environment dependence within present sensitivity; DESIVAST primary null) are supported by the tabulated numbers. However, several essential corrections are required before the paper meets PRD standards: resolve contradictory p-values (redshift scan; Paper IV σ-to-p), remove version-history/artifact prose from the main text, fix/standardize the monopole-reference usage, provide a citable DOI for the frozen analysis snapshot, and either remove or correctly quantify uncertainties for the ASTRA entropy-weighted test. Addressing these, plus the listed major/minor items, will substantially improve clarity and methodological rigor.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh pass)

ESSENTIAL

P5-E8. Sec. VI.B (covariates): “100% covariate-complete” contradicts inclusion of an edge-on covariate only available for a 152,455-galaxy featured subsample
- Claim: “Extending the regression with … edge-on fraction (on the 152,455-galaxy featured subsample…) … The regression parent is the 783,741 unique env-matched spirals… the covariate-extended models retain all 783,741 (100% covariate-complete).”
- Issue: If “edge-on fraction” is only defined on the 152,455 featured subset, the full 783,741-row model cannot be “100% covariate-complete” unless the edge-on variable was omitted from that model or imputed. The text reads as if edge-on was included while simultaneously claiming no missingness on the full parent.
- Required fix: Clarify the two models explicitly: (a) full-sample model with covariates available for all objects (list them), and (b) featured-only model that additionally includes edge-on fraction (state its parent n and results). Remove the “100% covariate-complete” statement for any model that includes a covariate not defined for all rows.

MAJOR

P5-M7. Small but systematic arithmetic mismatch for σfrom-half (filament class)
- Table III/Abstract: filament fCW = 0.4980 at n = 408,187 implies σ = 2(f−0.5)√n ≈ 2(−0.0020)√408,187 ≈ −2.55, not −2.61 as quoted. Other rows (wall, void, cluster) recompute to within rounding; filament differs by ~0.06σ. Please recompute from the tabulated integers and correct the displayed σ or state the exact f (more decimals) that was used.

P5-M8. Units statement around h is presented as a “convention” but one branch is just wrong, and inconsistent numerically
- Footnote in Sec. IV.A (step 2) presents “multiply-by-h” vs “divide-by-h” as alternative conventions and even gives a numerical “divide-by-h” value (≈1246 h−1 Mpc at z = 0.2). In standard usage, values in h−1 Mpc are smaller than Mpc for h < 1: D[h−1 Mpc] = h × D[Mpc]. The “divide-by-h” branch (yielding 1246 h−1 Mpc) is incorrect, not merely an alternative. Keep only the correct mapping and remove the erroneous numerical example.

P5-M9. λth = 0 threshold depends on normalization; document the invariance you rely on
- You state the CIC window is not deconvolved and “only the ordering and sign of eigenvalues relative to λth enter the classification,” adopting λth = 0. Without deconvolution and with masked FFTs, the effective normalization can shift. The λth = 0 decision is only robust if the trace/eigenvalue sign is demonstrably preserved (e.g., Tr(T) ∝ δ in your convention). Add a brief quantitative check (e.g., empirical distribution of Tr(T) vs δ on cells) or an explicit derivation tied to your discrete normalization to justify that λth = 0 is indeed a meaningful, normalization-independent separator in your pipeline.

P5-M10. Reuse of the same RNG stream across scan families risks correlated p-values
- Sec. V: You note “the same config-level seed initializes each scan family’s generator, so identical underlying random streams are shared across families,” later adding distinct-stream re-draws agree. Best practice is to use independent seeds per family to avoid hidden correlations. Please change the default to independent seeds per analysis family and confirm the reported p-values are unchanged; otherwise, report the re-draw values as primary.

P5-M11. Catalog-native V2 “non-void” complement is not the full low-z parent; comparability should be stated
- Sec. VIII.D: The V2-REVOLVER catalog-native void sample (nvoid = 104,912) is contrasted with a much smaller non-void n = 40,877 defined by OUT=0 ∧ ZONE≥0 objects that fail VOID0≥0. This is not a partition of the full low-z parent (nlz = 678,945): it is a partition of the catalog-native GALZONE-joinable subset satisfying internal quality flags, which may have different selection than the sphere-PIS parent. Please (i) state explicitly that this “non-void” is a restricted complement within the GALZONE-joined, quality-flagged subset; (ii) confirm the conclusion is unchanged if you compare against the full low-z non-void parent (or explain why that comparison is not meaningful for this catalog-native estimator).

MINOR

P5-n5. Class-level look-elsewhere p in Sec. VI.A is presented unclearly
- Text: “(p = 0.12 free vs 0.12 stratified; [A6])”. The “free” value is repeated and appears to have a stray placeholder earlier in the sentence in some versions. Please rewrite as a single, unambiguous pair (e.g., “p = 0.12 (free-shuffle) vs 0.12 (stratified)”) and remove any leftover placeholder text.

P5-n6. Mixed unit notation “Mpc/h” vs “h−1 Mpc” appears throughout
- Standardize on a single notation in the main text and figure labels to avoid confusion (e.g., “h−1 Mpc”).

P5-n7. HEALPix sky-position proxy vs. explicit-mask usage should be mirrored in captions
- Table XI/Fig. 8: The body text explains that “0 maximal voids/pixel” is a proxy for outside-DESIVAST coverage and that you later confirm with an explicit footprint intersection. Add that caveat to the Table XI caption to prevent misinterpretation when the table is viewed out of context.

P5-n8. Minor σ-to-p wording in VIII.E
- You characterize a residual of −1.55σ as “∼1σ level” in prose. Consider stating the precise residual there (−1.55σ) to avoid downplaying the magnitude.

P5-n9. Equation/caption clarity
- For the per-pixel look-elsewhere tests (Fig. 6, Table VI), add “two-sided max-|σ| statistic” explicitly in captions for consistency with the text’s two-sided definition in Sec. V.A.

NO DUPLICATES FROM INITIAL REPORT

All items above are new relative to my prior review. I focused on fresh arithmetic recomputation, figure-caption vs body coherence, unit normalization and thresholding logic, null-procedure comparability, and subtle internal contradictions (notably the covariate-completeness claim with an edge-on variable available only on a subset).