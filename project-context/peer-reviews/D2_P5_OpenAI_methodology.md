# P5 D2 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p5_desi_chirality/paper/p5_desi_chirality.pdf` md5=b65b3ac4 pages=33
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6093 chars)
**Wall time**: 316.7s

---

Production D2 visual check (camera-ready rendering)
- All previously noted D1 issues (squished/overflowing tables, cramped or missing figures, overlapping colorbars/labels, text/equations spilling into margins, dense abstract) appear resolved. Current tables render full width with adequate line spacing; figures have legible axis fonts, non-overlapping colorbars and labels, and adequate white space.
- No new visual regressions detected: no bad float placement, no half-blank pages, no orphaned headings, no text running into margins or adjacent columns.
- Page-level notes:
  - Pages 4, 6, 9, 11, 14, 16, 20, 22, 26: figures are clear, axes labeled, captions match the body claims.
  - Tables I, II, III, IV, V, VII, VIII, IX, X, XI, XII, XIII, XIV, XVI, XVII, XVIII render cleanly; no column wrap or math overflow.
  - One typographic nit: the footnote marker “a” on p.2 spills its sentence end across the page break (“with Φ … from Poisson’s equation”) but remains readable.

Methodology and statistical referee report (PRD standards)

ESSENTIAL items
P5-E1 (Abstract + throughout; pages 1–2, 3, 8, 21, 30–31)
Problem: Heavy dependence on a “companion” Paper IV (in preparation) for the primary chirality labels and the catalog-wide monopole (ΔfCW ≈ −0.0026) that is used repeatedly as a reference and subtracted in many tests. The present paper cannot be independently reproduced or fully assessed without the core classifier description, training/validation details, and the statistical provenance of the monopole reported in that companion. Version language (“Paper IV v1.0.166”) is also cited in the body.
Required fix: Make the paper self-contained for PRD. Either (a) include a concise but complete methods summary of the chirality classifier (architecture, training set, augmentation, label definition, performance metrics, calibration to remove mirror bias) and a rigorous, self-contained derivation of the global ΔfCW monopole with its uncertainty; or (b) convert to a two-paper submission with the companion accepted and citable, and rewrite all dependencies here as standard citations without version-history prose. Remove version tags from the narrative; if keeping code/data tags, move them to Data Availability only.

P5-E2 (Section V, Eq. (1), page 6)
Problem: Ambiguous typography in the predictive σ formula. It reads “σpred = ∆fCW 0.5/√N = 2 · ∆fCW · √N”. As written, the first term lacks an explicit division and is easy to misread.
Required fix: Typeset unambiguously as σpred = ∆fCW ÷ (0.5/√N) = 2 ∆fCW √N, or σpred = (∆fCW)/(0.5/√N). Ensure the same denominator convention matches the earlier definition σfrom half = (nCW − 0.5N)/(0.5√N).

P5-E3 (Sections VI A, VII, VIII F; pages 8–9, 15–16, 20–21)
Problem: Throughout, residuals “σobs − σpred” are used for inference against the catalog-monopole model. The text notes that the monopole estimate itself carries uncertainty (leading to ≈0.36–0.7σ uncertainty on σpred at class sample sizes), but that uncertainty is not folded into any formal test or bound; yet residual maxima of 1.64σ are interpreted as null findings.
Required fix: Either (a) incorporate the monopole-parameter uncertainty into the residual test (e.g., treat σpred as a normal with the propagated variance and report posterior predictive p-values or broadened acceptance bands), or (b) explicitly reframe every residual-based statement as descriptive only and move the formal hypothesis testing to the permutation pLEE and contingency χ2 results. Add a single consolidated paragraph near first use (Sec. V) and a reminder in Sec. VII that residuals within ≲0.7σ are inside the monopole-uncertainty floor.

P5-E4 (Section VI D, tracer-program split; pages 11–12)
Problem: The reported filament bright vs dark “two-sample |z| ≈ 2.1” is computed at the row level where samples are not disjoint (the same TARGETID can appear in both splits). The paper acknowledges this but still presents a z that assumes independence.
Required fix: Recompute the bright–dark contrast using unique TARGETIDs per class or a paired/stratified analysis that correctly handles overlap (e.g., McNemar or GEE), and report that result. If sample size precludes per-class clean splits, remove the per-class z and retain only the catalog-level unique-galaxy result (|z| = 1.95) with an explicit caveat.

P5-E5 (Abstract-last drift; pages 1–2 vs body)
Problem: Abstract claims “Phase 2 sensitivity sweep: per-cell label-shuffle look-elsewhere p-values span 0.13–0.56 (no cell below 0.05), … Rs=10 Mpc/h cells sit below the 25.9 Mpc/h grid resolution and are retained only as a degenerate near-unsmoothed limit.” In the body (Table VII, p.15) the Rs=10 cells are shown and one has p=0.56; the text later excludes Rs=10 from robustness. The abstract should mirror that caveat explicitly to avoid overstating the sweep’s resolved coverage.
Required fix: In the abstract, add “excluding under-resolved Rs=10 cells” to the p-value sweep claim, or report the ranges separately for resolved cells (Rs ∈ {25, 50}) and for Rs=10.

MAJOR items
P5-M1 (Appendix A, pages 30–31)
Problem: Toy EFT operator mapping is not gauge invariant and introduces a coordinate (ẑ) dependence; while caveats are noted, this section can be misread as a derived constraint. It is not supported by a calculation linking the operator to the measured ΔfCW.
Required fix: Move Appendix A to Supplemental Material or drastically condense to a brief qualitative remark in the Discussion, emphasizing that it is a speculative parametrization and explicitly not a constraint. Remove the appearance of a numerical “bound” unless backed by a proper forward model.

P5-M2 (Claims of “largest to date”, Sec. VIII B, page 18)
Problem: “To our knowledge, the largest matched-sample environmental-dependence test … in DESI DR1 to date” is asserted without a comparative citation.
Required fix: Provide specific, citable comparators (sample sizes and scope) or soften to “a large matched-sample …” without the superlative.

P5-M3 (Primary/secondary declaration, Sec. V B, page 7)
Problem: The designation of DESIVAST as “primary” and T-Web/others as “secondary” is post hoc by admission. While the handling is transparent, PRD expects a pre-declared primary estimand and analysis plan for multiple-testing contexts.
Required fix: Sharpen the pre-specification: clearly define the single primary estimand (void vs non-void ΔfCW) and the controlling family (Bonferroni-5) at first mention in the Introduction, and move exploratory elements to a dedicated “Exploratory analyses” section.

P5-M4 (Permutation NMC = 1000, Sec. V A; applied in Secs. VI, VII; pages 6–7, 15)
Problem: Several permutation p-values are reported with 2–3 decimals (e.g., 0.135, 0.372). With NMC=1000 the MC standard error is ≈0.01–0.02; some quoted claims (e.g., “stream-independent within the NMC standard error”) are fine, but the text sometimes uses these p’s as sharp thresholds.
Required fix: Annotate each family of permutation results with its MC resolution (±seMC), or round p-values accordingly (two decimals). Where close calls could occur, increase NMC (e.g., to 10,000) or state explicitly that no result was near 0.05 so NMC=1000 suffices.

P5-M5 (RSD treatment claims, Sec. XIII and Sec. VIII, pages 16, 29)
Problem: The paper asserts the primary DESIVAST void/non-void result is “RSD-bounded” and supports stability with a per-galaxy LOS Gaussian shift Monte Carlo. While informative, this is a fixed-void-geometry sensitivity, not a full RSD treatment.
Required fix: Rephrase to avoid implying RSD robustness beyond membership sensitivity at fixed void geometry. Add a one-sentence quantitative bound from the Monte Carlo in the main text of Sec. VIII (you have ranges; cite them prominently), and defer any claim about non-void subclass composition under RSD.

P5-M6 (Version/provenance language in main text, multiple pages)
Problem: Internal version markers (e.g., “Paper IV v1.0.166”, “manuscript tag v0.1.83-2026-06-19”) and artifact IDs [A#] appear in the narrative.
Required fix: Keep artifact IDs and Git tags only in a consolidated Data/Code Availability section and appendices. Remove version-history prose from the Introduction/Methods. PRD readers should not see internal versioning in the main text.

P5-M7 (Length and redundancy)
Problem: At 33 pages, the paper contains repeated statements of the main null, lengthy restatements of thresholds, and multiple similar stratifications.
Required fix: Reduce by ~20–25% by moving detailed stratification reprises to an Appendix and tightening repeated narrative (e.g., consolidate the multiple recountings of the catalog-monopole caveat).

MINOR items
P5-m1 (Eqn and units clarity; pages 5–6, 7–8)
- Ensure consistent notation for h−1 Mpc vs Mpc/h (both appear). The multiply-by-h convention footnote is good; add a single, early “Units” sentence in Sec. IV to standardize.

P5-m2 (HEALPix scans; pages 12–14)
- Where pLEE values are given per NSIDE, also report the number of occupied pixels (npix) in the caption rather than only in the table.

P5-m3 (Fig. 6 caption; page 14)
- State explicitly that the σ map is relative to 0.5, and that the per-pixel counts are ≥200 spirals, to match the body.

P5-m4 (Footnote break; page 2–3)
- Minor typography: the author-line footnote “a” splits mid-sentence (“with Φ … from Poisson”). Consider reflow to keep the full sentence on one page.

P5-m5 (Table VII; page 15)
- Shade or grey out the three under-resolved Rs = 10 rows to visually reinforce the caveat that these are not part of the robustness claim.

P5-m6 (Consistency of decimal places)
- Standardize the precision for fCW to four decimals in tables, and for σ to two decimals, across all tables.

NITs
P5-n1 (Wording)
- Replace “monopole leaks through” with “reflects the catalog-level monopole” (pages 8–9) to avoid colloquialism.
P5-n2 (Typos)
- “iden￾tical” hyphenation artifacts appear due to line breaks (e.g., pages 6–7). Ensure camera-ready copy removes soft hyphen remnants.

Arithmetic and internal-consistency audit (spot checks)
- Table III σ-values recomputed with σ = 2(f − 0.5)√N: filament −2.61 (N=408,187, f=0.4980), cluster −4.66 (397,505; 0.4963), wall +0.55 (6,673; 0.5034), void −0.68 (428; 0.4836): all match.
- Range across classes = 0.5034 − 0.4836 = 0.0198 = 1.98 pp: matches.
- Omnibus 4×2 χ2 (Table XVI) consistent with χ2 = 3.55, 3 d.o.f., p = 0.31; unique-TARGETID recompute (χ2 = 3.00, p = 0.39) plausible and consistent with row-level inflation discussion.
- Density-quintile prediction σpred = 2(−0.0026)√158,327 = −2.07, observed σs track within ≲1.9 as claimed.
- DESIVAST void vs non-void: Δf = 0.00067, SE = 0.00219 (pooled two-sample), z = 0.31, p = 0.76; 95% CI [−0.0036, +0.0050]: consistent.
- V2-REVOLVER/V2-VIDE two-sample SEs and z’s recompute to within rounding.
- Bonferroni thresholds: K=5 at α=0.05 gives |z|=2.575, reported 2.58; K=9 gives 2.77; K=4 at α=0.05 gives 2.50: all correct.
- Permutation NMC=1000 seMC = sqrt(p(1−p)/1000) ~ 0.01–0.015 for p in [0.1, 0.5]: consistent with stated precision.
- Cramér’s V for χ2=4933, n=811,609: V = sqrt(χ2/n) ≈ 0.078: correct.

Standalone-reader test
- The T-Web implementation is sufficiently described; selection-function and boundary caveats are candid. However, the paper is not fully standalone due to reliance on the (unpublished) chirality catalog and its global monopole. See P5-E1.

Effect sizes and practical significance
- Where large χ2 arises from sample size (program × class; V=0.078), the paper already reports Cramér’s V; good.
- For all nulls, the paper typically pairs σ/p with effect-size statements (e.g., percentage-point differences and counting floors); good.

Data/Code availability and provenance
- Rich provenance with GitHub repo and artifact IDs. Consolidate version tags to this section (P5-M6). Add an archival DOI (Zenodo) reference in the text (you mention it will accompany submission; include the DOI once minted).

## Summary recommendation
MAJOR REVISIONS

The statistical and computational methodology is, on the whole, careful and well documented, and the null conclusions are supported by multiple cross-checks. However, acceptance in PRD requires the paper to be self-contained and free of internal versioning prose. The heaviest blocker is the reliance on an unpublished companion for the primary labels and the catalog monopole that underpins many inferences. Clarify Eq. (1), correct the overlapping-sample test for bright/dark splits, temper or relocate the speculative EFT appendix, tighten the treatment of monopole-uncertainty in residual-based statements, and streamline presentation. With these revisions, the paper could be suitable for publication.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS (fresh-eyes pass)

P5-E6 (Sec. VIII A, one-sided Clopper–Pearson bound; page 17)
Problem: The 95% one-sided upper bound for 0/6 “successes” is typeset as “1 − 0.051/6 = 39%” and later as “1 − α 1/n.” As written, “0.051/6” reads as 0.05 divided by 6, not 0.05 to the 1/6 power.
Required fix: Correct the typography to the intended 1 − 0.05^(1/6) ≈ 39.3%, and standardize the general form as 1 − α^(1/n). This both avoids misinterpretation and matches the quoted 39%.

P5-M8 (Table IX; program split completeness; page 18)
Problem: The “bright/dark target-program split” table lists only bright and dark rows for the void and non-void classes, but the totals in each class do not sum to the corresponding class totals because “backup” and “other” programs are omitted (e.g., void: 56,477 + 469 = 56,946 < 56,981; non-void: 615,078 + 5,845 = 620,923 < 621,964).
Required fix: Either (a) add the backup and other rows, or (b) label the table and paragraph explicitly as “bright/dark only” and note the residual counts (35 and 1,041, respectively), so readers do not infer a mismatch.

P5-m7 (LEE thresholds; mixed α-levels; Sec. V A, and scan results throughout)
Problem: The empirical max-statistic permutation family is evaluated at pLEE < 0.05 (family-wise), while the parametric Bonferroni thresholds are presented at α = 0.01. The text says “the two return the same verdict,” but the α levels differ, which can confuse readers about the decision criterion.
Required fix: Harmonize the α levels or explicitly justify why the empirical control is at 0.05 and the parametric display at 0.01. Alternatively, present both at the same α (e.g., 0.05) and note that results are even safer under 0.01.

P5-m8 (Statistic name/definition drift; Sec. IX A, selection-corrected run; page 23)
Problem: The phrase “every class within |σ| ≤ 0.39 of the sample monopole” is ambiguous: it reads like a raw |σfrom half|, but context suggests you mean the monopole-referenced residual (σvs monopole).
Required fix: Replace with the defined term and statistic, e.g., “every class has |σvs monopole| ≤ 0.39,” and reference the exact denominator convention (0.5/√N) as done elsewhere.

P5-m9 (Units notation in footnote vs main text; Sec. IV A, footnote 1; page 5)
Problem: The footnote carefully explains the multiply-by-h convention, but then calls χ[h−1 Mpc] = χ[Mpc]/h an “alternative convention,” which is simply incorrect for converting a numeric value expressed in Mpc to h−1 Mpc. While the subsequent worked example is correct, the wording risks confusion.
Required fix: Rephrase to: “Some code bases internally store distances in different unit systems; here we convert numeric values from Mpc to h−1 Mpc by multiplying by h.” Remove the “alternative convention” phrasing to avoid implying both are acceptable.

P5-m10 (Consistency of symbols; Sec. IV A step 12 and elsewhere)
Problem: The text alternates between “log-density,” “log10(1 + δsmooth),” and “linear density” without always restating that the monotone transform preserves rank order for binning. Readers could miss that quartile bin edges are identical under either transform.
Required fix: At first use (step 12) add: “All within-class density binning uses the rank order of this covariate; because log10(1+δ) is monotone in δ, quartiles are invariant to the transform.”

P5-m11 (Comparability caveat for selection-corrected vs canonical σ)
Problem: In the selection-corrected classifier check (Sec. IX A), σfrom half values (e.g., wall −2.51, filament −3.73, cluster −2.33) are presented adjacent to canonical-run σ, but only briefly caveated that shell-mean subtraction whitens the field. Different class populations after re-labeling change the σ scales.
Required fix: Add a one-sentence reminder that σfrom half scales with √N and that the selection-corrected class Ns differ substantially (void 428 → 4,353; cluster 397,505 → 181,352), so raw σ are not directly comparable across builds; inference comes from the omnibus χ2 and σvs monopole residuals.

P5-m12 (Precision/units for tiny pp shifts; Sec. IV A step 4; page 5)
Problem: The text mixes percentage-point magnitudes at very different scales in one sentence: “per-class fCW moves by at most 0.23 pp (the small wall class; filament −0.005 pp, cluster +0.013 pp).” Values like 0.005 pp (=5×10−5 in fraction) are below the meaningful resolution given the class counts and MC precision.
Required fix: Either round consistently (e.g., report all fCW shifts to 0.01 pp) or move the sub-0.01 pp values to an appendix. Clarify that these are negligible compared to the counting floor.

P5-m13 (Caption clarity; Table VII and Fig. 7)
Problem: The body text rightly excludes Rs=10 as under-resolved; Table VII footnote does state this, but the visual (and the Fig. 7 heatmap) does not make the exclusion obvious.
Required fix: In the heatmap, hatch or mark the Rs = 10 row, and in Table VII add a column flag (e.g., “resolved? yes/no”) or a greyed style, matching the text caveat.

P5-m14 (Explicit npix for HEALPix scans; Sec. VI E captions)
Problem: While Table VI lists npix, the map figure captions don’t restate the npix used for the σ maps. Given different pixel selections (e.g., ≥200 spirals; ≥1 void), readers may lose track of counts.
Required fix: Add “npix = …” and the selection criteria (“≥200 spirals”) directly in the figure captions for the σ maps, matching the body text and Table VI.

Rationale
These items were not covered in the initial review and surfaced on a second, line-by-line pass with calculator in hand and by reconciling captions, tables, and body text. Most are clarity/typography and bookkeeping issues that can be fixed without rerunning the analysis but will prevent reader confusion and ensure strict PRD-style rigor. The Clopper–Pearson exponent typo (P5-E6) is the only place where a formula, as typeset, is mathematically wrong even though the numeric value quoted is right. The remaining items tighten completeness (program splits), consistency (α levels, statistic naming), and presentation (units, captions, and negligible pp shifts).