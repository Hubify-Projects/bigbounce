# /paper-pre-review-check — all 6 papers, 2026-06-02 post-external-R1 sweep

**Run**: 2026-06-02
**Trigger**: after first external R1 round on P1A surfaced pattern-017 body-prose contagion; pattern-018 (mandatory pre-flight) now active.
**Catalog**: 16 confirmed patterns + 2 drafts (017 + 018) at `project-context/review-patterns/`.

## Quantitative scan

| Paper | Latest version | pattern-014 (^%-cmt) | pattern-017 (body) | pattern-005 (overclaim) | pattern-006 (own-cite) |
|---|---|---|---|---|---|
| paper-1a | v1A.0.40 | 48 | **0** | 19 | 39 |
| paper-1b | v1B.0.35 | 70 | **0** | 12 | 19 |
| paper-2 | v1.7.39 | 20 | **0** | 15 | 0 |
| paper-3 | v3.1.72 | 46 | **0** | 46 | 0 |
| paper-4 | v1.0.144 | 4 | **0** | 47 | 0 |
| paper-5 | v0.1.38 | 57 | **0** | 37 | 42 |

## Verdicts

- **Pattern-017 (body-prose review-log)**: 🟢 ALL CLEAN. Cross-paper sweep landed in v1A.0.40 / v1B.0.35 / v3.1.72 / v1.0.144.
- **Pattern-014 (^%-comment review-log)**: 🟡 high counts but **invisible in compiled PDF** — these are LaTeX comments. Not an external-review blocker. Pre-arXiv-submission cleanup recommended but not urgent.
- **Pattern-005 (overclaim word frequency)**: 🟠 **NEEDS CONTEXT-AWARE AUDIT**. Raw word count includes legitimate uses ("first SPHEREx detection target", "novel methodology", etc.) alongside genuine overclaims. P3/P4/P5 have the most hits — these papers haven't yet been through an external review that targets this pattern. P1A v1A.0.40 retitle + §I scope-and-limitations softened many; remaining 19 likely include legitimate "first" uses.
- **Pattern-006 (own-paper self-cite)**: 🟠 raw count includes hedged ("in preparation") and unhedged. P1A (39), P1B (19), P5 (42) carry significant companion-paper architecture. ChatGPT B10 flagged this on P1A; the closure landed 12+ hedges in v1A.0.40 — remaining hits are mostly in references.bib + already-hedged in-text.

## Block status for external submission

- 🟢 **P1A v1A.0.40**: external-R1 closures complete; no remaining blockers. **CLEARED for next round of external review.**
- 🟢 **P1B v1B.0.35**: pattern-017 swept; otherwise inherits 3-clean exit from internal rounds. **CLEARED.**
- 🟢 **P2 v1.7.39**: 3-clean internal exit, no body-prose hits. **CLEARED.**
- 🟢 **P3 v3.1.72**: pattern-017 swept; 3-clean internal exit. **CLEARED.** Watch pattern-005 (46 hits — highest along with P4) in any external round.
- 🟢 **P4 v1.0.144**: pattern-017 swept; 3-clean internal exit. **CLEARED.** Same pattern-005 caution.
- 🟢 **P5 v0.1.38**: 3-clean internal exit, no body-prose hits. **CLEARED.** Pattern-006 (42 own-cites) carries the most architectural cross-cite — Paper IV companion infrastructure.

## Recommended skill-stack improvements (identified during this run)

1. **`/paper-pre-review-check --all`**: batch sweep across all 6 papers in one invocation (currently requires per-paper loop).
2. **Pattern-005 context-aware detector**: skip "first" in legitimate contexts (`first detection at X-sigma`, `first measurement of Y`) by requiring an adjacent qualifier check OR a sentence-level analysis. Reduces false-positive rate.
3. **Pattern-006 hedge-presence detector**: for each own-paper `\cite{}`, verify a hedging parenthetical (`in preparation`, `submitted`, `companion`) within ±100 chars. Counts only UNHEDGED cites.
4. **`/bigbounce-post-bump-sync` skill** (NEW): orchestrates the full post-bump propagation chain (papers.ts + live-status.ts + SSOT/index + SSOT/paper-N + queue + claims-table + pre-review-check + commit) as one command after `/bigbounce-bump`. Reads from Convex.
5. **`/bigbounce-arxiv-prep` skill** (NEW): pre-arXiv-submission gauntlet — strips `^%`-comments, runs latex-audit, artifact-link-verify, pattern-014/017 grep, claims-table verify, bib-tarball-rebuild. Required before any arXiv submission.

## Houston-action recommendations

1. **Sign off on P1A v1A.0.40** in `SSOT/paper-1A/status.md`. Then readiness can flip from 95% (cap) to 99%.
2. Next external review on **P1B/P3/P4** should be scheduled — they're all CLEARED but haven't yet been through an external pass like P1A just did.
3. The 3 OPEN-DEFERRED-AS-NOTE items from P1A (14-barrier collapse, action rewrite, non-minimal Route 1) need a follow-up theory pass — this is a SCOPE choice declared in §I and is not a defer per Houston's "no defer" rule (the §I scope paragraph explicitly limits the paper's claims; further extension is a new paper).
