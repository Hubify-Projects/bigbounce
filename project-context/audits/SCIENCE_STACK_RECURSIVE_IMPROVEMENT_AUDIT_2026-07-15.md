# Science-Stack Recursive Improvement Audit — 2026-07-15

## Executive finding

The project has the right conceptual loop—archive findings, mine recurring causes,
promote them into prevention, preflight papers, review exact PDFs, truth-audit, close,
and re-review—but the loop is not presently an enforced system. Its most important
learning components are prose-only skills, their data feed is stale, their checks are
not mandatory in active dispatch, and their effectiveness is not measured. This is
why the campaign feels incremental: reviewers remain the first reliable executors of
many checks that the accumulated catalog should already perform before dispatch.

The fix is not another broad skill collection. Per `/skill-governor`, it is one
canonical HubStack learning-loop engine, one BigBounce adapter, one machine-readable
pattern schema, and fail-closed integration into the immutable review-packet gate.
That converts review rounds from the primary defect-discovery mechanism into a
residual-novelty test.

The initial audit phase was read-only. The implementation update below records the
subsequent gated-tool, regression-test, and paper-release closures. None of those
process improvements by itself increases a paper's readiness.

## Implementation update — 2026-07-15

The P0 architecture described below is now materially enforced rather than
read-only guidance:

- the canonical HubStack pre-review engine and finding-event ledger are live;
- `tools/bigbounce_preflight.py` emits and verifies a six-paper receipt binding
  HEAD, registry, rule catalog, engines, source/PDF hashes, versions, pages, and
  paper-specific artifact validators;
- internal, direct-provider, external-browser, and native-PDF dispatch routes
  require the matching receipt before provider work;
- P1B artifact-manifest verification and six-paper artifact crosscheck are hard
  gates;
- the first enforced proactive sweep found P1B manifest-base drift and P5's
  nonexistent frozen-join claim before rereview, and both became regression
  fixtures;
- `directive_g.sh` now uses registry-owned served aliases rather than an
  O(all-served-PDFs) hash scan that could miss already-drifted aliases.
- dispatch no longer evaluates the same six-paper receipt three times, and
  immutable packet contents no longer include a volatile receipt hash excluded
  from their key; measured P3 dry-run wall time fell 36.20 s -> 13.05 s (64%).
- SciStack commit `ba36b4c` adds the versioned
  `finding-receipt-inventory/v1` schema, fail-closed receipt/event count and
  SHA reconciliation, and `metrics --inventory`; the finding-event suite is
  **11/11 passing**. Known-pattern escape and closure-regression metrics are now
  executable, but are reported as live campaign metrics only when the explicit
  receipt inventory reconciles completely. BigBounce's historical receipt
  inventory is still incomplete, so no complete-history rate is claimed.
- the exact P4 v1.0.255 and P5 v0.1.134 non-Anthropic boards were truth-audited
  and closed as P4 v1.0.256 and P5 v0.1.135, with exact PDF/version/SSOT,
  Convex, mirror, retention, and site synchronization. P4 remains readiness 80
  and P5 remains 74; closure and synchronization do not erase standing science,
  release, confirmation-review, or human-review gates.
- P5's focal low-cluster-count inference now has a deterministic, retained
  sensitivity using the identical 145,766-row estimand and 50-cluster unit: a
  reduced `K=13` nuisance model with CR1 inference plus a seeded 99,999-draw
  Rademacher wild-cluster efficient-score test. It is explicitly a post-review
  corroborating sensitivity, not a preregistered replacement for the focal model.
- `tools/int_wave.sh --codex-only` now makes subscription-only retry routing
  explicit and overrides an inherited API-enabled setting; its regression test
  proves the direct-provider stub is not invoked.

One retry incident remains deliberately visible. The first P5 Codex transport
ended before a verdict. During the later subscription-backed retry, a mistyped
API-disable switch caused an unnecessary second Grok/Gemini direct-provider pass.
Both policy-authorized receipt pairs remain in the six-row manifest, but the
rolling `API_P5_*` paths were overwritten by the second pass, leaving the first
pair without distinct on-disk raw bodies. This is an archive-completeness gap,
not evidence of a complete wave, and is exactly the class of loss that the new
inventory reconciliation must fail closed on.

## Evidence update — 2026-07-16

The P1B physical-spectrum closure lane produced two additional process
accelerations before production:

- a local Apple-Silicon NaMaster 2.6 runtime was built with Homebrew GCC after
  Apple Clang correctly failed on the required OpenMP flag, providing a
  no-provider-mutation execution route while the RunPod live-deletion and
  retention gates remain closed;
- the first bounded smoke run exposed a previously latent multipole-contract
  error: spectra stopped at `LMAX=2*NSIDE`, bins extended to `3*NSIDE`, and
  `NmtField` silently defaulted to `3*NSIDE-1`. The suite now uses one tested
  field/bin contract whose final exclusive edge is `LMAX+1`, and the corrected
  smoke run passes the exact-window equivalence check at `1.626e-19`;
- canonical realization-level process parallelism preserves ordered seeds and
  produces scientific JSON identical to the serial route. At `NSIDE=256`,
  `N=8`, four workers reduced measured wall time from 23.11 s to 17.20 s
  (25.6%). The frozen production command uses eight workers with one OpenMP
  thread each.

These changes accelerate and de-risk the missing production run; they do not
constitute the 500-realization result and do not increase readiness.

The next computational-closure increment is now committed and packaged:

- commit `6bb2bc1e` closes the verified P4/P5 computational confirmation
  findings and adds deterministic science-contract validators. P4's primary
  shuffle is bound to the strict release-safe sample (`890,069` selected,
  explicitly zero unsafe rows), and every FSC harmonic leg is bound to the same
  checksummed `24,087`-pixel support. P5's focal `K=13` estimate is exercised
  under NSIDE `2/4/8` and 3-D clustering, while sparse strata fail closed rather
  than emitting unsupported clustered inference;
- the new P4/P5 contract checks are integrated into
  `tools/bigbounce_preflight.py`, with regression fixtures for support identity,
  draw counts, harmonic coverage, clustering intervals, sparse-cluster
  suppression, and the corrected interaction counterfactual;
- the complete `tools/tests` suite passes **136/136** on the committed
  computational release. The focused science/preflight suite passes **28/28**;
- commit `d9b5d42d` bumps P5 to `v0.1.138-2026-07-16` solely to remove an
  isolated arXiv-build equation overflow. The exact 41-page PDF is
  SHA-256 `3c47ccf75da20653c463557fc54fff50da01e1e6bde43a225f61c46cd50baaf0`;
  readiness remains 74 and no science result changes;
- commit `ad55a7bd` adds commit-bound P4 `v1.0.258` and P5 `v0.1.138` source
  bundles plus standalone proofs. Both compile under isolated safe extraction
  with zero errors, zero undefined references, zero overfull boxes, and the
  expected 25/41 pages;
- six-paper preflight receipt
  `project-context/peer-reviews/pre-review-checks/portfolio_20260716T082655Z.json`
  passes with core SHA-256
  `22c87743968363b8248bf299af5b0d17a940b844ae0c87742f06ee25d2d5c70c`.

This evidence completes the current strict all-paper preflight and P4/P5
packaging increment. It does **not** complete historical receipt ingestion,
campaign-wide archive reconciliation, machine-readable coverage for every
approved pattern, the cross-paper claim graph, two consecutive clean residual
waves, or all-six external/human release gates.

## Implementation checkpoint — 2026-07-16

### P1B architecture-escape increment — 2026-07-16

The review loop’s repeated standalone-JCAP novelty and fragmentation finding
has been treated as an architecture signal rather than another prose-edit
request. P1B is now a focused `v2B.0.0` software metapaper targeting the
Journal of Open Research Software, backed by the installable
`namaster-proof` 0.1.0 package, 19 automated tests, Python 3.10–3.13 CI, an
independent synthetic example, and the retained 500-realization physical
validation campaign. The legacy `v1B.0.112` computational companion and all
of its review evidence remain retained rather than overwritten.

The release also exposed and closed a reusable process defect:
`tools/directive_g.sh` previously discovered unversioned PDF mirrors only from
paths that already existed, so a major manuscript rename could publish only
versioned aliases. Both public paper roots are now mandatory mirror targets,
with a regression test. The final four-page PDF has zero LaTeX errors,
undefined references, or logged box warnings; all four pages pass visual
inspection; five release copies are byte-identical; retention and Convex
synchronization pass. Readiness remains 56 because the new architecture has
not yet earned an exact-PDF review board.

The first exact v2B.0.0 board then demonstrated the intended recursive loop:
Grok returned MINOR, while Gemini and subscription-backed Codex returned
MAJOR. Truth audit rejected two false or overstated findings but retained real
software defects that surface-only paper review missed: silent spectrum
padding/truncation, invalid statistical inputs, overbroad two-file provenance
guarantees, stale retained documentation, incomplete JORS structure, and
insufficient artifact binding. v2B.0.1 / package 0.1.1 converts these into
fail-closed code and regression coverage, increasing the package suite from
19 to 23 tests. This is a concrete example of review feedback becoming a
preventive rule rather than a one-off prose patch. The archive identifier and
independent real-PyMaster benchmark remain open, so no readiness increase is
taken.

The full audit plan is **not complete**. The defensible acceptance accounting is
against the 12 checklist gates below:

### Current recursive-improvement increment — 2026-07-16

The previously absent cross-paper claim graph now has a fail-closed executable
foundation:

- `project-context/claim-dependency-graph.json` defines the first five
  content-bound headline claims and ten dependency anchors;
- `tools/verify_claim_dependency_graph.py` validates safe repository paths,
  unique claim IDs, multi-surface coverage, literal and JSON-pointer evidence,
  and emits a content-addressed receipt;
- the graph currently binds the P4 catalog row count across P4/P5, the imported
  P4 Catalog-C monopole across P4/P5, and the P4 strict-primary sample,
  exact harmonic support, and P5 focal robustness sample against retained
  science receipts;
- `tools/bigbounce_preflight.py` now requires this graph as a portfolio
  validator, so a covered dependency drift invalidates the next immutable
  review packet;
- the focused claim-graph and portfolio-preflight suites pass **21/21**,
  including positive, literal-drift, JSON-drift, duplicate-ID, and
  single-surface failure fixtures.

This moves the headline-claim dependency-graph gate from **open** to
**materially partial**. It is not complete: P1A, P1B, P2, and P3 headline
claims; site, SSOT, Convex, figures, tables, and release artifacts; transitive
changed-claim traversal; and complete quantitative-claim coverage still need
to be added. No readiness credit is taken for this process increment.

- **2/12 acceptance gates complete:** packet binding to
  preflight/catalog/registry evidence; and fail-closed enforcement on active
  INT, direct-provider, and external-browser dispatch.
- **5/12 materially partial:** strict all-paper preflight, which now correctly
  fails on newly enforced unresolved P1B science contracts; machine-readable
  pattern coverage; deterministic regression fixtures for high-severity
  patterns; executable learning metrics
  whose campaign-wide interpretation remains inventory-gated; and exact
  PDF/version/SSOT/Convex/site/package synchronization for recent P4/P5
  increments rather than all six papers at submission-ready state.
- **5/12 still open:** complete historical receipt representation; 100%
  event/manifest reconciliation; a headline-claim dependency graph spanning all
  six papers and public surfaces; two consecutive exact-PDF residual waves with
  zero known-pattern escapes and zero genuinely new BLOCKER/MAJOR findings; and
  a final board whose only deductions are explicit human, venue, or
  external-publication gates.

Additional work after the first evidence update closed the truth-audited
P4/P5 residual confirmation findings as P4 `v1.0.259` and P5 `v0.1.139`.
Both exact PDFs passed all-page visual audit, isolated source-bundle proof,
six-paper preflight, site build, retention, mirrors, and Convex synchronization.
These closures strengthen the proactive science-contract layer but do not
complete the unchecked campaign-wide gates above. P4's strict-primary public
release overlay is being built as the next release-contract gate; until an
immutable provider revision is actually published and verified, it must remain
reported as in progress rather than complete.

The next release-contract increment is now complete locally as P4 `v1.0.260`.
The unchanged public catalog remains pinned to immutable HF revision
`db11023306ab4eed1d7727670bd78e127b7af17a`; a content-addressed strict overlay
binds the current selection, exact null, schema, checksums, and reproducer.
Twenty-two focused release/preflight tests and the complete 140-test repository
suite pass. The 25-page PDF passes directive-G, all-page visual audit, retention,
16 byte-identical mirrors, Convex synchronization, and isolated source-bundle
proof. The all-paper preflight at commit `13cd7e85` passes with core SHA-256
`3662fefcc9c91da1a3bcfcb1fb2265241a3cf6aeebf3ae0aaf1a3f151814893a`.

This increment also removed an avoidable packaging delay: the generic arXiv
builder previously assumed `pdflatex` was globally discoverable even though the
canonical paper compiler uses TinyTeX by absolute path. The builder now reuses a
PATH executable when available and otherwise resolves the canonical TinyTeX
binary fail-closed. P4's commit-bound v1.0.260 bundle then compiled in isolated
safe extraction with zero errors, undefined references, or overfull boxes.
Immutable provider publication of the strict overlay remains open because no HF
token was available; the dry-run receipt is not represented as publication.

Deployment verification also caught a public-mirror regression that a successful
site build did not expose: Vercel updated the status page but retained the
v1.0.259 bytes at the canonical PDF alias and routed the new v1.0.260 filename
to HTML. A direct CLI repair was rejected because the 75-GB worktree exposed
53,027 files, above Vercel's 15,000-file request limit. The CLI attempt was
stopped; no successful redeploy is claimed. The public P4 read/download links
now use the immutable GitHub commit artifact, independently verified as
33,925,512 bytes with the canonical SHA-256, while local and repository mirrors
remain intact. A future deployment-surface cleanup must build from a bounded
source set instead of uploading the full research worktree.

The receipt-inventory parser has now been expanded with regression fixtures for
the explicit formats actually present in the campaign: Markdown-wrapped
severity tags, numbered severity sections, exact severity-summary counts,
explicit clean-review variants, matching parsed/raw ACCEPT verdicts, alternate
verbatim-response boundaries, and explicit provider failures. The focused suite
passes **14/14**. On the reproducible git-tracked corpus, parseable coverage
improved from **169/264 (64.0%)** at the initial bounded migration to
**259/271 (95.6%)**, with **1,574** explicit findings, six honest parse gaps,
and six failed legs. A full-worktree recovery view also exposes 11 untracked raw
receipts rather than allowing a committed inventory to reference absent files.

This is a substantial archive-ingestion acceleration, but it does not close the
historical learning gate. The partially migrated P4 v1.0.254 Codex receipt has
now been completed from its one-to-one truth audit, and the complete P4
v1.0.253 three-provider board has also been migrated. The ledger now contains
21 events; the four affected receipts reconcile at 8/8, 4/4, 3/3, and 6/6.

A declarative batch importer now verifies truth-audit and raw-receipt hashes,
canonical inventory membership/counts, event schema and identity, and
idempotent append behavior. Its first retained batch migrated all 11 P5
v0.1.138 findings, separating four verified manuscript minors, four standing
release/scope gates, and three editorial opinions. The ledger now contains 32
events. A second declarative batch then ingested the complete P4 v1.0.255
three-provider board: 19 findings separated into seven verified correctable
defects, six standing limitations, and six stale, falsified, or editorial
items. The ledger now contains 51 events. Canonical reconciliation remains
incomplete at **27/259 receipts (10.42%)**, with 232 count mismatches, zero hash
mismatches, and zero orphaned event receipts.
Campaign-wide escape and closure-regression rates therefore remain unavailable
as complete-history metrics.

Later closure state no longer requires mutating immutable finding events. A
linked append-only closure ledger verifies the original finding ID, exact
closure commit, version, and evidence-file bytes and emits a generated effective
status projection. Its first four entries bind the verified P5 v0.1.138
manuscript minors to the v0.1.139 closure commit. This closes the archival
finding-to-fix traceability gap while preserving standing publication gates and
without inventing a confirmation review.

The next closure-ledger increment binds 12 verified P4 defects to their exact
historical correction commits and immutable evidence bytes: seven v1.0.253
findings closed in v1.0.254 and five v1.0.254 findings closed in v1.0.255.
Provider-publication findings additionally cite retained receipts whose remote
bytes and SHA-256 values were verified. The generated effective-status
projection now contains 16 closures total. Standing DOI, release, scope, and
human-review gates were not relabeled as closed.

The complete P4 v1.0.255 board is now also ingested and reconciled at 19/19.
Seven verified correctable findings are linked to the exact v1.0.256 correction
commit and evidence bytes, increasing the effective closure projection to 23
findings. Standing training-replay, transfer-calibration, joint-covariance,
metadata, DOI, and human-review gates remain deferred rather than being
misrepresented as manuscript closures.

The successful Gemini and Codex-subscription legs of the P4 v1.0.256
confirmation board are now ingested and reconciled at 4/4 and 5/5. Its failed
Grok leg remains an explicit failed gap and produced no invented events. The
ledger now contains 60 events, canonical receipt reconciliation is **29/259
(11.20%)** with 230 count mismatches, and two verified manuscript regressions
are bound to their exact v1.0.257 correction commit. The effective closure
projection now contains 25 findings. Standing science, metadata, archive, DOI,
and human-review gates remain deferred.

The complete P4 v1.0.258 three-provider board is now ingested at 13/13. It adds
five verified artifact-to-manuscript or disclosure defects, two standing
training/overlap gates, and six stale, falsified, or editorial dispositions.
All five correctable defects are bound to the exact v1.0.259 source bytes.
The ledger now contains 73 events, canonical reconciliation is **32/259
(12.36%)** with 227 count mismatches, and the effective closure projection
contains 30 findings. The closure tool now supports fail-before-write,
idempotent array append, removing a repeated manual command per finding while
preserving commit- and byte-level evidence validation.

The complete P1B v1B.0.109 three-provider board is now ingested at 12/12.
Its NaMaster raw-spectrum error, executed-BBN provenance mismatch, inconsistent
S8 burn-in, ALP estimand wording, full-EB limitation, and immutable-release
gate remain open rather than receiving paper-only closures. The ledger now
contains 85 events and canonical reconciliation is **35/259 (13.51%)** with
224 count mismatches. A new fail-closed P1B science-contract validator requires
hashed raw-$C_\ell$ CAMB EE and physical lensed-BB inputs with a 500-realization
production receipt, exact CAMB 1.6.5 BBN table provenance, a 30%-burn S8
receipt, corrected estimand language, and a version-matched manifest. Because
those evidence artifacts do not yet exist, current all-paper preflight now
correctly fails rather than certifying P1B for another review wave. This honest
gate regression reduces the currently complete acceptance gates from 3/12 to
2/12 until the P1B production closures are executed.

Evidence and exact outcomes are recorded in
`project-context/audits/PROACTIVE_PORTFOLIO_SWEEP_2026-07-15.md`. Readiness was
not increased by these process or release-integrity closures.

## Scope and evidence inspected

- Canonical stack rules: `~/.claude/scistack/CLAUDE.md` and
  `~/.agent-shared/claude-skills/skill-governor/SKILL.md`.
- HubStack learning loop: `cascaded-r-rounds`, `cross-vendor-r-round`,
  `paper-pre-review-check`, `peer-review-truth-audit`,
  `r-round-finding-archive`, `r-round-pattern-mine`,
  `review-integrity-audit`, and `revision-tracker-update`.
- HubStack infra: `scistack-self-update`, `qc-gate`, `loop-model-routing`, and
  `readiness-cap-99`.
- AstroStack campaign layer: `bigbounce-r-round`, `bigbounce-ready`,
  `bigbounce-truth-audit`, `bigbounce-close`, `drive-to-100-fire`, and
  `houston-method-v2`.
- BigBounce review and packet tools, tests, onboarding, SSOT, pattern catalog,
  findings archive, and readiness instrumentation.

Observed state at the initial audit, with subsequent changes called out:

- 93 catalog markdown files exist: 69 `pattern-*` (14 drafts), eight design,
  six packaging, and eight site patterns.
- `INDEX.md` says its last pattern-mine run was 2026-06-26.
- The most recent per-round structured finding archives are dated 2026-06-10,
  despite extensive July INT/EXT review activity.
- `ALL-FINDINGS.json` uses several historical aggregate schemas rather than the
  row schema promised by `r-round-finding-archive`; there is no top-level
  `findings` array to query uniformly.
- At initial audit, no executable scripts lived with any HubStack learning-loop
  skill. The canonical finding-event CLI, receipt inventory schema,
  reconciliation, and metrics now exist at `ba36b4c`; the broader
  ingest -> mine -> compile-rules -> preflight engine remains incomplete.
- The repo has no test that executes archive -> mine -> preflight -> dispatch.
- `paper-pre-review-check` is mentioned in runbooks but no canonical repo tool
  implements its advertised runtime behavior.
- `tools/check_new_patterns.sh` implements only a small fixed subset, hardcodes
  the retired `CODE_2025` root, and skips missing papers instead of failing.
- Multiple legacy review/metrics tools hardcode `CODE_2025`; the active repo is
  under `CODE_YOU`.
- `bigbounce-ready` still requires Anthropic/OpenAI SDKs and describes obsolete
  vendor policy, conflicting with the current Codex-subscription + direct
  Grok/Gemini contract.
- The immutable `review_packet.py` gate verifies source/PDF identity, but does
  not bind a preflight receipt, catalog version, prior-closure regression scan,
  or portfolio consistency scan.

## Root-cause architecture audit

### 1. The learning loop is descriptive, not executable

`r-round-finding-archive`, `r-round-pattern-mine`, and
`paper-pre-review-check` describe detailed workflows but ship no canonical
scripts. Agents must reinterpret long markdown instructions on every round.
The result is nondeterministic coverage, no stable output schema, no idempotency,
and no regression suite. A mandatory prose step is not a gate.

**Consequence:** July findings are not feeding the archive; promoted prevention
rules do not automatically run; a clean external round cannot prove that known
failure modes were preempted.

### 2. The feedback data plane is broken at archive ingestion

The catalog is richer than the executable prevention layer, while the archive
lags the actual review corpus by more than a month. `ALL-FINDINGS.json` has
schema drift: the documented per-finding row model is not its queryable top-level
shape. Mining thresholds such as “three findings across two papers” and
“six consecutive rounds” therefore cannot be reproduced mechanically from the
current canonical aggregate.

**Consequence:** pattern promotion is based on remembered/manual observations,
not a complete append-only event stream. Review lessons exist, but are not
guaranteed to become prevention.

### 3. Prevention is paper-local and regex-heavy, not portfolio-wide

The catalog correctly records cross-paper drift, abstract/body drift, artifact
contradictions, numeric pairing errors, and closure regressions. Yet there is no
single all-paper preflight that builds a claim graph and checks:

- the same named quantity across all six papers, abstracts, tables, captions,
  site data, SSOT, and artifacts;
- cross-paper citations, version pins, submission order, and “in preparation”
  status;
- every changed claim against its generating artifact;
- every prior closure against the current source/PDF;
- every abstract/conclusion statement against its body evidence anchor;
- changed regions plus semantic dependents after closure edits.

`tools/v3_pattern040_all_papers.sh` and `v3_pattern041_audit.py` are useful
point solutions, but there is no canonical portfolio gate composing them.

**Consequence:** defects are fixed at one call site while downstream and sibling
paper sites escape, producing the repeated N+1 closure-regression pattern.

### 4. Dispatch does not require proof of prevention

`review_packet.py` provides strong exact-PDF content addressing, but the packet
schema lacks:

- preflight receipt SHA;
- catalog snapshot SHA;
- source commit on which preflight ran;
- exact list/version of checks executed;
- closure-regression ledger result;
- cross-paper claim-coherence result;
- machine-readable waiver records.

The active `int_wave*.sh` and EXT submission flow therefore can launch a review
without cryptographic evidence that the prevention layer ran against the same
source and PDF.

**Consequence:** “mandatory pre-review” remains an instruction, not a fail-closed
property.

### 5. Skills overlap and policy drift undermine DRY/MECE

The generic `cross-vendor-r-round` contains obsolete BigBounce API routes and
vendor requirements while disclaiming them in warnings. `cascaded-r-rounds`,
`drive-to-100-fire`, and `bigbounce-r-round` each restate convergence semantics.
`bigbounce-ready` tests old dependencies. Historical details remain mixed with
active contracts in operative skill bodies.

Canonical ownership should be:

- **HubStack learning-loop:** generic event schema, mining, prevention compiler,
  truth-audit semantics, convergence metrics.
- **HubStack publishing:** compile/PDF/artifact/package/site gates.
- **AstroStack BigBounce adapter:** six-paper registry, provider policy,
  readiness gate, paper-specific checks, SSOT/Convex binding.
- **BigBounce repo tools:** project-ephemeral implementations/config and receipts.

Anything else should route to those owners rather than restating their logic.

### 6. Metrics rewarded rounds, not learning efficiency

The existing `readinessMetrics` tracks verdicts, genuinely-new counts, clean
streaks, open compute, and open venue items. It does not measure whether the
system is learning faster. Missing metrics include:

- known-pattern escape rate (known issues first found by reviewers);
- preflight precision/recall after truth audit;
- defects prevented before dispatch;
- closure-regression rate;
- novel-valid findings per reviewer and per dollar/minute;
- re-flag rate for already-disclosed or falsified items;
- median finding-to-truth-audit and finding-to-closure latency;
- rounds and wall-clock time to minor-only convergence;
- catalog freshness and archive completeness;
- percentage of quantitative claims with executable evidence anchors;
- cross-paper consistency failures per release.

Commit `ba36b4c` now computes known-pattern escape and closure-regression metrics
from finding events and binds their campaign interpretation to explicit receipt
inventory reconciliation. That closes the metric-calculation primitive, not the
historical-data gap: until BigBounce inventories and reconciles all expected raw
receipts, a complete-history rate must remain unavailable rather than silently
treating missing or overwritten legs as zero findings. The other routing,
latency, evidence-coverage, and cycle-time metrics above remain to be completed.

### 7. Automation safety and portability are inconsistent

Several tools hardcode `/Users/houstongolden/Desktop/CODE_2025/bigbounce` and
some legacy scripts continue to import or describe forbidden OpenAI/Anthropic
API routes. A script that silently skips a missing file can report apparent
success while running against the wrong checkout. This directly weakens the
reproducibility of the learning loop.

## Minimal canonical target architecture

Do not add dozens of new skills. Extend the existing HubStack learning-loop
pack with one executable engine and expose one AstroStack adapter.

```text
raw INT/EXT receipts + exact review packet
                 |
                 v
        normalize_findings (append-only events)
                 |
        truth-audit + closure ledger
                 |
                 v
       pattern miner / promotion queue
                 |
         machine-readable rule catalog
                 |
                 v
  all-paper preflight + changed-claim dependency sweep
                 |
       signed/content-addressed receipt
                 |
                 v
     immutable packet gate -> residual review
                 |
                 +---- metrics compare prevention vs escapes
                 |
                 `---- every valid novel escape becomes a regression fixture
```

### Canonical components

1. **`hubstack/learning-loop/scripts/learning_loop.py`**
   One CLI with subcommands `ingest`, `audit-schema`, `mine`, `compile-rules`,
   `preflight`, `metrics`, and `verify-receipt`. It owns generic schemas and
   deterministic behavior. Existing skills become short routers/workflows around
   these subcommands.

2. **Machine-readable pattern sidecars**
   Keep human markdown, but require validated YAML/JSON fields for ID, category,
   severity, applicability, detector, evidence requirements, auto-fix policy,
   promotion state, tests, and provenance. Never execute arbitrary shell copied
   from markdown. Complex detectors reference named, tested plugins.

3. **Append-only finding events**
   A versioned JSONL event ledger with stable IDs and fields for packet SHA,
   paper/version/source/PDF SHA, reviewer/channel/model, raw receipt, claimed
   severity, truth verdict/evidence, pattern IDs, closure commit/artifact,
   first-seen/prior occurrence, and supersession. `ALL-FINDINGS.json` becomes a
   generated view, never a hand-evolved source.

4. **`tools/bigbounce_preflight.py` adapter**
   Reads `paper_registry.json`, invokes the generic engine for all papers, adds
   BigBounce-specific claim/artifact/SSOT/site/Convex checks, and emits one
   content-addressed portfolio receipt plus per-paper receipts.

5. **Packet-bound fail-closed gate**
   `review_packet.py` accepts only a PASS receipt whose source commit, source
   SHA, PDF SHA, catalog SHA, and registry SHA match the packet. Any edit after
   preflight invalidates the receipt. Waivers require structured owner, reason,
   evidence, expiry, and allowed gate; BLOCKER/MAJOR science checks cannot be
   waived by an agent.

6. **Changed-claim dependency graph**
   Store claim IDs in a registry mapping each headline quantity/statement to
   source spans, artifact generators, artifact files, figures, tables, abstracts,
   conclusions, sibling papers, SSOT, Convex, and site surfaces. On a diff, test
   the transitive dependency set rather than re-running only local grep.

## End-to-end implementation sequence

### P0 — Stop known-pattern escapes before the next review wave

1. Freeze an `finding-event-v1` JSON Schema and migrate all historical archives
   without deleting originals. Emit parse-error events for every unparsed source.
2. Ingest every review round after 2026-06-10, including exact-PDF July boards,
   and reconcile event counts against raw receipts/manifests.
3. Implement the generic `preflight` engine and convert the highest-value current
   checks first: patterns 008/030/036/040/041/045/046/047/048/051 plus citation,
   artifact-link, PDF freshness, version, and overclaim checks.
4. Add `tools/bigbounce_preflight.py --all --strict --changed-since <sha>`.
5. Require matching PASS receipts in `review_packet.py`, `int_wave.sh`,
   `int_wave_apjs.sh`, and `ext_submit.sh`.

**Exit proof:** attempting dispatch with a missing, stale, partial, wrong-paper,
or mismatched-SHA receipt fails; a fixture for each high-value pattern fails
preflight; a clean fixture passes.

### P1 — Make every review round improve prevention automatically

1. After truth audit, automatically ingest every finding.
2. For every VERIFIED novel finding, require either:
   - a deterministic detector regression fixture; or
   - a documented `not_mechanically_detectable` reason plus a prompt/rubric rule.
3. Mine clusters after each completed wave; generate a promotion proposal, never
   an unreviewed auto-commit.
4. Compile approved patterns into the next preflight catalog snapshot.
5. Re-run the new detector over all six papers immediately, not only the paper
   where it was found.

**Exit proof:** one synthetic novel finding flows from receipt to event, cluster,
approved rule, failing fixture, all-paper sweep, and packet-bound PASS receipt in
an integration test.

### P2 — Add proactive scientific perfection sweeps

Run these before residual external review:

- claim-to-artifact reproducibility and non-circularity;
- equation dimensional and quoted-value recomputation;
- parameter/value pairing scans;
- abstract/body/conclusion entailment;
- table/figure/caption/prose numeric consistency;
- assumption, estimator, null, mask, sample, and uncertainty consistency;
- literature/novelty/citation verification from primary sources;
- cross-paper shared-quantity and cross-citation consistency;
- data/code/release-card/DOI/URL reproducibility;
- adversarial scope/overclaim and alternative-explanation review;
- changed-regions-first regression review followed by whole-paper review;
- visual PDF, accessibility, journal format, and submission-package checks.

Each check must emit evidence and explicit coverage. “No issue found” without a
coverage manifest is not a pass.

### P3 — Measure and optimize the loop

Record per wave and per paper:

| Metric | Definition | Initial target |
|---|---|---|
| Known-pattern escape rate | VERIFIED findings matching an existing approved pattern / all VERIFIED findings | <5%, then 0% for two waves |
| Prevention yield | valid defects fixed by preflight before dispatch | Report count; trend upward initially |
| Closure-regression rate | VERIFIED findings caused by last closure / closure edits | <2% |
| Novel-valid yield | VERIFIED genuinely-new findings / reviewer legs | Use to route reviewers, never reward noise |
| Truth-audit precision | VERIFIED / all raised findings, by model/pattern | Calibrate prompts and reviewer weighting |
| Re-flag noise | prior-disclosed/falsified repeats / all findings | Trend downward; separate from readiness |
| Archive completeness | ingested raw receipts / expected receipts | 100% before wave close |
| Catalog latency | truth-audited novel finding to approved prevention rule | <1 wave |
| Evidence coverage | quantitative/headline claims with executable anchors / total | 100% for submission claims |
| Cycle time | immutable packet creation to truth-audited closure | Median and p90; trend downward |

Readiness must depend on scientific and publishing gates, not on raw round count.
The dashboard should show escape rate and closure-regression rate beside verdicts.

### P4 — Remove drift and duplicated authority

1. Shorten `cross-vendor-r-round` to generic mechanics and move historical vendor
   policy into a dated reference; BigBounce provider policy lives only in
   `bigbounce-r-round` plus tested config.
2. Make `cascaded-r-rounds` consume a convergence-policy object instead of
   restating BigBounce exit semantics.
3. Update `bigbounce-ready` to test current subscription/direct-provider routes,
   receipt validation, archive freshness, catalog compilation, and the all-paper
   preflight—not obsolete Anthropic/OpenAI SDK presence.
4. Replace hardcoded roots with repo discovery (`git rev-parse --show-toplevel` or
   `paper_registry.repo_root`) and fail closed on missing canonical inputs.
5. Retire/redirect obsolete scripts after tests prove the active route. Preserve
   historical receipts; do not rewrite history.

## Required test matrix

### Unit tests

- event-schema validation, stable ID generation, idempotent re-ingestion;
- parser fixtures for every active provider/receipt format and malformed output;
- pattern schema validation and duplicate/unknown ID rejection;
- detector positive, negative, boundary, and extraction-artifact fixtures;
- prior-closure regression and changed-dependency traversal;
- metric calculations, including failed legs as gaps rather than zero findings;
- provider-policy denial for OpenAI API and Anthropic routes.

### Integration tests

- raw receipt -> truth verdict -> event ledger -> mine -> compiled rule ->
  preflight -> immutable packet;
- all six registry entries; wrong paper/version/PDF/commit/catalog must fail;
- preflight after source edit must invalidate the old receipt;
- cross-paper shared-quantity drift must fail every affected packet;
- a valid structured waiver must be narrow and expire; invalid waivers fail;
- archive count must equal manifest/raw-receipt accounting.

### Golden regression corpus

Create minimal fixtures from each truth-audited real pattern, with sensitive or
large artifacts reduced to deterministic examples. Every VERIFIED novel finding
adds a failing-before/passing-after fixture in the same closure unit. This is the
most important recursive-improvement invariant.

## Process rules to promote into hard gates

1. **No review without prevention proof.** Exact PDF identity is necessary but
   insufficient; exact preflight identity is also mandatory.
2. **No finding closure without a regression fixture** when the failure is
   mechanically detectable.
3. **No single-paper closure.** Every approved new rule sweeps all six papers and
   all public/SSOT surfaces before the next dispatch.
4. **No manual aggregate as SSOT.** Events are append-only; indexes, summaries,
   dashboards, and pattern frequencies are generated.
5. **No readiness credit for repetition.** Re-flags and verdict variance remain
   visible but do not masquerade as novel science progress.
6. **No auto-falsification by model reputation.** Historical false-positive rate
   informs triage priority only; every claim still gets evidence-bound audit.
7. **No detector without coverage evidence.** Each pass records inputs, checks,
   versions, exclusions, and output digest.
8. **No skill proliferation.** Extend the canonical learning-loop pack; add a new
   skill only for a genuinely distinct responsibility under the ownership table.

## Honest ETA implications

“100% ready” cannot honestly be promised by an internal system: journal acceptance,
editor/referee response, author sign-off, licenses, DOI/archive publication, and
venue choices include external or Houston-controlled gates. A defensible 99%
means submission-ready with only documented external gates remaining, not accepted.

The current canonical board is P1A 62, P1B 56, P2 80, P3 56, P4 80, and P5 74,
so all-six 99% is not supportable tonight from current evidence. P0 enforcement
has reduced wasted review cycles, but it has also exposed real science, compute,
release, archive, and human-review gates that cannot honestly be compressed into
one automated evening.

Current planning ranges are:

- **Optimistic submission-candidate range:** 10–20 focused CC+SciStack working
  days if compute, release, and human decisions are continuously available
  (roughly 3–6 human-team months).
- **Realistic all-six submission-ready range:** 4–8 weeks, including residual
  truth-audited closure, exact-PDF confirmation, packaging/DOI work, and author
  review (roughly 6–12 human-team months).
- **Full-ambition range:** 6–12+ weeks if P1B production recomputation, new
  science analyses, or fresh major findings are required.

Actual journal acceptance is not schedulable by this stack; it depends on editors
and external referees. These ranges should be replaced with measured p50/p90 ETAs
after two complete instrumented waves rather than shortened merely because more
models are available.

## Acceptance checklist for the improvement program

- [ ] All raw review receipts since 2026-06-10 are represented in the event ledger.
- [ ] Event/manifest reconciliation is 100%; parse failures are explicit.
- [ ] All approved patterns have validated machine-readable rules or explicit
      non-mechanical status.
- [ ] Every high-severity recurring pattern has a regression fixture.
- [ ] Strict all-paper preflight passes on current committed sources and PDFs.
- [x] Review packets bind the matching preflight/catalog/registry receipts.
- [x] Active INT/direct-provider/external-browser dispatch routes require the gate.
- [ ] Cross-paper claim graph covers every headline quantitative claim.
- [ ] Known-pattern escape and closure-regression metrics are live for the
      complete BigBounce campaign. (The executable metrics and fail-closed
      inventory reconciliation are implemented and 11/11 tested at SciStack
      `ba36b4c`; the historical receipt inventory is not yet complete.)
- [ ] Two consecutive exact-PDF waves show zero known-pattern escapes and no
      genuinely-new BLOCKER/MAJOR issues after truth audit.
- [ ] PDF/version/SSOT/Convex/API/site/package gates pass for all six papers.
- [ ] Remaining readiness deductions are explicit human/venue/external gates.

## Immediate next action

P0 dispatch enforcement, strict six-paper preflight, and the P4/P5 computational
closure packages are implemented. P1B is now the active science critical path:
its corrected 500-realization CAMB/NaMaster canonical production is complete,
the six non-purification robustness configurations are running with durable
checkpoints, and the purification mask/field harmonic mismatch discovered by a
real smoke run is fixed and regression-tested at commit `f2564cf4`. Canonical
realization parallelism reduced the measured bounded benchmark wall time by
25.6% without changing the scientific JSON.

The preflight also no longer hard-codes historical manifest v1B.0.108. Commit
`23582538` makes the analysis-manifest validator consume the cataloged current
path and fail closed when that binding is absent. This converts version-matched
manifest selection from agent convention into an executable gate.

The next gate is to finish the P1B robustness battery, run the corrected
purification configuration, merge and verify the receipts, and produce a
version-matched immutable P1B release for exact-PDF non-Anthropic review. In
parallel only where it does not contend with that compute, the remaining
campaign-wide work is still to complete receipt/event reconciliation and the
cross-paper claim graph. The unchecked acceptance items above remain governing
work; neither the P1B compute progress nor prior P4/P5 closures imply that the
recursive-improvement program is fully implemented.
