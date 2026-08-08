# P3 RP3-INT-v125 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p3_anomaly_engine/paper3_draft.pdf` md5=c4700948 pages=32
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (5948 chars)
**Wall time**: 363.4s

---

Referee report for PRD (cosmology methods) — methodology/statistics audit

I have read the full 32-page manuscript, all figures, tables, equations, captions, and the abstract, and recomputed every quoted key scalar, percentage, and significance that can be checked from what is printed. Below I list all findings classified as ESSENTIAL, MAJOR, MINOR, and NIT, each with an ID, page, the specific issue (with quotation when applicable), and the required fix.

ESSENTIAL

P3-E1 (Abstract; also §III, pp. 1–2, 6–9): Headline “validated” count is only a lower bound (≥ 268,519) because the exact validated-only 5″ re-deduplication “is not recomputable from the committed aggregate artifacts.”
- Problem: A PRD headline quantitative result cannot be a non-reproducible lower bound. The abstract and conclusions prominently quote this number.
- Required fix: Rebuild and publish an exact validated-only 5″ de-duplication using a committed script and frozen inputs, and replace “≥ 268,519” with the exact unique-object count (and the exact point-source count). Deposit the script and manifest with frozen hashes/DOI.

P3-E2 (§III E, Table I p. 8; §III E text pp. 12–14; Table IV p. 14): eROSITA per-object anomaly score axis is irreproducible (“0.259 threshold could not be reconciled with any tested score axis… per-object SBigAE score axis is irreproducible”).
- Problem: The manuscript still prints the non-reproducible numeric threshold “0.259” in Table I and text, and calls the selection “published top-298” while acknowledging the axis cannot be reconstructed.
- Required fix: Remove all references to the non-reproducible threshold value from the main text, abstract, and tables. State unambiguously that the eROSITA tier is a membership list only; provide the reproducible raw-score axis and the exact rank-298 raw-score threshold used to sort the membership list; deposit the raw-score file with hashes/DOI. If you wish to quote any threshold, it must be on a reproducible axis.

P3-E3 (§III A pp. 9–11; §VI D(i) p. 23): No DESI injection–recovery curve; DESI is nevertheless included in the “validated catalog-grade subset.”
- Problem: DESI is the anchor survey and central to the paper’s scientific claims. Other surveys are validated by detector-sensitivity injection–recovery; DESI is not. The two Jaccard stability gates and a top-200 visual-inspection null are not substitutes for a sensitivity characterization.
- Required fix: Perform and report a DESI injection–recovery study (with the same continuum-dip and emission-line plants used elsewhere), giving the recovery-vs-amplitude curve and the recovery at 5σ (with uncertainties), and include the planting files. Alternatively, if you cannot add this, do not label DESI “validated;” reclassify it transparently (and adjust the validated subset definition and abstract accordingly).

P3-E4 (Data Availability, p. 26): Data release not yet public; DOI “will be minted… cited here in place of this sentence.”
- Problem: PRD requires that the data and code used to produce the results be publicly available at acceptance. “Will be made public” and a placeholder for a DOI are not acceptable.
- Required fix: Mint the DOI, deposit all referenced artifacts (catalogs, code, weights, scripts, and any MCMC chains), and replace all future tense with live links, DOIs, and frozen commit hashes in the paper. Include a concise table of artifacts with SHA-256 hashes matching what is in the repository.

P3-E5 (Abstract p. 1; §III, §VI D(ii) pp. 6–7, 25): “Validated catalog-grade subset” includes NEOWISE, which “passes a masking-geometry QA gate… not a detector-sensitivity test.”
- Problem: Conflating geometry QA with detector-sensitivity validation under the same “validated” umbrella is misleading.
- Required fix: Either (a) provide a detector-sensitivity injection–recovery test for NEOWISE on synthetic photometric anomalies, or (b) reclassify NEOWISE outside the “validated catalog-grade” subset and update all headline counts and language to distinguish “detector-sensitivity validated” from “QA-validated.”

P3-E6 (Table I p. 8; §III C pp. 11–13; §IV C p. 19): The headline 7-way unique-object count 378,280 depends on an arbitrary SDSS “continuity slice” (77,905) chosen to match the cross-transfer count; this is not an objective threshold.
- Problem: The primary headline total should not be anchored to an ad hoc fixed-size slice. You show the sensitivity (re-running dedup with SDSS top-1% and S > 5), which changes the unique-object total by tens of thousands.
- Required fix: Define the headline deduplicated total using only objective, per-survey thresholds (e.g., DESI S > 5, SDSS top-1% native, etc.) and move the continuity-slice analysis to a sensitivity appendix. Report the headline total and all multipliers with the objective-threshold configuration, and explicitly bound sensitivity to the SDSS threshold in the main text.

MAJOR

P3-M1 (§II B pp. 3–5; §III G p. 15; Table I p. 8): Gaia DR3 preprocessing for the 50K run is “lineage-inferred rather than directly recovered,” and XV-stability is 41% (FAIL).
- Problem: The exact preprocessing is unrecovered; the selection is training-sample-conditioned; yet Gaia is included in the “recommended tier.”
- Required fix: Either (a) rerun Gaia with a committed, released script and report the re-run catalog (and remove the unrecovered run), or (b) remove Gaia from any “recommended” count and present it solely as an exploratory appendix tier. In either case, make the status explicit in the abstract and conclusions.

P3-M2 (§II D Step 1 p. 6; §VI D(ii) p. 25): Validation gates (val-loss ≤ 0.30 ≤ 100 epochs, injection–recovery ≥ 50% at 5σ, Jaccard thresholds) are heuristic and not pre-registered; only one gate (SDSS 64% vs 50% at 5σ) is close to its cut.
- Required fix: Provide a brief sensitivity analysis showing that your pass/fail designations are insensitive to reasonable changes in these gate thresholds (e.g., 40–60% for injection–recovery, Jaccard cut ±0.05), or pre-register a principled rationale (e.g., power study, prior practice) for each threshold.

P3-M3 (§IV B p. 17): Cramér’s V expression is written with a square root but the following numeric expression omits it: “Cramér’s V = sqrt(χ2/(N·(k−1))) = 376,713/(378,280 × 24,048) ≈ 0.0064.”
- Problem: The printed equality is dimensionally inconsistent; the 0.0064 corresponds to the square root of the ratio, not the ratio itself.
- Required fix: Replace the second equality with V = sqrt(376,713/(378,280 × 24,048)) ≈ 0.0064, or write both steps explicitly.

P3-M4 (§III F pp. 14–15): Planck top-200 are ranked in-sample. The text gives a supportive held-out enrichment (48 observed vs 30 expected; p ≈ 5.5 × 10−4) but no full held-out rescoring.
- Required fix: Add a full held-out scoring of the 2 × 10^5 native bank (train on a disjoint set; score the held-out set) to demonstrate that most of the released top-200 are recoverable out-of-sample. If resource-limited, at minimum perform k-fold rotation experiments with disjoint scoring folds and report top-200 overlap distributions.

P3-M5 (§III H p. 15; Fig. 5 p. 15 caption; Table I p. 8): Mixed radii in SIMBAD unmatched fractions — per-survey at 5″, pooled aggregate at 3″ — appear in the same figure/caption.
- Required fix: Standardize radii across all reported SIMBAD unmatched fractions or annotate visually on the plot the different radii used and restate the caveat in the caption so readers do not directly compare the dashed line against the per-survey bars.

P3-M6 (§IV C p. 19): Headline “largest” catalog-size multipliers (e.g., ~141× vs. [11]) are process-scale, full-stream, not like-for-like. While you caveat this elsewhere, the prominence of these multipliers risks misinterpretation.
- Required fix: Move the process-scale multipliers out of the abstract, or explicitly append “process-scale, not like-for-like” in the abstract where the multipliers first appear, and add the like-for-like science-target comparison there.

MINOR

P3-m1 (§V pp. 19–21; Appendix C pp. 26–27): Keep “σ” channels clearly separated and notationally distinct. You do so in-text, but add a one-line preface at first juxtaposition reminding readers that σ(fNL) forecast widths and σ-level parameter shifts (e.g., γ = 4.61σ from mean) arise from different statistical objects and are not comparable.
- Required fix: Add a short “not comparable” sentence the first time the two σ notions appear in proximity (e.g., end of the abstract’s cosmology paragraph).

P3-m2 (§III A p. 10): The 95% binomial upper limit on 0/200 top-200 manual flags is quoted as ≤ 1.5%. Exact Clopper–Pearson upper bound is ≈1.49%, which is fine; cite the interval type (Clopper–Pearson) explicitly for completeness.

P3-m3 (§III H p. 15): NEOWISE polar-cap excess significance reported as “binomial z ≈ 4.0, p ≈ 6 × 10−5.” A simple normal approximation yields z ≈ 4.1, one-sided p ≈ 2 × 10−5; your quoted p is conservative. Add which-sidedness and the exact test used.

P3-m4 (§IV A, pp. 15–16): False-match rate estimate for DESI×SDSS 3″ control is done by RA-only shifts; you note this limitation. Please add one HEALPix-rotation control (random great-circle rotations) or state that you defer a geometry-preserving null and that current figures are heuristics only.

P3-m5 (Appendix E pp. 28–30): Define ρi in Eq. (E1) explicitly (e.g., κi or ρi stands for the per-bin cross-power amplitude used by the free-spectrum KDE product) and cite the exact NANOGrav convention. The current equation is standard but the observable is not defined in words.

P3-m6 (General): The paper is very long relative to the concrete methodological contribution. Consider moving some of the catalog-engineering and process-accounting prose (e.g., long timing/throughput paragraphs and extended survey-by-survey bookkeeping) to a data-release note or appendix and target ≤ 26 pages.

NIT

P3-N1 (§III B p. 11; Fig. 1 caption p. 3): “AE” used in the gallery as a proxy for rZ is explained in text; consider adding a parenthetical in the figure caption to avoid confusion (AE = Z-arm residual).

P3-N2 (§IV B p. 17): Minor typography: change “χ 2 ν” to “χ2ν” consistently.

P3-N3 (References): Ensure final bibliographic details (year/volume/page) are updated for [1], [12] if they are preprints at time of acceptance.

Arithmetic and internal-consistency checks I verified

- DESI anomaly fraction: 195,829 / 22,504,897 ≈ 0.00870 = 0.87% (ok).
- DESI science-bit recount: 2,468 / 20,299,155 ≈ 0.01216% (ok).
- DESI science-bit decomposition sums 2,371 + 95 + 2 = 2,468 (ok).
- Cross-survey dedup: 388,493 − 10,213 = 378,280 (ok); multicluster split 637 + 9,576 = 10,213 (ok).
- 6-way recommended: 275,151 − 5,834 = 269,317 (ok).
- Planck rate bookkeeping: 200 / 200,000 = 0.10% (ok).
- NEOWISE mask: 17/436 = 3.90% vs cap-area 1 − sin 80° = 1.52%; z ≈ 4.1 (ok).
- Novelty: 178/1,000 = 17.8%; binomial 68% SE ≈ 1.21% (ok).
- fNL Fisher “positivity-respecting” mapping with F0 = 1/8.98^2, c = 0.0747, α = 0.19 gives σ = 8.14; envelope [3.92, 8.98] (ok).
- Gold+Silver α = 1.83 ± 2.03 gives central σ ≈ 1.95 (ok).
- Cramér’s V numeric 0.0064 equals sqrt(χ2/(N(k−1))) (but formula presentation needs correction; see P3-M3).
- SDSS top-1%: 0.01 × 1,925,279 = 19,252.79 → 19,253 (ok).
- LAMOST top-1%: 0.01 × 11,334,161 = 113,341.61 → 113,342 (ok).
- Multipliers: 378,080/2,685 ≈ 140.8 (~141×); 269,117/2,685 ≈ 100.2 (~100×); 195,829/2,685 ≈ 72.9 (~73×) (ok).

Abstract-last drift check

- Abstract now clearly distinguishes validated subset and exploratory additions, and states that the 9.4% shift in σ(fNL) is within the 1σ envelope and not significant — consistent with the body. However, the abstract still presents an inexact “≥ 268,519” validated count (P3-E1) and includes NEOWISE under “validated,” despite only a geometry QA (P3-E5). Also, the process-scale multiplier language remains prominent; please move the like-for-like science-target comparison into the abstract (P3-M6).

Provenance and reproducibility surfaces

- Several key artifacts are promised but not yet public (P3-E4). The Gaia preprocessing is unrecovered (P3-M1). The eROSITA axis is irreproducible (P3-E2). The Planck top-200 are in-sample (P3-M4). These must be resolved before acceptance.

Standalone-reader test

- With the present text, a reader cannot exactly reconstruct the Gaia or eROSITA sections from the paper alone; the manuscript is generally self-contained for DESI/SDSS/LAMOST/Planck/NEOWISE, but the above reproducibility gaps must be closed (P3-E2, P3-M1).

Effect-size statements

- You generally provide effect sizes (e.g., Cramér’s V, bias amplitudes, novelty fractions). Please correct the Cramér’s V presentation (P3-M3) and keep “σ” channels distinct (P3-m1).

Summary recommendation

MAJOR REVISIONS

Justification: The manuscript is careful and thorough in many respects and addresses several issues flagged in earlier rounds (clear caveats on fNL forecast, injection–recovery gates for some surveys, and cross-survey dedup sensitivity). However, there remain critical methodology and reproducibility issues that must be resolved for PRD: (i) the headline validated unique-object count must be exact and reproducible (currently only a lower bound), (ii) the eROSITA score axis is irreproducible yet a hard numeric threshold is still printed, (iii) the main anchor survey (DESI) lacks a detector-sensitivity injection–recovery validation, (iv) NEOWISE is counted as “validated” despite being only geometry-QA, (v) the headline total depends on an ad hoc SDSS continuity slice, and (vi) key data-release artifacts and the DOI are not yet public. Addressing the ESSENTIAL items (E1–E6) and the main MAJOR items (M1–M4) will bring the work to PRD methodological standards. The remaining MINOR/NIT items can be handled in revision.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh pass)

ESSENTIAL

P3-E7 (Table I p. 8; §III C pp. 11–13): SDSS rate denominator mismatch
- Issue: The 77,905 anomalies are drawn from the native re-score pool of 1,925,279 spectra (a fixed-size continuity slice equal to the cross-transfer count), but Table I lists Ntotal = 2,304,830 and prints a 3.38% rate (= 77,905/2,304,830). The text simultaneously states the same 77,905 is “4.05% of the 1,925,279 native-rescored spectra.”
- Why it matters: The “Rate” column mixes denominators and mischaracterizes the selection basis for SDSS.
- Required fix: Report the SDSS “Rate” against the actual re-scored pool (4.05%), change the Ntotal column to 1,925,279 for the native slice, or mark the rate “N/A (continuity slice)” and explain in the cell/footnote that the count is a fixed-size native slice not a data-driven threshold. Do not divide by the 2.304M DR18 total when the anomalies come from the 1.925M re-score pool.

MAJOR

P3-M7 (Table I p. 8; caption footnotes ¶, †; §III H p. 15): NEOWISE anomaly count inconsistency (436 vs 419)
- Issue: The Table I NEOWISE row shows Nanom = 436† (top 1%), while the caption footnote “¶” and the body text state that the canonical Path-C native count uses the post-mask value 419. The caption even says the per‑survey Nanom “shows the canonical Path‑C native‑retrained counts directly: … NEOWISE 419,” which contradicts the 436 printed in the table.
- Required fix: Make the table’s NEOWISE Nanom the canonical post‑mask count (419). Move the pre‑mask 436 to a footnote. Verify that any totals/summations that depend on NEOWISE use 419 (the paper’s 388,493 survey-sum already assumes 419).

P3-M8 (Table I p. 8; §III D p. 12, §VI A p. 24): LAMOST SIMBAD-unmatched fraction (∼50%) is computed on the cross-transfer diagnostic set, not the released native top-1% tier
- Issue: The table presents “∼50%” SIMBAD-unmatched for LAMOST without prominently stating in the row that this statistic was measured on the cross-transfer diagnostic set (not on the native top-1% exploratory tier). The footnote clarifies this, but in the summary table it reads like a property of the released LAMOST native tier.
- Required fix: Either recompute the SIMBAD unmatched fraction for the native top-1% exploratory tier and report that value (with an “exploratory” qualifier), or remove the LAMOST SIMBAD number from the table and confine the cross-transfer diagnostic fraction to the text/appendix.

P3-M9 (Table I p. 8; §III D p. 12): Mixed denominators in “Rate” column (SDSS and LAMOST) obscure what is being measured
- Issue: For SDSS, the rate is computed against the full DR18 (2.304M) while the anomalies are from the 1.925M re-scored pool (see P3-E7). For LAMOST, the printed 0.99% rate uses the 11,418,594 DR10 total, but the top‑1% native slice is defined on the 11,334,161 re‑scored pool (84,433 unretrieved). The rate therefore mixes a full-DR denominator with a selection drawn from a smaller pool.
- Required fix: Standardize denominators in the “Rate” column to the actual scored pools per survey (or mark “N/A; fixed top‑1% on re‑scored pool of size …”). Where rates are not genuine detection frequencies (fixed-count tiers, continuity slices), label them explicitly in‑cell/footnote to prevent misinterpretation.

P3-M10 (§VI D(ii) p. 25; Fig. 10 p. 25; §III E p. 13; §III G p. 15): Cross-survey injection–recovery comparability
- Issue: Recovery curves use different plant morphologies across surveys (spectra: continuum-dip vs emission-line; Gaia: variability-axis injection; eROSITA: latent-subspace injection), yet the paper aggregates PASS/FAIL tallies in a single panel and narrative. While the NEOWISE geometry-QA is clearly separated, the non-NEOWISE injection tests still differ materially in what is being “recovered.”
- Required fix: Add an explicit comparability disclaimer in the main injection–recovery summary stating that recovery percentages are morphology‑dependent and not directly comparable across surveys. Summarize per‑survey plant definition next to each curve or in the caption/table to prevent cross‑reading the PASS/FAIL fractions as like-for-like detector sensitivities.

MINOR

P3-m7 (§III F p. 15): Planck held-out enrichment p-value method
- Issue: Observing 48 validation-set patches among the top‑200 where 30 are expected under p0 = 0.15 yields one‑sided binomial p ≈ 1.9 × 10−4 (z ≈ 3.56) by exact binomial calculation; the text prints p = 5.5 × 10−4.
- Required fix: Specify the test used (exact binomial vs normal approximation, any continuity correction) and either report the exact p-value or make the approximation explicit.

P3-m8 (Abstract p. 1; §III A p. 9–11): Ratio rounding
- Issue: “≈ 0.9×” for 2,468/2,685 is ≈ 0.92×.
- Required fix: Use ≈ 0.92× (or the exact ratio) for accuracy.

P3-m9 (§IV A pp. 15–16, footnote 1 p. 16): Random-coincidence accounting across survey pairs
- Issue: The ≤ 10 expected 5″ random coincidences are argued by scaling from DESI×SDSS and asserting the rest “sum to < 1.” For completeness, give area-scaled estimates (or upper bounds) for the other contributing pairs, or add an explicit sentence that they are negligible due to catalog sizes and disjoint footprints.

NIT

P3-N4 (Table I p. 8 caption language): The caption asserts the per‑survey Nanom column shows “canonical Path‑C native‑retrained counts,” but the printed NEOWISE value is the pre‑mask 436, not the canonical post‑mask 419.
- Fix: Align caption wording with the corrected table entry per P3‑M7 so the caption is not self‑contradictory.

NO OTHER NEW ISSUES FOUND
- I rechecked unit consistency for displayed equations, the figure/caption vs body descriptions, and all arithmetic I could recompute from the printed numbers. Apart from the items above, the remaining values (rates, ratios, counts, confidence intervals, Bayes factors, novelty fractions, dedup arithmetic) are internally consistent with the stated inputs within rounding.