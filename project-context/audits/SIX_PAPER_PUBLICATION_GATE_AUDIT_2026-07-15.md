# Six-paper publication-gate audit — 2026-07-15

## Executive finding

None of the six papers is presently supported at 95--99 publication readiness by the current evidence. The canonical board is P1A 62, P1B 56, P2 80, P3 56, P4 80, and P5 74. Those numbers are operational gate states, not acceptance probabilities. The earlier portfolio-wide 99 claim was retracted for valid reasons: it mixed packaging with scientific readiness, counted non-comparable or invalid review legs, and preceded exact-artifact reviews that found real defects.

The portfolio is much closer to a defensible submission set than those percentages alone suggest, but it is not one homogeneous queue. P1A and P3 are largely archive/venue/human-gated. P1B has a confirmed production-spectrum defect requiring recomputation. P2 has a clean automated exact-PDF board but still lacks load-bearing transfer/covariance/model-applicability work. P4 is actively closing three release-contract defects and retains irreducible training-realization/metadata gates. P5 has reached a bounded minor-only wording stop but depends on P4 and unavailable release inputs.

The honest critical-path estimate is:

- **95-level submission candidates, excluding actual editor/referee acceptance:** about **10--20 focused working days** if compute, archive publication, and author decisions are available immediately; **4--8 weeks** is the more realistic portfolio estimate because P1B and P2 contain genuine computation/analysis work and P4/P5 contain external-data or venue-scope decisions.
- **99-level packaged, author-signed submission candidates:** approximately **3--8 weeks**, conditional on choosing bounded venue scopes where irrecoverable historical inputs cannot be supplied and on completing DOI/archive work.
- **100% / officially accepted papers:** cannot be scheduled by this internal process. After submission, journal editorial and referee cycles typically add **months**, not hours or days. No automated model verdict is journal acceptance.

## Audit method and snapshot

This is a read-only gate audit. It uses the current SSOT banner and per-paper status files, the newest valid exact-PDF review bundles, truth-audit dispositions, current canonical PDF hashes/page counts, and the 2026-07-14 readiness-regression audit. It does not treat old `99` prose, raw model verdict words, a clean LaTeX build, or a draft release as sufficient proof of readiness.

Snapshot at inspection:

| Paper | Canonical artifact | Exact PDF evidence | Canonical readiness | 95--99 supported now? |
|---|---|---|---:|---|
| P1A | v1A.0.123, 7 pp, SHA-256 `4c450a67…` | Codex/ChatGPT-subscription ACCEPT after bounded minor closure | 62 | **No** — automated narrow-scope support, but archive/license/human/venue gates remain |
| P1B | v1B.0.109, 20 pp, SHA-256 `36b8fc98…` | Codex MAJOR / Gemini MINOR / Grok ACCEPT; truth audit confirms a physical-spectrum major | 56 | **No** |
| P2 | v1.7.122, 10 pp, SHA-256 `4097bac5…` | Valid Codex-subscription / Gemini-direct / Grok-direct ACCEPT board | 80 | **No** — manuscript board is clean, but declared load-bearing science/release gates remain |
| P3 | v3.2.0-r8, 16 pp, SHA-256 `b5f254f9…` | Bounded exact-r8 Codex/ChatGPT-subscription ACCEPT; bundle validation passes | 56 | **No** — archive/venue/human gates and bounded catalog-scope limitations remain |
| P4 | last released v1.0.254, 29 pp, SHA-256 `d8d4896d…` | Grok MINOR / Gemini MINOR / Codex MAJOR; truth audit confirms three new real majors | 80 | **No** — v1.0.255 source is in-flight and its current local PDF is not the released v1.0.254 artifact |
| P5 | v0.1.133, 39 pp, SHA-256 `db18dd93…` | Exact v0.1.132 Codex-subscription MINOR; one real wording minor closed under stop rule | 74 | **No** — dependency, archive, selection-product, power, and human AJ gates remain |

## Gate standard

A paper reaches evidence-backed 95--99 only when all four machine-verifiable gates are closed and only human submission/sign-off remains:

1. no open truth-audited blocker or major within the submitted claim scope;
2. every load-bearing number reproduces from committed, immutable artifacts, or the claim is explicitly narrowed so the unavailable analysis is not implied;
3. exact source/PDF/supplement/manifest/public archive are hash-bound and visually verified;
4. a valid fresh exact-artifact review confirms the hash-changed closure without an unresolved real major.

Readiness 100 remains author/editorial: Houston sign-off plus actual submission and journal disposition. An LLM ACCEPT cannot close that gate.

## Per-paper findings

### P1A — close to a bounded CQG Note submission, not 95--99 yet

**What is proved.** v1A.0.123 is a seven-page focused CQG Note candidate. The exact-PDF Codex/ChatGPT-subscription confirmation returned ACCEPT with no major or minor findings after the cutoff-scope and immutable-link edits. Its narrow ECH contact/transparency claims survived the valid review. The current canonical PDF hash matches the SSOT record.

**Open gates.** The SSOT still records: human CQG/editorial review, immutable archive/DOI, license authorization for the source bundle, remote post-push link resolution, and research-scope limitations including alternate-regulator, Lorentzian stress/observable, and state-specific renormalized axial-expectation analyses. The latter items need not all be performed if the Note's narrow claim and venue contract explicitly exclude them; that is a venue/author decision, not something an agent may silently waive.

**True blocker classification.** No demonstrated reader-visible scientific major remains in the submitted narrow claim. The immediate blockers are release/legal and human venue-fit gates.

**ETA.** **1--3 focused days** to reach a defensible 95--99 submission package if Houston authorizes the license/scope, the archive is minted, links are verified, and no new human review major appears. Actual CQG acceptance remains outside this ETA.

### P1B — confirmed major; on the computational critical path

**What is proved.** v1B.0.109 has a valid exact-PDF three-leg board. The truth audit confirms that the algebraic window/operator identity is useful, but the physical NaMaster validation is not: a `D_ell`-scale surrogate was passed to an interface expecting raw `C_ell`, producing an EE amplitude about `1.1e5` too large at `ell=140`; BB was also nonphysical. The generator contract has reportedly been repaired in later infrastructure commits, but no corrected 500-realization production run, robustness suite, figures, dependent numbers, or new exact PDF is yet authoritative.

**Other real gates.** The frozen runs used CAMB 1.6.5's default BBN table, not the later claimed `PArthENoPE` string; the exact table/domain/hash and manuscript statement must be repaired. The S8 overlay must be regenerated with the declared 30% burn-in. ALP mass prose mixes or overstates estimands. A new immutable manifest/release is required. Full-EB inference remains a disclosed scope/venue gate: either run it before claiming robust parameter inference or submit a deliberately narrow technical-companion result.

**True blocker classification.** One mandatory production recomputation major; one executed-provenance major; bounded numerical/wording fixes; immutable release; then a fresh exact board. P1B must not enter the submission bundle before these pass.

**ETA.** **3--7 focused days** if authenticated compute with PyMaster/CAMB is immediately available and the 500-MC suite completes cleanly. **2--4 weeks** if a full-EB likelihood is required for the selected venue rather than scope-bounded out. Compute availability and unexpected numerical shifts dominate uncertainty.

### P2 — strongest review result, but the board does not close the scientific program

**What is proved.** The exact v1.7.122 artifact has a valid, routing-compliant ACCEPT board from Codex/ChatGPT subscription, Gemini direct, and Grok direct. The truth audit supports the four-vertex coefficients, squeezed `-35/16`, and equilateral `-255/128` within the declared contraction-phase calculation. No further model-verdict chasing is warranted on this hash.

**Open gates.** The paper itself still types direct cubic bounce transfer, real SPHEREx covariance/likelihood, model-specific fermion/torsion applicability, immutable DOI/archive, and human PRD editorial review as open. These are not cosmetic. Without the transfer and survey covariance, the observational significance remains a conditional sensitivity mapping, not a complete end-to-end forecast. A scope decision could preserve the current paper as a theory/convention result, but it cannot simultaneously retain stronger observational claims without the missing work.

**True blocker classification.** No current manuscript algebra major; several load-bearing research/positioning gates. This is the clearest example of why raw ACCEPT is not equivalent to 95--99.

**ETA.** **2--4 days** for a rigorously narrowed theory/recast submission package plus archive if the venue accepts that contract. **1--3 weeks** for genuine direct-transfer/covariance/model-applicability closure, with a fresh exact board afterward. The latter is the honest estimate if the present scientific ambition is retained.

### P3 — technically packaged, chiefly venue/archive/human gated

**What is proved.** v3.2.0-r8 closes the r7 payload and threshold-provenance defects. Clean-tree validation reports 38/38 manifest payloads and 41/41 bundle files; the release is explicitly 170 core plus 11 lower-confidence positional associations, and the 0.1-arcsec boundary is post hoc/descriptive. A bounded exact-r8 Codex/ChatGPT-subscription confirmation returned ACCEPT.

**Open gates.** Immutable archive/DOI, final public release, venue/article-type acceptance, and human/editorial review remain open. The paper must remain a focused public-ID recovery/catalog-methods product; it cannot imply physical anomaly-class validation or catalog purity beyond the retained evidence. The current SSOT's 56 is conservative but evidence-backed; old high readiness text is superseded.

**True blocker classification.** Mostly release and human venue contract, not a currently demonstrated numerical defect.

**ETA.** **1--3 focused days** for DOI/archive, final checksum bundle, public-link verification, and author sign-off, assuming the focused ApJS catalog/methods scope is accepted. Journal acceptance remains external.

### P4 — active repair is necessary; three exact-release majors were real

**What is proved.** v1.0.254's observed-label null and 8,474,531-row semantic scan are useful, and its public HF dataset/model receipts were byte-verified. However, the exact board's Codex leg found three verified release defects: the public bootstrap omitted an import-time reproducer and failed in an empty directory; the quarantine validator checked aggregate counts but not exact `object_id` set equality/per-row HC equality; and the immutable model card falsely described Platt calibration as current production. Two bounded wording issues were also real (`definitive bias mitigation`; Figure 3's unsupported “after image-quality QA”).

**Current in-flight state.** The source now says v1.0.255 and the local PDF hash differs from the released v1.0.254 hash, so this is a work-in-progress closure, not yet evidence of a released or reviewed v1.0.255 candidate. The strengthened validator must be pinned to a commit containing every dependency, executed against the immutable public payload, republished with byte-verified HF receipts, recompiled/audited, and reviewed on the exact new PDF.

**Standing gates.** The historical classifier training realization cannot currently be reconstructed; full redshift/imaging/depth/seeing/PSF metadata are unavailable; spatially varying confusion transfer plus joint covariance remain incomplete; DOI/archive and human ApJS review remain open. These require either recovered/published evidence or an explicit bounded observed-label catalog contract that the venue accepts. Repeating caveats does not close them.

**ETA.** **2--5 focused days** to finish the v1.0.255 release-contract repair and one exact confirmation if the full scan/HF publication succeeds. **1--3 additional weeks** if complete metadata or a reconstructed training realization is treated as mandatory rather than venue-bounded. The latter may be impossible from surviving records; a transparent scope/venue decision is therefore on the critical path.

### P5 — minor-only latest wording review, but dependent and not release-complete

**What is proved.** The exact v0.1.132 Codex/ChatGPT-subscription review returned MINOR, not ACCEPT. Its sole new finding was a real overclaim in two environment-independence sentences. v0.1.133 closes those sentences, compiles to a 39-page retained PDF, and passed the documented arithmetic/A37/provenance/release/layout checks under the content-hash stop rule. The central result is properly bounded as an exploratory classifier-label null.

**Open gates.** Final Paper-IV/P4 labels, weights, and provenance must be frozen and P5 reverified against them. A1--A40 must resolve under an immutable public tag/archive/DOI. Exact DESIVAST selection products remain unavailable. Environment-dependent label-bias power is not established. Actual AJ editor/referee review remains open. The older external cap of 74 is therefore reasonable despite the latest bounded MINOR review.

**True blocker classification.** Cross-paper dependency on P4, release integrity, unavailable selection-function evidence, power/scope decision, and human venue review. Another review of unchanged v0.1.133 would be inefficient and should not substitute for these gates.

**ETA.** **2--4 focused days after P4 freezes** for dependency reverification, archive/tag, exact link checks, and one final package audit. **1--3 weeks** if new label-bias power or selection-function analysis is required by the chosen AJ claim scope.

## Critical path and realistic schedule

The work should not run as six serial review loops. The critical path is evidence production and release closure:

1. **P1B production rerun** and **P4 v1.0.255 contract repair** run in parallel.
2. **P2 scope decision/direct-transfer lane** runs in parallel with P1B/P4.
3. **P1A and P3 archive/legal/venue packages** are short independent lanes and should close while compute runs.
4. **P5 freezes only after P4**, then performs a single dependency reverification/package audit.
5. Exact-PDF review occurs once per changed candidate after proactive cross-paper sweeps; it is a confirmation gate, not the discovery engine.

| Scenario | Assumptions | Portfolio ETA to 95--99 submission candidates |
|---|---|---|
| Optimistic | immediate compute/auth; bounded venue scopes accepted; no new numerical shift; archive/legal decisions same day | **10--20 focused working days** |
| Realistic | P1B rerun debugging; P2 substantive transfer/covariance work; one closure regression; P4/P5 scope negotiation | **4--8 weeks** |
| Full-ambition | full-EB P1B, end-to-end P2 survey inference, reconstructed P4 training/metadata, new P5 power study | **6--12+ weeks**, with some inputs potentially unrecoverable |
| Official acceptance | all candidates submitted and journals respond | **months; not internally schedulable** |

These are wall-clock estimates under parallel execution. They are not promises of referee outcomes. The strongest uncertainty is not model-review latency; it is whether unavailable historical/data products are required by the final venue scope and whether corrected compute changes headline numbers.

## Efficiency diagnosis

The review loop has spent too much effort repeatedly sampling noisy verdict words on nearly identical artifacts. That behavior cannot close compute, archive, legal, metadata, or human gates. The 2026-07-14 regression audit correctly recommends stable gate readiness and a content-hash stop rule. Applying it strictly yields the following portfolio-level acceleration:

- stop rereviewing unchanged hashes after two valid zero-new-finding waves;
- mine every truth-audited real finding into a pre-review invariant and sweep all six papers before the next board;
- separate **claim-scope gates** from **must-compute gates** before edits begin;
- require executable clean-directory release bootstraps, exact row-identity checks, raw-vs-derived spectrum unit tests, executed-environment provenance, and cross-paper dependency checks before review;
- freeze immutable packets only after proactive source-to-claim, arithmetic, release, URL, and rendered-PDF audits all pass;
- report review distributions separately from stable readiness so noisy MAJOR/MINOR swings cannot create fake regressions or fake progress.

The fastest honest route is therefore not “more rounds.” It is one portfolio-wide proactive defect sweep, parallel closure of the actual evidence gates, and one exact confirmation per changed paper.

## Authoritative evidence used

- `project-context/SSOT/index.md`
- `project-context/SSOT/paper-{1,2,3,4,5}/status.md`
- `project-context/PUBLICATION_READINESS_REGRESSION_AUDIT_2026-07-14.md`
- `project-context/peer-reviews/INT_v3/ROUND_2026-07-14-P1A-v1A.0.123-EXACTPDF-4c450a67-CQG-NOTE-CODEX-SUBSCRIPTION-CONFIRM/`
- `project-context/peer-reviews/INT_v3/ROUND_2026-07-15-P1B-v1B.0.109-EXACTPDF-36b8fc98-NONANTHROPIC-CONFIRM/P1B_v1B.0.109_TRUTH_AUDIT.md`
- `project-context/peer-reviews/INT_v3/ROUND_2026-07-14-P2-v1.7.122-EXACTPDF-4097bac5-PRD-NONANTHROPIC-CONFIRM/P2_v1.7.122_NORMALIZED_TRUTH_AUDIT.md`
- `project-context/peer-reviews/INT_apjs/CONFIRM_2026-07-14_P3_v3.2.0-r8_b5f254f9/`
- `project-context/peer-reviews/INT_v3/ROUND_2026-07-15-P4-v1.0.254-EXACTPDF-d8d4896d-NONANTHROPIC/P4_v1.0.254_truth_audit.md`
- `project-context/peer-reviews/INT_v3/ROUND_2026-07-14-P5-v0.1.132-EXACTPDF-4b04d2fc-AJ-CODEX-SUBSCRIPTION-CONFIRM/P5_v0.1.132_NORMALIZED_STOP_RULE_DISPOSITION.md`
