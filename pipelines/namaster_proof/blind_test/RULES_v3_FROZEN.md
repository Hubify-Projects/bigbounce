# Frozen verifier rule set v3 — namaster-proof blind shortcut detection

**Frozen:** 2026-09-04, BEFORE the batch-3 scripts are written, BEFORE the batch-3
seal is drawn, and BEFORE any batch-3 run output exists. Committed alone, in its
own commit, so the repository history shows the rules were fixed first.

**Why v3 exists.** Batch 2 (35 runs, `public2/`) scored R0–R6 under
`RULES_v2_FROZEN.md`. Structural arms S1–S4 were detected 15/15 (one-sided 95%
lower bound 0.861) at 0/5 honest false positives, and the two value-level arms
escaped 5/5: `S5_metadata_forgery` (expected — forged trace) and
`S6_effective_multipole` (**no outcome pre-declared; the escape was the finding**).
Batch 2 also left the R6 *cross-run* disjunct untested: every S4 firing came from
the reference-equality disjunct. Batch 2 recorded both gaps as batch-3 proposals.
v3 = v2's R0–R6 verbatim, plus one new rule **R7**, plus one new arm
`S4b_cache_crossrun` that exercises the untested disjunct.

---

## R0–R6 — unchanged from v2

Carried over verbatim from `RULES_v2_FROZEN.md` (R0 receipt invalid, R1 code
mismatch, R2 grid mismatch, R3 3j-count mismatch, R4 operator shape/support
mismatch, R5 input-contract mismatch, R6 result reuse — both disjuncts, reference
equality OR a repeated bandpower digest under a differing `inputs.map_sha256`).
The withdrawn rules stay withdrawn: the wall-clock floor remains advisory-only and
never contributes to a call; the M-hash-collision rule remains withdrawn as
non-evidential.

## R7 — receipt-bound operator-consistency residual (NEW, value-level)

**Motivation.** R1–R6 are *trace-level*: they compare declared execution metadata
against a contract. S6 defeats them by construction — it genuinely builds the full
coupling operator (real l-grid, real 3j count, real shape and support) and takes
its shortcut *downstream*, dividing each band by a scalar transfer factor
`M[l_eff,:].sum()` instead of solving `M C = p`. No trace field differs. Catching
it requires a rule that reads the published **values**.

**New instrumented intermediate.** The batch-3 harness records the run's own
pseudo-spectrum as `intermediates.pseudo_cl` (a length-`lmax+1` float list). This
is a cheap quantity every honest MASTER pipeline already computes; it is measured
by the harness exactly as `map_sha256`, `n_wigner3j` and the operator hashes are.

**Rule.** Let `C` = the published `bandpowers`, `p` = `receipt.intermediates.pseudo_cl`,
`lmin = 2`. The verifier:

1. rebuilds the survey mask deterministically (`pcl.make_mask(nside)`) and
   **aborts the check** unless `sha256(mask) == contract.mask_sha256` (so the
   check is bound to the same mask R5 pins);
2. derives a spot-row set from the receipt itself —
   `h = sha256(receipt.inputs.mask_sha256 || band_hash(C))`, and takes the first
   `K = 6` distinct values of `lmin + (h[4i:4i+4] mod (lmax+1-lmin))`. The rows
   depend on the run's *own result hash*, so they are not knowable before the
   result exists and cannot be chosen by the runner;
3. recomputes **only those K rows** of the mode-coupling matrix from the mask
   power spectrum (cost ≈ K/(lmax+1) ≈ 9% of a full build — a spot-check, not a
   re-run, so the primitive's "verify without repeating the computation" property
   is preserved up to a small constant);
4. fires `R7_operator_consistency_residual` iff, for any spot row `l1`,
   `| sum_{l2>=lmin} M[l1,l2] C[l2] - p[l1] | > TOL * ||p[lmin:]||_2` with
   **`TOL = 1e-6`**.

`R7` is skipped (never fires) if `pseudo_cl` is absent or malformed; absence is
already caught by R5/R0 territory and is reported separately, not silently.

### Pre-registered tolerance justification and false-positive risk

`TOL = 1e-6` is set from **theory plus non-blind calibration**, before the seal,
never from batch-3 data. An honest run solves `(M[2:,2:] + 1e-12 I) C = p`, so its
exact residual is `-1e-12 * C`, i.e. relative residual of order
`eps * kappa(M)`. Measured on the public mask at `nside=64, lmax=64`:
`kappa(M[2:,2:]) = 1.28`, and honest relative residuals on three non-blind seeds
(11, 4242, 90210) were `1.4e-12`, `1.4e-12`, `8.4e-13`. The same seeds under the
S6 transformation give `1.5e-1`, `1.5e-1`, `7.5e-2`. `TOL = 1e-6` sits ~6 orders
above the honest scale and ~5 orders below the S6 scale; the decision is
insensitive to any choice across that 11-order gap.

**Theoretical false-positive risk.** Three channels, all small and all stated up
front: (i) *numerical* — needs a `10^6` relative-residual excursion from a
`kappa ~ 1` solve, which double precision does not produce; (ii) *environment
reproducibility* — the verifier's recomputed rows must match the runner's, which
holds only if `healpy`/`numpy` reproduce `anafast(mask)` bit-comparably; a
cross-machine verifier could see a genuine honest run disagree, so R7 is a
**same-environment** rule and that assumption is declared, not hidden (the mask
hash gate in step 1 catches the gross version of this failure); (iii) *ridge
scale* — a pipeline regularising far more heavily than `1e-12` would fail R7
legitimately. Expected FP on the batch-3 honest arm is therefore 0/6, but the
reported figure is the measured count with its one-sided 95% Clopper–Pearson
bound, never the expectation.

**Declared limitation (stated before the reveal).** R7 is bound to a *declared*
intermediate. An adversary who knows R7 can forge `pseudo_cl := M C` — one
matrix-vector product — and escape. R7 therefore does **not** make value-level
shortcuts undetectable-proof; it moves S6 from "a shortcut that leaves an honest
trace" into the S5 class, "deliberate fabrication of a recorded intermediate".
That is a real strengthening (the shortcut no longer escapes by omission) and a
real limit (it does not survive an informed forger), and both are claimed at
exactly that strength.

---

## Arms (batch 3)

Eight arms, **6 replicates each = 48 runs** (batch 2: 7 arms x 5 = 35):
`honest`, `S1_skip_operator`, `S2_truncate_operator`, `S3_grid_interpolate`,
`S4_cache_substitute`, **`S4b_cache_crossrun`** (new), `S5_metadata_forgery`,
`S6_effective_multipole`.

**`S4b_cache_crossrun`** publishes the bandpowers of an *earlier run in this same
batch* (the most recently published prior run) while declaring its own input map
and its own genuinely-built operator trace. It exercises R6's second disjunct,
which batch 2 never fired. If the arm lands in slot `run_000` there is no prior
run and the reference result is used instead; the reveal reports, per replicate,
which source was substituted, so a degenerate replicate cannot be mistaken for a
cross-run firing.

## Decision thresholds (batch 3, pre-registered)

- **Per-run call:** shortcut iff >= 1 of R0–R7 fires; honest otherwise. No
  aggregation, no scoring, no thresholding on rule counts.
- **Per-class detection** = flagged / n within an arm, reported as a count with a
  one-sided 95% Clopper–Pearson bound; never a bare percentage.
- **False-positive rate** = flagged honest runs / n honest, same treatment.
- **Independence caveat, restated and extended to R7:** R1–R5 compare
  seed-independent quantities against a fixed contract, so replicates within an
  arm are seed-varied executions of one deterministic variant — effective
  independent n per class is 1, not 6. R7 *is* seed-dependent (both `p` and the
  spot-row draw vary with the map), so its replicates are genuinely distinct
  evaluations of one deterministic variant; that is still class-level evidence,
  not a run-level confidence interval, and it is reported as such. **No
  claim of a per-run detection probability is made from these data.**

### Pre-declared expectations

| Arm | Pre-declared expectation | Basis |
|---|---|---|
| honest | 0/6 flagged | rules compare against a contract an honest run satisfies |
| S1, S2, S3 | 6/6 flagged | trace fields diverge (R2/R3/R4) |
| S4_cache_substitute | 6/6 flagged, R6 reference disjunct | published reference digest |
| S4b_cache_crossrun | 6/6 flagged, R6 **cross-run** disjunct; R7 also expected | reused digest under a differing map hash; reused `C` is inconsistent with this run's `p` |
| S5_metadata_forgery | 0/6 flagged (escapes) | forged trace incl. forged `pseudo_cl`; structural limit, stated as such |
| **S6_effective_multipole** | **6/6 flagged by R7** | the pre-registered prediction this batch tests |

S6's expectation is a *prediction*, not a guarantee: R7 was designed against the
S6 definition frozen in batch 2, so a batch-3 detection is a test of a rule
written before this batch's data existed, not a blind discovery. If R7 misses S6,
that miss is reported as the finding and no rule is added afterwards.

- **No rule may be added, removed, or edited between this freeze and the batch-3
  reveal.** Anything found wanting becomes a batch-4 proposal.
