# P3_v3151_R13 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1430pt
**Wall time**: 74.1s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=64317, completion=4079, reasoning=3106, total=68396

---

## PAPER-GPT-B1 — BLOCKER

**Section:** Title; Abstract; §4.3; §7; Data availability  
**Issue:** The exact headline `378,280` remains arithmetically unsupported. §4.3 admits `388,493 - 637 = 387,856` under the stated all-pairwise coincidence count, leaving a `9,576`-object unexplained shortfall, yet the title/abstract/conclusions/data-release text still present `378,280` as exact.  
**Fix:** Recompute the union-find cluster manifest and replace the headline, or demote `378,280` everywhere to “pending dedup recompute” and quote `387,856` as the current arithmetic upper-bound.

## PAPER-GPT-B2 — BLOCKER

**Section:** §2.2 Training and Scoring; Table 1 caption/footnotes; §3.2–3.3; §7  
**Issue:** Threshold policy is still internally contradictory and does not reproduce the headline count. §2.2 says SDSS uses absolute `S>5` and LAMOST/Gaia use 99th percentile; Table 1 caption says all three spectroscopic surveys use fixed `S>5`; the Path-C sum uses SDSS `77,905` at `S≥0.1060` and LAMOST `113,342` top-1%, not the strict `S>5` counts of `12` and `2,054`.  
**Fix:** Define one canonical count-generating threshold per survey in a single table, and recompute/report the Path-C total from those thresholds; move continuity slices such as SDSS top-77,905 to a non-headline diagnostic row.

## PAPER-GPT-B3 — BLOCKER

**Section:** §2.2 “In-sample scoring and held-out validation”  
**Issue:** The 5-fold Jaccard contradiction survives in the main methods text. §2.2 says each fold scores only the held-out `9,400` spectra, but then reports five top-1% sets of `470` objects with union `546` and `399` objects appearing in all five folds; those numbers are only possible if each fold scores the full `47,000` pool.  
**Fix:** Replace the stale held-out-only sentence with the caveat text’s corrected full-pool scoring description, or recompute the Jaccard statistics for true disjoint held-out top-1% sets.

## PAPER-GPT-B4 — MAJOR

**Section:** §5 Cosmological Applications; §7 Conclusions; §6.4 caveats (i,j)  
**Issue:** Fisher-positivity corrections are not propagated into the load-bearing body/conclusions. §5 still calls the linear `95%` interval `[3.62,12.95]` “canonical” even though caveat (i) says the positivity-respecting envelope is `[2.4,8.98]`; §7 still quotes `σ_fNL^GS = 2.28 ± 7.43`, whose lower bound is negative and explicitly rejected in caveat (j).  
**Fix:** Replace all body/conclusion linear extrapolation intervals with the positivity-respecting asymmetric mappings, and label any retained linear numbers as local derivatives only, not intervals.

## PAPER-GPT-B5 — MAJOR

**Section:** Appendix “Shot-noise sensitivity for sparse anomaly tracers”; Fig. B11 caption  
**Issue:** The shot-noise appendix uses incompatible `σ(f_NL)` baselines (`8.98/8.43` in main text vs `16.85/12.72/11.71` in the appendix) without defining a different Fisher configuration, and the improvement/degradation signs are inconsistent: a Fisher-information penalty should increase `σ`, yet the text describes `12.56` as a `+1.27%` improvement over `12.72`.  
**Fix:** Either remove this appendix from the present paper or restate it as a separate Fisher configuration with its own baseline definitions and corrected improvement signs.

## PAPER-GPT-B6 — MAJOR

**Section:** §2.2 OOD validation  
**Issue:** The OOD artifact numbers are now internally consistent, but the text overstates overlap control: using a different random seed does not “guarantee zero overlap” with the 47k training pool unless target IDs are explicitly intersected. This matters because the paragraph is used as an independence validation.  
**Fix:** Replace the seed-based guarantee with an explicit target-ID/hash intersection result, or state that independence is by construction only after verified ID-level de-duplication.
