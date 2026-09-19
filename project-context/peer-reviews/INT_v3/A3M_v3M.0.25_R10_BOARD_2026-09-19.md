# A3M R10 CONFIRMATION board — exact v3M.0.25

**Round:** `ROUND_2026-09-18-A3M-v3M.0.25-EXACTPDF-c5fe8889-R10CONFIRM`
**Artifact:** `research/track_a3_multichannel/paper/main.pdf`
sha256 `c5fe8889766be7f408b5e385f2826af85182ea50b00d4b8142f4db46422ca001`,
md5 `d46166cb88b32009cdc6be59bb620547`, 20 pp — byte-identical at
`site/public/papers/a3_multichannel_arxiv_v3M.0.25.pdf` and `public/papers/…v3M.0.25.pdf`,
and matching the Convex `paperVersions:current` row, before dispatch.
**Preflight:** `ROUND_…-R10CONFIRM/preflight_receipt.json` — PASS, 0 findings.
**Mode:** INT only (Directive N + Portfolio Decision 2026-09-02 #6). No Codex, no OpenAI API,
no browser EXT.
**Authority:** the one confirmation board directive R2 permits, because R9 closed real items.

## Leg status

| Leg | Model | Status | Verdict | Raw |
|---|---|---|---|---|
| Grok_brutal | `grok-4.3` | inherited from lane L1 | **REJECT** | `../ROUND_…-R10CONFIRM_A3M_Grok_brutal.md` |
| Gemini_cosmology | `gemini-3.1-pro-preview` | **no raw on disk → FAILED → RE-RUN** (126.5 s) | **MAJOR REVISIONS** | `../ROUND_…-R10CONFIRM_A3M_Gemini_cosmology.md` |
| Claude Fable 5.1 INT referee | `fable` sub-agent, verdict-blind cold read | **no raw on disk → FAILED → RE-RUN** (~22 min) | **MAJOR REVISIONS** (0E / 4M / 9m / 5n / 6 VR) | `A3M_v3M.0.25_R10_claude_fable_2026-09-19.md` |

No verdict in this board was recorded from a label: the two missing legs were re-run on the
same exact PDF and their raws were written and read before any verdict was entered.

## Outcome — the confirmation board did not confirm

| class | count |
|---|---|
| GENUINELY-NEW-REAL (closed in v3M.0.26) | **17** — 4 MAJOR, 1 MAJOR-lite, 12 minor/nit |
| FALSIFIED (source-cited) | 15 |
| RE-FLAG-OF-DISCLOSED | 5 |
| OPINION/GENRE | 4 |
| Carried (D-round / proof stage) | 2 |
| Open packaging actions | 2 — frozen DOI, push gate |
| Clean-wave count | **0** |

The four MAJORs: Table V's `f_PBH` columns were not evaluated at their rows' own labels; the
§VIII DBI window minimum used an unstated criterion on a single background (corrected **against**
the paper, `r_min` 12.6 → 10.3); p. 8 and p. 13 gave the same tensor amplitude incompatible
shortfalls; and two reproducibility citations resolve to nothing. **No physics error was found.**

Full per-finding audit with source citations: `A3M_v3M.0.25_R10_TRUTH_AUDIT_2026-09-19.md`.
Canonical dispositions: `../DISPOSITIONS/A3M.md` § "R10 CONFIRM".

## Directive R2

R9 + R10 = the full convergence budget. **Rounds STOP.** No further board on A3M without an
intervening science or scope decision (the director's call). Readiness stays **COMPUTED** at
cap 75; **no cap-95 recommendation is made** — the automated-review-convergence gate of
directive P is not met and packaging is incomplete.
