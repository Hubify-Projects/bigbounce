# P3_v3148_R10 R-round — REAL cross-vendor — Grok-4.3 brutal-honesty reviewer

**Model**: `x-ai/grok-4.3` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1300pt
**Wall time**: 31.3s
**Persona focus**: Cut through narrative inflation. Flag overclaim, false confidence, headline numbers that aren't load-bearing, anything written to dodge a reviewer rather than to be true. Is the central claim actually new? Are 'first', 'novel', 'unprecedented' framings honest given the actual literature?

---

**Tokens**: prompt=57441, completion=2595, reasoning=1734, total=60036

---

**PAPER-GRO-B1**  
**BLOCKER** — Abstract + §5 (multi-tracer Fisher)  
The abstract and main-text Fisher results still propagate the linear form \(\sigma(f_{\rm NL})(\alpha) = 8.98 - 3.66\alpha\) and quote the unphysical 95% envelope [3.62, 12.95] (or the GS case 2.28 ± 7.43 that crosses zero) even while caveat (i) and (j) admit the form violates Fisher positivity. The corrected positivity-respecting remap \(1/\sigma^2 = F_0 + c\alpha^2\) is only in the caveats, not anchored in the headline numbers or abstract.  

Fix: Replace the linear extrapolation and all quoted envelopes with the positivity-respecting form throughout abstract/§5; report only the central value 8.27 (or 1.95 for GS) with the corrected asymmetric interval [0.94, 8.98] and explicitly state the linear form is invalid outside the fiducial neighborhood.

**PAPER-GRO-B2**  
**BLOCKER** — §4.3 / crossmatches + Table 1 footnote  
The deduplication arithmetic is internally inconsistent: 637 pairwise coincidences imply at most 387,856 unique objects, yet the headline 378,280 is retained with a 9,576 shortfall explicitly flagged as deferral (a) and pending union-find recompute. The 378,280 number is therefore not load-bearing.  

Fix: Run the union-find on the released parquet, replace the headline with the verified unique count, and move the current 378,280 figure to a sensitivity row or delete it.

**PAPER-GRO-M1**  
**MAJOR** — Title + abstract + §1  
The framing “first multi-survey anomaly detection campaign at combined scale exceeding 37.3 million” and “largest-scale application … to date” is false advertising. Prior single-survey autoencoder work (Baron & Poznanski 2017, Liang et al. 2023) already exists at comparable per-survey scale; multi-survey concatenation with 5″ dedup is incremental, not unprecedented. The 141× claim is only versus one specific EDR paper, not the literature.  

Fix: Delete “first” and “largest-scale … to date”; replace with “largest published catalog from a uniform autoencoder pipeline across seven archives” and cite the actual prior single-survey baselines.

**PAPER-GRO-M2**  
**MAJOR** — Abstract + §3.4 + §6.4 (LAMOST)  
LAMOST is labeled a transparent FAIL (98% blue-excess contamination, 5.8% continuum-dip recovery) yet its 113k objects are still folded into the 378,280 headline and the “catalog-grade” split is left approximate. The exploratory-tier disclaimer is buried in footnotes and caveats.  

Fix: Move LAMOST to an explicit “exploratory / methodological lesson” appendix only; recompute the headline and all downstream statistics using only the six gate-passing or high-stability surveys (≈265k catalog-grade tier) and state the number explicitly.

**PAPER-GRO-M3**  
**MAJOR** — §5 (cosmological applications)  
The multi-tracer \(f_{\rm NL}\) result is reported as a “7.9% improvement” and “central-value forecast” while the text simultaneously states it is consistent with zero at <1σ and does not constitute a positive detection claim. The cosmological section is therefore narrative inflation around a null result.  

Fix: Retitle the section “Illustrative multi-tracer sensitivity study (null result at current S/N)” and lead with the statement that the empirical \(\alpha\) measurement yields no statistically significant improvement over the single-tracer baseline.

**PAPER-GRO-m4**  
**minor** — Abstract + §1  
The paper contains an unusually long preamble of version-history and reviewer-response notes that belong in the git log or a separate response document, not the submitted manuscript.  

Fix: Remove the entire multi-paragraph version-history block from the LaTeX source before submission.
