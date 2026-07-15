# Recursive review taxonomy and convergence-gate audit — 2026-07-15

## Purpose

This is a read-only evidence audit of the accumulated BigBounce review system. It asks one narrow question: **which defects have recurred often enough that another model review should never be the first mechanism to find them?** The answer is uncomfortable but useful. BigBounce has learned a great deal, yet the learning is stored mainly as prose patterns, truth-audit narratives, and dated acceleration logs. Too little of it is compiled into fail-closed preflight gates.

The evidence base includes:

- `project-context/review-patterns/INDEX.md` and the individual pattern files;
- `project-context/2026-06-04_internal_external_review_gap_analysis.md`;
- `project-context/2026-06-05_review_gap_closure_v3p1.md`;
- `project-context/peer-reviews/AUTOLOOP_IMPROVEMENTS.md`;
- `project-context/ACCELERATION_LOG_2026-07-10.md`;
- `project-context/PROCESS_AUDIT_2026-07-14.md`;
- `project-context/PUBLICATION_READINESS_REGRESSION_AUDIT_2026-07-14.md`;
- the current exact-PDF audits for P1B v1B.0.109, P3 v3.2.0-r7/r8, P4 v1.0.254, and P5 v0.1.132/v0.1.133;
- the canonical disposition ledgers under `project-context/peer-reviews/DISPOSITIONS/`;
- current review/preflight tooling under `tools/`.

No existing skill, tool, paper, review, or state file was changed by this audit.

## Executive finding

The review loop is not failing because it lacks lessons. It is failing to **compile lessons into mandatory, artifact-bound tests**.

`project-context/review-patterns/INDEX.md` contains more than seventy named review, design, packaging, and site patterns, including high-frequency closure regressions, paper/artifact contradictions, uncomputed claims, stale version pins, review-log leakage, sigma mixing, and cross-paper drift. However, `tools/check_new_patterns.sh` mechanically checks only patterns 037–039 plus one percentage/count heuristic. Many newer patterns remain `DRAFT`; the index says its last pattern mine was 2026-06-26; and the July exact-artifact majors have not yet been turned into portfolio-wide gates. Thus the system repeatedly pays frontier-review cost to rediscover failures it already knows how to name.

The right convergence architecture is:

1. ingest every truth-audited finding into a normalized defect ledger;
2. map it to a stable taxonomy and affected claim/artifact surface;
3. promote recurrent or high-severity defects into executable tests immediately;
4. run the full accumulated gate suite over all six papers before dispatch;
5. reserve models for semantic novelty, adversarial scientific judgment, and venue fit;
6. measure learning by **preflight interception rate**, not by number of new pattern documents or review rounds.

## Evidence that the same defect classes keep returning

### 1. Claim-to-artifact mismatch and circular validation

This is the highest-impact recurrent class.

- Pattern 021 records external artifacts contradicting the paper while PDF-only reviewers remain blind.
- Pattern 027 records headline numeric claims with no supporting on-disk artifact.
- Pattern 042 records validation scripts that assert literals rather than recomputing them.
- Patterns 046 and 048 formalize paper–artifact cross-checks and uncomputed quantitative claims.
- P3 r7 was blocked because three manifest-listed Parquet payloads were absent from the frozen tree; commit `d155eb27` closed that exact release defect.
- P4 v1.0.254 then exposed two variants: its public bootstrap was not clean-room runnable and its quarantine validator checked aggregate counts but not exact object identity or per-row HC equality (`P4_v1.0.254_truth_audit.md`, C-M1/C-M2; review evidence committed in `6db21909`).
- P1B v1B.0.109 exposed a more serious execution mismatch: a supposed Planck-like NaMaster validation fed D-ell-scale surrogate amplitudes into a raw-C-ell interface, invalidating physical-noise/scatter claims while leaving only the algebraic operator identity intact (`P1B_v1B.0.109_TRUTH_AUDIT.md`, finding 1).

These are not unrelated reviewer discoveries. They are one class: **a manuscript claim is stronger than the executed, frozen, independently reproduced evidence contract**.

### 2. Executed provenance differs from declared provenance

- Pattern 002 records dataset attribution drift across closures.
- Pattern 043 records invented configuration narratives.
- Pattern 047 records stale version pins on bump.
- P1B v1B.0.109 says the frozen chains used PArthENoPE, while frozen run metadata had no override and the later public YAML setting was added after execution; the literal setting was not runnable (`P1B_v1B.0.109_TRUTH_AUDIT.md`, finding 2).
- P4 v1.0.254 found an immutable model card claiming Platt calibration for the current production product although production inference used direct softmax/TTA scores and the paper called Catalog C uncalibrated (`P4_v1.0.254_truth_audit.md`, C-M3).
- The July readiness audit found wrong-artifact and stale-artifact legs, including a P2 review that explicitly read v1.7.67 while being counted toward v1.7.68.

This class requires an **execution-record diff**, not more prose review.

### 3. Closure-introduced regression

- Patterns 008, 030, and 051 separately name within-round and cross-round closure regressions.
- `PUBLICATION_READINESS_REGRESSION_AUDIT_2026-07-14.md` records closure-introduced P1A equation inversion and sphaleron wording regressions, a P1B likelihood-name contradiction, and later framing drift across the portfolio.
- `AUTOLOOP_IMPROVEMENTS.md` records a P4 v1.0.160 footnote logic flaw introduced during closure itself.
- Pattern 036 records a closure that fabricated a mathematical justification rather than verifying it.
- P5 v0.1.132 still required v0.1.133 wording repair because two strong causal statements survived after the underlying analysis had already been bounded (`P5_v0.1.132_NORMALIZED_STOP_RULE_DISPOSITION.md`).

The present loop frequently validates the issue being closed but does not run a sufficiently broad **change-impact regression suite** over all affected claims, figures, tables, artifacts, and companion papers.

### 4. Arithmetic, units, estimand, and statistical-null incoherence

- Pattern 025: a claim contradicts its own equation.
- Patterns 028, 033, and 041: cited-literature arithmetic, prose-asserted prefactors, and formula-to-number recomputation failures.
- Patterns 038 and 054: sigma values from different nulls juxtaposed without local qualification.
- Pattern 044: wrong pairing of analytic claims.
- The June v3.1 audit found wrong denominators, incompatible p/z descriptions, a 0.63 vs 0.398 dilution arithmetic error, stale sample counts, binning contradictions, and a 9.5 vs 9.30 sigma discrepancy.
- P1B v1B.0.109 is a unit/interface version of the same class: a five-order-of-magnitude mismatch survived because no executable dimensional contract guarded the library boundary.

This class is expensive to find with natural-language rereads and cheap to intercept with a **claim computation registry plus dimensional/interface tests**.

### 5. Overclaim, hidden conditioning, and abstract/body drift

- Patterns 005, 019, 020, 022, 045, and 068–069 all describe overclaiming, buried limitations, narrative substitution for derivation, abstract/body drift, and recurring disclosed concerns that need signposting.
- P4 v1.0.254 still used “definitive bias mitigation” despite explicitly stating that the seven controls were necessary but insufficient; Figure 3 also assigned “image-quality QA” as a cause unsupported for 35 missing rows (`P4_v1.0.254_truth_audit.md`, C-M5/C-m7).
- P5 v0.1.132 used “no environment dependence survives” and “direct confirmation” where the evidence supported only no detected residual classifier-label association.
- The June gap audit found title/abstract scope, sigma-comparability, companion dependency, and “superseded/retracted/gate closed” process language repeatedly dominating external feedback.

The catalog already knows the lexicon. The gap is that no single portfolio gate semantically compares **title → abstract → conclusions → figure captions → Data Availability → declared limitations** against the claim ledger.

### 6. Version, packet, receipt, and mirror integrity

- Patterns 026, 047, 062, 065, and the packaging/site pattern sets cover dead anchors, stale pins/PDFs, static site drift, mirror mismatch, and placeholder identifiers.
- Commits `35bbe3ec`, `0f268268`, `6a3908a1`, `be591f45`, and `1f942478` materially improved content-addressed packet handling.
- Commits `6b7d1974`, `1fd28b3f`, `4f7be06d`, and `51e9c24f` hardened exact-artifact/provider routing and prohibited OpenAI-API review.
- Nevertheless, P3 r7 attempts failed on HEAD/commit mismatch; the July process audit documents wrong-PDF attachments, stale URL capture, empty URL success, and manifest inflation; and the readiness audit identifies historic relabeling and wrong-artifact counting.

These improvements are real, but integrity checks remain spread among dispatch, archive, site, and paper-specific scripts. A single **release graph verifier** should prove that source, PDF, packet, review raws, receipts, manifest, mirrors, SSOT, Convex, and site all name the same immutable object.

### 7. Review-system noise mistaken for scientific progress or regression

- Patterns 001, 003, 007, 009–010, 012–013, 031, 034, 056, 058, 061–064, 066, 067, 070, and 071 describe provider confabulation, extraction artifacts, fallback-model weakness, same-vendor pseudo-diversity, verdict mismatch, outlier variance, and manifest optimism.
- `PUBLICATION_READINESS_REGRESSION_AUDIT_2026-07-14.md` demonstrates that the old 99 and EXT17 “18/18 ACCEPT” were not supported by comparable raw evidence; it also documents ACCEPT→MINOR→MAJOR→MINOR variation on a byte-identical P4 PDF.
- `ACCELERATION_LOG_2026-07-10.md` shows that canonical disposition ledgers and fingerprint matching roughly halved repeated truth-audit effort, but the ledgers remain uneven and the matcher explicitly remains a draft.

This class should be solved by immutable raw verdict preservation, typed validity, exact tuple identity, cross-vendor weighting, and a content-hash stop rule—not by repeatedly editing papers to chase verdict words.

## Why the existing learning loop does not compound enough

### Learning is catalogued but not compiled

The pattern catalog is a strong knowledge asset. Yet the executable consumer is much smaller than the knowledge base. `tools/check_new_patterns.sh` covers patterns 037, 038, and 039; it cannot prevent P1B's spectrum-interface defect, P4's clean-room bootstrap failure, exact-set mismatch, model-card drift, or P5's causal overclaim. A prose instruction that says “screen against all patterns” is not equivalent to a test suite that proves it happened.

### Promotion is slow and inconsistent

Several important patterns remain `DRAFT` despite multiple observed instances, including cross-section contradiction (040), arithmetic recomputation (041), literal/circular artifacts (042), invented configuration narratives (043), stale version pins (047), uncomputed claims (048), static site drift (065), and review variance (066). The catalog index itself says the last mine was 2026-06-26, while the highest-value exact-artifact findings occurred July 14–15.

### The unit of learning is the narrative finding, not the affected contract

Truth audits are excellent at adjudicating individual findings, but they rarely emit a machine-readable tuple such as:

`(paper, claim_id, artifact_id, defect_class, causal_surface, test_added, affected_surfaces, closure_commit, regression_scope, recurrence_count)`.

Without that record, the next paper cannot automatically inherit the test, and the next edit cannot know which downstream claims to revalidate.

### Repeated-review throughput is optimized more than first-pass defect interception

The fused owner loop, disposition ledgers, direct dispatch scripts, exact packets, receipts, and parallel review legs have cut wave time substantially. Those are valuable throughput improvements. But faster review is not the same as faster convergence. The best metric is the fraction of later valid reviewer findings that a preflight gate would already have caught. That metric is not currently prominent.

### Paper-specific release logic fragments universal invariants

Recent P3 and P4 work added strong paper-specific validators, but universal invariants—clean-checkout reproduction, exact membership, unique IDs, executable config, claim-to-artifact equality, remote-byte verification, and immutable graph coherence—are not enforced through one portfolio contract.

## Prioritized executable gates

The order below is based on expected reduction in genuinely new blocker/major findings, not implementation convenience.

### P0 — Universal claim–evidence contract gate

**Expected convergence impact: very high.** Would have intercepted P1B physical-spectrum claims, P3 missing payloads, P4 aggregate-only quarantine validation, and many patterns 021/027/042/046/048.

For every quantitative or causal manuscript claim, require a registry record:

- stable `claim_id` and exact source locations;
- claim scope (`observed-label`, `physical`, `forecast`, `algebraic`, etc.);
- executable producer command or explicitly `noncomputational` derivation;
- input/output artifact hashes;
- fields/rows/statistics used;
- equality/tolerance assertion;
- limitations and forbidden stronger interpretations;
- affected figure/table/abstract/conclusion/site surfaces.

Executable gate: run every registered claim verifier against an isolated checkout. Fail if a headline number is literal-only, an artifact is missing, a producer cannot run, output differs, an asserted scope is stronger than the registered evidence, or an affected surface is not enumerated.

### P0 — Clean-room release and bootstrap gate

**Expected convergence impact: very high.** Directly prevents P3 r7 and P4 v1.0.254 C-M1/C-M2 classes.

For each paper release:

1. create a fresh worktree/container containing only manifest-declared files;
2. install only declared dependencies;
3. run `--help`, schema validation, minimal fixture, and full validation;
4. verify all import-time dependencies are manifest-pinned;
5. verify exact primary/quarantine/control ID-set equality, uniqueness, per-row flag equality, and declared row counts;
6. write a signed/hash-bound receipt that records every invariant, not only aggregate PASS;
7. mutation-test the validator by replacing one ID, duplicating one row, changing one flag, removing one import, and corrupting one hash; every mutation must fail.

### P0 — Scientific interface and dimensional-contract gate

**Expected convergence impact: very high.** Designed around the P1B D-ell/C-ell failure and patterns 025/028/033/041/044.

At every external library boundary, record expected quantity, units, normalization, shape, physical range, and a trusted reference value. Tests must compare at several representative coordinates and deliberately pass a common wrong convention to prove failure. For every manuscript formula with quoted inputs and output, maintain a small independent recomputation test. A generated claim table should diff all repeated values across sections and papers.

Minimum immediate tests:

- raw `C_ell` versus `D_ell` discrimination and CAMB reference-spectrum hashes;
- sample count/fraction/z/p consistency;
- estimator and null identity attached to every sigma;
- burn-in/weighting/estimand identity attached to every posterior number;
- formula-to-quoted-number recomputation;
- units and normalization in artifact schema.

### P0 — Closure change-impact gate

**Expected convergence impact: high.** Prevents patterns 008/030/036/051 and the recorded P1A/P4/P5 regressions.

Every closure plan must declare changed claims and dependency edges before editing. After editing, automatically run:

- full claim registry for directly and transitively affected claims;
- abstract/body/conclusion/caption/Data Availability coherence check;
- legacy-token and old-number sweep across all six papers, figures, scripts, site, and manifests;
- cross-paper citation/value propagation audit;
- artifact regeneration proof rather than timestamp inference;
- git diff semantic review that asks “what new assertion did this closure introduce?”;
- targeted mutation/regression tests created from the finding.

No closure is complete until the test that would have caught the original issue fails on the parent commit and passes on the closure commit.

### P1 — Executed-provenance diff gate

**Expected convergence impact: high.** Prevents P1B BBN and P4 model-card defects plus patterns 002/043/047.

Machine-compare manuscript/config/card claims with archived execution metadata. Required comparisons include software/version, config key/value, environment/package data file, dataset revision, calibration transform, random seed/split, row count, preprocessing, and model revision. A later reproduction config must never be silently presented as the historical executed config. Any difference requires explicit `historical_executed` versus `current_reproduction` typing.

### P1 — Claim-scope semantic lint

**Expected convergence impact: high for reviewer convergence; medium for underlying science.** Prevents patterns 005/019/020/022/045/068/069 and current P4/P5 wording defects.

Build a structured scope matrix for title, abstract, results, captions, conclusions, and site. Flag unsupported escalators and causal verbs (`definitive`, `establishes`, `confirms`, `rules out`, `physical`, `primordial`, `unbiased`, `complete`) unless the claim registry explicitly licenses them. Also flag process-language leakage, version-history prose, ticket IDs, mutable branch language, and causal explanations for undocumented exclusions. This gate needs a semantic model pass, but it should operate on a fixed checklist and return source spans—not an open-ended referee verdict.

### P1 — Immutable release graph verifier

**Expected convergence impact: high for release integrity; medium for scientific findings.** Consolidates patterns 026/047/062/065 and packaging/site failures.

Build one graph from canonical source commit to TeX hash, PDF hash/pages, archive object, manifest, supplements, review packet, raw provider receipts, mirror files, public URLs, SSOT row, Convex row, API response, and site data. Fail on any disconnected node, old version, mutable-only URL, wrong paper, invalid leg, missing remote byte verification, relabeled raw verdict, or content mismatch. Include live HTTP checks after deployment.

### P1 — Review-learning compiler

**Expected convergence impact: high and compounding.** Converts prose learning into system behavior.

After every truth audit:

1. emit normalized JSON findings with taxonomy, evidence, novelty, validity, scope, and affected surfaces;
2. match against the pattern catalog and disposition ledger;
3. increment recurrence by distinct paper and round, not raw reviewer count;
4. require a `test_added` reference for every NEW-REAL blocker/major and every recurrent minor;
5. auto-open promotion when severity is blocker/major once or recurrence reaches two independent artifacts;
6. regenerate the preflight suite and catalog index;
7. run the new gate across all six papers immediately;
8. record how many additional latent hits it finds before another review.

Promotion should be evidence-driven, not wait for a manual pattern-mine day.

### P2 — Review validity and stop-rule gate

**Expected convergence impact: medium for time; essential for honesty.** Consolidates patterns 061–067/070–071 and the July readiness audit.

Count a review leg only if `(paper, PDF SHA-256, source commit, venue profile, prompt hash, provider, resolved model, modality)` matches the packet and the raw explicit recommendation is preserved. Invalid, failed, stale, wrong-PDF, prompt-echo, or empty legs are gaps. Truth audit may change finding dispositions but never rewrite the provider's verdict. Re-review only on a changed reader-visible hash or one declared high-risk confirmation. Two valid waves on the same content with zero new real reader-visible findings trigger a stop.

### P2 — Portfolio cross-paper coherence gate

**Expected convergence impact: medium-high.** Targets patterns 032, 037, 053–055, and companion/release dependencies.

Generate a cross-paper graph of shared numbers, artifact IDs, dataset/model revisions, definitions, companion citations, venue/article type, dates, and submission order. Fail if a shared identity has inconsistent values/scopes, a companion is called published without an immutable identifier, a downstream paper depends on an unavailable release, or a terminology rename leaves residuals anywhere in the portfolio.

### P2 — Editorial and visual preflight

**Expected convergence impact: medium.** Prevents the old internal/external editorial gap and design/packaging patterns.

Run exact rendered-PDF checks for page count/venue fit, abstract density, table/figure width, captions, underfilled pages, overflow, legibility, raw paths, audit prose, bibliography, URL resolution, and package completeness. This is separate from scientific review and should be deterministic where possible, visual-model based only for layout judgment.

## Required recursive learning metrics

The system should publish these per round and cumulatively:

1. **Preflight interception rate:** fraction of valid NEW-REAL review findings already detectable by a gate before dispatch. Target: >90% for mechanical/provenance/consistency classes.
2. **Escaped-known-defect count:** findings mapped to an existing pattern but not caught preflight. Target: zero; each escape is a test-suite failure.
3. **Novel-major rate per changed PDF hash:** separates real convergence from repeated verdict noise.
4. **Closure regression rate:** new real findings caused by closure edits / closures completed. Target: <2%, then zero.
5. **Finding-to-test latency:** time from truth-audited NEW-REAL to merged failing-then-passing regression. Target: same commit/round.
6. **Cross-paper sweep yield:** additional latent occurrences found when a new gate runs over all papers.
7. **Re-audit avoidance:** ledger-matched findings requiring no full repeated adjudication.
8. **Review efficiency:** new real blocker/major findings per provider-call and wall-clock hour; stop when content-hash rule fires.
9. **Release graph completeness:** connected required nodes / total required nodes; must be 100% before official submission.
10. **Gate mutation score:** proportion of seeded corruptions caught by validators. Target: 100% for declared invariants.

Raw ACCEPT/MINOR/MAJOR counts should remain visible evidence but should not be the primary learning metric or directly determine readiness.

## Immediate portfolio sweep implied by current evidence

Before any broad next review wave, run these cross-paper checks:

1. every public bootstrap from an empty directory, including import closure;
2. every release manifest against a clean checkout and remote bytes;
3. exact ID membership/uniqueness/per-row equality for every split, quarantine, tier, primary/auxiliary, and control table;
4. all library-bound arrays for units/normalization/reference values;
5. executed historical configs versus current public reproduction configs;
6. every headline number back to a computed artifact and producer;
7. title/abstract/captions/conclusions/site against the registered scope and limitations;
8. all repeated numbers, dataset/model revisions, companion claims, and terminology across all six papers;
9. all release graph nodes from source through live site/API;
10. mutation tests for each high-severity validator.

This sweep should precede, not follow, another expensive model board. It is likely to find more transferable defects than six isolated incremental closure rounds because it tests the *class* across the portfolio.

## Process architecture recommendation

Use a four-layer loop:

### Layer A — deterministic proof gates

Claim computation, units, schemas, exact sets, manifests, hashes, URLs, compile/layout, release graph, and cross-surface consistency. These run on every change and must be green before review.

### Layer B — adversarial semantic sweeps

Dedicated bounded agents inspect derivation correctness, hidden conditioning, alternative explanations, scope/causal language, venue fit, and cross-section contradictions. Each agent gets the claim registry and artifact receipts, not only the PDF.

### Layer C — independent exact-artifact board

Codex/ChatGPT subscription plus direct Grok and Gemini, with raw receipts and no OpenAI API or Anthropic leg. This is a fresh-referee instrument, not the first line of mechanical QA.

### Layer D — truth audit and learning compilation

Adjudicate against source and artifacts; preserve raw verdicts; close only real findings; add failing-then-passing tests; sweep all papers; update pattern/disposition/metrics; apply content-hash stop rule; then synchronize PDF/version/SSOT/Convex/API/site.

The recursive requirement is strict: **Layer D must make Layer A or B stronger before the next wave whenever a valid new defect class or escaped known defect appears.** A review round that produces a real finding but no new/updated gate is incomplete process work.

## Realistic effect on convergence

This architecture cannot make absent scientific evidence appear. P1B still requires a corrected physical-spectrum 500-MC production run; P4 retains historical training-realization/full-metadata/archive gates; human/editorial decisions and DOI/deposit actions remain external. It can, however, eliminate a large fraction of avoidable incremental loops by moving known-defect discovery before dispatch, propagating every lesson to all six papers, and preventing closures from silently creating the next round's defects.

The biggest near-term acceleration is not more reviewers. It is implementing the P0 gates, running them portfolio-wide, and allowing the next exact-artifact boards to spend their intelligence on genuinely novel scientific criticism.

## Concrete evidence/commit index

- `88f4116e`: initial learning-loop pattern catalog.
- `76585bbc`: three-month retro; sixteen patterns and measured 12.5x amplification.
- `6ef4d429`: native-PDF internal/external gap closure.
- `3b66a4c3`: cross-paper patterns 037–039 auto-mined.
- `8534e673`: patterns 045–048 plus artifact cross-checking/uncomputed-claim rules.
- `291d4881`: closure-regression protocol (pattern 051).
- `001c2b1e`: per-round self-improvement logging.
- `b7644b94`: patterns 061–064 drafts.
- `35bbe3ec`, `0f268268`, `6a3908a1`, `be591f45`, `1f942478`: content-addressed packet and evidence-bundle hardening.
- `6b7d1974`, `1fd28b3f`, `4f7be06d`, `51e9c24f`: exact binding, provider receipts, OpenAI-API denial, subscription routing.
- `d155eb27`: P3 r8 exact bundle closure.
- `54aeaae3`: P1B/P4 exact-review closure baseline before later exact audit exposed deeper execution defects.
- `96c3a97e`: P4 v1.0.254 semantic release reviewed by the exact board.
- `6db21909`: retained P4 v1.0.254 exact board and truth audit.

## Bottom line

BigBounce has already discovered most of the process principles it needs. The inefficiency is that its memory is predominantly documentary. Turn the memory into a universal, mutation-tested, claim-centered preflight compiler; make every real escaped finding add a test and trigger a six-paper sweep; and stop spending review rounds on defect classes the system already understands.
