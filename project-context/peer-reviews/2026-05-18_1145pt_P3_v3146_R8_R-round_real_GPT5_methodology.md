# P3_v3146_R8 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1145pt
**Wall time**: 128.6s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=61068, completion=7319, reasoning=6214, total=68387

---

## PAPER-GPT-B1 — BLOCKER — §4.3, Table 1, Conclusions, Data availability

**Issue:** The headline `378,280` unique count is still arithmetically unsupported. The paper admits `388,493 - 637 = 387,856` under the reported all-pairwise multi-survey coincidences, yet continues to assert exact `378,280` / `378,080 + 200` catalog sizes and data-product row counts as final.

**Fix:** Do not publish `378,280` as exact until the union-find cluster manifest reconciles the missing `9,576` collapses. Either replace with the arithmetic upper bound/provisional range or provide the recomputed cluster table proving the `10,213` duplicate-detection compression.

## PAPER-GPT-B2 — BLOCKER — §2.2, §6.4(i), Abstract, Conclusions

**Issue:** The DESI 5-fold Jaccard validation remains internally inconsistent in live methodology text. §2.2 and §6.4(i) say each fold scores only its disjoint `9,400` held-out spectra, but then report `546` union objects and `399` objects present in all five folds; that is impossible for disjoint held-out top-1% sets (`94` per fold, zero shared object IDs across folds).

**Fix:** Reconcile against the artifact: either state everywhere that each fold scored the full `47,000` pool (`470` top objects/fold), or recompute all Jaccard/union/all-five statistics for true held-out-only scoring. Remove “held-out validation CLOSED/PASS” until the convention is made consistent.

## PAPER-GPT-B3 — BLOCKER — §2.2, Table 1 caption/footnotes, §3.2–3.3, §6.4(h)

**Issue:** The spectroscopic threshold policy is still contradictory. Table 1 says DESI/SDSS/LAMOST use fixed `S>5`, but the headline Path-C counts use SDSS `S≥0.1060` (`77,905`, actually ~4.05% of `1,925,279`, not top-1%) and LAMOST `S≥0.4613` (`113,342`, top-1%); strict `S>5` gives only `12` SDSS and `2,054` LAMOST.

**Fix:** Split the table into strict-`S>5` and continuity/top-percentile rows, or make the headline count explicitly a heterogeneous-threshold catalog. Correct the SDSS “top-1%” language: `19,253`, not `77,905`, is the top-1% native SDSS slice.

## PAPER-GPT-M1 — MAJOR — §5, Abstract, §6.4(c), Conclusions

**Issue:** Fisher arithmetic is only partially fixed. The exact CI mapping is correct (`α∈[-1.084,1.464]` gives `[3.62,12.95]` and central `8.28`), but the abstract/§5/conclusions still quote `σ(f_NL)=8.27±2.37`; stale `[5.91,12.92]` references also remain despite the verification requirement of no remaining stale-envelope references.

**Fix:** Use one central value everywhere, preferably `8.28±2.37` if using `α=0.190`, or disclose the unrounded `α` that yields `8.27`. Delete the `[5.91,12.92]` historical interval entirely or move it to change-log metadata outside the paper.

## PAPER-GPT-M2 — MAJOR — §2.2, Fig. 1 caption, §3.4–3.5, Table 1

**Issue:** The promised single canonical anomaly score `S=(MSE-μ_val)/σ_val` is not enforced. Fig. 1 calls `S` “total per-element MSE,” Planck reports “score” values matching raw MSE/val_loss (`0.437–0.621`), eROSITA mixes canonical BigAE-`S` and IF raw scores, and survey thresholds combine z-scores, raw-MSE knees, IF axes, and percentiles.

**Fix:** Rename raw MSE, standardized `S`, IF raw score, and percentile rank as separate columns/variables throughout. Every table threshold must specify the exact axis and whether the count is absolute-threshold, knee-cut, or fixed-percentile.

## PAPER-GPT-m1 — minor — Table 1 footnote §, §6.4(v)

**Issue:** BigAE-vs-IF “strict subset” softening is mostly propagated, but stale verification-target text remains: Table 1 still says the intersection count is queued for the `v3.1.45` verification table, while §3.4/§6.4 say `v3.1.46+`. §6.4(v) also references nonexistent label `sec:erosita_two_axes`.

**Fix:** Change all target-version text to `v3.1.46+` and either add `\label{sec:erosita_two_axes}` or replace the broken reference with `\S\ref{sec:erosita}`.
