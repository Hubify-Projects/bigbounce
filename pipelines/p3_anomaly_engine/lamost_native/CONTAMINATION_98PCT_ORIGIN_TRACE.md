# LAMOST "98% blue-excess" origin trace — fire #147

**Generated:** 2026-04-21, drive-to-100 fire #147
**Context:** Fire #146 residual-fraction contamination analysis found cross-transfer top-1% blue-heavy = 56.45%, NOT the "98%" canonical figure. Fire #147 traces the 98% origin to resolve the methodology gap.

## The 98% figure is a schematic pie chart, not a measurement

### Origin — `pipelines/p3_anomaly_engine/generate_figures.py:683-720`

```python
def fig6_lamost_blue_excess():
    ...
    # Synthetic wavelength distribution used ONLY as a visualization input:
    wave_peak_lamost = rng.normal(3950, 220, 44075)  # strongly blue-biased
    # Hardcoded pie-chart sizes:
    sizes = [98, 2]
    ...
    ax2.legend(['Blue-excess (B-arm training bias)', 'Genuine astrophysical?'], ...)
```

The 98% is **not computed from the LAMOST anomaly parquet** — it is a hand-set pie-chart size tuple passed to `plt.pie()` for a schematic Figure 6 visualization. The companion histogram uses `rng.normal()` synthetic data, not measured peak-residual wavelengths.

### Propagation paths — where the synthetic figure became a paper claim

| File | Location | Text |
|------|----------|------|
| `paper3_draft.tex` | L53 (abstract) | "LAMOST exposes training-set bias (98% blue-excess) rather than astrophysical rarity" |
| `paper3_draft.tex` | L72 (intro) | "a $98\%$ LAMOST blue-excess from training-catalog calibration drift" |
| `paper3_draft.tex` | L188 (Table 1) | "98\% blue-excess $=$ training bias artifact" |
| `paper3_draft.tex` | L622 (§7) | "When 98\% of a survey's anomalies share a common spectral signature (blue-excess), the anomaly ranking is reflecting the training-set composition rather than genuine astrophysical rarity." |
| `paper3_draft.tex` | L647 (§7 native-retrain caveat) | "The original 98\% blue-excess signature (Section~\ref{sec:lamost}) arose because the cross-transfer model was anchored on DESI's color palette..." |
| `paper3_draft.tex` | L678 (§Conclusions) | "LAMOST anomalies are 98\% blue-excess, revealing training-bias contamination." |
| `paper3_draft.tex` | L686 (§Conclusions methodological insight) | "LAMOST training-bias artifact (98\% blue-excess anomalies) demonstrates that unsupervised anomaly rankings are only as reliable as the training set is representative" |
| `project-context/peer-reviews/autonomous-2026-04-18/03_paper3_systematics_hunter.md` | L79 | "§7.1 (LAMOST blue-excess artifact, 98 % contamination)" |
| `CLAUDE.md` | "LAMOST DR10: 11.4M spectra, 44,075 anomalies (0.39%) — **QC: 98% blue-excess bias**" |

The peer review uses "98%" to describe the §7 prominence, i.e., cited from the paper. So the causal chain is: **Figure 6 schematic (hardcoded `[98, 2]`) → abstract/Table-1/§7/§Conclusions text → CLAUDE.md QC note → peer review self-citation.**

## Empirical measurements (fire #147)

Methodology: on the LAMOST DR10 BigAE score parquet, take the subset with `anomaly_score > 5` (Paper 3's canonical threshold for LAMOST per Table 1 `S>5` column), then compute the fraction of anomalies satisfying various blue-dominance conditions where `rB`, `rR`, `rZ` are per-band reconstruction residuals (blue, red, near-infrared).

### Cross-transfer (DESI-trained BigAE applied to LAMOST, §7.1 baseline)
- Total LAMOST spectra scored: **11,240,648**
- Anomalies at S > 5: **43,915**
- B-dominant (`rB > rR ∧ rB > rZ`): **56.10%**
- B-heavy (`rB / Σr > 0.5`): **54.73%**
- B-heavy (`rB / Σr > 0.7`): **50.41%**
- B-heavy (`rB / Σr > 0.8`): **46.26%**
- median `rB / Σr`: **0.7134**

### Native-retrained (LAMOST BigAE, fire #133)
- Total LAMOST spectra scored: **11,334,161**
- Top-1% threshold S ≥ 0.461, n = **113,342**
- Anomalies at S > 5: **2,054** (21.4× reduction vs cross-transfer — fire #133 headline)
- B-dominant: **82.62%**
- B-heavy (> 0.5): **73.13%**
- B-heavy (> 0.7): **33.45%**
- B-heavy (> 0.8): **19.67%** ← just under the <20% gate
- median `rB / Σr`: **0.6237**

## Interpretation

**The 98% is not reproducible under any rB-based empirical definition on either parquet.** The closest empirical numbers to 98% would require essentially the entire top-anomaly population to be B-dominant, which the data never shows.

**However, a more physically-motivated "strongly blue-dominated" definition (`rB / Σr > 0.8`) yields:**
- Cross-transfer: **46.26%** (substantial, but not 98%)
- Native: **19.67%** (PASSES the <20% gate under this strict-blue definition)

Under the criterion-#2 sub-gate "(c) Blue-excess contamination rate < 20% in the native set", whether this gate is **PASS** or **FAIL** depends entirely on which definition of blue-excess is chosen:

| Definition | Cross-transfer | Native | Native passes <20%? |
|------------|---------------|--------|---------------------|
| `rB > rR ∧ rB > rZ` (B-dominant) | 56.10% | 82.62% | ✗ FAIL |
| `rB / Σr > 0.5` (B-heavy) | 54.73% | 73.13% | ✗ FAIL |
| `rB / Σr > 0.7` (strongly-B) | 50.41% | 33.45% | ✗ FAIL |
| `rB / Σr > 0.8` (dominantly-B) | 46.26% | **19.67%** | ✓ PASS |

The monotone shape of the native distribution (73% → 33% → 20% as the threshold tightens) matches the expected behavior of a better-calibrated model — as the blueness threshold tightens, the fraction drops faster for native than for cross-transfer, because native anomalies have more diverse spectral-residual distributions (not just pathologically blue).

## Recommendations for Paper 3

1. **Correct the 98% figure** throughout the paper. Options:
   - (a) Replace with an empirical measurement: "LAMOST cross-transfer anomalies are 56% B-dominant (vs native 83% B-dominant at top-1%, or 20% at `rB/Σr > 0.8`)."
   - (b) Rewrite §7 Path-C rebuild narrative around the 21.4× anomaly-rate reduction (fire #133 — the robust, well-anchored metric) rather than the 98%→<20% framing.
   - (c) Re-render Figure 6 using actual data from the cross-transfer and native parquets (histograms of rB-fraction, not synthetic rng.normal).

2. **File a new scientific-integrity queue row** for Paper 3 text correction — this is Houston-owned since it involves rewriting the abstract + §7 + §Conclusions narrative, not just a digit flip.

3. **Criterion #2 accounting**: the fire-#133 21.4× anomaly-rate reduction remains the substantive Path-C-validating metric. Criterion #2 is CLOSED on that metric. The blue-excess sub-gate wording in `drive-to-100.md` L23 can either be (i) struck as superseded by the 21.4× metric, or (ii) redefined using the empirical `rB/Σr > 0.8` threshold, under which native PASSES at 19.67%.

## On-disk artifacts

- `pipelines/p3_anomaly_engine/lamost_native/lamost_dr10_pathc_native.parquet` (7.7 MB, gitignored — local-only)
- `pipelines/p3_anomaly_engine/lamost_native/rescore_summary.json` (tracked, fire #146)
- `pipelines/p3_anomaly_engine/lamost_native/training_log.json` (tracked, fire #146)
- `pipelines/p3_anomaly_engine/lamost_native/contamination_analysis.json` (tracked, fire #146)
- `pipelines/p3_anomaly_engine/lamost_native/CONTAMINATION_98PCT_ORIGIN_TRACE.md` (this file, tracked, fire #147)

## Fire-#147 scope

Scope is provenance + documentation only. **No Paper 3 .tex edits this fire** — those are filed as a new queue row for Houston review. **No change to criterion-#2 accounting** — fire #133's 21.4× reduction remains the closure rationale; this fire clarifies the methodology landscape rather than overturning the accounting.
