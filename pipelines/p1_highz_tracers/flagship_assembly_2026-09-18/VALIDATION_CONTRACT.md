# Validation contract — DESI DR1 anomaly-score candidate catalogue (v2)

**What this is.** A catalogue release is only as good as the checks it can be
held to. This contract lists, one row per requirement, everything the release
must satisfy for its claims to stand, in a form a third party can re-run
against the published artifacts. Every row is machine-checkable; the checker
is `scripts/assemble_flagship_evidence.py` in this directory, its raw output
is `outputs/validation_contract_results.json`, and the rendered outcome table
is reproduced below.

**Status vocabulary.** `PASS`/`FAIL` — the requirement is met or not met.
`REPORTED` — a quantity the release must state, not a threshold it must clear.
`STRUCTURED-BUT-WEAK` — a test with a pre-declared null that the data clear
statistically but not materially; the weaker reading is the one that goes in
the paper.

## The requirements

**Provenance and binding.**
- **V1** The committed provenance gate exits 0 on the released tables.
- **V2** Every released artifact re-hashes to the SHA-256 in the landing
  receipt.
- **V3** The manifest chain closes end to end — sample $\to$ enrichment
  $\to$ cross-match $\to$ taxonomy — each stage binding the exact hash of its
  input and output under one run contract, with model, inference-code and
  zcatalog hashes recorded.
- **V3b** The enrichment stage's own MSE reproduction cross-check passed for
  every released row.

**Selection.**
- **V4** Replaying the pre-declared threshold rule on the science-target
  counts reproduces the released threshold and sample size.
- **V7** Every released object exceeds the stated score threshold.
- **V9** The released sky-fraction-by-score curve supports the stated claim
  that the provenance gate, not the score cut, is what makes the sample
  astrophysical.

**Internal consistency.**
- **V5** The cross-match output partitions the sample exactly: matched plus
  unmatched equals the sample, disjoint, no duplicate `TARGETID`s, enriched
  table covering the same identifiers.
- **V6** The taxonomy covers exactly the SIMBAD/NED-unmatched subset, 25
  clusters roll into 8 families, and the per-family counts agree with the
  per-object labels.
- **V8** The AllWISE table covers every released object and its match count
  equals the released figure.

**Is the score measuring anything?** (computed for this assembly, not
inherited)
- **V10** Within the science-target sample the anomaly score must not be a
  restatement of exposure quality or source brightness:
  $|\rho_{\rm Spearman}| < 0.2$ against median coadd S/N, coadd exposure
  time, `TSNR2_LRG`, `TSNR2_QSO` and $r$-band flux.
- **V11** The per-band residual decomposition identifies which camera arm
  drives the score (reported, not gated).
- **V12** The taxonomy's family partition is tested for structure in the
  128-dimensional latent space it was *not* built from — silhouette against a
  50-draw label-permutation null.

**Known defects the release must carry openly.**
- **DEFECT-1** The enriched table's `z`, `zwarn`, `spectype`, `subtype`
  columns are populated.
- **DEFECT-2** Every derived residual-diagnostic column carries values.
- **DEFECT-3** The reliable-redshift fraction is stated with the catalogue.

## Outcome (re-run 2026-09-18)

| ID | Requirement | Status | Observed |
|---|---|---|---|
| V1 | gates/check_sample_provenance.py exits 0 on the released sample tables (TARGETID > 0; OBJTYPE/FIBERSTATUS where carried) | **PASS** | flagship_sample_v2.parquet: rc=0 OK: {'sample': '/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3_v2/flagship_sample_v2.parquet', 'row_count': 1244, 'checked_objtype': False, 'checked_fiberstatus': False, 'status': 'clean'}; flagship_sample_v2_enriched.parquet: rc=0 OK: {'sample': '/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3_v2/flagship_sample_v2_enriched.parquet', 'row_count': 1244, 'checked_objtype': False, 'checked_fiberstatus': False, 'status': 'clean'} |
| V2 | every released artifact's SHA-256 equals the value in the landing receipt (PHASE3_V2_LANDING_2026-09-03.md) | **PASS** | 9/9 artifacts match |
| V3 | the manifest chain closes end to end: sample -> enrichment -> cross-match -> taxonomy, each stage binding the exact SHA-256 of its input and output, under one run contract, with the model / inference-code / zcatalog hashes recorded | **PASS** | 8/8 links verified; contract=6699d09ff886…, model=f5266ba48f47…, zcatalog=2d95ad993610… |
| V3b | the enrichment stage's own MSE reproduction cross-check passed for every released row | **PASS** | offenders=0 / rows_checked=1244 at relative tolerance 1e-06; enrichment groups completed 752/752, skipped 0 |
| V4 | replaying the pre-declared threshold rule (largest grid point with science-only count >= 300, step up if > 1,500) on the science-target counts selects the released threshold | **PASS** | rule selects S>3 with n=1244; released sample n=1244 |
| V5 | the cross-match output partitions the sample exactly: matched + unmatched = sample, disjoint, no duplicate TARGETIDs, and the enriched table covers the same TARGETIDs | **PASS** | matched=569, unmatched=675, sample=1244 unique of 1244 rows, enriched covers 1244/1244, overlap matched∩unmatched=0 |
| V6 | the taxonomy covers exactly the SIMBAD/NED-unmatched subset; 25 clusters roll up into 8 families; per-family counts sum to the unmatched count and match the per-object labels | **PASS** | objects=675 (unmatched=675), clusters=25, families=8, sum(family sizes)=675, per-object rollup identical: True |
| V7 | every released object exceeds the stated score threshold (S > 3) | **PASS** | min anomaly_score = 3.0002, max = 11.3316 |
| V8 | the AllWISE table covers every released object and its match count equals the released figure (74) | **PASS** | rows=1244, matched=74, median W1-W2 (matched) = 0.508 |
| V9 | the released sky-fraction-by-score validation supports the stated claim that every score bin above 3 is > 99.5% sky-or-nonscience before the provenance gate | **PASS** | 6 score bins, min sky-or-nonscience fraction = 0.99534 |
| V10 | within the science-target sample the anomaly score is not a restatement of exposure quality or source brightness (|Spearman rho| < 0.2 against S/N, exposure time, TSNR2 and r-band flux) | **PASS** | median coadd S/N: rho=+0.058 (p=0.039); coadd exposure time: rho=-0.076 (p=0.0072); TSNR2_LRG: rho=-0.093 (p=0.00098); TSNR2_QSO: rho=-0.096 (p=0.00067); r-band flux: rho=-0.016 (p=0.56) |
| V11 | the per-band residual decomposition identifies which camera arm drives the score (reported, not gated) | **REPORTED** | rB: rho=+0.527 (p=1.1e-89); rR: rho=-0.037 (p=0.19); rZ: rho=-0.142 (p=5.3e-07) |
| V12 | the released taxonomy's family partition is tested for structure in the 128-dimensional latent space it was NOT built from (silhouette vs a label-permutation null, 50 draws) | **STRUCTURED-BUT-WEAK** | silhouette = -0.0162; permutation null mean = -0.0244 (sd 0.0039); empirical p = 0.000. The partition is separable from a random relabelling, but the absolute silhouette is negative: the families are not latent-space-separated clusters and must be reported as descriptive groupings only |
| DEFECT-1 | the enriched table's zcatalog columns (z, zwarn, spectype, subtype) are populated | **FAIL** | unpopulated in flagship_sample_v2_enriched.parquet: ['z', 'zwarn', 'spectype', 'subtype']; authoritative values are present in flagship_sample_v2.parquet (z range -0.0031..6.7457, SPECTYPE {'GALAXY': 1153, 'QSO': 86, 'STAR': 5}); repair table emitted as outputs/flagship_sample_v2_zcat_rejoin.parquet |
| DEFECT-2 | every derived residual-diagnostic column in the enriched table carries values | **FAIL** | all-null columns: ['residual_kurtosis'] |
| DEFECT-3 | the fraction of released objects carrying a DESI-reliable redshift (ZWARN == 0) is stated with the catalogue | **REPORTED** | ZWARN == 0: 502/1244 (40.4%); ZWARN == 4 (SMALL_DELTA_CHI2): 742 |

## Reading of the three material results

**The score is not an exposure-quality proxy (V10).** Within the
science-target sample the anomaly score is essentially uncorrelated with every
available measure of how well the spectrum was measured: median coadd S/N
$\rho_s = +0.058$, coadd exposure time $-0.076$, `TSNR2_LRG` $-0.093$,
`TSNR2_QSO` $-0.096$, $r$-band flux $-0.016$. Several of those are formally
significant at $n=1{,}244$ and all are negligible in size. The honest
statement is therefore *negative and useful*: the $S>3$ tail is not explained
by faintness or short exposure. It is not evidence that the tail is
astrophysically interesting — only that the obvious instrumental explanation
does not account for it. Note the sign: the two significant correlations are
*negative*, i.e. if anything, longer exposures score slightly lower.

**The score is driven by the blue arm (V11).** The per-band residual
decomposition gives $\rho_s(S, r_B) = +0.527$ ($p \sim 10^{-89}$) against
$-0.037$ for $r_R$ and $-0.142$ for $r_Z$. Whatever the model is responding
to lives in the $b$ camera. This is a concrete, falsifiable handle for the
next generation of the model and the single most useful methodological result
in this assembly.

**The taxonomy is descriptive, and the latent space says so (V12).** The
8-family partition was built from $(S, \alpha, \delta)$ only. Tested in the
128-dimensional latent space, its silhouette is $-0.0162$ against a
permutation-null mean of $-0.0244$ (sd $0.0039$, empirical $p < 0.02$): the
partition is distinguishable from a random relabelling, but its absolute
silhouette is negative, so the families are **not** separated clusters in the
space the model actually encodes spectra into. The families must be reported
as descriptive groupings of the candidate list, never as physical classes —
which is what the release already does, now with a test behind it rather than
a caveat.

## Defects and their remediation

- **DEFECT-1 (FAIL).** `z`, `zwarn`, `spectype`, `subtype` are unpopulated in
  `flagship_sample_v2_enriched.parquet` (`z` all-null, `zwarn` all $-1$,
  `spectype`/`subtype` empty strings). The authoritative values are present in
  `flagship_sample_v2.parquet` and were re-joined on `TARGETID` for every
  number in this assembly. A repair table is emitted as
  `outputs/flagship_sample_v2_zcat_rejoin.parquet` (1,244 rows: `targetid`,
  `z`, `zwarn`, `spectype`, `deltachi2`). **The public release must ship the
  joined table, not the current enriched file**, or downstream users will read
  1,244 null redshifts.
- **DEFECT-2 (FAIL).** `residual_kurtosis` is all-null. It is not used by any
  result here; either populate it or drop the column from the published
  schema.
- **DEFECT-3 (REPORTED).** 502/1,244 (40.4%) carry `ZWARN == 0`; 742 carry
  `ZWARN == 4` (`SMALL_DELTA_CHI2`). Every redshift-dependent statement in the
  manuscript and in the follow-up set is restricted to the `ZWARN == 0`
  subset.
- **Open gate gap** (from `SELECTED_SAMPLE_DEFENSE.md`): the released tables
  do not carry `objtype`/`coadd_fiberstatus`, so the provenance gate cannot
  re-verify those two conditions from the published file alone. Carry both
  columns in the public release.

## Not in this contract

No requirement here establishes completeness, purity, or a selection function
for the catalogue. Those need an injection-recovery experiment with the exact
model and substrate named, which has not been run for this generation; it is
listed as open test OT-1 in `FOLLOWUP_TARGET_SET.md` and is the gate any
population-level claim would have to pass first.
