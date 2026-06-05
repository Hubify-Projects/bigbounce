# P3 2026-06-04_R4fixed — Brutal-honesty journal referee (treating this as a real PRD submission)

**Model**: `grok-4.3`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 15.1s

---

**Referee Report for P3 (2026-06-04_R4fixed)**

**Paper length**: 49 pages. PRD methods/catalog papers are typically 15–30 pages. The claimed contribution (a multi-survey anomaly catalog with native retraining and basic validation) does not justify the length. Recommended maximum: 25 pages after removal of all internal-audit prose, deferral language, and redundant hedging.

**Abstract vs. body mismatch (ESSENTIAL)**: The abstract claims the “largest-scale application … to date,” “first multi-survey anomaly detection campaign,” and a “genuine novelty fraction of ∼17.8%.” The body clarifies that 17.8% is a single-sample point estimate measured only on the top-1,000 DESI anomalies against 20 catalogs; the full-catalog rate is “empirically untested.” The 141× size claim is an aggregate (six-survey + Path-C expansion) versus a single-survey EDR baseline, not a like-for-like methodology comparison. The abstract must be rewritten to state exactly what the body proves.

**σ(fNL) values presented on inconsistent scales (ESSENTIAL)**: Multiple central values and intervals appear (fiducial α = 0.15 → σ(fNL) = 8.43; empirical αjk = 0.19 ± 0.65 → σ(fNL) = 8.14 with positivity-respecting envelope [3.92, 8.98]; linear-extrapolation 8.27 ± 2.37 superseded; Gold+Silver subset 1.95 with envelope [0.94, 8.98]). These are not on the same scale and are not qualified as such. The paper must either (a) adopt one canonical estimator with a single, explicitly labeled interval or (b) tabulate every variant with a clear statement that they are not directly comparable.

**Pervasive internal-audit / review-log / version-history language (ESSENTIAL)**: The manuscript contains dozens of instances of “Path-C,” “§VI D caveat (i),” “companion artifact,” “deferred,” “queued,” “supersedes,” “before/after diagnostic,” “gate PASS/FAIL,” “load-bearing headline,” and explicit references to prior rounds or companion files. All such language must be removed; the paper must read as a finished journal article.

**Duplicate or near-duplicate phrases**: Multiple near-verbatim repetitions of the 378,080 / 200 / 378,280 stratification, the LAMOST 98% blue-excess explanation, and the α measurement appear in the abstract, §I, §V, and §VII. These must be consolidated.

**Over-claim of novelty and “first” status (MAJOR)**: The work extends single-survey autoencoder searches (Baron & Poznanski 2017; Liang et al. 2023; Nicolaou et al. 2026). The multi-survey aspect and native-retrain protocol are incremental; the framing “first multi-survey … at combined scale exceeding 37.3 million” is not supported by a systematic literature comparison.

**Injection-recovery gates and cross-validation diagnostics (MAJOR)**: Six surveys are evaluated with two distinct metrics (5σ recovery rate ≥ 50% vs. XV-stability). Three pass the formal gate; three fail but are retained with “informative diagnostics.” The paper must either enforce a uniform gate or clearly state that the published catalog mixes objects that pass a detection-sensitivity threshold with objects that do not.

**LAMOST exploratory-tier status (MAJOR)**: The ∼113,000 LAMOST objects are retained in the headline aggregate but explicitly labeled unsuitable for SIMBAD/NED cross-matching or fNL tracer selection without reclassification. This distinction must appear in the abstract and in every table/figure that quotes the 378,280 number.

**Spatial uniformity and selection-function caveats (MINOR)**: The χ² = 143,936 non-uniformity test is dominated by inhomogeneous footprints; the paper acknowledges this but still presents the statistic. The claim of “no correlation with Galactic latitude or dust” is necessary but not sufficient without per-survey selection-function modeling.

**NITs**:
- P3-N1: Table I caption contains three separate threshold policies without a single consolidated footnote.
- P3-N2: Figure 5 panel labels use legacy “AE” notation for rZ; this must be explained once in the caption.
- P3-N3: References to “Hubify-Projects/bigbounce” GitHub repository appear before the data-availability statement.

**Summary recommendation**: REJECT

The manuscript cannot be accepted in its present form. It is 1.6–3× longer than PRD norms for the contribution, contains pervasive internal-audit language that must be stripped, presents σ(fNL) values on un-qualified inconsistent scales (an explicit ESSENTIAL violation), and has an abstract that does not accurately summarize what the body proves. Even after removal of internal prose, the remaining scientific increment (native-retrain protocol + 7-way deduplication on already-public surveys) is modest relative to the claimed framing. A substantially shortened (≤25 pp), cleaned version that adopts a single canonical fNL estimator, states all limitations in the abstract, and removes every “Path-C,” “§VI D caveat,” and “companion artifact” reference could be reconsidered as a Major Revision, but the current submission does not meet journal standards.