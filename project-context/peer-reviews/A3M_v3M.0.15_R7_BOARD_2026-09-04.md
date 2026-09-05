# A3M v3M.0.15 — R7 verification board (2026-09-04)

**Exact artifact.** `research/track_a3_multichannel/paper/main.pdf`
== `site/public/papers/a3_multichannel_arxiv_v3M.0.15.pdf`,
sha256 `909cf7893b89270f…`, md5 `4f2bf5e8204021bf06cbe27e3b8932c9`, 17 pp (verified this session).
Receipt: `INT_v3/ROUND_2026-09-04-A3M-v3M.0.15-EXACTPDF-909cf789-R7VERIFY/preflight_receipt.json`
(+ `api_legs_run.log`). No leg raw contains "Reviewer call FAILED" (grep = 0/0/0).

## Verdicts (read from raw text, not from labels)

| leg | model | verdict (raw) | ESSENTIAL | MAJOR | minor/nit | questions |
|---|---|---|---|---|---|---|
| Grok_brutal | grok-4.3 | **REJECT** ("Summary recommendation: REJECT") | 4 (E1–E4) | 3 (M1–M3) | 3 (N1,N2,N3) | 0 |
| Gemini_cosmology | gemini-3.1-pro-preview | **MAJOR REVISIONS** | 7 (E1–E7) | 2 (M1,M2) | 0 | 0 |
| Claude Fable 5.1 (INT) | fable-5.1 | **major-revisions** | — | 5 (M1–M5) | 14 (m1–m14) | 5 (Q1–Q5) |

Totals across legs: 11 ESSENTIAL + 10 MAJOR + 17 minor/nit + 5 questions = **43 raw findings**.

Truth-audit of every fingerprint: `INT_v3/A3M_v3M.0.15_R7_TRUTH_AUDIT_2026-09-04.md`.
