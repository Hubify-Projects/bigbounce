# P3 D1 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p3_anomaly_engine/paper3_draft.pdf` md5=62d7b294 pages=30
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7555 chars)
**Wall time**: 340.2s

---

PRODUCTION EDITOR VISUAL/PACKAGING QA (Design round D1)
Report only visual/packaging/layout issues seen in the rendered PDF

- D1-V1 (MINOR). Page 1–2, Abstract block. The abstract is a single dense paragraph exceeding 20 lines with multiple parenthetical clauses and long em-dash insertions; readability is strained. Required fix: break into 2–3 short paragraphs and tighten em-dash clauses; consider moving long gate-details parenthetical to a Methods summary sentence in the main text.

- D1-V2 (MAJOR). Page 9–10, Table I. The table is extremely dense, uses multiple special footnote symbols (†, ‡, §, ⋆, ♡, ♢, #, ♠, ∥) and long footnotes spanning nearly a column. Legibility suffers; several footnotes read like main text. Required fix: convert Table I to a full-width table* (two-column span) and move long expository footnotes into the caption or into an Appendix “Notes on Table I”; standardize footnote symbols to letters (a, b, c, …) per PRD style.

- D1-V3 (MINOR). Page 7, Fig. 2 (Mollweide map). Point markers are small and overlapping; survey color legend text is small. The “ACT DR6” points are plotted despite quarantine and the “Cross-transfer baseline” header competes with the quarantine caveat. Required fix: increase marker sizes with transparency or use density shading; enlarge legend text; add an explicit red “Quarantined (Appendix F)” label on the plot or drop ACT points from the main-figure rendering to avoid confusion.

- D1-V4 (MAJOR). Page 8, Fig. 3 (three panels). Right panel uses 10^2–10^11 dynamic range with tiny ticks/labels; left panel overlays two histograms with very fine binning; y-axis label abbreviated as “Prob. density.” Required fix: make Fig. 3 full-width; increase font sizes and line weights; expand y-label to “Probability density”; reduce bin count or overlay kernel density estimates for clarity.

- D1-V5 (MINOR). Page 11–12, Table III and Table IV. Both tables are placed mid-column with long captions; Table IV includes a long parenthetical about irreproducibility. Required fix: make these tables full-width or move the long methodological notes into the main text/Appendix, leaving concise captions.

- D1-V6 (MINOR). Page 16–17, Fig. 7 (four panels) and Fig. 8 (six spectra). These multi-panel figures are crowded; axis labels and red reconstruction overlays are thin. Required fix: promote each to full-width; increase axis font sizes and line thickness; ensure all panels share consistent y-limits and fonts.

- D1-V7 (NIT). Page 18, section header “D. Planck × ACT Cross-Correlation: Null Result” appears at bottom of page with only a couple of lines following (orphaned heading risk across versions). Required fix: enforce a keep-with-next for section headers; push the header to the next page if fewer than 3 lines follow.

- D1-V8 (MINOR). Page 22, Fig. 10 (injection–recovery curves). Legend and annotations (PASS/FAIL, 50% gate, “5× eval pt.”) are small. Required fix: full-width figure or increase font sizes; ensure colorblind-safe palette; add line styles to distinguish curves.

- D1-V9 (NIT). Page 24–25, Fig. 11 (shot-noise sensitivity). The “Normalization note” is long and belongs in the caption/main text. Required fix: move normalization note into caption; keep the panel uncluttered.

- D1-V10 (MINOR). Page 26, Fig. 12 (2×5 gallery). The per-panel RA text and family labels are small on print. Required fix: enlarge fonts; consider moving the gallery to Supplemental Material with a single representative in the main text.

- D1-V11 (MINOR). Repeated long file-paths in captions/text (e.g., pipelines/p3_anomaly_engine/…) wrap awkwardly across lines in narrow columns. Required fix: move long paths to footnotes or an Appendix; keep captions short.

- D1-V12 (MINOR). General typography. Frequent use of primes ″ for arcseconds and unicode footnote glyphs ♡, ♠, ♢ etc. can render inconsistently in some PDF viewers/printers. Required fix: replace with standard TeX macros and lettered footnotes.

- D1-V13 (MAJOR). Page 23, Acknowledgments/Data availability paragraph. A long single paragraph with URLs and file paths breaks justification and extends close to margins. Required fix: break into bullet list; ensure DOI/URL line-breaks are allowed at safe points; avoid mid-sentence URLs in the body.

- D1-V14 (MINOR). Equations (E1) and the definition block lines occasionally overrun measure in narrow columns (half-line overflow risk). Required fix: use multiline align environment; check for margin overflow.

- D1-V15 (MAJOR). Overall length and density. At 30 pages with many method-sidebars in captions/footnotes, the manuscript is visually dense. Required fix: move extended audit trails, path listings, and large galleries/tables (Tables VI–VIII; Fig. 12) to Supplemental Material. Target ≤ 24–25 pages for the main text.

METHODOLOGY AND STATISTICAL RIGOR REFEREE REPORT (PRD standards)

ESSENTIAL findings

- P3-E1. Abstract and §II D/Table I (Pages 1–2, 9–10). Terminology inconsistency for “catalog-grade tier.” Abstract states: “the recommended catalog-grade tier contains 269,317 unique entries … drawn from a direct, independent 6-way 5′′ dedup of DESI + SDSS + eROSITA + Planck native + Gaia + NEOWISE,” while in the same abstract and §II D the eROSITA (1.2% recovery) and Gaia (5.2%) components are explicitly stated to “fail the 5σ injection-recovery gate and remain exploratory components.” Required fix: define “catalog-grade” precisely and consistently. Either (a) restrict catalog-grade to surveys that pass validation gates (DESI, SDSS-native, Planck-native, NEOWISE), excluding Gaia and eROSITA from the catalog-grade count; or (b) retain the 6-way set but rename it “recommended working catalog (validated + exploratory; per-survey validity flags included).” Update all counts accordingly in the Abstract, §II D, §IV C, and Conclusions.

- P3-E2. Data availability and provenance placeholders (Page 23, Data availability). The text reads: “will be made public with the arXiv posting” and “A Zenodo DOI will be minted at submission and cited here in place of this sentence (DOI inserted at submission).” This is not acceptable for PRD publication. Required fix: replace all future-tense promises and placeholders with live, permanent DOIs/URLs and frozen release manifests (with SHA-256 hashes) that match exactly the artifacts and versions cited throughout. Remove parenthetical “will be inserted” language.

- P3-E3. Mixed-significance comparisons (Pages 19 and 22). Several places juxtapose quantities derived under different normalizations/nulls. Example: §V and Appendix C/Fig. 11 compare σ(fNL) baselines with different absolute normalizations; although a “Normalization note” exists in Fig. 11, the Abstract and §V should include a plain-language “not directly comparable” caveat wherever such numbers are placed side-by-side. Required fix: at every juxtaposition of σ(fNL) from the redshift-binned Fisher (§V) and from the shot-noise Fisher (Appendix C/Fig. 11), add an explicit sentence: “Absolute values are not directly comparable; only relative changes carry over.”

- P3-E4. eROSITA irreproducible score axis used in headline tables (Pages 11–12, Table IV; Page 9–10, Table I). The paper rightly explains that the published SBigAE axis is irreproducible and the membership list is canonical. However, Table I places the 298-member set alongside reproducible score-based tiers, and Table IV still uses a compound of fields implying a score column. Required fix: in all tables and text, mark the eROSITA tier unambiguously as “membership list only; per-object BigAE score irreproducible; use committed raw-score artifact or IF-axis for any thresholding.” Remove any residual implications of a reproducible SBigAE axis and ensure no thresholds (e.g., “0.259”) are presented as operational outside the production artifact context.

- P3-E5. Pre-registration / gating thresholds (Pages 5, 21–22). The text states that gate thresholds (validation MSE ≤ 0.30; injection ≥ 50% at 5σ; Jaccard ≥ 0.70/0.50) are heuristic. For PRD-level methodological rigor, this must be framed to avoid p-hacking concerns. Required fix: explicitly declare these thresholds a priori in a Methods subsection (“Gate thresholds and rationale”), justify them by prior literature or pilot power analysis, and show that conclusions (PASS/FAIL labels) are insensitive to reasonable threshold variations (e.g., 40–60% at 5σ; 0.60–0.80 Jaccard). Provide a small robustness table.

MAJOR findings

- P3-M1. Abstract arithmetic and traceability sweep (Pages 1–2). The abstract is unusually dense and mixes several numbers with caveats; each must be traceable precisely in the body. While most numbers check out, the reader must chase long footnotes to reconstruct logic (e.g., 269,317 includes Planck; 269,117 excludes). Required fix: add a one-line declarative sentence in the Abstract summarizing the stratification: “Of the 378,280 unique anomalies, 378,080 are point sources and 200 are Planck map patches; the recommended working 6-survey subset (excludes LAMOST) contains 269,317 unique entries including 200 Planck patches (269,117 point sources).”

- P3-M2. DESI rate denominators (Page 6, Table II and surrounding text). The paper reports 0.75% (GALAXY) and 0.037% (QSO) rates with Wilson 95% CIs “±0.02%” and “±0.003%,” on denominators “∼4.9M” and “∼1.5M.” A quick binomial SE suggests tighter CIs (≈±0.0039% and ≈±0.0016% respectively). Required fix: verify denominators and re-compute CIs; if conservative rounding was applied, state that explicitly (“rounded to two decimals for readability”) or provide exact CIs in an Appendix table.

- P3-M3. NEOWISE injection–recovery “PASS” classification (Pages 13, 22, Fig. 10). The NEOWISE gate is acknowledged as a masking-geometry QA that “passes by construction,” yet it is tallied as one of the three PASS results in the headline enumeration (“3 PASS”). Required fix: in all headline PASS/FAIL tallies (Abstract, §II D Step 5, §VI D(ii), Conclusions), explicitly phrase this as “2 sensitivity PASS (SDSS, Planck) + 1 geometry-QA PASS (NEOWISE)” to avoid misinterpretation.

- P3-M4. Cross-transfer SDSS figure annotations (Page 17, Fig. 8 caption). The caption admits “burned-in ‘Score’ annotations are display values … rather than catalog-pipeline outputs,” yet S = 49.5 is quoted and compared. Required fix: remove all non-catalog “display scores” from figure callouts, or clearly mark them as “display-only, not catalog scale,” and avoid any numeric comparisons against the S > 5 threshold in captions.

- P3-M5. ACT points on main baseline map (Page 7, Fig. 2). Although the caption warns that ACT is quarantined, plotting ACT points in a main-figure that communicates results invites confusion. Required fix: either (a) remove ACT from the main figure and move the ACT baseline map to Appendix F, or (b) grey out ACT points with a prominent “Quarantined (Appendix F)” banner in-figure.

- P3-M6. Use of training spectra in DESI scoring (Pages 4–5, 6). The 47,000 training spectra are included in the 22.5M scoring pool. Although robust k-fold and OOD Jaccard summaries are provided, PRD readers will expect an explicit statement of the fraction of training objects entering the S > 5 tail. Required fix: report the count and fraction of training-pool spectra that make the S > 5 anomaly set and verify their stability across folds; if non-negligible, provide an S > 5 catalog version with training spectra removed.

- P3-M7. Consistency of “largest”/“× times” claims (Pages 1–2, 21). Claims like “∼141× the size of the largest prior single-survey anomaly catalog” and “DESI-only ∼73×” are nuanced later (not like-for-like). Required fix: in Abstract and Conclusions, append “(not like-for-like; see §III A for science-class-restricted comparison ≈0.9×)” immediately after the “∼73×” claim to avoid overstatement in the summary.

- P3-M8. Reference formatting and dating (Page 29). Ref. [12] lists “Mon. Not. Roy. Astron. Soc. 547, Issue 2 (2026), arXiv:2506.17376.” Check consistency (2026 journal year vs. arXiv:2506). Required fix: verify and update to the final bibliographic information consistent with the cited work.

MINOR findings

- P3-n1. Cramér’s V computation (Page 15). The formula is printed with a line-break that could be misread (“Cram´er’s V =
p
χ2
p
/(N · (k − 1)) =
376,713/(378,280 × 24,047) ≈ 0.0064”). Required fix: rewrite as V = sqrt[ χ^2 / (N (k−1)) ] = sqrt(376,713 / (378,280×24,047)) = 0.0064.

- P3-n2. False-match rate computation units (Page 14). The SIMBAD surface density is given as nSIMBAD ≈ 3.0 × 10−5 arcsec−2. Required fix: add the explicit formula Pfalse = π r^2 n with r = 5″ to document the arithmetic that yields 2.4 × 10−3.

- P3-n3. Planck top-200 MSE range (Page 12). The MSE range [0.558, 0.621] appears without units/context. Required fix: state explicitly “per-patch standardized-MSE” in caption or text.

- P3-n4. Gaussian-bump injection amplitude units (Table VI footnote, Page 24). The amplitude is defined in “standardized patch units.” Required fix: state the mapping from KCMB units to standardized units (mean removal and division by per-patch std) up front.

- P3-n5. UMAP trustworthiness metrics (Appendix D, Page 25). Values are reported as 0.9797 ± 5×10−5. Required fix: specify the number of seeds and the exact trustworthiness definition (k=10) already present; add that this metric does not guarantee global structure preservation (clarify limitations).

- P3-n6. Duplicate non-ASCII characters (multiple pages). Occasional diacritics (Cram´er) are malformed. Required fix: ensure proper encoding and fonts.

NITs

- P3-N1. Consistency in abbreviations: use either “S/N” or “SNR” consistently (§III A and elsewhere mix both). Required fix: standardize to one abbreviation.

- P3-N2. Axis labeling: “Prob. density” (Fig. 3) should be “Probability density.”

- P3-N3. Minor copyedits: stray hyphenation (“re-score”, “retrain”) varies; unify to journal style.

QUANTITATIVE/CONSISTENCY AUDIT NOTES (spot checks)

- 195,829 / 22,504,897 = 0.870% (DESI S > 5 rate) — OK vs. 0.87%.
- SDSS cross-transfer: 77,905 / 2,304,830 = 3.38% — OK.
- LAMOST cross-transfer: 44,075 / 11,418,594 = 0.386% ~= 0.39% — OK.
- LAMOST rate compression: 44,075 / 2,054 ≈ 21.46× — OK (“21.5×”).
- SDSS compression to S > 5: 77,905 / 12 = 6,492× — OK (“∼6500×”).
- Path-C unique compression: (388,493 − 378,280) / 388,493 = 2.629% — OK.
- Multi-survey clusters: 637; intra-survey collapsed: 9,576; total collapsed: 10,213 — consistent with cluster-size histogram.
- Dedup radius sensitivity: max deviation |378,604 − 378,280| / 378,280 = 0.086% — OK.
- DESI “science-bit bitmask” fraction: 2,468 / 20.3M = 0.0122% — OK (Table II).
- Novelty fraction: 178/1,000 = 17.8%; SE ≈ 1.2% (68% Wilson) — OK.
- False-match Pfalse ≈ π 5″^2 × 3e−5 arcsec−2 ≈ 0.00236 — OK.
- Cramér’s V: sqrt(376,713 / (378,280×24,047)) ≈ 0.00644 — OK.
- fNL envelope: α = 0.19 ± 0.65; σ = 1/sqrt(0.01239 + 0.0747 α^2) ⇒ central 8.14; at α+ = 0.84 ⇒ 3.92; at α− clipped to 0 ⇒ 8.98 — OK.
- NANOGrav σ-shifts: (3.0 − 2.567) / 0.382 = +1.13σ; (4.33 − 2.567) / 0.382 = +4.60σ — OK (4.61σ quoted).

STANDALONE-READER TEST

- The manuscript is impressively self-critical; however, many crucial provenance statements depend on external repositories (file paths). For PRD, ensure all load-bearing artifacts (model configs, training splits, dedup manifests) are summarized in a compact, citable Appendix (with permanent DOIs) so the paper remains self-contained if URLs rot.

RECOMMENDED PAGE REDUCTION

- The main text can be reduced by moving: (i) long table notes (Table I) and computational details (Table VI) to Supplemental Material; (ii) taxonomy gallery (Fig. 12) to Supplemental, keeping one exemplar in the main text. Target ≤ 24–25 pages.

## Summary recommendation
MAJOR REVISIONS

The paper is thorough and unusually candid about limitations. However, several essential issues must be fixed before PRD publication: the inconsistent “catalog-grade” definition vs. inclusion of exploratory tiers; firming up data-availability to live DOIs; clarifying mixed-normalization σ(fNL) juxtapositions; and tightening presentation (Table I and multi-panel figures). A few methodological clarifications (NEOWISE gate classification, DESI training-set presence in the tail, eROSITA irreproducible axis labeling) are also required. With these addressed and the visual packaging improved, the manuscript will meet PRD’s methodological and presentation standards.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS AFTER SECOND PASS (focus: A–J checks). Only items not already in my initial review are listed.

ESSENTIAL

- P3-E6. NEOWISE gate evidence incomplete/inconsistent (Step-1 criterion). Methods Step 1 defines a two-part native-retrain gate (validation loss ≤ 0.30 within ≤ 100 epochs, or ≥ 50% recovery at 5σ). For NEOWISE, the paper reports only the masking-geometry injection “PASS by construction” (not a sensitivity test) and gives no native validation loss. Yet the Abstract and §II D language groups NEOWISE among surveys that “pass injection-recovery and native-retrain validation gates.” Required fix: either report the NEOWISE native validation loss and explicitly state which Step-1 branch it passes, or rephrase consistently to “geometry-QA PASS only; no sensitivity gate executed.”

- P3-E7. eROSITA ranking reproducibility gap in Table IV. The text states the top-298 membership list is ranked by the “committed raw-score artifact,” while Table IV prints only SIF,raw (IsolationForest) values. Without the raw-score column used for the ranking, readers cannot reproduce the listed order or audit ties. Required fix: add the committed raw-score values used to rank the membership list to Table IV (and to the public data file), or remove rank numbers from the table and present the list as an unordered membership.

MAJOR

- P3-M9. Full-sample scaler leakage not bounded for Gaia and NEOWISE. §II B discloses that scalers for Gaia and NEOWISE were fit on the full sample (leaks tail info), and only eROSITA received a bounded robustness check. Yet Gaia and NEOWISE selections are used in the catalog-grade/working counts. Required fix: either (a) re-run Gaia and NEOWISE with train-split-only scalers and report top-1% overlap/Jaccard vs. production; or (b) explicitly relabel both as exploratory pending scaler-robustness checks, mirroring the eROSITA “membership-only” framing.

- P3-M10. Planck top-200 patches include training data; no held-out stability is shown. §III F notes 152/200 released patches come from the training split; 48/200 from validation (overrepresentation of held-out, p ≈ 4×10−4). That’s good, but there is no robustness of the top-200 ranking on a pure-validation-only score pass. Required fix: publish the validation-only ranked top-200 list and report its overlap (Jaccard and rank Spearman) with the released list; if overlap < 90%, state that explicitly and carry both lists in the release.

- P3-M11. Mixed cone radii in SIMBAD “Total” row of Table I. The table’s per-survey unmatched fractions use 5″, but the “Total (cross-transfer, ACT-incl.)” unmatched fraction 58.8% is computed at 3″ (as noted later in §IV A). Reporting the 3″ aggregate in the 5″ table can mislead. Required fix: recompute the aggregate at 5″ for Table I, or drop the aggregate from the table and keep it only in §IV A with a clear 3″ label.

- P3-M12. “Largest multi-archive anomaly search” claim lacks a concrete comparative list. §VI E anchors to the largest prior single-survey catalog [11], but the “largest multi-archive” superlative is unsupported beyond “of which we are aware.” Required fix: add a short comparative table or paragraph citing prior multi-archive anomaly searches (if any), or explicitly confine the superlative to “largest point-source anomaly catalog we are aware of relative to the largest prior single-survey result [11].”

- P3-M13. LAMOST “98% blue-excess training-bias artifact” not quantified post-retrain. The artifact fraction (98%) is measured on the cross-transfer set; the native retrain compresses the anomaly rate by 21.5× but the paper does not re-tabulate per-arm dominance after retrain. The headline “98% artifact” thus mixes pre- and post-retrain samples. Required fix: provide the per-arm dominance histogram for the 113,342 native top-1% slice (or the stricter S>5 set) to substantiate the residual contamination claim, or rephrase to “cross-transfer artifact at 98%; native retrain shows 21.5× rate compression; post-retrain arm-dominance not re-tabulated.”

- P3-M14. False-overlap expectation (“≲10” across all survey pairs) undocumented. §IV A states “expected random coincidence contribution is ≲10 across all survey pairs” against 637 observed clusters. There is no derivation (surface densities, mask overlaps, or control trials). Required fix: add the calculation or Monte Carlo estimate (including radii and sky areas used) and report the resulting expectation with uncertainty.

- P3-M15. DESI training spectra in tail: fraction not reported. §III A clarifies overall k-fold/OOD robustness, but the exact number of the 47,000 training spectra that enter the S>5 anomaly set is not given. Required fix: report the count and fraction of training spectra in the 195,829 S>5 set, plus the fold-stability of those entries; if non-negligible, provide a DESI S>5 list with training spectra removed.

- P3-M16. “Rate” column semantics for fixed-count tiers. In Table I, Planck, Gaia, and NEOWISE “Rate (%) = 1.00” are predetermined selection fractions (top-1%) and, for Planck, the denominator later changes to 2×10^5 (0.10%). This invites misinterpretation as a measured anomaly frequency. Required fix: change the column header for fixed-count tiers to “Selection fraction” and add both 1.00% (20k bank) and 0.10% (200k bank) for Planck directly in the cell or footnote; avoid the word “rate” for fixed-count tiers throughout.

MINOR

- P3-m4. Planck KDE likelihood notation: define fyr explicitly. Eq. (E1) uses fyr but it is not defined in the main text/appendix (presumably 1/yr). Required fix: add “fyr ≡ 1 yr−1” immediately where Eq. (E1) appears.

- P3-m5. Novelty arithmetic clarity in §IV A (DESI top-10k). The text states “only 0.2% in SIMBAD; consistent with the expected 0.24% per-source false-match rate,” implying the matched fraction is consistent with chance. This is correct but easily misread. Required fix: add one sentence: “Observed SIMBAD matches: 20/10,000 vs. 24 expected from random coincidence (πr^2n); difference not significant.”

- P3-m6. Consistency of abbreviations for “top-1%”/“99th percentile.” Some places use “top-1%,” elsewhere “99th percentile.” Required fix: pick one term and use consistently; reserve “percentile” for empirical CDF context.

- P3-m7. Rounding consistency in percentages and uncertainties. Per-class DESI CIs are reported with two decimals (±0.02%, ±0.003%) while denominators are given as “∼4.9M”/“∼1.5M.” Required fix: either provide exact denominators with exact binomial CIs (preferred, e.g., Appendix table), or clearly state “rounded to two decimals for readability.”

- P3-m8. SIMBAD surface density nSIMBAD source. §IV A uses nSIMBAD ≈ 3.0×10−5 arcsec−2 but does not state how it was estimated (catalog count/area, footprint cut). Required fix: document the estimation method (e.g., HEALPix-averaged surface density outside the Galactic plane).

- P3-m9. Table I “Total unmatched 58.8%” footnote marker. The table shows “58.8¶¶” but the corresponding footnote text for ¶¶ is not present in the excerpted table block. Ensure the footnote is present and explicitly states the 3″ radius.

NITS

- P3-N4. Define KCMB once where first used (e.g., Planck preprocessing footnote), and use consistently.

- P3-N5. Minor numeric precision: reporting Spearman ρ > 0.9999999 for Planck top-200 reproducibility is over-precise for the scientific point. Consider rounding to ρ > 0.9999.

NO other contradictions, dimensional inconsistencies, or stale numbers were found beyond those already listed here and in my initial review.