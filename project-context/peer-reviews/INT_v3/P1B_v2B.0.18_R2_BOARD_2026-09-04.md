# P1B v2B.0.18 R2 — REVIEW BOARD

**Round:** `ROUND_2026-09-04-P1B-v2B.0.18-EXACTPDF-354d63b2-R2VERIFY`
**Exact artefact:** `arxiv/paper1b_namaster_proof.pdf` == `site/public/papers/paper1b_namaster_proof_v2B.0.18.pdf`
sha256 `354d63b2e672ba4084987d993e59b73fd457a020a6bb794895c6e1d5074f88d2`, md5 `89cbca0f…`, 12 pp.
**Venue frame:** JORS-SOFTWARE (Grok, Gemini) / astro-software reproducibility, PRD-level rigour (Claude INT).

## Verdicts (read from raw text, not labels)

| Leg | Model | Verdict (verbatim summary line) | Findings |
|---|---|---|---|
| Grok API (`Grok_brutal`) | grok-4.3 | **REJECT** | 8 — E1,E2,E3 (essential) · M1,M2,M3 (major) · N1,N2 (nits) |
| Gemini API (`Gemini_cosmology`) | gemini-3.1-pro-preview | **MINOR REVISIONS** | 5 — E1,E2 (essential) · M1 (major) · M2 (minor) · N1 (nit) |
| Claude INT Opus (`INT_v3`) | Opus (exact-PDF bound) | **major-revisions** | 23 — 7 MAJOR (M1–M7) · 11 minor (m1–m11) · 5 questions (Q1–Q5) |

Total raw findings across legs: **36** (+5 questions counted inside the Opus 23).

## Receipts / integrity

- Preflight receipt: `INT_v3/ROUND_.../preflight_receipt.json` — generic rule receipt, 9 rules, **0 findings**;
  `paper1b_namaster_proof.tex` sha256 `1a5d7741…`.
- API leg log: `INT_v3/ROUND_.../api_legs_run.log`. **No `Reviewer call FAILED` strings** in either raw.
- Both API raws record the same PDF sha256 as the INT leg and both ran a pass-2 `NO_NEW` confirmation.
- The Opus leg independently verified the pre-registration: rules commit `4451b135` (19:01:41)
  → seal `28efa21c` (19:04:15, contains **no run output**) → outputs `27300504` → reveal `974e2859`;
  it re-derived the sealed assignment from the revealed key and reproduced the committed digest
  `c96b5bf1…` byte-for-byte, and matched `verify.py` sha256 `6a9acd70…`. **The seal holds.**

## Verdict-word note

Grok's REJECT rests principally on venue fit (JORS scope/adoption, §E3) and on the
threat-model/design-limitation framing; Gemini's MINOR REVISIONS and Opus's
major-revisions agree on the same two substantive defects (the mislabelled interval and
the abstract's statistical/estimator over-statement). Verdict words are diagnostic
(directive P); the canonical audit below is the operative record.

**Truth audit:** `P1B_v2B.0.18_R2_TRUTH_AUDIT_2026-09-04.md`.
