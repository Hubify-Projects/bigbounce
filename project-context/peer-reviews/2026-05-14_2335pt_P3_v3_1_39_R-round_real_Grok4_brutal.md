# P3_v3_1_39 R-round — REAL cross-vendor — Grok-4 brutal-honesty reviewer

**Model**: `x-ai/grok-4` (via OpenRouter)
**Round**: 2026-05-14_2335pt
**Wall time**: 123.7s
**Persona focus**: Cut through narrative inflation. Flag overclaim, false confidence, headline numbers that aren't load-bearing, anything written to dodge a reviewer rather than to be true. Is the central claim actually new? Are 'first', 'novel', 'unprecedented' framings honest given the actual literature?

---

**Tokens**: prompt=52238, completion=1549, total=53787

---

## PAPER-GRO-B1 (MAJOR): Abstract and Title, Headline Number Inflation
The 378,280 headline aggregates 378,080 point sources with 200 non-object CMB patches for "completeness," but repeatedly warns against quoting it as object density; this is narrative inflation to claim "largest" catalog while the load-bearing point-source tier is 200 smaller and not consistently headlined. Fix: Revise title and abstract to lead with 378,080 point-source anomalies, relegate total to a stratified footnote, and drop "largest" unless substantiated against like-for-like literature (e.g., Liang2023 is single-survey, not multi).

## PAPER-GRO-B2 (MAJOR): Section 5, NANOGrav Recompute Framing
The gamma=2.567±0.382 recompute from real KDE is sound (supersedes synthetic 3.20±0.42), but bounce at +1.13sigma is "marginally consistent" while SMBHB at +4.61sigma is "excluded" without hedging posterior non-Gaussianity or model priors; this asymmetrically favors bounce despite both being above mean. Fix: Frame both as positive deviations with bounce closer to mean, report Gaussian-approximated likelihood ratio as parameter-shift only (not Bayes factor), and add caveat that exclusion assumes Gaussian posterior.

## PAPER-GRO-B3 (MAJOR): Section 5, f_NL Forecast Framing
The sigma(f_NL)=8.27±2.37 is properly anchored to empirical alpha=0.19±0.65 (consistent with null at 0.29sigma), but abstract/headline claims imply positive improvement without emphasizing <1sigma from null; central-value forecast is honest but downplays wide CI including no-improvement regime. Fix: Explicitly state in abstract and conclusions that 7.9% improvement is consistent with zero at <1sigma, and prioritize the asymmetric 95% CI [5.91,12.92] over symmetric ±2.37.

## PAPER-GRO-M1 (minor): Section 4.1, Novelty Overclaim
58.8% SIMBAD-unmatched is reported as aggregate but clarified as database-coverage, with genuine novelty ~17.8% for DESI top-1000; however, this is a single-stratum estimate without testing full-catalog rate, risking misinterpretation as bound. Fix: Add score-stratified novelty on quintiles/top-10,000 to confirm if full-catalog rate is higher/lower than 17.8%, and explicitly state it's not a bound.

## PAPER-GRO-M2 (minor): Section 2.3, Path-C Jaccard Anchoring
5-fold Jaccard mean=0.862 is claimed as PASS on DESI retrain, but gate criterion was preregistered as ≥0.70 without specifying if it's per-survey or global; anchoring is correct but not propagated to other surveys' stability (e.g., Gaia 41% noted in footnote). Fix: Report Jaccard for all native retrains uniformly, and if below gate, downgrade to exploratory tier like LAMOST.

## PAPER-GRO-N1 (nit): Bibliography, Fused Metadata Audit
CaiBrandenberger:2014 appears as fused "CaiBrandenberger:2014" but ADS/arXiv checks show separate Cai:2014 (arXiv:1406.4556) and Brandenberger papers; no coherence issue but pattern matches prior Shamir:2022/Jia:2023 fusions. Fix: Split into distinct citations with full metadata, and audit all for arXiv-ID/title/author/venue consistency.
