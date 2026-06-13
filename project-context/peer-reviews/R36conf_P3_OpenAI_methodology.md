# P3 R36conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper3_anomaly_catalog_v3.1.101.pdf` md5=2cba9f61 pages=28
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6334 chars)
**Wall time**: 301.2s

---

Referee Report (Methodology/Statistics) — Physical Review D

Summary of manuscript
The authors present a multi-archive anomaly-detection catalog (“Path-C”), applying native-trained autoencoders to seven data sets (DESI, SDSS, LAMOST, eROSITA, Planck CMB patches, Gaia, NEOWISE). Headline: 378,280 unique anomalies (378,080 point sources + 200 Planck patches) after 7-way 5″ deduplication of 388,493 detections. They quantify training/bias controls, injection–recovery gates, and a small set of cosmological applications: a multi-tracer fNL Fisher forecast based on an empirically estimated bias ratio α, and a 2-parameter MCMC fit to NANOGrav 15-yr KDE free-spectrum with a matter-bounce template.

Below I audit arithmetic, statistical claims, internal consistency, reproducibility, and scope. I recomputed all quoted percentages/ratios that can be derived from in-text numbers; where I could check, the arithmetic is generally consistent. However, I find several essential issues that must be corrected before the paper can be considered for PRD.

Findings

ESSENTIAL

P3-E1 (Section V, page 16; Table V row (i), page 21) — Dimensional/typographical error in the Fisher mapping
- Offending text: “F0 = 1/8.982 = 0.01239 (units: 1/σ(fNL)2); … 1/σ2 = F0 + c α2”
- Problem: Numerically, 0.01239 = 1/(8.982)2, not 1/8.982. The written expression is dimensionally wrong and inconsistent with the numeric value and with the intended mapping where α = 0 must reproduce σ(fNL) = 8.98 via 1/σ2 = F0.
- Required fix: Correct all occurrences to F0 = 1/(8.982)2 = 0.01239 and restate the units as dimensionless (or “in units of 1/σ2”). Verify that no downstream numeric uses elsewhere in the text or figures incorrectly used 1/8.982.

P3-E2 (Abstract, page 1) — Inaccurate “top-1% cut” language for DESI
- Offending text: “the DESI count is a top-1% cut of the full 22.5-M-spectrum scan…”
- Problem: In the body (e.g., Section II.B, pp. 4–5 and Table I), DESI uses an absolute S > 5 cut with an empirical rate of 0.87%, not 1%. Calling it a “top-1% cut” is inaccurate and risks misinterpretation of rates and consistency checks.
- Required fix: Replace with “an absolute S > 5.0 cut corresponding to a 0.87% rate on 22.5M spectra.” Ensure all other “top-1%” references for DESI are removed or corrected.

P3-E3 (Sections IV.B, page 14; Appendix/Table VI footnote †, page 23) — Version-history/internal-draft language in the body
- Offending text: “An earlier draft quoted 38,330 pixels … withdrawn”; “an earlier draft listed 10.6 s … has been withdrawn.”
- Problem: PRD does not allow version-history commentary or “earlier draft” bookkeeping in the body text.
- Required fix: Remove all version-history statements and rephrase neutrally. Report only the final, reproducible result (with artifact pointer if needed), or omit the quantity if it cannot be reproduced.

P3-E4 (Data availability, page 22) — Non-final placeholders for DOI/release; incomplete provenance
- Offending text: “will be publicly released with the arXiv posting,” and “A Zenodo DOI will be minted at submission and cited here in place of this sentence (DOI inserted at submission).”
- Problem: For PRD acceptance, data/code artifacts must be citable and immutable. Placeholders are not acceptable.
- Required fix: Provide final, public DOIs for all data products (catalog, Planck patch list), and frozen commit hashes/tags for code repositories. Ensure that the release manifest referenced in the text matches the actual DOI/tags and that the release is accessible at review time.

P3-E5 (Section III.E, pages 10–11; Table I footnotes; Table IV caption, page 11) — Irreproducible eROSITA score axis
- Offending text: Multiple places state that the published eROSITA SBigAE per-object score axis (threshold 0.259) is irreproducible from any committed artifact; selection is thus “membership-list-only.”
- Problem: For a methods paper, an irreproducible scoring axis is not acceptable unless entirely removed from any quantitative claims and tables, and the catalog component is clearly demoted to an exploratory list. As written, the paper still presents the 0.259 threshold in a way that looks load-bearing.
- Required fix: Either (a) fully reconstruct a reproducible scoring axis or adopt a reproducible alternative (e.g., the BigAE raw-MSE or IF-on-latent) and restate the selection accordingly; or (b) reframe eROSITA strictly as a membership-only exploratory tier with all score columns removed from the main paper, and ensure that no quantitative conclusion (counts, rates, overlaps, novelty) depends on that unrecoverable axis. The current hybrid presentation must be regularized.

P3-E6 (Abstract, page 1; several places) — Potentially misleading juxtaposition of “73×” DESI increase vs like-for-like “≈0.9×”
- Offending text: Abstract claims a “∼73×” DESI increase relative to [11], followed immediately by caveats.
- Problem: While you do note “not like-for-like” and later give the science-restricted recount (2,468 vs 2,685), the abstract still foregrounds the 73× figure, which is based on a fundamentally different denominator and can easily be misread as a science comparison. PRD abstracts must avoid headline metrics that are not apples-to-apples even when caveats follow.
- Required fix: Remove the “73×” claim from the abstract or replace it with the like-for-like statement only: “Restricted to DESI main-survey primary science targets, 2,468 anomalies are found, ≈0.92× the 2,685 of Liang et al.” You may keep the full-stream 195,829 count separately, but without converting it into an “×” comparison to [11].

MAJOR

P3-M1 (Structure/readability; throughout) — Heavy reliance on repository “artifact” pointers in lieu of in-paper definitions
- Problem: Numerous methodology-critical assertions point to JSON artifacts or script paths rather than specifying the numbers and procedures in the paper (e.g., exact k-fold splits, dedup sensitivity runs, scaler-refit robustness, OOD rescore seed, etc.). While reproducibility artifacts are welcome, PRD requires that the core methodology be self-contained.
- Required fix: For all load-bearing steps (training splits, validation selections, scaler fitting choice and implications, dedup radius sensitivity, Planck patch preprocessing), consolidate the full specification in the paper, with the repository as a supplement. Artifact pointers can remain, but the quantitative results they support should be recorded in the manuscript.

P3-M2 (Section III.F, pages 11–12; Table VI footnote †, page 23) — Training/validation bookkeeping for Planck native model; incomplete timings
- Problem: The paper stresses reproducibility and provides throughput numbers but states that the Planck native retrain wall-clock time “was not preserved.” In §III.F, top-200 patches include 152 training and 48 validation patches; while you argue this is standard for autoencoder scoring, PRD readers need a clear, held-out test demonstration that the anomaly ranking is not a memorization artifact.
- Required fix: Provide (i) the actual training wall-clock or remove runtime claims for that run entirely; (ii) a held-out-only top-N list and an overlap/ranking-stability analysis relative to the full score list (e.g., Spearman correlation and top-N overlap when scoring only on validation/held-out patches), beyond the mild “over-represented validation” statement. Quantify “no memorization” with a direct score-distribution comparison train vs val.

P3-M3 (Section II.B, page 3–4; Table I footnotes) — Mixed practice in scaler fitting (full-sample vs train-split), with only partial robustness checks
- Problem: You note that eROSITA scalers were fit on the full sample (not train split) and provide robustness with top-298 overlap. NEOWISE and Gaia lack the corresponding checks; Gaia’s preprocessing script was also not recovered, only “lineage-inferred.” These choices (and incomplete checks) materially affect anomaly ranking in tabular surveys.
- Required fix: Provide train-split-vs-full-sample scaler refits and top-k overlap statistics for NEOWISE and Gaia similar to the eROSITA check, or explicitly demote these tiers to exploratory-only in the main text. For Gaia, either recover the exact 20-feature production script or remove the “production” label and re-run a reproducible variant.

P3-M4 (Section IV.A, page 13; novelty) — Discovery-rate framing
- Problem: You do clearly distinguish the “58.8% SIMBAD-unmatched” database-coverage metric from the “17.8% genuine novelty” from CDS X-Match on DESI’s top-1,000. However, the 17.8% is presented for one stratum and one survey only, yet “novelty” is used elsewhere (e.g., Conclusions) in a catalog-wide tone.
- Required fix: Every use of “novelty fraction” outside §IV.A must explicitly state that 17.8% is a DESI top-1,000-stratum, single-survey estimate only, with no extrapolation to the full catalog. Consider adding a prominent caution box or a boldface qualifier the first time “novelty fraction” appears in the Abstract and Conclusions.

P3-M5 (Overlength and scope; entire manuscript) — The paper reads as a combined catalog + methods + cosmology forecast + PTA example. At 28 pages it is sprawling for the methodological advance claimed.
- Required fix: Condense to ≤20 pages by (i) moving the PTA MCMC details and much of the cosmology forecast discussion, including the shot-noise Fisher appendix, to supplemental; (ii) tightening long footnotes in Table I; (iii) consolidating descriptive catalog content (e.g., repeating the dedup accounting in multiple places).

MINOR

P3-m1 (Abstract and §III.A, pages 1 and 6–8) — Ratios and percentages
- Check: 195,829/22,504,897 = 0.00870 (0.87%); 2,468/190,015 = 1.30%; 2,468/20,299,155 = 0.0122%; “≈0.9×” of 2,685 is actually 0.918×; acceptable rounding but consider stating 0.92×.
- Required fix: Optionally replace “≈0.9×” with “≈0.92×” for precision.

P3-m2 (Table I, page 7; rates and bookkeeping notes)
- Check: Cross-transfer total 319,443/37,292,042 = 0.855% (0.86%); Path-C dedup compression = 10,213/388,493 = 2.629%.
- Required fix: None; numbers are consistent.

P3-m3 (Section III.H, page 12) — NEOWISE polar-cap fraction calculation
- Check: Two 10° caps yield area fraction 2 × (1 − cos 10°)/2 = 1.52%; observed 3.9% ⇒ 2.6× excess; correct.
- Required fix: None.

P3-m4 (Section IV.C, pages 15–16) — Dedup radius sensitivity
- Check: Unique counts 378,604 / 378,280 / 378,145 for 3″/5″/7″ → max deviation 324/378,280 = 0.0856%; stated 0.086% correct.
- Required fix: None.

P3-m5 (Figures; axis labeling)
- Fig. 3 (right): log–log axis on S spanning 102 to 1011 is clearly labeled; caption appropriately warns cross-transfer artifact. Fig. 7 axes include degrees; Fig. 5 panel has explicit (α, δ) units. Acceptable.
- Required fix: None.

P3-m6 (Section III.B, page 9) — Redrock z values for z≈6 candidates
- Suggestion: Add a note that these pipeline redshifts are low-S/N template fits and provide visual-inspection status (if any) or state explicitly that no visual confirmation has yet been performed.

P3-m7 (Terminology)
- The frequent use of “artifact” (in the repository sense) can be confused with “data artifact” (instrumental). Consider a short terminology note or replace “artifact” with “auxiliary file” or “record” to avoid ambiguity.

NIT

P3-n1 (Typos/notation consistency)
- Ensure consistent use of “z-scored” vs “standardized” in §II.B and avoid calling S values “z” anywhere (you already caution this; just ensure no stray uses remain).
- Use consistent notation for arcseconds (5′′) vs (5")—it alternates in captions and footnotes.

P3-n2 (Reference formatting)
- Verify that all references include year/journal consistently; e.g., [12] “Mon. Not. Roy. Astron. Soc. 547, Issue 2 (2026)” looks future-dated relative to submission month; confirm final citation data at acceptance.

P3-n3 (Duplicate phrasing)
- Scan for repeated constructs like “canonical canonical” etc. I did not find any egregious duplicates, but a final proofread is advised.

Statistical and arithmetic audit notes (selected recomputations)
- DESI 0.87%: 195,829 / 22,504,897 = 0.00870.
- DESI science-restricted 1.30% match among anomalies: 2,468 / 190,015 = 0.01298.
- Like-for-like vs [11]: 2,468 / 2,685 = 0.918.
- Total dedup compression: (388,493 − 378,280) / 388,493 = 0.02629.
- SIMBAD false-match rate at 5″ with n = 3.0×10−5 arcsec−2: π r2 n = π × 25 × 3e−5 = 2.36×10−3; expected false matches for 195,829 ≈ 462 (0.236%); aligns with text.
- DESI novelty fraction (CDS X-Match 18 catalogs): 178/1000 = 17.8%; σbin (68%) ≈ sqrt(p(1−p)/n) ≈ 1.21%; matches “±1.2%.”
- Fisher envelope for α = 0.19 ± 0.65 with corrected F0 (1/(8.982)2): 1/σ2 = 0.01239 + 0.0747 α2 ⇒ central σ = 8.14; lower-edge at α = 0.84 ⇒ σ ≈ 3.93; upper-edge clipping at α = 0 ⇒ 8.98. Correct, once F0 is squared in the text.
- NANOGrav MCMC: (3.0 − 2.567)/0.382 = 1.13σ; (4.33 − 2.567)/0.382 = 4.61σ; Bayes factor 3.23/(4.52×10−4) = 7.14×103; log10 B = 3.85; all consistent.

Effect-size/context checks
- You generally provide appropriate caveats distinguishing different null constructs (frequentist σ vs Bayes factor). Where sigma values from different procedures are juxtaposed (e.g., §V vs §V.A), you note they are not detections and that quantities are not directly comparable. This is good; keep these qualifications after edits.

Standalone-reader and provenance checks
- Several key results depend on external artifacts that are not strictly necessary to present in-paper (e.g., scaler refit overlaps, dedup radius sensitivity). Add the actual numbers into the manuscript for self-containment.
- Replace all “will be released” future tense with finalized DOIs and commit hashes.

Recommended maximum page count
- Recommend ≤20 pages main text and tables/figures, with PTA MCMC and detailed Fisher appendices moved to supplemental. The core methodology and catalog results can be presented more concisely.

## Summary recommendation
MAJOR REVISIONS

The manuscript contains substantive methodological work and extensive auditing. However, it cannot be accepted in its current form due to (i) an essential dimensional/typographical error in the Fisher mapping (F0 must be 1/σ2, not 1/σ), (ii) an inaccurate “top-1%” abstract statement for DESI that must be corrected, (iii) version-history language within the body text, (iv) non-final data/DOI placeholders, and (v) the unreproducible eROSITA score axis, which must be either reconstructed reproducibly or removed from load-bearing claims. Additional major issues concern readability/self-containment and Planck-native training bookkeeping. Addressing these items, plus the minor cleanups, will bring the paper to PRD standards.

---

## PASS 2 — self-critique findings (what initial review missed)

P3 — ADDITIONAL FINDINGS (second-pass audit)

ESSENTIAL

P3-E7 (Section III F; Table VI footnote †) — Mischaracterized train/validation composition of the Planck top-200
- Offending text: “the anomaly tail mildly over-represents held-out patches” (152 train, 48 validation; expected ≈170/30).
- Problem: Over-representation is statistically large, not “mild.” For n = 200, p = 0.15, observing 48 validation patches gives z ≈ (48 − 30)/sqrt(200×0.15×0.85) ≈ 3.6 (p ≈ 4×10−4). The direction indeed argues against memorization, but the characterization is inaccurate.
- Required fix: Quantify the significance (report binomial p-value) and add a held-out-only ranking test: e.g., compute score-distribution shift train vs validation, Spearman correlation of full vs held-out scores, and top-N overlaps (top-200 on validation-only vs full). This complements P3-M2 and corrects the “mild” wording.

P3-E8 (Table I; §III F) — Inconsistent rate denominator for Planck CMB tier
- Offending text: Table I lists “1.00%” for Planck with a caption note that the released tier is the top-200 of a 2×105 native bank (0.10%).
- Problem: The displayed “Rate (%)” column mixes denominators (20,000 cross-transfer vs 200,000 native re-score), which can be misread as a data-driven detection rate.
- Required fix: Harmonize denominators to the released selection pool (report 0.10%) or omit a percentage entirely for predetermined-count tiers. If you retain any percentage, state the denominator explicitly in the table cell or a dedicated column.

MAJOR

P3-M6 (Abstract; throughout) — “Largest-scale application across multiple archives” lacks a direct literature support
- Problem: The manuscript benchmarks against the largest single-survey catalog [11] but not against multi-archive anomaly searches. As written, the “largest-scale application … across multiple archives” claim is unsubstantiated beyond “of which we are aware.”
- Required fix: Either (i) add a brief literature comparison (citations and numbers) showing no prior multi-archive anomaly catalog at comparable scale, or (ii) soften to “larger than previously reported single-survey anomaly catalogs (to our knowledge)” and remove the cross-archive superlative.

P3-M7 (Sections V, VI D (i), Appendix C) — Internal inconsistency in the α-dependence and cross-referencing of the Fisher mapping
- Problem: The main text adopts a positivity-respecting quadratic mapping 1/σ2 = F0 + c α2, while Appendix C presents a linear-in-α sensitivity table obtained by scaling from α = 0.15. This mixes two different approximations. Also, the numeric c is introduced via a “5-α refit” located in §VI D (i), a section about DESI training overlap, making the cross-reference hard to follow.
- Required fix: Reconcile the dependence (state clearly that Appendix C is a fixed-α reference/illustration not used in the primary forecast) and move the “5-α refit” definition and c-value derivation into §V, with a clean cross-reference. Ensure there is a single, authoritative α-dependence in the main text.

P3-M8 (Table I; Fig. 6; §IV A) — SIMBAD-unmatched percentages mix heterogeneous strata and radii
- Problem: The DESI entry “∼99%” is from the top-10,000 stratum; other table entries appear to summarize full-tiers; Fig. 6’s pooled 58.8% is computed at 3″ while per-survey entries elsewhere use 5″.
- Required fix: For each per-survey SIMBAD fraction, state the denominator (e.g., “top-10K,” “full tier,” etc.) and the cone radius. Prefer a unified 5″ computation for the table, and note explicitly in Fig. 6 title/legend that the pooled figure uses 3″. Otherwise, readers will treat the mixed figures as directly comparable.

P3-M9 (Sections II B, III A; Table VII) — Metric inconsistency in arm-dominance classification
- Problem: Catalog selection and S use MSE, but per-arm dominance uses mean absolute residual (MAE). Without demonstrating invariance to this choice, “arm-dominance” could be sensitive to metric choice.
- Required fix: Either switch to per-arm MSE for consistency or provide a sensitivity analysis (MAE vs MSE per-arm) showing stable dominance assignments for the DESI sample.

MINOR

P3-m8 (§IV B) — Dust correlation reproducibility
- Problem: “no correlation with Planck dust intensity (Pearson r = 0.006, p = 0.21)” does not specify which dust map (e.g., τ353, E(B−V), I857), resolution/smoothing, or map version.
- Required fix: Specify the exact Planck dust layer, resolution, and any smoothing/windowing so the statistic can be reproduced.

P3-m9 (§III A) — Missing denominators and uncertainties for per-class DESI rates
- Offending text: “galaxies … 0.75% vs QSOs 0.037%.”
- Required fix: Add the underlying counts (numerator/denominator per class) and binomial uncertainties (e.g., Wilson 68% or 95%) to contextualize the “∼20×” statement.

P3-m10 (Fig. 6; Table I) — Clarify mixed radii
- Problem: Fig. 6 pooled result uses 3″ while table entries use 5″.
- Required fix: Add “(3″ pooled)” to the figure title or legend, and a pointer to the 5″ per-survey results in Table I.

P3-m11 (Appendix E, Eq. E1) — Variable definition/units
- Problem: ρi is not explicitly defined (strain PSD? characteristic strain per bin?) and units are not stated.
- Required fix: Define ρi and its units explicitly so dimensional meaning of Eq. (E1) is clear.

P3-m12 (Table VI; Appendix F) — ACT DR6 runtime/training numbers in the main computational table
- Problem: Including quarantined ACT DR6 training/throughput in Table VI can confuse readers.
- Required fix: Move ACT computational numbers to Appendix F only, or label them prominently as “quarantined, cross-transfer only.”

P3-m13 (§IV C, main text) — Compression percentage context
- Problem: “2.629% compression” appears in prose without an immediate numerator/denominator.
- Required fix: On first mention in the main text, append “(10,213/388,493)” for self-containment.

P3-m14 (Global) — Significant-figure consistency
- Problem: Some ratios are given at three significant figures (e.g., 0.012%) while others are rounded (“∼0.9×”).
- Required fix: Standardize rounding/significant figures (e.g., one or two significant digits for fractions unless a precise comparison is needed), and apply uniformly.

NO REPEATS
The issues above are in addition to (and do not duplicate) those raised in the initial review (P3-E1…P3-n3).