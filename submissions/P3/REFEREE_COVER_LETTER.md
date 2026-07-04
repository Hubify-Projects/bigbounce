# Cover Letter — Paper 3

**Title area:** A multi-survey autoencoder anomaly catalog across 37.3M sources and CMB map patches
**Source:** `pipelines/p3_anomaly_engine/paper3_draft.tex`
**Suggested venue:** ApJS (catalog venue)

Dear Editor,

Please consider this manuscript. This cover letter states its contribution,
scope, and disclosed limitations plainly.

## Contribution
The paper applies the BigAE autoencoder framework to 37.3 million sources and CMB
map patches across DESI DR1, SDSS DR18, LAMOST DR10, eROSITA DR1, Planck, and
NEOWISE, after per-survey native retraining and 5″ positional deduplication. Its
headline deliverable is a **validated catalog-grade subset of 268,519 unique
anomalies** — the four components that pass (or, for NEOWISE, supply the
geometry-QA analogue of) an injection-recovery / detector-sensitivity gate. The
count is directly recomputable end-to-end from committed per-survey lists. DESI,
which dominates the subset, now carries a real, committed 5σ injection-recovery
test (broad-class recovery 99–100%; a disclosed ≥15σ narrow-line floor) plus a
5-fold CV Jaccard gate and an OOD gate.

## Scope statement
The 268,519 headline is a **process-volume count — the anomaly candidates that
survive the per-survey validation gates across a full-instrument-stream scan —
NOT a count of confirmed physical detections.** The like-for-like,
science-target detection benchmark is separately reported as 2,468 DESI
anomaly clusters (~0.92× the largest published single-survey catalog). The two
must not be conflated, and the abstract states this directly. The paper's §V
cosmological material (multi-tracer f_NL, NANOGrav) is reframed as a
**methodological demonstration with no statistically significant improvement and
no detection claimed** — the multi-tracer central shift lies within the 1σ
envelope of the single-tracer baseline.

## Disclosed limitations (stated up front)
1. **eROSITA score-axis non-reproducibility.** Per-object scores and the 0.259
   production threshold are not recoverable across 16 monotone rescalings.
   eROSITA is sequestered as an exploratory-tier reproducible top-298 membership
   list, contributing zero score-dependent statistics and zero objects to the
   validated headline.
2. **Lost Gaia preprocessing lineage.** The exact 20-feature Gaia script was not
   recovered (lineage-inferred); the prior synthetic Gaia tier was removed
   entirely from all counts. Gaia is excluded from the validated tier.
3. **LAMOST exploratory tier** is a documented 98% blue-excess training-bias
   artifact, retained as a methodological lesson and gate-FAIL, excluded from the
   validated count.

## The judgment for the referee
The crux question LLM referees flag but cannot adjudicate is a **catalog-scope
call**: is a disclosed, sequestered, exploratory-tier score-axis
non-reproducibility (eROSITA) acceptable in a catalog paper whose *released
product is the committed, reproducible validated membership list* — or does a
catalog paper require every tier fully reproducible before publication? The
validated 268,519 subset stands independently of the exploratory tiers; the
exploratory limitations are foregrounded, not hidden. We ask you to weigh whether
the validated tier's reproducibility, with the exploratory tiers truthfully
sequestered by-design, meets the catalog-venue bar.

No genuinely-new correctness defect is outstanding; the previously-absent DESI
injection-recovery is now real and committed.

Sincerely,
Houston Golden (houston@hubify.com)
