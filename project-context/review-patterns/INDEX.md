# BigBounce Review-Pattern Catalog

Codified failure modes observed across 19 internal cross-vendor R-rounds, 9
CCAI self-review rounds, 1 R42 internal-multi round (2026-04-30), 1 P4
v1.0.66 external 4-vendor round (2026-05-15), 1 P1A external 3-reviewer
round (2026-06-02), 1 P4 v1.0.149 external 3-reviewer round (2026-06-04),
1 R39conf batch truth-audit (2026-06-13, 6 papers), and 1 EXT14 batch
external round (2026-06-13, 6 papers)
on 6 papers (P1A/P1B/P2/P3/P4/P5). Pattern mine last run: 2026-06-13 (EXT16 external round; pattern 060 promoted — \\mbox{-} math subscript escape extends pattern-059).

Every external/direct-vendor R-round must be pre-screened against these
patterns BEFORE dispatch, per the [[feedback-review-learning-loop]] and
[[feedback-three-stage-review]] standing directives.

Catalog is consumed by `/paper-pre-review-check` skill.

## Patterns

Sorted by severity then frequency descending.

Pattern mine last run: 2026-06-13 (EXT16 external round; pattern 060 promoted — \\mbox{-} math subscript escape extends pattern-059).

### High severity

| ID | Title | Severity | Freq |
|----|-------|----------|------|
| 001 | [Perplexity citation confabulation (real-arXiv-flagged-fake)](pattern-001-perplexity-citation-confab.md) | high | 38 |
| 009 | [GPT fallback (gpt-4o) low-rigor generic BLOCKERs](pattern-009-gpt-fallback-low-rigor.md) | high | 30+ |
| 017 | [Review-log artifacts in BODY prose (not %-comments)](pattern-017-review-log-in-body-prose.md) | high | 4-vendor convergent P4 v1.0.66 + 9 sites P1A v1A.0.35-36 |
| 002 | [Dataset attribution drift across closures](pattern-002-dataset-attribution-drift.md) | high | 6 |
| 003 | [Stale `%`-comment misread as paper body](pattern-003-stale-comment-misread.md) | high | 6 |
| 008 | [Closure introduces N+1 regression (within-round)](pattern-008-closure-introduced-regression.md) | high | 5 |
| 030 | [Round-to-round regression drift (across rounds)](pattern-030-round-to-round-regression-drift.md) | high | 5 |
| 019 | [Title/abstract markets a hypothesis the body has killed](pattern-019-title-overclaim-vs-body.md) | high | 5+ |
| 011 | [Confabulated bib survives many rounds till Perplexity catches](pattern-011-confabulated-bib-survives-first-draft.md) | high | 4 |
| 013 | [Perplexity catches real issue but proposes wrong fix](pattern-013-perplexity-counter-proposal-may-be-wrong.md) | high | 5 |
| 007 | [Reviewer arithmetic confabulation (number/sign wrong)](pattern-007-reviewer-arithmetic-confab.md) | high | 4 |
| 023 | [Trivial fix refused with false-cost / data-engineering-laziness](pattern-023-trivial-fix-refused-false-cost.md) | high | 6+ |
| 021 | [External artifact contradicts paper (PDF-only reviewers blind)](pattern-021-external-artifact-pdf-blind.md) | high | 6+ |
| 026 | [Reproducibility-anchor URL 404 / 401 / 410](pattern-026-reproducibility-anchor-404.md) | high | 4+ |
| 027 | [Headline numeric claim has no on-disk artifact (or disagrees)](pattern-027-headline-claim-without-on-disk-artifact.md) | high | 5+ |
| 020 | [Load-bearing disclosure buried in appendix / footnote / caveat](pattern-020-load-bearing-disclosure-buried.md) | high | 3+ |
| 028 | [Paper-side arithmetic disagrees with cited literature](pattern-028-arithmetic-vs-cited-literature.md) | high | 3+ |
| 029 | [Estimator multiplicity with no pre-registered primary](pattern-029-estimator-multiplicity-no-preregistration.md) | high | 3+ |
| 018 | [Internal R-rounds converge on "clean" while editorial artifacts persist (meta)](pattern-018-internal-rounds-blind-to-editorial.md) | high (meta) | 2 confirmed cases (P1A 8-round; P4 v1.0.66) |
| 031 | [Self-review severity-under-classification (CCAI optimism bias) (meta)](pattern-031-self-review-severity-underclassification.md) | high (meta) | 2 strong + 12.5× amplification ratio |
| 032 | [CCAI cross-paper bibkey / value / cite-anchor blindness (meta)](pattern-032-ccai-cross-paper-blindness.md) | high (meta) | 4 cross-paper drifts in one OOOOO |
| 033 | [Prose-asserted prefactor / OOM accepted by CCAI without derivation](pattern-033-prose-asserted-prefactor-acceptance.md) | high (meta) | 2 BLOCKER-tier in OOOOO |
| 038 | [σ values from different nulls juxtaposed without per-juxtaposition qualifier](pattern-038-sigma-mixing-without-per-juxtaposition-qualifier.md) | high | 6 (all papers, R10v3p1 cross-paper) |
| 039 | [Abstract Roman-numeral table reference points to wrong table](pattern-039-abstract-cross-reference-bug.md) | high | 5 (P1A/P1B/P3/P4/P5, R10v3p1 + 4-vendor consensus on P4) |
| 025 | [Mathematically-impossible attribution (claim contradicts own equation)](pattern-025-mathematically-impossible-attribution.md) | high | 1 (P4 R42 R3) |
| 054 | [σ values from different nulls juxtaposed without per-juxtaposition qualifier (cross-paper)](pattern-054-sigma-mixing-undeclared.md) | high | 8 (≥2 reviewers × P4/P3/P1A/P5, R39conf) |
| 055 | [Audit-artifact body leak (version tags / gate verdicts / ticket IDs in compiled PDF)](pattern-055-audit-artifact-body-leak.md) | high | 9 (multiple reviewers × P3/P4/P5, R39conf) |
| 057 | [Figure-regen text-residual (body text not swept after systematic rename)](pattern-057-figure-regen-text-residual.md) | medium | 3 (P5, EXT12 — 3 residual V-Web tokens in §VIII/§IX/App C post-figure-regen) |

### Medium severity

| ID | Title | Severity | Freq |
|----|-------|----------|------|
| 060 | [mbox-math-subscript-escape (\\mbox{-} form missed by pattern-059 union sweep)](pattern-060-mbox-math-subscript-escape.md) | medium | 1 (P5, EXT16 — V\\mbox{-}Web at l.2864 survived pattern-059 sweep) |
| 059 | [Math-mode subscript miss after global rename (extends pattern-057 to math context)](pattern-059-math-mode-subscript-miss-after-rename.md) | medium | 1 (P5, EXT14 — _{V-Web} subscript survived body-text sweep) |
| 053 | [Companion in-prep citation leak across multiple papers](pattern-053-companion-in-prep-citation.md) | medium | 6 (≥2 reviewers × P1A/P1B/P5, R39conf) |
| 012 | [Perplexity web-search misses recent arXiv (within ~6mo)](pattern-012-perplexity-web-search-miss.md) | medium | 20+ |
| 004 | [Buried §pathc_caveats closure not surfaced](pattern-004-buried-closure-restate.md) | medium | 14 |
| 005 | [Overclaim language (first/novel/load-bearing/publication-grade)](pattern-005-overclaim-language.md) | medium | 9 |
| 006 | [Companion paper self-cite missing in-prep hedge](pattern-006-companion-paper-hedge.md) | medium | 7 |
| 014 | [Review-log content left in `%`-comment block](pattern-014-text-comment-not-stripped-after-review.md) | medium | 4 |
| 022 | [Closure replaced derivation with narrative](pattern-022-closure-narrative-instead-of-derivation.md) | medium | 4+ |
| 024 | [Figure violates its own cited threshold](pattern-024-figure-violates-cited-threshold.md) | medium | 1 (predicts a class) |
| 037 | [Future-dated `\date{...}` block in title page across all papers](pattern-037-future-date-across-papers.md) | medium | 6 (all papers, R10v3p1 cross-paper) |

### Informational

| ID | Title | Severity | Freq |
|----|-------|----------|------|
| 058 | [Gemini fresh-chat no-verdict (synthesis-mode without explicit referee-format instruction)](pattern-058-gemini-fresh-chat-no-verdict.md) | informational | 6 (6/6 EXT12 Gemini chats — all 6 papers, fresh-chat protocol) |
| 015 | [Gemini billing-failure skip (vendor-side outage)](pattern-015-gemini-billing-skip.md) | informational | 19 |
| 010 | [Grok convergent-silence signal (shrinking output)](pattern-010-grok-convergent-silence.md) | informational | 8 |
| 016 | [Wide-net reflagging at exit boundary](pattern-016-exit-boundary-wide-net-reflag.md) | informational | 3 |
| 034 | [Same-vendor parallelism does not generate reviewer diversity (meta-arch)](pattern-034-multi-agent-same-vendor-no-diversity.md) | informational (meta-architecture) | structural; 12.5× ratio measurement |

## Cross-pattern observations

### Meta-finding: the 12.5× amplification ratio (pattern-034, the headline of the retro)

CCAI rounds (4 parallel same-vendor Claude agents) on a paper produce ~4
BLOCKER+MAJOR findings at "clean" exit. The same paper sent to a 4-vendor
cross-vendor round produces ~50. Ratio is **12.5×**. Source: 2026-05-08
OOOOO measurement on P3 + P2.

Direct campaign implication: every paper at 99% readiness that has NOT had
a cross-vendor round on its current version is implicitly accepting a
12.5× pipeline of external findings on first publication contact. This
formalizes the `/readiness-cap-99` rule from the meta-architecture side
(see pattern-034 + `/feedback_three_stage_review` standing directive).

### Three-stage review protocol (now mandatory)

Per the 2026-06-02 retro, no paper can hit 99% without ALL THREE of:
1. **Stage 1 — CCAI mechanical sweep**: same-vendor parallel agents for
   cheap cleanup of formatting, citation strings, obvious typos.
2. **Stage 2 — Cross-vendor R-round**: 4-5 distinct vendors via direct
   APIs (`/cross-vendor-r-round`) on the current version. ≥1 clean round
   required.
3. **Stage 3 — External journal-style review**: at least one external
   reviewer (human or frontier model reading as a journal reviewer).
   Pattern-018 makes this stage mandatory — internal cycles structurally
   miss editorial-hygiene defects.

### Per-pattern observations (legacy, retained)

- **Citation-forensics yield is monotonically declining**: P1A produced 5
  real attribution closures in round-2, then 1, 0, 0, 0 across rounds 3-6.
  Real defects exhaust fast.
- **GPT-4o (fallback from gpt-5)** never produced a VERIFIED closure
  across any paper after round-1 of any paper (pattern 009).
- **Perplexity is the only reviewer that produced VERIFIED citation
  closures** after round 1, and also the largest source of FALSIFIED
  claims.
- **Grok-4 is the best convergent-silence signal** (pattern 010).
- **The Eskilt2022b dataset attribution thread** (P1B R1-R7) is the
  cleanest case study of pattern 002+008.
- **Pattern-017 was the 4-vendor convergent BLOCKER on P4 v1.0.66
  (2026-05-15)** 18 days before it was named on the 2026-06-02 P1A
  external. This is the canonical instance of pattern-018.
- **Cross-paper closure-propagation audit** must run after every closure
  edit; pattern-030 + pattern-032 together require this. The new
  `/r-round-closure-propagation-audit` rule (in
  `/paper-pre-review-check` SKILL.md) enforces.

## How to add a new pattern

When a new R-round surfaces a finding that does NOT match any of the 35
catalogued patterns (+ 1 draft), AND the same shape appears in ≥2 distinct findings
across rounds, create `pattern-NNN-<kebab>.md` following the schema in
the existing files and append a row to the table above. Skill
`/paper-pre-review-check` picks up new patterns automatically by globbing
`pattern-*.md`.

## Pattern 037 (DRAFT) — iterative-closure-scope-creep

Each R-round closure adds content without restructuring. Paper grows from target (~20pp) to 50–60pp after 70–150 versions. External reviewers reject on scope. P4: 20→57pp / P3: 20→50pp. Draft at `pattern-037-iterative-closure-scope-creep-DRAFT.md`. Detection: `pdfinfo` page count gate in `/paper-pre-review-check` (WARN >40pp / ERROR >50pp).

Candidate cluster (not yet promoted to full pattern): **σ-value incommensurability** — presenting σ from binomial/MASTER/max-stat/density-stratified/analytic Bonferroni as if on one scale. Single source (2026-06-04 external P4 B5). Add to `CANDIDATE-CLUSTERS.md`.

## Pattern 036 — closure-fabricates-math-justification

Variant of [[pattern-008-closure-introduced-regression]]. Closure round responds to a 'justification gap' finding by ADDING fabricated math (orbit count, partition count, symmetry argument) rather than verifying. Caught on P2 R9 Gemini-M1 after 6 rounds × 4 vendors missed it. The fabricated 'exactly six orbits / complete S3 set' justification at L225 was added by R3 closure; underlying basis was physics-correct, but the layer was a lie.

Details: [pattern-036-closure-fabricates-math-justification.md](pattern-036-closure-fabricates-math-justification.md)

---
## Pattern 040 — cross-section internal claim contradiction (DRAFT)

META-reviewer (gpt-5-pro) catches claims in section X that contradict claims in section Y of the SAME paper. The 5 per-vendor reviewers miss it because they read locally. 4 firings in fire 13 across P1A (Sec.IV.D fine-tuning vs Sec.XII), P2 (spectator vs Ω_φ formula), P4 (pseudo-Cℓ vs deconvolved), P4 (v1.0.160 footnote logic). Recommends mechanical pre-commit cross-section grep + dedicated `/cross-section-coherence-check` skill at 6+ firings.

Details (draft): [pattern-040-cross-section-internal-contradiction-DRAFT.md](pattern-040-cross-section-internal-contradiction-DRAFT.md)

---
## Pattern 041 — META arithmetic check (DRAFT)

META-reviewer (gpt-5-pro) re-derives the paper's quoted result from the paper's own formula + parameters and finds inconsistencies. 4 firings in fire 14 across P1B (β=0.336° contradicts formula), P2 (β arithmetic gives 0.002° not 0.27°), P3 (γ ± 0.382 vs CI [2.304, 2.882] width 0.578), P5 (1.98pp vs 1.7pp range). Per-vendor reviewers don't re-derive; meta-reviewer does. Truth-audit verdict typically VERIFIED. Recommends pre-flight quote-formula recompute check at 6+ firings.

Details (draft): [pattern-041-meta-arithmetic-check-DRAFT.md](pattern-041-meta-arithmetic-check-DRAFT.md)

---
## Pattern 042 — Hardcoded-literal artifact scripts (DRAFT)

Verification scripts/anchors that ASSERT literals instead of computing them — the artifact exists and "passes" but is circular. R23conf recurrences: P2 `appendix_A1_wick_doubling.py` `benchmark_ratios` assigned-literal list feeding assertions; P4 `catalog_c_post_tta_dipole_summary.json` assertion-only anchor with no observed/null raw values. Detection: grep artifact scripts for assigned literal lists flowing into asserts; flag anchors lacking raw computed values. Prevention: every "we checked/verified X" claim must point to an artifact containing COMPUTED values, not asserted ones (`/paper-pre-review-check` + `/artifact-link-verify`).

Details (draft): [pattern-042-hardcoded-literal-artifact-scripts-DRAFT.md](pattern-042-hardcoded-literal-artifact-scripts-DRAFT.md)

---
## Pattern 043 — Invented-configuration narratives (DRAFT)

Paper text describes an analysis configuration matching NO committed artifact, typically reverse-engineered from a true total. R23conf recurrences: P1B §VI "three benchmark configs C=4/8/12, 3,240 samples each" invented around the real 9,720 = 2,160+6,840+720; P4 headline-null generator's undescribed `p_cw_eq>0.6` all-CW selection. Detection: diff each config/sample-count claim against the committed chain/catalog inventory; red flag = prose counts that are exact divisors of a true total. Prevention: configuration paragraphs must be generated FROM the committed configs (read the yaml/script), never written from memory (`/paper-pre-review-check` + `/never-fabricate-derivation`).

Details (draft): [pattern-043-invented-configuration-narratives-DRAFT.md](pattern-043-invented-configuration-narratives-DRAFT.md)

---
## Pattern 044 — Wrong-pairing analytic claims (DRAFT)

Analytic values quoted at parameter points where the committed computation gives different values — both value and point are real, the PAIRING is false. R23conf recurrences (P1B, ×2): Δφ/f_a=1.07 quoted "at m≈2H₀" when the committed ODE (c10b) gives 0.42 there and 1.07 at m≈4H₀; the 0.65-at-m=H₀ claim, actual 0.11. Detection: evaluate the committed function at each quoted point; if the quoted value occurs elsewhere on the grid it's a pairing swap, not a wrong number (distinguishes from pattern-041). Prevention: parameter-point claims carry the generating script + a committed grid-scan artifact (`/paper-pre-review-check` quote-formula gate).

Details (draft): [pattern-044-wrong-pairing-analytic-claims-DRAFT.md](pattern-044-wrong-pairing-analytic-claims-DRAFT.md)

---
## Pattern 045 — Abstract/body claim drift (EXT1)

Abstract claims drift from the body's final calibrated statements after multi-round body fixes (P1A "each fails at amplitude" vs §IV.D R4-naturalness; P2 missing cubic-transfer caveat; P3 abstract ordering; P5 "headline" dual-use). Prevention: every round, diff each abstract claim against its body citation — abstract is re-read holistically LAST.

Details: [pattern-045-abstract-body-drift.md](pattern-045-abstract-body-drift.md)

---
## Pattern 046 — Artifact/paper cross-check gap (EXT1)

On-disk artifacts contradict paper numbers/units/versions (P1B parameter_summary.json Cobaya-normalised units, burn-in 20%-vs-30%, P4 stale commit hash + mask description, P1A bundle v0.9.0 label). Internal rounds audit .tex only; referees download artifacts. Prevention: tools/artifact_crosscheck.py mechanical sweep every round.

Details: [pattern-046-artifact-paper-cross-check.md](pattern-046-artifact-paper-cross-check.md)

---
## Pattern 047 — Version-pin staleness on bump (EXT1)

Data Availability commit hashes, bundle metadata, DOI/hash manifests go stale across bumps (P4 hash 5 versions old; P2/P3 no frozen release prepared). Prevention: /bigbounce-version-bump gate — provenance surfaces update in the same commit as the stamp.

Details: [pattern-047-version-pin-staleness-on-bump.md](pattern-047-version-pin-staleness-on-bump.md)

---
## Pattern 048 — Uncomputed quantitative claim (EXT1)

Inequality/rate/robustness claims stated qualitatively where a number is checkable (P1A Γ_washout>H, e^32 separation; P2 fiducial-shift bound; P5 missing effect sizes/regression). Prevention: reviewer prompt demands the number, computation pointer, or explicit labeled-assumption tag for every >, <, exceeds, dominates, negligible, robust-to claim.

Details: [pattern-048-uncomputed-quantitative-claim.md](pattern-048-uncomputed-quantitative-claim.md)

---
## Pattern 051 — Closure-introduced regression (EXT2)

Fix waves create new defects: fresh math errors in patches, half-applied sweeps, wrong closure artifacts. ~40% of EXT2's genuinely-new findings were regressions from our own EXT1/R29 closures. Prevention: 5-point closure-wave protocol (sweep-completeness grep, self-diff regression check, new-math gate, closure-artifact verification, changed-regions-first review).

Details: [pattern-051-closure-introduced-regression.md](pattern-051-closure-introduced-regression.md)

---
## Pattern 052 — Re-raise vindication test (EXT3)

A reviewer re-raising a FALSIFIED finding is itself evidence. Auto-falsify on re-raise ONLY if the prior falsification cited primary evidence; assumption-based falsifications get mandatory primary-source verification on re-raise (P2 Addis citation was vindicated on the 3rd raise after two wrongful falsifications; P5 k=20 was correctly auto-falsified — discriminator is evidence quality of the prior verdict).

Details: [pattern-052-reraise-vindication.md](pattern-052-reraise-vindication.md)
