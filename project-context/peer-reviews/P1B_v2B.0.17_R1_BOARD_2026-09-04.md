# P1B verdict board — v2B.0.17 R1 (2026-09-04)

**Exact PDF binding:** `arxiv/paper1b_namaster_proof.pdf` ==
`site/public/papers/paper1b_namaster_proof_v2B.0.17.pdf`,
sha256 `0d0c92ab2b07add4f3de837c26d9ceff742b4931490a0d05c5a4fd4e4001fcac`,
md5 `7bc21cbe…`, 8 pp. Both paths verified byte-identical at audit time.
**Receipt:** `INT_v3/ROUND_2026-09-04-P1B-v2B.0.17-EXACTPDF-0d0c92ab-R1/preflight_receipt.json`
(+ `api_legs_run.log`). No `Reviewer call FAILED` string in either raw.

## Verdicts (read from raw text, not labels)

| Leg | Model | Verdict (verbatim) | Essential | Major | Minor/Nit | Questions |
|---|---|---|---|---|---|---|
| Grok_brutal (API) | grok-4.3 | **MAJOR REVISIONS** | 3 (E1–E3) | 2 (M1–M2) | 2 (N1–N2) | 0 |
| Gemini_cosmology (API) | gemini-3.1-pro-preview | **MAJOR REVISIONS** | 2 (E1–E2) | 1 (M1) | 2 (M2 minor, N1 nit) | 0 |
| Claude INT (Opus, exact-PDF) | opus | **major-revisions** | — | 8 (M1–M8) | 11 (m1–m11) | 8 |

Raw totals: 7 + 5 + 19 = **31 findings** + 8 author questions.
Active-leg set per directive M-AMENDED: Grok API, Gemini API, Claude INT. OpenAI/ChatGPT
column frozen (directive N) and excluded from the criterion.

## Convergence status

All three active legs return **major-revisions**. This is R1 on v2B.0.17 — no prior
disposition fingerprints exist for this version (`DISPOSITIONS/P1B.md` covers the
pre-v2B lane), so **no finding in this round is a re-flag**.

Truth-audit: `INT_v3/P1B_v2B.0.17_R1_TRUTH_AUDIT_2026-09-04.md`.
