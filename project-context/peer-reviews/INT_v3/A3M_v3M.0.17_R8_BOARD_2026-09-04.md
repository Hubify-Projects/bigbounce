# A3M v3M.0.17 — R8 verdict board (2026-09-04)

**Exact artifact:** `research/track_a3_multichannel/paper/main.pdf`
sha256 `5ada01728d4eb2eb…`, md5 `b18aafd1288ffddeea2c3a1ee074a23b`, 18 pp.
Served copy `site/public/papers/a3_multichannel_arxiv_v3M.0.17.pdf` — md5 identical (verified).
Receipt dir: `ROUND_2026-09-04-A3M-v3M.0.17-EXACTPDF-5ada0172-R8VERIFY/`.

| leg | model | verdict (raw text) | raw findings | raw path |
|---|---|---|---|---|
| Grok_brutal | grok-4.3 | **REJECT** | 14 (4 E / 4 M / 3 m / 3 nit) | `../ROUND_2026-09-04-A3M-v3M.0.17-EXACTPDF-5ada0172-R8VERIFY_A3M_Grok_brutal.md` |
| Gemini_cosmology | gemini-3.1-pro-preview | **MAJOR REVISIONS** | 6 (3 E / 2 M / 1 N) | `../ROUND_2026-09-04-A3M-v3M.0.17-EXACTPDF-5ada0172-R8VERIFY_A3M_Gemini_cosmology.md` |
| Claude Fable 5.1 (INT) | fable-5.1 | **MAJOR REVISIONS** | 20 (4 M / 12 minor / 4 Q) | `A3M_v3M.0.17_R8_claude_fable_2026-09-04.md` |

**Leg health:** `grep -l "Reviewer call FAILED"` over both API raws returns nothing; both raws
carry a wall time, a review-packet hash and a rendered-PDF confirmation. The Fable leg is
complete (Summary → Independent verification → Verdict → MAJOR → Minor → Questions →
Integrity note) and was written with no prior review history, SSOT or dispositions consulted.
No leg is FAILED. Verdict words above are transcribed from each raw's own recommendation line.

Truth-audit: `A3M_v3M.0.17_R8_TRUTH_AUDIT_2026-09-04.md`.
