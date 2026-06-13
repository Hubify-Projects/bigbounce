# P3 R36conf — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar` [FALLBACK from sonar-pro]
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper3_anomaly_catalog_v3.1.101.pdf` md5=2cba9f61 pages=28
**Input format**: TEXT + web search + pass-2 self-critique (9472 chars)
**Wall time**: 46.6s

---

## Referee Report: Spectrally Unusual Sources at Scale (Paper P3)

**Recommendation:** REJECT

**Justification:** This paper presents a massive multi-survey anomaly catalog but fails to meet the rigorous standards of *Physical Review D* due to fundamental issues with reproducibility, statistical interpretation, and the conflation of methodological artifacts with scientific results. The core anomaly detection pipeline contains irrecoverable provenance failures (specifically for eROSITA and Gaia), the primary cosmological claims (multi-tracer $f_{NL}$ improvement and NANOGrav spectral index) are statistically consistent with zero improvement or null results despite being framed as "forecasts pending follow-up," and the headline scale metrics are misleadingly inflated by including non-science-target spectra and non-comparable survey tiers. The paper relies on "forecasts" that are explicitly de-biased to show no improvement, yet continues to highlight the optimistic central value. Furthermore, the inclusion of a formally quarantined dataset (ACT DR6) in cross-correlation analyses without a native retrain violates the stated Path-C protocol. The combination of irreproducible score axes, unquantified catalog completeness for failing surveys, and the presentation of null results as potential detections renders the work unsuitable for publication in its current form.

---

### Detailed Findings

#### ESSENTIAL (Paper cannot be accepted without these fixes)

**P3-E1: Irreproducible Anomaly Score Axis for eROSITA DR1**
*   **Section/Page:** §III E (eROSITA DR1), Page 10; Table IV caption, Page 11.
*   **Problem:** The paper explicitly states that the production $S_{BigAE}$ score axis for eROSITA is "irreproducible from any committed artifact." A sweep over 16 monotone rescalings and 3 IsolationForest retrains failed to reproduce the production threshold (0.259) or the top-5 scores (Spearman $\rho = -0.10$). The authors admit the axis is "unrecoverable as a matter of provenance" due to an undocumented post-hoc rescaling step.
*   **Impact:** Downstream users cannot perform threshold re-derivation, score-weighted stacking, or re-isolation on the eROSITA tier. The paper claims a "genuine novelty fraction" based on a catalog where the primary selection metric is mathematically lost. This violates the core requirement of reproducibility for a data product.
*   **Required Fix:** The eROSITA tier must be excluded from the headline catalog or re-generated with a fully reproducible score axis. The current "membership list only" framing is insufficient for a paper claiming a multi-survey anomaly detection campaign where score-based analysis is implied.

**P3-E2: Irreproducible Gaia DR3 Preprocessing Specification**
*   **Section/Page:** §II B (Training and Scoring), Page 3; §III G (Gaia DR3), Page 12.
*   **Problem:** The authors state: "the exact 20-feature production preprocessing script for this run was not recovered from any committed backup." The Gaia specification is "lineage-inferred" from a successor run.
*   **Impact:** The Gaia anomaly rankings and rates are "best-available rather than fully reproducible from scratch." For a paper claiming a "largest-scale application" across seven archives, the inability to reproduce the preprocessing for one of the seven archives is a fatal flaw in the methodology.
*   **Required Fix:** The Gaia tier must be excluded from the headline catalog or the preprocessing must be fully recovered and documented.

**P3-E3: Statistical Consistency with Null for Primary Cosmological Claims**
*   **Section/Page:** §V (Cosmological Applications), Pages 16–17; §VII (Conclusions), Page 21.
*   **Problem:** The paper claims the anomaly catalog enables a "2.6–5σ detection of $f_{NL} = -35/8$" with SPHEREx. However, the empirical bias measurement yields $\alpha_{jk} = 0.19 \pm 0.65$, which is "0.29σ from null." The de-biased Fisher forecast returns the single-tracer baseline exactly ($\sigma(f_{NL}) = 8.98$), meaning **no multi-tracer improvement**. The paper explicitly states the "central 9.4% improvement is a noise-driven forecast pending higher-S/N follow-up, not a detection."
*   **Impact:** The authors frame a result consistent with zero improvement as a "forecast" for a future detection, misleadingly implying the current data supports the multi-tracer advantage. The NANOGrav result ($\gamma = 2.567 \pm 0.382$) is "marginally consistent" with the bounce prediction ($\gamma=3.0$ at $+1.13\sigma$) and strongly disfavors the SMBHB reference, but the authors admit the Bayes factor is "decisive only against the idealized circular-orbit SMBHB reference" and not a cosmological detection.
*   **Required Fix:** The cosmological section must be rewritten to explicitly state that the current data shows **no improvement** over the single-tracer baseline and that the SPHEREx forecast is conditional on future calibration, not a projection of current capability. The "2.6–5σ" claim must be removed or qualified as a *future* conditional possibility, not a current result.

**P3-E4: Misleading Scale Metrics and Inclusion of Non-Science Targets**
*   **Section/Page:** Abstract, Page 1; §III A (DESI DR1), Page 6; Table II, Page 7.
*   **Problem:** The headline count of 195,829 DESI anomalies is a "top-1% score-cut of the full 22.5-M-spectrum scan" including ~16 million "filler-tile, sky-fiber, or calibration-exposure spectra." The paper admits that ~98.7% of these anomalies fall on non-science-target spectra. The comparison to the Liang et al. benchmark (2,685 anomalies) is "not like-for-like" because Liang et al. scanned only science targets. The "like-for-like" recount yields 2,468 anomalies, which is **0.9×** the benchmark, not 73×.
*   **Impact:** The claim of being "141× the size of the largest prior single-survey anomaly catalog" is based on a non-comparable denominator (all spectra vs. science targets). This inflates the perceived scale and novelty of the work.
*   **Required Fix:** The headline scale metrics must be recalculated using only the validated science-target subset. The comparison to prior work must be corrected to reflect the 0.9× factor, not the 73× factor. The abstract must not claim "largest-scale" without qualifying the denominator.

**P3-E5: Violation of Path-C Protocol via ACT DR6 Cross-Correlation**
*   **Section/Page:** §IV D (Planck × ACT Cross-Correlation), Page 16; Appendix F, Page 26.
*   **Problem:** The Path-C protocol explicitly forbids retaining a survey that fails both gate criteria (val loss > 0.30 and injection recovery < 50%). ACT DR6 fails both. The authors state: "ACT DR6 is formally quarantined... and contributes zero objects to the 378,280 Path-C unique-object headline." However, §IV D uses the "formally quarantined cross-transfer ACT anomaly set" as the input for the Planck×ACT cross-correlation test.
*   **Impact:** The cross-correlation result is "largely guaranteed by footprint geometry alone" and carries "essentially no discriminating power." Using a quarantined, unvalidated dataset for a scientific analysis violates the stated methodology and introduces unquantified systematic errors.
*   **Required Fix:** The Planck×ACT cross-correlation analysis must be removed entirely, or the ACT dataset must be re-generated with a native retrain that passes the gate criteria. The current analysis is methodologically invalid.

#### MAJOR (Significant revision required)

**P3-M1: Unquantified Catalog Completeness for Failing Surveys**
*   **Section/Page:** §VI C (Limitations), Page 19; §VI D (ii), Page 20.
*   **Problem:** Three surveys (LAMOST, Gaia, eROSITA) fail the 5σ injection-recovery gate. The paper states: "catalog completeness for LAMOST, Gaia, and eROSITA is formally unquantified."
*   **Impact:** The headline catalog includes these surveys, but their completeness is unknown. This makes the "378,280 unique anomalies" figure scientifically ambiguous.
*   **Required Fix:** The completeness of these tiers must be estimated or the tiers must be excluded from the headline count.

**P3-M2: Novelty Fraction Overstatement and Lack of Full-Catalog Extrapolation**
*   **Section/Page:** §IV A (SIMBAD Cross-Match), Page 13; §VII (Conclusions), Page 21.
*   **Problem:** The paper reports a "genuine novelty fraction" of 17.8% for the DESI top-1,000. However, it explicitly states: "no bound exists on the full-catalog extrapolation, which is empirically untested." The 58.8% SIMBAD-unmatched fraction is admitted to "overstate discovery rates."
*   **Impact:** The novelty claim is a single-sample point estimate with no error bounds for the full catalog. The paper presents this as a definitive discovery rate without the necessary caveats.
*   **Required Fix:** The novelty fraction must be presented strictly as a point estimate for the top-1,000 with explicit warnings that it cannot be extrapolated to the full catalog.

**P3-M3: B-Dominant Contamination and Calibration Suspects**
*   **Section/Page:** §VI C (Limitations), Page 19; Table VII, Page 23.
*   **Problem:** 22.7% of DESI anomalies are "B-dominant" and flagged as "calibration-suspect." The paper admits "confirmation via photometric color selection is needed."
*   **Impact:** A significant fraction of the catalog may be instrumental artifacts rather than astrophysical anomalies.
*   **Required Fix:** The B-dominant fraction must be clearly separated or excluded from the "genuine anomaly" count, or the paper must provide the photometric confirmation.

**P3-M4: Unweighted Reconstruction Error and Noise-Driven Residuals**
*   **Section/Page:** §VI C (Limitations), Page 19; Eq. (1), Page 3.
*   **Problem:** The anomaly score uses unweighted per-element MSE. "Low-S/N spectral regions contribute noise-driven residuals on equal footing with high-S/N regions."
*   **Impact:** The score is not optimal in the maximum-likelihood sense, potentially biasing the catalog toward noisy spectra.
*   **Required Fix:** A noise-weighted validation slice must be performed, or the limitation must be more prominently discussed in the context of the catalog's reliability.

#### MINOR (Address but paper can proceed)

**P3-N1: Inconsistent Normalization of Fisher Forecast Baselines**
*   **Section/Page:** §V (b), Page 16; Appendix C, Page 23; Fig. 11, Page 24.
*   **Problem:** The paper uses two different normalizations for the single-tracer baseline: $\sigma(f_{NL})_{std} = 8.98$ in §V and $\sigma(f_{NL}) = 16.85$ in Appendix C/Fig. 11. The authors note they are "not on the same absolute normalization," but this creates confusion for readers.
*   **Required Fix:** Clarify the normalization difference in the text or use a consistent baseline throughout.

**P3-N2: Ambiguous "3 PASS / 3 FAIL" Shorthand**
*   **Section/Page:** §VI D (ii), Page 20; Fig. 10 caption, Page 20.
*   **Problem:** The "3 PASS" shorthand includes the NEOWISE mask test, which "passes by construction" and is a "QA check rather than a detector-sensitivity test."
*   **Required Fix:** Explicitly distinguish between the two sensitivity tests (SDSS, Planck) and the one QA test (NEOWISE) in all summaries.

**P3-N3: Figure 12 Taxonomy Labels**
*   **Section/Page:** Fig. 12, Page 25.
*   **Problem:** The "Cool Dwarf" label in the taxonomy gallery is ambiguous (could be "Cool/Unusual Star").
*   **Required Fix:** Ensure taxonomy labels are precise and consistent with the text definitions.

#### NIT (Cosmetic)

**P3-N4: Date Formatting in Abstract**
*   **Section/Page:** Abstract, Page 1.
*   **Problem:** "Dated: June 2026" is inconsistent with standard journal formatting (usually "Received... Accepted...").
*   **Required Fix:** Use standard date formatting.

**P3-N5: Reference  Year**
*   **Section/Page:** References, Page 27.
*   **Problem:** Reference  is listed as "(2026)" but the arXiv ID is `2506.17372` (June 2025).
*   **Required Fix:** Correct the year to 2025 or verify the publication date.

---

### Summary of Critical Issues for the Authors

1.  **Reproducibility:** You cannot publish a "largest multi-archive anomaly catalog" if the score axes for eROSITA and the preprocessing for Gaia are irreproducible. This is a fatal methodological flaw.
2.  **Statistical Honesty:** Your primary cosmological result (multi-tracer $f_{NL}$) shows **no improvement** over the single-tracer baseline. You must not frame a null result as a "forecast for a 2.6–5σ detection" without explicitly stating the current data supports no improvement.
3.  **Scale Integrity:** Your headline "141×" scale claim is based on a non-comparable denominator (all spectra vs. science targets). The like-for-like comparison is 0.9×. This misrepresents the novelty of your work.
4.  **Protocol Violation:** You used a quarantined dataset (ACT DR6) for a scientific cross-correlation analysis, violating your own Path-C protocol.

**Final Recommendation:** REJECT. The paper requires a complete re-generation of the eROSITA and Gaia tiers, a rewrite of the cosmological section to reflect the null result, and a correction of the scale metrics to use science-target denominators. Even with these fixes, the fundamental issue of irreproducible score axes may preclude publication unless the eROSITA tier is dropped entirely.

---

## PASS 2 — self-critique findings (what initial review missed)

P3-M5: **Table IV caption vs. body mismatch for the eROSITA top-5 list**
- **Section/Page:** Table IV caption, Page 11; §III E, Page 11.
- **Problem:** Table IV is described as the “Top 5 eROSITA anomalies,” but the body of §III E says the released eROSITA selection is a fixed **top-298 membership list** and that the published threshold axis is a membership-only selection product. The table itself prints only ranks 1–5 from that list, yet the surrounding text repeatedly frames the released eROSITA catalog as **n = 298**, not as a score-ranked top-5 sample.
- **Impact:** The table caption can be read as if the paper is presenting a genuine score-ordered top-5 anomaly set on a reproducible axis, when the body explicitly says the score axis is irreproducible and only the membership list is reproducible.
- **Required Fix:** Rephrase the caption to say **“first five entries of the released top-298 membership list”** and explicitly state that the ranking is only by the committed raw artifact, not by a reproducible catalog score axis.

P3-M6: **Table I “Rate (%)” for the total row is not a measured anomaly rate**
- **Section/Page:** Table I, Page 7.
- **Problem:** The total row lists **0.86%** for the cross-transfer baseline and **1.01%** for the Path-C unique row. The footnote later states these are **bookkeeping ratios** mixing fixed-count tiers and fixed-percentile tiers, and are **not measured anomaly frequencies**. The table presents them in the same “Rate (%)” column as the per-survey rates, which are true per-survey rates on their own denominators.
- **Impact:** This is a presentation inconsistency: the total-row percentage is structurally different from the survey-level rates, but the table formatting makes them look comparable.
- **Required Fix:** Split the column into **measured rate** vs. **bookkeeping ratio**, or remove the total-row rate entirely.

P3-M7: **Table I internally mixes cross-transfer counts and Path-C counts without marking the switch in the row labels**
- **Section/Page:** Table I, Page 7; §III, Pages 5–7.
- **Problem:** The table header says **“Summary of the multi-survey anomaly sweep”**, and the per-survey rows under “Nanom” are explicitly said to be **initial cross-transfer scan counts**, while the “Path-C unique (primary)” row below is the **native-retrained** result. That means the same table mixes two different result definitions in one count column without a clear row label distinction.
- **Impact:** Readers can easily misread the table as a single coherent set of counts. It is not: the per-survey lines are before-native-retrain baseline values, while the final row is the post-retrain headline.
- **Required Fix:** Separate the table into **baseline cross-transfer** and **Path-C native** blocks, or label each row explicitly as **cross-transfer** or **native**.

P3-M8: **Figure 3 caption overstates the meaning of the SDSS tail comparison**
- **Section/Page:** Fig. 3 caption, Page 9; §III C, Page 9.
- **Problem:** The caption states that SDSS scores span from the threshold to **\(S = 1.9 \times 10^{11}\)** for extreme-score M7 and T2 dwarfs, and that the native re-score compresses them to **\(S < 14\)**. In the body, however, the same objects are described as **cross-transfer artifacts** and the native re-score is said to apply to the **same objects**, but with a different score scale and a fixed-size continuity slice. The caption makes the compression sound like a direct property of the score distribution, while the body frames it as a consequence of the change in scoring procedure.
- **Impact:** The figure caption can be read as a direct astronomical statement about the population, when the body says it is largely a **model-domain-shift artifact**.
- **Required Fix:** Make the caption say explicitly that the tail collapse is a **cross-transfer-to-native score-axis effect**, not an intrinsic physical distribution change.

P3-M9: **Figure 10 caption counts NEOWISE as a PASS in the headline tally but the body classifies it as QA, not detector sensitivity**
- **Section/Page:** Fig. 10 caption, Page 20; §VI D(ii), Page 20; §III H, Page 12.
- **Problem:** The caption lists NEOWISE mask-geometry as **PASS**, and the body elsewhere says this test **passes by construction** and is a **QA check rather than a detector-sensitivity test**. The same figure is then used to support the “3 PASS / 3 FAIL” summary.
- **Impact:** The headline pass/fail count is heterogeneous: two true sensitivity passes plus one geometry sanity check. Treating all three as the same kind of pass inflates the apparent robustness of the pipeline.
- **Required Fix:** Relabel the summary as **2 sensitivity PASS + 1 QA PASS** and avoid collapsing them into a single pass count.

P3-M10: **Table V caveat (j) appears stale or inconsistent with the main-text Gold+Silver forecast**
- **Section/Page:** Table V, Page 23; §V, Page 17.
- **Problem:** Table V caveat (j) says **“GS corrected: \(\sigma(f_{NL})_{GS} \in [0.94, 8.98]\), central 1.95; prior \(\pm 7.43\) dropped”**. In the main text, the Gold+Silver subsection states **\(\alpha_{GS,jk} = +1.83 \pm 2.03\)** and a **central \(\sigma(f_{NL})_{GS} = 1.95\)** with envelope **[0.94, 8.98]**. The caveat and body are numerically consistent on the central value, but the caveat is isolated as a table note while the main text also refers to this as a **re-measurement on the 1,122-object subset**.
- **Impact:** The reader is forced to reconstruct which result is primary and which is derived. This is especially confusing because the same numerical pair is split across the main text and a caveat note rather than being tied together in one place.
- **Required Fix:** Consolidate the Gold+Silver result in one location and explicitly state that the caveat supersedes the fixed-prior Appendix C values.

P3-M11: **Appendix C/Fig. 11 baseline mismatch can be mistaken for an updated forecast**
- **Section/Page:** Appendix C, Page 24; Fig. 11, Page 24.
- **Problem:** Appendix C gives **\(\sigma(f_{NL})_{std} = 8.98\)** for the main forecast, while Fig. 11 uses an internal single-tracer baseline of **16.85** and a dense-tracer limit of **11.71**. The figure caption says these are on a different normalization, but the appendix body still presents the graph as a “multi-tracer Fisher \(\sigma(f_{NL})\) vs. tracer number density” result.
- **Impact:** Without reading the caption carefully, a reviewer could assume the appendix figure is simply a visualization of the same forecast as the main text, when in fact it is a **different internal normalization** and a different Fisher implementation.
- **Required Fix:** Put a prominent warning in the figure title or legend that Fig. 11 is **not on the §V normalization** and is for relative scaling only.

P3-M12: **Equation (1) is dimensionally underspecified unless the pixel normalization is stated**
- **Section/Page:** Eq. (1), Page 3; Appendix A, Page 23.
- **Problem:** Eq. (1) defines MSE as \(\frac{1}{N}\sum_i (x_i-\hat{x}_i)^2\), but the main text does not specify the units of \(x_i\) until later preprocessing sections. Because the inputs are standardized differently for different surveys, the equation alone is dimensionally ambiguous: the MSE is only unitless after the per-survey normalization is fixed.
- **Impact:** The equation is mathematically correct but not self-contained. A reader cannot infer the physical scale of MSE without the preprocessing context.
- **Required Fix:** State in the equation caption or immediately after Eq. (1) that \(x_i\) are **survey-normalized inputs**, so MSE is computed in standardized feature units.

P3-M13: **Figure 1 caption and body disagree on what the 83 “Exemplar-Set” objects are**
- **Section/Page:** Fig. 1 caption, Page 2; §II A, Page 2.
- **Problem:** The caption says the 83 Exemplar-Set anomalies are a **ranked visual-display sample of the companion high-z tracer pipeline**, force-included in the embedding sample, and “distinct from the 116-object GOLD QSO-candidate confidence tier.” The body later uses the same high-z pipeline language but does not clearly distinguish whether those 83 are part of the anomaly catalog or merely display objects.
- **Impact:** This is a provenance ambiguity: the figure can be mistaken for showing catalog members when it is actually a display-only subset.
- **Required Fix:** State explicitly in the caption that the 83 objects are **display-only and not a catalog tier**.

P3-M14: **Appendix F’s ACT cross-transfer count conflicts in wording with the main-text dedup bookkeeping**
- **Section/Page:** Appendix F, Page 26; Table I, Page 7; §III D, Page 10.
- **Problem:** Appendix F says the ACT scan returned **200 anomalous patches (top 1%)**, and the 8-way-with-ACT variant would produce **388,693 − 10,213 = 378,480 unique objects (+200 relative to the headline)**. Table I footnotes and the main text say ACT contributes **zero positional overlaps** and is excluded from the Path-C headline. The arithmetic itself is consistent, but the phrasing “+200 relative to the headline” is easy to confuse with a scientifically meaningful increment rather than a bookkeeping variant.
- **Impact:** The appendix can be read as though ACT adds a genuine incremental catalog tier, when it is explicitly quarantined and methodological only.
- **Required Fix:** Say **“bookkeeping-only +200 sensitivity variant”** and avoid phrasing that suggests a scientific extension of the headline catalog.

