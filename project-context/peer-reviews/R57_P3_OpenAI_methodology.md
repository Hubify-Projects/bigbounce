# P3 R57 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/private/tmp/R57_P3/paper3_draft.pdf` md5=044460cc pages=31
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7303 chars)
**Wall time**: 326.8s

---

Referee report on “Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies and a Native-Trained Novelty Fraction from 37.3 Million Sources and Map Patches”

Scope of review
You asked for a methodology-focused audit: statistical validity, derivation chains, dimensional consistency, internal arithmetic, error propagation, claims vs. body support, and reproducibility. I read the full 31-page manuscript, including all figures, tables, equations, captions, appendices, and the data-availability section. Below I list all issues found, classified by severity, each with an ID, page reference, a specific problem quote, and the required fix.

ESSENTIAL (must fix before the paper can be considered)

P3-E1 (Data availability placeholders; provenance not finalized) — Section “Data availability,” p. 24/31
Problem: “will be made public with the arXiv posting … A Zenodo DOI will be minted at submission and cited here in place of this sentence (DOI inserted at submission).”
Required fix: Replace all future-tense placeholders with finalized, permanent DOIs/URLs. Provide: (i) frozen data-set DOI(s) for the catalog(s), (ii) model-weight DOI(s), (iii) training/inference code release DOI/commit-hash(s), (iv) a manifest with SHA-256 hashes that matches exactly what the paper used. PRD cannot accept “will be released” language.

P3-E2 (Internal run-tags and bookkeeping artifacts in the body) — Multiple locations (e.g., pp. 4, 5, 6, 7, 12, 13, 14, 17, 18, 20, 22, 25, 27)
Problem: The main text repeatedly includes internal audit filenames and run-tags (“r24conf_pod_session_batch.json”, “r23conf_dedup_audits.json”, “…_R54.json”, “recovered_pod_scripts”, “ext3_fm1_…”, etc.). These are version-tracking artifacts, not stable scholarly references.
Required fix: Move all such internal paths and round-tags to a Reproducibility Appendix or to the data release README. In the body text, cite only stable DOIs/URLs and the minimal identifier needed for an external reader to verify the claim. Remove “R##-round” and similar internal references everywhere in the main text.

P3-E3 (Gaia DR3 preprocessing unrecoverable — non-reproducible tier) — §II.B (tabular preprocessing) p. 3/31; §III.G p. 14/31
Problem: “the exact 20-feature production script … was not recovered … specification is lineage-inferred rather than directly recovered… selection is training-sample-conditioned … treat as exploratory.” This is not reproducible under PRD standards, yet the Gaia tier contributes to the “catalog-grade” count of 269,317 (§III D, Table I footnote ♠).
Required fix: Either (a) fully reproduce the Gaia preprocessing/code and rerun the Gaia tier to make it strictly reproducible; or (b) remove Gaia from any “catalog-grade” or headline counts and isolate it as an explicitly non-reproducible exploratory appendix with no contribution to any headline figures.

P3-E4 (Ambiguous “catalog-grade” definition includes components explicitly labeled as exploratory or failing gates) — Abstract p. 1/31; Table I footnote ♠ pp. 7–8/31; Conclusions item 6–7 p. 23/31
Problem: The “catalog-grade tier contains 269,317 unique entries” but two of the six components in that count (Gaia, eROSITA) are stated to be exploratory (Gaia XV-stability 41%, eROSITA 1.2% injection-recovery and irreproducible score axis). NEOWISE “pass” is a geometry-only QA, not a detector sensitivity gate.
Required fix: Rename the tier to something non-normative (e.g., “primary deduplicated tier with per-object validity flags”) or restrict the “catalog-grade” label to surveys that clear detector-sensitivity gates with reproducible preprocessing (DESI, SDSS-native, Planck-native). Present Gaia, eROSITA, and NEOWISE (geometry-QA only) as exploratory/flagged, and exclude them from any label that implies robust validation.

P3-E5 (DESI training–test leakage not fully quantified at catalog level) — §II.B–C pp. 4–5/31; §III.A pp. 8–10/31; §VI.D (i) p. 22/31
Problem: The DESI catalog is scored on the full 22.5M including the 47k training set. While you provide 5-fold Jaccard and an OOD seed-control test, there is no explicit rerun excluding the training spectra from the scored catalog to show its effect on the S > 5 membership and rate.
Required fix: Provide a DESI rerun (or a differential recount) that excludes the 47,000 training spectra from the 22.5M scoring stream. Report: delta in the S > 5 tail count and the membership overlap. If the change is negligible, document it; if not, update headline counts and uncertainty statements accordingly.

P3-E6 (eROSITA per-object score axis irreproducible but used in-text; reproducibility gap) — §III.E pp. 11–13/31; Table I pp. 7–8/31
Problem: You state explicitly that the production SBigAE axis is irreproducible and that 0.259 cannot be reconciled with any committed monotone rescaling. Nonetheless the text still refers to “S > 0.259” and “score-knee” without a formal procedure.
Required fix: Eliminate every use of SBigAE values for eROSITA in the paper text and figures; present the eROSITA component strictly as a fixed membership list (n = 298) with no numeric anomaly-score values. If you wish to publish a score, it must be a reproducible axis (e.g., the raw-IF axis you already compute). State clearly that “298 sources constitute a fixed membership release; there is no valid per-object SBigAE score.”

P3-E7 (Abstract-last drift — “≈0.9×” vs body’s ≈0.92× like-for-like recount) — Abstract p. 1/31; §III.A Table II p. 10/31
Problem: Abstract: “science-class-restricted recount finds only 2,468 DESI anomaly clusters … ≈ 0.9× the benchmark’s 2,685”. 2,468/2,685 = 0.919 ~ 0.92×, not 0.9×. The body uses “≈0.9×” elsewhere as well.
Required fix: Replace “≈ 0.9×” with “≈ 0.92×” consistently, or give the exact fraction.

P3-E8 (Undefined “score-knee” selection procedure) — Multiple places, e.g., Table I footnotes ♡, ♠, # pp. 7–8/31; §III.E p. 11–13/31
Problem: You frequently refer to “score-knee” thresholds (e.g., SDSS top-1% score-knee at S ≥ 0.2051; eROSITA 0.259 “score-knee”) without formally defining the algorithmic procedure to locate the knee (elbow) and without a reproducible software reference.
Required fix: Define the “score-knee” quantitatively (e.g., Kneedle, second-derivative maximum, piecewise-linear SSE elbow, etc.), include the algorithm and parameters used, and deposit the code with a DOI. For eROSITA, if the axis is irreproducible, do not present a numeric knee at all (see P3-E6).

P3-E9 (Mixing sigma/“significance” measures across different nulls without explicit non-comparability at every juxtaposition) — §V pp. 18–21/31; §V A p. 20/31; Conclusions p. 23/31
Problem: You correctly state some non-comparability (e.g., fixed-α vs empirical-α, and that σ(fNL) and γ posterior shifts are different observables), but there are juxtapositions where that caveat is absent in-sentence. Example: §V end and Conclusions item 5 discuss σ(fNL) “central 9.4% improvement” and, immediately after, the NANOGrav γ result with +1.13σ without repeating “not directly comparable.”
Required fix: At every juxtaposition of σ(fNL) forecast intervals and the PTA γ posterior shift/Bayes factor, explicitly prepend “statistically not directly comparable” (or separate with a sentence that repeats the caveat).

MAJOR (significant revisions required)

P3-M1 (Terminology drift and tiering logic) — Abstract p. 1/31; §II.D pp. 5–6/31; Table I footnotes pp. 7–8/31; §VII p. 23/31
Problem: The paper uses “catalog-grade,” “primary,” “exploratory,” “validated,” and “membership-only” in overlapping, sometimes conflicting ways. E.g., the “catalog-grade” tier includes components that fail the 5σ injection-recovery gate (Gaia, eROSITA) and NEOWISE’s mask-only QA.
Required fix: Standardize tier definitions at the start (one paragraph, a table, and a legend code used throughout) and enforce them consistently in text, tables, and figures. Reserve “catalog-grade” for components that pass detector-sensitivity gates and are reproducible; everything else should be “exploratory/flagged.”

P3-M2 (Gate thresholds: heuristic, not pre-registered; limited plant morphologies; sensitivity analysis missing) — §II.D pp. 5–6/31; Fig. 10 p. 23/31
Problem: You acknowledge the gates are heuristic and not pre-registered. Emission-line plants give very different performance than continuum-dip plants, and only two spectral morphologies are tested.
Required fix: Add a short sensitivity study: recoveries for at least two additional spectral morphologies (e.g., broad-line-only, narrow doublets) with typical S/N per survey. Provide a supplementary table of recoveries vs. morphology and S/N. If not possible now, explicitly qualify all PASS/FAIL language as morphology-dependent and update the main claims accordingly.

P3-M3 (DESI “score vs SNR” correlation derived on a stratified sample; p-value depends on design) — §III.A p. 9/31
Problem: You correctly note the p-value reflects the stratified design, but you use p = 0.12 language that some readers may interpret as population-level. The population-weighted analysis is “queued.”
Required fix: Either remove the p-value from the main text and keep only the effect size (|ρ| = 0.03), or add a population-weighted random subsample result (effect size and p-value) now.

P3-M4 (Cramér’s V formula typesetting is wrong/ambiguous, though the numeric value is right) — §IV.B p. 16/31
Problem: You write: “Cramér’s V = √χ2 / √/(N · (k − 1)) = 376,713/(378,280 × 24,048) ≈ 0.0064.” The printed formula shows the ratio without the square root on the fraction, although the value 0.0064 is consistent with V = sqrt(χ2/(N(k−1))).
Required fix: Correct the printed formula to V = sqrt(χ2/(N(k−1))) and show one line of arithmetic to make it transparent.

P3-M5 (NEOWISE “PASS” is a geometry check only) — Abstract p. 1/31; §III.H p. 14/31; Fig. 10 p. 23/31
Problem: Although you insert caveats in §III and Fig. 10, the Abstract still reads as if NEOWISE “passes injection-recovery,” which can be misread as a detector sensitivity validation.
Required fix: In the Abstract, add “(geometry-only QA; not a detector-sensitivity test)” immediately after the NEOWISE PASS claim, mirroring the parenthetical detail you give later.

P3-M6 (Largest/scale novelty claims need explicit literature support) — Abstract p. 1/31; §VI.E p. 22/31
Problem: Claims like “largest application … of which we are aware” should be backed by a compact, explicit comparison (survey, Nprocessed, Nanom) in-text (not just a footnote to [11]). The field is moving; PRD requires verifiability.
Required fix: Add a one-paragraph survey of prior large-scale anomaly catalogs (refs, N processed, Nanom) and a table row comparing to your 378,280/37.3M numbers.

P3-M7 (“Genuine novelty fraction” still relies on a finite catalog set; definition must be explicit and not over-interpreted) — §IV.A p. 15/31
Problem: You do a commendable job of downscoping SIMBAD non-matches, but the “genuine novelty” metric still depends on a choice of 18 catalogs. That is fine, but the definition must be stated once, formally.
Required fix: Define “genuine novelty” explicitly as “absent from the union of the following 18 catalogs queried via CDS X-Match (list), 5″ radius.” Repeat that any other catalogs could reduce the rate; do not let “genuine” appear unqualified at new first mentions.

P3-M8 (Planck top-200 training/validation imbalance test: quantify spatial correlation impact) — §III.F p. 13/31
Problem: You correctly note that the 48/200 validation over-representation may be inflated by spatial correlation of patches and call for a block-bootstrap. As written, the “p ≈ 4 × 10−4” is a lower bound that some will over-interpret.
Required fix: Either (a) add a simple block-jackknife estimate (e.g., tile-level re-sampling) to corroborate the direction/magnitude, or (b) remove the numeric p-value and state only the qualitative direction (“over-representation toward held-out patches, opposite to memorization”).

P3-M9 (Use of “membership-only” eROSITA tier yet reporting a “0.03% rate”) — Table I p. 7/31; §III.E p. 11–13/31
Problem: You note the “rate” is a fixed-count selection, not a detection rate. The table still lists “0.03%,” which many readers will misread as an empirical anomaly frequency.
Required fix: In Table I, replace the eROSITA “Rate (%)” entry by “— (fixed n = 298)” with a footnote explaining no inference on an anomaly rate should be drawn.

MINOR (address before acceptance)

P3-n1 (Arithmetic audits)
- p. 6/31 dedup-radius sweep: unique counts 378,604 / 378,280 / 378,145 for 3″/5″/7″; “maximum unique-count variation of 0.086% relative to the 5″ result”: 324/378,280 = 0.0857% (OK). Please show both deltas explicitly (3″ vs 5″; 7″ vs 5″) for clarity.
- p. 1/31 “73×” DESI-over-[11]: 195,829/2,685 = 72.9 (OK). Add the exact divisor (2,685) once in the Abstract for transparency.

P3-n2 (Terminology: “score-knee” on SDSS top-1%) — Table I footnote ♡ p. 7–8/31
Problem: “top-1% score-knee set S ≥ 0.2051” — top-1% is a percentile cut; adding “score-knee” is confusing here.
Required fix: Remove “score-knee” at this instance (keep it where you use an elbow method), or define precisely.

P3-n3 (Units/axes in captions)
- Fig. 5 caption: add units for W1–W2 (“magnitudes”) and explicitly label the image cutout scale in arcseconds in the first sentence to match the pixel count now in sentence 2.

P3-n4 (Bibliography)
- Verify all arXiv IDs and years (e.g., [12] “Mon. Not. Roy. Astron. Soc. 547, Issue 2 (2026), arXiv:2506.17376” — future-dated arXiv IDs are placeholders). Replace with actual bibliographic details or “in press” with a valid arXiv link.

P3-n5 (SIMBAD false-match expectation)
- §IV.A p. 15/31: 0.24% per object → “∼ 460 expected false matches among the 195,829 DESI anomalies”: 195,829 × 0.002356 ≈ 461. OK. Add a sentence that the local-density correction near the Galactic plane could raise Pfalse locally and is deferred.

P3-n6 (Clarity on “Total (cross-transfer, ACT-incl.)” row) — Table I p. 7/31
Problem: The label suggests ACT-inclusion in the total; ACT is quarantined elsewhere.
Required fix: Add an inline note “(includes ACT’s 200 cross-transfer patches; excluded elsewhere)” in the table caption for full clarity.

P3-n7 (Equation (E1) context)
- Appendix E p. 27/31: Define ρi explicitly (dimensionless strain power per bin or equivalent) so the log10 expression’s dimensional consistency is unambiguous.

P3-n8 (Minor wording/typos)
- Several long em-dash chains and duplicated hyphens could be streamlined. A language pass will help readability without changing content.

NIT (cosmetic)

P3-N1 (Formatting) — Tables/footnotes, e.g., Table I
The dense footnote deck (♡, ♠, ♢, #, ¶, †, ∥, §, ⋆, ¶¶) is hard to navigate. Consider moving the longer methodological exegesis to a short Methods Appendix and keep the table footnotes strictly definitional.

P3-N2 (Figure 3 right panel)
The y-axis range spans >10 orders of magnitude and labels may be too small to read at journal column width. Consider adding an inset zoom around the 10^3–10^5 body for readability.

P3-N3 (Redundant caveats)
Phrases like “should not be interpreted as …” repeat very often. They are valuable but could be consolidated to sharpen the prose.

Length
At 31 pages, this is long for the claimed methodological contribution. Much of the length is internal run-audit and per-survey gate bookkeeping that could move to a Supplement/Appendix. I recommend trimming the main text to ≤24–26 pages by:
- Moving per-survey cross-transfer baseline details and internal artifact pathnames to Supplement.
- Consolidating the injection-recovery/gate narrative into one master figure + one methods appendix table.
- Moving Appendix D (image galleries) and some pedigree text to online supplement.

Abstract-last drift audit
I re-read the Abstract after the full review. Most load-bearing claims are consistent with the body and carry appropriate caveats (notably for novelty and NEOWISE). Two corrections are essential:
- Replace “≈ 0.9× the benchmark’s 2,685” with “≈ 0.92×”.
- Insert “(geometry-only QA; not a detector-sensitivity test)” immediately after “NEOWISE” in the gate claim, to mirror the body.

Standalone-reader test
The paper is largely self-contained. Two places break the rule:
- “Score-knee” is used without a formal definition (see P3-E8).
- “Genuine novelty fraction” should be defined once formally (P3-M7).

Effect sizes
You provide useful effect sizes (Cramér’s V, fractional improvements) in several places. Correct the Cramér’s V formula as per P3-M4 and keep the practice throughout.

## Summary recommendation
MAJOR REVISIONS

The submission presents a substantial and careful piece of work with many good methodological practices (explicit gates, cross-validation, thorough caveats). However, for PRD standards the paper still has critical issues: (i) non-finalized data/code provenance (placeholders), (ii) inclusion of a non-reproducible Gaia tier inside a “catalog-grade” count, (iii) eROSITA’s irreproducible score axis still referenced numerically, (iv) ambiguous “score-knee” without a formal definition, and (v) minor but real abstract/body arithmetic drift. Addressing the essential items (final DOIs/manifests, tiering cleanup, removing irreproducible axes, defining “score-knee,” and quantifying DESI training leakage) and the major clarifications will bring the paper up to PRD methodological rigor.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS AFTER SECOND-PASS AUDIT (fresh-eyes; do not repeat prior items)

ESSENTIAL

P3-E10 (LAMOST exploratory count ambiguous/misalleading in Abstract) — Abstract p. 1/31
Problem: “excludes the LAMOST exploratory tier (∼ 113,000 objects retained as a methodological lesson…)”. The body shows 113,342 LAMOST detections in the native top‑1% slice but only 108,963 unique LAMOST objects after 7‑way 5″ dedup (4,379 merge into catalog-grade clusters; Table I footnote ♠).
Required fix: Disambiguate in the Abstract: report both the pre-dedup detection count (113,342) and the post-dedup unique-object count (108,963), and make clear which number is used where.

P3-E11 (Processed-count inconsistency for Planck; total “37.3M processed” undercounts by 180k) — Abstract p. 1/31; Table I; §III F; Table VI footnote †
Problem: The Abstract headline “37.3 million sources and map patches” and Table I Ntotal add up Planck as 20,000 patches, but the Path‑C native re‑score actually processes 200,000 Planck patches (25.3 s at ~8,000 patches/s). This creates a mismatch between what was “processed” (200k) and what is tallied in Ntotal (20k).
Required fix: Make the accounting consistent. Either (a) define “processed” to include the 200k Planck native bank and update the 37.3M total accordingly (~37.45M), or (b) state explicitly that Table I’s Ntotal follows the cross-transfer input basis for Planck (20k) while the native re‑score processed 200k, and adjust the Abstract wording to “counts based on Table I Ntotal” (or similar). Prefer (a) for accuracy when claiming “largest by total processed.”

MAJOR

P3-M9 (“Anomaly rate shows no correlation with Galactic latitude”: metric/wording mismatch) — §IV B p. 16/31; Fig. 7
Problem: The text states “the anomaly rate shows no correlation with Galactic latitude (Spearman r = 0.0005, p = 0.92)”, but the plotted statistic (Fig. 7 bottom right) is anomaly score vs. angular distance, i.e., a per-object score–latitude correlation, not a rate (counts per area, normalized by coverage).
Required fix: Correct the statement to “anomaly score shows no correlation with Galactic latitude” or provide a true rate analysis (e.g., per-HEALPix anomaly counts normalized by exposure/coverage) with its own statistic and uncertainties.

P3-M10 (Aggregate SIMBAD-unmatched 58.8% is presented in Table I “Total” row but derives from a different denominator/procedure) — Table I p. 7/31; §IV A p. 15/31
Problem: The “Total (cross-transfer, ACT‑incl.)” row shows 58.8% unmatched, but this number is actually from a separate pooled top‑100 per survey (four surveys only) at 3″, not the per-survey 5″ convention. This invites misinterpretation as a table-consistent total.
Required fix: Replace that cell with “—” and move the 58.8% to a caption footnote explicitly stating its separate denominator and 3″ radius, or add an inline clarifier directly in the Total row cell.

MINOR

P3-n9 (Planck Ntotal=20,000 vs native re‑score 200,000 is confusing at a glance) — Table I p. 7/31; §III F; Table VI footnote †
Problem: Readers may assume Ntotal equals “processed.” Here it mixes cross-transfer input (20k) with native inference (200k).
Required fix: Add a “Nscored(native)” column for Planck (200,000) or add an asterisk on the Planck Ntotal cell pointing to footnote ♢ making the 20k vs 200k distinction unmistakable.

P3-n10 (Totals “Rate (%)” cells can still be misread as empirical rates) — Table I p. 7/31
Problem: Even with footnotes, the 0.86% and 1.01% in total rows look like inferred frequencies.
Required fix: Change those two total-row “Rate (%)” entries to “— (bookkeeping only; see caption)” and keep the explanatory footnote.

P3-n11 (Over-precision on extreme correlation) — §III F / Table VI footnote †
Problem: “Spearman ρ > 0.9999999” for Planck rescoring reproducibility is over‑precise and unlikely to be stable across platforms.
Required fix: Report to three decimals (e.g., ρ > 0.999) and provide the exact computation seed/code reference in the reproducibility appendix rather than in text.

P3-n12 (Clarify which quantity is tested in the “no dust correlation” claim) — §IV B p. 16/31
Problem: The text states “no correlation with Planck dust intensity,” but does not say whether the test is on counts per pixel, per-object score, or spatial density normalized by completeness.
Required fix: Specify the tested observable (e.g., per-object score vs τ353 at source positions) and add a sentence noting that a rate–dust test would require a coverage model (deferred).

P3-n13 (Define “SIF,raw” units/normalization) — Table IV p. 13/31
Problem: The IsolationForest score column “SIF,raw” is said to be on a “~0–3.5×10^4 scale,” but no definition is provided (path length? transformed anomaly score?).
Required fix: Add a one‑line definition (e.g., “mean path length transformed to anomaly score via …, higher = more anomalous”) and cite the code/parameters used.

P3-n14 (Figure–text micro-consistency on SDSS “top‑1% score‑knee”) — Table I footnote ♡; §III C
Problem: “top‑1% score‑knee set S ≥ 0.2051” mixes percentile and elbow terminology; elbow is not needed here.
Required fix: Drop “score‑knee” for the SDSS top‑1% selection (keep elbow terminology only where an elbow method is actually used).

P3-n15 (Explicit two-sided vs one-sided for binomial z) — §III H p. 14/31
Problem: The NEOWISE polar-cap excess significance is given as “binomial z ≈ 4.0, p ≈ 6×10−5” with no one‑ vs two‑sided qualifier.
Required fix: State whether p is one‑sided (as appropriate for an excess test) and keep the qualifier.

P3-n16 (Computational table completeness) — Table VI p. 25/31
Problem: Planck native CAE “Train time” is “—†”, despite other rows listing times.
Required fix: Provide the wall‑clock (even approximate) or explicitly state that it was not recorded and is therefore omitted by design.

P3-n17 (Terminology: “rate” vs “count”) — Multiple
Problem: Several places use “rate” loosely when the quantity is a count or fraction under a fixed-count selection (eROSITA, Planck, NEOWISE).
Required fix: Audit wording to ensure “rate” is used only for data-driven frequency estimates; elsewhere use “count,” “fixed-fraction,” or “predetermined count.”

NIT

P3-N4 (Figure 5 caption completeness) — Fig. 5 p. 14/31
Problem: W1−W2 units are not explicitly stated; the first sentence mentions pixel scale only in pixels.
Required fix: Add “W1−W2 in magnitudes” and state the cutout angular size in arcseconds in sentence one.

P3-N5 (Total-row label could still confuse about ACT inclusion) — Table I p. 7/31
Problem: Although the caption discusses ACT, the label “ACT-incl.” may still puzzle quick readers given ACT’s quarantine elsewhere.
Required fix: Append “(historical cross-transfer baseline including ACT’s 200 patches; excluded from Path‑C)” to the label or caption.

Explanation
These issues emerged from a targeted second pass focusing on arithmetic cross-checks, caption/body alignment, dimensional/null comparability, and table labeling. They were not covered in the first review and, while many are clarifications rather than conceptual faults, several directly affect headline clarity (processed counts; “rate” vs “score” wording; LAMOST exploratory count in the Abstract). Addressing them will further tighten the manuscript to PRD standards.