# P3 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-v63verify-v2_P3_v3_1_63
**Wall time**: 85.1s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=68994, completion=5174, reasoning=4142, total=74168

---

## PAPER-GPT-B1 — BLOCKER — §2.2 “In-sample scoring and held-out validation”

Concrete issue: §2.2 still says each fold “scores the held-out 20% (9,400 spectra)” but then reports five top-1% sets of 470 objects, union 546, and 399 objects appearing in all five folds. Those overlap numbers are mathematically impossible for disjoint held-out folds; they only work if each fold scored the full 47,000 pool, as stated later in §6.4(i).

Fix: Rewrite §2.2 to match §6.4(i): each fold trains on 80% and scores the full 47,000 pool for the Jaccard statistic. If held-out-only scoring was actually used, recompute all union/Jaccard/all-five counts.

## PAPER-GPT-B2 — BLOCKER — §5, §6.2, Conclusions item 5

Concrete issue: The paper still promotes the invalid local-linear Fisher propagation as headline in multiple places: “σ(fNL)=8.27±2.37,” “σGS=2.28±7.43,” and §5 even calls the linear [3.62,12.95] interval “canonical” after the abstract/caveat explicitly replace it with the positivity-respecting envelopes [3.92,8.98] and [0.94,8.98]. This is an internal contradiction and leaves unphysical error bars in the conclusions.

Fix: Make the positivity-respecting α² mapping the only headline in §5, §6.2, and Conclusions. Move 8.27±2.37 / 2.28±7.43 to a clearly labeled “invalid local-linear reference only” sentence or delete them.

## PAPER-GPT-M1 — MAJOR — Table I caption/footnotes; §2.2; §3.2–§3.3

Concrete issue: Threshold accounting is inconsistent. §2.2 says SDSS uses absolute S>5, Table I says SDSS/LAMOST are top-percentile slices, and the SDSS “top-1%” value 77,905 is not 1% of either 1,925,279 scored spectra or 2,304,830 total spectra; 19,253 is the actual 1% number stated elsewhere.

Fix: Split cross-transfer and Path-C native results into separate tables with explicit denominators: total catalog, successfully scored count, threshold, percentile, and anomaly count. Do not label the SDSS 77,905 continuity slice as top-1%.

## PAPER-GPT-M2 — MAJOR — Table I; §3.4 Planck CMB; §2.3 Path-C step 2

Concrete issue: Planck native retrain/re-score is described as 200,000 patches with top 200 anomalies, but Table I still lists Ntotal=20,000, Nanom=200, rate=1.00%. If the native Path-C Planck set is top 200 of 200,000, the rate is 0.10%, and the total processed in the Path-C row is off by 180,000.

Fix: Either update Table I and all total-source/rate arithmetic to use 200,000 native Planck patches, or explicitly state that only a 20,000-patch subset enters the released Path-C catalog and reconcile that with the §3.4 re-score text.

## PAPER-GPT-M3 — MAJOR — Appendix “Shot-noise sensitivity for sparse anomaly tracers”

Concrete issue: The shot-noise appendix uses σfNL baselines 16.85, 12.72, 11.71, 12.56, 13.35, which are not mapped to the main-text baseline σstd=8.98 / empirical σ=8.14. It also says a 15% Fisher-information penalty gives σ=12.56, a “+1.27%” improvement over σ=12.72, which is directionally inconsistent unless the reference model is different and clearly defined.

Fix: Define the separate Fisher configuration, tracer set, and baseline explicitly, or remove the appendix from the headline forecast. Recompute improvements consistently in Fisher information or σ, with one baseline per comparison.

## PAPER-GPT-M4 — MAJOR — §5.2 NANOGrav; Appendix PTA MCMC

Concrete issue: The PTA “likelihood” multiplies 30 per-bin free-spectrum KDE posterior marginals as independent likelihood factors, then quotes γ=2.567±0.382 and 1.13σ/4.61σ parameter shifts. The acknowledged missing inter-bin covariance/prior-Jacobian affects the parameter posterior itself, not only Bayes factors/model comparison.

Fix: Either use the proper joint free-spectrum likelihood/samples with covariance and prior handling, or downgrade the PTA result to an approximate diagnostic with no formal σ-disfavoring claims.
