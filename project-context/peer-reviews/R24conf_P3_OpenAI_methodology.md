# P3 R24conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper3_anomaly_catalog_v3.1.81.pdf` md5=aa791276 pages=24
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6871 chars)
**Wall time**: 291.1s

---

Referee report on “Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies …” (24 pp)

Scope of review
I evaluated the full manuscript (24 pages) with focus on methodology rigor: statistical definitions, estimator declarations, internal arithmetic, error propagation, dimensional consistency, and traceability of all load-bearing scalars from the abstract/conclusions to the body. I audited figures, tables, and key ratios.

Findings

ESSENTIAL

P3-E1 (Sec. V, p. 14; also Table IV caveat (i), p. 17) — Incorrect definition of F0 in Fisher mapping; dimensional inconsistency; lucky numerical cancellation
Quote: “1/σ^2(fNL) = F0 + c α^2 with F0 = 1/8.982 and c = 0.0747 … inserting αjk = 0.19 gives σ(fNL) = 8.14”
Problem: If F0 is taken literally as 1/8.982 ≈ 0.111, then 1/σ^2 ≈ 0.114 implies σ ≈ 2.96, not 8.14. The only way to reproduce 8.14 is F0 = 1/(8.982)^2 ≈ 0.0124. As written, the definition is wrong by a factor of σstd and dimensionally inconsistent with 1/σ^2.
Required fix: Correct the definition everywhere to F0 = 1/σ^2(fNL)std = 1/(8.982)^2 = 0.01237. Recompute and verify all dependent numbers and any text that repeats the incorrect “1/8.982” expression.

P3-E2 (Sec. V, p. 14) — Arithmetic error in “de-biased amplitude” computation
Quote: “max(0, αˆ^2 − σ^2_α) = max(0, 0.192 − 0.652) = 0”
Problem: α = 0.19 ⇒ α^2 = 0.0361 (not 0.192). σ_α = 0.65 ⇒ σ_α^2 = 0.4225 (not 0.652). The qualitative conclusion (clipped to zero) remains, but the printed numbers are wrong by factors of 5–7.
Required fix: Replace with max(0, 0.036 − 0.423) = 0. Update any nearby text that references 0.192 or 0.652.

P3-E3 (Abstract p. 1; Table I p. 8; Sec. IV.C p. 11; Conclusions p. 17) — Catalog-grade subset unique counts appear to reuse the 7-way dedup compression; 6-way dedup not provided; numerical inconsistency likely
Quote (Abstract): “recommended catalog-grade subset is ∼265,000 unique entries (264,938: DESI + SDSS + eROSITA + Planck native + Gaia + NEOWISE, including the 200 Planck map patches … dropping the map patches, leaving the 264,738 catalog-grade point-source subset)”
Problem: Sum of the six non-LAMOST per-survey counts = 195,829 + 77,905 + 298 + 200 + 500 + 419 = 275,151. The paper subtracts the full 7-way compression of 10,213 to reach 264,938, which implies that every collapsed duplicate involves only the six catalog-grade surveys and none involve LAMOST. This is unlikely given the 637 multi-survey clusters and 9,576 intra-survey duplicates reported for the 7-way run. Planck contributes zero overlaps, so reusing 10,213 is almost certainly incorrect for the 6-way subset. A 6-way union-find run is not shown.
Required fix: Run and report the actual 6-way 5″ deduplication (DESI, SDSS(native), eROSITA, Gaia, NEOWISE, Planck) and replace 264,938/264,738 with the measured unique counts. Provide the corresponding 6-way multi-survey cluster count and compression percentage. Update every place that currently subtracts “10,213” from non-LAMOST sums.

P3-E4 (Sec. II.B p. 3; Sec. III.F p. 7; Table I p. 8) — Canonical score axis inconsistency for Planck; contradicts “S refers without exception”
Quote (p. 3): “Throughout this paper, ‘S’ refers without exception to the per-survey standardized … residual”
Quote (p. 7): “Top-200 native anomaly patches (per-patch reconstruction-MSE anomaly score, Eq. 1; range [0.558, 0.621])”
Problem: Planck selection is described using raw MSE, not S. This contradicts the earlier “without exception” declaration and complicates cross-survey comparability and thresholds.
Required fix: Either (a) standardize the Planck scores to S and report S consistently (preferred), or (b) explicitly carve out Planck as an MSE-selected exception and update all text, captions, and Table I notes accordingly. Remove “without exception.”

P3-E5 (Table V footnote, p. 19; Sec. IV.C p. 11; Table I footnotes p. 8) — Version-history and internal review/audit tags present in the body
Examples:
- “an earlier draft listed 10.6 s … has been withdrawn” (Table V footnote)
- “audit artifact r23conf dedup audits.json” (p. 11; also repeated elsewhere)
- “The earlier ‘strict subset’ framing is replaced with …” (Table I footnote §)
Problem: PRD requires a clean scientific record. Versioning metadata, earlier-draft commentary, and internal audit-file names must not appear in the published text.
Required fix: Remove all version-history language, review-round markers, “r23conf”/“artifact” references, and editorial change logs from the manuscript. Confine provenance to a public data/code repository; cite it formally.

P3-E6 (Data availability, p. 18; Abstract p. 1) — Data/code “will be made public with the arXiv posting”; not presently accessible
Problem: PRD requires reproducibility at acceptance. Promises of future release do not meet the bar.
Required fix: Make the dataset and code public now (with permanent DOIs), or deposit as PRD supplemental material. Replace “will be made public” with working links/DOIs verified at submission. Ensure every number needed to reproduce the catalog, dedup, and Fisher forecasts is accessible.

P3-E7 (Sec. V, p. 14–15; Fig. 9) — Ambiguous construction of the “1σ envelope [3.92, 8.98]”; mixing of point-estimate mapping and uncertainty without a declared rule
Problem: The mapping from α uncertainty (α̂ ± σα) to σ(fNL) is convex and asymmetric. The text states “1σ envelope [3.92, 8.98]” but does not declare the propagation rule (e.g., σ− from α̂+σα and σ+ from α̂−σα, clipped at α=0). This is not a standard statistical interval and risks misinterpretation as a symmetric 68% CI.
Required fix: State the precise propagation rule used to produce [3.92, 8.98], e.g., “evaluate σ(fNL) at α = max(0, α̂ − σα) and α = α̂ + σα under 1/σ^2 = F0 + c α^2,” and emphasize it is a propagated envelope, not a likelihood-derived CI. Add an explicit “not directly comparable to the ±σα error on α (different null and metric)” disclaimer at the juxtaposition, per PRD standards.

MAJOR

P3-M1 (Abstract p. 1; Sec. I p. 1; Sec. VII p. 17) — Overly strong “largest” claims without a comprehensive survey of contemporaneous literature
Quote: “largest-scale application … largest prior single-survey anomaly catalog [11] … 141× larger …”
Problem: The “largest” framing hinges on [11]. To sustain a PRD-level claim, the manuscript should document that no larger anomaly catalogs (including photometric-only or cross-wavelength) exist as of submission. As written, it assumes [11] is the ceiling without a systematic search.
Required fix: Either (i) soften to “to our knowledge, larger than [11] by 141×”, or (ii) add a brief literature audit (even in a footnote) covering recent large-scale anomaly catalogs across major surveys.

P3-M2 (Sec. III.E p. 8–9; Table I footnotes) — eROSITA threshold description is ambiguous
Quote: “298 at S > 0.259 (top 0.03%; data-driven score-knee threshold).”
Problem: S > 0.259 corresponding to ~0.03% of 930,203 implies an extreme non-Gaussian tail. Given that IsolationForest is used for cross-validation on the BigAE latent, the dependence between detectors should be emphasized and the exact empirical quantile provided.
Required fix: Report the exact empirical percentile of the S > 0.259 cut (e.g., 0.032%) and explicitly restate detector non-independence in the main text where novelty is discussed.

P3-M3 (Sec. III.F p. 7; Appendix F p. 20) — Planck selection metric change vs cross-transfer ACT; juxtaposition may mislead
Problem: Planck native uses a convolutional AE + MSE range; ACT is quarantined but still used in a cross-correlation “null” demonstration. The caveats are present, but the figureless assertion of “null” could be misconstrued.
Required fix: Add a sentence in §IV.D explicitly noting the result is not a statistical test of common sky structures because the tested sets are (i) not independent and (ii) largely non-overlapping by construction; no significance should be ascribed.

P3-M4 (Fig. 8, p. 13) — Display “Score” annotations are not the catalog selection scores; risk of reader confusion
Problem: The caption explains the issue, but the numeric labels remain prominent and are close to the S > 5 threshold used elsewhere.
Required fix: Change on-plot labels to “Display score (non-catalog)” or remove the labels. Keep the warning in the caption.

P3-M5 (Bibliography, p. 23) — Inconsistent year for [12]
Quote: “[12] … arXiv:2506.17376 (2026)”
Problem: arXiv:2506.* corresponds to 2025-06, not 2026. This can mislead readers.
Required fix: Correct the year or provide the proper bibliographic reference (journal or correct arXiv year).

MINOR

P3-n1 (Sec. III.H p. 9–10) — NEOWISE polar-cap excess calculation
Check: Observed 17/436 = 3.90%. Two 10° caps have area fraction 2 × (1 − cos 10°)/2 = 1 − cos 10° ≈ 1.52%. Ratio ≈ 2.57×. The text rounds to 2.6×; fine. Note in text that the expected fraction assumes uniform sky density; state that source-selection non-uniformities could modulate the baseline.
Required fix: Add one sentence acknowledging that the “uniform-sphere” baseline neglects source-selection inhomogeneities.

P3-n2 (Sec. IV.A p. 10–11; Fig. 6 p. 11) — SIMBAD unmatched “aggregate 58.8%”
Check: 235/400 = 58.75%. The plotted “58.8%” is fine. Consider rounding to 58.8% explicitly in text.

P3-n3 (Table V footnotes, p. 19) — Missing Planck native training wall-clock
Problem: The dash is acceptable, but PRD readers benefit from a ballpark. If irretrievable, note “not recorded; typical run O(hours) on A100 at the reported 150-epoch schedule.”

P3-n4 (Sec. II.B p. 3–4) — “z-scored” vs spectroscopic redshift z warning
The paper already includes a warning; good. Consider replicating this warning in the first place where S is plotted against “z” to reduce the chance of misreading axes.

NITS

P3-N1 (Throughout) — Hyphenation and en-dashes
Replace sequences like “5σ gate (LAMOST 5.8%, Gaia 5.2%, eROSITA 1.2%) at 5σ” with “at 5σ (…” to avoid duplication.

P3-N2 (Sec. IV.C p. 11) — “friends-of-friends chain audit” subheading capitalization inconsistent with other subheadings.

P3-N3 (Fig. 7 caption, p. 12) — χ2 caveat sentence is long; consider splitting for readability.

Length and focus
At 24 pages, the paper is long for a methods + catalog paper with several digressions (e.g., PTA Appendix E, shot-noise Appendix C) only tangentially tied to the anomaly-detection methodology. I recommend tightening to ≤ 20 pages by moving derivation detail (PTA γ fit, shot-noise normalization discussion) to supplementary material and focusing the main text on (i) model definition, (ii) validation gates, (iii) catalog arithmetic, (iv) cross-match method, and (v) fNL Fisher mapping (with the now-corrected F0).

Abstract and conclusions audit
- “378,280 unique anomalies (378,080 point-source + 200 Planck)”: Traceable (Table I + 7-way dedup section). OK.
- “17.8% genuine novelty” for DESI top-1000: Traceable (Sec. IV.A). Wilson 68% ±1.2% is correct.
- “DESI Jaccard 0.862”: Traceable (Sec. II.B). OK.
- “3 PASS, 3 FAIL-with-diagnostic” for injection-recovery: Traceable (Sec. II.D Step 5; Fig. 10). OK.
- “σ(fNL) = 8.14 with 1σ envelope [3.92, 8.98]”: Numerically reproducible only if F0 = 1/(8.982)^2 (not “1/8.982” as written). Needs correction (P3-E1).
- “NANOGrav γ = 2.567 ± 0.382; +1.13σ and +4.61σ”: Numbers are correct. Bayes factor BMB/SMBHB ≈ 7.1×10^3 is plausible given priors but derivation details rely on external code; acceptable as an illustration if clearly labeled (they are).

Sigma consistency
The manuscript uses: (i) validation-set σ for S-definition; (ii) injection amplitude “nσ” (noise σ); (iii) σ(fNL) forecast width; (iv) Gaussian σ-units for parameter shifts in PTA. Most places are context-isolated. Where two appear in the same paragraph (Sec. V), add explicit “not directly comparable” language (P3-E7).

## Summary recommendation
MAJOR REVISIONS

Justification
The paper presents an ambitious, cross-survey anomaly catalog with extensive validation. However, there are critical methodological/arithmetical issues that must be corrected before PRD publication: the Fisher mapping constant F0 is defined incorrectly (breaking dimensional consistency), the “de-biased amplitude” numbers are arithmetically wrong, and the catalog-grade unique counts likely reuse a 7-way compression on a 6-way subset without actually running the 6-way deduplication. Additionally, the Planck score-axis exception contradicts the stated “without exception” S-definition, version-history/audit language appears in the body, and the data/code are not presently accessible. Addressing these ESSENTIAL items (and the MAJOR clarifications) will bring the manuscript within PRD methodological standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (second-pass audit)

ESSENTIAL

P3-E8 (Sec. IV.A p. 10–11; Fig. 6 caption) — Inconsistent SIMBAD matching radius used within the same section
Quote: “We cross-match … using a 5-arcsecond cone search.” Two sentences later: “the pooled unmatched fraction … 235/400 unmatched at a 3″ radius in that pooled run.”
Problem: The aggregate 58.8% figure is computed at 3″, while the text declares 5″. Per-survey unmatched fractions elsewhere use 5″. Mixing radii invalidates direct comparison and biases the pooled rate high relative to the 5″ procedure.
Required fix: Recompute the aggregate at the declared 5″ radius (or uniformly switch to 3″ everywhere) and clearly state the radius used for each fraction (per-survey and pooled). If the pooled run must remain at 3″ for logistical reasons, present both 3″ and 5″ values or add a correction factor/uncertainty showing the sensitivity to radius.

P3-E9 (Table I p. 8; Sec. III.F p. 7; Table V footnote p. 19) — Planck Ntotal and “Rate” inconsistent with the Path-C native run
Evidence:
- Table I reports Ntotal = 20,000 and Rate = 1.00% for Planck.
- The Path-C native Planck pipeline actually scores 2×10^5 masked SMICA patches (25.3 s re-score; Table V footnote), and selects the top 200 patches.
Problem: If the published Planck tier is drawn from the 200,000-patch native bank, then the effective selection fraction is 200/200,000 = 0.10%, not 1.00%. Keeping Ntotal = 20,000 in Table I contradicts the stated native re-score and misrepresents the denominator used for the published set.
Required fix: Make Table I reflect the actual Path-C processing: either (i) set Ntotal = 200,000 and Rate = 0.10% (with a footnote that the “200” count is a fixed-size top-ranked selection), or (ii) clearly segregate cross-transfer vs native Planck rows so that the denominators and rates are not conflated. As written, the main table says “total sources/patches processed” yet lists the cross-transfer 20,000 while the published tier comes from 200,000.

P3-E10 (Sec. II.D Step 1 p. 4; Sec. II.B p. 3; Sec. III.C–D p. 6–7) — Gate criterion “≤ 100 epochs” invoked but not documented for PASS cases
Quote (Step 1): “Retained if (a) validation loss ≤ 0.30 after ≤ 100 epochs, or (b) injection-recovery ≥ 50% at 5σ. SDSS gates PASS … LAMOST … PASS.”
Problem: The training description states typical convergence at 100–150 epochs. For SDSS and LAMOST you report val loss values but do not state the epoch at which those values were reached, leaving it unclear whether the “≤ 100 epochs” condition was actually met (only Planck explicitly uses criterion (b)).
Required fix: Report the best-epoch numbers for the SDSS and LAMOST native retrains and explicitly confirm they satisfied the ≤100-epoch branch, or revise the criterion (drop the ≤100 clause or reclassify the PASS basis).

MAJOR

P3-M6 (Sec. II.A p. 2; Fig. 1 caption p. 2; Sec. V p. 14) — Ambiguous reuse of the “gold-tier” label for two unrelated sets
Issue: “83 gold-tier anomalies” (Fig. 1) is a display subset from a companion pipeline, while “116-object GOLD QSO-candidate confidence tier” (Sec. V) is used in the forecast. Same label, different objects and purposes.
Required fix: Rename one of the tiers (e.g., “display-gold” vs “GOLD-confidence”) everywhere, including figure captions, to prevent readers from conflating them.

P3-M7 (Table I footnote § p. 8; Sec. III.E p. 8–9; Table III p. 9) — Symbol S used ambiguously for two different axes in eROSITA discussion
Examples:
- Main text uses S for the canonical BigAE z-scored residual (e.g., “298 at S > 0.259”).
- A footnote then says “equivalent to S > 0.259 on the eROSITA-native IsolationForest raw-score axis,” while Table III correctly distinguishes SBigAE and SIF,raw.
Problem: Overloading S to denote an IsolationForest raw score contradicts the paper’s definition of S and invites confusion.
Required fix: Replace the footnote phrasing with “IF raw isolation-score threshold = 0.259” (or whatever the raw-score cut is), and keep S reserved for the canonical BigAE score. Ensure all locations consistently distinguish SBigAE vs SIF,raw.

P3-M8 (Sec. II.C p. 4 vs. Table V footnote p. 19) — Inference-time inconsistency for Planck
Quote: “the CMB (Planck) … each ≲10 s of GPU time” (inference subtotal section).
But the native Planck re-score is reported as 25.3 s for 200,000 patches (Table V footnote).
Problem: Readers cannot tell whether the ≲10 s figure refers to the 20,000-patch cross-transfer pass, while the published Path-C set reflects the 200,000-patch native pass. As presented, the timing looks contradictory.
Required fix: Clarify that the ≲10 s statement refers to the 20,000-patch cross-transfer scan (not the published native run), and present both timings side-by-side with their respective Ntotal to avoid misinterpretation.

MINOR

P3-m5 (Sec. III.A p. 5, para “Cross-matching the top 10,000…”) — Rank-slice clarity for SIMBAD/NED matches
Quote: “0.2% in SIMBAD and 12.7% in NED; none of the top 100 appear in SIMBAD or NED…”
Comment: The two statements describe different rank slices (top-10,000 vs top-100). This is plausible but easy to misread as a contradiction.
Suggested fix: Add “(top-10,000)” and “(top-100)” inline to disambiguate the slices.

P3-m6 (Fig. 6 caption p. 11) — State the aggregation denominator explicitly in the figure
You explain in the text that DESI and LAMOST are excluded from the pooled 400, but the caption would benefit from a parenthetical “pooled over four surveys; 100 objects each.”

P3-m7 (Sec. III.F p. 7; Table I p. 8) — Planck “Rate” column labeling
Even if you keep the fixed “200 patches” selection, labeling the Rate as “1.00%” without the paired denominator invites misreading. Consider replacing Rate with “fixed-count (200)” for Planck (and similar fixed top-1% selections) or add a footnote that the reported “1.00%” corresponds to the 20,000 cross-transfer budget, not the 200,000 native bank used for the published set.

NITS

P3-N4 (Sec. IV.A p. 10–11) — When introducing the aggregate unmatched fraction, explicitly repeat the matching-radius setting used for that computation to prevent confusion with the 5″ default stated one sentence earlier.

P3-N5 (Fig. 1 caption p. 2) — Add parenthetical clarifier after “gold-tier anomalies (cyan stars)” such as “(display-only, distinct from GOLD confidence tier in Sec. V)” to prevent label confusion at first encounter.

Rationale for additional pass
The second-pass audit focused on radius consistency, denominators and rates tied to the Planck native vs cross-transfer pipelines, gate-criterion completeness, symbol usage, and potentially confusing tier nomenclature. These items were not covered in the initial review and, in several cases (Planck Ntotal/rate; mixed matching radii), affect the interpretability or reproducibility of reported percentages and selections.