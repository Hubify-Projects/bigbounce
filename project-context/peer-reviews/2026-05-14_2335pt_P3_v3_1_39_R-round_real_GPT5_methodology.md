# P3_v3_1_39 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Round**: 2026-05-14_2335pt
**Wall time**: 74.1s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=56810, completion=4874, total=61684

---

## PAPER-GPT-B1 — BLOCKER — §4.3, Table 1 footnotes, Conclusions item 8

**Issue:** The canonical arithmetic for `388,493 survey-level detections → 378,280 unique` requires **10,213 duplicate detections**. But §4.3 says there are only **637 multi-survey coincidences, all pairwise, no triples**; that would reduce the count by only 637, giving **387,856 unique**, not 378,280. The 378,280 headline is not arithmetically supported.

**Fix:** Recompute and publish the union-find dedup summary: number of clusters by multiplicity, total duplicate detections removed, and per-survey overlap matrix. Either change the unique count or replace the “637 all pairwise” statement with the actual 10,213-compression cluster accounting.

## PAPER-GPT-B2 — BLOCKER — §2.2 “In-sample scoring and held-out validation”

**Issue:** The DESI OOD validation is internally inconsistent. It states the DESI `S>5` threshold corresponds to **MSE ≈ 0.143**, while the 100k OOD sample has **median MSE = 0.178**, so more than half the OOD sample should exceed the threshold; nevertheless the paper claims the **0.87% anomaly rate is preserved**.

**Fix:** Resolve the units/normalization mismatch. Report OOD MSE on the exact same scale used for the production `S` cut, give the actual number above `S>5`, and remove the “0.87% preserved” claim unless it follows from the same threshold.

## PAPER-GPT-M1 — MAJOR — §2.2, Table 1, §3.2–3.3, Conclusions

**Issue:** The 378,280 catalog is built from non-uniform and partly arbitrary thresholds: SDSS contributes **77,905** from a “bookkeeping” continuity slice although only **12** pass native `S>5`; LAMOST contributes **113,342** top-1% exploratory objects although only **2,054** pass `S>5`; Gaia is included despite **41%** stability. The title/abstract still label the aggregate “Path-C unique anomalies,” which overstates catalog-grade reliability.

**Fix:** Split the headline into catalog-grade, exploratory, and diagnostic tiers with exact counts after dedup. Do not use SDSS/LAMOST/Gaia exploratory/top-percentile slices in the same headline as DESI/eROSITA/Planck/NEOWISE unless the threshold policy is explicitly tiered in the title, abstract, and conclusions.

## PAPER-GPT-M2 — MAJOR — §3.2–3.3, Table 1, Abstract

**Issue:** The “37.3 million sources” Path-C headline is not the actual native-scored denominator. SDSS native scoring covers **1,925,279 / 2,304,830** spectra, leaving **376,157 unscored**, and LAMOST excludes **84,433** spectra; yet the Path-C row still uses the full survey totals and claims a full 37.3M native catalog.

**Fix:** Report two denominators: archive size and successfully native-scored size. All Path-C rates and “from 37.3M” claims must use the successfully scored denominator, or explicitly say the native Path-C catalog is incomplete for SDSS/LAMOST.

## PAPER-GPT-M3 — MAJOR — §5.1, Appendix C

**Issue:** The `f_NL` uncertainty is not a propagated forecast uncertainty. The quoted `σ(f_NL)=8.27±2.37` propagates only the jackknife error on `α`; it excludes the stated zero-systematics assumptions, photo-z uncertainty, shot noise, fiber assignment, and selection-function errors. Appendix C also mixes incompatible baselines (`σ_fNL^std=8.98` in main text vs `12.72/16.85` in shot-noise appendix), and the stated 95% mapping from `α∈[-1.08,1.46]` to `σ_fNL∈[5.91,12.92]` does not follow from the linear table.

**Fix:** Recompute a single Fisher forecast with the same baseline throughout and propagate `α`, shot noise, photo-z, selection, and systematics nuisance parameters into one interval. Until then, quote `8.27` only as a central zero-systematics sensitivity number, not `±2.37` as a forecast error bar.

## PAPER-GPT-M4 — MAJOR — §5.2, Appendix D′, Bibliography

**Issue:** The NANOGrav recompute treats per-bin free-spectrum KDE posterior densities as independent likelihood factors. That ignores bin covariance and prior/Jacobian effects in the released free-spectrum posterior product, so the derived `γ=2.567±0.382` and especially the “SMBHB excluded at 4.61σ” language are not a proper model-level exclusion. Bibliography audit: no obvious fused-arXiv-ID pattern appears in the arXiv-bearing entries, but several metadata entries are ADS-incoherent/incomplete: `eROSITA_DR1` title is not the DR1 catalog title, `SDSS_DR18` title is truncated/incorrect, `GaiaDR3` lacks the full A&A title, `NEOWISE` lacks volume/pages/arXiv/DOI, and `Nicolaou2026` is unverifiable as written.

**Fix:** Rephrase the PTA result as a conditional free-spectrum posterior-shape fit, not an SMBHB model exclusion, unless a full covariance-aware/evidence calculation is provided. Clean the bibliography against ADS/arXiv with full title, author list/collaboration, venue, volume, page/article number, year, DOI/arXiv for every entry; remove or fully identify unverifiable “in press” citations.
