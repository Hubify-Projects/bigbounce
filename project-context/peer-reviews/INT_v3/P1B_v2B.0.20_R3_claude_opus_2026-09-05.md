# INT R3 referee report — P1B (NaMaster proof / execution receipts)

- Reviewer: Claude Opus INT leg (independent, skeptical; no expected verdict supplied)
- Date: 2026-09-05
- Artifact reviewed: `arxiv/paper1b_namaster_proof.pdf` (15 pp)
- sha256: `cf57f485c20acd8c5e9dc8277a65ca9a6ce1dac8db4b2e360be98845e7ee50cf`
- Identical to `site/public/papers/paper1b_namaster_proof_v2B.0.20.pdf` (same sha256, verified)
- Repo HEAD at review time: (see git log below)
- Scope of repo inspection: ONLY `pipelines/namaster_proof/blind_test/` for three verifications
  (batch-3 commit ordering, sealed assignment, PyMaster cross-check numbers). No review history,
  SSOT, or disposition files were read.

## What I verified independently in the repo

1. **Batch-3 commit ordering** (`git log --format='%h %ad %s' --date=iso -- <blind_test paths>`):
   `dcf96696` freeze RULES_v3 (R0–R7) → `d03fe376` pre-registration + scripts → `b19b72fc` seal
   (attempt 1) → `60917635` ABORT note → `56ef3fd2` harness fix (`variants3.seed_rng`) →
   `c7fb5e38` new seal → `4a7f9f82` 48 runs + blind verdicts → `5b643fc2` reveal + scorecard →
   `bf7d26e3` OTS anchor. The ordering the paper relies on is real and checkable.
2. **Sealed assignment**: `sha256(json.dumps(sealed3/assignment.json, sort_keys=True))` =
   `abfe2793bc6fa2c0…`, equal to `public3/sealed_digest.json:assignment_sha256` and to the
   value quoted in §6. Arm counts are exactly 6 per arm across 8 arms (48).
3. **PyMaster cross-check numbers** vs `pymaster_crosscheck_result.json`: coupling max/median rel
   diff 4.25e-13 / 6.43e-14 and bandpowers 1.54e-12 / 1.25e-12 — Table 5 reproduces the artifact
   exactly; per-band S6 errors 0.2316–1.1775 match the quoted "0.23–1.18".
4. Additionally read `verify3.py` (R7 implementation), `BATCH3_PREREGISTRATION.md`,
   `BATCH3_ABORT_NOTE.md`, `public3/scorecard.json`. No review history, SSOT, or disposition file
   was opened.

## Summary

A software metapaper (JORS-shaped section structure) whose centre of gravity has moved to a
genuinely interesting measurement: how well content-bound execution receipts detect silently
shortcut pseudo-C_ℓ computations. The blind design is real — frozen rules in their own commit,
sealed assignment committed before any output, per-batch reveal in commit order, and now a
Bitcoin-attested OpenTimestamps anchor for the batch-1/2 seals. The honesty posture is unusually
good: batch 1 is demoted to a pilot with its post-hoc rule changes named, negative classes are
reported as escapes, the metadata-forgery arm is declared unclosable by construction, the
in-house-estimator scope limit is stated, and the aborted batch-3 attempt is preserved and
explained. The PyMaster 3.x cross-check is a real and welcome addition that removes the "is the
instrumented estimator even right?" objection.

The remaining problems are concentrated in one place: **R7's security claim**. R7's "spot rows"
are derived by a public deterministic function of quantities the runner itself produces, so they
are perfectly predictable to the runner at write time. That does not invalidate the 6/6 number —
which correctly measures a *rule-unaware* S6 variant — but it does invalidate the sentence
"cannot be chosen by the runner" as a statement about evasion, and it means an R7-aware
effective-multipole runner (which already builds the full operator) evades R7 at **zero** marginal
cost, not at the "one matrix-vector product" cost the paper attributes to the informed forger.
There is also a fail-open path in the implementation, a batch-2/batch-3 inconsistency in how
Clopper–Pearson intervals are used, an arithmetic slip in a pooled count, and abstract/body text
that still says the protocol was "run in two batches". All are fixable without new experiments;
one warrants a two-line code guard and a re-run of `verify3.py` over the existing public3 tree.

**Verdict: major-revisions.**

## MAJOR

**M1. (§6, p. 7, "Batch 3: a value-level rule (R7)"; also Abstract) R7's spot rows are
predictable to the runner; the stated unpredictability property is wrong, and the informed-evasion
cost is overstated.**
*Issue.* The paper says the rows "depend on the run's own result and cannot be chosen by the
runner". `verify3.py::spot_rows` computes them as
`sha256(mask_sha256 ‖ sha256(bandpowers) ‖ salt) mod (lmax+1-lmin)` — a public function of two
values the runner holds *before it publishes anything*. Unchoosable is not the property that
matters; **unpredictable** is, and R7 has none. Concretely: S6 builds the full operator honestly
(that is why R3/R4 never fire on it), so an R7-aware S6 runner computes its C, computes the six
rows, and writes a `pseudo_cl` that is exact on those six entries and effective-multipole
everywhere else. That costs it nothing — the rows are rows of an M it already built — so R7 does
not move S6 into the "requires deliberate fabrication of a recorded intermediate" class in any
cost-meaningful sense; it moves it into "requires six correct entries". The runner can also grind
the low bits of a bandpower to reshuffle the draw at negligible cost. This is exactly a
Fiat–Shamir transform applied with a *prover-chosen* commitment: the challenge must be derived
from a value the prover committed to **before** it could adapt, or from a verifier-side nonce.
*What resolves it.* Any one of: (a) rewrite the claim honestly — R7 detects a rule-unaware
shortcut and the 6/6 is an unadapted-adversary measurement; state the zero-cost adaptive evasion
explicitly beside bound (3), which currently understates it; (b) bind the row draw to a
verifier-side nonce or a public randomness beacon (drand/NIST) with a timestamp after the run's
receipt digest, which restores real unpredictability and is a small change to `seal3.py`/`verify3.py`;
(c) both, with (b) tested in a batch 4. Option (a) alone is sufficient for acceptance.
Please also cite the relevant prior art here: Freivalds' probabilistic verification of matrix
products (1979) is the direct ancestor of R7, and Fiat–Shamir (1986) is the transform whose
soundness condition R7 violates. Their absence is the single largest gap in §7.

**M2. (`verify3.py::r7_residual`; §5 and §11) R7 fails open on a missing or malformed declared
intermediate.**
*Issue.* `r7_residual` returns `(False, nan)` — i.e. "does not fire" — when
`receipt["intermediates"]["pseudo_cl"]` is absent or has the wrong length, and again when the
rebuilt mask hash does not match the contract. No other rule requires the intermediate to be
present. A shortcut that simply omits `pseudo_cl` therefore silently disables the paper's only
value-level rule, in a package whose §5 selling point is that verification "fails closed". Every
batch-3 arm happened to emit the field, so the blind test never exercises this path.
*What resolves it.* Make absence/malformation of a contract-declared intermediate fire (a new
disjunct of R0, or R7 firing on non-applicability), re-run `verify3.py` over the committed
`public3/` tree (verdicts are unchanged for all 48 runs, so nothing is unblinded), and note in §6
that this branch was fail-open in the version that produced Table 4. If the authors prefer not to
touch frozen code, state the fail-open behaviour explicitly in §11 as a known evasion.

**M3. (§6 batch-3 paragraph and Table 4; Abstract) The batch-3 interval claims contradict the
batch-2 statistical standard, and one pooled count is wrong.**
*Issue (a).* Batch 2 argues at length that within-arm replicates are not independent draws, that
effective n per class is 1, and that "no run-level detection-probability interval is claimed".
Batch 3 then quotes 0.607 (S6, from 6 runs of one arm), 0.393 (honest FP, 6 runs) and 0.905
(pooled structural) — all of which are Clopper–Pearson intervals whose n is the *number of runs*
— while simultaneously asserting "these are class-level detection rates, not per-run
probabilities". A bound computed with n = 6 runs is a run-level bound; calling it class-level does
not change what was computed. Either justify why R7's replicates are independent enough to be the
inferential unit (they do vary with the map, which is a defensible argument, and the abort note
even states the maps were fresh random draws — that argument should be made explicitly and
consistently) or drop the intervals as batch 2 did.
*Issue (b).* "Structural arms S1–S4b pool to 24/24 (lower bound 0.905)" — S1, S2, S3, S4, S4b is
**five** arms × 6 = **30** runs, and 0.05^(1/30) = 0.905 confirms the bound was computed for
n = 30. `public3/scorecard.json:detection_structural_S1_S4b` gives 0.905 for the five-arm pool.
The text's "24/24" is an arithmetic slip; it should read 30/30.
*What resolves it.* Fix the count to 30/30, and make the independence treatment identical in the
two batches (either intervals in both with a stated inferential unit, or none in either).

**M4. (Abstract, p. 1; §6 "Protocol, two batches", p. 4) The abstract and §6 still describe a
two-batch protocol while reporting three batches.**
*Issue.* The abstract says the protocol was "run in two batches", then two sentences later
describes batch 3. §6's subheading is "Protocol, two batches" and its body says "The protocol was
run twice", followed by a full batch-3 subsection. Batch 3 is also missing from the numbered
protocol steps (1)–(5), which describe the batch-1/2 loop only.
*What resolves it.* Rewrite the protocol paragraph for three batches (pilot / primary / value-level
extension), including where the aborted attempt sits, and make the abstract's framing consistent.

**M5. (§6, p. 7 "Attempt 1 was aborted"; §11) The batch-3 audit trail and the abort disclosure are
incomplete in three specific ways.**
*Issue.* (i) The paper gives the batch-2 commit-ordered trail in full (4451b135 → 28efa21c →
27300504 → 974e2859 → b3347c53) but gives **no** equivalent trail for batch 3, which is now the
headline result; only the two seal digests and the aborted commit `b19b72fc` appear. I verified
the batch-3 ordering myself (dcf96696 → d03fe376 → b19b72fc → 60917635 → 56ef3fd2 → c7fb5e38 →
4a7f9f82 → 5b643fc2 → bf7d26e3) and it is clean, but a reader should not have to reconstruct it.
(ii) `BATCH3_PREREGISTRATION.md` declares arms, replicates, rules and per-arm expectations but
declares **no abort or stopping criterion**; the decision to discard attempt 1 was therefore a
post-hoc researcher degree of freedom, and the paper should say so plainly rather than only
narrating the defect. (iii) The abort was decided from `public3_aborted/verdicts.json`, and that
verdict pattern is itself partially arm-informative (the note states the only runs clearing R7
were the ones fabricating p, i.e. the forgery arm was effectively identifiable). The reason this
does *not* damage the reported result is that a fresh key and a fresh assignment were drawn after
the fix, so nothing learned about attempt 1's mapping transfers — that sentence is the one the
paper needs and does not have. Attempt 1's assignment is also not published (only its outputs are),
so its blindness is not externally checkable; say so.
*What resolves it.* Add the batch-3 commit trail; state that no abort criterion was pre-registered
and that this is a disclosed post-hoc decision; state the fresh-key/fresh-assignment argument for
why attempt 1 cannot contaminate batch 3; note that attempt 1's assignment is retained but
unpublished. With those four sentences I have no residual doubt about batch-3 blinding.

**M6. (§12 Archive, p. 13) The paper's principal new evidence is not archived.**
*Issue.* The Zenodo deposits pin `packages/namaster-proof` at commit `0a587b58` (July 21, 2026)
and the manuscript source. Batches 2 and 3 — the sealed assignments, keys, run outputs, receipts,
verdicts, scorecards, OTS proofs, and `verify3.py` — live only under `pipelines/` on a mutable
GitHub branch. For a paper whose thesis is that provenance must be content-bound and externally
anchored, the blind-test corpus must itself be deposited immutably.
*What resolves it.* Deposit `pipelines/namaster_proof/blind_test/` (all three batches plus
`public3_aborted/`) as its own Zenodo record with a DOI, cite it in §12, and quote its
checksum. This is also what makes the OTS anchors independently useful.

## minor

1. **PyMaster version does not match the cited artifact.** Abstract, §6 and §12 say "pymaster
   3.0.1"; `pipelines/namaster_proof/blind_test/pymaster_crosscheck_result.json` records
   `"pymaster": "3.0"`. Either correct the manuscript to 3.0 (the value the run recorded) or add
   the conda package version to the artifact so the 3.0.1 string is bound to something. In a paper
   about content-bound claims this one should not be loose.
2. **Two broken cross-references to items that do not exist.** §2 cites "batch-3 science item S2
   (§11)" and §6 cites "(Sec. 11, item S3)", but §11 numbers its open items L1–L4 and states that
   it numbers them "independently of the shortcut classes S1–S6 to avoid collision" — so these two
   pointers both collide with shortcut-class names *and* resolve to nothing.
3. **§6 is one long unnumbered section with ~12 internal "(§6)" self-references.** Split it into
   6.1 protocol, 6.2 batch 1 (pilot), 6.3 batch 2, 6.4 batch 3, 6.5 abort, 6.6 scope limits,
   6.7 PyMaster cross-check, and point the cross-references at subsections.
4. **No per-run appendix for batch 3.** Table 6 gives batch-2 per-run verdicts; batch 3 (the
   headline) has none. Add the equivalent table, including the `r7_relative_residual` column that
   `verdicts.json` already carries — the ~10^-12 vs ~10^-1 vs ~10^-17 separation is the most
   persuasive single number in the paper and currently appears only in prose.
5. **The abstract is ~500 words and carries five numeric bounds.** For any of the candidate venues
   this needs cutting to roughly half, with the interval arithmetic left to §6.
6. **"`ots verify` requires a Bitcoin node, which this machine does not run"** (§6 Scope limits) —
   the OpenTimestamps client falls back to public block explorers when no local node is configured;
   please re-check and either report the attested block heights or state precisely which
   verification mode you declined to trust and why.
7. **Table 1 trust taxonomy should mention the fail-open case.** Given M2, "asserted" fields whose
   absence disables a rule are a third category, not a sub-case of "asserted".
8. **§9's 500-realization campaign** reports a per-realization σ for one injected angle only and
   says the other two "are expected" to be comparable. Either recompute (it is cheap and the seeds
   are deterministic) or drop the expectation clause.
9. **§8's 1.41e-18 scalar** is carefully hedged, but the sentence "zero to double-precision
   rounding, not a fractional-error figure, since the original bandpower magnitudes were not
   retained" would read better beside the `rebuild_workspace_check.py` regeneration sentence that
   follows two lines later.
10. **Software vs. manuscript version.** §12's explanation of 0.1.7 vs v2B.0.20 is good; note that
    R7, `variants3.py` and `verify3.py` are *not* part of released 0.1.7 — a reader installing
    0.1.7 gets no R7. Say where the batch-3 code lives relative to the release.
11. **§7 attribution.** Sigstore/Rekor is correctly identified as the missing anchor; add one
    sentence on why a transparency-log entry does not by itself close S5 (it anchors the receipt,
    not the trace's truthfulness), otherwise the paragraph reads as if S5 were nearly closed.

## Questions

Q1. Was any consideration given to deriving R7's spot rows from a value the runner commits to
*before* computing its bandpowers (e.g. the input-map hash plus a sealed verifier nonce released
at reveal time)? That would make R7 sound in the adaptive setting and looks like a one-line change
to the draw, at the price of one extra sealed field.

Q2. What is the expected R7 residual for a "semantically wrong but equally expensive" computation —
say a mask applied with the wrong pixel ordering? R7 would presumably pass it (M C = p is
self-consistent), which is worth one sentence in §11 alongside the existing hedge.

Q3. In batch 3, S1–S4b all fired R7 in addition to R3/R4/R6. Is R7's marginal contribution
therefore exactly one class (S6), and does that make the paper's four-mechanism claim now
three mechanisms (trace mismatch, result reuse, value residual) across seven classes?

Q4. The batch-3 arm S4b's cross-run disjunct fired 4/6 because two replicates substituted from a
run that was itself substituting (`sealed3/crossrun_sources.json` shows run_037 ← run_036, itself
an S4b source). Was the source-selection rule pre-registered, or was it "the immediately preceding
run id"? The paper should state it, since it determines whether 4/6 is a property of R6 or of the
arm construction.

Q5. Would the authors consider a batch 4 that includes an explicitly R7-aware S6 variant (M1)?
Reporting it as an escape would be a stronger paper than reporting 6/6 against an unaware one, and
it costs a few minutes of CPU.

## Integrity note

Nothing in this manuscript reads as engineered. The three things I checked in the repository —
the batch-3 commit ordering, the sealed assignment digest, and the PyMaster cross-check numbers —
all reproduce exactly what the paper states, including the digest-of-canonical-JSON subtlety the
paper flags for batch 2. The paper consistently reports its negative classes as negatives, demotes
its own most favourable batch (batch 1, 12/12) to a pilot, and discloses three post-hoc changes
including one documentation-only correction it was under no external pressure to volunteer. The
`24/24` slip (M3b) runs *against* the authors' interest (the true figure is 30/30), which is the
signature of an honest arithmetic error rather than a favourable one. The abort disclosure is
candid about the defect and preserves the invalid runs.

On the novelty question I was asked to assess: **the manuscript makes no explicit priority claim
at all** — there is no "first", "novel", or "to our knowledge" anywhere in the 15 pages, and §7
claims only that "the delta claimed here is narrower". If a tier-N3 "first pre-registered, sealed,
externally time-stamped blind measurement of shortcut-detection sensitivity for pseudo-C_ℓ
receipts" is intended, it is not in the paper, and I would advise against adding it in that form.
What is defensibly new is the *combination*: applying a sealed, pre-registered blind design with
an adversarial class taxonomy to measure what a provenance receipt does and does not catch, and
reporting the escapes. What is **not** new, and must be cited if any priority language appears:
blind/salted analysis in physics (Klein & Roodman 2005 and the CMB/SN practice it describes);
pre-registration as a methodology; commitment-then-reveal and public timestamping (OpenTimestamps,
Sigstore/Rekor, already cited); content-bound attestation (in-toto/SLSA, already cited); and above
all Freivalds-style randomized verification of matrix products together with the Fiat–Shamir
challenge-derivation transform, which are the exact prior art for R7 and are currently absent
(M1). With those citations in place the honest claim is "first such measurement for pseudo-C_ℓ
execution receipts", which is narrow, true, and enough.

## Venue

The manuscript's skeleton (Statement of Need / Implementation and Architecture / Quality Control /
Availability / Reuse Potential) is JORS's metapaper template, and as a software paper it is
comfortably above that bar. But §6 is now the paper: a measurement, with a pre-registration, a
seal, a confusion matrix and an adversary model. My recommendation is to submit the measurement
where it will be refereed as a measurement — **ACM REP (Conference on Reproducibility and
Replicability)** is the closest fit, with **Computing in Science & Engineering** or
**Nature Scientific Data / Data Science (IOS)** as alternatives — and to keep a short JORS or
JOSS software paper for the package itself, cross-citing. If the authors prefer a single
submission, JORS will take it as-is once M1–M6 are addressed, but the R7 result will get less
scrutiny there than it deserves. arXiv cross-list: astro-ph.IM primary, cs.SE secondary.

**Submittable?** Not in this revision — M1 (the R7 unpredictability claim), M3 (the interval
inconsistency and the 24/24 slip) and M4 (the two-batch text) would each be caught by a careful
referee on first read. All six MAJORs are text-and-one-guard fixes; none requires new science. A
v2B.0.21 that closes them is submittable.
