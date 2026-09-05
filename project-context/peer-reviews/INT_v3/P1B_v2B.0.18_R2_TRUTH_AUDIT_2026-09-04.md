# P1B v2B.0.18 R2 — TRUTH AUDIT (skeptical, verdict-first)

**Exact artefact:** `arxiv/paper1b_namaster_proof.pdf` == `site/public/papers/paper1b_namaster_proof_v2B.0.18.pdf`
sha256 `354d63b2e672ba4084987d993e59b73fd457a020a6bb794895c6e1d5074f88d2`, md5 `89cbca0f…`, 12 pp.
**Round:** `ROUND_2026-09-04-P1B-v2B.0.18-EXACTPDF-354d63b2-R2VERIFY`
**Receipt:** `INT_v3/ROUND_2026-09-04-P1B-v2B.0.18-EXACTPDF-354d63b2-R2VERIFY/preflight_receipt.json`
(generic rule receipt: 9 rules, 0 findings). No `Reviewer call FAILED` strings in either raw.
**Board:** `P1B_v2B.0.18_R2_BOARD_2026-09-04.md`
**Prior ledger:** `DISPOSITIONS/P1B.md` (R1 canonical C1–C23)

## Plan (executed in the sections below)

1. Board built from raws (verdicts read from raw text, not labels).
2. Fingerprint every finding from all three legs; classify (a) genuinely-new REAL,
   (b) re-flag w/ disposition id, (c) FALSIFIED w/ source, (d) OPINION/genre/venue,
   (e) OUT-OF-SCOPE disclosed.
3. Verify the statistics claims directly against `pipelines/namaster_proof/blind_test/`
   (batch-2 scorecard, `RULES_v2_FROZEN.md`, `verify.py`, `variants2.py`, `windows` module).
4. Canonical list with class + citation + closure action; per-leg counts.
5. CLOSURE PLAN: (i) editorial edits for v2B.0.19, (ii) science items.
6. R2 statement + `DISPOSITIONS/P1B.md` update.

*(sections filled in below; committed section-by-section)*
