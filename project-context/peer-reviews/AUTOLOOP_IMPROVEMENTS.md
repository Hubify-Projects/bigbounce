# Autoloop Improvement Ideas Log

Houston standing directive 2026-06-05: "Don't just make the papers better every time. Make the skills and tools and everything you are using to review the papers better and better every single time."

Each entry: timestamp, observation, proposed improvement. Apply ones that demonstrably reduce the internal/external review gap.

---

## 2026-06-05 14:18pt — autoloop fire 1 setup

**Observation**: bash 3.2 on macOS doesn't support `declare -A` associative arrays. v3_review_autoloop.sh originally written with associative arrays failed first launch.
**Improvement applied**: rewrote autoloop with positional `case` lookup functions for bash 3.2 compatibility. Committed.

**Observation**: gpt-5 with `reasoning_effort=high` and `max_output_tokens=32000` consumed all reasoning budget before producing visible output (empty `output_text` despite 33s wall time).
**Improvement applied**: gpt-5 family gets `reasoning_effort=medium` + `max_output_tokens=64000`. Reasoning models (o3) keep `reasoning_effort=high`. Committed.

**Observation**: Claude Opus 4.7 rejected `thinking={"type": "enabled", "budget_tokens": 16000}` with "use thinking.type.adaptive and output_config.effort".
**Improvement applied**: switched Claude to `thinking={"type": "adaptive"}` + `output_config={"effort": "high"}`. Committed.

**Observation**: Anthropic SDK requires streaming for operations >10 min. Non-streaming call with `max_tokens=32000` + thinking failed immediately.
**Improvement applied**: switched Claude call to `client.messages.stream(...)` with text accumulation. Committed.

**Observation**: Claude formats finding IDs as `### P4-E1: ...` markdown h3 headers; GPT-5/Gemini use `**P4-E1**` or `- P4-E1`. The old synthesis parser only matched leading `*` / `**` / `-` / `P`.
**Improvement applied**: regex now accepts `#{1,4}` markdown headers + bold + `META-` prefix. P3 finding count jumped 41 → 112 with the fix.

**Improvement queued (not yet applied)**:
- gpt-5-pro for the meta-reviewer is ~5 min per call (acceptable but slow). Try Claude Opus 4.7 + extended thinking as a parallel meta-reviewer to cross-check.
- Perplexity citation forensics could call out specific arXiv IDs that don't exist. Build an arXiv-resolve sub-tool that fetches every citation's abstract and feeds it into the prompt — would eliminate citation-confab false positives (pattern-001).
- Find the cause of "ESS=0 / NIT=44" undercount in Perplexity output. Probably because Perplexity puts finding IDs in markdown table format that the parser doesn't recognize.

---

## 2026-06-05 15:18pt — autoloop fire 2 setup

**Improvement applied**: wired patterns 037, 038, 039 into
`~/.claude/scistack/hubstack/learning-loop/paper-pre-review-check/SKILL.md`.
These three patterns were auto-detected as cross-paper firings (fire 1)
appearing in 5-6 of 6 papers. The skill now has mechanical detection rules
so future R-rounds can catch them at compile time vs at review time.

**Improvement applied**: `tools/check_new_patterns.sh` runs the mechanical
detection on every paper. Initial baseline:
  P1A: clean
  P1B: clean
  P2:  ⚠ σ in 7 captions but 0 qualifier mentions (p038)
  P3:  clean
  P4:  ⚠ σ in 3 captions but 2 qualifier mentions (p038, close)
  P5:  ⚠ σ in 2 captions but 0 qualifier mentions (p038)

These hits will get logged in the next triage queue. P2, P4, P5 should
add `\sigmadisclaimer{}` macro to affected captions.

**Observation**: p037 future-year regex matches 2027+ but today is 2026,
so the "June 2026" dates are actually CURRENT. The pattern fires
because LLM reviewers have knowledge-cutoffs in 2024-2025 and incorrectly
flag "2026" as future. The real fix may be to use ISO-format dates that
make the year unambiguous to humans, or simply accept that this pattern
will keep firing until LLM reviewers catch up.

**Improvement queued**:
- Add cross-paper bibkey collision check (pattern-032 already covers this — verify it runs)
- Add stale-number-between-sections mechanical check (P4-E12 type) — search for repeated
  exact integers across sections and flag if same identity but different value.
- Wire pattern-038 σ-qualifier check into post-compile pdflatex audit (latex-audit skill).

## 2026-06-05 16:17pt — autoloop fire 3 setup

**Improvement applied**: `tools/v3_persistence_tracker.py` — cross-fire
fingerprint of META findings. Identifies findings the meta-reviewer surfaces
in multiple consecutive rounds. After 2 fires, 3 findings persist ≥2 rounds:
P1B/lee, P3/dedup, P4/binomial. After fire 3, these will likely hit 3/3 →
LOAD-BEARING tier, escalated to top of TRIAGE_QUEUE.

**Observation**: The current consensus_key heuristics in v3_autoloop_summary.py
cluster on shallow keywords (`audit_artifact`, `companion`, `length`). The deep
meta-reviewer findings (`binomial n_total`, `LEE double-correction`, `T-Web vs
V-Web`) are missed because they don't appear as single-word matches. The
persistence_tracker uses richer fingerprints — this is the right direction.

**Improvement queued**:
- Merge persistence_tracker's keyword vocabulary into v3_autoloop_summary.py so
  the cross-round diff also catches the deep findings, not just the shallow ones.
- Auto-promote PERSISTENT_FINDINGS.md entries to TRIAGE_QUEUE_<date>.md
  when count ≥3 rounds.
- Add fingerprint summary to AUTOLOOP_LOG.md per round.

## 2026-06-05 17:17pt — autoloop fire 4 setup

**Improvement applied**: `tools/v3_loop_terminate_check.py` — stricter NEW-ESS
counter that uses BOTH consensus_keys AND meta-finding fingerprints. The autoloop_summary
counter says "4 NEW ESS this round" but loop_terminate_check says 12. The
discrepancy is because:
- consensus_keys cluster on shallow keywords (e.g., "future_date", "sigma_mixing")
- meta-fingerprints capture deeper findings (e.g., "binomial", "lee", "dedup")
- many meta findings have NEW fingerprints (different aspects of the same
  underlying issue) round-over-round, so they count as "NEW" even though
  the underlying issue is persistent.

**Observation**: The cron's self-terminate condition ("0 NEW ESS for 3 rounds")
may never trigger under either counter because the autoloop is now mining
deeper findings each round. The TRIAGE_QUEUE and PERSISTENT_FINDINGS markers
are the actionable signal for Houston, not the autoloop counter.

**Improvement queued**: Add Houston-decision-tracker — when Houston resolves
a TRIAGE_QUEUE item (text edit, commit hash), record it in
`project-context/peer-reviews/HOUSTON_DECISIONS.md`. The autoloop then
filters out findings on that fingerprint from "NEW" counts.

**Cron prompt compliance**: zero .tex modifications this fire (review-only).

## 2026-06-05 18:17pt — autoloop fire 5 setup

**Improvement applied**: `tools/v3_version_aware_track.py` — cross-fire timeline
that ties findings to paper version bumps. Identifies which round each .tex
commit landed in, and which findings were CLOSED across the bump.

Verified P4 fire 1 → fire 2: 10 closures correspond to v1.0.158 → v1.0.159
commit (3 mechanical fixes I shipped: stale GZ1 N, dilution factor, Table II→I).

**Observation**: P2 and P3 don't have detectable `\paperVersion` macros — they
use different naming conventions. Future improvement: detect alternative
version macros (e.g., `\newcommand{\paperRev}{...}` or `\title{... v...}`)
or fall back to git commit dates.

**Improvement queued**:
- When pattern-037 (future date) keeps firing on 6/6 papers across 4+ rounds
  with NO closures: that's because the date is genuinely current (2026) and
  the LLM reviewers have older knowledge cutoffs. **Decision**: accept this
  pattern will keep firing and add a note in TRIAGE_QUEUE that it's an LLM-cutoff
  artifact, not a real paper issue. The check_new_patterns.sh already filters
  pre-2027 dates so it doesn't pollute the local check.

## 2026-06-05 19:19pt — autoloop fire 6 setup

**Improvement applied**: `project-context/peer-reviews/HOUSTON_DECISION_PACKAGE.md` —
one consolidated file with each of the 5 LOAD-BEARING findings, exact .tex
file/section location, current text (quoted), recommended fix (with A/B
options where decision is needed), effort estimate, and expected effect on
headline numbers.

This is the actionable bridge between the autoloop's signal generation
(LOAD-BEARING tier) and Houston's intervention. ~2 days of work to clear
the 5 LOAD-BEARING items; once cleared, the autoloop should converge within
3 more fires.

**Observation**: After 5 fires, total surface findings volatile (480-865 range,
mean ~686). But META-ESS counts stable (14-20 per round). The volatility is
in shallow findings being re-discovered with different consensus_keys; the
deep meta layer is more deterministic.

**Improvement queued**:
- Once Houston applies fixes to the 5 LOAD-BEARING items, add a "verification
  fire" mode that specifically re-tests against the persistence-tracker's
  expected closures. Currently the autoloop is blind to whether a fix worked
  until the next round naturally reveals it.

---

## 2026-06-08 13:54pt — fire 13 — flat-name PDF mirror lag bug

**Observation**: `tools/v3_review_autoloop.sh` reads each paper from a hard-coded flat-name
path (`site/public/paper1b_mcmc_companion.pdf`, etc.), but the LOAD-BEARING round
(commit `73522984`) only refreshed P3 / P4 / P5 flat-names. **P1B flat name was still v1B.0.42**
(from Jun 4) at fire 13 launch even though canonical v1B.0.43 had landed ~70min earlier.
That means fire 13's P1B review was on the wpivot-undefined version. Any wpivot-related
META findings should be discounted as fixed-but-not-reflected-in-PDF.

P1A / P2 / P3 flat-names happen to be current but only by accident (their canonical
versions haven't bumped recently).

**Improvement queued**: two-layer fix.
1. Add the flat-name refresh as an explicit step in `feedback_post_bump_full_sync`
   (currently implicit / luck-based).
2. Make `tools/v3_review_autoloop.sh` read the PDF directly from the source dir
   (`pipelines/p2_chirality/chirality_catalog_paper.pdf`, `arxiv/paper1b_mcmc_companion.pdf`,
   etc.) instead of the mirror — eliminates the lag entirely.

Patch-level fix for fire 14: `site/public/paper1b_mcmc_companion.pdf` refreshed
to v1B.0.43 mid-fire-13 (won't help fire 13 but unblocks fire 14).

---

## 2026-06-08 13:54pt — fire 13 — Convex paperSlug shorthand bug (historical)

**Observation**: All `tools/p*_convex_bump_*.mjs` standalone scripts wrote to
`paperSlug: "pX"` shorthand. But `convex/papers.ts:249` `listAllPaperStates` reads
`paper_versions` by `paper.slug` (long form, e.g. `"paper-1b"`). Months of bump
scripts were writing to a dead key — the Convex Paper State table on the homepage
has been stuck on stale versions for ~weeks. Houston caught it in the 2026-06-08
pushback.

**Improvement applied**: documented in `tools/README_convex_bump_slug_convention.md`.
Re-bumped all 5 affected papers (P1B/P2/P3/P4/P5) via long-form slug.
The `/bigbounce-bump` skill already uses long-form, no change needed there.

**Improvement queued**: delete or patch the historical `p*_convex_bump_*.mjs` scripts
since they're traps. They were one-shot tools that already ran, but they remain in
the repo as anti-patterns for the next agent to copy.


---

## 2026-06-08 14:00pt — fire 13 — persistence_tracker keyword fingerprinting is too coarse

**Observation**: `tools/v3_persistence_tracker.py` lines 81–103 use a fixed
single-word + phrase keyword list to fingerprint META findings. Two completely
unrelated P4 findings — one about a binomial-null trial count, another about
"MASTER-deconvolved pseudo-Cℓ" terminology — both fingerprint to the same
`master`-family key and look identical to the tracker.

This caused fires 11+12 closures to claim "0 NEW ESS" when content audit
of fire 13 vs fire 12 reveals 11+ genuinely new substantive findings:

- P1A Holst→Pontryagin mathematical error in Eq.(23)
- P1A Sec.IV.D vs Sec.XII fine-tuning contradiction
- P2 fa-cancellation in central β formula
- P2 Ω_φ ~ 0.17 spectator claim regression
- P1B SNR-on-the-mean vs per-realization framing
- P4 pseudo-Cℓ vs deconvolved-Cℓ terminology
- P4 v1.0.160 footnote logic flaw (regression I introduced!)
- P5 FFT sign conventions
- P5 Rs vs grid-resolution Nyquist
- P3 42hr wall-clock can't reconcile per-survey throughputs
- P3 22.5M-vs-6.5M "five primary target classes" contradiction

The tracker said "0 new fingerprints" because all 11 findings happen to mention
one of the existing single-word keywords (master/binomial/label/table_ii/etc.).

**Impact**: I almost called CronDelete to self-terminate the autoloop based
on the tracker's "3 consecutive 0-new-ESS" claim. That would have killed
the loop while it was producing extraordinarily high-value findings (the
Holst→Pontryagin mathematical error alone is a publication-blocking issue
the autoloop is the FIRST process to surface in 13+ rounds).

**Improvement queued**: switch to semantic-similarity fingerprinting.
Approach: for each finding, embed the (problem, required_fix) text via
sentence-transformers (or OpenAI text-embedding-3-small) and cluster by
cosine similarity ≥ 0.75. Two findings cluster together iff they're
talking about the same underlying issue. Single-keyword overlaps no longer
falsely merge.

Until that's built, **interpret "0 NEW fingerprints" as a necessary but
NOT sufficient condition for self-terminate.** Always also content-audit
fire-over-fire META files for genuinely-new high-significance findings
before advancing the counter.


---

## 2026-06-08 18:30pt — fire 18 — OpenAI quota exhausted + Gemini RECITATION blocks

**Observation 1 — OpenAI billing**: gpt-5-pro, gpt-5, and o3 all returning
`RateLimitError 429: insufficient_quota` consistently in fire 18. The OpenAI
account has hit a budget ceiling. Affects:
- OpenAI_methodology reviewer (1 of 5 per-vendor) — FAILED on all 6 papers
- v3.2 meta-reviewer (gpt-5-pro primary) — falling back to Claude opus 4.7

**Observation 2 — Gemini RECITATION**: gemini-2.5-pro returning
`finish_reason: 2` (RECITATION or SAFETY) at least once in fire 18. Auto-
falls back to gemini-2.0-flash but logs the issue. Possibly the meta-prompt
or paper text contains language that triggers Gemini's recitation filter
(maybe verbatim Eskilt et al. abstract quotes?).

**Impact**: degraded reviewer coverage for fire 18.
- P1A: 3/5 reviewers (Grok, Perplexity, Claude_brutal)
- Other papers: likely 3-4/5 each
- Meta fell back to Claude opus 4.7 (which uses the new format the
  v3_meta_content_diff.py extractor was fixed for in commit 42706887)

The autoloop CONTINUES with degraded coverage rather than aborting — this
is correct behavior, but logging the gaps matters for content-audit
interpretation.

**Improvement queued (Houston-only)**: top up OpenAI account budget OR
rotate to a new API key. The OPENAI_API_KEY in `.env.local` should be
re-checked.

**Improvement queued (tool-level)**:
- Autoloop pre-flight check should verify all 5 reviewer API keys + meta
  reviewer key have a budget allowance, log a warning if quota is low.
- Gemini RECITATION should auto-rewrite the prompt to remove the trigger
  (likely a famous-quote-fragment block).


## 2026-06-09 fire 21 — content-diff extractor: dash-bullet format support

**Observation**: `tools/v3_meta_content_diff.py` reported `🔴 NEW [P3-META-E1] (best_sim=0.00):` followed by an EMPTY quote string for P3 E1-E5 and P4 E1-E2 in fire 21. The findings DO exist in `auto-2026-06-09_1042pt_P3_META_REVIEW.md` but use a different formatting from the gpt-5-pro `## ESSENTIAL findings` heading + `### <PAPER>-META-E<N>` block:

```
P3-META-E1
- Severity: ESSENTIAL
- Section/page: ...
- Problem (quote): "..."
- Specific problem: ...
```

vs. the gpt-5-pro format:
```
### P3-META-E1
**Severity:** ESSENTIAL
**Quote:** "..."
```

The current extractor in `_extract_problem_from_block()` handles 2 of the 3 known formats but not the dash-bullet variant. As a result the diff tool shows NEW count correctly (it counts the heading match) but the quote is empty so the 5-gram Jaccard cluster collapses to similarity 0.00 against all prior findings — false-negative on RECURRING detection if the same issue had been raised in a prior fire under the dash-bullet format.

**Fix queued**:
- Extend `_extract_problem_from_block()` in `tools/v3_meta_content_diff.py` to ALSO match `^- Problem \(quote\):` and `^- Specific problem:` (dash-bullet variant).
- Same fix in `tools/v3_persistence_tracker_v2.py`.
- Add a unit-test fixture with all 3 known format variants to prevent format-fallback regression.

**Why this matters**: Fire 21 surfaced 12 NEW findings — 7 of them via the dash-bullet format. If the same finding RE-FIRES under the same format next round, the content-diff tool will not link them and will double-count as "NEW" instead of marking "RECURRING".

**Impact**: false-positive "NEW" count in fire 22+ on dash-bullet findings. Houston-facing severity LOW (synthesis files still capture everything), tool-level severity MEDIUM.
