# P3 INT-v3-2026-07-03 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p3_anomaly_engine/paper3_draft.pdf` md5=8698c0d0 pages=33
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 110.1s

---

**Referee Report for P3 (Physical Review D)**

**P3-E1** (ESSENTIAL) — Page 1, header block: “(Dated: July 3, 2026)”. A submission dated in the future is unacceptable. Required fix: replace with the actual submission or preprint date.

**P3-E2** (ESSENTIAL) — Throughout (esp. pp. 1–2, 4–7): repeated insertion of literal filesystem paths and internal script names (“pipelines/p3_anomaly_engine/scripts/reproduce_headline_dedup.py”, “pipelines/p3_anomaly_engine/outputs/reproduce_headline_dedup.json”, “artifact pipelines/p3_anomaly_engine/e rosita_scaler_refit.json”, etc.). These are internal-audit artifacts, not journal content. Required fix: remove every such string; replace with a clean reproducibility statement that does not reference private repository layout.

**P3-E3** (ESSENTIAL) — Abstract (p. 1) vs. body (pp. 2, 7): the headline numbers 268,519 / 377,780 are presented as the primary deliverable, yet the text immediately qualifies them as “process-volume count … not a count of confirmed physical detections” and states that the Gaia tier was removed post hoc. The abstract claim is therefore stronger than, and ordered differently from, the body’s final calibrated statement. Required fix: rewrite abstract to match the body’s explicit caveats or remove the numbers from the abstract.

**P3-E4** (ESSENTIAL) — Page 2 and Table I: multiple σ(f_NL) values (8.98, 8.14, 8.58) are juxtaposed without the mandatory qualifier “not directly comparable” at every instance. Required fix: insert the explicit non-comparability statement wherever any two null-procedure sigmas appear side-by-side.

**P3-E5** (ESSENTIAL) — Page 1 and §II: the argument is not self-contained. The reader is repeatedly referred to “the companion data repository,” “§III F,” “Table V caveat (b),” and unreleased JSON files for load-bearing numbers (injection-recovery fractions, Jaccard overlaps, scalers). Standalone-reader test fails. Required fix: move all essential numerical results and definitions into the main text or withdraw the paper.

**P3-M1** (MAJOR) — Page 1, abstract: “largest application of autoencoder anomaly detection by total sources processed in a single multi-archive framework.” No literature comparison or citation supports the superlative. Required fix: either delete the claim or supply a quantitative comparison to all prior works (Baron & Poznanski 2017, Liang et al. 2023, etc.) with page counts and source totals.

**P3-M2** (MAJOR) — Figure 1 (p. 4) and caption: the 83 “Exemplar-Set anomalies” are over-plotted on a UMAP trained on a 500 k stratified sample that already includes them (“force-included”). This is not an unbiased density test. Required fix: either remove the claim that the embedding is unbiased or show a control embedding with the 83 objects withheld.

**P3-M3** (MAJOR) — Table I (p. 9): the “Rate (%)” column mixes fundamentally different selection functions (fixed S > 5 for DESI, 99th-percentile slice for LAMOST, top-298 membership list for eROSITA). No effect-size or practical-significance statement accompanies any rate. Required fix: add Cramér’s V or equivalent for every quoted rate and state that rates are not comparable across rows.

**P3-M4** (MAJOR) — Page 2: “no statistically significant improvement on f_NL bounds is claimed.” The 9.4 % shift (8.98 → 8.14) lies inside the 1σ envelope, yet the paper still reports both numbers prominently. This is an unsupported quantitative claim of robustness. Required fix: remove the numerical comparison or supply the explicit test statistic and p-value.

**P3-N1** (MINOR) — Page 1: “37.3 Million Sources” in the title does not match any single number in Table I (the sum of the N_total column is 37.292 M). Required fix: reconcile or qualify the title.

**P3-N2** (MINOR) — Multiple instances of duplicated or near-duplicated phrasing (“canonical canonical-mask”, “the the”) and inconsistent capitalization of survey names. Required fix: copy-edit.

**P3-NIT1** (NIT) — Page 3: equation (1) is the standard MSE; the subsequent statement that “each input element x_i contributes equally regardless of its per-feature noise variance” is true only because the loss is unweighted. This is obvious and adds no information.

**Summary recommendation: REJECT**

The manuscript is an internal data-release note that has not been rewritten for journal standards. It contains a future date, dozens of private filesystem paths, non-self-contained numerical claims, an abstract that overstates the body’s calibrated results, and superlative novelty assertions without supporting citations. These are not cosmetic issues; they violate PRD’s requirements for a self-contained, rigorously audited methods paper. The work would need a complete rewrite (removal of all internal artifacts, proper literature comparison, self-contained numerical results, and an abstract that matches the final body text) before it could be considered.