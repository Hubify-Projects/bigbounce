# P3_v3140_R2 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-15_0300pt
**Wall time**: 138.2s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=57642, completion=8710, reasoning=7768, total=66352

---

## PAPER-GPT-B1 — BLOCKER — §2.2 / §Path-C Caveats (i) / Abstract

**Issue:** The DESI 5-fold “held-out” Jaccard validation is arithmetically impossible as written. If each fold scores only its disjoint 9,400-object held-out split, fold top-1% sets have 94 objects, cannot overlap across folds, and their union cannot be 546 objects (>470 max).  
**Fix:** State the actual protocol. If models scored a common 47k or 103k set, say so and recompute labels; if truly out-of-fold only, delete the Jaccard/all-five-fold claims and replace with a valid common-holdout multi-seed stability test.

## PAPER-GPT-B2 — BLOCKER — §4.3 / Table 1 footnote / Conclusions

**Issue:** Headline dedup arithmetic is unresolved: 388,493 detections → 378,280 uniques implies 10,213 duplicate detections collapsed, but §4.3 reports only 637 multi-survey clusters, all pairwise and no triples, which would collapse only 637 detections. The title/headline count depends on this contradiction.  
**Fix:** Recompute and publish the union-find cluster manifest with multiplicities; update 388,493/378,280/637 consistently or remove the unique-count headline until reconciled.

## PAPER-GPT-B3 — MAJOR — Table 1 / §3.2 / §3.3 / §3.5

**Issue:** The canonical Path-C count mixes incompatible thresholds. SDSS contributes 77,905 “native” objects via an arbitrary continuity slice at \(S\ge0.1060\), which is 4.05% of the 1,925,279 scored spectra, not top-1%, while the strict \(S>5\) native count is 12; LAMOST contributes a top-1% slice despite failing the 5σ gate; Planck native uses 200/200,000 patches while Table 1 still reports 200/20,000 = 1%.  
**Fix:** Define one canonical inclusion rule per survey, label exploratory tiers outside the headline, and recompute the Path-C sum/rates from the actually scored denominators.

## PAPER-GPT-B4 — MAJOR — §2.2 / §Path-C Caveats deferral (b)

**Issue:** DESI OOD normalization remains internally inconsistent: the paper says \(S>5\) corresponds to MSE \(\sim0.143\), but the OOD median MSE is 0.178, which would imply >50% exceed threshold, not the claimed preserved 0.87% anomaly rate.  
**Fix:** Report the OOD distribution in canonical \(S=(\mathrm{MSE}-\mu_{\rm val})/\sigma_{\rm val}\) units and give the exact OOD fraction above the production threshold; do not claim rate preservation until this is shown.

## PAPER-GPT-B5 — MAJOR — Abstract / §5

**Issue:** The Gold+Silver \(\alpha\) shift is incorrectly described as “toward the bounce prediction” and as preserving a bounce-induced \(f_{\rm NL}=-35/8\) shape signal. \(\alpha\) is a noisy clustering-bias ratio used in a forecast; it is not a measurement of \(f_{\rm NL}\), its sign, or the bounce bispectrum shape.  
**Fix:** Remove the bounce-shape interpretation from the \(\alpha\) discussion. State only that the high-confidence subset has a larger central bias-ratio estimate with \(<1\sigma\) significance.

## PAPER-GPT-B6 — minor — §3.4 / §7 / Appendix D Fig. A3 caption

**Issue:** Novelty framing still leaks. “203 novel eROSITA X-ray sources” conflicts with §4.1’s statement that extended VizieR/NED matching finds archival IDs for SIMBAD-unmatched samples; Appendix D’s “73% genuinely novel” uses only SIMBAD/NED/Milliquas and conflicts with the paper’s 20-catalog 17.8% single-sample novelty standard.  
**Fix:** Replace these with “SIMBAD-unmatched” or “not in SIMBAD/NED/Milliquas”; reserve “genuinely novel” for the 20-catalog DESI top-1000 measurement or a matching audit of the relevant subset.
