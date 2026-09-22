# DAF-19 corrected re-clustering — report

**Lane:** LAF4-af-reclustering · **Date:** 2026-09-22 · **Disposition addressed:** DAF-19 (paper-af, `project-context/peer-reviews/DISPOSITIONS/AF.md`)

## What was wrong (verified)

`taxonomy_flagship.py`, the generator behind the published `flagship_taxonomy_v2.json`
/ main.tex Table VIII, fed raw `(anomaly_score, ra_deg, dec_deg)` into
`StandardScaler -> PCA -> UMAP -> HDBSCAN`. RA is periodic at 360°; Euclidean
distance on raw degrees treats an object at RA=1° and one at RA=359° as
~358° apart when they are really ~2° apart. The published family 0
(302 objects) has a *naive* RA range of `[1.59°, 354.66°]`, i.e. a 350.4°
span — reproduced directly from `flagship_taxonomy_v2.json` in this run and
matching Table VIII exactly. That is the RA-wrap signature, not real sky
extent. The published run's hyperparameters were also absent from the
manuscript/manifest text (though present in `flagship_taxonomy_v2_manifest.json`
on disk), and PCA on 3 features (`n_components = min(10,3,674) = 3`) never
reduced dimension — confirmed in the script: `if n_features > n_components`
is false, so `reduced = scaled` unchanged.

## The fix

`recluster_spherical.py` (this directory) re-runs the identical
PCA→UMAP→HDBSCAN→kNN-reassignment→descriptor-merge pipeline on the **same
675-object input** (`flagship_crossmatch_v2_unmatched.parquet`, sha256
`c0a6b57bd672f81b1424a65449f99d891810073ea59e600c1fc35cfec30eb7c3`,
verified byte-identical to the published input before running), with three
changes:

1. **Spherical embedding.** Sky position enters as the unit vector
   `(cos(ra)cos(dec), sin(ra)cos(dec), sin(dec))` (radians) instead of raw
   degrees. Euclidean distance between two such vectors is a monotonic
   (chordal) function of the true great-circle separation, so the wrap
   disappears by construction — no object is treated as more distant than
   its true angular separation.
2. **Every hyperparameter and the seed stated**, and *reused verbatim* from
   the published run's own manifest (`pca_components=10, umap_neighbors=15,
   umap_min_dist=0.05, min_cluster_size=15, min_samples=3, random_state=42`)
   so the embedding fix is the only variable that changed between the
   published and corrected taxonomies — isolates its effect instead of
   conflating it with an unrelated hyperparameter change. Confirmed
   deterministic: rerun on the same input reproduced the identical
   23-cluster/9-family result bit-for-bit (`diff` of the metadata block was
   empty).
3. **(survey, programme) baseline.** A trivial partition by each object's
   own `(survey, programme)` pair (7 cells present in the 675-object
   sample) is compared against the corrected family labels via Adjusted
   Rand Index (ARI) and Adjusted Mutual Information (AMI), so the corrected
   taxonomy's structure can be graded against pure selection-driven
   structure, not just eyeballed.

PCA remains non-dimension-reducing with the corrected 4-feature input
(`score, x, y, z`; `n_components = min(10,4,674) = 4`) — reported honestly
in `outputs/reclustering_manifest.json` (`pca_reduced_dimension: false`)
rather than silently carried forward. This is a separate, smaller issue
than the RA wrap and is not claimed as fixed here; PCA is doing nothing on
either the published or the corrected 3–4-feature input, by construction of
having more components requested than features.

## Result: taxonomy vs. published (same 675 objects)

| | published (defective) | corrected (spherical) |
|---|---|---|
| clusters | 25 | 23 |
| families | 8 | 9 |
| largest family | 302 | 308 |
| weighted dominant-`(survey,programme)`-cell purity | 70.4% (Table IX) | 71.9% |
| largest wrap-aware RA span | 350.4° (naive; the wrap artifact) | **331.6°** (true, wrap-aware) |
| smallest family's wrap-aware RA span | (not reported) | 15.4° |

**Adjusted Rand Index vs. published:** 0.603. **Adjusted Mutual Information vs.
published:** 0.626. This is moderate-to-substantial agreement, not
near-1 (same taxonomy) and not near-0 (unrelated partitions): most of the
score-tier × survey/programme structure survives the fix, but specific
cluster and family boundaries move — 2 fewer clusters, 1 more family, and
per-family membership reshuffles at the margins (compare the full
per-family table in `outputs/corrected_family_table.json` against Table
VIII/IX). **No published family is reproduced unchanged**; the largest two
(302→308, 87→81 nearest matches) are recognizable but not identical, and a
new small family (16-object) appears with no exact published counterpart.

**Adjusted Rand Index vs. the (survey, programme) baseline:** 0.257.
**AMI:** 0.256. This is weak-to-moderate, not the ~1.0 a purely
selection-determined taxonomy would show. Read together with the 71.9%
weighted dominant-cell purity, the honest statement is: the corrected
families correlate substantially with survey/programme footprint (as the
paper's own §VI B "What the families are" already argued for the published
taxonomy) but are **not simply a relabeling of the 7 (survey, programme)
cells** — the anomaly-score axis and the corrected sky-position axis both
contribute real partition information beyond selection alone.

**Critically: fixing the RA wrap does NOT make the large families
sky-compact.** The corrected, wrap-aware measurement of the largest
family's true RA span is 331.6° — smaller than the naive published 350.4°,
but still enormous. This means the paper's own downstream conclusion in
"What the families are" (no family is a compact sky region; families are a
score-tier × survey/programme stratification) is **not an artifact of the
wrap bug** — it survives the fix, and is if anything reinforced by a
correctly-measured span table.

## Verdict on DAF-19

**All three named defects are fixed in this artifact:** (a) RA-wrap is
eliminated by construction (spherical embedding); (b) every hyperparameter
and the random seed are stated in `outputs/reclustering_manifest.json`,
reused identically from the published run for a clean isolated comparison;
(c) the (survey, programme) baseline is run and reported. The corrected
re-clustering that DAF-19's disposition named as the exact fix now exists,
is reproducible (rerun verified bit-identical), and is honestly compared
against both the published taxonomy and the selection baseline.

**DAF-19 can move to CLOSED** once the AF lane replaces main.tex §VI A's
limitation paragraph with a result citing this artifact (this lane does not
edit main.tex, SSOT, or site data per its brief — see
`PROPAGATION_NOTE.md`). The substantive finding to report is a **moderate
restructuring**, not a dissolution and not a confirmation of the exact
published numbers: 25→23 clusters, 8→9 families, ARI 0.60 vs. published,
and the non-compact-sky-region conclusion strengthened rather than
undermined. This does not upgrade the V12 latent-space null (already the
weaker `structured-but-weak` reading, unaffected by taxonomy-construction
choices) and does not by itself clear the ledger #8 discovery bar.

## DAF-29 re-check

DAF-29's closure scoped the abstract to claim reproducibility only for the
**catalogue selection** (score, provenance gate, threshold), with a forward
pointer to §VI A's own disclosed "not reproducible from the released files
alone" limitation on the taxonomy. That forward pointer is still accurate
for the taxonomy **as published** (`flagship_taxonomy_v2.json`'s exact
25-cluster/8-family result), which remains a fixed historical fact about
what was released. It stops being the full story only if/when the AF lane
adopts this corrected, hyperparameter-documented pipeline as the taxonomy
going forward — at that point the abstract's forward pointer should be
updated to reference the corrected (now reproducible) taxonomy instead of
an open-ended "not reproducible" caveat, while still being explicit that
the corrected taxonomy differs from the one shown in the current Table
VIII/IX (moderate restructuring, ARI 0.60). DAF-29's abstract wording does
not need to change unless/until that adoption decision is made.

## Files

- `recluster_spherical.py` — the corrected pipeline (self-contained, no
  network access, reuses only local repo artifacts).
- `outputs/flagship_taxonomy_corrected.json` — full corrected taxonomy
  (per-object cluster/family assignment, same schema family as the
  published file).
- `outputs/comparison_metrics.json` — ARI/AMI vs. published and vs.
  baseline.
- `outputs/corrected_family_table.json` — per-family n/descriptor/dominant
  cell/purity/wrap-aware RA span, the corrected analog of Tables VIII/IX.
- `outputs/reclustering_manifest.json` — Q2 reproducibility manifest
  (inputs+sha256, scripts, hyperparameters+seed, versions, compute venue,
  wall-clock).
