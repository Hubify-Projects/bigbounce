# Publication-readiness regression audit — 2026-07-14

## Executive conclusion

The portfolio did not broadly become scientifically worse. The apparent fall
from 90--99 readiness to 56--80 is mostly the combination of a non-comparable
review instrument, an inflated June baseline, a later scoring-formula change,
and bookkeeping defects. There were also real closure-introduced regressions
and previously missed defects, so the earlier universal-ready claim was not
reliable.

The strongest defensible high-verdict comparison is EXT11, not EXT17. EXT11
was still a contextual delta-review round, but its provider verdicts were raw
MINOR/ACCEPT results rather than post-hoc conversions. EXT17's advertised
18/18 ACCEPT was not a raw 18/18 board: the raw table contains 16 ACCEPT and 2
MINOR results, is itself mis-summed as 14/18, and then converts both MINOR
verdicts to ACCEPT during truth audit. One converted leg, P2 ChatGPT, explicitly
states that it reviewed stale v1.7.67 rather than the claimed v1.7.68 artifact.

Current exact-artifact reviews are materially stricter: fresh exact-artifact,
full-paper reads with content hashes, source commits, and venue/article profiles
recorded. They are not directly comparable to June browser-project delta or
"courtesy re-confirmation" prompts that reminded reviewers of earlier ACCEPTs.
Raw reviewer verdicts should therefore be treated as a noisy distribution, not
as the publication-readiness score.

## Normalized comparison

Provider order in every triplet below is **ChatGPT/OpenAI perspective · Grok ·
Gemini**. `A`, `m`, `M`, and `R` mean ACCEPT, MINOR, MAJOR, and REJECT. A dash is
a missing/non-comparable leg. EXT11 used browser reviews; the latest column uses
the most recent exact-artifact panel available on 2026-07-14. Historical
OpenAI-API legs are retained as raw diagnostic evidence, but under the corrected
policy they are not valid current board legs: the OpenAI perspective must come
from Codex/ChatGPT subscription CLI with API credentials unset.

| Paper | EXT11 artifact and raw verdicts | Latest exact artifact and raw verdicts | Normalized interpretation |
|---|---|---|---|
| P1A | v1A.0.73: `m · A · m` | v1A.0.122 exact board: `m · A · A` | The central claim remains supported. Codex found two bounded artifact/provenance minors: the pinned NJL artifact includes excluded `>M_Pl` legacy rows, and reader-facing artifact URLs still use mutable `blob/main` links. Human CQG editorial decision and immutable archival remain open gates. |
| P1B | v1B.0.70: `m · A · A` | v1B.0.106 is canonical but dirty/in-flight and awaits a fresh board; last v1B.0.104 was `R · A · —` | No valid current three-provider comparison. Finish the in-flight artifact, freeze it, then review the proxy-scope rewrite and robustness evidence once on the exact v1B.0.106 PDF. |
| P2 | v1.7.64: `m · A · A` | v1.7.122 valid board: `A · A · A`, with ChatGPT supplied by Codex subscription | Manuscript algebra is accepted by the valid panel; direct cubic transfer, real covariance/likelihood, model applicability, DOI, and human PRD gates remain separate. |
| P3 | v3.1.107: `m · A · m` | Latest valid board remains r6: historical diagnostic `M · A · m`; the r7 attempt produced no valid verdict | Grok and Gemini failed closed on a commit mismatch, and the Codex output was marked failed/incomplete. Correct and freeze r7 before its first valid confirmation; do not count the failed attempt as a regression or review result. |
| P4 | v1.0.187: `A · A · A` | v1.0.243: historical diagnostic `M · M · m` | Real catalog-contract and release gates remain. The narrow observed-label null is supported; no physical/primordial upper bound is licensed. |
| P5 | v0.1.76: `m · A · m` | v0.1.130: historical diagnostic `R · m · m` | The exploratory catalog null remains plausible, but Paper-IV dependency, post-hoc positioning, covariance specification, archive, and label-bias power are real gates. |

EXT11 itself has a bookkeeping inconsistency: `site/src/data/reviewTimeline.ts`
records 10 ACCEPT and 8 MINOR, while
`project-context/peer-reviews/EXT11_BATCH_TRUTH_AUDIT.md` headlines 12 ACCEPT and
6 MINOR even though its per-paper ladder totals 10 and 8. The raw per-paper
ladder above is used because it is internally reconstructible.

## Why EXT17 and readiness 99 were inflated

1. **Verdicts were relabeled.** `EXT17_BATCH_TRUTH_AUDIT.md` converts two raw
   MINOR verdicts into ACCEPT. A truth audit may falsify a finding; it must not
   rewrite the provider's recorded verdict.
2. **A wrong artifact was counted.** `EXT17_P2_ChatGPT.md` says the reviewer did
   not receive v1.7.68 and reviewed cached v1.7.67. That leg is invalid for the
   v1.7.68 board, not an effective ACCEPT.
3. **The prompts were acceptance-anchored delta reviews.** EXT17 reports use
   phrases such as "courtesy re-confirmation," "prior ACCEPT stands," "frozen
   since EXT14," and "only remaining concern." These test a stated patch, not
   the whole paper under a fresh referee instrument.
4. **Artifact provenance was weaker.** The June browser round did not bind every
   leg to a recorded PDF SHA-256 and immutable packet. Current exact rounds do.
5. **Readiness mixed unlike concepts.** Packaging completion, clean compilation,
   closure streaks, truth-audited findings, and reviewer words were collapsed
   into one 99. Commit `097fada1` later retracted the 99/program-complete claim
   because the verified fresh board did not support acceptance.

## Genuine regressions and newly discovered old defects

The lower state is not entirely reviewer harshness.

- EXT11's own truth audit identifies closure-introduced P1A equation inversion
  and sphaleron-wording regressions, plus a P1B likelihood-name contradiction.
- P4's edge-on sensitivity penalty used Fisher square-root scaling for a naive
  retained-contaminant estimator that dilutes linearly. Commit `39b7aed1` fixes
  8.98% to 18.8%; the narrow null is unchanged.
- P3 carried a real Data Availability self-consistency defect, fixed in
  `e24b42a9`, and later exact reviews exposed catalog-contract and coordinate-
  lineage gaps missed by delta reviews.
- Later audits corrected over-broad framing and artifact/analysis claims across
  the portfolio: P1A mechanism-class independence, P1B proxy interpretation,
  P2 forecast/transfer scope, P3 catalog-grade scope, P4 probability/catalog
  contract, and P5 exploratory/pre-registration language.
- Some real defects were introduced by repeated closure waves themselves;
  `project-context/review-patterns/pattern-030-round-to-round-regression-drift.md`
  documents this failure mode.

These findings mean the old 99 was inaccurate. They do not mean every harsh
current MAJOR/REJECT represents a newly broken scientific result. For example,
the same byte-identical P4 v1.0.239 received Grok ACCEPT, MINOR, MAJOR, then
MINOR across repeated reads. `pattern-066-llm-referee-run-to-run-variance` is
direct evidence that single-sweep verdict words are unstable.

## Scoring and bookkeeping drift

- June readiness was largely ladder/static-state driven. The later formula in
  `tools/post_verdict.sh` uses `50 + latest reviewer points`, with ACCEPT 16.7,
  MINOR 12, MAJOR 6, and REJECT 0. The two numbers measure different things.
- The formula makes a random word-verdict swing move readiness even when the PDF
  hash and truth-audited finding set are unchanged.
- `project-context/PROCESS_AUDIT_2026-07-14.md` documents wrong caps caused by
  stale row ordering, rich wave rows clobbered by single-verdict writes, and an
  INT/EXT reviewer-label collision. Fixes reduced but do not erase historical
  chart contamination.
- Wrong-paper, stale-PDF, prompt-echo, empty, and misfiled legs occurred. Such
  legs must be `invalid`/`failed` gaps, never zero scores or inferred verdicts.
- Venue changes are confounders: CQG Note, PRD Research, ApJS Catalog/Methods,
  and AJ Observational prompts impose different standards and must not share a
  single unqualified trend line.

## Strict anti-loop policy

### Stable gate readiness

Track five explicit gates per paper, each backed by immutable evidence:

1. **Scientific correctness:** no open truth-audited blocker/major on the paper's
   claims.
2. **Reproducibility:** quantitative claims reproduce from committed artifacts;
   external-data limitations are explicit.
3. **Manuscript/venue fit:** the frozen artifact meets the declared venue and
   article-type contract.
4. **Release integrity:** exact source, PDF, supplement, manifest, archive, and
   public mirrors are checksum-bound.
5. **Human/workflow:** author sign-off, identifiers, submission, and actual
   editor/referee decisions.

Stable readiness changes only when evidence changes one of these gates. It does
not fall merely because a new model repeats a standing disclosed limitation or
uses a harsher verdict word on the same hash.

### Raw reviewer distribution

Store every valid provider verdict verbatim as a separate distribution indexed
by `(paper, PDF SHA-256, source commit, venue profile, prompt hash, provider,
resolved model, modality)`. Never relabel a raw verdict after truth audit. Show
invalid/missing legs as gaps. This distribution is diagnostic evidence, not the
readiness percentage.

### Content-hash stop rule

1. Review a unique packet/provider/profile tuple once.
2. Truth-audit every finding and close only verified reader-visible defects.
3. Re-review only after the reader-visible PDF SHA-256 changes, or for one
   explicitly declared independent confirmation of a high-risk closure.
4. If two valid independent waves on the same content hash produce zero
   genuinely new reader-visible findings, stop. Preserve the verdict spread and
   advance based on stable gates.
5. Do not edit solely to chase a repeated verdict word or a known disclosed
   limitation. Route irreducible venue, external-data, archive, and human gates
   to their owners.
6. A changed prompt, provider model, or venue profile starts a new measurement
   series; it does not overwrite the earlier series.

## Immutable PDF retention policy

Never delete or overwrite the only copy of a compiled paper artifact. Every
release/round compile must be retained under a version-and-PST-timestamped name
with paper ID, version, source commit, PDF SHA-256, page count, build command,
and review-round references in an append-only manifest. Alias paths may move to
the latest artifact, but the immutable versioned PDF remains in archival
storage. Before any cleanup, verify at least the canonical archive plus two
independent mirrors and record their hashes. Historical PDF deletion is a
release-blocking failure.

## Current next gate by paper

| Paper | Current next gate |
|---|---|
| P1A | Close the two Codex minors without changing the scientific claims: repin or label the NJL artifact so `>M_Pl` rows are explicitly excluded legacy diagnostics, and replace mutable `blob/main` artifact links with commit-pinned URLs. Freeze and archive the corrected artifact. Do not rerun merely to chase ACCEPT; allow at most one hash-changed confirmation if policy requires it. Human CQG editorial decision remains open. |
| P1B | Finish and verify the dirty/in-flight v1B.0.106 exact-window robustness artifact, freeze and archive it, then run its first fresh standalone exact-PDF board. |
| P2 | Preserve the valid v1.7.122 ACCEPT board; do not chase more model verdicts. Track cubic transfer, real covariance/likelihood, fermion/torsion applicability, immutable archive, and human PRD decision as separate gates. |
| P3 | Correct the r7 commit mismatch, verify and freeze the v3.2.0-r7 primary/auxiliary/AAS-table bundle and catalog contract, archive all PDFs, then run its first valid exact ApJS confirmation. Keep r6 as the latest valid board until that succeeds. |
| P4 | Close the catalog schema/filter/example contract and quarantine/reconstruct unsafe probability columns; freeze/archive the release and run one exact ApJS confirmation. |
| P5 | Resolve exploratory positioning, Paper-IV label dependency, covariance specification, selection-matching scope, and release contract; freeze/archive and run one exact AJ confirmation. |

## Primary evidence

- `project-context/peer-reviews/EXT11_BATCH_TRUTH_AUDIT.md`
- `project-context/peer-reviews/EXT17_BATCH_TRUTH_AUDIT.md`
- `project-context/peer-reviews/EXT17_P2_ChatGPT.md`
- `project-context/peer-reviews/REVISION_TRACKER.md`
- `project-context/PROCESS_AUDIT_2026-07-14.md`
- `project-context/review-patterns/pattern-066-llm-referee-run-to-run-variance-DRAFT.md`
- `tools/post_verdict.sh`
- commits `088cb674`, `097fada1`, `39b7aed1`, and `e24b42a9`
