---
pattern_id: 058
status: active
first_seen: EXT12-batch-truth-audit (2026-06-13)
papers_observed: [P1A, P1B, P2, P3, P4, P5]
finding_count: 6  # 6/6 Gemini EXT12 chats produced synthesis-mode responses with no formal verdict
proposed_by: r-round-pattern-mine 2026-06-13
---

# pattern-058: gemini-fresh-chat-no-verdict

**Description**: Gemini 2.5 Thinking in fresh chats without an explicit referee-format instruction produces synthesis-mode responses — extended academic exposition that summarizes, contextualizes, and discusses the paper WITHOUT a formal ACCEPT / MINOR REVISIONS / MAJOR REVISIONS verdict line. This makes the response structurally incompatible with the truth-audit harvest pipeline, which relies on a regex hit for `REJECT|MAJOR|MINOR|ACCEPT` in the first 30 lines of the report.

**Evidence (EXT12)**:
- All 6 Gemini EXT12 chats (one per paper, fresh-chat protocol per EXT7 lesson) returned responses with no formal verdict in the first 30 lines.
- Reports were substantive but framed as "academic commentary" not "referee reports."
- Root cause: EXT12 Gemini prompt did not carry an explicit referee-format instruction as its first line. In prior rounds where Gemini was submitting to an existing thread, the format was established by the thread context; fresh chats lack that context.
- EXT11 Gemini baselines (ACCEPT × 6) were used as fallback, but classified as "NO VERDICT" in the EXT12 truth-audit.

**Resolution**:
Lead every Gemini submission (fresh-chat AND delta-prompt alike) with the following as the FIRST LINE of the prompt, before any paper-specific context:

> Produce a referee report in MNRAS format with **Recommendation: ACCEPT / MINOR REVISIONS / MAJOR REVISIONS** as the first line of your reply.

The harvest pipeline's regex check (`REJECT|MAJOR|MINOR|ACCEPT`) must fire within the first 30 lines of the report. If it doesn't, the submission is classified NO VERDICT and the leg must be re-submitted.

**Detection rule (mechanical)**:
```bash
# After harvesting a Gemini report, check for verdict in first 30 lines:
REPORT="<path_to_gemini_report.md>"
head -30 "$REPORT" | grep -iE "(ACCEPT|MINOR REVISIONS|MAJOR REVISIONS|REJECT)" \
  || echo "NO VERDICT: Gemini report lacks formal verdict in first 30 lines — reclassify and resubmit"
```

**Prevention**: encode the verdict-format first-line rule directly in `external-review-browser-loop/SKILL.md` Gemini section. The exact first-line text must appear in the skill. This rule applies to:
1. ALL fresh Gemini chats (mandatory per EXT7 lesson — Gemini silently drops uploads on reopened chats, requiring fresh chats every round).
2. ALL delta-prompts in existing Gemini threads (the prior verdict format does not persist across turns reliably).

**Severity**: informational (the reports are substantive; the failure is structural/harvest-pipeline incompatibility, not missing findings)

**Cross-reference**: pattern-015 (Gemini billing-failure skip — vendor-side outage causing no response at all) is the prior Gemini-specific pattern. Pattern-058 covers the opposite failure mode: Gemini RESPONDS but produces synthesis prose instead of a structured referee report. Both checks should run at harvest time. See also `/external-review-browser-loop` SKILL.md Gemini section.
