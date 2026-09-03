# Anomaly flagship — sample-provenance finding (internal record, 2026-09-03)

**Finding (verified on pod 8ofv5d4ynu7hku, read-only, 2026-09-03 ~15:40Z):**
the phase-3 S>8 sample (`flagship_sample_s8.parquet`, 3,810 rows) has
3,232 rows (84.8%) with negative TARGETID. In `zall-pix-iron.fits` (first
2M rows) TARGETID<0 rows are OBJTYPE=SKY (266,379) or blank (26,186); among
TARGETID>0 rows OBJTYPE is TGT 1,539,191 / SKY 167,511 / BAD 733. So the
autoencoder's high-score tail is dominated by sky fibers, which explains the
SIMBAD/NED match rate (92/3,810) and AllWISE (65). Coordinates and services
were correct. The enrichment carries no Redrock flags (no redrock file), so
nothing downstream could catch it. Reported first by a peer session
(code-you-79); confirmed here.

**What stands:** the sealed scan generation `clean-rerun-6699d09ff886` as
computed (the contract counted rows with anomaly_score>5; that is honest).
**What does not stand as a science claim:** "52,188 anomaly candidates" and
any phase-3 v1 taxonomy/benchmark interpretation. Phase-3 v1 artifacts are
landed and backed up as SAMPLE-V1-CONTAMINATED (provenance value only).

**Correction (in progress, pod kept alive):**
1. Science-target rule from the zcatalog: `OBJTYPE == 'TGT' AND
   COADD_FIBERSTATUS == 0` (TARGETID > 0 as a sanity check), with ZWARN and
   SPECTYPE carried per row for downstream use.
2. Derived, receipted science-target summary of the sealed generation
   (S>3/4/5/6/8/10 counts) recorded BESIDE the sealed summary; nothing sealed
   is overwritten.
3. Science-only S>8 sample (threshold re-chosen from the science-only
   distribution if S>8 is too small) → enrichment → cross-match → WISE →
   taxonomy under `/workspace/phase3_v2/`; backed up three ways; then the
   pod stops.
4. `build_flagship_sample.py` gains a contract-level science-target option
   with tests; linter-style gates check TARGETID sign / OBJTYPE /
   FIBERSTATUS so this cannot recur.
5. Ledger #8 and the manuscript architecture are filled only from the
   corrected run. Directive Q1: this record stays internal; the eventual
   paper/release describes the science-target selection as its method.

## Science-target numbers (v2 stage 01–03, 2026-09-03 16:57Z; `/workspace/phase3_v2/science_target_summary.json`, `sky_fraction_by_score.json`, `threshold_choice.json`)
| threshold | raw rows (all fibers) | science-only (OBJTYPE=TGT, FIBERSTATUS=0) |
|---|---|---|
| S>3 | 320,418 | **1,244** |
| S>4 | 86,053 | 152 |
| S>5 | 52,188 | 44 |
| S>6 | 27,180 | 20 |
| S>8 | 3,810 | 2 |
| S>10 | 337 | 1 |
Sky-or-nonscience fraction by score bin: [3,4) 99.53%; [4,5) 99.68%; [5,6) 99.90%;
[6,8) 99.92%; [8,10) 99.97%; [10,24.4] 99.70% (rows with TARGETID≤0 or not
joining the zcatalog counted as non-science). Pre-declared rule chose
threshold 3 → 1,244 science objects for v2 characterisation (enrichment →
SIMBAD/NED → AllWISE → taxonomy running unattended). Method result for the
eventual validation section: the archived autoencoder's anomaly score is
dominated by sky fibers; among science targets the S>3 tail is 5.7e−5 of
unique TARGETIDs.
