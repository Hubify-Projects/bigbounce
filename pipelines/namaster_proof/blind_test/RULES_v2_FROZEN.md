# Frozen verifier rule set v2 — namaster-proof blind shortcut detection

**Frozen:** 2026-09-04, BEFORE the batch-2 seal is drawn and before any batch-2 run
output exists. This file is the pre-registration of the decision rules; it is
committed alone, in its own commit, so that the repository history shows the rules
were fixed before the second batch was sealed or executed.

**Why v2 exists.** Batch 1 (18 runs, commit `d60949b7`) amended two rules *after*
seeing outcomes: a wall-clock floor (which would have fired on 3/3 honest runs) and
an M-hash-collision rule (not evidential). Post-hoc rule selection on the test set
means batch 1 measures rule development, not detector performance. Batch 1 is
hereby relabelled the **pilot / rule-development round**. The rules below are the
amended set, frozen; batch 2 is a fresh sealed batch scored under them, and batch 2
is the round whose confusion matrix may be reported as a blind result.

**Verifier under freeze:** `verify.py`, sha256 recorded in
`public2/frozen_rules_digest.json` at seal time and quoted in the batch-2 section
of `../VERIFICATION_PRIMITIVE_2026-09-04.md`.

---

## Rules R1–R6 (exactly as implemented in `verify.py::judge` + `main`)

A run is called **shortcut** if one or more rules fire, otherwise **honest**.

| Rule | Fires when | Implemented in |
|---|---|---|
| **R0** `R0_receipt_invalid` | `verify_json_receipt(result)` raises: the result bytes do not match the receipt's content binding, or the receipt is malformed. | `main()` |
| **R1** `R1_code_mismatch` | `receipt.code.sha256 != contract.code_sha256`. | `judge()` |
| **R2** `R2_grid_mismatch` | `receipt.intermediates.ell_grid != contract.ell_grid` (exact list equality). | `judge()` |
| **R3** `R3_3j_count_mismatch` | `receipt.intermediates.n_wigner3j != contract.n_wigner3j`. | `judge()` |
| **R4** `R4_operator_shape_mismatch` | `coupling_shape != contract.coupling_shape` **or** `coupling_support != contract.coupling_support`. | `judge()` |
| **R5** `R5_input_contract_mismatch` | `receipt.inputs.mask_sha256 != contract.mask_sha256`. | `judge()` |
| **R6** `R6_result_reuse_across_inputs` | `sha256(bandpowers) == contract.reference_bandpowers_sha256` **OR** (that digest was already seen on an earlier run whose `inputs.map_sha256` differs). | `main()` |

### R6 — description corrected to match the code (referee M3)

The R1 referee is right: the paper described R6 as *"a result hash repeats across
runs with differing input-map hashes"*, i.e. only the second disjunct, while the
code also flags equality with the **reference run's** bandpower hash.

**Resolution: the code is correct and the description is fixed** (no code change).
Rationale: `contract.reference_bandpowers_sha256` is a *published* field of the
public contract, produced by an honest reference run on a reference map seed that
no blind run uses. Any blind run reproducing it bit-for-bit under a different input
map has reused the reference result — that is the same evidence as the cross-run
disjunct, with the reference run playing the role of the earlier run. Removing the
disjunct would only make the rule blind to the most likely cache substitution (the
one nearest to hand). Both disjuncts are stated here verbatim and are quoted in the
paper's protocol step. R6's per-arm attribution is reported by disjunct in batch 2
so a reader can see which one fired.

### Withdrawn rules (NOT part of the decision set; recorded for audit only)

- **Wall-clock floor** (`wall_s < 0.25 * reference_wall_s`) — **advisory only.**
  Still computed and recorded per run as `wall_rule_would_fire`, never contributes
  to the call. Batch 1 measured a cold/warm cache ratio of ~54x on an *honest* run
  against a 3–15x shortcut signal, so the timing channel is dominated by cache
  state and is unusable as a provenance signal at this scale.
- **M-hash collision across runs** (`coupling_sha256` repeats) — **withdrawn, not
  evidential.** M depends only on the mask and the l-grid, so for a fixed survey
  mask *every honest run legitimately shares one M hash*. This is the "M-hash
  caveat": an M-hash collision is the expected honest behaviour, not a shortcut
  signature. Cache substitution is caught by result reuse (R6) instead.

---

## Decision thresholds (batch 2, pre-registered)

- **Per-run call:** shortcut iff >= 1 of R0–R6 fires; honest otherwise. No
  aggregation, no scoring, no thresholding on rule counts.
- **Per-class detection** = flagged / n within an arm, reported as a count with a
  one-sided 95% Clopper–Pearson bound (never a bare percentage).
- **False-positive rate** = flagged honest runs / n honest, same interval
  treatment.
- **Success criterion (pre-declared for batch 2):** every arm of S1–S4 detected
  5/5, honest 0/5 flagged. S5 (metadata forgery) is expected to escape 5/5 by
  construction. **S6 (effective-multipole evaluation) has NO pre-declared expected
  outcome** — it is the referee-requested hard class and its result, escape or
  detection, is the finding.
- **Independence caveat, pre-declared:** R1–R5 compare seed-independent quantities
  against a fixed contract, so the replicates within one arm are seed-varied
  executions of a single deterministic variant. Effective independent n per class
  for those rules is 1, not 5; the replicates test reproducibility of the rule
  firing, not independent draws from a population of shortcuts.
- **No rule may be added, removed, or edited between this freeze and the batch-2
  reveal.** If a rule is found wanting, it is recorded as a batch-3 proposal.
