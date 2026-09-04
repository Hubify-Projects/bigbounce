# A3M v3M.0.9 — R4VERIFY review board (2026-09-04)

- **Round id:** `ROUND_2026-09-04-A3M-v3M.0.9-EXACTPDF-6c543e5e-R4VERIFY`
- **Manuscript:** `research/track_a3_multichannel/paper/main.tex` + `main.pdf`, **v3M.0.9, 12 pp**
- **Exact PDF binding (`shasum -a 256`):**
  `6c543e5e9885c6db58e07576482ed6f283b0307ad1499c6309a4651d3c26fb1a`
  - `research/track_a3_multichannel/paper/main.pdf` → `6c543e5e…6fb1a` ✓
  - `site/public/papers/a3_multichannel_arxiv_v3M.0.9.pdf` → `6c543e5e…6fb1a` ✓ (byte-identical mirror)
  - every leg header carries this same sha256 ✓
- **Preflight receipt:** `project-context/peer-reviews/INT_v3/ROUND_2026-09-04-A3M-v3M.0.9-EXACTPDF-6c543e5e-R4VERIFY/preflight_receipt.json`
  — `schema bigbounce.pre-review-portfolio-receipt/v1`, `verdict: PASS`,
  `repository_head d8658cbf74a4341af3a55ed6ebd91d898c573b69` (matches HEAD at dispatch),
  `core_sha256 b1c2425bb0683e0da2d92f5b7a7740eb252ab6f724e9c0bcca4b57f1d8a9d95d`.
- **API run log:** same directory, `api_legs_run.log`. Grepped both raws for
  `Reviewer call FAILED` → **0 hits**; no leg was recorded from a failed call.
- **Venue standard applied by every leg:** Physical Review D, regular article.
- **Dispatch:** `python3 tools/v3_native_pdf_review.py research/track_a3_multichannel/paper/main.pdf
  ROUND_2026-09-04-A3M-v3M.0.9-EXACTPDF-6c543e5e-R4VERIFY A3M "Full adversarial peer review —
  treat this as a real PRD/MNRAS submission."` with `V3_REVIEWERS=Gemini_cosmology,Grok_brutal`,
  `INT_OUTDIR` and `BIGBOUNCE_PREFLIGHT_RECEIPT` pointed at the round directory above — same
  invocation shape as R3 (commit `9867b294`). OpenAI/Anthropic API routes DISABLED per directive N.

## Filing convention (matches R1–R3)

The two direct-API raws are written by the review engine at the top of
`project-context/peer-reviews/` and stay there; the per-round directory under
`INT_v3/` holds the Claude/Fable leg, the API run log, and the preflight
receipt. The Fable leg was moved from
`INT_v3/A3M_v3M.0.9_R4_claude_fable_2026-09-04.md` to
`INT_v3/ROUND_2026-09-04-…-R4VERIFY/A3M_fable_r4_leg.md` (git mv) to match
`A3M_fable_r1_leg.md` / `A3M_fable_r2_leg.md` / `A3M_fable_r3_leg.md`.

## Leg census (every attempted leg reported; absent legs never recorded as clean)

| Leg | Model | Verdict word **read from the raw** | Tagged findings in the raw | Raw path (sha256 of the raw file) |
|---|---|---|---|---|
| Claude Fable INT | `claude-fable-5-1` (Opus-tier referee subagent, directive N) | **major-revisions** | **5 MAJOR** findings + questions-to-authors + 1 integrity note | `INT_v3/ROUND_2026-09-04-…-R4VERIFY/A3M_fable_r4_leg.md` (`84f9ee4e…908d9a6`) |
| Grok API | `grok-4.3` (`Grok_brutal`, native PDF rasterized 150 DPI + pass-2 NO_NEW; 77.9 s) | **REJECT** | **4 ESSENTIAL / 3 MAJOR / 3 NIT = 10** | `ROUND_2026-09-04-A3M-v3M.0.9-EXACTPDF-6c543e5e-R4VERIFY_A3M_Grok_brutal.md` (`a0d31dd2…7ab48f35f3`) |
| Gemini API | `gemini-3.1-pro-preview` (`Gemini_cosmology`, native PDF; 415.7 s) | **MAJOR REVISIONS** | **2 ESSENTIAL / 1 MAJOR / 2 NIT = 5** | `ROUND_2026-09-04-A3M-v3M.0.9-EXACTPDF-6c543e5e-R4VERIFY_A3M_Gemini_cosmology.md` (`fe84f084…4d6871cd`) |
| OpenAI / ChatGPT | — | **ABSENT** — paused under directive N (never faked, never back-filled) | — | — |
| Perplexity | — | **ABSENT** — optional leg, not run (recorded absent, never as clean) | — | — |

**FAILED legs: 0** ("Reviewer call FAILED" grep returned 0 hits across both raws).

### Leg caveat recorded (non-fatal)

`api_legs_run.log` — `[Gemini_cosmology] pass-2 self-critique failed (non-fatal):
PortfolioError('portfolio receipt is stale: HEAD, registry, rules, source, or
PDF changed')`. The pass-1 report is complete (full ESSENTIAL/MAJOR/NIT list +
summary recommendation, present verbatim in the raw); only the pass-2
self-critique (the NO_NEW de-duplication pass, which Grok completed) failed
because the preflight receipt bound to HEAD `d8658cbf` was, by the time the
long-running Gemini pass-2 call fired, stale against a HEAD that had since
advanced elsewhere in the repo. Consequence: Gemini's finding list was not
self-pruned for redundancy against Grok's list — recorded here, not treated as
a leg failure, does not change any verdict word.

## Verdict-word summary (diagnostic only, never a gate — directive P)

`major-revisions` · `REJECT` · `MAJOR REVISIONS`. Verdict words are recorded as
feedback; convergence is decided by truth-audit genuinely-new-real count, not
by these words.

## Next artifact

Truth audit against `project-context/peer-reviews/DISPOSITIONS/A3M.md` (not
run in this dispatch — this bundle covers dispatch + raw filing + receipt
binding only, per the task scope).
