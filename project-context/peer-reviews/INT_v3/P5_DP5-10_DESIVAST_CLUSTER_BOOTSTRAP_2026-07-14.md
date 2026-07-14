# P5 DP5-10 compute report — DESIVAST cluster-aware uncertainty

**Date:** 2026-07-14
**Disposition scope:** compute artifact only; manuscript, SSOT, disposition ledger, version, PDFs, and site were intentionally not changed.
**Candidate outcome:** computed null preserved, with a raw-snapshot provenance caveat requiring truth-audit before integration.

## Exact estimand and validation

The script preserves the declared primary sign convention and sample definition:

\[
\Delta f_{\rm CW}=f_{\rm CW}^{\rm non\mbox{-}void,footprint}
-f_{\rm CW}^{\rm void}.
\]

Membership is the exact, k-unbounded point-in-union of all 101,863 DESIVAST
VoidFinder hole spheres. The control is non-void within the NSIDE=64 union of
hole angular discs and the holes' comoving radial span.

The original matched parquet was absent. The script rebuilt the parent from raw
DESI + P4 data using the historical `scripts/03` rule: quality-cut all redshifts,
1.0-arcsec nearest match, global nearest-separation de-duplication per P4 `dr8_id`,
then select CW/CCW at z<=0.24. It aborted unless every released ledger count
matched. All gates passed:

| Gate | Observed | Released reference |
|---|---:|---:|
| DESI quality rows | 16,361,731 | 16,361,731 |
| Matches within 1 arcsec | 2,349,908 | 2,349,908 |
| Global de-duplicated matches | 2,232,212 | 2,232,212 |
| Low-z CW/CCW parent | 678,945 | 678,945 |
| Exact void arm | 57,081 (CW 28,339) | 57,081 (CW 28,339) |
| Footprint non-void arm | 253,276 (CW 126,202) | 253,276 (CW 126,202) |

## Cluster-aware result

Each primary-sample galaxy was assigned to its nearest published DESIVAST
VoidFinder maximal centre in 3-D comoving Mpc/h. This creates one shared,
void-centred Voronoi partition for both arms. Of 3,765 published maximal voids,
3,756 regions contain at least one primary-sample row. The pairs bootstrap
resampled whole regions with replacement (`seed=20260714`, 20,000 replicates).

| Quantity | Result |
|---|---:|
| Point estimate, non-void minus void | +0.00180863 (+0.1809 pp) |
| Cluster-bootstrap SE | 0.00232807 |
| Cluster percentile 95% CI | [-0.00271506, +0.00635387] |
| Independent-binomial SE | 0.00231659 |
| SE ratio, cluster / binomial | 1.00496 |
| Variance design effect | 1.00994 |
| Delete-one-cluster jackknife SE | 0.00232758 |
| Jackknife normal 95% CI | [-0.00275334, +0.00637060] |

The cluster result is effectively identical to the counting-only interval and
preserves the null. This addresses covariance among galaxies sharing a published
maximal-void neighbourhood. It does not address classifier bias, selection-mask
error, void-catalog uncertainty, or correlations spanning multiple regions.

## Historical tie-order sensitivity

Repeat coadds can have exactly tied angular separations. The released parent
inherits pandas' default unstable quicksort ordering. A deterministic stable-first
sort produces 678,923 rows (-22), 57,062 void rows (CW 28,331), and 253,291
footprint non-void rows (CW 126,208). Its point estimate is +0.00177770 and its
cluster SE is 0.00233118, with 95% CI [-0.00273443, +0.00636382]. Relative to the
released rule, the point shifts by -0.00003093 (-0.0031 pp) and the SE by
+0.00000312; the inference is unchanged.

Future releases should version a total deterministic tie order such as
`(sep_arcsec, TARGETID, original_row_index)` and regenerate all dependent
artifacts together. The historical rule is retained here solely to reproduce the
published primary integers.

## Provenance and determinism

Material input SHA-256:

- `data/desi_zall.fits`: `2d95ad99361039b556c402b49e0e7c84df5f00106dc5731d44476a58b128b49b`
- `data/p4_chirality.parquet`: `e8525ba5c98576f6361580e4a0aa7a86929ccc9f79b1423808774cfaaf313563`
- `VoidFinder_NGC.fits`: `c69f2f7b2b1fed4554527475dd96584169b1ead5bbcd0c152164200e6a2f34c8`
- `VoidFinder_SGC.fits`: `47c43b9b446f4bcb47cbc023115ac5297f9afb0045aea96d853649a80d7219c1`
- Canonical reconstructed primary-row scientific hash: `f143419740d6b1e88641cff0e07d2136c204d940d6899ef9d3426b4920567c04`
- Result JSON SHA-256: `352fff9671351f42bea89a1a81386767f8ded1f915aee11179b2f3248fce83c8`

Full raw rebuild runtime was 354.218 s. A cache-backed verification rerun took
45.959 s. The canonical JSON and rerun JSON were byte-identical (`cmp=0`) with
the same SHA-256 above.

**Provenance caveat:** the locally materialized DESI FITS is the current upstream
file (22,371,272,640 bytes; HTTP `Last-Modified: Fri, 10 Jul 2026 21:39:33 GMT`),
but its SHA-256 differs from the May provenance sidecar's recorded raw hash
`50031c9b...`. It nevertheless reproduces every released parent and primary-arm
integer exactly. Because the historical per-row parquet/hash is unavailable,
byte-identical row identity to the May raw snapshot cannot be independently
proved. Treat this as a computed DP5-10 closure candidate with an explicit
snapshot-provenance residual, not as unconditional historical-row attestation.

## Artifacts

- `pipelines/p5_desi_chirality/scripts/35_desivast_cluster_bootstrap.py`
- `pipelines/p5_desi_chirality/outputs/35_desivast_cluster_bootstrap.json`
- Derived local caches (not tracked): `outputs/35_exact_primary_rows_cache.parquet`
  and `outputs/35_stable_tiebreak_primary_rows_cache.parquet`
