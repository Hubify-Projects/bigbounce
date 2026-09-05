# `namaster-proof` as a verification primitive — design note (2026-09-04)

**Lift target:** novelty audit `project-context/NOVELTY_AUDIT_2026-09-04.md`
§"#3 — `namaster-proof` as a verification primitive (candidate 10)". The paper
(`arxiv/paper1b_namaster_proof.tex`, v2B.0.16) currently frames the package as a
NaMaster-specific validation layer — honest tier **N2**. The audit's lift is to
reframe it as a *general verification primitive* and to demonstrate it with a
**blind shortcut-detection test**.

**Claim under test.** A referee who cannot afford to re-run an expensive exact
computation can, from receipts alone, decide whether the computation was
actually performed or silently shortcut.

---

## 1. What the receipt binds

The shipped primitive (`packages/namaster-proof/src/namaster_proof/receipts.py`)
binds, per published result:

| Field | Source | Trust |
|---|---|---|
| `result_sha256`, `result_bytes` | recomputed from the result bytes at verify time | **self-evident** (protected; cannot be overridden by metadata) |
| `result_file`, `schema_version` | protected | self-evident |
| caller metadata (suite, seeds, realizations…) | caller-asserted, checked by `validate_json_receipt` against a *trusted expected contract* | **asserted** |

The primitive therefore already gives *content binding* (the result bytes are
the ones the receipt describes) but only *asserted* binding for how the bytes
were produced. Shortcut detection lives entirely in the second row, so the blind
test extends the caller metadata into an **execution trace** emitted by an
instrumented harness rather than typed by the analyst:

- `inputs`: sha256 of the input map and of the mask, `nside`, `lmax`.
- `code`: sha256 of the compute module source actually imported.
- `env`: numpy/healpy versions, platform.
- `intermediates`: sha256 + shape of the mode-coupling matrix `M_{ℓℓ'}`, the
  ℓ-grid actually evaluated, and an instrumented counter of Wigner-3j
  evaluations performed.
- `outputs`: decoupled bandpowers (in the result file, hash-bound).
- `wall_s`: measured, not declared.

## 2. What it can and cannot detect, in principle

**Detectable** (the trace is a *consequence* of the code path taken):

1. **Operator skipped** — `f_sky` division instead of `M^{-1}`: no `M` hash, 0
   3j evaluations, wall-time orders of magnitude low.
2. **Operator truncated** — band-diagonal / low-rank `M`: `M` hash present but
   3j-evaluation count and matrix support disagree with the declared contract.
3. **Grid reduction + interpolation** — coarse ℓ grid silently interpolated:
   evaluated-ℓ list ≠ full grid; 3j count reduced by the stride factor.
4. **Cache substitution** — a previous run's result re-published under new
   inputs: `M`/result hashes repeat while `inputs.map_sha256` differs, or
   `M` hash does not depend on the mask it claims.

**Not detectable, in principle, by receipts alone:**

- **Metadata forgery.** An adversary who runs the shortcut and then *writes the
  honest trace* into the receipt is invisible: every protected field still
  recomputes, because the protected fields bind the result bytes, not the
  process. Only an external anchor (a witnessed execution environment, a
  third-party rerun, or a signed log from hardware/CI the analyst does not
  control) closes this. The paper already states the weaker version of this for
  coordinated result+receipt replacement (§"Content Validation").
- **Semantically wrong but equally expensive** computations (a wrong mask, a
  wrong beam) — the trace is self-consistent; only a contract on the *inputs*
  catches it, and only if the correct input hash is known independently.
- **Numerical drift** below the declared tolerance.

The honest framing of the primitive is therefore: **receipts convert an
expensive-computation claim into a cheap consistency check against a declared
contract, under a non-adversarial-analyst threat model.** They are a shortcut
detector, not a fraud detector.

## 3. Blind protocol

1. A **reference contract** is published first, from one honest reference run:
   full ℓ-grid, `M` shape, exact 3j-evaluation count, code sha256, tolerance.
2. A sealing script draws a random key, derives an assignment of `N` runs to
   `{honest, S1…S5}` by HMAC(key, run_id), and writes only the *sealed digest*
   of the assignment before running.
3. Each run executes its (unknown to the verifier) variant, publishes a result
   + receipt through `namaster_proof.receipts.publish_json`, into an opaquely
   named directory.
4. The **verifier** sees only the run directories, the reference contract, and
   the input manifest. Its decision rule flags a run when any of: receipt
   verification fails; code sha256 ≠ reference; ℓ-grid ≠ reference; 3j count ≠
   reference; `M` shape/support ≠ reference; `M` hash collides with another run
   whose input hash differs; or wall-time below a floor derived from the
   reference. It emits `honest` / `shortcut` per run with the triggering rule.
5. The key is then revealed and the confusion matrix computed.

**Success criterion (pre-declared):** ≥1 honest run and ≥1 run of each of S1–S4
present; **detection rate on S1–S4 = 100%** and **false-positive rate on honest
runs = 0%**. S5 (metadata forgery) is included *expecting it to escape*; its
escape is the reported limitation, not a failure of the protocol.

---

## 4. Reframing (executed 2026-09-04)

The blind test in `blind_test/` was implemented, sealed, run, and scored.
Artifacts: `blind_test/public/{contract,sealed_digest,verdicts,scorecard}.json`
and 18 result+receipt pairs under `blind_test/public/runs/`; manifest
`reproducibility/manifests/experiments/p1b-blind-shortcut-detection.json`.
18 runs, 3 per arm, nside 64, lmax 64, local CPU, ~1 min, $0.

**Result against the pre-declared criterion (§3), which is MET:**

| Arm | n | flagged | triggering rules |
|---|---|---|---|
| honest | 3 | 0 | — |
| S1 operator skipped | 3 | 3 | R3 (3j count), R4 (operator shape) |
| S2 operator truncated | 3 | 3 | R3, R4 |
| S3 grid reduced + interpolated | 3 | 3 | R2 (ℓ-grid), R3, R4 |
| S4 cache substitution | 3 | 3 | R6 (result reuse across inputs) |
| S5 metadata forgery | 3 | 0 | — (escapes, as pre-declared) |

Detection rate **12/12 = 100%** on the classes receipts can see (S1–S4);
**12/15 = 80%** over all shortcut runs including the forgery arm; **false
positive rate 0/3 = 0%** on honest runs. Seal verified: the assignment
re-derived from the revealed key hashes to the digest committed before any run
(`0f4ca4ba…`).

**N3-eligible claim sentence (supported by this test):**

> Under a non-adversarial-analyst threat model, execution-trace receipts
> decide, from the receipts alone and without re-running the computation,
> whether an expensive pseudo-C_ℓ analysis was actually performed: in a sealed
> blind test of 18 runs the verifier detected 12/12 (100%) of the
> operator-skipping, operator-truncating, grid-reducing, and cache-substituting
> shortcut runs with a 0% false-positive rate on honest runs, while the
> metadata-forgery arm escaped 3/3 — establishing that receipts of this kind
> are a *shortcut detector*, not a fraud detector.

**Two findings that change the recipe, both discovered by running it:**

1. **Wall-clock is not a usable rule.** The shortcut arms run 3–15× faster than
   honest ones, but a cold-cache honest reference run took 4.29 s against
   0.08 s warm — so the pre-declared wall floor (25% of the reference) would
   have fired on **3/3 honest runs**. It is recorded in each verdict as
   `wall_rule_would_fire` and excluded from the decision rule set. §3's rule
   list is amended accordingly.
2. **A coupling-matrix hash collision across runs is not evidence of cache
   substitution.** `M` depends only on the mask and the ℓ-grid, so for a fixed
   survey mask every honest run legitimately shares one `M` hash. §2's item 4
   is corrected: cache substitution is caught by *result* reuse under differing
   input-map hashes (rule R6), not by `M` reuse.

**Scope limits, stated plainly.** The estimator exercised here is this repo's
own spin-0 MASTER implementation, not NaMaster itself (`pymaster` is not
installed in the lab environment); the instrumented 3j counter is what makes
the trace a measured consequence of the code path, and an equivalent hook would
have to be added inside NaMaster to carry the claim over verbatim. The seal is
process-level — the verifier had no access to `sealed/` — not a cryptographic
pre-registration against an external timestamp. And the S5 escape is
structural: closing it needs an anchor outside the analyst's control (witnessed
CI, signed build/execution logs, or a third-party rerun), which is the natural
next lift and is **not** claimed here.

## 5. Packaging steps (Houston's click-list)

Neither step is done here; both need Houston's account actions.

1. **Zenodo DOI.** Create a new upload from a tagged tarball of
   `packages/namaster-proof/` plus `pipelines/namaster_proof/` (design note,
   `blind_test/` code, `sealed/`, `public/`). Upload type: software; title
   "namaster-proof: execution receipts as a shortcut-detection primitive";
   license MIT to match the package; link the GitHub repo so future tags mint
   versioned DOIs automatically. Record the concept DOI in P1B and in the
   manifest's `outputs`.
2. **ASCL entry.** Submit at ascl.net/code/submit once the Zenodo DOI exists:
   code name `namaster-proof`, one-line description "content receipts and blind
   shortcut detection for masked-sky pseudo-C_ℓ analyses", site = the GitHub
   repo, credit Houston Golden, and cite P1B as the describing paper. ASCL
   assigns an ascl:XXXX.XXX id to quote alongside the DOI.

---

## 6. Batch 2 (pre-registered) — 2026-09-04

Batch 1 (§4) amended two rules after seeing outcomes, so it is hereby relabelled
the **rule-development / pilot round**; its 12/12 and 0/3 are rule-fitting
numbers, not blind-test numbers. Batch 2 is a fresh sealed batch of **35 runs**
(7 arms x 5 replicates) scored by rules frozen *before* the seal was drawn.

### Commit-ordered audit trail

| # | Commit | Contents | State of the tree |
|---|---|---|---|
| 1 | `4451b135` | `blind_test/RULES_v2_FROZEN.md` **alone** | rules fixed; no batch-2 seal exists |
| 2 | `28efa21c` | pre-registration, `variants2.py` (S6), `seal2/run_blind2/reveal2`, `public2/sealed_digest.json`, `public2/frozen_rules_digest.json` | commitment in git; **no run output exists** |
| 3 | `27300504` | 35 run result+receipt pairs, `public2/verdicts.json`, `contract.json` | blind calls recorded; key still outside the repo |
| 4 | `974e2859` | `sealed2/{key.txt,assignment.json}`, `public2/scorecard.json` | reveal + scoring |
| 5 | `b3347c53` | `reproducibility/manifests/experiments/p1b-blind-shortcut-detection-batch2.json` | manifest |

Sealed digest `c96b5bf1…` (35 runs), key-file digest `bbf6373b…`; `seal_verified:
true`. The sealed key and assignment were held **outside the working tree** for the
whole sealed window, so the tree at commits 1–3 provably could not contain them.

### Rule fixes carried into the freeze (referee M3)

- **R6 description corrected to the code, no code change.** R6 fires on
  `sha256(bandpowers) == contract.reference_bandpowers_sha256` **OR** a repeat of a
  digest already seen under a different `inputs.map_sha256`. The reference disjunct
  is legitimate — the reference bandpower hash is a published contract field from a
  seed no blind run uses — and batch 2 shows it is the load-bearing one: **all 5 S4
  detections fired the reference disjunct, 0 the cross-run disjunct.** Under the
  rule as the paper previously *described* it, S4 would have gone undetected.
- **Wall-clock floor: advisory only**, recorded per run, never contributes to a
  call. It again flagged 5/5 honest runs (and 5/5 S6) in batch 2.
- **M-hash collision: withdrawn** — M depends only on the mask and the l-grid, so a
  collision is expected honest behaviour.

### Result (frozen rules, 35 runs)

| Arm | n | flagged | rules fired |
|---|---|---|---|
| honest | 5 | 0 | — |
| S1 operator skipped | 5 | 5 | R3, R4 |
| S2 operator truncated | 5 | 5 | R3, R4 |
| S3 grid reduced + interpolated | 5 | 5 | R2, R3, R4 |
| S4 cache substitution | 5 | 5 | R6 (reference disjunct 5/5) |
| S5 metadata forgery | 5 | 0 | — (escapes, pre-declared) |
| **S6 effective-multipole** | 5 | **0** | **— (escapes; no outcome was pre-declared)** |

- Structural classes S1–S4: **20/20**, one-sided 95% lower bound on sensitivity
  **0.861**.
- Honest false positives: **0/5**, one-sided 95% upper bound on FPR **0.451**.
- All shortcut arms including S5+S6: 20/30.
- Independence caveat: R1–R5 compare seed-independent quantities, so the five
  replicates in an arm are seed-varied executions of one deterministic variant —
  effective independent n per class is 1; the replicates measure firing
  reproducibility, not independent draws.

### S6 escaped, and that is the finding

S6 builds the full coupling operator genuinely (real l-grid, real 3j count, real
shape and support — all matching the contract) and takes the shortcut *downstream*,
dividing each band by the coupling evaluated at one effective multipole. Nothing in
R1–R6 inspects result **values** against the contract, so it is invisible to this
verifier. **No rule was added after the fact.** A value-level rule (e.g. a declared
tolerance band on bandpowers against an independently-known reference, or a
cross-checked second estimator) is proposed as **batch 3**, to be pre-registered
before batch 3 is sealed — future work, not claimed here.

### Revised claim sentence (what the two batches jointly support)

> Under a non-adversarial-analyst threat model — the analyst may alter the
> computation but runs an unmodified, instrumented harness — execution-trace
> receipts decide, from receipts alone and without re-running the computation,
> whether the *structural* steps of an expensive pseudo-C_l analysis were performed:
> in a sealed batch of 35 runs scored by decision rules frozen and committed before
> the seal was drawn, the verifier flagged 20/20 operator-skipping,
> operator-truncating, grid-reducing and cache-substituting runs (one-sided 95%
> lower bound 0.86) with 0/5 false positives on honest runs (one-sided 95% upper
> bound 0.45), while both the metadata-forgery arm and the effective-multipole arm
> escaped 5/5. Receipts of this kind are therefore a detector of *structural*
> shortcuts in instrumented steps — not of forged metadata, and not of value-level
> shortcuts taken downstream of the instrumented operator. An earlier 18-run pilot
> (§4) developed these rules and is reported as such.

**Remaining limitation (referee M2, stated not hidden).** The reveal is still
self-run: the same party sealed, ran, and unsealed. What the repository history
establishes is *ordering* — rules, then commitment, then outputs, then key, each in
its own commit, with the sealed material held outside the tree until the reveal —
which any reader can check. It is not an externally witnessed timestamp. An
external anchor (a transparency log such as Rekor, an OSF/Zenodo deposit of the
digest alone, or CI-witnessed execution on infrastructure the analyst does not
control) remains open, and is the same anchor that would be needed to close S5.
Scope limits from §4 are unchanged: this exercises the repository's own
instrumented spin-0 MASTER estimator, not NaMaster and not the spin-2 operator.

---

## Batch 3 (pre-registered) — a value-level rule, and the disjunct batch 2 never tested

Batch 2 closed with two named open items, both recorded there as batch-3 proposals:
`S6_effective_multipole` escaped 5/5 because every rule R0–R6 is *trace-level* and
S6 is trace-clean by construction; and every S4 firing came from R6's
reference-equality disjunct, so R6's cross-run disjunct had never fired. Batch 3
addresses both, pre-registered.

### R7 — receipt-bound operator-consistency residual (the new rule)

The harness records one new instrumented intermediate, `intermediates.pseudo_cl`
(65 floats — the pseudo-spectrum every MASTER pipeline computes as step one). The
verifier then, for each run: rebuilds the mask and refuses the check unless its
hash matches the contract; derives **K = 6** spot rows from
`sha256(inputs.mask_sha256 ‖ sha256(bandpowers))`, so the rows depend on the run's
own result and cannot be chosen by the runner; recomputes **only those 6 rows** of
the coupling matrix (~9% of a full build, so verification still does not repeat the
computation); and fires iff
`|Σ_{l2≥2} M[l1,l2] C[l2] − p[l1]| > 1e-6 · ‖p‖₂` on any spot row.
An effective-multipole shortcut cannot satisfy this: it divides each band by a
scalar transfer factor, so its `C` is not the solution of `M C = p` no matter how
honest its trace is.

`TOL = 1e-6` was fixed from theory plus **non-blind** calibration before the seal —
`κ(M[2:,2:]) = 1.28`, honest relative residuals `8.4e-13`–`1.4e-12` on seeds
11/4242/90210, the same seeds under S6 giving `7.5e-2`–`1.5e-1`. The tolerance sits
in an eleven-order gap; nothing was tuned after unblinding.

### Result (48 runs: 8 arms × 6, seal `abfe2793…`, `seal_verified: true`)

| Arm | Flagged | Rules that fired | R7 residual range |
|---|---|---|---|
| honest | **0/6** | — | 2.9e-14 – 1.4e-12 |
| S1_skip_operator | 6/6 | R3, R4, R7 | 1.4e-3 – 5.7e-2 |
| S2_truncate_operator | 6/6 | R3, R4, R7 | 2.4e-3 – 6.6e-3 |
| S3_grid_interpolate | 6/6 | R2, R3, R4, R7 | 7.4e-3 – 5.2e-1 |
| S4_cache_substitute | 6/6 | R6 (reference 6), R7 | 1.7e-2 – 1.4e-1 |
| **S4b_cache_crossrun** | 6/6 | R6 (**cross-run 4**, reference 2), R7 | 7.0e-3 – 2.6e-2 |
| S5_metadata_forgery | **0/6** | — | 7.5e-19 – 4.5e-17 |
| **S6_effective_multipole** | **6/6 — by R7 alone** | R7 | 1.8e-4 – 4.9e-2 |

Structural arms S1–S4b: 24/24, one-sided 95% lower bound **0.905**. S6: 6/6, lower
bound **0.607**. Honest false positives: **0/6**, one-sided 95% upper bound
**0.393**. The measured honest/S6 separation is eight orders on each side of the
threshold, so the S6 result is not threshold-sensitive.

**Does R7 catch S6? Yes, 6/6 — but the claim is bounded three ways.** (1) R7 was
written *against S6's batch-2 definition*: this is a pre-registered rule detecting a
known class, not a verifier discovering an unanticipated shortcut. (2) The false
positive cost is measured at 0/6 with an upper bound of 0.393 — six honest runs
cannot establish a small FP rate, only that none was seen. (3) R7 is bound to a
*declared* intermediate, so an informed forger escapes by fabricating
`p := M C` — one matrix-vector product. Batch 3 **exercises** that limit rather than
asserting it: S5 forges `pseudo_cl` consistently and escapes 6/6 with residuals at
1e-17. R7 therefore moves the effective-multipole shortcut out of "escapes by
omission" and into the S5 class, "requires deliberate fabrication of a recorded
intermediate". That is the whole of the improvement.

**Detection is class-level, not run-level (R2 audit, restated for R7).** R1–R5
compare seed-independent quantities against a fixed contract, so their replicates
are repeated executions of one deterministic variant — effective independent n per
class is 1. R7 *is* seed-dependent (both `p` and the spot-row draw vary), so its six
replicates are distinct evaluations, but still of a single deterministic variant.
The Clopper–Pearson bounds quoted above are class-level summaries. **No per-run
detection probability is claimed from these data**, and the intervals must not be
read as one.

**S4b and the cross-run disjunct.** 4/6 replicates fired R6's cross-run disjunct —
the first time it has ever fired. The other 2 collapsed to reference-equality
because the prior run they substituted was itself cache-substituting;
`sealed3/crossrun_sources.json` names the source run for each replicate, so the
collapse is auditable rather than silent.

### Attempt 1 was aborted on a harness defect, and is kept

The first batch-3 seal (`8b4fa840…`, commit `b19b72fc`) was executed, blind-judged,
and then **abandoned without ever being unsealed**. `pcl.make_map` ignores its
`seed` argument — healpy's `synfast` draws from the global NumPy RNG — so the new
`pseudo_cl` instrumentation described a *different random map* than the run
analysed, and R7 was measuring RNG divergence rather than operator consistency. The
defect was diagnosed from the public verdict file and the source, with the
assignment still sealed. All 48 invalid runs, receipts and verdicts are preserved
under `blind_test/public3_aborted/` with `BATCH3_ABORT_NOTE.md`; the rules file was
not touched; the harness fix was committed before the new key was drawn. This also
corrects a batch-1/2 statement: the sealed `map_seed` never actually selected those
batches' maps, so their replicates were fresh random draws rather than
"seed-varied executions" — which affects the wording, not their conclusions, since
no batch-1/2 rule depended on reproducing a map.

### External anchor

`public3/sealed_digest.json.ots` is an OpenTimestamps stamp of the batch-3 seal,
submitted to four calendars and currently **pending** Bitcoin confirmation. `ots
upgrade` on the batch-1 and batch-2 stamps now returns *Timestamp complete*: both
carry Bitcoin block-header attestations. `ots verify` requires a Bitcoin node,
which this machine does not run, so the attested heights are left for a reader with
a node or a public verifier to confirm. This is a genuine third-party *time*
witness; it still does not witness *execution*, and the reveal remains self-run.

### Audit trail (each step its own commit, in this order)

| Step | Commit | Content |
|---|---|---|
| 1 | `dcf96696` | `RULES_v3_FROZEN.md` **alone** — R0–R7 and thresholds, before any batch-3 script existed |
| 2 | `d03fe376` | pre-registration + the five loop scripts, no seal, no output |
| 3 | `b19b72fc` | attempt-1 sealed commitment alone |
| 4 | `60917635`, `1a4c3d4e` | attempt 1 aborted and preserved (`public3_aborted/`, abort note) |
| 5 | `77d5f5a5` | harness fix (`variants3.seed_rng`), **before** the new key was drawn |
| 6 | `c7fb5e38` | batch-3 sealed commitment alone — `abfe2793…`, no output yet |
| 7 | `4a7f9f82` | 48 runs + receipts + blind verdicts, still sealed |
| 8 | `5b643fc2` | reveal: key, assignment, cross-run sources, scorecard |
| 9 | `bf7d26e3` | OpenTimestamps stamp + batch-1/2 upgrades |
| 10 | `b5bcb278` | reproducibility manifest (`p1b-blind-shortcut-detection-batch3`) |

`RULES_v3_FROZEN.md` is byte-identical at `dcf96696` and at HEAD
(`git diff dcf96696 HEAD -- .../RULES_v3_FROZEN.md` is empty).

### Revised claim sentence (what the three batches jointly support)

> Under a non-adversarial-analyst threat model — the analyst may alter the
> computation but runs an unmodified, instrumented harness — execution-trace
> receipts decide, from receipts alone and without re-running the computation,
> whether an expensive pseudo-C_l analysis was actually performed. In a sealed
> batch of 48 runs scored by decision rules frozen and committed before the seal
> was drawn, the verifier flagged 24/24 operator-skipping, operator-truncating,
> grid-reducing and cache-substituting runs (one-sided 95% lower bound 0.91) and
> 6/6 runs of the effective-multipole shortcut that had escaped the previous batch
> (lower bound 0.61), at 0/6 false positives on honest runs (one-sided 95% upper
> bound 0.39). The effective-multipole class is caught by a value-level rule that
> recomputes six receipt-selected rows of the coupling operator and tests the
> published bandpowers against the declared pseudo-spectrum — about 9% of the work
> of the analysis. Detection is established at class level, not per run. The
> metadata-forgery arm still escapes 6/6, and it escapes *because* the forgery is
> complete: the same rule that catches a shortcut taken by omission is defeated by
> one fabricated intermediate. Receipts of this kind are therefore a detector of
> shortcuts taken by an analyst who does not forge — not of forgery.
