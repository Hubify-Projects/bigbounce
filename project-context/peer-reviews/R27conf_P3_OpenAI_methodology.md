# P3 R27conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper3_anomaly_catalog_v3.1.86.pdf` md5=31284b90 pages=26
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6451 chars)
**Wall time**: 312.1s

---

Referee report (Methodology/Statistical Rigor) — Physical Review D

Scope of this review
- I read the full 26-page manuscript, including all figures, tables and captions.
- I recomputed rates, ratios and quoted uncertainties from the numbers shown in the paper.
- I focus on statistical methodology, dimensional consistency, internal arithmetic, significance claims and reproducibility.

Global assessment
The paper is ambitious and unusually transparent, but there are multiple issues that must be addressed for PRD. The most serious are: a dimensional error in the Fisher-summary formula used to map bias enhancement into σ(fNL); pervasive “version history” and internal-run bookkeeping language in the body text; an irreproducible scoring axis for the eROSITA table; and avoidable data leakage in tabular feature scaling. Below I itemize all findings with priorities.

Findings

ESSENTIAL

P3-E1 (Section V and Table IV; pages 15 and 19): Dimensional error in the Fisher-summary mapping
- Problem: The text repeatedly states “1/σ^2(fNL) = F0 + c α^2 with F0 = 1/8.982” (Section V, page 15; Table IV (i), page 19). This is dimensionally wrong. If σstd = 8.98 is the single-tracer baseline, then F0 must be 1/σstd^2 = 1/(8.98)^2 ≈ 0.0124, not 1/σstd. Using F0 = 1/8.982 ≈ 0.111 would give σ = 3.0–3.1 for α=0, contradicting the baseline stated throughout.
- Impact: Although the central numbers quoted (σ = 8.14 for α̂ = 0.19; envelope [3.92, 8.98]) are consistent with the correct F0 = 1/8.98^2, the written formula is wrong and can mislead readers. It must be fixed everywhere it appears.
- Required fix:
  - Replace “F0 = 1/8.982” by “F0 = 1/(8.98)^2 = 0.0124” (to the precision you adopt).
  - Re-check and re-state c with proper units if you intend c to be an absolute increment in 1/σ^2 (you do not show how c=0.0747 was obtained; confirm it is computed under the correct normalization).
  - Recompute all derived numbers under the corrected F0 and update text if any values shift (they likely will not, but show the calculation explicitly in an appendix).

P3-E2 (Abstract; page 1): Version-history language present in the abstract
- Problem: “an earlier draft quoted 264,938/264,738 …” and similar editorial history appears in the abstract and elsewhere in the body.
- Required fix: Remove all “earlier draft/withdrawn/replaced” language from the abstract and body. The paper must read as a self-contained final account; any version history belongs in a change-log on a data repository, not in PRD.

P3-E3 (Multiple sections; pages 9–12, 21): Version-history and internal audit tags pervade the paper
- Problem: Numerous instances of internal bookkeeping appear in the body, e.g. “the earlier ‘strict subset’ framing is replaced” (Table I footnote block, page 9), “an earlier draft quoted 38,330 … withdrawn” (Section IV.B, page 12), “an earlier draft listed 10.6 s … withdrawn” (Table V footnote, page 21), repeated “artifact” mentions with repository JSON paths (“r24conf_pod_session_batch.json”, “r23conf_dedup_audits.json”, etc.).
- Required fix: Remove all version-history remarks, internal filenames, run IDs and “artifact” qualifiers from the main text and figures. Put any such provenance in a separate data-release note or Supplemental Material. PRD articles must not embed internal audit logs.

P3-E4 (Section II.B.a; page 3): Data leakage in feature scaling for tabular surveys
- Problem: You state that eROSITA and NEOWISE scalers are fit on the full sample (“statistics fit on the full 930K sample … then split 80/20”; “robust median/IQR transform fit on the full sample … then split 80/20”), which leaks validation information into normalization constants. You also say the Gaia production script is not fully recovered and the spec is “lineage-inferred”.
- Impact: While rankings may be robust, validation MSE (and hence S) are affected by leakage; for a Methods paper this is not acceptable without a demonstrated invariance of the anomaly ranking.
- Required fix:
  - Re-run the tabular-sample experiments with scalers fit on the training subset only (no look-ahead to validation). Quantify the effect on the anomaly ranking (e.g., Spearman rank correlation and Jaccard overlap at the published thresholds). If negligible, state the measured invariance; if not, update the catalog and all affected numbers.
  - Provide the exact Gaia-50K preprocessing script or remove the Gaia tier from the main catalog and demote it to exploratory in the paper (you do already label it exploratory, but the Methods section must not imply unrecovered production steps).

P3-E5 (Section III.E and Table III; pages 7–8 and 10): Irreproducible eROSITA “SBigAE” axis in the main table
- Problem: You explain that the published eROSITA SBigAE axis “could not be reconciled post hoc with the canonical-S definition … no committed score axis reproduces the production threshold … the selection is best read as fixed top-298 cap” (Section III.E). Yet Table III reports SBigAE values and the main text cites the 0.259 threshold (irreproducible axis).
- Required fix:
  - Either (a) recompute and publish a reproducible S axis consistent with Eq. (2) (and re-derive the threshold), or (b) remove SBigAE from Table III and the text, and clearly re-label the selection as “top-298 by committed raw BigAE reconstruction score” with that raw scalar provided. In case (b), eliminate the 0.259 value from the PRD article (keep it only in a data release note) and ensure no analysis in the paper uses that axis.

P3-E6 (Global; multiple pages): Nonstandard footnote markers and dense footnote blocks in Tables
- Problem: Table I uses symbols (♡, ♠, ∥, ⋆, §) and very long “footnotes” that contain critical results and caveats (some of which are version-history-like). This is nonstandard for PRD and makes the scientific record brittle.
- Required fix: Convert all footnote content that carries scientific meaning into proper text in the main body or concise numbered footnotes/endnotes. Avoid symbol clusters and reduce digressive content.

MAJOR

P3-M1 (Abstract; page 1): Claims of “largest-scale” and multiplicative factors need explicit, checkable references
- Problem: “largest-scale application … 141× the size of the largest prior single-survey anomaly catalog [11]; DESI-only subset is ~73×” are headline claims. They appear consistent numerically (378,080/2,685 ≈ 141; 195,829/2,685 ≈ 73), but the comparison set must be precisely specified (e.g., Liang et al. [11] EDR sample definition and anomaly criterion differ).
- Required fix: In the abstract or a short footnote immediately after the claim, precisely define the benchmark (which catalog, its count and criterion) and state caveats (survey/method differences). Do not rely on a later section for this.

P3-M2 (Section II.D Step 5 and Fig. 10; pages 4–5 and 18): Injection–recovery gate definition and pre-specification
- Problem: Gates are said to be “heuristic engineering thresholds fixed at Path-C design time” (page 18), but the paper reads like these choices were made after exploring the data extensively. NEOWISE’s “PASS by construction” is not a detector test yet is counted among the 3 PASS headline in multiple places.
- Required fix: Pre-specify in the paper (one place) the gate definitions and which ones constitute detector sensitivity tests. In the abstract and any headline sentence in the body, count only genuine detector-sensitivity PASS as PASS (SDSS continuum and Planck CMB). Elsewhere, keep NEOWISE as a QA check, not a PASS affecting tallies. Clarify which plant morphology (continuum dip vs. emission line) is the primary gate for spectroscopic surveys.

P3-M3 (Section III.C; page 6, Fig. 3 right): Extremely large cross-transfer S values without scale audit
- Problem: The SDSS cross-transfer S values span to 1.9×10^11. This is an astronomical z-score on the Eq. (2) scale and could only arise from MSE values many orders above the DESI validation σval. You present this as a cross-transfer artifact, which is fine, but no quantitative sanity check is provided linking typical MSE to this range.
- Required fix: Insert a short quantitative audit: report μval and σval for the DESI model used to score SDSS, and give the MSE that corresponds to S ≈ 10^11. Briefly argue why such MSEs are possible under the chosen normalization (or cap/transform values before z-scoring). Alternatively, plot SDSS cross-transfer on a log10 MSE axis rather than Eq. (2) S to avoid implying meaningful z-scores.

P3-M4 (Section III.A; page 5): Untraceable per-class anomaly rates
- Problem: “galaxies are flagged … at ~20× the rate of QSOs (0.75% vs. 0.037%)” is not supported by a figure/table in the paper.
- Required fix: Provide a table or figure with the class counts and rates supporting this claim, or remove the numeric comparison.

P3-M5 (Section IV.B; page 12): Spatial χ^2 test stated without minimal reproducible recipe
- Problem: You now provide Nside and pixel counts (good), but the test still assumes “uniform per-occupied-pixel mean with Poisson variance” after merging seven heterogeneous footprints. This is a crude null and the χ^2_ν number can be misinterpreted despite caveats.
- Required fix: Provide the exact count vector length (24,049), total count (378,280), and the mean used; include a one-line pseudo-code or formula for the χ^2 so readers can reproduce it. Keep the caveat that it is selection-function dominated.

P3-M6 (Section III.E; pages 7–8): Non-independence of IF cross-validation framed ambiguously
- Problem: You rightly note the IF and BigAE share a latent space, so the 95.3% overlap is non-independent. However, calling it “cross-validation” can be misread as independent validation.
- Required fix: Rename this to “internal consistency overlap using a second scoring function trained on the same learned representation.” Avoid “cross-validation” for this comparison.

MINOR

P3-m1 (Table I and text; pages 9–10): Totals and rates recomputation
- Cross-transfer total 319,443: Sum of the listed cross-transfer numbers (excluding ACT) is 319,243. Adding ACT’s 200 yields 319,443 as stated. The paper clarifies this in footnotes; consider a parenthetical “(includes +200 ACT for the baseline only)” in the table row to prevent confusion.
- Path-C unique: 388,493 – 10,213 = 378,280 (correct). 378,280 − 200 Planck = 378,080 point-sources (correct).
- Catalog-grade unique 269,317: Sum of the six catalog-grade survey counts (DESI 195,829 + SDSS 77,905 + eROSITA 298 + Planck 200 + Gaia 500 + NEOWISE 419) = 275,151; a 5,834-item compression to 269,317 is consistent. Then 269,317 + (113,342 − 4,379) = 378,280 (checks). Suggest gathering these equalities in one compact paragraph in the main text.

P3-m2 (Section IV.A; page 11): Novelty percentages and false-match rate
- I recomputed: Wilson 68% for 178/1000 is ±1.21% (matches “±1.2%”). SIMBAD random false-match per source at 5″: n × πr^2 = 3.0×10^-5×78.54 ≈ 0.00236 → 0.24% (matches). Keep both computations but add the exact numerical inputs inline for transparency.

P3-m3 (Section II.C; page 4): Throughput/time bookkeeping
- DESI pass: 22,504,897 / 1,142 s^-1 ≈ 19,712 s (stated 19,705 s; fine). Good to add one sentence noting how batching and I/O overlap account for the small difference.

P3-m4 (Figures): Axes and units
- Fig. 5: DR9 image pixels labeled as 256×256 → 108″×108″ implies 0.42″/px; Fig. 6 uses 128×128 → 54″, consistent with 0.42″/px. Consider stating the pixel scale once to avoid confusion given DESI Legacy Survey coadd pixel scales vary by instrument.

P3-m5 (Style): Overuse of “PASS/FAIL” in all-caps
- Consider using “passes”/“fails” in sentence case in the main text; keep all-caps only in a compact gate summary or figure legend, to meet PRD style.

P3-m6 (Style): Long parentheticals and em-dash chains
- Several sentences are hard to parse due to nested parentheses and em dashes. A modest editorial pass to simplify will improve readability without changing content.

NIT

P3-n1 (Typographical): Spacing and hyphenation
- A few instances of “5′′” vs “5
′′
” spacing appear inconsistently (e.g., Section II.D bullets, page 5). Standardize to arcsec symbols without line breaks.
- Occasional repeated words or awkward phrasing (“score−SNR”, “null … is geometry-driven”). A light copyedit will suffice.

P3-n2 (Symbol use): Heart/diamond/club-like footnote markers
- Replace with conventional numeric or alphabetic footnotes in PRD style.

P3-n3 (Bibliography): Check years/venues
- Verify final bibliographic metadata for [12] (arXiv:2506.17376 labeled 2025), and ensure all references have consistent journal/volume info where available.

Overclaims and significance checks

- σ(fNL) forecast: With the corrected F0, your central σ=8.14 and the “envelope” [3.92, 8.98] are internally consistent. You correctly note convexity, the squaring noise bias, and explicitly avoid a detection claim. Good.
- NANOGrav spectral index: γ = 2.567 ± 0.382 vs. γMB = 3.0 (+1.13σ) and γSMBHB = 4.33 (+4.61σ) recompute correctly. The Bayes factor BMB/SMBHB = 7.14×10^3 is not reproducible from what’s in the paper; please give the prior density, posterior density at each point, and numeric values (or provide a small table) to support the Savage–Dickey result (MAJOR if you intend to keep the number; otherwise, soften to a qualitative statement).
- SIMBAD-unmatched vs. archival novelty: You clearly warn that 58.8% is a database-coverage metric and provide the 17.8% genuine novelty fraction with a Wilson interval. Good.

Length and presentation
- At 26 pages, with long multi-paragraph table footnotes and many process digressions, the paper reads longer than needed for the core results. I recommend compressing to ~20 pages by:
  - Moving internal audit pathnames and detailed pod/GPU timings to Supplementary Material or a data-release note.
  - Converting long table footnotes into short numbered notes and shifting methodological digressions into a dedicated Methods appendix.

## Summary recommendation
MAJOR REVISIONS

The work is substantial and potentially publishable, but the paper cannot be accepted in its present form. The dimensional error in the Fisher-summary formula must be corrected everywhere; the eROSITA scoring axis must be made reproducible or removed from the PRD article; the tabular-sample data leakage must be eliminated or its impact quantified; and all version-history/internal-log language must be excised from the main paper. Several presentation issues also need tightening. Once these are fixed and the affected numbers re-validated, the manuscript will be in much stronger methodological shape for PRD.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (second pass)

P3-M7 (Planck “top-1%” labeling inconsistent with Path-C implementation)
- Issue: The paper repeatedly describes the Planck tier as a “top-1%” selection (Table I and several places in text). However, under Path-C the native re-score uses 2×10^5 patches and still retains exactly 200 patches, i.e., 0.1% of the re-scored set, not 1%. Table I also lists Ntotal = 20,000 (cross-transfer budget) and Rate = 1.00%.
- Impact: Readers can infer the final Planck tier is a top-1% selection on the native re-score, which it is not. This affects rate interpretability and reproducibility.
- Fix: State unambiguously that the published Path-C Planck tier is a fixed-count top-200 selection (not “top-1%”) on the 200k native re-score. In Table I, either (a) list both patch budgets (20k cross-transfer; 200k native) and remove the “1.00%” rate for Planck in favor of “fixed 200,” or (b) move the rate to a footnote explicitly tied only to the cross-transfer diagnostic.

P3-M8 (Figure 3 caption/data mismatch for LAMOST; native vs cross-transfer)
- Issue: Fig. 3 caption says “cross-transfer for SDSS, native for DESI/LAMOST,” but the LAMOST curve is labeled “LAMOST DR10 (44,075),” which is the cross-transfer anomaly count (native S > 5 gives 2,054; native top-1% slice 113,342).
- Impact: Confuses which LAMOST score axis/distribution is shown (native vs DESI-trained cross-transfer). This undermines interpretability of the left panel.
- Fix: Clarify in the caption and text which LAMOST set is plotted. If it is the DESI-trained cross-transfer distribution (44,075), say so and explain that its S-axis is on the DESI validation scale. If you intend to show the native LAMOST distribution, replace the curve and legend accordingly.

P3-M9 (Inconsistent α→σ(fNL) mapping between main text and Appendix C)
- Issue: Section V uses the positivity-respecting quadratic form 1/σ^2 = F0 + c α^2. Appendix C/Table VII instead linearly scales σ with α (Δσ/σstd ≈ (6.1%/0.15) α) to generate σ(fNL) values. These two mappings diverge substantially for moderate α (e.g., at α = 0.5 the quadratic gives σ ≈ 5.7 while Table VII reports 7.15).
- Impact: Two conflicting mappings for σ(fNL)(α) coexist in the paper, making the forecasts non-reproducible and internally inconsistent.
- Fix: Use a single, stated mapping throughout (preferably the quadratic Fisher form used in Section V) and regenerate Table VII accordingly, or clearly label Table VII as a rough linearized sanity check and remove numerical values that contradict the adopted model.

P3-M10 (Planck Ntotal in Table I vs text; reproducibility hazard)
- Issue: Table I lists Ntotal = 20,000 for Planck, while the Path-C native re-train and re-score use 200,000 patches (footnote and Section III F). The table does not indicate the second, larger patch bank used for the final tier.
- Impact: A reader reconstructing the Planck tier from Table I alone will use 20k patches and get a different selection when applying the “top-1%” instruction (which is itself obsolete under Path-C; see P3-M7).
- Fix: In Table I, add a note or column clarifying that the final Path-C re-score uses 200k patches and that the retained set is the fixed top-200 from that 200k ranking.

P3-M11 (Figure 3 cross-survey overlay of S without an explicit “not comparable” warning)
- Issue: Methods (Section II.B.b) say S values are not comparable across independently trained surveys. Fig. 3 left overlays DESI vs LAMOST S distributions on a shared x-axis without an explicit “not comparable across surveys” disclaimer in the caption (the caption mentions unit-area normalization of the y-axis, but not the x-axis caveat).
- Impact: Readers may incorrectly compare absolute S values across DESI and LAMOST.
- Fix: Add to the Fig. 3 caption that the S axes are survey-specific and not directly comparable; the panel is for qualitative tail-shape comparison only.

P3-m7 (Arithmetic check — dedup-radius sensitivity)
- Claim: Re-run at {3″,5″,7″} gives unique counts 378,604 / 378,280 / 378,145; “maximum unique-count variation of 0.086% relative to the canonical 5″ result.”
- Check: |378,604 − 378,280| / 378,280 = 0.000856 ≈ 0.0856% (matches). OK to keep; consider quoting the exact delta (324) alongside the percentage for transparency.

P3-m8 (Arithmetic check — spatial χ2ν)
- Claim: χ2 = 376,713 with dof = 24,048 → χ2ν = 15.7.
- Check: 376,713 / 24,048 = 15.66 (rounds to 15.7). Consider printing 15.66 or 15.7(rounded) for numerical clarity.

P3-m9 (Caption/body alignment — Planck score range vs validation)
- Claim: Planck native top-200 MSE range [0.558, 0.621]; native val loss 0.4437.
- Consistency: The anomaly MSEs sit modestly above the reported val loss; fine. A one-line note that the anomaly range is on the same per-patch-standardized MSE scale as the validation loss would make this immediately clear to readers.

P3-m10 (Arithmetic check — LAMOST “21.5× rate compression”)
- Cross-transfer S > 5: 44,075; native S > 5: 2,054. Ratio 44,075 / 2,054 = 21.47 (≈ 21.5). Correct; consider adding the exact ratio once in text.

P3-m11 (Figure 1 vs Section V tier naming)
- Fig. 1 refers to “83 gold-tier anomalies (visual-display sample)” and text clarifies this is distinct from the 116-object GOLD tier used in forecasts. Because “gold-tier” is used in two different senses (display set vs. QSO-confidence GOLD), add a parenthetical in Fig. 1 caption linking to the §V definition to avoid confusion.

P3-m12 (Appendix C “linear scaling” wording)
- The sentence “The fractional improvement scales as Δσ/σstd ≈ (6.1%/0.15) α, consistent with the linear-bias regime” reads like a formal result, but it is only a first-order heuristic around α = 0.15 and conflicts with your adopted quadratic Fisher form. Label it explicitly as a first-order Taylor approximation around α = 0.15 (if you keep it at all), or remove to avoid double-prescription.

Explanation
I concentrated on cross-panel/cross-section consistency, arithmetic spot checks, and places where procedure labels could mislead replication (Planck). The biggest new issues are the Planck “top-1%” labeling vs fixed-count implementation (P3-M7/M10) and the inconsistent α→σ mappings between the main text and Appendix C (P3-M9). The Fig. 3 LAMOST caption/data mismatch (P3-M8) is another concrete fix that will prevent misinterpretation. All other checks either matched your numbers or need only small clarifications as noted above.