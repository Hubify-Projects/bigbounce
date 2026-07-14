# P3 v3.2.0-r4 closure evidence

The clean replay rebuilt the 181-row catalog from immutable historical inputs and the
22.37 GB public DESI DR1 FITS in a fresh temporary directory. The validator was deliberately
invoked without `--parts-dir`; it derived the adjacent 143-part checkpoint and passed the
full FITS checksum, eight live byte-range comparisons, source-field equality, strict-ID-set
equality, direct all-neighbor geometry, and exact ZWARN-mask accounting.

The machine-readable result is `clean_replay.json`. The public AAS digital-asset DOI is
intentionally `null`: journal assignment has not occurred. This closure evidence is additive
to the immutable public r2 data snapshot; it does not claim that the r4 manuscript or validator
patches are already present at the older public snapshot commit.
