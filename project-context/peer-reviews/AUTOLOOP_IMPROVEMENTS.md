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
