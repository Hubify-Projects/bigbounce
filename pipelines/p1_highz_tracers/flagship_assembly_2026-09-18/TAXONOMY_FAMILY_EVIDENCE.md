# Taxonomy and per-family evidence — 8 families, 25 clusters

The 675 objects of the released sample with no SIMBAD or NED counterpart are
grouped by the release's unsupervised taxonomy: PCA $\to$ UMAP(2) $\to$
HDBSCAN on $(S, \alpha, \delta)$, with kNN noise reassignment, giving 25
clusters that roll up by descriptor identity into 8 families
(`flagship_taxonomy_v2.json`, `min_cluster_size=15`, `min_samples=3`,
`random_state=42`). Family sizes sum to 675 exactly (check V6).

**What the families are.** A family is a *score tier* $\times$ *dominant
survey/programme* grouping of the unmatched candidates. That is what the
clustering features can express and it is what the descriptors say. 70.4% of
objects sit in their own family's dominant survey/programme cell, and no
family is a compact sky region — the smallest family still spans $52^\circ$
in right ascension. Families are therefore **descriptive strata of the
candidate list, not physical classes**, and the latent-space test (V12,
silhouette $-0.016$ vs a permutation null of $-0.024$) gives that statement
a measurement rather than a caveat.

## Per-family evidence

Every column below is computed from the released artifacts by
`scripts/assemble_flagship_evidence.py`; redshift columns use the `ZWARN == 0`
subset only, and the values are re-joined from `flagship_sample_v2.parquet`
because the enriched table's redshift columns are unpopulated (DEFECT-1).

| Family | Tier | $N$ | Clusters | Survey/program | Score median (5–95%) | $r_B$ median | ZWARN$=0$ | median $z$ (ZWARN$=0$) | $z>2$ | $z>4$ | QSO | point src | AllWISE | $W1-W2>0.8$ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | low | 302 | 12 | main/dark | 3.14 (3.02–3.38) | 2.42 | 144 (48%) | 1.15 | 13 | 3 | 18 | 48% | 0 | 0 |
| 1 | elevated | 87 | 4 | main/dark | 3.35 (3.12–3.78) | 2.53 | 47 (54%) | 1.20 | 8 | 0 | 10 | 53% | 1 | 0 |
| 2 | elevated | 71 | 2 | sv3/bright | 3.53 (3.35–4.06) | 2.60 | 18 (25%) | 1.36 | 2 | 0 | 4 | 25% | 2 | 0 |
| 3 | extreme | 61 | 1 | sv3/bright | 4.38 (3.55–6.31) | 2.98 | 19 (31%) | 1.19 | 1 | 0 | 2 | 18% | 1 | 0 |
| 4 | low | 44 | 2 | sv3/bright | 3.10 (3.01–3.23) | 2.42 | 12 (27%) | 1.36 | 3 | 1 | 3 | 16% | 1 | 0 |
| 5 | low | 38 | 2 | sv1/other | 3.12 (3.01–3.28) | 2.20 | 15 (39%) | 1.01 | 2 | 0 | 4 | 16% | 1 | 1 |
| 6 | high | 36 | 1 | main/dark | 3.62 (3.44–4.31) | 2.81 | 27 (75%) | 1.09 | 0 | 0 | 1 | 39% | 0 | 0 |
| 7 | high | 36 | 1 | sv3/bright | 3.66 (3.37–4.01) | 2.66 | 7 (19%) | 0.93 | 0 | 0 | 0 | 31% | 0 | 0 |

Totals: N = 675 objects in 25 clusters; ZWARN$=0$: 289; QSO: 42; AllWISE matches: 6.

Sky extent and survey purity (same source, `family_evidence.csv`):

| Family | dominant survey/programme share | R.A. span (deg) | Dec. span (deg) |
|---|---|---|---|
| 0 | 78.5% | 350.4 | 94.7 |
| 1 | 85.1% | 260.7 | 81.2 |
| 2 | 46.5% | 89.8 | 67.3 |
| 3 | 50.8% | 147.1 | 58.9 |
| 4 | 65.9% | 75.9 | 40.5 |
| 5 | 68.4% | 72.4 | 14.8 |
| 6 | 75.0% | 51.7 | 23.3 |
| 7 | 50.0% | 114.7 | 22.8 |

## What each family actually contains

- **Family 0** (302, low tier, main/dark) — the bulk of the unmatched
  candidates and the most useful one: 144 objects (48%) carry a reliable
  redshift, 18 are pipeline QSOs, 13 sit at $z>2$ and 3 at $z>4$. It spans
  the whole footprint. It is a low-score family, so its members are the
  *least* unusual objects in the list; its value is as the comparison
  population for the higher tiers.
- **Family 1** (87, elevated, main/dark) — the highest reliable-redshift
  yield of the large families after 0 (54%), 10 pipeline QSOs, 8 at $z>2$.
- **Family 2** (71, elevated, sv3/bright) — only 25% reliable redshifts;
  a bright-programme family whose redshifts are mostly not usable.
- **Family 3** (61, **extreme tier**, sv3/bright, single cluster 9) — the
  highest-score family in the catalogue (median $S=4.38$, 95th percentile
  6.31, and the highest-scoring unmatched object in the catalogue, $S=7.15$).
  Its median blue
  residual $r_B=2.98$ is the largest of any family, consistent with the
  global finding that the score is driven by the $b$ camera (V11). 19
  objects (31%) carry a reliable redshift. **This is the family a follow-up
  programme should start with**, and three of the five FT-C targets come
  from it.
- **Family 4** (44, low, sv3/bright) — low scores, 27% reliable redshifts,
  one $z>4$ object.
- **Family 5** (38, low, sv1/other) — the only family containing an
  infrared-excess AGN candidate ($W1-W2 = 0.822$, the FT-B target).
- **Family 6** (36, high, main/dark, single cluster 8) — the cleanest family
  spectroscopically: 27/36 (75%) carry `ZWARN == 0`, by far the highest
  reliable-redshift fraction, at an elevated median score of 3.62 and no
  object above $z=2$. Low-redshift, well-measured, high-score: the family
  where an instrumental or template explanation is most easily testable.
- **Family 7** (36, high, sv3/bright, single cluster 11) — the mirror of
  family 6: the same score tier with the *worst* redshift reliability (19%),
  no QSO and no AllWISE match. Any follow-up here starts with re-reduction,
  not with physics.

## Honest limits of this taxonomy

1. The clustering features are $(S, \alpha, \delta)$. Sky position enters
   only as a proxy for survey/programme footprint, so the families partly
   encode DESI's observing strategy rather than the objects.
2. The partition has no material separation in the model's own 128-dimensional
   latent space (V12). A taxonomy built *on the latents* is the obvious next
   version and is listed as open test OT-2.
3. AllWISE coverage of the unmatched subset is 6/675 — mid-infrared colours
   cannot discriminate between these families at all. The 74 AllWISE matches
   in the full sample sit overwhelmingly in the SIMBAD/NED-matched half,
   which is expected: catalogued objects are catalogued because they are
   detectable elsewhere.
4. The three highest-scoring objects in the full sample ($S = 11.33$, $8.01$,
   $7.80$) are all SIMBAD/NED-**matched** and therefore absent from the
   taxonomy entirely. The score's most extreme responses are to objects that
   are already catalogued — a mild positive signal for the method and a
   reminder that the unmatched subset is not the interesting tail by
   construction.
5. No family is claimed to be astrophysically homogeneous, and no family is
   given a physical name (release labelling policy: descriptors only).
