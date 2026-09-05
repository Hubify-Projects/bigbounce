# Batch 3 — pre-registration (namaster-proof blind shortcut detection)

**Written and committed after `RULES_v3_FROZEN.md` (its own commit,
`dcf96696`), before the seal is drawn, and before any batch-3 run output exists.**
Commit ordering is the evidence: (1) `RULES_v3_FROZEN.md` alone, (2) this file +
the batch-3 scripts, (3) the sealed commitment alone, (4) run outputs + blind
verdicts, (5) key reveal + scorecard, (6) OpenTimestamps anchor. Each commit SHA
is quoted in `../VERIFICATION_PRIMITIVE_2026-09-04.md`.

## What batch 3 tests

Batch 2 closed with two open items, both recorded there as batch-3 proposals:

1. **S6 escaped 5/5.** The effective-multipole shortcut builds the full operator
   and shortcuts downstream, so no trace field diverges. R0–R6 are trace-level and
   structurally cannot see it. **R7** (frozen in v3) is the proposed answer: a
   value-level, receipt-bound operator-consistency residual spot-check.
2. **R6's cross-run disjunct was never exercised.** All 5 batch-2 S4 firings came
   from the reference-equality disjunct. **`S4b_cache_crossrun`** (new arm)
   substitutes an earlier run *of the same batch*, so only the cross-run disjunct
   can catch it.

## Design

- **Arms (8):** `honest`, `S1_skip_operator`, `S2_truncate_operator`,
  `S3_grid_interpolate`, `S4_cache_substitute`, `S4b_cache_crossrun`,
  `S5_metadata_forgery`, `S6_effective_multipole`.
- **Replicates:** 6 per arm -> **48 runs** (batch 2: 5 per arm, 35 runs).
- **Assignment:** `seal3.py`, unchanged in mechanism from `seal2.py` — a 32-byte
  `secrets.token_bytes` key, an HMAC permutation of a balanced 6-per-arm multiset
  (balanced by construction, then randomly ordered; not an i.i.d. draw), and a map
  seed per run derived as HMAC(key, run_id).
- **Sealed material** (`key.txt`, `assignment.json`, and the batch-3-only
  `crossrun_sources.json`) is written **outside the repository** to
  `$NP_SEALED_DIR` during the sealed window. Only the commitment enters git before
  the runs: `public3/sealed_digest.json` = {n_runs, assignment_sha256,
  key_file_sha256} and `public3/frozen_rules_digest.json` = sha256 of the frozen
  rules file and of every script in the loop, `verify3.py` included.
- **Verifier:** `verify3.py`, rules R0–R7 exactly as frozen. R0–R6 are executed by
  importing `judge` from the batch-2 `verify.py` unchanged, so the carried-over
  rules are the same bytes, not a re-typed copy. No rule changes before the reveal.

## The new instrumented field

`intermediates.pseudo_cl` — the run's own pseudo-spectrum, measured by the harness
(`variants3.pseudo_spectrum`) from the declared input map and the survey mask,
exactly as `map_sha256` and `n_wigner3j` are measured. It is small (65 floats) and
free: every honest MASTER pipeline computes it as step one.

## Pre-declared expectations

| Arm | Expectation | Basis |
|---|---|---|
| honest | 0/6 flagged | an honest run satisfies the contract and `M C = p` to ~1e-12 |
| S1, S2, S3 | 6/6 flagged | trace fields diverge (R2/R3/R4) |
| S4_cache_substitute | 6/6 flagged — R6 reference disjunct, **and R7** | it publishes the reference `C` while declaring its own `p` |
| S4b_cache_crossrun | 6/6 flagged — R6 **cross-run** disjunct, and R7 | reused digest under a differing `map_sha256`; reused `C` inconsistent with this run's `p` |
| S5_metadata_forgery | 0/6 flagged (escapes) | the forger also fabricates `pseudo_cl := M C`; the informed-forger limit R7 declares up front |
| **S6_effective_multipole** | **6/6 flagged by R7** | the prediction this batch tests |

S6's row is a *prediction from a rule written before this batch's data existed*,
not a blind discovery: R7 was designed against S6's batch-2 definition. It is
still a real test — R7 could fail on the spot-row draw, on the tolerance, or on
numerical reproducibility — but the claim made afterwards will be exactly
"a rule pre-registered against a known class detects that class", never
"the verifier discovered an unanticipated shortcut".

## S5 is implemented as a complete forgery, deliberately

Batch 2's S5 forged the trace but would have left `pseudo_cl` honest, which would
have made R7 fire on it for the wrong reason. Batch 3 forges it consistently
(`p := M C`, one matrix-vector product), so S5 remains the in-principle-undetectable
class and R7's declared limitation is *exercised* rather than asserted.

## Scoring (frozen with the rules)

Counts plus one-sided 95% Clopper–Pearson bounds; never a bare percentage. R6
firings are attributed by disjunct; R7's relative residual is recorded per run and
its per-arm min/max are reported. The advisory wall-clock flag is tallied and never
contributes to a call. The independence caveat is reported in the scorecard and is
extended to R7: R7 is seed-dependent, so its replicates are distinct evaluations of
one deterministic variant — class-level evidence, **not** a run-level interval, and
no per-run detection probability is claimed.

## Remaining limitations, stated up front

- The seal is still self-run; the reveal is performed by the same party. What the
  commit ordering establishes is that rules and commitment entered version control
  before any run artifact did. Batch 3 adds an **OpenTimestamps** anchor of the
  seal file (Bitcoin-witnessed, third-party), which is a genuine external time
  witness but still does not witness *execution*.
- R7 raises the cost of a value-level shortcut from omission to fabrication; it
  does not defeat an informed forger, and S5 is the standing demonstration.
- Classes S1–S5 were authored by the verifier's author; S6 was specified by an
  independent referee (INT R1 on P1B v2B.0.17, 2026-09-04, finding M4) after the
  batch-2 rules were frozen. S4b was specified by the batch-2 reveal's own audit
  of an untested disjunct, not by an independent party.
