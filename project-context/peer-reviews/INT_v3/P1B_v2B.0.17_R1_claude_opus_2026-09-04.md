# INT referee report — P1B v2B.0.17

- **PDF reviewed:** `site/public/papers/paper1b_namaster_proof_v2B.0.17.pdf`
  (NOTE: the requested path `..._namaster_proof_arxiv_v2B.0.17.pdf` does not exist
  in the repo; this is the only v2B.0.17 artifact present.)
- **sha256:** `0d0c92ab2b07add4f3de837c26d9ceff742b4931490a0d05c5a4fd4e4001fcac`
- **Pages:** 8 · **File size:** 451755 bytes · **PDF CreationDate:** 2026-09-04 18:51:29 PDT
- **Review date:** 2026-09-04
- **Referee:** independent INT leg, Claude Opus-tier, skeptical stance, no expected verdict supplied
- **Venue frame:** computational-reproducibility / astro-software methods
  (A&A Sec. 14 / JOSS-adjacent), assessed also against PRD-style rigour.
- **Scope of evidence used:** the PDF only, plus a narrowly-scoped inspection of
  `pipelines/namaster_proof/blind_test/` to verify specific claimed numbers (each
  such check is named explicitly in the findings below).

_(sections appended below as the review proceeds)_

## Summary

The manuscript is a software metapaper for `namaster-proof` 0.1.7, a small pure-Python
layer doing two things: (a) exact evaluation of a uniformly rotated [EE,EB,BE,BB]
spectrum through the complete NaMaster bandpower-window tensor (with a three-component
precontraction that makes grid evaluation cheap), and (b) atomic JSON publication with
SHA-256 content-bound sidecar receipts and fail-closed verification. Sections 1–5 and
7–13 are a competent, unusually honest JOSS/A&A-14-style software description: the
scope limits, the non-retained workspace tensor, the 39-vs-41 test split, the
untested-macOS status, and the "content binding, not a signature" caveat are all
disclosed at the right strength.

The paper's bid for novelty is Sec. 6: a pre-declared sealed blind test in which a
verifier that never re-runs the computation classifies 18 sealed runs, detecting 12/12
of four receipt-visible shortcut classes with 0/3 false positives, while a fifth
metadata-forgery class escapes 3/3 by design. The idea is genuinely good, the
"shortcut detector, not fraud detector" framing is the correct and honest one, and it
is held consistently across title, abstract, Sec. 6, and Sec. 10 — I checked and found
no place where the paper overclaims fraud detection.

But the experiment as reported cannot support the headline numbers. The decision-rule
set was amended after the outcomes were seen (two rules withdrawn, one of which would
have fired on 3/3 honest runs), and no fresh sealed batch was run under the frozen
amended rules; the shortcut classes were chosen by the same person who wrote the
verifier, and omit the one shortcut the paper's own Statement of Need calls "a common
shortcut"; the seal's temporal priority is not externally anchored (I verified the
digest reproduces, but sealed digest and run outputs entered git in a single commit);
the verifier as implemented uses a rule the paper does not describe; n=3 per arm
supports no "100%"/"0%" claim without an interval; the test exercises an in-house
spin-0 MASTER estimator, not NaMaster and not the spin-2 operator that is the
package's entire reason to exist — a fact absent from the abstract; and the manuscript
cites zero provenance/attestation literature, so a reader cannot situate the receipt
primitive against in-toto/SLSA, Sigstore, ReproZip, RO-Crate, or workflow-engine
provenance.

None of this is fatal to the software paper. Sections 1–5, 7–13 could be published
close to as-is. Sec. 6, as the paper's novel contribution, needs a re-run under frozen
rules, an external anchor, a related-work grounding, and abstract-level scope honesty
before its numbers can stand.

## Verdict

**major-revisions**

## MAJOR findings

### M1 — The decision rules were amended after the outcomes were seen; the reported 0% false-positive rate is therefore not a blind result (p. 4, Sec. 6, "Two corrections" + "Result")

The paper states the success criterion was pre-declared, then reports in the very next
paragraph that two rules were removed *because of what the run revealed*: the wall-time
floor "would have fired on 3 of 3 honest runs" and was "excluded from the decision rule
set", and the M-hash-collision rule was withdrawn as not evidential. Both amendments were
made on the same 18 runs from which 12/12 and 0/3 are then reported.

This is post-hoc rule selection on the test set. Under the rule set that was actually
pre-registered, the honest false-positive rate was 3/3 (100%), not 0/3 (0%). The paper
reports the amendment transparently — which is to its credit and is why this is
major-revisions rather than reject — but it still headlines 0% in the abstract and in
Table 2 as though it were the pre-declared outcome. A blind test whose rules move after
unblinding measures rule-fitting, not detector performance.

**Resolves it:** freeze the amended rule set (R1–R6 as implemented, wall rule dropped,
M-collision rule dropped), publish it, then run a *second, fresh* seal and a fresh batch
of runs and report that batch's confusion matrix as the headline result. The present
18 runs then become, honestly labelled, the rule-development/pilot round. If a re-run is
not possible, the abstract and Table 2 must report the pre-declared-rule outcome
(3/3 honest flagged) alongside the amended-rule outcome and must not lead with 0%.

### M2 — Seal priority is asserted, not externally anchored; "independently verified" overstates what was checked (p. 4, Sec. 6 "Protocol" step 2 and "Result"; p. 6 Sec. 10)

I verified the reproducible half of this claim: recomputing
`sha256(json.dumps(sealed/assignment.json, sort_keys=True))` returns
`0f4ca4ba8e431067c8d47e182264ccedb62a72a6a1c564e72ccbab653a4d5515`, matching
`public/sealed_digest.json` and the prefix quoted on p. 4, with `n_runs: 18`. The
assignment→digest binding is sound.

What is *not* established is the temporal claim that carries the whole blind design —
that the digest existed before any run executed. `public/sealed_digest.json` and
`public/runs/` entered version control in the *same single commit* (`d60949b7`,
2026-09-04, "run the blind shortcut-detection test and commit its artifacts"), so the
repository history contains no evidence of ordering. Sec. 10 concedes the seal is
"process-level ... not a cryptographic pre-registration against an external timestamp",
which is the right admission, but p. 4 simultaneously says "The seal was independently
verified" — and the verification performed (re-deriving the digest from the revealed key
via `reveal.py`) is neither independent nor a check on ordering. It confirms the
assignment was not edited after sealing; it cannot confirm sealing preceded execution.

**Resolves it:** (a) delete or rewrite "independently verified" to state exactly what was
re-derived; (b) for the M1 re-run, commit and push the sealed digest in its own commit
*before* any run artifact exists, and cite that commit SHA and its push timestamp in the
paper — or anchor the digest to an external timestamp (OSF registration, a public
transparency log, or an arXiv/Zenodo deposit of the digest alone). Two commits and a
quoted SHA cost nothing and convert this from an assertion to a receipt, which is
rhetorically important for a paper whose thesis is that receipts beat assertions.

### M3 — The implemented verifier applies a rule the paper does not describe, and the paper describes a rule the verifier does not apply (p. 4, Sec. 6 "Protocol" step 4 vs `blind_test/verify.py`)

Checked against `pipelines/namaster_proof/blind_test/verify.py` (named as permitted, to
verify the stated rule set):

1. Step (4) lists "an M hash collides across runs with differing input hashes" as a
   flagging rule. No such rule exists in `judge()` or `main()`. It was withdrawn per the
   corrections paragraph — but step (4), which purports to state the protocol as
   executed, still lists it. The two paragraphs contradict each other.
2. The implemented R6 rule is
   `digest == contract["reference_bandpowers_sha256"] or (prior and prior != map_sha256)`.
   The first disjunct — flag any run whose bandpower hash equals the *reference run's*
   bandpowers — is not described anywhere in the paper. It is materially stronger than
   the described rule ("a result hash repeats across runs with differing input-map
   hashes") and it is plausibly the disjunct that actually catches S4, since the
   cache-substitute variant would naturally return the reference result. A reader cannot
   reproduce the reported S4 detection from the paper's description of the rules.

**Resolves it:** replace step (4) with the verbatim rule list as implemented (R1 code
sha256, R2 ℓ-grid, R3 3j count, R4 coupling shape/support, R5 mask contract, R6 result
reuse — stating both disjuncts), remove the withdrawn M-collision rule from step (4) and
note the withdrawal only in the corrections paragraph, and state which rule fired for
each arm from `verdicts.json` rather than a prose summary.

### M4 — The four shortcut classes omit the shortcut the paper itself identifies as the common one, and are selected within the space the verifier can see (p. 2 Sec. 2 vs p. 3–4 Sec. 6)

Sec. 2 motivates the entire windows module with a specific real-practice shortcut: "A
common shortcut is to evaluate a theory spectrum at a representative multipole for each
bin" instead of applying the full window operator. That class does not appear in
S1–S5. The classes actually tested are operator-skipping, operator-truncating,
grid-reducing+interpolating, cache-substituting, and metadata forgery.

Two problems follow. First, the demonstration does not test the failure mode the paper
was written to prevent — a reader may reasonably ask whether a bin-centre/effective-ℓ
evaluation, which can leave the ℓ-grid, the 3j count and the coupling shape all
*correct* while producing wrong bandpowers, is visible to this verifier at all. On my
reading of the rule set it is not: nothing in R1–R6 inspects the *values* against the
contract. Second, S1–S4 are each detected by exactly the trace field instrumented for
them (3j count, ℓ-grid, coupling shape, result hash). With classes and verifier authored
by the same person, 12/12 is close to definitional rather than empirical. The paper needs
at least one class designed to be *hard* — e.g. bin-centre theory evaluation, an
analytic/approximate M, float32 downcasting, a reduced realization count in a covariance,
or truncating the coupling sum while keeping the full output ℓ-grid.

**Resolves it:** add the effective-multipole shortcut and at least one other
value-level-but-trace-clean class to the sealed batch; report honestly if they escape
(an escape is a *result*, and it sharpens the "shortcut detector" boundary from "catches
four classes" to "catches structural shortcuts, not value-level ones"). Also state
explicitly who selected the classes and when, relative to the seal and to the verifier's
authorship.

### M5 — n=3 per arm supports neither "100%" nor "0%"; no interval is given (p. 1 Abstract, p. 4 Table 2 and "Result")

The abstract reports "all 12 runs (100%)" and "a 0% false-positive rate", and Table 2
presents 3/3 cells. With 3 honest runs, the exact one-sided 95% upper bound on the
false-positive rate is ~0.63 (rule of three); with 12 detections the one-sided 95% lower
bound on per-class sensitivity is ~0.74. Reporting bare 100%/0% percentages on n=3 and
n=12 invites a reader to infer far more precision than exists.

Worse, the three replicates within an arm are not independent draws from a population of
shortcuts: each arm is one deterministic code variant executed three times with different
map seeds. Since R1–R4 compare code sha256, ℓ-grid, 3j count and coupling shape against a
fixed contract — none of which depend on the map seed — the three replicates of S1 are
guaranteed to produce identical rule firings. The effective sample size per class is 1,
not 3, and the paper should say so.

**Resolves it:** replace the bare percentages with counts plus one-sided Clopper-Pearson
bounds (e.g. "0/3 honest runs flagged; 95% upper bound on FPR 0.63"); state that
replicates within an arm are seed-varied executions of one deterministic variant and are
therefore not independent for the trace-comparison rules; and either enlarge n
substantially or reframe the result as a demonstration of *mechanism* ("each class fires
the predicted rule") rather than a *rate*.

### M6 — The blind test does not exercise NaMaster, and does not exercise the spin-2 operator that is the package's purpose; the abstract does not say so (p. 1 Abstract vs p. 4 "Scope limits", p. 6 Sec. 10)

Sec. 6's scope-limits paragraph and Sec. 10 both state plainly that the estimator
exercised is "this repository's own spin-0 MASTER implementation, not NaMaster itself"
because PyMaster is not installed in that environment. That disclosure is honest and
correctly placed in the body.

It is absent from the abstract, which says only that the verifier must decide "whether
each one actually performed the declared pseudo-Cℓ calculation" — in a paper titled
"...for pseudo-Cℓ computations", describing a package named `namaster-proof`, whose
Sections 3–4 are entirely about the spin-2 [EE,EB,BE,BB] window tensor. A reader of the
abstract alone will conclude the blind test validated the spin-2 NaMaster path. It did
not: it validated a spin-0 scalar path, and the instrumented Wigner-3j counter that
carries most of the detection power has no counterpart in an unmodified PyMaster. So the
central claim ("receipts detect shortcuts in pseudo-Cℓ computations") is demonstrated on
a code path that is neither the package's headline numerics nor the library it is named
after.

**Resolves it:** add one clause to the abstract — e.g. "demonstrated on an instrumented
spin-0 MASTER estimator standing in for NaMaster, which is not installed in the test
environment" — and state in Sec. 6 what specifically would have to be added inside
PyMaster (the paper says "an equivalent hook", which should be made concrete: which
function, what counter) to carry the claim over. Better still, install PyMaster and
re-run at least the honest and S1 arms through the real spin-2 operator, even at small
Nside; the paper already reports a working PyMaster environment for the Sec. 8 campaign,
which makes "PyMaster is not installed in this environment" read as an avoidable
limitation rather than a hard one.

### M7 — No related work on provenance/attestation; novelty is unlocatable (References, p. 8; Sec. 2 and Sec. 12)

The bibliography has four entries: Hivon+2002, Alonso+2019, Lewis+2000, Górski+2005 —
all pseudo-Cℓ/CMB infrastructure, none about reproducibility, provenance, or attestation.
For a paper submitted to a computational-reproducibility venue whose novel contribution
is a receipt primitive and an execution-trace contract, this is a structural omission.

The receipt/execution-trace idea has substantial adjacent prior art that a referee will
expect to see engaged: in-toto and SLSA (supply-chain attestation of "this artifact was
produced by this step"), Sigstore/Rekor (transparency-log anchoring, which is precisely
the external anchor Sec. 10 says is needed to close S5), ReproZip and Whole Tale
(execution capture), Snakemake and Nextflow provenance reports plus RO-Crate/W3C PROV
(workflow-level provenance metadata), MLflow (run tracking with parameter/artifact
binding), and the content-addressed-artifact pattern generally (Nix, Bazel remote
execution). Several of these already do content-binding of results to a declared step;
the sharper questions — what is genuinely new here versus what is a domain-specific
repackaging — cannot be answered by a reader from the current text.

To be fair to the paper: it does *not* claim "first of kind". Sec. 12 explicitly says the
receipt layer "is a small reusable module rather than a claim that the package is a
general provenance framework", which is appropriately modest. The problem is not
overclaiming; it is that with no related work at all, the reader cannot calibrate the
blind test's contribution either way.

**Resolves it:** add a short related-work subsection (half a page) placing the primitive
against attestation (in-toto/SLSA/Sigstore), execution capture (ReproZip), and workflow
provenance (Snakemake/Nextflow/RO-Crate/PROV), and state the delta explicitly. My reading
of the actual delta, which the paper should claim directly: existing tools attest *that a
declared step ran and produced these bytes*; this work adds a *semantic* execution trace
(3j count, ℓ-grid, operator shape) whose values are a measured consequence of the
numerical code path, so a referee can check that the *scientifically expensive part* was
performed — which supply-chain attestation does not address. That is a real and defensible
contribution and it is currently left implicit.

### M8 — The whole detector lives in the "asserted" trust tier, which Table 1 makes clear but Sec. 6 does not carry through (p. 3 Table 1, p. 3 "Execution-trace extension")

Table 1 is the best thing in the paper: it separates self-evident fields (recomputed from
result bytes) from asserted fields (caller-supplied). The text immediately below it
correctly notes that "Shortcut detection, below, lives entirely in the asserted row."

Sec. 6 then partly walks that back: the trace is described as "emitted by an instrumented
harness rather than typed by the analyst", which suggests a stronger trust tier than it
has. The harness runs on the analyst's machine under the analyst's control, and the code
sha256 in the trace is itself self-reported by that harness. The detector's power
therefore rests entirely on the assumption that the analyst modified the *compute module*
but not the *harness* — a narrow and somewhat arbitrary band of the threat space, which
the paper never states as such. S5's escape is the symptom; the underlying structural
point is that S1–S4 are detected only because the shortcut-taker was assumed to leave the
instrumentation honest.

**Resolves it:** state the threat model as an explicit assumption early in Sec. 6 —
"the analyst may alter the computation but runs an unmodified, trusted harness" — and
note that S1–S4 detection is conditional on it. This costs nothing, is plainly true, and
makes the shortcut/fraud boundary follow from a stated assumption rather than appearing
as a post-hoc concession.

## Minor findings

- **m1 (p. 4, Sec. 6 opening).** "a referee who cannot afford to re-run an expensive
  exact computation can, from receipts alone, decide whether the computation was actually
  performed or silently shortcut" — stated without the threat-model qualifier at the point
  of claim. The qualifier arrives a page later. Add "under the threat model of Sec. 6" or
  "for the receipt-visible classes" inline.
- **m2 (p. 4, "Protocol" step 2).** "assigns N runs to {honest, S1...S5} via
  HMAC(key, run_id)" understates the design: `seal.py` builds a fixed 3-per-arm multiset
  and HMAC-permutes it, so arm counts are balanced by construction, not randomized. Say
  "HMAC-derived random permutation of a balanced 3-per-arm design".
- **m3 (p. 2, Sec. 2).** The effective-multipole shortcut is asserted to be "not generally
  identical" to the full operator and able to appear "as a parameter-recovery bias", with
  no number anywhere in the paper. Sec. 8 says the PyMaster example "records the result
  beside an effective-multipole shortcut comparison" but never reports it. Give the
  magnitude (max fractional bandpower deviation, or the induced angle shift in degrees) —
  it is the quantitative justification for the entire windows module and it is missing.
- **m4 (p. 5, Sec. 7).** 41 tests are reported with no coverage figure and no link to a CI
  configuration or badge. For a JOSS-adjacent venue both are conventionally expected. Add
  line/branch coverage and cite the workflow file.
- **m5 (p. 5, Sec. 7).** "maximum absolute difference of 1.41e-18" for the [4,20,4,1025]
  workspace: the caveats (tensor not retained, not a universal error bound, regenerable via
  `examples/rebuild_workspace_check.py`) are well handled. But 1.41e-18 is below double
  precision eps scaled to typical bandpower magnitudes, so the number is essentially
  "exactly zero up to rounding" — say that, rather than quoting three significant figures
  of what is numerically noise.
- **m6 (p. 4, "Result").** "∼1 minute, $0 marginal cost" and Sec. 11's "approximately one
  to two minutes" disagree slightly. Harmonize.
- **m7 (p. 4, "Two corrections").** "the shortcut arms ran 3–15× faster than honest ones,
  but a cold-cache honest reference run took 4.29 s against 0.08 s warm" — the cold/warm
  ratio (54×) dwarfs the shortcut signal (3–15×), which is a genuinely instructive point
  about why timing is unusable as a provenance signal. It deserves one more sentence
  generalizing it, since it is one of the paper's more transferable findings.
- **m8 (p. 7, Sec. 11 "Operating system").** macOS is listed as untested, yet the PDF's own
  producer metadata and the development environment are macOS. If the suite in fact runs
  there, say "exercised locally on macOS but not covered by CI" rather than "untested".
- **m9 (p. 4, Table 2).** The "Triggering rule(s)" column gives prose names; give the
  implemented rule identifiers (R1–R6) so the table maps onto `verdicts.json` and
  `verify.py` directly.
- **m10 (Sec. 6 / Sec. 11).** The paper cites the sealed digest prefix but not the SHA-256
  of `verify.py` itself. Since M1 turns on when the rules were fixed, publishing a digest
  of the frozen verifier alongside the sealed assignment digest would be the natural
  self-consistent move for a paper about content-bound receipts.
- **m11 (p. 4, "Result").** Table 2 reports arms but not per-run verdicts; `verdicts.json`
  exists and is small. Include it as a table or appendix so the 18 individual calls are
  inspectable without a checkout.

## Questions for the authors

1. Who selected the five shortcut classes, and at what point relative to (a) writing
   `verify.py` and (b) drawing the seal? Was the class list itself committed before the
   verifier's rules were written?
2. Can you produce any record — a push timestamp, a signed commit, a CI run — establishing
   that `public/sealed_digest.json` existed before the run artifacts? Both entered git in
   commit `d60949b7`.
3. Does the verifier detect a bin-centre/effective-multipole evaluation? If not (as the
   rule set suggests), does that not place the paper's own motivating shortcut outside the
   detector's reach, and should the abstract say so?
4. The implemented R6 flags equality with `reference_bandpowers_sha256`. Was S4 detected by
   that disjunct or by the cross-run-reuse disjunct? Would S4 still be caught if the
   substituted cache came from a non-reference run?
5. PyMaster 2.6 was evidently available for the Sec. 8 campaign. What prevents re-running
   the blind test's honest and S1 arms against the real spin-2 operator at small Nside?
6. What concrete instrumentation hook inside PyMaster would carry the 3j-count rule over —
   which function, and would it require patching compiled code?
7. Are the three replicates per arm ever capable of differing in R1–R4 firings, given those
   rules compare seed-independent quantities?
8. How does the execution-trace contract relate to in-toto attestation predicates? Could the
   trace simply be carried as an in-toto predicate and anchored in Rekor, closing S5 with
   existing infrastructure rather than new work?

## Integrity note

I reviewed only the named PDF (sha256 `0d0c92ab...4001fcac`, 8 pages, all read) plus, as
permitted, `pipelines/namaster_proof/blind_test/{seal.py,verify.py,sealed/,public/}` to
verify three specific claimed numbers — the sealed digest `0f4ca4ba...` (reproduces
exactly), `n_runs: 18` (confirmed), and the verifier's stated rule set (confirmed
discrepant, see M3); I read no review history, SSOT, or dispositions, was told no expected
verdict, and reached major-revisions from the manuscript and those checks alone.
