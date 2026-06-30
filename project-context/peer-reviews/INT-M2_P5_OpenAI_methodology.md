# P5 INT-M2 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p5_desi_chirality/paper/p5_desi_chirality.pdf` md5=503d4e5b pages=34
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6198 chars)
**Wall time**: 378.9s

---

Referee report on “Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T-Web (Hahn 2007) Tidal-Tensor Cross-Check Across the DR1 Matched-Spiral Sample”

Scope of review
- Journal: Physical Review D (methods)
- Focus of review: statistical/methodological rigor, internal arithmetic consistency, dimensional analysis, error propagation, and alignment of abstract/conclusions with demonstrated results.

Overall assessment
The manuscript presents a careful environment-conditional null test of spiral galaxy chirality using DESI DR1, combining a deterministic T-Web classifier with a DESIVAST void-based re-projection and multiple robustness checks. The analysis is unusually transparent: statistics are defined explicitly, σ-from-half and monopole-referenced residuals are separated, multiple-testing is handled (Bonferroni and empirical max-stat permutation), and nearly every scalar in the abstract is traceable to a table/section with correct arithmetic. The main conclusions (null dependence of chirality on environment within the stated precision; the DESIVAST-anchored primary null; and identification of a catalog-wide classifier monopole) are supported by the computations shown.

I verified the load-bearing numbers in the abstract and conclusions against tables and text:
- DR1 ZWARN=0 row count 16,361,731 is consistent with the stated selections (§III B, Table II).
- Matched unique spirals 791,635; env-labeled parent 812,793 rows covering 783,820 unique spirals (3.56% duplicates) are consistent (§VI A, §VIII F).
- T-Web per-class fCW values and σ-from-half in the abstract match Table IV; the class-range 1.98 pp equals 0.5034 − 0.4836.
- The void-bin counting floor at n = 428 is 1/(2√n) ≈ 2.42 pp (1σ), so a 1.64 pp offset corresponds to 0.68σ as stated.
- DESIVAST primary: VoidFinder point-in-sphere nvoid = 56,981, fvoid = 0.4964 vs non-void 0.4971 gives ∆ = +0.00067, SE ≈ 0.00219, z ≈ +0.31, p ≈ 0.76 — matches Table IX/XI.
- Three-algorithm DESIVAST sphere-PIS contrasts in Table XI recompute to the listed SE, z, and p.
- HEALPix LEE p-values (NSIDE 16/32/64) match Table VII; Phase-2 cell pLEE match Table VIII.
- Cramér’s V from the class×program χ2 matches 0.078.

I list below a small number of concrete issues that should be addressed prior to acceptance. Only one is an outright formula error; the rest are clarity/citation/reproducibility issues.

Findings

ESSENTIAL

P5-E1 — §VIII A, p. 18: Clopper–Pearson upper bound formula and numeric illustration are wrong as written
- Text: “With 0 of 6, the one-sided 95% binomial upper bound on the true in-hole fraction is 1 − 0.051/6 = 39% (the standard one-sided Clopper–Pearson bound 1 − α1/n for 0 successes in n trials at confidence level 1 − α)”
- Problem: The displayed “1 − 0.051/6” is dimensionally/arithmetically incorrect and does not equal 39%. The correct Clopper–Pearson one-sided 95% upper bound for 0 successes in n trials is pU = 1 − α1/n with α = 0.05, i.e., 1 − 0.05^(1/6) ≈ 0.393.
- Required fix: Replace “1 − 0.051/6 = 39%” by “1 − 0.05^(1/6) ≈ 0.393 (39%)” and keep the parenthetical formula as written. Ensure the same correction is propagated anywhere else this appears (I did not see duplicates).

MAJOR

P5-M1 — Bibliography and provenance; reliance on “in preparation” Paper IV (multiple locations; e.g., Abstract; §I–II; Table I; §VIII F; References [3], [4])
- Problem: The paper repeatedly cites “Paper IV [3] (in preparation; posted concurrently)” for (i) the classifier architecture/validation and (ii) the catalog-wide chirality monopole used as a reference. While the labels themselves are publicly hosted (HuggingFace), PRD requires sufficient, citable provenance for any load-bearing external result.
- Required fix: Prior to acceptance, replace “in preparation” with a public preprint identifier (arXiv) for Paper IV (and the companion Paper II if retained), or remove reliance on non-public claims. At minimum:
  - Keep the analysis genuinely self-contained by relying only on the internal matched-sample monopole fP5 = 0.49719 (already provided in §VIII F and used in σvs monopole), and demote all Paper IV-only quantitative claims (e.g., full-sky dipole amplitude) to context without load-bearing status.
  - Update the bibliography entries [3], [4] accordingly or remove them if not essential.
  - If Paper IV remains “in preparation,” expand Table I or an appendix to summarize the minimum classifier-validation facts needed to trust the per-galaxy labels used here (e.g., training set, tested equivariance, mislabel rates), or point to a stable data descriptor DOI.

MINOR

P5-m1 — Version-history language in body text (footnote on p. 3; §IV A, step 9; multiple mentions)
- Text: “earlier preprint versions used the ‘V-Web’ label loosely… this version standardizes on ‘T-Web’…”
- Problem: Version-history prose belongs in a submission cover letter or endnote, not in the body of a PRD paper.
- Required fix: Remove or rephrase to a neutral methodological clarification without referring to “earlier preprint versions.” E.g., “We implement the Hahn et al. (2007) tidal-tensor (‘T-Web’) classifier; we do not use the velocity-shear ‘V-Web’ (Hoffman et al. 2012).”

P5-m2 — Row-level overlap in bright vs dark two-sample z within T-Web classes (§VI D.c–d; p. 12–13)
- Problem: You correctly note that the filament- and cluster-class bright vs dark comparisons at the env-labeled row level are not disjoint and the two-sample z is approximate. Nonetheless, a concrete |z| ≈ 2.1 is reported in main text.
- Required fix: Move the row-level |z| to a footnote or appendix and foreground only overlap-free unique-galaxy results (you already provide |z| = 1.95 for the whole catalog). Alternatively, supply a unique-TARGETID decomposition by class (if feasible) or explicitly label the class-level |z| as an upper-bound heuristic.

P5-m3 — Explicit pointers for selection/geometry cross-checks (§IX A, p. 23–25)
- Problem: The selection-corrected rebuild (shell means, randoms-weighted low-z stress test, geometry-footprint means) is central to showing that selection-function leakage does not fabricate an environment signal. The narrative cites artifacts [A17]–[A20], but a reader would benefit from one explicit line with the before/after class volume fractions and matched-spiral class counts (several are stated but dispersed).
- Required fix: Add a compact table in §IX A (or a paragraph) listing per-class populations and fCW before/after the shell correction and the randoms-weighted rebuild, with one artifact pointer.

P5-m4 — Data/Code availability: DOI (Appendix C, p. 32–33)
- Problem: You state “A DOI-minted archival snapshot of this directory accompanies journal submission,” but no DOI is listed.
- Required fix: Provide the DOI (and, if possible, Zenodo/OSF/etc. link) for the exact tagged repository used (“v0.1.91-2026-06-28”). If the DOI is pending, indicate “to be added in proof” and ensure it appears in the final version.

P5-m5 — Clarify the “≈0.1%” cell-coverage statement (§VI A, p. 8)
- Text: “only ≈0.1% of in-footprint grid cells fall inside a DESIVAST VoidFinder sphere…”
- Problem: This is a checkable claim; the manuscript does not provide a direct calculation or artifact pointer here.
- Required fix: Add the exact fraction with an artifact reference (e.g., total in-mask cells, number flagged point-in-sphere at the grid level) or soften this statement to qualitative without a number.

P5-m6 — Scope statement on the toy EFT mapping (Appendix A, p. 30–31)
- Problem: The toy operator is clearly labeled heuristic and non-gauge-invariant in the present slicing. To avoid misinterpretation, one more explicit sentence making clear that no quantitative limit is derived here (only a scaling estimate) would help.
- Required fix: Add “We do not derive or claim a quantitative constraint on any specific coupling; the expression is a schematic scaling only.”

NITS

P5-n1 — Minor typographic/notation items
- σfrom half is sometimes typeset without a space before “from” (e.g., §VI A). Consider standardizing on σ_from-half or z_(p=0.5).
- Ensure consistent spacing around “Mpc/h” vs “h−1 Mpc” across text/figures.
- A few long sentences could be split for readability (e.g., the long sentence in §VIII D spanning three catalog-native details).

P5-n2 — Length
- At 34 pages, the manuscript is long for the narrow claim (an environment-conditional null reinforced by thorough cross-checks). Consider moving one secondary cross-check (e.g., the ASTRA EDR per-object section) and the EFT appendix to Supplemental Material to keep the main paper focused. Target: ≤ 28 pages.

Checks passed (no action required)
- Distinction between σ-from-half, σvs monopole, and permutation p-values is maintained throughout; the text explicitly warns against cross-bin σ comparisons at different n and uses σvs monopole for that purpose.
- Multiple-testing is handled consistently (Bonferroni thresholds stated and used; empirical max-stat permutation nulls with NMC = 1000 used where appropriate).
- Dimensional analysis of Eq. (1) and the k-space operators (T-Web steps) is consistent; the “multiply-by-h” convention is correct and internally consistent with the stated sanity values.
- All quoted σ, p, and CI figures I recomputed from the displayed counts matched the text/tables to the stated precision.
- The selection-function (redshift-shell and randoms) and mask-dilation sensitivity analyses are appropriate; the fixed-redshift-space limitation is clearly stated and caveated.
- Effect-size reporting accompanies χ2 (Cramér’s V reported and interpreted as small).

## Summary recommendation
MINOR REVISIONS

The analysis is rigorous, transparent, and internally consistent. The principal numerical conclusions are well supported and carefully caveated (including the post-hoc primary designation, multiple-testing control, and redshift-space limitation). Before acceptance, the authors should correct the Clopper–Pearson formula/number (ESSENTIAL), resolve the “in preparation” provenance for Paper IV or make the paper fully self-contained with public citations (MAJOR), and address the minor clarity and reproducibility points above. With these changes, the paper will meet PRD’s methodological rigor bar.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh pass)

P5-E2 — Table XIII filament σvs monopole value inconsistent with stated formula and inputs
- Issue: Table XIII reports σvs monopole = +0.99 for the filament class (n = 408,187, fCW = 0.4980) against the stated matched-sample monopole fP5 = 0.49719. Using the paper’s definition σvs monopole = (fclass − fP5)/(0.5/√n) gives
  (0.4980 − 0.49719) / (0.5/√408,187) ≈ 0.00081 / 0.000783 ≈ +1.04,
  not +0.99. The cluster (−1.11) and void (−0.56) lines recompute correctly; the wall line also matches. The filament entry appears to be a rounding or carry-over error.
- Required fix: Recompute and correct the filament σvs monopole in Table XIII (expected ≈ +1.03 to +1.05 given the printed numbers), and update any downstream text that quotes the +0.99 value.

P5-E3 — Units/conversion footnote in §IV A step 2: the “alternative convention” numeric example is misleading
- Text (footnote 1): “The alternative convention χ[h−1 Mpc] = χ[Mpc]/h (divide-by-h, giving ≈1246 h−1 Mpc at z = 0.2) is not used here…”
- Issue: The numeric example 1246 h−1 Mpc does not represent the same physical distance as 843 Mpc (1246 h−1 Mpc corresponds to 1246/h ≈ 1842 Mpc). The paper’s chosen multiply-by-h convention (843 Mpc → 570 h−1 Mpc) is self-consistent and correct. Presenting 1246 h−1 Mpc as an “alternative” numeric form can be read as a valid equivalent, which it is not for the same physical χ(z). This risks confusing readers about units.
- Required fix: Remove the 1246 h−1 Mpc numeric, or explicitly state that dividing-by-h produces a different physical value and is incorrect if the unit remains h−1 Mpc. If you wish to contrast conventions, do so with a dimensionally consistent pair (e.g., “843 Mpc ≡ 570 h−1 Mpc; 843 Mpc ≡ 843 h Mpc is a different unit.”), and keep only the convention actually used in the code.

P5-M2 — Two-sample contrast details (Table XI and elsewhere) need an explicit formula choice (pooled vs unpooled)
- Issue: The z and SE(∆) values in Table XI match an unpooled large-sample two-proportion SE ≈ sqrt(p1(1−p1)/n1 + p2(1−p2)/n2) at p ≈ 0.5, but the text just says “binomial, two-sample.” For reproducibility, readers should not have to infer whether a pooled (H0: p1 = p2) or unpooled variance was used.
- Required fix: State the exact formula used for SE(∆) and z (pooled or unpooled), and whether continuity corrections were applied (they do not appear to be). A one-line equation suffices.

P5-m7 — Minor range/threshold bookkeeping drift in Phase-2 text vs table
- Issue: The body text says Phase-2 pLEE span 0.13–0.56 (nine cells) and max |σobs−σpred| ≤ 1.64σ in resolved cells; Table VIII lists free-shuffle pLEE spanning 0.13–0.55 and the same 1.64σ bound. The numbers are consistent in substance, but the upper pLEE bound carries a slight mismatch (0.55 vs 0.56).
- Recommended action: Harmonize the upper bound (use the table’s 0.55 or quote both free/stratified ranges explicitly as you do in the table note).

P5-m8 — Table XII “0 maximal voids per pixel” residual check: arithmetic traceability
- Issue: For the 0-void bin (n = 378,511; fCW = 0.4961), σfrom half recomputes to about −4.80 using the paper’s σ definition; the table prints −4.75. This looks like innocent rounding (sensitive to the undisplayed nCW), but the text uses this cell to make an important point about mask geometry.
- Recommended action: Add the integer nCW for this row (or cite [A15]) so readers can exactly reproduce the −4.75σ value; or round σ to two decimals consistently across Table XII.

P5-m9 — Table XIII header language
- Issue: The table mixes “σvs monopole” with the displayed “fCW − fP5” column. A few readers may misread σvs monopole as a one-sample z vs 0.5. You do explain this in §V and §VIII F, but the table itself could be clearer.
- Recommended action: Rename the second column “∆f (to fP5)” and the third “σ (to fP5)”, or add a note “σ computed vs fP5, not 0.5.”

P5-m10 — NSIDE=32 per-pixel statistics cross-reference
- Issue: §VIII F gives the NSIDE=32 per-pixel σvs monopole distribution moments on “1,791 valid pixels (≥ 200 spirals).” Figure 6’s NSIDE=32 panel and Table VII (npix = 3,303) refer to all occupied pixels without the ≥ 200 cut. The counts target different selections but a reader must infer this.
- Recommended action: In §VIII F, add “(≥ 200-spiral cut)” next to 1,791, and in the Figure 6 caption make clear the figure shows all occupied pixels, not just those passing the ≥ 200 cut used for pixel-moment calculations later.

P5-m11 — k-NN sufficiency guard in §VIII B needs a pointer like the others
- Issue: The statement “up to 249 hole centres can lie within one maximum-hole-radius… 28% have more than 20 such candidates” is useful but currently unreferenced.
- Recommended action: Add an artifact pointer (e.g., a small JSON/CSV with this histogram) as you did for other checks ([A10], [A15]).

P5-n3 — Minor rounding drift in the class-to-overall bright-fraction deviation
- Issue: §VI D.d states “max class-to-overall bright-fraction deviation 1.5 pp.” Using Table XVIII and the overall matched-spiral bright-fraction 0.978 (as given), wall is 96.22% (−1.58 pp), cluster 98.93% (+1.13 pp). “~1.6 pp” is a closer upper bound.
- Recommended action: Replace 1.5 pp by 1.6 pp (or “≈ 1.6 pp”).

P5-n4 — Consistency of significant-figure reporting for pp-scale effects
- Issue: Very small ∆f (e.g., +0.06 pp in §VIII E) are sometimes shown with two decimals in “pp,” other places with one. This is cosmetic but improves scanability when the whole argument hinges on pp-level nulls.
- Recommended action: Adopt a consistent 0.1 pp precision for ∣∆f∣ < 1 pp, and 0.01 pp when you quote an accompanying z that requires it.

Explanation
I focused on new issues not covered in my first report. Most core arithmetic re-checks (counts, σ-from-half, χ2, CIs, Bonferroni thresholds, permutation p-values, DESIVAST contrasts) still reproduce to the quoted precision. The items above are either small arithmetic mismatches (Table XIII filament σvs monopole), a confusing unit example (the 1246 h−1 Mpc “alternative”), or clarity/traceability fixes where the paper would benefit from one more pointer or a wording tweak.