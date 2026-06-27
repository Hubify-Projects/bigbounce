# P5 R57 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/private/tmp/R57_P5/p5_desi_chirality.pdf` md5=034b7bc0 pages=33
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (4727 chars)
**Wall time**: 320.3s

---

Referee report on “Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T‑Web (Hahn 2007) Tidal‑Tensor Cross‑Check Across the DR1 Matched‑Spiral Sample”

Scope of review
- Role: Methodology/statistics rigor, internal arithmetic, dimensional analysis, significance control, reproducibility.
- I audited every equation, table, and figure against the text and re-computed quoted σ, p, ratios, and ranges where possible from the provided counts.

Overall
- The statistical framework is generally sound (explicit definition of σfrom half, clear two-sample contrasts, Jeffreys intervals, permutation LEE controls, Bonferroni thresholds). Many numbers are internally consistent when recomputed from tables, and the paper repeatedly cautions about non-comparability of σ across bins of different N.
- However, there are several issues that must be corrected for PRD standards, chiefly: (i) version-history and code-artifact language in the body, (ii) a typesetting error that turns a power into a division in a one-sided binomial bound, (iii) reliance on an unpublished “Paper IV” for the core classification without providing a stable DOI and a self-contained minimum-methods description in this manuscript, (iv) the canonical T-Web run uses a global mean without completeness weighting even though the selection-corrected run changes class populations substantially; headline T-Web statements should be anchored on the corrected classification or clearly separated as “diagnostic only”.

Findings

ESSENTIAL

P5-E1 (Section VIII A; page 17)
Problem: Mis-typeset binomial bound: “with 0 of 6, the one-sided 95% binomial upper bound on the true in-hole fraction is 1 − 0.051/6 = 39% (the standard one-sided Clopper–Pearson bound 1 − α1/n for 0 successes in n trials...)”.
Issue: “0.051/6” reads as 0.05 divided by 6; the intended expression is 0.05^(1/6). This is an arithmetic/typographical error in a quantitative statement.
Required fix: Replace “1 − 0.051/6” with “1 − 0.05^(1/6) = 39.3%” (one-sided Clopper–Pearson bound for 0 of 6). Verify all exponent notations elsewhere.

P5-E2 (Sections IV A footnote on nomenclature, several places; pages 5, 7, 16–22, 31–32)
Problem: Version-history and internal bookkeeping language in the body. Examples:
- “earlier preprint versions used the ‘V-Web’ label loosely ... and this version standardizes on ‘T-Web’” (Sec. IV A).
- Multiple references to “committed implementation [A3] ... lines 106–108”, “artifact filename [A3] ... retained for backward compatibility”, etc.
Issue: PRD forbids version-history commentary and internal repository-path/line-number language in the main text.
Required fix: Remove all version-history commentary and code/line-number references from the main text. Move such details to a Supplemental Material “Reproducibility” section with a stable DOI.

P5-E3 (Appendix C; page 31–32; throughout)
Problem: Load-bearing data/methods (chirality labels and the global “monopole” offset) depend on an unpublished companion “Paper IV”. The text states “catalog is on HuggingFace” and “a DOI-minted archival snapshot accompanies submission” but no DOI is provided in the manuscript. Several main-text inferences (e.g., σpred lines, Figure references) rely on the Paper IV monopole ∆fCW = −0.0026 as a known constant.
Required fix:
- Provide a stable, citable DOI for the chirality catalog and the analysis code snapshot referenced throughout (not just a GitHub path or a promise).
- Add a concise, self-contained methods paragraph in this manuscript summarizing the classifier used for chirality (architecture, training set, parity-augmentation, confidence score, basic QA metrics), so the paper is readable without the companion paper. Where σpred uses an external ∆f from Paper IV, either (a) anchor statements on the internally measured matched-sample monopole fP5CW with its propagated uncertainty, or (b) keep using the Paper IV number but explicitly state and propagate its uncertainty in every place where predictions are compared to observed σ (you already do this in Sec. V; ensure consistency and that no conclusion depends on the external value).

P5-E4 (Sections VI A and VII; multiple pages)
Problem: The canonical T‑Web classification is computed against a global mean density without completeness weighting or radial selection correction, which the authors themselves show leads to substantial reallocation of class populations when a selection-corrected rebuild is performed (void 428→4,353; cluster 397,505→181,352; §IX A). While the headline qualitative conclusion is unchanged, many statistics and visuals emphasize the canonical map.
Required fix: Promote the selection-corrected classifier to the mainline T‑Web result where environment-dependent chirality is summarized (or present both side-by-side but explicitly identify the corrected one as the baseline). At minimum:
- Move the 4×2 homogeneity result (χ^2 = 0.11, p = 0.99) and the per-class fCW values for the selection-corrected run into the main Results section and clarify that quantitative T‑Web conclusions (ranges, class-by-class σ) are identical or tighter there. Clearly label the uncorrected run as “diagnostic; selection-shaped”.

MAJOR

P5-M1 (Abstract vs. Sections V–VIII; pages 1–3, 8–22)
Problem: Primary estimator pre‑declaration. The paper acknowledges that the primary path (DESIVAST-anchored ∆fCW) was designated post hoc (Sec. V B). While good transparency is shown and Bonferroni accounting is explicit, PRD requires that headline claims not be subject to garden‑of‑forking‑paths concerns.
Required fix: Tighten the abstract and Results to explicitly state up front that the DESIVAST-anchored two-sample ∆fCW is the pre-specified headline estimand for this paper and that all other analyses are secondary diagnostics. Move the “pre‑registration caveat” paragraph into Methods and reflect this designation in the abstract’s ordering. No change in numbers is needed; this is to prevent misinterpretation.

P5-M2 (Tables III/XVI; page 8–9 and Appendix B page 31)
Problem: Minor inconsistency between printed fCW (rounded to 4 decimals) and the exact counts. Example (filament): n=408,187; CW=203,261 → fCW=203,261/408,187=0.49845, printed as 0.4980; σfrom half is computed from counts (−2.61). The displayed f truncation can mislead when compared to σ.
Required fix: Print fCW to at least four significant digits consistent with the counts (e.g., 0.4985) or include a note “rounded; σ computed from counts” in the table caption.

P5-M3 (Section VII; page 13–16, Table VII)
Problem: Three Rs=10 Mpc/h sweep cells are below the 25.9 Mpc/h grid sampling scale; yet they are tabulated with pLEE and max residuals. The authors note they are excluded from the robustness claim, but their inclusion distracts and risks misinterpretation.
Required fix: Move the Rs=10 rows to a footnote or Supplementary Table and clearly mark them as “grid‑unresolved; for completeness only”. Keep the six resolved cells in the main table.

P5-M4 (Reproducibility; Appendix C and artifact references throughout)
Problem: The manuscript depends heavily on clickable GitHub artifacts ([A1]–[A30]); PRD requires a stable archival record. The text states that a DOI snapshot “accompanies journal submission” but provides no DOI. Some statements cite code line numbers and internal paths.
Required fix: Provide a single Zenodo (or equivalent) DOI for the exact snapshot used to generate all results and update all [A•] references to point to that DOI in a consolidated “Supplemental Material” index. Remove/relocate code line numbers from the main text.

MINOR

P5-n1 (Section V A; page 6–7, Eq. 2 and surrounding text)
Problem: Slight inconsistency in wording about two‑sided Bonferroni. The formula |σ|Bonf = √2 erfc−1(α/K) is correct for two‑sided control, but the preceding sentence mentions “each tail contributes α/2K”. This can confuse readers.
Required fix: Clarify explicitly that erfc already encodes two tails, so the two‑sided per‑family α becomes erfc argument α/K.

P5-n2 (Section IV A footnote on units; page 5)
Problem: The multiply-by-h convention for reporting χ in h−1 Mpc is nonstandard in prose and may confuse some readers.
Required fix: Add a short parenthetical “Numerically, χ[h−1 Mpc] = h × χ[Mpc]; e.g. 843 Mpc → 570 h−1 Mpc for h=0.6766” and remove the alternative-convention digression to avoid confusion.

P5-n3 (Section VI D; page 10–12)
Problem: The within-class density quartile table (Table V) lists “ρ̄” values on a log10 scale; the text clarifies later, but readers may miss that these are log10(1+δ) values.
Required fix: Add “log10(1+δsmooth)” directly in the column header or footnote.

P5-n4 (Section VIII E; page 20)
Problem: The term “per‑cap join values” appears to be a typo for “per‑capita” or “per‑cap”.
Required fix: Correct phrasing.

P5-n5 (Throughout)
Problem: Use of colloquial phrases (“garden-of-forking-paths”, “load‑bearing”) in the main text.
Required fix: Replace with standard technical wording.

P5-n6 (Length; entire manuscript, 33 pages)
Problem: The contribution is a carefully executed null test with extensive diagnostics; 33 pages is long for the main text at PRD.
Required fix: Condense the main text to ≤ 20 pages by moving secondary diagnostics (e.g., detailed HEALPix re-draw comparisons, RS=10 sweep cells, some ancillary sky-stratification plots/maps) to Supplemental Material. Keep the DESIVAST void analysis, the corrected T-Web analysis, and the key null tests in the main text.

NITS

P5-N1 (Figure/Table labeling; multiple pages)
Problem: Sometimes “pp” (percentage points) is used without definition; some readers may misread as percent.
Required fix: Define “pp = percentage points” once in Methods and/or use “percentage points (pp)” on first use.

P5-N2 (Bibliography; page 33)
Problem: Ref. [11] labeled “preprint (2026), arXiv:2604.02463” and [12] are contemporaneous but not peer reviewed. The text correctly treats them as concurrent. Ensure that any claims of validation remain caveated (they mostly are).
Required fix: No change in math; keep caveats explicit when invoking [11]/[12].

Recomputations and cross-check highlights
- Table III σfrom half values recompute exactly from the integer counts in Appendix B (filament −2.61, cluster −4.66, wall +0.55, void −0.68). The range 1.98 pp matches 0.5034 − 0.4836.
- Omnibus χ^2 = 3.55, 3 d.o.f., p ≈ 0.31 is consistent with counts in Table XVI.
- σpred = 2 ∆fCW √N with ∆f = −0.0026 gives ≈ −3.3 for classes with N ≈ 4×10^5, consistent with the observed raw σ and the residuals reported.
- DESIVAST primary: ∆f = +0.00067; SE ≈ 0.00219; z ≈ +0.31; p ≈ 0.76 (from Table VIII).
- V2-REVOLVER and V2-VIDE sphere-PIS contrasts’ SE and z recompute from counts (Table X).
- HEALPix per-pixel correlation r=0.006 (n=727) gives t ≈ 0.16, p ≈ 0.87–0.88, consistent.
- Density-quintile σobs vs σpred residuals (Table IV) recompute within rounding; max |σobs − σpred| ≈ 1.87, below Bonferroni-5 3.09.
- Bonferroni thresholds quoted are numerically correct for the stated K and α.

Effect sizes and interpretation
- The authors appropriately qualify that σfrom half scales as √N and is not comparable across classes, and they introduce σvs monopole residuals to compare across classes. They also provide Cramér’s V for the large contingency (V=0.078; for 4×2, the divisor min(r−1,c−1)=1 so the stated V=√(χ^2/n) is correct).
- The primary effect size ∆fCW in DESIVAST voids is +0.0007 with 95% CI [−0.0036, +0.0050]; this is reported transparently.

Standalone-reader test
- The paper remains partially dependent on the unpublished Paper IV for the chirality labels and the catalog-wide “monopole”. The authors do measure an internal matched-sample monopole and propagate its uncertainty in several places, but σpred calculations still reference the external ∆f. A minimum self-contained description plus a stable DOI is required.

Abstract-last drift sweep
- I checked each scalar in the abstract against the body: all headline numbers (N, fractions, σ, χ^2, p-values, ranges) are traceable to tables/sections and consistent within rounding. The abstract correctly states that the controlling void constraint comes from the DESIVAST-anchored re-projection (n=56,981, ∆=0.0007) rather than T-Web’s n=428 void bin, and it carries the redshift-space caveat consistent with §XIII.

## Summary recommendation
MAJOR REVISIONS

The statistical machinery is generally careful and internally consistent, and the primary DESIVAST two-sample contrast is a clean, well-powered null. However, for PRD standards the paper must (i) remove version-history/code-artifact language from the main text, (ii) correct the mis-typeset binomial bound, (iii) provide a stable DOI and a minimal, self-contained description of the chirality classifier used (to reduce reliance on an unpublished companion), and (iv) anchor T‑Web headline statements on the selection‑corrected classification (or clearly demote the uncorrected run to a diagnostic). After these are addressed and some condensation of secondary diagnostics to Supplemental Material, the paper would be suitable for reconsideration.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes pass)

Scope note: I re-checked arithmetic, caption/body consistency, units, cross-references, null comparability, abstract faithfulness, novelty claims, hedges, appendix/main alignment, and stale numbers. Items below are new relative to my prior report.

ESSENTIAL

P5-E5 (Section IX A; interior-buffer counts)
Problem: Two different removal counts are reported for the interior-buffer excision without a clear baseline.
- “retains 782,015 of the 783,820 unique env-matched spirals” (implies 1,805 removed)
- “interior-buffer variant (1,862 spirals removed)”
These appear in the same subsection and can be read as referring to the same operation.
Required fix: Disambiguate which figure applies to the canonical vs selection-corrected rebuild, and state the explicit parent N for each. If both apply to different builds, label them as such in-text; otherwise correct the stale number.

MAJOR

P5-M5 (Section VI D; VI A; regression and two-sample inferences with duplicates)
Problem: Several inferential procedures (notably the program-controlled logistic regression in §VI D and some per-class two-sample z-tests) are run on the env-labeled row-level parent, where some TARGETIDs appear more than once (multi-program coadds). Although you note this caveat for a two-sample statistic in §VI D, the regression SEs and z-values themselves are not adjusted for clustering by TARGETID.
Required fix: For any regression or two-sample test run on the row-level parent, either (i) deduplicate to one row per TARGETID before inference, or (ii) report cluster-robust (TARGETID-clustered) standard errors/z for regression coefficients and use paired/clustered two-sample tests. Explicitly state which option is used.

P5-M6 (Section VIII B/Table VIII; void membership k=20 vs exact)
Problem: The primary DESIVAST void/non-void contrast in Table VIII is reported for the k = 20 KDTree query, while you also show that 28% of galaxies have >20 candidate holes and that the exact k‑unbounded rerun changes membership for 100 galaxies (0.18%) and nudges ∆fCW slightly (to +0.0006).
Required fix: For the load-bearing DESIVAST result, publish the exact (k-unbounded) counts/∆/SE/z in the main table, and relegate the k=20 approximation to Supplemental. This avoids any perception that an approximation underlies the headline statistic.

P5-M7 (Section XV; novelty phrasing)
Problem: The statement “to our knowledge, the largest matched-sample environmental-dependence test … in DESI DR1” is not supported by an explicit comparison or citation.
Required fix: Either provide a brief literature comparison (sample sizes and scope) demonstrating this claim, or soften to a descriptive phrasing without a novelty superlative.

MINOR

P5-n7 (Section IV A step 5 vs §IX A; in-mask cell count drift)
Problem: Two slightly different in-mask cell counts appear:
- “3,150,086 in-mask” (Sec. IV A, step 5)
- “3,150,089 in-mask” (§IX A)
Required fix: Harmonize the number or add a parenthetical explaining that the latter comes from a separate rebuild (and why it differs by 3 cells).

P5-n8 (Figures 3 and 4 captions vs Methods)
Problem: Captions refer to “95% binomial confidence intervals” while Methods specify Jeffreys 95% binomial credible intervals. The procedures are different in principle.
Required fix: Use consistent terminology (“Jeffreys 95% binomial credible intervals”) in captions, or explicitly say “Jeffreys 95% binomial credible intervals” everywhere they are plotted.

P5-n9 (Table X note; sign conventions)
Problem: The note “the committed artifact stores the opposite-signed fvoid − fnon-void values” is an internal-repo detail in a main-text table.
Required fix: Move this repository remark to Supplemental/Reproducibility material. In the main text, keep only the sign convention used in the paper.

NITS

P5-N3 (Figure 8 top caption vs body resolution)
Problem: Caption uses NSIDE = 32 (885 occupied pixels) while §VIII E lists NSIDE = 16 (297 occupied pixels) for the table, which could confuse readers skimming figures.
Required fix: Add a one-line clarifier in the caption that the main-table stratification uses NSIDE = 16 while the map is shown at NSIDE = 32 for visualization.

P5-N4 (Typos)
Problem: “per‑cap join values” in §VIII D appears to be a typo.
Required fix: Replace with “per‑catalog” or remove “per‑cap”.

Explanation
Most arithmetic in tables and quoted statistics re-computes correctly from the provided counts (I spot-checked all that are reconstructible). The new issues above are chiefly consistency/stability and inference-robustness items that became apparent on a second pass, plus one instance where the exact statistic should replace an approximation in the main table.