# EXT Review Round — 2026-07-05 (verifiable, de-biased)

18/18 legs captured. Each leg: fresh chat, PDF upload, exact PRD-referee prompt,
raw verbatim response saved to `<PAPER>_<reviewer>.md` + `.png` screenshot,
verdict recorded in `manifest.jsonl` (verbatim from the "(1) VERDICT:" line).

## Verdict matrix (from raw responses)

| Paper | Version    | ChatGPT | Grok             | Gemini           |
|-------|------------|---------|------------------|------------------|
| P2    | v1.7.92    | REJECT  | MAJOR REVISIONS  | MAJOR REVISIONS  |
| P1A   | v1A.0.107  | REJECT  | MAJOR REVISIONS  | MAJOR REVISIONS  |
| P3    | v3.1.137   | REJECT  | MAJOR REVISIONS  | MAJOR REVISIONS  |
| P1B   | v1B.0.99   | REJECT  | MAJOR REVISIONS  | MAJOR REVISIONS  |
| P4    | v1.0.212   | REJECT  | MINOR REVISIONS  | MINOR REVISIONS  |
| P5    | v0.1.101   | REJECT  | MINOR REVISIONS  | MAJOR REVISIONS  |

FAILED legs: none.

## Reviewer models
- ChatGPT: Pro Extended (Pro thinking)
- Grok: Expert
- Gemini: 3 Pro (Ultra, houston@bamf.com /u/1/)

## Movement vs RS24 baseline (P1A REJECT / P2 MAJOR / P3 REJECT-ish)
- P2: ChatGPT REJECT, Grok+Gemini MAJOR. Grok/Gemini accept the −35/16
  factor-of-2 fix (Gemini only asks to soften "derived"→"scaling-limit"
  language); ChatGPT alone calls the −35/16 arithmetic internally
  inconsistent (single dissent → truth-audit target). No move to ACCEPT;
  P2 now firmly at the LLM-referee MAJOR floor rather than REJECT.
- P1A: ChatGPT REJECT, Grok+Gemini MAJOR. Both moderate referees flag the
  same two things: (a) "single-scale NDA no-go" reads as trivial dimensional
  analysis dressed as a structural theorem (Gemini explicit), (b) ansatz- vs
  derived-coefficient framing for Routes 2/3. Improved from prior REJECT/REJECT
  toward the MAJOR floor.
- P3: ChatGPT REJECT, Grok+Gemini MAJOR — off the double-REJECT; detection-
  significance upgrade did not flip a moderate referee to ACCEPT.
- P4: Grok+Gemini MINOR, ChatGPT REJECT — the two calibrated referees are at
  MINOR (closest to the recalibrated Grok+Gemini ACCEPT gate); ChatGPT REJECT
  is the known structural harsh-referee floor (directive H).
- P5: Grok MINOR, Gemini MAJOR, ChatGPT REJECT — split; Gemini majors are the
  gating items for P5.

## Pattern (consistent with directive H)
ChatGPT returned REJECT on all 6 papers — including published-quality P4 —
confirming the maximally-harsh-referee structural floor: it flags REJECT-level
issues on any real manuscript. Grok/Gemini track paper quality (MINOR for the
strong P4; MAJOR for the harder theory papers). The calibrated Grok+Gemini
signal is the operative gate.
