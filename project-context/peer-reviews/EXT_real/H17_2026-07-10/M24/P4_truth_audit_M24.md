# P4 — M24-EXT truth-audit

**Date:** 2026-07-13
**Paper:** P4 `pipelines/p2_chirality/paper/paper4_galaxy_chirality.tex`
**Reviewed version:** v1.0.239 (byte-unchanged; served md5 15211f0f, 35pp/4 mirrors)

## Raws — BOTH LEGS FAILED (no reviewer output captured)
Per directive I4 ("a leg that produced no output is FAILED, not a verdict") and the
readinessMetrics HONESTY CONTRACT ("a leg with no output is recorded verdict:'failed'
and rendered as a GAP, never a zero"):

- `EXT_real/H17_2026-07-10/M24/P4_grok_M24.md` — **273 bytes: Grok project landing
  sidebar stub only, no manuscript, no VERDICT line.** Screenshot `P4_grok_M24.png`
  shows the empty "Start a conversation in this project" pane (no review). → **FAILED.**
- `EXT_real/H17_2026-07-10/M24/P4_chatgpt_M24.md` — **0 bytes (empty).** Screenshot
  `P4_chatgpt_M24.png` shows an empty ChatGPT Chat pane (no upload, no verdict).
  → **FAILED.**

## Adjudication
There is **no raw reviewer text to verify**, so NO verdict can be recorded for either
P4 leg. The task brief's assumed "Grok MINOR (settling back from M21 ACCEPT)" and
"ChatGPT REJECT" cannot be attributed to these files — recording them would violate
directive I4 (never record a verdict from a label/expectation alone; a leg that
produced no output is FAILED, not a verdict).

## Streak + cap — BOTH HOLD (a FAILED leg is a GAP, not a genuinely-new finding and
## not a verdict change)
- **Clean-wave streak HOLDS at 9** (M21 was streak 9; a failed sweep neither advances
  nor resets — no content was reviewed). It does NOT advance to 10, because M24
  produced no clean re-read.
- **Cap HOLDS 85** (M21 recomputed cap: 50 + Grok-EXT ACCEPT 16.7 + ChatGPT-EXT
  MAJOR 6 + latest-Gemini INT 12 → rounded/formula = 85 per M21 post_verdict.sh).
  The failed M24 legs carry the M21 latest-per-reviewer verdicts forward unchanged;
  no drop, no bump.

## Re-sweep needed
P4 EXT must be re-run (headed browser) in a subsequent wave to obtain real verdicts on
v1.0.239. The M24 P4 legs are logged FAILED for audit-trail honesty.

## Integrity attestation
Both P4 raw files + both screenshots inspected; both confirmed empty/stub with no
reviewer output; recorded FAILED per directive I4; NO verdict synthesized from the
expected labels; cap + streak HELD (no content reviewed = no change); no fabrication.
