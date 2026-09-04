# A3M v3M.0.8 — R3 review board (2026-09-04)

- **Round id:** `ROUND_2026-09-04-A3M-v3M.0.8-EXACTPDF-8cf429e0-R3`
- **Manuscript:** `research/track_a3_multichannel/paper/main.tex` + `main.pdf`, **v3M.0.8, 10 pp**,
  dated September 4, 2026
- **Exact PDF binding (verified this session, `shasum -a 256`):**
  `8cf429e002d44c97308ccc994c9378a93b066e094de865d48f850d5e72291b9a`
  - `research/track_a3_multichannel/paper/main.pdf` → `8cf429e0…1b9a` ✓
  - `site/public/papers/a3_multichannel_arxiv_v3M.0.8.pdf` → `8cf429e0…1b9a` ✓ (byte-identical mirror)
  - md5 `0c61d2ab760a14e0ff27ca560585bcbf`
  - every leg header carries this same sha256 ✓
- **Preflight receipt:** `project-context/peer-reviews/INT_v3/ROUND_2026-09-04-A3M-v3M.0.8-EXACTPDF-8cf429e0-R3/preflight_receipt.json`
  — `schema bigbounce.pre-review-portfolio-receipt/v1`, `verdict: PASS`,
  `repository_head 8d5ca7c8c611b341b86d89a7e91aed8a071e941e`,
  `receipt_sha256 1edd12a7f812faafe502cc8a4f14ff68a10300a3dde97369d6418d91185c0c1e`,
  `generated_at 2026-09-04T06:40:26Z`.
- **API run log:** same directory, `api_legs_run.log`. Grepped for `Reviewer call FAILED` →
  **0 hits**; no leg was recorded from a failed call.
- **Venue standard applied by every leg:** Physical Review D, regular article.

## Filing convention (matches R1 and R2)

The two direct-API raws are written by the review engine at the top of
`project-context/peer-reviews/` and **stay there** (identical to
`ROUND_2026-09-02-…-R1_A3M_*` and `ROUND_2026-09-02-…-R2VERIFY_A3M_*`); the
per-round directory under `INT_v3/` holds the Claude/Fable leg, the API run
log, the preflight receipt, and the truth audit. The Fable leg was therefore
moved from `INT_v3/A3M_v3M.0.8_R3_claude_fable_2026-09-04.md` to
`INT_v3/ROUND_2026-09-04-…-R3/A3M_fable_r3_leg.md` (git mv) to match
`A3M_fable_r1_leg.md` / `A3M_fable_r2_leg.md`.

## Leg census (Rule 4 — every attempted leg reported; absent legs never recorded as clean)

| Leg | Model | Verdict word **read from the raw** | Tagged findings in the raw | Raw path (sha256 of the raw file) |
|---|---|---|---|---|
| Claude Fable INT | `claude-fable-5-1` (Opus-tier referee subagent, directive N) | **major-revisions** | **4 MAJOR / 15 minor** (+6 questions to authors, +1 integrity note) | `INT_v3/ROUND_2026-09-04-…-R3/A3M_fable_r3_leg.md` (`f0fc4556…2746f`) |
| Grok API | `grok-4.3` (`Grok_brutal`, native PDF rasterized 150 DPI + pass-2 NO_NEW; 71.8 s) | **REJECT** | **4 ESSENTIAL / 3 MAJOR / 1 MINOR / 2 NIT = 10** | `ROUND_2026-09-04-A3M-v3M.0.8-EXACTPDF-8cf429e0-R3_A3M_Grok_brutal.md` (`2e992d6b…ab48`) |
| Gemini API | `gemini-3.1-pro-preview` (`Gemini_cosmology`, native PDF; 786.7 s) | **MAJOR REVISIONS** | **4 ESSENTIAL / 1 NIT = 5** | `ROUND_2026-09-04-A3M-v3M.0.8-EXACTPDF-8cf429e0-R3_A3M_Gemini_cosmology.md` (`5bfdab9c…c286`) |
| OpenAI / ChatGPT | — | **ABSENT** — paused under directive N (never faked, never back-filled) | — | — |
| Perplexity | — | **ABSENT** — optional leg, not run (recorded absent, never as clean) | — | — |

**BLOCKERs: 0** (explicit, all three legs).

### Leg caveat recorded (non-fatal)

`api_legs_run.log:254` —
`[Gemini_cosmology] pass-2 self-critique failed (non-fatal): DeadlineExceeded('Stream removed (Deadline Exceeded)')`.
The Gemini **pass-1 report is complete** (full ESSENTIAL/NIT list + summary
recommendation, present verbatim in the raw); only the pass-2 self-critique
(the NO_NEW de-duplication pass that Grok completed) timed out. Consequence:
Gemini's finding list was **not** self-pruned for redundancy, so its raw may
carry items a completed pass-2 would have merged. This is recorded here, is
not treated as a failure of the leg, and does **not** change any verdict word
or any classification in the truth audit (each Gemini finding is dispositioned
on its own merits below).

## Verdict-word summary (diagnostic only, never a gate — directive P)

`major-revisions` · `REJECT` · `MAJOR REVISIONS`. Verdict words are recorded as
feedback; convergence is decided by the truth audit's genuinely-new-real count,
not by these words.

## Round justification (directive R2 convergence budget)

R2 (2026-09-02) declared the 2-round budget consumed and rounds stopped at
v3M.0.5. Between v3M.0.5 and v3M.0.8 the paper absorbed **three new science
closures** (the method-independent super-Hubble cross-check §II D, the computed
bounce cubic term §III A, and the lab-own-spectrum PBH null §V C — see
`project-context/SSOT/paper-a3m/status.md` "v3M.0.8"). Per directive R2 a
science/scope decision intervened, so R3 reviews **new content**, not the
already-dispositioned content. The truth audit confirms this reading: all four
MAJORs land on material that did not exist at R2.

## Next artifact

Truth audit: `INT_v3/A3M_v3M.0.8_R3_TRUTH_AUDIT_2026-09-04.md`.
Canonical dispositions: `project-context/peer-reviews/DISPOSITIONS/A3M.md`.
