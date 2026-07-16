# P1B C10 in-flight source provenance — 2026-07-16

Status: **OPEN — must be bound into the merged production receipt**

Three non-purification C10 processes (`apod_fwhm_0p5`,
`apod_fwhm_3p0`, and `mask_b30`) started at 2026-07-16 04:22:28 PDT while
repository `HEAD` was commit
`201f8ef69d2487ab5b109ec486d10f1b97319ad8`. The purification fix
`f2564cf4716e906f7b1b0521b0d79b0880aa576d` was committed at 04:29:55 PDT,
after those Python processes had imported their modules.

The current C10 `code_sha256()` implementation rereads source files from disk
when it writes a checkpoint or final receipt. Consequently, the fingerprint
`113c7db73201f673fbfbe8b234f4c411b935c8ee938915fe89b75ec515baee1c`
in the in-flight checkpoint receipts identifies the post-start disk state, not
the bytes loaded by the running interpreter. It must not be represented as a
process-start source fingerprint.

The source difference between the start commit and the purification fix is
restricted to:

1. importing `field_harmonic_kwargs`;
2. replacing the explicit non-purified `lmax=LMAX` argument with a helper that
   returns the identical `{"lmax": LMAX}` mapping when `purify_b=False`; and
3. adding `lmax_mask=LMAX` only when `purify_b=True`.

Therefore the three active non-purification numerical paths are source-level
equivalent across the change, but their final automatically written
`code_sha256` metadata is temporally inaccurate and requires an explicit
corrective provenance record. No purification result from the failed pre-fix
attempt is valid.

Before starting the corrected purification run:

- cache the source fingerprint once at process import/start;
- use that immutable value in checkpoint and final receipts;
- add a regression proving disk edits after import do not change the recorded
  producing-code fingerprint.

Before merging:

- preserve the original shard receipts;
- add a correction receipt binding process start time, start commit, changed
  source diff, non-purification equivalence, and original result hashes;
- make the merger require either an immutable start fingerprint or this narrow
  correction receipt;
- never silently rewrite or relabel the original receipts.
