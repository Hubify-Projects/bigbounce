# P3_v3151_R13 R-round — REAL cross-vendor — Grok-4.3 brutal-honesty reviewer

**Model**: `x-ai/grok-4.3` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1430pt
**Wall time**: 50.1s
**Persona focus**: Cut through narrative inflation. Flag overclaim, false confidence, headline numbers that aren't load-bearing, anything written to dodge a reviewer rather than to be true. Is the central claim actually new? Are 'first', 'novel', 'unprecedented' framings honest given the actual literature?

---

**Tokens**: prompt=58744, completion=3321, reasoning=2341, total=62065

---

**## PAPER-GRO-B1: BLOCKER — Headline unique count arithmetic failure**

**Section:** Title, abstract (lines ~50-70), §4.3 cross-survey matches, §6.4 caveats (a)

**Issue:** 388,493 survey-level detections minus the reported 637 multi-survey coincidences yields 387,856 unique objects, yet the paper freezes the title/abstract headline at 378,280 with an explicit 9,576 shortfall and defers the union-find recompute on the cluster manifest. This is a load-bearing math error carried across rounds.

**Fix:** Execute the union-find on pathc_multi_survey_matches.parquet, replace every instance of 378,280/378,080 with the corrected figure, and update the stratification note.

**## PAPER-GRO-B2: BLOCKER — Cosmological forecast not load-bearing**

**Section:** Abstract (bolded α and σ_fNL paragraphs), §5 (full Fisher text)

**Issue:** Empirical α_jk = 0.19 ± 0.65 is consistent with zero at 0.29σ; the resulting σ_fNL = 8.27 ± 2.37 is consistent with no improvement at <1σ (and the +1σ tail exceeds the single-tracer floor). The paper still headlines the 7.9% central improvement and the 74% GS improvement while burying the null-consistency result.

**Fix:** Move the σ_fNL = 8.27 figure to a secondary “illustrative central-value forecast” sentence; lead with the <1σ consistency statement and drop the percentage-improvement framing.

**## PAPER-GRO-B3: MAJOR — Novelty fraction over-claim in title and framing**

**Section:** Title (“Native-Trained Novelty Fractions”), abstract (17.8% paragraph), §4.1

**Issue:** 17.8% is a single top-1,000 DESI point estimate against 20 catalogs; the full-catalog rate is explicitly untested and the paper acknowledges the converse hypothesis is equally plausible. The title and “genuine novelty fraction” language imply a catalog-wide property that is not demonstrated.

**Fix:** Change title to “...and Top-1,000 Novelty Fraction” and restrict all novelty claims to the measured 17.8% at the top-1,000 stratum with the explicit qualifier already present in §4.1.

**## PAPER-GRO-B4: MAJOR — LAMOST exploratory tier still inflates headline**

**Section:** Abstract (LAMOST ~113k paragraph), Table 1 footnote, §3.3, §6.4

**Issue:** LAMOST native is labeled a transparent FAIL (5.8% continuum recovery, 98% prior blue-excess artifact) and restricted to “exploratory/methodological lesson” use, yet its ~113k objects are retained in the 378,280 aggregate and the catalog-grade tier is only ~265k. This mixes a failed detector into the primary number.

**Fix:** Report the catalog-grade tier (DESI+SDSS native+eROSITA+Gaia+NEOWISE+Planck) as the headline 264,938 (or corrected equivalent) and move LAMOST to a separate exploratory supplement; update all summary statistics accordingly.

**## PAPER-GRO-B5: minor — OOD reconciliation narrative length and residual ambiguity**

**Section:** §2.2 (OOD validation paragraph, ~lines 300-340)

**Issue:** The long reconciliation that the 0.87% rate reflects curation rather than the absolute S>5 cut is internally consistent with the quoted B10_ood_results_100k.json medians, but the text still requires readers to perform the mental subtraction (>50% of random SPARCL would be anomalies) instead of stating the operational threshold policy in one sentence.

**Fix:** Replace the paragraph with: “The absolute S>5 cut (MSE≈0.143) applied to the curated 22.5M catalog yields 0.87%; the same cut on the independent 100k OOD sample would flag >50% of sources. Downstream users must adopt a 99.13th-percentile cut on their own sample distribution.”

**## PAPER-GRO-B6: nit — Revision-history bloat in source**

**Section:** Preamble LaTeX comments (entire v3.1.40–v3.1.51 closure log)

**Issue:** The source contains multi-page reviewer-round closure logs that have no place in a submitted paper and make the document read as a changelog rather than a self-contained scientific work.

**Fix:** Delete the entire revision-history block before submission; retain only the minimal on-record deferral list in §6.4 if any items remain open.
