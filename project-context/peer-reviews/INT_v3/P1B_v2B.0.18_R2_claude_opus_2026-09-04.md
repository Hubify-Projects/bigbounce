# INT_v3 referee report — P1B (NaMaster execution-receipt proof)

- Reviewer: Claude Opus INT leg (independent, skeptical referee)
- Date: 2026-09-04
- Artefact reviewed: `arxiv/paper1b_namaster_proof.pdf`
- sha256: `354d63b2e672ba4084987d993e59b73fd457a020a6bb794895c6e1d5074f88d2`
- Identical (byte-for-byte) to `site/public/papers/paper1b_namaster_proof_v2B.0.18.pdf`
- Pages: 12 (all read). Producer pdfTeX-1.40.29, CreationDate 2026-09-04 19:42:50 PDT
- Venue frame: astro-software / reproducibility methods venue, PRD-level rigour
- Repo inspections: limited to numeric/commit-ordering verification in `pipelines/namaster_proof/blind_test/` (logged in the integrity note). Review history, SSOT and dispositions were NOT read.

## Summary

The manuscript documents `namaster-proof` v0.1.7 (a spin-2 window/receipt verification
package) and, in Sec. 6, reports a two-batch blind test of whether content-bound
execution receipts can detect that an expensive pseudo-C_l computation was silently
shortcut. Batch 1 (18 runs) is now correctly relabelled a pilot with its two post-hoc
rule amendments disclosed; batch 2 (35 runs, 7 arms x 5) is presented as the primary
pre-registered result: honest 0/5 flagged, structural classes S1-S4 flagged 20/20,
metadata forgery (S5) escaping 5/5 by construction, and effective-multipole (S6)
escaping 5/5 with no rule added afterwards. A related-work section positions the
receipt against in-toto/SLSA/Sigstore/ReproZip/Snakemake/Nextflow/RO-Crate/MLflow.

This revision is a substantial improvement over what the abstract itself describes as
the earlier state: the pilot's rule-fitting is disclosed and de-headlined, the S6
escape is in the abstract, the threat model is stated, and the scope is narrowed to
"structural shortcuts in instrumented steps". **The pre-registration mechanics check
out.** I verified them directly (see integrity note): the rules commit precedes the
seal commit, the seal commit contains no run output, and I re-derived the sealed
assignment from the revealed key and reproduced the committed digest
`c96b5bf1...` byte-for-byte. I could not falsify the ordering claim.

What remains are (a) statistical statements in the abstract that contradict the
paper's own independence caveat and that mislabel a 90% interval as 95%; (b) an
abstract sentence that misdescribes which estimator the numerical module uses and
that contradicts Secs. 8/9/12 on PyMaster; (c) a framing question about how much of
the 20/20 is independent evidence; and (d) several undefined or self-referential
cross-references. All are text-level, but (a) and (b) change headline claims, so I
cannot recommend acceptance in this revision.

**Verdict: major-revisions.**

## MAJOR

**M1 — The abstract's Clopper-Pearson bounds contradict the paper's own independence
caveat (Abstract p.1; Sec. 6 "Reporting counts", p.5).**
Sec. 6 states plainly that for rules R1-R5 "the five replicates within an arm are
seed-varied executions of one deterministic variant... effective independent n per
class is 1 for those rules, and the replicates measure firing reproducibility, not
sampling variance." If that is true — and it is: S1/S2/S3 are caught by R3/R4, which
compare seed-independent quantities against a fixed contract — then the binomial model
underlying a Clopper-Pearson interval on 20/20 does not hold, and the quoted lower
bound 0.861 is not a valid statement about detection probability. Yet the abstract
leads with "20 of 20 ... (one-sided 95% Clopper-Pearson lower bound 0.861)" and gives
no hint of the caveat. The same objection applies to the honest arm: "0 of 5 false
positives (upper bound 0.451)" is effectively 0/1 for R1-R5, since honest replicates
differ only by seed and R6 was the only seed-sensitive rule (and it fired 0 times on
honest runs).
*Resolves:* either drop the intervals from the abstract and report the design-honest
statement ("4 of 4 structural classes detected in every replicate; replicates measure
firing determinism, not sampling variance"), or keep an interval but compute it on the
quantity that is actually i.i.d. across the design — e.g. classes, n=4, one-sided 95%
lower bound 0.473 — and state in the abstract that within-arm replicates are not
independent for R1-R5. Do not let a bound survive in the abstract that the body
disowns two pages later.

**M2 — "95% interval [0.501, 0.807]" is a 90% interval (Sec. 6, "Reporting counts",
p.5).**
The two numbers are `lower95_one_sided` and `upper95_one_sided` from
`blind_test/public2/scorecard.json`. Two one-sided 95% bounds intersect to a
**90%** two-sided interval, not 95%. In a paper whose contribution is statistical
care about a detector's operating characteristics, this is a substantive error, not a
typo. A related framing problem: the pooled 20/30 "across all six shortcut arms" is
not an estimate of anything — its value is fixed by the arbitrary decision to include
two escape classes and four caught classes at equal replication, so it moves if one
adds a seventh class. It reads as a summary sensitivity and will be read that way.
*Resolves:* relabel as a 90% two-sided interval (or recompute a genuine 95% two-sided
CP interval), and either delete the 20/30 pooled figure or annotate it explicitly as
an artefact of the arm design with no external interpretation.

**M3 — The abstract misdescribes the numerical module as spin-0, and contradicts
Secs. 8/9/12 about PyMaster (Abstract p.1 vs Sec. 3 p.2, Sec. 8 p.7, Sec. 9 p.8,
Sec. 12 p.10).**
Two distinct problems in one abstract sentence ("it evaluates a uniformly rotated EE,
EB, BE, BB spectrum through the complete bandpower-window operator of an instrumented
spin-0 MASTER estimator in this repository (validated against NaMaster's couple-decouple
route on a synthetic workspace; not run against NaMaster or PyMaster itself)"):
1. The `windows` module contracts a user-supplied `[4, n_b, 4, n_l]` spin-2 workspace
   tensor (Sec. 3, Sec. 4). The in-house **spin-0** MASTER implementation is the blind
   test's instrumented estimator (Sec. 6 "Scope limits"), a different object entirely.
   As written the abstract tells the reader the package's headline numerical capability
   is spin-0, which is false and undercuts the paper's own physics.
2. "not run against NaMaster or PyMaster itself" is contradicted by Sec. 8 (a retained
   physical artifact with a `[4, 20, 4, 1025]` workspace and a 10^-10-gated equivalence
   check), Sec. 9 ("Real PyMaster integration", and a 500-realization campaign with
   PyMaster 2.6 / healpy 1.19.0), and Sec. 12 ("the retained physical validation used
   PyMaster 2.6"). The intended meaning is presumably "the blind test in Sec. 6 was not
   run against PyMaster, which is not installed in this environment," which is a much
   narrower and defensible statement.
*Resolves:* split the sentence. State that the window layer contracts a real spin-2
NaMaster workspace tensor and has been exercised against PyMaster 2.6 in the retained
production artifact (Sec. 8) and the integration example (Sec. 9); state separately
that the **blind test** was run on an in-house instrumented spin-0 MASTER estimator
because PyMaster is not installed in the test environment and carries no 3j counter.

**M4 — How much of "20/20 structural" is independent evidence, and is S4 a fair test?
(Sec. 6, Table 3, p.5.)**
Three concerns that together affect the strength of the headline claim:
1. S1 (operator skipped), S2 (operator truncated) and S3 (grid reduced) are all caught
   by the same trace mismatch — R3 (3j count) and R4 (operator shape/support) fire on
   every one; S3 additionally trips R2. These are not four independent detection
   mechanisms but essentially one: "the recorded operator-construction trace disagrees
   with the contract." S4 is caught only by R6, a second mechanism. So the demonstrated
   evidence is two mechanisms, each shown to be deterministic, not four.
2. S4's 5/5 is entirely the **reference disjunct** of R6 (`sha256(bandpowers) ==
   contract.reference_bandpowers_sha256`); the cross-run disjunct fired 0/5, which the
   paper reports honestly in Table 3 and I confirmed in `scorecard.json`. But that means
   the only realistic cache-substitution signal — a run reusing an *earlier blind run's*
   result — was never exercised. S4 as constructed substitutes the one result whose
   digest is published in the contract, i.e. the easiest possible case for the verifier.
   A cache-substituting analyst in the wild reuses a previous production result, not the
   reference-run bandpowers a referee already holds.
3. Consequently "flagged 20 of 20 runs drawn from four structural shortcut classes" is
   an over-strong summary of what was demonstrated.
*Resolves:* (i) say in Sec. 6 that S1-S3 share a detection mechanism and report the
mechanism count alongside the class count; (ii) either add a cache-substitution variant
that reuses a prior blind run's bandpowers (so the cross-run disjunct is exercised) or
state explicitly, in the S4 discussion and not only in the table, that the cross-run
disjunct is untested and that S4 exercises the reference disjunct only.

**M5 — The pre-registration is verifiable, but the paper does not tell a reader how to
verify it, and it slightly overstates what the freeze commit contains (Sec. 6
"Protocol", p.4; "Result (batch 2)", pp.4-5).**
The paper says the rule set "was frozen and committed alone, in its own commit, before
the seal commitment existed in the repository, and no rule was added, removed, or
edited between that freeze and the reveal." What the freeze commit `4451b135` actually
contains is one file, `RULES_v2_FROZEN.md` (87 lines of prose spec) — the executable
verifier `verify.py` is not in it, and `verify.py` **was** edited afterwards, in the
seal commit `28efa21c`. I checked the diff: it is a one-line change replacing a
hard-coded `public` directory with `sys.argv[1]`, with `judge()` and the R6 block
untouched, so the substantive claim survives. But a skeptical reader running
`git log -- verify.py` sees the verifier change after the "freeze" and has no way,
from the paper alone, to know it was plumbing.
Separately, no reader can reproduce the quoted digest `c96b5bf1...` by hashing
`sealed2/assignment.json` — that file hashes to `c8566d0e...`. The published digest is
`sha256(json.dumps(assignment, sort_keys=True))` (canonical form, no indent), per
`seal2.py::digest`. I reproduced it only after reading the source.
*Resolves:* add three sentences and a short "how to check this yourself" list: the
freeze commit contains the rules **specification**; `verify.py` was edited once between
freeze and seal for non-rule plumbing (name the commit and say what the diff is, and
that its post-seal digest `6a9acd70...` is the one pinned in
`public2/frozen_rules_digest.json`); and the sealed digest is over canonical sorted-key
JSON, not the on-disk file bytes, with the exact command a reader should run.

**M6 — "S3, open" and "S2, in progress" in Sec. 11 are undefined and collide with the
shortcut-class names (Sec. 6 p.6, Sec. 11 pp.8-9).**
Sec. 6 refers to "(Sec. 11, item S3)" and Sec. 11 writes "(S3, open)" and "(S2, in
progress)". No enumerated S1/S2/S3 limitation list exists anywhere in the manuscript —
these are dangling pointers into an internal tracker. Worse, S2 and S3 are already the
names of two shortcut arms (operator truncated; grid reduced + interpolated), so a
reader parsing "(S3, open)" naturally reads it as the grid-reduction class, which is
not open at all.
*Resolves:* delete the labels, or introduce an explicitly numbered limitations list in
Sec. 11 with names that cannot be confused with the shortcut classes (L1, L2, ...).

**M7 — The Statement of Need's motivating numbers are not traceable to any committed
artefact (Sec. 2, p.2).**
"a maximum fractional deviation of 1.66 and a median fractional deviation of 0.17 in
the decoupled bandpowers" is the number that justifies why S6 matters, and it is the
only quantitative claim in the paper with no artefact pointer. I searched
`pipelines/namaster_proof/` (scripts, `public2/` outputs, both manifests) and could not
locate either value or a script that emits them; every other headline number in Sec. 6
is traceable to `scorecard.json` or the commit trail.
*Resolves:* cite the script and the committed output that produce these two numbers, in
the same style as the rest of Sec. 6, or recompute and commit them.

## Minor

- **m1 (Abstract, p.1) — the novelty claim is scoped to a set of size one.** "to our
  knowledge this is the first pre-registered, sealed blind measurement of
  shortcut-detection sensitivity for pseudo-C_l execution receipts, including a negative
  class reported as an escape" is narrowed until it is unfalsifiable: nobody else has
  studied this object, so priority is trivially satisfied. It reads as a claim about
  literature coverage rather than about science. The genuine contribution — a quantified,
  pre-registered map of what a receipt-based check can and cannot catch, with the
  negative classes reported — is stronger without the flag. Recommend deleting "to our
  knowledge this is the first" and stating the contribution directly.
- **m2 (Sec. 6, pp.4-6) — self-referential cross-references.** "§6" is used repeatedly
  from *inside* Sec. 6 to point at Sec. 6: "S6 (effective multipole, §6)", "both are
  load-bearing — §6" (Table 2), "§6 gives its batch-2 count", "two of the rules were
  changed after batch-1 outcomes were seen (§6)". These resolve to the section the
  reader is already in. Replace with named paragraph pointers ("see *S6: the
  effective-multipole class escaped*") or subsection numbers.
- **m3 (Sec. 6, "Result", p.4) — the sealed window was ~34 seconds.** From the commit
  timestamps I read: rules 19:01:41, seal 19:04:15, outputs 19:04:37, reveal 19:04:49.
  The whole batch is one scripted sequence by one party. The ordering claim is unaffected
  and the paper already concedes "the reveal remains self-run", but a reader who checks
  the log will notice, and there is a specific residual attack the paper does not name:
  git history proves the order of *surviving* commits, not that no earlier attempt was
  run and discarded before the committed one. Recommend one sentence naming
  discard-and-retry as the residual gap that the OpenTimestamps anchor does not close
  either (OTS timestamps the sealed digest, not the absence of prior attempts) — a
  third-party rerun or witnessed environment is what closes it.
- **m4 (Sec. 6 "Scope limits", p.6) — the OpenTimestamps status is honest but should be
  dated and made checkable.** `public2/sealed_digest.json.ots` exists (875 bytes,
  2026-09-04 19:31). Give the reader the upgrade command (`ots upgrade`, `ots verify`)
  and say what a confirmed proof would and would not establish (existence of the digest
  before a block time — still not an external witness to the *execution*).
- **m5 (Sec. 6, "Protocol", p.4) — say where the pre-declared success criterion lives.**
  The criterion ("every arm of S1-S4 detected 5/5, honest 0/5 flagged; S5 expected to
  escape; no outcome pre-declared for S6") is in
  `blind_test/BATCH2_PREREGISTRATION.md`, which was committed in the seal commit
  `28efa21c` — before any run output, so the claim holds, but the paper does not cite the
  file or the commit. Cite both, as is done for the rules freeze.
- **m6 (Sec. 6, pilot paragraph, p.5) — pilot disclosure is nearly, but not quite,
  complete.** Two post-hoc rule changes are disclosed (wall-clock floor, M-hash
  collision). A third post-hoc change is not mentioned in the paper: the R6 *description*
  in the previous manuscript revision stated only the cross-run disjunct, and was
  corrected to match the code (which always contained the reference disjunct — I checked
  `verify.py` at `a07c496b`). No code changed, so this is a description fix, not a rule
  change — but since S4's entire 5/5 rests on the previously-undescribed disjunct (M4),
  the correction is material and belongs in the disclosure paragraph.
- **m7 (throughout) — no figures.** Four tables, zero figures, for a paper whose central
  result is a confusion matrix with intervals. A single figure — per-arm detection with
  the CP bounds, escapes marked — would carry the result better than Table 3 and is worth
  the space. Not blocking.
- **m8 (Sec. 8, p.7) — the 1.41e-18 scalar.** The paper is careful ("zero to
  double-precision rounding, not a fractional-error figure... the original bandpower
  magnitudes were not retained"), and the `rebuild_workspace_check.py` regeneration path
  is the right fix. Suggest stating the regenerated max|delta| once PyMaster is available
  in some environment, so the number in the paper is one a reader can match rather than a
  historical scalar plus a promise.
- **m9 (Sec. 7, p.6-7) — related work is adequate for the venue and correctly positioned.**
  in-toto/SLSA/Sigstore/ReproZip/Snakemake/Nextflow/RO-Crate/MLflow is the right set, and
  the "administrative vs. semantic trace" distinction is the correct axis. Two gaps worth
  a sentence each: (i) no citation to the trusted-computing / remote-attestation line
  (TPM measured boot, SGX/TDX attestation), which is the standard answer to "prove the
  computation actually ran" and would bound the S5 class properly; (ii) no mention of
  verifiable-computation / proof-carrying-computation work (SNARK-style), which is the
  cryptographic version of the exact claim being made. Neither is practical here, but a
  reader from the systems side will expect them named.
- **m10 (Sec. 12, p.10) — version-number paragraph is good.** The explicit statement that
  `v2B.0.18` is a manuscript revision and `0.1.7` is the software release, and that the
  two are not expected to agree, pre-empts the obvious confusion. Keep it.
- **m11 (Sec. 8, p.7) — "39/41 standalone-effective".** Stating the skip reason is right.
  Consider also stating that no coverage number is reported *because* no coverage tool is
  configured — currently the reader must infer that this is a deliberate abstention rather
  than an omission. (The sentence nearly does this; make it explicit.)

## Questions

1. Was the batch-2 sequence run exactly once? If any earlier full seal-run-reveal cycle
   was executed and not committed, that should be stated; if not, saying so explicitly
   costs one sentence and closes m3.
2. Why was the cross-run disjunct of R6 never exercised (S4 reuses the reference
   bandpowers, not a prior blind run's)? Was that a design choice or an artefact of how
   `variants2.py` constructs the cache substitution?
3. Sec. 2's 1.66 / 0.17 deviations: which script and which committed output produce them?
4. What is the smallest change to NaMaster/PyMaster that would carry the claim over —
   is an upstream 3j-evaluation counter feasible, or does the C implementation make the
   count unobservable without a fork? A sentence on this would make the Sec. 11 caveat
   actionable rather than terminal.
5. Is there a defensible reason to keep the pooled 20/30 figure at all (M2)?

## Integrity note

Artefact reviewed: `arxiv/paper1b_namaster_proof.pdf`, sha256
`354d63b2e672ba4084987d993e59b73fd457a020a6bb794895c6e1d5074f88d2`, byte-identical to
`site/public/papers/paper1b_namaster_proof_v2B.0.18.pdf`; 12 pages, all read.

I was told no expected verdict and read no review history, SSOT, or disposition file.
Repository inspection was confined to `pipelines/namaster_proof/blind_test/` for
number- and ordering-verification, plus one manifest file. Specifically I checked:

1. `git log --format='%h %ad %s' --date=iso -- pipelines/namaster_proof/blind_test/` —
   ordering confirmed: rules `4451b135` (19:01:41) -> seal `28efa21c` (19:04:15) ->
   outputs `27300504` (19:04:37) -> reveal `974e2859` (19:04:49) -> OTS `20c1fcbc`
   (19:31:53). The paper's quoted SHAs match, except that the manifest commit the paper
   names as `b3347c53` is not in this path's log (it presumably touches
   `reproducibility/manifests/`, which I did not inspect further).
2. `git ls-tree -r 28efa21c` under the blind-test path: the seal commit contains only
   `public2/sealed_digest.json` and `public2/frozen_rules_digest.json` — **no run
   output**, as claimed.
3. `git show --stat 4451b135`: one file, `RULES_v2_FROZEN.md`, 87 lines (basis of M5).
4. `git diff a07c496b 28efa21c -- verify.py`: 16 lines, one substantive line
   (`public = ROOT / (sys.argv[1] if ... else "public")`); `judge()` and the R6 block
   unchanged (basis of M5).
5. `git show a07c496b:.../verify.py`: the R6 reference disjunct was present from batch 1
   (basis of m6).
6. Independent re-derivation: `seal2.derive(bytes.fromhex(key.txt))` reproduces
   `sealed2/assignment.json` exactly and digests to
   `c96b5bf1d6d3dd3f6b8131e6260803bb2049e3481b9613b041091ac00a27e9ee`, matching the
   digest committed at `28efa21c` before any run output existed. **The seal holds.**
7. `shasum -a 256 verify.py` = `6a9acd705cb50ce1...`, matching
   `public2/frozen_rules_digest.json` and the paper's quoted `6a9acd70...`.
8. `public2/scorecard.json` vs Table 3: per-arm counts, rule attributions, R6 disjunct
   split (reference 5/5, cross-run 0/5), and `wall_would_fire` (honest 5, S6 5, S4 0) all
   match the text. Table 4's per-run arms match `sealed2/assignment.json` on spot-checks
   (runs 000/001/002 = S5/S3/S6).
9. Clopper-Pearson arithmetic recomputed by hand: 20/20 lower `0.05^(1/20)=0.8609`;
   0/5 upper `1-0.05^(1/5)=0.4507`; 12/12 lower `0.7791`; 0/3 upper `0.6316`. All as
   printed. The 20/30 pair `[0.5006, 0.8067]` is two one-sided 95% bounds — hence M2.
10. Sec. 2's 1.66 / 0.17: searched the pipeline directory and both manifests; not found
    (basis of M7).

I found no fabricated number and no misreported artefact. The escapes (S5, S6) are
reported in the abstract, the pilot's rule-fitting is de-headlined, and the negative
result is not buried — this is honest reporting. My MAJORs are about claim calibration
and reader-verifiability, not about integrity.

Nothing in this review was written to reach a predetermined verdict; no repo review
history was consulted before forming it.
