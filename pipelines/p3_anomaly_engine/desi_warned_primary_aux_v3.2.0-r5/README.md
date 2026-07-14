# P3 v3.2.0-r5 warned-primary auxiliary product

> **SECONDARY / WARNING-BEARING / NOT THE PRIMARY CATALOG / NOT PHYSICALLY VALIDATED**

This product contains exactly **2,267** public DESI DR1 global-primary rows that pass the
declared main-survey science-bit and one-arcsecond positional join but have nonzero `ZWARN`.
They are excluded from the 181-row warning-free primary catalog. Publishing this list does
not weaken that gate, establish that any spectrum is physically anomalous, measure purity,
or quantify model/selection efficiency.

The table `desi_dr1_warned_global_primary_aux_v3.2.0-r5.parquet` carries stable `P3-DESI-WARNED-*` IDs, all primary-product DESI and
historical-lineage fields, the exact integer/hex warning mask, and decoded set bits. The only
observed masks are 2, 4, 6, 2048, 2050, 2052, and 2054, composed of DESI Redrock bits 1
(`LITTLE_COVERAGE`), 2 (`SMALL_DELTA_CHI2`), and 11 (`POORDATA`).

Reproduction uses the 143 exact checkpoint parts created by the clean 28,425,963-row DESI
DR1 replay, plus immutable historical inputs at Hugging Face commit `cdaaa03a72c69d86f011be128d93f261dc5b39a8`.
Run the bundled validator with the same checkpoint and historical inputs; it independently
reselects the rows and requires exact key and carried-source-field equality.

The upstream BigAE production normalization/resampling and physical-feature sensitivity are
not recoverable from these rows. `original_score` is frozen canonical-S ranking metadata only.
