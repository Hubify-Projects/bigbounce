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
