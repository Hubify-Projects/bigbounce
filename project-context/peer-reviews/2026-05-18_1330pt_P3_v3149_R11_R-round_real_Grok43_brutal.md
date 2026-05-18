# P3_v3149_R11 R-round — REAL cross-vendor — Grok-4.3 brutal-honesty reviewer

**Model**: `x-ai/grok-4.3` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1330pt
**Wall time**: 25.5s
**Persona focus**: Cut through narrative inflation. Flag overclaim, false confidence, headline numbers that aren't load-bearing, anything written to dodge a reviewer rather than to be true. Is the central claim actually new? Are 'first', 'novel', 'unprecedented' framings honest given the actual literature?

---

**Tokens**: prompt=57667, completion=2137, reasoning=1351, total=59804

---

**## BLOCKER: PAPER-GRO-B1**

**Section:** Abstract (headline count) + §4.3 (cross-survey matches) + §6.4 deferral (a)

**Issue:** The canonical 378,280 unique-object headline is arithmetically inconsistent with the reported numbers. 388,493 survey-level detections minus 637 pairwise coincidences yields 387,856, leaving an unexplained 9,576-object shortfall. The text explicitly defers the union-find recompute while freezing the headline.

**Fix:** Replace the headline with the verified union-find result or explicitly state the current figure is provisional and quote the 387,856 upper bound under the pairwise assumption.

**## MAJOR: PAPER-GRO-B2**

**Section:** Abstract + §1 + §6.4 (limitations)

**Issue:** "Largest-scale application... to date" and "~141× the size of the largest prior" framing is not load-bearing. The ratio mixes six-survey aggregate scope with Path-C retraining; the like-for-like single-survey comparison (DESI DR1 at ~73×) is the only apples-to-apples metric, and prior single-survey autoencoder papers already exist at 10^5–10^6 scale.

**Fix:** Retitle and abstract to "largest single-survey autoencoder anomaly catalog on DESI DR1" plus "first 7-survey positional cross-match" and remove the 141× aggregate claim.

**## MAJOR: PAPER-GRO-B3**

**Section:** Abstract + §5 (f_NL forecast)

**Issue:** The central cosmological claim is presented with headline numbers (σ_fNL = 8.27 ± 2.37, 7.9% improvement) while the text states α_jk = 0.19 ± 0.65 is consistent with zero at 0.29σ and the improvement is consistent with no gain at <1σ. The empirical α measurement closes a deferral but does not support a positive multi-tracer detection.

**Fix:** Move the σ_fNL = 8.27 figure to a "central-value forecast only" subsection and lead the abstract/§5 with the null-consistent result; delete all improvement percentages from the headline summary.

**## MAJOR: PAPER-GRO-B4**

**Section:** Abstract + §3.3 (LAMOST) + §6.1

**Issue:** LAMOST is labeled a transparent FAIL (98% blue-excess contamination, 5.8% continuum-dip recovery) yet still contributes ~113k objects to the 378,280 headline and is retained "for completeness." The stratification language is a post-hoc patch rather than a pre-registered design choice.

**Fix:** Remove LAMOST native counts from the headline aggregate entirely; report only the catalog-grade ~265k tier and move the full LAMOST set to an appendix as a methodological failure case study.

**## minor: PAPER-GRO-M1**

**Section:** Abstract (multiple stratification paragraphs) + §6.4

**Issue:** The abstract contains an excessive number of parenthetical clarifications, tier definitions, and "should never be quoted" warnings. This reads as defensive drafting to prevent reviewer mis-citation rather than clean scientific communication.

**Fix:** Condense to one paragraph defining the two-tier structure and one sentence on recommended primary number; move all remaining caveats to §6.4.

**## nit: PAPER-GRO-N1**

**Section:** Title + abstract first sentence

**Issue:** "378,280 Path-C Unique Anomalies" includes 200 Planck map patches that are sky regions, not point sources. The title therefore misrepresents the physical nature of the catalog for any reader who stops at the title.

**Fix:** Change title to "378,080 Unique Point-Source Anomalies + 200 Planck Map Patches" or equivalent.
