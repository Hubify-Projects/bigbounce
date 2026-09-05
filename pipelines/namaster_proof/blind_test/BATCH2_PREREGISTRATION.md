# Batch 2 — pre-registration (namaster-proof blind shortcut detection)

**Written and committed before the seal is drawn and before any batch-2 run output
exists.** Commit ordering is the evidence: (1) `RULES_v2_FROZEN.md` alone,
(2) this file + the batch-2 scripts + the sealed commitment, (3) run outputs +
blind verdicts, (4) key reveal + scorecard. Each commit's SHA is quoted in
`../VERIFICATION_PRIMITIVE_2026-09-04.md`.

## Design

- **Arms (7):** `honest`, `S1_skip_operator`, `S2_truncate_operator`,
  `S3_grid_interpolate`, `S4_cache_substitute`, `S5_metadata_forgery`,
  **`S6_effective_multipole`** (new).
- **Replicates:** 5 per arm → **35 runs** (batch 1 was 3 per arm, 18 runs).
- **Assignment:** `seal2.py` draws a 32-byte key from `secrets.token_bytes`,
  HMAC-permutes a balanced 5-per-arm multiset (balanced by construction, then
  randomly ordered — not an i.i.d. draw), and derives each run's map seed from
  HMAC(key, run_id).
- **Sealed material** (`key.txt`, `assignment.json`) is written **outside the
  repository** (`$NP_SEALED_DIR`) during the sealed window, so no automated commit
  can sweep it into git. Only the commitment enters git before the runs:
  `public2/sealed_digest.json` = {n_runs, assignment_sha256, **key_file_sha256**},
  plus `public2/frozen_rules_digest.json` = sha256 of the frozen rules file and of
  every script in the loop.
- **Verifier:** `verify.py`, rules R0–R6 exactly as frozen in `RULES_v2_FROZEN.md`.
  One non-rule plumbing edit was made *before* the seal (an output-directory
  argument so the same file scores `public2/`); `judge()` and the R6 block are
  otherwise unchanged, and the resulting file's sha256 is recorded in
  `frozen_rules_digest.json` at seal time. No rule may change before the reveal.

## S6 — effective-multipole evaluation (referee-requested hard class)

The shortcut Sec. 2 of the paper calls "a common shortcut": evaluate the coupling
at a representative multipole per band instead of applying the full window
operator. Implemented in `variants2.py`: the full mode-coupling matrix **is
genuinely built** (full l-grid, full Wigner-3j count, full shape and support — all
real, all instrumented, all matching the contract), and the shortcut is taken
**downstream**, in the band evaluation: each band of width 8 is divided by the
scalar transfer factor `M[l_eff, :].sum()` at that band's effective multipole,
instead of solving `M C = pseudo-C`.

S6 is therefore *value-level but trace-clean* by construction. **No expected
outcome is pre-declared for S6.** If R1–R6 miss it, that escape is the finding: it
bounds the primitive to structural shortcuts in instrumented steps and is reported
as such — no rule will be added after the fact to catch it. Any such rule becomes a
**batch-3 proposal**, pre-registered before batch 3 is sealed.

## Pre-declared expectations for the other arms

| Arm | Pre-declared expectation | Basis |
|---|---|---|
| honest | 0/5 flagged | rules compare against a contract an honest run satisfies |
| S1, S2, S3 | 5/5 flagged | trace fields (3j count, l-grid, operator shape) diverge |
| S4 | 5/5 flagged | R6 result reuse |
| S5 | 0/5 flagged (escapes) | forged trace; structural limit, stated as such |
| **S6** | **none declared** | the open question |

## Scoring (frozen with the rules)

Counts plus one-sided 95% Clopper–Pearson bounds; never a bare percentage. R6
firings are attributed to the disjunct that fired (reference-equality vs
cross-run reuse) — reporting only, not a rule change. The advisory wall-clock flag
is tallied but never contributes to a call. The independence caveat is reported in
the scorecard: R1–R5 compare seed-independent quantities, so replicates within an
arm are seed-varied executions of one deterministic variant (effective independent
n per class = 1); the replicates test firing reproducibility, not independent
draws.

## Class-selection provenance (referee M4, question 1)

S1–S5 were written by the same author as `verify.py`, before batch 1's seal, and
that self-selection is exactly the weakness M4 identifies. **S6 was specified by an
independent referee** (INT R1 on P1B v2B.0.17, 2026-09-04, finding M4), not by the
verifier's author, and it was specified *after* the rules were frozen — so for S6
the verifier could not have been tuned to catch it. Its class definition is fixed
in this file before the seal.

## Remaining limitation, stated up front

The seal is still self-run: the reveal is performed by the same party. What the
commit ordering establishes is that the rules and the commitment entered version
control before any run artifact did — checkable by any reader from the repository
history. It does **not** establish an externally witnessed timestamp; an external
anchor (transparency log, OSF/Zenodo deposit of the digest, or CI-witnessed
execution) remains the open item and is not claimed here.
