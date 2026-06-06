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
