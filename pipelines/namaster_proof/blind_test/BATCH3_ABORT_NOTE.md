# Batch 3, attempt 1 — ABORTED (invalid harness), recorded not deleted

**Status: INVALID. Never unsealed. No verdict, no scorecard, no claim.**

Attempt 1 was sealed (`assignment_sha256`
`8b4fa8404d4ee0d7bb1276d376353ac045dbf16b05c8a8622141d46d4d6ed554`, commit
`b19b72fc`), executed (48 runs), and blind-verified. Its artifacts are kept under
`public3_aborted/` and its sealed key is retained; the assignment was **not
revealed and not inspected** before the abort decision, and the abort was
diagnosed entirely from the public verdict file plus the source.

## The defect

`pcl.make_map(nside, lmax, seed)` **ignores its `seed` argument**: it calls
`healpy.synfast`, which draws from the global NumPy RNG. Demonstrated directly —
two calls with the same seed return different maps; two calls bracketed by
`np.random.seed(s)` return identical maps.

Batches 1 and 2 were unaffected in substance, because no rule there depended on
reproducing a map: every intermediate they compared was measured *inside* the run.
But it does mean the sealed `map_seed` never actually selected the map, and the
batch-2 phrase "seed-varied executions of one deterministic variant" is loose —
the replicate maps were fresh random draws, which if anything makes the replicates
*more* independent, not less. That correction is carried into the batch-3 report.

Attempt 1's new instrumentation is where the defect became fatal.
`variants3.pseudo_spectrum` recomputed the pseudo-spectrum by re-simulating the
map, so the declared `intermediates.pseudo_cl` belonged to a **different random
map** than the one the run analysed. R7's residual therefore measured RNG
divergence, not operator consistency: honest runs failed it artefactually, and the
only runs it cleared were the ones whose declared `p` was fabricated to match
their own `C`. Reporting that as a false-positive rate would have been reporting
an artefact.

## Disposition

- Rules are **not** touched. `RULES_v3_FROZEN.md` (commit `dcf96696`) stands
  byte-identical: R7's definition, its spot-row draw, and `TOL = 1e-6` are
  unchanged. This is a fix to how the harness *measures* a declared intermediate,
  not a change to how the verifier *decides*.
- The fix (`variants3.py`) seeds the global RNG from the sealed `map_seed` before
  each map-producing call, so a run's map is reproducible from its sealed seed and
  the declared `pseudo_cl` is the pseudo-spectrum of the map actually analysed.
- The fix is committed **before** the new seal is drawn. A fresh key, a fresh
  assignment, and a fresh 48-run batch are executed under the same frozen rules;
  the new commitment goes to `public3/`.
- Nothing is deleted. `public3_aborted/` keeps the sealed commitment, the 48
  invalid run/receipt pairs, and the blind verdicts of the aborted attempt, so a
  reader can check that the abort was called on the harness and not on an outcome.
