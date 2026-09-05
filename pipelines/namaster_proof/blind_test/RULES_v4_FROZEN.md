# Frozen verifier rule set v4 — namaster-proof blind shortcut detection

**Frozen:** 2026-09-05, BEFORE the batch-4 scripts are written, BEFORE the
verifier-seed commitment is drawn, BEFORE the batch seal is drawn, and BEFORE any
batch-4 run output exists. Committed alone, in its own commit, so the repository
history shows the rules were fixed first.

**Why v4 exists.** The R3 referee report on P1B v2B.0.20
(`project-context/peer-reviews/INT_v3/P1B_v2B.0.20_R3_claude_opus_2026-09-05.md`)
raised three design MAJORs against R7:

* **M1 — R7's challenge is prover-chosen.** `verify3.py::spot_rows` derives the
  six spot rows as `sha256(mask_sha256 ‖ sha256(bandpowers) ‖ salt)`, a public
  function of two values the runner holds *before publishing anything*. R7's
  claimed property ("cannot be chosen by the runner") is the wrong property:
  unchoosable is not unpredictable. An R7-aware S6 runner has already built the
  full operator `M` (that is why R3/R4 never fire on S6), so it can compute the
  six rows and write a `pseudo_cl` exact on exactly those rows at **zero
  marginal cost**. In Fiat–Shamir terms R7 is a transform applied to a
  prover-chosen commitment, which does not satisfy the transform's soundness
  condition.
* **M2 — R7 fails OPEN.** `r7_residual` returns "does not fire" when
  `intermediates.pseudo_cl` is absent or malformed, and again when the rebuilt
  mask hash mismatches. Omitting the intermediate silently disables the only
  value-level rule, in a package whose selling point is fail-closed verification.
  No batch-3 arm exercised that path.
* **M3 — arithmetic.** The batch-3 structural pool is S1, S2, S3, S4, S4b = five
  arms x 6 = **30/30**, not 24/24; the one-sided 95% lower bound 0.905 already
  corresponds to n = 30. Corrected in the batch-4 note. Batch 4 additionally
  reports **class-level detection only** — counts per arm, no run-level
  Clopper–Pearson intervals — which is the treatment the R2/R3 audits asked for
  and which removes the batch-2/batch-3 inconsistency at the source.

v4 = v3's R0–R7 verbatim, plus one new rule **R8**, plus two new arms `S7` and
`S8` that attack R7 at exactly the two points M1 and M2 identify.

---

## R0–R7 — unchanged from v3

Carried over verbatim from `RULES_v3_FROZEN.md` (R0 receipt invalid, R1 code
mismatch, R2 grid mismatch, R3 3j-count mismatch, R4 operator shape/support
mismatch, R5 input-contract mismatch, R6 result reuse under both disjuncts, R7
receipt-bound operator-consistency residual). R7 is **retained unchanged and
fail-open on purpose**, so batch 4 measures the size of the defect M1 and M2
describe instead of hiding it: `S7` and `S8` are pre-registered to escape R7.
The withdrawn rules stay withdrawn (wall-clock floor advisory only; M-hash
collision non-evidential).

## R8 — post-commitment verifier challenge (NEW, value-level, fail-closed)

**Threat model addressed.** A *rule-aware* analyst: it knows R0–R8 verbatim, it
runs the instrumented harness, and it adapts its published receipt to whatever
it can predict. R7 gives such an analyst a free pass; R8 does not.

**Protocol (commit–run–reveal).**

1. **Verifier commitment (before the batch).** The verifier draws 32 random
   bytes `sigma` and publishes `sha256(sigma)` alone, in its own commit, before
   the batch seal is drawn and before any run exists.
2. **Run and publish.** The runner executes and publishes, for each run, its
   result `C` (bandpowers) plus a receipt containing `inputs.mask_sha256`, the
   operator hash `intermediates.coupling_sha256` (the M-hash), and the declared
   pseudo-spectrum `intermediates.pseudo_cl` (`p`). The verifier then binds each
   run with a **bound receipt digest**
   `D = sha256(inputs.mask_sha256 ‖ coupling_sha256 ‖ band_hash(C) ‖ band_hash(p))`
   and commits `public4/receipt_digests.json`.
3. **Reveal.** Only after every receipt and every `D` is committed does the
   verifier reveal `sigma`; anyone can check `sha256(sigma)` against the
   commitment made in step 1.
4. **Challenge.** Rows are drawn as
   `h = sha256(sigma ‖ run_id ‖ D ‖ salt)`, taking the first `K = 6` distinct
   values of `LMIN + (h[4i:4i+4] mod (lmax + 1 - LMIN))`, `LMIN = 2`.
5. **Test.** The verifier rebuilds the survey mask deterministically, requires
   `sha256(mask) == contract.mask_sha256`, recomputes **only those K rows** of
   `M` from the mask power spectrum (~9% of a full build), and fires
   `R8_post_commitment_challenge` iff for any challenged row `l1`
   `| sum_{l2 >= LMIN} M[l1,l2] C[l2] - p[l1] | > TOL * ||p[LMIN:]||_2`,
   with **`TOL = 1e-6`**, the v3 tolerance, unchanged and re-used deliberately
   (its calibration in `RULES_v3_FROZEN.md` — `kappa(M[2:,2:]) = 1.28`, honest
   relative residuals ~1e-12, S6 residuals ~1e-1 — is a property of the honest
   solve, not of batch-3 data, and no batch-4 datum informs it).

**Randomness source, in order of preference, declared before the batch.** (a)
The Bitcoin block hash of the OpenTimestamps attestation of the batch receipt
digest, if a *confirmed* attestation exists at challenge time — this makes the
challenge depend on randomness that did not exist when the runs were made. (b)
Otherwise the commit–reveal `sigma` above. Bitcoin confirmation of a stamp made
after the receipts are published takes hours, so (b) is the operative source for
this batch and (a) is recorded as the drop-in upgrade; the security argument is
identical (post-commitment randomness the runner cannot have known), the trust
assumption is not (b) trusts the verifier not to have leaked `sigma`, (a) trusts
no one). Which source was used is recorded in the scorecard.

**Fail-closed.** Unlike R7, **R8 never abstains.** If `pseudo_cl` is absent,
malformed, non-finite, or the wrong length; if `coupling_sha256` is missing; or
if the rebuilt mask does not hash to the contract's mask, R8 fires with the
reason attached and the run's call is `shortcut`, verdict tag
**`SHORTCUT-SUSPECT`**. A missing contract-declared intermediate is itself a
verdict, never a pass.

### Why an honest runner passes and a shortcut runner fails

An honest run computes `p` as the measured pseudo-spectrum of the map it
analysed and returns `C` solving `(M[2:,2:] + 1e-12 I) C = p`. Its residual
`M C - p = -1e-12 C` is of order `eps * kappa(M) ~ 1e-12` **on every row
simultaneously**, so it passes for any challenge set — the honest party needs no
knowledge of `sigma`. This is one-sided soundness: R8 has no false-positive
channel that an honest solve can enter (the three residual channels enumerated
in `RULES_v3_FROZEN.md` — numerical excursion, cross-environment `anafast`
irreproducibility, heavier-than-1e-12 ridge — carry over verbatim and are
declared here rather than rediscovered).

Conversely, any operator-level shortcut produces a published pair with
`p != M C` on generic rows. Let `f` be the fraction of rows on which the
published pair happens to agree to within `TOL`. R8 misses only if all `K`
independently drawn rows land in that set, i.e. with probability `f^K`; for
`K = 6` and the batch-3 measured S6 disagreement pattern `f` is far below 1.
This is **Freivalds' probabilistic verification of a matrix product**
(R. Freivalds, *Probabilistic machines can use less running time*, IFIP Congress
1977, pp. 839–842): verify `A B = C` by testing a random projection instead of
recomputing the product, with one-sided error and no false rejection of a
correct product. R8 is the row-sampled variant of that test applied to
`M C = p`. The commit–reveal step is the **Fiat–Shamir** condition (A. Fiat and
A. Shamir, *How to prove yourself*, CRYPTO '86, LNCS 263, pp. 186–194) applied
correctly: the challenge is derived from randomness fixed independently of the
prover's adaptive choices, which is precisely the condition R7 violates. Both
citations belong in the paper's related-work section; their absence was the
referee's stated largest gap.

**Cost-of-evasion statement.** Against R7, a rule-aware S6 runner evades at zero
marginal cost (six entries of an `M` it already holds). Against R8 the only way
to satisfy an unpredictable row is to make `p = M C` on rows chosen after `p`
and `C` are fixed; making that hold on all rows *is* the honest solve. A runner
that fabricates `p := M C` wholesale (the S5 forgery class) still escapes R8 —
that limit is unchanged, declared, and is the reason the claim sentence says
these receipts detect shortcuts taken by an analyst who does not forge.

---

## Arms (batch 4)

Nine arms, **6 replicates each = 54 runs**: `honest`, `S1_skip_operator`,
`S2_truncate_operator`, `S3_grid_interpolate`, `S4_cache_substitute`,
`S5_metadata_forgery`, `S6_effective_multipole`, **`S7_r7_aware_effective`**
(new), **`S8_omit_pseudo_cl`** (new).

**`S7_r7_aware_effective`** is the M1 adversary made concrete: it runs S6
exactly (full operator genuinely built, shortcut downstream), then computes
R7's spot rows with `verify3.spot_rows` — the verifier's own function, from the
same mask hash and the same published-bandpower hash — and overwrites `p` on
exactly those six rows with `(M C)` there, leaving every other entry at the
honest measured value. It costs six entries of a matrix it already has.

**`S8_omit_pseudo_cl`** is the M2 adversary: an S6 run that simply deletes
`intermediates.pseudo_cl` from its receipt.

## Decision thresholds (batch 4, pre-registered)

- **Per-run call:** shortcut iff >= 1 of R0–R8 fires; honest otherwise. No
  aggregation, no scoring, no thresholding on rule counts. A run flagged only by
  R8's non-applicability branch is additionally tagged `SHORTCUT-SUSPECT`.
- **Reporting: class level only.** Per arm, batch 4 reports the **count**
  flagged out of 6 and which rules fired. **No Clopper–Pearson interval, no
  per-run detection probability, and no pooled interval is computed or quoted**
  — the R2/R3 audits are right that within-arm replicates are seed-varied
  executions of one deterministic variant, so the inferential unit is the class,
  not the run. Batch 4 therefore states counts and mechanism, and the batch-3
  intervals are reported in the note only with the corrected 30/30 arithmetic
  and the explicit caveat that they were run-level quantities.

### Pre-declared expectations

| Arm | Pre-declared expectation | Basis |
|---|---|---|
| honest | 0/6 flagged | honest solve satisfies every rule; R8 one-sided |
| S1, S2, S3 | 6/6 (R2/R3/R4, and R7+R8 residual) | trace fields diverge |
| S4 | 6/6 (R6 reference disjunct, R7, R8) | published reference digest |
| S5 | 0/6 — escapes | complete forgery incl. `p := M C`; declared structural limit |
| S6 | 6/6 by R7 **and** R8 | rule-unaware shortcut; batch-3 replication |
| **S7** | **0/6 by R7 (R7 defeated at zero cost), 6/6 by R8** | the M1 prediction this batch tests |
| **S8** | **0/6 by R7 (R7 fails open), 6/6 by R8 fail-closed** | the M2 prediction this batch tests |

S7's and S8's outcomes are *predictions* of rules written before this batch's
data existed. If R8 misses either, the miss is reported as the finding and no
rule is added afterwards.

- **No rule may be added, removed, or edited between this freeze and the batch-4
  reveal. Nothing is tuned after unblinding.** Anything found wanting becomes a
  batch-5 proposal.
