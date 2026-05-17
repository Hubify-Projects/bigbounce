# P3_v3141 R-round — REAL cross-vendor — Grok-4.3 brutal-honesty reviewer

**Model**: `x-ai/grok-4.3` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-17_0200pt_P3_v3141_R3_R-round_real
**Wall time**: 68.7s
**Persona focus**: Cut through narrative inflation. Flag overclaim, false confidence, headline numbers that aren't load-bearing, anything written to dodge a reviewer rather than to be true. Is the central claim actually new? Are 'first', 'novel', 'unprecedented' framings honest given the actual literature?

---

**Tokens**: prompt=52996, completion=5464, reasoning=4640, total=58460

---

**## PAPER-GRO-B1: BLOCKER**

**Section:** Training and Scoring (OOD validation paragraph) + Path-C caveats (i)

**Issue:** Direct mathematical contradiction on OOD MSE normalization. Paper states 52.8% of the 100k OOD sample exceeds 5× training validation MSE (i.e., the fixed S>5 / MSE≈0.143 threshold) while simultaneously claiming “the 0.87% DESI anomaly rate is preserved on this independent OOD sample.” These statements are incompatible for any fixed threshold applied to the reported OOD distribution.

**Fix:** Either delete the “rate is preserved” sentence or report the actual counted fraction of the 100k OOD sample lying above the fixed MSE=0.143 threshold and reconcile the 52.8% figure. Do not leave both claims in the text.

**## PAPER-GRO-B2: BLOCKER**

**Section:** Cross-Survey Analysis (deduplication paragraph) + Path-C caveats (a)

**Issue:** Load-bearing arithmetic mismatch in 7-way deduplication. Paper reports 637 multi-survey 5″ coincidences (all pairwise, no triples) yet 388,493 survey-level detections → 378,280 unique objects implies 10,213 duplicates collapsed. The two numbers cannot both be correct under the stated union-find procedure.

**Fix:** Recompute the union-find cluster manifest with explicit per-cluster multiplicity counts and update both the 637 figure and the compression arithmetic to be internally consistent. Until reconciled, the headline 378,280 is not auditable.

**## PAPER-GRO-M1: MAJOR**

**Section:** Abstract (PTA sentence) vs. §5.2 NANOGrav Bounce Consistency

**Issue:** Abstract retains the stale synthetic-from-power-law value γ=3.20±0.42 (bounce at 0.48σ) while the body has superseded it with the real-KDE posterior γ=2.567±0.382 (bounce at +1.13σ). This is an abstract–body contradiction on a load-bearing cosmological consistency claim.

**Fix:** Update the abstract PTA sentence to the real-KDE numbers and σ-deviation, or remove the specific numerical claim entirely if the synthetic fit is no longer used.

**## PAPER-GRO-M2: MAJOR**

**Section:** Abstract (tier stratification language) + Table 1 footnotes + §3.1 eROSITA

**Issue:** Persistent placeholder/reference-set leakage. Table and footnotes still prominently feature the 9,303-object IsolationForest top-1% reference set for eROSITA while the published catalog headline is 298. The distinction is explained but the 9,303 number remains visually dominant and risks being mis-cited as the anomaly count.

**Fix:** Remove all references to 9,303 from the main table and footnotes; retain only the 298 headline with a single-sentence cross-validation diagnostic note if needed. Move the full XV-stability discussion to the caveats section.

**## PAPER-GRO-m1: minor**

**Section:** Abstract (Liang+2023 comparison) + §1 Introduction

**Issue:** 141× framing is now qualified as “not a like-for-like single-survey methodology comparison,” but the title and opening sentence still lead with the aggregate 378,280 / 2,685 ratio without equal prominence to the honest 73× DESI-only like-for-like figure.

**Fix:** Add a parenthetical in the title or first sentence: “(141× aggregate vs. 73× like-for-like DESI-only).”

**## PAPER-GRO-n1: nit**

**Section:** Abstract (final sentence on catalog release)

**Issue:** HuggingFace path is given as “bamfai/bigbounce-anomaly-catalog” but no version tag or commit hash is provided, making exact reproducibility of the released 378,280-row parquet unverifiable from the text alone.

**Fix:** Append “(v3.1.41, commit <short-hash>)” or equivalent.
