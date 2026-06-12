# P5 R35conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/p5_desi_chirality_v0.1.68.pdf` md5=8f7957f4 pages=31
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (3969 chars)
**Wall time**: 571.7s

---

Referee report on: “Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test ...” (31 pages)

Scope of review
- Focus: methodology rigor, statistical validity, internal arithmetic consistency, dimensional analysis, and abstract–body concordance as required by Physical Review D.
- I read the full manuscript and audited all tabulated/quoted scalars in the Abstract, Conclusions, and key tables/figures. Where applicable, I recomputed σ, χ², p-values, and effect-size measures from the numbers provided.

Headline checks that pass
- Appendix B contingency tables (Tables XVI–XVII) are internally consistent. For Table XVI (CW/CCW × V-Web class), each row’s CW+CCW = n and column totals sum to 812,793. For Table XVII (V-Web class × program on the bright+dark subset), each row’s bright+dark = n and the row totals sum to 811,609 as stated. These tables are properly cross-referenced from §VI A.
- Abstract headline per-class fCW, n, and σ-from-half values match Table III exactly. The 4×2 homogeneity test reported in the Abstract (χ² = 3.55, p = 0.31) is consistent with the table counts.
- The ∆fCW = +0.0007 DESIVAST-anchored void vs non-void contrast (Table VIII) with SE = 0.00219 (z = 0.31, p = 0.76) is arithmetically correct from the tabulated counts.
- Phase-2 sweep thresholds and p-values are consistent with the normal approximation and NMC = 1000 permutation resolution; Bonferroni thresholds quoted (e.g., |σ| ≈ 3.09 for K = 5, α = 0.01) are correct.
- Effect-size reporting for the very large χ² in the class×program table includes Cramér’s V = 0.078, which is arithmetically consistent with χ² = 4932 and n = 811,609.

Findings

ESSENTIAL (must fix before PRD publication)
P5-E1. Versioning/provenance language in main text
- Location: Title page (p. 1) and throughout; explicit instance: “(Dated: June 2026 — v0.1.68-2026-06-12)”.
- Problem: PRD articles must not carry internal build/version identifiers, round-tracking, or iteration logs in the scientific narrative.
- Required fix: Remove all internal version strings from the Title/Date line and body. Retain such identifiers only in a formal Data/Code Availability section or external repository metadata.

P5-E2. Draft-history and withdrawal commentary embedded in the main narrative
- Locations (non-exhaustive): §VI D, pp. 11–12 (“An earlier draft quoted ... withdrawn ...”); §VIII D, p. 18 (“An earlier draft reported ... reproduced exactly only under ... defect”); §VII/Table VII note and adjacent text; §IX B/C and multiple other places.
- Problem: The manuscript includes extensive internal revision history (“earlier draft”, “withdrawn numbers”, “superseded unfiltered-join version”, “defect”) that is inappropriate for the archival record.
- Required fix: Remove all draft-history commentary from the main text. If absolutely necessary, move to a short “Provenance notes” appendix or repository README, and present only the final, audited numbers in the manuscript.

P5-E3. Data/code DOI missing
- Location: Appendix C, Data and code availability (p. 31).
- Problem: The text states “A DOI-minted archival snapshot ... accompanies journal submission” but does not provide a DOI or an immutable release tag. PRD requires a stable, citable record of the exact version used.
- Required fix: Provide a minted DOI (Zenodo/Dataverse/OSF) for the exact repository snapshot corresponding to this submission, and state the immutable tag/commit hash in the manuscript.

MAJOR (significant revision)
P5-M1. Mixed bases for low-z non-void totals not explicitly reconciled where used
- Location: §VIII B (Table VIII) vs. §VIII E (p. 19–20).
- Problem: Table VIII uses the KDTree k = 20 hole-union membership (non-void n = 621,964), while §VIII E footprint retabulation references the exact-membership base (non-void n = 621,864). The manuscript does explain the 100-object delta in §VIII B, but the later section does not explicitly restate that it switches to the exact-membership base.
- Required fix: In §VIII E, add a one-sentence explicit reminder that all numbers in that paragraph use the exact-membership base (621,864), not the k = 20 base (621,964), to eliminate any possible confusion.

P5-M2. Overlength and editorial structure
- Location: Entire manuscript (31 pages).
- Problem: The methods/results are sound, but the main text is encumbered by repeated in-line path pointers to JSON artifacts and pipeline internals. The core scientific contribution (environmental-independence null, DESIVAST cross-checks, and sensitivity analysis) could be presented more concisely.
- Required fix: Reduce the main text by 25–35% by (i) removing draft-history prose (P5-E2), (ii) consolidating most in-line artifact file-path references into a single Reproducibility Appendix or external README, and (iii) moving implementation detail that is not load-bearing to Supplementary Material.

P5-M3. Consistency of terminology for the tidal-tensor classifier
- Location: §§I, IV and throughout.
- Problem: The manuscript uses “V-Web” to refer to an implementation of the Hahn (2007) tidal-tensor “T-Web.” A footnote clarifies this, but the dual use can confuse readers.
- Required fix: Standardize terminology early: e.g., “We implement the Hahn (2007) tidal-tensor (‘T-Web’) classifier; for continuity with prior work we refer to our implementation as ‘V-Web’ hereafter.” Then use a single consolidated term throughout.

P5-M4. Concentrate reproducibility pointers
- Location: Numerous sections include in-line filesystem paths to artifacts (e.g., pipelines/.../outputs/*.json) within the scientific prose.
- Problem: While commendable for reproducibility, such pointers belong in a dedicated Data/Code Availability section or Supplementary Material to keep the narrative focused.
- Required fix: Move most of these path references to Appendix C or Supplementary Material. In the main text, keep only high-level references (e.g., “see Data/Code Availability for exact artifacts”).

P5-M5. Abstract rounding consistency for HEALPix p-values
- Location: Abstract (p. 1) vs. Table VI (p. 12).
- Problem: Abstract lists “p = 0.61/0.135/0.413”; Table VI has 0.607/0.135/0.413.
- Required fix: Harmonize rounding. Either quote all to three decimals consistently (0.607/0.135/0.413) or state that values are rounded.

MINOR (address but can proceed)
P5-N1. Notation “σfrom half”
- Location: Throughout (e.g., §V, §VI).
- Problem: The manuscript uses “σfrom half” for the one-sample binomial z against p = 0.5. While defined, the label is unconventional and occasionally appears without a space (e.g., “−0.68σfrom half”).
- Required fix: Consider adopting “binomial z (vs 0.5)” or simply “z” after definition, and fix spacing.

P5-N2. Typographic accents and minor typesetting
- Locations: e.g., “Cram´er’s V” (pp. 11–12; should be “Cramér’s”), stray hyphenation around “σfrom half —” in several places.
- Required fix: Correct diacritics and spacing.

P5-N3. Clarify Jeffreys-interval usage once
- Location: §V (p. 6).
- Problem: Jeffreys intervals are used, but no formula is given. Not mandatory, but a parenthetical reference to the Beta(1/2,1/2) posterior credible interval formula would help a standalone reader.
- Suggested fix: Add a one-sentence reminder or a citation to a standard reference.

P5-N4. ASTRA overlap table filtration note
- Location: Table XIV (p. 27) and caption.
- Problem: The table reports “Range and max |σ| filtered to classes with n ≥ 100,” but for the V-Web-on-overlap line the visible class counts include void/wall = 1/2, which readers may find confusing.
- Required fix: Add “metrics exclude classes with n < 100” in the caption to re-emphasize that the reported range/max|σ| exclude those tiny bins.

Methodology/statistics audit—selected recomputations

- Binomial z definition and usage: σ = 2(f − 0.5)√N is used consistently. Recomputed for Table III: filament (−2.61), cluster (−4.66), wall (+0.55), void (−0.68): all correct to two decimals.
- Bonferroni thresholds: Eq. (2) |σ|Bonf = √2 erfc−1(α/K) evaluated for K = 5, α = 0.01 gives 3.09; for K = 1054, α = 0.05 gives ≈ 4.05. Correct.
- Phase 2 sweep residuals: The reported max |σobs − σpred| ≤ 1.87 (Table VII) is consistent with σpred = 2∆f√N at ∆f = −0.0026. The Rs = 10 rows are correctly flagged as grid-unresolved.
- Density quintiles: With N = 158,327 per quintile, σpred ≈ 2.07; computed residuals in Table IV agree (max residual ≈ 1.87 < 3.09 Bonferroni threshold).
- DESIVAST-anchored contrasts: For VoidFinder, ∆ = +0.00067 with SE = 0.00219 ⇒ z = 0.31 (p = 0.76): matches the text. V2-REVOLVER (sphere), ∆ = −0.0019, SE ≈ 0.0017 ⇒ |z| ≈ 1.12; V2-VIDE similar; catalog-native GALZONE two-sample contrasts are consistent with the reported SE and z.

Abstract–body concordance (pattern-045)
- All headline scalars in the Abstract were traceable to Tables III, VI, VII, VIII, X, XI, XII, and §VIII F. The claims are calibrated as “no evidence” rather than “proof of equality,” and the look-elsewhere corrections and monopole-subtraction caveats are carried into the body. No abstract overclaims detected.

Standalone-reader test (pattern-046/047)
- The work depends on “Paper IV” for the chirality catalog and the catalog-wide classifier monopole. However, the chirality labels are publicly hosted (HuggingFace link provided) and the manuscript re-estimates the matched-sample monopole (fP5 = 0.49719) and uses it where appropriate (Table XII), mitigating dependence on the companion paper. This is acceptable for PRD provided the data DOI is supplied (P5-E3).

Uncomputed/qualitative claims (pattern-048)
- Claims such as “range dominated by void counting noise,” “no cell below 0.05,” and “null after Bonferroni correction” are all backed by numbers or artifact pointers. No uncomputed quantitative claims identified.

Effect sizes
- Large-sample χ² is accompanied by Cramér’s V; class-level deviations are translated to percentage points; where appropriate, σpred from the monopole is subtracted and residuals are compared. Satisfactory.

## Summary recommendation
MAJOR REVISIONS

The statistical methodology is careful and, on audit, internally consistent. The primary conclusions (null environment dependence; DESIVAST-anchored contrasts consistent with zero; sensitivity checks) are supported by the numbers as presented. However, the manuscript in its current form contains extensive draft-history commentary and internal pipeline provenance woven into the narrative, and it lacks a minted DOI for the exact analysis snapshot. PRD requires a clean, archival presentation. I therefore recommend major revisions focused on: (1) removing draft-history/withdrawn-number prose from the main text; (2) providing a concrete DOI and immutable tag for the code/data snapshot; (3) consolidating reproducibility path references into an appendix; (4) minor editorial consistency fixes listed above. With these addressed, the paper would meet PRD methodological standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-audit pass)

P5-M6. Duplicate-row fraction is misstated (2.7% vs ≈3.6–3.7%)
- Locations: Abstract; §VI A main text; Fig. 3 caption.
- Issue: The manuscript repeatedly states “2.7% duplicate rows,” but the env-labeled parent has 812,793 rows covering 783,820 unique TARGETIDs, i.e. 28,973 extra rows. That is 28,973/812,793 ≈ 3.56% of the row-level parent and 28,973/783,820 ≈ 3.70% of the unique-spiral count, not 2.7%.
- Impact: Small quantitative inconsistency that recurs in multiple prominent places (Abstract, figure caption). The design-effect inflation shown, sqrt(812,793/783,820) ≈ 1.018, matches the 3.6–3.7% duplication, so the 2.7% text is likely a stale value.
- Required fix: Replace “2.7% duplicate rows” with “≈3.6–3.7% duplicate rows” consistently; retain the correct design-effect computation already shown.

P5-N5. σvs monopole for the filament class in Table XII is off by ≈0.1σ
- Location: §VIII F, Table XII (filament row).
- Issue: Using the stated definition σvs monopole = 2(f − fP5)√N with fP5 = 0.49719 (812,793-row env-labeled parent) and the Table III filament numbers (f = 0.498048, N = 408,187) gives σvs monopole ≈ +1.09, not +0.99 as tabulated. Cluster and wall rows match within rounding; the filament row is low by ≈0.1σ.
- Possible cause: Mixing the row-level vs unique-galaxy monopoles, or rounding fP5 differently. The text elsewhere notes both parents give nearly identical monopoles, so a 0.1σ drift is unexpected.
- Suggested fix: Recompute σvs monopole for the filament class from the exact inputs and state which parent monopole (row-level vs unique) is used for Table XII. Update the table value or add a footnote if a different reference was used.

P5-N6. Clopper–Pearson expression is typeset ambiguously
- Location: §VIII A (0/6 small-sample illustrative cross-match).
- Issue: The one-sided 95% upper bound for 0/6 is written as “1 − 0.051/6 = 39%.” This likely intends 1 − 0.05^(1/6), but as typeset it reads like 0.05 × (1/6).
- Required fix: Typeset explicitly as 1 − 0.05^(1/6) ≈ 0.393 (39.3%) to avoid ambiguity.

P5-N7. Figure 9 panel comparability could be clarified
- Location: Fig. 9 caption and surrounding text (§IX B).
- Issue: The left panel shows the V-Web full-sample canonical run, while the right panel shows the Tempel-overlap sample. The caption notes “full-sample canonical run, shown as reference,” and the like-for-like concordance is computed correctly in text. Still, readers may visually (mis)compare the two panels.
- Suggested fix: Add a brief sentence in the caption: “Left panel is not directly comparable to the right panel’s counts; quantitative like-for-like comparisons use the overlap-only numbers stated in text.”

P5-N8. Minor rounding mismatch in the Abstract’s “duplicate-rows do not drive the verdict” parenthetical
- Location: Abstract.
- Issue: The Abstract says “783,820 unique-spiral subset, so the 2.7% duplicate rows do not drive the verdict.” Per P5-M6 the correct duplicate rate is ≈3.6–3.7%. The conclusion is unchanged, but the percentage should be corrected for consistency with the design-effect calculation already shown.
- Required fix: Adjust the percentage in the Abstract to ≈3.6–3.7%.

NO OTHER NEW ARITHMETIC OR METHOD MISMATCHES FOUND
- I rechecked the remaining headline numbers (Table III σ, Table VIII/IX/X contrasts/SE/z/p, Table IV quintile residuals vs prediction, Table VI HEALPix p-values vs caption, Table VII sweep pLEE and ranges, Table XI per-bin σ, Appendix B contingency totals). All recomputed values agree within rounding or depend on intermediate data not provided but are internally coherent with the manuscript’s definitions.
- Equations and dimensional analysis remain consistent (e.g., σpred = 2Δf√N; Poisson/tidal-tensor units). Figure captions match body claims and units. Abstract statements are traceable to body tables/sections and do not overclaim, aside from the duplicate-percentage correction noted above.