# P3_v3153_R15 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1600pt
**Wall time**: 189.6s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=65367, completion=8722, reasoning=7768, total=74089

---

## PAPER-GPT-B1 — BLOCKER — Sec. 2.2 “In-sample scoring and held-out validation”

**Issue:** The text says each fold “scores the held-out 20% (9,400 spectra)” but then reports a 546-object union and 399 objects appearing in all five folds. That is mathematically impossible for disjoint held-out folds; the reported statistics only make sense if each fold scores the full 47,000-spectrum pool.

**Fix:** Replace the Sec. 2.2 paragraph with the full-pool scoring description used later in caveat (i), or recompute all Jaccard/union/all-five statistics under true held-out-only scoring.

## PAPER-GPT-B2 — BLOCKER — Sec. 2.2 + Table I caption/footnotes

**Issue:** The SDSS threshold policy is still internally inconsistent. Sec. 2.2 says SDSS uses an absolute canonical \(S>5\) cut with a 3.4% anomaly rate, but Table I footnote says \(S>5\) gives only 12 SDSS sources and the 77,905 count is at \(S\ge0.1060\); additionally, 77,905/1,925,279 = 4.05%, not top-1%.

**Fix:** State one SDSS policy everywhere: either use the strict \(S>5\) subset (12 objects), the true top-1% native subset (19,253 at \(S\ge0.2051\)), or explicitly label 77,905 as a top-4.05% continuity slice, not top-1% and not \(S>5\).

## PAPER-GPT-B3 — BLOCKER — Sec. 5, Abstract, Conclusions: Fisher-positivity propagation

**Issue:** The paper still presents unphysical/local-linear Fisher results as headline values in several places: abstract quotes \(\sigma^{\rm GS}_{f_{\rm NL}}=2.28\pm7.43\), Sec. 5 calls the linear \([3.62,12.95]\) interval “canonical credible interval,” and Conclusions quote \(8.27\pm2.37\) and \(2.28\pm7.43\). These contradict the corrected positivity-respecting envelopes \(\sigma=8.14\,[3.92,8.98]\) and \(\sigma_{\rm GS}=1.95\,[0.94,8.98]\).

**Fix:** Make the positivity-respecting mapping canonical everywhere. Keep \(8.27\pm2.37\), \([3.62,12.95]\), and \(2.28\pm7.43\) only as explicitly labeled invalid/local-linear reference values, never as headline forecasts or credible intervals.

## PAPER-GPT-M1 — MAJOR — Appendix “Shot-noise sensitivity”

**Issue:** The shot-noise systematic budget uses incompatible Fisher baselines and inconsistent penalty arithmetic. The main text uses \(\sigma^{\rm std}_{f_{\rm NL}}=8.98\), while the appendix switches to single-tracer \(16.85\), dense-tracer \(11.71\), and baseline-multi \(12.72\) without mapping configurations; a 15–30% Fisher-information penalty applied to \(\sigma=11.71\) should give \(11.71/\sqrt{0.85}=12.70\) and \(11.71/\sqrt{0.70}=13.99\), not 12.56–13.35.

**Fix:** Separate the Fisher configurations or use one baseline consistently. Recompute the shot-noise-degraded \(\sigma_{f_{\rm NL}}\) values from the stated information penalty and propagate them into the systematic-budget narrative.

## PAPER-GPT-M2 — MAJOR — Sec. 4.3 / Conclusions / Data availability: dedup arithmetic still incompatible

**Issue:** The paper simultaneously claims 637 pairwise multi-survey coincidences and \(388{,}493\rightarrow378{,}280\) after deduplication. Pairwise collapse of 637 coincidences reduces the count by 637, giving 387,856; the remaining 9,576-object compression is not demonstrated by the stated multi-survey match count.

**Fix:** Either publish the union-find manifest showing the additional intra-survey/cluster collapses, update the unique count to 387,856 under the stated evidence, or remove the exact 378,280 headline until the recompute is auditable.
