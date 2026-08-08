# P3 RA-INT — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p3_anomaly_engine/paper3_draft.pdf` md5=24ac287f pages=30
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7424 chars)
**Wall time**: 412.9s

---

Referee report on “Spectrally Unusual Sources at Scale: A Multi-Survey Catalog …” (30 pp)

Scope of review
I evaluated the methodology, internal arithmetic consistency, statistical validity, and provenance/reproducibility claims across the full manuscript, including all tables, figures, equations, captions, and the abstract/conclusions. Below I list findings with severity class (ESSENTIAL, MAJOR, MINOR, NIT), precise location, the issue, and the required fix.

ESSENTIAL findings

P3-E1 — Table I and text: inconsistent Ntotal vs. stated Planck native 2×10^5 patch bank
• Location: Table I (page 9) “Path-C unique (primary)” row; §III F (pages 12–13), Appendix footnote in Table VI (page 25)
• Issue: The paper states the Planck native retrain re-scores an independent 2×10^5-patch bank (page 12–13; Table VI footnote), but the “Path-C unique” Ntotal reported in Table I is 37,272,042, which equals the cross-transfer total minus ACT (−20,000) and still implicitly uses 20,000 Planck patches, not 200,000. If 200,000 Planck patches were actually processed, Ntotal should be larger by +180,000 relative to the cross-transfer-with-ACT-removed figure (i.e., ≈37,452,042), not smaller by 20,000. The abstract headline “37.3 million sources and CMB map patches” also implicitly depends on this consistency.
• Required fix: Recompute and correct all Ntotal figures to reflect the actual Planck native re-score bank size used in the Path-C results (and update the abstract “37.3 million” if needed). If the Table I Path-C Ntotal is intended to remain on a different basis (e.g., the original 20,000-patch bank for comparability), this must be stated explicitly in the table caption and the abstract revised to avoid implying a processed volume inconsistent with the Path-C workflow. Provide a single authoritative Ntotal used for headline claims.

P3-E2 — Tier labeling: “recommended” tier includes components that fail validation and are not reproducible
• Location: Abstract (page 1); Table I footnotes ♠/§⋆ (pages 9–10); §VII Conclusions (pages 21–22)
• Issue: The “recommended tier” (269,317 unique; 269,117 point-source after removing 200 Planck) includes Gaia and eROSITA anomalies, even though both explicitly fail the 5σ injection–recovery gate; eROSITA’s per-object SBigAE score axis is irreproducible; Gaia preprocessing is lineage-inferred and cross-validation stability is 41%. The same pages also define a separate “validated catalog-grade subset” that excludes these components. This is internally contradictory and risks misinterpretation by readers who will reasonably equate “recommended” with “validated.” 
• Required fix: Either (a) redefine the “recommended” tier to include only validated catalog-grade components (DESI, SDSS native, Planck native, NEOWISE geometry-QA) and report updated counts consistently in abstract, Table I, and conclusions; or (b) rename the current 269,317-tier to “recommended+exploratory” (or “full Path-C except LAMOST”) and reserve “recommended”/“catalog-grade” exclusively for the validated subset. All headline numbers must then track this adjusted terminology consistently.

P3-E3 — Validated-only dedup count given as a non-recomputable lower bound
• Location: Abstract (page 1) “… validated catalog-grade subset of ≥268,519 unique (≥268,319 point-source) … not recomputable from the committed aggregate artifacts …”
• Issue: A PRD methods paper cannot report a primary catalog headline as an unverifiable lower bound because the exact validated-only 5″ re-dedup “is not recomputable.” This undermines reproducibility and independent verification.
• Required fix: Recompute the validated-only 5″ deduplication from the per-survey native lists and provide an exact, auditably reproducible number (with a frozen manifest). If this cannot be done, the manuscript is not acceptable for PRD as a catalog/methods paper.

P3-E4 — Data-availability placeholders instead of persistent identifiers
• Location: Data availability (page 24), Abstract (page 2 mentions public release “with the arXiv posting”)
• Issue: The manuscript contains placeholders (“will be publicly released with the arXiv posting,” “A Zenodo DOI will be minted at submission and cited here in place of this sentence”), but no stable DOI(s) or frozen release tags/hashes. PRD requires finalized, citable, persistent artifacts at acceptance.
• Required fix: Provide (i) a minted DOI for the full catalog release (and version tag/commit hash of the GitHub code), (ii) a frozen, hash-verified data manifest consistent with the manuscript’s final numbers (including the validated-only dedup), and (iii) a stable archive for any large artifacts referenced in the text (e.g., the 2×10^5 Planck patch bank indices used for scoring).

P3-E5 — Cramér’s V expression written incorrectly
• Location: §IV B (page 15): “Cramér’s V = √(χ^2/(N·(k−1))) = 376,713/(378,280 × 24,048) ≈ 0.0064”
• Issue: The equation shows the square-root definition, but then equates it to the unsquared ratio 376,713/(378,280 × 24,048). Numerically 0.0064 is the square-root of that ratio, but the written equality is mathematically incorrect.
• Required fix: Correct the displayed equation to show the intermediate ratio and then the square root, e.g., V = √[376,713/(378,280 × 24,048)] ≈ √(4.14×10^−5) ≈ 0.0064.

P3-E6 — Overuse of internal versioning/audit file paths in main text
• Location: Numerous places throughout (e.g., pages 3–6, 12–13, 21–26). Examples: “pipelines/p3_anomaly_engine/…/log.json”, “…/ext3_fm1_erosita_scaler_refit.json”, “…/r24conf_pod_session_batch.json”, etc.
• Issue: The manuscript embeds internal file paths and run-log references extensively in the main text. PRD articles must be self-contained and citable without private pipeline internals. Such detail belongs in supplementary material or a data/code release README, not the main text.
• Required fix: Move all internal file-path references and run-log filenames to a Supplementary/Reproducibility appendix or the online repository’s README. Retain in the main text only citable, stable identifiers (e.g., DOI, repository tag/commit hash, and clear section/table/figure references). Replace in-text file paths with concise references to the relevant supplemental material.

MAJOR findings

P3-M1 — Mixed “rate” bookkeeping in Table I risks misinterpretation
• Location: Table I (pages 9–10), notes under symbols ∥ and caption text
• Issue: The totals row reports “Rate (%)” 0.86% (cross-transfer) and 1.01% (Path-C) while the caption cautions these are bookkeeping ratios mixing fixed-count tiers with data-driven ones. Given the prominence of these rows, many readers will inadvertently cite these as measured anomaly frequencies.
• Required fix: Remove the “Rate (%)” entry from the total rows, or replace with “n/a (bookkeeping only; see caption).” Also add an explicit boldface warning in the table body near those cells that these are not to be interpreted as measured frequencies.

P3-M2 — “Largest application … of which we are aware” novelty claim needs explicit literature basis
• Location: Abstract (page 1), §VI E (page 21)
• Issue: The claim is currently anchored to comparison with a single-survey benchmark [11]. For a PRD-level novelty assertion, a short explicit survey (or a table) of prior multi-archive anomaly-detection efforts (if any) and single-archive scale limits should be included, or the claim softened.
• Required fix: Either (a) add a short paragraph and citation set demonstrating that no larger multi-archive autoencoder anomaly search exists by total sources processed, or (b) soften the claim to “to our knowledge, larger than any published single-survey anomaly catalog.”

P3-M3 — Injection–recovery reporting lacks uncertainties and full protocol detail
• Location: §II D step 5 (pages 5–6), Fig. 10 (page 23), §III C/§III D/§III F (pages 10–13)
• Issue: The text states “500 planted signals per survey at six amplitude levels” but does not report binomial uncertainties for the quoted 5σ points, nor the randomization details (seeds, placement rules per survey) for all cases (some details exist for Planck). For PRD methods, readers need error bars/intervals attached to the gate decisions and a crisp protocol statement.
• Required fix: For each survey and plant morphology used in the gate decision, report n and k at 5σ, the binomial standard error (or Clopper–Pearson intervals), and the planting randomization rules. State the seeds (or seed derivation) and ensure the artifact is frozen with a DOI/tag.

P3-M4 — “Score-knee” selection for eROSITA is undefined
• Location: §III E (pages 11–12); Table I notes (#) (page 10)
• Issue: The eROSITA membership list (n=298) was selected at a “score-knee” of a production run whose axis is irreproducible. While the authors candidly mark the per-object score axis as non-reproducible, the term “score-knee” remains ambiguous as a selection rule.
• Required fix: Define precisely the knee-point procedure used in the production run (algorithm and parameters), or remove the reference and present the eROSITA selection solely as the “top-298 of the committed raw-score artifact” (which you already state). Make certain the release contains the raw-score values and rank order to allow independent re-formulation.

P3-M5 — ACT DR6 inclusion in Fig. 2 (baseline map) risks being misconstrued as a science result
• Location: Fig. 2 caption (page 7)
• Issue: While the caption does say ACT is quarantined and contributes zero to the headline, plotting ACT positions on a primary-figures page risks misinterpretation.
• Required fix: Move the ACT scatter to an appendix-only figure, or gray it out with an “Excluded (quarantined)” legend and a watermarked overlay inside the panel. Add “Appendix F (methodological record only)” in the figure legend.

MINOR findings

P3-m1 — Abstract-first vs body order mismatch on DESI scale multipliers
• Location: Abstract (page 1), §VII point 1 (page 21)
• Issue: Abstract quotes several “×” multipliers (∼141×, ∼100×, ∼73×) before the later careful caveat on like-for-like vs. full-stream. While caveats exist in the abstract, please mirror the precise phrasing used in §VII to minimize misreading.
• Required fix: In the abstract, add “process-scale, full-stream multipliers; not like-for-like science-target comparisons” immediately after the multipliers.

P3-m2 — Clarify use of different null procedures and metrics in proximity
• Location: Throughout §V and §V A (pages 17–20)
• Issue: The manuscript is generally careful (“not directly comparable” notes are present for σ(fNL) vs. shot-noise-normalized baselines; Bayes factors vs. σ-shifts). Add an explicit sentence wherever two different significance notions are juxtaposed (e.g., Fig. 9 vs. Appendix C or Fisher envelope vs. central).
• Required fix: Insert one-line reminders near these juxtapositions: “These metrics are not directly comparable.”

P3-m3 — SDSS “S > 5 yields only 12” vs continuity-slice 77,905: consider a one-sentence recap in §III C
• Location: §III C (page 10)
• Issue: The three thresholds are well documented in the footnote; a single in-body sentence summarizing why the 77,905 continuity slice is preserved (cross-survey continuity base) would help standalone readers.
• Required fix: Add a one-sentence rationale in the SDSS subsection body.

P3-m4 — Provide explicit counts for DESI training pool cross-validation splits
• Location: §II B (pages 3–5), §II D step 1 (page 5)
• Issue: You report the 5-fold Jaccard statistics precisely. Add the fold sizes (train/validation counts per fold, which should be 37,600/9,400 from 47,000) for completeness.
• Required fix: Add those numbers in §II D step 1 or in a short parenthetical.

NITs

P3-N1 — Typo/notation precision
• Location: §II B (page 4), “z is always written z with astrophysical context; the anomaly score S is never called ‘z’…” — slightly awkward repetition; consider rephrasing to “To avoid confusion, we reserve z for redshift and S for the standardized reconstruction residual.”
• Required fix: Wording cleanup.

P3-N2 — Units in Fig. 5 caption
• Location: page 13
• Issue: State explicitly “67″ on a side” after the pixel conversion for clarity.
• Required fix: Add “(~67 arcsec per side)” if space allows.

P3-N3 — Consistency of significant figures
• Location: scattered (e.g., “0.006, p = 0.35” vs. “r = 0.0005, p = 0.92” on page 15)
• Required fix: Use uniform sig figs (typically two to three) for correlation coefficients and p-values.

Arithmetic and statistical spot checks (selected)

- DESI anomaly rate: 195,829 / 22,504,897 ≈ 0.00870 (0.87%). OK.
- SDSS continuity slice: 77,905 / 1,925,279 ≈ 0.0405 (4.05%). OK.
- NEOWISE pole-cap excess: expected cap area fraction 2×(1−cos10°)/2 ≈ 1.52%; observed 17/436 ≈ 3.90%; ratio ≈ 2.57×; binomial z ≈ 4.05, p ~ 5×10^−5 to 8×10^−5 depending on continuity correction. Your “2.6×; z ≈ 4.0; p ≈ 6×10^−5” is consistent. OK.
- Totals: native counts sum to 388,493; minus 10,213 collapsed = 378,280 unique; point-source = 378,080 after removing 200 Planck patches. OK.
- LAMOST exploratory contribution: 113,342 − 4,379 = 108,963; 378,280 − 269,317 = 108,963. OK.
- Wilson 68% CI for 178/1000: √[p(1−p)/n] ≈ 0.0121; you quote ±1.2%. OK.
- Fisher envelope: F0 = 1/8.98^2 ≈ 0.01239; adding c α^2 with α=0.19 and c=0.0747 yields σ≈8.14; envelope edges [3.92, 8.98] using α±σ_α = [0.84, −0.46 → 0]. OK.
- NANOGrav γ shifts: (3.0−2.567)/0.382 ≈ 1.13σ; (4.33−2.567)/0.382 ≈ 4.61σ. OK.
- Cramér’s V numeric: √[376,713/(378,280×24,048)] ≈ √(4.14×10^−5) ≈ 0.0064. Numeric OK; expression needs fix (P3-E5).

Scope and length
At 30 pages with extensive in-text provenance and audit-path details, the manuscript is long for the claimed methodological contribution. Many pipeline file paths and run-log specifics can be moved to supplemental material without loss of clarity. Recommended maximum main-text page count: ≈20–22 pages, with a consolidated reproducibility appendix or external README carrying the run-level detail.

Abstract-last drift sweep
Most abstract claims map to body text with appropriate caveats. Exceptions requiring action:
- “37.3 million sources and CMB map patches” must be reconciled with the corrected Path-C Ntotal once P3-E1 is resolved.
- The “recommended tier contains 269,317 unique entries” must be relabeled or redefined per P3-E2, and the validated-only dedup must be made exact (P3-E3).

Provenance surfaces
The Data availability section must be converted from placeholders to final DOIs and frozen hashes. Claims such as “not recomputable” are not acceptable for a PRD catalog paper and must be resolved.

## Summary recommendation
MAJOR REVISIONS

The manuscript is technically sophisticated and includes many laudable self-checks and caveats. However, several essential issues must be addressed for PRD standards: (i) inconsistent Ntotal accounting for the Planck native bank; (ii) the contradictory use of “recommended” for a tier containing non-validated, non-reproducible components; (iii) an unverifiable lower-bound headline for the validated-only unique count; and (iv) lack of finalized, persistent data/code identifiers. Additionally, the widespread inclusion of internal pipeline file paths should be moved to supplementary material, and injection–recovery reporting needs binomial uncertainties and a concise, reproducible protocol statement. Once these are resolved (and the abstract/table language updated accordingly), the paper could be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS (fresh-eyes pass only; do not repeat prior items)

ESSENTIAL

P3-E7 — Planck “Rate (%)” inconsistency: 1.00% vs 0.10% (native-bank basis not aligned)
• Location: Table I (page 9; Planck row), footnote ♢ (page 10), §III F (pages 12–13)
• Issue: The Planck row shows Rate = 1.00% (top-200 of 20,000 cross-transfer patches) while §III F and footnote ♢ clarify the released tier is the top-200 of a 2×10^5 native re-score bank (i.e., 0.10%). Presenting 1.00% in the main table body without a visible in-row qualifier is misleading and inconsistent with the native Path-C basis used elsewhere.
• Required fix: Replace the Planck table-cell value with “0.10% (native; fixed-count 200/200,000)” or “n/a (fixed-count; see caption),” and confine any 1.00% figure to an explicit cross-transfer-only column or the footnote. Ensure that all places quoting a Planck “rate” use the same basis.

P3-E8 — “Total (cross-transfer, ACT-incl.)” SIMBAD-unmatched 58.8% is on an incommensurate basis
• Location: Table I totals row (pages 9–10), §IV A (page 14)
• Issue: The table’s “Total (cross-transfer, ACT-incl.)” lists SIMBAD-unmatched = 58.8%, but §IV A makes clear this 58.8% comes from a separate pooled top-100-per-survey exercise at a 3″ radius (235/400), not from the table’s cross-transfer totals. Mixing a 400-object, 3″-radius statistic into the totals row invites mis-citation as a catalog-wide fraction.
• Required fix: Remove that 58.8% from the totals row, or mark it “n/a (derived from a separate 3″, top-100-per-survey pooled test; see §IV A).” If retained, add boldface text in the cell itself indicating it is not computed from the totals row.

MAJOR

P3-M6 — SDSS cross-transfer “S” axis reaches 1.9×10^11 but is labeled as the same S of Eq. (2)
• Location: Fig. 3 (right panel) + caption (page 8), §II B (pages 3–5), §III C (page 10)
• Issue: The SDSS cross-transfer histogram shows S up to 1.9×10^11 on the y–axis labeled “Anomaly score S,” while Eq. (2) defines S as a validation z-score. Such magnitudes are physically implausible for a z-score and stem from reuse of DESI µval, σval on out-of-distribution SDSS spectra (acknowledged in text). However, the panel axis itself does not warn that these are cross-transfer scores on a DESI-trained normalization and are not interpretable as z-units.
• Required fix: Relabel the axis in the panel (and/or add an in-figure inset) to “S (DESI-trained cross-transfer scale; arbitrary units, not z-units)” to prevent readers from interpreting 10^10–10^11 values as standardized deviations. Echo this clarification in the figure caption in the first sentence of the right-panel description.

P3-M7 — Planck top-200 training/validation split “significance” lacks a correlation-corrected uncertainty
• Location: §III F (page 13; “naive binomial p ≈ 4 × 10−4 … spatially correlated”)
• Issue: The text quotes a naive binomial p-value (~4×10−4) for the 48/200 validation-split overrepresentation, then notes spatial correlation inflates the effective sample size, making the quoted p a lower bound. As written, the number will likely be cited as-is.
• Required fix: Either (a) provide a block-bootstrap/jackknife p-value with the adopted block size (or correlation length) and report both naive and corrected values, or (b) remove the numeric p and state “over-representation toward held-out patches is observed; a correlation-corrected significance will be provided in the released reproducibility notebook.”

P3-M8 — Table I “SIMBAD-unmatched (%)” per-survey vs aggregate radii are not signposted at point-of-use
• Location: Table I body (pages 9–10), §IV A (page 14)
• Issue: Per-survey SIMBAD fractions in Table I use 5″, whereas the 58.8% pooled metric (already addressed above) uses 3″. The caption notes this elsewhere, but the table itself gives no per-row reminder, and the pooled 58.8% appears in the same “SIMBAD-unmatched (%)” column.
• Required fix: Add a column footnote marker on each per-survey value: “5″ cone; pooled aggregate in totals row is from a separate 3″ test (see §IV A).”

MINOR

P3-m5 — Fig. 8 “display score” vs catalog score exception is confusing
• Location: Fig. 8 caption (page 18), §IV C text near Fig. 8
• Issue: The caption correctly warns that burned-in “display scores” are not catalog scores; but the body text then highlights that panel (d) equals the catalog cross-transfer value (49.5). This one-off exception invites confusion about the other panels.
• Required fix: Amend the caption to add: “Only panel (d) happens to match the catalog score by coincidence; all other burned-in values are non-catalog display metrics.”

P3-m6 — Appendix E Eq. (E1) unit conventions for logs need to be stated explicitly
• Location: Appendix E (page 26), Eq. (E1)
• Issue: The log terms implicitly assume fi and fyr are in the same units and Tobs is in years (so logs are of dimensionless ratios). The text sets fi = (i+1)/Tobs but does not explicitly declare the unit convention for fyr and Tobs.
• Required fix: Add one sentence: “All frequencies are in yr−1 (fi = (i+1)/Tobs, fyr = 1 yr−1) and Tobs in yr, so all logarithms in Eq. (E1) are of dimensionless ratios.”

P3-m7 — Table IV column header “Dec” is ambiguous
• Location: Table IV (page 12)
• Issue: The “Dec” column lists a single number although the IAU name already encodes both RA and Dec. The meaning is presumably declination, but the header alone is ambiguous.
• Required fix: Rename the header to “Declination (deg)” (or include both RA, Dec explicitly), or drop the “Dec” column since RA/Dec can be parsed from the IAU J-name, and provide both in the release table.

P3-m8 — Symbol definition for ecliptic latitude
• Location: §III H (page 13), Table I note † (pages 9–10)
• Issue: The symbol becl for ecliptic latitude is used without an explicit definition upon first appearance.
• Required fix: Define becl on first use, e.g., “|becl| denotes ecliptic latitude.”

P3-m9 — Minor consistency on Planck “fixed-count” language
• Location: Table I footnote ♢ (page 10), §III F (pages 12–13)
• Issue: Different phrasings are used for the Planck selection (“top-1% of 20,000” vs “fixed-count 200/200,000”). Unifying the wording would reduce confusion.
• Required fix: Standardize on “fixed-count 200 patches” and then specify the base bank size and implied percentage in parentheses for each context.

P3-m10 — Precision of “SIMBAD match-rate consistent with random” phrasing
• Location: §III A (page 6)
• Issue: The text says the 0.2% SIMBAD match rate in the DESI top-10,000 is “consistent with the expected 5″ random false-match rate of ≈0.24% per source.” The intent is clear, but “per source” could be misread as a catalog-level rate rather than a per-object chance.
• Required fix: Reword to “consistent with the expected per-object random-coincidence probability of ≈0.24% at 5″,” and give the implied expected count (~24 of 10,000) vs observed (~20) to make the comparison explicit.

Explanation
These additional items focus on (i) cross-basis inconsistencies that can mislead (Planck rate basis; pooled SIMBAD fraction in a totals row), (ii) labeling/axis clarity where out-of-distribution scaling makes the numerical range of S inherently non-z-like, (iii) statistical significance quoted without a correlation correction, and (iv) minor documentation/notation gaps. They complement, and do not repeat, the Essential/Major issues already raised in the initial review.